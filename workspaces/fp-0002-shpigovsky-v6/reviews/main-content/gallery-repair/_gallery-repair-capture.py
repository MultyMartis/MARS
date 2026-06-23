"""FP-0002 V6 — repaired gallery visual capture."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_DIR = ROOT / "reviews" / "main-content" / "gallery-repair"
PRE_OUT = ROOT / "reviews" / "main-content" / "pre-reviews-recovery"


def ensure_deps() -> None:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def capture_gallery(page, width: int, suffix: str) -> None:
    page.set_viewport_size({"width": width, "height": 900})
    page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
    page.locator(".home-gallery").screenshot(path=str(OUT_DIR / f"FP-0002-V6-GALLERY-REPAIRED-{suffix}.png"))


def main() -> int:
    if not DIST_HTML.is_file():
        print(f"MISSING_BUILD: {DIST_HTML}")
        return 2

    ensure_deps()
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PRE_OUT.mkdir(parents=True, exist_ok=True)

    metrics = {}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for width, suffix in [
            (1398, "DESKTOP"),
            (1024, "1024"),
            (768, "768"),
            (390, "390"),
            (320, "320"),
        ]:
            capture_gallery(page, width, suffix)

        page.set_viewport_size({"width": 1398, "height": 900})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        slider = page.locator("[data-gallery-slider]")
        box = slider.bounding_box()
        if box:
            page.mouse.move(box["x"] + box["width"] * 0.75, box["y"] + box["height"] / 2)
            page.mouse.down()
            page.mouse.move(box["x"] + box["width"] * 0.25, box["y"] + box["height"] / 2, steps=12)
            page.mouse.up()
            page.wait_for_timeout(400)
            slider.screenshot(path=str(OUT_DIR / "FP-0002-V6-GALLERY-REPAIRED-AFTER-DRAG.png"))

        page.set_viewport_size({"width": 1398, "height": 4200})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        s03 = page.locator(".home-treatment-prevention")
        why = page.locator(".home-why-us")
        s03_box = s03.bounding_box()
        why_box = why.bounding_box()
        if s03_box and why_box:
            clip_y = max(0, int(s03_box["y"] + s03_box["height"] - 40))
            clip_h = max(200, int(why_box["y"] + 160 - clip_y))
            if clip_y + clip_h <= 4200:
                page.screenshot(
                    path=str(OUT_DIR / "FP-0002-V6-GALLERY-REPAIRED-COMPARISON.png"),
                    clip={"x": 0, "y": clip_y, "width": 1398, "height": clip_h},
                )

        page.set_viewport_size({"width": 1398, "height": 9000})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        metrics = page.evaluate(
            """() => {
                const slider = document.querySelector('[data-gallery-slider]');
                const wrapper = slider ? slider.querySelector('.swiper-wrapper') : null;
                const slide = slider ? slider.querySelector('.swiper-slide') : null;
                const w = wrapper ? getComputedStyle(wrapper) : null;
                const s = slide ? getComputedStyle(slide) : null;
                return {
                    swiperCount: document.querySelectorAll('.swiper').length,
                    wrapperCount: document.querySelectorAll('.swiper-wrapper').length,
                    slideCount: document.querySelectorAll('.home-gallery .swiper-slide').length,
                    instanceCount: slider && slider.swiper ? 1 : 0,
                    wrapperDisplay: w ? w.display : null,
                    slideFlexShrink: s ? s.flexShrink : null,
                };
            }"""
        )

        for selector, name in [
            (".home-staff-photo", "home-staff-photo"),
            (".home-feature-grid", "home-feature-grid"),
            (".home-clinic-landscape", "home-clinic-landscape"),
        ]:
            block = page.locator(selector)
            block.screenshot(path=str(PRE_OUT / f"{name}-DESKTOP.png"))
            box = block.bounding_box()
            if box:
                page.screenshot(
                    path=str(PRE_OUT / f"{name}-CONTEXT.png"),
                    clip={
                        "x": 0,
                        "y": max(0, box["y"] - 80),
                        "width": 1398,
                        "height": min(9000, box["height"] + 200),
                    },
                )

        gallery = page.locator(".home-gallery")
        landscape = page.locator(".home-clinic-landscape")
        g_box = gallery.bounding_box()
        l_box = landscape.bounding_box()
        if g_box and l_box:
            clip_y = max(0, g_box["y"] - 40)
            clip_h = min(9000, l_box["y"] + l_box["height"] + 40 - clip_y)
            page.screenshot(
                path=str(PRE_OUT / "FP-0002-V6-GALLERY-TO-REVIEWS-BOUNDARY.png"),
                clip={"x": 0, "y": clip_y, "width": 1398, "height": clip_h},
            )

        browser.close()

    (OUT_DIR / "FP-0002-V6-GALLERY-REPAIR-METRICS.json").write_text(
        json.dumps(metrics, indent=2), encoding="utf-8"
    )
    print("CAPTURE_OK", json.dumps(metrics))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
