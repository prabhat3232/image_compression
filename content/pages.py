"""SEO helpers and trust page metadata."""

from content.config import CONTACT_EMAIL, PUBLISHER, SITE_NAME, SITE_URL


def canonical(path):
    if not path or path == "/":
        return f"{SITE_URL}/"
    return f"{SITE_URL}{path if path.startswith('/') else '/' + path}"


TRUST_PAGES = {
    "about": {
        "title": "About FileShrinkr",
        "description": "Learn about FileShrinkr — free online image compression with HEIC, AVIF, PNG, browser-private mode, target KB sizes, PDF merge, and in-browser editing by DSnM Solutions.",
        "h1": "About FileShrinkr",
    },
    "privacy": {
        "title": "Privacy Policy",
        "description": "How FileShrinkr handles uploaded images, cookies, Google Analytics, AdSense, and contact form data.",
        "h1": "Privacy Policy",
    },
    "terms": {
        "title": "Terms of Use",
        "description": "Terms and conditions for using FileShrinkr image compression and editing tools.",
        "h1": "Terms of Use",
    },
    "contact": {
        "title": "Contact Us",
        "description": "Get in touch with the FileShrinkr team. We typically respond within 24–48 hours.",
        "h1": "Contact FileShrinkr",
    },
}
