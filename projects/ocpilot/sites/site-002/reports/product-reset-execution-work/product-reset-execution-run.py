#!/usr/bin/env python3
"""SITE-002 product reset — EXECUTION (operator GO confirmed)."""
from __future__ import annotations

import ftplib
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

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

WORK = Path(__file__).resolve().parent
REPORTS = WORK.parent

DELETE_PHASES = [
    ("A", "oc_coupon_product", "DELETE FROM oc_coupon_product"),
    ("A", "oc_customer_wishlist", "DELETE FROM oc_customer_wishlist"),
    ("A", "oc_cart", "DELETE FROM oc_cart"),
    ("A", "oc_googleshopping_product", "DELETE FROM oc_googleshopping_product"),
    ("A", "oc_googleshopping_product_status", "DELETE FROM oc_googleshopping_product_status"),
    ("A", "oc_googleshopping_product_target", "DELETE FROM oc_googleshopping_product_target"),
    ("B", "oc_product_price_index", "DELETE FROM oc_product_price_index"),
    ("C", "oc_product_attribute", "DELETE FROM oc_product_attribute"),
    ("C", "oc_product_description", "DELETE FROM oc_product_description"),
    ("C", "oc_product_discount", "DELETE FROM oc_product_discount"),
    ("C", "oc_product_filter", "DELETE FROM oc_product_filter"),
    ("C", "oc_product_image", "DELETE FROM oc_product_image"),
    ("C", "oc_product_option_value", "DELETE FROM oc_product_option_value"),
    ("C", "oc_product_option", "DELETE FROM oc_product_option"),
    ("C", "oc_product_related", "DELETE FROM oc_product_related"),
    ("C", "oc_product_reward", "DELETE FROM oc_product_reward"),
    ("C", "oc_product_special", "DELETE FROM oc_product_special"),
    ("C", "oc_product_to_category", "DELETE FROM oc_product_to_category"),
    ("C", "oc_product_to_download", "DELETE FROM oc_product_to_download"),
    ("C", "oc_product_to_layout", "DELETE FROM oc_product_to_layout"),
    ("C", "oc_product_to_store", "DELETE FROM oc_product_to_store"),
    ("C", "oc_product_recurring", "DELETE FROM oc_product_recurring"),
    ("C", "oc_review", "DELETE FROM oc_review"),
    ("D", "oc_seo_url (product)", "DELETE FROM oc_seo_url WHERE query LIKE 'product_id=%'"),
    ("E", "oc_product", "DELETE FROM oc_product"),
]

PRE_COUNT_KEYS = {
    "oc_product": "SELECT COUNT(*) AS c FROM oc_product",
    "product_seo_urls": "SELECT COUNT(*) AS c FROM oc_seo_url WHERE query LIKE 'product_id=%'",
    "oc_product_attribute": "SELECT COUNT(*) AS c FROM oc_product_attribute",
    "oc_product_image": "SELECT COUNT(*) AS c FROM oc_product_image",
    "oc_product_price_index": "SELECT COUNT(*) AS c FROM oc_product_price_index",
}

POST_VERIFY = {
    "oc_product": "SELECT COUNT(*) AS c FROM oc_product",
    "oc_product_attribute": "SELECT COUNT(*) AS c FROM oc_product_attribute",
    "oc_product_price_index": "SELECT COUNT(*) AS c FROM oc_product_price_index",
    "product_seo_urls": "SELECT COUNT(*) AS c FROM oc_seo_url WHERE query LIKE 'product_id=%'",
    "seo_non_product": "SELECT COUNT(*) AS c FROM oc_seo_url WHERE query NOT LIKE 'product_id=%'",
    "oc_customer_wishlist": "SELECT COUNT(*) AS c FROM oc_customer_wishlist",
    "oc_cart": "SELECT COUNT(*) AS c FROM oc_cart",
    "oc_googleshopping_product": "SELECT COUNT(*) AS c FROM oc_googleshopping_product",
    "oc_category": "SELECT COUNT(*) AS c FROM oc_category",
    "oc_attribute": "SELECT COUNT(*) AS c FROM oc_attribute",
    "oc_filter_group": "SELECT COUNT(*) AS c FROM oc_filter_group",
    "oc_category_docs": "SELECT COUNT(*) AS c FROM oc_category_docs",
    "oc_setting": "SELECT COUNT(*) AS c FROM oc_setting",
    "oc_order": "SELECT COUNT(*) AS c FROM oc_order",
    "cron": "SELECT COUNT(*) AS c FROM cron",
}


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
    return op, re.search(r'name="token"\s+value="([^"]+)"', db_html).group(1)


