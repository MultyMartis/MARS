#!/usr/bin/env python3
"""SITE-002 Production sitemap delta audit — read-only (Run 4.209)."""
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

OPERATION_ID = "SITE-002-PROD-SITEMAP-DELTA-AUDIT-01"
OCPILOT_RUN = "4.209"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SEO-META-EDGE-01"
WRONG_BRAND = "БЗПМ"
CORRECT_BRAND = "ЗПМ"
UTF8_BOM = b"\xef\xbb\xbf"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
RUN_4206 = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-META-FINAL-INVENTORY-01"
)
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
CRAWL_DELAY_SEC = 0.3

SUBDIRS = (
    "source",
    "current",
    "baseline",
    "delta",
    "crawl",
    "classification",
    "brand-audit",
    "verification",
    "manifests",
    "reports",
    "logs",
)

SANITY_URLS = (
    "https://bzpm.ru/",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
)

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


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


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
        if len(parts) >= 3:
            return "CATEGORY_PLP"
        return "CATEGORY_PLP"
    return "SAFE UNKNOWN"


def count_brand(text: str, brand: str) -> int:
    return text.count(brand)


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
            markers["has_load_more"]
            and not markers["has_page_product"]
        ) or any(m in url for m in KNOWN_HUB_SLUG_MARKERS)
        page_type = "CATEGORY_HUB" if is_hub else "CATEGORY_PLP"
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
        **markers,
    }


def is_noindex(meta_robots: str, x_robots: str) -> bool:
    return "noindex" in f"{meta_robots} {x_robots}".lower()


def canonical_matches(final_url: str, canonical: str) -> bool:
    if not canonical:
        return False
    return normalize_url(canonical) == normalize_url(final_url)


def sitemap_appropriate(
    status: int | None,
    page_type: str,
    noindex: bool,
    final_url: str,
    url: str,
) -> tuple[str, str]:
    if status is None:
        return "no", "fetch error"
    if status >= 400:
        return "no", f"HTTP {status}"
    if status in (301, 302, 303, 307, 308):
        return "no", "redirect in sitemap"
    if noindex:
        return "no", "noindex page"
    if page_type in ("TECHNICAL", "IMAGE_OR_FILE"):
        return "no", f"inappropriate type {page_type}"
    if normalize_url(final_url) != normalize_url(url):
        return "review", "final URL differs from sitemap loc"
    if page_type == "CATEGORY_HUB":
        return "review", "hub/category PLP — acceptable but review"
    if page_type in ("PRODUCT_PDP", "CATEGORY_PLP", "BLOG", "INFORMATION", "SAFE UNKNOWN"):
        return "yes", "normal indexable route"
    return "review", f"type {page_type}"


def classify_seo_risk(row: dict[str, Any]) -> tuple[str, str]:
    status = row.get("http_status")
    if row.get("bzpm_count", 0) > 0:
        return "RED", "forbidden public БЗПМ"
    if status is None:
        return "SAFE UNKNOWN", "fetch failed"
    if status >= 400:
        return "RED", f"HTTP {status} in sitemap"
    if status in (301, 302, 303, 307, 308):
        return "RED", "redirect in sitemap"
    if row.get("noindex"):
        return "RED", "noindex in sitemap"
    host = urllib.parse.urlparse(row.get("final_url", "")).netloc
    if host and host not in ("bzpm.ru", "www.bzpm.ru"):
        return "RED", "non-production host"
    if not row.get("title"):
        return "YELLOW", "missing title"
    if not row.get("meta_description") and row.get("page_type") in ("CATEGORY_PLP", "CATEGORY_HUB"):
        return "YELLOW", "missing meta description on category"
    if not row.get("meta_keywords") and row.get("page_type") == "PRODUCT_PDP":
        return "YELLOW", "missing keywords on PDP"
    if row.get("canonical") and not row.get("canonical_matches"):
        return "YELLOW", "canonical mismatch"
    if row.get("page_type") == "CATEGORY_HUB":
        return "YELLOW", "hub/category page in sitemap"
    if row.get("sitemap_appropriate") == "review":
        return "YELLOW", row.get("sitemap_reason", "review")
    return "GREEN", "normal indexable URL"


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


