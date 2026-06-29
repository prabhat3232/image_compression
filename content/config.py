import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

SITE_URL = os.environ.get("SITE_URL", "https://fileshrinkr.com").rstrip("/")
SITE_NAME = "FileShrinkr"
PUBLISHER = "DSnM Solutions"
CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL", "xspace.dummy@gmail.com")
GMAIL_USER = os.environ.get("GMAIL_USER", "")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "")
# HTTPS fallback when SMTP ports 465/587 are blocked (ISP/hosting firewall)
CONTACT_WEBHOOK_URL = os.environ.get("CONTACT_WEBHOOK_URL", "").strip()

TRUST_SLUGS = ["about", "privacy", "terms", "contact"]

# Former tool/landing URLs → homepage with presets (301 redirects)
REMOVED_PAGE_REDIRECTS = {
    "tools": "/",
    "compress-jpg": "/?format=jpg&quality=75",
    "compress-png": "/?format=jpg&quality=80",
    "compress-webp": "/?format=webp&quality=80",
    "images-to-pdf": "/?format=pdf",
    "compress-for-email": "/?format=jpg&quality=70",
    "compress-for-whatsapp": "/?format=jpg&quality=65",
    "compress-for-website": "/?format=webp&quality=80",
    "resize-image": "/?tab=editor",
    "jpg-vs-webp": "/",
    "how-to-reduce-image-size": "/",
    "resize-for-instagram": "/?format=jpg&quality=80&strip_exif=1&resize_preset=instagram_square",
    "remove-image-metadata": "/?format=jpg&quality=85&strip_exif=1",
}

GUIDE_SLUGS = [
    "resize-photos-for-government-exam-forms",
    "compress-without-losing-quality",
    "best-image-format-for-websites",
    "merge-images-into-pdf",
    "prepare-images-for-email",
    "image-dpi-and-resolution",
]

GLOSSARY_SLUGS = [
    "lossy-compression",
    "lossless-compression",
    "exif-metadata",
    "dpi-resolution",
    "aspect-ratio",
    "webp-format",
    "svg-rasterization",
    "color-space",
]


def all_sitemap_paths():
    paths = ["/"]
    paths += [f"/{s}" for s in TRUST_SLUGS]
    paths += ["/guides"] + [f"/guides/{s}" for s in GUIDE_SLUGS]
    paths += ["/glossary"] + [f"/glossary/{s}" for s in GLOSSARY_SLUGS]
    return paths
