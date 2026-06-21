#!/usr/bin/env python3
"""BZPM M8.3 Wave 1 — live TEST audit (read-only)."""
import json
import re
import ssl
import urllib.parse
import urllib.request
import http.cookiejar
from datetime import datetime, timezone
from html import unescape

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DU = "polygonws_zpm"
DP = "VBCDry2bJ5P"
OUT = r"C:\AI MARS\projects\ocpilot\sites\site-002\m8.3-wave1-cleanup-work\m8.3-wave1-audit-result.json"

TEST_ATTR_IDS = (16, 105, 106, 107, 108, 109, 111)
MIGRATION_ATTR_IDS = (108, 109, 110, 111)


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
        if "MySQL returned an empty result set" in html:
            return []
        m = re.search(r"<td[^>]*>\s*(\d+(?:\.\d+)?)\s*</td>", html)
        if m:
            return [{"cnt": m.group(1)}]
        return []
    h = [x.lower() for x in rows[0]]
    return [dict(zip(h, r)) for r in rows[1:] if len(r) == len(h)]


def main():
    op = session()
    result = {
        "audit_utc": datetime.now(timezone.utc).isoformat(),
        "environment": "https://zpm.new-site.space/",
        "db": DB,
    }

    result["product_3071"] = run(
        op,
        """
        SELECT p.product_id, p.model, p.status, p.length, p.width, p.height, p.weight,
               pd.name, pd.description
        FROM oc_product p
        JOIN oc_product_description pd ON pd.product_id = p.product_id AND pd.language_id = 1
        WHERE p.product_id = 3071
        """,
    )

    result["product_3071_categories"] = run(
        op,
        """
        SELECT ptc.category_id, cd.name, c.status AS category_status
        FROM oc_product_to_category ptc
        JOIN oc_category c ON c.category_id = ptc.category_id
        JOIN oc_category_description cd ON cd.category_id = ptc.category_id AND cd.language_id = 1
        WHERE ptc.product_id = 3071
        ORDER BY ptc.category_id
        """,
    )

    result["test_attribute_definitions"] = run(
        op,
        f"""
        SELECT a.attribute_id, ad.name, a.filter_name, agd.name AS attribute_group,
               (SELECT COUNT(DISTINCT pa.product_id)
                FROM oc_product_attribute pa
                JOIN oc_product p ON p.product_id = pa.product_id
                WHERE pa.attribute_id = a.attribute_id AND pa.language_id = 1
                  AND TRIM(pa.text) != '' AND p.status = 1) AS active_product_count,
               (SELECT COUNT(DISTINCT pa.product_id)
                FROM oc_product_attribute pa
                WHERE pa.attribute_id = a.attribute_id AND pa.language_id = 1
                  AND TRIM(pa.text) != '') AS all_product_count
        FROM oc_attribute a
        JOIN oc_attribute_description ad ON ad.attribute_id = a.attribute_id AND ad.language_id = 1
        JOIN oc_attribute_group_description agd ON agd.attribute_group_id = a.attribute_group_id AND agd.language_id = 1
        WHERE a.attribute_id IN ({",".join(str(i) for i in TEST_ATTR_IDS)})
        ORDER BY a.attribute_id
        """,
    )

    result["test_attribute_values"] = run(
        op,
        """
        SELECT pa.product_id, p.status, pa.attribute_id, ad.name AS attribute_name, pa.text
        FROM oc_product_attribute pa
        JOIN oc_attribute_description ad ON ad.attribute_id = pa.attribute_id AND ad.language_id = 1
        JOIN oc_product p ON p.product_id = pa.product_id
        WHERE pa.language_id = 1
          AND (ad.name LIKE '%ТЕСТ%' OR ad.name LIKE '%тест%' OR ad.name LIKE '%TEST%' OR ad.name LIKE '%test%'
               OR pa.text LIKE '%ТЕСТ%' OR pa.text LIKE '%тест%' OR pa.text LIKE '%TEST%' OR pa.text LIKE '%test%')
        ORDER BY pa.product_id, pa.attribute_id
        """,
    )

    result["migration_attrs"] = run(
        op,
        f"""
        SELECT a.attribute_id, ad.name, a.filter_name,
               (SELECT COUNT(DISTINCT pa.product_id)
                FROM oc_product_attribute pa
                JOIN oc_product p ON p.product_id = pa.product_id
                WHERE pa.attribute_id = a.attribute_id AND pa.language_id = 1
                  AND TRIM(pa.text) != '' AND p.status = 1) AS active_product_count
        FROM oc_attribute a
        JOIN oc_attribute_description ad ON ad.attribute_id = a.attribute_id AND ad.language_id = 1
        WHERE a.attribute_id IN ({",".join(str(i) for i in MIGRATION_ATTR_IDS)})
        ORDER BY a.attribute_id
        """,
    )

    result["migration_attr_values_3071"] = run(
        op,
        f"""
        SELECT pa.attribute_id, ad.name, pa.text
        FROM oc_product_attribute pa
        JOIN oc_attribute_description ad ON ad.attribute_id = pa.attribute_id AND ad.language_id = 1
        WHERE pa.product_id = 3071 AND pa.language_id = 1
          AND pa.attribute_id IN ({",".join(str(i) for i in MIGRATION_ATTR_IDS)})
        ORDER BY pa.attribute_id
        """,
    )

    result["test_name_products"] = run(
        op,
        """
        SELECT p.product_id, p.status, pd.name
        FROM oc_product p
        JOIN oc_product_description pd ON pd.product_id = p.product_id AND pd.language_id = 1
        WHERE pd.name LIKE '%тест%' OR pd.name LIKE '%ТЕСТ%' OR pd.name LIKE '%test%' OR pd.name LIKE '%TEST%'
        ORDER BY p.status DESC, p.product_id
        LIMIT 50
        """,
    )

    result["attribute_110_detail"] = run(
        op,
        """
        SELECT pa.product_id, p.status, pa.text
        FROM oc_product_attribute pa
        JOIN oc_product p ON p.product_id = pa.product_id
        WHERE pa.attribute_id = 110 AND pa.language_id = 1 AND TRIM(pa.text) != ''
        """,
    )

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
