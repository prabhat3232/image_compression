/**
 * Browser-side image compression for FileShrinkr (hybrid mode).
 */
(function (global) {
  const MIME = {
    jpg: "image/jpeg",
    webp: "image/webp",
    avif: "image/avif",
    png: "image/png",
  };

  const LOSSY_FORMATS = new Set(["jpg", "webp", "avif"]);

  const RESIZE_PRESETS = global.FILESHRINKR_RESIZE_PRESETS || {
    instagram_square: [1080, 1080],
    facebook: [1200, 630],
    youtube: [1280, 720],
  };

  const MAX_WIDTH = 1280;

  let capabilitiesCache = null;

  function probeMime(mime) {
    return new Promise((resolve) => {
      const canvas = document.createElement("canvas");
      canvas.width = 2;
      canvas.height = 2;
      canvas.toBlob((blob) => resolve(!!blob), mime, 0.8);
    });
  }

  async function detectCapabilities() {
    if (capabilitiesCache) return capabilitiesCache;
    const [jpeg, webp, avif, png] = await Promise.all([
      probeMime("image/jpeg"),
      probeMime("image/webp"),
      probeMime("image/avif"),
      probeMime("image/png"),
    ]);
    capabilitiesCache = { jpeg, webp, avif, png };
    return capabilitiesCache;
  }

  function isHeicFile(file) {
    const name = (file.name || "").toLowerCase();
    return name.endsWith(".heic") || name.endsWith(".heif");
  }

  function loadImageFromFile(file) {
    return new Promise((resolve, reject) => {
      const url = URL.createObjectURL(file);
      const img = new Image();
      img.onload = () => {
        URL.revokeObjectURL(url);
        resolve(img);
      };
      img.onerror = () => {
        URL.revokeObjectURL(url);
        reject(new Error("decode_failed"));
      };
      img.src = url;
    });
  }

  function resizeCover(img, targetW, targetH) {
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");
    const imgRatio = img.width / img.height;
    const targetRatio = targetW / targetH;
    let newW, newH;
    if (imgRatio > targetRatio) {
      newH = targetH;
      newW = Math.round(targetH * imgRatio);
    } else {
      newW = targetW;
      newH = Math.round(targetW / imgRatio);
    }
    const tmp = document.createElement("canvas");
    tmp.width = newW;
    tmp.height = newH;
    tmp.getContext("2d").drawImage(img, 0, 0, newW, newH);
    const sx = Math.floor((newW - targetW) / 2);
    const sy = Math.floor((newH - targetH) / 2);
    canvas.width = targetW;
    canvas.height = targetH;
    ctx.drawImage(tmp, sx, sy, targetW, targetH, 0, 0, targetW, targetH);
    return canvas;
  }

  function scaleToMaxWidth(img, maxWidth) {
    if (img.width <= maxWidth) {
      const canvas = document.createElement("canvas");
      canvas.width = img.width;
      canvas.height = img.height;
      canvas.getContext("2d").drawImage(img, 0, 0);
      return canvas;
    }
    const newH = Math.max(1, Math.round(img.height * (maxWidth / img.width)));
    const canvas = document.createElement("canvas");
    canvas.width = maxWidth;
    canvas.height = newH;
    canvas.getContext("2d").drawImage(img, 0, 0, maxWidth, newH);
    return canvas;
  }

  function applyResize(img, options) {
    const { resizePreset, width, height } = options;
    if (resizePreset && RESIZE_PRESETS[resizePreset]) {
      const [tw, th] = RESIZE_PRESETS[resizePreset];
      return resizeCover(img, tw, th);
    }
    if (width && height && width > 0 && height > 0) {
      return resizeCover(img, width, height);
    }
    return scaleToMaxWidth(img, MAX_WIDTH);
  }

  function canvasToBlob(canvas, mime, quality) {
    return new Promise((resolve, reject) => {
      const q = mime === "image/png" ? undefined : quality / 100;
      canvas.toBlob(
        (blob) => (blob ? resolve(blob) : reject(new Error("encode_failed"))),
        mime,
        q
      );
    });
  }

  async function encodeToTargetSize(canvas, mime, targetBytes, qualityHint) {
    let bestBlob = null;
    let bestQ = 1;
    let within = false;
    let low = 1;
    let high = 100;

    while (low <= high) {
      const mid = Math.floor((low + high) / 2);
      const blob = await canvasToBlob(canvas, mime, mid);
      if (blob.size <= targetBytes) {
        within = true;
        bestBlob = blob;
        bestQ = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    if (!bestBlob) {
      bestBlob = await canvasToBlob(canvas, mime, 1);
      return { blob: bestBlob, qualityUsed: 1, withinTarget: false };
    }

    return { blob: bestBlob, qualityUsed: bestQ, withinTarget: within };
  }

  function outputFilename(originalName, format) {
    const base = originalName.replace(/\.[^.]+$/, "") || "image";
    const ext = format === "jpg" ? "jpg" : format;
    return `${base}_compressed.${ext}`;
  }

  function originalPreviewUrl(file) {
    return URL.createObjectURL(file);
  }

  async function compressFile(file, options) {
    const {
      format,
      quality,
      resizePreset,
      width,
      height,
      targetKb,
      pngLossless,
    } = options;
    const mime = MIME[format];
    if (!mime) throw new Error("unsupported_format");

    let img;
    try {
      img = await loadImageFromFile(file);
    } catch (e) {
      return { needsServer: true, file, reason: "decode_failed" };
    }

    const canvas = applyResize(img, { resizePreset, width, height });
    const origUrl = originalPreviewUrl(file);

    try {
      let blob;
      let withinTarget = true;
      let qualityUsed = quality;

      if (format === "png") {
        blob = await canvasToBlob(canvas, mime, quality);
      } else if (targetKb && LOSSY_FORMATS.has(format)) {
        const encoded = await encodeToTargetSize(canvas, mime, targetKb * 1024, quality);
        blob = encoded.blob;
        withinTarget = encoded.withinTarget;
        qualityUsed = encoded.qualityUsed;
      } else {
        blob = await canvasToBlob(canvas, mime, quality);
      }

      const compressedUrl = URL.createObjectURL(blob);
      return {
        blob,
        filename: outputFilename(file.name, format),
        originalSize: file.size,
        compressedSize: blob.size,
        withinTarget,
        qualityUsed,
        preview: { originalUrl: origUrl, compressedUrl },
      };
    } catch (e) {
      URL.revokeObjectURL(origUrl);
      return { needsServer: true, file, reason: "encode_failed" };
    }
  }

  async function compressBatch(files, options) {
    const results = [];
    const needsServer = [];
    let totalOriginal = 0;
    let totalCompressed = 0;
    let allWithinTarget = true;

    for (const file of files) {
      if (!file || !file.size) continue;
      const out = await compressFile(file, options);
      if (out.needsServer) {
        needsServer.push(file);
      } else {
        results.push(out);
        totalOriginal += out.originalSize;
        totalCompressed += out.compressedSize;
        if (out.withinTarget === false) allWithinTarget = false;
      }
    }

    return {
      results,
      needsServer,
      totalOriginal,
      totalCompressed,
      withinTarget: allWithinTarget,
    };
  }

  function downloadBlob(blob, filename) {
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  async function downloadResults(results) {
    if (!results.length) return;
    if (results.length === 1) {
      downloadBlob(results[0].blob, results[0].filename);
      return;
    }
    if (typeof JSZip === "undefined") {
      throw new Error("JSZip is required for batch download");
    }
    const zip = new JSZip();
    for (const r of results) {
      zip.file(r.filename, r.blob);
    }
    const zipBlob = await zip.generateAsync({ type: "blob" });
    const stamp = new Date().toISOString().replace(/[-:T.Z]/g, "").slice(0, 14);
    downloadBlob(zipBlob, `compressed_${stamp}.zip`);
  }

  function requiresServer(form, processingMode) {
    if (processingMode === "server") return true;
    const format = form.querySelector('input[name="format"]:checked')?.value;
    if (format === "pdf") return true;
    if (form.querySelector('input[name="strip_exif"]')?.checked) return true;
    if (form.querySelector('input[name="mozjpeg"]')?.checked) return true;
    return false;
  }

  global.FileShrinkrClient = {
    detectCapabilities,
    isHeicFile,
    compressBatch,
    downloadResults,
    requiresServer,
    applyResize,
    MIME,
    LOSSY_FORMATS,
  };
})(window);