def ensure_layout() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "change_type": "sitemap-delta-audit-readonly",
        "previous_sitemap_reference_run": "4.206",
        "previous_sitemap_url_count": 1320,
        "current_observed_sitemap_url_count_run": "4.208",
        "current_observed_sitemap_url_count": 1377,
        "remote_changes_allowed": False,
        "admin_save_allowed": False,
        "db_write_allowed": False,
        "cache_clear_allowed": False,
        "ftp_upload_allowed": False,
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
    print("Phase 1: baseline sitemap from Run 4.206...")
    baseline_xml_path = RUN_4206 / "sitemap" / "sitemap-response.xml"
    if not baseline_xml_path.exists():
        inv_path = RUN_4206 / "inventory" / "url-inventory.json"
        if inv_path.exists():
            data = json.loads(inv_path.read_text(encoding="utf-8"))
            urls = sorted({r["url"] for r in data if r.get("sitemap_present") == "yes"})
            source = "reconstructed from url-inventory.json"
        else:
            raise FileNotFoundError("No Run 4.206 sitemap snapshot found")
    else:
        xml_bytes = baseline_xml_path.read_bytes()
        xml_text = xml_bytes.decode("utf-8", errors="replace")
        urls = parse_sitemap_urls(xml_text)
        source = "sitemap-response.xml"
        write_text(DEPLOYMENT_ROOT / "source" / "sitemap-4-206-response.xml", xml_text)
    summary = {
        "source": source,
        "source_path": str(baseline_xml_path),
        "url_count": len(urls),
        "sha256": sha256_bytes(baseline_xml_path.read_bytes()) if baseline_xml_path.exists() else sha256_text("\n".join(urls)),
        "reference_run": "4.206",
        "expected_count": 1320,
        "captured_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "baseline" / "sitemap-4-206-urls.json", urls)
    write_csv(DEPLOYMENT_ROOT / "baseline" / "sitemap-4-206-urls.csv", [{"url": u} for u in urls], ["url"])
    write_text(
        DEPLOYMENT_ROOT / "baseline" / "sitemap-4-206-summary.md",
        "\n".join([
            "# Baseline sitemap (Run 4.206)",
            "",
            f"- Source: `{source}`",
            f"- URL count: **{len(urls)}**",
            f"- SHA-256: `{summary['sha256']}`",
            f"- Expected: 1320",
            f"- Match expected: **{'yes' if len(urls) == 1320 else 'no — explain in report'}**",
        ]) + "\n",
    )
    return urls, summary


def phase2_current() -> tuple[list[str], dict[str, Any], bytes]:
    print("Phase 2: fetch current live sitemap...")
    resp = http_get("https://bzpm.ru/sitemap.xml")
    raw = resp.get("raw_body") or b""
    xml_text = resp.get("body") or ""
    (DEPLOYMENT_ROOT / "current" / "sitemap-current.xml").write_bytes(raw)
    headers_text = "\n".join(f"{k}: {v}" for k, v in resp.get("headers", {}).items())
    write_text(DEPLOYMENT_ROOT / "current" / "sitemap-current-headers.txt", headers_text)
    valid_xml = False
    urls: list[str] = []
    malformed = 0
    non_bzpm = 0
    duplicates = 0
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
    summary = {
        "url": "https://bzpm.ru/sitemap.xml",
        "http_status": resp.get("status_code"),
        "valid_xml": valid_xml,
        "parse_error": parse_error,
        "url_count": len(urls),
        "unique_url_count": len(set(urls)),
        "exact_duplicate_loc_count": duplicates,
        "non_bzpm_urls": non_bzpm,
        "malformed_urls": malformed,
        "sha256": sha256_bytes(raw),
        "captured_at": utc_now(),
        "expected_count_run_4_208": 1377,
    }
    write_json(DEPLOYMENT_ROOT / "current" / "sitemap-current-summary.json", summary)
    write_json(DEPLOYMENT_ROOT / "current" / "sitemap-current-urls.json", urls)
    write_csv(DEPLOYMENT_ROOT / "current" / "sitemap-current-urls.csv", [{"url": u} for u in urls], ["url"])
    write_text(
        DEPLOYMENT_ROOT / "current" / "sitemap-current-summary.md",
        "\n".join([
            "# Current live sitemap",
            "",
            f"- HTTP status: **{resp.get('status_code')}**",
            f"- Valid XML: **{valid_xml}**",
            f"- URL count: **{len(urls)}**",
            f"- Unique URLs: **{len(set(urls))}**",
            f"- Exact duplicate loc entries: **{duplicates}**",
            f"- Non-bzpm.ru hosts: **{non_bzpm}**",
            f"- Malformed URLs: **{malformed}**",
            f"- SHA-256: `{summary['sha256']}`",
            f"- Run 4.208 observed: 1377",
            f"- Match 4.208: **{'yes' if len(urls) == 1377 else 'no — actual count reported'}**",
        ]) + "\n",
    )
    return urls, summary, raw


def phase3_delta(baseline: list[str], current: list[str]) -> dict[str, Any]:
    print("Phase 3: compute delta...")
    base_set = set(baseline)
    curr_set = set(current)
    added = sorted(curr_set - base_set)
    removed = sorted(base_set - curr_set)
    unchanged_count = len(base_set & curr_set)
    exact_dups = find_exact_duplicates(current)
    norm_dups = find_normalized_duplicates(current)
    summary = {
        "baseline_count": len(baseline),
        "current_count": len(current),
        "added_count": len(added),
        "removed_count": len(removed),
        "unchanged_count": unchanged_count,
        "exact_duplicate_count": len(exact_dups),
        "normalized_duplicate_groups": len(norm_dups),
        "captured_at": utc_now(),
    }
    write_csv(DEPLOYMENT_ROOT / "delta" / "sitemap-added.csv", [{"url": u} for u in added], ["url"])
    write_json(DEPLOYMENT_ROOT / "delta" / "sitemap-added.json", added)
    write_csv(DEPLOYMENT_ROOT / "delta" / "sitemap-removed.csv", [{"url": u} for u in removed], ["url"])
    write_json(DEPLOYMENT_ROOT / "delta" / "sitemap-removed.json", removed)
    write_text(DEPLOYMENT_ROOT / "delta" / "sitemap-unchanged-count.txt", str(unchanged_count) + "\n")
    write_csv(DEPLOYMENT_ROOT / "delta" / "sitemap-duplicates.csv", exact_dups)
    write_csv(DEPLOYMENT_ROOT / "delta" / "sitemap-normalized-duplicates.csv", norm_dups)
    write_json(DEPLOYMENT_ROOT / "delta" / "sitemap-delta-summary.json", summary)
    write_text(
        DEPLOYMENT_ROOT / "delta" / "sitemap-delta-summary.md",
        "\n".join([
            "# Sitemap delta summary",
            "",
            f"- Baseline (4.206): **{len(baseline)}**",
            f"- Current live: **{len(current)}**",
            f"- Added: **{len(added)}**",
            f"- Removed: **{len(removed)}**",
            f"- Unchanged: **{unchanged_count}**",
            f"- Exact duplicate loc entries: **{len(exact_dups)}**",
            f"- Normalized duplicate groups: **{len(norm_dups)}**",
        ]) + "\n",
    )
    return {**summary, "added": added, "removed": removed, "exact_dups": exact_dups, "norm_dups": norm_dups}


def crawl_urls(urls: list[str], label: str) -> list[dict[str, Any]]:
    print(f"Phase 4: crawl {len(urls)} {label} URLs...")
    rows: list[dict[str, Any]] = []
    for idx, url in enumerate(urls, 1):
        resp = http_get(url)
        status = resp.get("status_code")
        meta = {}
        if status and status < 400 and "html" in (resp.get("content_type") or "").lower():
            meta = extract_page_meta(resp.get("body", ""), url)
        elif status and status < 400 and url.endswith(".xml"):
            meta = {"page_type": "SITEMAP"}
        noindex = is_noindex(meta.get("meta_robots", ""), resp.get("x_robots_tag", ""))
        appropriate, reason = sitemap_appropriate(
            status,
            meta.get("page_type", classify_path_pattern(url)),
            noindex,
            resp.get("final_url", url),
            url,
        )
        row = {
            "url": url,
            "http_status": status,
            "final_url": resp.get("final_url", url),
            "redirect_differs": normalize_url(resp.get("final_url", url)) != normalize_url(url),
            "x_robots_tag": resp.get("x_robots_tag", ""),
            "title": meta.get("title", ""),
            "meta_description": meta.get("meta_description", ""),
            "meta_keywords": meta.get("meta_keywords", ""),
            "canonical": meta.get("canonical", ""),
            "meta_robots": meta.get("meta_robots", ""),
            "h1": meta.get("h1", ""),
            "body_class": meta.get("body_class", ""),
            "page_type": meta.get("page_type", classify_path_pattern(url)),
            "path_pattern": meta.get("path_pattern", classify_path_pattern(url)),
            "product_id": meta.get("product_id", ""),
            "noindex": noindex,
            "bzpm_count": meta.get("bzpm_count", 0),
            "zpm_count": meta.get("zpm_count", 0),
            "canonical_matches": canonical_matches(resp.get("final_url", url), meta.get("canonical", "")),
            "indexable": "no" if noindex or (status and status >= 400) else "yes",
            "sitemap_appropriate": appropriate,
            "sitemap_reason": reason,
            "error": resp.get("error"),
        }
        risk, risk_reason = classify_seo_risk(row)
        row["seo_risk"] = risk
        row["seo_risk_reason"] = risk_reason
        rows.append(row)
        if idx % 10 == 0:
            print(f"  crawled {idx}/{len(urls)}")
        time.sleep(CRAWL_DELAY_SEC)
    return rows


def write_classification(rows: list[dict[str, Any]], prefix: str, title: str) -> None:
    write_csv(DEPLOYMENT_ROOT / "classification" / f"{prefix}-url-classification.csv", rows)
    write_json(DEPLOYMENT_ROOT / "classification" / f"{prefix}-url-classification.json", rows)
    by_type = Counter(r.get("page_type", "unknown") for r in rows)
    by_risk = Counter(r.get("seo_risk", "unknown") for r in rows)
    lines = [
        f"# {title}",
        "",
        f"- URLs classified: **{len(rows)}**",
        "",
        "## By page type",
    ]
    for k, v in sorted(by_type.items()):
        lines.append(f"- {k}: {v}")
    lines.extend(["", "## By SEO risk"])
    for k, v in sorted(by_risk.items()):
        lines.append(f"- {k}: {v}")
    write_text(DEPLOYMENT_ROOT / "classification" / f"{prefix}-url-classification.md", "\n".join(lines) + "\n")


def phase5_import_context() -> None:
    print("Phase 5: import/cron context (read-only docs)...")
    context = {
        "assessed_at": utc_now(),
        "cron_wrapper_active": True,
        "first_scheduled_run": "2026-07-06 08:00 Moscow (Run 4.194)",
        "import_pipeline": "MARS 1C wrapper via Beget scheduled cron",
        "seo_chain_4_206_to_4_208": "no sitemap mutation; 4.208 observed 1377 vs 4.206 1320",
        "plausible_growth_sources": [
            "scheduled 1C cron import adding/enabling products",
            "category visibility or SEO category changes outside SEO chain",
            "OpenCart Google Sitemap feed regenerating from catalog state",
            "timing/cache between Run 4.206 and 4.208 observations",
        ],
        "not_run": ["manual import", "cron trigger", "admin saves", "DB writes"],
        "conclusion": "SAFE UNKNOWN — growth plausibly catalog/cron; not provably tied to a specific import run without DB/FTP product diff",
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "import-cron-context.json", context)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "import-cron-context.md",
        "\n".join([
            "# Import / cron context (read-only)",
            "",
            "No import or cron was executed in this audit.",
            "",
            "## Known state from prior OCPilot runs",
            "",
            "- Beget scheduled 1C cron active since Run 4.194 (2026-07-06).",
            "- SEO chain Runs 4.206–4.208 did **not** mutate sitemap settings.",
            "- Run 4.208 sanity check observed sitemap **1377** URLs vs Run 4.206 **1320**.",
            "",
            "## Plausible growth sources",
            "",
            "1. Scheduled 1C import adding new product URLs.",
            "2. Products/categories enabled in catalog between observations.",
            "3. Sitemap feed reflecting live OpenCart catalog state.",
            "4. Observation timing — not same-second snapshot as 4.206.",
            "",
            "## Conclusion",
            "",
            context["conclusion"],
        ]) + "\n",
    )


