#!/usr/bin/env python3
"""SITE-002 Production UX task intake — read-only (Run 4.217)."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import html
import io
import json
import random
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-UX-TASK-INTAKE-01"
OCPILOT_RUN = "4.217"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE = "SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)

EXTRA_INFO_ATTR = "Дополнительные сведения"
EXAMPLE_PDP = (
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye/"
    "polki-dlya-gastoemkostey/derzhatel-dlya-gastroemkostey-pg-10-3-900h330h40-gn-1-6-5-sht"
)

TASK01_URLS = [
    ("home", "https://bzpm.ru/"),
    ("katalog_root", "https://bzpm.ru/katalog"),
    ("neutral_hub", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie"),
    ("lari_parent", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari"),
    ("lari_skladskie", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/skladskie-lari"),
    ("lari_proizvodstvennye", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/proizvodstvennye-lari"),
    ("konditerskiy_parent", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/konditerskiy-inventar"),
    ("konditerskiy_formy", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/konditerskiy-inventar/formy-konditerskie"),
]

FTP_TASK01 = [
    "/public_html/catalog/view/theme/default/template/common/home.twig",
    "/public_html/catalog/view/theme/default/template/product/category.twig",
    "/public_html/catalog/controller/common/home.php",
    "/public_html/catalog/controller/product/category.php",
    "/public_html/catalog/view/theme/default/template/sections/catalogsections.twig",
    "/public_html/system/library/zpm/category_visibility.php",
    "/public_html/catalog/view/theme/default/stylesheet/stylesheet.css",
    "/public_html/catalog/view/theme/default/stylesheet/style.css",
    "/public_html/catalog/view/javascript/common.js",
    "/public_html/catalog/view/javascript/main.js",
    "/public_html/storage/modification/catalog/controller/common/home.php",
    "/public_html/storage/modification/catalog/controller/product/category.php",
    "/public_html/storage/modification/catalog/view/theme/default/template/common/home.twig",
    "/public_html/storage/modification/catalog/view/theme/default/template/product/category.twig",
]

FTP_TASK02 = [
    "/public_html/catalog/controller/product/product.php",
    "/public_html/catalog/view/theme/default/template/product/product.twig",
    "/public_html/catalog/model/catalog/product.php",
    "/public_html/storage/modification/catalog/controller/product/product.php",
    "/public_html/storage/modification/catalog/view/theme/default/template/product/product.twig",
    "/public_html/storage/modification/catalog/model/catalog/product.php",
]

SUBDIRS = (
    "http",
    "source-readonly",
    "task-01-new-sections",
    "task-02-extra-info",
    "authority-map",
    "implementation-options",
    "future-notes",
    "verification",
    "manifests",
    "reports",
    "logs",
)


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.in_h1 = False
        self.title = ""
        self.h1_list: list[str] = []
        self.meta: dict[str, str] = {}
        self.body_classes = ""
        self.links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {k: (v or "") for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = True
        if tag_l == "h1":
            self.in_h1 = True
        if tag_l == "meta":
            name = ad.get("name") or ad.get("property") or ""
            content = ad.get("content", "")
            if name:
                self.meta[name.lower()] = content
        if tag_l == "body":
            self.body_classes = ad.get("class", "")
        if tag_l == "link" and ad.get("rel") == "canonical":
            self.links.append({"rel": "canonical", "href": ad.get("href", "")})

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False
        if tag.lower() == "h1":
            self.in_h1 = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if self.in_h1:
            self.h1_list.append(data.strip())


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


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow(row)


def parse_production_section(path: Path, subsection: str | None = None) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    if subsection:
        sub = re.search(rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
        if not sub:
            raise RuntimeError(f"Subsection {subsection!r} not found")
        block = sub.group(1)
    fields: dict[str, str] = {}
    current: str | None = None
    for line in block.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            current = s[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current, "")
            continue
        if current:
            fields[current] = s
    return fields


def http_get(url: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xml,*/*", "Cache-Control": "no-cache"},
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = resp.read()
            charset = resp.headers.get_content_charset() or "utf-8"
            text = body.decode(charset, errors="replace")
            return {
                "url": url,
                "final_url": resp.geturl(),
                "status": resp.status,
                "headers": dict(resp.headers.items()),
                "body": text,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        raw = exc.read() if exc.fp else b""
        charset = exc.headers.get_content_charset() if exc.headers else None
        text = raw.decode(charset or "utf-8", errors="replace")
        return {
            "url": url,
            "final_url": exc.geturl(),
            "status": exc.code,
            "headers": dict(exc.headers.items()) if exc.headers else {},
            "body": text,
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "final_url": url, "status": None, "headers": {}, "body": "", "error": str(exc)}


def extract_page_meta(html_text: str) -> dict[str, Any]:
    p = MetaParser()
    try:
        p.feed(html_text)
    except Exception:
        pass
    canonical = next((l["href"] for l in p.links if l["rel"] == "canonical"), "")
    return {
        "title": html.unescape(p.title.strip()),
        "meta_description": p.meta.get("description", ""),
        "h1": " | ".join(h for h in p.h1_list if h),
        "body_classes": p.body_classes,
        "canonical": canonical,
        "meta_robots": p.meta.get("robots", ""),
    }


def parse_hub_cards(html_text: str) -> list[dict[str, str]]:
    cards: list[dict[str, str]] = []
    for block in re.findall(r'<a[^>]+class="[^"]*zpm-cat-card[^"]*"[^>]*>.*?</a>', html_text, re.DOTALL | re.I):
        href_m = re.search(r'href="([^"]+)"', block)
        name_m = re.search(r'class="[^"]*zpm-cat-card__title[^"]*"[^>]*>([^<]+)<', block)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', block)
        if href_m:
            cards.append(
                {
                    "name": name_m.group(1).strip() if name_m else "",
                    "href": href_m.group(1),
                    "img": img_m.group(1) if img_m else "",
                    "css_classes": "zpm-cat-card zpm-cat-card__title zpm-cat-card__img",
                }
            )
    return cards


def mentions_lari_konditerskiy(html_text: str) -> dict[str, bool]:
    low = html_text.lower()
    return {
        "lari": "/lari" in low or "лари" in low,
        "konditerskiy": "konditerskiy-inventar" in low or "кондитерский инвентарь" in low,
        "formy_konditerskie": "formy-konditerskie" in low or "формы кондитерские" in low,
    }


def parse_pdp_extra_info(html_text: str) -> dict[str, Any]:
    has_attr = EXTRA_INFO_ATTR in html_text
    value = ""
    group = ""
    row_html = ""
    toggle_pos = html_text.find("product-content__specs-toggle-wrap")
    attr_pos = html_text.find(EXTRA_INFO_ATTR)
    before_toggle = attr_pos < toggle_pos if attr_pos >= 0 and toggle_pos >= 0 else None
    m = re.search(
        rf'<div class="spec-table__key"><span>{re.escape(EXTRA_INFO_ATTR)}</span></div>\s*'
        r'<div class="spec-table__val[^"]*">(.*?)</div>',
        html_text,
        re.DOTALL | re.I,
    )
    if m:
        value = re.sub(r"<[^>]+>", " ", m.group(1))
        value = re.sub(r"\s+", " ", html.unescape(value)).strip()
        start = max(0, m.start() - 200)
        row_html = html_text[start : m.end() + 100]
    grp_m = re.search(
        rf'class="[^"]*spec-table__group[^"]*"[^>]*>.*?{re.escape(EXTRA_INFO_ATTR)}',
        html_text,
        re.DOTALL | re.I,
    )
    if grp_m:
        gm = re.search(r"<h\d[^>]*>([^<]+)</h", grp_m.group(0))
        if gm:
            group = gm.group(1).strip()
    specs_visible = 'class="product-content__specs' in html_text and "hidden" not in html_text[
        html_text.find("product-content__specs") : html_text.find("product-content__specs") + 80
    ]
    return {
        "has_extra_info": has_attr,
        "value": value,
        "value_length": len(value),
        "attribute_group": group,
        "row_before_specs_toggle": before_toggle,
        "specs_toggle_wrap_present": toggle_pos >= 0,
        "row_html_snippet": row_html[:1500],
        "specs_section_visible_by_default": specs_visible,
    }


def is_product_pdp_url(url: str) -> bool:
    parts = urllib.parse.urlparse(url).path.strip("/").split("/")
    return len(parts) >= 5 and parts[0] == "katalog"


def fetch_sitemap_product_urls(limit: int | None = None) -> list[str]:
    resp = http_get("https://bzpm.ru/sitemap.xml")
    if not resp["body"]:
        return []
    root = ET.fromstring(resp["body"])
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls: list[str] = []
    for loc in root.findall(".//sm:loc", ns):
        if loc.text:
            urls.append(loc.text.strip())
    if not urls:
        for loc in root.iter():
            if loc.tag.endswith("loc") and loc.text:
                urls.append(loc.text.strip())
    pdps = [u for u in urls if is_product_pdp_url(u)]
    if limit and len(pdps) > limit:
        random.seed(42)
        pdps = random.sample(pdps, limit)
    return pdps


def ftp_connect() -> ftplib.FTP:
    creds = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], int(creds.get("port") or 21), timeout=120)
    ftp.login(creds["username"], creds["password"])
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> tuple[bytes | None, str | None]:
    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {remote}", buf.write)
        return buf.getvalue(), None
    except Exception as exc:  # noqa: BLE001
        return None, str(exc)


def local_ftp_name(remote: str) -> str:
    return remote.strip("/").replace("/", "__")


def analyze_source_file(remote: str, content: str) -> dict[str, Any]:
    layer = "MODIFICATION" if "/storage/modification/" in remote else "LIVE"
    source_type = "SAFE UNKNOWN"
    notes: list[str] = []
    if remote.endswith(".twig"):
        source_type = "TWIG"
    elif remote.endswith(".php") and "/controller/" in remote:
        source_type = "PHP_CONTROLLER"
    elif remote.endswith(".php") and "/model/" in remote:
        source_type = "PHP_MODEL"
    elif remote.endswith(".php") and "category_visibility" in remote:
        source_type = "HARDCODED"
    if "buildHomepageCategoryCards" in content:
        notes.append("buildHomepageCategoryCards drives homepage zpm-cat-card tiles")
    if "neutral_hub_branch_ids" in content:
        notes.append("neutral_hub_branch_ids array controls hub/home branch tiles")
    if "getProductAttributes" in content:
        notes.append("getProductAttributes loads PDP attribute_groups")
    if "attribute_groups" in content and ".twig" in remote:
        notes.append("Twig iterates attribute_groups for spec-table")
    if "product-content__specs-toggle-wrap" in content:
        notes.append("specs toggle wrap anchor present")
    if "data-product-specs-toggle" in content:
        notes.append("JS hook data-product-specs-toggle for specs expand")
    return {
        "remote_path": remote,
        "layer": layer,
        "source_type": source_type,
        "size_bytes": len(content.encode("utf-8")),
        "notes": notes,
    }


def ensure_dirs() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "mode": "read-only-intake",
            "production_url": PRODUCTION_URL,
            "beget_full_backup_confirmed_by_operator": True,
            "production_mutation_allowed": False,
            "image_generation_allowed": False,
            "ftp_upload_allowed": False,
            "admin_save_allowed": False,
            "db_write_allowed": False,
            "cache_clear_allowed": False,
            "template_patch_allowed": False,
            "css_patch_allowed": False,
            "future_server_monitor_migration_note": "deferred",
            "baseline": BASELINE,
            "ocpilot_run": OCPILOT_RUN,
            "created_at": utc_now(),
        },
    )


def phase1_public_inventory() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for key, url in TASK01_URLS:
        resp = http_get(url)
        body = resp.get("body", "")
        meta = extract_page_meta(body) if body else {}
        cards = parse_hub_cards(body) if body else []
        mentions = mentions_lari_konditerskiy(body) if body else {}
        row = {
            "page_key": key,
            "url": url,
            "final_url": resp.get("final_url", url),
            "http_status": resp.get("status"),
            "title": meta.get("title", ""),
            "meta_description": meta.get("meta_description", ""),
            "h1": meta.get("h1", ""),
            "body_classes": meta.get("body_classes", ""),
            "category_cards_count": len(cards),
            "category_cards": cards,
            "mentions_lari": mentions.get("lari", False),
            "mentions_konditerskiy": mentions.get("konditerskiy", False),
            "mentions_formy_konditerskie": mentions.get("formy_konditerskie", False),
            "error": resp.get("error"),
        }
        rows.append(row)
        if body:
            write_text(DEPLOYMENT_ROOT / "http" / f"{key}.html", body)
        time.sleep(0.3)
    fields = [
        "page_key", "url", "http_status", "title", "meta_description", "h1",
        "body_classes", "category_cards_count", "mentions_lari", "mentions_konditerskiy",
        "mentions_formy_konditerskie", "error",
    ]
    csv_rows = [{k: row.get(k, "") for k in fields} for row in rows]
    write_csv(DEPLOYMENT_ROOT / "task-01-new-sections" / "public-page-inventory.csv", csv_rows, fields)
    write_json(DEPLOYMENT_ROOT / "task-01-new-sections" / "public-page-inventory.json", {"generated_at": utc_now(), "pages": rows})
    md = ["# Task 01 — Public page inventory", "", f"Generated: {utc_now()}", ""]
    for row in rows:
        md += [
            f"## {row['page_key']}",
            f"- URL: {row['url']}",
            f"- HTTP: {row.get('http_status')}",
            f"- Title: {row.get('title', '')}",
            f"- H1: {row.get('h1', '')}",
            f"- Body classes: `{row.get('body_classes', '')}`",
            f"- Category cards: {row.get('category_cards_count', 0)}",
            f"- Mentions lari: {row.get('mentions_lari')}",
            f"- Mentions konditerskiy: {row.get('mentions_konditerskiy')}",
            "",
        ]
    write_text(DEPLOYMENT_ROOT / "task-01-new-sections" / "public-page-inventory.md", "\n".join(md))
    return rows


def phase2_task01_source(ftp: ftplib.FTP) -> list[dict[str, Any]]:
    authority: list[dict[str, Any]] = []
    for remote in FTP_TASK01:
        data, err = ftp_download(ftp, remote)
        local = DEPLOYMENT_ROOT / "source-readonly" / local_ftp_name(remote)
        content = ""
        if data:
            local.parent.mkdir(parents=True, exist_ok=True)
            local.write_bytes(data)
            content = data.decode("utf-8", errors="replace")
        analysis = analyze_source_file(remote, content) if content else {
            "remote_path": remote, "layer": "MISSING", "source_type": "SAFE UNKNOWN", "notes": [err or "not found"],
        }
        block_name = ""
        page = ""
        risk = "LOW"
        generation = "SAFE UNKNOWN"
        if "home.php" in remote:
            page = "homepage"
            block_name = "catalogsections / zpm-cat-card grid"
            generation = "data-driven via CategoryVisibility::buildHomepageCategoryCards"
            risk = "MEDIUM"
        elif "category.php" in remote and "controller" in remote:
            page = "category PLP / neutral hub"
            block_name = "child category tiles on hub PLP"
            generation = "data-driven via category_visibility branch IDs + category images"
            risk = "MEDIUM"
        elif "catalogsections.twig" in remote:
            page = "homepage"
            block_name = "zpm-cat-card markup loop"
            generation = "Twig foreach categories from controller"
        elif "category_visibility.php" in remote:
            page = "homepage + neutral hub"
            block_name = "neutral_hub_branch_ids whitelist"
            generation = "HARDCODED PHP array + admin category image fields"
            risk = "HIGH — wrong ID breaks tile set"
        elif "category.twig" in remote:
            page = "category PLP"
            block_name = "subcategory cards / product grid"
        authority.append({
            "page": page,
            "visible_block": block_name,
            "source_file": remote,
            "source_type": analysis.get("source_type", "SAFE UNKNOWN"),
            "layer": analysis.get("layer", ""),
            "how_generated": generation,
            "add_lari_konditerskiy_likely": "category_visibility.php branch IDs + admin category images (hybrid A+C)",
            "image_pattern": "image/cache/catalog/Category-image/{slug}-300x300.webp from OpenCart category image",
            "risk_level": risk,
            "exists": data is not None,
            "sha256": sha256_bytes(data) if data else "",
            "notes": "; ".join(analysis.get("notes", [])),
        })
    fields = [
        "page", "visible_block", "source_file", "source_type", "layer", "how_generated",
        "add_lari_konditerskiy_likely", "image_pattern", "risk_level", "exists",
    ]
    write_csv(DEPLOYMENT_ROOT / "task-01-new-sections" / "source-authority-map.csv", authority, fields)
    write_json(DEPLOYMENT_ROOT / "task-01-new-sections" / "source-authority-map.json", {"files": authority})
    md = ["# Task 01 — Source authority map", ""]
    for a in authority:
        md.append(f"### {a['source_file']}")
        md.append(f"- Page/block: {a.get('page')} / {a.get('visible_block')}")
        md.append(f"- Type: {a.get('source_type')} ({a.get('layer')})")
        md.append(f"- Generation: {a.get('how_generated')}")
        md.append(f"- Risk: {a.get('risk_level')}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "task-01-new-sections" / "source-authority-map.md", "\n".join(md))
    return authority


def phase3_image_requirements(inventory: list[dict[str, Any]]) -> None:
    home = next((r for r in inventory if r["page_key"] == "home"), {})
    hub = next((r for r in inventory if r["page_key"] == "neutral_hub"), {})
    sample_imgs = []
    for c in (home.get("category_cards") or [])[:3]:
        if c.get("img"):
            sample_imgs.append(c["img"])
    dims = "300x300"
    fmt = "webp (cached from category master)"
    sections = [
        {"section": "Лари", "slug": "lari", "levels": ["parent"], "on_home": False, "on_hub": False},
        {"section": "Складские лари", "slug": "skladskie-lari", "levels": ["child"], "on_home": False, "on_hub": False},
        {"section": "Производственные лари", "slug": "proizvodstvennye-lari", "levels": ["child"], "on_home": False, "on_hub": False},
        {"section": "Кондитерский инвентарь", "slug": "konditerskiy-inventar", "levels": ["parent"], "on_home": False, "on_hub": False},
        {"section": "Формы кондитерские", "slug": "formy-konditerskie", "levels": ["child"], "on_home": False, "on_hub": False},
    ]
    for s in sections:
        slug = s["slug"]
        href = f"/katalog/nejtralnoe-oborudovanie/{slug}" if slug != "lari" else f"/katalog/nejtralnoe-oborudovanie/lari"
        for page_row, label in ((home, "home"), (hub, "hub")):
            for c in page_row.get("category_cards") or []:
                if slug in c.get("href", ""):
                    s[f"on_{label}"] = True
                    s["existing_img"] = c.get("img", "")
    req_rows = []
    for s in sections:
        req_rows.append({
            "section": s["section"],
            "slug": s["slug"],
            "target_size": dims,
            "format": fmt,
            "aspect_ratio": "1:1",
            "proposed_filename": f"catalog/Category-image/{s['slug']}.png",
            "cache_url_pattern": f"image/cache/catalog/Category-image/{s['slug']}-300x300.webp",
            "upload_path_future": "OpenCart admin category image + FTP image/catalog/Category-image/",
            "on_homepage_tile": s.get("on_home", False),
            "on_neutral_hub_tile": s.get("on_hub", False),
            "category_image_exists": bool(s.get("existing_img")),
            "homepage_separate_from_category": "no — same resize cache from category image",
        })
    write_csv(
        DEPLOYMENT_ROOT / "task-01-new-sections" / "image-requirements.csv",
        req_rows,
        list(req_rows[0].keys()) if req_rows else [],
    )
    write_json(
        DEPLOYMENT_ROOT / "task-01-new-sections" / "image-requirements.json",
        {"sample_reference_images": sample_imgs, "requirements": req_rows},
    )
    plan = [
        "# Image production plan (Task 01)",
        "",
        "**No images generated in this intake.**",
        "",
        "## Required images (parent tiles for entry points)",
        "",
        "| Section | Target | Proposed master |",
        "|---------|--------|-----------------|",
    ]
    for r in req_rows:
        if r["slug"] in ("lari", "konditerskiy-inventar"):
            plan.append(f"| {r['section']} | 300×300 WebP cache | `{r['proposed_filename']}` |")
    plan += [
        "",
        "## Workflow (future SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01)",
        "",
        "1. Generate/source white-background studio product images (operator or AI workflow).",
        "2. Upload masters via OpenCart admin category image or controlled FTP to `image/catalog/Category-image/`.",
        "3. Add category IDs to `neutral_hub_branch_ids` in `category_visibility.php`.",
        "4. Verify homepage + neutral hub tiles and responsive layout.",
        "",
        f"Reference tile URLs from live: {', '.join(sample_imgs[:2]) or 'none captured'}",
    ]
    write_text(DEPLOYMENT_ROOT / "task-01-new-sections" / "image-production-plan.md", "\n".join(plan))
    write_text(
        DEPLOYMENT_ROOT / "task-01-new-sections" / "image-requirements.md",
        "\n".join(
            [
                "# Image requirements",
                "",
                f"Analogous card size: **{dims}** ({fmt}).",
                "",
                "Parent sections **Лари** and **Кондитерский инвентарь** need tile images before entry-point rollout.",
                "Child PLPs (складские/производственные лари, формы кондитерские) use standard category PLP — tile images optional unless promoted to hub grid.",
                "",
                "See `image-production-plan.md` for future workflow.",
            ]
        ),
    )


def phase4_task01_options() -> None:
    options = {
        "A_admin_category_image_data_driven": {
            "label": "Admin category image + category_visibility branch IDs",
            "files_touched": [
                "system/library/zpm/category_visibility.php",
                "OpenCart admin category image fields",
            ],
            "rollback": "Restore category_visibility.php backup; revert category images in admin",
            "production_risk": "MEDIUM",
            "evidence": "Run 4.195 neutral parent rollout used same pattern",
            "recommended": True,
        },
        "B_hardcoded_template_patch": {
            "label": "Hardcoded Twig blocks for lari/konditerskiy",
            "files_touched": ["catalogsections.twig", "category.twig"],
            "rollback": "Restore Twig from backup",
            "production_risk": "HIGH — duplicates data-driven tiles",
            "recommended": False,
        },
        "C_hybrid": {
            "label": "Hybrid: images via admin, visibility via category_visibility.php",
            "files_touched": ["category_visibility.php", "admin images"],
            "rollback": "Same as A",
            "production_risk": "MEDIUM",
            "recommended": True,
        },
    }
    write_json(DEPLOYMENT_ROOT / "implementation-options" / "task-01-new-sections-options.json", options)
    md = [
        "# Task 01 implementation options",
        "",
        "**Recommended:** Option A/C (hybrid) — extend `neutral_hub_branch_ids` + category images; no hardcoded Twig cards.",
        "",
        "Future operation: **SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01**",
    ]
    for k, v in options.items():
        md.append(f"## {v['label']}")
        md.append(f"- Risk: {v['production_risk']}")
        md.append(f"- Recommended: {v.get('recommended')}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "implementation-options" / "task-01-new-sections-options.md", "\n".join(md))


def phase5_pdp_observation() -> dict[str, Any]:
    resp = http_get(EXAMPLE_PDP)
    body = resp.get("body", "")
    meta = extract_page_meta(body) if body else {}
    extra = parse_pdp_extra_info(body) if body else {}
    obs = {
        "url": EXAMPLE_PDP,
        "http_status": resp.get("status"),
        "product_title": meta.get("title", ""),
        "h1": meta.get("h1", ""),
        "body_classes": meta.get("body_classes", ""),
        **extra,
    }
    write_json(DEPLOYMENT_ROOT / "task-02-extra-info" / "example-pdp-observation.json", obs)
    md = [
        "# Example PDP observation",
        "",
        f"URL: {EXAMPLE_PDP}",
        f"HTTP: {obs.get('http_status')}",
        f"H1: {obs.get('h1')}",
        "",
        f"**{EXTRA_INFO_ATTR}** present: {obs.get('has_extra_info')}",
        f"Value length: {obs.get('value_length')}",
        f"Row before specs toggle: {obs.get('row_before_specs_toggle')}",
        "",
        "Value preview:",
        "",
        obs.get("value", "")[:500],
    ]
    write_text(DEPLOYMENT_ROOT / "task-02-extra-info" / "example-pdp-observation.md", "\n".join(md))
    if body:
        # extract product-content region snippet
        m = re.search(r'class="product-content"[\s\S]{0,12000}', body)
        snippet = m.group(0) if m else body[:8000]
        write_text(DEPLOYMENT_ROOT / "task-02-extra-info" / "example-pdp-dom-snippet.html", snippet)
        write_text(DEPLOYMENT_ROOT / "http" / "example-pdp.html", body)
    return obs


def phase6_task02_source(ftp: ftplib.FTP) -> list[dict[str, Any]]:
    authority: list[dict[str, Any]] = []
    for remote in FTP_TASK02:
        data, err = ftp_download(ftp, remote)
        local = DEPLOYMENT_ROOT / "source-readonly" / local_ftp_name(remote)
        content = ""
        if data:
            local.write_bytes(data)
            content = data.decode("utf-8", errors="replace")
        twig_var = ""
        filter_where = "controller recommended"
        if "attribute_groups" in content and "product.twig" in remote:
            twig_var = "attribute_groups"
            filter_where = "controller: extract before Twig; render new block after product-content__specs-toggle-wrap"
        if "getProductAttributes" in content:
            filter_where = "model getProductAttributes → controller filter → Twig separate block"
        authority.append({
            "source_file": remote,
            "source_type": "MODIFICATION" if "/modification/" in remote else analyze_source_file(remote, content).get("source_type"),
            "exists": data is not None,
            "attribute_loaded_via": "model_catalog_product->getProductAttributes(product_id)",
            "twig_variable": twig_var or "attribute_groups",
            "spec_table_selector": "spec-table / product-content__specs",
            "toggle_hook": "data-product-specs-toggle on .product-content__specs-toggle-wrap",
            "filter_recommendation": filter_where,
            "modification_overlay": "/storage/modification/" in remote,
            "sha256": sha256_bytes(data) if data else "",
            "error": err,
        })
    write_csv(
        DEPLOYMENT_ROOT / "task-02-extra-info" / "source-authority-map.csv",
        authority,
        ["source_file", "source_type", "exists", "twig_variable", "filter_recommendation", "modification_overlay"],
    )
    write_json(DEPLOYMENT_ROOT / "task-02-extra-info" / "source-authority-map.json", {"files": authority})
    write_text(
        DEPLOYMENT_ROOT / "task-02-extra-info" / "source-authority-map.md",
        "# Task 02 source authority\n\n"
        "Filter **Дополнительные сведения** in `product.php` controller; pass `extra_info_attribute`; "
        "render below `product-content__specs-toggle-wrap` in `product.twig`.\n",
    )
    return authority


def phase7_attribute_scope(sample_size: int = 100) -> list[dict[str, Any]]:
    urls = fetch_sitemap_product_urls(limit=sample_size)
    rows: list[dict[str, Any]] = []
    for i, url in enumerate(urls):
        resp = http_get(url)
        body = resp.get("body", "")
        meta = extract_page_meta(body) if body else {}
        extra = parse_pdp_extra_info(body) if body else {}
        rows.append({
            "url": url,
            "product_title": meta.get("h1") or meta.get("title", ""),
            "has_extra_info": extra.get("has_extra_info", False),
            "value_length": extra.get("value_length", 0),
            "row_location": "spec-table inside product-content__specs",
            "attribute_group": extra.get("attribute_group", ""),
            "value_preview": (extra.get("value") or "")[:120],
            "needs_migration": extra.get("has_extra_info", False),
            "http_status": resp.get("status"),
        })
        if (i + 1) % 20 == 0:
            time.sleep(1)
        else:
            time.sleep(0.15)
    write_csv(
        DEPLOYMENT_ROOT / "task-02-extra-info" / "attribute-scope-sample.csv",
        rows,
        ["url", "product_title", "has_extra_info", "value_length", "value_preview", "needs_migration"],
    )
    with_count = sum(1 for r in rows if r["has_extra_info"])
    write_json(
        DEPLOYMENT_ROOT / "task-02-extra-info" / "attribute-scope-sample.json",
        {
            "sample_size": len(rows),
            "with_extra_info": with_count,
            "without": len(rows) - with_count,
            "pct_with": round(100 * with_count / len(rows), 1) if rows else 0,
            "rows": rows,
        },
    )
    write_text(
        DEPLOYMENT_ROOT / "task-02-extra-info" / "attribute-scope-sample.md",
        f"# Attribute scope sample\n\nSampled **{len(rows)}** PDPs from sitemap.\n\n"
        f"With «{EXTRA_INFO_ATTR}»: **{with_count}** ({round(100*with_count/len(rows),1) if rows else 0}%).\n",
    )
    return rows


def phase8_task02_options() -> None:
    options = {
        "A_controller_extraction": {
            "recommended": True,
            "files": ["catalog/controller/product/product.php", "catalog/view/theme/default/template/product/product.twig"],
            "description": "Remove attribute from attribute_groups in controller; pass extra_info_attribute; render after toggle wrap",
            "risk": "LOW-MEDIUM",
            "js_toggle_impact": "none if block is outside specs table targeted by toggle",
        },
        "B_twig_only": {
            "recommended": False,
            "files": ["product.twig"],
            "description": "Skip row in Twig loop; awkward for grouped structure",
            "risk": "MEDIUM",
        },
        "C_css_only": {
            "recommended": False,
            "acceptable": False,
            "reason": "Wrong semantics; content remains in table",
        },
    }
    write_json(DEPLOYMENT_ROOT / "implementation-options" / "task-02-extra-info-options.json", options)
    write_text(
        DEPLOYMENT_ROOT / "implementation-options" / "task-02-extra-info-options.md",
        "# Task 02 options\n\n**Recommended: A** — controller extraction.\n\n"
        "Future: **SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01**\n",
    )


def phase9_future_notes() -> None:
    note = {
        "current_state": "Local Windows Task Scheduler post-1C monitor active (Run 4.215/4.216)",
        "future_improvement": "Move post-1C monitor to server-side runtime near production import",
        "reason": "Server-side logs and execution closer to 1C import cron",
        "status": "DEFERRED",
        "future_operation": "SITE-002-PROD-SERVER-MONITOR-READINESS-01",
    }
    write_json(DEPLOYMENT_ROOT / "future-notes" / "server-side-monitor-migration-deferred.json", note)
    write_text(
        DEPLOYMENT_ROOT / "future-notes" / "server-side-monitor-migration-deferred.md",
        "# Server-side monitor migration (deferred)\n\n"
        "Local post-1C monitor remains accepted temporary model.\n\n"
        "Future: **SITE-002-PROD-SERVER-MONITOR-READINESS-01** — not part of current work.\n",
    )


def phase10_charters() -> None:
    charters = {
        "SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01": {
            "purpose": "Move «Дополнительные сведения» out of specs table into separate block below product-content__specs-toggle-wrap",
            "scope": ["product.php controller filter", "product.twig new block", "no DB/admin changes"],
            "files_likely": [
                "/public_html/catalog/controller/product/product.php",
                "/public_html/catalog/view/theme/default/template/product/product.twig",
            ],
            "rollback": "Restore controller + Twig from deployment backup",
            "verification": ["example PDP", "sample PDP without attribute", "JS specs toggle"],
            "operator_approvals": ["Beget backup", "controlled deploy charter"],
        },
        "SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01": {
            "purpose": "Add images and entry cards for Лари and Кондитерский инвентарь on home + neutral hub",
            "scope": ["category images", "category_visibility.php branch IDs", "responsive verify"],
            "dependency": "Image assets must exist before tile rollout",
            "files_likely": [
                "/public_html/system/library/zpm/category_visibility.php",
                "OpenCart admin category images",
            ],
            "rollback": "Restore category_visibility.php; revert images",
            "excluded": ["sitemap", "meta", "header/footer/Yandex"],
        },
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "future-task-charters.json", charters)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "future-task-charters.md",
        "# Future task charters\n\nSee JSON for structured charters.\n",
    )


def run_all(sample_size: int) -> dict[str, Any]:
    ensure_dirs()
    log: list[str] = [f"Started {utc_now()}"]
    inv = phase1_public_inventory()
    log.append(f"Phase 1: {len(inv)} pages")
    phase3_image_requirements(inv)
    phase4_task01_options()
    pdp_obs = phase5_pdp_observation()
    log.append("Phase 5: example PDP captured")
    ftp = ftp_connect()
    try:
        auth1 = phase2_task01_source(ftp)
        auth2 = phase6_task02_source(ftp)
    finally:
        ftp.quit()
    log.append(f"Phase 2/6: FTP files task01={len(auth1)} task02={len(auth2)}")
    scope = phase7_attribute_scope(sample_size)
    log.append(f"Phase 7: sampled {len(scope)} PDPs")
    phase8_task02_options()
    phase9_future_notes()
    phase10_charters()
    summary = {
        "operation_id": OPERATION_ID,
        "completed_at": utc_now(),
        "pages_inventoried": len(inv),
        "pdp_sample_size": len(scope),
        "pdp_with_extra_info": sum(1 for r in scope if r.get("has_extra_info")),
        "example_pdp_has_extra_info": pdp_obs.get("has_extra_info"),
        "lari_on_home": next((r for r in inv if r["page_key"] == "home"), {}).get("mentions_lari"),
        "konditerskiy_on_home": next((r for r in inv if r["page_key"] == "home"), {}).get("mentions_konditerskiy"),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "intake-summary.json", summary)
    write_text(DEPLOYMENT_ROOT / "logs" / "run.log", "\n".join(log))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--sample-size", type=int, default=100)
    args = parser.parse_args()
    summary = run_all(args.sample_size)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
