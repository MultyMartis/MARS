#!/usr/bin/env python3
"""M9.8.9-06C — read-only price index root cause audit. NO mutations."""
import ftplib
import io
import json
import re
import ssl
import urllib.parse
import urllib.request
import http.cookiejar
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

BASE = "https://zpm.new-site.space"
PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"
FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

OUT_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-06c-audit-data")
OUT_JSON = OUT_DIR / "audit-data.json"


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


def pma_sql(op, csrf, sql: str) -> list:
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
        return []
    h = [x.lower() for x in rows[0]]
    return [dict(zip(h, r)) for r in rows[1:] if len(r) == len(h)]


def ftp_download(remote_path: str) -> bytes | None:
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=120)
        ftp.login(FTP_USER, FTP_PASS)
        bio = io.BytesIO()
        ftp.retrbinary("RETR " + remote_path, bio.write)
        ftp.quit()
        return bio.getvalue()
    except Exception as e:
        return None


def ftp_list(path: str) -> list:
    try:
        ftp = ftplib.FTP(FTP_HOST, timeout=120)
        ftp.login(FTP_USER, FTP_PASS)
        lines = []
        ftp.retrlines("LIST " + path, lines.append)
        ftp.quit()
        return lines
    except Exception:
        return []


def ftp_grep_paths(base_paths: list, patterns: list) -> dict:
    """List candidate PHP files and grep for patterns via download."""
    results = {}
    candidates = [
        "catalog/controller/common/cronjob.php",
        "admin/controller/common/cronjob.php",
        "reindex_prices.php",
        "catalog/model/catalog/product.php",
        "admin/model/catalog/product.php",
        "admin/controller/extension/module/exchange1c.php",
        "admin/controller/tool/exchange1c.php",
        "catalog/controller/tool/exchange1c.php",
    ]
    # expand via directory listing
    for sub in [
        "catalog/controller/common",
        "admin/controller/common",
        "admin/controller/extension/module",
        "admin/controller/tool",
        "system/library",
    ]:
        for line in ftp_list(sub):
            parts = line.split()
            if len(parts) >= 9 and parts[-1].endswith(".php"):
                rel = sub + "/" + parts[-1]
                if rel not in candidates:
                    candidates.append(rel)

    for rel in candidates:
        data = ftp_download(rel)
        if not data:
            continue
        text = data.decode("utf-8", "replace")
        hits = {}
        for pat in patterns:
            if pat.lower() in text.lower() or re.search(pat, text, re.I):
                hits[pat] = True
        if hits:
            results[rel] = {
                "size": len(data),
                "patterns": list(hits.keys()),
                "snippet_lines": [],
            }
            for i, line in enumerate(text.splitlines(), 1):
                for pat in patterns:
                    if pat.lower() in line.lower() or re.search(pat, line, re.I):
                        results[rel]["snippet_lines"].append({"line": i, "text": line.strip()[:200]})
                        break
    return results


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    data = {"timestamp": datetime.now(timezone.utc).isoformat(), "errors": []}

    # --- SQL: cron table ---
    try:
        op, csrf = pma_session()
        data["cron_describe"] = pma_sql(op, csrf, "DESCRIBE oc_cron")
        data["cron_all"] = pma_sql(
            op,
            csrf,
            "SELECT * FROM oc_cron ORDER BY cron_id",
        )
        data["cron_filtered"] = pma_sql(
            op,
            csrf,
            """
            SELECT * FROM oc_cron
            WHERE LOWER(COALESCE(file,'')) LIKE '%import%'
               OR LOWER(COALESCE(file,'')) LIKE '%offer%'
               OR LOWER(COALESCE(file,'')) LIKE '%1c%'
               OR LOWER(COALESCE(file,'')) LIKE '%exchange%'
               OR LOWER(COALESCE(file,'')) LIKE '%price%'
               OR LOWER(COALESCE(file,'')) LIKE '%product%'
               OR LOWER(COALESCE(route,'')) LIKE '%import%'
               OR LOWER(COALESCE(route,'')) LIKE '%offer%'
               OR LOWER(COALESCE(route,'')) LIKE '%1c%'
               OR LOWER(COALESCE(route,'')) LIKE '%exchange%'
               OR LOWER(COALESCE(action,'')) LIKE '%import%'
               OR LOWER(COALESCE(action,'')) LIKE '%offer%'
            ORDER BY cron_id
            """,
        )
        # fallback if table name is `cron` without prefix
        if not data["cron_all"]:
            data["cron_describe"] = pma_sql(op, csrf, "DESCRIBE cron")
            data["cron_all"] = pma_sql(op, csrf, "SELECT * FROM cron ORDER BY cron_id")
            data["cron_filtered"] = pma_sql(
                op,
                csrf,
                """
                SELECT * FROM cron
                WHERE LOWER(COALESCE(file,'')) LIKE '%import%'
                   OR LOWER(COALESCE(file,'')) LIKE '%offer%'
                   OR LOWER(COALESCE(file,'')) LIKE '%1c%'
                   OR LOWER(COALESCE(file,'')) LIKE '%exchange%'
                   OR LOWER(COALESCE(file,'')) LIKE '%price%'
                   OR LOWER(COALESCE(file,'')) LIKE '%product%'
                ORDER BY cron_id
                """,
            )
    except Exception as e:
        data["errors"].append(f"cron_sql: {e}")

    # --- SQL: coverage ---
    coverage_sql = """
    SELECT
      COUNT(DISTINCT p.product_id) AS active_products,
      COUNT(DISTINCT ppi.product_id) AS indexed_products,
      ROUND(100.0 * COUNT(DISTINCT ppi.product_id) / NULLIF(COUNT(DISTINCT p.product_id), 0), 2) AS coverage_pct
    FROM oc_product p
    INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
    INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
    INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
    LEFT JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
    WHERE p.status = 1 AND p.date_available <= NOW()
    """
    global_sql = """
    SELECT
      (SELECT COUNT(*) FROM oc_product p
       INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
       WHERE p.status = 1 AND p.date_available <= NOW()) AS active_products,
      (SELECT COUNT(DISTINCT product_id) FROM oc_product_price_index WHERE customer_group_id = 2) AS indexed_group2,
      (SELECT COUNT(*) FROM oc_product_price_index) AS total_index_rows
    """
    try:
        op, csrf = pma_session()
        data["coverage_301"] = pma_sql(op, csrf, coverage_sql.format(cat_id=301))
        data["coverage_80"] = pma_sql(op, csrf, coverage_sql.format(cat_id=80))
        data["coverage_global"] = pma_sql(op, csrf, global_sql)
    except Exception as e:
        data["errors"].append(f"coverage_sql: {e}")

    # --- SQL: variant C list for subtree 301 ---
    variant_c_sql = """
    SELECT
      p.product_id,
      p.model,
      p.sku,
      pd.name,
      p.price,
      p.price2,
      p.price3,
      p.discount1c,
      CASE WHEN ppi.product_id IS NOT NULL THEN 'yes' ELSE 'no' END AS has_price_index_group_2,
      ppi.price AS index_price,
      ppi.special AS index_special
    FROM oc_product p
    INNER JOIN oc_product_description pd ON p.product_id = pd.product_id AND pd.language_id = 1
    INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
    INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = 301
    INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
    LEFT JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
    WHERE p.status = 1 AND p.date_available <= NOW()
    ORDER BY p.product_id
    """
    try:
        op, csrf = pma_session()
        data["variant_c_301"] = pma_sql(op, csrf, variant_c_sql)
    except Exception as e:
        data["errors"].append(f"variant_c_sql: {e}")

    # --- FTP: key files ---
    key_files = [
        "catalog/controller/common/cronjob.php",
        "reindex_prices.php",
        "catalog/model/catalog/product.php",
    ]
    data["ftp_files"] = {}
    for rel in key_files:
        raw = ftp_download(rel)
        if raw:
            text = raw.decode("utf-8", "replace")
            OUT_DIR.joinpath(rel.replace("/", "__")).write_text(text, encoding="utf-8")
            data["ftp_files"][rel] = {"size": len(raw), "lines": len(text.splitlines())}

    # grep across codebase
    patterns = [
        "refreshPriceIndex",
        "import0_1",
        "offers0_1",
        "1c_exchange",
        "1c_incoming",
        "product_price_index",
        "price2",
        "price3",
        "discount1c",
        "exchange1c",
        "offers",
    ]
    data["ftp_grep"] = ftp_grep_paths([], patterns)

    # 1c_exchange dir listing
    data["ftp_1c_exchange"] = ftp_list("1c_exchange")
    data["ftp_1c_incoming"] = ftp_list("1c_incoming")

    OUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in data.items()}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
