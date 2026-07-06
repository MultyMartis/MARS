#!/usr/bin/env python3
"""SITE-002 Production final public meta inventory — read-only (Run 4.206)."""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
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

OPERATION_ID = "SITE-002-PROD-SEO-META-FINAL-INVENTORY-01"
OCPILOT_RUN = "4.206"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-BRAND-ZPM-01"
WRONG_BRAND = "БЗПМ"
CORRECT_BRAND = "ЗПМ"
UTF8_BOM = b"\xef\xbb\xbf"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
DISCOVERY_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-DISCOVERY-01"
)

SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
CRAWL_DELAY_SEC = 0.35
PDP_SAMPLE_TARGET = 120
PDP_SAMPLE_MAX = 150

SEED_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/about",
    "https://bzpm.ru/custom-equipment",
    "https://bzpm.ru/dealers",
    "https://bzpm.ru/delivery",
    "https://bzpm.ru/guarantee",
    "https://bzpm.ru/payment-methods",
    "https://bzpm.ru/contact",
    "https://bzpm.ru/blog",
    "https://bzpm.ru/blog/news",
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
]

KEY_CATEGORY_URLS = [
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-shpilki-i-protivni",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stellazhi",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/moechnye-vanny",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/zonty",
]

TECHNICAL_QUERY_PATTERNS = (
    r"[?&]sort=",
    r"[?&]order=",
    r"[?&]page=\d+",
    r"[?&]limit=",
    r"[?&]route=",
    r"/index\.php",
)

SUBDIRS = (
    "crawl",
    "inventory",
    "samples",
    "brand-audit",
    "llms",
    "sitemap",
    "robots",
    "verification",
    "manifests",
    "reports",
    "logs",
)

FAMILY_MARKERS = {
    "stoly": "stoly",
    "polki": "polki",
    "telezhki-servirovochnye": "telezhki_servirovochnye",
    "telezhki-shpilki-i-protivni": "telezhki",
    "shkafy-i-lari": "shkafy_lari",
    "podtovarniki-i-podstavki": "podstavki",
    "stellazhi": "stellazhi",
    "moechnye-vanny": "moechnye_vanny",
    "zonty": "zonty",
    "zonty-vytyazhnye": "zonty",
}


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


def http_get(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Cache-Control": "no-cache",
            "Accept": "text/html,application/xml,text/plain,*/*",
        },
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
                "content_type": response.headers.get("Content-Type", ""),
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
            "content_type": exc.headers.get("Content-Type", "") if exc.headers else "",
            "body": text,
            "raw_body": body,
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "url": url,
            "final_url": url,
            "status_code": None,
            "x_robots_tag": "",
            "content_type": "",
            "body": "",
            "raw_body": b"",
            "error": str(exc),
        }


def path_parts(url: str) -> list[str]:
    parsed = urllib.parse.urlparse(url)
    return [p for p in parsed.path.split("/") if p]


def is_product_pdp(url: str) -> bool:
    parts = path_parts(url)
    return len(parts) >= 5 and parts[0] == "katalog"


def is_technical_url(url: str) -> bool:
    return any(re.search(p, url, re.I) for p in TECHNICAL_QUERY_PATTERNS)


def classify_page_type(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.rstrip("/") or "/"
    if url.endswith("/llms.txt"):
        return "LLMS"
    if url.endswith("/robots.txt"):
        return "ROBOTS"
    if url.endswith("/sitemap.xml"):
        return "SITEMAP"
    if is_technical_url(url):
        return "TECHNICAL"
    parts = path_parts(url)
    if path == "/" or path == "":
        return "HOME"
    if parts == ["katalog"]:
        return "CATALOG_ROOT"
    if parts and parts[0] == "blog":
        return "BLOG_CATEGORY" if len(parts) > 1 else "BLOG"
    if parts and parts[0] == "katalog":
        if is_product_pdp(url):
            return "PRODUCT_PDP"
        return "CATEGORY"
    info_slugs = {
        "about", "custom-equipment", "dealers", "delivery",
        "guarantee", "payment-methods", "contact",
    }
    if parts and parts[0] in info_slugs:
        return "INFORMATION"
    return "SAFE UNKNOWN"


def detect_pdp_family(url: str) -> str:
    parts = path_parts(url)
    if len(parts) >= 3:
        slug = parts[2]
        if slug in FAMILY_MARKERS:
            return FAMILY_MARKERS[slug]
        if len(parts) >= 4:
            slug4 = parts[3]
            if slug4 in FAMILY_MARKERS:
                return FAMILY_MARKERS[slug4]
    return "generic"


def parse_sitemap_urls(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text)
    return [
        loc.text.strip()
        for loc in root.findall(f".//{SITEMAP_NS}loc")
        if loc.text
    ]


def extract_meta(html_text: str) -> dict[str, Any]:
    parser = MetaParser()
    try:
        parser.feed(html_text)
    except Exception:
        pass
    title = html.unescape(parser.title.strip())
    description = parser.meta.get("description", "")
    keywords = parser.meta.get("keywords", "")
    robots = parser.meta.get("robots", "")
    canonical = ""
    for link in parser.links:
        if link.get("rel") == "canonical":
            canonical = link.get("href", "")
            break
    h1_list = [h for h in parser.h1_list if h]
    return {
        "title": title,
        "meta_description": description,
        "meta_keywords": keywords,
        "meta_robots": robots,
        "canonical": canonical,
        "h1": " | ".join(h1_list),
        "h1_count": len(h1_list),
        "body_count": parser.body_open,
        "yandex_metrika": any(
            t in html_text.lower() for t in ("mc.yandex.ru/metrika", "ym(", "yandex.metrika")
        ),
        "yandex_webmaster": "yandex-verification" in html_text.lower(),
        "load_more_marker": "load-more" in html_text.lower() or "load_more" in html_text.lower(),
    }


def keyword_phrase_count(keywords: str) -> int:
    if not keywords or not keywords.strip():
        return 0
    return len([p for p in re.split(r",\s*", keywords.strip()) if p.strip()])


def has_numeric_pollution(keywords: str) -> bool:
    for phrase in re.split(r",\s*", keywords or ""):
        p = phrase.strip()
        if not p:
            continue
        if re.fullmatch(r"\d+", p):
            return True
        if re.fullmatch(r"\d+([,.]\d+)?", p):
            return True
        compact = re.sub(r"\s", "", p)
        if re.fullmatch(r"\d+([×xх]\d+)+", compact, re.I):
            return True
    return False


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.rstrip("/") or "/"
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, path, "", "", ""))


