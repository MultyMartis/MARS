"""FP-0002 V6 — Section 03 visual audit from canonical JPG only."""
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
S02_META = ROOT / "reviews" / "main-content" / "section-02-audit" / "FP-0002-V6-SECTION-02-BOUNDARY-META.json"


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


def find_section04_start(img, search_from: int = 2610) -> tuple[int, str]:
    w, h = img.size
    px = img.load()
    for y in range(search_from, min(h, 5200)):
        dark = sum(1 for x in range(80, w - 80, 40) if sum(px[x, y][:3]) < 180)
        if dark > 8:
            band = 0
            for yy in range(y, min(h, y + 120)):
                if sum(1 for x in range(80, w - 80, 40) if sum(px[x, yy][:3]) < 180) > 6:
                    band += 1
            if band > 40:
                return y, f"Large dark heading band at Y={y}"
    return 4120, "Fallback Section 04 Y from prior audit"


def main() -> int:
    ensure_pillow()
    from PIL import Image, ImageDraw, ImageFont

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img = Image.open(MOCKUP).convert("RGB")
    w, h = img.size

    s02 = json.loads(S02_META.read_text(encoding="utf-8"))
    s03_start = s02["boundaries"]["section_03_start_y"]
    s03_content_start = s03_start + 24
    s04_start, s04_ev = find_section04_start(img, s03_start + 200)

    # content end = last ink before section 04 whitespace
    px = img.load()
    s03_content_end = s04_start - 24
    for y in range(s04_start - 1, s03_start, -1):
        if any(sum(px[x, y][:3]) < 240 for x in range(48, w - 48, 20)):
            s03_content_end = y + 8
            break

    s03_end = s04_start

    wide_y0 = max(0, s02["boundaries"]["section_02_end_y"] - 40)
    wide_y1 = min(h, s04_start + 40)
    img.crop((0, wide_y0, w, wide_y1)).save(OUT_DIR / "FP-0002-V6-SECTION-03-WIDE-CONTEXT.png")

    crop_y0 = max(0, s03_start - 24)
    crop_y1 = min(h, s04_start + 24)
    img.crop((0, crop_y0, w, crop_y1)).save(OUT_DIR / "FP-0002-V6-SECTION-03-CANONICAL-CROP.png")

    boundary = Image.new("RGB", (w, crop_y1 - crop_y0), (255, 255, 255))
    boundary.paste(img.crop((0, crop_y0, w, crop_y1)), (0, 0))
    draw = ImageDraw.Draw(boundary)
    cx0, cx1 = 48, w - 48
    rel = lambda y: y - crop_y0
    for y, color, label in [
        (s03_start, (220, 0, 80), f"S03 start Y={s03_start}"),
        (s03_content_start, (0, 180, 0), f"S03 content start Y={s03_content_start}"),
        (s03_content_end, (0, 120, 255), f"S03 content end Y={s03_content_end}"),
        (s03_end, (255, 140, 0), f"S03 end / S04 start Y={s03_end}"),
    ]:
        draw.line([(cx0, rel(y)), (cx1, rel(y))], fill=color, width=2)
        draw.text((cx0 + 8, rel(y) + 4), label, fill=color)
    boundary.save(OUT_DIR / "FP-0002-V6-SECTION-03-BOUNDARIES.png")

    content = Image.new("RGB", (w, crop_y1 - crop_y0), (255, 255, 255))
    content.paste(img.crop((0, crop_y0, w, crop_y1)), (0, 0))
    cdraw = ImageDraw.Draw(content)
    cdraw.rectangle([(cx0, rel(s03_content_start)), (cx1, rel(s03_content_end))], outline=(0, 128, 0), width=2)
    content.save(OUT_DIR / "FP-0002-V6-SECTION-03-CONTENT-MAP.png")

    geometry = Image.new("RGB", (w, crop_y1 - crop_y0), (248, 250, 252))
    geometry.paste(img.crop((0, crop_y0, w, crop_y1)), (0, 0))
    gdraw = ImageDraw.Draw(geometry)
    gdraw.rectangle([(48, rel(s03_content_start)), (696, rel(s03_content_end))], outline=(255, 0, 0), width=1)
    gdraw.rectangle([(720, rel(s03_content_start)), (w - 48, rel(s03_content_end))], outline=(0, 0, 255), width=1)
    geometry.save(OUT_DIR / "FP-0002-V6-SECTION-03-GEOMETRY-MAP.png")

    meta = {
        "mockup_path": str(MOCKUP),
        "mockup_sha256": sha256(MOCKUP),
        "width_px": w,
        "height_px": h,
        "boundaries": {
            "section_02_end_y": s02["boundaries"]["section_02_end_y"],
            "section_03_start_y": s03_start,
            "section_03_content_start_y": s03_content_start,
            "section_03_content_end_y": s03_content_end,
            "section_03_end_y": s03_end,
            "section_04_start_y": s04_start,
            "section_04_evidence": s04_ev,
        },
        "decorative_excluded": ["service grid photos unless proven content-critical"],
        "content_image_count": 0,
    }
    (OUT_DIR / "FP-0002-V6-SECTION-03-BOUNDARY-META.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(meta["boundaries"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
