#!/usr/bin/env python3
"""SITE-002 Production contacts URL routing review — read-only (Run 4.237)."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import json
import re
import shlex
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

OPERATION_ID = "SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01"
OCPILOT_RUN = "4.237"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION_READ_ONLY"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
WRONG_BRAND = "БЗПМ"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

SUBDIRS = (
    "http-snapshots",
    "db-readonly",
    "ftp-source",
    "sitemap",
    "links-inventory",
    "routing-analysis",
    "implementation-charter",
    "manifests",
    "reports",
    "logs",
)

HTTP_URLS = [
    ("contacts", "https://bzpm.ru/kontakty", "primary_target"),
    ("contacts", "https://bzpm.ru/contact", "candidate"),
    ("contacts", "https://bzpm.ru/contacts", "candidate"),
    ("contacts", "https://bzpm.ru/index.php?route=information/contact", "native_route"),
    ("contacts", "https://bzpm.ru/index.php?route=information/information&information_id=7", "info_id_probe"),
    ("contacts", "https://bzpm.ru/index.php?route=information/information&information_id=4", "info_id_probe"),
    ("contacts", "https://bzpm.ru/index.php?route=information/information", "info_list"),
    ("stable", "https://bzpm.ru/", "regression"),
    ("stable", "https://bzpm.ru/katalog", "regression"),
    ("stable", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie", "regression"),
    ("stable", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari", "regression"),
    ("stable", "https://bzpm.ru/sitemap.xml", "regression"),
    ("stable", "https://bzpm.ru/robots.txt", "regression"),
    ("stable", "https://bzpm.ru/llms.txt", "regression"),
]

LINK_CRAWL_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/payment-methods",
    "https://bzpm.ru/delivery",
    "https://bzpm.ru/dealers",
    "https://bzpm.ru/guarantee",
    "https://bzpm.ru/custom-equipment",
]

CONTACT_SEARCH_TERMS = (
    "kontakty",
    "contact",
    "contacts",
    "information/contact",
    "Контакты",
)

CONTACT_BODY_MARKERS = (
    ("phone", re.compile(r"\+7|8\s*\(?\d{3}\)?|тел\.|телефон", re.I)),
    ("address", re.compile(r"адрес|ул\.|улиц|проспект|г\.\s*[А-Яа-я]", re.I)),
    ("map", re.compile(r"yandex\.ru/maps|google\.com/maps|iframe[^>]+map|zpm-map|contact-map", re.I)),
    ("contact_form", re.compile(r"zpm-form|route=information/contact|name=[\"']form|data-fb-form|contact-form", re.I)),
    ("requisites", re.compile(r"реквизит|ИНН|ОГРН|р/с", re.I)),
    ("opening_hours", re.compile(r"часы работы|режим работы|пн\.|понедельник", re.I)),
)

FTP_PATHS = [
    ("/public_html/catalog/controller/information/contact.php", "native contact controller"),
    ("/public_html/catalog/view/theme/default/template/information/contact.twig", "native contact template"),
    ("/public_html/catalog/controller/information/information.php", "information page controller"),
    ("/public_html/catalog/view/theme/default/template/information/information.twig", "information page template"),
    ("/public_html/catalog/controller/startup/seo_url.php", "SEO URL routing"),
    ("/public_html/catalog/controller/startup/seo_pro.php", "SEO PRO routing"),
    ("/public_html/catalog/controller/extension/feed/google_sitemap.php", "sitemap feed"),
    ("/public_html/catalog/view/theme/default/template/common/header.twig", "header links (protected)"),
    ("/public_html/catalog/view/theme/default/template/common/footer.twig", "footer links (protected)"),
    ("/public_html/.htaccess", "htaccess redirects"),
    ("/public_html/catalog/view/theme/default/template/information/payment.twig", "corp page pattern"),
    ("/public_html/catalog/view/theme/default/template/information/delivery.twig", "corp page pattern"),
    ("/public_html/catalog/view/theme/default/template/information/dealers.twig", "corp page pattern"),
    ("/public_html/catalog/view/theme/default/template/information/guarantee.twig", "corp page pattern"),
    ("/public_html/catalog/view/theme/default/template/information/custom_equipment.twig", "corp page pattern"),
]


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
            self._anchor_href = href
            self._anchor_text = ""
            self._in_anchor = True

    def handle_endtag(self, tag: str) -> None:
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = False
        elif tag_l == "h1":
            self.in_h1 = False
        elif tag_l == "a" and getattr(self, "_in_anchor", False):
            self._in_anchor = False
            text = getattr(self, "_anchor_text", "").strip()
            href = getattr(self, "_anchor_href", "")
            if href or text:
                self.anchors.append({"href": href, "text": text})

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if self.in_h1:
            text = data.strip()
            if text:
                self.h1_list.append(text)
        if getattr(self, "_in_anchor", False):
            self._anchor_text = getattr(self, "_anchor_text", "") + data


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
            "change_type": "contacts-url-routing-discovery",
            "target_url": "/kontakty",
            "production_mutation_allowed": False,
            "ftp_upload_allowed": False,
            "ftp_download_allowed": True,
            "db_select_allowed": True,
            "db_write_allowed": False,
            "admin_save_allowed": False,
            "redirect_change_allowed": False,
            "seo_url_change_allowed": False,
            "cache_clear_allowed": False,
            "import_run_allowed": False,
            "monitor_run_allowed": False,
            "report_only": True,
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


def http_fetch(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    chain: list[dict[str, Any]] = []
    current = url
    for _ in range(10):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                body = resp.read()
                entry = {
                    "url": current,
                    "status": resp.status,
                    "final_url": resp.geturl(),
                    "headers": {k.lower(): v for k, v in resp.headers.items()},
                }
                chain.append(entry)
                return {
                    "url": url,
                    "status": resp.status,
                    "final_url": resp.geturl(),
                    "redirect_chain": chain,
                    "headers": entry["headers"],
                    "body": body,
                    "error": None,
                }
        except urllib.error.HTTPError as exc:
            body = exc.read()
            chain.append({"url": current, "status": exc.code, "final_url": exc.geturl()})
            return {
                "url": url,
                "status": exc.code,
                "final_url": exc.geturl(),
                "redirect_chain": chain,
                "headers": {k.lower(): v for k, v in exc.headers.items()},
                "body": body,
                "error": str(exc),
            }
        except urllib.error.URLError as exc:
            return {
                "url": url,
                "status": None,
                "final_url": url,
                "redirect_chain": chain,
                "body": b"",
                "error": str(exc),
            }
    return {"url": url, "status": None, "final_url": url, "redirect_chain": chain, "body": b"", "error": "redirect loop"}


def detect_contact_signs(html: str) -> dict[str, bool]:
    signs: dict[str, bool] = {}
    for name, pattern in CONTACT_BODY_MARKERS:
        signs[name] = bool(pattern.search(html))
    return signs


def parse_html_page(body: bytes) -> dict[str, Any]:
    text = body.decode("utf-8", errors="replace")
    parser = PageParser()
    parser.feed(text)
    canonical = ""
    for link in parser.links:
        if link.get("rel") == "canonical":
            canonical = link.get("href", "")
    contact_signs = detect_contact_signs(text)
    return {
        "title": parser.title.strip(),
        "meta_description": parser.meta.get("description", ""),
        "meta_robots": parser.meta.get("robots", ""),
        "canonical": canonical,
        "h1": " | ".join([h for h in parser.h1_list if h]),
        "contact_signs": contact_signs,
        "contact_signs_count": sum(1 for v in contact_signs.values() if v),
        "bzpm_hits": text.count(WRONG_BRAND),
        "anchors": parser.anchors,
        "html": text,
    }


def slug_from_url(url: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "_", url.replace("https://bzpm.ru/", ""))[:120]
    return slug or "root"


def phase_http() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for group, url, path_class in HTTP_URLS:
        time.sleep(0.35)
        resp = http_fetch(url)
        parsed: dict[str, Any] = {}
        if resp.get("body"):
            parsed = parse_html_page(resp["body"])
            write_text(
                DEPLOYMENT_ROOT / "http-snapshots" / f"{slug_from_url(url)}.html",
                parsed.pop("html", ""),
            )
        signs = parsed.get("contact_signs", {})
        row = {
            "group": group,
            "url": url,
            "path_class": path_class,
            "http_status": resp.get("status"),
            "final_url": resp.get("final_url"),
            "redirect_chain": json.dumps(
                [{"url": x.get("url"), "status": x.get("status")} for x in resp.get("redirect_chain", [])],
                ensure_ascii=False,
            ),
            "title": parsed.get("title", ""),
            "meta_description": parsed.get("meta_description", ""),
            "meta_robots": parsed.get("meta_robots", ""),
            "canonical": parsed.get("canonical", ""),
            "h1": parsed.get("h1", ""),
            "has_phone": signs.get("phone", False),
            "has_address": signs.get("address", False),
            "has_map": signs.get("map", False),
            "has_contact_form": signs.get("contact_form", False),
            "has_requisites": signs.get("requisites", False),
            "has_opening_hours": signs.get("opening_hours", False),
            "contact_signs_count": parsed.get("contact_signs_count", 0),
            "bzpm_hits": parsed.get("bzpm_hits", 0),
            "error": resp.get("error"),
        }
        rows.append(row)
    fields = list(rows[0].keys()) if rows else []
    write_csv(DEPLOYMENT_ROOT / "http-snapshots" / "http-url-status.csv", rows, fields)
    write_json(DEPLOYMENT_ROOT / "http-snapshots" / "http-url-status.json", rows)
    md = ["# HTTP URL status\n", f"Generated: {utc_now()}\n\n"]
    for r in rows:
        md.append(f"## {r['url']}\n")
        md.append(f"- Status: {r['http_status']}\n")
        md.append(f"- Final URL: {r['final_url']}\n")
        md.append(f"- Title: {r['title']}\n")
        md.append(f"- Canonical: {r['canonical']}\n")
        md.append(f"- H1: {r['h1']}\n")
        md.append(f"- Contact signs: phone={r['has_phone']}, address={r['has_address']}, form={r['has_contact_form']}\n")
        md.append(f"- БЗПМ hits: {r['bzpm_hits']}\n\n")
    write_text(DEPLOYMENT_ROOT / "http-snapshots" / "http-url-status.md", "".join(md))
    return rows


def is_contact_related(href: str, text: str) -> bool:
    blob = f"{href} {text}".lower()
    return any(t.lower() in blob for t in CONTACT_SEARCH_TERMS)


def phase_links() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for page_url in LINK_CRAWL_URLS:
        time.sleep(0.3)
        resp = http_fetch(page_url)
        html = resp.get("body", b"").decode("utf-8", errors="replace")
        parser = PageParser()
        parser.feed(html)
        for anchor in parser.anchors:
            href = anchor.get("href", "")
            text = anchor.get("text", "")
            if not is_contact_related(href, text):
                continue
            abs_href = urljoin(page_url, href)
            rows.append({
                "source_page": page_url,
                "href_raw": href,
                "href_absolute": abs_href,
                "link_text": text,
                "in_header_footer_guess": "header" if "header" in html[:html.find(href) if href in html else 0] else "unknown",
            })
        for term in CONTACT_SEARCH_TERMS:
            if term.lower() in html.lower() and not any(term.lower() in r.get("href_raw", "").lower() for r in rows if r["source_page"] == page_url):
                rows.append({
                    "source_page": page_url,
                    "href_raw": "",
                    "href_absolute": "",
                    "link_text": f"[text-only mention: {term}]",
                    "in_header_footer_guess": "text_block",
                })
    deduped: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    for r in rows:
        key = (r["source_page"], r["href_absolute"], r["link_text"])
        if key not in seen:
            seen.add(key)
            deduped.append(r)
    fields = ["source_page", "href_raw", "href_absolute", "link_text", "in_header_footer_guess"]
    write_csv(DEPLOYMENT_ROOT / "links-inventory" / "internal-contact-links.csv", deduped, fields)
    write_json(DEPLOYMENT_ROOT / "links-inventory" / "internal-contact-links.json", deduped)
    md = ["# Internal contact links\n\n", f"Generated: {utc_now()}\n\n"]
    for r in deduped:
        md.append(f"- **{r['source_page']}** → `{r['href_absolute'] or r['link_text']}` ({r['link_text']})\n")
    write_text(DEPLOYMENT_ROOT / "links-inventory" / "internal-contact-links.md", "".join(md))
    return deduped


def phase_sitemap() -> dict[str, Any]:
    resp = http_fetch("https://bzpm.ru/sitemap.xml")
    body = resp.get("body", b"")
    write_text(DEPLOYMENT_ROOT / "sitemap" / "sitemap-live.xml", body.decode("utf-8", errors="replace"))
    locs: list[str] = []
    try:
        root = ET.fromstring(body)
        for loc in root.iter(SITEMAP_NS + "loc"):
            if loc.text:
                locs.append(loc.text.strip())
    except ET.ParseError:
        pass

    patterns = [
        "kontakty",
        "/contact",
        "/contacts",
        "information/contact",
    ]
    hits: list[dict[str, Any]] = []
    for loc in locs:
        loc_l = loc.lower()
        for p in patterns:
            if p in loc_l:
                hits.append({"pattern": p, "url": loc})
    row = {
        "total_loc_count": len(locs),
        "contact_hits": hits,
        "kontakty_in_sitemap": any("kontakty" in x.lower() for x in locs),
        "contact_keyword_in_sitemap": any(
            x.rstrip("/").endswith("/contact") or "/contact?" in x.lower() for x in locs
        ),
        "contacts_keyword_in_sitemap": any("contacts" in x.lower() for x in locs),
        "information_contact_in_sitemap": any("information/contact" in x.lower() for x in locs),
        "sitemap_dynamic": True,
        "update_mechanism": "OpenCart extension/feed/google_sitemap",
    }
    write_json(DEPLOYMENT_ROOT / "sitemap" / "contacts-sitemap-analysis.json", row)
    write_csv(
        DEPLOYMENT_ROOT / "sitemap" / "contacts-sitemap-analysis.csv",
        hits or [{"pattern": "none", "url": ""}],
        ["pattern", "url"],
    )
    md = ["# Contacts sitemap analysis\n\n", json.dumps(row, ensure_ascii=False, indent=2)]
    write_text(DEPLOYMENT_ROOT / "sitemap" / "contacts-sitemap-analysis.md", "\n".join(md))
    return row


def ftp_connect() -> ftplib.FTP:
    fields = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(fields["host"], int(fields.get("port") or 21), timeout=180)
    ftp.login(fields["username"], fields["password"])
    return ftp


def ftp_download_file(ftp: ftplib.FTP, remote_path: str) -> bytes | None:
    buf: list[bytes] = []

    def collect(data: bytes) -> None:
        buf.append(data)

    try:
        ftp.retrbinary("RETR " + remote_path, collect)
        return b"".join(buf)
    except ftplib.error_perm:
        return None


def local_ftp_name(remote_path: str) -> str:
    return remote_path.strip("/").replace("/", "__")


def analyze_source_content(remote_path: str, role: str, content: str) -> dict[str, Any]:
    lower = content.lower()
    checks = {
        "contains_kontakty": "kontakty" in lower or "/контакты" in lower,
        "contains_information_contact": "information/contact" in lower,
        "contains_contact_link": bool(re.search(r'href=["\'][^"\']*(?:kontakty|/contact|contacts|information/contact)', lower)),
        "contains_routing_logic": any(x in remote_path for x in ("seo_url", "seo_pro", "htaccess")),
        "contains_sitemap_logic": "google_sitemap" in remote_path or "sitemap" in lower,
    }
    needs_change = "no"
    reason = "reference only"
    if "header.twig" in remote_path or "footer.twig" in remote_path:
        needs_change = "maybe"
        reason = "May need header/footer link update if canonical contacts URL changes — protected Yandex blocks"
    elif "contact.php" in remote_path or "contact.twig" in remote_path:
        needs_change = "maybe"
        reason = "Native contact route owner — verify SEO URL mapping before template edits"
    elif "seo_url" in remote_path or "seo_pro" in remote_path:
        needs_change = "no"
        reason = "Routing layer — likely SEO URL DB record sufficient"
    elif "google_sitemap" in remote_path:
        needs_change = "no"
        reason = "Dynamic sitemap — should include contacts after SEO URL exists"
    elif ".htaccess" in remote_path:
        needs_change = "redirect_phase"
        reason = "Only if 301 from legacy URL needed after SEO URL fix"
    if checks["contains_kontakty"] and "404" not in reason:
        reason += "; references kontakty"
    return {
        "remote_path": remote_path,
        "role": role,
        "bytes": len(content.encode("utf-8", errors="replace")),
        **checks,
        "likely_needs_implementation_change": needs_change,
        "reason": reason,
    }


def phase_ftp() -> list[dict[str, Any]]:
    ftp = ftp_connect()
    rows: list[dict[str, Any]] = []
    download_count = 0
    try:
        for remote_path, role in FTP_PATHS:
            data = ftp_download_file(ftp, remote_path)
            row_base = {"remote_path": remote_path, "role": role, "downloaded": data is not None}
            if data is not None:
                download_count += 1
                local = DEPLOYMENT_ROOT / "ftp-source" / local_ftp_name(remote_path)
                local.write_bytes(data)
                text = data.decode("utf-8", errors="replace")
                row = analyze_source_content(remote_path, role, text)
                row["downloaded"] = True
                row["sha256"] = hashlib.sha256(data).hexdigest()
            else:
                row = {**row_base, "likely_needs_implementation_change": "unknown", "reason": "file not found"}
            rows.append(row)
    finally:
        ftp.quit()
    fields = [
        "remote_path", "role", "downloaded", "contains_kontakty", "contains_information_contact",
        "contains_contact_link", "contains_routing_logic", "contains_sitemap_logic",
        "likely_needs_implementation_change", "reason",
    ]
    write_csv(DEPLOYMENT_ROOT / "ftp-source" / "source-map.csv", rows, fields)
    write_json(DEPLOYMENT_ROOT / "ftp-source" / "source-map.json", rows)
    md = ["# FTP source map\n", f"Downloads: {download_count}\n\n"]
    for r in rows:
        md.append(f"- `{r['remote_path']}` — {r.get('reason', '')}\n")
    write_text(DEPLOYMENT_ROOT / "ftp-source" / "source-map.md", "".join(md))
    return rows


def ssh_mysql_query(sql: str) -> dict[str, Any]:
    try:
        import paramiko  # type: ignore
    except ImportError:
        return {"status": "blocked", "reason": "paramiko not available"}
    ssh_fields = parse_production_section(SECRETS_PATH, "SSH")
    db_fields = parse_production_section(SECRETS_PATH, "Database")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(
            ssh_fields["host"],
            port=int(ssh_fields.get("port") or 22),
            username=ssh_fields["username"],
            password=ssh_fields["password"],
            timeout=60,
            allow_agent=False,
            look_for_keys=False,
        )
    except Exception as exc:
        return {"status": "blocked", "reason": f"SSH connect failed: {exc}"}
    db_user = db_fields["username"]
    db_pass = db_fields["password"]
    db_name = db_fields["database"]
    sql_escaped = sql.replace("\\", "\\\\").replace('"', '\\"')
    cmd = (
        f'MYSQL_PWD={shlex.quote(db_pass)} mysql -N -B -u {shlex.quote(db_user)} '
        f'{shlex.quote(db_name)} -e "{sql_escaped}" 2>&1'
    )
    _stdin, stdout, stderr = client.exec_command(cmd, timeout=120)
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    client.close()
    if "ERROR" in out or "ERROR" in err or "Access denied" in out + err:
        return {"status": "failed", "stdout": out, "stderr": err}
    return {"status": "ok", "stdout": out, "stderr": err}


def tsv_to_rows(tsv: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in tsv.strip().splitlines():
        if line.strip():
            rows.append(line.split("\t"))
    return rows


def phase_db() -> dict[str, Any]:
    prefix_probe = ssh_mysql_query("SHOW TABLES LIKE '%information%'")
    result: dict[str, Any] = {"prefix_probe": prefix_probe, "queries": []}
    if prefix_probe.get("status") != "ok":
        write_json(DEPLOYMENT_ROOT / "db-readonly" / "db-status.json", result)
        return result

    tables = [line.strip() for line in prefix_probe.get("stdout", "").splitlines() if line.strip()]
    prefix = "oc_"
    if tables and not tables[0].startswith("oc_"):
        prefix = tables[0].split("information")[0] if "information" in tables[0] else "oc_"

    queries = {
        "information_by_title": f"""
            SELECT i.information_id, i.bottom, i.sort_order, i.status, id.language_id, id.title,
                   id.meta_title, id.meta_description, LENGTH(id.description) AS desc_len
            FROM {prefix}information i
            JOIN {prefix}information_description id ON i.information_id = id.information_id
            WHERE id.language_id = 1
              AND (id.title LIKE '%онтакт%' OR id.title LIKE '%contact%' OR id.title LIKE '%Contact%')
            ORDER BY i.information_id
        """,
        "information_ids_probe": f"""
            SELECT i.information_id, i.status, id.title, LENGTH(id.description) AS desc_len
            FROM {prefix}information i
            JOIN {prefix}information_description id ON i.information_id = id.information_id
            WHERE i.information_id IN (4, 7) AND id.language_id = 1
        """,
        "information_to_store": f"""
            SELECT its.information_id, its.store_id
            FROM {prefix}information_to_store its
            WHERE its.information_id IN (
                SELECT i.information_id FROM {prefix}information i
                JOIN {prefix}information_description id ON i.information_id = id.information_id
                WHERE id.language_id = 1 AND (id.title LIKE '%онтакт%' OR id.title LIKE '%contact%')
            )
        """,
        "information_to_layout": f"""
            SELECT itl.information_id, itl.store_id, itl.layout_id
            FROM {prefix}information_to_layout itl
            WHERE itl.information_id IN (
                SELECT i.information_id FROM {prefix}information i
                JOIN {prefix}information_description id ON i.information_id = id.information_id
                WHERE id.language_id = 1 AND (id.title LIKE '%онтакт%' OR id.title LIKE '%contact%')
            )
        """,
        "seo_url_contact": f"""
            SELECT seo_url_id, store_id, language_id, query, keyword
            FROM {prefix}seo_url
            WHERE keyword IN ('kontakty', 'contact', 'contacts')
               OR query LIKE 'information/%contact%'
               OR query LIKE 'information/information&information_id=%'
            ORDER BY query, keyword
        """,
        "seo_url_kontakty_probe": f"""
            SELECT seo_url_id, store_id, language_id, query, keyword
            FROM {prefix}seo_url
            WHERE keyword = 'kontakty'
        """,
        "setting_contact": f"""
            SELECT \`key\`, value
            FROM {prefix}setting
            WHERE \`key\` LIKE '%contact%' OR \`key\` LIKE '%email%' OR code = 'config'
            ORDER BY \`key\`
            LIMIT 30
        """,
    }

    parsed_data: dict[str, Any] = {"prefix": prefix, "tables_found": tables}
    for name, sql in queries.items():
        q = ssh_mysql_query(sql.strip())
        result["queries"].append({"name": name, "status": q.get("status"), "error": q.get("reason") or q.get("stderr")})
        if q.get("status") == "ok":
            parsed_data[name] = tsv_to_rows(q.get("stdout", ""))

    write_json(DEPLOYMENT_ROOT / "db-readonly" / "db-raw.json", parsed_data)
    write_json(DEPLOYMENT_ROOT / "db-readonly" / "db-status.json", result)

    info_rows: list[dict[str, Any]] = []
    for row in parsed_data.get("information_by_title", []):
        if len(row) >= 9:
            info_rows.append({
                "information_id": row[0],
                "bottom": row[1],
                "sort_order": row[2],
                "status": row[3],
                "language_id": row[4],
                "title": row[5],
                "meta_title": row[6],
                "meta_description": row[7],
                "description_length": row[8],
            })
    for row in parsed_data.get("information_ids_probe", []):
        if len(row) >= 4 and not any(r["information_id"] == row[0] for r in info_rows):
            info_rows.append({
                "information_id": row[0],
                "bottom": "",
                "sort_order": "",
                "status": row[1],
                "language_id": "1",
                "title": row[2],
                "meta_title": "",
                "meta_description": "",
                "description_length": row[3],
            })
    if info_rows:
        write_csv(DEPLOYMENT_ROOT / "db-readonly" / "information-pages.csv", info_rows, list(info_rows[0].keys()))
        write_json(DEPLOYMENT_ROOT / "db-readonly" / "information-pages.json", info_rows)

    seo_rows: list[dict[str, Any]] = []
    for row in parsed_data.get("seo_url_contact", []):
        if len(row) >= 5:
            seo_rows.append({
                "seo_url_id": row[0],
                "store_id": row[1],
                "language_id": row[2],
                "query": row[3],
                "keyword": row[4],
            })
    if seo_rows:
        write_csv(DEPLOYMENT_ROOT / "db-readonly" / "seo-url-records.csv", seo_rows, list(seo_rows[0].keys()))
        write_json(DEPLOYMENT_ROOT / "db-readonly" / "seo-url-records.json", seo_rows)

    md_lines = ["# Contact route candidates (DB read-only)\n\n", f"Prefix: `{prefix}`\n\n"]
    md_lines.append("## Information pages\n\n")
    for r in info_rows:
        md_lines.append(f"- id **{r['information_id']}**: {r['title']} (status={r['status']})\n")
    md_lines.append("\n## SEO URL records\n\n")
    for r in seo_rows:
        md_lines.append(f"- `{r['keyword']}` → `{r['query']}` (id {r['seo_url_id']})\n")
    kontakty_rows = parsed_data.get("seo_url_kontakty_probe", [])
    md_lines.append(f"\n## kontakty keyword rows: {len(kontakty_rows)}\n")
    write_text(DEPLOYMENT_ROOT / "db-readonly" / "contact-route-candidates.md", "".join(md_lines))
    return parsed_data


def infer_canonical(http_rows: list[dict[str, Any]], db_data: dict[str, Any], sitemap: dict[str, Any]) -> str:
    working = [
        r for r in http_rows
        if r.get("group") == "contacts" and r.get("http_status") == 200 and (r.get("contact_signs_count") or 0) >= 2
    ]
    if not working:
        working = [r for r in http_rows if r.get("group") == "contacts" and r.get("http_status") == 200]
    if working:
        best = max(working, key=lambda x: x.get("contact_signs_count", 0))
        final = best.get("final_url", "")
        if final.startswith("https://bzpm.ru/"):
            path = final.replace("https://bzpm.ru", "")
            return path or "/"
    seo_rows = db_data.get("seo_url_contact", [])
    for row in seo_rows:
        if len(row) >= 5 and row[4] in ("contact", "contacts", "kontakty"):
            return f"/{row[4]}"
    return "SAFE UNKNOWN"


def build_routing_analysis(
    http_rows: list[dict[str, Any]],
    db_data: dict[str, Any],
    sitemap: dict[str, Any],
    links: list[dict[str, Any]],
    ftp_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    kontakty_row = next((r for r in http_rows if r["url"].endswith("/kontakty")), {})
    contact_seo = [r for r in db_data.get("seo_url_contact", []) if len(r) >= 5]
    kontakty_seo = [r for r in db_data.get("seo_url_kontakty_probe", []) if len(r) >= 5]
    info_pages = db_data.get("information_by_title", [])

    native_contact_http = next(
        (r for r in http_rows if "route=information/contact" in r["url"]),
        {},
    )
    contact_pretty = next((r for r in http_rows if r["url"].endswith("/contact")), {})
    contacts_pretty = next((r for r in http_rows if r["url"].endswith("/contacts")), {})

    root_causes: list[str] = []
    if kontakty_row.get("http_status") == 404:
        root_causes.append("missing_seo_url_for_kontakty")
    if not kontakty_seo:
        root_causes.append("no_db_keyword_kontakty")
    if kontakty_row.get("http_status") == 404 and native_contact_http.get("http_status") == 200:
        root_causes.append("native_contact_works_but_pretty_url_absent")
    if not sitemap.get("kontakty_in_sitemap"):
        root_causes.append("absent_from_sitemap")
    broken_kontakty_links = [r for r in links if "kontakty" in (r.get("href_absolute") or r.get("href_raw", "")).lower()]
    if broken_kontakty_links:
        root_causes.append("internal_links_point_to_kontakty")

    recommended_option = "A"
    recommended_reason = "Add SEO URL keyword kontakty for native information/contact route"
    owner = "native information/contact"
    if info_pages and not native_contact_http.get("http_status") == 200:
        recommended_option = "B"
        recommended_reason = "Use information page with SEO URL kontakty"
        owner = f"information/information&information_id={info_pages[0][0] if info_pages else '?'}"
    elif contact_pretty.get("http_status") == 200 and kontakty_row.get("http_status") == 404:
        recommended_option = "C"
        recommended_reason = "301 redirect /kontakty to existing /contact if /contact is canonical"
        owner = "existing /contact SEO URL"

    analysis = {
        "canonical_contacts_url_recommended": "/kontakty",
        "canonical_contacts_url_current": infer_canonical(http_rows, db_data, sitemap),
        "kontakty_http_status": kontakty_row.get("http_status"),
        "native_contact_http_status": native_contact_http.get("http_status"),
        "contact_pretty_status": contact_pretty.get("http_status"),
        "contacts_pretty_status": contacts_pretty.get("http_status"),
        "contacts_owner": owner,
        "root_causes": root_causes,
        "recommended_implementation_option": recommended_option,
        "recommended_reason": recommended_reason,
        "should_not_do": [
            "duplicate contacts pages",
            "break existing contact form",
            "touch Yandex header/footer scripts",
            "hardcode contact content if DB page exists",
        ],
        "sitemap_should_include_after_fix": True,
        "header_footer_link_update_likely": any(
            r.get("contains_kontakty") or r.get("contains_contact_link")
            for r in ftp_rows if r.get("downloaded")
        ),
    }
    write_json(DEPLOYMENT_ROOT / "routing-analysis" / "contacts-routing-analysis.json", analysis)
    md = "# Contacts routing analysis\n\n" + json.dumps(analysis, ensure_ascii=False, indent=2)
    write_text(DEPLOYMENT_ROOT / "routing-analysis" / "contacts-routing-analysis.md", md)
    return analysis


def build_charter(
    http_rows: list[dict[str, Any]],
    db_data: dict[str, Any],
    sitemap: dict[str, Any],
    links: list[dict[str, Any]],
    routing: dict[str, Any],
) -> dict[str, Any]:
    seo_rows = [
        {"seo_url_id": r[0], "store_id": r[1], "language_id": r[2], "query": r[3], "keyword": r[4]}
        for r in db_data.get("seo_url_contact", []) if len(r) >= 5
    ]
    kontakty_exists = any(r["keyword"] == "kontakty" for r in seo_rows)
    contact_exists = any(r["keyword"] == "contact" and r["query"] == "information/contact" for r in seo_rows)

    charter = {
        "operation_id": "SITE-002-PROD-CONTACTS-URL-ROUTING-IMPLEMENTATION-01",
        "target_final_state": {
            "canonical_url": "/kontakty",
            "expected_http_status": 200,
            "route": "information/contact",
            "information_id": None,
            "seo_url_keyword": "kontakty",
            "seo_url_query": "information/contact",
            "sitemap_inclusion": "automatic via google_sitemap after SEO URL exists",
            "header_footer_links": "/kontakty",
            "redirects": "301 /contact → /kontakty only if /contact currently canonical and indexed",
            "canonical_tag": "https://bzpm.ru/kontakty",
        },
        "recommended_option": routing.get("recommended_implementation_option", "A"),
        "recommended_option_label": {
            "A": "SEO URL for native information/contact with keyword kontakty",
            "B": "SEO URL for information page information_id=N",
            "C": "301 redirect only",
            "D": "source route patch",
            "E": "hybrid SEO URL + header/footer + sitemap",
        }.get(routing.get("recommended_implementation_option", "A"), "hybrid"),
        "production_mutation_plan": {
            "db_rows": [] if kontakty_exists else [
                {
                    "table": "oc_seo_url",
                    "action": "INSERT",
                    "store_id": 0,
                    "language_id": 1,
                    "query": "information/contact",
                    "keyword": "kontakty",
                }
            ],
            "source_files": [],
            "redirects": [],
            "cache_clear": "seo_url / seo_pro cache after SEO URL insert",
            "admin_save": "none if SEO URL inserted via controlled SQL",
        },
        "rollback_plan": {
            "backup_seo_url_rows": "export oc_seo_url WHERE keyword='kontakty' OR query='information/contact'",
            "reverse": "DELETE inserted seo_url row; restore header/footer if changed",
        },
        "verification_plan": [
            "GET /kontakty → 200",
            "canonical https://bzpm.ru/kontakty",
            "H1/title contain Контакты",
            "contact form present if native route",
            "internal header/footer links → /kontakty",
            "sitemap contains /kontakty",
            "robots.txt / llms.txt unchanged",
            "0 public БЗПМ on contacts page",
            "regression: /, /katalog, /lari nested URL",
        ],
        "no_go_conditions": [
            "no contacts owner found",
            "duplicate keyword conflict on kontakty",
            "header/footer authority ambiguous",
            "native contact form mail flow unknown",
        ],
        "current_db_state": {
            "kontakty_seo_exists": kontakty_exists,
            "contact_seo_exists": contact_exists,
            "seo_records": seo_rows,
        },
        "current_http_state": {
            "kontakty_status": next((r["http_status"] for r in http_rows if r["url"].endswith("/kontakty")), None),
            "native_contact_status": next(
                (r["http_status"] for r in http_rows if "route=information/contact" in r["url"]), None
            ),
        },
    }
    write_json(
        DEPLOYMENT_ROOT / "implementation-charter" / "SITE-002-PROD-CONTACTS-URL-ROUTING-IMPLEMENTATION-CHARTER.json",
        charter,
    )
    md = "# SITE-002 Contacts URL Routing — Implementation Charter\n\n"
    md += json.dumps(charter, ensure_ascii=False, indent=2)
    write_text(
        DEPLOYMENT_ROOT / "implementation-charter" / "SITE-002-PROD-CONTACTS-URL-ROUTING-IMPLEMENTATION-CHARTER.md",
        md,
    )
    return charter


def determine_verdict(http_rows: list[dict[str, Any]], db_data: dict[str, Any], routing: dict[str, Any]) -> str:
    kontakty_known = any(r["url"].endswith("/kontakty") for r in http_rows)
    db_ok = bool(db_data.get("information_by_title") is not None or db_data.get("seo_url_contact") is not None)
    owner_known = routing.get("contacts_owner") != "SAFE UNKNOWN" and (
        routing.get("native_contact_http_status") == 200 or db_data.get("information_by_title")
    )
    if kontakty_known and db_ok and owner_known:
        return "SITE-002 CONTACTS URL ROUTING REVIEW COMPLETE — IMPLEMENTATION CHARTER READY"
    if kontakty_known and not db_ok:
        return "SITE-002 CONTACTS URL ROUTING REVIEW PARTIAL — DB STRUCTURE SAFE UNKNOWN"
    if kontakty_known and not owner_known:
        return "SITE-002 CONTACTS URL ROUTING REVIEW PARTIAL — CONTACTS OWNER SAFE UNKNOWN"
    return "SITE-002 CONTACTS URL ROUTING REVIEW BLOCKED — NO MUTATION PERFORMED"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-db", action="store_true")
    parser.add_argument("--skip-ftp", action="store_true")
    args = parser.parse_args()

    ensure_dirs()
    write_json(DEPLOYMENT_ROOT / "logs" / "run-start.json", {"timestamp": utc_now(), "operation_id": OPERATION_ID})

    http_rows = phase_http()
    links = phase_links()
    sitemap = phase_sitemap()
    ftp_rows = phase_ftp() if not args.skip_ftp else []
    db_data: dict[str, Any] = {}
    if not args.skip_db:
        db_data = phase_db()
    routing = build_routing_analysis(http_rows, db_data, sitemap, links, ftp_rows)
    charter = build_charter(http_rows, db_data, sitemap, links, routing)
    verdict = determine_verdict(http_rows, db_data, routing)

    summary = {
        "operation_id": OPERATION_ID,
        "ocpilot_run": OCPILOT_RUN,
        "timestamp": utc_now(),
        "verdict": verdict,
        "http_urls_checked": len(http_rows),
        "ftp_downloads": sum(1 for r in ftp_rows if r.get("downloaded")),
        "db_available": bool(db_data.get("seo_url_contact") is not None or db_data.get("information_by_title") is not None),
        "kontakty_status": next((r["http_status"] for r in http_rows if r["url"].endswith("/kontakty")), None),
        "canonical_current": routing.get("canonical_contacts_url_current"),
        "recommended_option": routing.get("recommended_implementation_option"),
        "sitemap_kontakty": sitemap.get("kontakty_in_sitemap"),
    }
    write_json(DEPLOYMENT_ROOT / "logs" / "final-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
