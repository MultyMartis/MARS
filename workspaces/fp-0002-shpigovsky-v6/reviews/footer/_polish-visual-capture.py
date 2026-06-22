"""Capture polish-pass screenshots @ 1398px — FP-0002 V6 footer socials + header nav."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_FOOTER = ROOT / "reviews" / "footer" / "visual" / "FP-0002-V6-FOOTER-SOCIALS-POLISH-01.png"
OUT_HEADER = ROOT / "reviews" / "header" / "visual" / "FP-0002-V6-HEADER-NAV-SPACING-POLISH-01.png"
OUT_FULL = ROOT / "reviews" / "footer" / "visual" / "FP-0002-V6-HEADER-HERO-FOOTER-POLISH-01.png"
VIEWPORT_W = 1398
VIEWPORT_H = 2200


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

    OUT_FOOTER.parent.mkdir(parents=True, exist_ok=True)
    OUT_HEADER.parent.mkdir(parents=True, exist_ok=True)
    url = DIST_HTML.as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": VIEWPORT_W, "height": VIEWPORT_H})
        page.goto(url, wait_until="networkidle")

        page.locator(".site-footer__top").screenshot(path=str(OUT_FOOTER))
        page.locator(".site-header__bottom").screenshot(path=str(OUT_HEADER))
        page.screenshot(path=str(OUT_FULL), full_page=True)
        browser.close()

    print(f"viewport={VIEWPORT_W}x{VIEWPORT_H}")
    print(f"footer={OUT_FOOTER}")
    print(f"header={OUT_HEADER}")
    print(f"full={OUT_FULL}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
