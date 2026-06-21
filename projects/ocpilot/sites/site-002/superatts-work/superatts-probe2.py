#!/usr/bin/env python3
"""Focused bath PDP + attribute ID probe."""
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
IDS = [12, 13, 14, 15, 21, 25, 26, 28, 29, 30, 33, 115]
TABLE = (
    "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/"
    "stoly-serii-premium/stoly-premium-600/"
    "stol-proizvodstvennyy-sp-p-18-6-1800h600h850"
)


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
    return op, token


def pma_sql(op, token, query):
    qdata = urllib.parse.urlencode(
        {"db": DB, "sql_query": query, "token": token, "sql_delimiter": ";"}
    ).encode()
    return op.open(
        urllib.request.Request(PMA + "/sql.php", data=qdata, method="POST"), timeout=180
    ).read().decode("utf-8", "replace")


def parse_rows(html):
    for tbl in re.findall(r'<table class="table table-striped table-hover[^"]*">(.*?)</table>', html, re.S):
        rows = []
        for tr in re.findall(r"<tr>(.*?)</tr>", tbl, re.S):
            cells = [
                unescape(re.sub(r"<[^>]+>", "", c).strip())
                for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)
            ]
            if cells:
                rows.append(cells)
        if len(rows) >= 2 and len(rows[0]) >= 2:
            hdr = [h.lower() for h in rows[0]]
            data = [dict(zip(hdr, r)) for r in rows[1:] if len(r) == len(hdr)]
            if data:
                return rows[0], data
    return [], []


def hero_atts(html):
    block = re.search(r'<dl class="product-hero__props">(.*?)</dl>', html, re.S)
    if not block:
        return []
    out = []
    for m in re.finditer(
        r'<div class="product-hero__prop">\s*<dt>(.*?)</dt>\s*<dd>(.*?)</dd>', block.group(1), re.S
    ):
        out.append(
            {
                "name": unescape(re.sub(r"\s+", " ", m.group(1).strip())),
                "value": unescape(re.sub(r"\s+", " ", m.group(2).strip())),
            }
        )
    return out


def spec_names(html):
    names = {}
    tab = re.search(r'id="tab-spec"[^>]*>(.*?)</div>\s*</div>\s*</div>\s*</section>', html, re.S)
    scope = tab.group(1) if tab else html
    for m in re.finditer(r"<dt[^>]*>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>", scope, re.S):
        n = unescape(re.sub(r"<[^>]+>", "", m.group(1)).strip())
        v = unescape(re.sub(r"<[^>]+>", "", m.group(2)).strip())
        if n:
            names[n.lower()] = v
    return names


def main():
    op, token = pma_login()
    ids_csv = ",".join(str(i) for i in IDS)

    _, prods = parse_rows(
        pma_sql(
            op,
            token,
            """
SELECT p.product_id, pd.name
FROM oc_product p
JOIN oc_product_description pd ON pd.product_id=p.product_id AND pd.language_id=1
WHERE pd.name LIKE '%ВМЦ-П3-2/500%' AND p.status=1
LIMIT 3
""",
        )
    )
    print("BATH PRODUCTS:", prods)

    bath_url = None
    product_id = None
    if prods:
        product_id = prods[0].get("product_id")
        _, seo = parse_rows(
            pma_sql(
                op,
                token,
                f"SELECT keyword FROM oc_seo_url WHERE query='product_id={product_id}' AND store_id=0 LIMIT 1",
            )
        )
        print("SEO:", seo)
        if seo:
            bath_url = "https://zpm.new-site.space/" + seo[0].get("keyword", "").lstrip("/")

    _, id_names = parse_rows(
        pma_sql(
            op,
            token,
            f"""
SELECT a.attribute_id, ad.name
FROM oc_attribute a
JOIN oc_attribute_description ad ON ad.attribute_id=a.attribute_id AND ad.language_id=1
WHERE a.attribute_id IN ({ids_csv})
ORDER BY FIELD(a.attribute_id, {ids_csv})
""",
        )
    )
    id_name_map = {r["attribute_id"]: r["name"] for r in id_names}
    print("ID MAP:", id_name_map)

    def attr_table(pid, label, url):
        _, rows = parse_rows(
            pma_sql(
                op,
                token,
                f"""
SELECT a.attribute_id, ad.name AS attribute_name, IFNULL(pa.text,'') AS product_value
FROM oc_attribute a
JOIN oc_attribute_description ad ON ad.attribute_id=a.attribute_id AND ad.language_id=1
LEFT JOIN oc_product_attribute pa ON pa.attribute_id=a.attribute_id
  AND pa.product_id={pid} AND pa.language_id=1
WHERE a.attribute_id IN ({ids_csv})
ORDER BY FIELD(a.attribute_id, {ids_csv})
""",
            )
        )
        html = urllib.request.urlopen(url, timeout=60).read().decode("utf-8", "replace")
        hero = hero_atts(html)
        specs = spec_names(html)
        table = []
        for r in rows:
            aid = r.get("attribute_id")
            name = r.get("attribute_name", id_name_map.get(aid, ""))
            val = (r.get("product_value") or "").strip()
            on_prod = "YES" if val else "NO"
            in_specs = "YES" if any(name.lower() in k or k in name.lower() for k in specs) else "NO"
            in_hero = "YES" if any(name.lower() in h["name"].lower() or h["name"].lower() in name.lower() for h in hero) else "NO"
            table.append(
                {
                    "id": aid,
                    "name": name,
                    "value": val,
                    "on_product": on_prod,
                    "in_full_specs": in_specs,
                    "in_hero": in_hero,
                }
            )
        print(f"\n=== {label} pid={pid} ===")
        print("URL:", url)
        print("HERO:", hero)
        for t in table:
            print(t)

    if product_id and bath_url:
        attr_table(product_id, "BATH", bath_url)

    _, table_prod = parse_rows(
        pma_sql(
            op,
            token,
            """
SELECT p.product_id FROM oc_product p
JOIN oc_product_description pd ON pd.product_id=p.product_id AND pd.language_id=1
WHERE pd.name LIKE '%SP-P-18-6%' AND p.status=1 LIMIT 1
""",
        )
    )
    if table_prod:
        attr_table(table_prod[0]["product_id"], "TABLE", TABLE)


if __name__ == "__main__":
    main()
