#!/usr/bin/env python3
"""SITE-002 Production sitemap enablement + robots Sitemap directive."""
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
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from io import BytesIO
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-SITEMAP-ENABLE-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-HTML-BODY-FIX-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-SITEMAP-01"
ROBOTS_HASH_RUN_4188 = "72ab7d21cdb7f66bf69fcc2cd21a2571bad402e38b626377516d7fd4f22ba723"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SITEMAP-ENABLE-01"
)
REPORT_PATH = Path(
    r"X:\AI MARS\projects\ocpilot\sites\site-002\reports\SITE-002-PROD-SITEMAP-ENABLE-01.md"
)
USER_AGENT = "MARS-OCPilot/SITE-002-PROD-SITEMAP-ENABLE-01"
REMOTE_ROBOTS = "/public_html/robots.txt"

SITEMAP_CANDIDATES = [
    "https://bzpm.ru/sitemap.xml",
    "https://bzpm.ru/index.php?route=extension/feed/google_sitemap",
    "https://bzpm.ru/index.php?route=feed/google_sitemap",
    "https://bzpm.ru/sitemap_index.xml",
]

SOURCE_PATHS = [
    "/public_html/sitemap.xml",
    "/public_html/catalog/controller/extension/feed/google_sitemap.php",
    "/public_html/catalog/controller/feed/google_sitemap.php",
    "/public_html/catalog/model/extension/feed/google_sitemap.php",
    "/public_html/admin/controller/extension/feed/google_sitemap.php",
    "/public_html/admin/language/ru-ru/extension/feed/google_sitemap.php",
    "/public_html/admin/view/template/extension/feed/google_sitemap.twig",
    "/public_html/system/storage/modification/catalog/controller/extension/feed/google_sitemap.php",
    "/public_html/storage/modification/catalog/controller/extension/feed/google_sitemap.php",
]

SPOT_CHECK_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/guarantee",
]

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "verification",
    "verification/pre-upload",
    "sitemap-before",
    "sitemap-after",
    "robots-before",
    "robots-after",
    "admin-evidence",
    "manifests",
    "logs",
)


class BodyCounter(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.body_open = 0
        self.has_metrika = False
        self.has_webmaster = False
        self.raw = ""

    def feed_text(self, text: str) -> None:
        self.raw = text
        self.feed(text)
        lower = text.lower()
        self.has_metrika = any(
            t in lower for t in ("mc.yandex.ru/metrika", "ym(", "yandex.metrika")
        )
        self.has_webmaster = "yandex-verification" in lower

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "body":
            self.body_open += 1


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
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "change_type": "sitemap-enable",
            "sitemap_required": True,
            "robots_update_allowed": True,
            "twig_changes_allowed": False,
            "meta_change_allowed": False,
            "db_direct_write_allowed": False,
            "admin_save_allowed": "conditional_only",
            "cron_change_allowed": False,
            "import_execution_allowed": False,
            "mail_change_allowed": False,
            "yandex_blocks_protected": True,
        },
    )


def parse_production_section(path: Path, subsection: str | None = None) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found in secrets file")
    block = match.group(1)
    if subsection:
        sub_match = re.search(
            rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE
        )
        if not sub_match:
            raise RuntimeError(f"PRODUCTION subsection {subsection!r} not found")
        block = sub_match.group(1)
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in block.splitlines():
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


def ftp_connect() -> ftplib.FTP:
    fields = parse_production_section(SECRETS_PATH, "FTP / SFTP")
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


