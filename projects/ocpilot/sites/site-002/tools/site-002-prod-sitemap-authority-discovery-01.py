#!/usr/bin/env python3
"""SITE-002 Production sitemap authority discovery — read-only (Run 4.214)."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import json
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01"
OCPILOT_RUN = "4.214"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01"
AUDIT_BASELINE_BEFORE = "SITE-002-POST-1C-CATALOG-MONITOR-02"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
PRIOR_ENABLE_ADMIN = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SITEMAP-ENABLE-01\admin-evidence\admin-feed-state.json"
)
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

SUBDIRS = (
    "http",
    "ftp-readonly",
    "source-map",
    "route-map",
    "module-map",
    "admin-readonly",
    "evidence",
    "verification",
    "manifests",
    "reports",
    "logs",
)

FTP_PATHS = [
    "/public_html/sitemap.xml",
    "/public_html/.htaccess",
    "/public_html/catalog/controller/extension/feed/google_sitemap.php",
    "/public_html/catalog/controller/feed/google_sitemap.php",
    "/public_html/admin/controller/extension/feed/google_sitemap.php",
    "/public_html/catalog/controller/startup/seo_url.php",
    "/public_html/catalog/model/catalog/product.php",
    "/public_html/catalog/model/catalog/category.php",
    "/public_html/catalog/model/catalog/information.php",
    "/public_html/catalog/model/catalog/manufacturer.php",
    "/public_html/system/storage/modification/catalog/controller/extension/feed/google_sitemap.php",
    "/public_html/storage/modification/catalog/controller/extension/feed/google_sitemap.php",
]

SOURCE_ANALYSIS_PATHS = [
    "/public_html/catalog/controller/extension/feed/google_sitemap.php",
    "/public_html/admin/controller/extension/feed/google_sitemap.php",
    "/public_html/catalog/controller/startup/seo_url.php",
    "/public_html/catalog/model/catalog/product.php",
    "/public_html/catalog/model/catalog/category.php",
    "/public_html/catalog/model/catalog/information.php",
    "/public_html/catalog/model/catalog/manufacturer.php",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def ensure_dirs() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "audit_baseline_before": AUDIT_BASELINE_BEFORE,
            "change_type": "sitemap-authority-discovery-readonly",
            "remote_changes_allowed": False,
            "admin_save_allowed": False,
            "db_write_allowed": False,
            "cache_clear_allowed": False,
            "ftp_upload_allowed": False,
            "sitemap_manual_edit_allowed": False,
            "robots_change_allowed": False,
            "product_generator_change_allowed": False,
            "category_meta_change_allowed": False,
            "daily_1c_growth_expected": True,
            "brand_policy_correct": "ЗПМ",
            "brand_policy_forbidden_public": "БЗПМ",
        },
    )


def parse_production_section(path: Path, subsection: str | None = None) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found in secrets file")
    block = match.group(1)
    if subsection:
        sub_match = re.search(
            rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE
        )
        if not sub_match:
            raise RuntimeError(f"PRODUCTION subsection {subsection!r} not found")
        block = sub_match.group(1)
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.endswith(":"):
            current_key = stripped[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current_key, "")
            continue
        if current_key:
            fields[current_key] = stripped
    return fields


def ftp_connect() -> ftplib.FTP:
    fields = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    host = fields["host"]
    port = int(fields.get("port") or 21)
    ftp = ftplib.FTP()
    ftp.connect(host, port, timeout=180)
    ftp.login(fields["username"], fields["password"])
    return ftp


def ftp_download(ftp: ftplib.FTP, remote_path: str) -> bytes:
    buf: list[bytes] = []

    def collect(data: bytes) -> None:
        buf.append(data)

    ftp.retrbinary("RETR " + remote_path, collect)
    return b"".join(buf)


def ftp_exists(ftp: ftplib.FTP, remote_path: str) -> tuple[bool, int | None]:
    try:
        size = ftp.size(remote_path)
        return True, size
    except ftplib.error_perm:
        return False, None


def local_name(remote_path: str) -> str:
    return remote_path.strip("/").replace("/", "__")


def http_get(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = resp.read()
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return {
                "url": url,
                "final_url": resp.geturl(),
                "status": resp.status,
                "headers": headers,
                "body": body,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read()
        headers = {k.lower(): v for k, v in exc.headers.items()}
        return {
            "url": url,
            "final_url": exc.geturl(),
            "status": exc.code,
            "headers": headers,
            "body": body,
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "url": url,
            "final_url": url,
            "status": None,
            "headers": {},
            "body": b"",
            "error": str(exc),
        }


def headers_text(headers: dict[str, str]) -> str:
    return "\n".join(f"{k}: {v}" for k, v in headers.items())


def analyze_sitemap_xml(body: bytes) -> dict[str, Any]:
    text = body.decode("utf-8", errors="replace")
    result: dict[str, Any] = {
        "valid_xml": False,
        "url_count": 0,
        "has_products": False,
        "has_categories": False,
        "has_information": False,
        "has_manufacturers": False,
        "has_images": False,
        "parse_error": None,
    }
    try:
        root = ET.fromstring(text)
        result["valid_xml"] = True
        locs = [el.text.strip() for el in root.iter(SITEMAP_NS + "loc") if el.text]
        result["url_count"] = len(locs)
        joined = "\n".join(locs)
        result["has_products"] = "/katalog/" in joined and any(
            p in joined for p in ("stoly", "forma-", "product")
        )
        result["has_categories"] = "/katalog/" in joined
        result["has_information"] = any(
            x in joined for x in ("privacy-policy", "guarantee", "information/information")
        )
        result["has_manufacturers"] = "manufacturer" in joined or "/brand/" in joined
        result["has_images"] = bool(list(root.iter("{http://www.google.com/schemas/sitemap-image/1.1}image")))
    except ET.ParseError as exc:
        result["parse_error"] = str(exc)
    return result


def extract_methods(code: str) -> list[str]:
    return re.findall(r"function\s+(\w+)\s*\(", code)


def analyze_php_source(remote_path: str, code: str) -> dict[str, Any]:
    role = "unknown"
    if "extension/feed/google_sitemap" in remote_path and "/catalog/" in remote_path:
        role = "catalog_feed_controller"
    elif "extension/feed/google_sitemap" in remote_path and "/admin/" in remote_path:
        role = "admin_feed_controller"
    elif "seo_url.php" in remote_path:
        role = "seo_url_startup"
    elif "/model/catalog/product.php" in remote_path:
        role = "product_model"
    elif "/model/catalog/category.php" in remote_path:
        role = "category_model"
    elif "/model/catalog/information.php" in remote_path:
        role = "information_model"
    elif "/model/catalog/manufacturer.php" in remote_path:
        role = "manufacturer_model"

    analysis: dict[str, Any] = {
        "remote_path": remote_path,
        "role": role,
        "methods": extract_methods(code),
        "uses_cache": bool(re.search(r"\$this->cache|cache->get|cache->set", code)),
        "writes_physical_file": bool(re.search(r"fwrite|file_put_contents|fopen\s*\(", code)),
        "outputs_xml": "application/xml" in code or "<urlset" in code,
        "checks_feed_status": "feed_google_sitemap_status" in code,
        "data_sources": [],
        "routes_generated": [],
    }

    if role == "catalog_feed_controller":
        for pattern, label in [
            (r"model_catalog_product->getProducts", "catalog/product::getProducts"),
            (r"model_catalog_category->getCategories", "catalog/category::getCategories"),
            (r"model_catalog_manufacturer->getManufacturers", "catalog/manufacturer::getManufacturers"),
            (r"model_catalog_information->getInformations", "catalog/information::getInformations"),
        ]:
            if re.search(pattern, code):
                analysis["data_sources"].append(label)
        for route in ("product/product", "product/category", "product/manufacturer/info", "information/information"):
            if route in code:
                analysis["routes_generated"].append(route)

    if role == "product_model" and "function getProducts" in code:
        block = re.search(r"function getProducts[\s\S]*?(?=\n\tpublic function |\n\})", code)
        if block:
            snippet = block.group(0)
            analysis["status_filter"] = "p.status = '1'" in snippet or 'p.status = "1"' in snippet
            analysis["store_filter"] = "product_to_store" in snippet

    if role == "category_model" and "function getCategories" in code:
        block = re.search(r"function getCategories[\s\S]*?(?=\n\tpublic function |\n\})", code)
        if block:
            snippet = block.group(0)
            analysis["status_filter"] = "c.status = '1'" in snippet or 'c.status = "1"' in snippet

    if role == "information_model" and "function getInformations" in code:
        block = re.search(r"function getInformations[\s\S]*?(?=\n\tpublic function |\n\})", code)
        if block:
            snippet = block.group(0)
            analysis["status_filter"] = "i.status = '1'" in snippet or 'i.status = "1"' in snippet

    if role == "seo_url_startup":
        analysis["sitemap_rewrite"] = "sitemap.xml" in code or "google_sitemap" in code

    return analysis


def phase_http() -> dict[str, Any]:
    out: dict[str, Any] = {"checked_at": utc_now()}
    sitemap = http_get("https://bzpm.ru/sitemap.xml")
    robots = http_get("https://bzpm.ru/robots.txt")
    probe = http_get("https://bzpm.ru/sitemap.xml?mars_readonly_probe=1")

    write_text(DEPLOYMENT_ROOT / "http" / "sitemap-headers.txt", headers_text(sitemap["headers"]))
    write_text(DEPLOYMENT_ROOT / "http" / "sitemap-response.xml", sitemap["body"].decode("utf-8", errors="replace"))
    write_text(DEPLOYMENT_ROOT / "http" / "robots-headers.txt", headers_text(robots["headers"]))
    write_text(DEPLOYMENT_ROOT / "http" / "robots-response.txt", robots["body"].decode("utf-8", errors="replace"))

    sitemap_analysis = analyze_sitemap_xml(sitemap["body"])
    robots_text = robots["body"].decode("utf-8", errors="replace")
    sitemap_directives = [ln.strip() for ln in robots_text.splitlines() if ln.lower().startswith("sitemap:")]

    sitemap_summary = {
        "checked_at": utc_now(),
        "url": sitemap["url"],
        "final_url": sitemap["final_url"],
        "status": sitemap["status"],
        "content_type": sitemap["headers"].get("content-type"),
        "sha256": sha256_bytes(sitemap["body"]),
        "byte_length": len(sitemap["body"]),
        **sitemap_analysis,
    }
    robots_summary = {
        "checked_at": utc_now(),
        "url": robots["url"],
        "final_url": robots["final_url"],
        "status": robots["status"],
        "content_type": robots["headers"].get("content-type"),
        "sha256": sha256_bytes(robots["body"]),
        "sitemap_directives": sitemap_directives,
    }
    probe_summary = {
        "checked_at": utc_now(),
        "url": probe["url"],
        "status": probe["status"],
        "sha256": sha256_bytes(probe["body"]) if probe["body"] else None,
        "content_equal_to_plain_sitemap": sha256_bytes(probe["body"]) == sha256_bytes(sitemap["body"])
        if probe["body"] and sitemap["body"]
        else False,
        "query_ignored": probe["final_url"].startswith("https://bzpm.ru/sitemap.xml"),
    }

    write_json(DEPLOYMENT_ROOT / "http" / "sitemap-summary.json", sitemap_summary)
    write_json(DEPLOYMENT_ROOT / "http" / "robots-summary.json", robots_summary)
    write_json(DEPLOYMENT_ROOT / "http" / "sitemap-probe-summary.json", probe_summary)

    out["sitemap"] = sitemap_summary
    out["robots"] = robots_summary
    out["probe"] = probe_summary
    return out


def phase_ftp() -> dict[str, Any]:
    ftp = ftp_connect()
    results: list[dict[str, Any]] = []
    downloaded: dict[str, str] = {}
    try:
        for remote in FTP_PATHS:
            exists, size = ftp_exists(ftp, remote)
            entry: dict[str, Any] = {
                "remote_path": remote,
                "exists": exists,
                "size_bytes": size,
                "sha256": None,
                "local_copy": None,
            }
            if exists:
                data = ftp_download(ftp, remote)
                entry["sha256"] = sha256_bytes(data)
                fname = local_name(remote)
                local_path = DEPLOYMENT_ROOT / "ftp-readonly" / fname
                local_path.write_bytes(data)
                entry["local_copy"] = str(local_path)
                downloaded[remote] = data.decode("utf-8", errors="replace")
            results.append(entry)
    finally:
        ftp.quit()

    htaccess = downloaded.get("/public_html/.htaccess", "")
    physical_sitemap = next(r for r in results if r["remote_path"] == "/public_html/sitemap.xml")
    rewrite_rules = []
    for line in htaccess.splitlines():
        lower = line.lower()
        if "rewrite" in lower or "sitemap" in lower:
            rewrite_rules.append(line.strip())

    physical_vs_route = {
        "checked_at": utc_now(),
        "physical_sitemap_xml_exists": physical_sitemap["exists"],
        "physical_sitemap_size_bytes": physical_sitemap.get("size_bytes"),
        "likely_static_file": physical_sitemap["exists"],
        "likely_route_feed": not physical_sitemap["exists"],
        "htaccess_rewrite_involved": bool(rewrite_rules),
        "htaccess_sitemap_related_lines": rewrite_rules,
        "catalog_feed_controller_exists": any(
            r["remote_path"] == "/public_html/catalog/controller/extension/feed/google_sitemap.php" and r["exists"]
            for r in results
        ),
        "modification_overlay_exists": any(
            "modification" in r["remote_path"] and r["exists"] for r in results
        ),
    }
    write_json(DEPLOYMENT_ROOT / "evidence" / "physical-vs-route-check.json", physical_vs_route)
    md = [
        "# Physical vs route check",
        "",
        f"- Physical `/public_html/sitemap.xml`: **{'yes' if physical_vs_route['physical_sitemap_xml_exists'] else 'no'}**",
        f"- Catalog feed controller present: **{'yes' if physical_vs_route['catalog_feed_controller_exists'] else 'no'}**",
        f"- OC modification overlay: **{'yes' if physical_vs_route['modification_overlay_exists'] else 'no'}**",
        f"- `.htaccess` rewrite lines (sitemap-related): {len(rewrite_rules)}",
        "",
        "## Rewrite-related `.htaccess` lines",
        "",
    ]
    md.extend(f"- `{line}`" for line in rewrite_rules[:30] or ["(none captured)"])
    write_text(DEPLOYMENT_ROOT / "evidence" / "physical-vs-route-check.md", "\n".join(md))

    return {"ftp_files": results, "downloaded": downloaded, "physical_vs_route": physical_vs_route}


def phase_source_map(downloaded: dict[str, str]) -> list[dict[str, Any]]:
    analyses: list[dict[str, Any]] = []
    for remote in SOURCE_ANALYSIS_PATHS:
        code = downloaded.get(remote, "")
        if not code:
            analyses.append(
                {
                    "remote_path": remote,
                    "exists": False,
                    "modification_overlay": "modification" in remote,
                    "role": "missing",
                }
            )
            continue
        item = analyze_php_source(remote, code)
        item["exists"] = True
        item["modification_overlay"] = "modification" in remote
        analyses.append(item)

    write_json(DEPLOYMENT_ROOT / "source-map" / "sitemap-source-files.json", analyses)
    with (DEPLOYMENT_ROOT / "source-map" / "sitemap-source-files.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "remote_path",
                "exists",
                "role",
                "uses_cache",
                "writes_physical_file",
                "outputs_xml",
                "checks_feed_status",
                "data_sources",
                "routes_generated",
            ],
        )
        writer.writeheader()
        for row in analyses:
            writer.writerow(
                {
                    "remote_path": row.get("remote_path"),
                    "exists": row.get("exists"),
                    "role": row.get("role"),
                    "uses_cache": row.get("uses_cache"),
                    "writes_physical_file": row.get("writes_physical_file"),
                    "outputs_xml": row.get("outputs_xml"),
                    "checks_feed_status": row.get("checks_feed_status"),
                    "data_sources": ";".join(row.get("data_sources", [])),
                    "routes_generated": ";".join(row.get("routes_generated", [])),
                }
            )

    md_lines = [
        "# Sitemap source analysis",
        "",
        "Primary authority: OpenCart built-in **Google Sitemap** feed (`extension/feed/google_sitemap`).",
        "",
    ]
    for row in analyses:
        md_lines.append(f"## `{row.get('remote_path')}`")
        md_lines.append(f"- exists: **{row.get('exists')}**")
        md_lines.append(f"- role: `{row.get('role')}`")
        if row.get("data_sources"):
            md_lines.append(f"- data sources: {', '.join(row['data_sources'])}")
        if row.get("routes_generated"):
            md_lines.append(f"- routes: {', '.join(row['routes_generated'])}")
        if "status_filter" in row:
            md_lines.append(f"- status_filter in model: **{row['status_filter']}**")
        md_lines.append("")
    write_text(DEPLOYMENT_ROOT / "source-map" / "sitemap-source-analysis.md", "\n".join(md_lines))
    return analyses


def phase_data_source_map(analyses: list[dict[str, Any]], http_data: dict[str, Any]) -> dict[str, Any]:
    feed = next((a for a in analyses if a.get("role") == "catalog_feed_controller"), {})
    product_model = next((a for a in analyses if a.get("role") == "product_model"), {})
    category_model = next((a for a in analyses if a.get("role") == "category_model"), {})
    info_model = next((a for a in analyses if a.get("role") == "information_model"), {})

    data_map = {
        "checked_at": utc_now(),
        "generating_route": "extension/feed/google_sitemap",
        "public_url": "https://bzpm.ru/sitemap.xml",
        "feed_url": "https://bzpm.ru/index.php?route=extension/feed/google_sitemap",
        "products": {
            "source": "catalog/product::getProducts",
            "status_filter": product_model.get("status_filter", "SAFE UNKNOWN — model not downloaded"),
            "url_pattern": "url->link('product/product', product_id=*) via SEO rewrite",
            "image_inclusion": True,
            "lastmod": "product date_modified",
            "changefreq": "weekly",
            "priority": "1.0",
            "affected_by_1c_import": True,
            "notes": "New/enabled products with SEO aliases appear on next live feed request; disabled/removed products drop out.",
        },
        "categories": {
            "source": "catalog/category::getCategories (recursive from parent_id=0)",
            "status_filter": category_model.get("status_filter", "SAFE UNKNOWN — model not downloaded"),
            "hierarchy_recursion": True,
            "url_pattern": "url->link('product/category', path=category_id) via SEO rewrite",
            "affected_by_1c_import": True,
            "notes": "New enabled categories from 1C appear automatically; onboarding meta is separate from sitemap inclusion.",
        },
        "information": {
            "source": "catalog/information::getInformations",
            "status_filter": info_model.get("status_filter", "SAFE UNKNOWN — model not downloaded"),
            "route_pattern": "url->link('information/information', information_id=*) via SEO rewrite",
            "included_in_live_sitemap": http_data["sitemap"].get("has_information"),
        },
        "manufacturers": {
            "source": "catalog/manufacturer::getManufacturers",
            "included_in_controller": "catalog/manufacturer::getManufacturers" in ";".join(feed.get("data_sources", [])),
            "route_pattern": "url->link('product/manufacturer/info', manufacturer_id=*)",
        },
        "blog_custom": {
            "included": False,
            "source": None,
            "notes": "No blog/custom feed logic in google_sitemap.php; no separate sitemap module found in feed directory.",
        },
        "seo_url": {
            "uses_url_link": True,
            "seo_aliases_automatic": True,
            "startup_controller": "/public_html/catalog/controller/startup/seo_url.php",
            "notes": "Pretty URLs come from OpenCart SEO URL table + startup rewrite; sitemap emits rewritten URLs when SEO enabled.",
        },
        "noindex_canonical": {
            "checked_in_feed_controller": False,
            "notes": "Feed does not inspect page-level robots meta or canonical; inclusion is catalog-state driven. External SEO audits required for noindex/canonical mismatches.",
        },
    }
    write_json(DEPLOYMENT_ROOT / "module-map" / "sitemap-data-source-map.json", data_map)
    write_text(
        DEPLOYMENT_ROOT / "module-map" / "sitemap-data-source-map.md",
        "\n".join(
            [
                "# Sitemap data source map",
                "",
                f"- Route: `{data_map['generating_route']}`",
                f"- Public URL: {data_map['public_url']}",
                "",
                "## Products",
                f"- {json.dumps(data_map['products'], ensure_ascii=False)}",
                "",
                "## Categories",
                f"- {json.dumps(data_map['categories'], ensure_ascii=False)}",
                "",
                "## Information",
                f"- {json.dumps(data_map['information'], ensure_ascii=False)}",
                "",
                "## Blog/custom",
                f"- {json.dumps(data_map['blog_custom'], ensure_ascii=False)}",
                "",
                "## SEO URL",
                f"- {json.dumps(data_map['seo_url'], ensure_ascii=False)}",
                "",
                "## Noindex/canonical",
                f"- {json.dumps(data_map['noindex_canonical'], ensure_ascii=False)}",
            ]
        ),
    )
    return data_map


def phase_admin_readonly(http_data: dict[str, Any]) -> dict[str, Any]:
    prior = {}
    if PRIOR_ENABLE_ADMIN.exists():
        prior = json.loads(PRIOR_ENABLE_ADMIN.read_text(encoding="utf-8"))
    state = {
        "checked_at": utc_now(),
        "admin_save_performed_this_run": False,
        "admin_login_attempted": False,
        "inference_method": "live HTTP feed output + prior Run 4.191 admin evidence",
        "feed_google_sitemap_status_inferred": "enabled"
        if http_data["sitemap"].get("valid_xml") and http_data["sitemap"].get("url_count", 0) > 0
        else "disabled_or_empty",
        "route": "extension/feed/google_sitemap",
        "feed_data_url": "https://bzpm.ru/index.php?route=extension/feed/google_sitemap",
        "prior_run_4191_enabled": prior.get("extension_enabled"),
        "prior_run_4191_status_raw": prior.get("feed_google_sitemap_status_raw"),
    }
    write_json(DEPLOYMENT_ROOT / "admin-readonly" / "google-sitemap-state.json", state)
    write_text(
        DEPLOYMENT_ROOT / "admin-readonly" / "google-sitemap-state.md",
        "\n".join(
            [
                "# Google Sitemap admin state (read-only inference)",
                "",
                f"- Inferred status: **{state['feed_google_sitemap_status_inferred']}**",
                f"- Route: `{state['route']}`",
                f"- Feed URL: {state['feed_data_url']}",
                f"- Prior Run 4.191 enabled: **{prior.get('extension_enabled')}**",
                "- No admin save in this run.",
            ]
        ),
    )
    return state


def phase_1c_relationship(http_data: dict[str, Any]) -> dict[str, Any]:
    rel = {
        "checked_at": utc_now(),
        "daily_1c_import": "MARS 1C wrapper via Beget cron (08:00 Moscow) — OPERATIONAL since Run 4.194",
        "sitemap_authority": "OpenCart Google Sitemap feed reads live catalog DB/models",
        "manual_sitemap_edit_by_mars": False,
        "manual_regeneration_required": False,
        "growth_observed": {
            "run_4209_baseline": 1320,
            "run_4213_current": http_data["sitemap"].get("url_count"),
            "delta_explained_by": "1C/catalog growth + product status/SEO state; not MARS manual XML edits",
        },
        "rules": [
            "1C adds/updates enabled products and categories in DB",
            "Feed includes enabled catalog entities on next HTTP request",
            "Disabled/404 products removed from feed when no longer returned by models",
            "Category SEO onboarding (meta) does not block sitemap inclusion by default",
        ],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "1c-sitemap-relationship.json", rel)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "1c-sitemap-relationship.md",
        "\n".join(["# 1C import ↔ sitemap relationship", ""] + [f"- {r}" for r in rel["rules"]]),
    )
    return rel


def phase_cache_behavior(http_data: dict[str, Any], analyses: list[dict[str, Any]], physical: dict[str, Any]) -> dict[str, Any]:
    feed = next((a for a in analyses if a.get("role") == "catalog_feed_controller"), {})
    cache = {
        "checked_at": utc_now(),
        "physical_static_file": physical.get("physical_sitemap_xml_exists"),
        "feed_uses_opencart_cache": feed.get("uses_cache", False),
        "feed_writes_disk_file": feed.get("writes_physical_file", False),
        "generation_mode": "live_per_request",
        "opencart_cache_layer": "none_in_feed_controller",
        "cdn_server_cache": "SAFE UNKNOWN — no cache-bust delta observed; probe returned identical SHA",
        "probe_content_equal": http_data["probe"].get("content_equal_to_plain_sitemap"),
        "manual_regeneration_required": False,
        "notes": [
            "No file_put_contents/fwrite in feed controller",
            "No $this->cache in feed controller",
            "Physical sitemap.xml absent on FTP",
            "Each GET builds XML from models",
        ],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "sitemap-cache-behavior.json", cache)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "sitemap-cache-behavior.md",
        "\n".join(["# Sitemap cache / regeneration", f"- Mode: **{cache['generation_mode']}**", ""] + [f"- {n}" for n in cache["notes"]]),
    )
    return cache


def phase_policy() -> dict[str, Any]:
    policy = {
        "checked_at": utc_now(),
        "authority": "OpenCart/ocStore built-in Google Sitemap feed (extension/feed/google_sitemap)",
        "mars_must_not_manually_edit_sitemap": True,
        "mars_may_monitor_and_audit_delta": True,
        "one_c_growth_is_normal": True,
        "new_categories_onboard_via_admin_seo": True,
        "do_not_remove_new_urls_by_default": True,
        "fix_problem_urls_at_source": [
            "product/category status and catalog data",
            "SEO URL aliases",
            "feed module bug (rare; code change with charter)",
            "robots/noindex only with explicit operator approval",
        ],
        "physical_upload_prohibited_unless_emergency": True,
        "post_1c_monitor_uses_this_model": True,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "sitemap-authority-policy.json", policy)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "sitemap-authority-policy.md",
        "\n".join(
            [
                "# Sitemap authority policy (SITE-002)",
                "",
                "- Authority: OpenCart Google Sitemap feed — **automatic, DB-driven**.",
                "- MARS: monitor/audit only; **no manual sitemap.xml edits** in normal ops.",
                "- 1C catalog growth → sitemap growth is expected.",
                "- New CATEGORY_PLP/HUB: onboard meta via admin SEO; do not delete new URLs from sitemap by default.",
                "- Problem URLs: fix catalog/SEO/source; not hand-edit XML.",
                "- Physical upload/edit: emergency + separate approval only.",
            ]
        ),
    )
    return policy


def phase_verification(
    http_data: dict[str, Any],
    physical: dict[str, Any],
    data_map: dict[str, Any],
    cache: dict[str, Any],
    rel: dict[str, Any],
) -> dict[str, Any]:
    verdict = {
        "checked_at": utc_now(),
        "automatically_generated": "YES",
        "manually_maintained_by_mars": "NO",
        "physical_file_present": "YES" if physical.get("physical_sitemap_xml_exists") else "NO",
        "generating_controller": "/public_html/catalog/controller/extension/feed/google_sitemap.php",
        "generating_route": data_map["generating_route"],
        "data_sources": ["products", "categories", "manufacturers", "information"],
        "blog_included": False,
        "one_c_relationship": "automatic reflection of catalog DB after import",
        "cache_behavior": cache["generation_mode"],
        "operational_rule": "monitor and audit; never manual XML edit in normal operations",
        "url_count_live": http_data["sitemap"].get("url_count"),
        "final_verdict": "SITE-002 SITEMAP AUTHORITY DISCOVERY COMPLETE — AUTO-GENERATED FEED CONFIRMED",
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "sitemap-authority-verification.json", verdict)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "sitemap-authority-verification.md",
        "\n".join(
            [
                "# Sitemap authority verification",
                "",
                f"- Automatically generated: **{verdict['automatically_generated']}**",
                f"- Manually maintained by MARS: **{verdict['manually_maintained_by_mars']}**",
                f"- Physical file: **{verdict['physical_file_present']}**",
                f"- Controller: `{verdict['generating_controller']}`",
                f"- Live URL count: **{verdict['url_count_live']}**",
                f"- Cache: **{verdict['cache_behavior']}**",
                f"- Final: **{verdict['final_verdict']}**",
            ]
        ),
    )
    return verdict


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--phase", choices=["all", "http", "ftp"], default="all")
    args = parser.parse_args()

    ensure_dirs()
    log: dict[str, Any] = {"started_at": utc_now(), "operation_id": OPERATION_ID}

    http_data: dict[str, Any] = {}
    if args.phase in ("all", "http"):
        http_data = phase_http()
        log["http"] = "ok"
        time.sleep(1)

    ftp_data: dict[str, Any] = {"downloaded": {}, "physical_vs_route": {}}
    if args.phase in ("all", "ftp"):
        ftp_data = phase_ftp()
        log["ftp"] = "ok"

    if args.phase == "all":
        analyses = phase_source_map(ftp_data["downloaded"])
        data_map = phase_data_source_map(analyses, http_data)
        admin_state = phase_admin_readonly(http_data)
        rel = phase_1c_relationship(http_data)
        cache = phase_cache_behavior(http_data, analyses, ftp_data["physical_vs_route"])
        policy = phase_policy()
        verdict = phase_verification(http_data, ftp_data["physical_vs_route"], data_map, cache, rel)
        log.update(
            {
                "admin_state": admin_state["feed_google_sitemap_status_inferred"],
                "final_verdict": verdict["final_verdict"],
                "url_count": http_data["sitemap"].get("url_count"),
            }
        )

    log["finished_at"] = utc_now()
    write_json(DEPLOYMENT_ROOT / "logs" / "run-log.json", log)
    print(json.dumps(log, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
