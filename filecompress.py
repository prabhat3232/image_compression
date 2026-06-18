import os
import time
import zipfile
from collections import defaultdict
from datetime import datetime
import shutil
import io

from flask import Flask, render_template, request, jsonify, send_file, make_response, send_from_directory, abort, Response
from werkzeug.utils import secure_filename
from PIL import Image
import ffmpeg
import img2pdf

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from content.config import SITE_URL, CONTACT_EMAIL, all_sitemap_paths
from content.pages import TRUST_PAGES, PHASE3_PAGES, canonical, build_schema_graph
from content.landing_pages import LANDING_PAGES, get_landing, all_landing_slugs
from content.guides import GUIDES, get_guide, all_guide_slugs
from content.glossary import GLOSSARY, get_glossary_term, all_glossary_slugs
from content.home_faq import HOME_FAQS, POPULAR_TOOLS
from content.mail import contact_delivery_configured, send_contact_email

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "change-me-in-production")

RESIZE_PRESETS = {
    "instagram_square": (1080, 1080),
    "facebook": (1200, 630),
    "youtube": (1280, 720),
}

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


def _resolve_related(slugs):
    related = []
    for slug in slugs:
        page = LANDING_PAGES.get(slug) or PHASE3_PAGES.get(slug) or TRUST_PAGES.get(slug)
        if page:
            related.append({"slug": slug, "title": page.get("h1") or page.get("title", slug)})
    return related


def _contact_rate_ok(ip):
    now = time.time()
    hits = [t for t in CONTACT_RATE_LIMIT[ip] if now - t < CONTACT_RATE_WINDOW]
    CONTACT_RATE_LIMIT[ip] = hits
    if len(hits) >= CONTACT_RATE_MAX:
        return False
    hits.append(now)
    return True


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


def _finalize_raster(path, output_format, quality, strip_exif=False, resize_preset=None):
    image = Image.open(path)
    if resize_preset and resize_preset in RESIZE_PRESETS:
        tw, th = RESIZE_PRESETS[resize_preset]
        image = _resize_cover(image.convert("RGB"), tw, th)
    elif output_format in ("jpg", "pdf"):
        image = image.convert("RGB")

    root, _ = os.path.splitext(path)
    out_path = path if output_format == "jpg" else f"{root}.{output_format}"

    save_kwargs = {}
    if strip_exif:
        save_kwargs["exif"] = b""

    if output_format == "webp":
        image.save(out_path, "WEBP", quality=quality, method=6)
    elif output_format == "jpg":
        image.save(out_path, "JPEG", quality=quality, optimize=True, **save_kwargs)
    else:
        image.save(out_path, quality=quality, **save_kwargs)

    if out_path != path and os.path.exists(path):
        os.remove(path)
    return out_path


def _json_with_sizes(payload, original_size, compressed_size):
    if original_size and compressed_size:
        payload["original_size"] = original_size
        payload["compressed_size"] = compressed_size
    return jsonify(payload)


