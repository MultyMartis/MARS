"""FP-0002 V6 one SCSS file law — Header/Hero/Footer visual capture @ 1398px."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_DIR = Path(__file__).resolve().parent / "visual"
VIEWPORT_W, VIEWPORT_H = 1398, 9000


def ensure_playwright():
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def clip(page, selector: str, out_path: Path) -> bool:
    el = page.query_selector(selector)
    if not el:
        print(f"MISSING_SELECTOR: {selector}")
        return False
    el.screenshot(path=str(out_path))
    return True


def main() -> int:
    if not DIST_HTML.is_file():
        print(f"MISSING_BUILD: {DIST_HTML}")
        return 2

    ensure_playwright()
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    url = DIST_HTML.as_uri()

    shots = {
        "FP-0002-V6-ONE-SCSS-FILE-HEADER.png": ".site-header",
        "FP-0002-V6-ONE-SCSS-FILE-HERO.png": ".hero",
        "FP-0002-V6-ONE-SCSS-FILE-FOOTER.png": ".site-footer",
        "FP-0002-V6-ONE-SCSS-FILE-FULL.png": None,
    }

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": VIEWPORT_W, "height": VIEWPORT_H})
        page.goto(url, wait_until="networkidle")

        for name, selector in shots.items():
            out = OUT_DIR / name
            if selector is None:
                page.screenshot(path=str(out), full_page=True)
            else:
                if not clip(page, selector, out):
                    browser.close()
                    return 3

        browser.close()

    print("SCREENSHOTS_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
