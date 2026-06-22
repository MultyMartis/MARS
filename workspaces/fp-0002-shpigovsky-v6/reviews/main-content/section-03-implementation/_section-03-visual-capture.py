"""FP-0002 V6 home section 03 — visual capture and comparison."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DIST_HTML = ROOT / "dist" / "index.html"
AUDIT_DIR = ROOT / "reviews" / "main-content" / "section-03-audit"
OUT_DIR = ROOT / "reviews" / "main-content" / "section-03-implementation"
META = AUDIT_DIR / "FP-0002-V6-SECTION-03-BOUNDARY-META.json"


def ensure_deps() -> None:
    try:
        from PIL import Image  # noqa: F401
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def main() -> int:
    if not DIST_HTML.is_file():
        print(f"MISSING_BUILD: {DIST_HTML}")
        return 2

    ensure_deps()
    from PIL import Image
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    meta = json.loads(META.read_text(encoding="utf-8"))
    b = meta["boundaries"]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1398, "height": 4200})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")

        section = page.locator(".home-treatment-prevention")
        section.screenshot(path=str(OUT_DIR / "FP-0002-V6-SECTION-03-DESKTOP.png"))

        s02 = page.locator(".home-founder-quote")
        s03 = page.locator(".home-treatment-prevention")
        s02_box = s02.bounding_box()
        s03_box = s03.bounding_box()
        if s02_box and s03_box:
            clip_y = max(0, s02_box["y"] + s02_box["height"] - 80)
            clip_h = (s03_box["y"] + s03_box["height"]) - clip_y + 40
            page.screenshot(
                path=str(OUT_DIR / "FP-0002-V6-SECTION-02-TO-03.png"),
                clip={"x": 0, "y": clip_y, "width": 1398, "height": clip_h},
            )

        footer = page.locator(".site-footer")
        footer_box = footer.bounding_box()
        if s03_box and footer_box:
            clip_y = max(0, s03_box["y"] - 40)
            clip_h = min(1400, footer_box["y"] - clip_y + 120)
            page.screenshot(
                path=str(OUT_DIR / "FP-0002-V6-SECTION-03-TO-04.png"),
                clip={"x": 0, "y": clip_y, "width": 1398, "height": clip_h},
            )

        if s02_box and footer_box:
            clip_y = max(0, s02_box["y"] + s02_box["height"] - 120)
            clip_h = min(2200, footer_box["y"] - clip_y + 80)
            page.screenshot(
                path=str(OUT_DIR / "FP-0002-V6-SECTION-03-FULL-CONTEXT.png"),
                clip={"x": 0, "y": clip_y, "width": 1398, "height": clip_h},
            )

        overflow = page.evaluate(
            """() => ({
              doc: document.documentElement.scrollWidth - document.documentElement.clientWidth,
              body: document.body.scrollWidth - document.body.clientWidth
            })"""
        )
        page.set_viewport_size({"width": 390, "height": 3200})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        overflow_mobile = page.evaluate(
            """() => ({
              doc: document.documentElement.scrollWidth - document.documentElement.clientWidth,
              body: document.body.scrollWidth - document.body.clientWidth
            })"""
        )
        browser.close()

    reference = Image.open(AUDIT_DIR / "FP-0002-V6-SECTION-03-CANONICAL-CROP.png").convert("RGB")
    render = Image.open(OUT_DIR / "FP-0002-V6-SECTION-03-DESKTOP.png").convert("RGB")
    target_h = max(render.height, reference.height)
    canvas = Image.new("RGB", (render.width + reference.width + 20, target_h), (240, 244, 248))
    canvas.paste(reference, (0, 0))
    canvas.paste(render, (reference.width + 20, 0))
    canvas.save(OUT_DIR / "FP-0002-V6-SECTION-03-COMPARISON.png")

    print(f"DESKTOP_OVERFLOW={max(overflow['doc'], overflow['body'])}")
    print(f"MOBILE_OVERFLOW={max(overflow_mobile['doc'], overflow_mobile['body'])}")
    print(f"CAPTURED in {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
