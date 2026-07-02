#!/usr/bin/env python3
"""FP-0002 V8 CF-009 lead form functional QA via Playwright."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-009-final-form" / "data"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4198

PAGES = [
    ("index.html", "home"),
    ("uslugi.html", "services"),
    ("uslugi-v2.html", "services-v2"),
    ("usluga-podrazdel-v1.html", "service-subdivision"),
    ("usluga-konechnaya-v1.html", "service-leaf"),
]

VIEWPORTS = [("desktop", 1437, 1000), ("mobile", 380, 900)]


def run_form_qa(page, page_file: str, viewport_id: str) -> dict:
    url = f"http://127.0.0.1:{PORT}/{page_file}"
    console_errors: list[str] = []
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    page.goto(url, wait_until="networkidle", timeout=120000)
    section = page.locator(".final-form, .home-final-form").first
    section.scroll_into_view_if_needed()
    page.wait_for_timeout(500)

    neutral_count = page.locator(".final-form").count()
    old_count = page.locator(".home-final-form").count()
    form = section.locator("[data-lead-form]")
    phone = form.locator("[data-phone-input]")

    empty_submit_blocks = False
    form.evaluate("el => el.requestSubmit()")
    page.wait_for_timeout(300)
    invalid_wrappers = form.locator(
        ".final-form__field--invalid, .home-final-form__field--invalid"
    ).count()
    empty_submit_blocks = invalid_wrappers >= 1

    phone.fill("+7 999 123 45 67")
    page.wait_for_timeout(200)
    phone_masked = phone.input_value()
    mask_works = "+7" in phone_masked and len(phone_masked.replace(" ", "")) >= 10

    return {
        "page_file": page_file,
        "viewport": viewport_id,
        "neutral_root_count": neutral_count,
        "old_root_count": old_count,
        "empty_submit_validation": empty_submit_blocks,
        "phone_mask_works": mask_works,
        "console_errors": console_errors,
        "result": "PASS"
        if neutral_count == 1 and old_count == 0 and empty_submit_blocks and mask_works
        else "FAIL",
    }


def main() -> None:
    rows: list[dict] = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for page_file, page_id in PAGES:
            for viewport_id, width, height in VIEWPORTS:
                page = browser.new_page(viewport={"width": width, "height": height})
                rows.append(run_form_qa(page, page_file, viewport_id))
                page.close()
        browser.close()

    payload = {
        "validation_id": "CF-009-FORM-FUNCTIONAL-QA",
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "port": PORT,
        "rows": rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in rows) else "FAIL",
    }
    (AUDIT / "CF-009-FORM-FUNCTIONAL-QA.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"overall": payload["overall"], "rows": len(rows)}, indent=2))
    if payload["overall"] != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
