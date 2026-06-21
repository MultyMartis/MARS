#!/usr/bin/env python3
"""BZPM M9 Phase 1 — storefront QA on TEST (Tables profile 301)."""
import json
import re
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://zpm.new-site.space"
OUT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\m9-phase1\m9-phase1-qa-result.json")

PAGES = [
    ("QA-01", "/katalog/nejtralnoe-oborudovanie/stoly/", "Столы PLP (SEO URL)"),
    ("QA-02", "/index.php?route=product/category&path=301", "Столы PLP (path=301)"),
    ("QA-03", "/katalog/nejtralnoe-oborudovanie", "Neutral hub"),
    ("QA-04", "/index.php?route=product/category&path=80", "Моечные ванны (no profile regression)"),
    (
        "QA-05",
        "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850",
        "Reference PDP (SPKB-18/7-ВЛ5)",
    ),
]

PRIMARY_MARKERS = [
    "Цена (₽)",
    "Только в наличии",
    "Длина (мм)",
    "Ширина (мм)",
    "Высота (мм)",
    "Материал столешницы",
    "Конструкция полки",
    "Тип опоры",
    "Макс. нагрузка",
    "Наличие борта",
]

SECONDARY_MARKERS = [
    "Дополнительные параметры",
    "Конструкция",
    "Материал полки",
    "Ножки",
    "Регулируемость опоры",
]

HIDDEN_MARKERS = [
    "Мойка",
    "Отверстие под смеситель",
    "Размер раковины",
    "Длина в упаковке",
    "Дополнительные сведения",
    "Комплект поставки",
    "Габариты нетто",
    "Страна производства",
    "Стандарт",
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
    req = urllib.request.Request(url, headers={"User-Agent": "BZPM-M9-Phase1-QA"})
    try:
        resp = urllib.request.urlopen(req, timeout=60, context=ctx)
        body = resp.read().decode("utf-8", "replace")
        return {"status": resp.status, "url": url, "body": body, "error": None}
    except Exception as e:
        return {"status": None, "url": url, "body": "", "error": str(e)}


def extract_filter_sidebar(body):
    m = re.search(r'<div class="flt"[^>]*data-filters[^>]*>(.*?)</form>\s*</div>', body, re.S)
    if m:
        return m.group(1)
    return body


def hits_in_sidebar(body, markers):
    scope = extract_filter_sidebar(body)
    return [m for m in markers if m in scope]


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    checks = []
    summary = {"pass": 0, "fail": 0, "unknown": 0}

    for check_id, path, label in PAGES:
        page = fetch(BASE + path)
        body = page["body"] or ""
        php_hits = [m for m in PHP_ERROR_MARKERS if m in body]

        if page["error"]:
            status = "unknown"
            detail = page["error"]
        elif php_hits:
            status = "fail"
            detail = f"PHP markers: {php_hits}"
        elif check_id in ("QA-01", "QA-02"):
            primary_hits = hits_in_sidebar(body, PRIMARY_MARKERS)
            secondary_hits = hits_in_sidebar(body, SECONDARY_MARKERS)
            hidden_hits = hits_in_sidebar(body, HIDDEN_MARKERS)
            has_secondary_section = "Дополнительные параметры" in extract_filter_sidebar(body)
            ok = (
                page["status"] == 200
                and len(primary_hits) >= 8
                and has_secondary_section
                and "Мойка" not in hidden_hits
                and len([h for h in hidden_hits if "упаковк" in h.lower() or h in HIDDEN_MARKERS[3:]]) == 0
            )
            status = "pass" if ok else "fail"
            detail = (
                f"{label} status={page['status']} primary={len(primary_hits)}/10 "
                f"secondary_section={has_secondary_section} secondary_markers={secondary_hits[:4]} "
                f"hidden_hits={hidden_hits}"
            )
        elif check_id == "QA-03":
            status = "pass" if page["status"] == 200 and not php_hits else "fail"
            detail = f"Neutral hub status={page['status']}"
        elif check_id == "QA-04":
            hidden_hits = hits_in_sidebar(body, HIDDEN_MARKERS[3:6])
            status = "pass" if page["status"] == 200 and not php_hits and not hidden_hits else "fail"
            detail = f"Vanny PLP status={page['status']} packaging/service_hits={hidden_hits}"
        elif check_id == "QA-05":
            status = "pass" if page["status"] == 200 and not php_hits else "fail"
            detail = f"PDP status={page['status']}"
        else:
            status = "unknown"
            detail = label

        checks.append({"id": check_id, "path": path, "status": status, "detail": detail})
        summary[status] = summary.get(status, 0) + 1

    result = {
        "task": "M9 Phase 1 Tables profile QA",
        "site": "SITE-002",
        "test_url": BASE,
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "summary": summary,
        "checks": checks,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
