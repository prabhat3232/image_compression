import os
import time
import zipfile
from collections import defaultdict
from datetime import datetime
import shutil
import io

from flask import Flask, render_template, request, jsonify, send_file, make_response, send_from_directory, abort, Response, redirect
from werkzeug.utils import secure_filename
from PIL import Image
import img2pdf

from image_processing import (
    AVIF_SUPPORTED,
    HEIC_SUPPORTED,
    MOZJPEG_SUPPORTED,
    RESIZE_PRESETS,
    is_heic_image,
    prepare_lossless_pdf_input,
    process_raster,
    raster_to_jpeg_temp,
)

ALLOWED_TARGET_KB = {20, 100, 500}

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from content.config import SITE_URL, CONTACT_EMAIL, all_sitemap_paths, REMOVED_PAGE_REDIRECTS
from content.seo import HOME_DESCRIPTION, HOME_HERO_SUBTITLE, HOME_KEYWORDS, HOME_TITLE, OG_IMAGE_ALT
from content.pages import TRUST_PAGES, canonical
from content.guides import GUIDES, get_guide, all_guide_slugs
from content.glossary import GLOSSARY, get_glossary_term, all_glossary_slugs
from content.home_faq import HOME_FAQS
from content.mail import contact_delivery_configured, send_contact_email

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "change-me-in-production")
app.config["TEMPLATES_AUTO_RELOAD"] = os.environ.get("FLASK_ENV") != "production"

CONTACT_RATE_LIMIT = defaultdict(list)
CONTACT_RATE_MAX = 3
CONTACT_RATE_WINDOW = 3600

# Configuration
app.config["UPLOAD_FOLDER"] = "uploads"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching

# Ensure directories exist
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

# We will use 'static' folder for serving the final files
STATIC_FOLDER = "static"
if not os.path.exists(STATIC_FOLDER):
    os.makedirs(STATIC_FOLDER)

_DOWNLOAD_MIMETYPES = {
    ".zip": "application/zip",
    ".pdf": "application/pdf",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".avif": "image/avif",
    ".png": "image/png",
}


def _download_mimetype(filename):
    ext = os.path.splitext(filename)[1].lower()
    return _DOWNLOAD_MIMETYPES.get(ext, "application/octet-stream")


def _contact_rate_ok(ip):
    now = time.time()
    hits = [t for t in CONTACT_RATE_LIMIT[ip] if now - t < CONTACT_RATE_WINDOW]
    CONTACT_RATE_LIMIT[ip] = hits
    if len(hits) >= CONTACT_RATE_MAX:
        return False
    hits.append(now)
    return True


def _json_with_sizes(payload, original_size, compressed_size):
    if original_size and compressed_size:
        payload["original_size"] = original_size
        payload["compressed_size"] = compressed_size
    return jsonify(payload)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(STATIC_FOLDER, "favicon.ico", mimetype="image/vnd.microsoft.icon")


@app.route("/")
def index():
    latest = [GUIDES[s] for s in all_guide_slugs()[:3]]
    return render_template(
        "index.html",
        home_faqs=HOME_FAQS,
        latest_guides=latest,
        heic_supported=HEIC_SUPPORTED,
        avif_supported=AVIF_SUPPORTED,
        mozjpeg_supported=MOZJPEG_SUPPORTED,
        resize_presets=RESIZE_PRESETS,
        seo_title=HOME_TITLE,
        seo_description=HOME_DESCRIPTION,
        seo_keywords=HOME_KEYWORDS,
        seo_hero_subtitle=HOME_HERO_SUBTITLE,
        seo_og_image_alt=OG_IMAGE_ALT,
    )

