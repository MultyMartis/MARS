#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-scan previously affected /page__FORM.php URLs after contract patch."""
from __future__ import annotations

import importlib.util
import json
import shutil
from pathlib import Path

_INV = Path(__file__).with_name("_form-contract-regression-01-inventory.py")
_spec = importlib.util.spec_from_file_location("form_contract_inv", _INV)
_inv = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_inv)
fetch = _inv.fetch
parse_page = _inv.parse_page

EVIDENCE = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-contract-regression-01")
BEFORE = EVIDENCE / "live-inventory.json"
BEFORE_COPY = EVIDENCE / "live-inventory-before.json"
OUT = EVIDENCE / "live-inventory-after.json"
EXTRA = [
    "https://i-seo.su/",
    "https://i-seo.su/webinar-seo-podryadchik.html",
    "https://i-seo.su/services/adv.html",
    "https://i-seo.su/services/serm.html",
    "https://i-seo.su/contacts.html",
]


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    if BEFORE.exists() and not BEFORE_COPY.exists():
        shutil.copy2(BEFORE, BEFORE_COPY)
    before = json.loads(BEFORE.read_text(encoding="utf-8"))
    urls = list(dict.fromkeys(before.get("affected_urls", []) + EXTRA))
    rows = []
    defects = []
    healthy_page = []
    for url in urls:
        status, html = fetch(url)
        if status != 200 or "<form" not in html.lower():
            rows.append({"url": url, "http": status, "skipped": True, "reason": "no-200-or-no-form"})
            continue
        row = parse_page(url, html, status)
        rows.append(row)
        for f in row.get("page_form_family") or []:
            rec = {"url": row["url"], **f}
            if f.get("proven_defect"):
                defects.append(rec)
            elif f.get("contract_status") == "HEALTHY":
                healthy_page.append(rec)
    restaurant = next(
        (r for r in rows if r.get("url", "").endswith("prodvizhenie-sajta-restorana.html")),
        {},
    )
    report = {
        "task": "ISEO-SU-SITE-OPS-FORM-CONTRACT-REGRESSION-01",
        "phase": "after-patch-rescan",
        "urls_scanned": len(rows),
        "previously_affected": len(before.get("affected_urls", [])),
        "broken_contract_forms_found_after": len(defects),
        "healthy_page_form_count": len(healthy_page),
        "still_broken_urls": sorted({d["url"] for d in defects}),
        "healthy_urls": sorted({h["url"] for h in healthy_page}),
        "restaurant": {
            "url": restaurant.get("url"),
            "http": restaurant.get("http"),
            "title": restaurant.get("title"),
            "h1": restaurant.get("h1"),
            "canonical": restaurant.get("canonical"),
            "page_form_family": restaurant.get("page_form_family"),
            "proven_defect_count": restaurant.get("proven_defect_count"),
        },
        "defects": defects,
        "pages": rows,
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "urls_scanned": report["urls_scanned"],
        "previously_affected": report["previously_affected"],
        "broken_after": report["broken_contract_forms_found_after"],
        "still_broken_urls": report["still_broken_urls"],
        "restaurant_status": (restaurant.get("page_form_family") or [{}])[0].get("contract_status"),
        "out": str(OUT),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
