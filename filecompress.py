import os
import time
import zipfile
from datetime import datetime
import shutil
import io

from flask import Flask, render_template, request, jsonify, send_file, make_response, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
import ffmpeg
import img2pdf

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = "your_secret_key"

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

@app.route("/")
def index():
    return render_template("index.html")

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

    try:
        for file in files:
            if file.filename == "":
                continue

            filename = secure_filename(file.filename)
            input_path = os.path.join(batch_dir, filename)
            file.save(input_path)

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
                return jsonify({
                    "status": "success", 
                    "download_url": f"/static/{merged_pdf_name}",
                    "filename": merged_pdf_name
                })
            except Exception as e:
                return jsonify({"error": f"Merge error: {str(e)}"}), 500

        # Case B: Single File (JPG/WEBP/PDF)
        if len(processed_files) == 1:
            file_path = processed_files[0]
            filename = os.path.basename(file_path)
            target_path = os.path.join(static_folder_abs, filename)
            
            shutil.copy(file_path, target_path)
            
            time.sleep(2.0) # Flush
            return jsonify({
                "status": "success",
                "download_url": f"/static/{filename}",
                "filename": filename
            })

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
            
            return jsonify({
                "status": "success",
                "download_url": f"/static/{zip_name}",
                "filename": zip_name
            })
            
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
    return send_from_directory(app.root_path, 'ads.txt')


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
