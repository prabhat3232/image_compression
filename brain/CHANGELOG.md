# FileShrinkr Changelog

## v0.2.1 — 2026-06-17 — Contact form + deploy prep

- Contact form: Google Apps Script webhook (`CONTACT_WEBHOOK_URL`) when SMTP blocked
- `mail.py`: webhook-first delivery, SMTP 465/587 fallback
- Homepage: Remove EXIF checkbox, compression size stats display
- Dynamic sitemap: `lastmod`, 32 URLs; static `sitemap.xml` synced
- `brain/DEPLOY.md` production checklist

## v0.2.0 — 2026-06-02 — AdSense content expansion (Phase 1–3)

- Wired Flask routes: trust pages, 10 SEO landings, Phase 3 tools, guides, glossary
- Dynamic `sitemap.xml` and `llms.txt` from `content/config.py`
- Homepage: nav, 21 FAQs, popular tools grid, latest guides, expanded footer
- `/compress` API: `strip_exif`, `resize_preset` (Instagram 1080×1080), size stats in JSON
- Contact form with Gmail SMTP via `.env` (`GMAIL_USER`, `GMAIL_APP_PASSWORD`)
- Added `.env.example`, `.gitignore` for `.env`, docker-compose `env_file`
- See `brain/ADSENSE_REAPPLY.md` for Phase 4 checklist
