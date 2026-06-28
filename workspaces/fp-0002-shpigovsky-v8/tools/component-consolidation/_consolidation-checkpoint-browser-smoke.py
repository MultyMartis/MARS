#!/usr/bin/env python3
"""FP-0002 V8 consolidation checkpoint browser smoke."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "audits" / "consolidation-checkpoint" / "data"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4196

PAGES = [
    ("home", "index.html"),
    ("services-legacy", "uslugi.html"),
    ("services-hub", "uslugi-v2.html"),
    ("service-subdivision", "usluga-podrazdel-v1.html"),
    ("service-leaf", "usluga-konechnaya-v1.html"),
]

VIEWPORTS = [("desktop", 1437, 1000), ("mobile", 380, 900)]


def smoke(page, page_file: str, viewport: str) -> dict:
    url = f"http://127.0.0.1:{PORT}/{page_file}"
    console_errors: list[str] = []
    failed_assets: list[str] = []

    def on_console(msg):
        if msg.type == "error":
            console_errors.append(msg.text)

    def on_request_failed(req):
        if req.url.startswith(f"http://127.0.0.1:{PORT}/"):
            failed_assets.append(req.url)

    page.on("console", on_console)
    page.on("requestfailed", on_request_failed)
    resp = page.goto(url, wait_until="networkidle", timeout=120000)
    overflow = page.evaluate(
        "() => document.documentElement.scrollWidth > document.documentElement.clientWidth"
    )
    return {
        "page": page_file,
        "viewport": viewport,
        "http": resp.status if resp else 0,
        "console_errors": len(console_errors),
        "failed_assets": len(failed_assets),
        "overflow": int(overflow),
        "result": "PASS"
        if resp
        and resp.status == 200
        and not console_errors
        and not failed_assets
        and not overflow
        else "FAIL",
    }


def main() -> None:
    rows: list[dict] = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for page_id, page_file in PAGES:
            for vp_id, w, h in VIEWPORTS:
                page = browser.new_page(viewport={"width": w, "height": h})
                rows.append(smoke(page, page_file, vp_id))
                page.close()
        browser.close()

    payload = {
        "validation_id": "FP-0002-V8-CONSOLIDATION-BROWSER-SMOKE",
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "port": PORT,
        "rows": rows,
        "overall": "PASS" if all(r["result"] == "PASS" for r in rows) else "FAIL",
    }
    AUDIT.mkdir(parents=True, exist_ok=True)
    (AUDIT / "FP-0002-V8-CONSOLIDATION-BROWSER-SMOKE.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"overall": payload["overall"], "rows": len(rows)}, indent=2))
    if payload["overall"] != "PASS":
        sys.exit(1)


if __name__ == "__main__":
    main()
