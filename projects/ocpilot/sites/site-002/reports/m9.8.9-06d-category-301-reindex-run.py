#!/usr/bin/env python3
"""M9.8.9-06D — category 301 price index rebuild via refreshPriceIndex()."""
from __future__ import annotations

import ftplib
import hashlib
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

BASE_URL = "https://zpm.new-site.space"
PLP_URL = BASE_URL + "/katalog/nejtralnoe-oborudovanie/stoly/"
PMA = "https://bruma.beget.com/phpMyAdmin"
DB = "polygonws_zpm"
DB_USER = "polygonws_zpm"
DB_PASS = "VBCDry2bJ5P"
FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports")
WORK_DIR = ROOT / "m9.8.9-06d-work"
BACKUP_DIR = WORK_DIR / "live-capture"
VARIANT_JSON = ROOT / "m9.8.9-06c-audit-data" / "variant-c-301-clean.json"
RESULT_JSON = WORK_DIR / "run-results.json"
REMOTE_SCRIPT = "reindex_prices_301_m98906d.php"

BACKUP_FILES = [
    "catalog/model/catalog/product.php",
    "catalog/controller/common/import_1C_offers.php",
    "admin/model/catalog/product.php",
    "reindex_prices.php",
]

COVERAGE_SQL = """
SELECT
  COUNT(DISTINCT p.product_id) AS active_products,
  COUNT(DISTINCT ppi.product_id) AS indexed_products,
  ROUND(100.0 * COUNT(DISTINCT ppi.product_id) / NULLIF(COUNT(DISTINCT p.product_id), 0), 2) AS coverage_pct
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = 301
INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
LEFT JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
WHERE p.status = 1 AND p.date_available <= NOW()
"""

PRICE_RANGE_SQL = """
SELECT
  MIN(IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)) AS min_price,
  MAX(IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)) AS max_price
FROM oc_product p
INNER JOIN oc_product_to_category p2c ON p.product_id = p2c.product_id
INNER JOIN oc_category_path cp ON p2c.category_id = cp.category_id AND cp.path_id = 301
INNER JOIN oc_product_to_store p2s ON p.product_id = p2s.product_id AND p2s.store_id = 0
INNER JOIN oc_product_price_index ppi ON p.product_id = ppi.product_id AND ppi.customer_group_id = 2
WHERE p.status = 1 AND p.date_available <= NOW()
"""


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_connect() -> ftplib.FTP:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_download(remote_path: str) -> bytes | None:
    try:
        ftp = ftp_connect()
        bio = io.BytesIO()
        ftp.retrbinary("RETR " + remote_path, bio.write)
        ftp.quit()
        return bio.getvalue()
    except Exception:
        return None


def ftp_upload(remote_path: str, data: bytes) -> None:
    ftp = ftp_connect()
    bio = io.BytesIO(data)
    ftp.storbinary("STOR " + remote_path, bio)
    ftp.quit()


def ftp_delete(remote_path: str) -> bool:
    try:
        ftp = ftp_connect()
        ftp.delete(remote_path)
        ftp.quit()
        return True
    except Exception:
        return False


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


def fetch_plp_price_range(html_out: Path | None = None) -> dict:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        PLP_URL,
        headers={"User-Agent": "MARS-M9.8.9-06D/1.0"},
    )
    html = urllib.request.urlopen(req, timeout=120, context=ctx).read().decode("utf-8", "replace")
    if html_out:
        html_out.write_text(html, encoding="utf-8")
    out = {"url": PLP_URL, "fetched_at": datetime.now(timezone.utc).isoformat()}
    m_min = re.search(r'data-range-min[^>]*min="(\d+)"[^>]*max="(\d+)"', html)
    m_max = re.search(r'data-range-max[^>]*min="(\d+)"[^>]*max="(\d+)"', html)
    m_from = re.search(r'name="price_from"[^>]*placeholder="(\d+)"', html)
    if m_min:
        out["slider_min"] = int(m_min.group(1))
        out["slider_max"] = int(m_min.group(2))
    if m_from:
        out["placeholder_from"] = int(m_from.group(1))
    if m_max:
        out["range_max_value"] = int(m_max.group(2))
    out["degenerate"] = out.get("slider_min") == out.get("slider_max") or (
        out.get("slider_max", 0) - out.get("slider_min", 0) < 1000
    )
    return out


def build_reindex_php(product_ids: list[int], token: str) -> str:
    ids_php = ", ".join(str(i) for i in product_ids)
    return """<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
set_time_limit(0);
ini_set('memory_limit', '512M');

if (!isset($_GET['token']) || $_GET['token'] !== '%(token)s') {
    http_response_code(403);
    die('Forbidden');
}

require_once('config.php');
require_once(DIR_SYSTEM . 'startup.php');

$registry = new Registry();
$db = new DB(DB_DRIVER, DB_HOSTNAME, DB_USERNAME, DB_PASSWORD, DB_DATABASE, DB_PORT);
$registry->set('db', $db);
$config = new Config();
$registry->set('config', $config);
require_once(DIR_SYSTEM . 'engine/model.php');

$admin_model_path = __DIR__ . '/admin/model/catalog/product.php';
if (file_exists($admin_model_path)) {
    require_once($admin_model_path);
} else {
    require_once(__DIR__ . '/catalog/model/catalog/product.php');
}

$model = new ModelCatalogProduct($registry);
if (!method_exists($model, 'refreshPriceIndex')) {
    die("Error: refreshPriceIndex not found\\n");
}

$product_ids = array(%(ids)s);
echo "M9.8.9-06D category 301 rebuild\\n";
echo "Products to process: " . count($product_ids) . "\\n";

$ok = 0;
$fail = 0;
foreach ($product_ids as $product_id) {
    echo "Processing ID: " . $product_id . "... ";
    try {
        $model->refreshPriceIndex((int)$product_id);
        echo "OK\\n";
        $ok++;
    } catch (Throwable $e) {
        echo "FAIL: " . $e->getMessage() . "\\n";
        $fail++;
    }
    flush();
}

echo "--- Done ---\\n";
echo "OK: " . $ok . ", FAIL: " . $fail . "\\n";
""" % {"token": token, "ids": ids_php}


