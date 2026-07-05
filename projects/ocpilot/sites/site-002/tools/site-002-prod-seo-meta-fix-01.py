#!/usr/bin/env python3
"""SITE-002 Production non-product SEO meta fix — Run 4.192."""
from __future__ import annotations

import argparse
import csv
import difflib
import ftplib
import hashlib
import html
import json
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from io import BytesIO
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-SEO-META-FIX-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SITEMAP-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-SEO-META-01"
META_FIX_PLAN = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-READINESS-ROBOTS-01\meta-audit\meta-fix-plan.md"
)
META_AUDIT_CSV = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-READINESS-ROBOTS-01\meta-audit\non-product-meta-audit.csv"
)
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-SEO-META-FIX-01"
)
USER_AGENT = "MARS-OCPilot/SITE-002-PROD-SEO-META-FIX-01"

REMOTE_CATEGORY = "/public_html/catalog/controller/product/category.php"
REMOTE_HEADER_CTRL = "/public_html/catalog/controller/common/header.php"
REMOTE_CONTACT = "/public_html/catalog/controller/information/contact.php"

BEFORE_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly?page=2",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly?limit=30",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly?sort=p.price&order=ASC",
    "https://bzpm.ru/guarantee",
    "https://bzpm.ru/contact",
    "https://bzpm.ru/index.php?route=information/contact",
    "https://bzpm.ru/cart",
    "https://bzpm.ru/checkout",
    "https://bzpm.ru/search",
    "https://bzpm.ru/compare-products",
    "https://bzpm.ru/wishlist",
]

SOURCE_PATHS = [
    REMOTE_CATEGORY,
    REMOTE_CONTACT,
    REMOTE_HEADER_CTRL,
    "/public_html/catalog/controller/information/information.php",
    "/public_html/catalog/controller/common/home.php",
    "/public_html/catalog/view/theme/default/template/product/category.twig",
]

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "verification",
    "verification/pre-upload",
    "meta-before",
    "meta-after",
    "admin-evidence",
    "crawl",
    "manifests",
    "logs",
)

# category keyword slug -> meta description proposal (admin)
CATEGORY_META: dict[str, dict[str, str]] = {
    "stoly": {
        "meta_title": "Столы для общепита и производств | ООО «ЗПМ»",
        "meta_description": "Производственные столы из нержавеющей стали для ресторанов, кафе и пищевых производств. Каталог моделей завода ЗПМ с поставкой по России.",
    },
    "podtovarniki-i-podstavki": {
        "meta_title": "Подтоварники и подставки | ООО «ЗПМ»",
        "meta_description": "Подтоварники и подставки из нержавеющей стали для профессиональной кухни и производств. Надёжные решения от завода ЗПМ.",
    },
    "polki-nastennye-i-nastolnye": {
        "meta_title": "Полки настенные и настольные | ООО «ЗПМ»",
        "meta_description": "Настенные и настольные полки из нержавеющей стали для общепита и пищевых производств. Производство и поставки завода ЗПМ.",
    },
    "shkafy-i-lari": {
        "meta_title": "Шкафы и лари для общепита | ООО «ЗПМ»",
        "meta_description": "Шкафы и лари из нержавеющей стали для кухни и складских зон общепита. Каталог моделей завода ЗПМ.",
    },
    "telezhki-servirovochnye": {
        "meta_title": "Тележки сервировочные | ООО «ЗПМ»",
        "meta_description": "Сервировочные тележки из нержавеющей стали для ресторанов, столовых и производств. Производство завода ЗПМ.",
    },
    "telezhki-shpilki-i-protivni": {
        "meta_title": "Тележки-шпильки и противни | ООО «ЗПМ»",
        "meta_description": "Тележки-шпильки и противни для пекарни и производства. Оборудование из нержавеющей стали от завода ЗПМ.",
    },
}

INFO_META: dict[str, dict[str, str]] = {
    "contact": {
        "meta_description": "Контакты завода пищевого машиностроения ЗПМ: адрес в Барнауле, телефон, e-mail и форма обратной связи для заказчиков и партнёров.",
    },
}

