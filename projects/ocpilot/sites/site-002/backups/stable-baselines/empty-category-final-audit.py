#!/usr/bin/env python3
"""BZPM — Empty category final audit (read-only, no code changes)."""
import json
import re
import ssl
import urllib.parse
import urllib.request
import http.cookiejar
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

BASE = "https://zpm.new-site.space"
PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"

OUT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\empty-category-audit-data.json")
LIVE_FILES_DIR = Path(
    r"C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-baselines\SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI\files"
)

NEUTRAL_ROOT_ID = 79
BRANCH_IDS = [301, 80, 322, 207, 326]
HIDDEN_EMPTY_SLUGS = ["polki", "stellazhi", "shkafy", "lari", "stoly-proizvodstvennye"]
FORBIDDEN_MEGAMENU = {
    "Стеллажи", "Полки", "Подтоварники", "Тележки", "Шкафы", "Лари", "Столы производственные",
}


def fetch(path: str) -> dict:
    url = BASE + path
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "BZPM-Empty-Category-Audit/1.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=90) as resp:
            body = resp.read().decode("utf-8", "replace")
            return {"status": resp.status, "body": body, "error": None}
    except Exception as e:
        return {"status": None, "body": "", "error": str(e)}


def pma_session():
    ctx = ssl.create_default_context()
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cj),
        urllib.request.HTTPSHandler(context=ctx),
    )
    lp = op.open(PMA + "/", timeout=60).read().decode("utf-8", "replace")
    token = re.search(r'name="token"\s+value="([^"]+)"', lp).group(1)
    op.open(
        urllib.request.Request(
            PMA + "/index.php",
            data=urllib.parse.urlencode(
                {
                    "pma_username": DB_USER,
                    "pma_password": DB_PASS,
                    "server": "1",
                    "target": "index.php",
                    "token": token,
                }
            ).encode(),
            method="POST",
        ),
        timeout=60,
    )
    db_html = op.open(PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60).read().decode(
        "utf-8", "replace"
    )
    csrf = re.search(r'name="token"\s+value="([^"]+)"', db_html).group(1)
    return op, csrf


def pma_sql(op, csrf, sql: str) -> list:
    html = op.open(
        urllib.request.Request(
            PMA + "/sql.php",
            data=urllib.parse.urlencode(
                {"db": DB, "sql_query": sql, "token": csrf, "sql_delimiter": ";"}
            ).encode(),
            method="POST",
        ),
        timeout=240,
    ).read().decode("utf-8", "replace")
    rows = []
    for tbl in re.findall(r'<table[^>]*class="[^"]*table[^"]*"[^>]*>(.*?)</table>', html, re.S):
        if "Browse" in tbl and "Drop" in tbl:
            continue
        parsed = []
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", tbl, re.S):
            cells = [
                unescape(re.sub(r"<[^>]+>", " ", c).strip())
                for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)
            ]
            cells = [re.sub(r"\s+", " ", c) for c in cells if c.strip()]
            if cells:
                parsed.append(cells)
        if len(parsed) >= 2 and not parsed[0][0].startswith("Table navigation"):
            rows = parsed
            break
    if len(rows) < 2:
        return []
    h = [x.lower() for x in rows[0]]
    return [dict(zip(h, r)) for r in rows[1:] if len(r) == len(h)]


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
        href_m = re.search(r'href="([^"]+)"', tile)
        if title_m:
            items.append(
                {
                    "name": title_m.group(1).strip(),
                    "count": int(count_m.group(1)) if count_m else None,
                    "href": href_m.group(1) if href_m else None,
                }
            )
    return items


def hub_cards(html: str) -> list:
    cards = []
    for card in re.findall(r'<a class="zpm-cat-card".*?</a>', html, re.S):
        title_m = re.search(r'zpm-cat-card__title">([^<]+)</div>', card)
        href_m = re.search(r'href="([^"]+)"', card)
        if title_m:
            cards.append({"name": title_m.group(1).strip(), "href": href_m.group(1) if href_m else None})
    return cards


def offcanvas_categories(html: str) -> list:
    items = []
    m = re.search(r'data-offcanvas-menu.*?offcanvas', html, re.S)
    block = m.group(0) if m else html
    for a in re.findall(r'<a[^>]+href="(/katalog/[^"]+)"[^>]*>([^<]+)</a>', block):
        href, name = a
        if "nejtralnoe-oborudovanie" in href:
            items.append({"name": name.strip(), "href": href})
    return items


