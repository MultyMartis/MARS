"""FP-0002 V6 — modal implementation screenshots."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST_HTML = ROOT / "dist" / "index.html"
OUT = ROOT / "reviews" / "modals" / "implementation"


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
        page = browser.new_page(viewport={"width": 1398, "height": 900})

        def goto() -> None:
            page.goto(DIST_HTML.as_uri(), wait_until="networkidle")

        def open_from(selector: str) -> None:
            goto()
            page.locator(selector).first.click()
            page.wait_for_selector('[data-modal-state="open"]', timeout=5000)

        goto()
        page.screenshot(path=str(OUT / "MODAL-CLOSED-PAGE-DESKTOP.png"), full_page=False)

        open_from('[data-modal-source="hero"]')
        page.locator(".modal-consultation__dialog").screenshot(path=str(OUT / "MODAL-OPEN-HERO-DESKTOP.png"))

        open_from('[data-modal-source="header"]')
        page.locator(".modal-consultation__dialog").screenshot(path=str(OUT / "MODAL-OPEN-HEADER-DESKTOP.png"))

        page.set_viewport_size({"width": 390, "height": 844})
        open_from('[data-modal-source="hero"]')
        page.locator(".modal-consultation__dialog").screenshot(path=str(OUT / "MODAL-OPEN-MOBILE-390.png"))

        page.set_viewport_size({"width": 1398, "height": 900})
        open_from('[data-modal-source="hero"]')
        page.locator('[data-modal-submit-target]').click()
        page.wait_for_timeout(300)
        page.locator(".modal-consultation__dialog").screenshot(path=str(OUT / "MODAL-REQUIRED-ERRORS.png"))

        open_from('[data-modal-source="hero"]')
        page.locator("#modal-consultation-name").fill("Тест")
        page.locator("#modal-consultation-phone").fill("+7 999")
        page.locator('[data-modal-submit-target]').click()
        page.wait_for_timeout(300)
        page.locator(".modal-consultation__dialog").screenshot(path=str(OUT / "MODAL-PHONE-INCOMPLETE.png"))

        open_from('[data-modal-source="hero"]')
        page.locator("#modal-consultation-consent-error").wait_for(state="hidden")
        page.locator('[data-modal-submit-target]').click()
        page.wait_for_timeout(300)
        page.locator(".modal-consultation__dialog").screenshot(path=str(OUT / "MODAL-CONSENT-ERROR.png"))

        open_from('[data-modal-source="hero"]')
        page.locator("#modal-consultation-name").focus()
        page.wait_for_timeout(200)
        page.locator(".modal-consultation__dialog").screenshot(path=str(OUT / "MODAL-FOCUS-STATE.png"))

        page.set_viewport_size({"width": 390, "height": 500})
        open_from('[data-modal-source="hero"]')
        page.locator("#modal-consultation-message").fill("Длинное описание ситуации " * 20)
        page.locator(".modal-consultation__dialog").screenshot(path=str(OUT / "MODAL-LONG-CONTENT-SCROLL.png"))

        page.set_viewport_size({"width": 1398, "height": 900})
        goto()
        page.locator(".home-final-form").scroll_into_view_if_needed()
        page.locator(".home-final-form").screenshot(path=str(OUT / "FINAL-FORM-REGRESSION.png"))

        page.set_viewport_size({"width": 1398, "height": 12000})
        goto()
        page.screenshot(path=str(OUT / "FULL-HOME-AFTER-MODALS.png"), full_page=True)

        overflow: dict[str, bool] = {}
        for width in [320, 375, 390, 430, 768, 1024, 1025, 1398]:
            page.set_viewport_size({"width": width, "height": 900})
            goto()
            result = page.evaluate(
                """() => ({
                    doc: document.documentElement.scrollWidth > document.documentElement.clientWidth,
                    body: document.body.scrollWidth > document.body.clientWidth
                })"""
            )
            overflow[str(width)] = bool(result["doc"] or result["body"])

        (OUT / "RESPONSIVE-OVERFLOW-CHECK.json").write_text(
            json.dumps(overflow, indent=2),
            encoding="utf-8",
        )

        browser.close()

    print(f"SCREENSHOTS_OK: {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
