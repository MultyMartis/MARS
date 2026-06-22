"""FP-0002 V6 responsive shell stable release — visual capture."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
OUT_DIR = ROOT / "reviews" / "releases" / "visual"


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
        page.screenshot(
            path=str(OUT_DIR / "FP-0002-V6-RESPONSIVE-SHELL-DESKTOP-FULL.png"),
            full_page=True,
        )

        for width, height, name, open_menu in [
            (390, 900, "FP-0002-V6-RESPONSIVE-SHELL-MOBILE-CLOSED.png", False),
            (390, 900, "FP-0002-V6-RESPONSIVE-SHELL-MOBILE-OPEN.png", True),
        ]:
            page.set_viewport_size({"width": width, "height": height})
            page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
            if open_menu:
                page.locator("[data-offcanvas-open]").click()
                page.wait_for_timeout(400)
            page.screenshot(path=str(OUT_DIR / name), full_page=False)

        page.set_viewport_size({"width": 390, "height": 2400})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        page.locator(".site-footer").screenshot(
            path=str(OUT_DIR / "FP-0002-V6-RESPONSIVE-SHELL-MOBILE-FOOTER.png")
        )

        browser.close()

    print(f"CAPTURED release shell screenshots in {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