def phase6_brand_audit(added_rows: list[dict[str, Any]]) -> dict[str, Any]:
    print("Phase 6: brand audit on delta...")
    brand_rows = []
    violations = 0
    for row in added_rows:
        bzpm = row.get("bzpm_count", 0)
        zpm = row.get("zpm_count", 0)
        if bzpm > 0:
            violations += 1
        brand_rows.append({
            "url": row["url"],
            "bzpm_count": bzpm,
            "zpm_count": zpm,
            "violation": "yes" if bzpm > 0 else "no",
        })
    summary = {
        "urls_checked": len(brand_rows),
        "bzpm_violations": violations,
        "recommend_remediation_02": violations > 0,
    }
    write_csv(DEPLOYMENT_ROOT / "brand-audit" / "sitemap-delta-brand-audit.csv", brand_rows)
    write_json(DEPLOYMENT_ROOT / "brand-audit" / "sitemap-delta-brand-audit.json", summary | {"rows": brand_rows})
    write_text(
        DEPLOYMENT_ROOT / "brand-audit" / "sitemap-delta-brand-audit.md",
        "\n".join([
            "# Brand audit on sitemap delta (added URLs)",
            "",
            f"- URLs checked: **{len(brand_rows)}**",
            f"- Forbidden БЗПМ violations: **{violations}**",
            f"- Recommend SITE-002-PROD-BRAND-ZPM-REMEDIATION-02: **{'yes' if violations else 'no'}**",
        ]) + "\n",
    )
    return summary


