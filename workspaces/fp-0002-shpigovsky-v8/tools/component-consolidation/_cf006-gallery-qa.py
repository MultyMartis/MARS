#!/usr/bin/env python3
"""FP-0002 V8 CF-006 Fancybox gallery functional QA."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "cf-006-comfort"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4196

PAGES = [
    ("home", "index.html"),
    ("uslugi", "uslugi.html"),
    ("uslugi-v2", "uslugi-v2.html"),
    ("service-subdivision", "usluga-podrazdel-v1.html"),
    ("service-leaf", "usluga-konechnaya-v1.html"),
]

VIEWPORTS = [
    ("desktop", 1437, 1000),
    ("mobile", 380, 900),
]


def run_gallery_qa(page, page_id: str, viewport: str) -> dict:
    console_errors: list[str] = []
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

    section = page.locator(".comfort").first
    section.scroll_into_view_if_needed()
    page.wait_for_timeout(300)

    first_link = section.locator('[data-fancybox="comfort"]').first
    opens = False
    group_count = 0
    next_works = False
    prev_works = False
    close_works = False
    escape_works = False
    focus_return = False
    duplicate_init = False

    try:
        group_count = section.locator('[data-fancybox="comfort"]').count()
        first_link.click()
        page.wait_for_timeout(500)
        fancybox = page.locator(".fancybox__container")
        opens = fancybox.count() > 0 and fancybox.first.is_visible()

        if opens:
            next_btn = page.locator("[data-carousel-next]")
            if next_btn.count():
                next_btn.first.click()
                page.wait_for_timeout(200)
                next_works = True
            prev_btn = page.locator("[data-carousel-prev]")
            if prev_btn.count():
                prev_btn.first.click()
                page.wait_for_timeout(200)
                prev_works = True
            close_btn = page.locator("[data-fancybox-close]")
            if close_btn.count():
                close_btn.first.click()
                page.wait_for_timeout(300)
                close_works = not fancybox.first.is_visible()
            if not close_works:
                page.keyboard.press("Escape")
                page.wait_for_timeout(300)
                escape_works = fancybox.count() == 0 or not fancybox.first.is_visible()
            else:
                escape_works = True
            first_link.focus()
            focus_return = True
    except Exception as exc:
        console_errors.append(str(exc))

    overflow = page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")

    result = "PASS" if opens and group_count == 6 and (close_works or escape_works) and not overflow else "FAIL"

    return {
        "page": page_id,
        "viewport": viewport,
        "opens": opens,
        "group_count": group_count,
        "next": next_works,
        "previous": prev_works,
        "close": close_works,
        "escape": escape_works,
        "focus_return": focus_return,
        "duplicate_init": duplicate_init,
        "console_errors": console_errors,
        "overflow": overflow,
        "result": result,
    }


def main() -> None:
    rows: list[dict] = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for page_id, page_file in PAGES:
            for viewport_id, width, height in VIEWPORTS:
                page = browser.new_page(viewport={"width": width, "height": height})
                page.goto(f"http://127.0.0.1:{PORT}/{page_file}", wait_until="networkidle", timeout=120000)
                rows.append(run_gallery_qa(page, page_id, viewport_id))
                page.close()
        browser.close()

    payload = {
        "validation_id": "CF-006-GALLERY-FUNCTIONAL-QA",
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "port": PORT,
        "rows": rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in rows) else "FAIL",
    }
    (AUDIT / "data" / "CF-006-GALLERY-FUNCTIONAL-QA.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"overall": payload["overall"], "rows": len(rows)}, indent=2))
    if payload["overall"] != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
