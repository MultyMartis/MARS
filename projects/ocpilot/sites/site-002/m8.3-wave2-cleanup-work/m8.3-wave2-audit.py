#!/usr/bin/env python3
"""BZPM M8.3 Wave 2 — live TEST audit (read-only)."""
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
DU = "polygonws_zpm"
DP = "VBCDry2bJ5P"

WORK = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\m8.3-wave2-cleanup-work")
OUT = WORK / "m8.3-wave2-audit-result.json"

PACKAGING_IDS = (44, 45, 46, 52, 53, 54, 56, 57)
SERVICE_IDS = (43, 48, 58)
TECHNICAL_WAVE2_IDS = (12, 27, 34, 36, 42)  # listed for TASK 1; not hidden in Wave 2 impl


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


def audit_attrs(op, ids, classification):
    id_list = ",".join(str(i) for i in ids)
    rows = run(
        op,
        f"""
        SELECT a.attribute_id, ad.name, a.filter_name, agd.name AS attribute_group,
               (SELECT COUNT(DISTINCT pa.product_id)
                FROM oc_product_attribute pa
                JOIN oc_product p ON p.product_id = pa.product_id
                WHERE pa.attribute_id = a.attribute_id AND pa.language_id = 1
                  AND TRIM(pa.text) != '' AND p.status = 1) AS active_sku_count,
               (SELECT COUNT(DISTINCT pa.product_id)
                FROM oc_product_attribute pa
                WHERE pa.attribute_id = a.attribute_id AND pa.language_id = 1
                  AND TRIM(pa.text) != '') AS all_sku_count,
               CASE WHEN EXISTS (
                 SELECT 1 FROM oc_product_attribute pa2
                 JOIN oc_product p2 ON p2.product_id = pa2.product_id
                 JOIN oc_product_to_category p2c ON p2c.product_id = p2.product_id
                 WHERE pa2.attribute_id = a.attribute_id AND pa2.language_id = 1
                   AND TRIM(pa2.text) != '' AND p2.status = 1
                   AND p2c.category_id IN (
                     SELECT category_id FROM oc_category_path WHERE path_id = 79
                   )
               ) THEN 'in_filter_today' ELSE 'no_active_neutral_fill' END AS filter_usage
        FROM oc_attribute a
        JOIN oc_attribute_description ad ON ad.attribute_id = a.attribute_id AND ad.language_id = 1
        LEFT JOIN oc_attribute_group_description agd
          ON agd.attribute_group_id = a.attribute_group_id AND agd.language_id = 1
        WHERE a.attribute_id IN ({id_list})
        ORDER BY a.attribute_id
        """,
    )
    for row in rows:
        row["classification"] = classification
    return rows


def main():
    op = session()
    result = {
        "audit_utc": datetime.now(timezone.utc).isoformat(),
        "environment": "https://zpm.new-site.space/",
        "db": DB,
        "wave": "M8.3 Wave 2",
        "packaging": audit_attrs(op, PACKAGING_IDS, "PACKAGING"),
        "service": audit_attrs(op, SERVICE_IDS, "SERVICE"),
        "technical_wave2_listed_not_hidden": audit_attrs(op, TECHNICAL_WAVE2_IDS, "TECHNICAL"),
    }

    result["wave1_verify"] = {
        "test_defs_remaining": run(
            op,
            """
            SELECT a.attribute_id, ad.name
            FROM oc_attribute a
            JOIN oc_attribute_description ad ON ad.attribute_id = a.attribute_id AND ad.language_id = 1
            WHERE ad.name LIKE '%ТЕСТ%' OR ad.name = 'Параметр'
            """,
        ),
        "product_3071_status": run(
            op, "SELECT product_id, status FROM oc_product WHERE product_id = 3071"
        ),
    }

    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