def pma_sql(op, csrf, sql: str, timeout: int = 300) -> tuple[list[dict], str]:
    html = op.open(
        urllib.request.Request(
            PMA + "/sql.php",
            data=urllib.parse.urlencode(
                {"db": DB, "sql_query": sql, "token": csrf, "sql_delimiter": ";"}
            ).encode(),
            method="POST",
        ),
        timeout=timeout,
    ).read().decode("utf-8", "replace")
    if re.search(r"class=\"error\"|MySQL said:|#(\d{4})", html, re.I):
        err = re.search(r'<div class="error"><h1>[^<]*</h1>\s*(.*?)</div>', html, re.S)
        if err:
            snippet = unescape(re.sub(r"<[^>]+>", " ", err.group(1))).strip()[:500]
            return [], snippet
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
            return [dict(zip(h, r)) for r in parsed[1:] if len(r) == len(h)], ""
    return [], ""


def scalar(op, csrf, sql: str) -> str:
    rows, err = pma_sql(op, csrf, sql)
    if err:
        return f"ERROR:{err}"
    if not rows:
        return "ERROR"
    return str(next(iter(rows[0].values())))


def table_count(op, csrf, table: str) -> str:
    return scalar(op, csrf, f"SELECT COUNT(*) AS c FROM `{table}`")


def live_capture(op, csrf) -> dict:
    capture = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "db": DB,
        "site": "https://zpm.new-site.space/",
        "authority": "SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01",
        "pre_counts": {k: scalar(op, csrf, sql) for k, sql in PRE_COUNT_KEYS.items()},
        "preserved_baseline": {
            "oc_category": scalar(op, csrf, POST_VERIFY["oc_category"]),
            "oc_attribute": scalar(op, csrf, POST_VERIFY["oc_attribute"]),
            "oc_filter_group": scalar(op, csrf, POST_VERIFY["oc_filter_group"]),
            "oc_category_docs": scalar(op, csrf, POST_VERIFY["oc_category_docs"]),
            "seo_non_product": scalar(op, csrf, POST_VERIFY["seo_non_product"]),
            "oc_order": scalar(op, csrf, POST_VERIFY["oc_order"]),
            "cron": scalar(op, csrf, POST_VERIFY["cron"]),
        },
        "delete_targets": {},
    }
    for phase, label, _ in DELETE_PHASES:
        if label.startswith("oc_seo_url"):
            capture["delete_targets"][label] = scalar(
                op, csrf, "SELECT COUNT(*) AS c FROM oc_seo_url WHERE query LIKE 'product_id=%'"
            )
        elif label == "oc_product":
            capture["delete_targets"][label] = capture["pre_counts"]["oc_product"]
        else:
            tbl = label
            capture["delete_targets"][label] = table_count(op, csrf, tbl)
    return capture


def execute_deletes(op, csrf) -> dict:
    results = {"started_at": datetime.now(timezone.utc).isoformat(), "steps": [], "errors": []}
    for phase, label, sql in DELETE_PHASES:
        before = (
            scalar(op, csrf, "SELECT COUNT(*) AS c FROM oc_seo_url WHERE query LIKE 'product_id=%'")
            if label.startswith("oc_seo_url")
            else table_count(op, csrf, label) if label != "oc_product" else scalar(op, csrf, "SELECT COUNT(*) AS c FROM oc_product")
        )
        _, err = pma_sql(op, csrf, sql, timeout=600)
        after = (
            scalar(op, csrf, "SELECT COUNT(*) AS c FROM oc_seo_url WHERE query LIKE 'product_id=%'")
            if label.startswith("oc_seo_url")
            else table_count(op, csrf, label) if label != "oc_product" else scalar(op, csrf, "SELECT COUNT(*) AS c FROM oc_product")
        )
        step = {
            "phase": phase,
            "table": label,
            "sql": sql,
            "rows_before": before,
            "rows_after": after,
            "rows_deleted": str(int(before) - int(after)) if before.isdigit() and after.isdigit() else "UNKNOWN",
            "error": err or None,
        }
        results["steps"].append(step)
        if err:
            results["errors"].append({"table": label, "error": err})
            break
    results["completed_at"] = datetime.now(timezone.utc).isoformat()
    return results


