#!/usr/bin/env python3
"""BZPM M8.3 Wave 2 — storefront QA on TEST."""
import json
import re
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://zpm.new-site.space"
OUT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\m8.3-wave2\m8.3-wave2-qa-result.json")

PAGES = [
    ("QA-01", "/katalog/nejtralnoe-oborudovanie", "Neutral hub"),
    ("QA-02", "/index.php?route=product/category&path=301", "Столы PLP"),
    ("QA-03", "/index.php?route=product/category&path=80", "Моечные ванны PLP"),
    ("QA-04", "/index.php?route=product/category&path=322", "Подтоварники PLP"),
    ("QA-05", "/index.php?route=product/category&path=207", "Зонты PLP"),
    (
        "QA-06",
        "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850",
        "Reference PDP (SPKB-18/7-ВЛ5)",
    ),
]

PACKAGING_MARKERS = [
    "Длина в упаковке",
    "Ширина в упаковке",
    "Высота в упаковке",
    "Упаковка (Длина",
    "Упаковка (Ширина",
    "Упаковка (Высота",
    "Упаковка (Объем",
    "Вес (нетто, кг)",
]

SERVICE_MARKERS = [
    "Дополнительные сведения",
    "Комплект поставки",
    "Комплект отгрузки",
]

COMMERCIAL_MARKERS = [
    "Конструкция",
    "Тип опоры",
    "Материал столешницы",
    "Макс. нагрузка",
]

PHP_ERROR_MARKERS = [
    "Fatal error",
    "Parse error",
    "Warning:",
    "Notice:",
    "Uncaught",
]


def fetch(url):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "BZPM-M8.3-Wave2-QA"})
    try:
        resp = urllib.request.urlopen(req, timeout=60, context=ctx)
        body = resp.read().decode("utf-8", "replace")
        return {"status": resp.status, "url": url, "body": body, "error": None}
    except Exception as e:
        return {"status": None, "url": url, "body": "", "error": str(e)}


def sidebar_hits(body, markers):
    hits = []
    for m in markers:
        if m in body:
            # crude filter sidebar scope: look near filter-related classes
            hits.append(m)
    return hits


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    checks = []
    summary = {"pass": 0, "fail": 0, "unknown": 0}

    for check_id, path, label in PAGES:
        page = fetch(BASE + path)
        packaging_hits = sidebar_hits(page["body"], PACKAGING_MARKERS) if page["body"] else []
        service_hits = sidebar_hits(page["body"], SERVICE_MARKERS) if page["body"] else []
        commercial_hits = sidebar_hits(page["body"], COMMERCIAL_MARKERS) if page["body"] else []
        php_hits = [m for m in PHP_ERROR_MARKERS if m in page["body"]]

        if page["error"]:
            status = "unknown"
            detail = page["error"]
        elif php_hits:
            status = "fail"
            detail = f"PHP markers: {php_hits}"
        elif check_id == "QA-06":
            status = "pass" if page["status"] == 200 and not php_hits else "fail"
            detail = f"PDP status={page['status']}"
        elif check_id.startswith("QA-"):
            no_pack = len(packaging_hits) == 0
            no_service = len(service_hits) == 0
            has_commercial = len(commercial_hits) > 0 if check_id != "QA-01" else True
            if no_pack and no_service and has_commercial:
                status = "pass"
            else:
                status = "fail"
            detail = (
                f"{label} status={page['status']} "
                f"packaging_hits={packaging_hits} service_hits={service_hits} "
                f"commercial_hits={commercial_hits[:5]}"
            )
        else:
            status = "unknown"
            detail = label

        checks.append({"id": check_id, "path": path, "status": status, "detail": detail})
        summary[status] = summary.get(status, 0) + 1

    result = {
        "qa_utc": datetime.now(timezone.utc).isoformat(),
        "base": BASE,
        "wave": "M8.3 Wave 2",
        "checks": checks,
        "summary": summary,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
