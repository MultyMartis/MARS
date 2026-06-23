"""FP-0002 V6 home gallery — visual capture."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_DIR = ROOT / "reviews" / "main-content" / "gallery-implementation"


def ensure_deps() -> None:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def capture(page, width: int, height: int, name: str) -> None:
    page.set_viewport_size({"width": width, "height": height})
    page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
    gallery = page.locator(".home-gallery")
    gallery.screenshot(path=str(OUT_DIR / name))


def main() -> int:
    if not DIST_HTML.is_file():
        print(f"MISSING_BUILD: {DIST_HTML}")
        return 2

    ensure_deps()
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        capture(page, 1398, 900, "FP-0002-V6-GALLERY-DESKTOP.png")
        capture(page, 1024, 900, "FP-0002-V6-GALLERY-TABLET.png")
        capture(page, 375, 900, "FP-0002-V6-GALLERY-MOBILE-375.png")
        capture(page, 320, 900, "FP-0002-V6-GALLERY-MOBILE-320.png")

        page.set_viewport_size({"width": 1398, "height": 900})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        slider = page.locator("[data-gallery-slider]")
        box = slider.bounding_box()
        if box:
            page.mouse.move(box["x"] + box["width"] * 0.7, box["y"] + box["height"] / 2)
            page.mouse.down()
            page.mouse.move(box["x"] + box["width"] * 0.3, box["y"] + box["height"] / 2, steps=12)
            page.mouse.up()
            page.wait_for_timeout(400)
            slider.screenshot(path=str(OUT_DIR / "FP-0002-V6-GALLERY-SWIPE-AFTER.png"))

        page.set_viewport_size({"width": 1398, "height": 2400})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        s03 = page.locator(".home-treatment-prevention")
        why = page.locator(".home-why-us")
        s03_box = s03.bounding_box()
        why_box = why.bounding_box()
        if s03_box and why_box:
            clip_y = max(0, s03_box["y"] + s03_box["height"] - 40)
            clip_h = max(200, min(1200, why_box["y"] + 160 - clip_y))
            if clip_y + clip_h <= 2400:
                page.screenshot(
                    path=str(OUT_DIR / "FP-0002-V6-GALLERY-COMPARISON.png"),
                    clip={"x": 0, "y": clip_y, "width": 1398, "height": clip_h},
                )

        browser.close()

    print("CAPTURE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