def clear_opencart_cache() -> dict:
    cleared = []
    errors = []
    for cache_dir in ("system/storage/cache", "system/storage/cache/template"):
        ftp = ftplib.FTP(FTP_HOST, timeout=120)
        try:
            ftp.login(FTP_USER, FTP_PASS)
            ftp.cwd(cache_dir)
            entries = []
            ftp.retrlines("LIST", entries.append)
            for line in entries:
                parts = line.split(None, 8)
                if len(parts) < 9:
                    continue
                name = parts[8]
                if name in (".", "..", "index.html"):
                    continue
                if line.startswith("d"):
                    continue
                try:
                    ftp.delete(name)
                    cleared.append(f"{cache_dir}/{name}")
                except ftplib.error_perm as e:
                    errors.append(f"{cache_dir}/{name}: {e}")
        except Exception as e:
            errors.append(f"{cache_dir}: {e}")
        finally:
            try:
                ftp.quit()
            except Exception:
                pass
    return {"cleared_count": len(cleared), "cleared_sample": cleared[:40], "errors": errors}


def main():
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    op, csrf = pma_session()

    pre_capture = live_capture(op, csrf)
    pre_path = WORK / f"pre-capture-{ts}.json"
    pre_path.write_text(json.dumps(pre_capture, ensure_ascii=False, indent=2), encoding="utf-8")

    manifest = {
        "manifest_id": f"product-reset-execution-{ts}",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "authority": "SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01",
        "operator_approval": "GO CONFIRMED",
        "beget_backup": "CONFIRMED",
        "physical_images_policy": "DO NOT DELETE",
        "dry_run_reference": "SITE-002-PRODUCT-RESET-DRY-RUN-FINAL.md",
        "database": DB,
        "site_url": "https://zpm.new-site.space/",
        "pre_capture_file": pre_path.name,
        "pre_counts": pre_capture["pre_counts"],
        "delete_plan": [
            {"phase": p, "table": t, "expected_rows": pre_capture["delete_targets"].get(t)}
            for p, t, _ in DELETE_PHASES
        ],
    }
    manifest_path = WORK / f"manifest-{ts}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    delete_results = execute_deletes(op, csrf)
    delete_path = WORK / f"delete-results-{ts}.json"
    delete_path.write_text(json.dumps(delete_results, ensure_ascii=False, indent=2), encoding="utf-8")

    post_verify = {k: scalar(op, csrf, sql) for k, sql in POST_VERIFY.items()}
    post_path = WORK / f"post-verify-{ts}.json"
    post_path.write_text(json.dumps(post_verify, ensure_ascii=False, indent=2), encoding="utf-8")

    cache_result = clear_opencart_cache() if not delete_results["errors"] else {
        "skipped": True,
        "reason": "delete errors present",
    }
    cache_path = WORK / f"cache-clear-{ts}.json"
    cache_path.write_text(json.dumps(cache_result, ensure_ascii=False, indent=2), encoding="utf-8")

    total_deleted = sum(
        int(s["rows_deleted"])
        for s in delete_results["steps"]
        if str(s.get("rows_deleted", "")).isdigit()
    )

    ready = (
        not delete_results["errors"]
        and post_verify.get("oc_product") == "0"
        and post_verify.get("product_seo_urls") == "0"
        and post_verify.get("oc_product_price_index") == "0"
        and post_verify.get("oc_customer_wishlist") == "0"
        and post_verify.get("oc_cart") == "0"
        and post_verify.get("oc_googleshopping_product") == "0"
        and int(post_verify.get("oc_category", "0")) > 0
        and int(post_verify.get("oc_attribute", "0")) > 0
    )

    run_summary = {
        "timestamp": ts,
        "manifest": manifest_path.name,
        "pre_capture": pre_path.name,
        "delete_results": delete_path.name,
        "post_verify": post_path.name,
        "cache_clear": cache_path.name,
        "total_rows_deleted": total_deleted,
        "execution_errors": delete_results["errors"],
        "ready_for_clean_1c_import": ready,
        "post_verify": post_verify,
        "cache_result": cache_result,
    }
    summary_path = WORK / f"run-summary-{ts}.json"
    summary_path.write_text(json.dumps(run_summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(run_summary, ensure_ascii=False, indent=2))
    return run_summary, ts, delete_results, pre_capture, post_verify, cache_result, ready


if __name__ == "__main__":
    main()
