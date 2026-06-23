"""FP-0002 V6 — lower-home six corrections screenshots."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST_HTML = ROOT / "dist" / "index.html"
OUT = ROOT / "reviews" / "main-content" / "lower-home-corrections"


def ensure_deps() -> None:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def main() -> int:
    if not DIST_HTML.is_file():
        print(f"MISSING_BUILD: {DIST_HTML}")
        return 2

    ensure_deps()
    from playwright.sync_api import sync_playwright

    OUT.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        def shot(selector: str, name: str, width: int, height: int = 900) -> None:
            page.set_viewport_size({"width": width, "height": height})
            page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
            page.locator(selector).scroll_into_view_if_needed()
            page.locator(selector).screenshot(path=str(OUT / name))

        shot(".home-rehabilitation-program__directions", "PROGRAM-DIRECTIONS-DESKTOP.png", 1398)
        shot(".home-rehabilitation-program__directions", "PROGRAM-DIRECTIONS-MOBILE-390.png", 390)

        shot(".home-comfort__gallery", "COMFORT-FANCYBOX-GALLERY-DESKTOP.png", 1398)
        shot(".home-comfort__gallery", "COMFORT-GALLERY-MOBILE-390.png", 390)

        page.set_viewport_size({"width": 1398, "height": 900})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        page.locator('.home-comfort__gallery-item[data-fancybox="home-comfort"]').first.click()
        page.wait_for_timeout(600)
        page.screenshot(path=str(OUT / "COMFORT-FANCYBOX-OPEN.png"), full_page=False)

        shot(".home-videos__grid", "VIDEOS-TWO-CARDS-DESKTOP.png", 1398)
        shot(".home-videos__grid", "VIDEOS-TWO-CARDS-MOBILE-390.png", 390)

        shot(".home-specialists", "SPECIALISTS-SWIPER-DESKTOP.png", 1398)
        shot(".home-specialists", "SPECIALISTS-SWIPER-MOBILE-390.png", 390)

        page.set_viewport_size({"width": 1398, "height": 900})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        slider = page.locator("[data-specialists-slider]")
        box = slider.bounding_box()
        if box:
            page.mouse.move(box["x"] + box["width"] * 0.8, box["y"] + box["height"] / 2)
            page.mouse.down()
            page.mouse.move(box["x"] + box["width"] * 0.2, box["y"] + box["height"] / 2, steps=12)
            page.mouse.up()
            page.wait_for_timeout(400)
            slider.screenshot(path=str(OUT / "SPECIALISTS-SWIPER-AFTER-DRAG.png"))

        shot(".home-faq", "FAQ-OWN-DESIGN-DESKTOP.png", 1398)
        shot(".home-faq", "FAQ-OWN-DESIGN-MOBILE-390.png", 390)

        page.set_viewport_size({"width": 1398, "height": 900})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        page.locator(".home-faq__question").first.click()
        page.wait_for_timeout(300)
        page.locator(".home-faq__item").first.screenshot(path=str(OUT / "FAQ-OPEN-ITEM.png"))

        shot(".home-final-form", "FINAL-FORM-DESKTOP.png", 1398)
        shot(".home-final-form", "FINAL-FORM-MOBILE-390.png", 390)

        page.set_viewport_size({"width": 1398, "height": 12000})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        page.screenshot(path=str(OUT / "FULL-HOME-AFTER-CORRECTIONS.png"), full_page=True)

        browser.close()

    print(f"SCREENSHOTS_OK: {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