def brand_snippets(text: str, limit: int = 3) -> list[str]:
    snippets: list[str] = []
    for match in re.finditer(re.escape(WRONG_BRAND), text):
        start = max(0, match.start() - 35)
        end = min(len(text), match.end() + 35)
        snippet = text[start:end].replace("\n", " ").replace("\r", " ")
        snippets.append(re.sub(r"\s+", " ", snippet).strip())
        if len(snippets) >= limit:
            break
    return snippets


def authority_guess(url: str, page_type: str) -> str:
    if page_type == "LLMS":
        return "LLMS"
    if page_type == "PRODUCT_PDP":
        return "PRODUCT_GENERATOR"
    if page_type == "BLOG" or page_type == "BLOG_CATEGORY":
        return "CONTROLLER"
    if page_type == "CATEGORY":
        return "ADMIN_META"
    if page_type == "INFORMATION":
        return "CONTROLLER"
    if page_type == "CATALOG_ROOT":
        return "CONTROLLER"
    if page_type == "HOME":
        return "TEMPLATE"
    return "SAFE UNKNOWN"


def classify_indexability(
    status: int | None,
    final_url: str,
    url: str,
    meta_robots: str,
    x_robots: str,
    page_type: str,
) -> str:
    if status is None:
        return "SAFE UNKNOWN"
    if status in (301, 302, 303, 307, 308):
        return "REDIRECT"
    if status >= 400:
        return "ERROR"
    robots_combined = f"{meta_robots} {x_robots}".lower()
    if "noindex" in robots_combined:
        if page_type == "TECHNICAL" or is_technical_url(url) or is_technical_url(final_url):
            return "TECHNICAL"
        return "NOINDEX"
    if page_type in ("ROBOTS", "SITEMAP", "LLMS"):
        return "INDEXABLE"
    if page_type == "TECHNICAL":
        return "TECHNICAL"
    if status == 200:
        return "INDEXABLE"
    return "SAFE UNKNOWN"


def classify_title(title: str, page_type: str, titles_seen: Counter[str]) -> str:
    if page_type in ("ROBOTS", "SITEMAP", "LLMS"):
        return "TITLE_SAFE_UNKNOWN"
    if not title:
        return "TITLE_MISSING"
    length = len(title)
    if length < 15:
        return "TITLE_TOO_SHORT"
    if length > 70:
        return "TITLE_TOO_LONG"
    if titles_seen[title] > 1:
        return "TITLE_DUPLICATE"
    return "TITLE_OK"


def classify_description(desc: str, page_type: str, desc_seen: Counter[str]) -> str:
    if page_type in ("ROBOTS", "SITEMAP", "LLMS"):
        return "DESCRIPTION_SAFE_UNKNOWN"
    if not desc:
        if page_type == "PRODUCT_PDP":
            return "DESCRIPTION_MISSING"
        if page_type in ("HOME", "CATEGORY", "INFORMATION", "BLOG", "BLOG_CATEGORY", "CATALOG_ROOT"):
            return "DESCRIPTION_MISSING"
        return "DESCRIPTION_SAFE_UNKNOWN"
    length = len(desc)
    if length < 50:
        return "DESCRIPTION_TOO_SHORT"
    if length > 320:
        return "DESCRIPTION_TOO_LONG"
    if desc_seen[desc] > 1:
        return "DESCRIPTION_DUPLICATE"
    return "DESCRIPTION_OK"


def classify_keywords(keywords: str, page_type: str, kw_seen: Counter[str]) -> str:
    if page_type in ("ROBOTS", "SITEMAP", "LLMS", "INFORMATION", "BLOG", "BLOG_CATEGORY", "HOME", "CATALOG_ROOT", "CATEGORY"):
        if not keywords:
            return "KEYWORDS_EMPTY_ALLOWED"
        return "KEYWORDS_OK" if not has_numeric_pollution(keywords) else "KEYWORDS_NUMERIC_POLLUTION"
    if page_type == "PRODUCT_PDP":
        if not keywords:
            return "KEYWORDS_MISSING"
        if has_numeric_pollution(keywords):
            return "KEYWORDS_NUMERIC_POLLUTION"
        if len(keywords) > 320:
            return "KEYWORDS_TOO_LONG"
        if kw_seen[keywords] > 1:
            return "KEYWORDS_DUPLICATE_SPAM"
        return "KEYWORDS_OK"
    return "KEYWORDS_SAFE_UNKNOWN"


def classify_brand(text_fields: str) -> str:
    if WRONG_BRAND in text_fields:
        return "BRAND_FORBIDDEN_BZPM"
    if CORRECT_BRAND in text_fields:
        return "BRAND_OK_ZPM"
    return "BRAND_MISSING_OK"


def classify_canonical(canonical: str, final_url: str, page_type: str) -> str:
    if page_type in ("ROBOTS", "SITEMAP", "LLMS"):
        return "CANONICAL_SAFE_UNKNOWN"
    if not canonical:
        return "CANONICAL_MISSING"
    if normalize_url(canonical) != normalize_url(final_url):
        return "CANONICAL_MISMATCH"
    return "CANONICAL_OK"


