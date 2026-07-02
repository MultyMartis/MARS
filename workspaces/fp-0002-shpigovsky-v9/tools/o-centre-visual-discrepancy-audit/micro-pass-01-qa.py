"""Technical QA for O-Centre micro-pass 01."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

V8 = Path(r"X:\AI MARS\workspaces\fp-0002-shpigovsky-v8")
DIST = V8 / "dist"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4722
URL = f"http://127.0.0.1:{PORT}/o-centre.html"


def main() -> None:
    html = (DIST / "o-centre.html").read_text(encoding="utf-8")
    ids = re.findall(r'\bid="([^"]+)"', html)
    dup_ids = sorted({i for i in ids if ids.count(i) > 1})
    includes_unresolved = html.count("@@include")
    asset_refs = re.findall(r'(?:src|href)="(assets/[^"]+)"', html)
    missing_assets = [a for a in asset_refs if not (DIST / a).exists()]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1437, "height": 900})
        errors: list[str] = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        page.goto(URL, wait_until="load", timeout=60000)
        page.wait_for_timeout(3000)
        overflow = page.evaluate(
            "() => document.documentElement.scrollWidth > window.innerWidth"
        )
        browser.close()

    out = {
        "build_dist_exists": DIST.exists(),
        "unresolved_includes": includes_unresolved,
        "duplicate_ids": dup_ids,
        "missing_assets": missing_assets,
        "console_errors": errors,
        "horizontal_overflow_1437": overflow,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    if includes_unresolved or missing_assets or dup_ids or errors or overflow:
        sys.exit(1)


if __name__ == "__main__":
    main()
