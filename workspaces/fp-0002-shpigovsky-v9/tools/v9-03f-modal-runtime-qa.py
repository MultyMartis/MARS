#!/usr/bin/env python3
"""FP-0002 V9-03F — modal scroll stability runtime QA."""
import json
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print(json.dumps({"pass": False, "error": "playwright not installed"}))
    sys.exit(1)

PORT = 8796
BASE = f"http://127.0.0.1:{PORT}"
SCENARIOS = [
    {
        "id": "home-footer",
        "url": "/",
        "scroll_selector": "footer.site-footer",
        "trigger_selector": 'footer button[data-modal-source="footer-appointment"]',
    },
    {
        "id": "home-middle-cta",
        "url": "/",
        "scroll_selector": "[data-modal-source='founder-quote']",
        "trigger_selector": "[data-modal-source='founder-quote']",
    },
    {
        "id": "o-centre-lower",
        "url": "/o-centre/",
        "scroll_selector": "footer.site-footer",
        "trigger_selector": 'footer button[data-modal-source="footer-appointment"]',
    },
    {
        "id": "alcohol-dependence",
        "url": "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
        "scroll_selector": "footer.site-footer",
        "trigger_selector": 'footer button[data-modal-source="footer-appointment"]',
    },
    {
        "id": "contacts",
        "url": "/kontakty/",
        "scroll_selector": "footer.site-footer",
        "trigger_selector": 'footer button[data-modal-source="footer-appointment"]',
    },
]

results = []


def run_scenario(page, scenario):
    page.goto(BASE + scenario["url"], wait_until="networkidle")
    page.wait_for_selector(scenario["scroll_selector"], timeout=15000)
    page.locator(scenario["scroll_selector"]).scroll_into_view_if_needed()
    page.wait_for_timeout(300)
    before_y = page.evaluate("() => window.scrollY")
    marker_before = page.evaluate(
        """(sel) => {
            const el = document.querySelector(sel);
            if (!el) return null;
            return el.getBoundingClientRect().top;
        }""",
        scenario["scroll_selector"],
    )
    trigger = page.locator(scenario["trigger_selector"]).first
    trigger.click()
    page.wait_for_selector('.modal-consultation[data-modal-state="open"]', timeout=5000)
    open_y = page.evaluate("() => window.scrollY")
    body_locked = page.evaluate(
        "() => document.body.classList.contains('is-modal-scroll-locked')"
    )
    marker_open = page.evaluate(
        """(sel) => {
            const el = document.querySelector(sel);
            if (!el) return null;
            return el.getBoundingClientRect().top;
        }""",
        scenario["scroll_selector"],
    )
    overlay_alpha = page.evaluate(
        """() => {
            const overlay = document.querySelector('.modal-consultation__overlay');
            if (!overlay) return null;
            return window.getComputedStyle(overlay).backgroundColor;
        }"""
    )
    page.keyboard.press("Escape")
    page.wait_for_function(
        """() => {
            const modal = document.querySelector('.modal-consultation[data-modal="consultation"]');
            return modal && modal.hasAttribute('hidden');
        }""",
        timeout=8000,
    )
    page.wait_for_timeout(400)
    after_y = page.evaluate("() => window.scrollY")
    marker_after = page.evaluate(
        """(sel) => {
            const el = document.querySelector(sel);
            if (!el) return null;
            return el.getBoundingClientRect().top;
        }""",
        scenario["scroll_selector"],
    )
    body_unlocked = page.evaluate(
        "() => !document.body.classList.contains('is-modal-scroll-locked')"
    )
    open_delta = abs(open_y - before_y)
    close_delta = abs(after_y - before_y)
    marker_open_delta = (
        None
        if marker_before is None or marker_open is None
        else abs(marker_open - marker_before)
    )
    marker_close_delta = (
        None
        if marker_before is None or marker_after is None
        else abs(marker_after - marker_before)
    )
    passed = (
        open_delta <= 8
        and close_delta <= 8
        and body_locked
        and body_unlocked
        and (marker_open_delta is None or marker_open_delta <= 8)
        and (marker_close_delta is None or marker_close_delta <= 8)
    )
    return {
        "id": scenario["id"],
        "pass": passed,
        "before_y": before_y,
        "open_y": open_y,
        "after_y": after_y,
        "open_delta": open_delta,
        "close_delta": close_delta,
        "marker_before": marker_before,
        "marker_open_delta": marker_open_delta,
        "marker_close_delta": marker_close_delta,
        "body_locked": body_locked,
        "body_unlocked": body_unlocked,
        "overlay_color": overlay_alpha,
    }


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    for scenario in SCENARIOS:
        try:
            results.append(run_scenario(page, scenario))
        except Exception as exc:
            results.append({"id": scenario["id"], "pass": False, "error": str(exc)})
    page.close()
    page = browser.new_page(viewport={"width": 390, "height": 844})
    mobile = SCENARIOS[0]
    try:
        results.append({**run_scenario(page, mobile), "id": "mobile-home-footer"})
    except Exception as exc:
        results.append({"id": "mobile-home-footer", "pass": False, "error": str(exc)})
    browser.close()

summary = {
    "pass": all(r.get("pass") for r in results),
    "port": PORT,
    "results": results,
}
out = Path(__file__).resolve().parents[1] / "FP-0002-V9-03F-MODAL-RUNTIME-VALIDATION-DATA.json"
out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
print(json.dumps(summary, indent=2))
sys.exit(0 if summary["pass"] else 1)
