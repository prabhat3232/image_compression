"""Glossary terms for FileShrinkr — definitions for image compression concepts."""

GLOSSARY = {
    "lossy-compression": {
        "slug": "lossy-compression",
        "title": "Lossy Compression",
        "definition": [
            "Lossy compression reduces file size by permanently discarding some image data that the encoder judges least visible to human eyes. JPEG and lossy WEBP are common lossy formats. The process is irreversible: once detail is removed, you cannot restore the original pixels from the compressed file alone. That trade accepts tiny imperfections in smooth gradients or fine textures in exchange for dramatically smaller files suitable for web pages, email, and social sharing.",
            "Quality sliders control how aggressive lossy encoding is. High settings preserve more detail and produce larger files; low settings shrink files faster but may introduce blocky artifacts in skies, noise in shadows, or softness around text. The goal is finding the lowest quality where the image still looks acceptable at its display size—not at full zoom on a monitor.",
            "FileShrinkr applies lossy compression when you export JPG or WEBP with the quality slider, and when you create compressed PDFs from raster images. For photographs destined for screens, lossy formats are usually the right default. Reserve lossless paths when fidelity is mandatory or when you plan further editing from the exported file.",
        ],
        "related_terms": [
            "lossless-compression",
            "webp-format",
            "dpi-resolution",
            "color-space",
        ],
    },
    "lossless-compression": {
        "slug": "lossless-compression",
        "title": "Lossless Compression",
        "definition": [
            "Lossless compression shrinks files by encoding redundancy more efficiently without throwing away pixel values. PNG and lossless WEBP use lossless methods. When you decompress, every pixel matches the pre-compression source. File sizes are larger than lossy equivalents for photographs, but lossless is essential for graphics with sharp edges, text, and transparency where artifacts would be obvious.",
            "Lossless does not mean the file is small—only that no detail was sacrificed. A noisy photograph saved as PNG may still be megabytes because random noise lacks patterns the encoder can compress. Lossless shines on screenshots, logos, and diagrams where repeated flat colors and straight lines compress well.",
            "FileShrinkr's lossless PDF export embeds original image bytes via img2pdf without re-encoding to JPEG. Use that path for scans, signed documents, and assets headed to print workflows. For everyday web photos, lossy JPG or WEBP at tuned quality delivers better size-to-quality balance than lossless PNG.",
        ],
        "related_terms": [
            "lossy-compression",
            "webp-format",
            "exif-metadata",
            "svg-rasterization",
        ],
    },
    "exif-metadata": {
        "slug": "exif-metadata",
        "title": "EXIF Metadata",
        "definition": [
            "EXIF (Exchangeable Image File Format) is metadata embedded in many JPEG and some other image files. It can record camera make and model, exposure settings, focal length, capture date, orientation flags, and sometimes GPS coordinates. Thumbnails and color profiles may also live in EXIF blocks. Viewers often ignore this data when displaying the image, but it still counts toward file size and may leak information you did not intend to share.",
            "Orientation EXIF tells software how to rotate a photo for correct display without altering pixel data. Some tools respect orientation; others ignore it, which is why explicitly rotating in an editor is safer before compression or PDF merge. GPS and device fields are privacy-sensitive when photos leave your control through email or public uploads.",
            "When preparing images on FileShrinkr, remember that compressed JPG outputs may retain EXIF from sources unless stripped upstream. Smaller social-ready files benefit from removing unused metadata. Future dedicated metadata-stripping options complement compression; until then, factor privacy into your pre-upload workflow for location-tagged photos.",
        ],
        "related_terms": [
            "dpi-resolution",
            "lossy-compression",
            "color-space",
            "lossless-compression",
        ],
    },
    "dpi-resolution": {
        "slug": "dpi-resolution",
        "title": "DPI and Resolution",
        "definition": [
            "Resolution describes how many pixels an image contains—width and height in pixels. DPI (dots per inch) and PPI (pixels per inch) describe how those pixels map to physical print size. A twenty-four hundred pixel wide image is twenty-four hundred pixels on screen regardless of whether metadata claims seventy-two or three hundred DPI. Browsers lay out images by pixel dimensions and CSS, not by DPI labels alone.",
            "Print workflows use DPI to calculate inches: three thousand pixels at three hundred DPI equals ten inches wide on paper. Web workflows use CSS pixels and device pixel ratios. Serving a four-thousand-pixel image in a four-hundred-pixel layout wastes bandwidth because the browser downscales. Target roughly one to two times your layout width in source pixels for sharp retina displays.",
            "FileShrinkr scales very wide uploads to practical maximums for compression and PDF export. Focus on pixel dimensions when tuning quality; changing DPI metadata without resampling does not shrink on-screen file appearance. Match pixel targets to channel—email, hero banner, thumbnail—and compress after resizing for predictable results.",
        ],
        "related_terms": [
            "aspect-ratio",
            "lossy-compression",
            "exif-metadata",
            "color-space",
        ],
    },
    "aspect-ratio": {
        "slug": "aspect-ratio",
        "title": "Aspect Ratio",
        "definition": [
            "Aspect ratio is the proportional relationship between an image's width and height, expressed as a ratio such as sixteen-nine, four-three, or one-one for squares. A sixteen hundred by nine hundred photo and an eight hundred by four hundred photo share the same sixteen-nine aspect ratio even though their pixel counts differ. Consistent ratios keep gallery grids, carousels, and PDF page layouts visually orderly.",
            "Cropping changes aspect ratio by removing pixels from edges. Platforms like Instagram and YouTube enforce ratios in previews; exporting at native ratios avoids automatic cropping that might cut subjects. Mixed ratios in a merged PDF still work—each page sizes to its image—but uniform orientation simplifies printing and professional presentation.",
            "Use FileShrinkr's crop tool before compression to frame subjects and lock aspect ratio for product shots or social templates. Pair aspect ratio decisions with resolution targets: a square ten eighty pixel export suits many social slots; a sixteen-nine nineteen twenty pixel export suits video thumbnails and wide heroes.",
        ],
        "related_terms": [
            "dpi-resolution",
            "svg-rasterization",
            "lossy-compression",
            "webp-format",
        ],
    },
    "webp-format": {
        "slug": "webp-format",
        "title": "WEBP Format",
        "definition": [
            "WEBP is a modern image format developed for the web, supporting both lossy and lossless compression as well as transparency and animation. Lossy WEBP typically produces files twenty-five to thirty-five percent smaller than JPEG at similar visual quality for photographs. Browsers including Chrome, Firefox, Safari, and Edge render WEBP natively, making it a strong default for sites you control.",
            "WEBP transparency competes with PNG for cut-out product shots and UI elements, often at smaller sizes than PNG for comparable content. Not every legacy system accepts WEBP attachments—some email clients still treat it as a generic file—so JPG remains the compatibility fallback when you cannot predict the viewing environment.",
            "FileShrinkr exports WEBP with the same quality slider used for JPG compression. Choose WEBP for blog images, product galleries, and app assets where modern browser support is assured. Compare JPG and WEBP outputs from the same source when migrating a site; smaller WEBP files improve LCP without visible quality loss when tuned correctly.",
        ],
        "related_terms": [
            "lossy-compression",
            "lossless-compression",
            "color-space",
            "aspect-ratio",
        ],
    },
    "svg-rasterization": {
        "slug": "svg-rasterization",
        "title": "SVG Rasterization",
        "definition": [
            "SVG (Scalable Vector Graphics) stores shapes, paths, and text as mathematical descriptions rather than a fixed pixel grid. Browsers render SVG crisply at any zoom level, which makes SVG ideal for logos, icons, and simple illustrations. Rasterization is the process of converting that vector description into a bitmap—a grid of pixels at specific width and height.",
            "Once rasterized, the image behaves like any JPEG or PNG: scaling up can look soft because no additional vector detail exists. Rasterization resolution matters: exporting an icon at sixty-four pixels suits favicons; exporting at five hundred twelve pixels suits high-DPI displays. Complex SVGs with filters, embedded bitmaps, or huge path counts may rasterize slowly or produce large files.",
            "When you upload SVG to FileShrinkr, the tool rasterizes it for JPG, WEBP, or PDF output at appropriate dimensions. Keep original SVGs for inline website markup where scalability matters. Use FileShrinkr when you need a compressed raster thumbnail, a WEBP variant for CMS upload, or a PDF sheet that embeds vector-derived bitmaps for recipients who cannot use SVG.",
        ],
        "related_terms": [
            "lossless-compression",
            "aspect-ratio",
            "dpi-resolution",
            "webp-format",
        ],
    },
    "color-space": {
        "slug": "color-space",
        "title": "Color Space",
        "definition": [
            "A color space defines the range of colors an image can represent and how numeric values map to visible hues. sRGB is the standard color space for web and most consumer displays. Adobe RGB and ProPhoto RGB encompass wider gamuts useful in professional photography and print, but colors outside sRGB may look dull or shifted when converted for screens that cannot display those extremes.",
            "Embedded ICC profiles in image files tell software how to interpret color values. Mismatched profiles can make the same file look washed out in one viewer and oversaturated in another. Converting to sRGB before web export stabilizes appearance across browsers and compression tools. Compression itself does not fix color problems—it encodes whatever pixels are present.",
            "When FileShrinkr compresses JPG or WEBP, output colors follow the processed pixel data from your upload. If skin tones or brand colors look wrong after compression, check source color space and convert to sRGB in an editor before upload. Consistent color space handling pairs with format and quality choices for predictable publishing results.",
        ],
        "related_terms": [
            "lossy-compression",
            "exif-metadata",
            "webp-format",
            "dpi-resolution",
        ],
    },
}


def get_glossary_term(slug):
  return GLOSSARY.get(slug)


def all_glossary_slugs():
  return list(GLOSSARY.keys())
