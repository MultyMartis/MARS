"""FP-0002 V6 — Section 02 visual audit from canonical JPG only."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MOCKUP = (
    ROOT.parent
    / "website-factory-operations"
    / "FP-0002-SHPIGOVSKY"
    / "INCOMING"
    / "01_DESIGN"
    / "HOME-PAGE-FULL-MOCKUP.jpg"
)
OUT_DIR = Path(__file__).resolve().parent
CONTENT_IMG_DIR = ROOT / "src" / "img" / "content"


def ensure_pillow() -> None:
    try:
        from PIL import Image, ImageDraw  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "-q"])


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def detect_card_grid_end(img, search_from: int = 1180) -> tuple[int, str]:
    """Bottom edge of 3×2 card grid (operator-canonical Section 01)."""
    w, h = img.size
    px = img.load()
    col_centers = [(265, 474), (490, 908), (924, 1342)]
    bottom = search_from
    for y in range(search_from, min(h, 2150)):
        if any(sum(px[(a + b) // 2, y][:3]) < 620 for a, b in col_centers):
            bottom = y
    bottom = min(bottom + 8, 2110)
    return bottom, f"Last card-row ink band before quote whitespace Y≈{bottom}"


def find_quote_start(img, after_y: int) -> tuple[int, str]:
    w, h = img.size
    px = img.load()
    for y in range(after_y + 8, min(h, after_y + 80), 2):
        for x in range(48, 200, 6):
            r, g, b = px[x, y][:3]
            if r > 175 and g < 105 and b < 105 and (r - max(g, b)) > 90:
                return y, f"Large red opening quote mark at x≈{x}, y≈{y}"
    return after_y + 20, "Fallback padding after card grid"


def find_section03_start(img, after_y: int) -> tuple[int, str]:
    w, h = img.size
    px = img.load()
    for y in range(after_y + 320, min(h, after_y + 620), 4):
        dark = sum(1 for x in range(48, 620, 10) if sum(px[x, y][:3]) < 290)
        if dark > 22:
            top = y
            for yy in range(y, max(after_y, y - 50), -2):
                dark2 = sum(1 for x in range(48, 620, 12) if sum(px[x, yy][:3]) < 290)
                if dark2 < 10:
                    top = yy + 1
                    break
            return top - 28, f"Treatment heading band top at y≈{y}"
    return after_y + 480, "Fallback section 03 scan"


def detect_portrait_box(img, y0: int, y1: int) -> tuple[int, int, int, int, str]:
    w, _ = img.size
    px = img.load()
    x_start = int(w * 0.52)
    min_x, min_y, max_x, max_y = w, y1, 0, y0
    for y in range(y0 + 10, y1 - 40, 3):
        for x in range(x_start, w - 36, 4):
            r, g, b = px[x, y][:3]
            lum = r + g + b
            if 220 < lum < 760 and abs(r - g) < 40 and b < r + 30:
                min_x = min(min_x, x)
                min_y = min(min_y, y)
                max_x = max(max_x, x)
                max_y = max(max_y, y)
    if max_x > min_x and max_y > min_y:
        pad = 6
        return (
            max(0, min_x - pad),
            max(y0, min_y - pad),
            min(w, max_x + pad),
            min(y1, max_y + pad),
            "Portrait skin-tone cluster on right column",
        )
    return (780, y0 + 20, w - 48, y1 - 60, "Fallback portrait column bounds")


def find_content_zones(img, s02_start: int, s02_end: int, portrait: tuple) -> dict:
    w, _ = img.size
    quote_x1 = portrait[0] - 24
    author_top = portrait[1] + int((portrait[3] - portrait[1]) * 0.55)
    return {
        "quote_mark": (48, s02_start, 130, s02_start + 72),
        "quote_text": (48, s02_start + 56, quote_x1, s02_end - 110),
        "portrait": portrait[:4],
        "author_block": (portrait[0], author_top, w - 48, author_top + 110),
        "cta": (portrait[0], author_top + 118, portrait[0] + 290, author_top + 158),
    }


def draw_label(draw, text: str, x: int, y: int, color: tuple[int, int, int]) -> None:
    draw.text((x + 1, y + 1), text, fill=(255, 255, 255))
    draw.text((x, y), text, fill=color)


def main() -> int:
    if not MOCKUP.is_file():
        print(f"MISSING_MOCKUP: {MOCKUP}")
        return 2

    ensure_pillow()
    from PIL import Image, ImageDraw

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CONTENT_IMG_DIR.mkdir(parents=True, exist_ok=True)

    digest = sha256(MOCKUP)
    img = Image.open(MOCKUP).convert("RGB")
    w, h = img.size

    card_end, card_ev = detect_card_grid_end(img)
    section01_end = card_end + 10
    section02_start, s02_ev = find_quote_start(img, card_end)
    section02_end, s03_ev = find_section03_start(img, section02_start)
    section03_start = section02_end
    portrait_box = detect_portrait_box(img, section02_start, section02_end)
    zones = find_content_zones(img, section02_start, section02_end, portrait_box)

    wide_y0 = max(0, section01_end - 100)
    wide_y1 = min(h, section03_start + 100)
    img.crop((0, wide_y0, w, wide_y1)).save(OUT_DIR / "FP-0002-V6-SECTION-02-WIDE-CONTEXT.png")

    crop_y0 = max(0, section02_start - 24)
    crop_y1 = min(h, section02_end + 24)
    crop = img.crop((0, crop_y0, w, crop_y1))
    crop.save(OUT_DIR / "FP-0002-V6-SECTION-02-CANONICAL-CROP.png")

    rel = lambda y: y - crop_y0  # noqa: E731

    bound = crop.copy()
    draw = ImageDraw.Draw(bound)
    lines = [
        (section01_end, (255, 140, 0), f"Section 01 end Y={section01_end} CONFIRMED"),
        (section02_start, (220, 0, 80), f"Section 02 start Y={section02_start} CONFIRMED"),
        (section02_start + 24, (0, 180, 0), f"Section 02 content start Y={section02_start + 24} HIGH"),
        (section02_end - 24, (0, 120, 255), f"Section 02 content end Y={section02_end - 24} HIGH"),
        (section02_end, (255, 140, 0), f"Section 02 end Y={section02_end} CONFIRMED"),
        (section03_start, (128, 0, 128), f"Section 03 start Y={section03_start} CONFIRMED"),
    ]
    for y, color, label in lines:
        ry = rel(y)
        draw.line([(0, ry), (w, ry)], fill=color, width=2)
        draw_label(draw, label, 12, max(4, ry - 18), color)
    bound.save(OUT_DIR / "FP-0002-V6-SECTION-02-BOUNDARIES.png")

    content = crop.copy()
    cdraw = ImageDraw.Draw(content)
    colors = {
        "quote_mark": (179, 38, 30),
        "quote_text": (0, 120, 200),
        "portrait": (200, 0, 200),
        "author_block": (0, 160, 0),
        "cta": (255, 140, 0),
    }
    for key, (zx0, zy0, zx1, zy1) in zones.items():
        cdraw.rectangle([(zx0, rel(zy0)), (zx1, rel(zy1))], outline=colors[key], width=2)
        draw_label(cdraw, key, zx0 + 6, rel(zy0) + 4, colors[key])
    content.save(OUT_DIR / "FP-0002-V6-SECTION-02-CONTENT-MAP.png")

    geo = crop.copy()
    gdraw = ImageDraw.Draw(geo)
    cx0, cx1 = 48, w - 48
    gdraw.rectangle([(0, rel(section02_start)), (w, rel(section02_end))], outline=(255, 0, 0), width=2)
    gdraw.rectangle([(cx0, rel(section02_start)), (cx1, rel(section02_end))], outline=(0, 0, 255), width=1)
    col_split = portrait_box[0] - 12
    gdraw.line([(col_split, rel(section02_start)), (col_split, rel(section02_end))], fill=(180, 180, 255), width=1)
    draw_label(gdraw, "2-col split", col_split + 8, rel(section02_start) + 8, (80, 80, 200))
    geo.save(OUT_DIR / "FP-0002-V6-SECTION-02-GEOMETRY-MAP.png")

    px0, py0, px1, py1 = portrait_box[:4]
    portrait_crop = img.crop((px0, py0, px1, py1))
    portrait_path = CONTENT_IMG_DIR / "founder-sergey-shpigovsky.png"
    portrait_crop.save(portrait_path)

    meta = {
        "mockup_path": str(MOCKUP),
        "mockup_sha256": digest,
        "width_px": w,
        "height_px": h,
        "boundaries": {
            "section_01_end_y": section01_end,
            "section_01_end_evidence": card_ev,
            "section_02_start_y": section02_start,
            "section_02_content_start_y": section02_start + 24,
            "section_02_content_end_y": section02_end - 24,
            "section_02_end_y": section02_end,
            "section_03_start_y": section03_start,
            "section_02_evidence": s02_ev,
            "section_03_evidence": s03_ev,
        },
        "portrait_box": {
            "x0": px0,
            "y0": py0,
            "x1": px1,
            "y1": py1,
            "evidence": portrait_box[4],
            "exported_to": str(portrait_path.relative_to(ROOT)).replace("\\", "/"),
        },
        "zones": {k: {"x0": v[0], "y0": v[1], "x1": v[2], "y1": v[3]} for k, v in zones.items()},
        "decorative_excluded": ["background red cross watermark — operator policy"],
        "content_image_count": 1,
        "decorative_image_count_in_mockup": 1,
        "supersedes": "Section 01 V2 boundary Y=1491 assumed 3-card row only; corrected for operator 3×2 grid",
    }
    meta_path = OUT_DIR / "FP-0002-V6-SECTION-02-BOUNDARY-META.json"
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
