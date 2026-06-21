#!/usr/bin/env python3
import json, re, ssl, urllib.parse, urllib.request, http.cookiejar
from html import unescape
from pathlib import Path

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"

def pma_session():
    ctx = ssl.create_default_context()
    cj = http.cookiejar.CookieJar()
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj), urllib.request.HTTPSHandler(context=ctx))
    lp = op.open(PMA + "/", timeout=60).read().decode("utf-8", "replace")
    token = re.search(r'name="token"\s+value="([^"]+)"', lp).group(1)
    op.open(urllib.request.Request(PMA + "/index.php", data=urllib.parse.urlencode({"pma_username": DB_USER, "pma_password": DB_PASS, "server": "1", "target": "index.php", "token": token}).encode(), method="POST"), timeout=60)
    db_html = op.open(PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60).read().decode("utf-8", "replace")
    return op, re.search(r'name="token"\s+value="([^"]+)"', db_html).group(1)

def pma_sql(op, csrf, sql):
    html = op.open(urllib.request.Request(PMA + "/sql.php", data=urllib.parse.urlencode({"db": DB, "sql_query": sql, "token": csrf, "sql_delimiter": ";"}).encode(), method="POST"), timeout=120).read().decode("utf-8", "replace")
    for tbl in re.findall(r'<table[^>]*class="[^"]*table[^"]*"[^>]*>(.*?)</table>', html, re.S):
        if "Browse" in tbl and "Drop" in tbl:
            continue
        parsed = []
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", tbl, re.S):
            cells = [unescape(re.sub(r"<[^>]+>", " ", c).strip()) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]
            cells = [re.sub(r"\s+", " ", c) for c in cells if c.strip()]
            if cells:
                parsed.append(cells)
        if len(parsed) >= 2 and not parsed[0][0].startswith("Table navigation"):
            h = [x.lower() for x in parsed[0]]
            return [dict(zip(h, r)) for r in parsed[1:] if len(r) == len(h)]
    return []

op, csrf = pma_session()
queries = {
    "oc_cart": "SELECT COUNT(*) AS c FROM oc_cart",
    "oc_googleshopping_product": "SELECT COUNT(*) AS c FROM oc_googleshopping_product",
    "oc_googleshopping_product_status": "SELECT COUNT(*) AS c FROM oc_googleshopping_product_status",
    "oc_customer_search": "SELECT COUNT(*) AS c FROM oc_customer_search",
    "oc_backup_move_polka_to_83": "SELECT COUNT(*) AS c FROM oc_backup_move_polka_to_83",
    "cron": "SELECT id, name, command, active, duration, lastrun FROM cron ORDER BY id",
    "order_option": "SELECT COUNT(*) AS c FROM oc_order_option",
}
out = {k: pma_sql(op, csrf, q) for k, q in queries.items()}
Path(__file__).resolve().parent.joinpath("probe-ancillary.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(out, ensure_ascii=False, indent=2))
