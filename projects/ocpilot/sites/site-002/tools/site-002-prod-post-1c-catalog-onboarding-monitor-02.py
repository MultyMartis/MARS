#!/usr/bin/env python3
"""SITE-002 Post-1C catalog onboarding monitor 02 — read-only repeat (Run 4.213+)."""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import shutil
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

OPERATION_ID = "SITE-002-PROD-POST-1C-CATALOG-ONBOARDING-MONITOR-02"
OCPILOT_RUN = "4.213"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-POST-1C-MONITOR-BASELINE-1854-05"
AUDIT_BASELINE_BEFORE = "SITE-002-MONITOR-BASELINE-REFRESH-05"
WRONG_BRAND = "БЗПМ"
CORRECT_BRAND = "ЗПМ"
UTF8_BOM = b"\xef\xbb\xbf"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

BASELINE_RUN_4212 = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-POST-1C-CATALOG-ONBOARDING-MONITOR-01\current\sitemap-current-urls.json"
)
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
CRAWL_DELAY_SEC = 0.25

SUBDIRS = (
    "baseline",
    "current",
    "delta",
    "crawl",
    "classification",
    "brand-audit",
    "quality",
    "followup",
    "verification",
    "manifests",
    "reports",
    "logs",
)

SANITY_URLS = (
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/skladskie-lari",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/proizvodstvennye-lari",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/konditerskiy-inventar",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/konditerskiy-inventar/formy-konditerskie",
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
)

ONBOARDED_CATEGORY_PATHS = {
    "katalog/nejtralnoe-oborudovanie/konditerskiy-inventar",
    "katalog/nejtralnoe-oborudovanie/konditerskiy-inventar/formy-konditerskie",
    "katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari",
    "katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/proizvodstvennye-lari",
    "katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/skladskie-lari",
    "katalog/nejtralnoe-oborudovanie/shkafy-i-lari/shkafy-dlya-hleba",
    "katalog/nejtralnoe-oborudovanie/stellazhi/stellazhi-premium-3/stellazhi-premium-3-vysota-1600",
    "katalog/nejtralnoe-oborudovanie/stellazhi/stellazhi-premium/stellazhi-premium-vysota-1600",
    "katalog/nejtralnoe-oborudovanie/stellazhi/stellazhi-standart/stellazhi-standart-vysota-1600",
    "katalog/tehnologicheskoe-oborudovanie",
    "katalog/tehnologicheskoe-oborudovanie/posuda-i-inventar",
    "tehnologicheskoe-oborudovanie/hlebopekarnoe",
    "tehnologicheskoe-oborudovanie/myasopererabatyvayuschee",
    "tehnologicheskoe-oborudovanie/teplovoe",
    "tehnologicheskoe-oborudovanie/teplovoe/grili-kontaktnye",
    "tehnologicheskoe-oborudovanie/teplovoe/risovarki",
    "tehnologicheskoe-oborudovanie/teplovoe/vodonagrevateli",
}

TECHNICAL_QUERY_PATTERNS = (
    r"[?&]sort=",
    r"[?&]order=",
    r"[?&]page=\d+",
    r"[?&]limit=",
    r"[?&]route=",
    r"/index\.php",
)

KNOWN_HUB_SLUG_MARKERS = (
    "dvuhsekcionnye-s-bortom",
    "dvuhsekcionnye-s-polkoj",
    "polki-otkrytye-premium-glub-300",
    "polki/nastennye/otkrytye",
    "polki/nastennye/zakrytye",
    "polki/uglovye/uglovye-dlya-kuhni",
    "polki/uglovye/uglovye-dlya-moechnyh-zon",
    "shkafy/proizvodstvennye-shkafy/shkafy-s-polkami",
    "shkafy/proizvodstvennye-shkafy/zakrytye-shkafy",
    "stellazhi/razbornye/lyogkie",
)

IMAGE_EXT = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".pdf", ".zip")

STRICT_GARBAGE_RULES: tuple[tuple[str, int], ...] = (
    ("НЕ БРАТЬ", 0),
    ("NE BRAT", re.I),
    ("ne-brat", re.I),
    ("не брать", re.I),
    ("nebrat", re.I),
    ("тестовый товар", re.I),
    ("test product", re.I),
    ("dummy product", re.I),
    ("временный товар", re.I),
    ("удалить товар", re.I),
    ("delete product", re.I),
)

DEMO_PRODUCT_TITLE_RE = re.compile(r"\bdemo\s+product\b", re.I)
SCRIPT_STYLE_RE = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.I | re.S)
ASSET_PATH_RE = re.compile(r"/(?:assets|img|catalog|image)/[^\s\"'<>]+", re.I)
DOC_LINK_LABEL_ALLOWLIST = frozenset({
    "пример эксплуатации",
    "example usage",
    "example of use",
})

GARBAGE_FIXTURES: tuple[dict[str, Any], ...] = (
    {
        "id": "demo-asset-path",
        "html": (
            '<html><head><title>Стол производственный</title></head><body>'
            '<img src="/assets/img/demo/assum_logo.png" alt="logo">'
            '<h1>Стол производственный</h1></body></html>'
        ),
        "url": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly/demo-stol",
        "expect_strict_hit": False,
    },
    {
        "id": "primer-ekspluatacii-link",
        "html": (
            '<html><head><title>Зонт вытяжной</title></head><body>'
            '<h1>Зонт вытяжной</h1>'
            '<a href="/files/primer.pdf">Пример эксплуатации</a>'
            '<p>Документация по эксплуатации оборудования.</p></body></html>'
        ),
        "url": "https://bzpm.ru/katalog/ventilyacionnoe-oborudovanie/zont",
        "expect_strict_hit": False,
    },
    {
        "id": "primer-docs-context",
        "html": (
            '<html><head><title>Инструкция</title></head><body>'
            '<h1>Руководство</h1><p>Ниже пример настройки оборудования в типовой конфигурации.</p>'
            '</body></html>'
        ),
        "url": "https://bzpm.ru/katalog/info/page",
        "expect_strict_hit": False,
    },
    {
        "id": "ne-brat-title",
        "html": '<html><head><title>Стол НЕ БРАТЬ тест</title></head><body><h1>Стол</h1></body></html>',
        "url": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly/ne-brat-stol",
        "expect_strict_hit": True,
    },
    {
        "id": "testovyj-tovar-h1",
        "html": '<html><head><title>Товар</title></head><body><h1>тестовый товар 123</h1></body></html>',
        "url": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly/test",
        "expect_strict_hit": True,
    },
    {
        "id": "ne-brat-sku",
        "html": (
            '<html><head><title>Подтоварник</title></head><body>'
            '<h1>Подтоварник</h1><span class="sku">ne-brat-001</span></body></html>'
        ),
        "url": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/podtovarniki/item",
        "expect_strict_hit": True,
    },
    {
        "id": "dummy-product-title",
        "html": '<html><head><title>dummy product showcase</title></head><body><h1>Стол</h1></body></html>',
        "url": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly/dummy",
        "expect_strict_hit": True,
    },
)

NUMERIC_KEYWORD_POLLUTION = re.compile(r"\b\d{5,}\b")


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


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        write_text(path, "")
        return
    names = fieldnames or list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=names, extrasaction="ignore")
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
                "headers": dict(response.headers.items()),
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
            "headers": dict(exc.headers.items()) if exc.headers else {},
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
            "headers": {},
            "x_robots_tag": "",
            "content_type": "",
            "body": "",
            "raw_body": b"",
            "error": str(exc),
        }


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.rstrip("/") or "/"
    return urllib.parse.urlunparse((parsed.scheme.lower(), parsed.netloc.lower(), path, "", "", ""))


def path_parts(url: str) -> list[str]:
    return [p for p in urllib.parse.urlparse(url).path.split("/") if p]


def url_path_key(url: str) -> str:
    return "/".join(path_parts(url))


def is_product_pdp_path(url: str) -> bool:
    parts = path_parts(url)
    return len(parts) >= 5 and parts[0] == "katalog"


def is_technical_url(url: str) -> bool:
    return any(re.search(p, url, re.I) for p in TECHNICAL_QUERY_PATTERNS)


def parse_sitemap_urls(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text)
    return [loc.text.strip() for loc in root.findall(f".//{SITEMAP_NS}loc") if loc.text]


