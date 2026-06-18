"""SEO helpers and trust page metadata."""

import json

from content.config import CONTACT_EMAIL, PUBLISHER, SITE_NAME, SITE_URL


def canonical(path):
    if not path or path == "/":
        return f"{SITE_URL}/"
    return f"{SITE_URL}{path if path.startswith('/') else '/' + path}"


def faq_schema(faqs, page_url):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {"@type": "Answer", "text": item["a"]},
            }
            for item in faqs
        ],
    }


def howto_schema(name, description, steps, page_url):
    return {
        "@type": "HowTo",
        "name": name,
        "description": description,
        "step": [
            {
                "@type": "HowToStep",
                "position": i + 1,
                "name": s["name"],
                "text": s["text"],
            }
            for i, s in enumerate(steps)
        ],
    }


def build_schema_graph(page_url, faqs=None, howto=None):
    graph = [
        {
            "@type": "WebPage",
            "@id": f"{page_url}#webpage",
            "url": page_url,
            "name": SITE_NAME,
            "isPartOf": {"@id": f"{SITE_URL}/#website"},
        }
    ]
    if howto:
        graph.append(howto_schema(howto["name"], howto["description"], howto["steps"], page_url))
    if faqs:
        graph.append(faq_schema(faqs, page_url))
    return json.dumps({"@context": "https://schema.org", "@graph": graph})


TRUST_PAGES = {
    "about": {
        "title": "About FileShrinkr",
        "description": "Learn about FileShrinkr, a free online image compressor and editor built by DSnM Solutions for batch JPG, WEBP, and PDF workflows.",
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

PHASE3_PAGES = {
    "resize-for-instagram": {
        "slug": "resize-for-instagram",
        "title": "Resize Images for Instagram — 1080×1080 Online",
        "description": "Resize and compress photos for Instagram posts, stories, and reels. Free square and portrait presets.",
        "h1": "Resize Images for Instagram",
        "preset_format": "jpg",
        "preset_quality": 80,
        "show_widget": True,
        "resize_preset": "instagram_square",
        "show_strip_exif": True,
        "related_slugs": ["resize-image", "compress-jpg", "compress-for-website"],
        "faqs": [
            {"q": "What size should Instagram photos be?", "a": "Square feed posts work well at 1080×1080 pixels. FileShrinkr's Instagram preset scales your image to that size before compression."},
            {"q": "Will resizing reduce quality?", "a": "Scaling down from very large originals usually looks sharp on mobile. We compress after resize to keep file size manageable."},
        ],
        "howto_steps": [
            {"name": "Upload your photo", "text": "Choose a JPG or PNG from your phone or camera."},
            {"name": "Use Instagram preset", "text": "The resize preset applies 1080×1080 dimensions automatically."},
            {"name": "Download", "text": "Save the optimized JPG ready to upload to Instagram."},
        ],
        "sections": [
            {
                "heading": "Why Instagram dimensions matter",
                "paragraphs": [
                    "Instagram displays feed images in a square or portrait crop depending on how users scroll. Uploading a massive twelve-megapixel file does not improve what followers see—it only slows your upload and may trigger compression on Instagram's servers that you cannot control.",
                    "Preparing images at 1080 pixels on the long edge matches Instagram's recommended feed resolution. You keep control over sharpness and compression before the platform touches your work.",
                    "FileShrinkr combines resize and JPG compression in one step so creators can batch-prepare content without opening desktop editors.",
                ],
            },
            {
                "heading": "Square posts vs stories",
                "paragraphs": [
                    "Classic feed posts often use a 1:1 aspect ratio. Stories and reels use taller 9:16 frames. Starting from a well-lit, centered composition makes cropping easier.",
                    "If your source image is landscape, consider using FileShrinkr's editor tab to crop before applying the Instagram resize preset.",
                    "Consistent dimensions across a grid help brand accounts look professional and load quickly for mobile followers.",
                ],
            },
        ],
    },
    "remove-image-metadata": {
        "slug": "remove-image-metadata",
        "title": "Remove EXIF Metadata from Images Online",
        "description": "Strip GPS, camera, and device EXIF data from JPG and PNG photos while compressing. Protect privacy before sharing online.",
        "h1": "Remove Image Metadata (EXIF)",
        "preset_format": "jpg",
        "preset_quality": 85,
        "show_widget": True,
        "show_strip_exif": True,
        "related_slugs": ["compress-jpg", "compress-png", "privacy"],
        "faqs": [
            {"q": "What is EXIF metadata?", "a": "EXIF stores camera settings, timestamps, and sometimes GPS coordinates embedded in photo files."},
            {"q": "Why remove EXIF before posting?", "a": "Sharing photos online can unintentionally reveal location or device details. Stripping EXIF reduces privacy risk."},
        ],
        "howto_steps": [
            {"name": "Upload images", "text": "Select photos that may contain location or device metadata."},
            {"name": "Enable Remove EXIF", "text": "Keep the metadata removal option checked (on by default on this page)."},
            {"name": "Download clean files", "text": "Save compressed images without embedded EXIF tags."},
        ],
        "sections": [
            {
                "heading": "What metadata hides in your photos",
                "paragraphs": [
                    "Digital cameras and smartphones write EXIF records into JPEG files: lens model, exposure time, software version, and sometimes precise GPS coordinates. Social networks may strip some fields, but not always before processing copies.",
                    "Journalists, parents, and remote workers often prefer to share images without location breadcrumbs. Removing metadata is a simple hygiene step before publishing.",
                    "FileShrinkr can strip EXIF during compression so you do not need a separate metadata tool.",
                ],
            },
            {
                "heading": "Compression plus privacy",
                "paragraphs": [
                    "Metadata removal slightly reduces file size and removes identifying tags. Combined with sensible JPG quality, you get share-ready images that are smaller and safer.",
                    "For archival originals, keep an unmodified master copy offline. Use FileShrinkr for distribution copies intended for web, email, or social media.",
                ],
            },
        ],
    },
}
