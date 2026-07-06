#!/usr/bin/env python3
"""SITE-002 Production deep category PLP meta edge fix — Run 4.207."""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-SEO-META-EDGE-FIX-01"
OCPILOT_RUN = "4.207"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-BRAND-ZPM-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-SEO-META-EDGE-01"
AUDIT_BASELINE = "SITE-002-SEO-META-FINAL-INVENTORY-01"
WRONG_BRAND = "БЗПМ"
CORRECT_BRAND = "ЗПМ"
UTF8_BOM = b"\xef\xbb\xbf"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
INVENTORY_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-META-FINAL-INVENTORY-01"
)
CATEGORY_MAP_CANDIDATE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-META-CONTENT-FIX-01\admin-evidence\category-full-map.json"
)
CATEGORY_PAGES_MAP = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-META-CONTENT-FIX-01\admin-evidence\category-pages-map.json"
)
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
CRAWL_DELAY_SEC = 0.35

SANITY_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/about",
    "https://bzpm.ru/blog",
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
]

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "admin-evidence",
    "crawl-before",
    "crawl-after",
    "copy",
    "inventory",
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

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: (v or "") for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = True
        elif tag_l == "h1":
            self.in_h1 = True
        elif tag_l == "body":
            self.body_open += 1
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
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "final_url": url, "status_code": None, "x_robots_tag": "", "body": "", "error": str(exc)}


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
        "body_count": parser.body_open,
        "yandex_metrika": any(t in html_text.lower() for t in ("mc.yandex.ru/metrika", "ym(", "yandex.metrika")),
        "yandex_webmaster": "yandex-verification" in html_text.lower(),
    }


def normalize_name(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("\xa0", " ").strip()).lower()


def url_slug(url: str) -> str:
    path = urllib.parse.urlparse(url).path.rstrip("/")
    return path.split("/")[-1] if path else ""


def is_deep_category_plp(url: str, page_type: str) -> bool:
    if page_type != "CATEGORY":
        return False
    parts = [p for p in urllib.parse.urlparse(url).path.split("/") if p]
    return len(parts) >= 4 and parts[0] == "katalog"


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
            "change_type": "deep-category-meta-edge-fix",
            "target_page_type": "CATEGORY",
            "product_pdp_changes_allowed": False,
            "product_generator_change_allowed": False,
            "llms_txt_change_allowed": False,
            "robots_change_allowed": False,
            "sitemap_change_allowed": False,
            "header_footer_change_allowed": False,
            "db_direct_write_allowed": False,
            "admin_save_allowed": "exact_category_seo_fields_only",
            "brand_policy_correct": CORRECT_BRAND,
            "brand_policy_forbidden_public": WRONG_BRAND,
            "domain_bzpm_ru_allowed": True,
            "created_at": utc_now(),
        },
    )


