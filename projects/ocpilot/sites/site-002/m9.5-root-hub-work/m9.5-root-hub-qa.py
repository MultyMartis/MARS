#!/usr/bin/env python3
"""BZPM M9.5 — Neutral Root Hub QA on TEST."""
import json
import re
import ssl
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://zpm.new-site.space"
OUT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\qa\m9.5-root-hub\m9.5-root-hub-qa-result.json")

HUB_URL = "/katalog/nejtralnoe-oborudovanie"
BRANCH_URLS = {
    301: "/katalog/nejtralnoe-oborudovanie/stoly/",
    80: "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
    322: "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/",
    207: "/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/",
    326: "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/",
}

HIDDEN_EMPTY_CAT_IDS = [83, 86, 85]
HIDDEN_EMPTY_SLUGS = ["polki", "stellazhi", "/telezhki/"]

TABLE_PRIMARY = [
    "Цена (₽)", "Только в наличии", "Длина (мм)", "Ширина (мм)", "Высота (мм)",
    "Материал столешницы", "Конструкция полки", "Тип опоры", "Макс. нагрузка", "Наличие борта",
]
SINK_PRIMARY = [
    "Цена (₽)", "Только в наличии", "Длина (мм)", "Ширина (мм)", "Высота (мм)",
    "Размер раковины", "Мойка", "Наличие борта",
]

PHP_ERROR_MARKERS = ["Fatal error", "Parse error", "Warning:", "Notice:", "Uncaught"]


def fetch(url):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "BZPM-M9.5-Root-Hub-QA"})
    try:
        resp = urllib.request.urlopen(req, timeout=60, context=ctx)
        body = resp.read().decode("utf-8", "replace")
        return {"status": resp.status, "url": url, "body": body, "error": None}
    except Exception as e:
        return {"status": None, "url": url, "body": "", "error": str(e)}


def extract_filter_sidebar(body):
    m = re.search(r'<div class="flt"[^>]*data-filters[^>]*>(.*?)</form>\s*</div>', body, re.S)
    return m.group(1) if m else ""


def hits_in_sidebar(body, markers):
    scope = extract_filter_sidebar(body)
    return [m for m in markers if m in scope]


def php_errors(body):
    return [m for m in PHP_ERROR_MARKERS if m in body]


def hub_card_hrefs(body):
    cards = re.findall(
        r'<a class="zpm-cat-card" href="([^"]+)"',
        body,
    )
    return cards


def hub_card_titles(body):
    return re.findall(r'<div class="zpm-cat-card__title">([^<]+)</div>', body)


checks = []


def add_check(id_, status, detail):
    checks.append({"id": id_, "status": status, "detail": detail})


# QA-01 Hub page loads
hub = fetch(BASE + HUB_URL)
if hub["error"]:
    add_check("QA-01", "fail", f"Hub fetch error: {hub['error']}")
elif hub["status"] != 200:
    add_check("QA-01", "fail", f"Hub status={hub['status']}")
else:
    add_check("QA-01", "pass", "Neutral hub HTTP 200")

body = hub.get("body", "")

# QA-02 PHP errors
errs = php_errors(body)
add_check("QA-02", "pass" if not errs else "fail", f"php_markers={errs}")

# QA-03 Hub mode class
add_check(
    "QA-03",
    "pass" if "category--hub" in body else "fail",
    "category--hub present" if "category--hub" in body else "category--hub missing",
)

# QA-04 No filter sidebar on hub
has_filter_sidebar = "data-filter-sidebar" in body and "category--hub" in body
# On hub, sidebar should be absent
sidebar_in_hub = bool(re.search(r'category--hub[\s\S]*?data-filter-sidebar', body))
add_check(
    "QA-04",
    "pass" if not sidebar_in_hub else "fail",
    "filter sidebar absent on hub" if not sidebar_in_hub else "filter sidebar still in hub markup",
)

# QA-05 No mobile filter button
has_filter_btn = "data-filter-open" in body and "category--hub" in body
filter_btn_in_hub = bool(re.search(r'category--hub[\s\S]*?data-filter-open', body))
add_check(
    "QA-05",
    "pass" if not filter_btn_in_hub else "fail",
    "mobile filter btn absent" if not filter_btn_in_hub else "data-filter-open still present",
)

# QA-06 No product grid on hub
hub_section = re.search(r'category--hub(.*?)<\/section>', body, re.S)
hub_chunk = hub_section.group(1) if hub_section else body
has_product_grid = "category__grid" in hub_chunk and "p-card" in hub_chunk
add_check(
    "QA-06",
    "pass" if not has_product_grid else "fail",
    "no product grid on hub" if not has_product_grid else "product grid still present",
)

