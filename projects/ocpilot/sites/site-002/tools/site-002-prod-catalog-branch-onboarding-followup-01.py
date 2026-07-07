#!/usr/bin/env python3
"""SITE-002 Production catalog branch onboarding follow-up — Run 4.211."""
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

OPERATION_ID = "SITE-002-PROD-CATALOG-BRANCH-ONBOARDING-FOLLOWUP-01"
OCPILOT_RUN = "4.211"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CATALOG-NEW-BRANCH-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01"
TARGET_URL = "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/proizvodstvennye-lari"
TARGET_SLUG = "proizvodstvennye-lari"
EXPECTED_PARENT_NAME = "Лари"
EXPECTED_PARENT_ID = 88
WRONG_BRAND = "БЗПМ"
CORRECT_BRAND = "ЗПМ"
UTF8_BOM = b"\xef\xbb\xbf"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
PRIOR_DEPLOYMENT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-01"
)
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
CRAWL_DELAY_SEC = 0.35

META_DESCRIPTION_COPY = (
    "Производственные лари ЗПМ из нержавеющей стали для хранения инвентаря и продукции "
    "в цехах, на кухнях и производственных участках."
)

SANITY_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/skladskie-lari",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
]

SUBDIRS = (
    "inventory",
    "crawl-before",
    "crawl-after",
    "admin-evidence",
    "copy",
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


def parse_category_breadcrumb(text: str) -> tuple[str, str]:
    cleaned = text.replace("\t", " ").strip()
    parts = [p.strip() for p in re.split(r"\s*>\s*", cleaned) if p.strip()]
    if not parts:
        return "", ""
    name = re.sub(r"\s+\d+\s*$", "", parts[-1]).strip()
    parent = parts[-2] if len(parts) > 1 else ""
    return name, parent


def load_sitemap_urls() -> set[str]:
    urls: set[str] = set()
    current_csv = Path(
        r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
        r"\SITE-002-PROD-SITEMAP-DELTA-AUDIT-01\current\sitemap-current-urls.csv"
    )
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
            "change_type": "single-category-onboarding-followup",
            "target_url": TARGET_URL,
            "target_page_type": "CATEGORY_PLP_OR_HUB",
            "admin_save_allowed": "exact_category_seo_field_only",
            "db_direct_write_allowed": False,
            "ftp_upload_allowed": False,
            "file_fallback_allowed": False,
            "delete_hide_noindex_allowed": False,
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


def phase1_target_inventory() -> dict[str, Any]:
    row = {
        "url": TARGET_URL,
        "source_run": "4.210 deferred",
        "reason": "category_id unresolved — duplicate name Производственные without parent filter",
        "include": "yes",
        "out_of_scope": "",
    }
    write_csv(DEPLOYMENT_ROOT / "inventory" / "target-url.csv", [row], list(row.keys()))
    write_json(DEPLOYMENT_ROOT / "inventory" / "target-url.json", {"generated_at": utc_now(), "target": row})
    write_text(
        DEPLOYMENT_ROOT / "inventory" / "target-url.md",
        "\n".join(
            [
                "# Target URL inventory",
                "",
                f"- URL: {TARGET_URL}",
                f"- Source: Run 4.210 deferred",
                f"- Reason: {row['reason']}",
                f"- Include: {row['include']}",
            ]
        ),
    )
    return row


def crawl_url(url: str, sitemap_urls: set[str]) -> dict[str, Any]:
    resp = http_get(url)
    body = resp.get("body") or ""
    meta = extract_meta(body) if body else {}
    product_grid = "product-layout" in body or "product-thumb" in body or "product-grid" in body
    return {
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
        "page_category": meta.get("page_category", False),
        "page_product": meta.get("page_product", False),
        "breadcrumb_context": meta.get("h1", ""),
        "product_grid_marker": product_grid,
        "forbidden_bzpm_count": body.count(WRONG_BRAND),
        "zpm_count": body.count(CORRECT_BRAND),
        "sitemap_membership": url.rstrip("/") in sitemap_urls,
        "indexable": "noindex" not in (meta.get("meta_robots", "") + resp.get("x_robots_tag", "")).lower(),
        "error": resp.get("error"),
    }


def phase2_crawl_before(sitemap_urls: set[str]) -> dict[str, Any]:
    row = crawl_url(TARGET_URL, sitemap_urls)
    write_csv(DEPLOYMENT_ROOT / "crawl-before" / "target-before.csv", [row], list(row.keys()))
    write_json(DEPLOYMENT_ROOT / "crawl-before" / "target-before.json", {"captured_at": utc_now(), "row": row})
    write_text(
        DEPLOYMENT_ROOT / "crawl-before" / "target-before.md",
        "\n".join(
            [
                "# Crawl before",
                "",
                f"URL: {TARGET_URL}",
                f"HTTP: {row.get('http_status')}",
                f"page--category: {row.get('page_category')}",
                f"desc_len: {row.get('description_length')}",
                f"БЗПМ count: {row.get('forbidden_bzpm_count')}",
            ]
        ),
    )
    return row


def scrape_admin_categories(page: Any, admin_base: str, token: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen: set[int] = set()
    for page_num in range(1, 10):
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
    return rows


def read_admin_category_fields(page: Any, admin_base: str, token: str, category_id: int) -> dict[str, Any]:
    edit_url = f"{admin_base}index.php?route=catalog/category/edit&user_token={token}&category_id={category_id}"
    page.goto(edit_url, wait_until="domcontentloaded", timeout=120000)
    page.wait_for_timeout(2000)
    parent_sel = page.locator('select[name="parent_id"] option:checked')
    parent_id = ""
    parent_name = ""
    if parent_sel.count():
        parent_name = parent_sel.inner_text().strip()
        parent_id = page.locator('select[name="parent_id"]').input_value()
    seo_url = ""
    seo_loc = page.locator('input[name="category_seo_url[1]"]')
    if seo_loc.count():
        seo_url = seo_loc.input_value().strip()
    return {
        "category_id": category_id,
        "category_name": page.locator('input[name="category_description[1][name]"]').input_value().strip(),
        "parent_id": parent_id,
        "parent_name": parent_name,
        "seo_url": seo_url,
        "meta_title": page.locator('input[name="category_description[1][meta_title]"]').input_value(),
        "meta_description": page.locator('textarea[name="category_description[1][meta_description]"]').input_value(),
        "meta_keywords": page.locator('input[name="category_description[1][meta_keyword]"]').input_value()
        if page.locator('input[name="category_description[1][meta_keyword]"]').count()
        else "",
    }


def resolve_category_id(
    live_row: dict[str, Any],
    admin_categories: list[dict[str, Any]],
    admin_fields: dict[str, Any] | None,
) -> dict[str, Any]:
    h1 = live_row.get("h1", "")
    norm_h1 = normalize_name(h1)
    signals: list[dict[str, Any]] = []

    parent_matches = [
        c
        for c in admin_categories
        if normalize_name(c["name"]) == norm_h1 and normalize_name(c.get("parent", "")) == normalize_name(EXPECTED_PARENT_NAME)
    ]
    for cat in parent_matches:
        signals.append(
            {
                "signal": "admin_list_name_parent",
                "category_id": cat["category_id"],
                "name": cat["name"],
                "parent": cat["parent"],
            }
        )

    if admin_fields:
        signals.append(
            {
                "signal": "admin_edit_parent_id",
                "category_id": admin_fields["category_id"],
                "parent_id": admin_fields.get("parent_id"),
                "parent_name": admin_fields.get("parent_name"),
                "seo_url": admin_fields.get("seo_url"),
            }
        )

    chosen_id: int | None = None
    confidence = "LOW"
    rationale: list[str] = []

    if len(parent_matches) == 1:
        chosen_id = parent_matches[0]["category_id"]
        confidence = "HIGH"
        rationale.append("unique admin list match: name + parent Лари")
    elif admin_fields and str(admin_fields.get("parent_id")) == str(EXPECTED_PARENT_ID):
        chosen_id = admin_fields["category_id"]
        confidence = "HIGH"
        rationale.append(f"admin edit parent_id={EXPECTED_PARENT_ID}")

    if chosen_id and admin_fields and admin_fields["category_id"] == chosen_id:
        if admin_fields.get("seo_url") and admin_fields["seo_url"] != TARGET_SLUG:
            confidence = "MEDIUM"
            rationale.append(f"seo_url mismatch: {admin_fields.get('seo_url')} != {TARGET_SLUG}")
        elif admin_fields.get("seo_url") == TARGET_SLUG:
            rationale.append("seo_url matches target slug")

    if "/lari/" in TARGET_URL and chosen_id:
        rationale.append("live URL path contains /lari/")

    return {
        "category_id": chosen_id,
        "admin_category_name": admin_fields.get("category_name") if admin_fields else (parent_matches[0]["name"] if parent_matches else ""),
        "parent_category": EXPECTED_PARENT_NAME,
        "parent_category_id": EXPECTED_PARENT_ID,
        "seo_url": admin_fields.get("seo_url", "") if admin_fields else "",
        "live_url": TARGET_URL,
        "live_h1": h1,
        "confidence": confidence,
        "signals": signals,
        "rationale": rationale,
        "duplicate_name_note": "Производственные also exists under Шкафы (category_id 130)",
    }


def phase3_resolve(live_row: dict[str, Any]) -> dict[str, Any]:
    from playwright.sync_api import sync_playwright

    admin = parse_production_section(SECRETS_PATH, "OpenCart Admin")
    resolution: dict[str, Any] = {}

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

        candidate_id = 140
        parent_matches = [
            c
            for c in admin_categories
            if normalize_name(c["name"]) == normalize_name(live_row.get("h1", ""))
            and normalize_name(c.get("parent", "")) == normalize_name(EXPECTED_PARENT_NAME)
        ]
        if parent_matches:
            candidate_id = parent_matches[0]["category_id"]

        admin_fields = read_admin_category_fields(page, admin_base, token, candidate_id)
        resolution = resolve_category_id(live_row, admin_categories, admin_fields)
        resolution["current_admin_meta_title"] = admin_fields.get("meta_title", "")
        resolution["current_admin_meta_description"] = admin_fields.get("meta_description", "")
        resolution["current_admin_meta_keywords"] = admin_fields.get("meta_keywords", "")
        resolution["captured_at"] = utc_now()

        browser.close()

    write_json(DEPLOYMENT_ROOT / "manifests" / "category-id-resolution.json", resolution)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "category-id-resolution.md",
        "\n".join(
            [
                "# Category ID resolution",
                "",
                f"- category_id: **{resolution.get('category_id')}**",
                f"- confidence: **{resolution.get('confidence')}**",
                f"- parent: {resolution.get('parent_category')} (id {resolution.get('parent_category_id')})",
                f"- seo_url: `{resolution.get('seo_url')}`",
                "",
                "## Rationale",
                "",
            ]
            + [f"- {r}" for r in resolution.get("rationale", [])]
            + ["", f"Note: {resolution.get('duplicate_name_note')}"]
        ),
    )
    return resolution


def phase_authority_copy_before_dryrun(resolution: dict[str, Any], live_row: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    cid = resolution.get("category_id")
    confidence = resolution.get("confidence")
    authority = "ADMIN_CATEGORY" if cid and confidence == "HIGH" else "SAFE_UNKNOWN"
    planned = "ADMIN_SEO_SAVE" if authority == "ADMIN_CATEGORY" else "DEFERRED_SAFE_UNKNOWN"

    copy_text = META_DESCRIPTION_COPY
    if WRONG_BRAND in copy_text:
        raise RuntimeError("Forbidden brand in copy")
    if CORRECT_BRAND not in copy_text:
        raise RuntimeError("Missing ЗПМ in copy")

    authority_row = {
        "url": TARGET_URL,
        "category_id": cid or "",
        "category_name": resolution.get("admin_category_name", live_row.get("h1", "")),
        "parent_category": resolution.get("parent_category", ""),
        "current_admin_meta_title": resolution.get("current_admin_meta_title", ""),
        "current_admin_meta_description": resolution.get("current_admin_meta_description", ""),
        "current_admin_meta_keywords": resolution.get("current_admin_meta_keywords", ""),
        "live_title": live_row.get("title", ""),
        "live_description": live_row.get("meta_description", ""),
        "authority": authority,
        "planned_method": planned,
        "confidence": confidence,
    }
    authority_rows = [authority_row]

    copy_rows: list[dict[str, Any]] = []
    admin_actions: list[dict[str, Any]] = []
    if planned == "ADMIN_SEO_SAVE":
        before_desc = resolution.get("current_admin_meta_description", "")
        copy_rows.append(
            {
                "url": TARGET_URL,
                "category_id": cid,
                "category_name": authority_row["category_name"],
                "meta_description_before": before_desc,
                "meta_description_after": copy_text,
                "description_length": len(copy_text),
                "contains_zpm": CORRECT_BRAND in copy_text,
                "contains_forbidden_bzpm": WRONG_BRAND in copy_text,
            }
        )
        admin_actions.append(
            {
                "url": TARGET_URL,
                "category_id": cid,
                "category_name": authority_row["category_name"],
                "field": "meta_description",
                "before": before_desc,
                "after": copy_text,
                "expected_verification_url": TARGET_URL,
                "rollback_description": before_desc,
            }
        )

    write_csv(DEPLOYMENT_ROOT / "manifests" / "category-authority-map.csv", authority_rows, list(authority_row.keys()))
    write_json(DEPLOYMENT_ROOT / "manifests" / "category-authority-map.json", authority_rows)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "category-authority-map.md",
        f"# Category authority map\n\n- {TARGET_URL} id={cid} {planned} confidence={confidence}\n",
    )

    write_csv(
        DEPLOYMENT_ROOT / "copy" / "category-meta-copy-final.csv",
        copy_rows,
        list(copy_rows[0].keys()) if copy_rows else ["url", "category_id", "meta_description_after"],
    )
    write_json(DEPLOYMENT_ROOT / "copy" / "category-meta-copy-final.json", copy_rows)
    write_text(
        DEPLOYMENT_ROOT / "copy" / "category-meta-copy-final.md",
        f"# Meta copy\n\n{copy_text}\n\nLength: {len(copy_text)}\n",
    )

    before_rows = []
    if admin_actions:
        before_rows = [
            {
                "category_id": admin_actions[0]["category_id"],
                "category_name": admin_actions[0]["category_name"],
                "current_meta_title": resolution.get("current_admin_meta_title", ""),
                "current_meta_description": admin_actions[0]["before"],
                "current_meta_keywords": resolution.get("current_admin_meta_keywords", ""),
                "planned_new_description": admin_actions[0]["after"],
                "rollback_description": admin_actions[0]["rollback_description"],
            }
        ]
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-seo-before.json", before_rows)
    write_csv(
        DEPLOYMENT_ROOT / "admin-evidence" / "category-seo-before.csv",
        before_rows,
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
        "\n".join(["# Before evidence"] + [f"- id={r['category_id']}" for r in before_rows]),
    )

    write_json(DEPLOYMENT_ROOT / "manifests" / "admin-actions.json", admin_actions)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md",
        "\n".join(
            [
                "# Implementation plan",
                "",
                f"Admin saves: {len(admin_actions)}",
                "Field: meta_description only",
                "Delete/hide/noindex: 0",
                "",
            ]
            + [f"- category_id={a['category_id']} {a['url']}" for a in admin_actions]
        ),
    )

    dry = {
        "target_url": TARGET_URL,
        "category_id": cid,
        "confidence": confidence,
        "admin_save_count": len(admin_actions),
        "forbidden_bzpm_in_copy": 0,
        "delete_hide_noindex": 0,
        "file_uploads": 0,
        "db_writes": 0,
        "examples": admin_actions,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", dry)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "\n".join(
            [
                "# Dry-run",
                "",
                f"category_id: {cid}",
                f"confidence: {confidence}",
                f"admin saves: {len(admin_actions)}",
                f"before: `{admin_actions[0]['before'] if admin_actions else 'n/a'}`",
                f"after: `{admin_actions[0]['after'] if admin_actions else 'n/a'}`",
            ]
        ),
    )

    return authority_rows, copy_rows, admin_actions