def load_inventory_rows() -> list[dict[str, str]]:
    path = INVENTORY_ROOT / "inventory" / "meta-quality-classification.csv"
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def phase1_edge_gaps() -> list[dict[str, Any]]:
    rows = load_inventory_rows()
    targets: list[dict[str, Any]] = []
    for row in rows:
        url = row["url"].rstrip("/")
        page_type = row.get("page_type", "")
        desc_class = row.get("description_class", "")
        title_class = row.get("title_class", "")
        issue_types: list[str] = []
        include = "no"
        reason = ""

        if page_type == "PRODUCT_PDP":
            reason = "PDP excluded by charter"
        elif page_type in ("HOME", "INFORMATION", "BLOG", "BLOG_CATEGORY", "CATALOG_ROOT", "ROBOTS", "SITEMAP", "LLMS"):
            if desc_class == "DESCRIPTION_MISSING" and page_type == "CATALOG_ROOT":
                reason = "catalog root out of deep PLP scope"
            else:
                reason = f"non-target page_type={page_type}"
        elif page_type == "CATEGORY":
            if desc_class == "DESCRIPTION_MISSING" and is_deep_category_plp(url, page_type):
                issue_types.append("missing_description")
                include = "yes"
                reason = "deep sub-category PLP missing description"
            elif title_class == "TITLE_DUPLICATE" and is_deep_category_plp(url, page_type):
                issue_types.append("duplicate_title")
                include = "yes"
                reason = "deep category duplicate title"
            elif desc_class == "DESCRIPTION_DUPLICATE" and is_deep_category_plp(url, page_type):
                issue_types.append("duplicate_description")
                include = "yes"
                reason = "deep category duplicate description"
            else:
                reason = "category not in edge scope"
        else:
            reason = f"unknown page_type={page_type}"

        targets.append(
            {
                "url": url,
                "page_type": page_type,
                "issue_type": "|".join(issue_types) if issue_types else "",
                "current_title": row.get("title", ""),
                "current_description": row.get("meta_description", ""),
                "current_keywords": row.get("meta_keywords", ""),
                "title_length": row.get("title_length", ""),
                "description_length": row.get("description_length", ""),
                "canonical": row.get("canonical", ""),
                "meta_robots": row.get("meta_robots", ""),
                "x_robots_tag": row.get("x_robots_tag", ""),
                "h1": row.get("h1", ""),
                "category_slug": url_slug(url),
                "category_name": row.get("h1", ""),
                "category_id": "",
                "include": include,
                "reason": reason,
            }
        )

    included = [t for t in targets if t["include"] == "yes"]
    write_csv(
        DEPLOYMENT_ROOT / "inventory" / "edge-gap-targets.csv",
        targets,
        list(targets[0].keys()) if targets else [],
    )
    write_json(DEPLOYMENT_ROOT / "inventory" / "edge-gap-targets.json", {"generated_at": utc_now(), "targets": targets, "included_count": len(included)})
    md = [
        "# Edge gap targets",
        "",
        f"Generated: {utc_now()}",
        f"Total rows: {len(targets)}",
        f"Included: {len(included)}",
        "",
        "## Included URLs",
        "",
    ]
    for t in included:
        md.append(f"- {t['url']} — {t['issue_type']} — {t['reason']}")
    write_text(DEPLOYMENT_ROOT / "inventory" / "edge-gap-targets.md", "\n".join(md))
    return included


