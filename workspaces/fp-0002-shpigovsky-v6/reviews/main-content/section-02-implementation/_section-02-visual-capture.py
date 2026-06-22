"""FP-0002 V6 home section 02 — visual capture and comparison."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DIST_HTML = ROOT / "dist" / "index.html"
MOCKUP = (
    ROOT.parent
    / "website-factory-operations"
    / "FP-0002-SHPIGOVSKY"
    / "INCOMING"
    / "01_DESIGN"
    / "HOME-PAGE-FULL-MOCKUP.jpg"
)
AUDIT_DIR = ROOT / "reviews" / "main-content" / "section-02-audit"
OUT_DIR = ROOT / "reviews" / "main-content" / "section-02-implementation"
META = AUDIT_DIR / "FP-0002-V6-SECTION-02-BOUNDARY-META.json"


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
    if not MOCKUP.is_file():
        print(f"MISSING_MOCKUP: {MOCKUP}")
        return 2

    ensure_deps()
    import json

    from PIL import Image
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    meta = json.loads(META.read_text(encoding="utf-8"))
    b = meta["boundaries"]
    y0 = b["section_02_start_y"] - 24
    y1 = b["section_02_end_y"] + 24

    mockup = Image.open(MOCKUP).convert("RGB")
    mockup.crop((0, y0, mockup.width, y1)).save(OUT_DIR / "FP-0002-V6-SECTION-02-MOCKUP-REFERENCE.png")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1398, "height": 3200})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")

        section = page.locator(".home-founder-quote")
        section.screenshot(path=str(OUT_DIR / "FP-0002-V6-SECTION-02-DESKTOP.png"))

        s01 = page.locator(".home-recovery-intro")
        s02 = page.locator(".home-founder-quote")
        s01_box = s01.bounding_box()
        s02_box = s02.bounding_box()
        if s01_box and s02_box:
            clip_y = max(0, s01_box["y"] + s01_box["height"] - 80)
            clip_h = (s02_box["y"] + s02_box["height"]) - clip_y + 40
            page.screenshot(
                path=str(OUT_DIR / "FP-0002-V6-SECTION-01-TO-02.png"),
                clip={"x": 0, "y": clip_y, "width": 1398, "height": clip_h},
            )

        footer = page.locator(".site-footer")
        footer_box = footer.bounding_box()
        if s02_box and footer_box:
            clip_y = max(0, s02_box["y"] - 40)
            clip_h = min(1200, (footer_box["y"] + 120) - clip_y)
            page.screenshot(
                path=str(OUT_DIR / "FP-0002-V6-SECTION-02-TO-03.png"),
                clip={"x": 0, "y": clip_y, "width": 1398, "height": clip_h},
            )

        if s01_box and footer_box:
            clip_y = max(0, s01_box["y"] + s01_box["height"] - 120)
            clip_h = min(1800, footer_box["y"] - clip_y + 80)
            page.screenshot(
                path=str(OUT_DIR / "FP-0002-V6-SECTION-02-FULL-CONTEXT.png"),
                clip={"x": 0, "y": clip_y, "width": 1398, "height": clip_h},
            )

        overflow = page.evaluate(
            """() => ({
              doc: document.documentElement.scrollWidth - document.documentElement.clientWidth,
              body: document.body.scrollWidth - document.body.clientWidth
            })"""
        )
        page.set_viewport_size({"width": 390, "height": 2400})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        overflow_mobile = page.evaluate(
            """() => ({
              doc: document.documentElement.scrollWidth - document.documentElement.clientWidth,
              body: document.body.scrollWidth - document.body.clientWidth
            })"""
        )
        browser.close()

    render = Image.open(OUT_DIR / "FP-0002-V6-SECTION-02-DESKTOP.png").convert("RGB")
    reference = Image.open(OUT_DIR / "FP-0002-V6-SECTION-02-MOCKUP-REFERENCE.png").convert("RGB")
    target_h = max(render.height, reference.height)
    canvas_w = render.width + reference.width + 20
    canvas = Image.new("RGB", (canvas_w, target_h), (240, 244, 248))
    canvas.paste(reference, (0, 0))
    canvas.paste(render, (reference.width + 20, 0))
    canvas.save(OUT_DIR / "FP-0002-V6-SECTION-02-COMPARISON.png")

    print(f"DESKTOP_OVERFLOW={max(overflow['doc'], overflow['body'])}")
    print(f"MOBILE_OVERFLOW={max(overflow_mobile['doc'], overflow_mobile['body'])}")
    print(f"CAPTURED in {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
