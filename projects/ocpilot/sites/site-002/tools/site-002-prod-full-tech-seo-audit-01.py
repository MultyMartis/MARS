#!/usr/bin/env python3
"""SITE-002 Production full technical / SEO / site health audit — read-only (Run 4.241)."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import html
import json
import re
import shlex
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

OPERATION_ID = "SITE-002-PROD-FULL-TECH-SEO-AUDIT-01"
OCPILOT_RUN = "4.241"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION_READ_ONLY_AUDIT"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01"
WRONG_BRAND = "БЗПМ"
CORRECT_BRAND = "ЗПМ"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
AUDIT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\audits"
    rf"\{OPERATION_ID}"
)
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
CRAWL_DELAY_SEC = 0.2
BASE_DOMAIN = "bzpm.ru"

SUBDIRS = (
    "crawl", "http", "sitemap", "robots-llms", "meta", "canonicals", "headings",
    "links", "assets", "images", "categories", "products", "information-pages",
    "forms", "structured-data", "brand-scan", "source-readonly", "db-readonly",
    "issue-register", "roadmap", "manifests", "reports", "logs", "security",
)

SEED_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/",
    "https://bzpm.ru/contact",
    "https://bzpm.ru/kontakty",
    "https://bzpm.ru/custom-equipment",
    "https://bzpm.ru/payment-methods",
    "https://bzpm.ru/delivery",
    "https://bzpm.ru/dealers",
    "https://bzpm.ru/guarantee",
    "https://bzpm.ru/about",
    "https://bzpm.ru/blog",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/sitemap.xml",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/skladskie-lari",
]

KEY_INFO_PAGES = [
    "/contact", "/custom-equipment", "/payment-methods", "/delivery",
    "/dealers", "/guarantee", "/about",
]

SECURITY_PATHS = [
    "/admin/", "/config.php", "/phpinfo.php", "/storage/", "/vendor/",
    "/.git/HEAD", "/backup", "/backup.zip", "/system/storage/logs/",
    "/index.php?route=extension/feed/google_sitemap",
]

TECHNICAL_QUERY_PATTERNS = (
    r"[?&]sort=", r"[?&]order=", r"[?&]page=\d+", r"[?&]limit=",
    r"[?&]route=", r"/index\.php", r"[?&]session", r"/cart", r"/checkout",
    r"/account", r"/compare", r"/wishlist",
)

EXCLUDE_CRAWL_PATTERNS = (
    r"/admin", r"/cart", r"/checkout", r"/account", r"/compare",
    r"/wishlist", r"[?&]route=", r"/index\.php\?",
)

GARBAGE_MARKERS = (
    ("lorem ipsum", re.I), ("dummy product", re.I), ("test product", re.I),
    ("тестовый товар", re.I), ("НЕ БРАТЬ", 0), ("placeholder", re.I),
    ("undefined", re.I), ("stack trace", re.I), ("fatal error", re.I),
)

SOURCE_FILES = [
    ("/public_html/catalog/controller/extension/feed/google_sitemap.php", "sitemap_controller"),
    ("/public_html/catalog/controller/startup/seo_url.php", "seo_url_startup"),
    ("/public_html/catalog/controller/startup/seo_pro.php", "seo_pro_startup"),
    ("/public_html/system/library/category_visibility.php", "category_visibility"),
    ("/public_html/catalog/view/theme/default/template/common/header.twig", "header_twig"),
    ("/public_html/catalog/view/theme/default/template/common/footer.twig", "footer_twig"),
    ("/public_html/robots.txt", "robots_txt"),
    ("/public_html/llms.txt", "llms_txt"),
]

stats: dict[str, Any] = {"ftp_reads": 0, "ftp_listings": 0, "db_selects": 0}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.in_title = False
        self.in_h1 = False
        self.h1_list: list[str] = []
        self.meta: dict[str, str] = {}
        self.links: list[dict[str, str]] = []
        self.anchors: list[dict[str, str]] = []
        self.images: list[dict[str, str]] = []
        self.scripts: list[str] = []
        self.stylesheets: list[str] = []
        self._in_anchor = False
        self._anchor_href = ""
        self._anchor_text = ""
        self._anchor_rel = ""
        self.lang = ""
        self.structured_data_blocks = 0
        self.forms: list[dict[str, str]] = []
        self._in_script_ld = False
        self._script_buf = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {k: (v or "") for k, v in attrs}
        tl = tag.lower()
        if tl == "html" and "lang" in ad:
            self.lang = ad["lang"]
        elif tl == "title":
            self.in_title = True
        elif tl == "h1":
            self.in_h1 = True
        elif tl == "meta":
            name = (ad.get("name") or ad.get("property") or "").lower()
            if name:
                self.meta[name] = ad.get("content", "")
        elif tl == "link":
            rel = ad.get("rel", "").lower()
            href = ad.get("href", "")
            if rel and href:
                self.links.append({"rel": rel, "href": href})
            if rel == "stylesheet" and href:
                self.stylesheets.append(href)
        elif tl == "a":
            self._in_anchor = True
            self._anchor_href = ad.get("href", "")
            self._anchor_text = ""
            self._anchor_rel = ad.get("rel", "")
        elif tl == "img":
            self.images.append({
                "src": ad.get("src", ""), "alt": ad.get("alt", ""),
                "width": ad.get("width", ""), "height": ad.get("height", ""),
                "loading": ad.get("loading", ""),
            })
        elif tl == "script":
            src = ad.get("src", "")
            if src:
                self.scripts.append(src)
            stype = ad.get("type", "").lower()
            if stype == "application/ld+json":
                self._in_script_ld = True
                self._script_buf = ""
        elif tl == "form":
            self.forms.append({
                "action": ad.get("action", ""), "method": ad.get("method", "get"),
                "id": ad.get("id", ""), "class": ad.get("class", ""),
            })

    def handle_endtag(self, tag: str) -> None:
        tl = tag.lower()
        if tl == "title":
            self.in_title = False
        elif tl == "h1":
            self.in_h1 = False
        elif tl == "a" and self._in_anchor:
            self._in_anchor = False
            self.anchors.append({
                "href": self._anchor_href, "text": self._anchor_text.strip(),
                "rel": self._anchor_rel,
            })
        elif tl == "script" and self._in_script_ld:
            self._in_script_ld = False
            if self._script_buf.strip():
                self.structured_data_blocks += 1

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if self.in_h1:
            t = data.strip()
            if t:
                self.h1_list.append(t)
        if self._in_anchor:
            self._anchor_text += data
        if self._in_script_ld:
            self._script_buf += data


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
        w = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


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
    key: str | None = None
    for line in block.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            key = s[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(key, "")
        elif key:
            fields[key] = s
    return fields


def http_fetch(url: str, method: str = "GET") -> dict[str, Any]:
    t0 = time.monotonic()
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT}, method=method)
    chain: list[dict[str, Any]] = []
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = resp.read()
            chain.append({"url": url, "status": resp.status})
            elapsed = round(time.monotonic() - t0, 3)
            return {
                "url": url, "status": resp.status, "final_url": resp.geturl(),
                "redirect_chain": chain, "redirect_hops": len(chain) - 1,
                "headers": {k.lower(): v for k, v in resp.headers.items()},
                "body": body, "response_time_sec": elapsed, "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read() if exc.fp else b""
        chain.append({"url": url, "status": exc.code})
        return {
            "url": url, "status": exc.code, "final_url": exc.geturl(),
            "redirect_chain": chain, "redirect_hops": len(chain) - 1,
            "headers": {k.lower(): v for k, v in exc.headers.items()} if exc.headers else {},
            "body": body, "response_time_sec": round(time.monotonic() - t0, 3),
            "error": str(exc),
        }
    except Exception as exc:
        return {
            "url": url, "status": None, "final_url": url, "redirect_chain": chain,
            "redirect_hops": 0, "headers": {}, "body": b"",
            "response_time_sec": round(time.monotonic() - t0, 3), "error": str(exc),
        }


def is_internal(url: str) -> bool:
    p = urlparse(url)
    if not p.netloc:
        return True
    return p.netloc.lower() in (BASE_DOMAIN, f"www.{BASE_DOMAIN}")


def normalize_url(url: str) -> str:
    p = urlparse(url)
    path = p.path.rstrip("/") or "/"
    return urllib.parse.urlunparse((p.scheme or "https", p.netloc or BASE_DOMAIN, path, "", "", ""))


def is_crawl_allowed(url: str) -> bool:
    for pat in EXCLUDE_CRAWL_PATTERNS:
        if re.search(pat, url, re.I):
            return False
    return True


def classify_url_type(url: str, in_sitemap: bool) -> str:
    p = urlparse(url)
    path = p.path.rstrip("/") or "/"
    if url.endswith("/robots.txt"):
        return "service"
    if url.endswith("/llms.txt"):
        return "service"
    if url.endswith("/sitemap.xml"):
        return "service"
    if path == "/":
        return "homepage"
    parts = [x for x in path.split("/") if x]
    if parts == ["katalog"]:
        return "catalog_root"
    if parts and parts[0] == "katalog":
        return "product" if len(parts) >= 5 else "category"
    if parts and parts[0] == "contact":
        return "contact"
    info = {"about", "custom-equipment", "dealers", "delivery", "guarantee", "payment-methods"}
    if parts and parts[0] in info:
        return "information"
    if parts and parts[0] == "blog":
        return "information"
    if p.path.endswith((".css", ".js", ".jpg", ".png", ".webp", ".svg", ".gif", ".woff", ".woff2")):
        return "static_asset"
    if p.path == "/kontakty":
        return "404"
    return "information" if in_sitemap else "excluded"


def parse_sitemap(xml_text: str) -> list[str]:
    try:
        root = ET.fromstring(xml_text)
        return [loc.text.strip() for loc in root.findall(f".//{SITEMAP_NS}loc") if loc.text]
    except ET.ParseError:
        return []


def parse_page(body: bytes) -> dict[str, Any]:
    text = body.decode("utf-8", errors="replace")
    p = PageParser()
    try:
        p.feed(text)
    except Exception:
        pass
    canonical = ""
    for link in p.links:
        if link.get("rel") == "canonical":
            canonical = link.get("href", "")
    h1s = [h for h in p.h1_list if h]
    return {
        "title": html.unescape(p.title.strip()),
        "meta_description": p.meta.get("description", ""),
        "meta_robots": p.meta.get("robots", ""),
        "canonical": canonical,
        "h1": " | ".join(h1s),
        "h1_count": len(h1s),
        "lang": p.lang,
        "viewport": p.meta.get("viewport", ""),
        "og_title": p.meta.get("og:title", ""),
        "og_description": p.meta.get("og:description", ""),
        "og_image": p.meta.get("og:image", ""),
        "og_url": p.meta.get("og:url", ""),
        "twitter_card": p.meta.get("twitter:card", ""),
        "anchors": p.anchors,
        "images": p.images,
        "scripts": p.scripts,
        "stylesheets": p.stylesheets,
        "forms": p.forms,
        "structured_data_blocks": p.structured_data_blocks,
        "html_text": text,
        "has_load_more": "load-more" in text.lower() or "load_more" in text.lower(),
        "has_price": bool(re.search(r'class=["\'][^"\']*price', text, re.I)),
        "has_add_to_cart": bool(re.search(r'button-cart|btn-cart|add-to-cart|cart/add', text, re.I)),
        "has_breadcrumb": bool(re.search(r'breadcrumb', text, re.I)),
        "bzpm_count": text.count(WRONG_BRAND),
    }


def ensure_dirs() -> None:
    for sub in SUBDIRS:
        (AUDIT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    write_json(AUDIT_ROOT / "manifests" / "operation.json", {
        "operation_id": OPERATION_ID, "site_id": SITE_ID, "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL, "baseline_before": BASELINE_BEFORE,
        "operator_backup_note": "full Beget backup made before audit",
        "change_type": "full-tech-seo-site-health-audit",
        "production_mutation_allowed": False, "ftp_upload_allowed": False,
        "db_write_allowed": False, "admin_save_allowed": False,
        "cache_clear_allowed": False, "import_run_allowed": False,
        "monitor_run_allowed": False, "report_only": True,
        "started_at": utc_now(),
    })


def phase_url_inventory(sitemap_urls: list[str]) -> list[dict[str, Any]]:
    inventory: dict[str, dict[str, Any]] = {}
    sitemap_set = set(sitemap_urls)

    def add(url: str, source: str, notes: str = "") -> None:
        nu = normalize_url(url) if is_internal(url) else url
        if nu not in inventory:
            inventory[nu] = {
                "url": nu, "source": source, "type": classify_url_type(nu, nu in sitemap_set),
                "in_sitemap": nu in sitemap_set, "linked_from": set(),
                "expected_indexable": "yes" if nu in sitemap_set else "maybe",
                "crawl_allowed": "yes" if is_crawl_allowed(nu) else "no", "notes": notes,
            }
        else:
            inventory[nu]["source"] += f";{source}"

    for u in sitemap_urls:
        add(u, "sitemap")
    for u in SEED_URLS:
        add(u, "seed")

    rows = []
    for u, row in sorted(inventory.items()):
        r = dict(row)
        r["linked_from"] = "|".join(sorted(row["linked_from"])) if row["linked_from"] else ""
        rows.append(r)

    fields = ["url", "source", "type", "in_sitemap", "linked_from", "expected_indexable", "crawl_allowed", "notes"]
    write_csv(AUDIT_ROOT / "crawl" / "url-inventory.csv", rows, fields)
    write_json(AUDIT_ROOT / "crawl" / "url-inventory.json", rows)
    md = [f"# URL inventory\n\nGenerated: {utc_now()}\n\nTotal: {len(rows)}\n\n"]
    by_type = Counter(r["type"] for r in rows)
    for t, c in sorted(by_type.items()):
        md.append(f"- {t}: {c}\n")
    write_text(AUDIT_ROOT / "crawl" / "url-inventory.md", "".join(md))
    return rows


def phase_http_crawl(inventory: list[dict[str, Any]]) -> tuple[list[dict], dict[str, dict]]:
    crawl_urls = [r["url"] for r in inventory if r["crawl_allowed"] == "yes" and not r["url"].endswith((".txt", ".xml"))]
    crawl_urls += [u for u in SEED_URLS if u.endswith((".txt", ".xml"))]
    crawl_urls = list(dict.fromkeys(crawl_urls))

    http_rows: list[dict[str, Any]] = []
    page_cache: dict[str, dict] = {}

    for i, url in enumerate(crawl_urls):
        if i > 0:
            time.sleep(CRAWL_DELAY_SEC)
        resp = http_fetch(url)
        ct = resp.get("headers", {}).get("content-type", "")
        parsed: dict[str, Any] = {}
        if resp.get("body") and "html" in ct.lower():
            parsed = parse_page(resp["body"])
            page_cache[url] = {"resp": resp, "parsed": parsed}

        chain_str = json.dumps(resp.get("redirect_chain", []), ensure_ascii=False)
        row = {
            "url": url, "status": resp.get("status"), "final_url": resp.get("final_url"),
            "redirect_chain": chain_str, "redirect_hops": resp.get("redirect_hops", 0),
            "content_type": ct, "response_time_sec": resp.get("response_time_sec"),
            "title": parsed.get("title", ""), "canonical": parsed.get("canonical", ""),
            "robots_meta": parsed.get("meta_robots", ""), "body_size": len(resp.get("body") or b""),
            "error": resp.get("error"), "h1_count": parsed.get("h1_count", 0),
            "soft_404_signs": "404" in parsed.get("title", "").lower() or "not found" in parsed.get("title", "").lower(),
        }
        http_rows.append(row)
        if (i + 1) % 100 == 0:
            print(f"  HTTP crawl: {i + 1}/{len(crawl_urls)}", file=sys.stderr)

    fields = list(http_rows[0].keys()) if http_rows else ["url"]
    write_csv(AUDIT_ROOT / "http" / "http-status-audit.csv", http_rows, fields)
    write_json(AUDIT_ROOT / "http" / "http-status-audit.json", http_rows)

    non200_sitemap = [r for r in http_rows if r["url"] in {x["url"] for x in inventory if x["in_sitemap"]} and r["status"] != 200]
    md = [f"# HTTP status audit\n\nGenerated: {utc_now()}\n\nCrawled: {len(http_rows)}\n\n"]
    md.append(f"## Non-200 sitemap URLs: {len(non200_sitemap)}\n\n")
    for r in non200_sitemap[:50]:
        md.append(f"- {r['url']} → {r['status']}\n")
    write_text(AUDIT_ROOT / "http" / "http-status-audit.md", "".join(md))
    return http_rows, page_cache


def phase_links(page_cache: dict[str, dict], http_status: dict[str, int]) -> list[dict]:
    link_rows: list[dict] = []
    broken: list[dict] = []
    redirected: list[dict] = []

    for source, data in page_cache.items():
        parsed = data["parsed"]
        html_text = parsed.get("html_text", "")
        for anchor in parsed.get("anchors", []):
            href = anchor.get("href", "")
            if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
                continue
            target = urljoin(source, href)
            if not is_internal(target):
                continue
            norm = normalize_url(target)
            loc = "unknown"
            if "header" in html_text[:html_text.find(href) if href in html_text else 0].lower():
                loc = "header"
            elif "footer" in html_text.lower() and href in html_text[html_text.lower().rfind("footer"):]:
                loc = "footer"
            elif "breadcrumb" in html_text.lower():
                loc = "breadcrumbs"
            status = http_status.get(norm)
            row = {
                "source_url": source, "anchor_text": anchor.get("text", "")[:200],
                "href": href, "normalized_target": norm, "target_status": status,
                "link_location": loc, "nofollow": "nofollow" in anchor.get("rel", "").lower(),
            }
            link_rows.append(row)
            if status and status >= 400:
                broken.append(row)
            elif status and status in (301, 302, 303, 307, 308):
                redirected.append(row)

    fields = ["source_url", "anchor_text", "href", "normalized_target", "target_status", "link_location", "nofollow"]
    write_csv(AUDIT_ROOT / "links" / "internal-link-audit.csv", link_rows, fields)
    write_json(AUDIT_ROOT / "links" / "internal-link-audit.json", link_rows)

    kontakty_links = [r for r in link_rows if "kontakty" in r["href"].lower() or "kontakty" in r["normalized_target"].lower()]
    md_b = [f"# Broken internal links\n\nTotal broken: {len(broken)}\n\n"]
    for r in broken[:100]:
        md_b.append(f"- {r['source_url']} → {r['normalized_target']} ({r['target_status']})\n")
    write_text(AUDIT_ROOT / "links" / "broken-internal-links.md", "".join(md_b))

    md_r = [f"# Redirected internal links\n\nTotal: {len(redirected)}\n\n"]
    lari_old = [r for r in redirected if "/lari" in r["href"] and "shkafy-i-lari" not in r["normalized_target"]]
    for r in lari_old[:30]:
        md_r.append(f"- {r['source_url']} → {r['normalized_target']}\n")
    if kontakty_links:
        md_r.append(f"\n## Links to /kontakty: {len(kontakty_links)}\n")
        for r in kontakty_links:
            md_r.append(f"- {r['source_url']} → {r['href']}\n")
    write_text(AUDIT_ROOT / "links" / "redirected-internal-links.md", "".join(md_r))
    return link_rows


def phase_assets(page_cache: dict[str, dict]) -> list[dict]:
    asset_rows: list[dict] = []
    checked: set[str] = set()
    image_rows: list[dict] = []

    for source, data in page_cache.items():
        parsed = data["parsed"]
        for img in parsed.get("images", []):
            src = img.get("src", "")
            if not src:
                continue
            abs_u = urljoin(source, src)
            if not is_internal(abs_u):
                continue
            image_rows.append({
                "source_page": source, "asset_url": abs_u, "asset_type": "image",
                "alt_text": img.get("alt", ""), "width": img.get("width", ""),
                "height": img.get("height", ""), "lazy_loading": img.get("loading", ""),
            })
            if abs_u not in checked:
                checked.add(abs_u)
        for src in parsed.get("scripts", []) + parsed.get("stylesheets", []):
            abs_u = urljoin(source, src)
            if is_internal(abs_u):
                checked.add(abs_u)

    for i, url in enumerate(sorted(checked)):
        if i > 0 and i % 20 == 0:
            time.sleep(CRAWL_DELAY_SEC)
        resp = http_fetch(url)
        asset_rows.append({
            "asset_url": url, "status": resp.get("status"), "final_url": resp.get("final_url"),
            "content_type": resp.get("headers", {}).get("content-type", ""),
            "size": len(resp.get("body") or b""),
        })

    broken_assets = [r for r in asset_rows if r["status"] and r["status"] >= 400]
    write_csv(AUDIT_ROOT / "assets" / "asset-status-audit.csv", asset_rows,
              ["asset_url", "status", "final_url", "content_type", "size"])
    write_json(AUDIT_ROOT / "assets" / "asset-status-audit.json", asset_rows)
    write_csv(AUDIT_ROOT / "images" / "image-alt-audit.csv", image_rows,
              ["source_page", "asset_url", "asset_type", "alt_text", "width", "height", "lazy_loading"])
    write_json(AUDIT_ROOT / "images" / "image-alt-audit.json", image_rows)
    md = [f"# Broken assets\n\nTotal assets checked: {len(asset_rows)}\nBroken: {len(broken_assets)}\n\n"]
    for r in broken_assets[:80]:
        md.append(f"- {r['asset_url']} → {r['status']}\n")
    write_text(AUDIT_ROOT / "assets" / "broken-assets.md", "".join(md))
    return asset_rows


def phase_meta(page_cache: dict[str, dict], http_rows: list[dict]) -> None:
    meta_rows: list[dict] = []
    h1_rows: list[dict] = []
    canon_rows: list[dict] = []
    sd_rows: list[dict] = []
    titles = Counter()
    descs = Counter()

    status_map = {r["url"]: r["status"] for r in http_rows}

    for url, data in page_cache.items():
        if status_map.get(url) != 200:
            continue
        p = data["parsed"]
        title = p.get("title", "")
        desc = p.get("meta_description", "")
        titles[title] += 1
        descs[desc] += 1
        utype = classify_url_type(url, True)
        meta_rows.append({
            "url": url, "page_type": utype, "title": title, "title_length": len(title),
            "meta_description": desc, "description_length": len(desc),
            "canonical": p.get("canonical", ""), "h1_count": p.get("h1_count", 0),
            "h1_text": p.get("h1", ""), "robots_meta": p.get("meta_robots", ""),
            "viewport": p.get("viewport", ""), "lang": p.get("lang", ""),
            "og_title": p.get("og_title", ""), "og_image": p.get("og_image", ""),
            "twitter_card": p.get("twitter_card", ""),
            "structured_data_blocks": p.get("structured_data_blocks", 0),
        })
        h1_rows.append({"url": url, "h1_count": p.get("h1_count", 0), "h1_text": p.get("h1", "")})
        canon_rows.append({"url": url, "canonical": p.get("canonical", ""), "final_url": url})
        sd_rows.append({"url": url, "structured_data_blocks": p.get("structured_data_blocks", 0)})

    dup_titles = {t: c for t, c in titles.items() if c > 1 and t}
    dup_descs = {d: c for d, c in descs.items() if c > 1 and d}
    missing_title = [r for r in meta_rows if not r["title"]]
    missing_desc = [r for r in meta_rows if not r["meta_description"] and r["page_type"] in ("homepage", "category", "information", "contact", "catalog_root")]
    missing_h1 = [r for r in meta_rows if r["h1_count"] == 0 and r["page_type"] not in ("product",)]
    multi_h1 = [r for r in meta_rows if r["h1_count"] > 1]

    write_csv(AUDIT_ROOT / "meta" / "meta-audit.csv", meta_rows,
              ["url", "page_type", "title", "title_length", "meta_description", "description_length",
               "canonical", "h1_count", "h1_text", "robots_meta", "viewport", "lang",
               "og_title", "og_image", "twitter_card", "structured_data_blocks"])
    write_json(AUDIT_ROOT / "meta" / "meta-audit.json", meta_rows)
    write_csv(AUDIT_ROOT / "headings" / "h1-audit.csv", h1_rows, ["url", "h1_count", "h1_text"])
    write_csv(AUDIT_ROOT / "canonicals" / "canonical-audit.csv", canon_rows, ["url", "canonical", "final_url"])
    write_csv(AUDIT_ROOT / "structured-data" / "structured-data-audit.csv", sd_rows, ["url", "structured_data_blocks"])

    md_dup = [f"# Meta duplicates\n\nDuplicate titles: {len(dup_titles)}\nDuplicate descriptions: {len(dup_descs)}\n\n"]
    for t, c in sorted(dup_titles.items(), key=lambda x: -x[1])[:30]:
        md_dup.append(f"- ({c}x) {t[:100]}\n")
    write_text(AUDIT_ROOT / "meta" / "meta-duplicates.md", "".join(md_dup))

    md_miss = [f"# Missing meta\n\nMissing title: {len(missing_title)}\nMissing desc (key pages): {len(missing_desc)}\nMissing H1: {len(missing_h1)}\nMultiple H1: {len(multi_h1)}\n"]
    write_text(AUDIT_ROOT / "meta" / "meta-missing.md", "".join(md_miss))


def phase_sitemap_robots_llms(sitemap_urls: list[str], http_rows: list[dict]) -> dict[str, Any]:
    status_map = {r["url"]: r for r in http_rows}
    sitemap_rows = []
    for u in sitemap_urls:
        hr = status_map.get(u, {})
        sitemap_rows.append({"url": u, "status": hr.get("status"), "in_crawl": bool(hr)})

    non200 = [r for r in sitemap_rows if r["status"] != 200]
    lari_flat = [u for u in sitemap_urls if re.search(r"/katalog/nejtralnoe-oborudovanie/lari(?!/)", u) and "shkafy-i-lari" not in u]
    lari_nested = [u for u in sitemap_urls if "shkafy-i-lari/lari" in u]
    contact_in = any(u.rstrip("/").endswith("/contact") for u in sitemap_urls)
    kontakty_in = any("kontakty" in u.lower() for u in sitemap_urls)

    write_csv(AUDIT_ROOT / "sitemap" / "sitemap-audit.csv", sitemap_rows, ["url", "status", "in_crawl"])
    write_json(AUDIT_ROOT / "sitemap" / "sitemap-audit.json", sitemap_rows)
    sm_md = [
        f"# Sitemap summary\n\nURLs: {len(sitemap_urls)}\nNon-200: {len(non200)}\n",
        f"Flat lari URLs in sitemap: {len(lari_flat)}\nNested lari URLs: {len(lari_nested)}\n",
        f"/contact in sitemap: {contact_in}\n/kontakty in sitemap: {kontakty_in}\n",
    ]
    write_text(AUDIT_ROOT / "sitemap" / "sitemap-summary.md", "".join(sm_md))

    robots_resp = http_fetch("https://bzpm.ru/robots.txt")
    llms_resp = http_fetch("https://bzpm.ru/llms.txt")
    robots_body = (robots_resp.get("body") or b"").decode("utf-8", errors="replace")
    llms_body = (llms_resp.get("body") or b"").decode("utf-8", errors="replace")
    write_text(AUDIT_ROOT / "robots-llms" / "robots-live.txt", robots_body)
    write_text(AUDIT_ROOT / "robots-llms" / "llms-live.txt", llms_body)

    robots_md = [
        f"# Robots audit\n\nStatus: {robots_resp.get('status')}\n",
        f"Sitemap directive present: {'Sitemap:' in robots_body}\n",
        f"Disallow admin: {'Disallow: /admin' in robots_body or 'admin' in robots_body.lower()}\n\n",
        "```\n" + robots_body[:2000] + "\n```\n",
    ]
    write_text(AUDIT_ROOT / "robots-llms" / "robots-audit.md", "".join(robots_md))

    llms_kontakty = "kontakty" in llms_body.lower()
    llms_contact = "/contact" in llms_body
    llms_bzpm = WRONG_BRAND in llms_body
    llms_md = [
        f"# LLMS audit\n\nStatus: {llms_resp.get('status')}\n",
        f"Uses /contact: {llms_contact}\nReferences kontakty: {llms_kontakty}\n",
        f"Public БЗПМ: {llms_bzpm}\n\n```\n" + llms_body[:3000] + "\n```\n",
    ]
    write_text(AUDIT_ROOT / "robots-llms" / "llms-audit.md", "".join(llms_md))

    return {
        "sitemap_count": len(sitemap_urls), "sitemap_non200": len(non200),
        "lari_flat_in_sitemap": lari_flat, "lari_nested_count": len(lari_nested),
        "contact_in_sitemap": contact_in, "kontakty_in_sitemap": kontakty_in,
        "robots_status": robots_resp.get("status"), "llms_status": llms_resp.get("status"),
        "llms_bzpm": llms_bzpm, "llms_kontakty": llms_kontakty,
    }


def phase_catalog(page_cache: dict[str, dict], http_rows: list[dict], sitemap_urls: list[str]) -> None:
    cat_rows: list[dict] = []
    prod_rows: list[dict] = []
    bc_rows: list[dict] = []

    for url in sitemap_urls:
        ut = classify_url_type(url, True)
        data = page_cache.get(url)
        if not data:
            continue
        p = data["parsed"]
        resp_status = next((r["status"] for r in http_rows if r["url"] == url), None)
        base = {
            "url": url, "status": resp_status, "title": p.get("title", ""),
            "h1": p.get("h1", ""), "canonical": p.get("canonical", ""),
            "meta_description": p.get("meta_description", ""),
            "has_breadcrumb": p.get("has_breadcrumb", False),
            "has_load_more": p.get("has_load_more", False),
            "bzpm_count": p.get("bzpm_count", 0),
        }
        if ut == "category":
            cat_rows.append({**base, "has_products_listing": p.get("has_price", False)})
            bc_rows.append({"url": url, "has_breadcrumb": p.get("has_breadcrumb", False), "h1": p.get("h1", "")})
        elif ut == "product":
            prod_rows.append({
                **base, "has_image": len(p.get("images", [])) > 0,
                "has_price": p.get("has_price", False),
                "has_add_to_cart": p.get("has_add_to_cart", False),
            })

    cat_issues = [r for r in cat_rows if r["status"] != 200 or r["bzpm_count"] > 0]
    prod_issues = [r for r in prod_rows if r["status"] != 200 or not r.get("has_price") or r["bzpm_count"] > 0]

    write_csv(AUDIT_ROOT / "categories" / "category-audit.csv", cat_rows,
              ["url", "status", "title", "h1", "canonical", "meta_description", "has_breadcrumb", "has_load_more", "has_products_listing", "bzpm_count"])
    write_json(AUDIT_ROOT / "categories" / "category-audit.json", cat_rows)
    write_csv(AUDIT_ROOT / "products" / "product-audit.csv", prod_rows,
              ["url", "status", "title", "h1", "canonical", "has_image", "has_price", "has_add_to_cart", "bzpm_count"])
    write_json(AUDIT_ROOT / "products" / "product-audit.json", prod_rows)
    write_csv(AUDIT_ROOT / "categories" / "breadcrumb-audit.csv", bc_rows, ["url", "has_breadcrumb", "h1"])

    write_text(AUDIT_ROOT / "categories" / "category-issues.md",
               f"# Category issues\n\nTotal categories: {len(cat_rows)}\nIssues: {len(cat_issues)}\n")
    write_text(AUDIT_ROOT / "products" / "product-issues.md",
               f"# Product issues\n\nTotal products: {len(prod_rows)}\nIssues: {len(prod_issues)}\nNo price visible: {sum(1 for r in prod_rows if not r.get('has_price'))}\n")


def phase_info_forms(page_cache: dict[str, dict]) -> None:
    info_rows: list[dict] = []
    form_rows: list[dict] = []
    for path in KEY_INFO_PAGES:
        url = f"https://bzpm.ru{path}"
        data = page_cache.get(url)
        if not data:
            resp = http_fetch(url)
            time.sleep(CRAWL_DELAY_SEC)
            data = {"parsed": parse_page(resp.get("body") or b""), "resp": resp}
        p = data["parsed"]
        info_rows.append({
            "url": url, "title": p.get("title", ""), "h1": p.get("h1", ""),
            "canonical": p.get("canonical", ""), "meta_description": p.get("meta_description", ""),
            "form_count": len(p.get("forms", [])), "bzpm_count": p.get("bzpm_count", 0),
        })
        for i, form in enumerate(p.get("forms", [])):
            form_rows.append({
                "page_url": url, "form_index": i, "action": form.get("action", ""),
                "method": form.get("method", ""), "id": form.get("id", ""),
                "class": form.get("class", ""),
            })

    write_csv(AUDIT_ROOT / "information-pages" / "information-page-audit.csv", info_rows,
              ["url", "title", "h1", "canonical", "meta_description", "form_count", "bzpm_count"])
    write_csv(AUDIT_ROOT / "forms" / "forms-static-audit.csv", form_rows,
              ["page_url", "form_index", "action", "method", "id", "class"])
    write_json(AUDIT_ROOT / "forms" / "forms-static-audit.json", form_rows)
    write_text(AUDIT_ROOT / "forms" / "forms-issues.md",
               f"# Forms audit\n\nInfo pages: {len(info_rows)}\nForms found: {len(form_rows)}\n")


def phase_brand_scan(page_cache: dict[str, dict]) -> list[dict]:
    findings: list[dict] = []
    for url, data in page_cache.items():
        text = data["parsed"].get("html_text", "")
        if WRONG_BRAND in text:
            findings.append({
                "url": url, "marker": WRONG_BRAND, "count": text.count(WRONG_BRAND),
                "classification": "real_issue", "sample": text[text.find(WRONG_BRAND):text.find(WRONG_BRAND) + 80],
            })
        for marker, flags in GARBAGE_MARKERS:
            pat = re.compile(re.escape(marker) if isinstance(flags, int) else marker, flags if isinstance(flags, int) else 0)
            if pat.search(text):
                cls = "false_positive" if "пример" in marker.lower() else "needs_review"
                findings.append({"url": url, "marker": marker, "count": 1, "classification": cls, "sample": ""})

    write_csv(AUDIT_ROOT / "brand-scan" / "public-brand-scan.csv", findings,
              ["url", "marker", "count", "classification", "sample"])
    write_json(AUDIT_ROOT / "brand-scan" / "public-brand-scan.json", findings)
    md = [f"# Brand/content hygiene\n\nБЗПМ hits: {sum(1 for f in findings if f['marker'] == WRONG_BRAND)}\n\n"]
    for f in findings:
        if f["marker"] == WRONG_BRAND:
            md.append(f"- {f['url']}: {f['count']}x\n")
    write_text(AUDIT_ROOT / "brand-scan" / "content-hygiene-findings.md", "".join(md))
    return findings


def phase_security() -> list[dict]:
    rows: list[dict] = []
    for path in SECURITY_PATHS:
        url = PRODUCTION_URL.rstrip("/") + path
        time.sleep(CRAWL_DELAY_SEC)
        resp = http_fetch(url, method="HEAD" if not path.endswith("/") else "GET")
        body_preview = (resp.get("body") or b"")[:500].decode("utf-8", errors="replace")
        risk = "LOW"
        if resp.get("status") == 200:
            if "config" in path or "backup" in path or ".git" in path:
                risk = "CRITICAL"
            elif "storage" in path or "vendor" in path or "logs" in path:
                risk = "HIGH" if "Index of" in body_preview or "Directory listing" in body_preview else "MEDIUM"
            elif "admin" in path:
                risk = "LOW"
        rows.append({
            "path": path, "url": url, "status": resp.get("status"),
            "risk": risk, "content_exposed": bool(body_preview.strip()) and resp.get("status") == 200,
            "body_preview_len": len(resp.get("body") or b""),
        })

    write_csv(AUDIT_ROOT / "security" / "public-exposure-basic-audit.csv", rows,
              ["path", "url", "status", "risk", "content_exposed", "body_preview_len"])
    write_json(AUDIT_ROOT / "security" / "public-exposure-basic-audit.json", rows)
    write_text(AUDIT_ROOT / "security" / "public-exposure-basic-audit.md",
               f"# Security exposure\n\nChecked: {len(rows)}\nCritical: {sum(1 for r in rows if r['risk'] == 'CRITICAL')}\n")
    return rows


def mysql_select(sql: str) -> str:
    import paramiko
    ssh = parse_production_section(SECRETS_PATH, "SSH")
    db = parse_production_section(SECRETS_PATH, "Database")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(ssh["host"], port=int(ssh.get("port") or 22), username=ssh["username"],
              password=ssh["password"], timeout=60, allow_agent=False, look_for_keys=False)
    esc = sql.replace("\\", "\\\\").replace('"', '\\"')
    cmd = f'MYSQL_PWD={shlex.quote(db["password"])} mysql -N -B -u {shlex.quote(db["username"])} {shlex.quote(db["database"])} -e "{esc}" 2>&1'
    _i, o, e = c.exec_command(cmd, timeout=120)
    out = o.read().decode() + e.read().decode()
    c.close()
    stats["db_selects"] += 1
    return out


def phase_db_readonly() -> dict[str, Any]:
    summary: dict[str, Any] = {"available": False}
    try:
        cat_count = mysql_select("SELECT COUNT(*) FROM oc_category WHERE status=1")
        prod_count = mysql_select("SELECT COUNT(*) FROM oc_product WHERE status=1")
        info_count = mysql_select("SELECT COUNT(*) FROM oc_information WHERE status=1")
        seo_dup = mysql_select(
            "SELECT keyword, COUNT(*) c FROM oc_seo_url GROUP BY keyword HAVING c>1 LIMIT 50"
        )
        missing_meta_cat = mysql_select(
            "SELECT c.category_id FROM oc_category c LEFT JOIN oc_category_description cd ON c.category_id=cd.category_id AND cd.language_id=1 WHERE c.status=1 AND (cd.meta_title IS NULL OR cd.meta_title='') LIMIT 100"
        )
        lari_path = mysql_select(
            "SELECT category_id, parent_id FROM oc_category WHERE category_id IN (79,88,358,140,141)"
        )
        lari_seo = mysql_select(
            "SELECT query, keyword FROM oc_seo_url WHERE query LIKE 'category_id=%' AND keyword LIKE '%lari%' LIMIT 20"
        )

        dup_rows = []
        for line in seo_dup.strip().splitlines():
            parts = line.split("\t")
            if len(parts) >= 2:
                dup_rows.append({"keyword": parts[0], "count": parts[1]})

        miss_rows = [{"category_id": line.strip()} for line in missing_meta_cat.strip().splitlines() if line.strip()]

        write_csv(AUDIT_ROOT / "db-readonly" / "seo-url-duplicates.csv", dup_rows, ["keyword", "count"])
        write_csv(AUDIT_ROOT / "db-readonly" / "missing-meta-db-crosscheck.csv", miss_rows, ["category_id"])

        path_lines = [l for l in lari_path.strip().splitlines() if l.strip()]
        write_text(AUDIT_ROOT / "db-readonly" / "category-path-anomalies.csv",
                   "category_id\tparent_id\n" + lari_path.strip() + "\n")

        md = [
            f"# DB readonly summary\n\nGenerated: {utc_now()}\n\n",
            f"Active categories: {cat_count.strip()}\n",
            f"Active products: {prod_count.strip()}\n",
            f"Active information pages: {info_count.strip()}\n",
            f"SEO URL duplicate keywords: {len(dup_rows)}\n",
            f"Categories missing meta_title: {len(miss_rows)}\n\n",
            f"## Lari category records\n```\n{lari_path}\n```\n\n",
            f"## Lari SEO URLs\n```\n{lari_seo}\n```\n",
        ]
        write_text(AUDIT_ROOT / "db-readonly" / "db-summary.md", "".join(md))
        summary = {
            "available": True, "active_categories": cat_count.strip(),
            "active_products": prod_count.strip(), "seo_dup_count": len(dup_rows),
            "missing_meta_categories": len(miss_rows), "lari_path": lari_path.strip(),
        }
    except Exception as exc:
        write_text(AUDIT_ROOT / "db-readonly" / "db-summary.md",
                   f"# DB readonly summary\n\nSAFE UNKNOWN: {exc}\n")
        summary["error"] = str(exc)
    return summary


def phase_source_readonly() -> list[dict]:
    rows: list[dict] = []
    try:
        fields = parse_production_section(SECRETS_PATH, "FTP / SFTP")
        ftp = ftplib.FTP()
        ftp.connect(fields["host"], int(fields.get("port") or 21), timeout=180)
        ftp.login(fields["username"], fields["password"])
        for remote, role in SOURCE_FILES:
            buf: list[bytes] = []
            try:
                ftp.retrbinary("RETR " + remote.lstrip("/"), buf.append)
                content = b"".join(buf).decode("utf-8", errors="replace")
                stats["ftp_reads"] += 1
                local_name = remote.replace("/", "__").strip("_")
                write_text(AUDIT_ROOT / "source-readonly" / local_name, content[:50000])
                rows.append({
                    "remote_path": remote, "role": role, "bytes": len(content),
                    "contains_bzpm": WRONG_BRAND in content,
                    "contains_kontakty": "kontakty" in content.lower(),
                    "contains_contact": "/contact" in content,
                    "downloaded": True,
                })
            except ftplib.error_perm:
                rows.append({"remote_path": remote, "role": role, "downloaded": False})
        ftp.quit()
    except Exception as exc:
        write_text(AUDIT_ROOT / "source-readonly" / "source-observations.md", f"FTP error: {exc}\n")
        return rows

    write_csv(AUDIT_ROOT / "source-readonly" / "source-authority-map.csv", rows,
              ["remote_path", "role", "bytes", "contains_bzpm", "contains_kontakty", "contains_contact", "downloaded"])
    write_json(AUDIT_ROOT / "source-readonly" / "source-authority-map.json", rows)
    write_text(AUDIT_ROOT / "source-readonly" / "source-observations.md",
               f"# Source observations\n\nFiles downloaded: {sum(1 for r in rows if r.get('downloaded'))}\n")
    return rows


def build_issue_register(
    http_rows: list[dict], link_rows: list[dict], sitemap_info: dict,
    brand_findings: list[dict], security_rows: list[dict], db_summary: dict,
    asset_rows: list[dict], sitemap_urls: list[str],
) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    n = 0

    def add(severity: str, category: str, title: str, description: str,
            samples: list[str], evidence: str, wave: str, **kw: Any) -> None:
        nonlocal n
        n += 1
        issues.append({
            "issue_id": f"SITE-002-AUDIT-{n:03d}",
            "severity": severity, "category": category, "title": title,
            "description": description, "affected_urls_count": kw.get("count", len(samples)),
            "sample_urls": "|".join(samples[:5]), "evidence_file": evidence,
            "likely_owner": kw.get("owner", "operator"),
            "recommended_fix_type": kw.get("fix_type", "review"),
            "risk_of_fix": kw.get("risk", "medium"),
            "requires_production_mutation": kw.get("mutation", "yes"),
            "requires_db_write": kw.get("db_write", "maybe"),
            "requires_ftp_upload": kw.get("ftp", "maybe"),
            "requires_admin_save": kw.get("admin", "maybe"),
            "requires_operator_decision": kw.get("decision", "no"),
            "dependencies": kw.get("deps", ""),
            "suggested_wave": wave, "notes": kw.get("notes", ""),
        })

    # Accepted non-issues
    add("P4", "routing", "/kontakty 404 accepted",
        "Run 4.238 decision: /contact canonical; /kontakty 404 is not a bug unless internal links point to it.",
        ["https://bzpm.ru/kontakty"], "links/redirected-internal-links.md", "F",
        mutation="no", fix_type="none", notes="accepted project decision")

    kontakty_links = [r for r in link_rows if "kontakty" in r.get("href", "").lower()]
    if kontakty_links:
        add("P1", "links", "Internal links point to /kontakty",
            f"{len(kontakty_links)} internal links target /kontakty which returns 404.",
            [r["source_url"] for r in kontakty_links], "links/broken-internal-links.md", "C",
            count=len(kontakty_links))

    if not sitemap_info.get("contact_in_sitemap"):
        add("P3", "sitemap", "/contact not in sitemap",
            "Optional SEO hygiene: canonical contacts URL /contact omitted from sitemap.xml.",
            ["https://bzpm.ru/contact"], "sitemap/sitemap-summary.md", "F",
            mutation="yes", fix_type="sitemap_policy", decision="yes")

    sitemap_non200 = [r for r in http_rows if r["url"] in set(sitemap_urls) and r["status"] != 200]
    if sitemap_non200:
        add("P0" if any(r["status"] and r["status"] >= 500 for r in sitemap_non200) else "P1",
            "http", "Sitemap URLs return non-200",
            f"{len(sitemap_non200)} sitemap URLs do not return HTTP 200.",
            [r["url"] for r in sitemap_non200], "http/http-status-audit.csv", "A",
            count=len(sitemap_non200))

    flat_lari = sitemap_info.get("lari_flat_in_sitemap") or []
    if flat_lari:
        add("P1", "sitemap", "Old flat Lari URLs still in sitemap",
            f"{len(flat_lari)} flat /lari URLs remain in sitemap after reparent.",
            flat_lari, "sitemap/sitemap-summary.md", "B", count=len(flat_lari))

    broken_links = [r for r in link_rows if r.get("target_status") and r["target_status"] >= 404
                    and "kontakty" not in r.get("normalized_target", "")]
    if broken_links:
        add("P1", "links", "Broken internal links (excl. kontakty policy)",
            f"{len(broken_links)} internal links target 404/5xx URLs.",
            list({r["normalized_target"] for r in broken_links})[:5],
            "links/broken-internal-links.md", "C", count=len(broken_links))

    broken_assets = [r for r in asset_rows if r.get("status") and r["status"] >= 400]
    css_js_broken = [r for r in broken_assets if any(x in r["asset_url"] for x in (".css", ".js"))]
    if css_js_broken:
        add("P0", "assets", "Broken CSS/JS assets",
            f"{len(css_js_broken)} critical stylesheet/script assets return errors.",
            [r["asset_url"] for r in css_js_broken], "assets/broken-assets.md", "A",
            count=len(css_js_broken))

    bzpm = [f for f in brand_findings if f["marker"] == WRONG_BRAND and f.get("classification") == "real_issue"]
    if bzpm:
        add("P1", "brand", "Public БЗПМ brand leakage",
            f"{len(bzpm)} pages contain forbidden public brand БЗПМ.",
            [f["url"] for f in bzpm], "brand-scan/public-brand-scan.csv", "D",
            count=len(bzpm))

    if sitemap_info.get("llms_bzpm"):
        add("P1", "brand", "БЗПМ in llms.txt", "llms.txt contains forbidden brand БЗПМ.",
            ["https://bzpm.ru/llms.txt"], "robots-llms/llms-audit.md", "D")

    crit_sec = [r for r in security_rows if r["risk"] == "CRITICAL" and r.get("status") == 200]
    if crit_sec:
        add("P0", "security", "Critical public exposure",
            f"Sensitive paths return 200: {[r['path'] for r in crit_sec]}",
            [r["url"] for r in crit_sec], "security/public-exposure-basic-audit.csv", "A")

    if db_summary.get("available") and db_summary.get("seo_dup_count", 0) > 0:
        add("P2", "seo", "Duplicate SEO URL keywords in DB",
            f"{db_summary['seo_dup_count']} duplicate keyword entries in oc_seo_url.",
            [], "db-readonly/seo-url-duplicates.csv", "B",
            count=db_summary["seo_dup_count"], mutation="yes", db_write="yes")

    if db_summary.get("missing_meta_categories", 0) > 0:
        add("P2", "seo", "Categories missing meta_title in DB",
            f"{db_summary['missing_meta_categories']} active categories lack meta_title.",
            [], "db-readonly/missing-meta-db-crosscheck.csv", "B",
            count=db_summary["missing_meta_categories"], admin="yes")

    add("P4", "operations", "Post-1C import verification pending",
        "Run 4.240 blocked: next post-patch 1C import not yet observed for Lari reparent + TXT Duration confirmation.",
        [], "db-readonly/db-summary.md", "F", mutation="no", fix_type="wait", notes="operational pending")

    chains = [r for r in http_rows if r.get("redirect_hops", 0) > 1]
    if chains:
        add("P2", "http", "Redirect chains >1 hop",
            f"{len(chains)} URLs have redirect chains longer than 1 hop.",
            [r["url"] for r in chains[:5]], "http/http-status-audit.csv", "C",
            count=len(chains))

    write_csv(AUDIT_ROOT / "issue-register" / "SITE-002-FULL-TECH-SEO-AUDIT-ISSUE-REGISTER.csv", issues,
              ["issue_id", "severity", "category", "title", "description", "affected_urls_count",
               "sample_urls", "evidence_file", "likely_owner", "recommended_fix_type", "risk_of_fix",
               "requires_production_mutation", "requires_db_write", "requires_ftp_upload",
               "requires_admin_save", "requires_operator_decision", "dependencies", "suggested_wave", "notes"])
    write_json(AUDIT_ROOT / "issue-register" / "SITE-002-FULL-TECH-SEO-AUDIT-ISSUE-REGISTER.json", issues)

    md = [f"# Issue register\n\nTotal: {len(issues)}\n\n"]
    for sev in ("P0", "P1", "P2", "P3", "P4"):
        grp = [i for i in issues if i["severity"] == sev]
        if grp:
            md.append(f"## {sev} ({len(grp)})\n\n")
            for i in grp:
                md.append(f"- **{i['issue_id']}** — {i['title']}\n")
    write_text(AUDIT_ROOT / "issue-register" / "SITE-002-FULL-TECH-SEO-AUDIT-ISSUE-REGISTER.md", "".join(md))
    return issues


def build_roadmap(issues: list[dict]) -> None:
    waves = {
        "A": {"title": "Critical safety / broken pages", "objective": "Fix P0/P1 production-impacting issues",
              "issue_ids": [i["issue_id"] for i in issues if i["suggested_wave"] == "A"]},
        "B": {"title": "SEO/indexation foundation", "objective": "Sitemap, canonical, meta, DB SEO duplicates",
              "issue_ids": [i["issue_id"] for i in issues if i["suggested_wave"] == "B"]},
        "C": {"title": "Internal link / redirect hygiene", "objective": "Broken links, redirect chains, old paths",
              "issue_ids": [i["issue_id"] for i in issues if i["suggested_wave"] == "C"]},
        "D": {"title": "Catalog/product template/content", "objective": "Category/product specifics, brand cleanup",
              "issue_ids": [i["issue_id"] for i in issues if i["suggested_wave"] == "D"]},
        "E": {"title": "Forms/information pages", "objective": "Static form/page issues",
              "issue_ids": [i["issue_id"] for i in issues if i["suggested_wave"] == "E"]},
        "F": {"title": "Optional polish", "objective": "OG, alt, sitemap /contact, accepted observations",
              "issue_ids": [i["issue_id"] for i in issues if i["suggested_wave"] == "F"]},
    }
    md = [f"# Remediation roadmap\n\nGenerated: {utc_now()}\n\n"]
    for wk, w in waves.items():
        md.append(f"## Wave {wk} — {w['title']}\n\n")
        md.append(f"**Objective:** {w['objective']}\n\n")
        md.append(f"**Issue IDs:** {', '.join(w['issue_ids']) or 'none'}\n\n")
        md.append("- Mutation type: scoped production change with backup\n")
        md.append("- Rollback: Beget backup + git checkpoint\n")
        md.append("- Operator approval: required for P0/P1\n\n")
    write_text(AUDIT_ROOT / "roadmap" / "SITE-002-FULL-TECH-SEO-AUDIT-REMEDIATION-ROADMAP.md", "".join(md))
    write_json(AUDIT_ROOT / "roadmap" / "SITE-002-FULL-TECH-SEO-AUDIT-REMEDIATION-ROADMAP.json", waves)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-db", action="store_true")
    parser.add_argument("--skip-ftp", action="store_true")
    parser.add_argument("--max-urls", type=int, default=0, help="0 = all sitemap URLs")
    args = parser.parse_args()

    print(f"=== {OPERATION_ID} ===", file=sys.stderr)
    ensure_dirs()

    print("Phase 0: sitemap fetch", file=sys.stderr)
    sm_resp = http_fetch("https://bzpm.ru/sitemap.xml")
    sm_xml = (sm_resp.get("body") or b"").decode("utf-8", errors="replace")
    write_text(AUDIT_ROOT / "sitemap" / "sitemap-live.xml", sm_xml)
    sitemap_urls = parse_sitemap(sm_xml)
    if args.max_urls > 0:
        sitemap_urls = sitemap_urls[: args.max_urls]
    print(f"  Sitemap URLs: {len(sitemap_urls)}", file=sys.stderr)

    print("Phase 1: URL inventory", file=sys.stderr)
    inventory = phase_url_inventory(sitemap_urls)

    print("Phase 2: HTTP crawl", file=sys.stderr)
    http_rows, page_cache = phase_http_crawl(inventory)
    http_status = {r["url"]: r["status"] for r in http_rows}

    print("Phase 3: Internal links", file=sys.stderr)
    link_rows = phase_links(page_cache, http_status)

    print("Phase 4: Assets", file=sys.stderr)
    asset_rows = phase_assets(page_cache)

    print("Phase 5: Meta/head", file=sys.stderr)
    phase_meta(page_cache, http_rows)

    print("Phase 6: Sitemap/robots/llms", file=sys.stderr)
    sitemap_info = phase_sitemap_robots_llms(sitemap_urls, http_rows)

    print("Phase 7: Catalog", file=sys.stderr)
    phase_catalog(page_cache, http_rows, sitemap_urls)

    print("Phase 8: Info/forms", file=sys.stderr)
    phase_info_forms(page_cache)

    print("Phase 9: Brand scan", file=sys.stderr)
    brand_findings = phase_brand_scan(page_cache)

    print("Phase 10: Security", file=sys.stderr)
    security_rows = phase_security()

    db_summary: dict[str, Any] = {"available": False}
    if not args.skip_db:
        print("Phase 11: DB readonly", file=sys.stderr)
        db_summary = phase_db_readonly()

    source_rows: list[dict] = []
    if not args.skip_ftp:
        print("Phase 12: Source readonly", file=sys.stderr)
        source_rows = phase_source_readonly()

    print("Phase 13-14: Issue register + roadmap", file=sys.stderr)
    issues = build_issue_register(
        http_rows, link_rows, sitemap_info, brand_findings,
        security_rows, db_summary, asset_rows, sitemap_urls,
    )
    build_roadmap(issues)

    summary = {
        "operation_id": OPERATION_ID, "completed_at": utc_now(),
        "sitemap_url_count": len(sitemap_urls),
        "http_crawled": len(http_rows),
        "issues_total": len(issues),
        "issues_p0": sum(1 for i in issues if i["severity"] == "P0"),
        "issues_p1": sum(1 for i in issues if i["severity"] == "P1"),
        "ftp_reads": stats["ftp_reads"],
        "db_selects": stats["db_selects"],
    }
    write_json(AUDIT_ROOT / "manifests" / "audit-summary.json", summary)
    write_json(AUDIT_ROOT / "logs" / "run-log.json", summary)
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
