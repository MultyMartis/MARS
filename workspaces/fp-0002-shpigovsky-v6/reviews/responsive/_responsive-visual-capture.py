"""FP-0002 V6 responsive visual capture — mobile header, offcanvas, footer."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_DIR = ROOT / "reviews" / "responsive" / "visual"
DESKTOP_W = 1398
DESKTOP_H = 2400


def ensure_playwright() -> None:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def capture(page, width: int, height: int, name: str, *, selector: str | None = None, full_page: bool = False) -> None:
    page.set_viewport_size({"width": width, "height": height})
    page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
    path = OUT_DIR / name
    if selector:
        page.locator(selector).screenshot(path=str(path))
    else:
        page.screenshot(path=str(path), full_page=full_page)


def main() -> int:
    if not DIST_HTML.is_file():
        print(f"MISSING_BUILD: {DIST_HTML}")
        return 2

    ensure_playwright()
    from playwright.sync_api import sync_playwright

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    shots = [
        (DESKTOP_W, DESKTOP_H, "FP-0002-V6-PRE-MOBILE-DESKTOP-HEADER.png", ".site-header", False),
        (DESKTOP_W, DESKTOP_H, "FP-0002-V6-PRE-MOBILE-DESKTOP-FOOTER.png", ".site-footer", False),
        (DESKTOP_W, DESKTOP_H, "FP-0002-V6-PRE-MOBILE-DESKTOP-FULL.png", None, True),
        (320, 900, "FP-0002-V6-MOBILE-HEADER-320.png", ".site-header", False),
        (375, 900, "FP-0002-V6-MOBILE-HEADER-375.png", ".site-header", False),
        (390, 900, "FP-0002-V6-MOBILE-HEADER-390.png", ".site-header", False),
        (430, 900, "FP-0002-V6-MOBILE-HEADER-430.png", ".site-header", False),
        (320, 2400, "FP-0002-V6-MOBILE-FOOTER-320.png", ".site-footer", False),
        (375, 2400, "FP-0002-V6-MOBILE-FOOTER-375.png", ".site-footer", False),
        (390, 2400, "FP-0002-V6-MOBILE-FOOTER-390.png", ".site-footer", False),
        (390, 2400, "FP-0002-V6-MOBILE-FULL-390.png", None, True),
        (1024, DESKTOP_H, "FP-0002-V6-BREAKPOINT-1024.png", None, True),
        (1025, DESKTOP_H, "FP-0002-V6-BREAKPOINT-1025.png", None, True),
        (DESKTOP_W, DESKTOP_H, "FP-0002-V6-POST-MOBILE-DESKTOP-FULL.png", None, True),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for width, height, name, selector, full_page in shots:
            capture(page, width, height, name, selector=selector, full_page=full_page)

        for width, height, name, open_menu in [
            (375, 900, "FP-0002-V6-OFFCANVAS-CLOSED-375.png", False),
            (375, 900, "FP-0002-V6-OFFCANVAS-OPEN-375.png", True),
            (390, 900, "FP-0002-V6-OFFCANVAS-OPEN-390.png", True),
        ]:
            page.set_viewport_size({"width": width, "height": height})
            page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
            if open_menu:
                page.locator("[data-offcanvas-open]").click()
                page.wait_for_timeout(400)
            page.screenshot(path=str(OUT_DIR / name), full_page=False)

        browser.close()

    print(f"CAPTURED {len(list(OUT_DIR.glob('FP-0002-V6-*.png')))} screenshots in {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
