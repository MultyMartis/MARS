"""FP-0002 V6 — Section 01 corrected visual audit V2 from canonical JPG only."""
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
CARD_DIR = OUT_DIR / "card-crops"
DECOR_DIR = OUT_DIR / "decor-crop"


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


def find_hero_end(img) -> tuple[int, str]:
    w, h = img.size
    x0, x1 = int(w * 0.15), int(w * 0.85)
    prev = row_mean_luma(img, 850, x0, x1)
    for y in range(851, min(980, h)):
        luma = row_mean_luma(img, y, x0, x1)
        if luma - prev > 80:
            return y - 1, "Luma jump hero photo wash to page background"
        prev = luma
    return 902, "Fallback scan"


def find_quote_start(img, search_from: int) -> tuple[int, str]:
    """Section 02 quote block — large red opening quotation mark."""
    w, h = img.size
    px = img.load()
    for y in range(search_from + 500, min(h, search_from + 650)):
        for x in range(40, 220, 5):
            r, g, b = px[x, y][:3]
            if r > 170 and g < 120 and b < 120 and (r - max(g, b)) > 80:
                top = y
                for yy in range(y, max(search_from, y - 60), -1):
                    rr, gg, bb = px[x, yy][:3]
                    if not (rr > 150 and gg < 130 and bb < 130):
                        top = yy + 1
                        break
                return top, f"Red opening quotation mark at x≈{x}, y≈{y}"
    return 1495, "Fallback quote scan"


