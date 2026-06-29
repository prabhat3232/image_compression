"""Editorial guides for FileShrinkr — long-form how-to content."""

GUIDES = {
    "resize-photos-for-government-exam-forms": {
        "slug": "resize-photos-for-government-exam-forms",
        "title": "How to Resize Photos for Government Exam Forms",
        "description": (
            "Resize and compress passport-style photos for SSC, UPSC, railway, and state "
            "recruitment portals. Meet pixel dimensions, JPG format, and 20–100 KB file-size limits."
        ),
        "sections": [
            {
                "heading": "Why exam portals reject your photo",
                "paragraphs": [
                    "Government and public-sector application forms rarely accept the photo straight from your phone. Portals enforce maximum file size in kilobytes, fixed width and height in pixels, JPG format only, and sometimes rules about background color, face visibility, or aspect ratio. A five-megabyte iPhone HEIC or a four-thousand-pixel-wide JPEG will fail before your application is even reviewed.",
                    "Rejections are frustrating because the error message is often vague—\"invalid image\" or \"file size exceeded\"—without telling you whether the problem is dimensions, format, or bytes. The fix is almost always the same: crop to the required frame, resize to the listed pixel size, export as JPG, and compress until the file falls under the portal's KB cap while the face stays sharp.",
                    "FileShrinkr is built for this workflow. Use the Image Editor to crop and resize, then compress with a target file size preset (20 KB, 100 KB, or 500 KB) or custom width and height on the compressor. Server mode handles iPhone HEIC uploads and optional EXIF removal; Browser mode can process JPG privately when your connection or privacy preferences matter.",
                ],
            },
            {
                "heading": "Read the notification before you edit",
                "paragraphs": [
                    "Every exam—SSC CGL, UPSC civil services, railway RRB, state PSC, police recruitment, teaching eligibility tests—publishes its own photo specification in the official notification or on the upload screen. Copy those numbers exactly: width × height in pixels, maximum file size in KB, allowed format (almost always JPG or JPEG), and any notes on background (white, light blue) or ears visibility.",
                    "Do not rely on blog posts or year-old YouTube tutorials. Requirements change between cycles. A size that worked for last year's form may be rejected this year if the commission lowered the KB limit or changed dimensions from 3.5 × 4.5 cm equivalents to a specific pixel box such as 200 × 230 or 240 × 320.",
                    "Keep the official PDF or screenshot of the upload instructions beside you while editing. FileShrinkr's custom width and height fields let you match pixel requirements precisely after you crop the subject in the editor tab.",
                ],
            },
            {
                "heading": "Typical requirements you will see",
                "paragraphs": [
                    "File size caps of 20 KB, 50 KB, or 100 KB are common on Indian government portals. Twenty kilobytes is tight for a portrait but achievable when you resize first and let FileShrinkr's target KB mode find the highest acceptable quality under that ceiling. If the portal allows 100 KB, you have more room for facial detail—use the 100 KB preset instead of over-compressing.",
                    "Dimension rules usually describe a passport-style head-and-shoulders frame. Portals may list centimeters (3.5 × 4.5 cm) or pixels (for example 200 × 230, 350 × 450, or 600 × 800). Centimeter labels are print-oriented; online forms validate pixels. When only centimeters are given, use the pixel values shown on the same page—if none are listed, match the pixel box the upload preview displays when you select a file.",
                    "Format is almost always JPG or JPEG. PNG, WEBP, and HEIC are typically rejected. Signature uploads are separate and often have even smaller KB limits; the same resize-then-compress workflow applies. Enable Remove EXIF in Server mode if you want to strip camera metadata before submission.",
                ],
            },
            {
                "heading": "Step 1 — Crop and resize in the editor",
                "paragraphs": [
                    "Open FileShrinkr and switch to the Image Editor tab. Upload your passport-style photo or take a well-lit picture against a plain light background. Use crop to frame head and shoulders with a little space above the head, matching the aspect ratio implied by the form's width and height.",
                    "Set explicit width and height in the resize controls if the editor exposes them, or note the target pixels for the compressor step. Straighten slightly tilted photos with rotate. Avoid heavy filters or beauty modes—portals want a natural, recognizable face. If the notification forbids shadows or hats, fix those before export; compression cannot fix policy violations.",
                    "When you are satisfied, click Compress This Image to send the edited canvas to the compressor without re-uploading. That handoff keeps one consistent crop from edit through final JPG export.",
                ],
            },
            {
                "heading": "Step 2 — Export JPG and hit the KB limit",
                "paragraphs": [
                    "On the compressor tab, choose Server mode if you uploaded HEIC from an iPhone or need EXIF removal. Select JPG as the output format. Enter the exact width and height from the form, or use a resize preset only if it matches the notification—Instagram presets are for social media, not SSC uploads.",
                    "Turn on the target file size option and pick the KB cap from the form: 20 KB, 100 KB, or 500 KB as available. FileShrinkr searches for the best quality at or below that size. If the portal limit is 50 KB and no preset matches, start with 100 KB and lower quality manually, or use 20 KB and verify visually—sometimes slightly higher quality at 100 KB still passes if the portal rounds generously.",
                    "Use the before/after preview to confirm the face is not blurry or blocky. If eyes or text on a nameplate look soft, resize to the correct pixels first, then retry with a slightly higher KB allowance if the rules permit. Download the final JPG and check the file properties on your computer: size in KB and image dimensions should match the form.",
                ],
            },
            {
                "heading": "Step 3 — Verify before you upload",
                "paragraphs": [
                    "Open the JPG locally at one hundred percent zoom. Confirm ears, chin, and hair boundaries match the notification. Upload a test file if the portal allows replacing the photo before payment. Some systems lock the image after fee submission.",
                    "Rename the file if the form requires a specific pattern (for example registration number.jpg). Avoid spaces and special characters in filenames; underscores or hyphens are safer on older government servers.",
                    "If upload still fails, compare your file's KB and pixel dimensions character by character against the instructions. One pixel over or one kilobyte over often triggers rejection. Re-export with stricter target KB or one pixel less on width and height.",
                ],
            },
            {
                "heading": "Signatures, SC/ST certificates, and multi-page scans",
                "paragraphs": [
                    "Signature images usually need a small pixel box and a very low KB cap—often under 20 KB. Crop tightly around the ink, use JPG, and apply the 20 KB target. White background scans compress better than grey paper photos.",
                    "When a form asks for identity proofs or caste certificates as separate uploads, each file may have its own limit. Process them one at a time rather than batching unlike sizes. For multiple page scans that must be one document, see our guide on merging images into PDF—but photo and signature slots almost always want standalone JPGs, not PDF.",
                    "FileShrinkr batch ZIP is useful when several family members need the same treatment for different exams, not when one form wants five different dimension rules in one submission.",
                ],
            },
            {
                "heading": "Quick checklist for exam applicants",
                "paragraphs": [
                    "Confirm official width × height pixels and max KB from the current notification. Crop passport-style in the editor; straighten and use a plain background. Export JPG; use target KB matching the form. Preview face sharpness; strip EXIF in Server mode if desired. Verify file size and dimensions on disk before paying the application fee.",
                    "Bookmark FileShrinkr on your phone and desktop during application season. Deadlines cluster on the last day; having a reliable resize-and-compress tool avoids panic trips to cyber cafés.",
                    "For general compression theory and quality trade-offs, read our guides on compressing without losing quality and preparing images for email—the same principles apply, but exam forms are stricter about dimensions than most email clients.",
                ],
            },
        ],
        "related_slugs": [
            "compress-without-losing-quality",
            "prepare-images-for-email",
            "image-dpi-and-resolution",
            "merge-images-into-pdf",
        ],
    },
    "compress-without-losing-quality": {
        "slug": "compress-without-losing-quality",
        "title": "How to Compress Images Without Losing Quality",
        "description": (
            "Learn practical techniques to shrink JPG, PNG, WEBP, and HEIC file sizes while keeping photos sharp. "
            "Covers AVIF export, target KB sizes (20–500 KB), quality settings, and lossless PNG or PDF options."
        ),
        "sections": [
            {
                "heading": "Why compression and quality feel like opposites",
                "paragraphs": [
                    "Every image on your phone or camera starts as a large file packed with pixel data. When you upload that photo to a website, attach it to an email, or share it on WhatsApp, the platform or recipient often needs something smaller. Compression reduces file size by removing or reorganizing data. The challenge is that aggressive compression can introduce blur, blocky artifacts, or muddy colors that make a professional photo look amateur.",
                    "The good news is that most everyday images contain far more data than human eyes can appreciate at typical screen sizes. A twelve-megapixel vacation shot might look identical on a laptop at eighty percent quality versus one hundred percent, yet the smaller file loads faster and costs less bandwidth. The trick is knowing which levers to pull—format, dimensions, quality percentage, and metadata—so you shrink the file without visibly damaging the subject.",
                    "FileShrinkr gives you those levers in one place. Compress to JPG, WEBP, AVIF, or PNG with an adjustable quality slider or target file size (20–500 KB), use Instagram and social resize presets, export merged PDFs with optional lossless embedding, and crop or resize in the built-in editor before compression. Browser mode processes many formats privately on your device; server mode handles HEIC, PDF, and full EXIF removal.",
                ],
            },
            {
                "heading": "Start with the right dimensions",
                "paragraphs": [
                    "Before you touch the quality slider, ask whether the image needs to be as large as it is. A photo captured at four thousand pixels wide will produce a hefty file even at moderate quality. If the image will appear in a blog sidebar at six hundred pixels, scaling it down first removes millions of pixels that nobody would ever see. That alone can cut file size by seventy percent or more with zero perceptible loss on the target display.",
                    "Web designers often target maximum widths between twelve hundred and nineteen hundred pixels for hero images, and far less for thumbnails. Email attachments benefit from even smaller dimensions because many clients display images inline at modest sizes. Social platforms apply their own scaling, so sending a four-thousand-pixel image to Instagram or Facebook simply wastes bytes.",
                    "Use FileShrinkr's editor tab to crop distracting edges or resize to a sensible maximum before compression. Combining a reasonable width with format-specific compression yields smaller files than cranking quality to the lowest setting on an oversized original. Think of resolution as the first and often most effective compression step.",
                ],
            },
            {
                "heading": "Choose the format that matches your content",
                "paragraphs": [
                    "JPEG remains the default for photographs because it excels at compressing smooth color gradients and natural scenes. PNG preserves sharp edges and transparency but produces larger files for photos. WEBP offers a modern balance: typically twenty-five to thirty-five percent smaller than JPEG at equivalent visual quality, with broad browser support today. Picking the wrong format is a common reason people either overshoot file size or destroy image quality.",
                    "Use JPG or WEBP for camera photos, portraits, landscapes, and any image without transparency. Reserve PNG when you need a crisp logo, screenshot with text, or an icon with a transparent background. Avoid saving a busy photograph as PNG unless you have a specific reason; the file will balloon while looking no better than a well-tuned WEBP.",
                    "On FileShrinkr, select JPG for maximum compatibility with older systems and email clients. Choose WEBP when you control the delivery environment—your own website, a modern app, or internal documentation. The quality slider behaves similarly for both formats, but WEBP often wins on size at the same visual result.",
                ],
            },
            {
                "heading": "Dial in quality with a visual check",
                "paragraphs": [
                    "Quality settings map to how aggressively a lossy encoder discards detail. At one hundred percent you get minimal compression; at fifty percent you may see banding in skies and softness in hair. Most web photos look excellent between seventy-five and eighty-five percent. Marketing hero images might justify eighty-five to ninety, while thumbnails and background textures can drop to sixty-five without complaint.",
                    "Always judge quality at the size and context where the image will appear. Zooming to pixel level on a five-thousand-pixel original will reveal artifacts that disappear when the image is displayed at eight hundred pixels wide on a phone. Compare the compressed preview against the original at realistic dimensions rather than at full resolution.",
                    "FileShrinkr processes images with Pillow (and optional MozJPEG for JPG on the server) or in your browser when private mode is enabled. Download results and compare with the built-in before/after preview. If artifacts appear, bump quality up five or ten points, lower the target KB, or resize first—then compress again.",
                ],
            },
            {
                "heading": "When lossless and near-lossless options matter",
                "paragraphs": [
                    "Some workflows cannot tolerate any re-encoding. Legal scans, medical imaging references, or brand assets headed to print may need every pixel preserved. In those cases, lossy JPG compression is the wrong tool. Instead, keep originals archived and only distribute copies that meet the delivery requirement—sometimes that means PNG or TIFF, sometimes a PDF with embedded images at full resolution.",
                    "FileShrinkr's PDF export supports two paths. With compression enabled, images are optimized for smaller PDFs suitable for email and web. With compression disabled, img2pdf embeds originals without re-encoding, producing a lossless PDF ideal for document archives or print shops that will handle their own optimization. Merging multiple scans into one PDF with the lossless option preserves each page exactly as uploaded.",
                    "Lossless compression formats like PNG still reduce file size by encoding redundancy more efficiently, but they will not match the byte savings of lossy JPG or WEBP on photographs. Choose lossless when fidelity is mandatory; choose lossy when human viewers are the final audience and loading speed matters.",
                ],
            },
            {
                "heading": "Strip metadata and batch consistently",
                "paragraphs": [
                    "Digital photos often carry EXIF metadata: GPS coordinates, camera model, timestamps, and embedded thumbnails. This hidden data can add tens or hundreds of kilobytes per file without contributing to what viewers see. Removing metadata is a safe way to shrink size slightly and reduce privacy exposure when sharing photos publicly.",
                    "Consistency matters when you compress a gallery or product catalog. Mixed quality levels make some images look soft while others look harsh. Pick a baseline—WEBP at eighty percent for product shots, JPG at seventy-five for blog inline images—and apply it across the set. Uniform processing also simplifies caching and layout because file sizes cluster predictably.",
                    "FileShrinkr's batch upload accepts multiple files, applies your chosen format and quality, and packages results in a ZIP when you need many downloads at once. For PDF workflows, merge mode combines images into a single document in upload order, which is ideal for scanned receipts, portfolio pages, or photo albums. Start with sensible dimensions, pick the right format, tune quality with a real preview, and reserve lossless PDF export for the cases that truly require it—that workflow keeps files small and images sharp.",
                ],
            },
        ],
        "related_slugs": [
            "resize-photos-for-government-exam-forms",
            "best-image-format-for-websites",
            "image-dpi-and-resolution",
            "prepare-images-for-email",
            "merge-images-into-pdf",
        ],
    },
    "best-image-format-for-websites": {
        "slug": "best-image-format-for-websites",
        "title": "Best Image Format for Websites: JPG vs WEBP vs AVIF vs PNG",
        "description": (
            "Compare JPG, WEBP, AVIF, PNG, and SVG for web publishing. Learn which format fits photos, "
            "logos, transparency, HEIC sources, and performance goals on modern sites."
        ),
        "sections": [
            {
                "heading": "What web images need to accomplish",
                "paragraphs": [
                    "A website image must load quickly, look correct on phones and desktops, and fit the design without breaking layout. Slow images hurt Core Web Vitals, especially Largest Contentful Paint, which Google uses as a ranking signal. Oversized PNG photographs and unoptimized hero banners are among the most common reasons a otherwise fast site feels sluggish.",
                    "Format choice is the foundation of that performance story. Each format uses different compression math, color models, and feature sets. Picking the right one for each asset type—photo versus logo versus illustration—often matters more than tweaking a quality slider on the wrong format.",
                    "FileShrinkr supports JPG, WEBP, AVIF, PNG, and PDF export from uploaded JPG, PNG, WEBP, HEIC, and SVG sources, so you can produce web-ready assets without installing desktop software. Understanding when to use each output format helps you compress once and publish confidently.",
                ],
            },
            {
                "heading": "JPEG: the workhorse for photographs",
                "paragraphs": [
                    "JPEG uses lossy compression tuned for continuous-tone images like portraits, product photos, and scenery. Nearly every browser, email client, and CMS accepts it without conversion. That universal compatibility makes JPG the safest default when you do not control the full delivery chain or when you need assets for mixed environments.",
                    "JPEG does not support transparency. Any soft edges or cut-out subjects require a flat background color before export. It also struggles with crisp text and hard edges; screenshots and UI captures saved as JPG often look fuzzy compared to PNG. For photos without transparency, though, JPG at seventy-five to eighty-five percent quality typically beats PNG on size while looking equally good on screen.",
                    "Use FileShrinkr's JPG output when feeding images into legacy templates, Word documents, slide decks, or third-party marketplaces that mandate JPEG. Enable MozJPEG in server mode for sharper JPGs at the same file size. The compressor scales wide images, applies social presets, and encodes with your quality or target KB setting.",
                ],
            },
            {
                "heading": "WEBP: modern efficiency for the open web",
                "paragraphs": [
                    "WEBP combines lossy and lossless modes and generally delivers smaller files than JPEG at comparable visual quality. Google, Shopify, and most modern frameworks recommend WEBP for photographic content served on the web. Safari, Chrome, Firefox, and Edge all support it today, which removes the main historical barrier to adoption.",
                    "Lossy WEBP excels for hero images, blog featured images, and gallery thumbnails. Lossless WEBP can replace PNG for some graphics, though complex illustrations with transparency may still favor PNG. WEBP also supports transparency, giving it an advantage over JPG for cut-out product shots when you want smaller files than PNG provides.",
                    "On FileShrinkr, select WEBP as the output format and adjust quality similarly to JPG. Export WEBP for assets you place on your own site through a CMS or static generator. Pair WEBP with a JPG fallback only if analytics show meaningful traffic from very old browsers—an increasingly rare requirement.",
                ],
            },
            {
                "heading": "PNG and SVG: graphics, logos, and icons",
                "paragraphs": [
                    "PNG uses lossless compression and supports full alpha transparency. It is the right choice for logos, icons, diagrams, and screenshots where sharp lines matter. Photographs saved as PNG become unnecessarily large; a three-megabyte PNG beach photo might shrink to three hundred kilobytes as WEBP with no visible loss on a laptop screen.",
                    "SVG stores vector paths rather than pixels, making it ideal for icons, simple illustrations, and logos that must scale across breakpoints without multiple raster sizes. SVG files are tiny for simple shapes and stay crisp at any resolution. Complex SVGs with filters or embedded bitmaps can grow heavy, and SVG is not appropriate for photographs.",
                    "When you upload SVG to FileShrinkr, the tool rasterizes it for JPG, WEBP, AVIF, PNG, or PDF output at appropriate dimensions. Keep original SVGs for inline site markup, and use FileShrinkr when you need a raster thumbnail, a compressed WEBP or AVIF variant, or a PDF sheet of vector-derived images for print or sharing.",
                ],
            },
            {
                "heading": "Decision matrix for common web scenarios",
                "paragraphs": [
                    "For blog featured photos and marketing heroes, prefer WEBP at eighty percent quality; fall back to JPG when a partner platform rejects WEBP. For product catalog photos on white backgrounds, WEBP or JPG works; use WEBP with transparency only if the cut-out is essential. For UI screenshots and documentation, PNG remains king. For navigation icons and brand marks, SVG in the HTML with a PNG fallback for email templates.",
                    "E-commerce sites often mix formats: SVG logos, WEBP product galleries, and PNG for badges that need transparency without photographic content. Content management systems increasingly auto-convert uploads to WEBP at the CDN layer, but starting with a well-compressed source file reduces double-encoding artifacts.",
                    "FileShrinkr lets you process the same source batch to JPG and WEBP separately if you want side-by-side comparisons. Compress once at the target quality, download, and upload to your host rather than relying on the CMS to crunch already-huge originals. Smaller sources compress faster and more predictably downstream.",
                ],
            },
            {
                "heading": "Performance habits beyond format choice",
                "paragraphs": [
                    "Format alone does not fix a four-thousand-pixel-wide image displayed at six hundred pixels. Resize to the maximum display width, compress at appropriate quality, and serve responsive variants if your stack supports srcset. Lazy-loading below-the-fold images prevents bandwidth contention with critical CSS and JavaScript.",
                    "Name files descriptively, set width and height attributes to reduce layout shift, and cache aggressively at the CDN. Measuring real-user LCP with field data beats guessing from synthetic lab tests. When LCP elements are images, shrinking the hero file is often the cheapest performance win available.",
                    "Use FileShrinkr as the first step in your publishing pipeline: resize in the editor if needed, export WEBP or JPG at tuned quality, and merge sets into PDF only when the deliverable is a document rather than inline HTML. Matching format to content type, then applying sensible dimensions and quality, gives you fast pages that still look professional.",
                ],
            },
        ],
        "related_slugs": [
            "compress-without-losing-quality",
            "image-dpi-and-resolution",
            "prepare-images-for-email",
            "merge-images-into-pdf",
        ],
    },
    "merge-images-into-pdf": {
        "slug": "merge-images-into-pdf",
        "title": "How to Merge Images into One PDF",
        "description": (
            "Step-by-step guidance for combining JPG, PNG, WEBP, and HEIC images into a single PDF. "
            "Covers merge order, compressed versus lossless export, and practical use cases."
        ),
        "sections": [
            {
                "heading": "Why merge images into a PDF",
                "paragraphs": [
                    "A single PDF is easier to email, archive, and print than a folder of loose JPEGs. Insurance claims, rental applications, school forms, and design approvals often specify one attachment. PDFs preserve page order, display consistently across devices, and open without requiring viewers to hunt through multiple downloads.",
                    "Photographers and creatives merge contact sheets or portfolio spreads. Small businesses combine scanned receipts for monthly bookkeeping. Teachers bundle worksheet photos into one handout file. The pattern is the same: multiple raster images need to become one portable document without unnecessary quality loss.",
                    "FileShrinkr supports PDF export for individual images and merge mode that combines an entire batch into one file. You can choose compressed PDFs for smaller attachments or lossless embedding when fidelity matters. No desktop Acrobat license or command-line tools required.",
                ],
            },
            {
                "heading": "Prepare your images before merging",
                "paragraphs": [
                    "Order matters. PDF pages follow the upload sequence, so rename files with numeric prefixes—01-cover.jpg, 02-diagram.jpg—if your browser or OS sorts alphabetically. Rotate misaligned phone photos in FileShrinkr's editor before export so recipients do not tilt their heads reading scanned documents.",
                    "Crop excess margins on scans to keep pages visually consistent. Mixed portrait and landscape images will each occupy a full page; consider rotating landscape scans to portrait orientation if you want uniform printing on standard paper. Extremely wide panoramas may leave large white borders when centered on a PDF page—that is normal unless you crop first.",
                    "Check that each source file is readable at intended size. Blurry uploads stay blurry in PDF; compression cannot recover focus. For text-heavy scans, ensure adequate resolution—roughly fifteen hundred pixels on the long edge is a practical minimum for readable body text when printed.",
                ],
            },
            {
                "heading": "Compressed PDF export for sharing",
                "paragraphs": [
                    "When file size limits matter—email gateways, municipal portals, or mobile uploads—enable image compression during PDF creation. FileShrinkr scales wide images to a sensible maximum and applies your quality setting before embedding pages. The result is a PDF far smaller than lossless embedding would produce, often small enough for Gmail's twenty-five megabyte limit even with dozens of phone photos.",
                    "Compressed PDFs trade some fine detail for bytes. That trade is acceptable for proof approvals, sharing vacation albums with family, or submitting utility bill photos to a landlord. Text in scans remains legible when the source resolution was reasonable. Continuous-tone photos show minor softness only if you set quality aggressively low.",
                    "Select PDF as the output format, enable merge, and leave compression on—the default path for most sharing scenarios. Tune the quality slider: seventy for aggressive size reduction, eighty for balanced results, ninety when you need near-original photo appearance. Download the merged PDF and verify a few pages before sending.",
                ],
            },
            {
                "heading": "Lossless PDF export for archival quality",
                "paragraphs": [
                    "Some workflows forbid re-encoding. Print shops, legal archives, and brand compliance teams may require pixels identical to the uploaded scan. FileShrinkr's lossless PDF path uses img2pdf to embed original image bytes without JPEG recompression, preserving each file exactly as uploaded within a standard PDF container.",
                    "Lossless PDFs are larger. A set of high-resolution phone scans might exceed email limits, so plan to use cloud links or file-sharing services when choosing this option. The benefit is zero encoder artifacts and predictable color for professionals who will process the file downstream.",
                    "Disable image compression when exporting PDF on FileShrinkr to activate the lossless path. Merge still combines all uploads in order. Use this for engineering drawings exported as PNG, camera RAW conversions already at full quality, or signed contracts where every pixel might matter legally.",
                ],
            },
            {
                "heading": "Individual PDFs versus one merged file",
                "paragraphs": [
                    "FileShrinkr lets you export each image as its own PDF or merge everything into one document. Individual PDFs suit workflows where recipients import pages into separate systems—one invoice per PDF into accounting software, for example. Merged PDFs suit human readers who want linear navigation with scroll or page thumbnails.",
                    "If you need both, run the batch twice: once without merge for per-file PDFs archived locally, once with merge for distribution. Batch ZIP download packages multiple compressed JPG or WEBP outputs when PDF is not required, which is faster for web publishing pipelines.",
                    "Remember that PDF is a container, not a magic compressor. Embedding ten uncompressed PNG screenshots can still produce a huge file even in merge mode. Pre-process screenshots to JPG or WEBP when lossless embedding is not required.",
                ],
            },
            {
                "heading": "Troubleshooting common merge issues",
                "paragraphs": [
                    "If the PDF refuses to upload elsewhere, check total size against the destination limit. Re-export with lower quality or fewer pages per batch. If colors look wrong, confirm whether the source used wide-gamut profiles; converting to sRGB in an editor before upload can stabilize appearance across viewers.",
                    "Blank pages usually mean a corrupted source file or an unsupported intermediate format—try re-saving the image as JPG before upload. Upside-down pages mean rotation metadata was ignored; rotate explicitly in the editor rather than relying on EXIF orientation alone.",
                    "FileShrinkr processes files server-side and returns a download link for the merged PDF or ZIP. For repeatable document bundles—monthly expense scans, onboarding packets, coursework submissions—keep a folder template with numbered filenames and a saved quality preset. Merge images to PDF once, verify, and send; recipients get a professional single attachment instead of an scattered image dump.",
                ],
            },
        ],
        "related_slugs": [
            "prepare-images-for-email",
            "compress-without-losing-quality",
            "best-image-format-for-websites",
            "image-dpi-and-resolution",
        ],
    },
    "prepare-images-for-email": {
        "slug": "prepare-images-for-email",
        "title": "How to Prepare Images for Email Attachments",
        "description": (
            "Shrink photos and scans to fit Gmail, Outlook, and corporate email limits. "
            "Target KB presets, dimensions, and format choice before you hit send."
        ),
        "sections": [
            {
                "heading": "Email limits are stricter than you think",
                "paragraphs": [
                    "Gmail allows roughly twenty-five megabytes per message including encoding overhead, which means your attachments should stay comfortably below twenty megabytes to avoid silent failures or bounced sends. Outlook and Microsoft 365 impose similar limits, often twenty to thirty-five megabytes depending on tenant policy. Mobile carriers and corporate gateways may cut far lower—ten megabytes or less—when scanning attachments for security.",
                    "Recipients on phones pay data charges for large downloads and may not open multi-megabyte images at all. Even when a message delivers successfully, huge inline images slow conversation threads and fill mailbox quotas. Preparing images before attaching them is courtesy and reliability engineering in one step.",
                    "FileShrinkr helps you hit safe targets quickly: compress to JPG, WEBP, AVIF, or PNG with target KB presets (20–500 KB), merge multiple scans into one PDF, and download a ZIP of batch-processed files. You see results before opening your mail client, which beats discovering a send failure after composing a long message.",
                ],
            },
            {
                "heading": "Set size and dimension targets",
                "paragraphs": [
                    "For a handful of casual photos, aim for one hundred to three hundred kilobytes per image at roughly sixteen hundred pixels on the long edge. That keeps a ten-photo gallery under three megabytes with room for message text. For document scans, five hundred kilobytes per page is usually plenty when text is the priority.",
                    "When total attachment budget is fixed—say eight megabytes for a conservative corporate gateway—divide by the number of files and compress to meet that per-file ceiling. PDF merge helps: ten scans as individual JPGs might inflate metadata and headers; one merged PDF often packages the same content with less overhead and simpler recipient experience.",
                    "Use FileShrinkr's editor to downscale images that exceed your pixel targets before compression. A four-thousand-pixel phone photo compressed to eighty percent quality may still exceed a three-hundred-kilobyte goal; resizing to sixteen hundred pixels first makes the quality slider effective again.",
                ],
            },
            {
                "heading": "Choose JPG, WEBP, AVIF, PNG, or PDF for email",
                "paragraphs": [
                    "JPG is the safest format for photo attachments because every mail client displays it inline without plugins. WEBP is smaller but some desktop clients still treat it as a generic attachment rather than a previewable image. When you know recipients use modern Gmail or Apple Mail, WEBP can shave another twenty percent off size; otherwise default to JPG for broad compatibility.",
                    "PDF works best for multi-page scans, forms, and mixed aspect ratios that should print on standard paper. One PDF attachment beats five separate images in a professional context. Enable compression on FileShrinkr unless the recipient explicitly requires lossless archival quality.",
                    "Avoid PNG for email photographs; file sizes balloon without visual benefit. PNG remains appropriate for small logos embedded in signatures, not for camera roll exports. SVG is rarely useful as an attachment—rasterize to JPG if you need universal preview.",
                ],
            },
            {
                "heading": "Quality settings that preserve readability",
                "paragraphs": [
                    "Email photos rarely need print-grade fidelity. Quality seventy to seventy-five keeps skin tones smooth and landscapes attractive at phone screen sizes. Drop to sixty-five for secondary images or when you must squeeze an extra file into the same total budget. Raise to eighty only for hero images where detail is part of the message—product shots for a client approval, for example.",
                    "Scanned text demands sharper settings than scenery. Start at eighty quality and verify that small fonts remain crisp. If artifacts appear in letterforms, increase quality or resolution slightly rather than accepting blurry paragraphs. Rotated or skewed scans should be corrected in the editor before compression so OCR tools downstream read them cleanly.",
                    "FileShrinkr applies your quality choice consistently across batch uploads, which helps when you attach twelve similar receipt photos. Uniform processing prevents one random oversized file from breaking an otherwise compliant message.",
                ],
            },
            {
                "heading": "Privacy and metadata considerations",
                "paragraphs": [
                    "Photos embed EXIF metadata: GPS location, device identifiers, and capture timestamps. Sharing images by email can unintentionally reveal where and when you took them. Stripping metadata before send reduces privacy risk and removes bytes. Even when location is not sensitive, cleaner files look more professional.",
                    "Corporate policies may prohibit certain attachment types or require encryption for confidential scans. Compression does not replace encryption, but smaller files encrypt and upload faster to secure portals. Know your organization's rules before batching HR or medical images.",
                    "When metadata removal is part of your workflow, enable EXIF stripping in Server mode on FileShrinkr before you compress JPG, WEBP, or AVIF exports. That removes GPS, camera, and timestamp data while shrinking file size for safer public sharing.",
                ],
            },
            {
                "heading": "Workflow checklist before you send",
                "paragraphs": [
                    "Rename files descriptively—invoice-march-electric.pdf beats IMG_4092.jpg in a client's inbox. Confirm total attachment size in your file explorer before composing. Open the compressed PDF or JPG locally to verify orientation, crop, and legibility. If using merge, scroll through every page once; one upside-down scan is a common preventable embarrassment.",
                    "For recurring sends—weekly field reports, property listings, classroom updates—save a FileShrinkr preset mentally: sixteen hundred pixel max width, JPG at seventy-five, merge scans to PDF. Repeatable habits beat relearning limits every time.",
                    "When a message still exceeds limits after compression, split into two emails with clear subject lines or upload a cloud link for the overflow. FileShrinkr gets you most of the way; knowing when to split rather than over-compress preserves quality for recipients who genuinely need it.",
                ],
            },
        ],
        "related_slugs": [
            "resize-photos-for-government-exam-forms",
            "merge-images-into-pdf",
            "compress-without-losing-quality",
            "best-image-format-for-websites",
            "image-dpi-and-resolution",
        ],
    },
    "image-dpi-and-resolution": {
        "slug": "image-dpi-and-resolution",
        "title": "Understanding Image DPI and Resolution for Web",
        "description": (
            "Clarify pixels versus DPI, what resolution matters on screens versus print, "
            "and how to export web images that look sharp without wasting bandwidth."
        ),
        "sections": [
            {
                "heading": "Pixels are real; DPI is metadata",
                "paragraphs": [
                    "Digital images are grids of pixels—colored dots on a screen. Resolution in web context usually means pixel dimensions: nineteen twenty by ten eighty, eight hundred by six hundred, and so on. DPI, dots per inch, describes how densely those pixels would print on paper. A three-thousand-pixel-wide image set to seventy-two DPI or three hundred DPI contains the same pixel data and looks identical on a monitor.",
                    "Changing DPI without resampling does not change file size or on-screen appearance. Software that exports screenshots at seventy-two DPI versus ninety-six DPI is mostly labeling the file, not altering detail. Confusion arises because print workflows use DPI to calculate physical size: three thousand pixels at three hundred DPI maps to ten inches wide on paper.",
                    "For FileShrinkr users, focus on pixel width and height first. The compressor scales very wide images to a practical maximum for web delivery. DPI metadata in a JPG exported for email or websites rarely affects how recipients view the file in browsers or mail clients.",
                ],
            },
            {
                "heading": "What resolution screens actually need",
                "paragraphs": [
                    "Most laptop screens display content around one thousand to two thousand pixels wide depending on device and scaling. Mobile phones fit readable layouts in three hundred to four hundred CSS pixels width even when the physical display has more pixels through device pixel ratio. Serving a four-thousand-pixel image when the CSS box is six hundred pixels wastes bandwidth because the browser downscales anyway.",
                    "Retina or high-DPI displays benefit from roughly two times the CSS pixel dimensions for crispness—an eight hundred pixel wide slot might use a sixteen hundred pixel source. Beyond that multiplier, extra pixels seldom improve perceived sharpness for photographs. Vector SVG icons sidestep the problem entirely for simple graphics.",
                    "When preparing images in FileShrinkr, resize in the editor to twice your layout width for photos, or match exact pixel dimensions for thumbnails and cards. Then compress at seventy-five to eighty-five quality. That pairing delivers sharp results without overshooting file size goals.",
                ],
            },
            {
                "heading": "Print resolution versus web resolution",
                "paragraphs": [
                    "Print shops often request three hundred DPI at the intended physical dimensions. A five-by-seven inch print at three hundred DPI needs fifteen hundred by twenty-one hundred pixels. Web banners measured in pixels do not need three hundred DPI metadata if pixel dimensions already match the display slot.",
                    "If someone asks for a high-resolution file, clarify whether they mean more pixels or different DPI metadata. Photographers exporting for clients should supply sufficient pixels for the largest print size promised—often twenty-four hundred to four thousand pixels on the long edge for casual prints. Web-only deliverables can be much smaller.",
                    "FileShrinkr's lossless PDF export preserves original pixels for print handoff. Compressed JPG and WEBP exports target screen and email workflows where smaller files matter more than print margins. Choose the export path that matches the recipient's workflow rather than defaulting to maximum pixels everywhere.",
                ],
            },
            {
                "heading": "Aspect ratio and layout stability",
                "paragraphs": [
                    "Resolution pairs with aspect ratio—the proportional relationship between width and height. A twelve hundred by eight hundred image and a twelve hundred by twelve hundred image share width but occupy different vertical space in layout. Cropping to consistent aspect ratios before compression keeps gallery grids tidy and prevents awkward letterboxing in PDF merge output.",
                    "Social platforms enforce aspect ratios in previews: square, four-five portrait, sixteen-nine landscape. Exporting at those native ratios avoids platform-side cropping that might cut faces or product edges. FileShrinkr's crop tool helps frame subjects before export.",
                    "When merging images to PDF, mixed aspect ratios each receive their own page geometry. Portrait scans and landscape photos in one merge still work, but uniform orientation simplifies printing. Plan aspect ratio at capture or crop stage, not only at compression.",
                ],
            },
            {
                "heading": "How compression interacts with resolution",
                "paragraphs": [
                    "Compression algorithms analyze patterns across pixels. Very small images compress quickly but show artifacts sooner because each pixel represents a larger share of the scene. Very large images tolerate lower quality settings because details are abundant, yet file size grows with pixel count even at low quality. The sweet spot is enough pixels for the display context, then tuned lossy compression.",
                    "Upsampling a small image to higher resolution before compression does not add real detail—it invents soft interpolation. Start from the best source available, downsample to target dimensions, then compress. If the source is a screenshot, preserve PNG until final export to JPG or WEBP to avoid double JPEG artifacts.",
                    "FileShrinkr scales and encodes with Pillow in server mode or locally in browser-private mode. Resize first with presets or custom dimensions, then set quality or a target KB limit. A soft output might need higher quality—or a smaller width before compression.",
                ],
            },
            {
                "heading": "Practical export presets for FileShrinkr",
                "paragraphs": [
                    "Blog inline image: twelve hundred to sixteen hundred pixels wide, WEBP or JPG at eighty percent quality. Product thumbnail: four hundred to six hundred pixels square, WEBP at seventy-five. Email attachment photo: sixteen hundred pixels max, JPG at seventy-five. Full-width hero: nineteen twenty pixels wide max, WEBP at eighty-five unless file size budget is tight.",
                    "Scanned document page: fifteen hundred to twenty-four hundred pixels on the long edge, merge to compressed PDF at eighty quality for email or lossless PDF for archival. Social square crop: ten eighty by ten eighty before export, JPG at eighty for platforms that recompress uploads.",
                    "Record which preset worked for your audience and reuse it. Resolution and DPI confusion fades once you standardize on pixel targets per channel. FileShrinkr handles scaling and compression; your editorial rules handle how sharp each channel needs to be.",
                ],
            },
        ],
        "related_slugs": [
            "compress-without-losing-quality",
            "best-image-format-for-websites",
            "prepare-images-for-email",
            "merge-images-into-pdf",
        ],
    },
}


def get_guide(slug):
  return GUIDES.get(slug)


def all_guide_slugs():
  return list(GUIDES.keys())
