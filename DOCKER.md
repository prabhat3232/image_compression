# Image Compression & Editing Tools - Docker Setup

## Quick Start

### Using Docker Compose (Recommended)

```bash
# Build and start the container
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the container
docker-compose down
```

The application will be available at `http://localhost:3000`

### Using Docker CLI

```bash
# Build the image
docker build -t image-tools .

# Run the container
docker run -d \
  -p 3000:3000 \
  -v $(pwd)/uploads:/app/uploads \
  -v $(pwd)/static:/app/static \
  --name image-tools \
  image-tools

# View logs
docker logs -f image-tools

# Stop the container
docker stop image-tools
docker rm image-tools
```

## Features

- **Image Compressor**: Compress images to JPG, WEBP, or PDF with quality control
- **Image Editor**: Resize, rotate, and flip images client-side
- **Auto-download**: Compressed files download automatically
- **PDF Merge**: Combine multiple images into a single PDF

## Volumes

- `./uploads`: Temporary storage for uploaded files
- `./static`: Storage for processed files (compressed images, ZIPs, PDFs)

## Environment Variables

- `FLASK_ENV`: Set to `production` for production deployment (default in docker-compose)

## Ports

- `3000`: Web application port

## Notes

- All image editing is done client-side (browser) using HTML5 Canvas
- Image compression uses ffmpeg for optimal quality
- Files in `uploads/` and `static/` folders are persisted via Docker volumes
