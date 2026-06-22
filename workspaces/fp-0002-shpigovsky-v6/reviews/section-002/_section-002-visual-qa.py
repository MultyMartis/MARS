"""FP-0002 V6 SECTION-002 visual QA @ 1398px desktop."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_DIR = Path(__file__).resolve().parent / "visual"
OUT_SECTION = OUT_DIR / "FP-0002-V6-SECTION-002-DESKTOP-RENDER-01.png"
OUT_COMBO = OUT_DIR / "FP-0002-V6-SECTION-001-002-DESKTOP-RENDER-01.png"
VIEWPORT_W = 1398


def ensure_playwright():
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
    url = DIST_HTML.as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": VIEWPORT_W, "height": 1200})

        page.goto(url, wait_until="networkidle")
        section = page.query_selector(".intro-programs")
        if not section:
            print("MISSING_SECTION: .intro-programs")
            browser.close()
            return 3

        box = section.bounding_box()
        if not box:
            print("MISSING_BBOX")
            browser.close()
            return 4

        page.screenshot(
            path=str(OUT_SECTION),
            clip={
                "x": 0,
                "y": max(0, box["y"]),
                "width": VIEWPORT_W,
                "height": min(box["height"], 4000),
            },
        )

        page.set_viewport_size({"width": VIEWPORT_W, "height": 2200})
        page.goto(url, wait_until="networkidle")
        page.screenshot(path=str(OUT_COMBO), full_page=False)

        browser.close()

    print(json.dumps({"section": str(OUT_SECTION), "combo": str(OUT_COMBO), "viewport": VIEWPORT_W}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
