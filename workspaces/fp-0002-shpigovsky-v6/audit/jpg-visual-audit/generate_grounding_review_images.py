#!/usr/bin/env python3
"""Generate grounding review images from JPG + existing block boundaries. JPG only."""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parents[1]
JPG = Path(
    r"C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN\HOME-PAGE-FULL-MOCKUP.jpg"
)
AUDIT_JSON = ROOT / "FP-0002-V6-JPG-AUDIT.json"
OUT_DIR = ROOT / "review"
CROP_PAD = 180
THUMB_WIDTH = 600


def load_blocks() -> list[dict]:
    data = json.loads(AUDIT_JSON.read_text(encoding="utf-8"))
    blocks = data["blocks"]
    # normalize last block to image height (exclusive end)
    if blocks[-1]["y_end"] < data["source"]["height"]:
        blocks[-1]["y_end"] = data["source"]["height"]
        blocks[-1]["height"] = blocks[-1]["y_end"] - blocks[-1]["y_start"]
    return blocks, data["source"]["height"], data["source"]["width"]


def try_font(size: int = 14):
    for name in ("arial.ttf", "Arial.ttf", "segoeui.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def make_full_page_with_boundaries(im: Image.Image, blocks: list[dict], out: Path) -> None:
    w, h = im.size
    scale = THUMB_WIDTH / w
    thumb_h = int(h * scale)
    thumb = im.resize((THUMB_WIDTH, thumb_h), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(thumb)
    font = try_font(11)
    boundaries = [b["y_start"] for b in blocks] + [blocks[-1]["y_end"]]
    colors = ["#e53935", "#1e88e5", "#43a047", "#fb8c00"]
    for i, y in enumerate(boundaries):
        ty = int(y * scale)
        color = colors[i % len(colors)]
        draw.line([(0, ty), (THUMB_WIDTH - 1, ty)], fill=color, width=1)
        label = f"Y={y}"
        if i < len(blocks):
            label = f"{blocks[i]['id']} {label}"
        draw.text((4, min(ty + 2, thumb_h - 14)), label, fill=color, font=font)
    thumb.save(out, quality=92, optimize=True)


def make_contact_sheet(im: Image.Image, blocks: list[dict], out: Path) -> None:
    w, h = im.size
    font = try_font(13)
    font_sm = try_font(11)
    boundaries: list[tuple[int, str, str]] = []
    for i in range(len(blocks) - 1):
        y = blocks[i + 1]["y_start"]
        prev_id = blocks[i]["id"]
        next_id = blocks[i + 1]["id"]
        boundaries.append((y, prev_id, next_id))

    crops: list[Image.Image] = []
    sheet_w = w
    for y, prev_id, next_id in boundaries:
        y0 = max(0, y - CROP_PAD)
        y1 = min(h, y + CROP_PAD)
        crop = im.crop((0, y0, w, y1))
        canvas = Image.new("RGB", (sheet_w, crop.height + 36), (245, 247, 250))
        canvas.paste(crop, (0, 36))
        d = ImageDraw.Draw(canvas)
        d.text((8, 8), f"BND Y={y}  |  {prev_id} -> {next_id}", fill=(30, 30, 30), font=font)
        d.line([(0, 36 + CROP_PAD), (sheet_w, 36 + CROP_PAD)], fill=(229, 57, 53), width=2)
        crops.append(canvas)

    total_h = sum(c.height for c in crops)
    sheet = Image.new("RGB", (sheet_w, total_h), (255, 255, 255))
    y_off = 0
    for c in crops:
        sheet.paste(c, (0, y_off))
        y_off += c.height
    # downscale if extremely tall
    if sheet.height > 32000:
        scale = 32000 / sheet.height
        sheet = sheet.resize((int(sheet_w * scale), 32000), Image.Resampling.LANCZOS)
    sheet.save(out, quality=90, optimize=True)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    blocks, img_h, img_w = load_blocks()
    im = Image.open(JPG).convert("RGB")
    assert im.size == (img_w, img_h), f"size mismatch {im.size} vs {img_w}x{img_h}"
    make_full_page_with_boundaries(
        im, blocks, OUT_DIR / "FP-0002-V6-FULL-PAGE-WITH-BOUNDARIES.jpg"
    )
    make_contact_sheet(im, blocks, OUT_DIR / "FP-0002-V6-BOUNDARY-CONTACT-SHEET.jpg")
    print("Wrote review images to", OUT_DIR)


if __name__ == "__main__":
    main()