def catalog_sections(html: str) -> list:
    items = []
    for a in re.findall(r'catalogsections[\s\S]*?<a[^>]+href="([^"]+)"[^>]*>[\s\S]*?<[^>]+>([^<]+)<', html):
        items.append({"href": a[0], "name": a[1].strip()})
    return items


def subcategory_chips(html: str) -> list:
    return re.findall(r'zpm-sub-cat-chips[\s\S]*?<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>', html)


def footer_catalog_links(html: str) -> list:
    m = re.search(r"zpm-footer__col--catalog.*?</div>\s*</div>", html, re.S)
    block = m.group(0) if m else html
    return re.findall(r'class="zpm-footer__link"[^>]*href="([^"]+)"[^>]*>([^<]+)</a>', block)


def katalog_page_categories(html: str) -> list:
    items = []
    for tile in re.findall(r'zpm-catalog__tile.*?href="([^"]+)".*?zpm-catalog__tile-title">([^<]+)</span>', html, re.S):
        items.append({"href": tile[0], "name": tile[1].strip()})
    return items


def row_val(row: dict, *keys: str):
    for k in keys:
        if k in row:
            return row[k]
    for k, v in row.items():
        lk = k.lower()
        for want in keys:
            if want.lower() in lk:
                return v
    return None


def row_int(row: dict, *keys: str) -> int:
    v = row_val(row, *keys)
    try:
        return int(v or 0)
    except (TypeError, ValueError):
        return 0


def row_name(row: dict) -> str:
    return str(row_val(row, "name", "cd.name") or "").strip()


def read_local(path_rel: str) -> str:
    p = LIVE_FILES_DIR / path_rel.replace("/", "\\")
    if p.exists():
        return p.read_text(encoding="utf-8", errors="replace")
    return ""


def code_audit_findings() -> list:
    findings = []
    cv = read_local("system/library/zpm/category_visibility.php")
    if "prepareMegamenuCategories" in cv and "count <= 0" in cv:
        findings.append(
            {
                "layer": "PHP library",
                "file": "system/library/zpm/category_visibility.php",
                "function": "prepareMegamenuCategories",
                "filters_empty": True,
                "scope": "megamenu children only",
                "note": "Filters children with getTotalProducts <= 0",
            }
        )
    else:
        findings.append(
            {
                "layer": "PHP library",
                "file": "system/library/zpm/category_visibility.php",
                "filters_empty": False,
                "issue": "prepareMegamenuCategories missing or incomplete",
            }
        )

    header = read_local("catalog/controller/common/header.php")
    findings.append(
        {
            "layer": "Controller",
            "file": "catalog/controller/common/header.php",
            "calls_prepareMegamenu": "prepareMegamenuCategories" in header,
            "note": "Megamenu data path",
        }
    )

    katalog = read_local("catalog/controller/product/katalog.php")
    findings.append(
        {
            "layer": "Controller",
            "file": "catalog/controller/product/katalog.php",
            "calls_prepareMegamenu": "prepareMegamenuCategories" in katalog,
            "filters_on_cache_build": "getTotalProducts" in katalog,
            "note": "/katalog cache build path",
        }
    )

    category = read_local("catalog/controller/product/category.php")
    hub_filter = bool(re.search(r"totalsub\s*<=\s*0|getTotalProducts", category))
    findings.append(
        {
            "layer": "Controller",
            "file": "catalog/controller/product/category.php",
            "hub_branch_filter": hub_filter,
            "getNeutralHubBranchIds": "getNeutralHubBranchIds" in category,
            "note": "Hub mode branch cards",
        }
    )

    for twig, scope in [
        ("catalog/view/theme/default/template/common/megamenu.twig", "megamenu"),
        ("catalog/view/theme/default/template/sections/offcanvasmenu.twig", "offcanvas"),
        ("catalog/view/theme/default/template/sections/catalogsections.twig", "home catalog sections"),
        ("catalog/view/theme/default/template/product/category.twig", "category page / hub"),
    ]:
        content = read_local(twig)
        has_loop = "{% for" in content and "children" in content
        has_count_guard = "count" in content and ("if" in content or "> 0" in content)
        findings.append(
            {
                "layer": "Twig",
                "file": twig,
                "scope": scope,
                "renders_children_unconditionally": has_loop and not has_count_guard,
                "has_count_guard": has_count_guard,
            }
        )

    return findings


