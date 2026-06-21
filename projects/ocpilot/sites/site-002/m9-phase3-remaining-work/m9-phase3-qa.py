#!/usr/bin/env python3
"""BZPM M9 Phase 3 — storefront QA on TEST (322, 207, 326 + 301/80 regression)."""
import json
import re
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://zpm.new-site.space"
OUT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\m9-phase3\m9-phase3-qa-result.json")

PAGES = [
    ("QA-01", "/katalog/nejtralnoe-oborudovanie/stoly/", "Столы PLP regression (301)"),
    ("QA-02", "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/", "Моечные ванны PLP regression (80)"),
    ("QA-03", "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/", "Подтоварники PLP (322)"),
    ("QA-04", "/index.php?route=product/category&path=322", "Подтоварники PLP (path=322)"),
    ("QA-05", "/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/", "Зонты PLP (207)"),
    ("QA-06", "/index.php?route=product/category&path=207", "Зонты PLP (path=207)"),
    ("QA-07", "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/", "Тележки серв. PLP (326)"),
    ("QA-08", "/index.php?route=product/category&path=326", "Тележки серв. PLP (path=326)"),
    (
        "QA-09",
        "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/podtovarniki-premium/podtovarnik-pp-p-12-6-1200h600h300",
        "Reference podtovarnik PDP",
    ),
    (
        "QA-10",
        "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/telezhka-dlya-sbora-posudy-ts-1-800h500h930",
        "Reference telezhka PDP",
    ),
    (
        "QA-11",
        "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850",
        "Reference table PDP",
    ),
    (
        "QA-12",
        "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-celnotyanutye-premium-3/vanna-moechnaya-vmc-p3-2-500-1150h700h850",
        "Reference sink PDP",
    ),
]

TABLE_PRIMARY = [
    "Цена (₽)", "Только в наличии", "Длина (мм)", "Ширина (мм)", "Высота (мм)",
    "Материал столешницы", "Конструкция полки", "Тип опоры", "Макс. нагрузка", "Наличие борта",
]
SINK_PRIMARY = [
    "Цена (₽)", "Только в наличии", "Длина (мм)", "Ширина (мм)", "Высота (мм)",
    "Размер раковины", "Мойка", "Наличие борта",
]
PODTOVARNIKI_PRIMARY = [
    "Цена (₽)", "Только в наличии", "Длина (мм)", "Ширина (мм)", "Высота (мм)",
    "Конструкция полки", "Макс. нагрузка",
]
PODTOVARNIKI_SECONDARY = [
    "Дополнительные параметры", "Материал столешницы", "Тип опоры", "Конструкция",
]
ZONTY_PRIMARY = [
    "Цена (₽)", "Только в наличии", "Длина (мм)", "Ширина (мм)", "Высота (мм)", "Конструкция",
]
ZONTY_SECONDARY = ["Дополнительные параметры", "Страна производства"]
TELEZHKI_PRIMARY = [
    "Цена (₽)", "Только в наличии", "Длина (мм)", "Ширина (мм)", "Высота (мм)",
]

GLOBAL_HIDDEN = [
    "Длина в упаковке", "Дополнительные сведения", "Комплект поставки",
    "Габариты нетто", "Стандарт",
]
CROSS_FAMILY = [
    "Мойка", "Отверстие под смеситель", "Размер раковины",
]

PHP_ERROR_MARKERS = ["Fatal error", "Parse error", "Warning:", "Notice:", "Uncaught"]


def fetch(url):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "BZPM-M9-Phase3-QA"})
    try:
        resp = urllib.request.urlopen(req, timeout=60, context=ctx)
        body = resp.read().decode("utf-8", "replace")
        return {"status": resp.status, "url": url, "body": body, "error": None}
    except Exception as e:
        return {"status": None, "url": url, "body": "", "error": str(e)}


def extract_filter_sidebar(body):
    m = re.search(r'<div class="flt"[^>]*data-filters[^>]*>(.*?)</form>\s*</div>', body, re.S)
    return m.group(1) if m else body


def hits_in_sidebar(body, markers):
    scope = extract_filter_sidebar(body)
    return [m for m in markers if m in scope]