def crawl_urls(urls: list[str], label: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for url in urls:
        resp = http_get(url)
        meta = extract_meta(resp["body"]) if resp.get("body") else {}
        parts = [p for p in urllib.parse.urlparse(url).path.split("/") if p]
        is_pdp = len(parts) >= 5 and parts[0] == "katalog"
        is_category = len(parts) >= 3 and parts[0] == "katalog" and not is_pdp
        body = resp.get("body") or ""
        rows.append(
            {
                "url": url,
                "http_status": resp.get("status_code"),
                "final_url": resp.get("final_url"),
                "title": meta.get("title", ""),
                "meta_description": meta.get("meta_description", ""),
                "meta_keywords": meta.get("meta_keywords", ""),
                "h1": meta.get("h1", ""),
                "canonical": meta.get("canonical", ""),
                "meta_robots": meta.get("meta_robots", ""),
                "x_robots_tag": resp.get("x_robots_tag", ""),
                "body_count": meta.get("body_count", 0),
                "contains_forbidden_bzpm": WRONG_BRAND in body,
                "forbidden_bzpm_count": body.count(WRONG_BRAND),
                "contains_zpm": CORRECT_BRAND in body,
                "zpm_count": body.count(CORRECT_BRAND),
                "product_pdp": is_pdp,
                "category_page": is_category,
                "error": resp.get("error"),
            }
        )
        time.sleep(CRAWL_DELAY_SEC)
    write_csv(DEPLOYMENT_ROOT / label / f"edge-meta-{label.split('-')[-1]}.csv", rows, list(rows[0].keys()) if rows else [])
    write_json(DEPLOYMENT_ROOT / label / f"edge-meta-{label.split('-')[-1]}.json", {"captured_at": utc_now(), "rows": rows})
    md = [f"# Edge meta {label}", "", f"Captured: {utc_now()}", f"Count: {len(rows)}", ""]
    for row in rows:
        md.append(f"- {row['url']} — {row.get('http_status')} — desc_len={len(row.get('meta_description') or '')}")
    write_text(DEPLOYMENT_ROOT / label / f"edge-meta-{label.split('-')[-1]}.md", "\n".join(md))
    return rows


def parse_category_breadcrumb(text: str) -> tuple[str, str]:
    cleaned = text.replace("\t", " ").strip()
    parts = [p.strip() for p in re.split(r"\s*>\s*", cleaned) if p.strip()]
    if not parts:
        return "", ""
    name = re.sub(r"\s+\d+\s*$", "", parts[-1]).strip()
    parent = parts[-2] if len(parts) > 1 else ""
    return name, parent


def load_category_map_seed() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if CATEGORY_PAGES_MAP.exists():
        for row in json.loads(CATEGORY_PAGES_MAP.read_text(encoding="utf-8")):
            name, parent = parse_category_breadcrumb(row["text"])
            rows.append(
                {
                    "category_id": row["category_id"],
                    "name": name,
                    "parent": parent,
                    "text": row["text"],
                }
            )
    elif CATEGORY_MAP_CANDIDATE.exists():
        for row in json.loads(CATEGORY_MAP_CANDIDATE.read_text(encoding="utf-8")):
            name, parent = parse_category_breadcrumb(row["text"])
            rows.append({"category_id": row["category_id"], "name": name, "parent": parent, "text": row["text"]})
    return rows


def scrape_admin_categories(page: Any, admin_base: str, token: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen: set[int] = set()
    page_num = 1
    while page_num <= 6:
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
        page_num += 1
    seed = load_category_map_seed()
    for row in seed:
        if row["category_id"] not in seen:
            rows.append(row)
            seen.add(row["category_id"])
    return rows


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
    edit_url = f"{admin_base}index.php?route=catalog/category/edit&user_token={token}&category_id={category_id}"
    page.goto(edit_url, wait_until="domcontentloaded", timeout=120000)
    page.wait_for_timeout(1500)
    loc = page.locator('input[name*="keyword"]')
    if loc.count() == 0:
        return ""
    return loc.first.input_value().strip()


def build_name_index(admin_categories: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    index: dict[str, list[dict[str, Any]]] = {}
    for cat in admin_categories:
        key = normalize_name(cat["name"])
        index.setdefault(key, []).append(cat)
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

    return None, "SAFE_UNKNOWN", "LOW"


def generate_description(name: str, url: str) -> str:
    path = urllib.parse.urlparse(url).path.lower()
    label = name.strip() or url_slug(url).replace("-", " ").title()
    if any(x in path for x in ("moechnye-vanny", "rukomoynik", "kotlomoyk", "komplektuyuschie-dlya-vann")):
        base = (
            f"{label} ЗПМ из нержавеющей стали для моечных зон, кухонь и пищевых производств. "
            "Подбор по конструкции, размерам и назначению."
        )
    elif any(x in path for x in ("telezhk", "protivni", "shpilk")):
        base = (
            f"{label} ЗПМ для кухни, цеха и общепита. "
            "Тележки и аксессуары из нержавеющей стали для хранения и перемещения продукции."
        )
    elif "stoly" in path:
        base = (
            f"{label} ЗПМ для профессиональных кухонь и производственных зон. "
            "Серийные столы из нержавеющей стали с разными параметрами и исполнением."
        )
    elif any(x in path for x in ("polki", "stellazh", "podtovarnik", "podstavk", "shkafy")):
        base = (
            f"{label} ЗПМ из нержавеющей стали для общепита и пищевых производств. "
            "Подберите изделия по назначению, размерам и исполнению."
        )
    elif "zonty" in path:
        base = (
            f"{label} ЗПМ из нержавеющей стали для вентиляции профессиональных кухонь и цехов. "
            "Подбор по типу, размерам и комплектации."
        )
    else:
        base = (
            f"{label} ЗПМ из нержавеющей стали для общепита и пищевых производств. "
            "Подберите изделия по назначению, размерам и исполнению."
        )
    if WRONG_BRAND in base:
        raise RuntimeError(f"Forbidden brand in generated copy for {url}")
    if len(base) < 120:
        base = base.rstrip(".") + ". Надёжные решения для ресторанов, столовых и производств."
    if len(base) > 165:
        base = base[:162].rsplit(" ", 1)[0] + "."
    return base


def phase_authority_and_copy(
    targets: list[dict[str, Any]],
    before_rows: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise RuntimeError("playwright required for authority mapping") from exc

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

        for target in targets:
            url = target["url"].rstrip("/")
            live = before_by_url.get(url, {})
            h1 = live.get("h1") or target.get("h1") or target.get("category_name") or ""
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
                    "current_admin_meta_description": target.get("current_description", ""),
                    "live_title": live.get("title", target.get("current_title", "")),
                    "live_description": live.get("meta_description", target.get("current_description", "")),
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
                authority_rows[-1]["authority"] = "SAFE_UNKNOWN"
                continue

            current_title = page.locator('input[name="category_description[1][meta_title]"]').input_value()
            current_desc = page.locator('textarea[name="category_description[1][meta_description]"]').input_value()
            cat_name = page.locator('input[name="category_description[1][name]"]').input_value().strip()
            authority_rows[-1]["current_admin_meta_title"] = current_title
            authority_rows[-1]["current_admin_meta_description"] = current_desc
            authority_rows[-1]["category_name"] = cat_name or h1

            new_desc = generate_description(cat_name or h1, url)
            new_title = current_title
            if target.get("issue_type", "").startswith("duplicate") and current_title:
                if " | " not in current_title and len(current_title) < 55:
                    new_title = f"{cat_name or h1} — нейтральное оборудование | ООО «ЗПМ»"

            copy_rows.append(
                {
                    "url": url,
                    "category_id": cid,
                    "category_name": cat_name or h1,
                    "meta_title_before": current_title,
                    "meta_description_before": current_desc,
                    "meta_title_after": new_title,
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
                    "field": "meta_description",
                    "before": current_desc,
                    "after": new_desc,
                    "meta_title_before": current_title,
                    "meta_title_after": new_title,
                    "expected_verification_url": url,
                    "rollback_description": current_desc,
                    "rollback_title": current_title,
                }
            )

        browser.close()

    write_csv(DEPLOYMENT_ROOT / "manifests" / "category-authority-map.csv", authority_rows, list(authority_rows[0].keys()) if authority_rows else [])
    write_json(DEPLOYMENT_ROOT / "manifests" / "category-authority-map.json", authority_rows)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "category-authority-map.md",
        "\n".join([f"# Category authority map", "", f"Mapped: {utc_now()}", ""] + [f"- {r['url']} id={r['category_id']} {r['planned_method']}" for r in authority_rows]),
    )
    write_csv(DEPLOYMENT_ROOT / "copy" / "category-meta-copy-final.csv", copy_rows, list(copy_rows[0].keys()) if copy_rows else [])
    write_json(DEPLOYMENT_ROOT / "copy" / "category-meta-copy-final.json", copy_rows)
    write_json(DEPLOYMENT_ROOT / "manifests" / "admin-actions.json", admin_actions)
    write_json(DEPLOYMENT_ROOT / "manifests" / "file-actions.json", [])
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md",
        "\n".join(
            [
                "# Implementation plan",
                "",
                f"Generated: {utc_now()}",
                f"Admin category SEO saves: {len(admin_actions)}",
                "File fallback: 0",
                "Product PDP: 0",
                "",
            ]
        ),
    )
    return authority_rows, copy_rows, admin_actions


def capture_admin_before(admin_actions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return []
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
            if page.locator('textarea[name="category_description[1][meta_description]"]').count() == 0:
                rows.append({"category_id": cid, "error": "form not found"})
                continue
            rows.append(
                {
                    "category_id": cid,
                    "name": page.locator('input[name="category_description[1][name]"]').input_value().strip(),
                    "current_meta_title": page.locator('input[name="category_description[1][meta_title]"]').input_value(),
                    "current_meta_description": page.locator('textarea[name="category_description[1][meta_description]"]').input_value(),
                    "planned_new_description": action["after"],
                    "rollback_description": action["rollback_description"],
                    "rollback_title": action["rollback_title"],
                }
            )
        browser.close()
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-seo-before.json", rows)
    write_csv(
        DEPLOYMENT_ROOT / "admin-evidence" / "category-seo-before.csv",
        rows,
        ["category_id", "name", "current_meta_title", "current_meta_description", "planned_new_description", "rollback_description", "rollback_title"],
    )
    return rows


def phase_dry_run(targets: list[dict[str, Any]], admin_actions: list[dict[str, Any]], copy_rows: list[dict[str, Any]]) -> None:
    forbidden = [r for r in copy_rows if r.get("contains_forbidden_bzpm")]
    pdp = [t for t in targets if t.get("page_type") == "PRODUCT_PDP"]
    payload = {
        "target_count": len(targets),
        "admin_save_count": len(admin_actions),
        "deferred_count": len(targets) - len(admin_actions),
        "forbidden_bzpm_in_copy": len(forbidden),
        "product_pdp_in_targets": len(pdp),
        "file_uploads": 0,
        "examples": admin_actions[:5],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "\n".join(
            [
                "# Dry-run",
                "",
                f"Generated: {utc_now()}",
                f"Targets: {len(targets)}",
                f"Admin saves: {len(admin_actions)}",
                f"Deferred: {len(targets) - len(admin_actions)}",
                f"Forbidden БЗПМ in copy: {len(forbidden)}",
                f"PDP in targets: {len(pdp)}",
                "File uploads: 0",
                "Header/footer: 0",
                "DB writes: 0",
            ]
        ),
    )
    if forbidden or pdp:
        raise RuntimeError("Dry-run gate failed: forbidden brand or PDP in targets")


def admin_execute_saves(admin_actions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
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
            raise RuntimeError("Admin login failed for deploy")
        for action in admin_actions:
            cid = action["category_id"]
            edit_url = f"{admin_base}index.php?route=catalog/category/edit&user_token={token}&category_id={cid}"
            page.goto(edit_url, wait_until="domcontentloaded", timeout=120000)
            page.wait_for_timeout(2000)
            before_desc = page.locator('textarea[name="category_description[1][meta_description]"]').input_value()
            before_title = page.locator('input[name="category_description[1][meta_title]"]').input_value()
            if action.get("meta_title_after") and action["meta_title_after"] != before_title:
                page.fill('input[name="category_description[1][meta_title]"]', action["meta_title_after"])
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
    url_count = 0
    sitemap_valid = False
    if sitemap["status_code"] == 200:
        try:
            root = ET.fromstring(sitemap["body"])
            url_count = len(root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"))
            sitemap_valid = url_count > 0
        except ET.ParseError:
            pass
    llms_body = llms.get("body", "").encode("utf-8") if llms.get("body") else b""
    home = http_get("https://bzpm.ru/")
    home_meta = extract_meta(home["body"]) if home.get("body") else {}
    return {
        "robots_status": robots["status_code"],
        "sitemap_status": sitemap["status_code"],
        "sitemap_valid": sitemap_valid,
        "sitemap_url_count": url_count,
        "llms_status": llms["status_code"],
        "llms_utf8_bom": llms_body.startswith(UTF8_BOM),
        "llms_forbidden_bzpm": WRONG_BRAND in (llms.get("body") or ""),
        "home_body_count": home_meta.get("body_count"),
        "home_yandex_metrika": home_meta.get("yandex_metrika"),
        "home_yandex_webmaster": home_meta.get("yandex_webmaster"),
    }


def phase_quality_recheck(before_rows: list[dict[str, Any]], after_rows: list[dict[str, Any]]) -> dict[str, Any]:
    before_missing = sum(1 for r in before_rows if not (r.get("meta_description") or "").strip())
    after_missing = sum(1 for r in after_rows if not (r.get("meta_description") or "").strip())
    before_descs = [r.get("meta_description") or "" for r in before_rows if r.get("meta_description")]
    after_descs = [r.get("meta_description") or "" for r in after_rows if r.get("meta_description")]
    dup_before = sum(1 for _, c in Counter(before_descs).items() if c > 1)
    dup_after = sum(1 for _, c in Counter(after_descs).items() if c > 1)
    bzpm = sum(r.get("forbidden_bzpm_count", 0) for r in after_rows)
    result = {
        "missing_descriptions_before": before_missing,
        "missing_descriptions_after": after_missing,
        "duplicate_descriptions_before": dup_before,
        "duplicate_descriptions_after": dup_after,
        "forbidden_bzpm_count": bzpm,
        "checked_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "edge-quality-recheck.json", result)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "edge-quality-recheck.md",
        "\n".join(
            [
                "# Edge quality recheck",
                "",
                f"Checked: {utc_now()}",
                f"Missing descriptions before/after: {before_missing}/{after_missing}",
                f"Duplicate descriptions before/after: {dup_before}/{dup_after}",
                f"Forbidden БЗПМ count: {bzpm}",
            ]
        ),
    )
    return result


def run_prepare() -> dict[str, Any]:
    ensure_dirs()
    targets = phase1_edge_gaps()
    before_rows = crawl_urls([t["url"] for t in targets], "crawl-before")
    excluded = [r for r in before_rows if r.get("product_pdp")]
    if excluded:
        targets = [t for t in targets if t["url"].rstrip("/") not in {r["url"].rstrip("/") for r in excluded}]
        write_json(DEPLOYMENT_ROOT / "inventory" / "excluded-pdp.json", excluded)
    critical_bzpm = [r for r in before_rows if r.get("contains_forbidden_bzpm")]
    if critical_bzpm:
        write_json(DEPLOYMENT_ROOT / "inventory" / "critical-bzpm.json", critical_bzpm)
    _, copy_rows, admin_actions = phase_authority_and_copy(targets, before_rows)
    before_evidence = capture_admin_before(admin_actions)
    phase_dry_run(targets, admin_actions, copy_rows)
    return {"targets": len(targets), "admin_actions": len(admin_actions), "before_evidence": len(before_evidence)}


def run_deploy() -> dict[str, Any]:
    admin_actions = json.loads((DEPLOYMENT_ROOT / "manifests" / "admin-actions.json").read_text(encoding="utf-8"))
    if not admin_actions:
        return {"status": "SKIPPED", "saves": 0}
    saves = admin_execute_saves(admin_actions)
    verified = sum(1 for s in saves if s.get("verified"))
    return {"status": "COMPLETE" if verified == len(saves) else "PARTIAL", "saves": len(saves), "verified": verified}


def run_verify() -> dict[str, Any]:
    admin_actions = json.loads((DEPLOYMENT_ROOT / "manifests" / "admin-actions.json").read_text(encoding="utf-8"))
    urls = [a["url"] for a in admin_actions] + SANITY_URLS
    after_rows = crawl_urls(urls, "crawl-after")
    before_path = DEPLOYMENT_ROOT / "crawl-before" / "edge-meta-before.json"
    before_rows = json.loads(before_path.read_text(encoding="utf-8"))["rows"] if before_path.exists() else []
    target_urls = {a["url"].rstrip("/") for a in admin_actions}
    before_targets = [r for r in before_rows if r["url"].rstrip("/") in target_urls]
    after_targets = [r for r in after_rows if r["url"].rstrip("/") in target_urls]
    summary = []
    for action in admin_actions:
        url = action["url"].rstrip("/")
        b = next((r for r in before_targets if r["url"].rstrip("/") == url), {})
        a = next((r for r in after_targets if r["url"].rstrip("/") == url), {})
        summary.append(
            {
                "url": url,
                "description_before": b.get("meta_description", ""),
                "description_after": a.get("meta_description", ""),
                "verified": bool(a.get("meta_description") and action["after"][:40] in a.get("meta_description", "")),
            }
        )
    write_json(DEPLOYMENT_ROOT / "verification" / "before-after-summary.json", summary)
    write_csv(
        DEPLOYMENT_ROOT / "verification" / "before-after-summary.csv",
        summary,
        ["url", "description_before", "description_after", "verified"],
    )
    preservation = verify_preservation()
    write_json(DEPLOYMENT_ROOT / "verification" / "preservation.json", preservation)
    recheck = phase_quality_recheck(before_targets, after_targets)
    return {"preservation": preservation, "recheck": recheck, "verified_count": sum(1 for s in summary if s["verified"])}


def run_wave2() -> dict[str, Any]:
    """Restore wrong parent save and remediate deferred targets."""
    rollback_actions = [
        {
            "category_id": 83,
            "url": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye",
            "after": "Полки для общепита и производств: настенные, угловые, открытые и закрытые.",
            "meta_title_after": "Полки | ООО «ЗПМ»",
            "rollback_description": "Полки для общепита и производств: настенные, угловые, открытые и закрытые.",
            "rollback_title": "Полки | ООО «ЗПМ»",
        }
    ]
    rollback_saves = admin_execute_saves(rollback_actions)
    prep = run_prepare()
    dep = run_deploy()
    ver = run_verify()
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "wave2-summary.json",
        {"rollback": rollback_saves, "prepare": prep, "deploy": dep, "verify": ver, "finished_at": utc_now()},
    )
    return {"rollback": rollback_saves, "prepare": prep, "deploy": dep, "verify": ver}


def run_all() -> int:
    prep = run_prepare()
    dep = run_deploy()
    ver = run_verify()
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "run-summary.json",
        {"operation_id": OPERATION_ID, "prepare": prep, "deploy": dep, "verify": ver, "finished_at": utc_now()},
    )
    print(json.dumps({"prepare": prep, "deploy": dep, "verify": ver}, ensure_ascii=False, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--phase", choices=("prepare", "deploy", "verify", "all", "wave2"), default="all")
    args = parser.parse_args()
    if args.phase == "prepare":
        print(json.dumps(run_prepare(), ensure_ascii=False, indent=2))
        return 0
    if args.phase == "deploy":
        print(json.dumps(run_deploy(), ensure_ascii=False, indent=2))
        return 0
    if args.phase == "verify":
        print(json.dumps(run_verify(), ensure_ascii=False, indent=2))
        return 0
    if args.phase == "wave2":
        print(json.dumps(run_wave2(), ensure_ascii=False, indent=2))
        return 0
    return run_all()


if __name__ == "__main__":
    sys.exit(main())
