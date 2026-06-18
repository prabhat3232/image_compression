# FileShrinkr — Production deploy checklist

## 1. Server setup

```bash
git pull origin main
cp .env.example .env   # then edit .env
docker compose build
docker compose up -d
```

## 2. Required `.env` on server

| Variable | Required | Notes |
|----------|----------|-------|
| `SITE_URL` | Yes | `https://fileshrinkr.com` |
| `FLASK_SECRET_KEY` | Yes | Random string |
| `CONTACT_WEBHOOK_URL` | Yes | Google Apps Script Web app URL |
| `CONTACT_EMAIL` | Yes | Public inbox |
| `GMAIL_USER` / `GMAIL_APP_PASSWORD` | Optional | SMTP often blocked; webhook is primary |

See `temp/contact-email-apps-script.js` for webhook setup.

## 3. Verify after deploy

- https://fileshrinkr.com/ — homepage + compressor
- https://fileshrinkr.com/sitemap.xml — **32 URLs**
- https://fileshrinkr.com/robots.txt
- https://fileshrinkr.com/ads.txt
- https://fileshrinkr.com/contact — submit test message
- Sample landings: `/compress-jpg`, `/guides`, `/glossary`

## 4. Google Search Console

1. Property: `fileshrinkr.com`
2. **Sitemaps** → submit `https://fileshrinkr.com/sitemap.xml`
3. **URL inspection** → request indexing for `/`, `/compress-jpg`, `/about`
4. **Rich results** → test FAQ on homepage and `/compress-jpg`

## 5. AdSense (after 2–4 weeks indexing)

Follow `brain/ADSENSE_REAPPLY.md`.

Target: **30+ indexed pages** before reapplying.

## 6. Regenerate static sitemap (optional)

Flask serves dynamic sitemap at runtime. To refresh the committed `sitemap.xml` backup:

```bash
python temp/gen_sitemap.py
```
