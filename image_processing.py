"""Raster image processing for FileShrinkr (HEIC, AVIF, WEBP, JPG, PNG)."""

import os
import tempfile

from PIL import Image, features

RESIZE_PRESETS = {
    "instagram_square": (1080, 1080),
    "facebook": (1200, 630),
    "youtube": (1280, 720),
}

MAX_RASTER_WIDTH = 1280
LOSSY_FORMATS = frozenset({"jpg", "jpeg", "webp", "avif"})

HEIC_SUPPORTED = False
try:
    from pillow_heif import register_heif_opener

    register_heif_opener()
    HEIC_SUPPORTED = True
except ImportError:
    pass

AVIF_SUPPORTED = features.check("avif")

try:
    MOZJPEG_SUPPORTED = features.check_feature("mozjpeg")
except (AttributeError, ValueError):
    MOZJPEG_SUPPORTED = False


def is_heic_path(path):
    ext = os.path.splitext(path)[1].lower()
    return ext in (".heic", ".heif")


def is_heic_image(path):
    if is_heic_path(path):
        return True
    try:
        with Image.open(path) as img:
            return img.format == "HEIF"
    except Exception:
        return False


def _resize_cover(img, target_w, target_h):
    img_ratio = img.width / img.height
    target_ratio = target_w / target_h
    if img_ratio > target_ratio:
        new_h = target_h
        new_w = int(target_h * img_ratio)
    else:
        new_w = target_w
        new_h = int(target_w / img_ratio)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    return img.crop((left, top, left + target_w, top + target_h))


def _scale_to_max_width(image, max_width=MAX_RASTER_WIDTH):
    if image.width <= max_width:
        return image
    ratio = max_width / image.width
    new_h = max(1, int(image.height * ratio))
    return image.resize((max_width, new_h), Image.LANCZOS)


def _apply_resize(image, output_format, resize_preset=None, width=None, height=None):
    if resize_preset and resize_preset in RESIZE_PRESETS:
        tw, th = RESIZE_PRESETS[resize_preset]
        needs_rgb = output_format in ("jpg", "jpeg", "pdf", "webp", "avif")
        base = image.convert("RGB") if needs_rgb and image.mode not in ("RGB",) else image
        return _resize_cover(base, tw, th)

    if width and height and width > 0 and height > 0:
        needs_rgb = output_format in ("jpg", "jpeg", "pdf", "webp", "avif")
        base = image.convert("RGB") if needs_rgb and image.mode not in ("RGB",) else image
        return _resize_cover(base, int(width), int(height))

    image = _scale_to_max_width(image)
    if output_format in ("jpg", "jpeg", "pdf"):
        return image.convert("RGB")
    return image


def _strip_metadata(image):
    """Return a fresh image without EXIF/metadata."""
    if image.mode == "P":
        image = image.convert("RGBA")
    clean = Image.new(image.mode, image.size)
    clean.putdata(list(image.getdata()))
    if image.mode == "P":
        clean.putpalette(image.getpalette())
    return clean


def _save_raster(image, output_path, output_format, quality, strip_exif=False, use_mozjpeg=False):
    fmt = output_format.lower()
    if strip_exif:
        image = _strip_metadata(image)

    if fmt == "webp":
        kwargs = {"quality": quality, "method": 6}
        if strip_exif:
            kwargs["exif"] = b""
        image.save(output_path, "WEBP", **kwargs)
    elif fmt == "avif":
        kwargs = {"quality": quality}
        if strip_exif:
            kwargs["exif"] = b""
        image.save(output_path, "AVIF", **kwargs)
    elif fmt in ("jpg", "jpeg"):
        kwargs = {"quality": quality, "optimize": True}
        if strip_exif:
            kwargs["exif"] = b""
        image.save(output_path, "JPEG", **kwargs)
    elif fmt == "png":
        if image.mode not in ("RGBA", "LA", "P"):
            image = image.convert("RGBA")
        image.save(output_path, "PNG", optimize=True, compress_level=9)
    else:
        raise ValueError(f"Unsupported raster format: {output_format}")


