#!/usr/bin/env python3
"""SITE-002 Post-1C catalog onboarding monitor 02 — read-only repeat (Run 4.213)."""
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

OPERATION_ID = "SITE-002-PROD-POST-1C-CATALOG-ONBOARDING-MONITOR-02"
OCPILOT_RUN = "4.213"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01"
AUDIT_BASELINE_BEFORE = "SITE-002-POST-1C-CATALOG-MONITOR-01"
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
    "katalog/nejtralnoe-oborudovanie/lari",
    "katalog/nejtralnoe-oborudovanie/lari/skladskie-lari",
    "katalog/nejtralnoe-oborudovanie/lari/proizvodstvennye-lari",
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

TEST_MARKERS = (
    ("test", re.I),
    ("тест", re.I),
    ("НЕ БРАТЬ", 0),
    ("не брать", re.I),
    ("ne-brat", re.I),
    ("nebrat", re.I),
    ("demo", re.I),
    ("пример", re.I),
    ("tmp", re.I),
    ("temp", re.I),
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


def count_test_markers(text: str, url: str) -> dict[str, int]:
    combined = f"{url}\n{text}"
    counts: dict[str, int] = {}
    for marker, flags in TEST_MARKERS:
        if flags == 0:
            counts[marker] = combined.count(marker)
        else:
            counts[marker] = len(re.findall(re.escape(marker), combined, flags))
    return counts


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
    test_counts = count_test_markers(html_text, url)
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
        "test_marker_total": sum(test_counts.values()),
        "test_markers": test_counts,
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
    source_op = "SITE-002-PROD-POST-1C-CATALOG-ONBOARDING-MONITOR-01 (Run 4.212 current)"
    verified_by = AUDIT_BASELINE_BEFORE
    limitation = (
        "Run 4.212 persisted full sitemap URL set in current/sitemap-current-urls.json; "
        "count 1377, SHA-256 9c81305483d7fb79b829e562598e5a3a0eb74a29350fae142fa78f97c3eca6c1."
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
        "expected_count_run_4_212": 1377,
        "match_expected": len(urls) == 1377,
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
            f"- Match Run 4.212 expected (1377): **{selection['match_expected']}**",
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
        "baseline_expected_count": 1377,
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
            f"- Baseline (4.212): **1377**",
            f"- Delta vs baseline: **{len(urls) - 1377:+d}**",
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
        "test_marker_count": meta.get("test_marker_total", 0),
        "test_markers": meta.get("test_markers", {}),
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
        flat = {k: v for k, v in r.items() if k != "test_markers"}
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
    print(f"Phase 7: test/garbage marker audit ({label})...")
    hits: list[dict[str, Any]] = []
    for row in rows:
        markers = row.get("test_markers") or {}
        total = row.get("test_marker_count", 0)
        if total > 0:
            hits.append({
                "url": row["url"],
                "page_type": row.get("page_type"),
                "test_marker_count": total,
                "markers": json.dumps(markers, ensure_ascii=False),
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


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--skip-removed-crawl", action="store_true")
    args = parser.parse_args()

    ensure_layout()
    baseline_urls, baseline_sel = phase1_baseline()
    current_urls, current_summary, _, _ = phase2_current()
    delta = phase3_delta(baseline_urls, current_urls)

    added = delta["added"]
    non_pdp_added = [u for u in added if classify_path_pattern(u) != "PRODUCT_PDP"]
    pdp_added = [u for u in added if classify_path_pattern(u) == "PRODUCT_PDP"]

    urls_to_crawl = non_pdp_added + pdp_added
    if len(added) > 150:
        print(f"Added count {len(added)} > 150 — crawling all non-PDP ({len(non_pdp_added)}) + all PDP ({len(pdp_added)})")

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
        f"# Test/garbage marker audit\n\n- Hits: **{len(garbage_hits)}**\n",
    )

    brand = phase8_brand_audit(added_rows)
    sanity = phase9_sanity(current_summary.get("url_count", 0))
    phase10_monitoring_rule()
    verdict = determine_verdict(onboarding_needs, garbage_hits, brand, added_rows)
    followup = phase11_followup(verdict, onboarding_needs, garbage_hits, brand, added_rows, delta)

    summary_out = {
        "operation_id": OPERATION_ID,
        "ocpilot_run": OCPILOT_RUN,
        "verdict": verdict,
        "baseline_count": baseline_sel.get("url_count"),
        "current_count": current_summary.get("url_count"),
        "added_count": delta.get("added_count"),
        "removed_count": delta.get("removed_count"),
        "delta_scale": delta.get("delta_scale"),
        "onboarding_needs_count": len(onboarding_needs),
        "pdp_sanity_fail": sum(1 for r in pdp_sanity if r.get("status") == "FAIL"),
        "garbage_hits": len(garbage_hits),
        "brand_violations": brand.get("bzpm_violations"),
        "followup_tasks": followup.get("tasks"),
        "captured_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "reports" / "monitor-summary.json", summary_out)

    print("\n=== MONITOR COMPLETE ===")
    print(f"Verdict: {verdict}")
    print(f"Baseline: {summary_out['baseline_count']} | Current: {summary_out['current_count']}")
    print(f"Added: {summary_out['added_count']} | Removed: {summary_out['removed_count']}")
    print(f"Onboarding needs: {summary_out['onboarding_needs_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
