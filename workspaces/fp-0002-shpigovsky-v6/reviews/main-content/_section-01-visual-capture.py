"""FP-0002 V6 home section 01 — visual capture."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_DIR = ROOT / "reviews" / "main-content" / "visual"


def ensure_playwright() -> None:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def main() -> int:
    if not DIST_HTML.is_file():
        print(f"MISSING_BUILD: {DIST_HTML}")
        return 2

    ensure_playwright()
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size({"width": 1398, "height": 2400})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")

        page.locator(".home-intro-mission").screenshot(
            path=str(OUT_DIR / "FP-0002-V6-HOME-SECTION-01-DESKTOP.png")
        )

        hero = page.locator(".hero")
        section = page.locator(".home-intro-mission")
        hero_box = hero.bounding_box()
        section_box = section.bounding_box()
        if hero_box and section_box:
            clip_y = max(0, hero_box["y"] - 20)
            clip_h = (section_box["y"] + section_box["height"]) - clip_y + 20
            page.screenshot(
                path=str(OUT_DIR / "FP-0002-V6-HOME-HERO-TO-SECTION-01.png"),
                clip={"x": 0, "y": clip_y, "width": 1398, "height": clip_h},
            )

        footer = page.locator(".site-footer")
        footer_box = footer.bounding_box()
        if section_box and footer_box:
            clip_y = max(0, section_box["y"] - 20)
            clip_h = (footer_box["y"] + min(footer_box["height"], 420)) - clip_y
            page.screenshot(
                path=str(OUT_DIR / "FP-0002-V6-HOME-SECTION-01-TO-FOOTER-CONTEXT.png"),
                clip={"x": 0, "y": clip_y, "width": 1398, "height": clip_h},
            )

        browser.close()

    print(f"CAPTURED section 01 screenshots in {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