def encode_to_target_size(image, output_path, output_format, target_bytes, strip_exif=False, use_mozjpeg=False):
    """
    Binary-search quality for lossy formats to stay under target_bytes.
    Returns (quality_used, within_target).
    """
    fmt = output_format.lower()
    if fmt not in LOSSY_FORMATS:
        _save_raster(image, output_path, output_format, 85, strip_exif=strip_exif, use_mozjpeg=use_mozjpeg)
        return 85, True

    best_q = 1
    best_size = None
    low, high = 1, 100
    within = False

    while low <= high:
        mid = (low + high) // 2
        fd, tmp_path = tempfile.mkstemp(suffix=f".{fmt if fmt != 'jpeg' else 'jpg'}")
        os.close(fd)
        try:
            _save_raster(image, tmp_path, output_format, mid, strip_exif=strip_exif, use_mozjpeg=use_mozjpeg)
            size = os.path.getsize(tmp_path)
            if size <= target_bytes:
                within = True
                best_q = mid
                best_size = size
                low = mid + 1
            else:
                high = mid - 1
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    if best_size is None:
        _save_raster(image, output_path, output_format, 1, strip_exif=strip_exif, use_mozjpeg=use_mozjpeg)
        return 1, False

    _save_raster(image, output_path, output_format, best_q, strip_exif=strip_exif, use_mozjpeg=use_mozjpeg)
    return best_q, within


def process_raster(
    input_path,
    output_path,
    output_format,
    quality,
    strip_exif=False,
    resize_preset=None,
    width=None,
    height=None,
    target_kb=None,
    png_lossless=True,
    use_mozjpeg=False,
):
    """
    Open input, resize, and save as jpg, webp, avif, or png.
    Returns dict with path, within_target, quality_used.
    """
    if is_heic_path(input_path) and not HEIC_SUPPORTED:
        raise RuntimeError("HEIC support is not available on the server")

    if output_format == "avif" and not AVIF_SUPPORTED:
        raise RuntimeError("AVIF encoding is not available on the server")

    if use_mozjpeg and output_format not in ("jpg", "jpeg"):
        use_mozjpeg = False

    with Image.open(input_path) as image:
        if output_format == "png" and png_lossless:
            working = image.copy()
        else:
            working = image

        working = _apply_resize(working, output_format, resize_preset, width, height)

        within_target = True
        quality_used = quality

        if target_kb and output_format.lower() in LOSSY_FORMATS:
            target_bytes = int(target_kb) * 1024
            quality_used, within_target = encode_to_target_size(
                working,
                output_path,
                output_format,
                target_bytes,
                strip_exif=strip_exif,
                use_mozjpeg=use_mozjpeg,
            )
        else:
            _save_raster(
                working,
                output_path,
                output_format,
                quality,
                strip_exif=strip_exif,
                use_mozjpeg=use_mozjpeg,
            )

    return {
        "path": output_path,
        "within_target": within_target,
        "quality_used": quality_used,
    }


def raster_to_jpeg_temp(
    input_path,
    output_path,
    quality,
    strip_exif=False,
    resize_preset=None,
    width=None,
    height=None,
    target_kb=None,
    use_mozjpeg=False,
):
    """Convert any supported raster (including HEIC) to JPEG for PDF pipelines."""
    return process_raster(
        input_path,
        output_path,
        "jpg",
        quality,
        strip_exif=strip_exif,
        resize_preset=resize_preset,
        width=width,
        height=height,
        target_kb=target_kb,
        use_mozjpeg=use_mozjpeg,
    )


def prepare_lossless_pdf_input(input_path, batch_dir, file_root):
    """
    img2pdf needs JPEG/PNG/TIFF. Convert HEIC and other formats to a temp JPEG.
    Returns path suitable for img2pdf.convert().
    """
    ext = os.path.splitext(input_path)[1].lower()
    if ext in (".jpg", ".jpeg", ".png", ".tiff", ".tif"):
        return input_path
    temp_path = os.path.join(batch_dir, f"{file_root}_lossless_pdf.jpg")
    with Image.open(input_path) as image:
        image.convert("RGB").save(temp_path, "JPEG", quality=95, optimize=True)
    return temp_path
