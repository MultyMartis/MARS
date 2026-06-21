#!/usr/bin/env python3
"""Final dry-run supplement — READ ONLY."""
import json, re, ssl, urllib.parse, urllib.request, http.cookiejar
from html import unescape
from pathlib import Path

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"
OUT = Path(__file__).resolve().parent / "probe-final.json"


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
    return op, re.search(r'name="token"\s+value="([^"]+)"', db_html).group(1)


def pma_sql(op, csrf, sql):
    html = op.open(
        urllib.request.Request(
            PMA + "/sql.php",
            data=urllib.parse.urlencode(
                {"db": DB, "sql_query": sql, "token": csrf, "sql_delimiter": ";"}
            ).encode(),
            method="POST",
        ),
        timeout=120,
    ).read().decode("utf-8", "replace")
    for tbl in re.findall(
        r'<table[^>]*class="[^"]*table[^"]*"[^>]*>(.*?)</table>', html, re.S
    ):
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
            h = [x.lower() for x in parsed[0]]
            return [dict(zip(h, r)) for r in parsed[1:] if len(r) == len(h)]
    return []


def scalar(op, csrf, sql):
    r = pma_sql(op, csrf, sql)
    if not r:
        return "ERROR"
    row = r[0]
    return next(iter(row.values()))


op, csrf = pma_session()
queries = {
    "googleshopping_product_target": "SELECT COUNT(*) AS c FROM oc_googleshopping_product_target",
    "distinct_main_images": "SELECT COUNT(DISTINCT image) AS c FROM oc_product WHERE image IS NOT NULL AND image <> ''",
    "distinct_gallery_images": "SELECT COUNT(DISTINCT image) AS c FROM oc_product_image",
    "union_distinct_product_image_paths": (
        "SELECT COUNT(*) AS c FROM ("
        "SELECT image FROM oc_product WHERE image <> '' "
        "UNION SELECT image FROM oc_product_image"
        ") t"
    ),
    "oc_category": "SELECT COUNT(*) AS c FROM oc_category",
    "oc_category_description": "SELECT COUNT(*) AS c FROM oc_category_description",
    "oc_category_path": "SELECT COUNT(*) AS c FROM oc_category_path",
    "oc_category_filter": "SELECT COUNT(*) AS c FROM oc_category_filter",
    "oc_category_docs": "SELECT COUNT(*) AS c FROM oc_category_docs",
    "oc_category_doc_description": "SELECT COUNT(*) AS c FROM oc_category_doc_description",
    "oc_attribute": "SELECT COUNT(*) AS c FROM oc_attribute",
    "oc_attribute_description": "SELECT COUNT(*) AS c FROM oc_attribute_description",
    "oc_attribute_group": "SELECT COUNT(*) AS c FROM oc_attribute_group",
    "oc_attribute_group_description": "SELECT COUNT(*) AS c FROM oc_attribute_group_description",
    "oc_filter": "SELECT COUNT(*) AS c FROM oc_filter",
    "oc_filter_description": "SELECT COUNT(*) AS c FROM oc_filter_description",
    "oc_filter_group": "SELECT COUNT(*) AS c FROM oc_filter_group",
    "oc_filter_group_description": "SELECT COUNT(*) AS c FROM oc_filter_group_description",
    "oc_setting": "SELECT COUNT(*) AS c FROM oc_setting",
    "oc_theme": "SELECT COUNT(*) AS c FROM oc_theme",
    "oc_order": "SELECT COUNT(*) AS c FROM oc_order",
    "cron_count": "SELECT COUNT(*) AS c FROM cron",
    "seo_non_product": "SELECT COUNT(*) AS c FROM oc_seo_url WHERE query NOT LIKE 'product_id=%'",
    "products_zero_attributes": (
        "SELECT COUNT(*) AS c FROM oc_product p "
        "LEFT JOIN oc_product_attribute pa ON p.product_id = pa.product_id "
        "WHERE pa.product_id IS NULL"
    ),
}
out = {k: scalar(op, csrf, sql) for k, sql in queries.items()}
out["cron_rows"] = pma_sql(op, csrf, "SELECT id, name, command, active, duration, lastrun FROM cron ORDER BY id")
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(out, ensure_ascii=False, indent=2))
