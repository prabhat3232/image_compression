import json
import smtplib
import ssl
import urllib.error
import urllib.request

from content.config import (
    CONTACT_EMAIL,
    CONTACT_WEBHOOK_URL,
    GMAIL_APP_PASSWORD,
    GMAIL_USER,
)

SMTP_TIMEOUT = 12


def smtp_configured():
    """True when direct Gmail SMTP credentials are present."""
    return bool(GMAIL_USER and GMAIL_APP_PASSWORD)


def contact_delivery_configured():
    """True when any outbound contact delivery method is configured."""
    return smtp_configured() or bool(CONTACT_WEBHOOK_URL)


def _send_via_smtp(name, sender_email, subject, message, recipient, body):
    msg = _build_message(recipient, sender_email, subject, body)
    errors = []

    for label, send_fn in (
        ("Gmail SMTP (port 465)", _smtp_ssl),
        ("Gmail SMTP (port 587)", _smtp_starttls),
    ):
        try:
            send_fn(msg, recipient)
            return True, None
        except Exception as exc:
            errors.append(f"{label}: {exc}")

    return False, errors[-1] if errors else "SMTP failed"


def _build_message(recipient, sender_email, subject, body):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart()
    msg["From"] = GMAIL_USER
    msg["To"] = recipient
    msg["Reply-To"] = sender_email
    msg["Subject"] = f"[FileShrinkr Contact] {subject}"
    msg.attach(MIMEText(body, "plain", "utf-8"))
    return msg


def _smtp_ssl(msg, recipient):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=SMTP_TIMEOUT, context=context) as server:
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_USER, [recipient], msg.as_string())


def _smtp_starttls(msg, recipient):
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=SMTP_TIMEOUT) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_USER, [recipient], msg.as_string())


def _send_via_webhook(name, sender_email, subject, message):
    payload = json.dumps(
        {
            "name": name,
            "email": sender_email,
            "subject": subject,
            "message": message,
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        CONTACT_WEBHOOK_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Webhook HTTP {exc.code}: {detail[:200]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Webhook unreachable: {exc.reason}") from exc

    try:
        data = json.loads(raw)
        if data.get("ok") is False:
            raise RuntimeError(data.get("error") or "Webhook rejected the message")
    except json.JSONDecodeError:
        pass
    return True


def send_contact_email(name, sender_email, subject, message):
    if not contact_delivery_configured():
        return False, "Email service is not configured."

    recipient = CONTACT_EMAIL or GMAIL_USER
    body = (
        f"New contact form submission from FileShrinkr\n\n"
        f"Name: {name}\n"
        f"Email: {sender_email}\n"
        f"Subject: {subject}\n\n"
        f"Message:\n{message}\n"
    )

    errors = []

    if CONTACT_WEBHOOK_URL:
        try:
            _send_via_webhook(name, sender_email, subject, message)
            return True, None
        except Exception as exc:
            errors.append(str(exc))

    if smtp_configured():
        ok, err = _send_via_smtp(name, sender_email, subject, message, recipient, body)
        if ok:
            return True, None
        errors.append(err)

    if errors:
        last = errors[-1]
        if "timed out" in last.lower() or "unreachable" in last.lower():
            return (
                False,
                "Could not reach the mail server (SMTP may be blocked on this network). "
                "Set CONTACT_WEBHOOK_URL in .env using the Google Apps Script in temp/contact-email-apps-script.js",
            )
        return False, last

    return False, "Email service is not configured."
