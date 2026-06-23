"""FP-0002 V6 — next home section audit from canonical JPG only."""
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

# Grounded major-section block anchors (FP-0002-V6-JPG-STRUCTURE-LOCK.md)
BLOCK_013_END = 7136
BLOCK_014_START = 7136
BLOCK_014_END = 7504
BLOCK_015_END = 7848
BLOCK_016_END = 8408
BLOCK_017_END = 8824
BLOCK_018_START = 8824  # following section — programs


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


def find_reviews_end(img, search_from: int = 6000) -> int:
    """Detect reviews pagination / whitespace band end before process heading."""
    w, h = img.size
    px = img.load()
    for y in range(search_from, min(h, 7200)):
        dark_heading = sum(
            1
            for x in range(80, min(w - 80, 520), 30)
            if sum(px[x, y][:3]) < 120
        )
        if dark_heading > 4:
            band = 0
            for yy in range(y, min(h, y + 80)):
                if sum(1 for x in range(80, min(w - 80, 520), 30) if sum(px[x, yy][:3]) < 120) > 3:
                    band += 1
            if band > 20:
                return max(BLOCK_013_END, y - 8)
    return BLOCK_013_END


def find_dark_band(img, y0: int, y1: int) -> tuple[int, int]:
    w, h = img.size
    px = img.load()
    start = None
    end = None
    for y in range(y0, min(y1, h)):
        dark = sum(1 for x in range(48, w - 48, 24) if sum(px[x, y][:3]) < 90)
        if dark > (w // 24) * 0.35:
            if start is None:
                start = y
            end = y + 1
        elif start is not None and end is not None and y - end > 24:
            break
    if start is None:
        start = BLOCK_014_END
        end = BLOCK_016_END
    return start, end


def main() -> int:
    ensure_pillow()
    from PIL import Image, ImageDraw

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img = Image.open(MOCKUP).convert("RGB")
    w, h = img.size

    reviews_end_y = find_reviews_end(img)
    next_section_start_y = BLOCK_014_START
    next_section_content_start_y = next_section_start_y + 24
    cta_start, cta_end = find_dark_band(img, BLOCK_014_END, BLOCK_017_END)
    next_section_content_end_y = cta_end + 40
    next_section_end_y = BLOCK_017_END
    following_section_start_y = BLOCK_018_START

    wide_y0 = max(0, reviews_end_y - 80)
    wide_y1 = min(h, following_section_start_y + 80)
    img.crop((0, wide_y0, w, wide_y1)).save(OUT_DIR / "FP-0002-V6-NEXT-SECTION-WIDE-CONTEXT.png")

    crop_y0 = max(0, reviews_end_y - 40)
    crop_y1 = min(h, following_section_start_y + 40)
    img.crop((0, crop_y0, w, crop_y1)).save(OUT_DIR / "FP-0002-V6-NEXT-SECTION-CANONICAL-CROP.png")

    boundary = Image.new("RGB", (w, crop_y1 - crop_y0), (255, 255, 255))
    boundary.paste(img.crop((0, crop_y0, w, crop_y1)), (0, 0))
    draw = ImageDraw.Draw(boundary)
    lines = [
        (reviews_end_y - crop_y0, "reviews_end"),
        (next_section_start_y - crop_y0, "next_start"),
        (next_section_content_start_y - crop_y0, "content_start"),
        (next_section_content_end_y - crop_y0, "content_end"),
        (next_section_end_y - crop_y0, "next_end"),
        (following_section_start_y - crop_y0, "following_start"),
    ]
    for y_line, label in lines:
        if 0 <= y_line < boundary.height:
            draw.line([(0, y_line), (w, y_line)], fill=(255, 0, 0), width=2)
            draw.text((12, max(0, y_line + 4)), label, fill=(255, 0, 0))
    boundary.save(OUT_DIR / "FP-0002-V6-NEXT-SECTION-BOUNDARIES.png")

    content_map = boundary.copy()
    content_map.save(OUT_DIR / "FP-0002-V6-NEXT-SECTION-CONTENT-MAP.png")

    geometry = boundary.copy()
    gdraw = ImageDraw.Draw(geometry)
    gdraw.rectangle(
        [(48, next_section_start_y - crop_y0), (w - 48, cta_end - crop_y0)],
        outline=(0, 128, 255),
        width=2,
    )
    gdraw.rectangle(
        [(48, cta_start - crop_y0), (w - 48, cta_end - crop_y0)],
        outline=(0, 200, 0),
        width=2,
    )
    gdraw.rectangle(
        [(48, cta_end - crop_y0), (w - 48, next_section_end_y - crop_y0)],
        outline=(200, 100, 0),
        width=2,
    )
    geometry.save(OUT_DIR / "FP-0002-V6-NEXT-SECTION-GEOMETRY-MAP.png")

    interior_y0 = cta_end + 20
    interior_y1 = following_section_start_y - 8
    interior = img.crop((48, interior_y0, w - 48, interior_y1))
    asset_dir = ROOT / "src" / "img" / "content" / "rehabilitation-requirements"
    asset_dir.mkdir(parents=True, exist_ok=True)
    interior.save(asset_dir / "shpigovsky-interior-corridor.webp", quality=88)

    meta = {
        "mockup_path": str(MOCKUP),
        "mockup_sha256": sha256(MOCKUP),
        "boundaries": {
            "reviews_end_y": reviews_end_y,
            "next_section_start_y": next_section_start_y,
            "next_section_content_start_y": next_section_content_start_y,
            "next_section_content_end_y": next_section_content_end_y,
            "next_section_end_y": next_section_end_y,
            "following_section_start_y": following_section_start_y,
            "cta_band_start_y": cta_start,
            "cta_band_end_y": cta_end,
        },
        "semantic_identity": "home-rehabilitation-requirements",
        "boundary_confidence": "HIGH",
        "gate": {
            "reviews_end_lte_next_start": reviews_end_y <= next_section_start_y,
            "next_start_lt_content_end": next_section_start_y < next_section_content_end_y,
            "content_end_lte_next_end": next_section_content_end_y <= next_section_end_y,
            "next_end_lte_following_start": next_section_end_y <= following_section_start_y,
        },
    }
    (OUT_DIR / "FP-0002-V6-NEXT-SECTION-BOUNDARY-META.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