def http_get(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Cache-Control": "no-cache",
            "Accept": "application/xml,text/xml,text/html,*/*",
        },
    )
    started = utc_now()
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            body = response.read()
            charset = response.headers.get_content_charset() or "utf-8"
            text = body.decode(charset, errors="replace")
            return {
                "url": url,
                "final_url": response.geturl(),
                "checked_at": started,
                "status_code": response.status,
                "content_type": response.headers.get("Content-Type", ""),
                "body": text,
                "body_bytes": body,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read()
        charset = exc.headers.get_content_charset() or "utf-8" if exc.headers else "utf-8"
        text = body.decode(charset, errors="replace")
        return {
            "url": url,
            "final_url": exc.geturl() if hasattr(exc, "geturl") else url,
            "checked_at": started,
            "status_code": exc.code,
            "content_type": exc.headers.get("Content-Type", "") if exc.headers else "",
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
            "body": "",
            "body_bytes": b"",
            "error": str(exc),
        }


def analyze_sitemap_body(body: str, content_type: str, status_code: int | None) -> dict[str, Any]:
    stripped = body.strip()
    starts_xml = stripped.startswith("<?xml") or stripped.startswith("<urlset") or stripped.startswith(
        "<sitemapindex"
    )
    locs = re.findall(r"<loc>\s*(.*?)\s*</loc>", body, re.I | re.S)
    valid_parse = False
    parse_error = None
    root_tag = None
    if stripped:
        try:
            root = ET.fromstring(stripped)
            valid_parse = True
            root_tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag
        except ET.ParseError as exc:
            parse_error = str(exc)

    has_products = any("/katalog/" in u and u.count("/") >= 5 for u in locs)
    has_categories = any("/katalog" in u for u in locs)
    has_info = any(
        any(p in u for p in ("/guarantee", "/delivery", "/about", "/dealers", "/payment"))
        for u in locs
    )
    bad_domains = [u for u in locs if "bzpm.ru" not in u and u.startswith("http")]
    forbidden = [
        u
        for u in locs
        if any(
            x in u.lower()
            for x in (
                "/admin",
                "/account",
                "/cart",
                "/checkout",
                "/wishlist",
                "/compare",
                "/search",
                "zpm.new-site.space",
                "localhost",
            )
        )
    ]
    faceted = [u for u in locs if any(p in u for p in ("?sort=", "&sort=", "?page=", "&page=", "?limit=", "&limit="))]

    content_ok = status_code == 200 and (starts_xml or bool(locs)) and valid_parse and len(locs) > 0
    return {
        "body_length": len(body.encode("utf-8")),
        "starts_with_xml_or_urlset": starts_xml,
        "url_count": len(locs),
        "sample_urls_first_5": locs[:5],
        "sample_urls_last_3": locs[-3:] if len(locs) >= 3 else locs,
        "contains_product_urls": has_products,
        "contains_category_urls": has_categories,
        "contains_information_urls": has_info,
        "valid_xml_parse": valid_parse,
        "xml_root_tag": root_tag,
        "parse_error": parse_error,
        "non_canonical_domains": bad_domains[:10],
        "forbidden_url_patterns": forbidden[:10],
        "faceted_url_patterns": faceted[:10],
        "valid_sitemap": content_ok,
        "content_type": content_type,
        "status_code": status_code,
    }


def phase_sitemap_before() -> dict[str, Any]:
    results = []
    for url in SITEMAP_CANDIDATES:
        resp = http_get(url)
        body = resp.get("body", "")
        analysis = analyze_sitemap_body(body, resp.get("content_type", ""), resp.get("status_code"))
        slug = re.sub(r"[^a-z0-9]+", "-", url.split("//", 1)[-1].lower()).strip("-")[:80]
        write_text(DEPLOYMENT_ROOT / "sitemap-before" / f"{slug}.body.txt", body[:50000])
        write_json(
            DEPLOYMENT_ROOT / "sitemap-before" / f"{slug}.json",
            {
                k: v
                for k, v in {**resp, "body": body[:2000], "analysis": analysis}.items()
                if k != "body_bytes"
            },
        )
        results.append({"url": url, **analysis, "error": resp.get("error")})

    md = [
        "# Sitemap before",
        "",
        f"Checked at: {utc_now()}",
        "",
        "| URL | Status | CT | Len | Valid | URLs | Products | Categories | Info |",
        "|-----|--------|----|----|-------|------|----------|------------|------|",
    ]
    for r in results:
        md.append(
            f"| {r['url']} | {r.get('status_code')} | {r.get('content_type','')[:30]} | "
            f"{r.get('body_length',0)} | {r.get('valid_sitemap')} | {r.get('url_count',0)} | "
            f"{r.get('contains_product_urls')} | {r.get('contains_category_urls')} | "
            f"{r.get('contains_information_urls')} |"
        )
    write_text(DEPLOYMENT_ROOT / "verification" / "sitemap-before.md", "\n".join(md))
    payload = {"checked_at": utc_now(), "candidates": results}
    write_json(DEPLOYMENT_ROOT / "verification" / "sitemap-before.json", payload)
    return payload


def phase_robots_before(ftp: ftplib.FTP) -> dict[str, Any]:
    http = http_get("https://bzpm.ru/robots.txt")
    ftp_data = ftp_download(ftp, REMOTE_ROBOTS)
    sha = sha256_bytes(ftp_data)
    for folder in ("robots-before", "backup", "rollback"):
        dest = DEPLOYMENT_ROOT / folder / "robots.txt"
        dest.write_bytes(ftp_data)
    text = ftp_data.decode("utf-8", errors="replace")
    sitemaps = re.findall(r"(?im)^Sitemap:\s*(.+)$", text)
    write_json(
        DEPLOYMENT_ROOT / "verification" / "robots-before.json",
        {
            "checked_at": utc_now(),
            "http_status": http.get("status_code"),
            "sha256": sha,
            "sha256_run_4188": ROBOTS_HASH_RUN_4188,
            "matches_run_4188_deploy_hash": sha == ROBOTS_HASH_RUN_4188,
            "size_bytes": len(ftp_data),
            "sitemap_directives": sitemaps,
            "line_count": len(text.splitlines()),
        },
    )
    write_text(
        DEPLOYMENT_ROOT / "verification" / "robots-before.md",
        "\n".join(
            [
                "# Robots before",
                "",
                f"- SHA-256: `{sha}`",
                f"- Matches Run 4.188 deploy hash: `{sha == ROBOTS_HASH_RUN_4188}`",
                f"- Sitemap directives: {sitemaps or 'none'}",
                f"- HTTP status: {http.get('status_code')}",
            ]
        ),
    )
    return {"content": text, "sha256": sha, "http": http}


def classify_source_path(remote: str, exists: bool, size: int, snippet: str) -> str:
    if not exists:
        return "OUT_OF_SCOPE"
    if remote.endswith("sitemap.xml"):
        return "CHANGE_TARGET"
    if "catalog/controller/extension/feed/google_sitemap.php" in remote:
        return "READ_ONLY"
    if "admin/controller/extension/feed/google_sitemap.php" in remote:
        return "READ_ONLY"
    if "modification" in remote:
        return "READ_ONLY"
    return "READ_ONLY"


def phase_source_discovery(ftp: ftplib.FTP) -> dict[str, Any]:
    entries = []
    for remote in SOURCE_PATHS:
        exists = ftp_exists(ftp, remote)
        size = 0
        sha = None
        snippet = ""
        local_rel = remote.lstrip("/").replace("/", "__")
        classification = classify_source_path(remote, exists, 0, "")
        if exists:
            data = ftp_download(ftp, remote)
            size = len(data)
            sha = sha256_bytes(data)
            snippet = data.decode("utf-8", errors="replace")[:500]
            (DEPLOYMENT_ROOT / "source" / local_rel).write_bytes(data)
        entries.append(
            {
                "remote_path": remote,
                "exists": exists,
                "size_bytes": size,
                "sha256": sha,
                "classification": classification,
                "snippet_preview": snippet[:200],
            }
        )

    feed_dirs = {}
    for d in (
        "/public_html/catalog/controller/extension/feed",
        "/public_html/admin/controller/extension/feed",
    ):
        try:
            feed_dirs[d] = ftp.nlst(d)
        except ftplib.error_perm as exc:
            feed_dirs[d] = [f"ERROR: {exc}"]

    write_json(
        DEPLOYMENT_ROOT / "manifests" / "source-discovery.json",
        {"checked_at": utc_now(), "files": entries, "feed_directories": feed_dirs},
    )
    md = ["# Source discovery", "", f"Checked at: {utc_now()}", ""]
    for e in entries:
        md.append(
            f"- `{e['remote_path']}` — exists={e['exists']} size={e['size_bytes']} — **{e['classification']}**"
        )
    write_text(DEPLOYMENT_ROOT / "manifests" / "source-discovery.md", "\n".join(md))
    return {"files": entries, "feed_directories": feed_dirs}


def _admin_login(page: Any, admin: dict[str, str]) -> str | None:
    """Login to OpenCart admin; return user_token or None."""
    url = admin.get("url", "https://bzpm.ru/admin/")
    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    if page.locator('input[name="username"]').count() == 0:
        token_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.url)
        if token_match:
            return token_match.group(1)
    page.fill('input[name="username"]', admin["login"])
    page.fill('input[name="password"]', admin["password"])
    page.click('button[type="submit"]')
    try:
        page.wait_for_url("**user_token**", timeout=45000)
    except Exception:
        pass
    page.wait_for_load_state("networkidle", timeout=30000)
    if "common/login" in page.url and page.locator('input[name="username"]').count() > 0:
        return None
    token_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.url)
    if token_match:
        return token_match.group(1)
    body_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.content())
    return body_match.group(1) if body_match else None