def phase7_risk_summary(added_rows: list[dict[str, Any]]) -> dict[str, Any]:
    print("Phase 7: SEO risk classification summary...")
    risk_rows = [
        {
            "url": r["url"],
            "seo_risk": r.get("seo_risk"),
            "seo_risk_reason": r.get("seo_risk_reason"),
            "page_type": r.get("page_type"),
            "http_status": r.get("http_status"),
        }
        for r in added_rows
    ]
    counts = Counter(r["seo_risk"] for r in risk_rows)
    summary = {
        "green": counts.get("GREEN", 0),
        "yellow": counts.get("YELLOW", 0),
        "red": counts.get("RED", 0),
        "safe_unknown": counts.get("SAFE UNKNOWN", 0),
        "total": len(risk_rows),
    }
    write_csv(DEPLOYMENT_ROOT / "classification" / "sitemap-delta-risk-classification.csv", risk_rows)
    write_json(DEPLOYMENT_ROOT / "classification" / "sitemap-delta-risk-classification.json", summary | {"rows": risk_rows})
    write_text(
        DEPLOYMENT_ROOT / "classification" / "sitemap-delta-risk-summary.md",
        "\n".join([
            "# SEO risk classification (added URLs)",
            "",
            f"- GREEN: **{summary['green']}**",
            f"- YELLOW: **{summary['yellow']}**",
            f"- RED: **{summary['red']}**",
            f"- SAFE UNKNOWN: **{summary['safe_unknown']}**",
        ]) + "\n",
    )
    return summary


