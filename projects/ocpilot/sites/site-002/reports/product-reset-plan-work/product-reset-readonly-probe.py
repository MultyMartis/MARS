#!/usr/bin/env python3
"""SITE-002 product reset plan — READ ONLY DB probe. No mutations."""
from __future__ import annotations

import json
import re
import ssl
import urllib.parse
import urllib.request
import http.cookiejar
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

# Credentials from existing OCPilot probe pattern (local script, not for report)
PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"

OUT = Path(__file__).resolve().parent / "probe-results.json"

PRODUCT_TABLES = [
    "oc_product",
    "oc_product_description",
    "oc_product_attribute",
    "oc_product_discount",
    "oc_product_filter",
    "oc_product_image",
    "oc_product_option",
    "oc_product_option_value",
    "oc_product_related",
    "oc_product_reward",
    "oc_product_special",
    "oc_product_to_category",
    "oc_product_to_download",
    "oc_product_to_layout",
    "oc_product_to_store",
    "oc_product_recurring",
    "oc_product_price_index",
    "oc_review",
    "oc_seo_url",
    "oc_coupon_product",
    "oc_customer_wishlist",
    "oc_order_product",
]

CUSTOM_CANDIDATES = [
    "oc_category_docs",
    "oc_category_doc_description",
    "cron",
]


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
    db_html = op.open(
        PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60
    ).read().decode("utf-8", "replace")
    csrf = re.search(r'name="token"\s+value="([^"]+)"', db_html).group(1)
    return op, csrf


def pma_sql(op, csrf, sql: str) -> list[dict]:
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
    for tbl in re.findall(
        r'<table[^>]*class="[^"]*table[^"]*"[^>]*>(.*?)</table>', html, re.S
    ):
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
            return [dict(zip(h, r)) for r in parsed[1:] if len(r) == len(h)]
    return []


def main():
    op, csrf = pma_session()
    results = {"run_at": datetime.now(timezone.utc).isoformat(), "db": DB}

    # Discover product-related tables
    all_tables = pma_sql(
        op,
        csrf,
        "SELECT TABLE_NAME FROM information_schema.TABLES "
        f"WHERE TABLE_SCHEMA = '{DB}' AND (TABLE_NAME LIKE 'oc\\_product%' "
        "OR TABLE_NAME LIKE 'oc\\_review%' OR TABLE_NAME LIKE '%product%') "
        "ORDER BY TABLE_NAME",
    )
    results["discovered_tables"] = sorted({
        t for r in all_tables
        for t in [r.get("table_name") or r.get("TABLE_NAME")]
        if t
    })

    # Row counts per known table
    table_counts = {}
    for tbl in sorted(set(PRODUCT_TABLES + results["discovered_tables"])):
        if not tbl:
            continue
        cnt = pma_sql(op, csrf, f"SELECT COUNT(*) AS row_count FROM `{tbl}`")
        table_counts[tbl] = cnt[0].get("row_count") if cnt else "ERROR"

    results["table_counts"] = table_counts

    # product_id distinct counts where applicable
    pid_tables = [
        t
        for t in table_counts
        if t.startswith("oc_product") or t in ("oc_review", "oc_coupon_product", "oc_customer_wishlist", "oc_order_product")
    ]
    pid_counts = {}
    for tbl in pid_tables:
        if tbl == "oc_product":
            continue
        cols = pma_sql(
            op,
            csrf,
            f"SELECT COLUMN_NAME FROM information_schema.COLUMNS "
            f"WHERE TABLE_SCHEMA='{DB}' AND TABLE_NAME='{tbl}' AND COLUMN_NAME='product_id'",
        )
        if cols:
            r = pma_sql(op, csrf, f"SELECT COUNT(DISTINCT product_id) AS distinct_product_ids FROM `{tbl}`")
            pid_counts[tbl] = r[0].get("distinct_product_ids") if r else "ERROR"
    results["distinct_product_id_counts"] = pid_counts

    summary_queries = {
        "total_products": "SELECT COUNT(*) AS c FROM oc_product",
        "active_products": "SELECT COUNT(*) AS c FROM oc_product WHERE status=1 AND date_available <= NOW()",
        "products_with_xml_id": "SELECT COUNT(*) AS c FROM oc_product WHERE xml_id IS NOT NULL AND xml_id <> ''",
        "product_images_rows": "SELECT COUNT(*) AS c FROM oc_product_image",
        "products_with_main_image": "SELECT COUNT(*) AS c FROM oc_product WHERE image IS NOT NULL AND image <> ''",
        "product_seo_urls": "SELECT COUNT(*) AS c FROM oc_seo_url WHERE query LIKE 'product_id=%'",
        "product_price_index_rows": "SELECT COUNT(*) AS c FROM oc_product_price_index",
        "price_index_products_group2": "SELECT COUNT(DISTINCT product_id) AS c FROM oc_product_price_index WHERE customer_group_id=2",
        "category_docs_rows": "SELECT COUNT(*) AS c FROM oc_category_docs",
        "order_product_rows": "SELECT COUNT(*) AS c FROM oc_order_product",
        "customer_wishlist_rows": "SELECT COUNT(*) AS c FROM oc_customer_wishlist",
        "coupon_product_rows": "SELECT COUNT(*) AS c FROM oc_coupon_product",
        "reviews_rows": "SELECT COUNT(*) AS c FROM oc_review",
    }
    summary = {}
    for key, sql in summary_queries.items():
        r = pma_sql(op, csrf, sql)
        summary[key] = r[0].get("c") if r else "ERROR"
    results["summary"] = summary

    # Category product counts (key branches)
    branch_sql = """
    SELECT cp.path_id AS category_id,
           cd.name AS category_name,
           COUNT(DISTINCT p.product_id) AS product_count,
           SUM(CASE WHEN p.status=1 AND p.date_available <= NOW() THEN 1 ELSE 0 END) AS active_count
    FROM oc_category_path cp
    INNER JOIN oc_product_to_category p2c ON cp.category_id = p2c.category_id
    INNER JOIN oc_product p ON p2c.product_id = p.product_id
    INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
    LEFT JOIN oc_category_description cd ON cp.path_id = cd.category_id AND cd.language_id = 1
    WHERE cp.path_id IN (79, 80, 207, 301, 322, 326)
    GROUP BY cp.path_id, cd.name
    ORDER BY cp.path_id
    """
    results["branch_product_counts"] = pma_sql(op, csrf, branch_sql)

    # Image path samples
    img_sql = """
    SELECT image, COUNT(*) AS cnt FROM oc_product
    WHERE image IS NOT NULL AND image <> ''
    GROUP BY image ORDER BY cnt DESC LIMIT 15
    """
    results["main_image_samples"] = pma_sql(op, csrf, img_sql)

    gallery_sql = """
    SELECT image, COUNT(*) AS cnt FROM oc_product_image
    GROUP BY image ORDER BY cnt DESC LIMIT 10
    """
    results["gallery_image_samples"] = pma_sql(op, csrf, gallery_sql)

    # Tables with product_id column not in standard list
    extra_pid = pma_sql(
        op,
        csrf,
        f"SELECT TABLE_NAME FROM information_schema.COLUMNS "
        f"WHERE TABLE_SCHEMA='{DB}' AND COLUMN_NAME='product_id' ORDER BY TABLE_NAME",
    )
    results["all_tables_with_product_id"] = sorted({
        t for r in extra_pid
        for t in [r.get("table_name") or r.get("TABLE_NAME")]
        if t
    })

    OUT.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