@app.route("/compress", methods=["POST"])
def compress_image():
    # Validate file upload
    if "file" not in request.files:
        return "No file part", 400

    files = request.files.getlist("file")
    if not files or files[0].filename == "":
        return "No selected file", 400

    # Get input parameters
    quality = request.form.get("quality", type=int)
    if not quality or quality < 1 or quality > 100:
        return "Quality must be between 1 and 100", 400

    output_format = request.form.get("format")
    if output_format not in ["jpg", "webp", "avif", "png", "pdf"]:
        return "Invalid format selected", 400

    if output_format == "avif" and not AVIF_SUPPORTED:
        return jsonify({"error": "AVIF encoding is not available on the server"}), 400

    merge_pdf = request.form.get("merge_pdf") == "on"
    compress_pdf_images = request.form.get("compress_pdf_images", "on") == "on"
    strip_exif = request.form.get("strip_exif") == "on"
    png_lossless = request.form.get("png_lossless", "on") == "on"
    use_mozjpeg = request.form.get("mozjpeg") == "on" and MOZJPEG_SUPPORTED
    if request.form.get("mozjpeg") == "on" and output_format != "jpg":
        return jsonify({"error": "MozJPEG is only available for JPG output"}), 400

    resize_preset = request.form.get("resize_preset")
    if resize_preset not in RESIZE_PRESETS:
        resize_preset = None

    custom_width = request.form.get("width", type=int)
    custom_height = request.form.get("height", type=int)
    if (custom_width and not custom_height) or (custom_height and not custom_width):
        return jsonify({"error": "Both width and height are required for custom resize"}), 400
    if custom_width and custom_width < 1:
        custom_width = None
    if custom_height and custom_height < 1:
        custom_height = None
    if resize_preset:
        custom_width = None
        custom_height = None

    target_kb = request.form.get("target_kb", type=int)
    if target_kb is not None and target_kb not in ALLOWED_TARGET_KB:
        target_kb = None
    if target_kb and output_format in ("png", "pdf"):
        return jsonify({"error": "Target file size is not available for PNG or PDF"}), 400

    # Setup directories
    batch_id = datetime.now().strftime("%Y%m%d%H%M%S")
    upload_folder_abs = os.path.abspath(app.config["UPLOAD_FOLDER"])
    batch_dir = os.path.join(upload_folder_abs, batch_id)
    if not os.path.exists(batch_dir):
        os.makedirs(batch_dir)
        
    static_folder_abs = os.path.abspath(STATIC_FOLDER)

    processed_files = []      # List of absolute paths to processed files
    pdf_merge_inputs = []     # List of absolute paths for PDF merging
    pdf_merge_original_inputs = []  # List of original files for lossless PDF merging
    errors = []
    original_size = 0
    all_within_target = True

    try:
        for file in files:
            if file.filename == "":
                continue

            filename = secure_filename(file.filename)
            if not os.path.splitext(filename)[1]:
                orig_ext = os.path.splitext(file.filename or "")[1].lower()
                if orig_ext in (".heic", ".heif"):
                    filename = (filename or "image") + orig_ext
            input_path = os.path.join(batch_dir, filename)
            file.save(input_path)
            original_size += os.path.getsize(input_path)

            file_root, _ = os.path.splitext(filename)
            
            # Determine output filename and intermediate paths
            if output_format == "pdf" and merge_pdf:
                # For merging, we create temporary JPGs
                temp_filename = f"{file_root}_compressed.jpg"
                compressed_path = os.path.join(batch_dir, temp_filename)
                final_path = compressed_path # Not final yet, just for the list
            else:
                # For individual files
                ext = "pdf" if output_format == "pdf" else output_format
                out_filename = f"{file_root}_compressed.{ext}"
                
                if output_format == "pdf":
                    # Intermediate JPG for PDF conversion
                    temp_jpg = f"{file_root}_compressed.jpg"
                    compressed_path = os.path.join(batch_dir, temp_jpg)
                    final_path = os.path.join(batch_dir, out_filename)
                else:
                    # Direct compression
                    compressed_path = os.path.join(batch_dir, out_filename)
                    final_path = compressed_path

            if is_heic_image(input_path) and not HEIC_SUPPORTED:
                errors.append(f"HEIC support is not available on the server ({filename})")
                continue

            try:
                if output_format == "pdf" and not compress_pdf_images:
                    lossless_input = prepare_lossless_pdf_input(input_path, batch_dir, file_root)
                    if merge_pdf:
                        pdf_merge_original_inputs.append(lossless_input)
                    else:
                        with open(final_path, "wb") as pdf_file:
                            with open(lossless_input, "rb") as img_file:
                                pdf_file.write(
                                    img2pdf.convert(
                                        img_file.read(),
                                        layout_fun=img2pdf.get_layout_fun(None),
                                    )
                                )
                        processed_files.append(final_path)
                elif output_format == "pdf":
                    pdf_result = raster_to_jpeg_temp(
                        input_path,
                        compressed_path,
                        quality,
                        strip_exif=strip_exif,
                        resize_preset=resize_preset,
                        width=custom_width,
                        height=custom_height,
                        target_kb=target_kb,
                        use_mozjpeg=use_mozjpeg,
                    )
                    if not pdf_result.get("within_target", True):
                        all_within_target = False
                    if merge_pdf:
                        pdf_merge_inputs.append(compressed_path)
                    else:
                        image = Image.open(compressed_path)
                        image.convert("RGB").save(final_path, "PDF", resolution=100.0)
                        if os.path.exists(compressed_path) and compressed_path != final_path:
                            os.remove(compressed_path)
                        processed_files.append(final_path)
                else:
                    result = process_raster(
                        input_path,
                        final_path,
                        output_format,
                        quality,
                        strip_exif=strip_exif,
                        resize_preset=resize_preset,
                        width=custom_width,
                        height=custom_height,
                        target_kb=target_kb,
                        png_lossless=png_lossless,
                        use_mozjpeg=use_mozjpeg,
                    )
                    if not result.get("within_target", True):
                        all_within_target = False
                    processed_files.append(final_path)
            except Exception as e:
                error_msg = f"Error processing {filename}: {str(e)}"
                print(error_msg)
                errors.append(error_msg)
                continue


        if not processed_files and not pdf_merge_inputs and not pdf_merge_original_inputs:
             return f"No files processed. Errors: {'; '.join(errors)}", 500

        # --- FINAL OUTPUT GENERATION ---

        # Case A: Merge to Request PDF
        if output_format == "pdf" and merge_pdf:
            if not pdf_merge_inputs and not pdf_merge_original_inputs:
                return jsonify({"error": "No valid images to merge."}), 500
            
            merged_pdf_name = f"merged_{batch_id}.pdf"
            merged_pdf_path = os.path.join(static_folder_abs, merged_pdf_name)
            
            try:
                if compress_pdf_images:
                    # Standard quality with Pillow
                    images = [Image.open(p).convert("RGB") for p in pdf_merge_inputs]
                    images[0].save(merged_pdf_path, "PDF", save_all=True, append_images=images[1:], resolution=100.0)
                else:
                    # Lossless conversion with img2pdf (use original files)
                    with open(merged_pdf_path, "wb") as pdf_file:
                        pdf_file.write(img2pdf.convert(pdf_merge_original_inputs))
                
                time.sleep(2.0) # Flush
                compressed_size = os.path.getsize(merged_pdf_path)
                payload = {
                    "status": "success",
                    "download_url": f"/static/{merged_pdf_name}",
                    "filename": merged_pdf_name,
                    "within_target": all_within_target,
                }
                return _json_with_sizes(payload, original_size, compressed_size)
            except Exception as e:
                return jsonify({"error": f"Merge error: {str(e)}"}), 500

        # Case B: Single File (JPG/WEBP/PDF)
        if len(processed_files) == 1:
            file_path = processed_files[0]
            filename = os.path.basename(file_path)
            target_path = os.path.join(static_folder_abs, filename)
            
            shutil.copy(file_path, target_path)
            
            time.sleep(2.0) # Flush
            compressed_size = os.path.getsize(target_path)
            return _json_with_sizes({
                "status": "success",
                "download_url": f"/static/{filename}",
                "filename": filename,
                "within_target": all_within_target,
            }, original_size, compressed_size)

        # Case C: Multiple Files -> ZIP
        zip_name = f"compressed_{batch_id}.zip"
        zip_path = os.path.join(static_folder_abs, zip_name)
        
        try:
            print(f"DEBUG: Creating ZIP at {zip_path}")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for p in processed_files:
                    if os.path.exists(p):
                        zipf.write(p, os.path.basename(p))
            
            if not os.path.exists(zip_path):
                raise Exception("ZIP file not found after creation")
                
            print(f"DEBUG: ZIP Size: {os.path.getsize(zip_path)}")
            
            # FILE SYSTEM SYNC DELAY (Crucial for Chrome)
            time.sleep(2.0)
            
            compressed_size = os.path.getsize(zip_path)
            return _json_with_sizes({
                "status": "success",
                "download_url": f"/static/{zip_name}",
                "filename": zip_name,
                "within_target": all_within_target,
            }, original_size, compressed_size)
            
        except Exception as e:
             return jsonify({"error": f"ZIP error: {str(e)}"}), 500

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Server error: {str(e)}"}), 500


