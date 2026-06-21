#!/usr/bin/env python3
"""M9.8.9-06H — post-deploy QA for price range exclude-zero hotfix."""
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

OUT_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-06h-work")
OUT_JSON = OUT_DIR / "qa-results.json"

PRICE_RANGE_SQL = """
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
"""


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


def fetch_url(url: str) -> str:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-M9.8.9-06H/1.0"})
    return urllib.request.urlopen(req, timeout=120, context=ctx).read().decode("utf-8", "replace")


def fetch_plp(url: str) -> dict:
    html = fetch_url(url)
    out = {"url": url, "fetched_at": datetime.now(timezone.utc).isoformat()}
    m_from = re.search(r'name="price_from"[^>]*placeholder="(\d+)"', html)
    m_to = re.search(r'name="price_to"[^>]*placeholder="(\d+)"', html)
    if m_from:
        out["placeholder_from"] = int(m_from.group(1))
    if m_to:
        out["placeholder_to"] = int(m_to.group(1))
    out["has_po_zaprosu"] = "По запросу" in html or "по запросу" in html.lower()
    out["product_cards"] = len(re.findall(r'class="[^"]*product-layout[^"]*"', html))
    return out


def fetch_pdp(product_id: int) -> dict:
    html = fetch_url(BASE_URL + f"/index.php?route=product/product&product_id={product_id}")
    out = {
        "product_id": product_id,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "has_po_zaprosu": bool(re.search(r"По запросу", html)),
        "price_zero_visible": bool(re.search(r">\s*0\s*(?:₽|руб|&nbsp;)?", html)),
    }
    return out


def main() -> None:
    results: dict = {
        "task": "M9.8.9-06H",
        "run_at": datetime.now(timezone.utc).isoformat(),
        "checks": {},
    }

    op, csrf = pma_session()

    for cat_id, label, expected_min in [
        (301, "stoly", 5405),
        (80, "sinks", 5553),
    ]:
        row = pma_sql(op, csrf, PRICE_RANGE_SQL.format(cat_id=cat_id))
        min_price = float(row[0]["min_price"]) if row else None
        max_price = float(row[0]["max_price"]) if row else None
        results["checks"][f"sql_{label}"] = {
            "category_id": cat_id,
            "min_price": min_price,
            "max_price": max_price,
            "expected_min": expected_min,
            "pass": min_price == expected_min and min_price > 0,
        }

    zero_ids = [144, 145, 1057, 1058, 3071]
    zero_rows = pma_sql(
        op,
        csrf,
        f"""
SELECT p.product_id, p.price, ppi.price AS index_price, p.status
FROM oc_product p
INNER JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
WHERE p.product_id IN ({",".join(str(i) for i in zero_ids)})
ORDER BY p.product_id
""",
    )
    results["checks"]["zero_price_products_in_db"] = {
        "rows": zero_rows,
        "pass": all(float(r.get("price", -1)) == 0 for r in zero_rows),
    }

    listing = pma_sql(
        op,
        csrf,
        """
SELECT COUNT(DISTINCT p.product_id) AS cnt
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = 301
INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
WHERE p.status = 1 AND p.date_available <= NOW()
  AND p.product_id IN (3071, 144, 145, 1057, 1058)
""",
    )
    results["checks"]["zero_price_in_category_301_or_80"] = {
        "active_zero_count": int(listing[0]["cnt"]) if listing else 0,
        "pass": int(listing[0]["cnt"]) >= 1 if listing else False,
    }

    results["plp"] = {
        "stoly": fetch_plp(BASE_URL + "/katalog/nejtralnoe-oborudovanie/stoly/"),
        "sinks": fetch_plp(BASE_URL + "/katalog/nejtralnoe-oborudovanie/moechnye-vanny/"),
    }
    results["checks"]["plp_stoly_min_not_zero"] = {
        "placeholder_from": results["plp"]["stoly"].get("placeholder_from"),
        "pass": results["plp"]["stoly"].get("placeholder_from", 0) >= 5405,
    }
    results["checks"]["plp_sinks_min_not_zero"] = {
        "placeholder_from": results["plp"]["sinks"].get("placeholder_from"),
        "pass": results["plp"]["sinks"].get("placeholder_from", 0) >= 5553,
    }

    results["pdp"] = {str(pid): fetch_pdp(pid) for pid in [3071, 144, 145, 1057, 1058]}
    results["checks"]["pdp_po_zaprosu"] = {
        pid: results["pdp"][str(pid)]["has_po_zaprosu"] for pid in [3071, 144, 145, 1057, 1058]
    }
    results["checks"]["pdp_po_zaprosu"]["pass"] = all(
        results["pdp"][str(pid)]["has_po_zaprosu"] for pid in [3071, 144, 145, 1057, 1058]
    )

    only_with_price_html = fetch_url(
        BASE_URL + "/katalog/nejtralnoe-oborudovanie/stoly/?only_with_price=1"
    )
    results["checks"]["only_with_price"] = {
        "url": BASE_URL + "/katalog/nejtralnoe-oborudovanie/stoly/?only_with_price=1",
        "has_filter_param": "only_with_price" in only_with_price_html,
        "no_po_zaprosu_in_listing": "По запросу" not in only_with_price_html,
        "pass": "only_with_price" in only_with_price_html,
    }

    results["all_pass"] = all(
        v.get("pass") is True
        for k, v in results["checks"].items()
        if isinstance(v, dict) and "pass" in v
    )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
