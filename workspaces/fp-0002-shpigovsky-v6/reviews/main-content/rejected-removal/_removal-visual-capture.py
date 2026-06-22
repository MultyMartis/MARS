"""FP-0002 V6 — post-removal shell validation screenshots."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_DIR = ROOT / "reviews" / "main-content" / "rejected-removal"


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

        page.set_viewport_size({"width": 1398, "height": 2200})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        page.screenshot(path=str(OUT_DIR / "FP-0002-V6-SECTION-01-REMOVED-DESKTOP.png"), full_page=True)
        page.screenshot(path=str(OUT_DIR / "FP-0002-V6-SHELL-AFTER-REMOVAL.png"), full_page=True)

        page.set_viewport_size({"width": 390, "height": 2400})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        page.screenshot(path=str(OUT_DIR / "FP-0002-V6-SECTION-01-REMOVED-MOBILE.png"), full_page=True)

        browser.close()

    print(f"CAPTURED removal validation in {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
