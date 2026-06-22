"""Reproducible Header desktop visual QA @ 1398px — FP-0002 V6 checkpoint."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
REF_CROP = ROOT / "specifications" / "section-001" / "evidence" / "02-header-estimate-band.jpg"
OUT_PNG = Path(__file__).resolve().parent / "_qa-header-render.png"
OUT_JSON = Path(__file__).resolve().parent / "_qa-header-metrics.json"
VIEWPORT_W, VIEWPORT_H = 1398, 200


def ensure_playwright():
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def mae_rgb(a, b):
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
    if not REF_CROP.is_file():
        print(f"MISSING_REF: {REF_CROP}")
        return 2

    ensure_playwright()
    from PIL import Image
    from playwright.sync_api import sync_playwright

    url = DIST_HTML.as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": VIEWPORT_W, "height": VIEWPORT_H})
        page.goto(url, wait_until="networkidle")
        page.screenshot(path=str(OUT_PNG), full_page=False)
        browser.close()

    ref = Image.open(REF_CROP)
    shot = Image.open(OUT_PNG)
    mae = round(mae_rgb(ref, shot), 2)
    metrics = {
        "viewport": {"width": VIEWPORT_W, "height": VIEWPORT_H},
        "reference": str(REF_CROP.relative_to(ROOT)).replace("\\", "/"),
        "screenshot": str(OUT_PNG.relative_to(ROOT)).replace("\\", "/"),
        "mae_per_channel": mae,
        "structural_pass_threshold": 25.0,
        "structural_pass": mae <= 25.0,
        "verdict": "STRUCTURAL PASS" if mae <= 25.0 else "REVIEW REQUIRED",
    }
    OUT_JSON.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metrics, indent=2))
    return 0 if metrics["structural_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