STORE_META_TRIM = {
    "meta_description": (
        "Завод пищевого машиностроения ЗПМ производит оборудование для ресторанов, кафе и пищевых производств. "
        "Каталог нейтрального оборудования из нержавеющей стали."
    ),
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
            "change_type": "seo-meta-fix",
            "product_pages_excluded": True,
            "robots_change_allowed": False,
            "sitemap_change_allowed": False,
            "header_footer_change_allowed": False,
            "yandex_blocks_protected": True,
            "db_direct_write_allowed": False,
            "admin_save_allowed": "conditional_only",
            "cron_change_allowed": False,
            "import_execution_allowed": False,
            "mail_change_allowed": False,
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
        headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache", "Accept": "text/html,application/xml,*/*"},
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
                "body": text,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read()
        charset = exc.headers.get_content_charset() or "utf-8"
        text = body.decode(charset, errors="replace")
        return {
            "url": url,
            "final_url": exc.geturl() if hasattr(exc, "geturl") else url,
            "status_code": exc.code,
            "body": text,
            "error": str(exc),
        }
    except Exception as exc:
        return {"url": url, "final_url": url, "status_code": None, "body": "", "error": str(exc)}


def is_product_url(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    if "product_id=" in parsed.query.lower():
        return True
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) >= 4 and parts[0] == "katalog":
        return True
    return False


def extract_meta(html_text: str) -> dict[str, Any]:
    parser = MetaParser()
    try:
        parser.feed(html_text)
    except Exception:
        pass
    canonical = next((l["href"] for l in parser.links if l["rel"] == "canonical"), "")
    title = html.unescape(parser.title.strip())
    description = parser.meta.get("description", "")
    return {
        "title": title,
        "title_length": len(title),
        "meta_description": description,
        "description_length": len(description),
        "h1_list": [h for h in parser.h1_list if h],
        "h1_count": len([h for h in parser.h1_list if h]),
        "h1_text": " | ".join(h for h in parser.h1_list if h),
        "canonical": canonical,
        "meta_robots": parser.meta.get("robots", ""),
        "og_title": parser.meta.get("og:title", ""),
        "og_description": parser.meta.get("og:description", ""),
        "body_count": parser.body_open,
        "has_metrika": any(t in html_text.lower() for t in ("mc.yandex.ru/metrika", "ym(", "yandex.metrika")),
        "has_webmaster_verification": "yandex-verification" in html_text.lower(),
    }


def crawl_urls(urls: list[str], label: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for url in urls:
        resp = http_get(url)
        meta = extract_meta(resp["body"]) if resp["body"] else {}
        robots_effective = meta.get("meta_robots", "")
        x_robots = resp.get("x_robots_tag") or ""
        if x_robots and "noindex" in x_robots.lower():
            robots_effective = x_robots
        row = {
            "url": url,
            "final_url": resp["final_url"],
            "status_code": resp["status_code"],
            "error": resp["error"],
            "accidental_product": is_product_url(resp["final_url"] or url),
            "x_robots_tag": x_robots,
            **meta,
            "meta_robots_effective": robots_effective,
        }
        rows.append(row)
    out_dir = DEPLOYMENT_ROOT / label
    write_json(out_dir / f"{label}.json", rows)
    fieldnames = list(rows[0].keys()) if rows else []
    with (out_dir / f"{label}.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    passes = sum(1 for r in rows if r.get("status_code") == 200 and not r.get("accidental_product"))
    write_text(
        out_dir / f"{label}-summary.md",
        "\n".join(
            [
                f"# Meta {label.replace('meta-', '')}",
                "",
                f"Captured: {utc_now()}",
                f"URLs: {len(urls)}",
                f"HTTP 200 non-product: {passes}",
                "",
                "| URL | Status | Title len | Desc len | Robots | Canonical |",
                "|-----|--------|-----------|----------|--------|-----------|",
            ]
            + [
                f"| {r['url'][:60]} | {r.get('status_code')} | {r.get('title_length', 0)} | "
                f"{r.get('description_length', 0)} | {r.get('meta_robots', '')} | {(r.get('canonical') or '')[:40]} |"
                for r in rows
            ]
        ),
    )
    return rows


def parse_meta_fix_plan() -> list[dict[str, Any]]:
    text = META_FIX_PLAN.read_text(encoding="utf-8")
    entries: list[dict[str, Any]] = []
    blocks = re.split(r"\n## ", text)
    for block in blocks[1:]:
        lines = block.splitlines()
        url = lines[0].strip()
        entry: dict[str, Any] = {"url": url, "issues": [], "include": True}
        for line in lines[1:]:
            if line.startswith("- Classification:"):
                entry["classification"] = line.split(":", 1)[1].strip()
            elif line.startswith("- Issues:"):
                entry["issues"] = [i.strip() for i in line.split(":", 1)[1].split(",")]
            elif line.startswith("- Current title:"):
                entry["current_title"] = line.split(":", 1)[1].strip()
            elif line.startswith("- Current description:"):
                entry["current_description"] = line.split(":", 1)[1].strip()
        entries.append(entry)
    return entries


def authority_for(entry: dict[str, Any]) -> str:
    url = entry["url"]
    issues = entry.get("issues", [])
    if any(x in url for x in ("/cart", "/checkout", "/search", "/wishlist", "/compare", "/account/")):
        return "CONTROLLER"
    if "route=information/contact" in url:
        return "CONTROLLER"
    if any(v in issues for v in ("duplicate_title", "missing_description")) and "stoly?" in url:
        return "CONTROLLER"
    if "missing_description" in issues and "/katalog/" in url and "?" not in url:
        return "ADMIN"
    if "description_length" in issues and url.rstrip("/") in ("https://bzpm.ru", "https://bzpm.ru/"):
        return "ADMIN"
    if "missing_description" in issues and "/contact" in url:
        return "ADMIN"
    if "duplicate_title" in issues and "/katalog" in url:
        return "ROUTE_RULE"
    return "SAFE UNKNOWN"


def priority_for(entry: dict[str, Any]) -> str:
    url = entry["url"]
    issues = entry.get("issues", [])
    if any(x in url for x in ("/cart", "/checkout", "/search", "/wishlist", "/compare", "/account/")):
        return "P1"
    if "missing_description" in issues and "/katalog/" in url and "?" not in url:
        return "P1"
    if "route=information/contact" in url or (url.endswith("/contact") and "missing_description" in issues):
        return "P1"
    if "?" in url and "duplicate_title" in issues:
        return "P2"
    if "description_length" in issues:
        return "P2"
    if "title_length" in issues and "/blog" in url:
        return "P3"
    return "P3"


def build_working_plan() -> list[dict[str, Any]]:
    entries = parse_meta_fix_plan()
    plan: list[dict[str, Any]] = []
    for e in entries:
        if is_product_url(e["url"]):
            e["include"] = False
        e["priority"] = priority_for(e)
        e["authority"] = authority_for(e)
        e["risk"] = "low" if e["authority"] == "CONTROLLER" else "medium"
        plan.append(e)
    write_json(DEPLOYMENT_ROOT / "manifests" / "meta-fix-working-plan.json", plan)
    md = ["# Meta fix working plan", "", f"Generated: {utc_now()}", ""]
    for item in plan:
        md.append(f"## {item['url']}")
        md.append(f"- Priority: {item['priority']}")
        md.append(f"- Issues: {', '.join(item.get('issues', []))}")
        md.append(f"- Authority: {item['authority']}")
        md.append(f"- Include: {item['include']}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "manifests" / "meta-fix-working-plan.md", "\n".join(md))
    return plan


def patch_category_php(content: str) -> str:
    marker = "$this->document->setKeywords($category_info['meta_keyword']);"
    insert = """
\t\t\t$this->document->setKeywords($category_info['meta_keyword']);

\t\t\t$is_default_sort = ($sort === 'pd.name' && $order === 'ASC');
\t\t\t$seo_variant = (isset($this->request->get['limit']))
\t\t\t\t|| (isset($this->request->get['sort']) && !$is_default_sort)
\t\t\t\t|| (isset($this->request->get['order']) && !$is_default_sort)
\t\t\t\t|| ($page > 1)
\t\t\t\t|| !empty($filter)
\t\t\t\t|| isset($this->request->get['filters']);

\t\t\tif ($seo_variant) {
\t\t\t\t$this->response->addHeader('X-Robots-Tag: noindex, follow');
\t\t\t}

\t\t\t$clean_category_canonical = $this->url->link('product/category', 'path=' . $category_info['category_id']);

\t\t\t$zpm_category_meta_defaults = array(
\t\t\t\t'Столы' => array(
\t\t\t\t\t'title' => 'Столы для общепита и производств | ООО «ЗПМ»',
\t\t\t\t\t'description' => 'Производственные столы из нержавеющей стали для ресторанов, кафе и пищевых производств. Каталог моделей завода ЗПМ с поставкой по России.'
\t\t\t\t),
\t\t\t\t'Подтоварники и подставки' => array(
\t\t\t\t\t'title' => 'Подтоварники и подставки | ООО «ЗПМ»',
\t\t\t\t\t'description' => 'Подтоварники и подставки из нержавеющей стали для профессиональной кухни и производств. Надёжные решения от завода ЗПМ.'
\t\t\t\t),
\t\t\t\t'Полки настенные и настольные' => array(
\t\t\t\t\t'title' => 'Полки настенные и настольные | ООО «ЗПМ»',
\t\t\t\t\t'description' => 'Настенные и настольные полки из нержавеющей стали для общепита и пищевых производств. Производство и поставки завода ЗПМ.'
\t\t\t\t),
\t\t\t\t'Шкафы и лари' => array(
\t\t\t\t\t'title' => 'Шкафы и лари для общепита | ООО «ЗПМ»',
\t\t\t\t\t'description' => 'Шкафы и лари из нержавеющей стали для кухни и складских зон общепита. Каталог моделей завода ЗПМ.'
\t\t\t\t),
\t\t\t\t'Тележки сервировочные' => array(
\t\t\t\t\t'title' => 'Тележки сервировочные | ООО «ЗПМ»',
\t\t\t\t\t'description' => 'Сервировочные тележки из нержавеющей стали для ресторанов, столовых и производств. Производство завода ЗПМ.'
\t\t\t\t),
\t\t\t\t'Тележки-шпильки и противни' => array(
\t\t\t\t\t'title' => 'Тележки-шпильки и противни | ООО «ЗПМ»',
\t\t\t\t\t'description' => 'Тележки-шпильки и противни для пекарни и производства. Оборудование из нержавеющей стали от завода ЗПМ.'
\t\t\t\t),
\t\t\t);
\t\t\tif (isset($zpm_category_meta_defaults[$category_info['name']])) {
\t\t\t\t$zpm_defaults = $zpm_category_meta_defaults[$category_info['name']];
\t\t\t\tif (!trim(strip_tags((string)$category_info['meta_description']))) {
\t\t\t\t\t$this->document->setDescription($zpm_defaults['description']);
\t\t\t\t}
\t\t\t\tif (utf8_strlen((string)$category_info['meta_title']) < 20) {
\t\t\t\t\t$this->document->setTitle($zpm_defaults['title']);
\t\t\t\t}
\t\t\t}"""
    if marker not in content:
        raise RuntimeError("category.php marker not found for SEO patch")
    if "seo_variant" in content:
        return content
    content = content.replace(marker, insert, 1)

    old_canon = """\t\t\tif ($page == 1) {
\t\t\t    $this->document->addLink($this->url->link('product/category', 'path=' . $category_info['category_id']), 'canonical');
\t\t\t} else {
\t\t\t\t$this->document->addLink($this->url->link('product/category', 'path=' . $category_info['category_id'] . '&page='. $page), 'canonical');
\t\t\t}"""
    new_canon = """\t\t\t$this->document->addLink($clean_category_canonical, 'canonical');"""
    if old_canon in content:
        content = content.replace(old_canon, new_canon, 1)
    return content


def patch_header_controller(content: str) -> str:
    if "zpm_seo_noindex_guard" in content:
        return content
    needle = "public function index() {"
    if needle not in content:
        raise RuntimeError("header.php controller index() not found")
    guard = """
\t\t// ZPM SEO: technical/account routes should not be indexed
\t\t$route = isset($this->request->get['route']) ? (string)$this->request->get['route'] : '';
\t\t$request_uri = isset($this->request->server['REQUEST_URI']) ? strtolower((string)$this->request->server['REQUEST_URI']) : '';
\t\t$noindex_routes = array(
\t\t\t'checkout/cart', 'checkout/checkout', 'product/search', 'product/compare',
\t\t\t'account/wishlist', 'account/login', 'account/register', 'account/forgotten', 'account/account'
\t\t);
\t\t$noindex_paths = array('/cart', '/checkout', '/search', '/compare-products', '/wishlist', '/my-account', '/account/');
\t\t$zpm_seo_noindex_guard = in_array($route, $noindex_routes, true);
\t\tif (!$zpm_seo_noindex_guard && strpos($route, 'account/') === 0) {
\t\t\t$zpm_seo_noindex_guard = true;
\t\t}
\t\tif (!$zpm_seo_noindex_guard) {
\t\t\tforeach ($noindex_paths as $noindex_path) {
\t\t\t\tif ($request_uri === $noindex_path
\t\t\t\t\t|| strpos($request_uri, $noindex_path . '?') === 0
\t\t\t\t\t|| strpos($request_uri, $noindex_path . '/') === 0
\t\t\t\t\t|| strpos($request_uri, rtrim($noindex_path, '/') . '/') === 0) {
\t\t\t\t\t$zpm_seo_noindex_guard = true;
\t\t\t\t\tbreak;
\t\t\t\t}
\t\t\t}
\t\t}
\t\tif (!$zpm_seo_noindex_guard && strpos($request_uri, 'wishlist') !== false) {
\t\t\t$zpm_seo_noindex_guard = true;
\t\t}
\t\tif ($zpm_seo_noindex_guard) {
\t\t\t$this->response->addHeader('X-Robots-Tag: noindex, follow');
\t\t}

"""
    return content.replace(needle, needle + guard, 1)


def patch_contact_controller(content: str) -> str:
    if "zpm_contact_seo_canonical" in content:
        return content
    needle = "public function index() {"
    if needle not in content:
        raise RuntimeError("contact.php index() not found")
    guard = """
\t\t// ZPM SEO: canonical friendly contact URL; noindex legacy query route duplicate
\t\t$this->document->setDescription('Контакты завода пищевого машиностроения ЗПМ: адрес в Барнауле, телефон, e-mail и форма обратной связи для заказчиков и партнёров.');
\t\t$this->document->addLink($this->url->link('information/contact'), 'canonical');
\t\tif (!empty($this->request->server['REQUEST_URI']) && strpos($this->request->server['REQUEST_URI'], 'index.php') !== false) {
\t\t\t$this->response->addHeader('X-Robots-Tag: noindex, follow');
\t\t}
\t\t$zpm_contact_seo_canonical = true;

"""
    return content.replace(needle, needle + guard, 1)


def php_lint(path: Path) -> tuple[bool, str]:
    try:
        proc = subprocess.run(
            ["php", "-l", str(path)],
            capture_output=True,
            text=True,
            timeout=30,
        )
        return proc.returncode == 0, (proc.stdout + proc.stderr).strip()
    except FileNotFoundError:
        return True, "php not available — skipped"
    except Exception as exc:
        return False, str(exc)


def prepare_patches() -> dict[str, Any]:
    files: dict[str, Path] = {}
    for remote in (REMOTE_CATEGORY, REMOTE_HEADER_CTRL, REMOTE_CONTACT):
        local_name = remote.split("/")[-1]
        src = DEPLOYMENT_ROOT / "source" / local_name
        if not src.exists():
            raise RuntimeError(f"Missing source file {src}")
        content = src.read_text(encoding="utf-8")
        if local_name == "category.php":
            content = patch_category_php(content)
        elif local_name == "header.php":
            content = patch_header_controller(content)
        elif local_name == "contact.php":
            content = patch_contact_controller(content)
        out = DEPLOYMENT_ROOT / "prepared" / local_name
        out.write_text(content, encoding="utf-8")
        files[remote] = out
    lint_results = {str(p): php_lint(p) for p in files.values()}
    write_json(DEPLOYMENT_ROOT / "manifests" / "files-to-change.json", {"files": list(files.keys()), "lint": lint_results})
    return {"files": files, "lint": lint_results}


def backup_remote_files(ftp: ftplib.FTP, remotes: list[str]) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for remote in remotes:
        data = ftp_download(ftp, remote)
        name = remote.split("/")[-1]
        for folder in ("backup", "rollback", "source"):
            (DEPLOYMENT_ROOT / folder / name).write_bytes(data)
        hashes[remote] = sha256_bytes(data)
    write_json(DEPLOYMENT_ROOT / "manifests" / "backup-hashes.json", hashes)
    return hashes


def dry_run_diff() -> None:
    diffs: list[dict[str, Any]] = []
    for remote in (REMOTE_CATEGORY, REMOTE_HEADER_CTRL, REMOTE_CONTACT):
        name = remote.split("/")[-1]
        before = (DEPLOYMENT_ROOT / "source" / name).read_text(encoding="utf-8").splitlines()
        after = (DEPLOYMENT_ROOT / "prepared" / name).read_text(encoding="utf-8").splitlines()
        diff = list(difflib.unified_diff(before, after, fromfile=f"backup/{name}", tofile=f"prepared/{name}", lineterm=""))
        diffs.append({"remote": remote, "diff": diff})
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", diffs)
    md = ["# Dry run", "", f"Generated: {utc_now()}", ""]
    for item in diffs:
        md.append(f"## {item['remote']}")
        md.extend(["```diff"] + item["diff"][:80] + ["```", ""])
    write_text(DEPLOYMENT_ROOT / "manifests" / "dry-run.md", "\n".join(md))


def verify_pre_upload(ftp: ftplib.FTP, backup_hashes: dict[str, str]) -> bool:
    ok = True
    for remote, expected in backup_hashes.items():
        data = ftp_download(ftp, remote)
        current = sha256_bytes(data)
        name = remote.split("/")[-1]
        (DEPLOYMENT_ROOT / "verification" / "pre-upload" / name).write_bytes(data)
        if current != expected:
            ok = False
    return ok


def deploy_files(ftp: ftplib.FTP, files: dict[str, Path]) -> None:
    for remote, local in files.items():
        ftp_upload(ftp, remote, local.read_bytes())


def _admin_login(page: Any, admin: dict[str, str]) -> str | None:
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


def discover_category_ids(page: Any, admin_url: str, token: str) -> dict[str, int]:
    """Map SEO keyword slug to category_id from admin category list."""
    mapping: dict[str, int] = {}
    list_url = _admin_url(admin_url, "catalog/category", token)
    page.goto(list_url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_load_state("domcontentloaded", timeout=90000)
    html_body = page.content()
    for slug in CATEGORY_META:
        pattern = rf"category_id=(\d+)[^\"'>]*keyword={re.escape(slug)}|keyword={re.escape(slug)}[^\"'>]*category_id=(\d+)"
        m = re.search(pattern, html_body)
        if m:
            mapping[slug] = int(m.group(1) or m.group(2))
            continue
        edit_links = page.locator(f'a[href*="category_id="][href*="{slug}"]')
        if edit_links.count() > 0:
            href = edit_links.first.get_attribute("href") or ""
            mid = re.search(r"category_id=(\d+)", href)
            if mid:
                mapping[slug] = int(mid.group(1))
    # fallback: search by name in table rows
    if len(mapping) < len(CATEGORY_META):
        rows = page.locator("table tbody tr")
        for i in range(rows.count()):
            row = rows.nth(i)
            text = row.inner_text()
            for slug, meta in CATEGORY_META.items():
                if slug in mapping:
                    continue
                name_part = meta["meta_title"].split("|")[0].strip()
                if name_part.split()[0] in text:
                    href = row.locator('a[href*="category_id="]').first.get_attribute("href") or ""
                    mid = re.search(r"category_id=(\d+)", href)
                    if mid:
                        mapping[slug] = int(mid.group(1))
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-id-map.json", mapping)
    return mapping


def admin_save_categories(page: Any, admin_url: str, token: str, id_map: dict[str, int]) -> list[dict[str, Any]]:
    saves: list[dict[str, Any]] = []
    for slug, fields in CATEGORY_META.items():
        cid = id_map.get(slug)
        if not cid:
            saves.append({"slug": slug, "status": "SKIPPED", "reason": "category_id not found"})
            continue
        edit_url = _admin_url(admin_url, "catalog/category/edit", token, category_id=str(cid))
        page.goto(edit_url, wait_until="domcontentloaded", timeout=90000)
        page.wait_for_load_state("domcontentloaded", timeout=90000)
        before = {
            "meta_title": page.locator('input[name="category_description[1][meta_title]"]').input_value(),
            "meta_description": page.locator('textarea[name="category_description[1][meta_description]"]').input_value(),
        }
        page.fill('input[name="category_description[1][meta_title]"]', fields["meta_title"])
        page.fill('textarea[name="category_description[1][meta_description]"]', fields["meta_description"])
        page.click('#form-category button[type="submit"], #form-category .btn-primary')
        page.wait_for_load_state("networkidle", timeout=30000)
        saves.append(
            {
                "entity": f"category/{slug}",
                "category_id": cid,
                "fields_changed": ["meta_title", "meta_description"],
                "before": before,
                "after": fields,
                "status": "SAVED",
            }
        )
    return saves


def admin_save_store_and_contact(page: Any, admin_url: str, token: str) -> list[dict[str, Any]]:
    saves: list[dict[str, Any]] = []
    settings_url = _admin_url(admin_url, "setting/setting", token)
    page.goto(settings_url, wait_until="domcontentloaded", timeout=60000)
    page.wait_for_load_state("networkidle", timeout=30000)
    if page.locator('textarea[name="config_meta_description"]').count():
        before_desc = page.locator('textarea[name="config_meta_description"]').input_value()
        page.fill('textarea[name="config_meta_description"]', STORE_META_TRIM["meta_description"])
        page.click('#form-setting button[type="submit"], #form-setting .btn-primary')
        page.wait_for_load_state("networkidle", timeout=30000)
        saves.append(
            {
                "entity": "setting/store",
                "fields_changed": ["config_meta_description"],
                "before": {"config_meta_description": before_desc[:120] + "..."},
                "after": STORE_META_TRIM,
                "status": "SAVED",
            }
        )
    # information/contact is layout — try information pages list for contact
    info_url = _admin_url(admin_url, "catalog/information", token)
    page.goto(info_url, wait_until="domcontentloaded", timeout=60000)
    contact_link = page.locator('a:has-text("Контакты"), a[href*="information_id="]:has-text("Contact")')
    if contact_link.count() == 0:
        contact_link = page.locator('table tbody tr:has-text("Контакт") a[href*="information_id="]')
    if contact_link.count() > 0:
        contact_link.first.click()
        page.wait_for_load_state("networkidle", timeout=30000)
        if page.locator('textarea[name="information_description[1][meta_description]"]').count():
            before = page.locator('textarea[name="information_description[1][meta_description]"]').input_value()
            page.fill(
                'textarea[name="information_description[1][meta_description]"]',
                INFO_META["contact"]["meta_description"],
            )
            page.click('#form-information button[type="submit"], #form-information .btn-primary')
            page.wait_for_load_state("networkidle", timeout=30000)
            saves.append(
                {
                    "entity": "information/contact",
                    "fields_changed": ["meta_description"],
                    "before": {"meta_description": before},
                    "after": INFO_META["contact"],
                    "status": "SAVED",
                }
            )
    return saves


def phase_admin_saves() -> dict[str, Any]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"status": "SKIPPED", "reason": "playwright unavailable"}
    admin = parse_production_section(SECRETS_PATH, "OpenCart Admin")
    url = admin.get("url", "https://bzpm.ru/admin/")
    result: dict[str, Any] = {"checked_at": utc_now(), "saves": [], "status": "FAILED"}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            token = _admin_login(page, admin)
            if not token:
                result["status"] = "LOGIN_FAILED"
                browser.close()
                return result
            id_map = discover_category_ids(page, url, token)
            saves = admin_save_categories(page, url, token, id_map)
            saves.extend(admin_save_store_and_contact(page, url, token))
            result["saves"] = saves
            result["status"] = "COMPLETE"
            page.goto(_admin_url(url, "common/logout", token), timeout=15000)
        except Exception as exc:
            result["status"] = "ERROR"
            result["error_type"] = type(exc).__name__
        browser.close()
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "admin-saves.json", result)
    write_text(
        DEPLOYMENT_ROOT / "admin-evidence" / "admin-saves.md",
        "\n".join(
            ["# Admin saves", "", f"Status: {result.get('status')}", ""]
            + [f"- {s.get('entity', '?')}: {s.get('status')}" for s in result.get("saves", [])]
        ),
    )
    return result


def verify_robots_sitemap() -> dict[str, Any]:
    robots = http_get("https://bzpm.ru/robots.txt")
    sitemap = http_get("https://bzpm.ru/sitemap.xml")
    sitemap_valid = False
    url_count = 0
    if sitemap["status_code"] == 200 and sitemap["body"].strip().startswith("<"):
        try:
            root = ET.fromstring(sitemap["body"])
            ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            url_count = len(root.findall(".//sm:url", ns) or root.findall(".//url"))
            sitemap_valid = url_count > 0
        except ET.ParseError:
            pass
    return {
        "robots_status": robots["status_code"],
        "robots_unchanged_hint": "Sitemap:" in robots["body"],
        "sitemap_status": sitemap["status_code"],
        "sitemap_valid": sitemap_valid,
        "sitemap_url_count": url_count,
    }


def build_authority_map() -> None:
    plan = json.loads((DEPLOYMENT_ROOT / "manifests" / "meta-fix-working-plan.json").read_text(encoding="utf-8"))
    entries = []
    for item in plan:
        if not item.get("include"):
            continue
        entries.append(
            {
                "url": item["url"],
                "authority": item["authority"],
                "admin_save_required": item["authority"] == "ADMIN",
                "file_deploy_required": item["authority"] == "CONTROLLER",
                "rollback": "admin field restore" if item["authority"] == "ADMIN" else "FTP rollback file",
            }
        )
    write_json(DEPLOYMENT_ROOT / "manifests" / "fix-authority-map.json", entries)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "fix-authority-map.md",
        "\n".join(["# Fix authority map", ""] + [f"- {e['url']}: **{e['authority']}**" for e in entries]),
    )


def build_copy_proposals() -> None:
    proposals = []
    for slug, fields in CATEGORY_META.items():
        proposals.append(
            {
                "entity": f"category/{slug}",
                "proposed_title": fields["meta_title"],
                "proposed_description": fields["meta_description"],
                "authority": "ADMIN",
            }
        )
    proposals.append({"entity": "store/home", **STORE_META_TRIM, "authority": "ADMIN"})
    proposals.append({"entity": "information/contact", **INFO_META["contact"], "authority": "ADMIN"})
    write_json(DEPLOYMENT_ROOT / "manifests" / "meta-copy-proposals.json", proposals)
    write_text(DEPLOYMENT_ROOT / "manifests" / "meta-copy-proposals.md", "# Meta copy proposals\n\nSee JSON.\n")


def build_implementation_plan() -> None:
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md",
        "\n".join(
            [
                "# Implementation plan",
                "",
                "## PLAN C — Hybrid",
                "",
                "1. FTP deploy (3 files max):",
                f"   - `{REMOTE_CATEGORY}` — noindex + clean canonical for query variants",
                f"   - `{REMOTE_HEADER_CTRL}` — noindex for cart/checkout/search/compare/wishlist/account",
                f"   - `{REMOTE_CONTACT}` — canonical /contact; noindex legacy query route",
                "",
                "2. Admin saves:",
                "   - Category meta_title/meta_description for 6 PLP categories",
                "   - Store config_meta_description trim (home)",
                "   - Contact information meta_description if page exists in admin",
                "",
                "## Excluded",
                "- Product PDP",
                "- header.twig / footer.twig",
                "- robots.txt / sitemap",
            ]
        ),
    )
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "admin-actions.json",
        {
            "categories": list(CATEGORY_META.keys()),
            "store_fields": ["config_meta_description"],
            "information": ["contact meta_description"],
        },
    )


def ftp_source_discovery(ftp: ftplib.FTP) -> None:
    for remote in SOURCE_PATHS:
        if ftp_exists(ftp, remote):
            data = ftp_download(ftp, remote)
            name = remote.replace("/public_html/", "").replace("/", "__")
            (DEPLOYMENT_ROOT / "source" / name).write_bytes(data)
            if remote.endswith(".php"):
                short = remote.split("/")[-1]
                (DEPLOYMENT_ROOT / "source" / short).write_bytes(data)


def run_all(deploy: bool, admin: bool) -> int:
    ensure_dirs()
    build_working_plan()
    crawl_urls(BEFORE_URLS, "meta-before")
    ftp_fields = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    remotes = [REMOTE_CATEGORY, REMOTE_HEADER_CTRL, REMOTE_CONTACT]
    with ftp_connect(ftp_fields) as ftp:
        ftp_source_discovery(ftp)
        backup_hashes = backup_remote_files(ftp, remotes)
        patch_result = prepare_patches()
        dry_run_diff()
        build_authority_map()
        build_copy_proposals()
        build_implementation_plan()
        if not all(r[0] for r in patch_result["lint"].values()):
            print("PHP lint failed", patch_result["lint"], file=sys.stderr)
            return 1
        if deploy:
            if not verify_pre_upload(ftp, backup_hashes):
                print("STOP — LIVE FILE CHANGED SINCE BACKUP", file=sys.stderr)
                return 2
            deploy_files(ftp, patch_result["files"])
    admin_result = {"status": "SKIPPED"}
    if admin:
        admin_result = phase_admin_saves()
    crawl_urls(BEFORE_URLS, "meta-after")
    preservation = verify_robots_sitemap()
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "run-summary.json",
        {
            "operation_id": OPERATION_ID,
            "deploy": deploy,
            "admin": admin,
            "admin_result": admin_result,
            "preservation": preservation,
            "finished_at": utc_now(),
        },
    )
    print(json.dumps({"deploy": deploy, "admin_status": admin_result.get("status"), "preservation": preservation}, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("plan", "crawl-before", "deploy", "all"), default="all")
    parser.add_argument("--no-deploy", action="store_true")
    parser.add_argument("--no-admin", action="store_true")
    args = parser.parse_args()
    if args.phase == "plan":
        ensure_dirs()
        build_working_plan()
        build_copy_proposals()
        build_implementation_plan()
        return 0
    if args.phase == "crawl-before":
        ensure_dirs()
        crawl_urls(BEFORE_URLS, "meta-before")
        return 0
    deploy = args.phase == "deploy" or (args.phase == "all" and not args.no_deploy)
    admin = not args.no_admin
    return run_all(deploy=deploy, admin=admin)


if __name__ == "__main__":
    raise SystemExit(main())
