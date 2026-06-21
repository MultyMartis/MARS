#!/usr/bin/env python3
"""BZPM M8.3 Wave 1 — storefront QA on TEST."""
import json
import re
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://zpm.new-site.space"
OUT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\m8.3-wave1\m8.3-wave1-qa-result.json")

PAGES = [
    ("QA-01", "/katalog", "Catalog hub"),
    ("QA-02", "/katalog/nejtralnoe-oborudovanie", "Neutral hub"),
    ("QA-03", "/index.php?route=product/category&path=301", "Столы PLP"),
    ("QA-04", "/index.php?route=product/category&path=80", "Моечные ванны PLP"),
    (
        "QA-05",
        "/index.php?route=product/product&product_id=3071",
        "Product 3071 PDP (should be hidden/inactive)",
    ),
    (
        "QA-06",
        "/index.php?route=product/product&product_id=1",
        "Reference PDP sample",
    ),
]

TEST_MARKERS = [
    "ТЕСТ",
    "тест",
    "шир ТЕСТ",
    "выс ТЕСТ",
    "дл ТЕСТ",
    "марка стали ТЕСТ",
    "толщина столешницы ТЕСТ",
    "толщина материала ног ТЕСТ",
    "shir-test",
    "vys-test",
    "dl-test",
]


def fetch(url):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "BZPM-M8.3-QA"})
    try:
        resp = urllib.request.urlopen(req, timeout=60, context=ctx)
        body = resp.read().decode("utf-8", "replace")
        return {"status": resp.status, "url": url, "body": body, "error": None}
    except Exception as e:
        return {"status": None, "url": url, "body": "", "error": str(e)}


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    checks = []
    summary = {"pass": 0, "fail": 0, "unknown": 0}

    for check_id, path, label in PAGES:
        page = fetch(BASE + path)
        hits = [m for m in TEST_MARKERS if m in page["body"]]
        if page["error"]:
            status = "unknown"
            detail = page["error"]
        elif check_id == "QA-05":
            # inactive product: may 404 or show disabled — no TEST filter attrs required
            status = "pass" if not hits else "fail"
            detail = f"PDP status={page['status']} test_marker_hits={hits}"
        elif check_id in ("QA-01", "QA-02", "QA-03", "QA-04"):
            status = "pass" if not hits else "fail"
            detail = f"{label} status={page['status']} test_marker_hits={hits}"
        else:
            status = "pass" if page["status"] == 200 else "unknown"
            detail = f"{label} status={page['status']}"

        checks.append({"id": check_id, "path": path, "status": status, "detail": detail})
        summary[status] = summary.get(status, 0) + 1

    result = {
        "qa_utc": datetime.now(timezone.utc).isoformat(),
        "base": BASE,
        "checks": checks,
        "summary": summary,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
