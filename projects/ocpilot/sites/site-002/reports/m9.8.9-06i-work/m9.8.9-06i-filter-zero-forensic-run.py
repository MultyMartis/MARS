#!/usr/bin/env python3
"""M9.8.9-06I — filter zero-results forensic (read-only)."""
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

OUT_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-06i-work")
OUT_JSON = OUT_DIR / "forensic-results.json"

CATEGORIES = {
    "stoly": {
        "category_id": 301,
        "url": BASE_URL + "/katalog/nejtralnoe-oborudovanie/stoly/",
        "profile": "301_stoly",
    },
    "podtovarniki": {
        "category_id": 322,
        "url": BASE_URL + "/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/",
        "profile": "322_podtovarniki",
    },
    "moechnye_vanny": {
        "category_id": 80,
        "url": BASE_URL + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
        "profile": "80_moechnye_vanny",
    },
    "zonty": {
        "category_id": 207,
        "url": BASE_URL + "/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/",
        "profile": "207_zonty",
    },
    "telezhki": {
        "category_id": 326,
        "url": BASE_URL + "/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/",
        "profile": "326_telezhki",
    },
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
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-M9.8.9-06I/1.0"})
    return urllib.request.urlopen(req, timeout=120, context=ctx).read().decode("utf-8", "replace")


def count_cards(html: str) -> int:
    n = len(re.findall(r'<article class="p-card', html))
    if n:
        return n
    return len(re.findall(r'class="[^"]*product-layout[^"]*"', html))


def extract_filter_groups(html: str) -> list[dict]:
    groups: dict[str, dict] = {}
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
            key = name
            if name.startswith("attr["):
                key = re.match(r"attr\[([^\]]+)\]", name).group(1)
            groups.setdefault(
                key,
                {
                    "legend": legend,
                    "param_type": "numeric_attr_id" if key.isdigit() else ("slug" if name.startswith("attr[") else name),
                    "html_name": name,
                    "sample_values": [],
                },
            )
            if val and val not in groups[key]["sample_values"]:
                groups[key]["sample_values"].append(val)

    # price / dim ranges from data-range blocks
    for field in ("price", "len", "w", "h"):
        m = re.search(
            rf'data-range[^>]*data-range-field="{field}"[^>]*>.*?data-range-min[^>]*min="(\d+)"[^>]*max="(\d+)"',
            html,
            re.S,
        )
        if m:
            groups[field + "_range"] = {
                "legend": field,
                "param_type": "range",
                "html_name": f"{field}_from/{field}_to",
                "min": int(m.group(1)),
                "max": int(m.group(2)),
            }
    return list(groups.values())


def probe_filter(base_url: str, filter_str: str) -> dict:
    qs = "filters=" + urllib.parse.quote(filter_str, safe="[];=")
    url = base_url + "?" + qs
    html = fetch_url(url)
    return {
        "filter": filter_str,
        "url": url,
        "cards": count_cards(html),
    }


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results = {
        "task": "M9.8.9-06I",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "categories": {},
        "db_attributes": {},
    }

    op, csrf = pma_session()

    # DB: filter_name for attrs 47, 51 and product counts
    attr_sql = """
SELECT ad.attribute_id, ad.name, ad.filter_name,
  (SELECT COUNT(DISTINCT pa.product_id) FROM oc_product_attribute pa
   INNER JOIN oc_product p ON pa.product_id = p.product_id AND p.status = 1
   WHERE pa.attribute_id = ad.attribute_id) AS product_count,
  (SELECT COUNT(DISTINCT pa.product_id) FROM oc_product_attribute pa
   INNER JOIN oc_product p ON pa.product_id = p.product_id AND p.status = 1
   INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
   INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = 301
   WHERE pa.attribute_id = ad.attribute_id) AS count_cat_301,
  (SELECT COUNT(DISTINCT pa.product_id) FROM oc_product_attribute pa
   INNER JOIN oc_product p ON pa.product_id = p.product_id AND p.status = 1
   INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
   INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = 322
   WHERE pa.attribute_id = ad.attribute_id) AS count_cat_322
FROM oc_attribute_description ad
WHERE ad.attribute_id IN (47, 51, 22, 33, 20, 25, 21, 29, 23, 28)
  AND ad.language_id = 1
"""
    results["db_attributes"]["key_attrs"] = pma_sql(op, csrf, attr_sql)

    # Simulate SQL mismatch: filter_name='51' vs attribute_id=51
    for cat_id, label in [(301, "stoly"), (322, "podtovarniki")]:
        for aid in (47, 51):
            sql_slug = f"""
SELECT COUNT(DISTINCT pa.product_id) AS cnt
FROM oc_product_attribute pa
INNER JOIN oc_attribute_description ad ON pa.attribute_id = ad.attribute_id AND ad.language_id = 1
INNER JOIN oc_product p ON pa.product_id = p.product_id AND p.status = 1
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
WHERE ad.filter_name = '{aid}'
"""
            sql_id = f"""
SELECT COUNT(DISTINCT pa.product_id) AS cnt
FROM oc_product_attribute pa
INNER JOIN oc_product p ON pa.product_id = p.product_id AND p.status = 1
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
WHERE pa.attribute_id = {aid}
"""
            results["db_attributes"].setdefault("sql_resolution_probe", {})[
                f"{label}_attr_{aid}_by_filter_name"
            ] = pma_sql(op, csrf, sql_slug)
            results["db_attributes"].setdefault("sql_resolution_probe", {})[
                f"{label}_attr_{aid}_by_attribute_id"
            ] = pma_sql(op, csrf, sql_id)

    for key, meta in CATEGORIES.items():
        print(f"Probing {key}...")
        html = fetch_url(meta["url"])
        baseline = count_cards(html)
        groups = extract_filter_groups(html)
        cat_out = {
            "category_id": meta["category_id"],
            "url": meta["url"],
            "profile": meta["profile"],
            "baseline_cards": baseline,
            "html_filter_groups": groups,
            "probes": [],
        }

        # baseline
        cat_out["probes"].append({"filter": "(baseline)", "cards": baseline})

        # switches
        for sw in ("in_stock=1", "preorder_only=1", "only_with_price=1", "only_discount=1"):
            cat_out["probes"].append(probe_filter(meta["url"], sw))

        # first checkbox per attr group
        attr_groups: dict[str, list[str]] = {}
        for m in re.finditer(r'name="attr\[([^\]]+)\]\[\]"[^>]*value="([^"]+)"', html):
            g, v = m.group(1), m.group(2)
            attr_groups.setdefault(g, []).append(v)

        for g, vals in attr_groups.items():
            v = vals[0]
            fs = f"attr[{g}][]={v}"
            cat_out["probes"].append(probe_filter(meta["url"], fs))

        # attr 51 specific if present
        if "51" in attr_groups:
            for v in attr_groups["51"][:3]:
                cat_out["probes"].append(probe_filter(meta["url"], f"attr[51][]={v}"))

        # subcategory first
        sid = re.search(r'name="s\[\]"[^>]*value="(\d+)"', html)
        if sid:
            cat_out["probes"].append(probe_filter(meta["url"], f"s[]={sid.group(1)}"))

        # price range: min only, max only, full range
        pf = re.search(r'name="price_from"[^>]*(?:value|placeholder)="(\d+)"', html)
        pt = re.search(r'name="price_to"[^>]*(?:value|placeholder)="(\d+)"', html)
        if pf and pt:
            pfrom, pto = pf.group(1), pt.group(1)
            cat_out["price_range_html"] = {"from": int(pfrom), "to": int(pto)}
            cat_out["probes"].append(probe_filter(meta["url"], f"price_from={pfrom};price_to={pto}"))
            mid = str((int(pfrom) + int(pto)) // 2)
            cat_out["probes"].append(probe_filter(meta["url"], f"price_from={pfrom};price_to={mid}"))

        results["categories"][key] = cat_out

    OUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")


if __name__ == "__main__":
    main()