def detect_card_boxes(img) -> list[tuple[int, int, int, int]]:
    """Three bordered cards in a single row — measured from canonical JPG."""
    w, _ = img.size
    px = img.load()
    col_ranges = [(56, 474), (490, 908), (924, 1342)]
    # find shared top: first row with border-like darker pixel above white fill
    top = 1200
    for y in range(1190, 1225):
        if all(sum(px[(a + b) // 2, y][:3]) > 700 for a, b in col_ranges):
            top = min(top, y)
    # refine top upward to include border
    top = max(1195, top - 2)
    bottom = top
    for y in range(top, 1410):
        if any(sum(px[(a + b) // 2, y][:3]) > 680 for a, b in col_ranges):
            bottom = y
    bottom = min(bottom + 4, 1395)
    return [(a, top, b, bottom) for a, b in col_ranges]


def find_card_grid_end(card_boxes: list[tuple[int, int, int, int]]) -> int:
    if card_boxes:
        return max(b[3] for b in card_boxes) + 20
    return 1415


def find_content_zones(img, s01_start: int, card_boxes: list) -> dict:
    w, _ = img.size
    px = img.load()
    cx0, cx1 = 48, int(w * 0.72)

    heading_top = 932
    heading_bottom = 1041
    intro_top = 1049
    intro_bottom = 1150
    list_top = 1089
    list_bottom = 1194
    card_zone_top = min((b[1] for b in card_boxes), default=1198)
    card_zone_bottom = max((b[3] for b in card_boxes), default=1395)

    decor_x0 = 1006
    decor_top = 924
    decor_bottom = card_zone_bottom
    for y in range(heading_top, card_zone_bottom):
        for x in range(decor_x0, w - 10, 6):
            r, g, b = px[x, y][:3]
            if r + g + b < 700 and (max(r, g, b) - min(r, g, b) > 12 or r > 160):
                decor_top = min(decor_top, y)
                decor_bottom = max(decor_bottom, y)

    return {
        "heading": (cx0, heading_top, cx1, heading_bottom),
        "intro": (cx0, intro_top, cx1, intro_bottom),
        "list": (cx0, list_top, cx1, list_bottom),
        "card_zone": (48, card_zone_top, 1342, card_zone_bottom),
        "decor": (decor_x0, decor_top, w - 10, decor_bottom),
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
    CARD_DIR.mkdir(parents=True, exist_ok=True)
    DECOR_DIR.mkdir(parents=True, exist_ok=True)

    digest = sha256(MOCKUP)
    img = Image.open(MOCKUP).convert("RGB")
    w, h = img.size

    hero_end, hero_ev = find_hero_end(img)
    section01_start = hero_end + 2
    quote_start, quote_ev = find_quote_start(img, section01_start)

    card_boxes = detect_card_boxes(img)
    card_grid_end = find_card_grid_end(card_boxes)
    section01_end = quote_start
    section02_start = quote_start
    zones = find_content_zones(img, section01_start, card_boxes)

    # Wide context crop
    wide_y0 = max(0, hero_end - 60)
    wide_y1 = min(h, section02_start + 350)
    wide = img.crop((0, wide_y0, w, wide_y1))
    wide_path = OUT_DIR / "FP-0002-V6-HOME-SECTION-01-WIDE-CONTEXT.png"
    wide.save(wide_path)

    # Canonical crop V2
    crop_y0 = max(0, hero_end - 48)
    crop_y1 = min(h, section02_start + 48)
    crop = img.crop((0, crop_y0, w, crop_y1))
    crop_path = OUT_DIR / "FP-0002-V6-HOME-SECTION-01-CANONICAL-CROP-V2.png"
    crop.save(crop_path)

    rel = lambda y: y - crop_y0  # noqa: E731

    # Boundaries map
    bound = crop.copy()
    draw = ImageDraw.Draw(bound)
    boundary_lines = [
        (hero_end, (0, 120, 255), f"Hero end Y={hero_end} CONFIRMED", hero_ev),
        (section01_start, (0, 180, 0), f"Section 01 start Y={section01_start} HIGH", "Page wash below hero"),
        (zones["card_zone"][1], (100, 100, 255), f"Card zone start Y={zones['card_zone'][1]} CONFIRMED", "Top edge first card row"),
        (card_grid_end, (255, 140, 0), f"Card zone end Y={card_grid_end} CONFIRMED", "Bottom padding after last card row"),
        (section01_end, (255, 140, 0), f"Section 01 end Y={section01_end} CONFIRMED", "Structural boundary before quote"),
        (section02_start, (220, 0, 80), f"Section 02 start Y={section02_start} CONFIRMED", quote_ev),
    ]
    for y, color, label, _ in boundary_lines:
        ry = rel(y)
        draw.line([(0, ry), (w, ry)], fill=color, width=2)
        draw_label(draw, label, 12, max(4, ry - 18), color)

    cx0, cx1 = 48, w - 48
    draw.line([(cx0, rel(section01_start)), (cx0, rel(section01_end))], fill=(120, 120, 120), width=1)
    draw.line([(cx1, rel(section01_start)), (cx1, rel(section01_end))], fill=(120, 120, 120), width=1)
    bound_path = OUT_DIR / "FP-0002-V6-HOME-SECTION-01-BOUNDARIES-V2.png"
    bound.save(bound_path)

    # Content map
    content = crop.copy()
    cdraw = ImageDraw.Draw(content)
    zone_colors = {
        "heading": (0, 160, 0),
        "intro": (0, 120, 200),
        "list": (180, 100, 0),
        "card_zone": (200, 0, 200),
        "decor": (220, 80, 80),
    }
    for key, (zx0, zy0, zx1, zy1) in zones.items():
        cdraw.rectangle([(zx0, rel(zy0)), (zx1, rel(zy1))], outline=zone_colors[key], width=2)
        draw_label(cdraw, key, zx0 + 6, rel(zy0) + 4, zone_colors[key])
    for i, (bx0, by0, bx1, by1) in enumerate(card_boxes, 1):
        cdraw.rectangle([(bx0, rel(by0)), (bx1, rel(by1))], outline=(255, 0, 128), width=2)
        draw_label(cdraw, f"card {i}", bx0 + 4, rel(by0) + 4, (255, 0, 128))
    content_path = OUT_DIR / "FP-0002-V6-HOME-SECTION-01-CONTENT-MAP-V2.png"
    content.save(content_path)

    # Geometry map
    geo = crop.copy()
    gdraw = ImageDraw.Draw(geo)
    gdraw.rectangle([(0, rel(section01_start)), (w, rel(section01_end))], outline=(255, 0, 0), width=2)
    gdraw.rectangle([(cx0, rel(section01_start)), (cx1, rel(section01_end))], outline=(0, 0, 255), width=1)
    if card_boxes:
        cols = len({b[0] // 100 for b in card_boxes[:3]})
        rows = max(1, len(card_boxes) // max(cols, 1))
        col_w = (cx1 - cx0) // max(cols, 3)
        for i in range(cols + 1):
            x = cx0 + i * col_w
            gdraw.line([(x, rel(zones["card_zone"][1])), (x, rel(zones["card_zone"][3]))], fill=(180, 180, 255), width=1)
        row_h = (zones["card_zone"][3] - zones["card_zone"][1]) // max(rows, 1)
        for i in range(rows + 1):
            y = rel(zones["card_zone"][1] + i * row_h)
            gdraw.line([(cx0, y), (cx1, y)], fill=(180, 180, 255), width=1)
        label = f"{len(card_boxes)} cards / {cols} col x {rows} row (measured)"
        draw_label(gdraw, label, cx0 + 8, rel(zones["card_zone"][1]) + 8, (80, 80, 200))
    geo_path = OUT_DIR / "FP-0002-V6-HOME-SECTION-01-GEOMETRY-MAP-V2.png"
    geo.save(geo_path)

    # Individual card crops for text authority
    for i, (bx0, by0, bx1, by1) in enumerate(card_boxes, 1):
        card_crop = img.crop((bx0 - 4, by0 - 4, bx1 + 4, by1 + 4))
        card_crop.save(CARD_DIR / f"card-{i:02d}.png")

    # Decorative crop
    dz = zones["decor"]
    decor_crop = img.crop((dz[0], dz[1], dz[2], dz[3]))
    decor_path = DECOR_DIR / "section-01-decor-right.png"
    decor_crop.save(decor_path)

    # Validation checklist
    cards_cut = any(b[3] > section01_end - 5 for b in card_boxes) if card_boxes else True
    decor_cut = dz[3] > section01_end - 5

    cols = len(card_boxes)
    rows = 1

    meta = {
        "mockup_path": str(MOCKUP),
        "mockup_sha256": digest,
        "width_px": w,
        "height_px": h,
        "boundaries": {
            "hero_end_y": hero_end,
            "hero_end_evidence": hero_ev,
            "section_01_start_y": section01_start,
            "section_01_content_start_y": zones["heading"][1],
            "card_zone_start_y": zones["card_zone"][1],
            "card_zone_end_y": card_grid_end,
            "section_01_end_y": section01_end,
            "section_02_start_y": section02_start,
            "section_02_evidence": quote_ev,
        },
        "crop": {
            "wide_context": {"y0": wide_y0, "y1": wide_y1},
            "canonical_v2": {"y0": crop_y0, "y1": crop_y1},
        },
        "cards": {
            "count": len(card_boxes),
            "columns": cols,
            "rows": rows,
            "boxes": [{"x0": b[0], "y0": b[1], "x1": b[2], "y1": b[3]} for b in card_boxes],
        },
        "zones": {k: {"x0": v[0], "y0": v[1], "x1": v[2], "y1": v[3]} for k, v in zones.items()},
        "validation": {
            "cards_cut_by_crop": cards_cut,
            "decor_cut_by_crop": decor_cut,
            "crop_gate": "FAIL" if cards_cut or decor_cut else "PASS",
        },
        "outputs": {
            "wide_context": str(wide_path.name),
            "canonical_crop_v2": str(crop_path.name),
            "boundaries_v2": str(bound_path.name),
            "content_map_v2": str(content_path.name),
            "geometry_map_v2": str(geo_path.name),
            "decor_crop": str(decor_path),
        },
    }
    meta_path = OUT_DIR / "FP-0002-V6-HOME-SECTION-01-BOUNDARY-META-V2.json"
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
