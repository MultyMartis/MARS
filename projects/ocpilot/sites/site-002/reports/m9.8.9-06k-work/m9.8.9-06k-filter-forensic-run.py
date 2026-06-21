#!/usr/bin/env python3
"""M9.8.9-06K — filter forensic after clean 1C import (read-only)."""
from __future__ import annotations

import json
import re
import ssl
import urllib.parse
import urllib.request
import http.cookiejar
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"
BASE_URL = "https://zpm.new-site.space"

OUT_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-06k-work")
OUT_JSON = OUT_DIR / "forensic-results.json"

CATEGORIES = {
    "stoly": {
        "category_id": 301,
        "name": "Столы",
        "url": BASE_URL + "/katalog/nejtralnoe-oborudovanie/stoly/",
        "profile": "301_stoly",
        "status": "broken",
        "profile_attrs": [22, 51, 33, 20, 25, 21, 112, 26, 31, 115, 18, 47],
    },
    "podtovarniki": {
        "category_id": 322,
        "name": "Подтоварники и подставки",
        "url": BASE_URL + "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/",
        "profile": "322_podtovarniki",
        "status": "broken",
        "profile_attrs": [51, 20, 22, 33, 21, 38, 26, 31, 115, 30, 24, 19],
    },
    "telezhki": {
        "category_id": 326,
        "name": "Тележки сервировочные",
        "url": BASE_URL + "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/",
        "profile": "326_telezhki",
        "status": "broken",
        "profile_attrs": [],
    },
    "moechnye_vanny": {
        "category_id": 80,
        "name": "Моечные ванны",
        "url": BASE_URL + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
        "profile": "80_moechnye_vanny",
        "status": "working",
        "profile_attrs": [29, 23, 25, 28, 47, 18, 33, 26, 21, 31, 22, 17],
    },
    "zonty": {
        "category_id": 207,
        "name": "Зонты вытяжные",
        "url": BASE_URL + "/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/",
        "profile": "207_zonty",
        "status": "working",
        "profile_attrs": [21, 34],
    },
}

# Other neutral branches to spot-check
OTHER_NEUTRAL = {
    "nejtralnoe_hub": {"category_id": 79, "name": "Нейтральное оборудование (hub)"},
}


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
    db_html = op.open(
        PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60
    ).read().decode("utf-8", "replace")
    csrf = re.search(r'name="token"\s+value="([^"]+)"', db_html).group(1)
    return op, csrf


