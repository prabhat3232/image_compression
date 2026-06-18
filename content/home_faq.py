"""Homepage FAQ — 20+ items for SEO and AdSense depth."""

HOME_FAQS = [
    {"q": "What is FileShrinkr?", "a": "FileShrinkr is a free online tool to compress images, export PDFs, and edit photos in your browser. No account is required."},
    {"q": "Which image formats can I upload?", "a": "You can upload JPG, PNG, WEBP, and SVG files. Output formats include JPG, WEBP, and PDF."},
    {"q": "Is FileShrinkr free?", "a": "Yes. Compression and editing are free with no signup or subscription."},
    {"q": "How does compression work?", "a": "Images are processed on our server using FFmpeg and Pillow. You choose quality from 1 to 100 and pick an output format."},
    {"q": "Are my files stored permanently?", "a": "Uploads are used for processing in a temporary batch folder. Do not upload sensitive documents you cannot risk exposing to a web service."},
    {"q": "Can I compress multiple images at once?", "a": "Yes. Upload several files and download a ZIP archive containing all compressed results."},
    {"q": "How do I merge images into one PDF?", "a": "Select PDF as the output format and enable Merge all images into one PDF before compressing."},
    {"q": "What is the lossless PDF option?", "a": "When compress images in PDF is unchecked, we embed originals with img2pdf to avoid re-encoding quality loss."},
    {"q": "Does the image editor run locally?", "a": "Yes. Crop, resize, rotate, and flip use HTML5 Canvas in your browser. Only compression uses the server."},
    {"q": "What quality setting should I use?", "a": "Start at 75 for a balance of size and clarity. Email attachments often work at 70; web heroes may use 80–85."},
    {"q": "Can I use FileShrinkr on mobile?", "a": "The site works on modern mobile browsers. Large batches may be slower on limited connections."},
    {"q": "Why is my download delayed?", "a": "We add a short filesystem sync delay so browsers reliably start downloads, especially in Chrome."},
    {"q": "Does FileShrinkr remove EXIF metadata?", "a": "You can enable Remove EXIF on supported flows to strip camera and GPS metadata during compression."},
    {"q": "Can I resize for Instagram?", "a": "Use our Resize for Instagram page for 1080×1080 presets, or the editor tab for custom dimensions."},
    {"q": "Is WEBP better than JPG?", "a": "WEBP often produces smaller files at similar quality. JPG remains more compatible with older email clients."},
    {"q": "Do you sell my data?", "a": "No. We do not sell personal information. See our Privacy Policy for analytics and advertising disclosures."},
    {"q": "How do I contact support?", "a": "Use the Contact page or email us. We aim to respond within 24–48 hours."},
    {"q": "Can I use compressed images commercially?", "a": "You retain rights to your images. You are responsible for complying with licenses and applicable laws."},
    {"q": "What if compression fails?", "a": "Try a different format, lower file size, or ensure the file is a valid image. Corrupt files may be rejected."},
    {"q": "Does FileShrinkr work offline?", "a": "The editor can work on loaded images offline, but compression requires an internet connection to our server."},
    {"q": "Who operates FileShrinkr?", "a": "FileShrinkr is published by DSnM Solutions. Learn more on our About page."},
]

POPULAR_TOOLS = [
    {"title": "Compress JPG", "url": "/compress-jpg", "desc": "Shrink JPEG photos for email and web."},
    {"title": "Compress WEBP", "url": "/compress-webp", "desc": "Modern format for faster websites."},
    {"title": "Images to PDF", "url": "/images-to-pdf", "desc": "Convert or merge into one PDF."},
    {"title": "Compress for Email", "url": "/compress-for-email", "desc": "Fit attachment size limits."},
    {"title": "Resize Image", "url": "/resize-image", "desc": "Dimensions guide + editor."},
    {"title": "Instagram Resize", "url": "/resize-for-instagram", "desc": "1080×1080 preset."},
    {"title": "Remove EXIF", "url": "/remove-image-metadata", "desc": "Strip metadata for privacy."},
    {"title": "JPG vs WEBP", "url": "/jpg-vs-webp", "desc": "Choose the right format."},
]
