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

LANDING_SLUGS = [
    "compress-jpg",
    "compress-png",
    "compress-webp",
    "images-to-pdf",
    "compress-for-email",
    "compress-for-whatsapp",
    "compress-for-website",
    "resize-image",
    "jpg-vs-webp",
    "how-to-reduce-image-size",
]

GUIDE_SLUGS = [
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

PHASE3_SLUGS = [
    "resize-for-instagram",
    "remove-image-metadata",
]


def all_sitemap_paths():
    paths = ["/"]
    paths += [f"/{s}" for s in TRUST_SLUGS]
    paths += [f"/{s}" for s in LANDING_SLUGS]
    paths += ["/guides"] + [f"/guides/{s}" for s in GUIDE_SLUGS]
    paths += ["/glossary"] + [f"/glossary/{s}" for s in GLOSSARY_SLUGS]
    paths += [f"/{s}" for s in PHASE3_SLUGS]
    return paths
