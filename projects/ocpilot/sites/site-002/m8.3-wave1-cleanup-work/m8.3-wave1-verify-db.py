#!/usr/bin/env python3
"""Quick post-cleanup DB verify."""
import json
import re
import ssl
import urllib.parse
import urllib.request
import http.cookiejar
from html import unescape

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DU = "polygonws_zpm"
DP = "VBCDry2bJ5P"


def session():
    ctx = ssl.create_default_context()
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cj),
        urllib.request.HTTPSHandler(context=ctx),
    )
    lp = op.open(PMA + "/", timeout=60).read().decode("utf-8", "replace")
    t = re.search(r'name="token"\s+value="([^"]+)"', lp).group(1)
    op.open(
        urllib.request.Request(
            PMA + "/index.php",
            data=urllib.parse.urlencode(
                {
                    "pma_username": DU,
                    "pma_password": DP,
                    "server": "1",
                    "target": "index.php",
                    "token": t,
                }
            ).encode(),
            method="POST",
        ),
        timeout=60,
    )
    return op


def run(op, sql):
    db = op.open(PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60).read().decode(
        "utf-8", "replace"
    )
    csrf = re.search(r'name="token"\s+value="([^"]+)"', db).group(1)
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


def main():
    op = session()
    queries = {
        "test_attrs_remaining": "SELECT COUNT(*) AS cnt FROM oc_attribute WHERE attribute_id IN (16,105,106,107,108,109,111)",
        "test_filter_names": "SELECT attribute_id, filter_name FROM oc_attribute WHERE filter_name LIKE '%test%'",
        "test_pa_rows": """
            SELECT pa.product_id, pa.attribute_id, pa.text, ad.name
            FROM oc_product_attribute pa
            LEFT JOIN oc_attribute_description ad ON ad.attribute_id = pa.attribute_id AND ad.language_id = 1
            WHERE ad.name LIKE '%ТЕСТ%' OR pa.text IN ('0,6','0,85')
        """,
        "active_products_with_test_name": """
            SELECT product_id, status FROM oc_product p
            JOIN oc_product_description pd ON pd.product_id = p.product_id AND pd.language_id = 1
            WHERE pd.name LIKE '%ТЕСТ%' AND p.status = 1
        """,
    }
    out = {k: run(op, v) for k, v in queries.items()}
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
