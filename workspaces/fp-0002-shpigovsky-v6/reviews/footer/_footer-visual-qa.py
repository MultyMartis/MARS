"""Reproducible Footer desktop visual QA @ 1398px — FP-0002 V6."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
JPG = (
    ROOT.parent
    / "website-factory-operations"
    / "FP-0002-SHPIGOVSKY"
    / "INCOMING"
    / "01_DESIGN"
    / "HOME-PAGE-FULL-MOCKUP.jpg"
)
OUT_DIR = Path(__file__).resolve().parent / "visual"
OUT_FOOTER = OUT_DIR / "FP-0002-V6-FOOTER-DESKTOP-RENDER-01.png"
OUT_FULL = OUT_DIR / "FP-0002-V6-HEADER-HERO-FOOTER-DESKTOP-RENDER-01.png"
OUT_JSON = Path(__file__).resolve().parent / "_qa-footer-metrics.json"
VIEWPORT_W = 1398
VIEWPORT_H = 2200


def ensure_playwright() -> None:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def mae_rgb(a, b) -> float:
    from PIL import Image

    if a.size != b.size:
        b = b.resize(a.size)
    px_a = a.convert("RGB")
    px_b = b.convert("RGB")
    w, h = px_a.size
    total = 0.0
    for y in range(h):
        for x in range(w):
            ra, ga, ba = px_a.getpixel((x, y))
            rb, gb, bb = px_b.getpixel((x, y))
            total += abs(ra - rb) + abs(ga - gb) + abs(ba - bb)
    return total / (w * h * 3)


def main() -> int:
    if not DIST_HTML.is_file():
        print(f"MISSING_BUILD: {DIST_HTML}")
        return 2
    if not JPG.is_file():
        print(f"MISSING_JPG: {JPG}")
        return 2

    ensure_playwright()
    from PIL import Image
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    url = DIST_HTML.as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": VIEWPORT_W, "height": VIEWPORT_H})
        page.goto(url, wait_until="networkidle")
        page.screenshot(path=str(OUT_FULL), full_page=True)

        footer = page.locator(".site-footer")
        footer.screenshot(path=str(OUT_FOOTER))
        footer_box = footer.bounding_box()
        browser.close()

    jpg = Image.open(JPG)
    ref_footer = jpg.crop((0, 15776, VIEWPORT_W, 16343))
    shot_footer = Image.open(OUT_FOOTER)

    compare_h = min(ref_footer.height, shot_footer.height)
    ref_crop = ref_footer.crop((0, 0, VIEWPORT_W, compare_h))
    shot_crop = shot_footer.crop((0, 0, min(VIEWPORT_W, shot_footer.width), compare_h))

    metrics = {
        "viewport": {"width": VIEWPORT_W, "height": VIEWPORT_H},
        "footer_bounding_box": footer_box,
        "screenshots": {
            "footer": str(OUT_FOOTER.relative_to(ROOT)).replace("\\", "/"),
            "header_hero_footer": str(OUT_FULL.relative_to(ROOT)).replace("\\", "/"),
        },
        "jpg_reference": {
            "footer_crop": {"x": 0, "y": 15776, "w": VIEWPORT_W, "h": 567},
        },
        "mae": {
            "footer_top_region": round(mae_rgb(ref_crop, shot_crop), 2),
        },
    }
    OUT_JSON.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metrics, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
