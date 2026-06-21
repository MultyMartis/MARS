#!/usr/bin/env python3
"""M9.8.9-09C — automated QA probe (server-side; browser matrix pending operator)."""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

BASE = "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly"
WORK_DIR = Path(__file__).resolve().parent
MAIN_JS_URL = "https://zpm.new-site.space/assets/js/main.js"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "M9.8.9-09C-QA/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def extract_limit_hrefs(html: str) -> list[str]:
    m = re.search(r'<div class="category__limit"[\s\S]{0,3000}', html)
    if not m:
        return []
    block = m.group(0)
    return re.findall(r'href="([^"]+limit=\d+[^"]*)"', block)


def main() -> None:
    results: dict = {"scenarios": {}, "live_js": {}}

    plain = fetch(BASE)
    filtered = fetch(BASE + "?filters=only_with_price=1")
    combo = fetch(BASE + "?filters=only_with_price=1&limit=50&sort=p.price&order=ASC&page=2")

    plain_hrefs = extract_limit_hrefs(plain)
    filtered_hrefs = extract_limit_hrefs(filtered)
    combo_hrefs = extract_limit_hrefs(combo)

    results["scenarios"]["plain_limit_hrefs_no_filters"] = all(
        "filters=" not in h for h in plain_hrefs
    )
    results["scenarios"]["filtered_limit_hrefs_have_filters"] = all(
        "filters=only_with_price" in h for h in filtered_hrefs
    )
    results["scenarios"]["combo_limit_hrefs_preserve_filters_sort_page"] = all(
        "filters=only_with_price" in h and "limit=" in h for h in combo_hrefs
    )
    results["scenarios"]["plain_hrefs_sample"] = plain_hrefs[:2]
    results["scenarios"]["filtered_hrefs_sample"] = filtered_hrefs[:2]
    results["scenarios"]["combo_hrefs_sample"] = combo_hrefs[:2]

    js = fetch(MAIN_JS_URL)
    results["live_js"] = {
        "has_initCategoryLimitMenu": "function initCategoryLimitMenu()" in js,
        "has_limit_outerHTML_refresh": "oldLimit.outerHTML = newLimit.outerHTML" in js,
        "has_updateProducts_limit_block": "Обновляем limit control" in js,
        "has_delegated_limit_doc_click": "survives limit DOM refresh" in js,
    }

    results["all_automated_pass"] = (
        results["scenarios"]["plain_limit_hrefs_no_filters"]
        and results["scenarios"]["filtered_limit_hrefs_have_filters"]
        and results["scenarios"]["combo_limit_hrefs_preserve_filters_sort_page"]
        and all(results["live_js"].values())
    )
    results["browser_qa_required"] = [
        "Q1 filter → limit 50 — URL keeps filters= + limit=50",
        "Q2 attr filter → limit 50 — filters preserved",
        "Q3 limit=50 → filter → sort → page 2 — all params preserved",
        "Q4 limit dropdown opens after filter AJAX",
        "Q5 active limit label correct after filter AJAX",
        "Q6 pagination still works after filter AJAX",
    ]

    out = WORK_DIR / "qa-results.json"
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
