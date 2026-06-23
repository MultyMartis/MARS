"""FP-0002 V6 next home section — visual capture and comparison."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DIST_HTML = ROOT / "dist" / "index.html"
AUDIT_DIR = ROOT / "reviews" / "main-content" / "next-section-audit"
OUT_DIR = ROOT / "reviews" / "main-content" / "next-section-implementation"
META = AUDIT_DIR / "FP-0002-V6-NEXT-SECTION-BOUNDARY-META.json"
MOCKUP = (
    ROOT.parent
    / "website-factory-operations"
    / "FP-0002-SHPIGOVSKY"
    / "INCOMING"
    / "01_DESIGN"
    / "HOME-PAGE-FULL-MOCKUP.jpg"
)


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

    metrics = {"overflow": {}, "widths": {}}

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for width in (1398, 390):
            page = browser.new_page(viewport={"width": width, "height": 4200})
            page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
            section = page.locator(".home-rehabilitation-requirements")
            if width == 1398:
                section.screenshot(path=str(OUT_DIR / "FP-0002-V6-NEXT-SECTION-DESKTOP.png"))
            else:
                section.screenshot(path=str(OUT_DIR / "FP-0002-V6-NEXT-SECTION-MOBILE-390.png"))

            reviews = page.locator(".home-reviews")
            next_sec = page.locator(".home-rehabilitation-requirements")
            reviews_box = reviews.bounding_box()
            next_box = next_sec.bounding_box()
            if reviews_box and next_box and width == 1398:
                clip_y = max(0, reviews_box["y"] + reviews_box["height"] - 80)
                clip_h = (next_box["y"] + next_box["height"]) - clip_y + 40
                page.screenshot(
                    path=str(OUT_DIR / "FP-0002-V6-REVIEWS-TO-NEXT-SECTION.png"),
                    clip={"x": 0, "y": clip_y, "width": width, "height": clip_h},
                )

            footer = page.locator(".site-footer")
            footer_box = footer.bounding_box()
            if next_box and footer_box and width == 1398:
                clip_y = max(0, next_box["y"] + next_box["height"] - 40)
                clip_h = min(900, footer_box["y"] - clip_y + 120)
                page.screenshot(
                    path=str(OUT_DIR / "FP-0002-V6-NEXT-SECTION-TO-FOLLOWING.png"),
                    clip={"x": 0, "y": clip_y, "width": width, "height": clip_h},
                )

            if reviews_box and footer_box and width == 1398:
                clip_y = max(0, reviews_box["y"] - 40)
                clip_h = min(2400, footer_box["y"] - clip_y + 80)
                page.screenshot(
                    path=str(OUT_DIR / "FP-0002-V6-NEXT-SECTION-FULL-CONTEXT.png"),
                    clip={"x": 0, "y": clip_y, "width": width, "height": clip_h},
                )

            overflow = page.evaluate(
                """() => ({
                  doc: document.documentElement.scrollWidth - document.documentElement.clientWidth,
                  body: document.body.scrollWidth - document.body.clientWidth
                })"""
            )
            metrics["overflow"][str(width)] = overflow
            page.close()

        browser.close()

    mock = Image.open(MOCKUP).convert("RGB")
    b = meta["boundaries"]
    crop = mock.crop((0, b["reviews_end_y"] - 40, mock.width, b["following_section_start_y"] + 40))
    crop.save(OUT_DIR / "FP-0002-V6-NEXT-SECTION-COMPARISON-REF.png")

    built = Image.open(OUT_DIR / "FP-0002-V6-NEXT-SECTION-DESKTOP.png").convert("RGB")
    built_resized = built.resize((crop.width, crop.height))
    built_resized.save(OUT_DIR / "FP-0002-V6-NEXT-SECTION-COMPARISON.png")

    (OUT_DIR / "FP-0002-V6-NEXT-SECTION-CAPTURE-METRICS.json").write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(metrics, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