def classify_robots(meta_robots: str, x_robots: str, indexability: str, page_type: str) -> str:
    combined = f"{meta_robots} {x_robots}".lower()
    if page_type in ("ROBOTS", "SITEMAP", "LLMS"):
        return "ROBOTS_SAFE_UNKNOWN"
    if "noindex" in combined:
        if indexability == "TECHNICAL" or page_type == "TECHNICAL":
            return "ROBOTS_EXPECTED_NOINDEX"
        return "ROBOTS_UNEXPECTED_NOINDEX"
    return "ROBOTS_OK"


def pdp_description_quality(desc: str) -> str:
    if not desc:
        return "MISSING"
    length = len(desc)
    if length < 50:
        return "TOO_SHORT"
    if length > 320:
        return "TOO_LONG"
    generic_markers = ("купить", "заказать", "цена", "доставка")
    if not any(m in desc.lower() for m in generic_markers):
        return "GENERIC"
    return "OK"


def pdp_keywords_quality(keywords: str) -> str:
    if not keywords:
        return "MISSING"
    if has_numeric_pollution(keywords):
        return "POLLUTED"
    if len(keywords) > 320:
        return "TOO_LONG"
    return "OK"


def sample_pdp_urls(all_pdp: list[str], target: int = PDP_SAMPLE_TARGET) -> list[str]:
    by_family: dict[str, list[str]] = defaultdict(list)
    for url in all_pdp:
        by_family[detect_pdp_family(url)].append(url)
    families = sorted(by_family.keys())
    if not families:
        return all_pdp[:target]
    per_family = max(8, target // max(len(families), 1))
    sampled: list[str] = []
    for family in families:
        bucket = by_family[family]
        step = max(1, len(bucket) // per_family)
        picks = bucket[::step][:per_family]
        sampled.extend(picks)
    if len(sampled) < target:
        remaining = [u for u in all_pdp if u not in sampled]
        step = max(1, len(remaining) // max(target - len(sampled), 1))
        sampled.extend(remaining[::step][: target - len(sampled)])
    return sampled[:PDP_SAMPLE_MAX]


def load_discovery_pdp_urls() -> list[str]:
    sample_path = DISCOVERY_ROOT / "pdp-samples" / "pdp-url-samples.json"
    if not sample_path.exists():
        return []
    data = json.loads(sample_path.read_text(encoding="utf-8"))
    return [r["product_url"] for r in data if r.get("include") == "yes"]


def ensure_layout() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "change_type": "final-meta-inventory-readonly",
        "remote_changes_allowed": False,
        "admin_save_allowed": False,
        "db_write_allowed": False,
        "cache_clear_allowed": False,
        "ftp_upload_allowed": False,
        "header_footer_change_allowed": False,
        "robots_change_allowed": False,
        "sitemap_change_allowed": False,
        "brand_policy_correct": CORRECT_BRAND,
        "brand_policy_forbidden_public": WRONG_BRAND,
        "domain_bzpm_ru_allowed": True,
        "captured_at": utc_now(),
        "ocpilot_run": OCPILOT_RUN,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)


def phase1_url_inventory() -> tuple[list[str], list[dict[str, Any]]]:
    print("Phase 1: URL inventory...")
    sitemap_resp = http_get("https://bzpm.ru/sitemap.xml")
    sitemap_urls: list[str] = []
    if sitemap_resp["body"].strip().startswith("<"):
        try:
            sitemap_urls = parse_sitemap_urls(sitemap_resp["body"])
        except ET.ParseError:
            pass
    (DEPLOYMENT_ROOT / "sitemap" / "sitemap-response.xml").write_bytes(
        sitemap_resp.get("raw_body") or b""
    )

    all_known: dict[str, dict[str, Any]] = {}
    for url in sitemap_urls:
        all_known[normalize_url(url)] = {
            "url": url,
            "source": "sitemap",
            "sitemap_present": "yes",
        }
    for url in SEED_URLS + KEY_CATEGORY_URLS:
        key = normalize_url(url)
        if key not in all_known:
            all_known[key] = {"url": url, "source": "seed", "sitemap_present": "no"}
        else:
            all_known[key]["source"] = all_known[key]["source"] + "+seed"

    inventory_rows: list[dict[str, Any]] = []
    pdp_urls: list[str] = []
    for key in sorted(all_known.keys()):
        entry = all_known[key]
        url = entry["url"]
        page_type = classify_page_type(url)
        include = "yes"
        reason = "core route"
        if page_type == "PRODUCT_PDP":
            pdp_urls.append(url)
            include = "sample"
            reason = "PDP sampled for meta crawl"
        elif page_type == "SAFE UNKNOWN":
            include = "no"
            reason = "unclassified route — excluded from meta crawl"
        elif page_type == "TECHNICAL":
            include = "optional"
            reason = "technical/query route"
        inventory_rows.append({
            "url": url,
            "source": entry["source"],
            "page_type": page_type,
            "include_in_meta_inventory": include,
            "reason": reason,
            "sitemap_present": entry.get("sitemap_present", "no"),
        })

    sampled_pdp = sample_pdp_urls(pdp_urls)
    discovery_pdp = load_discovery_pdp_urls()
    for u in discovery_pdp:
        if u not in sampled_pdp:
            sampled_pdp.append(u)
    sampled_pdp = sampled_pdp[:PDP_SAMPLE_MAX]
    sampled_set = set(sampled_pdp)

    for row in inventory_rows:
        if row["page_type"] == "PRODUCT_PDP":
            row["include_in_meta_inventory"] = "yes" if row["url"] in sampled_set else "no"
            row["reason"] = (
                "PDP included in stratified sample"
                if row["url"] in sampled_set
                else "PDP excluded — sample cap"
            )

    crawl_urls = [
        row["url"]
        for row in inventory_rows
        if row["include_in_meta_inventory"] == "yes"
    ]
    for url in SEED_URLS:
        if url not in crawl_urls:
            crawl_urls.append(url)

    fields = ["url", "source", "page_type", "include_in_meta_inventory", "reason", "sitemap_present"]
    write_csv(DEPLOYMENT_ROOT / "inventory" / "url-inventory.csv", inventory_rows, fields)
    write_json(
        DEPLOYMENT_ROOT / "inventory" / "url-inventory.json",
        {
            "captured_at": utc_now(),
            "sitemap_url_count": len(sitemap_urls),
            "inventory_total": len(inventory_rows),
            "crawl_url_count": len(crawl_urls),
            "pdp_total": len(pdp_urls),
            "pdp_sampled": len(sampled_pdp),
            "rows": inventory_rows,
            "crawl_urls": crawl_urls,
        },
    )
    summary = [
        "# URL inventory summary",
        "",
        f"Captured: {utc_now()}",
        "",
        f"| Sitemap URLs | {len(sitemap_urls)} |",
        f"| Inventory rows | {len(inventory_rows)} |",
        f"| Crawl URLs | {len(crawl_urls)} |",
        f"| PDP total | {len(pdp_urls)} |",
        f"| PDP sampled | {len(sampled_pdp)} |",
        "",
        "## By page type",
        "",
    ]
    type_counts = Counter(r["page_type"] for r in inventory_rows)
    for pt, cnt in sorted(type_counts.items()):
        summary.append(f"- **{pt}**: {cnt}")
    write_text(DEPLOYMENT_ROOT / "inventory" / "url-inventory-summary.md", "\n".join(summary) + "\n")
    return crawl_urls, inventory_rows


def phase2_meta_crawl(crawl_urls: list[str]) -> list[dict[str, Any]]:
    print(f"Phase 2: Meta crawl ({len(crawl_urls)} URLs)...")
    rows: list[dict[str, Any]] = []
    for idx, url in enumerate(crawl_urls, 1):
        if idx > 1:
            time.sleep(CRAWL_DELAY_SEC)
        resp = http_get(url)
        body = resp.get("body") or ""
        raw = resp.get("raw_body") or b""
        page_type = classify_page_type(url)
        is_html = "<html" in body.lower() or page_type in (
            "HOME", "CATALOG_ROOT", "CATEGORY", "PRODUCT_PDP",
            "INFORMATION", "BLOG", "BLOG_CATEGORY",
        )
        meta = extract_meta(body) if is_html else {
            "title": "", "meta_description": "", "meta_keywords": "",
            "meta_robots": "", "canonical": "", "h1": "", "h1_count": 0,
            "body_count": 0, "yandex_metrika": False, "yandex_webmaster": False,
            "load_more_marker": False,
        }
        status = resp["status_code"]
        final_url = resp["final_url"]
        indexability = classify_indexability(
            status, final_url, url, meta.get("meta_robots", ""),
            resp.get("x_robots_tag", ""), page_type,
        )
        canonical = meta.get("canonical", "")
        row: dict[str, Any] = {
            "url": url,
            "http_status": status,
            "final_url": final_url,
            "page_type": page_type,
            "title": meta.get("title", ""),
            "title_length": len(meta.get("title", "")),
            "meta_description": meta.get("meta_description", ""),
            "description_length": len(meta.get("meta_description", "")),
            "meta_keywords": meta.get("meta_keywords", ""),
            "keywords_length": len(meta.get("meta_keywords", "")),
            "keywords_phrase_count": keyword_phrase_count(meta.get("meta_keywords", "")),
            "canonical": canonical,
            "canonical_matches_final_url": (
                "yes" if canonical and normalize_url(canonical) == normalize_url(final_url) else "no"
            ),
            "meta_robots": meta.get("meta_robots", ""),
            "x_robots_tag": resp.get("x_robots_tag", ""),
            "h1": meta.get("h1", ""),
            "h1_count": meta.get("h1_count", 0),
            "indexability": indexability,
            "body_count": meta.get("body_count", 0),
            "yandex_metrika_present": meta.get("yandex_metrika", False),
            "yandex_webmaster_present": meta.get("yandex_webmaster", False),
            "load_more_marker": meta.get("load_more_marker", False),
            "error": resp.get("error"),
            "contains_forbidden_bzpm": WRONG_BRAND in body,
            "forbidden_bzpm_count": body.count(WRONG_BRAND),
            "contains_zpm": CORRECT_BRAND in body,
            "zpm_count": body.count(CORRECT_BRAND),
            "bzpm_ru_domain_present": "bzpm.ru" in body.lower(),
        }
        if page_type == "LLMS":
            row["llms_utf8_valid"] = True
            try:
                raw.decode("utf-8")
            except UnicodeDecodeError:
                row["llms_utf8_valid"] = False
            row["llms_bom_present"] = raw.startswith(UTF8_BOM)
            row["llms_mojibake"] = "Ð" in body or "Ñ" in body
        if page_type == "SITEMAP" and body.strip().startswith("<"):
            try:
                row["sitemap_url_count"] = len(parse_sitemap_urls(body))
            except ET.ParseError:
                row["sitemap_url_count"] = 0
        if page_type == "ROBOTS":
            row["robots_sitemap_directive"] = "yes" if re.search(r"(?mi)^sitemap:", body) else "no"
        rows.append(row)
        if idx % 25 == 0:
            print(f"  crawled {idx}/{len(crawl_urls)}")

    raw_fields = list(rows[0].keys()) if rows else []
    write_json(
        DEPLOYMENT_ROOT / "crawl" / "meta-crawl-raw.json",
        {"captured_at": utc_now(), "url_count": len(rows), "rows": rows},
    )
    write_csv(DEPLOYMENT_ROOT / "crawl" / "meta-crawl-raw.csv", rows, raw_fields)
    write_json(DEPLOYMENT_ROOT / "inventory" / "final-meta-inventory.json", {"captured_at": utc_now(), "rows": rows})
    write_csv(DEPLOYMENT_ROOT / "inventory" / "final-meta-inventory.csv", rows, raw_fields)

    md_lines = [
        "# Final meta inventory",
        "",
        f"Captured: {utc_now()}",
        f"URLs crawled: {len(rows)}",
        "",
        "| URL | Type | Status | Title len | Desc len | Indexability | БЗПМ |",
        "|-----|------|--------|-----------|----------|--------------|------|",
    ]
    for r in rows[:200]:
        md_lines.append(
            f"| {r['url']} | {r['page_type']} | {r['http_status']} | "
            f"{r['title_length']} | {r['description_length']} | {r['indexability']} | "
            f"{r['forbidden_bzpm_count']} |"
        )
    if len(rows) > 200:
        md_lines.append(f"\n… and {len(rows) - 200} more rows in CSV/JSON.")
    write_text(DEPLOYMENT_ROOT / "inventory" / "final-meta-inventory.md", "\n".join(md_lines) + "\n")

    try:
        import openpyxl  # type: ignore
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "meta-inventory"
        ws.append(raw_fields)
        for r in rows:
            ws.append([r.get(f) for f in raw_fields])
        wb.save(DEPLOYMENT_ROOT / "inventory" / "final-meta-inventory.xlsx")
    except ImportError:
        write_text(
            DEPLOYMENT_ROOT / "inventory" / "final-meta-inventory.xlsx.skip",
            "openpyxl not installed — xlsx skipped\n",
        )
    return rows


def phase3_quality_classification(crawl_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    print("Phase 3: Meta quality classification...")
    titles = Counter(r["title"] for r in crawl_rows if r.get("title"))
    descs = Counter(r["meta_description"] for r in crawl_rows if r.get("meta_description"))
    kws = Counter(r["meta_keywords"] for r in crawl_rows if r.get("meta_keywords"))
    classified: list[dict[str, Any]] = []
    for row in crawl_rows:
        pt = row["page_type"]
        brand_text = " ".join([
            row.get("title", ""), row.get("meta_description", ""),
            row.get("meta_keywords", ""), row.get("h1", ""),
        ])
        q = {
            **row,
            "title_class": classify_title(row.get("title", ""), pt, titles),
            "description_class": classify_description(row.get("meta_description", ""), pt, descs),
            "keywords_class": classify_keywords(row.get("meta_keywords", ""), pt, kws),
            "brand_class": classify_brand(brand_text),
            "canonical_class": classify_canonical(
                row.get("canonical", ""), row.get("final_url", ""), pt,
            ),
            "robots_class": classify_robots(
                row.get("meta_robots", ""), row.get("x_robots_tag", ""),
                row.get("indexability", ""), pt,
            ),
        }
        classified.append(q)

    fields = list(classified[0].keys()) if classified else []
    write_csv(DEPLOYMENT_ROOT / "inventory" / "meta-quality-classification.csv", classified, fields)
    write_json(
        DEPLOYMENT_ROOT / "inventory" / "meta-quality-classification.json",
        {"captured_at": utc_now(), "rows": classified},
    )
    summary_counts = {
        "title": Counter(r["title_class"] for r in classified),
        "description": Counter(r["description_class"] for r in classified),
        "keywords": Counter(r["keywords_class"] for r in classified),
        "brand": Counter(r["brand_class"] for r in classified),
        "canonical": Counter(r["canonical_class"] for r in classified),
        "robots": Counter(r["robots_class"] for r in classified),
    }
    md = ["# Meta quality summary", "", f"Captured: {utc_now()}", ""]
    for section, counter in summary_counts.items():
        md.append(f"## {section}")
        md.append("")
        for k, v in sorted(counter.items()):
            md.append(f"- {k}: {v}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "inventory" / "meta-quality-summary.md", "\n".join(md) + "\n")
    return classified


def phase4_brand_audit(crawl_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    print("Phase 4: Brand regression audit...")
    audit_rows: list[dict[str, Any]] = []
    for row in crawl_rows:
        url = row["url"]
        pt = row["page_type"]
        resp = http_get(url) if False else None  # body already in crawl — reuse counts
        body_snippets: list[str] = []
        if row.get("forbidden_bzpm_count", 0) > 0:
            # re-fetch only if violation for snippets — use stored fields
            body_snippets = brand_snippets(
                " ".join([
                    row.get("title", ""), row.get("meta_description", ""),
                    row.get("meta_keywords", ""), row.get("h1", ""),
                ])
            )
        violation = row.get("forbidden_bzpm_count", 0) > 0
        audit_rows.append({
            "url": url,
            "response_type": pt,
            "contains_forbidden_bzpm": "yes" if violation else "no",
            "count_forbidden_bzpm": row.get("forbidden_bzpm_count", 0),
            "contexts_snippets_sanitized": body_snippets,
            "contains_correct_zpm": "yes" if row.get("contains_zpm") else "no",
            "count_zpm": row.get("zpm_count", 0),
            "bzpm_ru_domain_present": "yes" if row.get("bzpm_ru_domain_present") else "no",
            "violation": "yes" if violation else "no",
            "authority_guess_if_violation": authority_guess(url, pt) if violation else "",
        })

    fields = list(audit_rows[0].keys()) if audit_rows else []
    write_csv(DEPLOYMENT_ROOT / "brand-audit" / "brand-regression-audit.csv", audit_rows, fields)
    write_json(
        DEPLOYMENT_ROOT / "brand-audit" / "brand-regression-audit.json",
        {"captured_at": utc_now(), "violation_count": sum(1 for r in audit_rows if r["violation"] == "yes"), "rows": audit_rows},
    )
    violations = [r for r in audit_rows if r["violation"] == "yes"]
    md = [
        "# Brand regression audit",
        "",
        f"Captured: {utc_now()}",
        "",
        f"URLs audited: {len(audit_rows)}",
        f"Violations (`{WRONG_BRAND}`): {len(violations)}",
        "",
    ]
    if violations:
        md.append("## Violations")
        md.append("")
        for v in violations:
            md.append(f"- {v['url']} — count {v['count_forbidden_bzpm']} — {v['authority_guess_if_violation']}")
    else:
        md.append(f"No public `{WRONG_BRAND}` detected in crawled responses.")
    write_text(DEPLOYMENT_ROOT / "brand-audit" / "brand-regression-audit.md", "\n".join(md) + "\n")
    return audit_rows


def phase5_product_samples(classified: list[dict[str, Any]]) -> list[dict[str, Any]]:
    print("Phase 5: Product meta sample analysis...")
    pdp_rows = [r for r in classified if r["page_type"] == "PRODUCT_PDP"]
    samples: list[dict[str, Any]] = []
    for row in pdp_rows:
        parts = path_parts(row["url"])
        family = detect_pdp_family(row["url"])
        category = parts[2] if len(parts) > 2 else ""
        name = row.get("h1") or row.get("title", "")
        desc = row.get("meta_description", "")
        kw = row.get("meta_keywords", "")
        samples.append({
            "url": row["url"],
            "product_name": name,
            "family_category": family,
            "category_slug": category,
            "title": row.get("title", ""),
            "meta_description": desc,
            "meta_keywords": kw,
            "description_contains_kupit": "yes" if "купить" in desc.lower() else "no",
            "description_contains_zpm": "yes" if CORRECT_BRAND in desc else "no",
            "description_contains_bzpm": "yes" if WRONG_BRAND in desc else "no",
            "keywords_contain_zpm": "yes" if CORRECT_BRAND in kw else "no",
            "keywords_contain_bzpm": "yes" if WRONG_BRAND in kw else "no",
            "numeric_only_keyword_pollution": "yes" if has_numeric_pollution(kw) else "no",
            "keyword_phrase_count": keyword_phrase_count(kw),
            "description_quality": pdp_description_quality(desc),
            "keywords_quality": pdp_keywords_quality(kw),
        })
    fields = list(samples[0].keys()) if samples else []
    write_csv(DEPLOYMENT_ROOT / "samples" / "product-meta-sample-analysis.csv", samples, fields)
    write_json(
        DEPLOYMENT_ROOT / "samples" / "product-meta-sample-analysis.json",
        {
            "captured_at": utc_now(),
            "sample_count": len(samples),
            "description_ok": sum(1 for s in samples if s["description_quality"] == "OK"),
            "keywords_ok": sum(1 for s in samples if s["keywords_quality"] == "OK"),
            "bzpm_in_description": sum(1 for s in samples if s["description_contains_bzpm"] == "yes"),
            "bzpm_in_keywords": sum(1 for s in samples if s["keywords_contain_bzpm"] == "yes"),
            "rows": samples,
        },
    )
    md = [
        "# Product meta sample analysis",
        "",
        f"Sample count: {len(samples)}",
        f"Description OK: {sum(1 for s in samples if s['description_quality'] == 'OK')}",
        f"Keywords OK: {sum(1 for s in samples if s['keywords_quality'] == 'OK')}",
        f"Forbidden brand in description: {sum(1 for s in samples if s['description_contains_bzpm'] == 'yes')}",
        f"Forbidden brand in keywords: {sum(1 for s in samples if s['keywords_contain_bzpm'] == 'yes')}",
    ]
    write_text(DEPLOYMENT_ROOT / "samples" / "product-meta-sample-analysis.md", "\n".join(md) + "\n")
    return samples


def phase6_non_product_samples(classified: list[dict[str, Any]]) -> list[dict[str, Any]]:
    print("Phase 6: Non-product meta analysis...")
    types = {"HOME", "CATALOG_ROOT", "CATEGORY", "INFORMATION", "BLOG", "BLOG_CATEGORY", "TECHNICAL"}
    rows = [r for r in classified if r["page_type"] in types]
    samples: list[dict[str, Any]] = []
    for row in rows:
        samples.append({
            "url": row["url"],
            "page_type": row["page_type"],
            "title": row.get("title", ""),
            "meta_description": row.get("meta_description", ""),
            "meta_keywords": row.get("meta_keywords", ""),
            "title_class": row.get("title_class"),
            "description_class": row.get("description_class"),
            "robots_class": row.get("robots_class"),
            "brand_class": row.get("brand_class"),
            "canonical_class": row.get("canonical_class"),
            "indexability": row.get("indexability"),
        })
    fields = list(samples[0].keys()) if samples else []
    write_csv(DEPLOYMENT_ROOT / "samples" / "non-product-meta-analysis.csv", samples, fields)
    write_json(
        DEPLOYMENT_ROOT / "samples" / "non-product-meta-analysis.json",
        {"captured_at": utc_now(), "count": len(samples), "rows": samples},
    )
    issues = [
        s for s in samples
        if s["description_class"] == "DESCRIPTION_MISSING"
        or s["brand_class"] == "BRAND_FORBIDDEN_BZPM"
        or s["robots_class"] == "ROBOTS_UNEXPECTED_NOINDEX"
        or s["canonical_class"] == "CANONICAL_MISMATCH"
    ]
    md = [
        "# Non-product meta analysis",
        "",
        f"Pages analyzed: {len(samples)}",
        f"Issues flagged: {len(issues)}",
        "",
    ]
    for s in issues:
        md.append(f"- {s['url']} — desc:{s['description_class']} brand:{s['brand_class']} robots:{s['robots_class']}")
    write_text(DEPLOYMENT_ROOT / "samples" / "non-product-meta-analysis.md", "\n".join(md) + "\n")
    return samples


def phase7_special_files(crawl_rows: list[dict[str, Any]]) -> dict[str, Any]:
    print("Phase 7: Special file checks...")
    llms_resp = http_get("https://bzpm.ru/llms.txt")
    robots_resp = http_get("https://bzpm.ru/robots.txt")
    sitemap_resp = http_get("https://bzpm.ru/sitemap.xml")
    raw_llms = llms_resp.get("raw_body") or b""
    llms_text = llms_resp.get("body") or ""
    (DEPLOYMENT_ROOT / "llms" / "llms-response.txt").write_bytes(raw_llms)
    (DEPLOYMENT_ROOT / "robots" / "robots-response.txt").write_bytes(robots_resp.get("raw_body") or b"")
    (DEPLOYMENT_ROOT / "sitemap" / "sitemap-response.xml").write_bytes(sitemap_resp.get("raw_body") or b"")

    llms_check = {
        "url": "https://bzpm.ru/llms.txt",
        "http_status": llms_resp["status_code"],
        "utf8_valid": True,
        "bom_present": raw_llms.startswith(UTF8_BOM),
        "contains_zpm": CORRECT_BRAND in llms_text,
        "contains_forbidden_bzpm": WRONG_BRAND in llms_text,
        "mojibake_detected": bool(re.search(r"[ÐÑÃ]", llms_text)),
        "readable_russian": bool(re.search(r"[а-яА-ЯёЁ]", llms_text)),
        "internal_paths_leak": bool(re.search(r"(?i)(/public_html/|AI MARS|MARS-Localhost|secrets\.md)", llms_text)),
        "dev_urls_leak": bool(re.search(r"new-site\.space", llms_text)),
    }
    try:
        raw_llms.decode("utf-8")
    except UnicodeDecodeError:
        llms_check["utf8_valid"] = False

    robots_text = robots_resp.get("body") or ""
    robots_check = {
        "url": "https://bzpm.ru/robots.txt",
        "http_status": robots_resp["status_code"],
        "sitemap_directive_present": bool(re.search(r"(?mi)^sitemap:", robots_text)),
        "contains_forbidden_bzpm": WRONG_BRAND in robots_text,
        "blocks_main_catalog": bool(re.search(r"(?mi)^disallow:\s*/katalog", robots_text)),
        "blocks_products": bool(re.search(r"(?mi)^disallow:\s*/katalog/.+/.*", robots_text)),
    }

    sitemap_text = sitemap_resp.get("body") or ""
    sitemap_urls: list[str] = []
    malformed = 0
    non_bzpm = 0
    if sitemap_text.strip().startswith("<"):
        try:
            sitemap_urls = parse_sitemap_urls(sitemap_text)
            for u in sitemap_urls:
                if not u.startswith("https://bzpm.ru/"):
                    non_bzpm += 1
                if not u.startswith("http"):
                    malformed += 1
        except ET.ParseError:
            malformed = -1

    sitemap_check = {
        "url": "https://bzpm.ru/sitemap.xml",
        "http_status": sitemap_resp["status_code"],
        "valid_xml": malformed != -1,
        "url_count": len(sitemap_urls),
        "non_bzpm_urls": non_bzpm,
        "malformed_urls": malformed,
    }

    write_json(DEPLOYMENT_ROOT / "llms" / "llms-final-check.json", llms_check)
    write_json(DEPLOYMENT_ROOT / "robots" / "robots-final-check.json", robots_check)
    write_json(DEPLOYMENT_ROOT / "sitemap" / "sitemap-final-check.json", sitemap_check)

    for name, check, folder in (
        ("llms", llms_check, "llms"),
        ("robots", robots_check, "robots"),
        ("sitemap", sitemap_check, "sitemap"),
    ):
        md = [f"# {name} final check", "", f"Captured: {utc_now()}", ""]
        for k, v in check.items():
            md.append(f"- **{k}**: {v}")
        write_text(DEPLOYMENT_ROOT / folder / f"{name}-final-check.md", "\n".join(md) + "\n")

    return {"llms": llms_check, "robots": robots_check, "sitemap": sitemap_check}


def compute_risk_level(
    brand_violations: int,
    missing_core_meta: int,
    product_issues: int,
    special: dict[str, Any],
) -> str:
    if brand_violations > 0:
        return "RED"
    if not special["llms"]["bom_present"] or not special["llms"]["utf8_valid"]:
        return "RED"
    if special["llms"]["contains_forbidden_bzpm"]:
        return "RED"
    if not special["robots"]["sitemap_directive_present"]:
        return "RED"
    if special["sitemap"]["url_count"] < 100:
        return "RED"
    if missing_core_meta > 3 or product_issues > 10:
        return "YELLOW"
    if missing_core_meta > 0 or product_issues > 0:
        return "YELLOW"
    return "GREEN"


def phase8_dashboard(
    inventory_rows: list[dict[str, Any]],
    classified: list[dict[str, Any]],
    brand_audit: list[dict[str, Any]],
    product_samples: list[dict[str, Any]],
    special: dict[str, Any],
) -> dict[str, Any]:
    print("Phase 8: Summary dashboard...")
    indexable_html = [
        r for r in classified
        if r.get("indexability") == "INDEXABLE"
        and r["page_type"] not in ("ROBOTS", "SITEMAP", "LLMS")
    ]
    core_types = {"HOME", "CATALOG_ROOT", "CATEGORY", "INFORMATION", "BLOG", "BLOG_CATEGORY"}
    missing_core = [
        r for r in classified
        if r["page_type"] in core_types
        and r.get("indexability") == "INDEXABLE"
        and r.get("description_class") == "DESCRIPTION_MISSING"
    ]
    product_issues = [
        s for s in product_samples
        if s["description_quality"] != "OK"
        or s["keywords_quality"] != "OK"
        or s["description_contains_bzpm"] == "yes"
        or s["keywords_contain_bzpm"] == "yes"
    ]
    brand_violations = sum(1 for b in brand_audit if b["violation"] == "yes")
    dashboard = {
        "captured_at": utc_now(),
        "operation_id": OPERATION_ID,
        "total_urls_inventoried": len(inventory_rows),
        "total_urls_crawled": len(classified),
        "count_by_page_type": dict(Counter(r["page_type"] for r in classified)),
        "indexable_html_count": len(indexable_html),
        "missing_title_count": sum(1 for r in classified if r.get("title_class") == "TITLE_MISSING"),
        "missing_description_count": sum(1 for r in classified if r.get("description_class") == "DESCRIPTION_MISSING"),
        "missing_keywords_pdp_count": sum(
            1 for r in classified
            if r["page_type"] == "PRODUCT_PDP" and r.get("keywords_class") == "KEYWORDS_MISSING"
        ),
        "overlong_description_count": sum(1 for r in classified if r.get("description_class") == "DESCRIPTION_TOO_LONG"),
        "duplicate_title_count": sum(1 for r in classified if r.get("title_class") == "TITLE_DUPLICATE"),
        "duplicate_description_count": sum(1 for r in classified if r.get("description_class") == "DESCRIPTION_DUPLICATE"),
        "forbidden_bzpm_count": brand_violations,
        "product_sample_count": len(product_samples),
        "product_sample_ok_description": sum(1 for s in product_samples if s["description_quality"] == "OK"),
        "product_sample_ok_keywords": sum(1 for s in product_samples if s["keywords_quality"] == "OK"),
        "technical_noindex_count": sum(1 for r in classified if r.get("indexability") == "TECHNICAL"),
        "unexpected_noindex_count": sum(1 for r in classified if r.get("robots_class") == "ROBOTS_UNEXPECTED_NOINDEX"),
        "robots_status": "OK" if special["robots"]["sitemap_directive_present"] else "FAIL",
        "sitemap_status": "OK" if special["sitemap"]["url_count"] >= 100 else "FAIL",
        "llms_status": "OK" if special["llms"]["bom_present"] and not special["llms"]["contains_forbidden_bzpm"] else "FAIL",
        "yandex_metrika_on_home": any(
            r.get("yandex_metrika_present") for r in classified if r["page_type"] == "HOME"
        ),
        "single_body_home": all(
            r.get("body_count", 0) <= 1 for r in classified if r["page_type"] == "HOME"
        ),
        "final_risk_level": compute_risk_level(
            brand_violations, len(missing_core), len(product_issues), special,
        ),
    }
    write_json(DEPLOYMENT_ROOT / "reports" / "final-meta-dashboard.json", dashboard)
    md = [
        "# Final meta dashboard",
        "",
        f"Captured: {utc_now()}",
        "",
        f"**Risk level: {dashboard['final_risk_level']}**",
        "",
    ]
    for k, v in dashboard.items():
        if k not in ("captured_at", "operation_id", "count_by_page_type"):
            md.append(f"- **{k}**: {v}")
    md.append("")
    md.append("## Page types")
    for k, v in sorted(dashboard["count_by_page_type"].items()):
        md.append(f"- {k}: {v}")
    write_text(DEPLOYMENT_ROOT / "reports" / "final-meta-dashboard.md", "\n".join(md) + "\n")
    return dashboard


def phase9_next_action(dashboard: dict[str, Any], brand_audit: list[dict[str, Any]]) -> None:
    print("Phase 9: Next action plan...")
    risk = dashboard["final_risk_level"]
    proposals: list[dict[str, str]] = []
    if dashboard["forbidden_bzpm_count"] > 0:
        proposals.append({
            "operation": "SITE-002-PROD-BRAND-ZPM-REMEDIATION-02",
            "reason": f"Public {WRONG_BRAND} remains in {dashboard['forbidden_bzpm_count']} URLs",
        })
    if dashboard["missing_description_count"] > 0 or dashboard["unexpected_noindex_count"] > 0:
        proposals.append({
            "operation": "SITE-002-PROD-SEO-META-EDGE-FIX-01",
            "reason": "Edge meta gaps or unexpected noindex on indexable routes",
        })
    pdp_kw_missing = dashboard.get("missing_keywords_pdp_count", 0)
    if pdp_kw_missing > 5:
        proposals.append({
            "operation": "SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-TUNE-02",
            "reason": f"Product generator gaps — {pdp_kw_missing} PDP missing keywords",
        })

    if risk == "GREEN" and not proposals:
        recommendation = "no_immediate_production_mutation"
        actions = [
            "Routine monitoring of meta and brand policy",
            "Optional periodic meta crawl (quarterly)",
            "Optional Google/Yandex Webmaster sitemap resubmit if not done recently",
        ]
    else:
        recommendation = "follow_up_operations_proposed"
        actions = [p["operation"] + ": " + p["reason"] for p in proposals]

    plan = {
        "captured_at": utc_now(),
        "final_risk_level": risk,
        "recommendation": recommendation,
        "proposed_operations": proposals,
        "actions": actions,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "next-action-plan.json", plan)
    md = ["# Next action plan", "", f"Risk: {risk}", "", f"Recommendation: {recommendation}", ""]
    for a in actions:
        md.append(f"- {a}")
    write_text(DEPLOYMENT_ROOT / "manifests" / "next-action-plan.md", "\n".join(md) + "\n")


def run_all() -> dict[str, Any]:
    ensure_layout()
    crawl_urls, inventory_rows = phase1_url_inventory()
    crawl_rows = phase2_meta_crawl(crawl_urls)
    classified = phase3_quality_classification(crawl_rows)
    brand_audit = phase4_brand_audit(crawl_rows)
    product_samples = phase5_product_samples(classified)
    non_product = phase6_non_product_samples(classified)
    special = phase7_special_files(crawl_rows)
    dashboard = phase8_dashboard(inventory_rows, classified, brand_audit, product_samples, special)
    phase9_next_action(dashboard, brand_audit)
    write_text(
        DEPLOYMENT_ROOT / "logs" / "run.log",
        f"{utc_now()} {OPERATION_ID} complete — risk {dashboard['final_risk_level']}\n",
    )
    return dashboard


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--phase", choices=("all", "1", "2"), default="all")
    args = parser.parse_args()
    if args.phase == "all":
        dashboard = run_all()
        print(f"Done — risk level: {dashboard['final_risk_level']}")
        print(f"URLs crawled: {dashboard['total_urls_crawled']}")
        print(f"Forbidden brand violations: {dashboard['forbidden_bzpm_count']}")
        return 0
    ensure_layout()
    if args.phase == "1":
        phase1_url_inventory()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
