#!/usr/bin/env python3
"""FP-0002 V8 CF-008 accordion functional QA via Playwright."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-008-faq" / "data"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4198

PAGES = [
    ("index.html", "home"),
    ("uslugi.html", "services"),
    ("uslugi-v2.html", "services-v2"),
    ("usluga-podrazdel-v1.html", "service-subdivision"),
    ("usluga-konechnaya-v1.html", "service-leaf"),
]

VIEWPORTS = [("desktop", 1437, 1000), ("mobile", 380, 900)]


def run_accordion_qa(page, page_file: str) -> dict:
    url = f"http://127.0.0.1:{PORT}/{page_file}"
    console_errors: list[str] = []
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    page.goto(url, wait_until="networkidle", timeout=120000)
    page.locator(".faq, .home-faq").first.scroll_into_view_if_needed()
    page.wait_for_timeout(500)

    section_count = page.locator(".faq").count()
    old_count = page.locator(".home-faq").count()

    # Reset to known initial: first open
    page.evaluate(
        """() => {
          const section = document.querySelector('.faq, .home-faq');
          const triggers = section ? section.querySelectorAll('[data-accordion-button]') : [];
          triggers.forEach((btn, idx) => {
            const panel = document.getElementById(btn.getAttribute('aria-controls'));
            const open = idx === 0;
            btn.setAttribute('aria-expanded', open ? 'true' : 'false');
            if (panel) panel.hidden = !open;
          });
        }"""
    )

    btn2 = page.locator("[data-accordion-button]").nth(1)
    btn1 = page.locator("[data-accordion-button]").first

    click_open = False
    click_close = False
    enter_works = False
    space_works = False
    aria_updates = False
    hidden_updates = False

    btn2.click()
    page.wait_for_timeout(200)
    click_open = btn2.get_attribute("aria-expanded") == "true"
    panel2_id = btn2.get_attribute("aria-controls")
    panel2_hidden = page.evaluate(f"() => document.getElementById('{panel2_id}').hidden")
    hidden_updates = panel2_hidden is False
    aria_updates = click_open and hidden_updates
    click_close = False
    btn2.click()
    page.wait_for_timeout(200)
    click_close = btn2.get_attribute("aria-expanded") == "false"

    btn2.focus()
    page.keyboard.press("Enter")
    page.wait_for_timeout(200)
    enter_works = btn2.get_attribute("aria-expanded") == "true"
    page.keyboard.press(" ")
    page.wait_for_timeout(200)
    space_works = btn2.get_attribute("aria-expanded") == "false"

    overflow = page.evaluate("() => document.documentElement.scrollWidth > document.documentElement.clientWidth")

    return {
        "instance_count": section_count,
        "old_root_count": old_count,
        "click_open": click_open,
        "click_close": click_close,
        "enter": enter_works,
        "space": space_works,
        "aria_update": aria_updates,
        "hidden_update": hidden_updates,
        "duplicate_init": section_count == 1,
        "overflow": overflow,
        "console_errors": console_errors,
        "result": "PASS"
        if section_count == 1
        and old_count == 0
        and click_open
        and click_close
        and enter_works
        and space_works
        and aria_updates
        and hidden_updates
        and not overflow
        and not console_errors
        else "FAIL",
    }


def main() -> None:
    rows: list[dict] = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for page_file, page_id in PAGES:
            for vp_id, w, h in VIEWPORTS:
                page = browser.new_page(viewport={"width": w, "height": h})
                qa = run_accordion_qa(page, page_file)
                rows.append({"page": page_id, "page_file": page_file, "viewport": vp_id, **qa})
                page.close()
        browser.close()

    payload = {
        "validation_id": "CF-008-ACCORDION-FUNCTIONAL-QA",
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "port": PORT,
        "rows": rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in rows) else "FAIL",
    }
    (AUDIT / "CF-008-ACCORDION-FUNCTIONAL-QA.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"overall": payload["overall"], "rows": len(rows)}, indent=2))
    if payload["overall"] != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