# QA-07 No pagination on hub
has_pagination = bool(re.search(r'category--hub[\s\S]*?pagination', hub_chunk, re.I))
add_check(
    "QA-07",
    "pass" if not has_pagination else "fail",
    "no pagination on hub" if not has_pagination else "pagination still present",
)

# QA-08 No subcategory chips on hub
has_chips = "zpm-sub-cat-chips" in hub_chunk
add_check(
    "QA-08",
    "pass" if not has_chips else "fail",
    "no subcategory chips on hub" if not has_chips else "chips still present",
)

# QA-09 Hub cards count
card_count = len(re.findall(r'class="zpm-cat-card"', hub_chunk))
add_check(
    "QA-09",
    "pass" if card_count == 5 else "fail",
    f"hub_cards={card_count} (expected 5)",
)

hrefs = hub_card_hrefs(body)

# QA-10 Card titles
titles = hub_card_titles(body)
expected_titles = ["Столы", "Моечные ванны", "Подтоварники и подставки", "Зонты вытяжные", "Тележки сервировочные"]
missing_titles = [t for t in expected_titles if t not in titles]
add_check(
    "QA-10",
    "pass" if not missing_titles else "fail",
    f"titles_ok missing={missing_titles}" if missing_titles else "all 5 branch titles present",
)

# QA-11 Hidden empty categories not as hub cards
hidden_hits = []
for slug in HIDDEN_EMPTY_SLUGS:
    for h in hrefs:
        if slug in h.lower():
            hidden_hits.append(slug)
add_check(
    "QA-11",
    "pass" if not hidden_hits else "fail",
    f"empty_branch_card_slugs={hidden_hits}",
)

# QA-12 Intro copy
intro_expected = "Выберите тип нейтрального оборудования"
add_check(
    "QA-12",
    "pass" if intro_expected in body else "fail",
    "pageintro description present" if intro_expected in body else "pageintro description missing",
)

# QA-13 Certificates + dealers on hub (section markers, not exact headings)
has_cert = "certificates" in body.lower() or "сертифик" in body.lower()
has_dealers = "blockdealers" in body.lower() or "оптовик" in body.lower() or "дилер" in body.lower()
add_check(
    "QA-13",
    "pass" if has_cert and has_dealers else "fail",
    f"cert={has_cert} dealers={has_dealers}",
)

# QA-14 Branch card links
branch_link_ok = all(any(slug in h for h in hrefs) for slug in ["stoly", "moechnye-vanny", "podtovarniki", "zonty-vytyazhnye", "telezhki-servirovochnye"])
add_check(
    "QA-14",
    "pass" if branch_link_ok else "fail",
    f"card_hrefs={hrefs}",
)

# Branch regression + M9 profiles
for cat_id, path in BRANCH_URLS.items():
    page = fetch(BASE + path)
    qa_id = f"QA-BR-{cat_id}"
    if page["error"] or page["status"] != 200:
        add_check(qa_id, "fail", f"status={page.get('status')} err={page.get('error')}")
        continue
    b = page["body"]
    pe = php_errors(b)
    if pe:
        add_check(qa_id, "fail", f"php={pe}")
        continue
    has_grid = "category__grid" in b and ("p-card" in b or "productcard" in b.lower())
    has_filter = "data-filters" in b or "data-filter-sidebar" in b
    if not has_grid:
        add_check(qa_id, "fail", "product grid missing on branch")
        continue
    if not has_filter:
        add_check(qa_id, "fail", "filter missing on branch")
        continue
    # M9 profile spot-check
    if cat_id == 301:
        primary = hits_in_sidebar(b, TABLE_PRIMARY)
        add_check(qa_id, "pass" if len(primary) >= 5 else "fail", f"301 profile primary_hits={len(primary)}")
    elif cat_id == 80:
        primary = hits_in_sidebar(b, SINK_PRIMARY)
        add_check(qa_id, "pass" if len(primary) >= 5 else "fail", f"80 profile primary_hits={len(primary)}")
    else:
        add_check(qa_id, "pass", f"branch {cat_id} PLP OK (grid+filter)")

passed = sum(1 for c in checks if c["status"] == "pass")
failed = sum(1 for c in checks if c["status"] == "fail")

result = {
    "task": "M9.5 Neutral Root Hub",
    "site": "SITE-002",
    "base_url": BASE,
    "run_at_utc": datetime.now(timezone.utc).isoformat(),
    "summary": {"passed": passed, "failed": failed, "total": len(checks)},
    "checks": checks,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
print("Written:", OUT)
if failed:
    for c in checks:
        if c["status"] == "fail":
            print("FAIL:", c["id"], c["detail"])
