#!/usr/bin/env python3
"""SITE-002 Production visual capture — read-only Playwright screenshots."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

CAPTURE_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\captures\SITE-002-PROD-INITIAL-CAPTURE-01"
)
BASE_URL = "https://bzpm.ru"

PAGES = [
    ("homepage", "/"),
    ("catalog", "/katalog/"),
    ("about", "/about"),
    ("delivery", "/delivery"),
    ("payment", "/payment-methods"),
    ("dealers", "/dealers"),
    ("warranty", "/guarantee"),
    ("custom-manufacturing", "/custom-equipment"),
    ("product", "/index.php?route=product/product&product_id=50"),
]

VIEWPORTS = {
    "desktop": {"width": 1440, "height": 1200},
    "mobile": {"width": 390, "height": 844},
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def dismiss_cookie_banner(page) -> None:
    for selector in [
        "button:has-text('Принять')",
        "button:has-text('Согласен')",
        "button:has-text('OK')",
        ".cookie-accept",
        "#cookie-accept",
    ]:
        try:
            loc = page.locator(selector).first
            if loc.is_visible(timeout=1500):
                loc.click(timeout=2000)
                page.wait_for_timeout(500)
                return
        except Exception:
            continue


def main() -> int:
    results: list[dict] = []
    desktop_dir = CAPTURE_ROOT / "screenshots" / "desktop"
    mobile_dir = CAPTURE_ROOT / "screenshots" / "mobile"
    desktop_dir.mkdir(parents=True, exist_ok=True)
    mobile_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for vp_name, vp in VIEWPORTS.items():
            context = browser.new_context(
                viewport=vp,
                user_agent="MARS-OCPilot/SITE-002-PROD-INITIAL-CAPTURE-01 (read-only)",
            )
            page = context.new_page()
            out_dir = desktop_dir if vp_name == "desktop" else mobile_dir
            for slug, path in PAGES:
                url = BASE_URL + path
                entry = {"slug": slug, "viewport": vp_name, "url": url, "status": "FAIL", "file": None, "error": None}
                try:
                    resp = page.goto(url, wait_until="networkidle", timeout=60000)
                    dismiss_cookie_banner(page)
                    page.wait_for_timeout(800)
                    filename = f"{slug}.png"
                    target = out_dir / filename
                    page.screenshot(path=str(target), full_page=True)
                    entry["status"] = "PASS" if resp and resp.ok else "PARTIAL"
                    entry["file"] = str(target.relative_to(CAPTURE_ROOT))
                except Exception as exc:
                    entry["error"] = type(exc).__name__
                results.append(entry)
            context.close()
        browser.close()

    manifest = {"captured_at": utc_now(), "results": results}
    out = CAPTURE_ROOT / "screenshots" / "screenshot-manifest.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    passed = sum(1 for r in results if r["status"] in ("PASS", "PARTIAL"))
    print(f"Screenshots: {passed}/{len(results)} captured")
    return 0 if passed > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
