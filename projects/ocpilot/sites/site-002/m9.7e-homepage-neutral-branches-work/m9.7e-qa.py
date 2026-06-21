#!/usr/bin/env python3
"""BZPM M9.7E — QA after homepage neutral branch deploy."""
import json
import re
import urllib.request
from pathlib import Path

BASE = "https://zpm.new-site.space"
WORK = Path(__file__).resolve().parent
QA_DIR = WORK / "qa"
QA_DIR.mkdir(exist_ok=True)

EXPECTED_HOME = {
    "Столы",
    "Моечные ванны",
    "Подтоварники и подставки",
    "Зонты вытяжные",
    "Тележки сервировочные",
}
FORBIDDEN_HOME = {
    "Нейтральное оборудование",
    "Столы производственные",
    "Полки",
    "Стеллажи",
    "Подтоварники",
    "Тележки",
    "Шкафы",
    "Лари",
}
EXPECTED_BRANCH_ORDER = [
    "Столы",
    "Моечные ванны",
    "Подтоварники и подставки",
    "Зонты вытяжные",
    "Тележки сервировочные",
]
PHP_ERROR_MARKERS = ("Notice:", "Warning:", "Fatal error:")

QA_URLS = [
    ("home", "/"),
    ("katalog", "/katalog"),
    ("neutral_hub", "/katalog/nejtralnoe-oborudovanie"),
    ("stoly", "/katalog/nejtralnoe-oborudovanie/stoly/"),
    ("vanny", "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"),
]


def fetch(path: str) -> dict:
    url = BASE + path
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "M9.7E-QA"})
        resp = urllib.request.urlopen(req, timeout=60)
        body = resp.read().decode("utf-8", "replace")
        return {"url": url, "status": resp.status, "body": body, "error": None}
    except Exception as e:
        return {"url": url, "status": None, "body": "", "error": str(e)}


def homepage_cat_cards(html: str) -> list:
    m = re.search(r'<section class="zpm-cat-sections"[^>]*>.*?</section>', html, re.S)
    block = m.group(0) if m else ""
    cards = []
    for card in re.findall(r'<a class="zpm-cat-card".*?</a>', block, re.S):
        title_m = re.search(r'zpm-cat-card__title">([^<]+)</div>', card)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', card)
        href_m = re.search(r'href="([^"]+)"', card)
        if title_m:
            cards.append(
                {
                    "name": title_m.group(1).strip(),
                    "img": img_m.group(1) if img_m else None,
                    "href": href_m.group(1) if href_m else None,
                }
            )
    return cards


def hub_cards(html: str) -> list:
    cards = []
    for card in re.findall(r'<a class="zpm-cat-card".*?</a>', html, re.S):
        title_m = re.search(r'zpm-cat-card__title">([^<]+)</div>', card)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', card)
        href_m = re.search(r'href="([^"]+)"', card)
        if title_m:
            cards.append(
                {
                    "name": title_m.group(1).strip(),
                    "img": img_m.group(1) if img_m else None,
                    "href": href_m.group(1) if href_m else None,
                }
            )
    return cards


def neutral_megamenu(html: str) -> list:
    m = re.search(
        r'data-cat-pane="Нейтральное оборудование".*?zpm-catalog__grid(.*?)zpm-catalog__last-block',
        html,
        re.S,
    )
    if not m:
        return []
    block = m.group(1)
    items = []
    for tile in re.findall(r'<a class="zpm-catalog__tile".*?</a>', block, re.S):
        title_m = re.search(r'zpm-catalog__tile-title">([^<]+)</span>', tile)
        count_m = re.search(r'<span>(\d+) шт\.</span>', tile)
        if title_m:
            items.append(
                {
                    "name": title_m.group(1).strip(),
                    "count": int(count_m.group(1)) if count_m else None,
                }
            )
    return items


def php_errors(html: str) -> list:
    return [m for m in PHP_ERROR_MARKERS if m in html]


def main():
    pages = {name: fetch(path) for name, path in QA_URLS}
    checks = []
    summary = {"pass": 0, "fail": 0, "warn": 0}

    def add(cid, status, detail, evidence=None):
        checks.append({"id": cid, "status": status, "detail": detail, "evidence": evidence or {}})
        summary[status] = summary.get(status, 0) + 1

    for name, page in pages.items():
        errs = php_errors(page["body"])
        if page["error"]:
            add(f"HTTP-{name}", "fail", f"{name}: {page['error']}")
        elif errs:
            add(f"HTTP-{name}", "fail", f"{name}: PHP markers {errs}")
        elif page["status"] == 200:
            add(f"HTTP-{name}", "pass", f"{name}: HTTP 200")
        else:
            add(f"HTTP-{name}", "fail", f"{name}: status={page['status']}")

    home_cards = homepage_cat_cards(pages["home"]["body"])
    home_names = [c["name"] for c in home_cards]
    home_set = set(home_names)
    placeholders = [c["name"] for c in home_cards if c.get("img") and "placeholder" in c["img"]]
    forbidden_present = sorted(home_set & FORBIDDEN_HOME)
    missing = sorted(EXPECTED_HOME - home_set)

    add(
        "HOME-CARD-COUNT",
        "pass" if len(home_cards) == 5 else "fail",
        f"homepage cards={len(home_cards)} names={home_names}",
        {"cards": home_cards},
    )
    add(
        "HOME-EXPECTED-SET",
        "pass" if not missing and home_set == EXPECTED_HOME else "fail",
        f"missing={missing} extra={sorted(home_set - EXPECTED_HOME)}",
    )
    add(
        "HOME-ORDER",
        "pass" if home_names == EXPECTED_BRANCH_ORDER else "fail",
        f"order={home_names}",
    )
    add("HOME-NO-ROOT", "pass" if "Нейтральное оборудование" not in home_set else "fail", f"forbidden root present")
    add("HOME-NO-FORBIDDEN", "pass" if not forbidden_present else "fail", f"forbidden={forbidden_present}")
    add("HOME-NO-PLACEHOLDER", "pass" if not placeholders else "fail", f"placeholder={placeholders}")

    hub = hub_cards(pages["neutral_hub"]["body"])
    add(
        "REG-HUB-CARDS",
        "pass" if len(hub) == 5 else "fail",
        f"hub cards={len(hub)}",
        {"hub_cards": hub},
    )

    mm = neutral_megamenu(pages["home"]["body"])
    mm_zero = [x["name"] for x in mm if x.get("count") == 0]
    add(
        "REG-MEGAMENU",
        "pass" if len(mm) == 5 and not mm_zero else "fail",
        f"megamenu tiles={len(mm)} zero={mm_zero}",
        {"megamenu": mm},
    )

    result = {
        "task": "M9.7E homepage neutral branches QA",
        "base_url": BASE,
        "summary": summary,
        "checks": checks,
        "homepage_cards": home_cards,
        "hub_cards": hub,
        "megamenu": mm,
    }

    out = QA_DIR / "m9.7e-qa-result.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"summary": summary, "homepage_cards": home_cards}, ensure_ascii=False, indent=2))
    print("Saved:", out)


if __name__ == "__main__":
    main()
