"""FP-0002 V6 — pre-reviews image fix and reviews implementation captures."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST_HTML = ROOT / "dist" / "index.html"
IMAGE_OUT = ROOT / "reviews" / "main-content" / "pre-reviews-image-fix"
REVIEWS_OUT = ROOT / "reviews" / "main-content" / "reviews-implementation"


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

    IMAGE_OUT.mkdir(parents=True, exist_ok=True)
    REVIEWS_OUT.mkdir(parents=True, exist_ok=True)

    metrics: dict[str, object] = {}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for width, staff_suffix, land_suffix in [
            (1398, "DESKTOP", "DESKTOP"),
            (390, "MOBILE", "MOBILE"),
        ]:
            page.set_viewport_size({"width": width, "height": 900})
            page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
            page.locator(".home-staff-photo").screenshot(
                path=str(IMAGE_OUT / f"FP-0002-V6-STAFF-IMAGE-FIX-{staff_suffix}.png")
            )
            page.locator(".home-clinic-landscape").screenshot(
                path=str(IMAGE_OUT / f"FP-0002-V6-CLINIC-LANDSCAPE-FIX-{land_suffix}.png")
            )

        for width, suffix in [
            (1398, "DESKTOP"),
            (768, "TABLET"),
            (390, "MOBILE-390"),
            (320, "MOBILE-320"),
        ]:
            page.set_viewport_size({"width": width, "height": 900})
            page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
            page.locator(".home-reviews").screenshot(
                path=str(REVIEWS_OUT / f"FP-0002-V6-REVIEWS-{suffix}.png")
            )

        page.set_viewport_size({"width": 1398, "height": 900})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        slider = page.locator("[data-reviews-slider]")
        box = slider.bounding_box()
        if box:
            page.mouse.move(box["x"] + box["width"] * 0.75, box["y"] + box["height"] / 2)
            page.mouse.down()
            page.mouse.move(box["x"] + box["width"] * 0.25, box["y"] + box["height"] / 2, steps=12)
            page.mouse.up()
            page.wait_for_timeout(400)
            slider.screenshot(path=str(REVIEWS_OUT / "FP-0002-V6-REVIEWS-AFTER-DRAG.png"))

        page.set_viewport_size({"width": 1398, "height": 9000})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        landscape = page.locator(".home-clinic-landscape")
        reviews = page.locator(".home-reviews")
        land_box = landscape.bounding_box()
        rev_box = reviews.bounding_box()
        if land_box and rev_box:
            clip_y = max(0, int(land_box["y"] - 40))
            clip_h = min(9000, int(rev_box["y"] + rev_box["height"] + 40 - clip_y))
            page.screenshot(
                path=str(REVIEWS_OUT / "FP-0002-V6-PRE-REVIEWS-TO-REVIEWS-CONTEXT.png"),
                clip={"x": 0, "y": clip_y, "width": 1398, "height": clip_h},
            )

        mockup = Path(
            r"C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN\HOME-PAGE-FULL-MOCKUP.jpg"
        )
        if mockup.is_file():
            from PIL import Image

            im = Image.open(mockup)
            im.crop((0, 5980, 1398, 6460)).save(REVIEWS_OUT / "FP-0002-V6-REVIEWS-COMPARISON-MOCKUP.jpg", quality=92)
            page.set_viewport_size({"width": 1398, "height": 900})
            page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
            page.locator(".home-reviews").screenshot(path=str(REVIEWS_OUT / "FP-0002-V6-REVIEWS-COMPARISON-IMPLEMENTATION.png"))
            im_impl = Image.open(REVIEWS_OUT / "FP-0002-V6-REVIEWS-COMPARISON-IMPLEMENTATION.png").resize((1398, 480))
            im_mock = Image.open(REVIEWS_OUT / "FP-0002-V6-REVIEWS-COMPARISON-MOCKUP.jpg").resize((1398, 480))
            combo = Image.new("RGB", (1398, 960))
            combo.paste(im_mock, (0, 0))
            combo.paste(im_impl, (0, 480))
            combo.save(REVIEWS_OUT / "FP-0002-V6-REVIEWS-COMPARISON.png")

        metrics = page.evaluate(
            """() => {
                const gallery = document.querySelector('[data-gallery-slider]');
                const reviews = document.querySelector('[data-reviews-slider]');
                return {
                    gallerySlideCount: document.querySelectorAll('.home-gallery .swiper-slide').length,
                    galleryInstanceCount: gallery && gallery.swiper ? 1 : 0,
                    reviewsSlideCount: document.querySelectorAll('.home-reviews .swiper-slide').length,
                    reviewsInstanceCount: reviews && reviews.swiper ? 1 : 0,
                    totalSwiperCount: document.querySelectorAll('.swiper').length,
                };
            }"""
        )

        browser.close()

    (REVIEWS_OUT / "FP-0002-V6-REVIEWS-CAPTURE-METRICS.json").write_text(
        json.dumps(metrics, indent=2), encoding="utf-8"
    )
    print("CAPTURE_OK", json.dumps(metrics))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
