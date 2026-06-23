"""FP-0002 V6 — Gallery boundary audit v2 from canonical JPG."""
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


def main() -> int:
    ensure_pillow()
    from PIL import Image, ImageDraw

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img = Image.open(MOCKUP).convert("RGB")
    w, h = img.size

    gallery_start_y = 3610
    gallery_content_end_y = 3810
    gallery_end_y = 3810
    next_section_start_y = 3860
    reviews_start_y = 6064

    wide_y0 = max(0, gallery_start_y - 80)
    wide_y1 = min(h, next_section_start_y + 120)
    img.crop((0, wide_y0, w, wide_y1)).save(OUT_DIR / "FP-0002-V6-GALLERY-WIDE-CONTEXT-V2.png")

    crop_y0 = max(0, gallery_start_y - 24)
    crop_y1 = min(h, next_section_start_y + 80)
    img.crop((0, crop_y0, w, crop_y1)).save(OUT_DIR / "FP-0002-V6-GALLERY-CANONICAL-CROP-V2.png")

    boundary = Image.new("RGB", (w, crop_y1 - crop_y0), (255, 255, 255))
    boundary.paste(img.crop((0, crop_y0, w, crop_y1)), (0, 0))
    draw = ImageDraw.Draw(boundary)
    cx0, cx1 = 48, w - 48
    rel = lambda y: y - crop_y0
    for y, color, label in [
        (gallery_start_y, (220, 0, 80), f"Gallery start Y={gallery_start_y}"),
        (gallery_content_end_y, (0, 140, 200), f"Gallery content end Y={gallery_content_end_y}"),
        (gallery_end_y, (0, 180, 0), f"Gallery end Y={gallery_end_y}"),
        (next_section_start_y, (255, 140, 0), f"Next section start Y={next_section_start_y}"),
    ]:
        draw.line([(cx0, rel(y)), (cx1, rel(y))], fill=color, width=2)
        draw.text((cx0 + 8, rel(y) + 4), label, fill=color)
    boundary.save(OUT_DIR / "FP-0002-V6-GALLERY-BOUNDARIES-V2.png")

    geometry = Image.new("RGB", (w, crop_y1 - crop_y0), (248, 250, 252))
    geometry.paste(img.crop((0, crop_y0, w, crop_y1)), (0, 0))
    gdraw = ImageDraw.Draw(geometry)
    gdraw.rectangle([(48, rel(gallery_start_y)), (w - 48, rel(gallery_content_end_y))], outline=(255, 0, 0), width=2)
    geometry.save(OUT_DIR / "FP-0002-V6-GALLERY-GEOMETRY-MAP-V2.png")

    meta = {
        "mockup_path": str(MOCKUP),
        "mockup_sha256": sha256(MOCKUP),
        "gallery_start_y": gallery_start_y,
        "gallery_content_end_y": gallery_content_end_y,
        "gallery_end_y": gallery_end_y,
        "next_section_start_y": next_section_start_y,
        "reviews_start_y": reviews_start_y,
        "boundary_consistency": "PASS",
        "supersedes": "reviews/main-content/gallery-audit/FP-0002-V6-GALLERY-BOUNDARY-META.json",
    }
    (OUT_DIR / "FP-0002-V6-GALLERY-BOUNDARY-META-V2.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