def main():
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    token = f"m98906d-301-{stamp}"
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    WORK_DIR.mkdir(parents=True, exist_ok=True)

    results = {
        "task": "M9.8.9-06D",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "authority": "SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01",
        "errors": [],
    }

    # --- Backup ---
    manifest_files = {}
    for rel in BACKUP_FILES:
        raw = ftp_download(rel)
        if not raw:
            results["errors"].append(f"backup_failed: {rel}")
            continue
        local_name = rel.replace("/", "__")
        out_path = BACKUP_DIR / local_name
        out_path.write_bytes(raw)
        manifest_files[rel] = {
            "local": str(out_path),
            "sha256": sha256_hex(raw),
            "size": len(raw),
        }

    manifest = {
        "task": "M9.8.9-06D",
        "stamp": stamp,
        "files": manifest_files,
        "rollback_note": "No site files modified; only temporary reindex script deployed and removed.",
    }
    manifest_path = WORK_DIR / f"manifest-{stamp}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    results["backup"] = {"manifest": str(manifest_path), "files": list(manifest_files.keys())}

    # --- Load SKU list ---
    variant = json.loads(VARIANT_JSON.read_text(encoding="utf-8"))
    product_ids = [int(x["product_id"]) for x in variant if x.get("has_index") == "no"]
    results["products_to_process"] = len(product_ids)
    results["product_ids_sample"] = product_ids[:5]

    # --- Before metrics ---
    try:
        op, csrf = pma_session()
        results["coverage_before"] = pma_sql(op, csrf, COVERAGE_SQL)
        results["price_range_db_before"] = pma_sql(op, csrf, PRICE_RANGE_SQL)
    except Exception as e:
        results["errors"].append(f"before_sql: {e}")

    try:
        results["plp_before"] = fetch_plp_price_range(WORK_DIR / "plp-stoly-before.html")
    except Exception as e:
        results["errors"].append(f"plp_before: {e}")

    # --- Deploy & run rebuild ---
    php_source = build_reindex_php(product_ids, token)
    php_path = WORK_DIR / REMOTE_SCRIPT
    php_path.write_text(php_source, encoding="utf-8")
    results["rebuild_method"] = {
        "mechanism": "refreshPriceIndex(product_id) via admin/model/catalog/product.php",
        "pattern": "adapted from live reindex_prices.php",
        "remote_script": REMOTE_SCRIPT,
        "direct_sql_insert": False,
    }

    run_output = ""
    rebuild_ok = False
    try:
        ftp_upload(REMOTE_SCRIPT, php_source.encode("utf-8"))
        run_url = BASE_URL + "/" + REMOTE_SCRIPT + "?" + urllib.parse.urlencode({"token": token})
        ctx = ssl.create_default_context()
        req = urllib.request.Request(run_url, headers={"User-Agent": "MARS-M9.8.9-06D/1.0"})
        run_output = urllib.request.urlopen(req, timeout=900, context=ctx).read().decode("utf-8", "replace")
        (WORK_DIR / "reindex-run-output.txt").write_text(run_output, encoding="utf-8")
        rebuild_ok = "Done" in run_output and "FAIL:" not in run_output.split("Done")[0][-500:]
        m_ok = re.search(r"OK:\s*(\d+),\s*FAIL:\s*(\d+)", run_output)
        if m_ok:
            results["rebuild_counts"] = {"ok": int(m_ok.group(1)), "fail": int(m_ok.group(2))}
        results["rebuild_output_tail"] = run_output[-2000:]
    except Exception as e:
        results["errors"].append(f"rebuild_run: {e}")
    finally:
        deleted = ftp_delete(REMOTE_SCRIPT)
        results["remote_script_removed"] = deleted

    results["rebuild_executed"] = rebuild_ok

    # --- After metrics ---
    try:
        op, csrf = pma_session()
        results["coverage_after"] = pma_sql(op, csrf, COVERAGE_SQL)
        results["price_range_db_after"] = pma_sql(op, csrf, PRICE_RANGE_SQL)
    except Exception as e:
        results["errors"].append(f"after_sql: {e}")

    try:
        results["plp_after"] = fetch_plp_price_range(WORK_DIR / "plp-stoly-after.html")
    except Exception as e:
        results["errors"].append(f"plp_after: {e}")

    # --- Slider / filter verification ---
    before = results.get("plp_before", {})
    after = results.get("plp_after", {})
    results["slider_verification"] = {
        "before_degenerate": before.get("degenerate"),
        "after_degenerate": after.get("degenerate"),
        "before_range": [before.get("slider_min"), before.get("slider_max")],
        "after_range": [after.get("slider_min"), after.get("slider_max")],
        "range_span_before": (before.get("slider_max") or 0) - (before.get("slider_min") or 0),
        "range_span_after": (after.get("slider_max") or 0) - (after.get("slider_min") or 0),
        "right_thumb_no_longer_collapsed": not after.get("degenerate", True),
    }

    RESULT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