@app.route("/download_file/<path:filename>")
def download_file_route(filename):
    try:
        static_folder_abs = os.path.abspath(STATIC_FOLDER)
        file_path = os.path.join(static_folder_abs, filename)

        print(f"DEBUG: Request to download_file: {filename}")
        print(f"DEBUG: Looking in: {static_folder_abs}")
        
        if not os.path.exists(file_path):
             print(f"DEBUG: FAIL - File not found at {file_path}")
             return "File not found", 404
             
        size = os.path.getsize(file_path)
        print(f"DEBUG: Found file. Size: {size} bytes. Sending...")

        # Explicitly use send_from_directory which is safer than send_file for paths
        response = send_from_directory(
            static_folder_abs, 
            filename, 
            as_attachment=True,
            download_name=filename,
            mimetype=_download_mimetype(filename),
        )
        
        # Ensure no caching
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        
        return response

    except Exception as e:
        print(f"DEBUG: Error serving {filename}: {e}")
        return str(e), 500


@app.route('/ads.txt')
def ads_txt():
    response = send_from_directory(
        app.root_path,
        'ads.txt',
        mimetype='text/plain; charset=utf-8',
    )
    # Help crawlers avoid caching stale/mis-typed responses.
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.root_path, 'robots.txt')


@app.route('/sitemap.xml')
def sitemap_xml():
    today = datetime.now().strftime("%Y-%m-%d")
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in all_sitemap_paths():
        loc = SITE_URL + (path if path != "/" else "/")
        priority = "1.0" if path == "/" else "0.8"
        changefreq = "weekly" if path in ("/", "/guides") else "monthly"
        lines.append(
            f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod>"
            f"<changefreq>{changefreq}</changefreq><priority>{priority}</priority></url>"
        )
    lines.append("</urlset>")
    response = Response("\n".join(lines), mimetype="application/xml")
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


