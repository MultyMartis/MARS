#!/usr/bin/env python3
"""SITE-002 Production category Lari reparent discovery — read-only (Run 4.234)."""
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

OPERATION_ID = "SITE-002-PROD-CATEGORY-LARI-REPARENT-DISCOVERY-01"
OCPILOT_RUN = "4.234"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION_READ_ONLY"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
WRONG_BRAND = "БЗПМ"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
KNOWN_CATEGORY_IDS = (79, 80, 86, 88, 140, 141, 358, 360)
CATEGORY_NAMES = ("Лари", "Шкафы и лари", "Нейтральное оборудование", "Складские лари", "Производственные лари", "Стеллажи")

SUBDIRS = (
    "http-snapshots",
    "db-readonly",
    "ftp-source",
    "sitemap",
    "entrypoints",
    "seo-url",
    "breadcrumbs",
    "one-c",
    "analysis",
    "implementation-charter",
    "manifests",
    "reports",
    "logs",
)

HTTP_URLS = [
    ("primary", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari", "current_wrong"),
    ("primary", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari", "current_parent"),
    ("primary", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari", "target_future"),
    ("parent", "https://bzpm.ru/katalog", "stable"),
    ("parent", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie", "stable"),
    ("child", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/skladskie-lari", "current_child"),
    ("child", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari/proizvodstvennye-lari", "current_child"),
    ("child", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/skladskie-lari", "target_child"),
    ("child", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/proizvodstvennye-lari", "target_child"),
    ("regression", "https://bzpm.ru/", "stable"),
    ("regression", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly", "stable"),
    ("regression", "https://bzpm.ru/sitemap.xml", "stable"),
    ("regression", "https://bzpm.ru/robots.txt", "stable"),
    ("regression", "https://bzpm.ru/llms.txt", "stable"),
]

FTP_PATHS = [
    ("/public_html/system/library/zpm/category_visibility.php", "homepage/hub/megamenu whitelist"),
    ("/public_html/catalog/controller/common/home.php", "homepage controller"),
    ("/public_html/catalog/controller/product/category.php", "category/hub controller"),
    ("/public_html/catalog/controller/extension/feed/google_sitemap.php", "sitemap feed"),
    ("/public_html/catalog/controller/startup/seo_url.php", "SEO URL routing"),
    ("/public_html/catalog/controller/common/import_1C.php", "1C catalog import entry"),
    ("/public_html/catalog/controller/common/import_1C_process.php", "1C category/product processor"),
    ("/public_html/public_html/.htaccess", "htaccess redirects"),
    ("/public_html/.htaccess", "htaccess redirects"),
]

IMPORT_LOG_CANDIDATES = [
    DEPLOYMENT_ROOT.parent / "SITE-002-POST-1C-IMPORT-LOGS-AND-MONITOR-ARTIFACTS-AUDIT-01" / "server-downloads" / "mars_1c_import_2026-07-08_080008.txt",
    DEPLOYMENT_ROOT.parent / "SITE-002-POST-1C-IMPORT-LOGS-AND-MONITOR-ARTIFACTS-AUDIT-01" / "server-downloads" / "mars_1c_import_20260708.log",
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
        self.body_class = ""
        self.in_breadcrumb = False
        self.breadcrumb_parts: list[str] = []
        self.breadcrumb_links: list[str] = []
        self.cat_cards: list[dict[str, str]] = []
        self._capture_link = False
        self._current_text = ""
        self._in_tile_title = False
        self._tile_href = ""
        self._tile_title = ""
        self.product_count_text = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: (v or "") for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = True
        elif tag_l == "h1":
            self.in_h1 = True
        elif tag_l == "body":
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
        elif tag_l == "a":
            href = attrs_dict.get("href", "")
            classes = attrs_dict.get("class", "")
            if "breadcrumb" in classes or "zpm-breadcrumb" in classes:
                self.in_breadcrumb = True
                self._capture_link = True
                self._current_text = ""
                if href:
                    self.breadcrumb_links.append(href)
            if "zpm-catalog__tile" in classes or "zpm-cat-card" in classes:
                self._tile_href = href
                self._tile_title = ""
        elif tag_l == "span" and "zpm-catalog__tile-title" in attrs_dict.get("class", ""):
            self._in_tile_title = True
            self._tile_title = ""

    def handle_endtag(self, tag: str) -> None:
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = False
        elif tag_l == "h1":
            self.in_h1 = False
        elif tag_l == "a" and self.in_breadcrumb:
            self.in_breadcrumb = False
            self._capture_link = False
        elif tag_l == "span" and self._in_tile_title:
            self._in_tile_title = False
            if self._tile_href or self._tile_title:
                self.cat_cards.append({"href": self._tile_href, "title": self._tile_title.strip()})
                self._tile_href = ""
                self._tile_title = ""

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if not text:
            return
        if self.in_title:
            self.title += data
        if self.in_h1:
            self.h1_list.append(text)
        if self.in_breadcrumb:
            self.breadcrumb_parts.append(text)
        if self._in_tile_title:
            self._tile_title += data
        if "товар" in text.lower() and ("показано" in text.lower() or "найдено" in text.lower()):
            self.product_count_text = text


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


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
            "change_type": "category-reparent-discovery",
            "category_subject": "Лари",
            "current_expected_wrong_url": "/katalog/nejtralnoe-oborudovanie/lari",
            "target_expected_url": "/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari",
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
            return {"url": url, "status": None, "final_url": url, "redirect_chain": chain, "body": b"", "error": str(exc)}
    return {"url": url, "status": None, "final_url": url, "redirect_chain": chain, "body": b"", "error": "redirect loop"}


def parse_html_page(body: bytes) -> dict[str, Any]:
    text = body.decode("utf-8", errors="replace")
    parser = PageParser()
    parser.feed(text)
    canonical = ""
    for link in parser.links:
        if link.get("rel") == "canonical":
            canonical = link.get("href", "")
    breadcrumbs = " / ".join(parser.breadcrumb_parts)
    return {
        "title": parser.title.strip(),
        "meta_description": parser.meta.get("description", ""),
        "meta_robots": parser.meta.get("robots", ""),
        "canonical": canonical,
        "h1": " | ".join([h for h in parser.h1_list if h]),
        "breadcrumbs_text": breadcrumbs,
        "breadcrumbs_links": parser.breadcrumb_links,
        "category_cards": parser.cat_cards,
        "product_count_text": parser.product_count_text,
        "body_class": parser.body_class,
        "bzpm_hits": text.count(WRONG_BRAND),
        "html": text,
    }


def phase_http() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for group, url, path_class in HTTP_URLS:
        time.sleep(0.35)
        resp = http_fetch(url)
        parsed: dict[str, Any] = {}
        if resp.get("body"):
            parsed = parse_html_page(resp["body"])
            slug = re.sub(r"[^a-zA-Z0-9._-]+", "_", url.replace("https://bzpm.ru/", ""))[:120]
            write_text(DEPLOYMENT_ROOT / "http-snapshots" / f"{slug or 'root'}.html", parsed.pop("html", ""))
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
            "canonical": parsed.get("canonical", ""),
            "h1": parsed.get("h1", ""),
            "breadcrumbs_text": parsed.get("breadcrumbs_text", ""),
            "breadcrumbs_links": json.dumps(parsed.get("breadcrumbs_links", []), ensure_ascii=False),
            "category_cards_count": len(parsed.get("category_cards", [])),
            "category_cards": json.dumps(parsed.get("category_cards", []), ensure_ascii=False),
            "product_count_text": parsed.get("product_count_text", ""),
            "meta_robots": parsed.get("meta_robots", ""),
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
        md.append(f"- Path class: {r['path_class']}\n")
        md.append(f"- Title: {r['title']}\n")
        md.append(f"- Canonical: {r['canonical']}\n")
        md.append(f"- H1: {r['h1']}\n")
        md.append(f"- Breadcrumbs: {r['breadcrumbs_text']}\n")
        md.append(f"- Category cards: {r['category_cards_count']}\n")
        md.append(f"- БЗПМ hits: {r['bzpm_hits']}\n\n")
    write_text(DEPLOYMENT_ROOT / "http-snapshots" / "http-url-status.md", "".join(md))
    return rows


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
    checks = {
        "contains_88": "88" in content,
        "contains_86": "86" in content,
        "contains_358": "358" in content,
        "contains_lari": "lari" in content.lower() or "Лари" in content,
        "contains_shkafy_i_lari": "shkafy-i-lari" in content.lower() or "Шкафы и лари" in content,
        "contains_whitelist": "neutral_hub_branch_ids" in content or "getNeutralHubBranchIds" in content,
    }
    needs_change = "unknown"
    reason = ""
    if "neutral_hub_branch_ids" in content and "88" in content:
        needs_change = "maybe"
        reason = "Static whitelist includes category 88 (Лари) as top-level neutral branch; may need review after reparent"
    if "import_1C" in remote_path or "import_1C_process" in remote_path:
        needs_change = "review"
        reason = "1C import may own category parent relations — verify before manual reparent"
    if "google_sitemap" in remote_path:
        needs_change = "no"
        reason = "Dynamic sitemap from DB category tree — should update after parent/path change"
    if "seo_url" in remote_path:
        needs_change = "no"
        reason = "Routing layer — path derived from category_path + seo_url keywords"
    if ".htaccess" in remote_path:
        needs_change = "redirect_phase"
        reason = "May need 301 rules for old /lari paths after reparent"
    return {
        "remote_path": remote_path,
        "role": role,
        "bytes": len(content.encode("utf-8", errors="replace")),
        "contains_static_category_id": checks["contains_88"] or checks["contains_86"] or checks["contains_358"],
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
            if data is None and remote_path.startswith("/public_html/public_html/"):
                alt = remote_path.replace("/public_html/public_html/", "/public_html/", 1)
                data = ftp_download_file(ftp, alt)
                if data is not None:
                    remote_path = alt
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
                row = {**row_base, "downloaded": False, "likely_needs_implementation_change": "unknown", "reason": "file not found"}
            rows.append(row)
    finally:
        ftp.quit()
    fields = [
        "remote_path", "role", "downloaded", "contains_static_category_id", "contains_88", "contains_86",
        "contains_358", "contains_lari", "contains_shkafy_i_lari", "contains_whitelist",
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
    prefix_probe = ssh_mysql_query(
        "SHOW TABLES LIKE '%category%'"
    )
    result: dict[str, Any] = {"prefix_probe": prefix_probe, "queries": []}
    if prefix_probe.get("status") != "ok":
        write_json(DEPLOYMENT_ROOT / "db-readonly" / "db-status.json", result)
        return result

    tables = [line.strip() for line in prefix_probe.get("stdout", "").splitlines() if line.strip()]
    prefix = "oc_"
    if tables and not tables[0].startswith("oc_"):
        prefix = tables[0].split("category")[0] if "category" in tables[0] else "oc_"

    ids_csv = ",".join(str(i) for i in KNOWN_CATEGORY_IDS)
    names_csv = ",".join(f"'{n}'" for n in CATEGORY_NAMES)

    queries = {
        "category_by_id": f"""
            SELECT c.category_id, c.parent_id, c.status, c.sort_order, c.image, c.date_added, c.date_modified,
                   cd.name, cd.meta_title, cd.meta_description, LENGTH(cd.description) AS desc_len, cd.language_id
            FROM {prefix}category c
            JOIN {prefix}category_description cd ON c.category_id = cd.category_id
            WHERE c.category_id IN ({ids_csv}) AND cd.language_id = 1
            ORDER BY c.category_id
        """,
        "category_by_name": f"""
            SELECT c.category_id, c.parent_id, cd.name
            FROM {prefix}category c
            JOIN {prefix}category_description cd ON c.category_id = cd.category_id
            WHERE cd.name IN ({names_csv}) AND cd.language_id = 1
            ORDER BY cd.name, c.category_id
        """,
        "category_path": f"""
            SELECT cp.category_id, cp.path_id, cp.level
            FROM {prefix}category_path cp
            WHERE cp.category_id IN ({ids_csv}) OR cp.path_id IN ({ids_csv})
            ORDER BY cp.category_id, cp.level
        """,
        "seo_url": f"""
            SELECT seo_url_id, store_id, language_id, query, keyword
            FROM {prefix}seo_url
            WHERE query IN ({','.join(f"'category_id={i}'" for i in KNOWN_CATEGORY_IDS)})
               OR keyword LIKE '%lari%'
            ORDER BY query, keyword
        """,
        "product_counts": f"""
            SELECT c.category_id, cd.name,
                   COUNT(DISTINCT p2c.product_id) AS direct_products,
                   COUNT(DISTINCT CASE WHEN p.status = 1 THEN p2c.product_id END) AS active_products
            FROM {prefix}category c
            JOIN {prefix}category_description cd ON c.category_id = cd.category_id AND cd.language_id = 1
            LEFT JOIN {prefix}product_to_category p2c ON c.category_id = p2c.category_id
            LEFT JOIN {prefix}product p ON p2c.product_id = p.product_id
            WHERE c.category_id IN ({ids_csv})
            GROUP BY c.category_id, cd.name
            ORDER BY c.category_id
        """,
        "child_counts": f"""
            SELECT parent.category_id AS parent_id, pd.name AS parent_name,
                   COUNT(child.category_id) AS child_count
            FROM {prefix}category parent
            JOIN {prefix}category_description pd ON parent.category_id = pd.category_id AND pd.language_id = 1
            LEFT JOIN {prefix}category child ON child.parent_id = parent.category_id
            WHERE parent.category_id IN ({ids_csv})
            GROUP BY parent.category_id, pd.name
        """,
        "lari_children": f"""
            SELECT c.category_id, c.parent_id, cd.name
            FROM {prefix}category c
            JOIN {prefix}category_description cd ON c.category_id = cd.category_id AND cd.language_id = 1
            WHERE c.parent_id IN (88, 358)
            ORDER BY c.parent_id, c.sort_order, cd.name
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

    # category-structure.csv
    cat_rows: list[dict[str, Any]] = []
    for row in parsed_data.get("category_by_id", []):
        if len(row) >= 12:
            cat_rows.append({
                "category_id": row[0], "parent_id": row[1], "status": row[2], "sort_order": row[3],
                "image": row[4], "date_added": row[5], "date_modified": row[6], "name": row[7],
                "meta_title": row[8], "meta_description": row[9], "description_length": row[10], "language_id": row[11],
            })
    if cat_rows:
        write_csv(
            DEPLOYMENT_ROOT / "db-readonly" / "category-structure.csv",
            cat_rows,
            list(cat_rows[0].keys()),
        )
        write_json(DEPLOYMENT_ROOT / "db-readonly" / "category-structure.json", cat_rows)

    path_rows: list[dict[str, Any]] = []
    for row in parsed_data.get("category_path", []):
        if len(row) >= 3:
            path_rows.append({"category_id": row[0], "path_id": row[1], "level": row[2]})
    if path_rows:
        write_csv(DEPLOYMENT_ROOT / "db-readonly" / "category-paths.csv", path_rows, list(path_rows[0].keys()))

    seo_rows: list[dict[str, Any]] = []
    for row in parsed_data.get("seo_url", []):
        if len(row) >= 5:
            seo_rows.append({
                "seo_url_id": row[0], "store_id": row[1], "language_id": row[2], "query": row[3], "keyword": row[4],
            })
    if seo_rows:
        write_csv(DEPLOYMENT_ROOT / "db-readonly" / "seo-url-records.csv", seo_rows, list(seo_rows[0].keys()))

    prod_rows: list[dict[str, Any]] = []
    for row in parsed_data.get("product_counts", []):
        if len(row) >= 4:
            prod_rows.append({
                "category_id": row[0], "name": row[1], "direct_products": row[2], "active_products": row[3],
            })
    if prod_rows:
        write_csv(DEPLOYMENT_ROOT / "db-readonly" / "product-category-counts.csv", prod_rows, list(prod_rows[0].keys()))

    md = ["# DB category structure (read-only)\n\n", f"Prefix: `{parsed_data.get('prefix')}`\n\n"]
    for c in cat_rows:
        md.append(f"## {c['name']} (id {c['category_id']})\n")
        md.append(f"- parent_id: {c['parent_id']}\n")
        md.append(f"- status: {c['status']}\n\n")
    write_text(DEPLOYMENT_ROOT / "db-readonly" / "category-structure.md", "".join(md))
    return parsed_data


def extract_cards_from_html(html: str, selector_class: str = "zpm-catalog__tile-title") -> list[dict[str, str]]:
    cards: list[dict[str, str]] = []
    for m in re.finditer(
        r'<a[^>]+class="[^"]*(?:zpm-cat-card|zpm-catalog__tile)[^"]*"[^>]+href="([^"]+)"[^>]*>.*?'
        r'<span[^>]+class="[^"]*zpm-catalog__tile-title[^"]*"[^>]*>([^<]+)</span>',
        html,
        re.DOTALL | re.IGNORECASE,
    ):
        cards.append({"href": m.group(1), "title": m.group(2).strip()})
    if not cards:
        for m in re.finditer(r'class="zpm-catalog__tile-title"[^>]*>([^<]+)<', html):
            cards.append({"href": "", "title": m.group(1).strip()})
    return cards


def extract_megamenu(html: str) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for m in re.finditer(
        r'<a[^>]+href="([^"]*nejtralnoe-oborudovanie[^"]*)"[^>]*>([^<]+)</a>',
        html,
        re.IGNORECASE,
    ):
        title = re.sub(r"\s+", " ", m.group(2)).strip()
        if title and len(title) < 80:
            items.append({"href": m.group(1), "title": title})
    seen: set[str] = set()
    deduped: list[dict[str, str]] = []
    for it in items:
        key = (it["href"], it["title"])
        if key not in seen:
            seen.add(key)
            deduped.append(it)
    return deduped


def phase_entrypoints(http_rows: list[dict[str, Any]]) -> dict[str, Any]:
    home_html = (DEPLOYMENT_ROOT / "http-snapshots" / "index.html").read_text(encoding="utf-8", errors="replace") if (DEPLOYMENT_ROOT / "http-snapshots" / "index.html").exists() else ""
    if not home_html:
        for f in DEPLOYMENT_ROOT.glob("http-snapshots/*.html"):
            if "home" in f.name or f.name in ("index.html",):
                home_html = f.read_text(encoding="utf-8", errors="replace")
                break
    # Re-fetch key pages for card extraction
    pages = {
        "homepage": "https://bzpm.ru/",
        "catalog": "https://bzpm.ru/katalog",
        "neutral_hub": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
        "shkafy_i_lari": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari",
    }
    entry: dict[str, Any] = {}
    for key, url in pages.items():
        slug = re.sub(r"[^a-zA-Z0-9._-]+", "_", url.replace("https://bzpm.ru/", ""))[:120]
        html_path = DEPLOYMENT_ROOT / "http-snapshots" / f"{slug or 'root'}.html"
        html = html_path.read_text(encoding="utf-8", errors="replace") if html_path.exists() else ""
        cards = extract_cards_from_html(html)
        entry[key] = {"url": url, "cards": cards}
        write_csv(
            DEPLOYMENT_ROOT / "entrypoints" / f"{key.replace(' ', '-')}-categories.csv",
            [{"title": c["title"], "href": c["href"]} for c in cards],
            ["title", "href"],
        )

    home_cards = entry.get("homepage", {}).get("cards", [])
    hub_cards = entry.get("neutral_hub", {}).get("cards", [])
    shkafy_cards = entry.get("shkafy_i_lari", {}).get("cards", [])

    home_html_path = DEPLOYMENT_ROOT / "http-snapshots"
    for f in home_html_path.glob("*.html"):
        if f.name in ("katalog.html",) or "nejtralnoe-oborudovanie.html" in f.name:
            continue
        if "stoly" not in f.name and "sitemap" not in f.name and "robots" not in f.name and "llms" not in f.name:
            if "lari" not in f.name and "shkafy" not in f.name and "skladskie" not in f.name and "proizvodstvennye" not in f.name:
                candidate = f.read_text(encoding="utf-8", errors="replace")
                if "zpm-cat-card" in candidate or "zpm-catalog__tile" in candidate:
                    home_html = candidate
                    home_cards = extract_cards_from_html(candidate)
                    break

    megamenu = extract_megamenu(home_html)
    write_csv(
        DEPLOYMENT_ROOT / "entrypoints" / "megamenu-categories.csv",
        megamenu,
        ["title", "href"],
    )

    analysis = {
        "homepage": {
            "lari_top_level": any("lari" in c.get("href", "") and "shkafy" not in c.get("href", "") for c in home_cards),
            "shkafy_top_level": any("shkafy-i-lari" in c.get("href", "") for c in home_cards),
            "cards": home_cards,
            "order_az": [c["title"] for c in home_cards],
            "generation": "whitelist via category_visibility.php + dynamic sort (Run 4.221)",
        },
        "neutral_hub": {
            "lari_direct_child": any("lari" in c.get("href", "") and "shkafy" not in c.get("href", "") for c in hub_cards),
            "shkafy_direct_child": any("shkafy-i-lari" in c.get("href", "") for c in hub_cards),
            "cards": hub_cards,
        },
        "shkafy_i_lari_page": {
            "lari_absent": not any("lari" in c.get("href", "") for c in shkafy_cards),
            "child_cards": shkafy_cards,
        },
        "megamenu": megamenu,
        "future_change_classification": {
            "homepage_after_reparent": "lari remains in whitelist as branch tile but href should update if SEO path changes; may stay top-level marketing tile OR move under shkafy only on hub tree",
            "neutral_hub_after_reparent": "lari should disappear as direct child; appear under shkafy-i-lari",
            "whitelist": "DB-only may be enough if tile hrefs are dynamic from category model; whitelist ID 88 can remain",
        },
    }
    write_json(DEPLOYMENT_ROOT / "entrypoints" / "entrypoint-analysis.json", analysis)
    write_text(
        DEPLOYMENT_ROOT / "entrypoints" / "entrypoint-analysis.md",
        "# Entrypoint analysis\n\n" + json.dumps(analysis, ensure_ascii=False, indent=2),
    )
    return analysis


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
        "/katalog/nejtralnoe-oborudovanie/lari",
        "/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari",
        "/skladskie-lari",
        "/proizvodstvennye-lari",
        "/shkafy-i-lari",
    ]
    pattern_hits: dict[str, list[str]] = {p: [] for p in patterns}
    for loc in locs:
        for p in patterns:
            if p in loc:
                pattern_hits[p].append(loc)

    row = {
        "total_loc_count": len(locs),
        "old_lari_url_present": any("/nejtralnoe-oborudovanie/lari" in x and "/shkafy-i-lari/" not in x for x in locs),
        "target_lari_url_present": any("/shkafy-i-lari/lari" in x for x in locs),
        "old_child_skladskie_present": any("/lari/skladskie-lari" in x and "/shkafy-i-lari/" not in x for x in locs),
        "old_child_proizvodstvennye_present": any("/lari/proizvodstvennye-lari" in x and "/shkafy-i-lari/" not in x for x in locs),
        "target_child_skladskie_present": any("/shkafy-i-lari/lari/skladskie-lari" in x for x in locs),
        "target_child_proizvodstvennye_present": any("/shkafy-i-lari/lari/proizvodstvennye-lari" in x for x in locs),
        "sitemap_dynamic": True,
        "update_mechanism": "OpenCart extension/feed/google_sitemap reads category tree from DB",
        "pattern_hits": pattern_hits,
    }
    write_json(DEPLOYMENT_ROOT / "sitemap" / "sitemap-lari-analysis.json", row)
    write_csv(
        DEPLOYMENT_ROOT / "sitemap" / "sitemap-lari-analysis.csv",
        [{"pattern": k, "count": len(v), "sample": v[0] if v else ""} for k, v in pattern_hits.items()],
        ["pattern", "count", "sample"],
    )
    write_text(
        DEPLOYMENT_ROOT / "sitemap" / "sitemap-lari-analysis.md",
        "# Sitemap Lari analysis\n\n" + json.dumps(row, ensure_ascii=False, indent=2),
    )

    redirects = {
        "recommendations": [
            {
                "from": "/katalog/nejtralnoe-oborudovanie/lari",
                "to": "/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari",
                "type": "301",
                "reason": "Old indexed/sitemaped URL after reparent",
            },
            {
                "from": "/katalog/nejtralnoe-oborudovanie/lari/skladskie-lari",
                "to": "/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/skladskie-lari",
                "type": "301",
                "reason": "Child path changes with parent",
            },
            {
                "from": "/katalog/nejtralnoe-oborudovanie/lari/proizvodstvennye-lari",
                "to": "/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/proizvodstvennye-lari",
                "type": "301",
                "reason": "Child path changes with parent",
            },
        ],
        "implement_in": ".htaccess or OpenCart SEO redirect layer — discovery only",
    }
    write_json(DEPLOYMENT_ROOT / "seo-url" / "redirect-recommendations.json", redirects)
    write_text(
        DEPLOYMENT_ROOT / "seo-url" / "redirect-recommendations.md",
        "# Redirect recommendations (not implemented)\n\n" + json.dumps(redirects, ensure_ascii=False, indent=2),
    )
    return row


def phase_one_c(ftp_rows: list[dict[str, Any]]) -> dict[str, Any]:
    import_text = ""
    process_text = ""
    for r in ftp_rows:
        if r.get("downloaded") and "import_1C_process" in r.get("remote_path", ""):
            p = DEPLOYMENT_ROOT / "ftp-source" / local_ftp_name(r["remote_path"])
            if p.exists():
                process_text = p.read_text(encoding="utf-8", errors="replace")
        if r.get("downloaded") and r.get("remote_path", "").endswith("import_1C.php"):
            p = DEPLOYMENT_ROOT / "ftp-source" / local_ftp_name(r["remote_path"])
            if p.exists():
                import_text = p.read_text(encoding="utf-8", errors="replace")

    signals = {
        "imports_categories": bool(re.search(r"category", import_text + process_text, re.I)),
        "updates_parent": bool(re.search(r"parent_id", process_text)),
        "updates_category_path": bool(re.search(r"category_path", process_text)),
        "preserves_manual": "SAFE UNKNOWN — requires XML sample + diff on next import",
        "lari_imported_or_manual": "LIKELY MIXED — Лари id 88 onboarded Run 4.210/4.211 with admin SEO; 1C daily growth adds products/categories",
    }

    ownership = {
        "classification": "mixed",
        "1c_authoritative_for": ["new categories from XML", "product-category links", "product data"],
        "opencart_authoritative_for": ["manual admin SEO", "category_visibility whitelist", "demo/onboarding branches"],
        "reparent_risk": "1C import may reset parent_id if category xml_id exists in feed with different parent",
        "recommended_path": "Verify 1C XML group hierarchy for Лари under Шкафы и лари before manual reparent; hybrid: 1C-side fix OR one-time reparent + import wrapper guard",
        "signals": signals,
        "import_log_available": any(p.exists() for p in IMPORT_LOG_CANDIDATES),
    }
    write_json(DEPLOYMENT_ROOT / "one-c" / "one-c-category-ownership.json", ownership)
    write_text(
        DEPLOYMENT_ROOT / "one-c" / "one-c-category-ownership.md",
        "# 1C category ownership\n\n" + json.dumps(ownership, ensure_ascii=False, indent=2),
    )
    return ownership


def build_charter(http_rows: list[dict[str, Any]], db_data: dict[str, Any], entry: dict[str, Any], sitemap: dict[str, Any], one_c: dict[str, Any]) -> dict[str, Any]:
    lari_parent = "SAFE UNKNOWN"
    shkafy_id = "358"
    for row in db_data.get("category_by_id", []):
        if len(row) >= 2 and row[0] == "88":
            lari_parent = row[1]
        if len(row) >= 8 and "Шкафы" in row[7]:
            shkafy_id = row[0]

    charter = {
        "operation_id": "SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION",
        "target_final_state": {
            "lari_category_id": 88,
            "shkafy_i_lari_category_id": int(shkafy_id) if str(shkafy_id).isdigit() else shkafy_id,
            "neutral_hub_category_id": 79,
            "lari_children_ids": [140, 141],
            "old_url": "/katalog/nejtralnoe-oborudovanie/lari",
            "new_url": "/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari",
            "current_parent_id": lari_parent,
            "target_parent_id": shkafy_id,
            "breadcrumbs_target": "Каталог / Нейтральное оборудование / Шкафы и лари / Лари",
            "sitemap": "Auto-regenerate via google_sitemap after DB path update",
            "homepage_whitelist": "ID 88 may remain in neutral_hub_branch_ids; href becomes new path if dynamic",
            "redirects": "301 old lari + child paths strongly recommended",
        },
        "options": {
            "A_db_migration": "UPDATE parent_id; rebuild category_path for 88+descendants; verify seo_url; add redirects",
            "B_admin_save": "OpenCart admin change parent — triggers path rebuild; still need redirects",
            "C_1c_correction": "Fix 1C export hierarchy so import sets correct parent",
            "D_hybrid": "1C verify + admin/DB reparent + redirect + post-import monitor",
        },
        "recommended": "D_hybrid — verify 1C XML parent first; then OpenCart admin reparent (safer path rebuild) OR controlled DB script; add 301 redirects; run post-1C monitor after next import",
        "tables_likely_touched": ["oc_category", "oc_category_path", "oc_seo_url (verify only)", "public_html/.htaccess (redirects)"],
        "files_likely_touched": ["category_visibility.php (only if whitelist semantics change)", ".htaccess"],
        "backup_plan": ["Export oc_category/category_path/seo_url rows for ids 88,140,141,358,79", "FTP backup .htaccess", "Rollback SQL for parent_id and category_path"],
        "verification_plan": [
            "Old /lari URLs return 301",
            "New /shkafy-i-lari/lari 200",
            "Breadcrumbs and canonical on new path",
            "Sitemap old URLs absent, new present",
            "Homepage/hub cards hrefs correct",
            "Child PLPs under new paths",
            "Next 1C import does not revert parent",
        ],
        "risks": [
            "SEO keyword duplicate for lari segment",
            "1C import reverting parent_id",
            "Child category_path cascade",
            "External indexed old URLs",
            "Whitelist shows wrong hierarchy if static hrefs",
        ],
        "no_go_conditions": [
            "1C will revert on next import without guard",
            "category_id 88 mismatch",
            "duplicate seo keyword conflict unresolved",
        ],
    }
    write_json(DEPLOYMENT_ROOT / "implementation-charter" / "SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-CHARTER.json", charter)
    md = "# SITE-002 Category Lari Reparent — Implementation Charter\n\n"
    md += json.dumps(charter, ensure_ascii=False, indent=2)
    write_text(DEPLOYMENT_ROOT / "implementation-charter" / "SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-CHARTER.md", md)
    return charter


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-db", action="store_true")
    parser.add_argument("--skip-ftp", action="store_true")
    args = parser.parse_args()

    ensure_dirs()
    write_json(DEPLOYMENT_ROOT / "logs" / "run-start.json", {"timestamp": utc_now(), "operation_id": OPERATION_ID})

    http_rows = phase_http()
    ftp_rows = phase_ftp() if not args.skip_ftp else []
    db_data: dict[str, Any] = {}
    if not args.skip_db:
        db_data = phase_db()
    entry = phase_entrypoints(http_rows)
    sitemap = phase_sitemap()
    one_c = phase_one_c(ftp_rows)
    charter = build_charter(http_rows, db_data, entry, sitemap, one_c)

    verdict = "SITE-002 CATEGORY LARI REPARENT DISCOVERY COMPLETE — IMPLEMENTATION CHARTER READY"
    if not db_data.get("category_by_id"):
        verdict = "SITE-002 CATEGORY LARI REPARENT DISCOVERY PARTIAL — DB STRUCTURE SAFE UNKNOWN"

    summary = {
        "operation_id": OPERATION_ID,
        "ocpilot_run": OCPILOT_RUN,
        "timestamp": utc_now(),
        "verdict": verdict,
        "http_urls_checked": len(http_rows),
        "ftp_downloads": sum(1 for r in ftp_rows if r.get("downloaded")),
        "db_available": bool(db_data.get("category_by_id")),
        "sitemap_loc_count": sitemap.get("total_loc_count"),
    }
    write_json(DEPLOYMENT_ROOT / "logs" / "final-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
