# Project Context: Media Tools Web App

## Overview
This project is a lightweight, Flask-based web application that provides:
1.  **Image Compression**: Compresses images and converts them to different formats (JPG, WEBP, PDF).

## Tech Stack
-   **Backend**: Python, Flask
-   **Frontend**: HTML5, Tailwind CSS (via CDN), JavaScript
-   **Image Processing**: `ffmpeg-python`, `Pillow` (PIL)

## Key Features

### Image Compressor
-   **Formats**: Input supports standard image formats. Output supports JPG, WEBP, and PDF.
-   **Quality Control**: Adjustable compression quality (1-100).
-   **PDF Conversion**: Can convert compressed images directly to PDF.
-   **Processing**: Uses FFmpeg for efficient scaling and compression.
-   **Multi-file Support**: Compresses multiple images at once and downloads them as a ZIP file.
-   **Drag & Drop**: Modern UI with drag-and-drop file upload.

## Project Structure
```text
.
├── brain/                  # Project documentation and context
├── templates/
│   └── index.html          # Main single-page application UI
├── uploads/                # Temporary directory for file processing
├── filecompress.py         # Main Flask application entry point
└── requirements.txt        # Python dependencies
```

## Setup & Usage
1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: FFmpeg must be installed on the system and available in the PATH.*

2.  **Run the Application**:
    ```bash
    python filecompress.py
    ```

3.  **Access the UI**:
    Open a browser and navigate to `http://localhost:3000`.