def main():
    op, csrf = pma_session()

    db_children = pma_sql(
        op,
        csrf,
        f"""
        SELECT c.category_id, cd.name, c.parent_id, c.status,
               (SELECT COUNT(DISTINCT p.product_id)
                FROM oc_product p
                JOIN oc_product_to_category p2c ON p2c.product_id = p.product_id
                WHERE p2c.category_id = c.category_id AND p.status = 1) AS direct_active,
               (SELECT COUNT(DISTINCT p.product_id)
                FROM oc_product p
                JOIN oc_product_to_category p2c ON p2c.product_id = p.product_id
                JOIN oc_category_path cp ON cp.category_id = p2c.category_id
                WHERE cp.path_id = c.category_id AND p.status = 1) AS subtree_active
        FROM oc_category c
        JOIN oc_category_description cd ON cd.category_id = c.category_id AND cd.language_id = 1
        WHERE c.parent_id = {NEUTRAL_ROOT_ID} AND c.status = 1
        ORDER BY cd.name
        """,
    )

    db_all_zero_subtree = pma_sql(
        op,
        csrf,
        """
        SELECT c.category_id, cd.name, c.parent_id, c.status,
               (SELECT COUNT(DISTINCT p.product_id)
                FROM oc_product p
                JOIN oc_product_to_category p2c ON p2c.product_id = p.product_id
                JOIN oc_category_path cp ON cp.category_id = p2c.category_id
                WHERE cp.path_id = c.category_id AND p.status = 1) AS subtree_active
        FROM oc_category c
        JOIN oc_category_description cd ON cd.category_id = c.category_id AND cd.language_id = 1
        WHERE c.status = 1
        HAVING subtree_active = 0
        ORDER BY c.parent_id, cd.name
        LIMIT 200
        """,
    )

    pages = {
        "home": fetch("/"),
        "katalog": fetch("/katalog"),
        "neutral_hub": fetch("/katalog/nejtralnoe-oborudovanie"),
        "stoly": fetch("/katalog/nejtralnoe-oborudovanie/stoly/"),
        "vanny": fetch("/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"),
    }

    home_html = pages["home"]["body"]
    hub_html = pages["neutral_hub"]["body"]
    katalog_html = pages["katalog"]["body"]

    live_surfaces = {
        "megamenu_neutral": neutral_megamenu(home_html),
        "hub_cards": hub_cards(hub_html),
        "katalog_tiles": katalog_page_categories(katalog_html),
        "offcanvas_neutral": offcanvas_categories(home_html),
        "footer_catalog": [{"href": h, "name": n} for h, n in footer_catalog_links(home_html)],
        "stoly_subcat_chips": [{"href": h, "name": n} for h, n in subcategory_chips(pages["stoly"]["body"])],
        "vanny_subcat_chips": [{"href": h, "name": n} for h, n in subcategory_chips(pages["vanny"]["body"])],
    }

    issues = []

    for item in live_surfaces["megamenu_neutral"]:
        if item.get("count") == 0:
            issues.append({"surface": "megamenu", "type": "zero_count_visible", "item": item})
        if item["name"] in FORBIDDEN_MEGAMENU:
            issues.append({"surface": "megamenu", "type": "forbidden_empty_branch", "item": item})

    db_zero_child_names = {row_name(r) for r in db_children if row_int(r, "subtree_active") == 0}
    db_active_child_names = {row_name(r) for r in db_children if row_int(r, "subtree_active") > 0}

    for surface_key, items in live_surfaces.items():
        for item in items:
            name = item.get("name", "")
            if name in db_zero_child_names:
                issues.append(
                    {
                        "surface": surface_key,
                        "type": "db_zero_subtree_still_visible",
                        "name": name,
                        "href": item.get("href"),
                    }
                )

    for child in db_children:
        cid = row_int(child, "category_id")
        subtree = row_int(child, "subtree_active")
        name = row_name(child)
        if subtree == 0 and cid not in BRANCH_IDS:
            issues.append(
                {
                    "surface": "database",
                    "type": "neutral_child_zero_products",
                    "category_id": cid,
                    "name": name,
                    "subtree_active": subtree,
                }
            )

    result = {
        "audited_at_utc": datetime.now(timezone.utc).isoformat(),
        "test_url": BASE,
        "authority": "LIVE TEST STATE AFTER MANUAL UI REFINEMENT",
        "db_neutral_children": db_children,
        "db_all_zero_subtree_sample": db_all_zero_subtree,
        "live_surfaces": live_surfaces,
        "code_audit": code_audit_findings(),
        "issues": issues,
        "issue_count": len(issues),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"issues": len(issues), "surfaces": {k: len(v) for k, v in live_surfaces.items()}}, ensure_ascii=False))
    if issues:
        for i in issues[:20]:
            print("ISSUE", i)


if __name__ == "__main__":
    main()
