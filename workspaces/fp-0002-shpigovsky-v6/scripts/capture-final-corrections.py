"""FP-0002 V6 — final corrections screenshots."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST_HTML = ROOT / "dist" / "index.html"
OUT = ROOT / "reviews" / "main-content" / "final-corrections"


def ensure_deps() -> None:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def main() -> int:
    if not DIST_HTML.is_file():
        print(f"MISSING_BUILD: {DIST_HTML}")
        return 2

    ensure_deps()
    from playwright.sync_api import sync_playwright

    OUT.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        def shot(selector: str, name: str, width: int, height: int = 900) -> None:
            page.set_viewport_size({"width": width, "height": height})
            page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
            page.locator(selector).scroll_into_view_if_needed()
            page.locator(selector).screenshot(path=str(OUT / name))

        shot(".home-articles__grid", "YOGA-BOS-IMAGES-DESKTOP.png", 1398)
        shot(".home-articles__grid", "YOGA-BOS-IMAGES-MOBILE-390.png", 390)

        shot(".home-final-form", "FINAL-FORM-DESKTOP.png", 1398)
        shot(".home-final-form", "FINAL-FORM-MOBILE-390.png", 390)

        page.set_viewport_size({"width": 1398, "height": 900})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        page.locator(".home-final-form__consent-input").focus()
        page.wait_for_timeout(200)
        page.locator(".home-final-form").screenshot(path=str(OUT / "FINAL-FORM-CONSENT-FOCUS.png"))

        page.set_viewport_size({"width": 1398, "height": 900})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        page.locator(".home-final-form__band").screenshot(path=str(OUT / "FINAL-FORM-BACKGROUND-COMPARISON.png"))

        page.set_viewport_size({"width": 1398, "height": 12000})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
        page.screenshot(path=str(OUT / "FULL-HOME-AFTER-FINAL-CORRECTIONS.png"), full_page=True)

        widths = [320, 375, 390, 430, 768, 1024, 1025, 1398]
        overflow = {}
        for width in widths:
            page.set_viewport_size({"width": width, "height": 900})
            page.goto(DIST_HTML.as_uri(), wait_until="networkidle")
            result = page.evaluate(
                """() => ({
                    doc: document.documentElement.scrollWidth > document.documentElement.clientWidth,
                    body: document.body.scrollWidth > document.body.clientWidth
                })"""
            )
            overflow[str(width)] = bool(result["doc"] or result["body"])

        import json

        (OUT / "RESPONSIVE-OVERFLOW-CHECK.json").write_text(
            json.dumps(overflow, indent=2),
            encoding="utf-8",
        )

        browser.close()

    print(f"SCREENSHOTS_OK: {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
