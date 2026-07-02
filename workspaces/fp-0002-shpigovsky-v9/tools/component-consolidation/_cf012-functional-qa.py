#!/usr/bin/env python3
"""CF-012 functional QA smoke for program consumers."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "audits" / "cf-012-program-modifiers" / "data" / "CF-012-FUNCTIONAL-QA.json"
PORT = 4199

CASES = [
    ("uslugi-v2.html", "#services-program", '[data-modal-source="services-program-guest"]'),
    ("usluga-podrazdel-v1.html", "#service-subdivision-program", None),
    ("usluga-konechnaya-v1.html", "#service-leaf-program", None),
]


def main() -> None:
    rows = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for page_file, section_sel, modal_sel in CASES:
            for vp, w, h in [("desktop", 1437, 1000), ("mobile", 380, 900)]:
                ctx = browser.new_context(viewport={"width": w, "height": h})
                page = ctx.new_page()
                errors = []
                page.on("pageerror", lambda e: errors.append(str(e)))
                page.goto(f"http://127.0.0.1:{PORT}/{page_file}", wait_until="networkidle")
                section = page.query_selector(section_sel)
                modal_ok = True
                if modal_sel:
                    btn = page.query_selector(modal_sel)
                    if btn:
                        btn.click()
                        modal_ok = page.is_visible("[data-modal]")
                        page.keyboard.press("Escape")
                overflow = page.evaluate(
                    "() => document.documentElement.scrollWidth > document.documentElement.clientWidth"
                )
                rows.append(
                    {
                        "page": page_file,
                        "viewport": vp,
                        "section_found": bool(section),
                        "modal_ok": modal_ok,
                        "overflow": overflow,
                        "console_errors": len(errors),
                        "result": "PASS"
                        if section and modal_ok and not overflow and not errors
                        else "FAIL",
                    }
                )
                ctx.close()
        browser.close()

    payload = {
        "validated_utc": datetime.now(timezone.utc).isoformat(),
        "rows": rows,
        "result": "PASS" if all(r["result"] == "PASS" for r in rows) else "FAIL",
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"result": payload["result"]}, indent=2))


if __name__ == "__main__":
    main()
