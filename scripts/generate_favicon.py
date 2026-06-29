"""Generate PNG and ICO favicon assets from the FileShrinkr icon design."""

from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "static"

BG = (15, 23, 42)
CYAN = (56, 189, 248)
INDIGO = (129, 140, 248)


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _gradient_color(x, y, w, h):
    t = (x / max(w - 1, 1) + y / max(h - 1, 1)) / 2
    return _lerp(CYAN, INDIGO, min(max(t, 0), 1))


def draw_icon(size: int) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pad = size * 0.06
    radius = size * 0.22

    draw.rounded_rectangle((0, 0, size - 1, size - 1), radius=radius, fill=BG)

    frame = (
        size * 0.16,
        size * 0.25,
        size * 0.84,
        size * 0.75,
    )
    frame_radius = size * 0.08
    for offset in range(2):
        color = _gradient_color(size // 2, size // 2, size, size)
        draw.rounded_rectangle(
            (frame[0] - offset, frame[1] - offset, frame[2] + offset, frame[3] + offset),
            radius=frame_radius,
            outline=color,
            width=max(1, size // 16),
        )

    peak = [
        (size * 0.24, size * 0.69),
        (size * 0.36, size * 0.52),
        (size * 0.45, size * 0.59),
        (size * 0.59, size * 0.42),
        (size * 0.76, size * 0.69),
    ]
    for i in range(len(peak) - 1):
        draw.line(
            [peak[i], peak[i + 1]],
            fill=_gradient_color(int(peak[i][0]), int(peak[i][1]), size, size),
            width=max(1, size // 18),
        )

    sun_r = size * 0.045
    sun = (size * 0.34, size * 0.41)
    draw.ellipse(
        (sun[0] - sun_r, sun[1] - sun_r, sun[0] + sun_r, sun[1] + sun_r),
        fill=CYAN,
    )

    ax, ay = size * 0.66, size * 0.14
    aw = size * 0.16
    draw.line([(ax + aw, ay), (ax + aw, ay + aw)], fill=CYAN, width=max(1, size // 16))
    draw.line([(ax + aw, ay), (ax, ay + aw)], fill=CYAN, width=max(1, size // 16))

    return img


def main():
    STATIC.mkdir(parents=True, exist_ok=True)
    sizes = {16: "favicon-16x16.png", 32: "favicon-32x32.png", 180: "apple-touch-icon.png"}
    images = {}
    for size, name in sizes.items():
        path = STATIC / name
        icon = draw_icon(size)
        icon.save(path, format="PNG")
        images[size] = icon
        print(f"Wrote {path}")

    ico_path = STATIC / "favicon.ico"
    images[32].save(
        ico_path,
        format="ICO",
        sizes=[(16, 16), (32, 32)],
        append_images=[images[16]],
    )
    print(f"Wrote {ico_path}")


if __name__ == "__main__":
    main()
