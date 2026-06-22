"""FP-0002 V6 — Header/Hero/Footer-placeholder restored screenshot @ 1398px."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_PNG = Path(__file__).resolve().parent / "visual" / "FP-0002-V6-HEADER-HERO-FOOTER-PLACEHOLDER-RESTORED.png"
VIEWPORT_W, VIEWPORT_H = 1398, 1200


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

    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    url = DIST_HTML.as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": VIEWPORT_W, "height": VIEWPORT_H})
        page.goto(url, wait_until="networkidle")
        page.screenshot(path=str(OUT_PNG), full_page=True)
        browser.close()

    print(f"Screenshot: {OUT_PNG}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