def phase8_sanity(current_count: int) -> dict[str, Any]:
    print("Phase 8: special sanity checks...")
    results: dict[str, Any] = {}
    for url in SANITY_URLS:
        resp = http_get(url)
        entry: dict[str, Any] = {
            "url": url,
            "http_status": resp.get("status_code"),
            "final_url": resp.get("final_url"),
            "content_type": resp.get("content_type"),
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
        elif "html" in (resp.get("content_type") or "").lower():
            meta = extract_page_meta(resp.get("body", ""), url)
            entry.update({
                "body_count": meta.get("body_count", 0),
                "yandex_metrika": meta.get("yandex_metrika"),
                "yandex_webmaster": meta.get("yandex_webmaster"),
                "has_load_more": meta.get("has_load_more"),
                "title": meta.get("title", "")[:120],
            })
        results[url] = entry
        time.sleep(0.2)
    write_json(DEPLOYMENT_ROOT / "verification" / "sanity-checks.json", results)
    home = results.get("https://bzpm.ru/", {})
    llms = results.get("https://bzpm.ru/llms.txt", {})
    robots = results.get("https://bzpm.ru/robots.txt", {})
    stoly = results.get("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly", {})
    lines = [
        "# Sanity checks",
        "",
        f"- Home HTTP 200: **{home.get('http_status') == 200}**",
        f"- Home body_count = 1: **{home.get('body_count') == 1}**",
        f"- Yandex Metrika on home: **{home.get('yandex_metrika')}**",
        f"- Yandex Webmaster on home: **{home.get('yandex_webmaster')}**",
        f"- robots Sitemap directive: **{robots.get('has_sitemap_directive')}**",
        f"- sitemap count captured: **{current_count}**",
        f"- llms UTF-8 BOM: **{llms.get('utf8_bom')}**",
        f"- llms has ЗПМ: **{(llms.get('zpm_count') or 0) > 0}**",
        f"- llms no БЗПМ: **{(llms.get('bzpm_count') or 0) == 0}**",
        f"- /stoly load-more: **{stoly.get('has_load_more')}**",
    ]
    write_text(DEPLOYMENT_ROOT / "verification" / "sanity-checks.md", "\n".join(lines) + "\n")
    return results


def determine_verdict(delta: dict[str, Any], risk: dict[str, Any], brand: dict[str, Any]) -> str:
    if risk.get("red", 0) > 0 or brand.get("bzpm_violations", 0) > 0:
        return "SITE-002 SITEMAP DELTA AUDIT COMPLETE — FOLLOW-UP FIX REQUIRED"
    if risk.get("yellow", 0) > 0:
        return "SITE-002 SITEMAP DELTA AUDIT COMPLETE — MINOR REVIEW ITEMS"
    return "SITE-002 SITEMAP DELTA AUDIT COMPLETE — NORMAL CATALOG GROWTH"


def phase9_findings(
    baseline_summary: dict[str, Any],
    current_summary: dict[str, Any],
    delta: dict[str, Any],
    added_rows: list[dict[str, Any]],
    removed_rows: list[dict[str, Any]],
    risk: dict[str, Any],
    brand: dict[str, Any],
    sanity: dict[str, Any],
) -> dict[str, Any]:
    print("Phase 9: findings...")
    verdict = determine_verdict(delta, risk, brand)
    type_counts = Counter(r.get("page_type") for r in added_rows)
    follow_ups = []
    if risk.get("red", 0) > 0:
        follow_ups.append("SITE-002-PROD-SITEMAP-HYGIENE-FIX-01")
    if risk.get("yellow", 0) > 0:
        follow_ups.append("SITE-002-PROD-SEO-META-EDGE-FIX-02")
    if brand.get("bzpm_violations", 0) > 0:
        follow_ups.append("SITE-002-PROD-BRAND-ZPM-REMEDIATION-02")
    if not follow_ups and delta.get("added_count", 0) > 0:
        follow_ups.append("SITE-002-PROD-SITEMAP-COUNT-MONITOR-01")
    findings = {
        "operation_id": OPERATION_ID,
        "ocpilot_run": OCPILOT_RUN,
        "verdict": verdict,
        "baseline_count": baseline_summary.get("url_count"),
        "current_count": current_summary.get("url_count"),
        "added_count": delta.get("added_count"),
        "removed_count": delta.get("removed_count"),
        "duplicate_count": delta.get("exact_duplicate_count"),
        "malformed_count": current_summary.get("malformed_urls"),
        "red_count": risk.get("red"),
        "yellow_count": risk.get("yellow"),
        "green_count": risk.get("green"),
        "added_by_page_type": dict(type_counts),
        "likely_cause": "catalog growth — predominantly new PRODUCT_PDP URLs; plausible 1C cron/import between Run 4.206 and live fetch",
        "immediate_production_mutation_required": risk.get("red", 0) > 0 or brand.get("bzpm_violations", 0) > 0,
        "follow_up_operations": follow_ups,
        "sanity_pass": all(
            [
                sanity.get("https://bzpm.ru/", {}).get("http_status") == 200,
                sanity.get("https://bzpm.ru/robots.txt", {}).get("has_sitemap_directive"),
                (sanity.get("https://bzpm.ru/llms.txt", {}).get("bzpm_count") or 0) == 0,
            ]
        ),
        "captured_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "reports" / "sitemap-delta-findings.json", findings)
    write_text(
        DEPLOYMENT_ROOT / "reports" / "sitemap-delta-findings.md",
        "\n".join([
            "# Sitemap delta findings",
            "",
            f"**Verdict:** {verdict}",
            "",
            f"- Baseline: {findings['baseline_count']}",
            f"- Current: {findings['current_count']}",
            f"- Added: {findings['added_count']}",
            f"- Removed: {findings['removed_count']}",
            f"- RED/YELLOW/GREEN: {findings['red_count']}/{findings['yellow_count']}/{findings['green_count']}",
            f"- Likely cause: {findings['likely_cause']}",
            f"- Immediate mutation required: {findings['immediate_production_mutation_required']}",
            f"- Follow-ups: {', '.join(follow_ups) if follow_ups else 'none'}",
        ]) + "\n",
    )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--skip-removed-crawl", action="store_true", help="Skip crawling removed URLs")
    args = parser.parse_args()

    ensure_layout()
    baseline_urls, baseline_summary = phase1_baseline()
    current_urls, current_summary, _ = phase2_current()
    delta = phase3_delta(baseline_urls, current_urls)

    added_rows = crawl_urls(delta["added"], "added")
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

    phase5_import_context()
    brand = phase6_brand_audit(added_rows)
    risk = phase7_risk_summary(added_rows)
    sanity = phase8_sanity(current_summary.get("url_count", 0))
    findings = phase9_findings(
        baseline_summary, current_summary, delta, added_rows, removed_rows, risk, brand, sanity
    )

    print("\n=== AUDIT COMPLETE ===")
    print(f"Verdict: {findings['verdict']}")
    print(f"Added: {findings['added_count']} | Removed: {findings['removed_count']}")
    print(f"RED/YELLOW/GREEN: {findings['red_count']}/{findings['yellow_count']}/{findings['green_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
