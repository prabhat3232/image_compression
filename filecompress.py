import os
import json
from datetime import datetime
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
from PIL import Image

import ffmpeg  # ffmpeg-python library
from yt_dlp import YoutubeDL  # yt-dlp library

app = Flask(__name__)
app.secret_key = "your_secret_key"  # For flash messages if needed

# Temporary folder to store uploaded/downloaded files
app.config["UPLOAD_FOLDER"] = "uploads"
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/compress", methods=["POST"])
def compress_image():
    # Validate file upload
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    # Save the uploaded file
    filename = secure_filename(file.filename)
    input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(input_path)

    # Get the quality input
    quality = request.form.get("quality", type=int)
    if not quality or quality < 1 or quality > 100:
        return "Quality must be between 1 and 100", 400

    # Get the output format
    output_format = request.form.get("format")
    if output_format not in ["jpg", "webp", "pdf"]:
        return "Invalid format selected", 400

    # Generate a unique timestamp for filenames
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Set up output paths based on the selected format
    if output_format in ["jpg", "webp"]:
        output_file_name = f"compressed_{timestamp}.{output_format}"
        compressed_image_path = os.path.join(app.config["UPLOAD_FOLDER"], output_file_name)
    elif output_format == "pdf":
        # First compress as JPG then convert to PDF
        output_file_name = f"compressed_{timestamp}.jpg"
        compressed_image_path = os.path.join(app.config["UPLOAD_FOLDER"], output_file_name)

    pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], f"compressed_{timestamp}.pdf")

    # Use ffmpeg-python to compress the image.
    # The equivalent command is:
    #   ffmpeg -i input_path -vf scale="1280:-1" -q:v quality compressed_image_path
    try:
        (
            ffmpeg
            .input(input_path)
            .filter('scale', '1280:-1')
            .output(compressed_image_path, **{'qscale:v': quality})
            .run(overwrite_output=True)
        )
    except ffmpeg.Error as e:
        return "Failed to compress image: " + str(e), 500

    # If PDF is selected, convert the compressed image to PDF using Pillow
    if output_format == "pdf":
        try:
            image = Image.open(compressed_image_path)
            image.convert("RGB").save(pdf_path, "PDF")
            return send_file(
                pdf_path,
                mimetype="application/pdf",
                as_attachment=True,
                download_name=f"compressed_{timestamp}.pdf"
            )
        except Exception as e:
            return "Failed to convert image to PDF: " + str(e), 500

    # If JPEG or WEBP is selected, send the compressed image
    mimetype = "image/jpeg" if output_format == "jpg" else "image/webp"
    return send_file(
        compressed_image_path,
        mimetype=mimetype,
        as_attachment=True,
        download_name=output_file_name
    )


@app.route("/video_info", methods=["POST"])
def video_info():
    """
    Given a video URL, fetch video metadata and return available formats with detailed information.
    """
    url = request.form.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        # Use yt-dlp to extract video info without downloading
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    formats = info.get("formats", [])
    available_formats = []
    
    for f in formats:
        # Calculate approximate size in MB if available
        filesize = f.get("filesize") or f.get("filesize_approx")
        filesize_mb = round(filesize / (1024 * 1024), 2) if filesize else None
        
        # Create a more detailed format description
        format_note = []
        if f.get("format_note"):
            format_note.append(f.get("format_note"))
        if f.get("width") and f.get("height"):
            format_note.append(f"{f.get('width')}x{f.get('height')}")
        if filesize_mb:
            format_note.append(f"{filesize_mb}MB")
        if f.get("acodec") == "none":
            format_note.append("no audio")
        elif f.get("vcodec") == "none":
            format_note.append("audio only")
            
        fmt = {
            "format_id": f.get("format_id"),
            "ext": f.get("ext"),
            "format_note": " - ".join(format_note),
            "width": f.get("width"),
            "height": f.get("height"),
            "filesize": filesize_mb,
            "vcodec": f.get("vcodec"),
            "acodec": f.get("acodec"),
            "is_audio_only": f.get("vcodec") == "none",
            "is_video_only": f.get("acodec") == "none",
        }
        available_formats.append(fmt)

    # Sort formats by resolution (if video) or quality (if audio)
    available_formats.sort(
        key=lambda x: (x.get("height") or 0, x.get("filesize") or 0),
        reverse=True
    )

    return jsonify({
        "title": info.get("title"),
        "duration": info.get("duration"),
        "formats": available_formats
    })


@app.route("/download_video", methods=["POST"])
def download_video():
    """
    Download the video using yt-dlp with robust format handling and validation.
    """
    url = request.form.get("url")
    selected_format_id = request.form.get("format_id")
    if not url:
        return "No URL provided", 400
    if not selected_format_id:
        return "No format selected", 400

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_template = os.path.join(app.config["UPLOAD_FOLDER"], f"download_{timestamp}.%(ext)s")

    # First verify the format is available
    try:
        with YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # Check if the selected format is available
            available_formats = [f.get('format_id') for f in info.get('formats', [])]
            if selected_format_id not in available_formats:
                return f"Format {selected_format_id} is not available for this video. Available formats: {', '.join(available_formats)}", 400

    except Exception as e:
        return f"Failed to verify format availability: {str(e)}", 500

    # Set up download options with format validation
    download_opts = {
        'outtmpl': output_template,
        'quiet': True,
        # Try multiple format selection strategies
        'format': (
            # First try the exact format
            f'[format_id={selected_format_id}]/'
            # Then try the format with best audio
            f'{selected_format_id}+bestaudio/'
            # Finally fall back to best format
            'best'
        ),
        'merge_output_format': 'mp4',
        # Minimal postprocessing to avoid errors
        'postprocessors': []
    }

    try:
        with YoutubeDL(download_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            downloaded_file = ydl.prepare_filename(info_dict)
            
            # Check for different possible extensions
            if not os.path.exists(downloaded_file):
                base_path = os.path.splitext(downloaded_file)[0]
                for ext in ['.mp4', '.webm', '.mkv', '.m4a', '.mp3']:
                    if os.path.exists(base_path + ext):
                        downloaded_file = base_path + ext
                        break

    except Exception as e:
        error_message = str(e)
        # Log the full error for debugging
        print(f"Download error: {error_message}")
        return f"Failed to download video: {error_message}", 500

    if not os.path.exists(downloaded_file):
        return "Downloaded file not found", 500

    # Determine mimetype based on file extension
    ext = downloaded_file.split(".")[-1].lower()
    mimetypes = {
        'mp4': 'video/mp4',
        'mkv': 'video/x-matroska',
        'webm': 'video/webm',
        'mp3': 'audio/mpeg',
        'm4a': 'audio/mp4',
    }
    mimetype = mimetypes.get(ext, 'application/octet-stream')

    return send_file(
        downloaded_file,
        as_attachment=True,
        download_name=os.path.basename(downloaded_file),
        mimetype=mimetype,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