def admin_execute_saves(admin_actions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    from playwright.sync_api import sync_playwright

    if not admin_actions:
        return []
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


def phase_verify(before_row: dict[str, Any], admin_actions: list[dict[str, Any]], saves: list[dict[str, Any]]) -> dict[str, Any]:
    sitemap_urls = load_sitemap_urls()
    after_row = crawl_url(TARGET_URL, sitemap_urls)
    write_csv(DEPLOYMENT_ROOT / "crawl-after" / "target-after.csv", [after_row], list(after_row.keys()))
    write_json(DEPLOYMENT_ROOT / "crawl-after" / "target-after.json", {"captured_at": utc_now(), "row": after_row})
    write_text(
        DEPLOYMENT_ROOT / "crawl-after" / "target-after.md",
        "\n".join(
            [
                "# Crawl after",
                "",
                f"desc_len: {after_row.get('description_length')}",
                f"contains ЗПМ: {CORRECT_BRAND in (after_row.get('meta_description') or '')}",
            ]
        ),
    )

    action = admin_actions[0] if admin_actions else {}
    summary = [
        {
            "url": TARGET_URL,
            "category_id": action.get("category_id", ""),
            "description_before": before_row.get("meta_description", ""),
            "description_after": after_row.get("meta_description", ""),
            "description_length": after_row.get("description_length", 0),
            "contains_zpm": CORRECT_BRAND in (after_row.get("meta_description") or ""),
            "contains_bzpm": after_row.get("forbidden_bzpm_count", 0) > 0,
            "title_unchanged": before_row.get("title") == after_row.get("title"),
            "verified": bool(saves and saves[0].get("verified")),
        }
    ]
    write_json(DEPLOYMENT_ROOT / "verification" / "before-after-summary.json", summary)
    write_csv(
        DEPLOYMENT_ROOT / "verification" / "before-after-summary.csv",
        summary,
        list(summary[0].keys()) if summary else [],
    )
    write_text(
        DEPLOYMENT_ROOT / "verification" / "before-after-summary.md",
        f"# Before/after\n\nverified={summary[0].get('verified') if summary else False}\n",
    )

    preservation = verify_preservation()
    write_json(DEPLOYMENT_ROOT / "verification" / "sanity-checks.json", preservation)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "sanity-checks.md",
        "\n".join(["# Sanity checks", "", json.dumps(preservation, ensure_ascii=False, indent=2)]),
    )
    return {"summary": summary, "preservation": preservation, "after_row": after_row}


