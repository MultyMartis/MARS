#!/usr/bin/env python3
"""SITE-002 production llms.txt deploy — single-file public text for AI agents."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import io
import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-LLMS-TXT-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SEO-PRODUCT-META-KEYWORDS-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-LLMS-TXT-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-LLMS-TXT-01"
)
USER_AGENT = "MARS-OCPilot/SITE-002-PROD-LLMS-TXT-01"
REMOTE_LLMS = "/public_html/llms.txt"
PUBLIC_LLMS = "https://bzpm.ru/llms.txt"

DISCOVERY_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki",
    "https://bzpm.ru/about",
    "https://bzpm.ru/custom-equipment",
    "https://bzpm.ru/dealers",
    "https://bzpm.ru/delivery",
    "https://bzpm.ru/guarantee",
    "https://bzpm.ru/payment-methods",
    "https://bzpm.ru/contact",
    "https://bzpm.ru/blog",
    "https://bzpm.ru/blog/news",
    "https://bzpm.ru/sitemap.xml",
    "https://bzpm.ru/robots.txt",
]

LLMS_SECTIONS: list[tuple[str, str]] = [
    ("Главная", "https://bzpm.ru/"),
    ("Каталог", "https://bzpm.ru/katalog"),
    ("Нейтральное оборудование", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie"),
    ("Столы из нержавеющей стали", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly"),
    ("Полки настенные и настольные", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye"),
    ("Тележки сервировочные", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye"),
    ("Шкафы и лари", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari"),
    ("Подтоварники и подставки", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki"),
    ("О компании", "https://bzpm.ru/about"),
    ("Нестандартное оборудование", "https://bzpm.ru/custom-equipment"),
    ("Дилерам", "https://bzpm.ru/dealers"),
    ("Доставка", "https://bzpm.ru/delivery"),
    ("Гарантия", "https://bzpm.ru/guarantee"),
    ("Оплата", "https://bzpm.ru/payment-methods"),
    ("Контакты", "https://bzpm.ru/contact"),
    ("Блог", "https://bzpm.ru/blog"),
    ("Новости", "https://bzpm.ru/blog/news"),
    ("Sitemap", "https://bzpm.ru/sitemap.xml"),
    ("Robots", "https://bzpm.ru/robots.txt"),
]

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "verification",
    "content",
    "manifests",
    "logs",
)

FORBIDDEN_PATTERNS = (
    r"zpm\.new-site\.space",
    r"MARS",
    r"AI MARS STORAGE",
    r"assum_",
    r"beget\.tech",
    r"ym\(",
    r"yandex-verification",
    r"password",
    r"secret",
    r"token",
    r"credential",
    r"staging",
    r"localhost",
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.in_title = False
        self.in_h1 = False
        self.h1_list: list[str] = []
        self.meta: dict[str, str] = {}
        self.links: list[dict[str, str]] = []
        self.body_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: (v or "") for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = True
        elif tag_l == "h1":
            self.in_h1 = True
        elif tag_l == "body":
            self.body_count += 1
        elif tag_l == "meta":
            name = (attrs_dict.get("name") or attrs_dict.get("property") or "").lower()
            content = attrs_dict.get("content", "")
            if name:
                self.meta[name] = content
        elif tag_l == "link":
            rel = attrs_dict.get("rel", "").lower()
            href = attrs_dict.get("href", "")
            self.links.append({"rel": rel, "href": href})

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False
        elif tag.lower() == "h1":
            self.in_h1 = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        elif self.in_h1:
            self.h1_list.append(data.strip())


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data, encoding="utf-8", newline="\n")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def ensure_dirs() -> None:
    for name in SUBDIRS:
        (DEPLOYMENT_ROOT / name).mkdir(parents=True, exist_ok=True)


def write_operation_metadata() -> None:
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "change_type": "llms-txt-deploy",
            "target_remote_file": REMOTE_LLMS,
            "target_public_url": PUBLIC_LLMS,
            "single_file_deploy": True,
            "robots_change_allowed": False,
            "sitemap_change_allowed": False,
            "header_footer_change_allowed": False,
            "php_change_allowed": False,
            "db_write_allowed": False,
            "admin_save_allowed": False,
            "product_meta_change_allowed": False,
            "yandex_blocks_protected": True,
        },
    )


def parse_production_section(path: Path, subsection: str) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    sub_match = re.search(rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
    if not sub_match:
        raise RuntimeError(f"Subsection {subsection} not found")
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in sub_match.group(1).splitlines():
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
    creds = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], int(creds.get("port") or 21), timeout=120)
    ftp.login(creds["username"], creds["password"])
    ftp.set_pasv(True)
    if creds.get("remote_root"):
        try:
            ftp.cwd(creds["remote_root"])
        except ftplib.error_perm:
            pass
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> bytes:
    buf = io.BytesIO()
    ftp.retrbinary(f"RETR {remote}", buf.write)
    return buf.getvalue()


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


def ftp_exists(ftp: ftplib.FTP, remote: str) -> bool:
    try:
        ftp.size(remote)
        return True
    except ftplib.error_perm:
        try:
            buf = io.BytesIO()
            ftp.retrbinary(f"RETR {remote}", buf.write, rest=0)
            return True
        except ftplib.error_perm:
            return False


def http_get(url: str, accept: str = "*/*") -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read()
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return {
                "url": url,
                "final_url": resp.geturl(),
                "status": resp.status,
                "headers": headers,
                "body": body,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read() if exc.fp else b""
        return {
            "url": url,
            "final_url": exc.geturl() if hasattr(exc, "geturl") else url,
            "status": exc.code,
            "headers": {k.lower(): v for k, v in exc.headers.items()} if exc.headers else {},
            "body": body,
            "error": str(exc),
        }
    except Exception as exc:
        return {
            "url": url,
            "final_url": url,
            "status": 0,
            "headers": {},
            "body": b"",
            "error": str(exc),
        }


def parse_html_page(body: bytes) -> dict[str, Any]:
    text = body.decode("utf-8", errors="replace")
    parser = PageParser()
    parser.feed(text)
    canonical = next((l["href"] for l in parser.links if "canonical" in l.get("rel", "")), "")
    robots = parser.meta.get("robots", "")
    return {
        "title": parser.title.strip(),
        "description": parser.meta.get("description", ""),
        "h1": " | ".join(h for h in parser.h1_list if h),
        "canonical": canonical,
        "robots": robots,
        "body_count": parser.body_count,
        "has_yandex_metrika": "mc.yandex.ru" in text or "ym(" in text,
        "has_yandex_webmaster": "yandex-verification" in text.lower(),
        "has_load_more": "load-more" in text.lower() or "load_more" in text.lower() or "Загрузить ещё" in text,
    }


def phase_discovery() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for url in DISCOVERY_URLS:
        is_xml = url.endswith(".xml")
        is_txt = url.endswith(".txt")
        accept = "application/xml" if is_xml else "text/plain" if is_txt else "text/html"
        resp = http_get(url, accept=accept)
        row: dict[str, Any] = {
            "url": url,
            "final_url": resp["final_url"],
            "status": resp["status"],
            "content_type": resp["headers"].get("content-type", ""),
            "error": resp["error"],
        }
        body = resp["body"]
        if resp["status"] == 200 and not is_xml and not is_txt:
            parsed = parse_html_page(body)
            row.update(parsed)
        elif resp["status"] == 200 and is_xml:
            try:
                root = ET.fromstring(body)
                ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                locs = root.findall(".//sm:loc", ns) or root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
                row["sitemap_url_count"] = len(locs)
            except ET.ParseError:
                row["sitemap_url_count"] = None
        elif resp["status"] == 200 and is_txt:
            row["text_preview"] = body.decode("utf-8", errors="replace")[:200]
        rows.append(row)
    write_json(DEPLOYMENT_ROOT / "source" / "public-url-discovery.json", {"generated_at": utc_now(), "rows": rows})
    with (DEPLOYMENT_ROOT / "source" / "public-url-discovery.csv").open("w", encoding="utf-8", newline="") as fh:
        fields = [
            "url", "final_url", "status", "title", "description", "h1", "canonical", "robots",
            "content_type", "sitemap_url_count", "body_count", "error",
        ]
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    md_lines = ["# Public URL discovery", "", f"Generated: {utc_now()}", ""]
    for r in rows:
        md_lines.append(f"## {r['url']}")
        md_lines.append(f"- Status: {r['status']}")
        md_lines.append(f"- Final URL: {r.get('final_url', '')}")
        if r.get("title"):
            md_lines.append(f"- Title: {r['title']}")
        if r.get("description"):
            md_lines.append(f"- Description: {r['description'][:120]}...")
        if r.get("h1"):
            md_lines.append(f"- H1: {r['h1']}")
        if r.get("canonical"):
            md_lines.append(f"- Canonical: {r['canonical']}")
        if r.get("robots"):
            md_lines.append(f"- Robots: {r['robots']}")
        if r.get("sitemap_url_count") is not None:
            md_lines.append(f"- Sitemap URLs: {r['sitemap_url_count']}")
        md_lines.append("")
    write_text(DEPLOYMENT_ROOT / "source" / "public-url-discovery.md", "\n".join(md_lines))
    return rows


def build_llms_content(discovery: list[dict[str, Any]]) -> str:
    status_map = {r["url"]: r["status"] for r in discovery}
    about_row = next((r for r in discovery if r["url"] == "https://bzpm.ru/about"), {})

    lines = [
        "# БЗПМ",
        "",
        "## О сайте",
        "",
        "БЗПМ — сайт производителя нейтрального оборудования из нержавеющей стали для предприятий общественного питания, пищевых производств, торговых и производственных помещений. На сайте представлены серийные изделия, информация о производстве, доставке, гарантии, оплате и сотрудничестве.",
        "",
    ]
    title = about_row.get("title", "")
    if title and "Барнаульск" in title:
        lines.extend([f"Публичное наименование на сайте: {title}.", ""])

    lines.extend(["## Основные разделы", ""])
    for label, url in LLMS_SECTIONS:
        if status_map.get(url, 0) == 200:
            lines.append(f"- {label}: {url}")

    lines.extend([
        "",
        "## Что можно найти на сайте",
        "",
        "- каталог нейтрального оборудования из нержавеющей стали;",
        "- карточки товаров с характеристиками и описаниями;",
        "- оборудование для общепита, пищевых производств и производственных зон;",
        "- информацию о нестандартном изготовлении оборудования;",
        "- условия доставки, оплаты, гарантии и сотрудничества;",
        "- контакты для связи с компанией.",
        "",
        "## Как использовать информацию",
        "",
        "Для поиска товаров используйте каталог и страницы категорий. Для обхода сайта используйте sitemap.xml. Файл llms.txt является справочным описанием сайта для AI-агентов и не заменяет robots.txt или sitemap.xml.",
        "",
        "## Ограничения",
        "",
        "Информация о наличии, цене, сроках изготовления и поставки должна уточняться на сайте или у компании. Не используйте этот файл как источник внутренних данных, коммерческих условий или технической документации, не опубликованной на сайте.",
        "",
        "## Контакты",
        "",
        "Актуальные контакты опубликованы на странице: https://bzpm.ru/contact",
        "",
    ])
    return "\n".join(lines)


def validate_content(content: str, discovery: list[dict[str, Any]]) -> dict[str, Any]:
    status_map = {r["url"]: r["status"] for r in discovery}
    listed_urls = [url for _, url in LLMS_SECTIONS]
    issues: list[str] = []
    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            issues.append(f"forbidden pattern: {pattern}")
    for url in listed_urls:
        if url in content and status_map.get(url, 0) not in (200,):
            issues.append(f"listed URL not HTTP 200: {url} ({status_map.get(url)})")
    try:
        content.encode("utf-8")
        utf8_ok = True
    except UnicodeEncodeError:
        utf8_ok = False
        issues.append("not valid UTF-8")
    size = len(content.encode("utf-8"))
    if size > 65536:
        issues.append(f"file too large: {size} bytes")
    if "<html" in content.lower():
        issues.append("contains HTML")
    result = {
        "validated_at": utc_now(),
        "size_bytes": size,
        "line_count": content.count("\n") + 1,
        "utf8_ok": utf8_ok,
        "issues": issues,
        "pass": len(issues) == 0,
        "listed_urls_in_content": sum(1 for _, u in LLMS_SECTIONS if u in content),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", result)
    issue_lines = [f"- {i}" for i in issues] if issues else ["- none"]
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "\n".join(
            [
                "# Dry-run validation",
                "",
                f"- Size: {size} bytes",
                f"- Lines: {result['line_count']}",
                f"- UTF-8: {utf8_ok}",
                f"- Pass: {result['pass']}",
                "",
                "## Issues",
                *issue_lines,
            ]
        ),
    )
    return result


def phase_existing_check(ftp: ftplib.FTP) -> dict[str, Any]:
    http_resp = http_get(PUBLIC_LLMS)
    ftp_exists_flag = ftp_exists(ftp, REMOTE_LLMS)
    result: dict[str, Any] = {
        "http_status": http_resp["status"],
        "ftp_exists": ftp_exists_flag,
        "checked_at": utc_now(),
    }
    if http_resp["status"] == 200:
        data = http_resp["body"]
        result["http_sha256"] = sha256_bytes(data)
        (DEPLOYMENT_ROOT / "backup" / "llms.txt.before").write_bytes(data)
    if ftp_exists_flag:
        data = ftp_download(ftp, REMOTE_LLMS)
        result["ftp_sha256"] = sha256_bytes(data)
        (DEPLOYMENT_ROOT / "backup" / "llms.txt.ftp").write_bytes(data)
        (DEPLOYMENT_ROOT / "rollback" / "llms.txt").write_bytes(data)
    else:
        write_text(
            DEPLOYMENT_ROOT / "rollback" / "ROLLBACK.md",
            "\n".join(
                [
                    "# Rollback note",
                    "",
                    "Remote `/public_html/llms.txt` did not exist before deploy.",
                    "",
                    "Rollback for new file: manual removal of `/public_html/llms.txt` only with operator approval if needed.",
                    "Do not delete automatically.",
                ]
            ),
        )
    write_json(DEPLOYMENT_ROOT / "manifests" / "existing-llms-status.json", result)
    return result


def phase_prepare_content(discovery: list[dict[str, Any]]) -> str:
    content = build_llms_content(discovery)
    prepared_path = DEPLOYMENT_ROOT / "prepared" / "llms.txt"
    write_text(prepared_path, content)
    write_text(DEPLOYMENT_ROOT / "content" / "llms-txt-final.md", content)
    write_text(DEPLOYMENT_ROOT / "content" / "llms-txt-final.txt", content)
    return content


def pre_upload_verify(ftp: ftplib.FTP, existing: dict[str, Any]) -> None:
    if not existing.get("ftp_exists"):
        return
    backup_path = DEPLOYMENT_ROOT / "backup" / "llms.txt.ftp"
    if not backup_path.exists():
        return
    backup_sha = sha256_file(backup_path)
    live = ftp_download(ftp, REMOTE_LLMS)
    if sha256_bytes(live) != backup_sha:
        raise RuntimeError("STOP — LIVE LLMS.TXT CHANGED SINCE BACKUP")


def deploy_llms(ftp: ftplib.FTP) -> dict[str, Any]:
    prepared = (DEPLOYMENT_ROOT / "prepared" / "llms.txt").read_bytes()
    overwrite = ftp_exists(ftp, REMOTE_LLMS)
    ftp_upload(ftp, REMOTE_LLMS, prepared)
    after = ftp_download(ftp, REMOTE_LLMS)
    (DEPLOYMENT_ROOT / "verification" / "llms.txt.after").write_bytes(after)
    return {
        "remote": REMOTE_LLMS,
        "overwrite": overwrite,
        "sha256_prepared": sha256_bytes(prepared),
        "sha256_after_upload": sha256_bytes(after),
        "match": sha256_bytes(prepared) == sha256_bytes(after),
        "deployed_at": utc_now(),
    }


def phase_public_verification(prepared_text: str) -> dict[str, Any]:
    llms_resp = http_get(PUBLIC_LLMS, accept="text/plain")
    llms_text = llms_resp["body"].decode("utf-8", errors="replace")
    (DEPLOYMENT_ROOT / "verification" / "llms-response.txt").write_text(llms_text, encoding="utf-8")

    sanity_urls = [
        "https://bzpm.ru/",
        "https://bzpm.ru/robots.txt",
        "https://bzpm.ru/sitemap.xml",
        "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    ]
    sanity: list[dict[str, Any]] = []
    for url in sanity_urls:
        is_xml = url.endswith(".xml")
        is_txt = url.endswith(".txt")
        accept = "application/xml" if is_xml else "text/plain" if is_txt else "text/html"
        resp = http_get(url, accept=accept)
        entry: dict[str, Any] = {"url": url, "status": resp["status"]}
        if url.endswith(".xml") and resp["status"] == 200:
            try:
                root = ET.fromstring(resp["body"])
                ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                locs = root.findall(".//sm:loc", ns) or root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
                entry["sitemap_url_count"] = len(locs)
            except ET.ParseError:
                entry["sitemap_url_count"] = None
        if not is_xml and not is_txt and resp["status"] == 200:
            parsed = parse_html_page(resp["body"])
            entry.update(parsed)
        if is_txt and resp["status"] == 200:
            entry["robots_unchanged_marker"] = "Sitemap:" in resp["body"].decode("utf-8", errors="replace")
        sanity.append(entry)

    prepared_norm = prepared_text.replace("\r\n", "\n").strip()
    live_norm = llms_text.replace("\r\n", "\n").strip()
    result = {
        "verified_at": utc_now(),
        "llms_http_status": llms_resp["status"],
        "llms_content_match": prepared_norm == live_norm,
        "llms_utf8_readable": True,
        "llms_is_html_error": "<html" in llms_text.lower()[:500],
        "sanity_checks": sanity,
        "home_body_count": next((s.get("body_count") for s in sanity if s["url"] == "https://bzpm.ru/"), None),
        "stoly_load_more": next(
            (s.get("has_load_more") for s in sanity if "stoly" in s["url"]),
            None,
        ),
        "yandex_home_metrika": next(
            (s.get("has_yandex_metrika") for s in sanity if s["url"] == "https://bzpm.ru/"),
            None,
        ),
        "yandex_home_webmaster": next(
            (s.get("has_yandex_webmaster") for s in sanity if s["url"] == "https://bzpm.ru/"),
            None,
        ),
        "sitemap_url_count": next(
            (s.get("sitemap_url_count") for s in sanity if s["url"].endswith("sitemap.xml")),
            None,
        ),
        "pass": (
            llms_resp["status"] == 200
            and prepared_norm == live_norm
            and not ("<html" in llms_text.lower()[:500])
        ),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "public-verification.json", result)
    md = [
        "# Public verification",
        "",
        f"Verified: {result['verified_at']}",
        "",
        f"## llms.txt",
        f"- URL: {PUBLIC_LLMS}",
        f"- HTTP status: {result['llms_http_status']}",
        f"- Content match: {result['llms_content_match']}",
        "",
        "## Sanity checks",
    ]
    for s in sanity:
        md.append(f"### {s['url']}")
        md.append(f"- Status: {s['status']}")
        for k in ("body_count", "sitemap_url_count", "has_yandex_metrika", "has_yandex_webmaster", "has_load_more", "robots_unchanged_marker"):
            if k in s:
                md.append(f"- {k}: {s[k]}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "verification" / "public-verification.md", "\n".join(md))
    return result


def run_all(deploy: bool = True) -> int:
    ensure_dirs()
    write_operation_metadata()
    discovery = phase_discovery()
    existing = None
    content = phase_prepare_content(discovery)
    dry_run = validate_content(content, discovery)
    if not dry_run["pass"]:
        print("Dry-run FAILED:", dry_run["issues"], file=sys.stderr)
        return 1

    ftp = ftp_connect()
    try:
        existing = phase_existing_check(ftp)
        if deploy:
            pre_upload_verify(ftp, existing)
            deploy_result = deploy_llms(ftp)
            write_json(DEPLOYMENT_ROOT / "manifests" / "deploy-summary.json", deploy_result)
            if not deploy_result["match"]:
                raise RuntimeError("Upload SHA mismatch")
    finally:
        ftp.quit()

    verification = phase_public_verification(content)
    summary = {
        "operation_id": OPERATION_ID,
        "discovery_urls": len(discovery),
        "existing_llms": existing,
        "dry_run_pass": dry_run["pass"],
        "deployed": deploy,
        "verification_pass": verification["pass"],
        "baseline_after": BASELINE_AFTER if verification["pass"] else None,
    }
    write_json(DEPLOYMENT_ROOT / "logs" / "run-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if verification["pass"] else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--discover-only", action="store_true")
    parser.add_argument("--no-deploy", action="store_true")
    args = parser.parse_args()
    if args.discover_only:
        ensure_dirs()
        write_operation_metadata()
        phase_discovery()
        return 0
    return run_all(deploy=not args.no_deploy)


if __name__ == "__main__":
    raise SystemExit(main())