@app.route("/")
def index():
    latest = [GUIDES[s] for s in all_guide_slugs()[:3]]
    return render_template(
        "index.html",
        home_faqs=HOME_FAQS,
        popular_tools=POPULAR_TOOLS,
        latest_guides=latest,
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
    if output_format not in ["jpg", "webp", "pdf"]:
        return "Invalid format selected", 400

    merge_pdf = request.form.get("merge_pdf") == "on"
    compress_pdf_images = request.form.get("compress_pdf_images", "on") == "on"
    strip_exif = request.form.get("strip_exif") == "on"
    resize_preset = request.form.get("resize_preset")
    if resize_preset not in RESIZE_PRESETS:
        resize_preset = None
    
    print(f"DEBUG: compress_pdf_images checkbox value: {request.form.get('compress_pdf_images')}")
    print(f"DEBUG: compress_pdf_images boolean: {compress_pdf_images}")

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

    try:
        for file in files:
            if file.filename == "":
                continue

            filename = secure_filename(file.filename)
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

            # 1. Compress using ffmpeg
            try:
                # For PDF without compression, skip ffmpeg entirely and use original
                if output_format == "pdf" and not compress_pdf_images:
                    # Use original file directly - no copying, no conversion
                    compressed_path = input_path
                    print(f"DEBUG: Skipping ffmpeg, using original file: {input_path}")
                else:
                    # Compress with ffmpeg
                    (
                        ffmpeg
                        .input(input_path)
                        .filter('scale', 1280, -1)
                        .output(compressed_path, **{'qscale:v': quality})
                        .run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
                    )
            except ffmpeg.Error as e:
                error_msg = f"Error compressing {filename}: {e.stderr.decode('utf8') if e.stderr else str(e)}"
                print(error_msg)
                errors.append(error_msg)
                continue

            # Post-process: resize preset, EXIF strip, WEBP conversion
            raster_format = "jpg" if output_format == "pdf" else output_format
            needs_pillow = (
                raster_format == "webp"
                or strip_exif
                or resize_preset
            )
            if needs_pillow and not (output_format == "pdf" and not compress_pdf_images):
                try:
                    compressed_path = _finalize_raster(
                        compressed_path,
                        raster_format,
                        quality,
                        strip_exif=strip_exif,
                        resize_preset=resize_preset,
                    )
                except Exception as e:
                    error_msg = f"Error post-processing {filename}: {str(e)}"
                    print(error_msg)
                    errors.append(error_msg)
                    continue

            # 2. Convert to Individual PDF if needed
            if output_format == "pdf" and not merge_pdf:
                try:
                    if compress_pdf_images:
                        print(f"DEBUG: Using Pillow for PDF conversion (compressed)")
                        # Standard quality with Pillow
                        image = Image.open(compressed_path)
                        rgb_image = image.convert("RGB")
                        rgb_image.save(final_path, "PDF", resolution=100.0)
                        # Cleanup intermediate JPG
                        if os.path.exists(compressed_path):
                            os.remove(compressed_path)
                    else:
                        print(f"DEBUG: Using img2pdf for PDF conversion (lossless) - input_path: {input_path}")
                        # Lossless conversion with img2pdf
                        # img2pdf embeds images without re-encoding
                        try:
                            with open(input_path, "rb") as img_file:
                                # Use img2pdf with layout that preserves original dimensions
                                pdf_bytes = img2pdf.convert(
                                    img_file.read(),
                                    layout_fun=img2pdf.get_layout_fun(None)  # Preserve original size
                                )
                            with open(final_path, "wb") as pdf_file:
                                pdf_file.write(pdf_bytes)
                            print(f"DEBUG: Lossless PDF created at: {final_path}")
                        except Exception as img2pdf_error:
                            print(f"DEBUG: img2pdf failed, falling back to Pillow: {img2pdf_error}")
                            # Fallback to Pillow if img2pdf fails
                            image = Image.open(input_path)
                            rgb_image = image.convert("RGB")
                            rgb_image.save(final_path, "PDF", resolution=300.0, quality=100)
                            print(f"DEBUG: Fallback PDF created at: {final_path}")
                except Exception as e:
                    error_msg = f"Error converting {filename} to PDF: {str(e)}"
                    print(error_msg)
                    errors.append(error_msg)
                    continue

            # 3. Add to lists
            if output_format == "pdf" and merge_pdf:
                pdf_merge_inputs.append(compressed_path)
                pdf_merge_original_inputs.append(input_path)  # Track original for lossless
            else:
                processed_files.append(final_path)


        if not processed_files and not pdf_merge_inputs:
             return f"No files processed. Errors: {'; '.join(errors)}", 500

        # --- FINAL OUTPUT GENERATION ---

        # Case A: Merge to Request PDF
        if output_format == "pdf" and merge_pdf:
            if not pdf_merge_inputs:
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
                return _json_with_sizes({
                    "status": "success",
                    "download_url": f"/static/{merged_pdf_name}",
                    "filename": merged_pdf_name
                }, original_size, compressed_size)
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
                "filename": filename
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
                "filename": zip_name
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
            mimetype="application/zip" if filename.endswith(".zip") else "application/pdf"
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
    body = [
        "# FileShrinkr",
        f"# {SITE_URL}",
        "",
        "FileShrinkr is a free online image compressor and editor by DSnM Solutions.",
        "Supports JPG, PNG, WEBP, SVG upload; JPG, WEBP, PDF output; batch ZIP; PDF merge.",
        "",
        "## Pages",
    ]
    for path in all_sitemap_paths():
        body.append(f"- {SITE_URL}{path if path != '/' else '/'}")
    response = Response("\n".join(body) + "\n", mimetype="text/plain; charset=utf-8")
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


def _render_landing(slug):
    page = get_landing(slug) or PHASE3_PAGES.get(slug)
    if not page:
        abort(404)
    page_url = canonical(f"/{slug}")
    howto = None
    if page.get("howto_steps"):
        howto = {
            "name": page["h1"],
            "description": page["description"],
            "steps": page["howto_steps"],
        }
    schema_json = build_schema_graph(page_url, faqs=page.get("faqs"), howto=howto)
    return render_template(
        "pages/landing.html",
        page=page,
        canonical=page_url,
        schema_json=schema_json,
        related=_resolve_related(page.get("related_slugs", [])),
    )


@app.route("/guides")
def guides_index():
    guides = [GUIDES[s] for s in all_guide_slugs()]
    return render_template("blog/index.html", guides=guides, canonical=canonical("/guides"))


@app.route("/guides/<slug>")
def guide_detail(slug):
    guide = get_guide(slug)
    if not guide:
        abort(404)
    related = [GUIDES[s] for s in guide.get("related_guides", []) if s in GUIDES]
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


def _make_landing_view(slug):
    def view():
        return _render_landing(slug)
    view.__name__ = f"landing_{slug}"
    return view


for _slug in all_landing_slugs() + list(PHASE3_PAGES.keys()):
    app.add_url_rule(f"/{_slug}", endpoint=f"landing_{_slug}", view_func=_make_landing_view(_slug))


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