def run_prepare() -> dict[str, Any]:
    ensure_dirs()
    phase1_target_inventory()
    sitemap_urls = load_sitemap_urls()
    before_row = phase2_crawl_before(sitemap_urls)
    if before_row.get("http_status") != 200 or not before_row.get("page_category") or not before_row.get("indexable"):
        return {"status": "BLOCKED", "reason": "target not live category/indexable", "before": before_row}
    resolution = phase3_resolve(before_row)
    _, _, admin_actions = phase_authority_copy_before_dryrun(resolution, before_row)
    return {
        "status": "READY" if admin_actions else "DEFERRED",
        "category_id": resolution.get("category_id"),
        "confidence": resolution.get("confidence"),
        "admin_actions": len(admin_actions),
        "before_description_length": before_row.get("description_length"),
    }


def run_deploy() -> dict[str, Any]:
    admin_actions = json.loads((DEPLOYMENT_ROOT / "manifests" / "admin-actions.json").read_text(encoding="utf-8"))
    if not admin_actions:
        return {"status": "NO_MUTATION_REQUIRED", "saves": 0}
    saves = admin_execute_saves(admin_actions)
    verified = sum(1 for s in saves if s.get("verified"))
    return {"status": "COMPLETE" if verified == len(saves) else "PARTIAL", "saves": len(saves), "verified": verified, "saves_detail": saves}


def run_verify() -> dict[str, Any]:
    before_data = json.loads((DEPLOYMENT_ROOT / "crawl-before" / "target-before.json").read_text(encoding="utf-8"))
    before_row = before_data["row"]
    admin_actions = json.loads((DEPLOYMENT_ROOT / "manifests" / "admin-actions.json").read_text(encoding="utf-8"))
    saves_path = DEPLOYMENT_ROOT / "admin-evidence" / "category-seo-after.json"
    saves = json.loads(saves_path.read_text(encoding="utf-8")) if saves_path.exists() else []
    return phase_verify(before_row, admin_actions, saves)


def run_all() -> int:
    prep = run_prepare()
    dep = {"status": "SKIPPED", "saves": 0}
    ver: dict[str, Any] = {}
    if prep.get("status") == "READY":
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
