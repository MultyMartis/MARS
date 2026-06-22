"""FP-0002 V6 — clean Section 01 visual audit from canonical JPG only."""
from __future__ import annotations

import hashlib
import json
import shutil
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
DESKTOP_WIDTH = 1398


def ensure_pillow() -> None:
    try:
        from PIL import Image, ImageDraw, ImageFont  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "-q"])


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def row_signature(img, y: int, x0: int, x1: int) -> tuple[int, ...]:
    px = img.load()
    step = max(1, (x1 - x0) // 120)
    sig: list[int] = []
    for x in range(x0, x1, step):
        r, g, b = px[x, y][:3]
        sig.extend((r // 8, g // 8, b // 8))
    return tuple(sig)


def row_mean_luma(img, y: int, x0: int, x1: int) -> float:
    px = img.load()
    step = max(1, (x1 - x0) // 200)
    total = 0.0
    count = 0
    for x in range(x0, x1, step):
        r, g, b = px[x, y][:3]
        total += 0.2126 * r + 0.7152 * g + 0.0722 * b
        count += 1
    return total / max(count, 1)


def find_hero_end(img) -> int:
    """Hero ends where full-width photo wash transitions to light page background."""
    w, h = img.size
    x0, x1 = int(w * 0.15), int(w * 0.85)
    prev = row_mean_luma(img, 850, x0, x1)
    for y in range(851, min(980, h)):
        luma = row_mean_luma(img, y, x0, x1)
        if luma - prev > 80:
            return y - 1
        prev = luma
    return 904


def find_section02_start(img, section01_start: int) -> int:
    """Section 02 begins at large red quote marks on white background."""
    w, h = img.size
    px = img.load()
    x_scan = int(w * 0.12)
    for y in range(section01_start + 400, min(h, section01_start + 700)):
        r, g, b = px[x_scan, y][:3]
        if r > 170 and g < 120 and b < 120 and (r - max(g, b)) > 100:
            return y - 2
    return 1496


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

    digest = sha256(MOCKUP)
    ref_copy = OUT_DIR / "FP-0002-V6-HOME-FULL-MOCKUP-REFERENCE.png"
    shutil.copy2(MOCKUP, ref_copy)

    img = Image.open(MOCKUP).convert("RGB")
    w, h = img.size

    hero_end = find_hero_end(img)
    section01_start = hero_end + 2
    section02_start = find_section02_start(img, section01_start)
    section01_end = section02_start - 2

    # Canonical crop with context
    crop_y0 = max(0, hero_end - 48)
    crop_y1 = min(h, section02_start + 48)
    crop = img.crop((0, crop_y0, w, crop_y1))
    crop_path = OUT_DIR / "FP-0002-V6-HOME-SECTION-01-CANONICAL-CROP.png"
    crop.save(crop_path)

    # Boundaries annotation on crop coordinates
    bound = crop.copy()
    draw = ImageDraw.Draw(bound)
    colors = {
        "hero_end": (0, 120, 255),
        "s01_start": (0, 180, 0),
        "s01_end": (255, 140, 0),
        "s02_start": (220, 0, 80),
        "container": (120, 120, 120),
    }
    rel = lambda y: y - crop_y0  # noqa: E731
    for y, key, label in (
        (hero_end, "hero_end", f"Hero end Y={hero_end}"),
        (section01_start, "s01_start", f"Section 01 start Y={section01_start}"),
        (section01_end, "s01_end", f"Section 01 end Y={section01_end}"),
        (section02_start, "s02_start", f"Section 02 start Y={section02_start}"),
    ):
        ry = rel(y)
        draw.line([(0, ry), (w, ry)], fill=colors[key], width=2)
        draw_label(draw, label, 12, max(4, ry - 18), colors[key])

    # Container edges — light gray content band
    cx0 = int(w * 0.035)
    cx1 = int(w * 0.965)
    draw.line([(cx0, rel(section01_start)), (cx0, rel(section01_end))], fill=colors["container"], width=1)
    draw.line([(cx1, rel(section01_start)), (cx1, rel(section01_end))], fill=colors["container"], width=1)
    draw_label(draw, "container L", cx0 + 4, rel(section01_start) + 8, colors["container"])
    draw_label(draw, "container R", cx1 - 110, rel(section01_start) + 8, colors["container"])

    bound_path = OUT_DIR / "FP-0002-V6-HOME-SECTION-01-BOUNDARIES.png"
    bound.save(bound_path)

    # Geometry map — card grid guides (3 columns estimated from mockup)
    geo = crop.copy()
    gdraw = ImageDraw.Draw(geo)
    grid_top = rel(section01_start + 200)
    grid_bottom = rel(section01_end - 24)
    col_w = (cx1 - cx0) // 3
    for i in range(4):
        x = cx0 + i * col_w
        gdraw.line([(x, grid_top), (x, grid_bottom)], fill=(180, 180, 255), width=1)
    for row in range(3):
        y = grid_top + row * ((grid_bottom - grid_top) // 2)
        gdraw.line([(cx0, y), (cx1, y)], fill=(180, 180, 255), width=1)
    gdraw.rectangle([(cx0, rel(section01_start)), (cx1, rel(section01_end))], outline=(255, 0, 0), width=2)
    draw_label(gdraw, "3-col x 2-row card grid (ESTIMATED)", cx0 + 8, grid_top + 8, (80, 80, 200))
    geo_path = OUT_DIR / "FP-0002-V6-HOME-SECTION-01-GEOMETRY-MAP.png"
    geo.save(geo_path)

    # Content map — highlight text bands (no OCR invention)
    content = crop.copy()
    cdraw = ImageDraw.Draw(content)
    bands = [
        (rel(section01_start + 28), rel(section01_start + 95), "S01-E01 heading band"),
        (rel(section01_start + 100), rel(section01_start + 175), "S01-E02 intro paragraph"),
        (rel(section01_start + 185), rel(section01_start + 290), "S01-E03 checklist (4 items)"),
        (grid_top, grid_bottom, "S01-E04..E09 card text bands"),
    ]
    for y0, y1, label in bands:
        cdraw.rectangle([(cx0, y0), (cx1, y1)], outline=(0, 160, 0), width=2)
        draw_label(cdraw, label, cx0 + 6, y0 + 4, (0, 120, 0))
    content_path = OUT_DIR / "FP-0002-V6-HOME-SECTION-01-CONTENT-MAP.png"
    content.save(content_path)

    meta = {
        "mockup_path": str(MOCKUP),
        "mockup_sha256": digest,
        "width_px": w,
        "height_px": h,
        "color_mode": "RGB",
        "aspect_ratio": round(w / h, 6),
        "boundaries": {
            "hero_end_y": hero_end,
            "section_01_start_y": section01_start,
            "section_01_end_y": section01_end,
            "section_02_start_y": section02_start,
        },
        "container_edges_px": {"left": cx0, "right": cx1},
        "outputs": {
            "reference": str(ref_copy.name),
            "canonical_crop": str(crop_path.name),
            "boundaries": str(bound_path.name),
            "geometry_map": str(geo_path.name),
            "content_map": str(content_path.name),
        },
    }
    meta_path = OUT_DIR / "FP-0002-V6-HOME-SECTION-01-BOUNDARY-META.json"
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
