from flask import Flask, render_template, request, send_file, url_for, make_response
import ffmpeg
from werkzeug.utils import secure_filename
from datetime import datetime
from PIL import Image
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/compress", methods=["POST"])
def compress_image():
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    filename = secure_filename(file.filename)
    input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(input_path)

    quality = request.form.get("quality", type=int)
    if not quality or quality < 1 or quality > 100:
        return "Quality must be between 1 and 100", 400

    output_format = request.form.get("format")
    if output_format not in ["jpg", "webp", "pdf"]:
        return "Invalid format selected", 400

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    compressed_image_path = ""
    output_file_name = ""
    pdf_path = ""

    if output_format in ["jpg", "pdf"]:
        output_file_name = f"compressed_{timestamp}.jpg"
        compressed_image_path = os.path.join(app.config["UPLOAD_FOLDER"], output_file_name)
    elif output_format == "webp":
        output_file_name = f"compressed_{timestamp}.webp"
        compressed_image_path = os.path.join(app.config["UPLOAD_FOLDER"], output_file_name)
    
    if output_format == "pdf":
        pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], f"compressed_{timestamp}.pdf")

    try:
        if output_format in ["jpg", "pdf"]:
            (
                ffmpeg
                .input(input_path)
                .filter('scale', 1280, -1)
                .output(compressed_image_path, q=quality)
                .run()
            )
        elif output_format == "webp":
            (
                ffmpeg
                .input(input_path)
                .filter('scale', 1280, -1)
                .output(compressed_image_path, quality=quality)
                .run()
            )
    except ffmpeg.Error as e:
        return f"Failed to compress image: {e.stderr}", 500
    except Exception as e:
        return f"Error: {str(e)}", 500

    if output_format == "pdf":
        try:
            image = Image.open(compressed_image_path)
            image.convert("RGB").save(pdf_path, "PDF")
            return send_file(pdf_path, mimetype="application/pdf", as_attachment=True, download_name=f"compressed_{timestamp}.pdf")
        except Exception as e:
            return f"Failed to convert image to PDF: {str(e)}", 500
    else:
        mimetype = "image/jpeg" if output_format == "jpg" else "image/webp"
        return send_file(
            compressed_image_path,
            mimetype=mimetype,
            as_attachment=True,
            download_name=output_file_name
        )

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    try:
        pages = []
        # Get all available routes
        routes = [url for url in app.url_map.iter_rules() if url.endpoint != 'sitemap' and url.endpoint != 'send_static_file']
        
        # Generate sitemap XML with proper formatting
        xml = "<?xml version='1.0' encoding='UTF-8'?>\n"
        xml += "<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>\n"
        
        for rule in routes:
            xml += f"  <url>\n"
            xml += f"    <loc>http://localhost:3000{rule}</loc>\n"
            xml += f"    <lastmod>{datetime.now().strftime('%Y-%m-%dT%H:%M:%S+00:00')}</lastmod>\n"
            xml += f"    <changefreq>weekly</changefreq>\n"
            xml += f"    <priority>0.8</priority>\n"
            xml += f"  </url>\n"
        
        xml += "</urlset>"

        # Return the XML with the correct MIME type and styling
        response = make_response(xml)
        response.mimetype = 'text/xml'
        response.headers['Content-Type'] = 'text/xml; charset=utf-8'
        
        return response
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