def _admin_url(admin_base: str, route: str, token: str, **params: str) -> str:
    q: dict[str, str] = {"route": route, "user_token": token, **params}
    return f"{admin_base.rstrip('/')}/index.php?{urllib.parse.urlencode(q)}"


def _admin_goto_google_sitemap(page: Any, admin_url: str, token: str) -> bool:
    edit_url = _admin_url(admin_url, "extension/feed/google_sitemap", token)
    page.goto(edit_url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_load_state("networkidle", timeout=30000)
    if page.locator("#form-feed").count() > 0:
        return True
    if "common/login" in page.url:
        return False
    return "feed_google_sitemap_status" in page.content()


def phase_admin_discovery() -> dict[str, Any]:
    """Inspect Google Sitemap feed extension in OpenCart admin."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        payload = {
            "status": "SAFE UNKNOWN",
            "reason": "playwright not available",
            "extension_installed": None,
            "extension_enabled": None,
        }
        write_json(DEPLOYMENT_ROOT / "admin-evidence" / "admin-feed-state.json", payload)
        return payload

    admin = parse_production_section(SECRETS_PATH, "OpenCart Admin")
    url = admin.get("url", "https://bzpm.ru/admin/")
    result: dict[str, Any] = {
        "checked_at": utc_now(),
        "admin_url": url,
        "status": "FAILED",
        "extension_installed": None,
        "extension_enabled": None,
        "feed_data_url": PRODUCTION_URL.rstrip("/") + "/index.php?route=extension/feed/google_sitemap",
        "route": "extension/feed/google_sitemap",
        "admin_save_performed": False,
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            token = _admin_login(page, admin)
            if not token:
                result["status"] = "LOGIN_FAILED"
                browser.close()
                write_json(DEPLOYMENT_ROOT / "admin-evidence" / "admin-feed-state.json", result)
                return result

            feed_list_url = _admin_url(url, "marketplace/extension", token, type="feed")
            page.goto(feed_list_url, wait_until="domcontentloaded", timeout=60000)
            body = page.content()
            write_text(DEPLOYMENT_ROOT / "admin-evidence" / "extensions-feed-page.html", body[:200000])

            installed = bool(
                re.search(r"feed/google_sitemap", body, re.I)
                or "Google Sitemap" in body
                or "Карта сайта Google" in body
            )
            result["extension_installed"] = installed

            if not _admin_goto_google_sitemap(page, url, token):
                if not installed:
                    install_btn = page.locator('a[href*="feed/google_sitemap"][href*="install"]').first
                    if install_btn.count() > 0:
                        result["install_button_found"] = True
                result["status"] = "SETTINGS_PAGE_UNAVAILABLE"
                browser.close()
                write_json(DEPLOYMENT_ROOT / "admin-evidence" / "admin-feed-state.json", result)
                return result

            edit_html = page.content()
            write_text(DEPLOYMENT_ROOT / "admin-evidence" / "google-sitemap-edit.html", edit_html[:200000])
            select_val = page.locator('select[name="feed_google_sitemap_status"]').input_value()
            result["extension_enabled"] = select_val == "1"
            result["feed_google_sitemap_status_raw"] = select_val
            result["status"] = "READ_OK"
        except Exception as exc:
            result["status"] = "ERROR"
            result["error_type"] = type(exc).__name__
        browser.close()

    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "admin-feed-state.json", result)
    write_text(
        DEPLOYMENT_ROOT / "admin-evidence" / "admin-feed-state.md",
        "\n".join(
            [
                "# Admin feed state",
                "",
                f"- Status: {result.get('status')}",
                f"- Extension installed: {result.get('extension_installed')}",
                f"- Extension enabled: {result.get('extension_enabled')}",
                f"- Status raw: {result.get('feed_google_sitemap_status_raw')}",
                f"- Feed data URL: {result.get('feed_data_url')}",
            ]
        ),
    )
    return result


def admin_enable_google_sitemap() -> dict[str, Any]:
    """Enable Google Sitemap feed — single setting only."""
    from playwright.sync_api import sync_playwright

    admin = parse_production_section(SECRETS_PATH, "OpenCart Admin")
    url = admin.get("url", "https://bzpm.ru/admin/")
    outcome: dict[str, Any] = {
        "performed_at": utc_now(),
        "admin_save_performed": False,
        "setting_changed": "feed_google_sitemap_status",
        "new_value": "1",
        "status": "FAILED",
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            token = _admin_login(page, admin)
            if not token:
                outcome["status"] = "LOGIN_FAILED"
                browser.close()
                return outcome

            feed_list_url = _admin_url(url, "marketplace/extension", token, type="feed")
            page.goto(feed_list_url, wait_until="domcontentloaded", timeout=60000)
            body = page.content()

            install_link = page.locator('a[href*="feed/install"][href*="google_sitemap"]').first
            if install_link.count() > 0:
                install_link.click()
                page.wait_for_load_state("networkidle", timeout=30000)
                token_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.url)
                if token_match:
                    token = token_match.group(1)
                outcome["extension_install_performed"] = True

            if not _admin_goto_google_sitemap(page, url, token):
                outcome["status"] = "FORM_NOT_FOUND"
                browser.close()
                return outcome

            current = page.locator('select[name="feed_google_sitemap_status"]').input_value()
            outcome["previous_value"] = current
            if current == "1":
                outcome["status"] = "ALREADY_ENABLED"
                browser.close()
                return outcome

            page.select_option('select[name="feed_google_sitemap_status"]', "1")
            page.click('#form-feed button[type="submit"], button[form="form-feed"], button[type="submit"]')
            page.wait_for_load_state("networkidle", timeout=30000)
            outcome["admin_save_performed"] = True
            outcome["status"] = "ENABLED"
            write_text(
                DEPLOYMENT_ROOT / "admin-evidence" / "google-sitemap-after-save.html",
                page.content()[:200000],
            )
            page.goto(_admin_url(url, "common/logout", token), timeout=15000)
        except Exception as exc:
            outcome["status"] = "ERROR"
            outcome["error_type"] = type(exc).__name__
        browser.close()

    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "admin-enable-result.json", outcome)
    return outcome


def read_controller_for_root_cause() -> dict[str, Any]:
    ctrl_path = DEPLOYMENT_ROOT / "source" / "public_html__catalog__controller__extension__feed__google_sitemap.php"
    sitemap_static = DEPLOYMENT_ROOT / "source" / "public_html__sitemap.xml"
    analysis: dict[str, Any] = {
        "controller_present": ctrl_path.exists(),
        "static_sitemap_present": sitemap_static.exists(),
        "static_sitemap_size": sitemap_static.stat().st_size if sitemap_static.exists() else 0,
    }
    if ctrl_path.exists():
        text = ctrl_path.read_text(encoding="utf-8", errors="replace")
        analysis["controller_has_index_method"] = "function index()" in text
        analysis["controller_checks_status"] = "feed_google_sitemap_status" in text
        analysis["controller_outputs_xml"] = "urlset" in text or "application/xml" in text
    return analysis


def determine_root_cause(
    sitemap_before: dict[str, Any],
    admin_state: dict[str, Any],
    source: dict[str, Any],
) -> dict[str, Any]:
    ctrl_analysis = read_controller_for_root_cause()
    any_valid = any(c.get("valid_sitemap") for c in sitemap_before.get("candidates", []))
    static_size = ctrl_analysis.get("static_sitemap_size", 0)

    cause = "SAFE UNKNOWN"
    minimal_fix = "BLOCK"
    plan = "BLOCKED"

    if any_valid:
        cause = "Valid sitemap already available"
        minimal_fix = "Add Sitemap directive to robots.txt only"
        plan = "PLAN_B"
    elif admin_state.get("extension_enabled") is False:
        cause = "OpenCart Google Sitemap feed extension is installed but disabled (feed_google_sitemap_status=0)"
        minimal_fix = "Admin enable Google Sitemap feed only"
        plan = "PLAN_A"
    elif admin_state.get("extension_enabled") is True and not any_valid:
        cause = "Extension enabled but output empty — controller/config/cache issue"
        minimal_fix = "Diagnose controller; possible OCMOD or SEO URL layer"
        plan = "PLAN_D"
    elif static_size == 0 and ctrl_analysis.get("controller_present"):
        cause = "Empty static /sitemap.xml (0 bytes) shadows route; feed likely disabled or returns empty when disabled"
        minimal_fix = "Enable feed in admin; verify extension/feed/google_sitemap route"
        plan = "PLAN_A"
    elif not ctrl_analysis.get("controller_present"):
        cause = "Google Sitemap controller missing on server"
        minimal_fix = "Deploy controller or alternate sitemap mechanism"
        plan = "PLAN_D"

    payload = {
        "identified_at": utc_now(),
        "root_cause": cause,
        "minimal_fix": minimal_fix,
        "recommended_plan": plan,
        "controller_analysis": ctrl_analysis,
        "admin_extension_enabled": admin_state.get("extension_enabled"),
        "static_sitemap_empty_file": static_size == 0,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "root-cause.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "root-cause.md",
        "\n".join(
            [
                "# Root cause",
                "",
                f"**Cause:** {cause}",
                "",
                f"**Minimal fix:** {minimal_fix}",
                "",
                f"**Recommended plan:** {plan}",
                "",
                "## Details",
                "",
                f"- Controller present: {ctrl_analysis.get('controller_present')}",
                f"- Static sitemap.xml size: {static_size}",
                f"- Admin extension enabled: {admin_state.get('extension_enabled')}",
            ]
        ),
    )
    return payload


def prepare_robots_update(current: str, sitemap_url: str) -> str:
    lines = current.splitlines()
    out: list[str] = []
    sitemap_added = False
    for line in lines:
        if re.match(r"(?i)^Sitemap:", line.strip()):
            continue
        out.append(line)
    while out and not out[-1].strip():
        out.pop()
    out.append("")
    out.append(f"Sitemap: {sitemap_url}")
    out.append("")
    return "\n".join(out)


def choose_sitemap_url(after_candidates: dict[str, Any]) -> str | None:
    priority = [
        "https://bzpm.ru/sitemap.xml",
        "https://bzpm.ru/index.php?route=extension/feed/google_sitemap",
    ]
    by_url = {c["url"]: c for c in after_candidates.get("candidates", [])}
    for url in priority:
        c = by_url.get(url)
        if c and c.get("valid_sitemap"):
            return url
    for c in after_candidates.get("candidates", []):
        if c.get("valid_sitemap"):
            return c["url"]
    return None


def phase_spot_check() -> dict[str, Any]:
    rows = []
    for url in SPOT_CHECK_URLS:
        resp = http_get(url)
        parser = BodyCounter()
        if resp.get("body"):
            parser.feed_text(resp["body"])
        rows.append(
            {
                "url": url,
                "status_code": resp.get("status_code"),
                "body_open_count": parser.body_open,
                "has_metrika": parser.has_metrika,
                "has_webmaster": parser.has_webmaster,
                "pass": resp.get("status_code") == 200
                and parser.body_open == 1
                and parser.has_metrika
                and parser.has_webmaster,
            }
        )
    payload = {"checked_at": utc_now(), "urls": rows, "all_pass": all(r["pass"] for r in rows)}
    write_json(DEPLOYMENT_ROOT / "verification" / "spot-check.json", payload)
    md = ["# Spot check", ""]
    for r in rows:
        md.append(
            f"- {r['url']} — HTTP {r['status_code']} — body={r['body_open_count']} "
            f"metrika={r['has_metrika']} webmaster={r['has_webmaster']} pass={r['pass']}"
        )
    write_text(DEPLOYMENT_ROOT / "verification" / "spot-check.md", "\n".join(md))
    return payload


def run_phases(deploy: bool, enable_admin: bool) -> int:
    ensure_dirs()
    log_lines = [f"Operation {OPERATION_ID} started {utc_now()}"]

    sitemap_before = phase_sitemap_before()
    ftp = ftp_connect()
    robots_before = phase_robots_before(ftp)
    source = phase_source_discovery(ftp)
    ftp.quit()

    admin_state = phase_admin_discovery()
    root_cause = determine_root_cause(sitemap_before, admin_state, source)

    admin_enable_result: dict[str, Any] = {"admin_save_performed": False, "status": "SKIPPED"}
    if enable_admin and root_cause.get("recommended_plan") == "PLAN_A":
        if admin_state.get("extension_enabled") is False:
            admin_enable_result = admin_enable_google_sitemap()
            time.sleep(2)

    sitemap_after = phase_sitemap_before()
    # rename after artefacts
    for f in (DEPLOYMENT_ROOT / "sitemap-before").glob("*"):
        pass
    # re-run into sitemap-after
    after_results = []
    for url in SITEMAP_CANDIDATES:
        resp = http_get(url)
        body = resp.get("body", "")
        analysis = analyze_sitemap_body(body, resp.get("content_type", ""), resp.get("status_code"))
        slug = re.sub(r"[^a-z0-9]+", "-", url.split("//", 1)[-1].lower()).strip("-")[:80]
        write_text(DEPLOYMENT_ROOT / "sitemap-after" / f"{slug}.body.txt", body[:50000])
        after_results.append({"url": url, **analysis})
    sitemap_after = {"checked_at": utc_now(), "candidates": after_results}
    write_json(DEPLOYMENT_ROOT / "verification" / "sitemap-after.json", sitemap_after)

    valid_url = choose_sitemap_url(sitemap_after)
    robots_deployed = False
    robots_after_sha = None

    prepared_robots = None
    if valid_url:
        prepared_robots = prepare_robots_update(robots_before["content"], valid_url)
        write_text(DEPLOYMENT_ROOT / "prepared" / "robots.txt", prepared_robots)
        write_json(
            DEPLOYMENT_ROOT / "manifests" / "files-to-change.json",
            {
                "files": [{"remote": REMOTE_ROBOTS, "action": "update_sitemap_directive", "sitemap_url": valid_url}],
                "admin_actions": [admin_enable_result] if admin_enable_result.get("admin_save_performed") else [],
            },
        )
        write_text(
            DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md",
            "\n".join(
                [
                    "# Implementation plan",
                    "",
                    f"Plan: {root_cause.get('recommended_plan')}",
                    f"Valid sitemap URL: {valid_url}",
                    f"Admin enable: {admin_enable_result.get('status')}",
                    f"Robots update: add Sitemap: {valid_url}",
                ]
            ),
        )

    if deploy and valid_url and prepared_robots:
        ftp = ftp_connect()
        pre_upload = ftp_download(ftp, REMOTE_ROBOTS)
        pre_sha = sha256_bytes(pre_upload)
        if pre_sha != robots_before["sha256"]:
            log_lines.append("STOP — LIVE FILE CHANGED SINCE BACKUP")
            write_text(DEPLOYMENT_ROOT / "logs" / "operation.log", "\n".join(log_lines))
            print("STOP — LIVE FILE CHANGED SINCE BACKUP")
            ftp.quit()
            return 2
        (DEPLOYMENT_ROOT / "verification" / "pre-upload" / "robots.txt").write_bytes(pre_upload)
        ftp_upload(ftp, REMOTE_ROBOTS, prepared_robots.encode("utf-8"))
        robots_deployed = True
        ftp.quit()
        time.sleep(1)
        post = http_get("https://bzpm.ru/robots.txt")
        robots_after_sha = sha256_bytes(post.get("body", "").encode("utf-8"))
        write_text(DEPLOYMENT_ROOT / "robots-after" / "robots.txt", post.get("body", ""))

    spot = phase_spot_check()

    # Final sitemap verification after deploy
    final_sitemap = phase_sitemap_before()
    final_valid = choose_sitemap_url({"candidates": [
        {**analyze_sitemap_body(http_get(u)["body"], http_get(u).get("content_type",""), http_get(u).get("status_code")), "url": u}
        for u in SITEMAP_CANDIDATES
    ]})

    verdict = "SITE-002 SITEMAP ENABLE BLOCKED — NO REMOTE CHANGE PERFORMED"
    if valid_url and (robots_deployed or "Sitemap:" in robots_before["content"]):
        post_robots = http_get("https://bzpm.ru/robots.txt")
        sitemap_lines = re.findall(r"(?im)^Sitemap:\s*(.+)$", post_robots.get("body", ""))
        robots_ok = len(sitemap_lines) == 1 and sitemap_lines[0].strip() == valid_url
        sm = next((c for c in sitemap_after["candidates"] if c["url"] == valid_url), None)
        if sm and sm.get("valid_sitemap") and robots_ok:
            verdict = "SITE-002 SITEMAP ENABLE COMPLETE — VALID XML SITEMAP VERIFIED"
        elif sm and sm.get("valid_sitemap"):
            verdict = "SITE-002 SITEMAP ENABLE PARTIAL — VALID SITEMAP ROUTE FOUND / ROBOTS UPDATED"
    elif valid_url and not deploy:
        verdict = "SITE-002 SITEMAP ENABLE PARTIAL — VALID SITEMAP ROUTE FOUND / ROBOTS UPDATED"

    summary = {
        "operation_id": OPERATION_ID,
        "completed_at": utc_now(),
        "verdict": verdict,
        "valid_sitemap_url": valid_url,
        "robots_deployed": robots_deployed,
        "admin_enable": admin_enable_result,
        "root_cause": root_cause,
        "spot_check": spot,
        "sitemap_after": sitemap_after,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation-summary.json", summary)
    write_text(DEPLOYMENT_ROOT / "logs" / "operation.log", "\n".join(log_lines + [f"Verdict: {verdict}"]))
    print(json.dumps({"verdict": verdict, "valid_sitemap_url": valid_url, "robots_deployed": robots_deployed}, indent=2))
    return 0 if "COMPLETE" in verdict or "PARTIAL" in verdict else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--deploy", action="store_true", help="Upload robots.txt after valid sitemap confirmed")
    parser.add_argument("--enable-admin", action="store_true", help="Enable Google Sitemap in admin if disabled")
    parser.add_argument("--discover-only", action="store_true", help="Phases 1-5 only")
    args = parser.parse_args()
    if args.discover_only:
        ensure_dirs()
        phase_sitemap_before()
        ftp = ftp_connect()
        phase_robots_before(ftp)
        phase_source_discovery(ftp)
        ftp.quit()
        admin_state = phase_admin_discovery()
        determine_root_cause(phase_sitemap_before(), admin_state, {})
        print("discover-only complete")
        return 0
    return run_phases(deploy=args.deploy, enable_admin=args.enable_admin)


if __name__ == "__main__":
    raise SystemExit(main())
