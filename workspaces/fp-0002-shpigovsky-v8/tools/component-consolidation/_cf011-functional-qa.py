#!/usr/bin/env python3
"""FP-0002 V8 CF-011 CTA functional QA via Playwright."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-011-dark-cta" / "data"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4199

CASES = [
    ("uslugi-v2-secondary", "uslugi-v2.html", '[data-modal-source="services-program-cta-secondary"]', "services-program-cta-secondary"),
    ("subdivision-start", "usluga-podrazdel-v1.html", '#service-subdivision-start [data-modal-open="consultation"]', "service-subdivision-cta-01"),
    ("leaf-cta-01", "usluga-konechnaya-v1.html", '#service-leaf-cta-01 [data-modal-open="consultation"]', "service-leaf-cta-01"),
]

VIEWPORTS = [("desktop", 1437, 1000), ("mobile", 380, 900)]


def main() -> None:
    rows: list[dict] = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for vp_name, w, h in VIEWPORTS:
            ctx = browser.new_context(viewport={"width": w, "height": h})
            page = ctx.new_page()
            for case_id, file_name, selector, source in CASES:
                page.goto(f"http://127.0.0.1:{PORT}/{file_name}", wait_until="networkidle")
                btn = page.query_selector(selector)
                visible = btn.is_visible() if btn else False
                src = btn.get_attribute("data-modal-source") if btn else None
                keyboard_ok = False
                click_ok = False
                dup_modal = False
                if btn:
                    btn.click()
                    page.wait_for_timeout(300)
                    modals = page.query_selector_all('[data-modal="consultation"]')
                    open_modals = [m for m in modals if m.is_visible()]
                    click_ok = len(open_modals) >= 1
                    dup_modal = len(open_modals) > 1
                    page.keyboard.press("Escape")
                    page.wait_for_timeout(200)
                    btn.focus()
                    page.keyboard.press("Enter")
                    page.wait_for_timeout(300)
                    keyboard_ok = any(m.is_visible() for m in page.query_selector_all('[data-modal="consultation"]'))
                    page.keyboard.press("Escape")
                rows.append(
                    {
                        "consumer": case_id,
                        "viewport": vp_name,
                        "click": click_ok,
                        "keyboard": keyboard_ok,
                        "target_modal_source": src,
                        "expected_source": source,
                        "duplicate_action": dup_modal,
                        "result": "PASS"
                        if visible and src == source and click_ok and not dup_modal
                        else "FAIL",
                    }
                )
            ctx.close()
        browser.close()

    payload = {
        "validation_id": "CF-011-FUNCTIONAL-QA",
        "port": PORT,
        "rows": rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in rows) else "FAIL",
    }
    AUDIT.mkdir(parents=True, exist_ok=True)
    (AUDIT / "CF-011-FUNCTIONAL-QA.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"overall": payload["overall"]}, indent=2))


if __name__ == "__main__":
    main()
