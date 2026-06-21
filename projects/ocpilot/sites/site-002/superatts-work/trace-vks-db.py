#!/usr/bin/env python3
"""DB attribute table for VKS-P-1/400/900 product."""
import io
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
SUPER_ATTS_IDS = [12, 13, 14, 15, 21, 25, 26, 28, 29, 30, 33, 115]
VKS_KW = "katalog/nejtralnoe-oborudovanie/moechnye-vanny/kotlomoyki-premium/vanna-kotlomoechnaya-vks-p-1-400-900-1000h500h850"


def pma_login():
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
                    "pma_username": DU,
                    "pma_password": DP,
                    "server": "1",
                    "target": "index.php",
                    "token": token,
                }
            ).encode(),
            method="POST",
        ),
        timeout=60,
    )
    db_page = op.open(
        PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60
    ).read().decode("utf-8", "replace")
    csrf = re.search(r'name="token"\s+value="([^"]+)"', db_page)
    return op, csrf.group(1) if csrf else token


def pma_sql(op, csrf, query):
    qdata = urllib.parse.urlencode(
        {"db": DB, "sql_query": query, "token": csrf, "sql_delimiter": ";"}
    ).encode()
    html = op.open(
        urllib.request.Request(PMA + "/sql.php", data=qdata, method="POST"),
        timeout=180,
    ).read().decode("utf-8", "replace")
    if "error" in html.lower() and "MySQL" in html:
        return []
    for tbl in re.findall(r"<table[^>]*>(.*?)</table>", html, re.S | re.I):
        trs = re.findall(r"<tr[^>]*>(.*?)</tr>", tbl, re.S | re.I)
        if len(trs) < 2:
            continue
        parsed = []
        for tr in trs:
            cells = [
                unescape(re.sub(r"<[^>]+>", " ", c).strip())
                for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S | re.I)
            ]
            cells = [re.sub(r"\s+", " ", c) for c in cells if c.strip()]
            if cells:
                parsed.append(cells)
        if len(parsed) >= 2 and len(parsed[0]) >= 2:
            hdr = parsed[0]
            if hdr[0].lower() in ("attribute_id", "product_id", "query"):
                return [dict(zip(hdr, r)) for r in parsed[1:] if len(r) == len(hdr)]
    return []


def main():
    op, csrf = pma_login()
    seo = pma_sql(
        op,
        csrf,
        f"SELECT query, keyword FROM oc_seo_url WHERE keyword='{VKS_KW}' LIMIT 1",
    )
    print("SEO:", seo)
    pid = None
    if seo:
        m = re.search(r"product_id=(\d+)", seo[0].get("query", ""))
        pid = m.group(1) if m else None
    if not pid:
        prods = pma_sql(
            op,
            csrf,
            "SELECT p.product_id, pd.name FROM oc_product p JOIN oc_product_description pd ON pd.product_id=p.product_id AND pd.language_id=1 WHERE pd.name LIKE '%VKS-P-1/400/900%' LIMIT 3",
        )
        print("PRODS:", prods)
        if prods:
            pid = prods[0].get("product_id")
    print("PID:", pid)
    if not pid:
        return
    ids_csv = ",".join(str(i) for i in SUPER_ATTS_IDS)
    rows = pma_sql(
        op,
        csrf,
        f"""
SELECT a.attribute_id, ad.name AS attribute_name, pa.text AS product_value
FROM oc_attribute a
JOIN oc_attribute_description ad ON ad.attribute_id=a.attribute_id AND ad.language_id=1
LEFT JOIN oc_product_attribute pa ON pa.attribute_id=a.attribute_id
  AND pa.product_id={pid} AND pa.language_id=1
WHERE a.attribute_id IN ({ids_csv})
ORDER BY FIELD(a.attribute_id, {ids_csv})
""",
    )
    print("\nID | name | value | exists | should_in_super_atts")
    for r in rows:
        aid = r.get("attribute_id")
        name = r.get("attribute_name", "")
        val = (r.get("product_value") or "").strip()
        exists = bool(val)
        should = exists and int(aid) in SUPER_ATTS_IDS
        print(f"{aid} | {name} | {val} | {exists} | {should}")


if __name__ == "__main__":
    main()
