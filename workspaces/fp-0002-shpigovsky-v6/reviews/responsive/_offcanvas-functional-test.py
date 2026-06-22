"""FP-0002 V6 off-canvas functional matrix."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DIST_HTML = ROOT / "dist" / "index.html"
OUT = Path(__file__).resolve().parent / "FP-0002-V6-OFFCANVAS-FUNCTIONAL-MATRIX.json"


def ensure_playwright() -> None:
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright", "-q"])
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])


def main() -> int:
    ensure_playwright()
    from playwright.sync_api import sync_playwright

    results: dict[str, str] = {}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 375, "height": 800})
        page.goto(DIST_HTML.as_uri(), wait_until="networkidle")

        open_btn = page.locator("[data-offcanvas-open]")
        close_btn = page.locator("[data-offcanvas-close]")
        offcanvas = page.locator("[data-offcanvas]")
        overlay = page.locator("[data-offcanvas-overlay]")

        open_btn.click()
        page.wait_for_timeout(350)

        results["open_via_menu_button"] = "PASS" if offcanvas.get_attribute("data-offcanvas-state") == "open" else "FAIL"
        results["aria_expanded"] = "PASS" if open_btn.get_attribute("aria-expanded") == "true" else "FAIL"
        results["aria_hidden"] = "PASS" if offcanvas.get_attribute("aria-hidden") == "false" else "FAIL"
        results["focus_enters_panel"] = "PASS" if page.evaluate("document.activeElement.closest('[data-offcanvas-panel]') !== null") else "FAIL"
        results["body_scroll_locked"] = "PASS" if page.evaluate("document.body.getAttribute('data-offcanvas-state') === 'open'") else "FAIL"

        page.mouse.click(20, 400)
        page.wait_for_timeout(350)
        results["overlay_close"] = "PASS" if offcanvas.get_attribute("data-offcanvas-state") == "closed" else "FAIL"

        open_btn.click()
        page.wait_for_timeout(200)
        close_btn.click()
        page.wait_for_timeout(350)
        results["close_button"] = "PASS" if offcanvas.get_attribute("data-offcanvas-state") == "closed" else "FAIL"

        open_btn.click()
        page.wait_for_timeout(200)
        page.keyboard.press("Escape")
        page.wait_for_timeout(350)
        results["escape_close"] = "PASS" if offcanvas.get_attribute("data-offcanvas-state") == "closed" else "FAIL"

        open_btn.click()
        page.wait_for_timeout(200)
        close_btn.click()
        page.wait_for_timeout(350)
        results["focus_returns"] = "PASS" if open_btn.evaluate("el => el === document.activeElement") else "FAIL"

        open_btn.click()
        page.wait_for_timeout(200)
        page.set_viewport_size({"width": 1025, "height": 800})
        page.evaluate("window.dispatchEvent(new Event('resize'))")
        page.wait_for_timeout(400)
        results["resize_mobile_to_desktop_cleanup"] = "PASS" if offcanvas.get_attribute("data-offcanvas-state") == "closed" else "FAIL"
        results["body_scroll_restored"] = "PASS" if page.evaluate("document.body.getAttribute('data-offcanvas-state') !== 'open'") else "FAIL"

        page.set_viewport_size({"width": 375, "height": 800})
        page.evaluate("window.dispatchEvent(new Event('resize'))")
        page.wait_for_timeout(200)
        results["resize_desktop_to_mobile_state"] = "PASS" if offcanvas.get_attribute("data-offcanvas-state") == "closed" else "FAIL"

        if offcanvas.get_attribute("data-offcanvas-state") == "open":
            page.keyboard.press("Escape")
            page.wait_for_timeout(300)
        if offcanvas.get_attribute("data-offcanvas-state") == "open":
            close_btn.click(force=True)
            page.wait_for_timeout(300)

        open_btn.evaluate("el => { el.click(); el.click(); }")
        page.wait_for_timeout(250)
        results["multiple_open_clicks"] = "PASS" if offcanvas.get_attribute("data-offcanvas-state") == "open" else "FAIL"

        browser.close()

    OUT.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(results, indent=2, ensure_ascii=False))
    return 0 if all(v == "PASS" for v in results.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