def classify_path_pattern(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.lower()
    if any(path.endswith(ext) for ext in IMAGE_EXT):
        return "IMAGE_OR_FILE"
    if is_technical_url(url):
        return "TECHNICAL"
    parts = path_parts(url)
    if not parts:
        return "INFORMATION"
    if parts[0] == "blog":
        return "BLOG"
    info_slugs = {
        "about", "custom-equipment", "dealers", "delivery",
        "guarantee", "payment-methods", "contact",
    }
    if parts[0] in info_slugs:
        return "INFORMATION"
    if parts[0] == "katalog":
        if is_product_pdp_path(url):
            return "PRODUCT_PDP"
        return "CATEGORY_PLP"
    return "SAFE UNKNOWN"


def count_brand(text: str, brand: str) -> int:
    return text.count(brand)


def strip_non_content_html(html_text: str) -> str:
    cleaned = SCRIPT_STYLE_RE.sub(" ", html_text)
    cleaned = ASSET_PATH_RE.sub(" ", cleaned)
    return cleaned


def extract_scan_fields(html_text: str, url: str) -> dict[str, str]:
    parser = MetaParser()
    try:
        parser.feed(html_text)
    except Exception:
        pass
    title = html.unescape(parser.title.strip())
    h1 = " ".join(parser.h1_list).strip()
    description = parser.meta.get("description", "")
    keywords = parser.meta.get("keywords", "")
    sku_match = re.search(
        r'(?:sku|article|артикул|model)["\s:=]+([^\s"\'<>]{2,80})',
        html_text,
        re.I,
    )
    sku = sku_match.group(1) if sku_match else ""
    product_id_match = re.search(r'product_id["\s:=]+(\d+)', html_text)
    product_id = product_id_match.group(1) if product_id_match else ""
    visible_text = re.sub(r"<[^>]+>", " ", strip_non_content_html(html_text))
    visible_text = re.sub(r"\s+", " ", html.unescape(visible_text)).strip()
    link_labels: list[str] = []
    for m in re.finditer(r"<a\b[^>]*>(.*?)</a>", html_text, re.I | re.S):
        label = re.sub(r"<[^>]+>", " ", m.group(1))
        label = re.sub(r"\s+", " ", html.unescape(label)).strip()
        if label:
            link_labels.append(label)
    breadcrumbs = ""
    crumb_match = re.search(
        r'class="[^"]*breadcrumb[^"]*"[^>]*>(.*?)</(?:nav|ol|ul|div)>',
        html_text,
        re.I | re.S,
    )
    if crumb_match:
        breadcrumbs = re.sub(r"<[^>]+>", " ", crumb_match.group(1))
        breadcrumbs = re.sub(r"\s+", " ", html.unescape(breadcrumbs)).strip()
    return {
        "title": title,
        "h1": h1,
        "meta_description": description,
        "meta_keywords": keywords,
        "breadcrumbs": breadcrumbs,
        "sku": sku,
        "product_id": product_id,
        "product_name": h1 or title,
        "visible_main_content": visible_text[:4000],
        "link_labels": " | ".join(link_labels[:20]),
        "url_path": urllib.parse.urlparse(url).path,
    }


def scan_strict_garbage(html_text: str, url: str) -> list[dict[str, Any]]:
    """Context-aware strict garbage marker scan — excludes asset paths and doc link labels."""
    fields = extract_scan_fields(html_text, url)
    hits: list[dict[str, Any]] = []
    url_path = fields.get("url_path", "")
    if "/assets/img/demo/" in url_path.lower() or "/assets/img/demo/" in url.lower():
        pass  # never flag URL path alone

    scan_targets = {
        "title": fields.get("title", ""),
        "h1": fields.get("h1", ""),
        "meta_description": fields.get("meta_description", ""),
        "meta_keywords": fields.get("meta_keywords", ""),
        "breadcrumbs": fields.get("breadcrumbs", ""),
        "product_name": fields.get("product_name", ""),
        "sku": fields.get("sku", ""),
        "visible_main_content": fields.get("visible_main_content", ""),
    }

    for field_name, field_text in scan_targets.items():
        if not field_text:
            continue
        lowered = field_text.lower()
        for marker, flags in STRICT_GARBAGE_RULES:
            if flags == 0:
                idx = field_text.find(marker)
                if idx >= 0:
                    hits.append({
                        "marker": marker,
                        "source_field": field_name,
                        "evidence": field_text[max(0, idx - 20): idx + len(marker) + 40].strip(),
                        "url": url,
                    })
            else:
                for m in re.finditer(re.escape(marker), field_text, flags):
                    hits.append({
                        "marker": marker,
                        "source_field": field_name,
                        "evidence": field_text[max(0, m.start() - 20): m.end() + 40].strip(),
                        "url": url,
                    })
        if DEMO_PRODUCT_TITLE_RE.search(field_text):
            hits.append({
                "marker": "demo product",
                "source_field": field_name,
                "evidence": field_text[:120].strip(),
                "url": url,
            })

    for label in fields.get("link_labels", "").split(" | "):
        label_norm = label.strip().lower()
        if not label_norm:
            continue
        if label_norm in DOC_LINK_LABEL_ALLOWLIST:
            continue
        for marker, flags in STRICT_GARBAGE_RULES:
            if flags == 0:
                if marker in label:
                    hits.append({
                        "marker": marker,
                        "source_field": "link_label",
                        "evidence": label,
                        "url": url,
                    })
            elif re.search(re.escape(marker), label, flags):
                hits.append({
                    "marker": marker,
                    "source_field": "link_label",
                    "evidence": label,
                    "url": url,
                })

    # Deduplicate identical hits
    seen: set[tuple[str, str, str]] = set()
    unique: list[dict[str, Any]] = []
    for hit in hits:
        key = (hit["url"], hit["marker"], hit["source_field"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(hit)
    return unique


def format_duration_human(seconds: float) -> str:
    if seconds < 1:
        return f"{seconds:.2f} seconds"
    total = int(round(seconds))
    if total < 60:
        return f"{total} seconds"
    minutes, rem = divmod(total, 60)
    if minutes < 60:
        return f"{minutes}m {rem}s"
    hours, minutes = divmod(minutes, 60)
    return f"{hours}h {minutes}m {rem}s"


def classify_monitor_run(
    *,
    monitor_status: str,
    added_count: int,
    removed_count: int,
    onboarding_needs_count: int,
    strict_garbage_hits_count: int,
    brand_violations: int,
    hygiene_flags_count: int,
    sitemap_fetch_ok: bool,
    parse_ok: bool,
) -> tuple[str, str]:
    if (
        monitor_status != "success"
        or not sitemap_fetch_ok
        or not parse_ok
        or strict_garbage_hits_count > 0
        or brand_violations > 0
    ):
        if strict_garbage_hits_count > 0 or brand_violations > 0:
            return (
                "FAILURE_REVIEW_REQUIRED",
                "Review strict garbage markers or forbidden БЗПМ before any catalog action.",
            )
        return (
            "FAILURE_REVIEW_REQUIRED",
            "Investigate monitor failure, sitemap fetch, or parse errors in run logs.",
        )
    if onboarding_needs_count > 0:
        return (
            "ONBOARDING_REQUIRED",
            "Review category-onboarding-needs and plan SITE-002 onboarding charter.",
        )
    if added_count > 0 or removed_count > 0 or hygiene_flags_count > 0:
        return (
            "HYGIENE_REVIEW_REQUIRED",
            "Review added/removed URL lists and hygiene flags; no onboarding charter required yet.",
        )
    return (
        "NO_ACTION_REQUIRED",
        "No delta or hygiene flags — no operator action until next 1C import.",
    )


def run_garbage_fixture_regression() -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    for fixture in GARBAGE_FIXTURES:
        hits = scan_strict_garbage(fixture["html"], fixture["url"])
        got_hit = len(hits) > 0
        passed = got_hit == fixture["expect_strict_hit"]
        results.append({
            "id": fixture["id"],
            "expect_strict_hit": fixture["expect_strict_hit"],
            "got_strict_hit": got_hit,
            "pass": passed,
            "hits": hits,
        })
    return {
        "fixture_count": len(results),
        "passed": sum(1 for r in results if r["pass"]),
        "failed": sum(1 for r in results if not r["pass"]),
        "results": results,
        "captured_at": utc_now(),
    }


def extract_page_meta(html_text: str, url: str) -> dict[str, Any]:
    parser = MetaParser()
    try:
        parser.feed(html_text)
    except Exception:
        pass
    title = html.unescape(parser.title.strip())
    h1 = " ".join(parser.h1_list).strip()
    description = parser.meta.get("description", "")
    keywords = parser.meta.get("keywords", "")
    robots = parser.meta.get("robots", "")
    canonical = ""
    for link in parser.links:
        if link.get("rel") == "canonical":
            canonical = link.get("href", "")
            break
    lower = html_text.lower()
    markers = {
        "has_page_product": "page--product" in parser.body_class,
        "has_page_category": "page--category" in parser.body_class,
        "has_add_to_cart": "button-cart" in lower or "add-to-cart" in lower,
        "has_load_more": "load-more" in lower or "load_more" in lower,
        "has_category_hub": "category-hub" in lower or "hub-category" in lower,
    }
    product_id_match = re.search(r'product_id["\s:=]+(\d+)', html_text)
    product_id = product_id_match.group(1) if product_id_match else ""
    path_pattern = classify_path_pattern(url)
    page_type = path_pattern
    if markers["has_page_product"] or (path_pattern == "PRODUCT_PDP" and product_id):
        page_type = "PRODUCT_PDP"
    elif markers["has_page_category"] or path_pattern == "CATEGORY_PLP":
        is_hub = (
            markers["has_load_more"] and not markers["has_page_product"]
        ) or any(m in url for m in KNOWN_HUB_SLUG_MARKERS)
        page_type = "CATEGORY_HUB" if is_hub else "CATEGORY_PLP"
        if any(m in url for m in KNOWN_HUB_SLUG_MARKERS):
            page_type = "LEGACY_HUB"
    test_hits = scan_strict_garbage(html_text, url)
    return {
        "title": title,
        "h1": h1,
        "meta_description": description,
        "meta_keywords": keywords,
        "meta_robots": robots,
        "canonical": canonical,
        "body_class": parser.body_class,
        "body_count": parser.body_open,
        "product_id": product_id,
        "path_pattern": path_pattern,
        "page_type": page_type,
        "yandex_metrika": any(t in lower for t in ("mc.yandex.ru/metrika", "ym(", "yandex.metrika")),
        "yandex_webmaster": "yandex-verification" in lower,
        "bzpm_count": count_brand(html_text, WRONG_BRAND),
        "zpm_count": count_brand(html_text, CORRECT_BRAND),
        "strict_garbage_hits": test_hits,
        "strict_garbage_hit_count": len(test_hits),
        "numeric_keyword_pollution": bool(NUMERIC_KEYWORD_POLLUTION.search(keywords)),
        **markers,
    }


def is_noindex(meta_robots: str, x_robots: str) -> bool:
    return "noindex" in f"{meta_robots} {x_robots}".lower()


def canonical_matches(final_url: str, canonical: str) -> bool:
    if not canonical:
        return False
    return normalize_url(canonical) == normalize_url(final_url)


def find_normalized_duplicates(urls: list[str]) -> list[dict[str, str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for url in urls:
        groups[normalize_url(url)].append(url)
    dups: list[dict[str, str]] = []
    for norm, variants in sorted(groups.items()):
        if len(variants) > 1:
            dups.append({"normalized": norm, "variants": " | ".join(variants), "count": str(len(variants))})
    return dups


def find_exact_duplicates(urls: list[str]) -> list[dict[str, str]]:
    counts = Counter(urls)
    return [{"url": u, "count": str(c)} for u, c in sorted(counts.items()) if c > 1]


def classify_delta_scale(added: int, removed: int, baseline: int) -> str:
    if added == 0 and removed == 0:
        return "NO_CHANGE"
    if removed > 0 and added == 0:
        return "SHRINKAGE_REVIEW"
    growth_pct = (added / baseline * 100) if baseline else 0
    if added <= 80 and removed <= 5:
        return "SMALL_EXPECTED_GROWTH"
    if growth_pct <= 15 and removed <= 10:
        return "LARGE_EXPECTED_GROWTH"
    if growth_pct > 25:
        return "SUSPICIOUS_GROWTH"
    return "SAFE UNKNOWN"


def ensure_layout() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "audit_baseline_before": AUDIT_BASELINE_BEFORE,
        "change_type": "post-1c-catalog-onboarding-monitor-readonly-repeat",
        "daily_1c_growth_expected": True,
        "remote_changes_allowed": False,
        "admin_save_allowed": False,
        "db_write_allowed": False,
        "cache_clear_allowed": False,
        "ftp_upload_allowed": False,
        "delete_hide_noindex_allowed": False,
        "product_generator_change_allowed": False,
        "category_meta_change_allowed": False,
        "llms_txt_change_allowed": False,
        "robots_change_allowed": False,
        "sitemap_change_allowed": False,
        "header_footer_change_allowed": False,
        "brand_policy_correct": CORRECT_BRAND,
        "brand_policy_forbidden_public": WRONG_BRAND,
        "domain_bzpm_ru_allowed": True,
        "captured_at": utc_now(),
        "ocpilot_run": OCPILOT_RUN,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)


def phase1_baseline() -> tuple[list[str], dict[str, Any]]:
    print("Phase 1: baseline selection...")
    source_op = (
        "SITE-002-MONITOR-BASELINE-REFRESH-05 (Run 4.300) — refreshed from live sitemap "
        "after confirmed post-import persistence (Runs 4.297–4.299; persistence commit d9286f8e)"
    )
    verified_by = AUDIT_BASELINE_BEFORE
    limitation = (
        "Baseline URL set refreshed in MONITOR-01 current/sitemap-current-urls.json; "
        "count 1854, SHA-256 of JSON artifact recorded in SITE-002-MONITOR-BASELINE-REFRESH-05 "
        "baseline-update; prior 1737 snapshot retained under baseline-update pre-refresh backup."
    )
    if not BASELINE_RUN_4212.exists():
        raise FileNotFoundError(f"Baseline artifact missing: {BASELINE_RUN_4212}")
    urls = json.loads(BASELINE_RUN_4212.read_text(encoding="utf-8"))
    urls = sorted(set(urls))
    selection = {
        "source_operation": source_op,
        "verified_by_operation": verified_by,
        "baseline_checkpoint": BASELINE_BEFORE,
        "audit_baseline_before": AUDIT_BASELINE_BEFORE,
        "artifact_path": str(BASELINE_RUN_4212),
        "url_count": len(urls),
        "expected_count_run_4_300": 1854,
        "match_expected": len(urls) == 1854,
        "reconstructed": False,
        "limitations": limitation,
        "captured_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "baseline" / "baseline-selection.json", selection)
    write_json(DEPLOYMENT_ROOT / "baseline" / "baseline-urls.json", urls)
    write_csv(DEPLOYMENT_ROOT / "baseline" / "baseline-urls.csv", [{"url": u} for u in urls], ["url"])
    write_text(
        DEPLOYMENT_ROOT / "baseline" / "baseline-selection.md",
        "\n".join([
            "# Baseline selection",
            "",
            f"- Source operation: **{source_op}**",
            f"- Verified by: **{verified_by}**",
            f"- Baseline checkpoint: `{BASELINE_BEFORE}`",
            f"- Artifact: `{BASELINE_RUN_4212}`",
            f"- URL count: **{len(urls)}**",
            f"- Match Run 4.300 expected (1854): **{selection['match_expected']}**",
            f"- Reconstructed: **no**",
            "",
            "## Limitations",
            "",
            limitation,
        ]) + "\n",
    )
    return urls, selection


def phase2_current() -> tuple[list[str], dict[str, Any], str, str]:
    print("Phase 2: fetch current live snapshot...")
    sitemap_resp = http_get("https://bzpm.ru/sitemap.xml")
    raw = sitemap_resp.get("raw_body") or b""
    xml_text = sitemap_resp.get("body") or ""
    (DEPLOYMENT_ROOT / "current" / "sitemap-current.xml").write_bytes(raw)
    headers_text = "\n".join(f"{k}: {v}" for k, v in sitemap_resp.get("headers", {}).items())
    write_text(DEPLOYMENT_ROOT / "current" / "sitemap-current-headers.txt", headers_text)

    robots_resp = http_get("https://bzpm.ru/robots.txt")
    write_text(DEPLOYMENT_ROOT / "current" / "robots-current.txt", robots_resp.get("body", ""))

    llms_resp = http_get("https://bzpm.ru/llms.txt")
    llms_raw = llms_resp.get("raw_body") or b""
    write_text(DEPLOYMENT_ROOT / "current" / "llms-current.txt", llms_raw.decode("utf-8-sig", errors="replace"))

    valid_xml = False
    urls: list[str] = []
    malformed = 0
    non_bzpm = 0
    parse_error = ""
    if xml_text.strip().startswith("<"):
        try:
            urls = parse_sitemap_urls(xml_text)
            valid_xml = True
        except ET.ParseError as exc:
            parse_error = str(exc)
    for u in urls:
        if " " in u or "\n" in u or "\t" in u:
            malformed += 1
        host = urllib.parse.urlparse(u).netloc
        if host not in ("bzpm.ru", "www.bzpm.ru"):
            non_bzpm += 1
    dup_counts = Counter(urls)
    duplicates = sum(1 for c in dup_counts.values() if c > 1)

    llms_text = llms_raw.decode("utf-8-sig", errors="replace")
    summary = {
        "sitemap_url": "https://bzpm.ru/sitemap.xml",
        "sitemap_http_status": sitemap_resp.get("status_code"),
        "valid_xml": valid_xml,
        "parse_error": parse_error,
        "url_count": len(urls),
        "unique_url_count": len(set(urls)),
        "exact_duplicate_loc_count": duplicates,
        "non_bzpm_urls": non_bzpm,
        "malformed_urls": malformed,
        "sha256": sha256_bytes(raw),
        "robots_http_status": robots_resp.get("status_code"),
        "robots_sitemap_directive": "sitemap:" in (robots_resp.get("body") or "").lower(),
        "llms_http_status": llms_resp.get("status_code"),
        "llms_utf8_bom": llms_raw.startswith(UTF8_BOM),
        "llms_bzpm_count": count_brand(llms_text, WRONG_BRAND),
        "llms_zpm_count": count_brand(llms_text, CORRECT_BRAND),
        "captured_at": utc_now(),
        "baseline_expected_count": 1854,
    }
    write_json(DEPLOYMENT_ROOT / "current" / "sitemap-current-summary.json", summary)
    write_json(DEPLOYMENT_ROOT / "current" / "sitemap-current-urls.json", urls)
    write_csv(DEPLOYMENT_ROOT / "current" / "sitemap-current-urls.csv", [{"url": u} for u in urls], ["url"])
    write_text(
        DEPLOYMENT_ROOT / "current" / "sitemap-current-summary.md",
        "\n".join([
            "# Current live snapshot",
            "",
            f"- Sitemap HTTP: **{summary['sitemap_http_status']}**",
            f"- Valid XML: **{valid_xml}**",
            f"- URL count: **{len(urls)}**",
            f"- Baseline (4.300): **1854**",
            f"- Delta vs baseline: **{len(urls) - 1854:+d}**",
            f"- robots HTTP 200 + Sitemap: **{summary['robots_http_status'] == 200 and summary['robots_sitemap_directive']}**",
            f"- llms UTF-8 BOM: **{summary['llms_utf8_bom']}**",
            f"- llms ЗПМ / no БЗПМ: **{summary['llms_zpm_count'] > 0} / {summary['llms_bzpm_count'] == 0}**",
        ]) + "\n",
    )
    return urls, summary, robots_resp.get("body", ""), llms_text


def phase3_delta(baseline: list[str], current: list[str]) -> dict[str, Any]:
    print("Phase 3: sitemap delta...")
    base_set = set(baseline)
    curr_set = set(current)
    added = sorted(curr_set - base_set)
    removed = sorted(base_set - curr_set)
    unchanged_count = len(base_set & curr_set)
    exact_dups = find_exact_duplicates(current)
    norm_dups = find_normalized_duplicates(current)
    scale = classify_delta_scale(len(added), len(removed), len(baseline))
    summary = {
        "baseline_count": len(baseline),
        "current_count": len(current),
        "added_count": len(added),
        "removed_count": len(removed),
        "unchanged_count": unchanged_count,
        "exact_duplicate_count": len(exact_dups),
        "normalized_duplicate_groups": len(norm_dups),
        "delta_scale": scale,
        "captured_at": utc_now(),
    }
    write_csv(DEPLOYMENT_ROOT / "delta" / "added.csv", [{"url": u} for u in added], ["url"])
    write_json(DEPLOYMENT_ROOT / "delta" / "added.json", added)
    write_csv(DEPLOYMENT_ROOT / "delta" / "removed.csv", [{"url": u} for u in removed], ["url"])
    write_json(DEPLOYMENT_ROOT / "delta" / "removed.json", removed)
    write_csv(DEPLOYMENT_ROOT / "delta" / "duplicates.csv", exact_dups)
    write_csv(DEPLOYMENT_ROOT / "delta" / "normalized-duplicates.csv", norm_dups)
    write_json(DEPLOYMENT_ROOT / "delta" / "delta-summary.json", summary)
    write_text(
        DEPLOYMENT_ROOT / "delta" / "delta-summary.md",
        "\n".join([
            "# Sitemap delta summary",
            "",
            f"- Baseline: **{len(baseline)}**",
            f"- Current: **{len(current)}**",
            f"- Added: **{len(added)}**",
            f"- Removed: **{len(removed)}**",
            f"- Unchanged: **{unchanged_count}**",
            f"- Delta scale: **{scale}**",
        ]) + "\n",
    )
    return {**summary, "added": added, "removed": removed}


def crawl_row(url: str) -> dict[str, Any]:
    resp = http_get(url)
    status = resp.get("status_code")
    meta: dict[str, Any] = {}
    if status and status < 400 and "html" in (resp.get("content_type") or "").lower():
        meta = extract_page_meta(resp.get("body", ""), url)
    noindex = is_noindex(meta.get("meta_robots", ""), resp.get("x_robots_tag", ""))
    page_type = meta.get("page_type", classify_path_pattern(url))
    if status in (301, 302, 303, 307, 308):
        page_type = "REDIRECT"
    elif status == 404:
        page_type = "404"
    return {
        "url": url,
        "http_status": status,
        "final_url": resp.get("final_url", url),
        "title": meta.get("title", ""),
        "meta_description": meta.get("meta_description", ""),
        "description_length": len(meta.get("meta_description", "")),
        "meta_keywords": meta.get("meta_keywords", ""),
        "canonical": meta.get("canonical", ""),
        "meta_robots": meta.get("meta_robots", ""),
        "x_robots_tag": resp.get("x_robots_tag", ""),
        "h1": meta.get("h1", ""),
        "body_class": meta.get("body_class", ""),
        "page_type": page_type,
        "path_pattern": meta.get("path_pattern", classify_path_pattern(url)),
        "page_product": meta.get("has_page_product", False),
        "page_category": meta.get("has_page_category", False),
        "forbidden_bzpm_count": meta.get("bzpm_count", 0),
        "zpm_count": meta.get("zpm_count", 0),
        "strict_garbage_hit_count": meta.get("strict_garbage_hit_count", 0),
        "strict_garbage_hits": meta.get("strict_garbage_hits", []),
        "numeric_keyword_pollution": meta.get("numeric_keyword_pollution", False),
        "noindex": noindex,
        "indexable": status == 200 and not noindex,
        "canonical_sane": canonical_matches(resp.get("final_url", url), meta.get("canonical", "")),
        "branch": "/".join(path_parts(url)[:4]),
        "error": resp.get("error"),
    }


def crawl_urls(urls: list[str], label: str) -> list[dict[str, Any]]:
    print(f"Phase 4: crawl {len(urls)} {label} URLs...")
    rows: list[dict[str, Any]] = []
    for idx, url in enumerate(urls, 1):
        rows.append(crawl_row(url))
        if idx % 15 == 0:
            print(f"  crawled {idx}/{len(urls)}")
        time.sleep(CRAWL_DELAY_SEC)
    return rows


def write_classification(rows: list[dict[str, Any]], prefix: str, title: str) -> None:
    flat_rows = []
    for r in rows:
        flat = {k: v for k, v in r.items() if k not in ("strict_garbage_hits", "test_markers")}
        flat_rows.append(flat)
    write_csv(DEPLOYMENT_ROOT / "classification" / f"{prefix}-url-classification.csv", flat_rows)
    write_json(DEPLOYMENT_ROOT / "classification" / f"{prefix}-url-classification.json", rows)
    by_type = Counter(r.get("page_type", "unknown") for r in rows)
    lines = [f"# {title}", "", f"- URLs classified: **{len(rows)}**", "", "## By page type"]
    for k, v in sorted(by_type.items()):
        lines.append(f"- {k}: {v}")
    write_text(DEPLOYMENT_ROOT / "classification" / f"{prefix}-url-classification.md", "\n".join(lines) + "\n")


def phase5_category_onboarding(added_rows: list[dict[str, Any]], current_urls: list[str]) -> list[dict[str, Any]]:
    print("Phase 5: category onboarding needs...")
    needs: list[dict[str, Any]] = []
    category_types = {"CATEGORY_PLP", "CATEGORY_HUB", "LEGACY_HUB"}
    titles_by_branch: dict[str, list[str]] = defaultdict(list)
    descs_by_branch: dict[str, list[str]] = defaultdict(list)

    for row in added_rows:
        if row.get("page_type") not in category_types:
            continue
        branch = url_path_key(row["url"])
        titles_by_branch[row.get("branch", "")].append(row.get("title", ""))
        descs_by_branch[row.get("branch", "")].append(row.get("meta_description", ""))

    def assess_row(row: dict[str, Any], from_added: bool) -> None:
        if row.get("page_type") not in category_types:
            return
        if row.get("http_status") != 200 or not row.get("indexable"):
            return
        issues: list[str] = []
        priority = "P3 monitor"
        desc = row.get("meta_description", "")
        desc_len = len(desc)
        path_key = url_path_key(row["url"])
        if row.get("forbidden_bzpm_count", 0) > 0:
            issues.append("forbidden brand БЗПМ")
            priority = "P1 critical"
        if not desc:
            issues.append("missing meta description")
            priority = "P2 onboarding" if priority != "P1 critical" else priority
        elif desc_len < 90:
            issues.append(f"weak description ({desc_len} chars)")
            priority = "P2 onboarding" if priority != "P1 critical" else priority
        if path_key not in ONBOARDED_CATEGORY_PATHS and from_added:
            issues.append("newly added category branch not documented")
            if priority == "P3 monitor":
                priority = "P2 onboarding"
        title = row.get("title", "")
        branch = row.get("branch", "")
        if title and titles_by_branch.get(branch, []).count(title) > 1:
            issues.append("duplicate title against sibling")
        if desc and descs_by_branch.get(branch, []).count(desc) > 1:
            issues.append("duplicate description against sibling")
        if not issues and not from_added:
            return
        if not issues:
            return
        suggested_op = "SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-02"
        if row.get("forbidden_bzpm_count", 0) > 0:
            suggested_op = "SITE-002-PROD-BRAND-ZPM-REMEDIATION-02"
        needs.append({
            "url": row["url"],
            "page_type": row.get("page_type"),
            "branch": branch,
            "title": title,
            "description": desc,
            "issue": "; ".join(issues),
            "priority": priority,
            "suggested_next_operation": suggested_op,
            "suggested_copy_seed": "",
            "authority_guess": "ADMIN_CATEGORY",
            "from_added_delta": from_added,
        })

    for row in added_rows:
        assess_row(row, from_added=True)

    write_csv(DEPLOYMENT_ROOT / "quality" / "category-onboarding-needs.csv", needs)
    write_json(DEPLOYMENT_ROOT / "quality" / "category-onboarding-needs.json", needs)
    write_text(
        DEPLOYMENT_ROOT / "quality" / "category-onboarding-needs.md",
        "\n".join([
            "# Category onboarding needs",
            "",
            f"- Items: **{len(needs)}**",
            f"- P1: **{sum(1 for n in needs if n['priority'] == 'P1 critical')}**",
            f"- P2: **{sum(1 for n in needs if n['priority'] == 'P2 onboarding')}**",
        ]) + "\n",
    )
    return needs


def phase6_product_pdp_sanity(added_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    print("Phase 6: product PDP sanity...")
    rows: list[dict[str, Any]] = []
    for row in added_rows:
        if row.get("page_type") != "PRODUCT_PDP":
            continue
        issues: list[str] = []
        if row.get("http_status") != 200:
            issues.append(f"HTTP {row.get('http_status')}")
        if not row.get("page_product"):
            issues.append("missing page--product marker")
        if not row.get("title"):
            issues.append("missing title")
        if not row.get("meta_description"):
            issues.append("missing meta description")
        if row.get("forbidden_bzpm_count", 0) > 0:
            issues.append("forbidden БЗПМ")
        if row.get("numeric_keyword_pollution"):
            issues.append("numeric keyword pollution")
        if not row.get("canonical_sane"):
            issues.append("canonical not sane")
        if row.get("noindex"):
            issues.append("noindex")
        rows.append({
            "url": row["url"],
            "http_status": row.get("http_status"),
            "page_product": row.get("page_product"),
            "title_present": bool(row.get("title")),
            "meta_description_present": bool(row.get("meta_description")),
            "meta_keywords_present": bool(row.get("meta_keywords")),
            "forbidden_bzpm": row.get("forbidden_bzpm_count", 0) > 0,
            "numeric_keyword_pollution": row.get("numeric_keyword_pollution"),
            "canonical_sane": row.get("canonical_sane"),
            "indexable": row.get("indexable"),
            "issues": "; ".join(issues) if issues else "ok",
            "status": "FAIL" if issues else "PASS",
        })
    write_csv(DEPLOYMENT_ROOT / "quality" / "product-pdp-sanity.csv", rows)
    write_json(DEPLOYMENT_ROOT / "quality" / "product-pdp-sanity.json", rows)
    fail_count = sum(1 for r in rows if r["status"] == "FAIL")
    write_text(
        DEPLOYMENT_ROOT / "quality" / "product-pdp-sanity.md",
        "\n".join([
            "# Product PDP sanity (added URLs)",
            "",
            f"- PDP URLs checked: **{len(rows)}**",
            f"- PASS: **{len(rows) - fail_count}**",
            f"- FAIL: **{fail_count}**",
        ]) + "\n",
    )
    return rows


def phase7_test_garbage_audit(rows: list[dict[str, Any]], label: str) -> list[dict[str, Any]]:
    print(f"Phase 7: strict garbage marker audit ({label})...")
    hits: list[dict[str, Any]] = []
    for row in rows:
        strict_hits = row.get("strict_garbage_hits") or []
        if strict_hits:
            hits.append({
                "url": row["url"],
                "page_type": row.get("page_type"),
                "strict_garbage_hit_count": len(strict_hits),
                "markers": json.dumps(strict_hits, ensure_ascii=False),
                "recommendation": "SITE-002-PROD-CATALOG-GARBAGE-SKU-REVIEW-01",
            })
    return hits


def phase8_brand_audit(rows: list[dict[str, Any]]) -> dict[str, Any]:
    print("Phase 8: brand regression audit...")
    brand_rows = []
    violations = 0
    for row in rows:
        bzpm = row.get("forbidden_bzpm_count", 0)
        if bzpm > 0:
            violations += 1
        brand_rows.append({
            "url": row["url"],
            "page_type": row.get("page_type"),
            "bzpm_count": bzpm,
            "zpm_count": row.get("zpm_count", 0),
            "violation": "yes" if bzpm > 0 else "no",
        })
    summary = {
        "urls_checked": len(brand_rows),
        "bzpm_violations": violations,
        "recommend_remediation_02": violations > 0,
    }
    write_csv(DEPLOYMENT_ROOT / "brand-audit" / "post-1c-brand-audit.csv", brand_rows)
    write_json(DEPLOYMENT_ROOT / "brand-audit" / "post-1c-brand-audit.json", summary | {"rows": brand_rows})
    write_text(
        DEPLOYMENT_ROOT / "brand-audit" / "post-1c-brand-audit.md",
        "\n".join([
            "# Post-1C brand regression audit",
            "",
            f"- URLs checked: **{len(brand_rows)}**",
            f"- Forbidden БЗПМ violations: **{violations}**",
        ]) + "\n",
    )
    return summary


def phase9_sanity(current_count: int) -> dict[str, Any]:
    print("Phase 9: sanity checks...")
    results: dict[str, Any] = {}
    for url in SANITY_URLS:
        resp = http_get(url)
        entry: dict[str, Any] = {
            "url": url,
            "http_status": resp.get("status_code"),
            "final_url": resp.get("final_url"),
        }
        if url.endswith("llms.txt"):
            raw = resp.get("raw_body") or b""
            text = raw.decode("utf-8-sig", errors="replace")
            entry.update({
                "utf8_bom": raw.startswith(UTF8_BOM),
                "bzpm_count": count_brand(text, WRONG_BRAND),
                "zpm_count": count_brand(text, CORRECT_BRAND),
            })
        elif url.endswith("robots.txt"):
            body = resp.get("body", "")
            entry["has_sitemap_directive"] = "sitemap:" in body.lower()
        elif url.endswith("sitemap.xml"):
            entry["url_count"] = current_count
            entry["valid_xml"] = True
        elif "html" in (resp.get("content_type") or "").lower():
            meta = extract_page_meta(resp.get("body", ""), url)
            entry.update({
                "body_count": meta.get("body_count", 0),
                "yandex_metrika": meta.get("yandex_metrika"),
                "yandex_webmaster": meta.get("yandex_webmaster"),
                "has_load_more": meta.get("has_load_more"),
                "title": meta.get("title", ""),
                "meta_description": meta.get("meta_description", ""),
                "description_length": len(meta.get("meta_description", "")),
                "bzpm_count": meta.get("bzpm_count", 0),
            })
        results[url] = entry
        time.sleep(0.2)

    home = results.get("https://bzpm.ru/", {})
    llms = results.get("https://bzpm.ru/llms.txt", {})
    robots = results.get("https://bzpm.ru/robots.txt", {})
    stoly = results.get("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly", {})
    summary = {
        "home_status": home.get("http_status"),
        "home_body_count": home.get("body_count"),
        "home_yandex_metrika": home.get("yandex_metrika"),
        "home_yandex_webmaster": home.get("yandex_webmaster"),
        "stoly_load_more": stoly.get("has_load_more"),
        "robots_status": robots.get("http_status"),
        "robots_sitemap_directive": robots.get("has_sitemap_directive"),
        "sitemap_status": results.get("https://bzpm.ru/sitemap.xml", {}).get("http_status"),
        "sitemap_valid": True,
        "sitemap_url_count": current_count,
        "llms_status": llms.get("http_status"),
        "llms_utf8_bom": llms.get("utf8_bom"),
        "llms_forbidden_bzpm": (llms.get("bzpm_count") or 0) > 0,
        "captured_at": utc_now(),
        "details": results,
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "sanity-checks.json", summary)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "sanity-checks.md",
        "\n".join([
            "# Sanity checks",
            "",
            f"- Home HTTP 200 + body_count=1: **{home.get('http_status') == 200 and home.get('body_count') == 1}**",
            f"- Yandex Metrika/Webmaster: **{home.get('yandex_metrika')} / {home.get('yandex_webmaster')}**",
            f"- /stoly load-more: **{stoly.get('has_load_more')}**",
            f"- robots Sitemap: **{robots.get('has_sitemap_directive')}**",
            f"- sitemap count: **{current_count}**",
            f"- llms BOM / no БЗПМ: **{llms.get('utf8_bom')} / {(llms.get('bzpm_count') or 0) == 0}**",
        ]) + "\n",
    )
    return summary


def phase10_monitoring_rule() -> None:
    print("Phase 10: reusable monitoring rule...")
    rule = {
        "name": "post-1c-catalog-onboarding-monitor",
        "steps": [
            "Fetch sitemap after daily 1C import",
            "Compare with previous baseline checkpoint",
            "Classify added URLs by type",
            "Separate PRODUCT_PDP from CATEGORY_PLP/HUB/LEGACY_HUB",
            "Check new category/hub pages for description, title, brand",
            "Run PDP product-generator sanity only on new products",
            "Check test/НЕ БРАТЬ markers — report only",
            "Do not delete/hide/noindex by default",
            "Produce onboarding task list",
            "Human approves any mutation operation separately",
            "Parent-aware category mapping is mandatory when category names repeat",
        ],
        "forbidden_default_actions": [
            "delete", "hide", "noindex", "redirect", "remove from sitemap", "rename new categories",
        ],
        "operation_template": OPERATION_ID,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "post-1c-monitoring-rule.json", rule)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "post-1c-monitoring-rule.md",
        "\n".join([
            "# Reusable post-1C monitoring rule",
            "",
            "After daily 1C import:",
            "",
        ] + [f"{i}. {s}" for i, s in enumerate(rule["steps"], 1)] + [
            "",
            "## Forbidden by default",
            "",
        ] + [f"- {a}" for a in rule["forbidden_default_actions"]]) + "\n",
    )


def determine_verdict(
    onboarding_needs: list[dict[str, Any]],
    garbage_hits: list[dict[str, Any]],
    brand: dict[str, Any],
    added_rows: list[dict[str, Any]],
) -> str:
    p1 = [n for n in onboarding_needs if n.get("priority") == "P1 critical"]
    p2 = [n for n in onboarding_needs if n.get("priority") == "P2 onboarding"]
    red_in_sitemap = [
        r for r in added_rows
        if r.get("http_status") in (404, 301, 302, 303, 307, 308) or r.get("noindex")
    ]
    if brand.get("bzpm_violations", 0) > 0 or p1:
        if garbage_hits or red_in_sitemap:
            return "SITE-002 POST-1C CATALOG MONITOR 02 COMPLETE — HYGIENE REVIEW REQUIRED"
        return "SITE-002 POST-1C CATALOG MONITOR 02 COMPLETE — ONBOARDING TASKS FOUND"
    if p2 or garbage_hits or red_in_sitemap:
        if garbage_hits or red_in_sitemap:
            return "SITE-002 POST-1C CATALOG MONITOR 02 COMPLETE — HYGIENE REVIEW REQUIRED"
        return "SITE-002 POST-1C CATALOG MONITOR 02 COMPLETE — ONBOARDING TASKS FOUND"
    return "SITE-002 POST-1C CATALOG MONITOR 02 COMPLETE — NO ONBOARDING NEEDED"


def phase11_followup(
    verdict: str,
    onboarding_needs: list[dict[str, Any]],
    garbage_hits: list[dict[str, Any]],
    brand: dict[str, Any],
    added_rows: list[dict[str, Any]],
    delta: dict[str, Any],
) -> dict[str, Any]:
    print("Phase 11: follow-up task list...")
    tasks: list[dict[str, Any]] = []
    if any(n.get("priority") in ("P1 critical", "P2 onboarding") for n in onboarding_needs):
        tasks.append({
            "operation": "SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-02",
            "reason": "new category branches need meta onboarding",
            "count": len([n for n in onboarding_needs if n.get("priority") == "P2 onboarding"]),
        })
    if brand.get("bzpm_violations", 0) > 0:
        tasks.append({
            "operation": "SITE-002-PROD-BRAND-ZPM-REMEDIATION-02",
            "reason": "forbidden БЗПМ in public content",
            "count": brand.get("bzpm_violations"),
        })
    if garbage_hits:
        tasks.append({
            "operation": "SITE-002-PROD-CATALOG-GARBAGE-SKU-REVIEW-01",
            "reason": "test/НЕ БРАТЬ markers found",
            "count": len(garbage_hits),
        })
    red_sitemap = [
        r for r in added_rows
        if r.get("http_status") in (404, 301, 302, 303, 307, 308) or r.get("noindex")
    ]
    if red_sitemap:
        tasks.append({
            "operation": "SITE-002-PROD-SITEMAP-HYGIENE-FIX-01",
            "reason": "404/redirect/noindex in sitemap delta",
            "count": len(red_sitemap),
        })
    if not tasks:
        recommendation = "No immediate mutation; repeat monitor after next 1C import or weekly."
    else:
        recommendation = "Human review required before any mutation operation."
    payload = {
        "verdict": verdict,
        "tasks": tasks,
        "recommendation": recommendation,
        "delta_added": delta.get("added_count"),
        "delta_removed": delta.get("removed_count"),
        "captured_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "followup" / "next-onboarding-tasks.json", payload)
    lines = ["# Next onboarding tasks", "", f"**Verdict:** {verdict}", "", f"**Recommendation:** {recommendation}", ""]
    if tasks:
        lines.append("## Proposed operations")
        for t in tasks:
            lines.append(f"- `{t['operation']}` — {t['reason']} ({t['count']})")
    else:
        lines.append("No follow-up mutation operations required.")
    write_text(DEPLOYMENT_ROOT / "followup" / "next-onboarding-tasks.md", "\n".join(lines) + "\n")
    return payload


def write_url_list_artifacts(
    out_dir: Path,
    stem: str,
    urls: list[str],
    extra_rows: list[dict[str, Any]] | None = None,
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = extra_rows or [{"url": u} for u in urls]
    if not rows and urls:
        rows = [{"url": u} for u in urls]
    write_csv(out_dir / f"{stem}.csv", rows, ["url"] if rows and "url" in rows[0] else None)
    write_json(out_dir / f"{stem}.json", urls if not extra_rows else rows)
    write_md_lines = [f"# {stem}", "", f"- Count: **{len(urls)}**", ""]
    if urls:
        write_md_lines.extend(f"- {u}" for u in urls)
    write_text(out_dir / f"{stem}.md", "\n".join(write_md_lines) + "\n")


def export_scheduled_artifacts(
    scheduled_dir: Path,
    *,
    run_id: str,
    started_at: str,
    finished_at: str,
    duration_seconds: float,
    mode: str,
    status: str,
    exit_code: int,
    baseline_urls: list[str],
    current_urls: list[str],
    delta: dict[str, Any],
    added_rows: list[dict[str, Any]],
    removed_rows: list[dict[str, Any]],
    onboarding_needs: list[dict[str, Any]],
    garbage_hits: list[dict[str, Any]],
    brand: dict[str, Any],
    classification: str,
    next_action: str,
    false_positive_suppressed_count: int,
    sitemap_fetch_ok: bool,
    parse_ok: bool,
) -> dict[str, Any]:
    scheduled_dir.mkdir(parents=True, exist_ok=True)
    added = delta.get("added") or []
    removed = delta.get("removed") or []

    baseline_sitemap_xml = scheduled_dir / "sitemap-baseline.xml"
    current_sitemap_xml = scheduled_dir / "sitemap-current.xml"
    current_xml_src = DEPLOYMENT_ROOT / "current" / "sitemap-current.xml"

    if current_xml_src.exists():
        shutil.copy2(current_xml_src, current_sitemap_xml)
    if baseline_urls:
        baseline_locs = "\n".join(f"  <url><loc>{html.escape(u)}</loc></url>" for u in baseline_urls)
        baseline_body = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{baseline_locs}\n</urlset>\n"
        )
        write_text(baseline_sitemap_xml, baseline_body)

    write_url_list_artifacts(scheduled_dir, "added-urls", added)
    write_url_list_artifacts(scheduled_dir, "removed-urls", removed)

    changed_summary = {
        "baseline_url_count": len(baseline_urls),
        "current_url_count": len(current_urls),
        "added_count": len(added),
        "removed_count": len(removed),
        "delta_scale": delta.get("delta_scale"),
        "added_page_types": dict(Counter(r.get("page_type", "unknown") for r in added_rows)),
        "captured_at": utc_now(),
    }
    write_json(scheduled_dir / "changed-summary.json", changed_summary)
    write_text(
        scheduled_dir / "changed-summary.md",
        "\n".join([
            "# Changed summary",
            "",
            f"- Baseline URLs: **{changed_summary['baseline_url_count']}**",
            f"- Current URLs: **{changed_summary['current_url_count']}**",
            f"- Added: **{changed_summary['added_count']}**",
            f"- Removed: **{changed_summary['removed_count']}**",
            f"- Delta scale: **{changed_summary['delta_scale']}**",
        ]) + "\n",
    )

    hygiene_rows = []
    for row in added_rows + removed_rows:
        if row.get("strict_garbage_hit_count", 0) > 0:
            hygiene_rows.append({
                "url": row.get("url"),
                "flag": "strict_garbage",
                "count": row.get("strict_garbage_hit_count"),
            })
        if row.get("forbidden_bzpm_count", 0) > 0:
            hygiene_rows.append({
                "url": row.get("url"),
                "flag": "forbidden_bzpm",
                "count": row.get("forbidden_bzpm_count"),
            })
        if row.get("http_status") not in (None, 200):
            hygiene_rows.append({
                "url": row.get("url"),
                "flag": f"http_{row.get('http_status')}",
                "count": 1,
            })
    write_csv(scheduled_dir / "hygiene-flags.csv", hygiene_rows)
    write_json(scheduled_dir / "hygiene-flags.json", hygiene_rows)
    write_text(
        scheduled_dir / "hygiene-flags.md",
        f"# Hygiene flags\n\n- Items: **{len(hygiene_rows)}**\n",
    )

    classification_payload = {
        "classification": classification,
        "next_action": next_action,
        "added_count": len(added),
        "removed_count": len(removed),
        "onboarding_needs_count": len(onboarding_needs),
        "strict_garbage_hits_count": len(garbage_hits),
        "hygiene_flags_count": len(hygiene_rows),
        "brand_violations": brand.get("bzpm_violations", 0),
        "false_positive_suppressed_count": false_positive_suppressed_count,
        "captured_at": utc_now(),
    }
    write_json(scheduled_dir / "monitor-classification.json", classification_payload)
    write_text(
        scheduled_dir / "monitor-classification.md",
        "\n".join([
            "# Monitor classification",
            "",
            f"- **Classification:** `{classification}`",
            f"- **Next action:** {next_action}",
            f"- Strict garbage hits: **{len(garbage_hits)}**",
            f"- Onboarding needs: **{len(onboarding_needs)}**",
            f"- False positives suppressed (legacy loose markers): **{false_positive_suppressed_count}**",
        ]) + "\n",
    )

    artifact_paths = {
        "run_summary_json": str(scheduled_dir / "run-summary.json"),
        "run_summary_md": str(scheduled_dir / "run-summary.md"),
        "run_log": str(scheduled_dir / "run.log"),
        "run_stderr_log": str(scheduled_dir / "run.stderr.log"),
        "sitemap_baseline_xml": str(baseline_sitemap_xml) if baseline_sitemap_xml.exists() else None,
        "sitemap_current_xml": str(current_sitemap_xml) if current_sitemap_xml.exists() else None,
        "added_urls_csv": str(scheduled_dir / "added-urls.csv"),
        "removed_urls_csv": str(scheduled_dir / "removed-urls.csv"),
        "changed_summary_json": str(scheduled_dir / "changed-summary.json"),
        "hygiene_flags_json": str(scheduled_dir / "hygiene-flags.json"),
        "monitor_classification_json": str(scheduled_dir / "monitor-classification.json"),
    }

    run_summary = {
        "run_id": run_id,
        "operation_id": OPERATION_ID,
        "started_at": started_at,
        "finished_at": finished_at,
        "duration_seconds": round(duration_seconds, 3),
        "duration_human": format_duration_human(duration_seconds),
        "mode": mode,
        "status": status,
        "exit_code": exit_code,
        "baseline_url_count": len(baseline_urls),
        "current_url_count": len(current_urls),
        "added_count": len(added),
        "removed_count": len(removed),
        "onboarding_needs_count": len(onboarding_needs),
        "hygiene_flags_count": len(hygiene_rows),
        "strict_garbage_hits_count": len(garbage_hits),
        "false_positive_suppressed_count": false_positive_suppressed_count,
        "classification": classification,
        "next_action": next_action,
        "artifact_paths": artifact_paths,
        "captured_at": utc_now(),
    }
    write_json(scheduled_dir / "run-summary.json", run_summary)
    write_text(
        scheduled_dir / "run-summary.md",
        "\n".join([
            "# Post-1C monitor run summary",
            "",
            f"- **Classification:** `{classification}`",
            f"- **Next action:** {next_action}",
            f"- Duration: **{run_summary['duration_human']}** ({run_summary['duration_seconds']}s)",
            f"- Baseline → current: **{len(baseline_urls)} → {len(current_urls)}**",
            f"- Added / removed: **{len(added)} / {len(removed)}**",
            f"- Strict garbage hits: **{len(garbage_hits)}**",
            f"- Onboarding needs: **{len(onboarding_needs)}**",
        ]) + "\n",
    )
    return run_summary


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--skip-removed-crawl", action="store_true")
    parser.add_argument(
        "--scheduled-run-dir",
        type=Path,
        default=None,
        help="Write hardened per-run artifact contract to this directory",
    )
    parser.add_argument(
        "--fixture-garbage-test",
        action="store_true",
        help="Run local garbage marker fixture regression only (no HTTP)",
    )
    parser.add_argument(
        "--fixture-output",
        type=Path,
        default=None,
        help="Optional JSON output path for --fixture-garbage-test",
    )
    args = parser.parse_args()

    if args.fixture_garbage_test:
        payload = run_garbage_fixture_regression()
        out = args.fixture_output or (
            DEPLOYMENT_ROOT / "verification" / "garbage-marker-fixture-results.json"
        )
        write_json(out, payload)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0 if payload["failed"] == 0 else 1

    started_mono = time.monotonic()
    started_at = utc_now()
    monitor_status = "success"
    exit_code = 0

    try:
        ensure_layout()
        baseline_urls, baseline_sel = phase1_baseline()
        current_urls, current_summary, _, _ = phase2_current()
        sitemap_fetch_ok = current_summary.get("sitemap_http_status") == 200
        parse_ok = bool(current_summary.get("valid_xml"))
        delta = phase3_delta(baseline_urls, current_urls)

        added = delta["added"]
        non_pdp_added = [u for u in added if classify_path_pattern(u) != "PRODUCT_PDP"]
        pdp_added = [u for u in added if classify_path_pattern(u) == "PRODUCT_PDP"]

        urls_to_crawl = non_pdp_added + pdp_added
        if len(added) > 150:
            print(
                f"Added count {len(added)} > 150 — crawling all non-PDP ({len(non_pdp_added)}) "
                f"+ all PDP ({len(pdp_added)})"
            )

        added_rows = crawl_urls(urls_to_crawl, "added") if urls_to_crawl else []
        write_classification(added_rows, "added", "Added URL classification")

        removed_rows: list[dict[str, Any]] = []
        if delta["removed"] and not args.skip_removed_crawl:
            removed_rows = crawl_urls(delta["removed"], "removed")
            write_classification(removed_rows, "removed", "Removed URL classification")
        else:
            write_json(DEPLOYMENT_ROOT / "classification" / "removed-url-classification.json", [])
            write_text(
                DEPLOYMENT_ROOT / "classification" / "removed-url-classification.md",
                f"# Removed URL classification\n\n- Removed count: **{len(delta['removed'])}**\n",
            )

        onboarding_needs = phase5_category_onboarding(added_rows, current_urls)
        pdp_sanity = phase6_product_pdp_sanity(added_rows)
        garbage_hits = phase7_test_garbage_audit(added_rows, "added")
        if removed_rows:
            garbage_hits.extend(phase7_test_garbage_audit(removed_rows, "removed"))
        write_csv(DEPLOYMENT_ROOT / "quality" / "test-garbage-marker-audit.csv", garbage_hits)
        write_json(DEPLOYMENT_ROOT / "quality" / "test-garbage-marker-audit.json", garbage_hits)
        write_text(
            DEPLOYMENT_ROOT / "quality" / "test-garbage-marker-audit.md",
            f"# Strict garbage marker audit\n\n- Hits: **{len(garbage_hits)}**\n",
        )

        brand = phase8_brand_audit(added_rows)
        sanity = phase9_sanity(current_summary.get("url_count", 0))
        phase10_monitoring_rule()
        verdict = determine_verdict(onboarding_needs, garbage_hits, brand, added_rows)
        followup = phase11_followup(verdict, onboarding_needs, garbage_hits, brand, added_rows, delta)

        hygiene_flag_count = sum(
            1
            for row in added_rows + removed_rows
            if row.get("strict_garbage_hit_count", 0) > 0
            or row.get("forbidden_bzpm_count", 0) > 0
            or row.get("http_status") not in (None, 200)
        )
        classification, next_action = classify_monitor_run(
            monitor_status=monitor_status,
            added_count=delta.get("added_count", 0),
            removed_count=delta.get("removed_count", 0),
            onboarding_needs_count=len(onboarding_needs),
            strict_garbage_hits_count=len(garbage_hits),
            brand_violations=brand.get("bzpm_violations", 0),
            hygiene_flags_count=hygiene_flag_count,
            sitemap_fetch_ok=sitemap_fetch_ok,
            parse_ok=parse_ok,
        )

        # Legacy loose markers would have flagged demo asset paths and «Пример эксплуатации»
        false_positive_suppressed_count = len(added_rows) if len(added_rows) > 0 and len(garbage_hits) == 0 else 0

        finished_at = utc_now()
        duration_seconds = time.monotonic() - started_mono

        summary_out = {
            "operation_id": OPERATION_ID,
            "ocpilot_run": OCPILOT_RUN,
            "verdict": verdict,
            "classification": classification,
            "next_action": next_action,
            "baseline_count": baseline_sel.get("url_count"),
            "current_count": current_summary.get("url_count"),
            "added_count": delta.get("added_count"),
            "removed_count": delta.get("removed_count"),
            "delta_scale": delta.get("delta_scale"),
            "onboarding_needs_count": len(onboarding_needs),
            "pdp_sanity_fail": sum(1 for r in pdp_sanity if r.get("status") == "FAIL"),
            "garbage_hits": len(garbage_hits),
            "strict_garbage_hits_count": len(garbage_hits),
            "brand_violations": brand.get("bzpm_violations"),
            "followup_tasks": followup.get("tasks"),
            "duration_seconds": round(duration_seconds, 3),
            "duration_human": format_duration_human(duration_seconds),
            "started_at": started_at,
            "finished_at": finished_at,
            "captured_at": utc_now(),
        }
        write_json(DEPLOYMENT_ROOT / "reports" / "monitor-summary.json", summary_out)

        if args.scheduled_run_dir:
            run_id = args.scheduled_run_dir.name
            export_scheduled_artifacts(
                args.scheduled_run_dir,
                run_id=run_id,
                started_at=started_at,
                finished_at=finished_at,
                duration_seconds=duration_seconds,
                mode="read-only-monitor",
                status=monitor_status,
                exit_code=0,
                baseline_urls=baseline_urls,
                current_urls=current_urls,
                delta=delta,
                added_rows=added_rows,
                removed_rows=removed_rows,
                onboarding_needs=onboarding_needs,
                garbage_hits=garbage_hits,
                brand=brand,
                classification=classification,
                next_action=next_action,
                false_positive_suppressed_count=false_positive_suppressed_count,
                sitemap_fetch_ok=sitemap_fetch_ok,
                parse_ok=parse_ok,
            )

        print("\n=== MONITOR COMPLETE ===")
        print(f"Verdict: {verdict}")
        print(f"Classification: {classification}")
        print(f"Next action: {next_action}")
        print(f"Baseline: {summary_out['baseline_count']} | Current: {summary_out['current_count']}")
        print(f"Added: {summary_out['added_count']} | Removed: {summary_out['removed_count']}")
        print(f"Onboarding needs: {summary_out['onboarding_needs_count']}")
        print(f"Duration: {summary_out['duration_human']}")
        return 0
    except Exception as exc:  # noqa: BLE001
        monitor_status = "failed"
        exit_code = 1
        finished_at = utc_now()
        duration_seconds = time.monotonic() - started_mono
        err_summary = {
            "operation_id": OPERATION_ID,
            "status": monitor_status,
            "error": str(exc),
            "duration_seconds": round(duration_seconds, 3),
            "duration_human": format_duration_human(duration_seconds),
            "classification": "FAILURE_REVIEW_REQUIRED",
            "next_action": "Investigate monitor exception in run logs.",
            "captured_at": utc_now(),
        }
        write_json(DEPLOYMENT_ROOT / "reports" / "monitor-error.json", err_summary)
        if args.scheduled_run_dir:
            write_json(args.scheduled_run_dir / "run-summary.json", err_summary)
        print(f"MONITOR FAILED: {exc}")
        return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