@app.route('/llms.txt')
def llms_txt():
    llms_path = os.path.join(os.path.dirname(__file__), "llms.txt")
    if os.path.isfile(llms_path):
        with open(llms_path, encoding="utf-8") as f:
            body = f.read()
    else:
        body = "\n".join([
            "# FileShrinkr",
            f"# {SITE_URL}",
            "",
            "FileShrinkr is a free online image compressor and editor by DSnM Solutions.",
            "Hybrid browser + server processing: HEIC, AVIF, PNG, JPG, WEBP, PDF; target KB sizes;",
            "browser-private mode; Instagram/Facebook/YouTube resize; batch ZIP; PDF merge; editor.",
        ])
    response = Response(body if body.endswith("\n") else body + "\n", mimetype="text/plain; charset=utf-8")
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


def _render_trust(slug, flash_message=None, flash_ok=False):
    page = TRUST_PAGES.get(slug)
    if not page:
        abort(404)
    return render_template(
        "pages/trust.html",
        slug=slug,
        page=page,
        canonical=canonical(f"/{slug}"),
        contact_email=CONTACT_EMAIL,
        smtp_configured=contact_delivery_configured(),
        flash_message=flash_message,
        flash_ok=flash_ok,
    )


@app.route("/about")
def about():
    return _render_trust("about")


