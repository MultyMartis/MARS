#!/usr/bin/env python3
import json, re, ssl, urllib.parse, urllib.request, http.cookiejar
from html import unescape
from pathlib import Path

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"
OUT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-06c-audit-data\supplement.json")


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


def pma_sql(op, csrf, sql):
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
        return {"rows": [], "error_hint": "parse_failed", "html_len": len(html)}
    h = [x.lower() for x in rows[0]]
    return {"rows": [dict(zip(h, r)) for r in rows[1:] if len(r) == len(h)], "count": len(rows) - 1}


def main():
    op, csrf = pma_session()
    queries = {
        "cron_describe_full": "SHOW COLUMNS FROM oc_cron",
        "cron_all": "SELECT * FROM oc_cron ORDER BY id",
        "cron_active": "SELECT * FROM oc_cron WHERE active = 1",
        "cron_1c": """
            SELECT * FROM oc_cron
            WHERE command IN ('1c','1c_offers')
               OR LOWER(name) LIKE '%import%'
               OR LOWER(name) LIKE '%offer%'
               OR LOWER(name) LIKE '%1c%'
            ORDER BY id
        """,
        "variant_c_count": """
            SELECT COUNT(DISTINCT p.product_id) AS cnt
            FROM oc_product p
            INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
            INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = 301
            WHERE p.status = 1 AND p.date_available <= NOW()
        """,
        "variant_c_sample": """
            SELECT p.product_id, p.model, p.sku, pd.name, p.price,
                   CASE WHEN ppi.product_id IS NULL THEN 'no' ELSE 'yes' END AS has_index,
                   ppi.price AS index_price
            FROM oc_product p
            INNER JOIN oc_product_description pd ON p.product_id = pd.product_id AND pd.language_id = 1
            INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
            INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = 301
            INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
            LEFT JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
            WHERE p.status = 1 AND p.date_available <= NOW()
            ORDER BY has_index ASC, p.product_id
            LIMIT 30
        """,
        "variant_c_indexed_only": """
            SELECT p.product_id, p.model, pd.name, p.price, ppi.price AS index_price, ppi.special
            FROM oc_product p
            INNER JOIN oc_product_description pd ON p.product_id = pd.product_id AND pd.language_id = 1
            INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
            INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = 301
            INNER JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
            WHERE p.status = 1
        """,
        "missing_index_301_count": """
            SELECT COUNT(DISTINCT p.product_id) AS missing_count
            FROM oc_product p
            INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
            INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = 301
            INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
            LEFT JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
            WHERE p.status = 1 AND p.date_available <= NOW() AND ppi.product_id IS NULL
        """,
    }
    res = {}
    for k, q in queries.items():
        res[k] = pma_sql(op, csrf, q)
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v.get("count", len(v.get("rows", []))) for k, v in res.items()}, indent=2))


if __name__ == "__main__":
    main()
