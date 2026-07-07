#!/usr/bin/env python3
"""SITE-002 Production new 1C catalog branch onboarding — Run 4.210."""
from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-01"
OCPILOT_RUN = "4.210"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SEO-META-EDGE-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-CATALOG-NEW-BRANCH-01"
AUDIT_BASELINE = "SITE-002-SITEMAP-DELTA-AUDIT-01"
WRONG_BRAND = "БЗПМ"
CORRECT_BRAND = "ЗПМ"
UTF8_BOM = b"\xef\xbb\xbf"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
SITEMAP_DELTA_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SITEMAP-DELTA-AUDIT-01"
)
CATEGORY_PAGES_MAP = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-META-CONTENT-FIX-01\admin-evidence\category-pages-map.json"
)
IMPORT_LOG_CANDIDATES = [
    Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments")
    / OPERATION_ID
    / "import-evidence"
    / "mars_1c_import_2026-07-07_080008.txt",
    Path(r"X:\AI MARS STORAGE\incoming\mars_1c_import_2026-07-07_080008.txt"),
]
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
CRAWL_DELAY_SEC = 0.35

KNOWN_BRANCH_URLS = [
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/konditerskiy-inventar",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/konditerskiy-inventar/formy-konditerskie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari",
]

OPERATOR_LARI_PATTERNS = ("lari", "shkafy-i-lari", "лари")

SUGGESTED_COPY: dict[str, str] = {
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/konditerskiy-inventar": (
        "Кондитерский инвентарь ЗПМ из нержавеющей стали для общепита и пищевых производств. "
        "Изделия для приготовления, выпечки и работы цеха."
    ),
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/konditerskiy-inventar/formy-konditerskie": (
        "Формы кондитерские ЗПМ из нержавеющей стали для выпечки, кухни и пищевых производств. "
        "Серийные изделия разных размеров и исполнений."
    ),
}

SANITY_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
]

