#!/usr/bin/env python3
"""Parse cron table - table name is `cron` without oc_ prefix."""
import json, re, ssl, urllib.parse, urllib.request, http.cookiejar
from html import unescape
from pathlib import Path

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"
OUT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-06c-audit-data\cron-and-variant.json")


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


def pma_sql_all_tables(html):
    """Parse ALL result tables from PMA response."""
    all_results = []
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
            h = [x.lower() for x in parsed[0]]
            rows = [dict(zip(h, r)) for r in parsed[1:] if len(r) == len(h)]
            if rows:
                all_results.append({"headers": h, "rows": rows, "count": len(rows)})
    return all_results


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
    tables = pma_sql_all_tables(html)
    return {"tables": tables, "html_len": len(html), "sql": sql.strip()}


def main():
    op, csrf = pma_session()
    queries = {
        "cron_columns": "SHOW COLUMNS FROM cron",
        "cron_rows": "SELECT id, name, command, active, duration, lastrun FROM cron ORDER BY id",
        "cron_active": "SELECT id, name, command, active, duration, lastrun FROM cron WHERE active = 1",
        "variant_c_full_export": """
            SELECT p.product_id, p.model, p.sku, pd.name, p.price,
                   IF(ppi.product_id IS NULL, 'no', 'yes') AS has_price_index_group_2
            FROM oc_product p
            INNER JOIN oc_product_description pd ON p.product_id = pd.product_id AND pd.language_id = 1
            INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
            INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = 301
            INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
            LEFT JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
            WHERE p.status = 1 AND p.date_available <= NOW()
            ORDER BY p.product_id
        """,
    }
    res = {}
    for k, q in queries.items():
        res[k] = pma_sql(op, csrf, q)
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    for k, v in res.items():
        counts = [t["count"] for t in v["tables"]]
        print(k, counts)


if __name__ == "__main__":
    main()
