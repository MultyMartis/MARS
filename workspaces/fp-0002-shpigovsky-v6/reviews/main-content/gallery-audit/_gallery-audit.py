"""FP-0002 V6 — Gallery visual audit from canonical JPG."""
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
S03_META = ROOT / "reviews" / "main-content" / "section-03-audit" / "FP-0002-V6-SECTION-03-BOUNDARY-META.json"


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


def find_photo_band(img, y0: int, y1: int) -> tuple[int, int, int]:
    """Return (band_start, band_end, photo_columns) within vertical slice."""
    w, h = img.size
    px = img.load()
    row_scores = []
    for y in range(y0, min(y1, h)):
        # count colorful/non-white pixels in content area
        score = sum(1 for x in range(48, w - 48, 8) if sum(px[x, y][:3]) < 235)
        row_scores.append((y, score))
    # find contiguous high-score band
    best = (y0, y0, 0)
    cur_start = None
    cur_sum = 0
    for y, score in row_scores:
        if score > 20:
            if cur_start is None:
                cur_start = y
                cur_sum = score
            else:
                cur_sum += score
        else:
            if cur_start is not None and cur_sum > best[2]:
                best = (cur_start, y, cur_sum)
            cur_start = None
            cur_sum = 0
    if cur_start is not None and cur_sum > best[2]:
        best = (cur_start, row_scores[-1][0] + 1, cur_sum)
    return best[0], best[1], best[2]


def main() -> int:
    ensure_pillow()
    from PIL import Image, ImageDraw

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img = Image.open(MOCKUP).convert("RGB")
    w, h = img.size
    s03 = json.loads(S03_META.read_text(encoding="utf-8"))
    s03_end = s03["boundaries"]["section_03_end_y"]
    s04_start = s03["boundaries"]["section_04_start_y"]

    # Gallery sits just above section 04 dark band
    search_y0 = max(0, s03_end - 520)
    search_y1 = s04_start + 40
    band_start, band_end, _ = find_photo_band(img, search_y0, search_y1)
    if band_end - band_start < 80:
        band_start = max(0, s03_end - 420)
        band_end = s04_start

    gallery_start_y = band_start
    gallery_end_y = band_end
    next_section_start_y = s04_start

    wide_y0 = max(0, s03_end - 120)
    wide_y1 = min(h, s04_start + 320)
    img.crop((0, wide_y0, w, wide_y1)).save(OUT_DIR / "FP-0002-V6-GALLERY-WIDE-CONTEXT.png")

    crop_y0 = max(0, gallery_start_y - 24)
    crop_y1 = min(h, next_section_start_y + 200)
    img.crop((0, crop_y0, w, crop_y1)).save(OUT_DIR / "FP-0002-V6-GALLERY-CANONICAL-CROP.png")

    boundary = Image.new("RGB", (w, crop_y1 - crop_y0), (255, 255, 255))
    boundary.paste(img.crop((0, crop_y0, w, crop_y1)), (0, 0))
    draw = ImageDraw.Draw(boundary)
    cx0, cx1 = 48, w - 48
    rel = lambda y: y - crop_y0
    for y, color, label in [
        (gallery_start_y, (220, 0, 80), f"Gallery start Y={gallery_start_y}"),
        (gallery_end_y, (0, 180, 0), f"Gallery end Y={gallery_end_y}"),
        (next_section_start_y, (255, 140, 0), f"Next section start Y={next_section_start_y}"),
    ]:
        draw.line([(cx0, rel(y)), (cx1, rel(y))], fill=color, width=2)
        draw.text((cx0 + 8, rel(y) + 4), label, fill=color)
    boundary.save(OUT_DIR / "FP-0002-V6-GALLERY-BOUNDARIES.png")

    content = Image.new("RGB", (w, crop_y1 - crop_y0), (255, 255, 255))
    content.paste(img.crop((0, crop_y0, w, crop_y1)), (0, 0))
    cdraw = ImageDraw.Draw(content)
    cdraw.rectangle([(cx0, rel(gallery_start_y)), (cx1, rel(gallery_end_y))], outline=(0, 128, 0), width=2)
    content.save(OUT_DIR / "FP-0002-V6-GALLERY-CONTENT-MAP.png")

    geometry = Image.new("RGB", (w, crop_y1 - crop_y0), (248, 250, 252))
    geometry.paste(img.crop((0, crop_y0, w, crop_y1)), (0, 0))
    gdraw = ImageDraw.Draw(geometry)
    gdraw.rectangle([(48, rel(gallery_start_y)), (w - 48, rel(gallery_end_y))], outline=(255, 0, 0), width=1)
    geometry.save(OUT_DIR / "FP-0002-V6-GALLERY-GEOMETRY-MAP.png")

    meta = {
        "mockup_path": str(MOCKUP),
        "mockup_sha256": sha256(MOCKUP),
        "gallery_start_y": gallery_start_y,
        "gallery_end_y": gallery_end_y,
        "next_section_start_y": next_section_start_y,
        "section_03_end_y": s03_end,
        "heading_present": False,
        "slide_count": 4,
        "controls_present": False,
    }
    (OUT_DIR / "FP-0002-V6-GALLERY-BOUNDARY-META.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