@app.route("/privacy")
def privacy():
    return _render_trust("privacy")


@app.route("/terms")
def terms():
    return _render_trust("terms")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    flash_message = None
    flash_ok = False
    if request.method == "POST":
        if request.form.get("website"):
            flash_message = "Thank you. Your message was sent."
            flash_ok = True
        elif not _contact_rate_ok(request.remote_addr or "unknown"):
            flash_message = "Too many messages. Please try again later or email us directly."
        else:
            name = (request.form.get("name") or "").strip()[:120]
            email = (request.form.get("email") or "").strip()[:200]
            subject = (request.form.get("subject") or "").strip()[:200]
            message = (request.form.get("message") or "").strip()[:5000]
            if name and email and subject and message:
                ok, err = send_contact_email(name, email, subject, message)
                if ok:
                    flash_message = "Thank you. We received your message and will respond soon."
                    flash_ok = True
                else:
                    flash_message = err or "Could not send message. Please email us directly."
            else:
                flash_message = "Please fill in all fields."
    return _render_trust("contact", flash_message=flash_message, flash_ok=flash_ok)


@app.route("/guides")
def guides_index():
    guides = [GUIDES[s] for s in all_guide_slugs()]
    return render_template("blog/index.html", guides=guides, canonical=canonical("/guides"))


@app.route("/guides/<slug>")
def guide_detail(slug):
    guide = get_guide(slug)
    if not guide:
        abort(404)
    related = [GUIDES[s] for s in guide.get("related_slugs", guide.get("related_guides", [])) if s in GUIDES]
    return render_template(
        "blog/post.html",
        guide=guide,
        canonical=canonical(f"/guides/{slug}"),
        related=related,
    )


@app.route("/glossary")
def glossary_index():
    terms = [GLOSSARY[s] for s in all_glossary_slugs()]
    return render_template("glossary.html", terms=terms, term=None, canonical=canonical("/glossary"))


@app.route("/glossary/<slug>")
def glossary_detail(slug):
    term = get_glossary_term(slug)
    if not term:
        abort(404)
    related_terms = [GLOSSARY[s] for s in term.get("related_terms", []) if s in GLOSSARY]
    return render_template(
        "glossary.html",
        term=term,
        terms=None,
        related_terms=related_terms,
        canonical=canonical(f"/glossary/{slug}"),
    )


for _slug, _target in REMOVED_PAGE_REDIRECTS.items():
    def _make_redirect_view(target=_target, slug=_slug):
        def view():
            return redirect(target, code=301)
        view.__name__ = f"redirect_{slug}"
        return view
    app.add_url_rule(f"/{_slug}", endpoint=f"redirect_{_slug}", view_func=_make_redirect_view())


if __name__ == "__main__":
    print("Starting server...")
    # Threaded=True might help if connection is being dropped? 
    # But usually standard run is single-threaded or threaded depending on flask version. 
    # Default is threaded=True in newer flask.
    # Get port from environment variable or default to 3000
    port = int(os.environ.get("PORT", 3000))
    # Turn off debug mode in production
    debug_mode = os.environ.get("FLASK_ENV") != "production"
    
    print(f"Starting server on port {port} (Debug: {debug_mode})...")
    app.run(debug=debug_mode, host="0.0.0.0", port=port)
