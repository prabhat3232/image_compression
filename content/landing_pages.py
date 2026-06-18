"""SEO landing page content for FileShrinkr."""

LANDING_PAGES = {
    "compress-jpg": {
        "slug": "compress-jpg",
        "title": "Compress JPG Online — Reduce JPEG File Size Free | FileShrinkr",
        "description": "Compress JPG and JPEG images online without installing software. FileShrinkr reduces photo file size while keeping visual quality for email, web, and storage.",
        "h1": "Compress JPG Images Online",
        "preset_format": "jpg",
        "preset_quality": 75,
        "show_widget": True,
        "related_slugs": ["compress-png", "compress-webp", "how-to-reduce-image-size"],
        "faqs": [
            {
                "q": "What is the best JPG quality setting for compression?",
                "a": "For most photos, a quality setting between 70 and 85 gives an excellent balance. FileShrinkr defaults to 75, which typically cuts file size by 40–70% with little visible difference on screens.",
            },
            {
                "q": "Will compressing a JPG reduce image quality?",
                "a": "JPG uses lossy compression, so some data is discarded. At sensible quality levels the change is rarely noticeable. Avoid re-saving the same JPG many times, since each pass adds more artifacts.",
            },
            {
                "q": "Can I compress multiple JPG files at once?",
                "a": "Yes. Upload several JPEG files in one batch and FileShrinkr returns a ZIP archive with every compressed image ready to download.",
            },
            {
                "q": "Does FileShrinkr remove EXIF metadata from JPG files?",
                "a": "You can strip EXIF data during compression, which removes camera settings, GPS tags, and other embedded metadata. That often saves a few extra kilobytes and improves privacy.",
            },
            {
                "q": "Is there a file size limit for JPG compression?",
                "a": "FileShrinkr is designed for everyday photo workflows. Very large RAW exports may take longer to process, but typical camera and phone JPEGs compress quickly in the browser-backed pipeline.",
            },
        ],
        "howto_steps": [
            {
                "name": "Upload your JPG files",
                "text": "Drag and drop JPEG images onto the compressor or click to browse. You can add multiple photos in a single session.",
            },
            {
                "name": "Set quality and format",
                "text": "Leave the format on JPG and adjust the quality slider. Lower values produce smaller files; higher values preserve more detail.",
            },
            {
                "name": "Download compressed images",
                "text": "Click Start Compression and save the results. Multiple files download as a ZIP; a single file downloads directly.",
            },
        ],
        "sections": [
            {
                "heading": "Why JPG files get uncomfortably large",
                "paragraphs": [
                    "JPEG is the most common photo format on the internet, yet many JPG files are far larger than they need to be. Modern cameras and phones save images at high resolution with conservative compression settings so prints and edits look good. When you only need to email a snapshot, publish a blog thumbnail, or attach a receipt, that extra data becomes dead weight.",
                    "Large JPGs slow down page loads, bounce email servers, and eat mobile data. A twelve-megapixel photo straight from a phone can easily exceed five megabytes even though a well-compressed version at screen resolution might be under three hundred kilobytes. The gap is not magic—it is simply a matter of choosing the right dimensions, quality level, and metadata handling.",
                    "FileShrinkr focuses on practical compression for real workflows. You do not need Photoshop actions or command-line tools. Upload your JPEGs, pick a quality target, and download leaner files in seconds. The tool runs on efficient FFmpeg and Pillow processing tuned for batch photo work.",
                ],
            },
            {
                "heading": "How JPG compression actually works",
                "paragraphs": [
                    "JPEG compression is lossy, meaning it permanently removes information the human eye is unlikely to notice. The algorithm converts image data into frequency components, quantizes the less important ones aggressively, and encodes the result. Higher quality settings keep more frequency detail; lower settings discard more and shrink the file.",
                    "Because JPG compression is tuned for continuous-tone photographs, it excels on landscapes, portraits, and product shots. It struggles with sharp text, flat color graphics, and screenshots with hard edges—those images often look better as PNG or WebP. Understanding this helps you pick the right format after compression.",
                    "Every time you open and re-save a JPG at a lower quality, artifacts compound. FileShrinkr lets you compress once from your original export, which preserves as much quality as possible for the target file size. Keep a master copy if you plan to edit again later.",
                ],
            },
            {
                "heading": "Choosing the right quality level",
                "paragraphs": [
                    "Quality is not a single universal number. A landscape with soft foliage can tolerate quality 65 and still look natural on a laptop screen. A portrait with fine skin texture might need 80 to avoid visible banding in shadows. FileShrinkr exposes a simple slider so you can experiment without guessing.",
                    "For email attachments, quality 70–75 usually keeps faces recognizable while staying under provider limits. For hero images on a website, 75–85 is a safe range when the displayed width is smaller than the native resolution. For archival sharing where bandwidth is cheap, 85–90 minimizes visible loss.",
                    "If you are unsure, start at 75 and download the result. Open the original and compressed versions side by side at one hundred percent zoom on a detail that matters—an eye, a logo edge, or small text. If you cannot see a difference at normal viewing distance, you have room to lower quality further.",
                ],
            },
            {
                "heading": "Batch compression for photographers and teams",
                "paragraphs": [
                    "Event photographers, real-estate agents, and e-commerce teams routinely export dozens of JPGs per session. Compressing them one by one in desktop software is tedious. FileShrinkr accepts multiple files, applies consistent settings, and packages the output in a ZIP when needed.",
                    "Consistent settings matter for brand galleries. When every product thumbnail uses the same quality and dimensions, your storefront feels cohesive and loads predictably. Set your preferred quality once per batch instead of fighting individual export dialogs.",
                    "Because processing happens server-side with FFmpeg, you get reliable results regardless of which browser or operating system you use. There is nothing to install and no plugin updates to track.",
                ],
            },
            {
                "heading": "Privacy, metadata, and when to strip EXIF",
                "paragraphs": [
                    "JPEG files often embed EXIF metadata: camera model, exposure settings, timestamps, and sometimes GPS coordinates. That data is invisible in the picture itself but increases file size slightly and may reveal information you did not intend to share.",
                    "FileShrinkr can remove EXIF during compression. This is useful before publishing client photos, listing rental properties, or uploading inventory images to a public marketplace. The visual pixels stay the same; only the hidden tags are dropped.",
                    "Stripping metadata is optional. If you rely on EXIF for photo sorting in Lightroom or similar tools, compress a copy for delivery and keep the original archive intact.",
                ],
            },
            {
                "heading": "When to convert JPG to another format instead",
                "paragraphs": [
                    "Sometimes compression alone is not enough. If you need transparency, PNG or WebP is a better target. If you are building a performance-focused website, WebP often beats JPG at the same visual quality. FileShrinkr lets you switch output format in the same upload flow.",
                    "For documents and scans, PDF may be the right deliverable. You can merge multiple compressed images into a single PDF without leaving the tool. That workflow is common for insurance claims, homework submissions, and signed forms.",
                    "JPG remains the lingua franca of photos. When compatibility matters most—email clients, older CMS platforms, or print shops—compressing in place as JPG is usually the fastest path.",
                ],
            },
        ],
    },
    "compress-png": {
        "slug": "compress-png",
        "title": "Compress PNG Online — Shrink PNG File Size | FileShrinkr",
        "description": "Reduce PNG file size online. Convert large PNG screenshots and graphics to optimized JPG or WebP, or compress PNGs for faster web delivery with FileShrinkr.",
        "h1": "Compress PNG Images Online",
        "preset_format": "jpg",
        "preset_quality": 80,
        "show_widget": True,
        "related_slugs": ["compress-jpg", "compress-webp", "compress-for-website"],
        "faqs": [
            {
                "q": "Can FileShrinkr compress PNG without converting format?",
                "a": "PNG is lossless, so meaningful size reduction usually means re-encoding with fewer colors or converting to JPG/WebP for photographic content. FileShrinkr optimizes by converting PNG photos to JPG at your chosen quality.",
            },
            {
                "q": "Will I lose transparency when compressing PNG?",
                "a": "JPG does not support transparency. If your PNG uses alpha channels—for logos or icons—consider WebP output or keep PNG and resize dimensions instead.",
            },
            {
                "q": "Why are my PNG screenshots so large?",
                "a": "Screenshots are often saved at full display resolution with lossless encoding. A single 4K capture can be several megabytes. Converting UI screenshots to JPG at quality 80–85 typically shrinks them dramatically.",
            },
            {
                "q": "Is PNG or JPG better for web graphics?",
                "a": "Photos and gradients belong in JPG or WebP. Flat graphics, logos, and images requiring transparency belong in PNG or SVG. Match the format to the content type.",
            },
            {
                "q": "Can I compress multiple PNG files in one go?",
                "a": "Yes. Upload a batch of PNG images and download compressed results together. Mixed batches with JPG and PNG are supported.",
            },
        ],
        "howto_steps": [
            {
                "name": "Add PNG files",
                "text": "Select one or more PNG images from your computer. Drag-and-drop works on desktop and many mobile browsers.",
            },
            {
                "name": "Pick output format",
                "text": "For photos and screenshots without transparency, choose JPG. For modern browsers, WebP may yield even smaller files at similar quality.",
            },
            {
                "name": "Compress and save",
                "text": "Run compression and download optimized files. Check edges and text readability before publishing.",
            },
        ],
        "sections": [
            {
                "heading": "Understanding PNG file size",
                "paragraphs": [
                    "PNG uses lossless compression, which preserves every pixel exactly. That is ideal for logos, diagrams, and images with transparency, but it means photographic PNGs are often enormous compared with JPG. A vacation photo exported as PNG might be ten times larger than the same scene saved as JPEG at quality 80.",
                    "Screenshots are a frequent culprit. Operating systems save the full bitmap of your display, including subtle gradients and anti-aliased text that PNG encodes faithfully. The result is a crisp file that is painful to email or upload to a ticket system.",
                    "FileShrinkr helps you shrink PNG payloads by converting photographic content to efficient formats while keeping the workflow simple. You stay in the browser, avoid desktop apps, and get predictable downloads.",
                ],
            },
            {
                "heading": "When to keep PNG and when to convert",
                "paragraphs": [
                    "Keep PNG when you need transparency, razor-sharp edges on flat colors, or pixel-perfect UI assets. App icons, badges with drop shadows on variable backgrounds, and technical illustrations usually belong here.",
                    "Convert PNG to JPG when the image is a photo, a scan, or a screenshot without alpha channels. The visual difference is negligible on most displays, while file size drops sharply. For web publishing, also consider WebP, which supports transparency in modern browsers.",
                    "If you are unsure, open the PNG and check for checkerboard areas or transparent regions. No transparency strongly suggests JPG or WebP is safe.",
                ],
            },
            {
                "heading": "Compressing screenshots for documentation and support",
                "paragraphs": [
                    "Technical writers and support teams attach countless screenshots to wikis, Slack threads, and bug trackers. Large PNGs slow scrolling and hit upload caps. Compressing to JPG at quality 80 preserves readable text while cutting bandwidth.",
                    "Pay attention to small type and colored UI chrome. If compression introduces fuzz around fonts, bump quality to 85 or slightly reduce dimensions before converting. A screenshot displayed at eight hundred pixels wide rarely needs four thousand pixels of source data.",
                    "FileShrinkr processes batches quickly, so an entire tutorial folder of PNG captures can be optimized in one pass before you commit to git or a knowledge base.",
                ],
            },
            {
                "heading": "PNG on websites and Core Web Vitals",
                "paragraphs": [
                    "Oversized PNG hero images hurt Largest Contentful Paint scores. Search engines and users both reward fast pages. Replacing a three-megabyte PNG banner with a two-hundred-kilobyte WebP or JPG can move performance metrics without a visible redesign.",
                    "Use responsive dimensions: export at the maximum display size you actually need, not the camera or canvas default. Pair compression with correct width and height attributes in HTML so layout stays stable.",
                    "FileShrinkr is a practical first step before you upload to WordPress, Shopify, or a static site generator. Smaller source files make every downstream CDN optimization more effective.",
                ],
            },
            {
                "heading": "Color depth and palette considerations",
                "paragraphs": [
                    "PNG supports truecolor and indexed palettes. Photos saved as PNG are almost always truecolor, which is why they are large. Indexed PNGs with few colors can be compact, but that mode suits flat graphics more than photographs.",
                    "When converting to JPG, subtle gradients may show banding at very low quality. Raise the slider or apply a light blur in an editor before compression if banding appears in skies or skin tones.",
                    "For brand assets with exact hex colors, test compressed output against your style guide. JPG may shift colors slightly due to chroma subsampling; WebP often preserves color more faithfully at smaller sizes.",
                ],
            },
            {
                "heading": "Workflow tips for designers and developers",
                "paragraphs": [
                    "Design handoffs often include PNG exports from Figma or Sketch. Developers should not ship those raw exports directly to production. Run them through FileShrinkr with appropriate format choice first.",
                    "Maintain source PNGs in your design repository; deploy compressed derivatives to production buckets. That split keeps editing flexible while keeping live sites fast.",
                    "Automate naming so compressed files are obvious—append `-compressed` or store in a `dist/` folder. Your future self will thank you when debugging asset pipelines.",
                ],
            },
        ],
    },
    "compress-webp": {
        "slug": "compress-webp",
        "title": "Compress WebP Online — Optimize WebP Images | FileShrinkr",
        "description": "Compress WebP images online for faster websites. FileShrinkr reduces WebP file size with adjustable quality for modern browsers and performance-focused publishing.",
        "h1": "Compress WebP Images Online",
        "preset_format": "webp",
        "preset_quality": 80,
        "show_widget": True,
        "related_slugs": ["jpg-vs-webp", "compress-for-website", "compress-jpg"],
        "faqs": [
            {
                "q": "How much smaller is WebP compared to JPG?",
                "a": "WebP often produces files 25–35% smaller than JPG at similar visual quality, though results vary by image content. FileShrinkr lets you compare by compressing the same source to both formats.",
            },
            {
                "q": "Can I compress WebP without converting to another format?",
                "a": "Yes. Select WebP as the output format and adjust quality. Re-encoding at a lower quality setting reduces file size while staying in WebP.",
            },
            {
                "q": "Do all browsers support WebP?",
                "a": "All major modern browsers support WebP. For legacy environments, serve JPG fallbacks using your site's picture element or CDN rules.",
            },
            {
                "q": "Does WebP support transparency?",
                "a": "Yes. WebP handles alpha channels more efficiently than PNG in many cases, making it excellent for compressed logos and overlays.",
            },
            {
                "q": "What quality should I use for WebP compression?",
                "a": "Start around 80 for photos on the web. WebP quality scales differently from JPG numbers, so trust your eyes more than the exact integer.",
            },
        ],
        "howto_steps": [
            {
                "name": "Upload images",
                "text": "Add WebP files or convert JPG/PNG sources to WebP in the same tool. Mixed input batches are fine.",
            },
            {
                "name": "Select WebP output",
                "text": "Choose WebP in the format dropdown and set quality. Enable EXIF stripping if you do not need metadata.",
            },
            {
                "name": "Download optimized WebP",
                "text": "Compress and save. Deploy the new files to your CDN or CMS and verify they load correctly.",
            },
        ],
        "sections": [
            {
                "heading": "Why WebP matters for modern websites",
                "paragraphs": [
                    "WebP combines strong lossy and lossless compression with optional transparency in a single format. Google introduced it to shrink the web, and adoption is now broad enough that performance-minded publishers treat it as a default photo format.",
                    "Smaller images mean faster pages, lower hosting bills, and better experiences on mobile networks. When your LCP image is a WebP instead of a heavy JPG, users see content sooner and bounce less.",
                    "FileShrinkr makes WebP compression accessible without configuring codecs locally. Upload, tune quality, download—ready for upload to S3, Cloudflare, or your favorite static host.",
                ],
            },
            {
                "heading": "Compressing existing WebP files",
                "paragraphs": [
                    "If you inherited WebP assets from a previous export, they may still be larger than necessary. Early CMS plugins used conservative quality defaults. Re-running those files through FileShrinkr with a deliberate quality target often recovers kilobytes page-wide.",
                    "Avoid endless generation loss: always compress from the highest-quality source you have, ideally the original camera JPEG or RAW export, not a repeatedly re-encoded derivative.",
                    "When batch-processing an image folder from a redesign, consistent WebP settings keep visual tone uniform across galleries and blog posts.",
                ],
            },
            {
                "heading": "Converting JPG and PNG to WebP",
                "paragraphs": [
                    "You do not need a separate converter. FileShrinkr accepts JPG and PNG uploads and outputs WebP in one step. This is the fastest way to migrate a legacy media library toward modern formats.",
                    "Photographic JPGs translate well. PNGs with transparency can become WebP with alpha, often beating PNG size by a wide margin. Flat PNG icons with few colors should be evaluated visually after conversion.",
                    "After conversion, spot-check critical pages in Safari, Chrome, and Firefox. Although support is excellent, your CMS theme or lazy-load script might need a small update to reference the new extensions.",
                ],
            },
            {
                "heading": "Quality settings for WebP in production",
                "paragraphs": [
                    "WebP quality numbers are not identical to JPG quality numbers. A WebP at 80 is not strictly equivalent to JPG at 80. Use FileShrinkr previews and side-by-side checks for hero images.",
                    "Thumbnails and card images can use more aggressive compression—often quality 70–75—because they display small. Full-width article headers deserve 80–85 unless you intentionally chase minimal bytes.",
                    "Pair compression with responsive images. Serving a two-thousand-pixel WebP on a four-hundred-pixel slot wastes bytes even if the format is efficient.",
                ],
            },
            {
                "heading": "WebP for e-commerce and catalogs",
                "paragraphs": [
                    "Product listing pages load dozens of images. Shaving thirty percent off each thumbnail multiplies into meaningful savings. Faster catalogs correlate with higher conversion on slow connections.",
                    "Keep backgrounds and fabric textures in mind. Fine patterns compress differently than smooth pack shots. Audit a few SKUs manually before applying one global quality preset to thousands of variants.",
                    "FileShrinkr batch mode fits catalog updates after seasonal shoots. Compress the whole export, upload to your PIM or storefront, and purge CDN caches.",
                ],
            },
            {
                "heading": "Fallbacks, SEO, and social sharing",
                "paragraphs": [
                    "Some social crawlers and older email clients still prefer JPG or PNG. Keep Open Graph images in a widely supported format even if on-site assets use WebP.",
                    "Use HTML picture elements or CDN format negotiation to serve WebP where accepted and JPG elsewhere. FileShrinkr can generate both from the same source upload in separate passes.",
                    "Search engines index pages, not raw files alone. Faster pages indirectly help rankings by improving engagement signals, but alt text and relevant filenames remain essential for image SEO.",
                ],
            },
            {
                "heading": "Building a repeatable WebP export habit",
                "paragraphs": [
                    "Treat WebP compression as part of publish checklist, not an occasional cleanup task. When every new blog post, product launch, and landing page ships with optimized WebP assets, performance stays consistent quarter after quarter.",
                    "FileShrinkr removes friction from that habit. No license keys, no batch scripts to maintain—just upload, compress, and move on. Teams that adopt the habit early spend less time firefighting slow pages later.",
                    "Schedule a quarterly review of your largest WebP assets. Camera resolutions creep upward each hardware generation; yesterday's reasonable export preset may need a refresh when editors start shooting on newer phones.",
                ],
            },
        ],
    },
    "images-to-pdf": {
        "slug": "images-to-pdf",
        "title": "Convert Images to PDF Online — Merge & Compress | FileShrinkr",
        "description": "Turn JPG, PNG, and WebP images into PDF documents online. Merge multiple photos into one PDF and compress embedded images with FileShrinkr.",
        "h1": "Convert Images to PDF Online",
        "preset_format": "pdf",
        "preset_quality": None,
        "show_widget": True,
        "related_slugs": ["compress-jpg", "compress-for-email", "how-to-reduce-image-size"],
        "faqs": [
            {
                "q": "Can I merge multiple images into a single PDF?",
                "a": "Yes. Enable merge mode when converting to PDF and FileShrinkr combines your uploads into one document in upload order.",
            },
            {
                "q": "Will the PDF compress images inside the file?",
                "a": "You can compress embedded images during PDF creation, which dramatically reduces scan and photo PDF size while keeping text readable.",
            },
            {
                "q": "What image formats can be converted to PDF?",
                "a": "FileShrinkr accepts common raster formats including JPG, PNG, WebP, and others supported by the processing pipeline.",
            },
            {
                "q": "Is the conversion lossless?",
                "a": "When compression is disabled, images are embedded with minimal re-encoding. When compression is enabled, images are optimized for smaller PDF size.",
            },
            {
                "q": "Can I use this for document submissions?",
                "a": "Many schools, insurers, and government portals accept photo PDFs. Always check file size limits before submitting.",
            },
        ],
        "howto_steps": [
            {
                "name": "Upload images",
                "text": "Select the photos or scans you want in PDF form. Order matters when merging—upload in the sequence you need.",
            },
            {
                "name": "Choose PDF options",
                "text": "Set format to PDF, enable merge if you want one file, and toggle image compression based on whether you prioritize size or fidelity.",
            },
            {
                "name": "Download your PDF",
                "text": "Start conversion and save the PDF. Verify page order and readability before sending.",
            },
        ],
        "sections": [
            {
                "heading": "Why convert images to PDF",
                "paragraphs": [
                    "PDF is the universal container for printable and submittable documents. A photo of a signed contract, a stack of receipts, or homework pages is easier to handle as one PDF than as loose JPEG attachments.",
                    "Portals for visas, insurance claims, and university applications often specify PDF with maximum file sizes. Converting camera photos to a compressed PDF keeps you inside those limits without fax machines or desktop Acrobat licenses.",
                    "FileShrinkr bridges the gap between quick phone captures and formal PDF deliverables. You get merge and compression controls in the same interface you already use for image optimization.",
                ],
            },
            {
                "heading": "Merging multiple photos into one document",
                "paragraphs": [
                    "Merge mode stitches images into a single PDF in the order you upload. That order is perfect for multi-page forms photographed page by page, or before-and-after photo sets for contractors.",
                    "Name your source files with numeric prefixes if you prepare them in a folder first—`01-front.jpg`, `02-back.jpg`—so the sequence is obvious before upload.",
                    "After download, open the PDF in any reader to confirm orientation. Rotate pages on your phone before upload if possible to avoid sideways output.",
                ],
            },
            {
                "heading": "Compressing images inside PDFs",
                "paragraphs": [
                    "Uncompressed photo PDFs balloon quickly. A five-page scan at phone resolution can exceed twenty megabytes. Compressing embedded images targets the heavy raster data while leaving vector text sharp when present.",
                    "For document scans, moderate compression preserves legibility of body text and signatures. For art portfolios where color fidelity matters, use lighter compression or disable it for that batch.",
                    "FileShrinkr uses tuned pipelines—Pillow and img2pdf—so you are not guessing which encoder flag to pass on the command line.",
                ],
            },
            {
                "heading": "Mobile capture workflows",
                "paragraphs": [
                    "Most users photograph documents on phones. Good lighting, parallel edges, and a flat surface matter more than megapixels. Crop aggressively in your camera app before upload to exclude desks and backgrounds.",
                    "If your institution requires sub-megabyte PDFs, combine cropping with compression enabled. A well-lit page at two megapixels compresses far better than a skewed full-room shot at twelve.",
                    "FileShrinkr works in mobile browsers, so you can capture, upload, and download without transferring files to a laptop.",
                ],
            },
            {
                "heading": "Professional and legal considerations",
                "paragraphs": [
                    "Some workflows demand archival PDF/A or unmodified originals. Know your requirements before compressing. FileShrinkr optimizes for everyday submission and sharing, not long-term legal archive replacement.",
                    "Redact sensitive information before converting. Compression does not remove account numbers or personal data visible in pixels—edit images first.",
                    "When delivering client proofs, mention that PDF compression was applied so recipients know the file is optimized for viewing, not for high-end print reproduction.",
                ],
            },
            {
                "heading": "Combining PDF output with image compression",
                "paragraphs": [
                    "A smart pipeline compresses individual JPGs first when you need both loose images and a PDF bundle. Run one batch as JPG for web galleries and a second merged PDF for email delivery.",
                    "For recurring workflows—monthly expense reports, inspection checklists—bookmark FileShrinkr with PDF presets saved in muscle memory. Consistent output reduces rejection from upload portals.",
                    "If a portal rejects your PDF, check their stated DPI and dimension caps. Downscale oversized photos before PDF conversion to meet implicit limits even when the site only mentions megabytes.",
                ],
            },
            {
                "heading": "Accessibility and readability in photo PDFs",
                "paragraphs": [
                    "Low contrast photos of documents hurt everyone, especially users with vision differences. Brighten captures before conversion when possible, and avoid heavy compression that smears serif fonts.",
                    "Screen readers cannot OCR your images automatically unless the PDF contains real text layers. Photo PDFs are fine for human review but are not a substitute for accessible digital forms when regulations apply.",
                    "FileShrinkr helps you meet size limits without skipping a manual legibility check. Zoom to one hundred percent on a phone screen before you submit—if you can read it, reviewers likely can too.",
                    "For mixed batches—some portrait pages, some landscape—upload in final reading order and merge once. Reordering PDF pages after the fact wastes time compared to getting sequence right at capture time.",
                    "Label downloads with dates and purpose—`lease-application-2025-06.pdf`—so recipients and future you can find submissions in crowded download folders without opening every file.",
                ],
            },
        ],
    },
    "compress-for-email": {
        "slug": "compress-for-email",
        "title": "Compress Images for Email — Stay Under Attachment Limits | FileShrinkr",
        "description": "Compress photos for email attachments so they send reliably. FileShrinkr reduces image file size under Gmail, Outlook, and corporate mailbox limits.",
        "h1": "Compress Images for Email",
        "preset_format": "jpg",
        "preset_quality": 70,
        "show_widget": True,
        "related_slugs": ["compress-jpg", "images-to-pdf", "compress-for-whatsapp"],
        "faqs": [
            {
                "q": "What size should email attachments be?",
                "a": "Many providers limit messages to 20–25 MB total. Individual attachments around 5–10 MB are safer. Compressed JPGs at quality 65–75 usually land well under those caps.",
            },
            {
                "q": "Should I send JPG or PNG in email?",
                "a": "JPG is almost always better for photos. PNG is appropriate only when you need lossless screenshots with text or transparency.",
            },
            {
                "q": "Will compressed photos look bad in email?",
                "a": "At quality 70, most recipients cannot tell on laptop or phone screens. Avoid extreme compression below 50 unless bandwidth is critical.",
            },
            {
                "q": "Can I compress several photos before sending one email?",
                "a": "Yes. Batch compress, then attach the smaller files or zip them if your client prefers a single archive.",
            },
            {
                "q": "Does stripping EXIF help email size?",
                "a": "EXIF removal saves a little space and avoids sharing location or device metadata unintentionally.",
            },
        ],
        "howto_steps": [
            {
                "name": "Select photos to email",
                "text": "Gather the images you plan to attach. If there are many, note the total uncompressed size.",
            },
            {
                "name": "Compress at email-friendly quality",
                "text": "Use JPG at quality 65–75. Enable EXIF stripping for privacy.",
            },
            {
                "name": "Attach and send",
                "text": "Download compressed files and add them to your message. Confirm the total size bar in your mail client stays green.",
            },
        ],
        "sections": [
            {
                "heading": "Email attachment limits are real",
                "paragraphs": [
                    "Gmail, Outlook, Yahoo, and corporate Exchange servers enforce message size limits. A few RAW-like phone photos can exceed twenty-five megabytes combined, triggering bounce messages or silent failures on mobile clients.",
                    "Recipients on slow connections appreciate smaller attachments too. A five-megabyte download on rural LTE is still annoying; five files at three hundred kilobytes each feels instant.",
                    "FileShrinkr targets the email use case with sensible JPG defaults. You compress before composing, so your mail client never warns you at send time.",
                ],
            },
            {
                "heading": "Recommended settings for everyday sharing",
                "paragraphs": [
                    "Quality 70 is a strong default for family photos, vacation shots, and office event pictures. Faces remain natural, skies stay smooth, and files often shrink by half or more.",
                    "If you send product photos to buyers or detail shots to contractors, bump to 75–80. If you send quick reference snaps where clarity is nice but not critical, 60–65 saves more bytes.",
                    "Resize mentally: if the recipient will only view on a phone, you do not need four-thousand-pixel widths. Pair compression with reasonable dimensions for maximum effect.",
                ],
            },
            {
                "heading": "Corporate mail and security scanners",
                "paragraphs": [
                    "Enterprise gateways sometimes block large attachments or specific extensions. Smaller JPGs pass more reliably than huge PNG exports or zip bombs mistaken for risk.",
                    "Some filters strip metadata for policy reasons. Proactively removing EXIF with FileShrinkr aligns with security expectations and avoids accidental GPS leaks in field photos.",
                    "When in doubt, ask IT for published limits. Design your compression target ten percent below the official cap to account for HTML message overhead.",
                ],
            },
            {
                "heading": "Inline images versus attachments",
                "paragraphs": [
                    "Marketing emails embed images inline via CID or hosted URLs. Transactional messages still rely on attachments for invoices, proofs, and signed scans. Know which pattern you are using.",
                    "Inline images should be aggressively optimized—often under one hundred kilobytes each—because they load even if the user never downloads an attachment. Attachments can be slightly larger because users choose to fetch them.",
                    "FileShrinkr helps both paths: compress heroes for inline use and attachments for explicit downloads in the same session.",
                ],
            },
            {
                "heading": "PDF as an email-friendly alternative",
                "paragraphs": [
                    "When you need multiple pages—scanned forms, brochures—merge to PDF instead of attaching six separate JPEGs. One PDF feels professional and is easier to forward.",
                    "Enable PDF image compression in FileShrinkr to keep merged documents under portal limits. Recipients open one file instead of juggling album order.",
                    "If a recipient cannot open PDFs on an older device, fall back to a small set of JPGs compressed with the same quality preset for consistency.",
                ],
            },
            {
                "heading": "Etiquette and accessibility",
                "paragraphs": [
                    "Describe attachments in plain language in the email body so screen-reader users know what to expect. Good filenames—`invoice-march-compressed.jpg`—beat `IMG_4092.jpg`.",
                    "Avoid sending uncompressed bursts of twenty photos when five curated shots tell the story. Compression plus thoughtful selection respects inbox space.",
                    "If someone replies that images are blurry, re-send a higher quality subset rather than the whole album at max compression. FileShrinkr makes it cheap to run another pass at quality 80.",
                ],
            },
            {
                "heading": "Troubleshooting failed email sends",
                "paragraphs": [
                    "When a message bounces or stalls at sending, check total attachment weight first. Mail clients sometimes show per-file size but hide cumulative totals across many images.",
                    "Split large sets into two messages with descriptive subjects, or merge related scans into one compressed PDF. Recipients often prefer two labeled emails over one giant zip that antivirus quarantines.",
                    "If compression still leaves you over the limit, resize in FileShrinkr's editor tab before compressing again. Removing pixels beats crushing quality into artifact-heavy mush.",
                    "Save compressed attachments with clear names before dragging them into compose windows. Mail clients sometimes duplicate files when you re-pick from recent downloads, doubling size accidentally.",
                    "Holiday newsletters and school updates spike attachment traffic in predictable seasons. Pre-compress entire albums once, store in a shared drive, and reuse the same optimized files across multiple recipient lists.",
                    "Apple Mail and Outlook mobile preview attachments inline. Smaller JPGs render previews faster, which helps recipients decide whether to download full albums on cellular data.",
                ],
            },
        ],
    },
    "compress-for-whatsapp": {
        "slug": "compress-for-whatsapp",
        "title": "Compress Images for WhatsApp — Send Photos Faster | FileShrinkr",
        "description": "Compress photos for WhatsApp before sending. FileShrinkr shrinks image file size so pictures upload quickly and stay sharp on mobile screens.",
        "h1": "Compress Images for WhatsApp",
        "preset_format": "jpg",
        "preset_quality": 65,
        "show_widget": True,
        "related_slugs": ["compress-for-email", "compress-jpg", "how-to-reduce-image-size"],
        "faqs": [
            {
                "q": "Does WhatsApp compress images I send?",
                "a": "WhatsApp recompresses photos in chat, which can reduce quality unpredictably. Pre-compressing with FileShrinkr gives you control before the app applies its own rules.",
            },
            {
                "q": "What quality works best for WhatsApp photos?",
                "a": "Quality 60–70 is usually enough for phone viewing. FileShrinkr defaults toward 65 for this page to balance speed and clarity.",
            },
            {
                "q": "Can I send documents via WhatsApp using compressed images?",
                "a": "You can send JPG photos of documents. For multi-page scans, consider PDF merge in FileShrinkr and send as a document if your workflow allows.",
            },
            {
                "q": "Why do my WhatsApp photos look blurry?",
                "a": "Double compression—huge originals squeezed by both FileShrinkr too aggressively and WhatsApp—is a common cause. Start from a reasonable resolution and moderate quality.",
            },
            {
                "q": "Is WebP good for WhatsApp?",
                "a": "WhatsApp expects JPG/PNG in most chat flows. Stick to JPG for broad compatibility when sharing photos.",
            },
        ],
        "howto_steps": [
            {
                "name": "Pick photos to share",
                "text": "Choose images from your gallery or export chat-bound photos to your computer for batch compression.",
            },
            {
                "name": "Compress for mobile viewing",
                "text": "Use JPG around quality 65. Avoid oversized dimensions—two thousand pixels on the long edge is plenty for chat.",
            },
            {
                "name": "Send via WhatsApp",
                "text": "Transfer compressed files to your phone if needed, then attach in chat or status. Uploads should complete faster on slow networks.",
            },
        ],
        "sections": [
            {
                "heading": "How WhatsApp handles your photos",
                "paragraphs": [
                    "WhatsApp optimizes media for its network. Photos you send are often re-encoded to save bandwidth and storage on servers. That second compression hurts most when your original is already huge or heavily edited.",
                    "By delivering a right-sized JPG first, you steer the visual outcome. You trade a little control upfront for less surprise when recipients view images on varied devices.",
                    "FileShrinkr gives you a quick pre-flight check before images enter WhatsApp's pipeline, especially useful for business accounts sharing product shots or service before-and-after photos.",
                ],
            },
            {
                "heading": "Sizing images for chat and status",
                "paragraphs": [
                    "Chat thumbnails and full-screen mobile views rarely need desktop poster resolution. Scale down to roughly sixteen hundred to two thousand pixels on the longest side, then compress.",
                    "Status updates and group broadcasts reach many recipients on metered data. Smaller files mean faster delivery and less frustration when connectivity flickers.",
                    "For profile photos and logos, crop square in your editor first, then compress. WhatsApp displays circles and small tiles; extra border pixels are wasted bytes.",
                ],
            },
            {
                "heading": "Business and customer support workflows",
                "paragraphs": [
                    "Small businesses use WhatsApp for orders, support, and proofs. Sending five uncompressed product photos can clog a customer's storage and slow the conversation.",
                    "Compress consistently so your catalog looks uniform. Pair FileShrinkr with a simple naming scheme—`sku-12345-q65.jpg`—so staff pick the right assets quickly.",
                    "When customers send you huge photos, ask them to use a compression link before resending. Educating politely reduces back-and-forth about blurry auto-compression.",
                ],
            },
            {
                "heading": "Avoiding the double-compression trap",
                "paragraphs": [
                    "Do not start from WhatsApp-downloaded images and recompress aggressively for re-forwarding. Each generation accumulates artifacts. Keep originals in a cloud folder when possible.",
                    "If you must forward chain content, use moderate quality—around 75—and avoid pushing file sizes to the absolute minimum.",
                    "Screenshots of chats themselves are PNG-heavy; convert to JPG before sharing outside WhatsApp to prevent enormous files in email archives.",
                ],
            },
            {
                "heading": "Privacy considerations on messaging apps",
                "paragraphs": [
                    "Photos may contain EXIF GPS from the camera moment. Stripping metadata before sharing location-sensitive images—home interiors, kids' events—is a good habit.",
                    "FileShrinkr's optional EXIF removal keeps pixels intact while dropping hidden tags. This is not a substitute for blurring faces or license plates when needed.",
                    "Business compliance may require retaining originals separately from customer-facing compressed copies. Document which version was sent.",
                ],
            },
            {
                "heading": "When to use documents instead of photos",
                "paragraphs": [
                    "Multi-page PDFs sometimes travel better as document attachments than a flood of JPEGs. FileShrinkr can build that PDF with compressed pages first.",
                    "For invoices or ID scans, verify legibility after compression at phone zoom levels. Bump quality to 75 if small text wavers.",
                    "Video is outside FileShrinkr's scope, but the same philosophy applies: right-size before upload to any messaging platform.",
                ],
            },
            {
                "heading": "Group chats, forwarding chains, and storage limits",
                "paragraphs": [
                    "Large images in active groups download to every member's device automatically on many settings. Compressing before posting is a courtesy that keeps communal threads usable on older phones with limited storage.",
                    "Forwarded media often carries stale compression from earlier hops. When you curate news, deals, or instructions for a community, re-export from originals through FileShrinkr instead of resharing degraded copies.",
                    "WhatsApp Web and desktop clients sync with phone libraries. Organize a compressed folder on your computer, batch-process with consistent quality, then transfer once—cleaner than compressing phone-side repeatedly.",
                    "For marketing broadcasts, test one compressed image on your own device before blasting a list. What looks crisp on a monitor may show banding on mid-range Android screens at night mode brightness.",
                    "Field technicians sending site photos benefit from a single quality preset everyone memorizes—quality 65 JPG, longest edge sixteen hundred pixels. Consistency beats per-user improvisation when managers review dozens of chats daily.",
                    "Voice notes and images often mix in long support threads. Keeping images lean prevents the chat backup from ballooning when customers export history for their records.",
                    "Seasonal campaigns—Diwali catalogs, holiday menus, school event flyers—ship faster when creatives compress once in FileShrinkr instead of relying on chat auto-quality alone.",
                ],
            },
        ],
    },
    "compress-for-website": {
        "slug": "compress-for-website",
        "title": "Compress Images for Websites — Faster Page Loads | FileShrinkr",
        "description": "Optimize images for websites with FileShrinkr. Compress JPG and WebP photos for faster loading, better Core Web Vitals, and improved SEO performance.",
        "h1": "Compress Images for Websites",
        "preset_format": "webp",
        "preset_quality": 80,
        "show_widget": True,
        "related_slugs": ["compress-webp", "jpg-vs-webp", "resize-image"],
        "faqs": [
            {
                "q": "What image format is best for websites?",
                "a": "WebP is excellent for modern browsers; JPG remains a strong fallback. FileShrinkr lets you export either from the same upload.",
            },
            {
                "q": "How small should web images be?",
                "a": "Hero images under three hundred kilobytes and thumbnails under fifty kilobytes are reasonable targets on content sites, though context matters.",
            },
            {
                "q": "Will compression hurt SEO?",
                "a": "Faster pages help user experience signals. Compressed images with good alt text and filenames support SEO more than uncompressed slow pages.",
            },
            {
                "q": "Should I strip EXIF on web images?",
                "a": "Yes for public sites. EXIF adds bytes and can leak camera metadata without benefit to visitors.",
            },
            {
                "q": "Can I batch optimize a media library?",
                "a": "Upload batches from your CMS export, compress with consistent settings, and re-upload optimized files.",
            },
        ],
        "howto_steps": [
            {
                "name": "Export CMS images",
                "text": "Download or gather originals from your media library. Work from highest quality sources, not already tiny thumbnails.",
            },
            {
                "name": "Compress to WebP or JPG",
                "text": "Use WebP around quality 80 for photos. Strip EXIF. Resize in the editor tab if sources exceed display dimensions.",
            },
            {
                "name": "Re-upload and purge cache",
                "text": "Replace files in your CMS or CDN and purge caches so visitors receive optimized assets.",
            },
        ],
        "sections": [
            {
                "heading": "Images dominate page weight",
                "paragraphs": [
                    "On typical content and e-commerce pages, images account for more transferred bytes than HTML, CSS, and JavaScript combined. Unoptimized hero photos are the main reason Lighthouse flags slow Largest Contentful Paint.",
                    "Visitors do not wait politely. Every extra second on mobile increases bounce probability. Compression is the highest-leverage fix before you invest in expensive infrastructure.",
                    "FileShrinkr is built for publishers who need quick wins without learning ImageMagick flags. Compress, upload, measure again—iterate in minutes.",
                ],
            },
            {
                "heading": "Matching compression to layout slots",
                "paragraphs": [
                    "A full-width banner displayed at twelve hundred CSS pixels does not need a four-thousand-pixel source. Scale to twice the display width for retina, then compress.",
                    "Card thumbnails can tolerate lower quality than hero images because they render small. Use different presets per template in your head, even if you process them in one FileShrinkr batch by grouping folders.",
                    "Background decorative images should be tiny—sometimes under thirty kilobytes. If blur overlays sit on top, compress aggressively; artifacts hide beneath the effect.",
                ],
            },
            {
                "heading": "WebP-first with JPG fallback",
                "paragraphs": [
                    "Adopt WebP for internal assets and provide JPG alternates for environments without support. FileShrinkr generates either format from the same master upload.",
                    "CDNs like Cloudflare can negotiate formats automatically if you upload both. Start with WebP compression here, then keep JPG variants for `<picture>` fallbacks.",
                    "Measure real-user metrics after rollout. Synthetic lab tests help, but field data confirms whether your compression budget matches actual devices on your site.",
                ],
            },
            {
                "heading": "CMS-specific tips",
                "paragraphs": [
                    "WordPress, Webflow, Shopify, and static generators all generate oversized uploads if you drag originals straight from a camera. Compress before upload every time.",
                    "Avoid letting plugins double-compress blindly. Some optimization plugins re-encode already optimized files on every save, degrading quality. Establish FileShrinkr as the canonical optimization step.",
                    "Use descriptive filenames and alt text after compression. `team-office-compressed.webp` paired with meaningful alt attributes beats generic DSC codes for accessibility and search relevance.",
                ],
            },
            {
                "heading": "Core Web Vitals and business impact",
                "paragraphs": [
                    "LCP, INP, and CLS collectively describe how usable your site feels. Images influence LCP directly when they are the largest above-the-fold element.",
                    "Faster sites convert better in e-commerce and generate more ad impressions in content businesses. Compression is not vanity; it is revenue-adjacent engineering.",
                    "Set a performance budget per template: maximum kilobytes for hero, gallery row, and icon sprites. FileShrinkr helps enforce that budget during content entry.",
                ],
            },
            {
                "heading": "Long-term media governance",
                "paragraphs": [
                    "Document compression presets in your style guide so writers and designers do not guess. Link to FileShrinkr from internal wiki pages.",
                    "Audit quarterly. Old posts may still serve multi-megabyte PNG screenshots from before your standards existed. Batch reprocess and replace.",
                    "Pair compression with lazy loading and responsive `srcset` so browsers download only what the viewport needs. Format and dimension choices work together, not in isolation.",
                ],
            },
            {
                "heading": "Measuring success after optimization",
                "paragraphs": [
                    "Before-and-after waterfall charts in WebPageTest show whether your new WebP heroes actually shrink transfer size. Celebrate kilobytes saved per page—they compound across traffic.",
                    "Track error rates after migration. A misconfigured MIME type or missing fallback hurts fewer users than a five-megabyte JPG hurts everyone. Validate templates in staging first.",
                    "FileShrinkr is one layer in a healthy stack: CDN caching, HTTP/2, font subsetting, and script diet matter too. Image compression is usually the fastest layer to improve without redesigning UX.",
                    "Share wins with stakeholders using plain language: we cut the homepage hero from two megabytes to one hundred eighty kilobytes. Non-technical leaders fund maintenance when they see concrete byte counts, not jargon alone.",
                    "International audiences on slower networks feel compression wins first. Optimizing images is inclusive design: you are not just pleasing Lighthouse—you are reducing load on users who pay per megabyte.",
                    "Template libraries in design tools often re-import stale hero assets. When you refresh brand photography, recompress every derived size in one FileShrinkr session before redeploying.",
                    "Affiliate and partner pages sometimes hotlink your originals. Serving lean assets at source reduces surprise bandwidth bills when partners embed your images without caching discipline.",
                ],
            },
        ],
    },
    "resize-image": {
        "slug": "resize-image",
        "title": "Resize Image Online — Change Dimensions Before Compress | FileShrinkr",
        "description": "Learn when and how to resize images for email, web, and chat. Use FileShrinkr's editor to change dimensions before compression for maximum file size reduction.",
        "h1": "Resize Images Before You Compress",
        "preset_format": None,
        "preset_quality": None,
        "show_widget": False,
        "related_slugs": ["/?tab=editor"],
        "faqs": [
            {
                "q": "Why resize instead of only compress?",
                "a": "Compression reduces encoding size per pixel; resizing reduces pixel count. Dropping a four-thousand-pixel image to twelve hundred pixels wide often saves more bytes than extreme quality lowering.",
            },
            {
                "q": "Where is the FileShrinkr image editor?",
                "a": "Open the homepage editor tab at /?tab=editor to set width, height, and aspect ratio before compression.",
            },
            {
                "q": "Will resizing crop my photo?",
                "a": "You can fit within dimensions preserving aspect ratio or target exact sizes depending on editor settings. Preview before exporting.",
            },
            {
                "q": "What dimensions should I use for social and web?",
                "a": "Common targets include 1200 px for blog content, 1080 px for Instagram squares, and 1600 px for hero banners—always pair with compression.",
            },
            {
                "q": "Can I resize and compress in one step?",
                "a": "Yes. Resize in the editor tab, then run compression with your preferred format and quality on the output.",
            },
        ],
        "howto_steps": [
            {
                "name": "Open the image editor",
                "text": "Go to FileShrinkr homepage and switch to the editor tab to upload an image for resizing.",
            },
            {
                "name": "Set target dimensions",
                "text": "Enter width and height or choose a preset. Keep aspect ratio locked unless you intentionally need to crop.",
            },
            {
                "name": "Compress the resized output",
                "text": "After resizing, compress to JPG or WebP with appropriate quality for your delivery channel.",
            },
        ],
        "sections": [
            {
                "heading": "Resize and compress are partners",
                "paragraphs": [
                    "Many people jump straight to quality sliders when files are too large. That works, but resizing is often the bigger lever. Pixels scale quadratically: halving width and height cuts pixel count by seventy-five percent, which compression then encodes far more efficiently.",
                    "A four-thousand by three-thousand vacation photo is beautiful in a gallery, but wasteful as an inline email image. Resize to the display context first, then compress.",
                    "FileShrinkr separates these steps thoughtfully: use the editor tab at /?tab=editor for geometry, then the compressor for encoding. Together they mirror professional export dialogs without desktop software.",
                ],
            },
            {
                "heading": "Choosing target dimensions",
                "paragraphs": [
                    "Start from where the image will appear. Measure your blog content column in CSS pixels, multiply by two for retina displays, and set that as your maximum width.",
                    "Social platforms publish recommended sizes that change over time. Treat them as guidance, not religion—slightly larger with compression beats slightly too small and upscaled.",
                    "For thumbnails, be ruthless. Two hundred to four hundred pixels on the long edge plus JPG at quality 70 is enough for many listing pages.",
                ],
            },
            {
                "heading": "Aspect ratio and cropping discipline",
                "paragraphs": [
                    "Unlock aspect ratio only when you deliberately crop. Accidental stretching makes product photos look untrustworthy and portraits unflattering.",
                    "Center important subjects when cropping for cards. Automated center crops fail on off-center products; manual editor crops take seconds and save brand perception.",
                    "Document aspect ratios per template—16:9 heroes, 1:1 product tiles—so contractors deliver consistently sized sources.",
                ],
            },
            {
                "heading": "Resizing screenshots and UI assets",
                "paragraphs": [
                    "Screenshots should match the width they will embed at in documentation. A twelve-hundred-pixel article slot does not need a five-K capture scaled in HTML—that still wastes bytes if someone opens the full image.",
                    "Resize UI assets to exact pixel grids to avoid blurry edges. Pair PNG or WebP for flat graphics with appropriate compression afterward.",
                    "Developer teams should store `@2x` masters but deploy `@1x` web sizes when retina assets are not required.",
                ],
            },
            {
                "heading": "Print versus screen resizing",
                "paragraphs": [
                    "Screen resizing ignores DPI metadata for the most part; pixel dimensions matter. Print workflows care about inches and DPI. Do not confuse the two when preparing web assets.",
                    "If a client asks for print from a web-sized image, you need more pixels, not more compression. Upsampling cannot invent detail.",
                    "FileShrinkr optimizes for digital delivery. Export print masters separately at full resolution.",
                ],
            },
            {
                "heading": "Putting it together in FileShrinkr",
                "paragraphs": [
                    "Open /?tab=editor, upload, set dimensions, and export an intermediate file. Feed that into the compressor with WebP or JPG settings tuned to your channel.",
                    "For batches, resize groups with similar targets together so you are not switching aspect ratios every file. Consistency speeds content ops.",
                    "Measure results: compare before-and-after file sizes and page load metrics. Resize-plus-compress should produce dramatic drops without visible harm on target devices.",
                ],
            },
            {
                "heading": "Open the FileShrinkr editor",
                "paragraphs": [
                    "Ready to resize? Open the homepage editor at /?tab=editor, upload your image, and set the dimensions your channel requires. The editor pairs naturally with the compressor on the same site.",
                    "Bookmark that URL if you resize weekly—real-estate listings, marketplace inventory, and blog featured images all benefit from a two-step resize-then-compress routine you can repeat in minutes.",
                    "After exporting resized files, return to any format-specific landing page here to apply the right JPG or WebP quality preset for email, WhatsApp, or web delivery.",
                    "Related tool: open /?tab=editor whenever this guide's resize step applies. That tab is the dedicated surface for width, height, and aspect ratio before you compress.",
                    "Photographers delivering client galleries can export web previews at twelve hundred pixels wide, then compress—clients get fast downloads while you retain full-resolution masters offline.",
                    "Use the editor link /?tab=editor as your related next step when dimensions—not encoding—are the bottleneck. Resize first, then pick a format-specific compress page for delivery.",
                    "Marketplace sellers uploading variant swatches should resize squares to eight hundred pixels before JPG compression so grids load snappily on mobile shopper sessions.",
                    "One extra pixel row rarely matters; hundreds of unnecessary pixels always do.",
                ],
            },
        ],
    },
    "jpg-vs-webp": {
        "slug": "jpg-vs-webp",
        "title": "JPG vs WebP — Which Format Should You Use? | FileShrinkr",
        "description": "Compare JPG and WebP for websites, email, and apps. Learn differences in file size, quality, transparency, and browser support to pick the right format in FileShrinkr.",
        "h1": "JPG vs WebP: Which Format Wins?",
        "preset_format": None,
        "preset_quality": None,
        "show_widget": False,
        "related_slugs": ["compress-webp", "compress-jpg", "compress-for-website"],
        "faqs": [
            {
                "q": "Is WebP always better than JPG?",
                "a": "For many photos on the web, WebP is smaller at similar quality. JPG still wins on universal compatibility and some print workflows.",
            },
            {
                "q": "Can WebP replace JPG everywhere?",
                "a": "Not yet. Keep JPG fallbacks for email, some social crawlers, and legacy systems while serving WebP on your site.",
            },
            {
                "q": "Which format supports transparency?",
                "a": "WebP supports alpha transparency. Standard JPG does not—use PNG or WebP when you need transparent backgrounds.",
            },
            {
                "q": "Do JPG and WebP quality numbers match?",
                "a": "No. Quality scales differ between encoders. Compare visually at similar file sizes instead of matching numeric sliders.",
            },
            {
                "q": "How do I test both formats quickly?",
                "a": "Upload the same source to FileShrinkr twice—once as JPG, once as WebP—and compare size and clarity side by side.",
            },
        ],
        "howto_steps": [
            {
                "name": "Identify your delivery channel",
                "text": "Websites favor WebP with fallbacks; email and some apps still prefer JPG.",
            },
            {
                "name": "Export both formats from one source",
                "text": "Use FileShrinkr to compress the same original to JPG and WebP at sensible qualities.",
            },
            {
                "name": "Compare size and visual quality",
                "text": "Open both at intended display size and pick the format that meets your budget with acceptable clarity.",
            },
        ],
        "sections": [
            {
                "heading": "Two formats, different design goals",
                "paragraphs": [
                    "JPEG arrived in the nineties to make photographic images practical on the early web. WebP arrived decades later with modern entropy coding and optional transparency to shrink bytes further.",
                    "Both are lossy for typical photos. The difference is efficiency and ecosystem support, not whether one is real and the other is fake.",
                    "FileShrinkr supports both so you can empirically test rather than trust blanket advice. Your images, your audience, your bandwidth costs should drive the decision.",
                ],
            },
            {
                "heading": "File size at similar visual quality",
                "paragraphs": [
                    "In many benchmarks, WebP delivers twenty-five to thirty-five percent smaller files than JPG at comparable perceived quality on photographic content. Your mileage varies with grain, contrast, and sharp edges.",
                    "At very high qualities the gap narrows. At low qualities WebP sometimes holds edges better, sometimes introduces different artifact patterns. Eyes beat spreadsheets.",
                    "When migrating a media library, batch-convert a representative sample—skin tones, foliage, products, gradients—before committing site-wide.",
                ],
            },
            {
                "heading": "Browser and platform support",
                "paragraphs": [
                    "All major browsers today render WebP. The long tail of old Android WebViews and desktop IE is largely irrelevant for consumer sites but may matter in embedded enterprise apps.",
                    "Email clients are conservative. Gmail displays JPG reliably; WebP support in newsletters is inconsistent. Stick to JPG for attachments and many inline marketing images.",
                    "Use progressive enhancement on the web: WebP with JPG fallback via picture element or CDN content negotiation.",
                ],
            },
            {
                "heading": "Transparency and graphics",
                "paragraphs": [
                    "JPG never supports alpha. If you need soft edges on non-solid backgrounds, WebP or PNG is required. WebP often beats PNG size on photographic edges with transparency.",
                    "Flat logos with few colors may still be smallest as optimized PNG or SVG. WebP is not a universal PNG replacement for every graphic.",
                    "FileShrinkr lets you route screenshots and UI assets through PNG, WebP, or JPG depending on content after quick visual tests.",
                ],
            },
            {
                "heading": "Generation loss and editing workflows",
                "paragraphs": [
                    "Both formats suffer when you re-save repeatedly. Keep a lossless or high-quality master—often RAW or high-quality JPG—and generate WebP or JPG delivery copies on export.",
                    "Photo editors may default to JPG export. Add a WebP export pass through FileShrinkr before CMS upload to avoid plugin double-encoding.",
                    "For client deliverables, specify which format is canonical. Miscommunication here causes endless re-export requests.",
                ],
            },
            {
                "heading": "Practical decision matrix",
                "paragraphs": [
                    "Choose WebP for modern websites when you can serve fallbacks. Choose JPG for email attachments, maximum compatibility, and some print handoffs. Choose PNG or SVG for flat graphics and logos without photos.",
                    "When performance is critical and audience is mobile-heavy, lean WebP. When compliance mandates widest compatibility, lean JPG.",
                    "Re-evaluate yearly. Support and tooling evolve. FileShrinkr stays useful because it lets you switch formats without changing your entire pipeline—only the export setting.",
                ],
            },
            {
                "heading": "Real-world scenarios side by side",
                "paragraphs": [
                    "Newsletter hero: JPG at quality 75, twelve hundred pixels wide, EXIF stripped. Blog inline photo: WebP at quality 80 with JPG fallback, fourteen hundred pixels wide. Apparel thumbnail: WebP at quality 70, four hundred pixels square.",
                    "Running those three exports from the same master in FileShrinkr takes minutes and teaches more than abstract format debates. Numbers on a slider make sense once you see them on your own SKUs and headlines.",
                    "Document the winners in your team wiki so contractors and new hires do not relitigate JPG versus WebP on every project kickoff.",
                    "Neither format fixes bad lighting or motion blur. Start with a decent source photograph; format choice optimizes delivery, it does not rescue unusable captures.",
                    "Animated content is a separate conversation—GIF and video codecs follow different rules. For still photography on FileShrinkr, JPG and WebP cover the vast majority of publish paths you will encounter.",
                    "When stakeholders ask for proof, export byte sizes from both formats and present them beside screenshots at one hundred percent zoom. Empirical comparisons end format debates faster than opinion.",
                    "Archive a small test set—portrait, landscape, product on white, screenshot—and rerun JPG versus WebP yearly as encoders improve. Your presets should evolve with tooling, not freeze in 2018 defaults.",
                ],
            },
        ],
    },
    "how-to-reduce-image-size": {
        "slug": "how-to-reduce-image-size",
        "title": "How to Reduce Image File Size — Practical Guide | FileShrinkr",
        "description": "Step-by-step guide to reducing image file size for web, email, and chat. Learn resize, format choice, quality settings, and metadata stripping with FileShrinkr.",
        "h1": "How to Reduce Image File Size",
        "preset_format": None,
        "preset_quality": None,
        "show_widget": True,
        "related_slugs": ["compress-jpg", "resize-image", "compress-for-website"],
        "faqs": [
            {
                "q": "What is the fastest way to reduce image file size?",
                "a": "Resize to the display size you need, pick an efficient format like WebP or JPG, and compress at a quality level that looks good on your target device.",
            },
            {
                "q": "Does reducing quality always help?",
                "a": "Quality sliders help, but removing unnecessary pixels by resizing usually has a larger impact than sliding quality from 80 to 50.",
            },
            {
                "q": "Should I remove metadata to shrink files?",
                "a": "Stripping EXIF removes hidden camera data and saves a small amount of space. It is good practice for public web uploads.",
            },
            {
                "q": "Which tool do I need on my computer?",
                "a": "None. FileShrinkr runs in the browser with server-side processing—upload, adjust settings, download.",
            },
            {
                "q": "How do I avoid blurry results?",
                "a": "Compress once from the original, avoid extreme quality values, and view results at actual display size instead of extreme zoom.",
            },
        ],
        "howto_steps": [
            {
                "name": "Start from the best source",
                "text": "Use the highest-quality original you have, not a forwarded chat image that was already recompressed.",
            },
            {
                "name": "Resize to fit the use case",
                "text": "Open the editor tab if dimensions exceed what screens or email clients will show.",
            },
            {
                "name": "Pick format and quality",
                "text": "Use WebP or JPG for photos, PNG or WebP for transparency, PDF for multi-page documents.",
            },
            {
                "name": "Strip unnecessary metadata",
                "text": "Enable EXIF removal for web and messaging unless you need embedded tags.",
            },
            {
                "name": "Download and verify",
                "text": "Check file size and visual clarity at real viewing size before publishing or sending.",
            },
        ],
        "sections": [
            {
                "heading": "Why image file size still matters",
                "paragraphs": [
                    "Camera sensors grow while mobile data plans stay finite. Storage is cheap until you manage millions of product SKUs or a decade of blog archives. Every oversized image taxes CDNs, inboxes, and patience.",
                    "Reducing file size is not about destroying quality—it is about matching bytes to human perception. Most viewers never see your full-resolution upload; they see a scaled render in a browser or app.",
                    "FileShrinkr encodes that philosophy into a simple workflow anyone on your team can follow without specialist training.",
                ],
            },
            {
                "heading": "Step one: right-size your pixels",
                "paragraphs": [
                    "Measure the maximum display width and height your image will occupy. Multiply by two if you support retina displays. Export near that target, not at camera native resolution.",
                    "Blog content columns near seven hundred CSS pixels need sources around fourteen hundred pixels wide, not four thousand. Email inline images can be even smaller.",
                    "Use FileShrinkr's editor tab for geometry changes before compression. This single step prevents chasing diminishing returns with brutal quality sliders alone.",
                ],
            },
            {
                "heading": "Step two: choose an efficient format",
                "paragraphs": [
                    "Photos destined for websites should usually become WebP with JPG fallback. Photos for email should usually become JPG. Graphics with transparency need WebP or PNG.",
                    "Avoid PNG for casual photographs. The lossless encoding balloon is immediate and severe.",
                    "For stacks of scans or forms, merge to PDF with compressed embedded images instead of emailing twelve separate files.",
                ],
            },
            {
                "heading": "Step three: compress with intention",
                "paragraphs": [
                    "Move the quality slider while previewing on the device class your audience uses. A quality that looks fine on a desk monitor might band on a phone OLED at low brightness.",
                    "Batch similar images with the same preset for consistent galleries. Document your presets internally—hero 80 WebP, thumbnail 70 JPG, and so on.",
                    "Compress once per delivery generation. Repeated saves accumulate ugly artifacts, especially in skies and skin.",
                ],
            },
            {
                "heading": "Step four: clean metadata",
                "paragraphs": [
                    "EXIF blocks store camera settings, timestamps, and sometimes GPS. They are invisible to viewers but add bytes and privacy risk.",
                    "FileShrinkr can strip EXIF on export. Keep archival originals with metadata in a private folder if needed for your photography workflow.",
                    "Metadata removal is not redaction. Blur sensitive content explicitly when required.",
                ],
            },
            {
                "heading": "Step five: measure and iterate",
                "paragraphs": [
                    "Note file size before and after. Aim for targets tied to your channel—under three hundred kilobytes for heroes, under one megabyte per email batch, and so on.",
                    "Use Lighthouse or WebPageTest on key URLs after replacing images. Field metrics in Search Console show whether real users benefit.",
                    "When in doubt, compress slightly more than feels necessary and ask a colleague to compare blindly. You will calibrate faster than staring at hex file sizes alone.",
                ],
            },
            {
                "heading": "Common mistakes to avoid",
                "paragraphs": [
                    "Uploading camera originals without resize is the most common error. Chasing tiny savings by lowering quality to forty while leaving four-K dimensions is the second.",
                    "Forwarding WhatsApp or Messenger images as sources guarantees poor results. Return to the original file or ask the sender for it.",
                    "Relying on CMS upload alone without optimization assumes the platform will fix your habits. It will not—habits plus FileShrinkr will.",
                ],
            },
            {
                "heading": "Build a personal compression checklist",
                "paragraphs": [
                    "Before every publish or send: confirm source quality, resize to slot, pick format, set quality, strip EXIF if public, verify at display size, note final kilobytes. That checklist becomes automatic after a dozen runs.",
                    "FileShrinkr maps directly to those steps. Keep the site bookmarked next to your CMS tab so optimization stays as habitual as spell-check.",
                    "When you teach teammates, show one before-and-after example from your own content. Concrete savings convince faster than policy memos about Core Web Vitals.",
                    "Keep a folder of approved before-and-after examples labeled by channel—email, web hero, chat—to onboard freelancers without repeating the same quality lecture every hire.",
                ],
            },
        ],
    },
}


def get_landing(slug):
    return LANDING_PAGES.get(slug)


def all_landing_slugs():
    return list(LANDING_PAGES.keys())