def pma_sql(op, csrf, sql: str) -> list[dict]:
    html = op.open(
        urllib.request.Request(
            PMA + "/sql.php",
            data=urllib.parse.urlencode(
                {"db": DB, "sql_query": sql, "token": csrf, "sql_delimiter": ";"}
            ).encode(),
            method="POST",
        ),
        timeout=300,
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


def fetch_url(url: str) -> str:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-M9.8.9-06K/1.0"})
    return urllib.request.urlopen(req, timeout=120, context=ctx).read().decode("utf-8", "replace")


def count_cards(html: str) -> int:
    n = len(re.findall(r'<article class="p-card', html))
    if n:
        return n
    return len(re.findall(r'class="[^"]*product-layout[^"]*"', html))


def extract_sidebar_filters(html: str) -> list[dict]:
    """Extract filter inventory from sidebar HTML."""
    filters: list[dict] = []
    seen: set[str] = set()

    for m in re.finditer(
        r'<fieldset[^>]*class="[^"]*flt__group[^"]*"[^>]*>.*?<legend[^>]*>(.*?)</legend>.*?</fieldset>',
        html,
        re.S,
    ):
        legend = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        block = m.group(0)
        for inp in re.finditer(
            r'name="(attr\[[^\]]+\]\[\]|s\[\]|price_from|price_to|len_from|len_to|w_from|w_to|h_from|h_to|in_stock|preorder_only|only_with_price|only_discount)"[^>]*',
            block,
        ):
            name = inp.group(1)
            tag = inp.group(0)
            vm = re.search(r'value="([^"]*)"', tag)
            val = vm.group(1) if vm else ""
            if name.startswith("attr["):
                key = re.match(r"attr\[([^\]]+)\]", name).group(1)
                key_type = "numeric" if key.isdigit() else "slug"
            elif name == "s[]":
                key, key_type = "s", "subcategory"
            elif name in ("price_from", "price_to"):
                key, key_type = name, "price_range"
            else:
                key, key_type = name, "switch"

            uid = f"{key}|{name}|{val}"
            if uid in seen:
                continue
            seen.add(uid)

            attr_id = None
            if key.isdigit():
                attr_id = int(key)
            elif key_type == "slug":
                # attribute_id not in HTML — resolved later from DB
                attr_id = None

            filters.append(
                {
                    "filter_key": key,
                    "filter_name_legend": legend,
                    "attribute_id": attr_id,
                    "key_type": key_type,
                    "html_name": name,
                    "sample_value": val,
                }
            )

    for field in ("price", "len", "w", "h"):
        m = re.search(
            rf'data-range[^>]*data-range-field="{field}"',
            html,
        )
        if m:
            filters.append(
                {
                    "filter_key": f"{field}_range",
                    "filter_name_legend": field,
                    "attribute_id": None,
                    "key_type": "range",
                    "html_name": f"{field}_from/{field}_to",
                    "sample_value": None,
                }
            )
    return filters


def extract_html_names(html: str) -> dict:
    names: dict[str, list[str]] = {}
    for m in re.finditer(
        r'name="(attr\[[^\]]+\]\[\]|s\[\]|price_from|price_to|len_from|len_to|w_from|w_to|h_from|h_to|in_stock|preorder_only|only_with_price|only_discount)"',
        html,
    ):
        n = m.group(1)
        names.setdefault(n, [])
    return {k: len(v) for k, v in names.items()}


def probe_filter(base_url: str, filter_str: str) -> dict:
    qs = "filters=" + urllib.parse.quote(filter_str, safe="[];=")
    url = base_url + "?" + qs
    html = fetch_url(url)
    return {"filter": filter_str, "url": url, "cards": count_cards(html)}


def category_stats_sql(cat_id: int) -> str:
    return f"""
SELECT
  {cat_id} AS category_id,
  (SELECT COUNT(DISTINCT p.product_id)
   FROM oc_product p
   INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
   INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
   INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
   WHERE p.status = 1) AS total_products,
  (SELECT COUNT(DISTINCT p.product_id)
   FROM oc_product p
   INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
   INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
   INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
   WHERE p.status = 1
     AND EXISTS (SELECT 1 FROM oc_product_attribute pa WHERE pa.product_id = p.product_id AND pa.language_id = 1)) AS with_attributes,
  (SELECT COUNT(DISTINCT p.product_id)
   FROM oc_product p
   INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
   INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
   INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
   WHERE p.status = 1
     AND NOT EXISTS (SELECT 1 FROM oc_product_attribute pa WHERE pa.product_id = p.product_id AND pa.language_id = 1)) AS without_attributes
"""


def attr_coverage_sql(cat_id: int, attr_ids: list[int]) -> str:
    if not attr_ids:
        return ""
    ids = ",".join(str(i) for i in attr_ids)
    return f"""
SELECT
  ad.attribute_id,
  ad.name,
  ad.filter_name,
  IF(ad.filter_name IS NULL OR ad.filter_name = '', 'EMPTY', 'SET') AS filter_name_state,
  COUNT(DISTINCT pa.product_id) AS products_with_value,
  GROUP_CONCAT(DISTINCT pa.text ORDER BY pa.text SEPARATOR ' | ') AS sample_values
FROM oc_attribute_description ad
LEFT JOIN oc_product_attribute pa ON pa.attribute_id = ad.attribute_id AND pa.language_id = 1
LEFT JOIN oc_product p ON pa.product_id = p.product_id AND p.status = 1
LEFT JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
LEFT JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
WHERE ad.attribute_id IN ({ids}) AND ad.language_id = 1
GROUP BY ad.attribute_id, ad.name, ad.filter_name
ORDER BY ad.attribute_id
"""


def attribute_data_sql(cat_id: int) -> str:
    """Simulate getAttributesByCategory — attribute_data keys and values."""
    return f"""
SELECT
  IF(ad.filter_name IS NULL OR ad.filter_name = '', CAST(a.attribute_id AS CHAR), ad.filter_name) AS filter_key,
  a.attribute_id,
  ad.name AS attribute_name,
  ad.filter_name,
  pa.text AS value_text,
  COUNT(DISTINCT pa.product_id) AS product_count
FROM oc_product_attribute pa
INNER JOIN oc_attribute a ON pa.attribute_id = a.attribute_id
INNER JOIN oc_attribute_description ad ON a.attribute_id = ad.attribute_id AND ad.language_id = 1
INNER JOIN oc_product_to_category p2c ON pa.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
INNER JOIN oc_product p ON pa.product_id = p.product_id AND p.status = 1
WHERE pa.language_id = 1 AND TRIM(pa.text) != ''
GROUP BY filter_key, a.attribute_id, ad.name, ad.filter_name, pa.text
ORDER BY a.sort_order, ad.name, pa.text
"""


def sql_resolution_probe(cat_id: int, attr_key: str, value: str, is_numeric: bool) -> dict:
    esc_val = value.replace("'", "''")
    if is_numeric:
        sql = f"""
SELECT COUNT(DISTINCT p.product_id) AS cnt
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
INNER JOIN oc_product_attribute pa ON pa.product_id = p.product_id AND pa.attribute_id = {int(attr_key)} AND pa.language_id = 1
WHERE p.status = 1 AND pa.text = '{esc_val}'
"""
        sql_broken = f"""
SELECT COUNT(DISTINCT p.product_id) AS cnt
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
INNER JOIN oc_product_attribute pa ON pa.product_id = p.product_id AND pa.language_id = 1
INNER JOIN oc_attribute_description ad ON pa.attribute_id = ad.attribute_id AND ad.language_id = 1
WHERE p.status = 1 AND ad.filter_name = '{attr_key}' AND pa.text = '{esc_val}'
"""
    else:
        sql = f"""
SELECT COUNT(DISTINCT p.product_id) AS cnt
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
INNER JOIN oc_product_attribute pa ON pa.product_id = p.product_id AND pa.language_id = 1
INNER JOIN oc_attribute_description ad ON pa.attribute_id = ad.attribute_id AND ad.language_id = 1
WHERE p.status = 1 AND ad.filter_name = '{esc_val}' AND pa.text = '{esc_val}'
""".replace(f"ad.filter_name = '{esc_val}'", f"ad.filter_name = '{attr_key}'")
        sql_broken = None

    return {"correct_sql": sql.strip(), "broken_sql_if_slug_mismatch": sql_broken}


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results = {
        "task": "M9.8.9-06K",
        "authority": "SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01",
        "context": "post clean catalog reset + import0_1.xml + offers0_1.xml",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "global": {},
        "categories": {},
    }

    op, csrf = pma_session()

    # Global post-import counts
    for label, sql in [
        ("product_totals", "SELECT COUNT(*) AS total_products, SUM(status=1) AS active FROM oc_product"),
        ("product_attribute_rows", "SELECT COUNT(*) AS rows, COUNT(DISTINCT product_id) AS products FROM oc_product_attribute"),
        ("price_index", """
SELECT COUNT(DISTINCT ppi.product_id) AS indexed,
  (SELECT COUNT(*) FROM oc_product WHERE status=1) AS active_products
FROM oc_product_price_index ppi
INNER JOIN oc_product p ON ppi.product_id = p.product_id AND p.status = 1
WHERE ppi.customer_group_id = 2
"""),
    ]:
        results["global"][label] = pma_sql(op, csrf, sql)

    # filter_name state for all profile attrs
    all_attrs = sorted({a for c in CATEGORIES.values() for a in c["profile_attrs"]})
    if all_attrs:
        ids = ",".join(str(i) for i in all_attrs)
        results["global"]["attribute_descriptions"] = pma_sql(
            op,
            csrf,
            f"""SELECT attribute_id, name, filter_name,
              IF(filter_name IS NULL OR filter_name='', 'EMPTY', filter_name) AS effective_key
              FROM oc_attribute_description WHERE attribute_id IN ({ids}) AND language_id=1
              ORDER BY attribute_id""",
        )

    for key, meta in CATEGORIES.items():
        print(f"Probing {key}...")
        cat_id = meta["category_id"]
        cat_out = {
            "category_id": cat_id,
            "name": meta["name"],
            "url": meta["url"],
            "profile": meta["profile"],
            "operator_status": meta["status"],
        }

        cat_out["category_statistics"] = pma_sql(op, csrf, category_stats_sql(cat_id))
        if meta["profile_attrs"]:
            cat_out["attribute_coverage"] = pma_sql(
                op, csrf, attr_coverage_sql(cat_id, meta["profile_attrs"])
            )
        cat_out["attribute_data_db"] = pma_sql(op, csrf, attribute_data_sql(cat_id))

        # Price index in category
        cat_out["price_index_coverage"] = pma_sql(
            op,
            csrf,
            f"""
SELECT
  COUNT(DISTINCT p.product_id) AS total_active,
  COUNT(DISTINCT ppi.product_id) AS indexed_cg2,
  SUM(CASE WHEN ppi.price > 0 OR ppi.special > 0 THEN 1 ELSE 0 END) AS with_positive_price
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
LEFT JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
WHERE p.status = 1
""",
        )

        html = fetch_url(meta["url"])
        cat_out["baseline_cards"] = count_cards(html)
        cat_out["sidebar_filters"] = extract_sidebar_filters(html)
        cat_out["html_form_names"] = extract_html_names(html)

        # Enrich sidebar with attribute_id from DB for slug keys
        slug_keys = [f["filter_key"] for f in cat_out["sidebar_filters"] if f["key_type"] == "slug"]
        if slug_keys:
            slugs = ",".join("'" + s.replace("'", "''") + "'" for s in slug_keys)
            slug_map = pma_sql(
                op,
                csrf,
                f"SELECT filter_name, attribute_id, name FROM oc_attribute_description WHERE filter_name IN ({slugs}) AND language_id=1",
            )
            slug_lookup = {r.get("filter_name", ""): r for r in slug_map}
            for f in cat_out["sidebar_filters"]:
                if f["key_type"] == "slug" and f["filter_key"] in slug_lookup:
                    f["attribute_id"] = int(slug_lookup[f["filter_key"]].get("attribute_id", 0))
                    f["db_attribute_name"] = slug_lookup[f["filter_key"]].get("name", "")

        # Orphan filter values: shown in HTML but 0 products match
        orphans = []
        for m in re.finditer(r'name="attr\[([^\]]+)\]\[\]"[^>]*value="([^"]+)"', html):
            g, v = m.group(1), m.group(2)
            is_num = g.isdigit()
            if is_num:
                cnt_sql = f"""
SELECT COUNT(DISTINCT pa.product_id) AS cnt FROM oc_product_attribute pa
INNER JOIN oc_product p ON pa.product_id=p.product_id AND p.status=1
INNER JOIN oc_product_to_category p2c ON p.product_id=p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id=cp.category_id AND cp.path_id={cat_id}
WHERE pa.attribute_id={int(g)} AND pa.text='{v.replace("'","''")}' AND pa.language_id=1
"""
            else:
                cnt_sql = f"""
SELECT COUNT(DISTINCT pa.product_id) AS cnt FROM oc_product_attribute pa
INNER JOIN oc_attribute_description ad ON pa.attribute_id=ad.attribute_id AND ad.language_id=1
INNER JOIN oc_product p ON pa.product_id=p.product_id AND p.status=1
INNER JOIN oc_product_to_category p2c ON p.product_id=p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id=cp.category_id AND cp.path_id={cat_id}
WHERE ad.filter_name='{g.replace("'","''")}' AND pa.text='{v.replace("'","''")}' AND pa.language_id=1
"""
            cnt = pma_sql(op, csrf, cnt_sql)
            c = int(cnt[0].get("cnt", 0)) if cnt else -1
            if c == 0:
                orphans.append({"filter_key": g, "value": v, "key_type": "numeric" if is_num else "slug", "db_match_count": c})

        cat_out["orphan_filter_values"] = orphans

        # Live probes
        probes = [{"filter": "(baseline)", "cards": cat_out["baseline_cards"]}]
        for sw in ("in_stock=1", "preorder_only=1", "only_with_price=1", "only_discount=1"):
            probes.append(probe_filter(meta["url"], sw))

        attr_groups: dict[str, list[str]] = {}
        for m in re.finditer(r'name="attr\[([^\]]+)\]\[\]"[^>]*value="([^"]+)"', html):
            g, v = m.group(1), m.group(2)
            attr_groups.setdefault(g, []).append(v)

        sql_probes = []
        for g, vals in attr_groups.items():
            v = vals[0]
            fs = f"attr[{g}][]={v}"
            pr = probe_filter(meta["url"], fs)
            probes.append(pr)
            is_num = g.isdigit()
            cnt_correct = pma_sql(
                op,
                csrf,
                f"""
SELECT COUNT(DISTINCT p.product_id) AS cnt
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id=p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id=cp.category_id AND cp.path_id={cat_id}
INNER JOIN oc_product_attribute pa ON pa.product_id=p.product_id AND pa.language_id=1
{"INNER JOIN oc_attribute_description ad ON pa.attribute_id=ad.attribute_id AND ad.language_id=1" if not is_num else ""}
WHERE p.status=1
  AND {"pa.attribute_id="+g if is_num else "ad.filter_name='"+g.replace("'","''")+"'"}
  AND pa.text='{v.replace("'","''")}'
""",
            )
            cnt_broken = None
            if is_num:
                cnt_broken = pma_sql(
                    op,
                    csrf,
                    f"""
SELECT COUNT(DISTINCT p.product_id) AS cnt
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id=p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id=cp.category_id AND cp.path_id={cat_id}
INNER JOIN oc_product_attribute pa ON pa.product_id=p.product_id AND pa.language_id=1
INNER JOIN oc_attribute_description ad ON pa.attribute_id=ad.attribute_id AND ad.language_id=1
WHERE p.status=1 AND ad.filter_name='{g}' AND pa.text='{v.replace("'","''")}'
""",
                )
            sql_probes.append(
                {
                    "filter_key": g,
                    "sample_value": v,
                    "key_type": "numeric" if is_num else "slug",
                    "db_count_correct_resolution": cnt_correct[0] if cnt_correct else None,
                    "db_count_broken_filter_name_resolution": cnt_broken[0] if cnt_broken else None,
                    "live_cards_after_filter": pr["cards"],
                    "constructed_sql_correct": (
                        f"EXISTS (... attribute_id={g} AND pa.text='{v}')" if is_num
                        else f"EXISTS (... ad.filter_name='{g}' AND pa.text='{v}')"
                    ),
                    "constructed_sql_broken_pre06j": (
                        f"EXISTS (... ad.filter_name='{g}' AND pa.text='{v}')" if is_num else None
                    ),
                }
            )

        cat_out["live_probes"] = probes
        cat_out["sql_probes"] = sql_probes

        # Price range probe
        pf = re.search(r'name="price_from"[^>]*(?:value|placeholder)="(\d+)"', html)
        pt = re.search(r'name="price_to"[^>]*(?:value|placeholder)="(\d+)"', html)
        if pf and pt:
            pfrom, pto = pf.group(1), pt.group(1)
            cat_out["price_range_html"] = {"from": int(pfrom), "to": int(pto)}
            pr = probe_filter(meta["url"], f"price_from={pfrom};price_to={pto}")
            cat_out["live_probes"].append(pr)

        results["categories"][key] = cat_out

    # 06J deployment signal: attr[51] on stoly should return >0 if patch live
    stoly_51 = next(
        (p for p in results["categories"]["stoly"]["live_probes"] if "attr[51]" in p.get("filter", "")),
        None,
    )
    results["global"]["patch_06j_signal"] = {
        "test": "stoly attr[51][] first value",
        "probe": stoly_51,
        "interpretation": (
            "06J likely LIVE" if stoly_51 and stoly_51.get("cards", 0) > 0
            else "06J likely NOT live OR no attribute data"
        ),
    }

    OUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")


if __name__ == "__main__":
    main()
