"""Lossless crop of pre-reviews images — remove baked-in white/light margins."""
from __future__ import annotations

from pathlib import Path

from PIL import Image


def crop_margins(im: Image.Image, threshold: int = 238, tol: int = 15) -> tuple[Image.Image, tuple[int, int, int, int]]:
    rgb = im.convert("RGB")
    width, height = rgb.size
    pixels = rgb.load()

    def is_margin(x: int, y: int) -> bool:
        red, green, blue = pixels[x, y]
        if red > threshold and green > threshold and blue > threshold:
            return True
        if abs(red - green) < tol and abs(green - blue) < tol and red > 215 and green > 220 and blue > 230:
            return True
        return False

    sample_x = max(1, width // 80)
    sample_y = max(1, height // 80)

    top = 0
    for y in range(height):
        if sum(is_margin(x, y) for x in range(0, width, sample_x)) < (width // sample_x) * 0.9:
            top = y
            break

    bottom = height - 1
    for y in range(height - 1, -1, -1):
        if sum(is_margin(x, y) for x in range(0, width, sample_x)) < (width // sample_x) * 0.9:
            bottom = y
            break

    left = 0
    for x in range(width):
        if sum(is_margin(x, y) for y in range(0, height, sample_y)) < (height // sample_y) * 0.9:
            left = x
            break

    right = width - 1
    for x in range(width - 1, -1, -1):
        if sum(is_margin(x, y) for y in range(0, height, sample_y)) < (height // sample_y) * 0.9:
            right = x
            break

    box = (left, top, right, bottom)
    return rgb.crop((left, top, right + 1, bottom + 1)), box


def main() -> int:
    base = Path(__file__).resolve().parents[1] / "src" / "img" / "content" / "pre-reviews"
    names = ["shpigovsky-staff-group.webp", "shpigovsky-clinic-landscape.webp"]

    for name in names:
        src = base / name
        original = Image.open(src)
        cropped, box = crop_margins(original)
        print(f"{name}: {original.size} -> {cropped.size} box={box}")
        cropped.save(src, quality=92, method=6)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
