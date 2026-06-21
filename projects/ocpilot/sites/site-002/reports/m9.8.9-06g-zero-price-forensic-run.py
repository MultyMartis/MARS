#!/usr/bin/env python3
"""M9.8.9-06G — read-only zero-price forensic audit. NO mutations."""
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

PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"
BASE_URL = "https://zpm.new-site.space"

OUT_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-06g-work")
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
    db_html = op.open(
        PMA + "/db_structure.php?db=" + urllib.parse.quote(DB), timeout=60
    ).read().decode("utf-8", "replace")
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


def fetch_plp(url: str) -> dict:
    html = urllib.request.urlopen(url, timeout=60).read().decode("utf-8", "replace")
    out = {"url": url, "fetched_at": datetime.now(timezone.utc).isoformat()}
    m_from = re.search(r'name="price_from"[^>]*placeholder="([^"]*)"', html)
    m_to = re.search(r'name="price_to"[^>]*placeholder="([^"]*)"', html)
    m_min = re.search(r'data-range-min[^>]*min="([^"]*)"', html)
    m_max = re.search(r'data-range-max[^>]*max="([^"]*)"', html)
    out["placeholder_from"] = m_from.group(1) if m_from else None
    out["placeholder_to"] = m_to.group(1) if m_to else None
    out["range_min_attr"] = m_min.group(1) if m_min else None
    out["range_max_attr"] = m_max.group(1) if m_max else None
    out["po_zaprosu_count"] = len(re.findall(r"По запросу", html))
    return out