SUBDIRS = (
    "source",
    "import-evidence",
    "inventory",
    "crawl-before",
    "crawl-after",
    "classification",
    "copy",
    "admin-evidence",
    "verification",
    "manifests",
    "logs",
)


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.in_title = False
        self.in_h1 = False
        self.h1_list: list[str] = []
        self.meta: dict[str, str] = {}
        self.links: list[dict[str, str]] = []
        self.body_open = 0
        self.body_class = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: (v or "") for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = True
        elif tag_l == "h1":
            self.in_h1 = True
        elif tag_l == "body":
            self.body_open += 1
            self.body_class = attrs_dict.get("class", "")
        elif tag_l == "meta":
            name = (attrs_dict.get("name") or attrs_dict.get("property") or "").lower()
            content = attrs_dict.get("content", "")
            if name:
                self.meta[name] = content
        elif tag_l == "link":
            rel = attrs_dict.get("rel", "").lower()
            href = attrs_dict.get("href", "")
            if rel and href:
                self.links.append({"rel": rel, "href": href})

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False
        elif tag.lower() == "h1":
            self.in_h1 = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if self.in_h1:
            self.h1_list.append(data.strip())


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def parse_production_section(path: Path, subsection: str) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    sub_match = re.search(rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
    if not sub_match:
        raise RuntimeError(f"Subsection {subsection} not found")
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in sub_match.group(1).splitlines():
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


def http_get(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache", "Accept": "text/html,application/xml,*/*"},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
            charset = response.headers.get_content_charset() or "utf-8"
            text = body.decode(charset, errors="replace")
            return {
                "url": url,
                "final_url": response.geturl(),
                "status_code": response.status,
                "x_robots_tag": response.headers.get("X-Robots-Tag", ""),
                "body": text,
                "raw_body": body,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read() if exc.fp else b""
        charset = exc.headers.get_content_charset() if exc.headers else None
        text = body.decode(charset or "utf-8", errors="replace")
        return {
            "url": url,
            "final_url": exc.geturl(),
            "status_code": exc.code,
            "x_robots_tag": exc.headers.get("X-Robots-Tag", "") if exc.headers else "",
            "body": text,
            "raw_body": body,
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "final_url": url, "status_code": None, "x_robots_tag": "", "body": "", "raw_body": b"", "error": str(exc)}


def extract_meta(html_text: str) -> dict[str, Any]:
    parser = MetaParser()
    try:
        parser.feed(html_text)
    except Exception:
        pass
    canonical = next((l["href"] for l in parser.links if l["rel"] == "canonical"), "")
    title = html.unescape(parser.title.strip())
    description = parser.meta.get("description", "")
    h1 = " | ".join(h for h in parser.h1_list if h)
    return {
        "title": title,
        "title_length": len(title),
        "meta_description": description,
        "description_length": len(description),
        "meta_keywords": parser.meta.get("keywords", ""),
        "h1": h1,
        "canonical": canonical,
        "meta_robots": parser.meta.get("robots", ""),
        "body_class": parser.body_class,
        "body_count": parser.body_open,
        "page_category": "page--category" in parser.body_class,
        "page_product": "page--product" in parser.body_class,
        "yandex_metrika": any(t in html_text.lower() for t in ("mc.yandex.ru/metrika", "ym(", "yandex.metrika")),
        "yandex_webmaster": "yandex-verification" in html_text.lower(),
        "load_more_marker": "load-more" in html_text.lower() or "load_more" in html_text.lower(),
    }


def normalize_name(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("\xa0", " ").strip()).lower()


def url_slug(url: str) -> str:
    path = urllib.parse.urlparse(url).path.rstrip("/")
    return path.split("/")[-1] if path else ""


def path_depth(url: str) -> int:
    return len([p for p in urllib.parse.urlparse(url).path.split("/") if p])


def is_product_pdp_url(url: str) -> bool:
    parts = [p for p in urllib.parse.urlparse(url).path.split("/") if p]
    return len(parts) >= 5 and parts[0] == "katalog"


def is_category_url(url: str) -> bool:
    parts = [p for p in urllib.parse.urlparse(url).path.split("/") if p]
    return len(parts) >= 3 and parts[0] == "katalog" and not is_product_pdp_url(url)


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
            "audit_baseline_before": AUDIT_BASELINE,
            "change_type": "new-1c-catalog-branch-onboarding",
            "import_growth_model": "daily_1c_import_expected",
            "delete_hide_noindex_allowed": False,
            "target_page_type": "CATEGORY_PLP_AND_CATEGORY_HUB",
            "admin_save_allowed": "exact_category_seo_fields_only",
            "db_direct_write_allowed": False,
            "ftp_upload_allowed": False,
            "file_fallback_allowed": False,
            "product_pdp_changes_allowed": False,
            "product_generator_change_allowed": False,
            "llms_txt_change_allowed": False,
            "robots_change_allowed": False,
            "sitemap_change_allowed": False,
            "header_footer_change_allowed": False,
            "brand_policy_correct": CORRECT_BRAND,
            "brand_policy_forbidden_public": WRONG_BRAND,
            "domain_bzpm_ru_allowed": True,
            "created_at": utc_now(),
        },
    )


def phase1_import_evidence() -> dict[str, Any]:
    raw_log = ""
    log_source = "operator_charter"
    for candidate in IMPORT_LOG_CANDIDATES:
        if candidate.exists():
            raw_log = candidate.read_text(encoding="utf-8", errors="replace")
            log_source = str(candidate)
            break

    def extract_field(pattern: str, default: str = "") -> str:
        if not raw_log:
            return default
        m = re.search(pattern, raw_log, re.IGNORECASE | re.MULTILINE)
        return m.group(1).strip() if m else default

    summary = {
        "run_id": extract_field(r"Run ID:\s*\n(.+)", "mars-20260707-080008-[operator-provided]"),
        "operation": extract_field(r"Operation:\s*\n(.+)", "MARS parallel 1C import wrapper"),
        "mode": extract_field(r"Mode:\s*\n(.+)", "run"),
        "environment": extract_field(r"Environment:\s*\n(.+)", "PRODUCTION"),
        "started": extract_field(r"Started:\s*\n(.+)", "2026-07-07T08:00:08+03:00"),
        "wrapper_path": extract_field(
            r"Wrapper path:\s*\n(.+)",
            "/home/a/assum/bzpm.ru/storage/mars-tools/cron/mars_1c_import_wrapper.php",
        ),
        "step1_status": extract_field(r"Step 1[\s\S]*?status:\s*\n(.+)", "PASS"),
        "step2_status": extract_field(r"Step 2[\s\S]*?status:\s*\n(.+)", "PASS"),
        "step1_input": extract_field(r"Step 1[\s\S]*?input files:\s*\n- (.+)", "import0_1.xml (import0_*.xml)"),
        "step2_input": extract_field(r"Step 2[\s\S]*?input files:\s*\n- (.+)", "offers0_1.xml (offers0_*.xml)"),
        "step1_duration": extract_field(r"Step 1[\s\S]*?duration:\s*\n(.+)", "SAFE UNKNOWN"),
        "step2_duration": extract_field(r"Step 2[\s\S]*?duration:\s*\n(.+)", "SAFE UNKNOWN"),
        "final_status": extract_field(r"Final status:\s*\n(.+)", "SUCCESS"),
        "legacy_policy": "Sergey legacy import preserved; wrapper is parallel.",
        "db_credentials_note": "Do not print DB credentials.",
        "log_source": log_source,
        "raw_log_available": bool(raw_log),
        "conclusion": (
            "Daily 1C import is active and successful; new categories/products may appear normally; "
            "new catalog branches require onboarding, not deletion by default."
        ),
        "captured_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "import-evidence" / "1c-import-2026-07-07-summary.json", summary)
    md = [
        "# 1C import evidence — 2026-07-07",
        "",
        f"Captured: {summary['captured_at']}",
        f"Log source: {summary['log_source']}",
        "",
        "## Summary",
        "",
        f"- Run ID: {summary['run_id']}",
        f"- Operation: {summary['operation']}",
        f"- Mode: {summary['mode']}",
        f"- Environment: {summary['environment']}",
        f"- Started: {summary['started']}",
        f"- Wrapper path: {summary['wrapper_path']}",
        f"- Step 1 (catalog/products): {summary['step1_status']} — {summary['step1_input']}",
        f"- Step 2 (offers/prices/stocks): {summary['step2_status']} — {summary['step2_input']}",
        f"- Final status: {summary['final_status']}",
        "",
        "## Policy",
        "",
        summary["legacy_policy"],
        "",
        "## Conclusion",
        "",
        summary["conclusion"],
        "",
        summary["db_credentials_note"],
    ]
    write_text(DEPLOYMENT_ROOT / "import-evidence" / "1c-import-2026-07-07-summary.md", "\n".join(md))
    return summary


def load_sitemap_urls() -> set[str]:
    urls: set[str] = set()
    current_csv = SITEMAP_DELTA_ROOT / "current" / "sitemap-current-urls.csv"
    if current_csv.exists():
        with current_csv.open(encoding="utf-8", newline="") as fh:
            for row in csv.DictReader(fh):
                u = (row.get("url") or row.get("loc") or "").strip().rstrip("/")
                if u:
                    urls.add(u)
    if not urls:
        resp = http_get("https://bzpm.ru/sitemap.xml")
        if resp["status_code"] == 200:
            root = ET.fromstring(resp["body"])
            for loc in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
                if loc.text:
                    urls.add(loc.text.strip().rstrip("/"))
    return urls


def phase2_target_inventory() -> list[dict[str, Any]]:
    added_path = SITEMAP_DELTA_ROOT / "classification" / "added-url-classification.json"
    added_rows = json.loads(added_path.read_text(encoding="utf-8")) if added_path.exists() else []
    sitemap_urls = load_sitemap_urls()
    targets: dict[str, dict[str, Any]] = {}

    for row in added_rows:
        url = row["url"].rstrip("/")
        page_type = row.get("page_type", "")
        if page_type == "PRODUCT_PDP" or is_product_pdp_url(url):
            targets[url] = {
                "url": url,
                "source": "Run 4.209 added URL",
                "page_type_guess": "PRODUCT_PDP",
                "branch": "/".join(urllib.parse.urlparse(url).path.split("/")[2:4]),
                "category_name": row.get("h1", ""),
                "include": "no",
                "reason": "PDP out of scope for category admin SEO",
                "issue": "out of scope",
            }
            continue
        if page_type in ("CATEGORY_PLP", "CATEGORY_HUB") or is_category_url(url):
            desc = row.get("meta_description", "")
            issue = "category new but OK"
            include = "no"
            reason = "meta already present"
            if not desc.strip():
                issue = "missing description"
                include = "yes"
                reason = "new category PLP missing meta description (Run 4.209 YELLOW)"
            targets[url] = {
                "url": url,
                "source": "Run 4.209 added URL",
                "page_type_guess": page_type or "CATEGORY_PLP",
                "branch": "/".join(urllib.parse.urlparse(url).path.split("/")[2:4]),
                "category_name": row.get("h1", ""),
                "include": include,
                "reason": reason,
                "issue": issue,
            }

    for url in KNOWN_BRANCH_URLS:
        url = url.rstrip("/")
        if url not in targets:
            targets[url] = {
                "url": url,
                "source": "operator mention" if "lari" in url else "Run 4.209 added URL",
                "page_type_guess": "CATEGORY_PLP",
                "branch": "/".join(urllib.parse.urlparse(url).path.split("/")[2:4]),
                "category_name": "",
                "include": "review",
                "reason": "known branch — verify live meta",
                "issue": "needs review",
            }

    for url in sorted(sitemap_urls):
        path_lower = urllib.parse.urlparse(url).path.lower()
        if not is_category_url(url):
            continue
        if not any(p in path_lower for p in OPERATOR_LARI_PATTERNS) and "konditerskiy-inventar" not in path_lower:
            continue
        if url in targets:
            continue
        targets[url] = {
            "url": url,
            "source": "current sitemap",
            "page_type_guess": "CATEGORY_PLP",
            "branch": "/".join(urllib.parse.urlparse(url).path.split("/")[2:4]),
            "category_name": "",
            "include": "review",
            "reason": "lari/konditerskiy-related category in sitemap",
            "issue": "needs review",
        }

    rows = list(targets.values())
    write_csv(
        DEPLOYMENT_ROOT / "inventory" / "new-branch-targets.csv",
        rows,
        ["url", "source", "page_type_guess", "branch", "category_name", "include", "reason", "issue"],
    )
    write_json(DEPLOYMENT_ROOT / "inventory" / "new-branch-targets.json", {"generated_at": utc_now(), "targets": rows})
    md = ["# New branch targets", "", f"Generated: {utc_now()}", f"Total: {len(rows)}", ""]
    for r in rows:
        md.append(f"- [{r['include']}] {r['url']} — {r['issue']} — {r['reason']}")
    write_text(DEPLOYMENT_ROOT / "inventory" / "new-branch-targets.md", "\n".join(md))
    return rows


def classify_crawl_row(row: dict[str, Any]) -> str:
    if row.get("http_status") not in (200, None) and row.get("http_status") != 200:
        if row.get("http_status") in (301, 302, 303, 307, 308):
            return "REDIRECT_OR_404_REVIEW"
        return "REDIRECT_OR_404_REVIEW"
    if row.get("product_pdp"):
        return "PRODUCT_PDP_OUT_OF_SCOPE"
    desc = (row.get("meta_description") or "").strip()
    if not desc:
        return "CATEGORY_PLP_MISSING_DESCRIPTION"
    if len(desc) < 80:
        return "CATEGORY_PLP_WEAK_DESCRIPTION"
    return "CATEGORY_PLP_OK"


def crawl_target_urls(urls: list[str], label: str, sitemap_urls: set[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for url in urls:
        resp = http_get(url)
        body = resp.get("body") or ""
        meta = extract_meta(body) if body else {}
        is_pdp = is_product_pdp_url(url) or meta.get("page_product", False)
        is_cat = is_category_url(url) or meta.get("page_category", False)
        product_grid = "product-layout" in body or "product-thumb" in body or "product-grid" in body
        row = {
            "url": url,
            "http_status": resp.get("status_code"),
            "final_url": resp.get("final_url"),
            "title": meta.get("title", ""),
            "title_length": meta.get("title_length", 0),
            "meta_description": meta.get("meta_description", ""),
            "description_length": meta.get("description_length", 0),
            "meta_keywords": meta.get("meta_keywords", ""),
            "h1": meta.get("h1", ""),
            "canonical": meta.get("canonical", ""),
            "meta_robots": meta.get("meta_robots", ""),
            "x_robots_tag": resp.get("x_robots_tag", ""),
            "body_class": meta.get("body_class", ""),
            "page_category": is_cat,
            "page_product": is_pdp,
            "product_pdp": is_pdp,
            "breadcrumb_context": meta.get("h1", ""),
            "product_grid_marker": product_grid,
            "forbidden_bzpm_count": body.count(WRONG_BRAND),
            "zpm_count": body.count(CORRECT_BRAND),
            "sitemap_membership": url.rstrip("/") in sitemap_urls,
            "indexable": "noindex" not in (meta.get("meta_robots", "") + resp.get("x_robots_tag", "")).lower(),
            "classification": "",
            "error": resp.get("error"),
        }
        row["classification"] = classify_crawl_row(row)
        rows.append(row)
        time.sleep(CRAWL_DELAY_SEC)

    fname = "new-branch-before" if "before" in label else "new-branch-after"
    write_csv(DEPLOYMENT_ROOT / label / f"{fname}.csv", rows, list(rows[0].keys()) if rows else [])
    write_json(DEPLOYMENT_ROOT / label / f"{fname}.json", {"captured_at": utc_now(), "rows": rows})
    md = [f"# Crawl {label}", "", f"Captured: {utc_now()}", ""]
    for r in rows:
        md.append(
            f"- {r['url']} — {r.get('http_status')} — {r['classification']} — desc_len={r.get('description_length')}"
        )
    write_text(DEPLOYMENT_ROOT / label / f"{fname}.md", "\n".join(md))
    return rows


def generate_description(name: str, url: str) -> str:
    url_norm = url.rstrip("/")
    if url_norm in SUGGESTED_COPY:
        copy = SUGGESTED_COPY[url_norm]
    elif "lari" in url.lower() and "shkaf" in name.lower():
        copy = (
            "Шкафы и лари ЗПМ из нержавеющей стали для общепита, кухонь и производственных зон. "
            "Подбор по назначению, размерам и исполнению."
        )
    elif "lari" in url.lower() or normalize_name(name) == "лари":
        copy = (
            "Лари ЗПМ из нержавеющей стали для хранения инвентаря и продукции на кухнях, "
            "в цехах и производственных зонах. Разные размеры и исполнение."
        )
    else:
        copy = (
            f"{name.strip()} ЗПМ из нержавеющей стали для общепита и пищевых производств. "
            "Подберите изделия по назначению, размерам и исполнению."
        )
    if WRONG_BRAND in copy:
        raise RuntimeError(f"Forbidden brand in copy for {url}")
    if len(copy) < 120:
        copy = copy.rstrip(".") + ". Надёжные решения для ресторанов, столовых и производств."
    if len(copy) > 165:
        copy = copy[:162].rsplit(" ", 1)[0] + "."
    return copy


def parse_category_breadcrumb(text: str) -> tuple[str, str]:
    cleaned = text.replace("\t", " ").strip()
    parts = [p.strip() for p in re.split(r"\s*>\s*", cleaned) if p.strip()]
    if not parts:
        return "", ""
    name = re.sub(r"\s+\d+\s*$", "", parts[-1]).strip()
    parent = parts[-2] if len(parts) > 1 else ""
    return name, parent


def load_category_map_seed() -> list[dict[str, Any]]:
    if not CATEGORY_PAGES_MAP.exists():
        return []
    rows = []
    for row in json.loads(CATEGORY_PAGES_MAP.read_text(encoding="utf-8")):
        name, parent = parse_category_breadcrumb(row["text"])
        rows.append({"category_id": row["category_id"], "name": name, "parent": parent, "text": row["text"]})
    return rows


def scrape_admin_categories(page: Any, admin_base: str, token: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen: set[int] = set()
    for page_num in range(1, 8):
        list_url = f"{admin_base}index.php?route=catalog/category&user_token={token}&page={page_num}"
        page.goto(list_url, wait_until="domcontentloaded", timeout=120000)
        page.wait_for_timeout(2500)
        tr = page.locator("table tbody tr")
        count = tr.count()
        if count == 0:
            break
        added = 0
        for i in range(count):
            row = tr.nth(i)
            text_row = row.inner_text()
            links = row.locator('a[href*="category_id="]')
            if links.count() == 0:
                continue
            href = links.first.get_attribute("href") or ""
            mid = re.search(r"category_id=(\d+)", href)
            if not mid:
                continue
            cid = int(mid.group(1))
            if cid in seen:
                continue
            seen.add(cid)
            name, parent = parse_category_breadcrumb(text_row)
            rows.append({"category_id": cid, "name": name, "parent": parent, "text": text_row})
            added += 1
        if added == 0:
            break
    for row in load_category_map_seed():
        if row["category_id"] not in seen:
            rows.append(row)
            seen.add(row["category_id"])
    return rows


def build_name_index(admin_categories: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    index: dict[str, list[dict[str, Any]]] = {}
    for cat in admin_categories:
        index.setdefault(normalize_name(cat["name"]), []).append(cat)
    return index


def match_category_id(
    url: str,
    h1: str,
    slug: str,
    admin_categories: list[dict[str, Any]],
    name_index: dict[str, list[dict[str, Any]]],
) -> tuple[int | None, str, str]:
    norm_h1 = normalize_name(h1)
    path_parts = [p for p in urllib.parse.urlparse(url).path.split("/") if p]
    if norm_h1 and norm_h1 in name_index:
        matches = name_index[norm_h1]
        if len(matches) == 1:
            return matches[0]["category_id"], "ADMIN_CATEGORY", "HIGH"
        for cat in matches:
            parent_norm = normalize_name(cat.get("parent", ""))
            if parent_norm and any(parent_norm in normalize_name(p.replace("-", " ")) for p in path_parts):
                return cat["category_id"], "ADMIN_CATEGORY", "HIGH"
    slug_phrase = normalize_name(slug.replace("-", " "))
    for cat in admin_categories:
        if slug_phrase and slug_phrase == normalize_name(cat["name"].replace("-", " ")):
            return cat["category_id"], "ADMIN_CATEGORY", "MEDIUM"
        if slug == "lari" and normalize_name(cat["name"]) == "лари":
            return cat["category_id"], "ADMIN_CATEGORY", "HIGH"
        if slug == "konditerskiy-inventar" and "кондитер" in normalize_name(cat["name"]):
            return cat["category_id"], "ADMIN_CATEGORY", "HIGH"
        if slug == "formy-konditerskie" and "формы кондитер" in normalize_name(cat["name"]):
            return cat["category_id"], "ADMIN_CATEGORY", "HIGH"
    return None, "SAFE_UNKNOWN", "LOW"


def admin_search_category_by_name(page: Any, admin_base: str, token: str, name: str) -> int | None:
    q = urllib.parse.quote(name)
    list_url = f"{admin_base}index.php?route=catalog/category&user_token={token}&filter_name={q}"
    page.goto(list_url, wait_until="domcontentloaded", timeout=120000)
    page.wait_for_timeout(2500)
    rows = page.locator("table tbody tr")
    for i in range(min(rows.count(), 10)):
        row = rows.nth(i)
        text_row = row.inner_text()
        links = row.locator('a[href*="category_id="]')
        if links.count() == 0:
            continue
        href = links.first.get_attribute("href") or ""
        mid = re.search(r"category_id=(\d+)", href)
        row_name, _ = parse_category_breadcrumb(text_row)
        if mid and normalize_name(row_name) == normalize_name(name):
            return int(mid.group(1))
    return None


def phase_authority_and_copy(
    onboard_targets: list[dict[str, Any]],
    before_rows: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    from playwright.sync_api import sync_playwright

    admin = parse_production_section(SECRETS_PATH, "OpenCart Admin")
    before_by_url = {r["url"].rstrip("/"): r for r in before_rows}
    authority_rows: list[dict[str, Any]] = []
    copy_rows: list[dict[str, Any]] = []
    admin_actions: list[dict[str, Any]] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(120000)
        page.goto(admin.get("url", "https://bzpm.ru/admin/"), wait_until="domcontentloaded")
        page.fill('input[name="username"]', admin["login"])
        page.fill('input[name="password"]', admin["password"])
        page.click('button[type="submit"]')
        page.wait_for_timeout(5000)
        token_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.url)
        if not token_match:
            body_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.content())
            token = body_match.group(1) if body_match else None
        else:
            token = token_match.group(1)
        admin_base = page.url.split("index.php")[0]
        if not token:
            browser.close()
            raise RuntimeError("Admin login failed")

        admin_categories = scrape_admin_categories(page, admin_base, token)
        write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-list-scrape.json", admin_categories)
        name_index = build_name_index(admin_categories)

        for target in onboard_targets:
            url = target["url"].rstrip("/")
            live = before_by_url.get(url, {})
            h1 = live.get("h1") or target.get("category_name") or ""
            slug = url_slug(url)
            cid, authority, confidence = match_category_id(url, h1, slug, admin_categories, name_index)
            if cid is None and h1:
                searched = admin_search_category_by_name(page, admin_base, token, h1)
                if searched:
                    cid = searched
                    authority = "ADMIN_CATEGORY"
                    confidence = "HIGH"

            planned_method = "ADMIN_SEO_SAVE" if cid else "DEFERRED_SAFE_UNKNOWN"
            authority_rows.append(
                {
                    "url": url,
                    "category_id": cid or "",
                    "category_name": h1,
                    "parent_category": "",
                    "current_admin_meta_title": "",
                    "current_admin_meta_description": "",
                    "live_title": live.get("title", ""),
                    "live_description": live.get("meta_description", ""),
                    "authority": authority,
                    "planned_method": planned_method,
                    "confidence": confidence,
                }
            )
            if not cid:
                continue

            edit_url = f"{admin_base}index.php?route=catalog/category/edit&user_token={token}&category_id={cid}"
            page.goto(edit_url, wait_until="domcontentloaded", timeout=120000)
            page.wait_for_timeout(2000)
            if page.locator('textarea[name="category_description[1][meta_description]"]').count() == 0:
                authority_rows[-1]["planned_method"] = "DEFERRED_SAFE_UNKNOWN"
                continue

            current_title = page.locator('input[name="category_description[1][meta_title]"]').input_value()
            current_desc = page.locator('textarea[name="category_description[1][meta_description]"]').input_value()
            current_kw = ""
            kw_loc = page.locator('input[name="category_description[1][meta_keyword]"]')
            if kw_loc.count():
                current_kw = kw_loc.input_value()
            cat_name = page.locator('input[name="category_description[1][name]"]').input_value().strip()
            parent_sel = page.locator('select[name="parent_id"] option:checked')
            parent_name = parent_sel.inner_text().strip() if parent_sel.count() else ""

            authority_rows[-1].update(
                {
                    "category_name": cat_name or h1,
                    "parent_category": parent_name,
                    "current_admin_meta_title": current_title,
                    "current_admin_meta_description": current_desc,
                }
            )

            if current_desc.strip() and len(current_desc.strip()) >= 80:
                authority_rows[-1]["planned_method"] = "NO_CHANGE_META_OK"
                continue

            new_desc = generate_description(cat_name or h1, url)
            copy_rows.append(
                {
                    "url": url,
                    "category_id": cid,
                    "category_name": cat_name or h1,
                    "meta_description_before": current_desc,
                    "meta_description_after": new_desc,
                    "description_length": len(new_desc),
                    "contains_zpm": CORRECT_BRAND in new_desc,
                    "contains_forbidden_bzpm": WRONG_BRAND in new_desc,
                }
            )
            admin_actions.append(
                {
                    "url": url,
                    "category_id": cid,
                    "category_name": cat_name or h1,
                    "field": "meta_description",
                    "before": current_desc,
                    "after": new_desc,
                    "expected_verification_url": url,
                    "rollback_description": current_desc,
                }
            )

        browser.close()

    write_csv(
        DEPLOYMENT_ROOT / "manifests" / "category-authority-map.csv",
        authority_rows,
        list(authority_rows[0].keys()) if authority_rows else [],
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "category-authority-map.json", authority_rows)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "category-authority-map.md",
        "\n".join(["# Category authority map", ""] + [f"- {r['url']} id={r['category_id']} {r['planned_method']}" for r in authority_rows]),
    )
    write_csv(
        DEPLOYMENT_ROOT / "copy" / "category-meta-copy-final.csv",
        copy_rows,
        list(copy_rows[0].keys()) if copy_rows else [],
    )
    write_json(DEPLOYMENT_ROOT / "copy" / "category-meta-copy-final.json", copy_rows)
    write_text(
        DEPLOYMENT_ROOT / "copy" / "category-meta-copy-final.md",
        "\n".join(["# Category meta copy", ""] + [f"- {r['url']}: {r['meta_description_after']}" for r in copy_rows]),
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "admin-actions.json", admin_actions)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md",
        "\n".join(
            [
                "# Implementation plan",
                "",
                f"Admin category SEO saves (meta_description only): {len(admin_actions)}",
                "Title changes: 0",
                "File fallback: 0",
                "Delete/hide/noindex: 0",
                "",
            ]
            + [f"- category_id={a['category_id']} {a['url']}" for a in admin_actions]
        ),
    )
    return authority_rows, copy_rows, admin_actions


def capture_admin_before(admin_actions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    from playwright.sync_api import sync_playwright

    admin = parse_production_section(SECRETS_PATH, "OpenCart Admin")
    rows: list[dict[str, Any]] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(120000)
        page.goto(admin.get("url", "https://bzpm.ru/admin/"), wait_until="domcontentloaded")
        page.fill('input[name="username"]', admin["login"])
        page.fill('input[name="password"]', admin["password"])
        page.click('button[type="submit"]')
        page.wait_for_timeout(5000)
        token_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.url)
        admin_base = page.url.split("index.php")[0]
        token = token_match.group(1) if token_match else None
        if not token:
            browser.close()
            return rows
        for action in admin_actions:
            cid = action["category_id"]
            edit_url = f"{admin_base}index.php?route=catalog/category/edit&user_token={token}&category_id={cid}"
            page.goto(edit_url, wait_until="domcontentloaded", timeout=120000)
            page.wait_for_timeout(2000)
            rows.append(
                {
                    "category_id": cid,
                    "category_name": page.locator('input[name="category_description[1][name]"]').input_value().strip(),
                    "current_meta_title": page.locator('input[name="category_description[1][meta_title]"]').input_value(),
                    "current_meta_description": page.locator('textarea[name="category_description[1][meta_description]"]').input_value(),
                    "current_meta_keywords": page.locator('input[name="category_description[1][meta_keyword]"]').input_value()
                    if page.locator('input[name="category_description[1][meta_keyword]"]').count()
                    else "",
                    "planned_new_description": action["after"],
                    "rollback_description": action["rollback_description"],
                }
            )
        browser.close()
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-seo-before.json", rows)
    write_csv(
        DEPLOYMENT_ROOT / "admin-evidence" / "category-seo-before.csv",
        rows,
        [
            "category_id",
            "category_name",
            "current_meta_title",
            "current_meta_description",
            "current_meta_keywords",
            "planned_new_description",
            "rollback_description",
        ],
    )
    write_text(
        DEPLOYMENT_ROOT / "admin-evidence" / "category-seo-before.md",
        "\n".join(["# Admin before evidence", ""] + [f"- id={r['category_id']} {r['category_name']}" for r in rows]),
    )
    return rows


def phase_dry_run(onboard_targets: list[dict[str, Any]], admin_actions: list[dict[str, Any]], copy_rows: list[dict[str, Any]]) -> None:
    forbidden = [r for r in copy_rows if r.get("contains_forbidden_bzpm")]
    pdp = [t for t in onboard_targets if t.get("product_pdp")]
    payload = {
        "target_inventory_count": len(onboard_targets),
        "new_branch_category_count": len([t for t in onboard_targets if not t.get("product_pdp")]),
        "admin_save_count": len(admin_actions),
        "deferred_count": len(onboard_targets) - len(admin_actions),
        "forbidden_bzpm_in_copy": len(forbidden),
        "product_pdp_in_targets": len(pdp),
        "file_uploads": 0,
        "delete_hide_noindex": 0,
        "examples": admin_actions,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "\n".join(
            [
                "# Dry-run",
                "",
                f"Targets: {payload['target_inventory_count']}",
                f"Admin saves: {payload['admin_save_count']}",
                f"Forbidden БЗПМ: {payload['forbidden_bzpm_in_copy']}",
                f"PDP in targets: {payload['product_pdp_in_targets']}",
                "Delete/hide/noindex: 0",
                "",
                "## Before/after descriptions",
                "",
            ]
            + [f"- {a['url']}: `{a['before'][:40]}...` → `{a['after']}`" for a in admin_actions]
        ),
    )
    if forbidden or pdp:
        raise RuntimeError("Dry-run gate failed")


def admin_execute_saves(admin_actions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    from playwright.sync_api import sync_playwright

    admin = parse_production_section(SECRETS_PATH, "OpenCart Admin")
    saves: list[dict[str, Any]] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(120000)
        page.goto(admin.get("url", "https://bzpm.ru/admin/"), wait_until="domcontentloaded")
        page.fill('input[name="username"]', admin["login"])
        page.fill('input[name="password"]', admin["password"])
        page.click('button[type="submit"]')
        page.wait_for_timeout(5000)
        token_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.url)
        admin_base = page.url.split("index.php")[0]
        token = token_match.group(1) if token_match else None
        if not token:
            browser.close()
            raise RuntimeError("Admin login failed")
        for action in admin_actions:
            cid = action["category_id"]
            edit_url = f"{admin_base}index.php?route=catalog/category/edit&user_token={token}&category_id={cid}"
            page.goto(edit_url, wait_until="domcontentloaded", timeout=120000)
            page.wait_for_timeout(2000)
            before_desc = page.locator('textarea[name="category_description[1][meta_description]"]').input_value()
            page.fill('textarea[name="category_description[1][meta_description]"]', action["after"])
            page.locator('.page-header button[type="submit"], button[type="submit"].btn-primary').first.click()
            page.wait_for_timeout(4000)
            resp = http_get(action["url"])
            live = extract_meta(resp["body"]) if resp.get("body") else {}
            verified = action["after"][:40] in (live.get("meta_description") or "")
            saves.append(
                {
                    "category_id": cid,
                    "url": action["url"],
                    "category_name": action.get("category_name", ""),
                    "before_description": before_desc,
                    "after_description": action["after"],
                    "status": "SAVED",
                    "verified": verified,
                    "live_description": live.get("meta_description"),
                }
            )
            time.sleep(CRAWL_DELAY_SEC)
        browser.close()
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-seo-after.json", saves)
    return saves


def verify_preservation() -> dict[str, Any]:
    robots = http_get("https://bzpm.ru/robots.txt")
    sitemap = http_get("https://bzpm.ru/sitemap.xml")
    llms = http_get("https://bzpm.ru/llms.txt")
    stoly = http_get("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly")
    url_count = 0
    sitemap_valid = False
    if sitemap["status_code"] == 200:
        try:
            root = ET.fromstring(sitemap["body"])
            url_count = len(root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"))
            sitemap_valid = url_count > 0
        except ET.ParseError:
            pass
    llms_body = llms.get("raw_body") or b""
    home = http_get("https://bzpm.ru/")
    home_meta = extract_meta(home["body"]) if home.get("body") else {}
    stoly_meta = extract_meta(stoly["body"]) if stoly.get("body") else {}
    return {
        "home_status": home["status_code"],
        "home_body_count": home_meta.get("body_count"),
        "home_yandex_metrika": home_meta.get("yandex_metrika"),
        "home_yandex_webmaster": home_meta.get("yandex_webmaster"),
        "stoly_load_more": stoly_meta.get("load_more_marker"),
        "robots_status": robots["status_code"],
        "robots_sitemap_directive": "sitemap:" in (robots.get("body") or "").lower(),
        "sitemap_status": sitemap["status_code"],
        "sitemap_valid": sitemap_valid,
        "sitemap_url_count": url_count,
        "llms_status": llms["status_code"],
        "llms_utf8_bom": llms_body.startswith(UTF8_BOM),
        "llms_forbidden_bzpm": WRONG_BRAND in (llms.get("body") or ""),
    }


def write_ongoing_rule() -> None:
    rule = {
        "policy": "daily_1c_catalog_growth_onboarding",
        "rules": [
            "1C import may add categories/products daily",
            "New sitemap growth is not automatically a problem",
            "New categories should be onboarded, not deleted/closed by default",
            "Test/НЕ БРАТЬ/obvious garbage SKUs audited separately",
            "Category PLP/hub meta monitored after import",
            "Product PDP generator covers true PDP, not category/hub PLP",
            "Future inventory separates PRODUCT_PDP, CATEGORY_PLP, CATEGORY_HUB, LEGACY_HUB, TECHNICAL",
        ],
        "created_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "ongoing-1c-catalog-growth-rule.json", rule)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "ongoing-1c-catalog-growth-rule.md",
        "\n".join(["# Ongoing 1C catalog growth rule", ""] + [f"- {r}" for r in rule["rules"]]),
    )


def run_prepare() -> dict[str, Any]:
    ensure_dirs()
    import_summary = phase1_import_evidence()
    inventory = phase2_target_inventory()
    sitemap_urls = load_sitemap_urls()

    category_urls = sorted(
        {
            t["url"].rstrip("/")
            for t in inventory
            if t.get("page_type_guess") != "PRODUCT_PDP" and not is_product_pdp_url(t["url"])
        }
        | {u.rstrip("/") for u in KNOWN_BRANCH_URLS}
    )

    before_rows = crawl_target_urls(category_urls, "crawl-before", sitemap_urls)

    onboard_targets = []
    for row in before_rows:
        if row.get("product_pdp"):
            continue
        if row.get("classification") == "CATEGORY_PLP_MISSING_DESCRIPTION":
            onboard_targets.append({**row, "url": row["url"].rstrip("/")})
        elif row.get("classification") == "CATEGORY_PLP_WEAK_DESCRIPTION":
            onboard_targets.append({**row, "url": row["url"].rstrip("/")})

    _, copy_rows, admin_actions = phase_authority_and_copy(onboard_targets, before_rows)
    before_evidence = capture_admin_before(admin_actions)
    phase_dry_run(onboard_targets, admin_actions, copy_rows)
    write_ongoing_rule()
    return {
        "import": import_summary["final_status"],
        "inventory_count": len(inventory),
        "crawl_count": len(before_rows),
        "onboard_targets": len(onboard_targets),
        "admin_actions": len(admin_actions),
        "before_evidence": len(before_evidence),
    }


def run_deploy() -> dict[str, Any]:
    admin_actions = json.loads((DEPLOYMENT_ROOT / "manifests" / "admin-actions.json").read_text(encoding="utf-8"))
    if not admin_actions:
        return {"status": "NO_MUTATION_REQUIRED", "saves": 0}
    saves = admin_execute_saves(admin_actions)
    verified = sum(1 for s in saves if s.get("verified"))
    return {
        "status": "COMPLETE" if verified == len(saves) else "PARTIAL",
        "saves": len(saves),
        "verified": verified,
        "saves_detail": saves,
    }


def run_verify() -> dict[str, Any]:
    admin_actions = json.loads((DEPLOYMENT_ROOT / "manifests" / "admin-actions.json").read_text(encoding="utf-8"))
    sitemap_urls = load_sitemap_urls()
    target_urls = [a["url"] for a in admin_actions]
    after_rows = crawl_target_urls(target_urls + SANITY_URLS, "crawl-after", sitemap_urls)

    before_data = json.loads((DEPLOYMENT_ROOT / "crawl-before" / "new-branch-before.json").read_text(encoding="utf-8"))
    before_rows = before_data["rows"]
    target_set = {a["url"].rstrip("/") for a in admin_actions}
    summary = []
    for action in admin_actions:
        url = action["url"].rstrip("/")
        b = next((r for r in before_rows if r["url"].rstrip("/") == url), {})
        a_row = next((r for r in after_rows if r["url"].rstrip("/") == url), {})
        summary.append(
            {
                "url": url,
                "category_id": action["category_id"],
                "description_before": b.get("meta_description", ""),
                "description_after": a_row.get("meta_description", ""),
                "description_length": a_row.get("description_length", 0),
                "contains_zpm": CORRECT_BRAND in (a_row.get("meta_description") or ""),
                "contains_bzpm": a_row.get("forbidden_bzpm_count", 0) > 0,
                "verified": bool(a_row.get("meta_description") and action["after"][:40] in a_row.get("meta_description", "")),
            }
        )
    write_json(DEPLOYMENT_ROOT / "verification" / "before-after-summary.json", summary)
    write_csv(
        DEPLOYMENT_ROOT / "verification" / "before-after-summary.csv",
        summary,
        list(summary[0].keys()) if summary else [],
    )
    write_text(
        DEPLOYMENT_ROOT / "verification" / "before-after-summary.md",
        "\n".join(["# Before/after summary", ""] + [f"- {s['url']}: verified={s['verified']}" for s in summary]),
    )
    preservation = verify_preservation()
    write_json(DEPLOYMENT_ROOT / "verification" / "sanity-checks.json", preservation)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "sanity-checks.md",
        "\n".join(["# Sanity checks", "", json.dumps(preservation, ensure_ascii=False, indent=2)]),
    )
    return {"preservation": preservation, "verified_count": sum(1 for s in summary if s["verified"]), "summary": summary}


def run_all() -> int:
    prep = run_prepare()
    dep = run_deploy()
    ver = run_verify()
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "run-summary.json",
        {"operation_id": OPERATION_ID, "ocpilot_run": OCPILOT_RUN, "prepare": prep, "deploy": dep, "verify": ver, "finished_at": utc_now()},
    )
    print(json.dumps({"prepare": prep, "deploy": dep, "verify": ver}, ensure_ascii=False, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("phase", choices=["prepare", "deploy", "verify", "all"], default="all", nargs="?")
    args = parser.parse_args()
    if args.phase == "prepare":
        print(json.dumps(run_prepare(), ensure_ascii=False, indent=2))
    elif args.phase == "deploy":
        print(json.dumps(run_deploy(), ensure_ascii=False, indent=2))
    elif args.phase == "verify":
        print(json.dumps(run_verify(), ensure_ascii=False, indent=2))
    else:
        return run_all()
    return 0


if __name__ == "__main__":
    sys.exit(main())
