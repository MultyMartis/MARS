#!/usr/bin/env python3
"""BZPM M8.3 Wave 1 — TEST cleanup on polygonws_zpm (TEST only)."""
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

WORK = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\m8.3-wave1-cleanup-work")
BACKUP = WORK / "backups"
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

PRODUCT_ID = 3071
TEST_ATTR_IDS = [16, 105, 106, 107, 108, 109, 111]
VALUE_ATTR_IDS = [105, 106, 107, 108, 109, 111]


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


def run(op, sql, expect_rows=True):
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
    if "MySQL said:" in html or "#1064" in html or "Access denied" in html:
        err = re.search(r"MySQL said:\s*<[^>]+>([^<]+)", html)
        raise RuntimeError(f"SQL error: {err.group(1).strip() if err else 'mysql error'}")
    if not expect_rows:
        affected = re.search(r"(\d+)\s+rows?\s+affected", html, re.I)
        return {"affected": affected.group(1) if affected else "unknown", "html_snip": html[:500]}
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
        m = re.search(r"(\d+)\s+rows?\s+affected", html, re.I)
        if m:
            return [{"affected": m.group(1)}]
        return []
    h = [x.lower() for x in rows[0]]
    return [dict(zip(h, r)) for r in rows[1:] if len(r) == len(h)]


def backup_state(op):
    ids = ",".join(str(i) for i in TEST_ATTR_IDS)
    val_ids = ",".join(str(i) for i in VALUE_ATTR_IDS)
    return {
        "backup_utc": datetime.now(timezone.utc).isoformat(),
        "product": run(
            op,
            f"""
            SELECT p.product_id, p.model, p.status, p.length, p.width, p.height, p.weight,
                   pd.name, pd.description
            FROM oc_product p
            JOIN oc_product_description pd ON pd.product_id = p.product_id AND pd.language_id = 1
            WHERE p.product_id = {PRODUCT_ID}
            """,
        ),
        "product_attributes": run(
            op,
            f"""
            SELECT pa.product_id, pa.attribute_id, pa.language_id, pa.text, ad.name AS attribute_name
            FROM oc_product_attribute pa
            JOIN oc_attribute_description ad ON ad.attribute_id = pa.attribute_id AND ad.language_id = 1
            WHERE pa.product_id = {PRODUCT_ID} AND pa.attribute_id IN ({val_ids})
            """,
        ),
        "attribute_definitions": run(
            op,
            f"""
            SELECT a.attribute_id, a.attribute_group_id, a.sort_order, a.filter_name,
                   ad.language_id, ad.name
            FROM oc_attribute a
            JOIN oc_attribute_description ad ON ad.attribute_id = a.attribute_id
            WHERE a.attribute_id IN ({ids})
            """,
        ),
    }


def main():
    BACKUP.mkdir(parents=True, exist_ok=True)
    op = session()
    backup = backup_state(op)
    backup_path = BACKUP / f"m8.3-wave1-pre-cleanup-{STAMP}.json"
    backup_path.write_text(json.dumps(backup, ensure_ascii=False, indent=2), encoding="utf-8")

    result = {
        "cleanup_utc": datetime.now(timezone.utc).isoformat(),
        "environment": "https://zpm.new-site.space/",
        "backup_file": str(backup_path),
        "steps": [],
    }

    # 1.1 HIDE product 3071
    step = run(
        op,
        f"UPDATE oc_product SET status = 0 WHERE product_id = {PRODUCT_ID}",
        expect_rows=False,
    )
    result["steps"].append({"id": "1.1", "action": "HIDE product 3071", "result": step})

    # 1.2 DELETE TEST attribute values (105-111 except 110 is commercial — excluded)
    step = run(
        op,
        f"""
        DELETE FROM oc_product_attribute
        WHERE product_id = {PRODUCT_ID}
          AND attribute_id IN ({",".join(str(i) for i in VALUE_ATTR_IDS)})
        """,
        expect_rows=False,
    )
    result["steps"].append({"id": "1.2", "action": "DELETE TEST values on 3071", "result": step})

    # 1.3 DELETE TEST attribute definitions
    step = run(
        op,
        f"DELETE FROM oc_attribute_description WHERE attribute_id IN ({",".join(str(i) for i in TEST_ATTR_IDS)})",
        expect_rows=False,
    )
    result["steps"].append({"id": "1.3a", "action": "DELETE oc_attribute_description", "result": step})

    step = run(
        op,
        f"DELETE FROM oc_attribute WHERE attribute_id IN ({",".join(str(i) for i in TEST_ATTR_IDS)})",
        expect_rows=False,
    )
    result["steps"].append({"id": "1.3b", "action": "DELETE oc_attribute defs", "result": step})

    # Post-verify
    verify = {
        "product_3071_status": run(
            op, f"SELECT product_id, status FROM oc_product WHERE product_id = {PRODUCT_ID}"
        ),
        "remaining_test_values": run(
            op,
            """
            SELECT pa.product_id, pa.attribute_id, ad.name, pa.text
            FROM oc_product_attribute pa
            JOIN oc_attribute_description ad ON ad.attribute_id = pa.attribute_id AND ad.language_id = 1
            WHERE ad.name LIKE '%ТЕСТ%' OR ad.name LIKE '%тест%'
            """,
        ),
        "remaining_test_defs": run(
            op,
            """
            SELECT a.attribute_id, ad.name
            FROM oc_attribute a
            JOIN oc_attribute_description ad ON ad.attribute_id = a.attribute_id AND ad.language_id = 1
            WHERE ad.name LIKE '%ТЕСТ%' OR ad.name = 'Параметр'
            """,
        ),
        "attr_110_preserved": run(
            op,
            """
            SELECT a.attribute_id, ad.name,
                   (SELECT COUNT(*) FROM oc_product_attribute pa
                    WHERE pa.attribute_id = 110 AND pa.language_id = 1) AS value_rows
            FROM oc_attribute a
            JOIN oc_attribute_description ad ON ad.attribute_id = a.attribute_id AND ad.language_id = 1
            WHERE a.attribute_id = 110
            """,
        ),
    }
    result["verify"] = verify

    out = WORK / f"m8.3-wave1-cleanup-result-{STAMP}.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