def main():
    op, csrf = pma_session()
    results = {
        "task": "M9.8.9-06G",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "authority": "SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01",
        "queries": {},
    }

    results["queries"]["zero_price_total"] = pma_sql(
        op,
        csrf,
        """
SELECT COUNT(*) AS total_zero_price
FROM oc_product p
INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
WHERE p.price = 0 AND p.status = 1 AND p.date_available <= NOW()
""",
    )

    results["queries"]["zero_price_sample"] = pma_sql(
        op,
        csrf,
        """
SELECT p.product_id, p.model, p.sku, pd.name, p.price, p.quantity
FROM oc_product p
INNER JOIN oc_product_description pd ON p.product_id = pd.product_id AND pd.language_id = 1
INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
WHERE p.price = 0 AND p.status = 1 AND p.date_available <= NOW()
ORDER BY p.product_id
LIMIT 30
""",
    )

    results["queries"]["zero_price_products_detail"] = pma_sql(
        op,
        csrf,
        """
SELECT p.product_id, p.model, p.sku, pd.name, p.price, p.quantity,
       GROUP_CONCAT(DISTINCT p2c.category_id ORDER BY p2c.category_id SEPARATOR ',') AS category_ids
FROM oc_product p
LEFT JOIN oc_product_description pd ON p.product_id = pd.product_id AND pd.language_id = 1
LEFT JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
WHERE p.price = 0 AND p.status = 1 AND p.date_available <= NOW()
GROUP BY p.product_id, p.model, p.sku, pd.name, p.price, p.quantity
ORDER BY p.product_id
""",
    )

    results["queries"]["zero_price_category_names"] = pma_sql(
        op,
        csrf,
        """
SELECT p.product_id, cd.category_id, cd.name AS category_name
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_description cd ON p2c.category_id = cd.category_id AND cd.language_id = 1
WHERE p.price = 0 AND p.status = 1 AND p.date_available <= NOW()
ORDER BY p.product_id, cd.category_id
""",
    )

    results["queries"]["reported_ids"] = pma_sql(
        op,
        csrf,
        """
SELECT p.product_id, p.model, p.sku, pd.name, p.price, p.quantity, p.status
FROM oc_product p
LEFT JOIN oc_product_description pd ON p.product_id = pd.product_id AND pd.language_id = 1
WHERE p.product_id IN (144,145,1057,1058,3071)
""",
    )

    results["queries"]["reported_ids_index"] = pma_sql(
        op,
        csrf,
        """
SELECT p.product_id, p.price AS oc_price, ppi.price AS index_price, ppi.special,
       IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price) AS effective_price
FROM oc_product p
LEFT JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
WHERE p.product_id IN (144,145,1057,1058,3071)
""",
    )

    results["queries"]["zero_price_by_category"] = pma_sql(
        op,
        csrf,
        """
SELECT cp.path_id AS root_category_id, cd.name AS category_name,
       COUNT(DISTINCT p.product_id) AS zero_price_count
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id
INNER JOIN oc_category_description cd ON cp.path_id = cd.category_id AND cd.language_id = 1
INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
WHERE p.price = 0 AND p.status = 1 AND p.date_available <= NOW()
GROUP BY cp.path_id, cd.name
ORDER BY zero_price_count DESC
LIMIT 25
""",
    )

    for cat_id, key in [(301, "zero_in_301"), (80, "zero_in_80")]:
        results["queries"][key] = pma_sql(
            op,
            csrf,
            f"""
SELECT COUNT(DISTINCT p.product_id) AS cnt
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
WHERE p.price = 0 AND p.status = 1 AND p.date_available <= NOW()
""",
        )

    results["queries"]["zero_in_index_effective"] = pma_sql(
        op,
        csrf,
        """
SELECT COUNT(DISTINCT p.product_id) AS products_with_zero_effective_index
FROM oc_product p
INNER JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
WHERE p.status = 1 AND p.date_available <= NOW()
  AND IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price) = 0
""",
    )

    results["queries"]["zero_product_and_index"] = pma_sql(
        op,
        csrf,
        """
SELECT COUNT(DISTINCT p.product_id) AS cnt
FROM oc_product p
INNER JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
WHERE p.price = 0 AND p.status = 1 AND p.date_available <= NOW()
  AND ppi.price = 0
""",
    )

    for cat_id, prefix in [(301, "301"), (80, "80")]:
        results["queries"][f"price_range_{prefix}"] = pma_sql(
            op,
            csrf,
            f"""
SELECT
  MIN(IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)) AS min_price,
  MAX(IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)) AS max_price,
  COUNT(DISTINCT p.product_id) AS product_count
FROM oc_product_price_index ppi
INNER JOIN oc_product p ON ppi.product_id = p.product_id
INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id
WHERE cp.path_id = {cat_id}
  AND ppi.customer_group_id = 2
  AND p.status = 1 AND p.date_available <= NOW()
  AND p2s.store_id = 0
""",
        )
        results["queries"][f"price_range_{prefix}_excl_zero"] = pma_sql(
            op,
            csrf,
            f"""
SELECT
  MIN(IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)) AS min_price,
  MAX(IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)) AS max_price
FROM oc_product_price_index ppi
INNER JOIN oc_product p ON ppi.product_id = p.product_id
INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id
WHERE cp.path_id = {cat_id}
  AND ppi.customer_group_id = 2
  AND p.status = 1 AND p.date_available <= NOW()
  AND p2s.store_id = 0
  AND IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price) > 0
""",
        )
        results["queries"][f"zero_effective_in_{prefix}"] = pma_sql(
            op,
            csrf,
            f"""
SELECT p.product_id, p.model, p.price AS oc_price, ppi.price AS index_price, ppi.special
FROM oc_product p
INNER JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = {cat_id}
INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
WHERE p.status = 1 AND p.date_available <= NOW()
  AND IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price) = 0
ORDER BY p.product_id
LIMIT 20
""",
        )

    results["queries"]["index_coverage_301"] = pma_sql(
        op,
        csrf,
        """
SELECT
  COUNT(DISTINCT p.product_id) AS active_products,
  COUNT(DISTINCT ppi.product_id) AS indexed_products
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = 301
INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
LEFT JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
WHERE p.status = 1 AND p.date_available <= NOW()
""",
    )

    results["plp"] = {
        "stoly": fetch_plp(BASE_URL + "/katalog/nejtralnoe-oborudovanie/stoly/"),
        "sinks": fetch_plp(BASE_URL + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"),
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
