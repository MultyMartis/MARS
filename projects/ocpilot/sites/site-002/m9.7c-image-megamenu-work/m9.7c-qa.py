#!/usr/bin/env python3
"""M9.7C regression QA on TEST."""
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://zpm.new-site.space"
OUT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\m9.7c-image-megamenu-work\qa\m9.7c-qa-result.json")

EXPECTED_MEGAMENU = {
    "Столы",
    "Моечные ванны",
    "Подтоварники и подставки",
    "Зонты вытяжные",
    "Тележки сервировочные",
}
FORBIDDEN_MEGAMENU = {
    "Стеллажи",
    "Полки",
    "Подтоварники",
    "Тележки",
    "Шкафы",
    "Лари",
    "Столы производственные",
}

URLS = [
    ("home", "/"),
    ("katalog", "/katalog"),
    ("neutral_hub", "/katalog/nejtralnoe-oborudovanie"),
    ("stoly", "/katalog/nejtralnoe-oborudovanie/stoly/"),
    ("vanny", "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"),
    ("podtovarniki", "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/"),
    ("zonty", "/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/"),
    ("telezhki", "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/"),
    (
        "ref_table_pdp",
        "/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850",
    ),
    (
        "ref_sink_pdp",
        "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/vanny-celnotyanutye-premium-3/vanna-moechnaya-vmc-p3-2-500-1150h700h850",
    ),
]


def fetch(path):
    url = BASE + path
    req = urllib.request.Request(url, headers={"User-Agent": "M9.7C-QA"})
    try:
        resp = urllib.request.urlopen(req, timeout=60)
        return resp.getcode(), resp.read().decode("utf-8", "replace")
    except Exception as e:
        return 0, str(e)


def neutral_megamenu(html):
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
        img_m = re.search(r'<img[^>]+src="([^"]+)"', tile)
        if title_m:
            items.append(
                {
                    "name": title_m.group(1).strip(),
                    "count": int(count_m.group(1)) if count_m else None,
                    "img": img_m.group(1) if img_m else None,
                }
            )
    return items


def hub_cards(html):
    cards = []
    for card in re.findall(r'<a class="zpm-cat-card".*?</a>', html, re.S):
        title_m = re.search(r'zpm-cat-card__title">([^<]+)</div>', card)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', card)
        if title_m:
            cards.append({"name": title_m.group(1).strip(), "img": img_m.group(1) if img_m else None})
    return cards


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    checks = []
    url_results = {}

    for key, path in URLS:
        code, html = fetch(path)
        php_warn = bool(re.search(r"(Notice:|Warning:|Fatal error:)", html))
        url_results[key] = {"path": path, "http": code, "php_warnings": php_warn}
        checks.append(
            {
                "id": f"HTTP-{key}",
                "result": "PASS" if code == 200 else "FAIL",
                "detail": f"{key}: HTTP {code}",
            }
        )
        if php_warn:
            checks.append({"id": f"PHP-{key}", "result": "FAIL", "detail": "PHP warning detected"})

    home_html = url_results["home"]["http"] and fetch("/")[1] or ""
    hub_html = fetch("/katalog/nejtralnoe-oborudovanie")[1]

    mm = neutral_megamenu(home_html)
    names = {x["name"] for x in mm}
    zero_counts = [x["name"] for x in mm if x.get("count") == 0]
    placeholders = [x["name"] for x in mm if x.get("img") and "placeholder" in x["img"]]
    forbidden_present = sorted(names & FORBIDDEN_MEGAMENU)
    missing_expected = sorted(EXPECTED_MEGAMENU - names)

    checks.append(
        {
            "id": "MM-COUNT",
            "result": "PASS" if len(mm) == 5 else "FAIL",
            "detail": f"megamenu neutral tiles={len(mm)} names={[x['name'] for x in mm]}",
        }
    )
    checks.append(
        {
            "id": "MM-NO-ZERO",
            "result": "PASS" if not zero_counts else "FAIL",
            "detail": f"zero-count tiles: {zero_counts}",
        }
    )
    checks.append(
        {
            "id": "MM-NO-FORBIDDEN",
            "result": "PASS" if not forbidden_present else "FAIL",
            "detail": f"forbidden still visible: {forbidden_present}",
        }
    )
    checks.append(
        {
            "id": "MM-EXPECTED-SET",
            "result": "PASS" if not missing_expected and names == EXPECTED_MEGAMENU else "FAIL",
            "detail": f"missing={missing_expected}",
        }
    )
    checks.append(
        {
            "id": "MM-NO-PLACEHOLDER",
            "result": "PASS" if not placeholders else "FAIL",
            "detail": f"placeholder imgs: {placeholders}",
        }
    )

    cards = hub_cards(hub_html)
    hub_placeholders = [c["name"] for c in cards if c.get("img") and "placeholder" in c["img"]]
    checks.append(
        {
            "id": "HUB-CARD-COUNT",
            "result": "PASS" if len(cards) == 5 else "FAIL",
            "detail": f"hub cards={len(cards)} names={[c['name'] for c in cards]}",
        }
    )
    checks.append(
        {
            "id": "HUB-NO-PLACEHOLDER",
            "result": "PASS" if not hub_placeholders else "FAIL",
            "detail": f"hub placeholder imgs: {hub_placeholders}",
        }
    )

    summary = {
        "pass": sum(1 for c in checks if c["result"] == "PASS"),
        "fail": sum(1 for c in checks if c["result"] == "FAIL"),
    }
    result = {
        "task": "M9.7C",
        "base_url": BASE,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "megamenu_before_note": "12 neutral tiles incl 7 zero-count before fix",
        "megamenu_after": mm,
        "hub_cards": cards,
        "url_results": {k: {"path": v["path"], "http": v["http"], "php_warnings": v["php_warnings"]} for k, v in url_results.items()},
        "checks": checks,
        "summary": summary,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    for c in checks:
        if c["result"] == "FAIL":
            print("FAIL", c["id"], c["detail"])


if __name__ == "__main__":
    main()
