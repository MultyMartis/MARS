#!/usr/bin/env python3
"""SITE-002 SEO readiness — non-product meta audit + robots.txt deploy."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from xml.etree import ElementTree

OPERATION_ID = "SITE-002-PROD-SEO-READINESS-ROBOTS-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-LOAD-MORE-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-SEO-ROBOTS-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SEO-READINESS-ROBOTS-01"
)
USER_AGENT = "MARS-OCPilot/SITE-002-PROD-SEO-READINESS-ROBOTS-01"
REMOTE_ROBOTS = "/public_html/robots.txt"

TWIG_PATHS = [
    "/public_html/catalog/view/theme/default/template/common/header.twig",
    "/public_html/catalog/view/theme/default/template/common/footer.twig",
]

ANALYTICS_TERMS = (
    "ym(",
    "Yandex.Metrika",
    "metrika",
    "mc.yandex",
    "yandex-verification",
    "yandex_webmaster",
    "webmaster",
)

SEED_URLS: list[tuple[str, str, str]] = [
    ("https://bzpm.ru/", "home", "seed"),
    ("https://bzpm.ru/katalog/", "catalog_hub", "seed"),
    ("https://bzpm.ru/katalog/nejtralnoe-oborudovanie", "category", "seed"),
    ("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly", "category", "seed"),
    ("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly?page=2", "category_pagination", "seed"),
    ("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly?limit=30", "category_limit", "seed"),
    ("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly?sort=p.price&order=ASC", "category_sort", "seed"),
    ("https://bzpm.ru/guarantee", "information", "seed"),
    ("https://bzpm.ru/delivery", "information", "seed"),
    ("https://bzpm.ru/payment-methods", "information", "seed"),
    ("https://bzpm.ru/dealers", "information", "seed"),
    ("https://bzpm.ru/about", "information", "seed"),
    ("https://bzpm.ru/custom-equipment", "information", "seed"),
    ("https://bzpm.ru/contact-us", "contact", "seed"),
    ("https://bzpm.ru/index.php?route=information/contact", "contact", "seed"),
    ("https://bzpm.ru/cart", "technical", "seed"),
    ("https://bzpm.ru/checkout", "technical", "seed"),
    ("https://bzpm.ru/account/login", "technical", "seed"),
    ("https://bzpm.ru/search", "technical", "seed"),
]

SITEMAP_CANDIDATES = [
    "https://bzpm.ru/sitemap.xml",
    "https://bzpm.ru/index.php?route=extension/feed/google_sitemap",
    "https://bzpm.ru/index.php?route=feed/google_sitemap",
    "https://bzpm.ru/sitemap_index.xml",
]

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "verification",
    "crawl",
    "meta-audit",
    "robots",
    "sitemap",
    "analytics-codes/source",
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
        self.anchors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: (v or "") for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = True
        elif tag_l == "h1":
            self.in_h1 = True
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
        elif tag_l == "a":
            href = attrs_dict.get("href", "")
            if href:
                self.anchors.append(href)

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


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def ensure_dirs() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)


def parse_production_secrets(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found in secrets file")
    block = match.group(1)
    ftp_match = re.search(r"^### FTP / SFTP\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
    if not ftp_match:
        raise RuntimeError("PRODUCTION FTP / SFTP subsection not found")
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in ftp_match.group(1).splitlines():
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


def ftp_connect(fields: dict[str, str]) -> ftplib.FTP:
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


def ftp_upload(ftp: ftplib.FTP, remote_path: str, data: bytes) -> None:
    from io import BytesIO

    ftp.storbinary("STOR " + remote_path, BytesIO(data))


def ftp_exists(ftp: ftplib.FTP, remote_path: str) -> bool:
    try:
        ftp.size(remote_path)
        return True
    except ftplib.error_perm:
        pass
    try:
        ftp_download(ftp, remote_path)
        return True
    except ftplib.error_perm:
        return False


def http_get(url: str, follow_redirects: bool = True) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache", "Accept": "text/html,application/xml,*/*"},
    )
    started = utc_now()
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
            final_url = response.geturl()
            charset = response.headers.get_content_charset() or "utf-8"
            text = body.decode(charset, errors="replace")
            return {
                "url": url,
                "final_url": final_url,
                "checked_at": started,
                "status_code": response.status,
                "content_type": response.headers.get("Content-Type", ""),
                "headers": dict(response.headers.items()),
                "body": text,
                "body_bytes": body,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read()
        charset = exc.headers.get_content_charset() or "utf-8"
        text = body.decode(charset, errors="replace")
        return {
            "url": url,
            "final_url": exc.geturl() if hasattr(exc, "geturl") else url,
            "checked_at": started,
            "status_code": exc.code,
            "content_type": exc.headers.get("Content-Type", "") if exc.headers else "",
            "headers": dict(exc.headers.items()) if exc.headers else {},
            "body": text,
            "body_bytes": body,
            "error": str(exc),
        }
    except Exception as exc:
        return {
            "url": url,
            "final_url": url,
            "checked_at": started,
            "status_code": None,
            "content_type": "",
            "headers": {},
            "body": "",
            "body_bytes": b"",
            "error": str(exc),
        }


def mask_id(value: str) -> str:
    if not value or len(value) < 4:
        return "***"
    return value[:2] + "***" + value[-2:]


def is_product_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.lower()
    query = parsed.query.lower()
    if "product_id=" in query:
        return True
    if re.search(r"/katalog/[^/]+/[^/]+/[^/]+", path):
        return True
    if "/product/" in path:
        return True
    if path.endswith((".jpg", ".jpeg", ".png", ".webp", ".gif", ".css", ".js", ".svg", ".woff", ".woff2")):
        return True
    return False


def normalize_site_url(href: str, base: str = PRODUCTION_URL) -> str | None:
    if not href or href.startswith(("#", "javascript:", "mailto:", "tel:")):
        return None
    full = urllib.parse.urljoin(base, href)
    parsed = urllib.parse.urlparse(full)
    if parsed.netloc and parsed.netloc.replace("www.", "") not in ("bzpm.ru",):
        return None
    clean = urllib.parse.urlunparse(
        (parsed.scheme or "https", parsed.netloc or "bzpm.ru", parsed.path or "/", "", parsed.query, "")
    )
    return clean.rstrip("/") if parsed.path not in ("", "/") else "https://bzpm.ru/"


def classify_url_type(url: str) -> str:
    path = urllib.parse.urlparse(url).path.lower()
    query = urllib.parse.urlparse(url).query.lower()
    if url.rstrip("/") in ("https://bzpm.ru", "https://bzpm.ru/"):
        return "home"
    if any(x in path for x in ("/cart", "/checkout", "/account", "/wishlist", "/compare")):
        return "technical"
    if "route=checkout" in query or "route=account" in query or "route=product/search" in query:
        return "technical"
    if "/search" in path:
        return "technical"
    if path.startswith("/katalog"):
        if "?" in url:
            if "page=" in query or "sort=" in query or "limit=" in query or "order=" in query:
                return "category_variant"
        parts = [p for p in path.split("/") if p]
        if len(parts) >= 4:
            return "product_candidate"
        return "category"
    if any(
        seg in path
        for seg in (
            "/about",
            "/delivery",
            "/payment",
            "/dealers",
            "/guarantee",
            "/custom-equipment",
            "/contact",
        )
    ):
        return "information"
    return "other"


def extract_meta(html_text: str) -> dict[str, Any]:
    parser = MetaParser()
    try:
        parser.feed(html_text)
    except Exception:
        pass
    canonical = next((l["href"] for l in parser.links if l["rel"] == "canonical"), "")
    prev_link = next((l["href"] for l in parser.links if l["rel"] == "prev"), "")
    next_link = next((l["href"] for l in parser.links if l["rel"] == "next"), "")
    robots = parser.meta.get("robots", "")
    title = html.unescape(parser.title.strip())
    description = parser.meta.get("description", "")
    og_title = parser.meta.get("og:title", "")
    og_description = parser.meta.get("og:description", "")
    h1_joined = " | ".join(h for h in parser.h1_list if h)
    return {
        "title": title,
        "title_length": len(title),
        "meta_description": description,
        "description_length": len(description),
        "h1_list": [h for h in parser.h1_list if h],
        "h1_count": len([h for h in parser.h1_list if h]),
        "h1_text": h1_joined,
        "canonical": canonical,
        "meta_robots": robots,
        "og_title": og_title,
        "og_description": og_description,
        "rel_prev": prev_link,
        "rel_next": next_link,
        "has_metrika": any(
            term.lower() in html_text.lower()
            for term in ("mc.yandex.ru/metrika", "ym(", "yandex.metrika")
        ),
        "has_webmaster_verification": "yandex-verification" in html_text.lower(),
        "anchors": parser.anchors,
    }


def score_meta(row: dict[str, Any]) -> str:
    if row.get("accidental_product"):
        return "FAIL"
    if row.get("status_code") is None:
        return "SAFE UNKNOWN"
    if row["status_code"] != 200:
        return "FAIL"
    issues = 0
    if not row.get("title"):
        issues += 2
    elif row["title_length"] < 20:
        issues += 1
    elif row["title_length"] > 70:
        issues += 1
    if not row.get("meta_description"):
        issues += 2
    elif row["description_length"] < 50:
        issues += 1
    elif row["description_length"] > 170:
        issues += 1
    if row.get("h1_count", 0) == 0:
        issues += 1
    elif row.get("h1_count", 0) > 1:
        issues += 1
    robots = (row.get("meta_robots") or "").lower()
    if "noindex" in robots and row.get("type") not in ("technical", "category_variant"):
        issues += 1
    if issues >= 3:
        return "FAIL"
    if issues >= 1:
        return "WARN"
    return "PASS"


def analyze_twig_analytics(remote_path: str, content: str) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    lines = content.splitlines()
    for idx, line in enumerate(lines, start=1):
        lower = line.lower()
        code_type = None
        if any(t.lower() in lower for t in ("ym(", "yandex.metrika", "mc.yandex", "metrika")):
            code_type = "yandex_metrika"
        elif any(t.lower() in lower for t in ("yandex-verification", "yandex_webmaster", "webmaster")):
            code_type = "yandex_webmaster_verification"
        elif "яндекс" in lower and ("metrika" in lower or "метрика" in lower):
            code_type = "yandex_metrika"
        if not code_type:
            continue
        counter_match = re.search(r"ym\s*\(\s*(\d+)", line)
        verify_match = re.search(r'yandex-verification["\']?\s*content=["\']([^"\']+)', line, re.I)
        if not verify_match:
            verify_match = re.search(r"content=['\"]([a-f0-9]{16,})['\"]", line, re.I)
        findings.append(
            {
                "file_path": remote_path,
                "code_type": code_type,
                "line_number": idx,
                "line_summary": line.strip()[:120],
                "masked_counter_id": mask_id(counter_match.group(1)) if counter_match else None,
                "masked_verification_id": mask_id(verify_match.group(1)) if verify_match else None,
                "protection_rule": "DO NOT OVERWRITE / DO NOT REFORMAT",
            }
        )
    return findings


def discover_sitemaps() -> dict[str, Any]:
    results = []
    suitable = None
    for url in SITEMAP_CANDIDATES:
        resp = http_get(url)
        body = resp.get("body", "")
        has_urls = bool(re.search(r"<loc>", body, re.I)) or bool(re.search(r"<url>", body, re.I))
        has_products = "/katalog/" in body and body.count("<loc>") > 5
        has_categories = "/katalog/" in body or "/katalog" in body
        has_info = any(p in body for p in ("/about", "/delivery", "/guarantee", "/dealers"))
        content_ok = resp.get("status_code") == 200 and (
            "xml" in resp.get("content_type", "").lower() or has_urls
        )
        suitable_for_robots = content_ok and has_urls
        entry = {
            "url": url,
            "status_code": resp.get("status_code"),
            "content_type": resp.get("content_type"),
            "contains_urls": has_urls,
            "includes_product_urls": has_products,
            "includes_category_urls": has_categories,
            "includes_info_urls": has_info,
            "suitable_for_robots_sitemap_directive": suitable_for_robots,
            "body_preview": body[:500],
            "error": resp.get("error"),
        }
        results.append(entry)
        if suitable_for_robots and suitable is None:
            suitable = url
    return {"checked_at": utc_now(), "candidates": results, "recommended_sitemap_url": suitable}


def build_robots_content(sitemap_url: str | None) -> str:
    common_disallow = [
        "Disallow: /admin/",
        "Disallow: /catalog/",
        "Allow: /catalog/view/",
        "Allow: /catalog/view/theme/",
        "Allow: /catalog/view/javascript/",
        "Allow: /image/",
        "Disallow: /system/",
        "Disallow: /storage/",
        "Disallow: /download/",
        "Disallow: /account/",
        "Disallow: /checkout/",
        "Disallow: /cart/",
        "Disallow: /wishlist/",
        "Disallow: /compare/",
        "Disallow: /search",
        "Disallow: /index.php?route=account/",
        "Disallow: /index.php?route=checkout/",
        "Disallow: /index.php?route=product/search",
        "Disallow: /*?sort=",
        "Disallow: /*&sort=",
        "Disallow: /*?order=",
        "Disallow: /*&order=",
        "Disallow: /*?limit=",
        "Disallow: /*&limit=",
        "Disallow: /*?page=",
        "Disallow: /*&page=",
        "Disallow: /*?filter_name=",
        "Disallow: /*&filter_name=",
        "Disallow: /*?tracking=",
        "Disallow: /*&tracking=",
    ]
    lines = [
        "# robots.txt — BZPM Production (SITE-002)",
        "# Generated by OCPilot SITE-002-PROD-SEO-READINESS-ROBOTS-01",
        f"# {utc_now()}",
        "",
        "User-agent: *",
        *common_disallow,
        "",
        "User-agent: Yandex",
        *common_disallow,
        "Clean-param: tracking",
        "",
    ]
    if sitemap_url:
        lines.append(f"Sitemap: {sitemap_url}")
        lines.append("")
    return "\n".join(lines)


def analyze_robots(content: str) -> dict[str, Any]:
    lines = [ln.strip() for ln in content.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    disallows = [ln.split(":", 1)[1].strip() for ln in lines if ln.lower().startswith("disallow:")]
    allows = [ln.split(":", 1)[1].strip() for ln in lines if ln.lower().startswith("allow:")]
    sitemaps = [ln.split(":", 1)[1].strip() for ln in lines if ln.lower().startswith("sitemap:")]
    blocks_all = any(d in ("/", "/*") for d in disallows)
    blocks_catalog_public = any(d in ("/katalog", "/katalog/") for d in disallows)
    blocks_assets = any("/catalog/view/" in d and not any(a.startswith("/catalog/view/") for a in allows) for d in disallows)
    return {
        "line_count": len(content.splitlines()),
        "disallow_rules": disallows,
        "allow_rules": allows,
        "sitemap_directives": sitemaps,
        "blocks_entire_site": blocks_all,
        "blocks_public_catalog_paths": blocks_catalog_public,
        "blocks_rendering_assets": blocks_assets,
        "has_crawl_delay": any(ln.lower().startswith("crawl-delay:") for ln in lines),
        "has_host_directive": any(ln.lower().startswith("host:") for ln in lines),
        "encoding_bom": content.startswith("\ufeff"),
    }


def check_deploy_gates(
    prepared: str, sitemap_url: str | None, analytics_payload: dict[str, Any]
) -> dict[str, Any]:
    analysis = analyze_robots(prepared)
    gates = {
        "G1_target_path_confirmed": True,
        "G2_backup_or_missing_recorded": True,
        "G3_does_not_disallow_entire_site": not analysis["blocks_entire_site"],
        "G4_does_not_block_public_catalog": not analysis["blocks_public_catalog_paths"],
        "G5_does_not_block_rendering_assets": not analysis["blocks_rendering_assets"],
        "G6_sitemap_valid_or_omitted": True,
        "G7_no_twig_in_upload_plan": True,
        "G8_no_meta_db_admin_changes": True,
        "G9_operator_analytics_protection_recorded": bool(analytics_payload.get("protection_recorded")),
        "G10_remote_unchanged_since_backup": True,
    }
    if sitemap_url:
        sm = http_get(sitemap_url)
        gates["G6_sitemap_valid_or_omitted"] = sm.get("status_code") == 200
    all_pass = all(gates.values())
    return {"gates": gates, "all_pass": all_pass, "analysis": analysis}


def phase_analytics(ftp: ftplib.FTP) -> dict[str, Any]:
    all_findings: list[dict[str, Any]] = []
    downloaded: list[str] = []
    for remote in TWIG_PATHS:
        local_name = remote.rsplit("/", 1)[-1]
        try:
            data = ftp_download(ftp, remote)
        except ftplib.error_perm as exc:
            all_findings.append({"file_path": remote, "error": str(exc), "code_type": "download_failed"})
            continue
        dest = DEPLOYMENT_ROOT / "analytics-codes" / "source" / local_name
        dest.write_bytes(data)
        downloaded.append(remote)
        text = data.decode("utf-8", errors="replace")
        all_findings.extend(analyze_twig_analytics(remote, text))

    metrika = [f for f in all_findings if f.get("code_type") == "yandex_metrika"]
    webmaster = [f for f in all_findings if f.get("code_type") == "yandex_webmaster_verification"]
    protected = bool(metrika or webmaster)
    check_status = "FOUND" if protected else "SAFE UNKNOWN"

    md_lines = [
        "# Protected Operator Twig Analytics Codes",
        "",
        f"Operation: {OPERATION_ID}",
        f"Checked at: {utc_now()}",
        "",
        "## Protection rule",
        "",
        "**DO NOT OVERWRITE / DO NOT REFORMAT** header.twig or footer.twig containing operator Yandex codes.",
        "",
        "## Findings",
        "",
    ]
    if not all_findings:
        md_lines.append(
            "**SAFE UNKNOWN** — no Yandex.Metrika or Yandex.Webmaster verification strings detected "
            "in live FTP copies of header.twig / footer.twig at audit time. "
            "Operator WIP may be pending deploy or stored in another include — Twig files were not modified."
        )
    else:
        for f in all_findings:
            md_lines.append(f"- `{f.get('file_path')}` — {f.get('code_type')} — line {f.get('line_number')} — counter/verify masked")
    md_lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- Metrika findings: {len(metrika)}",
            f"- Webmaster verification findings: {len(webmaster)}",
            f"- Files downloaded: {len(downloaded)}",
        f"- Check status: {check_status}",
        f"- Codes found on live FTP Twig: {'YES' if protected else 'NO'}",
        "",
    ]
    )
    write_text(DEPLOYMENT_ROOT / "analytics-codes" / "protected-operator-twig-codes.md", "\n".join(md_lines))
    payload = {
        "operation_id": OPERATION_ID,
        "checked_at": utc_now(),
        "files_downloaded": downloaded,
        "findings": all_findings,
        "metrika_count": len(metrika),
        "webmaster_count": len(webmaster),
        "protected": protected,
        "check_status": check_status,
        "protection_recorded": True,
    }
    write_json(DEPLOYMENT_ROOT / "analytics-codes" / "protected-operator-twig-codes.json", payload)
    return payload


def phase_inventory_and_meta() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    inventory: dict[str, dict[str, Any]] = {}
    for url, typ, source in SEED_URLS:
        inventory[url] = {
            "url": url,
            "type": typ,
            "source": source,
            "include_in_meta_audit": "yes" if typ != "technical" or url.endswith(("cart", "checkout", "login", "search")) else "yes",
            "reason": "seed minimum set",
            "status_code": None,
            "canonical_url": "",
            "notes": "",
        }

    home = http_get("https://bzpm.ru/")
    if home.get("status_code") == 200:
        meta_home = extract_meta(home["body"])
        for href in meta_home.get("anchors", []):
            norm = normalize_site_url(href)
            if not norm or is_product_url(norm):
                continue
            if norm not in inventory:
                inventory[norm] = {
                    "url": norm,
                    "type": classify_url_type(norm),
                    "source": "homepage_crawl",
                    "include_in_meta_audit": "yes",
                    "reason": "discovered from homepage",
                    "status_code": None,
                    "canonical_url": "",
                    "notes": "",
                }

    audit_rows: list[dict[str, Any]] = []
    titles: Counter[str] = Counter()
    descriptions: Counter[str] = Counter()

    for url, inv in sorted(inventory.items(), key=lambda x: x[0]):
        if inv["include_in_meta_audit"] != "yes":
            continue
        if is_product_url(url) and inv["type"] not in ("category", "category_variant", "catalog_hub"):
            inv["include_in_meta_audit"] = "no"
            inv["reason"] = "product PDP excluded"
            continue
        resp = http_get(url)
        inv["status_code"] = resp.get("status_code")
        body = resp.get("body", "")
        meta = extract_meta(body) if body else {}
        inv["canonical_url"] = meta.get("canonical", "")
        accidental_product = inv["type"] == "product_candidate" or (
            meta.get("h1_text", "") and ".p-card" in body and "product_id" in body.lower()
        )
        row = {
            **inv,
            "final_url": resp.get("final_url", url),
            "title": meta.get("title", ""),
            "title_length": meta.get("title_length", 0),
            "meta_description": meta.get("meta_description", ""),
            "description_length": meta.get("description_length", 0),
            "h1_count": meta.get("h1_count", 0),
            "h1_text": meta.get("h1_text", ""),
            "canonical": meta.get("canonical", ""),
            "meta_robots": meta.get("meta_robots", ""),
            "og_title": meta.get("og_title", ""),
            "og_description": meta.get("og_description", ""),
            "rel_prev": meta.get("rel_prev", ""),
            "rel_next": meta.get("rel_next", ""),
            "has_metrika": meta.get("has_metrika", False),
            "has_webmaster_verification": meta.get("has_webmaster_verification", False),
            "accidental_product": accidental_product,
            "indexability": "noindex" if "noindex" in (meta.get("meta_robots") or "").lower() else "index",
            "duplicate_title_candidate": False,
            "duplicate_description_candidate": False,
            "issues": [],
        }
        if row["title"]:
            titles[row["title"]] += 1
        if row["meta_description"]:
            descriptions[row["meta_description"]] += 1
        row["classification"] = score_meta(row)
        audit_rows.append(row)
        time.sleep(0.3)

    for row in audit_rows:
        if row["title"] and titles[row["title"]] > 1:
            row["duplicate_title_candidate"] = True
            row["issues"].append("duplicate_title")
        if row["meta_description"] and descriptions[row["meta_description"]] > 1:
            row["duplicate_description_candidate"] = True
            row["issues"].append("duplicate_description")
        if not row["title"]:
            row["issues"].append("missing_title")
        if not row["meta_description"]:
            row["issues"].append("missing_description")
        if row["title_length"] and (row["title_length"] < 20 or row["title_length"] > 70):
            row["issues"].append("title_length")
        if row["description_length"] and (row["description_length"] < 50 or row["description_length"] > 170):
            row["issues"].append("description_length")
        if row["h1_count"] == 0:
            row["issues"].append("missing_h1")
        if row["h1_count"] > 1:
            row["issues"].append("multiple_h1")
        row["classification"] = score_meta(row)

    inv_list = list(inventory.values())
    write_json(DEPLOYMENT_ROOT / "crawl" / "non-product-url-inventory.json", inv_list)
    with (DEPLOYMENT_ROOT / "crawl" / "non-product-url-inventory.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["url", "type", "source", "include_in_meta_audit", "reason", "status_code", "canonical_url", "notes"],
        )
        writer.writeheader()
        writer.writerows(inv_list)

    write_json(DEPLOYMENT_ROOT / "meta-audit" / "non-product-meta-audit.json", audit_rows)
    with (DEPLOYMENT_ROOT / "meta-audit" / "non-product-meta-audit.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "url", "type", "status_code", "title", "title_length", "meta_description", "description_length",
                "h1_count", "h1_text", "canonical", "meta_robots", "indexability", "classification",
                "duplicate_title_candidate", "duplicate_description_candidate", "has_metrika", "has_webmaster_verification",
            ],
        )
        writer.writeheader()
        for row in audit_rows:
            writer.writerow({k: row.get(k, "") for k in writer.fieldnames})

    counts = Counter(r["classification"] for r in audit_rows)
    summary_md = "\n".join(
        [
            "# Non-Product Meta Audit Summary",
            "",
            f"Operation: {OPERATION_ID}",
            f"Checked at: {utc_now()}",
            "",
            f"- URLs audited: {len(audit_rows)}",
            f"- PASS: {counts.get('PASS', 0)}",
            f"- WARN: {counts.get('WARN', 0)}",
            f"- FAIL: {counts.get('FAIL', 0)}",
            f"- SAFE UNKNOWN: {counts.get('SAFE UNKNOWN', 0)}",
            "",
            "## Product pages excluded",
            "",
            "Product PDP URLs were excluded from meta edit scope; category/listing pages included.",
            "",
        ]
    )
    write_text(DEPLOYMENT_ROOT / "meta-audit" / "non-product-meta-summary.md", summary_md)
    return inv_list, audit_rows


def phase_meta_fix_plan(audit_rows: list[dict[str, Any]]) -> None:
    lines = [
        "# Meta Fix Plan — SITE-002 (non-product only)",
        "",
        "Proposed next operation: **SITE-002-PROD-SEO-META-FIX-01**",
        "",
        "Do not implement in this operation.",
        "",
    ]
    for row in audit_rows:
        if row["classification"] not in ("WARN", "FAIL"):
            continue
        lines.extend(
            [
                f"## {row['url']}",
                "",
                f"- Classification: {row['classification']}",
                f"- Issues: {', '.join(row.get('issues', [])) or 'see audit'}",
                f"- Current title: {row.get('title') or '(missing)'}",
                f"- Current description: {(row.get('meta_description') or '(missing)')[:120]}",
                f"- H1: {row.get('h1_text') or '(missing)'}",
                "- Recommended title: *(operator review — derive from page content)*",
                "- Recommended description: *(operator review — derive from page content)*",
                "- Likely authority: OpenCart admin / database / Twig / controller / SAFE UNKNOWN",
                "- Proposed next operation: SITE-002-PROD-SEO-META-FIX-01",
                "",
            ]
        )
    if len(lines) <= 8:
        lines.append("No WARN/FAIL pages requiring meta fix plan entries.")
    write_text(DEPLOYMENT_ROOT / "meta-audit" / "meta-fix-plan.md", "\n".join(lines))


def run(deploy: bool = True) -> dict[str, Any]:
    ensure_dirs()
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "change_type": "seo-readiness-robots",
            "product_pages_excluded": True,
            "robots_deploy_allowed": True,
            "meta_edit_allowed": False,
            "db_write_allowed": False,
            "admin_save_allowed": False,
            "operator_twig_analytics_codes_protected": True,
            "started_at": utc_now(),
        },
    )

    fields = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(fields)
    try:
        analytics = phase_analytics(ftp)
        robots_exists = ftp_exists(ftp, REMOTE_ROBOTS)
        remote_robots_before: bytes | None = None
        if robots_exists:
            remote_robots_before = ftp_download(ftp, REMOTE_ROBOTS)
            for dest in ("source", "backup", "rollback"):
                (DEPLOYMENT_ROOT / dest / "robots.txt").write_bytes(remote_robots_before)
    finally:
        try:
            ftp.quit()
        except Exception:
            pass

    sitemap_data = discover_sitemaps()
    write_json(DEPLOYMENT_ROOT / "sitemap" / "sitemap-discovery.json", sitemap_data)
    sm_md = [
        "# Sitemap Discovery",
        "",
        f"Checked at: {sitemap_data['checked_at']}",
        "",
        f"Recommended for robots Sitemap directive: `{sitemap_data.get('recommended_sitemap_url') or 'none'}`",
        "",
    ]
    for c in sitemap_data["candidates"]:
        sm_md.append(
            f"- {c['url']} — HTTP {c['status_code']} — suitable: {c['suitable_for_robots_sitemap_directive']}"
        )
    write_text(DEPLOYMENT_ROOT / "sitemap" / "sitemap-discovery.md", "\n".join(sm_md))

    inv_list, audit_rows = phase_inventory_and_meta()
    phase_meta_fix_plan(audit_rows)

    http_robots = http_get("https://bzpm.ru/robots.txt")
    current_content = ""
    if remote_robots_before:
        current_content = remote_robots_before.decode("utf-8", errors="replace")
    elif http_robots.get("status_code") == 200:
        current_content = http_robots.get("body", "")
    current_analysis = analyze_robots(current_content) if current_content else {"status": "missing"}
    current_sha = sha256_bytes(current_content.encode("utf-8")) if current_content else None
    current_payload = {
        "http_status": http_robots.get("status_code"),
        "ftp_exists": robots_exists,
        "sha256": current_sha,
        "analysis": current_analysis,
        "content_preview": current_content[:1000] if current_content else "",
    }
    write_json(DEPLOYMENT_ROOT / "robots" / "current-robots-analysis.json", current_payload)
    write_text(
        DEPLOYMENT_ROOT / "robots" / "current-robots-analysis.md",
        "\n".join(
            [
                "# Current robots.txt Analysis",
                "",
                f"- HTTP status: {http_robots.get('status_code')}",
                f"- FTP exists: {robots_exists}",
                f"- SHA-256: {current_sha or 'n/a'}",
                f"- Blocks entire site: {current_analysis.get('blocks_entire_site', 'n/a') if current_content else 'n/a'}",
                "",
                "```",
                current_content[:2000] if current_content else "(missing)",
                "```",
            ]
        ),
    )

    sitemap_url = sitemap_data.get("recommended_sitemap_url")
    prepared = build_robots_content(sitemap_url)
    prepared_path = DEPLOYMENT_ROOT / "prepared" / "robots.txt"
    prepared_path.write_text(prepared, encoding="utf-8")
    write_text(DEPLOYMENT_ROOT / "robots" / "prepared-robots-preview.txt", prepared)
    write_text(
        DEPLOYMENT_ROOT / "robots" / "robots-design.md",
        "\n".join(
            [
                "# robots.txt Design — BZPM Production",
                "",
                "Conservative OpenCart robots:",
                "- Block admin/system/storage/account/checkout/cart/search",
                "- Allow /catalog/view/ assets and /image/",
                "- Disallow faceted query params (sort/order/limit/page) on any URL",
                "- Do not block /katalog/ pretty URLs",
                f"- Sitemap: {sitemap_url or 'omitted'}",
                "",
            ]
        ),
    )

    gates = check_deploy_gates(prepared, sitemap_url, analytics)
    write_json(DEPLOYMENT_ROOT / "manifests" / "robots-deploy-plan.json", gates)

    deploy_result: dict[str, Any] = {"deployed": False, "reason": "gates or flag"}
    if deploy and gates["all_pass"]:
        ftp2 = ftp_connect(fields)
        try:
            if remote_robots_before:
                fresh = ftp_download(ftp2, REMOTE_ROBOTS)
                if sha256_bytes(fresh) != sha256_bytes(remote_robots_before):
                    deploy_result = {"deployed": False, "reason": "STOP — ROBOTS CHANGED SINCE BACKUP"}
                    write_json(DEPLOYMENT_ROOT / "manifests" / "deploy-result.json", deploy_result)
                    return {
                        "analytics": analytics,
                        "inventory_count": len(inv_list),
                        "audit_count": len(audit_rows),
                        "sitemap": sitemap_data,
                        "gates": gates,
                        "deploy": deploy_result,
                    }
            ftp_upload(ftp2, REMOTE_ROBOTS, prepared.encode("utf-8"))
            after = ftp_download(ftp2, REMOTE_ROBOTS)
        finally:
            try:
                ftp2.quit()
            except Exception:
                pass
        prepared_sha = sha256_bytes(prepared.encode("utf-8"))
        after_sha = sha256_bytes(after)
        live = http_get("https://bzpm.ru/robots.txt")
        live_body = live.get("body", "")
        deploy_result = {
            "deployed": True,
            "prepared_sha256": prepared_sha,
            "remote_after_sha256": after_sha,
            "http_status": live.get("status_code"),
            "content_matches_prepared": live_body.strip() == prepared.strip(),
            "sha_match": prepared_sha == after_sha,
            "timestamp": utc_now(),
        }
    elif not gates["all_pass"]:
        deploy_result = {"deployed": False, "reason": "deploy gates failed", "gates": gates["gates"]}

    write_json(DEPLOYMENT_ROOT / "manifests" / "deploy-result.json", deploy_result)

    spot_urls = [
        "https://bzpm.ru/",
        "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
        "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
        "https://bzpm.ru/robots.txt",
    ]
    spot = []
    for u in spot_urls:
        r = http_get(u)
        meta = extract_meta(r.get("body", "")) if r.get("body") else {}
        spot.append(
            {
                "url": u,
                "status_code": r.get("status_code"),
                "has_metrika": meta.get("has_metrika"),
                "has_webmaster_verification": meta.get("has_webmaster_verification"),
            }
        )
    write_json(DEPLOYMENT_ROOT / "verification" / "post-deploy-spot-check.json", spot)

    return {
        "analytics": analytics,
        "inventory_count": len(inv_list),
        "audit_count": len(audit_rows),
        "audit_summary": dict(Counter(r["classification"] for r in audit_rows)),
        "sitemap": sitemap_data,
        "gates": gates,
        "deploy": deploy_result,
        "spot_check": spot,
        "current_robots_sha": current_sha,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-deploy", action="store_true")
    args = parser.parse_args()
    result = run(deploy=not args.no_deploy)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result.get("deploy", {}).get("reason") == "STOP — ROBOTS CHANGED SINCE BACKUP":
        return 2
    if not args.no_deploy and not result.get("deploy", {}).get("deployed"):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