def profile_layout_ok(body):
    scope = extract_filter_sidebar(body)
    if "Длина (мм)" not in scope:
        return False
    if "Дополнительные параметры" in scope:
        return scope.index("Длина (мм)") < scope.find("Дополнительные параметры")
    return True


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    checks = []
    summary = {"pass": 0, "fail": 0, "unknown": 0}

    for check_id, path, label in PAGES:
        page = fetch(BASE + path)
        body = page["body"] or ""
        php_hits = [m for m in PHP_ERROR_MARKERS if m in body]
        sidebar = extract_filter_sidebar(body)

        if page["error"]:
            status, detail = "unknown", page["error"]
        elif php_hits:
            status, detail = "fail", f"PHP markers: {php_hits}"
        elif check_id in ("QA-01",):
            primary = hits_in_sidebar(body, TABLE_PRIMARY)
            hidden = hits_in_sidebar(body, CROSS_FAMILY + GLOBAL_HIDDEN)
            ok = page["status"] == 200 and len(primary) >= 8 and "Мойка" not in sidebar
            status = "pass" if ok else "fail"
            detail = f"{label} status={page['status']} primary={len(primary)}/10 hidden={hidden}"
        elif check_id in ("QA-02",):
            primary = hits_in_sidebar(body, SINK_PRIMARY)
            hidden = hits_in_sidebar(body, ["Конструкция полки", "Макс. нагрузка"] + GLOBAL_HIDDEN)
            ok = page["status"] == 200 and len(primary) >= 7 and "Конструкция полки" not in sidebar
            status = "pass" if ok else "fail"
            detail = f"{label} status={page['status']} primary={len(primary)}/8 hidden={hidden}"
        elif check_id in ("QA-03", "QA-04"):
            primary = hits_in_sidebar(body, PODTOVARNIKI_PRIMARY)
            secondary = hits_in_sidebar(body, PODTOVARNIKI_SECONDARY)
            hidden = hits_in_sidebar(body, CROSS_FAMILY + GLOBAL_HIDDEN)
            ok = (
                page["status"] == 200
                and len(primary) >= 6
                and "Дополнительные параметры" in sidebar
                and profile_layout_ok(body)
                and "Мойка" not in sidebar
                and not [h for h in hidden if h in CROSS_FAMILY]
            )
            status = "pass" if ok else "fail"
            detail = (
                f"{label} status={page['status']} primary={len(primary)}/7 "
                f"secondary={secondary[:4]} hidden={hidden} profile_layout={profile_layout_ok(body)}"
            )
        elif check_id in ("QA-05", "QA-06"):
            primary = hits_in_sidebar(body, ZONTY_PRIMARY)
            secondary = hits_in_sidebar(body, ZONTY_SECONDARY)
            hidden = hits_in_sidebar(body, ["Мойка", "Конструкция полки", "Габариты нетто", "Стандарт"])
            ok = (
                page["status"] == 200
                and len(primary) >= 5
                and "Конструкция" in sidebar
                and "Мойка" not in sidebar
                and "Габариты нетто" not in sidebar
            )
            status = "pass" if ok else "fail"
            detail = (
                f"{label} status={page['status']} primary={len(primary)}/6 "
                f"secondary={secondary} hidden={hidden}"
            )
        elif check_id in ("QA-07", "QA-08"):
            primary = hits_in_sidebar(body, TELEZHKI_PRIMARY)
            hidden = hits_in_sidebar(body, ["Стандарт", "Мойка", "Конструкция полки"] + GLOBAL_HIDDEN)
            ok = page["status"] == 200 and len(primary) >= 5 and "Стандарт" not in sidebar
            status = "pass" if ok else "fail"
            detail = f"{label} status={page['status']} primary={len(primary)}/5 hidden={hidden}"
        elif check_id in ("QA-09", "QA-10", "QA-11", "QA-12"):
            status = "pass" if page["status"] == 200 and not php_hits else "fail"
            detail = f"PDP status={page['status']}"
        else:
            status, detail = "unknown", label

        checks.append({"id": check_id, "path": path, "status": status, "detail": detail})
        summary[status] = summary.get(status, 0) + 1

    result = {
        "task": "M9 Phase 3 remaining branches QA",
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
