"""FP-0002 V6 Universal Style Scale — visual capture @ 1398px."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_DIR = Path(__file__).resolve().parent / "visual"
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

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    url = DIST_HTML.as_uri()

    shots = {
        "FP-0002-V6-UNIVERSAL-STYLE-SCALE-FULL.png": {"full_page": True},
        "FP-0002-V6-UNIVERSAL-STYLE-SCALE-HEADER.png": {"selector": ".site-header"},
        "FP-0002-V6-UNIVERSAL-STYLE-SCALE-FOOTER.png": {"selector": ".site-footer"},
    }

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": VIEWPORT_W, "height": VIEWPORT_H})
        page.goto(url, wait_until="networkidle")

        for name, opts in shots.items():
            path = OUT_DIR / name
            if opts.get("full_page"):
                page.screenshot(path=str(path), full_page=True)
            else:
                el = page.query_selector(opts["selector"])
                if not el:
                    print(f"MISSING_SELECTOR: {opts['selector']}")
                    browser.close()
                    return 3
                el.screenshot(path=str(path))

        browser.close()

    for name in shots:
        print(f"Screenshot: {OUT_DIR / name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
