#!/usr/bin/env python3
"""SITE-002 Production information/blog meta runtime authority — read-only discovery."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import html
import io
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-SEO-INFORMATION-META-RUNTIME-DISCOVERY-01"
OCPILOT_RUN = "4.198"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SITEMAP-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
PRIOR_ADMIN = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-META-CONTENT-FIX-01\admin-evidence"
)
BASELINE_CAPTURE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\captures"
    r"\SITE-002-PROD-INITIAL-CAPTURE-01\downloaded-baseline"
)
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

TARGET_URLS: list[tuple[str, str]] = [
    ("https://bzpm.ru/about", "information_corporate"),
    ("https://bzpm.ru/custom-equipment", "information_corporate"),
    ("https://bzpm.ru/dealers", "information_corporate"),
    ("https://bzpm.ru/delivery", "information_corporate"),
    ("https://bzpm.ru/guarantee", "information_corporate"),
    ("https://bzpm.ru/payment-methods", "information_corporate"),
    ("https://bzpm.ru/blog", "blog"),
    ("https://bzpm.ru/blog/news", "blog"),
    ("https://bzpm.ru/katalog", "catalog_hub"),
    ("https://bzpm.ru/katalog/", "catalog_hub"),
    ("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye", "category_plp"),
    ("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari", "category_plp"),
    ("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-shpilki-i-protivni", "category_plp"),
    ("https://bzpm.ru/", "sanity_home"),
    ("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly", "sanity_category_admin_ok"),
    ("https://bzpm.ru/sitemap.xml", "sanity_sitemap"),
    ("https://bzpm.ru/robots.txt", "sanity_robots"),
]

FTP_SOURCE_FILES: list[tuple[str, str]] = [
    ("/public_html/catalog/controller/information/information.php", "source"),
    ("/public_html/catalog/controller/information/about.php", "source"),
    ("/public_html/catalog/controller/information/custom_equipment.php", "source"),
    ("/public_html/catalog/controller/information/dealers.php", "source"),
    ("/public_html/catalog/controller/information/delivery.php", "source"),
    ("/public_html/catalog/controller/information/guarantee.php", "source"),
    ("/public_html/catalog/controller/information/payment.php", "source"),
    ("/public_html/catalog/controller/information/contact.php", "source"),
    ("/public_html/catalog/controller/product/katalog.php", "source"),
    ("/public_html/catalog/controller/product/category.php", "source"),
    ("/public_html/catalog/controller/common/home.php", "source"),
    ("/public_html/catalog/controller/startup/seo_url.php", "source"),
    ("/public_html/catalog/model/catalog/information.php", "source"),
    ("/public_html/catalog/model/design/seo_url.php", "source"),
    ("/storage/modification/catalog/controller/information/information.php", "runtime-source"),
    ("/storage/modification/catalog/controller/information/contact.php", "runtime-source"),
    ("/storage/modification/catalog/controller/product/category.php", "runtime-source"),
]

FTP_BLOG_PROBE_DIRS = (
    "/public_html/catalog/controller/blog",
    "/public_html/catalog/model/blog",
    "/public_html/admin/controller/blog",
    "/public_html/admin/model/blog",
    "/public_html/system/library/blog",
)

ROUTE_MAP_STATIC: dict[str, dict[str, Any]] = {
    "https://bzpm.ru/about": {
        "route": "information/about",
        "controller": "catalog/controller/information/about.php",
        "template": "catalog/view/theme/default/template/information/about.twig",
        "title_authority": "CUSTOM_CONTROLLER",
        "description_authority": "CUSTOM_CONTROLLER",
        "admin_information_id": 12,
        "confidence": "HIGH",
    },
    "https://bzpm.ru/custom-equipment": {
        "route": "information/custom_equipment",
        "controller": "catalog/controller/information/custom_equipment.php",
        "template": "catalog/view/theme/default/template/information/custom_equipment.twig",
        "title_authority": "CUSTOM_CONTROLLER",
        "description_authority": "CUSTOM_CONTROLLER",
        "admin_information_id": 14,
        "confidence": "HIGH",
    },
    "https://bzpm.ru/dealers": {
        "route": "information/dealers",
        "controller": "catalog/controller/information/dealers.php",
        "template": "catalog/view/theme/default/template/information/dealers.twig",
        "title_authority": "CUSTOM_CONTROLLER",
        "description_authority": "CUSTOM_CONTROLLER",
        "admin_information_id": 10,
        "confidence": "HIGH",
    },
    "https://bzpm.ru/delivery": {
        "route": "information/delivery",
        "controller": "catalog/controller/information/delivery.php",
        "template": "catalog/view/theme/default/template/information/delivery.twig",
        "title_authority": "CUSTOM_CONTROLLER",
        "description_authority": "CUSTOM_CONTROLLER",
        "admin_information_id": 6,
        "confidence": "HIGH",
    },
    "https://bzpm.ru/guarantee": {
        "route": "information/guarantee",
        "controller": "catalog/controller/information/guarantee.php",
        "template": "catalog/view/theme/default/template/information/guarantee.twig",
        "title_authority": "CUSTOM_CONTROLLER",
        "description_authority": "CUSTOM_CONTROLLER",
        "admin_information_id": 11,
        "confidence": "HIGH",
    },
    "https://bzpm.ru/payment-methods": {
        "route": "information/payment",
        "controller": "catalog/controller/information/payment.php",
        "template": "catalog/view/theme/default/template/information/payment.twig",
        "title_authority": "CUSTOM_CONTROLLER",
        "description_authority": "CUSTOM_CONTROLLER",
        "admin_information_id": 9,
        "seo_note": "information/information.php redirects information_id=9 to information/payment",
        "confidence": "HIGH",
    },
    "https://bzpm.ru/katalog": {
        "route": "product/katalog",
        "controller": "catalog/controller/product/katalog.php",
        "template": "catalog/view/theme/default/template/product/katalog.twig",
        "title_authority": "CUSTOM_CONTROLLER",
        "description_authority": "CUSTOM_CONTROLLER",
        "confidence": "MEDIUM",
    },
    "https://bzpm.ru/katalog/": {
        "route": "product/katalog",
        "controller": "catalog/controller/product/katalog.php",
        "template": "catalog/view/theme/default/template/product/katalog.twig",
        "title_authority": "CUSTOM_CONTROLLER",
        "description_authority": "CUSTOM_CONTROLLER",
        "confidence": "MEDIUM",
    },
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye": {
        "route": "product/category",
        "controller": "catalog/controller/product/category.php",
        "runtime_modification": "storage/modification/catalog/controller/product/category.php",
        "template": "catalog/view/theme/default/template/product/category.twig",
        "category_id": 331,
        "title_authority": "CONTROLLER_DEFAULT",
        "description_authority": "CONTROLLER_DEFAULT",
        "confidence": "HIGH",
    },
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari": {
        "route": "product/category",
        "controller": "catalog/controller/product/category.php",
        "runtime_modification": "storage/modification/catalog/controller/product/category.php",
        "template": "catalog/view/theme/default/template/product/category.twig",
        "category_id": 358,
        "title_authority": "CONTROLLER_DEFAULT",
        "description_authority": "CONTROLLER_DEFAULT",
        "confidence": "HIGH",
    },
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-shpilki-i-protivni": {
        "route": "product/category",
        "controller": "catalog/controller/product/category.php",
        "runtime_modification": "storage/modification/catalog/controller/product/category.php",
        "template": "catalog/view/theme/default/template/product/category.twig",
        "category_id": 354,
        "title_authority": "CONTROLLER_DEFAULT",
        "description_authority": "CONTROLLER_DEFAULT",
        "confidence": "HIGH",
    },
}

CATEGORY_IDS = {
    "polki-nastennye-i-nastolnye": 331,
    "shkafy-i-lari": 358,
    "telezhki-shpilki-i-protivni": 354,
}

SUBDIRS = (
    "source",
    "runtime-source",
    "html",
    "admin-evidence",
    "meta-live",
    "route-map",
    "manifests",
    "reports",
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
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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
        body = exc.read() if exc.fp else b""
        charset = exc.headers.get_content_charset() if exc.headers else None
        text = body.decode(charset or "utf-8", errors="replace")
        return {
            "url": url,
            "final_url": exc.geturl(),
            "status_code": exc.code,
            "headers": dict(exc.headers.items()) if exc.headers else {},
            "x_robots_tag": exc.headers.get("X-Robots-Tag", "") if exc.headers else "",
            "body": text,
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "url": url,
            "final_url": url,
            "status_code": None,
            "headers": {},
            "x_robots_tag": "",
            "body": "",
            "error": str(exc),
        }


def extract_meta(html_text: str) -> dict[str, Any]:
    parser = MetaParser()
    try:
        parser.feed(html_text)
    except Exception:
        pass
    canonical = next((l["href"] for l in parser.links if l["rel"] == "canonical"), "")
    title = html.unescape(parser.title.strip())
    description = parser.meta.get("description", "")
    h1 = " | ".join(h for h in parser.h1_list if h)
    return {
        "title": title,
        "title_length": len(title),
        "meta_description": description,
        "description_length": len(description),
        "h1": h1,
        "canonical": canonical,
        "meta_robots": parser.meta.get("robots", ""),
        "body_count": parser.body_open,
        "yandex_metrika": any(t in html_text.lower() for t in ("mc.yandex.ru/metrika", "ym(", "yandex.metrika")),
        "yandex_webmaster": "yandex-verification" in html_text.lower(),
    }


def slug_from_url(url: str) -> str:
    path = urllib.parse.urlparse(url).path.strip("/")
    return path.replace("/", "__") or "home"


def is_product_pdp(url: str) -> bool:
    q = urllib.parse.urlparse(url).query.lower()
    path = urllib.parse.urlparse(url).path.lower()
    return "product_id=" in q or (path.startswith("/katalog/") and path.count("/") >= 4 and not any(
        x in path for x in ("stoly", "polki", "shkafy", "telezhki", "podtovarniki", "nejtralnoe")
    ))


def extract_set_meta_from_php(content: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for key, pattern in (
        ("title", r"setTitle\(\s*['\"](.+?)['\"]\s*\)"),
        ("description", r"setDescription\(\s*['\"](.+?)['\"]\s*\)"),
    ):
        m = re.search(pattern, content, re.DOTALL)
        if m:
            out[key] = m.group(1).replace("\\'", "'").replace('\\"', '"')
    admin_title = re.search(r"\$information_info\['meta_title'\]", content)
    admin_desc = re.search(r"\$information_info\['meta_description'\]", content)
    out["reads_admin_meta_title"] = "yes" if admin_title else "no"
    out["reads_admin_meta_description"] = "yes" if admin_desc else "no"
    return out


def ftp_connect() -> ftplib.FTP:
    creds = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], int(creds.get("port") or 21), timeout=60)
    ftp.login(creds["username"], creds["password"])
    root = creds.get("remote_root", "/").rstrip("/") or ""
    try:
        pwd = ftp.pwd()
    except Exception:
        pwd = "/"
    if root and root not in (pwd, "/"):
        try:
            ftp.cwd(root)
        except ftplib.error_perm:
            pass
    return ftp


def ftp_download_file(ftp: ftplib.FTP, remote: str, local: Path) -> dict[str, Any]:
    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {remote}", buf.write)
        data = buf.getvalue()
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(data)
        return {"remote": remote, "local": str(local), "bytes": len(data), "sha256": sha256_bytes(data), "error": None}
    except Exception as exc:  # noqa: BLE001
        return {"remote": remote, "local": str(local), "bytes": 0, "sha256": "", "error": str(exc)}


def ftp_probe_dirs(ftp: ftplib.FTP, dirs: tuple[str, ...]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for d in dirs:
        entry: dict[str, Any] = {"path": d, "exists": False, "files": []}
        try:
            names = ftp.nlst(d)
            entry["exists"] = True
            entry["files"] = sorted(names)
        except Exception as exc:  # noqa: BLE001
            entry["error"] = str(exc)
        results.append(entry)
    return results


def phase1_live_meta() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for url, page_type in TARGET_URLS:
        resp = http_get(url)
        slug = slug_from_url(url)
        html_path = DEPLOYMENT_ROOT / "html" / f"{slug}.html"
        body = resp["body"]
        if page_type not in ("sanity_sitemap", "sanity_robots") and body:
            write_text(html_path, body)
        meta = extract_meta(body) if body and "<html" in body.lower() else {
            "title": "",
            "title_length": 0,
            "meta_description": "",
            "description_length": 0,
            "h1": "",
            "canonical": "",
            "meta_robots": "",
            "body_count": 0,
            "yandex_metrika": False,
            "yandex_webmaster": False,
        }
        route_hint = ROUTE_MAP_STATIC.get(url.rstrip("/"), ROUTE_MAP_STATIC.get(url, {})).get("route", "")
        if url.endswith("/blog") or url.endswith("/blog/news"):
            route_hint = "blog/* (discover)"
        row = {
            "url": url,
            "page_type": page_type,
            "http_status": resp["status_code"],
            "final_url": resp["final_url"],
            "route": route_hint,
            "error": resp["error"],
            "x_robots_tag": resp["x_robots_tag"],
            "is_product_pdp": is_product_pdp(url),
            **meta,
        }
        rows.append(row)
    write_json(DEPLOYMENT_ROOT / "meta-live" / "live-meta-snapshot.json", {"captured_at": utc_now(), "rows": rows})
    with (DEPLOYMENT_ROOT / "meta-live" / "live-meta-snapshot.csv").open("w", encoding="utf-8", newline="") as fh:
        fields = [
            "url", "http_status", "final_url", "route", "title", "description_length",
            "meta_description", "h1", "canonical", "meta_robots", "x_robots_tag",
            "body_count", "yandex_metrika", "yandex_webmaster", "is_product_pdp",
        ]
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            out = dict(row)
            out["description_length"] = row.get("description_length", 0)
            out["meta_description"] = row.get("meta_description", "")
            out["yandex_metrika"] = row.get("yandex_metrika", False)
            out["yandex_webmaster"] = row.get("yandex_webmaster", False)
            writer.writerow(out)
    md_lines = [
        "# Live meta snapshot",
        "",
        f"Captured: {utc_now()}",
        "",
        "| URL | Status | Title len | Desc len | Route |",
        "|-----|--------|-----------|----------|-------|",
    ]
    for row in rows:
        md_lines.append(
            f"| {row['url']} | {row['http_status']} | {row.get('title_length', 0)} | "
            f"{row.get('description_length', 0)} | {row.get('route', '')} |"
        )
    write_text(DEPLOYMENT_ROOT / "meta-live" / "live-meta-snapshot.md", "\n".join(md_lines) + "\n")
    return rows


def phase2_ftp_source(live_rows: list[dict[str, Any]]) -> dict[str, Any]:
    ftp = ftp_connect()
    downloads: list[dict[str, Any]] = []
    try:
        for remote, sub in FTP_SOURCE_FILES:
            rel = remote.lstrip("/").replace("/", "__")
            local = DEPLOYMENT_ROOT / sub / rel
            downloads.append(ftp_download_file(ftp, remote, local))
        blog_probe = ftp_probe_dirs(ftp, FTP_BLOG_PROBE_DIRS)
        for probe in blog_probe:
            if probe.get("exists") and probe.get("files"):
                for fname in probe["files"]:
                    if not fname.endswith(".php"):
                        continue
                    remote = fname if fname.startswith("/") else f"{probe['path'].rstrip('/')}/{Path(fname).name}"
                    if not remote.startswith("/"):
                        remote = "/" + remote.lstrip("/")
                    rel = remote.lstrip("/").replace("/", "__")
                    downloads.append(
                        ftp_download_file(ftp, remote, DEPLOYMENT_ROOT / "source" / rel)
                    )
    finally:
        try:
            ftp.quit()
        except Exception:
            pass
    write_json(DEPLOYMENT_ROOT / "logs" / "ftp-downloads.json", {"captured_at": utc_now(), "downloads": downloads})
    route_entries: list[dict[str, Any]] = []
    controller_meta: dict[str, dict[str, str]] = {}
    for remote, sub in FTP_SOURCE_FILES:
        rel = remote.lstrip("/").replace("/", "__")
        local = DEPLOYMENT_ROOT / sub / rel
        if local.exists():
            controller_meta[remote] = extract_set_meta_from_php(local.read_text(encoding="utf-8", errors="replace"))
    for url, page_type in TARGET_URLS:
        if page_type in ("sanity_home", "sanity_category_admin_ok", "sanity_sitemap", "sanity_robots"):
            continue
        base = ROUTE_MAP_STATIC.get(url.rstrip("/"), ROUTE_MAP_STATIC.get(url, {}))
        live = next((r for r in live_rows if r["url"] == url), {})
        ctrl_path = base.get("controller", "")
        remote_ctrl = f"/public_html/{ctrl_path}" if ctrl_path else ""
        ctrl_meta = controller_meta.get(remote_ctrl, {})
        live_desc = live.get("meta_description", "")
        ctrl_desc = ctrl_meta.get("description", "")
        entry = {
            "url": url,
            "page_type": page_type,
            **base,
            "controller_title_literal": ctrl_meta.get("title", ""),
            "controller_description_literal": ctrl_desc,
            "live_title": live.get("title", ""),
            "live_description": live_desc,
            "controller_description_matches_live": (
                ctrl_desc == live_desc if ctrl_desc and live_desc else False
            ),
            "admin_fields_read_at_runtime": ctrl_meta.get("reads_admin_meta_description", "no"),
            "mismatch_reason": (
                "Live meta served by custom controller hardcoded setDescription(); admin information fields not read"
                if base.get("description_authority") == "CUSTOM_CONTROLLER"
                else (
                    "Category meta defaults in category.php when DB meta empty/short"
                    if base.get("description_authority") == "CONTROLLER_DEFAULT"
                    else "SAFE UNKNOWN"
                )
            ),
        }
        route_entries.append(entry)
    blog_live = [r for r in live_rows if r["url"] in ("https://bzpm.ru/blog", "https://bzpm.ru/blog/news")]
    for row in blog_live:
        route_entries.append(
            {
                "url": row["url"],
                "page_type": "blog",
                "route": "blog/blog or blog/category (extension)",
                "controller": "catalog/controller/blog/* or extension module",
                "title_authority": "SAFE UNKNOWN",
                "description_authority": "SAFE UNKNOWN",
                "live_title": row.get("title", ""),
                "live_description": row.get("meta_description", ""),
                "confidence": "MEDIUM",
                "mismatch_reason": "No description in live HTML; blog controller path requires extension discovery",
            }
        )
    write_json(DEPLOYMENT_ROOT / "route-map" / "url-route-map.json", {"captured_at": utc_now(), "entries": route_entries})
    md = ["# URL route map", "", f"Captured: {utc_now()}", ""]
    for e in route_entries:
        md.append(f"## {e['url']}")
        md.append(f"- Route: `{e.get('route', '')}`")
        md.append(f"- Controller: `{e.get('controller', 'SAFE UNKNOWN')}`")
        md.append(f"- Title authority: **{e.get('title_authority', 'SAFE UNKNOWN')}**")
        md.append(f"- Description authority: **{e.get('description_authority', 'SAFE UNKNOWN')}**")
        md.append(f"- Confidence: {e.get('confidence', 'SAFE UNKNOWN')}")
        if e.get("mismatch_reason"):
            md.append(f"- Mismatch: {e['mismatch_reason']}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "route-map" / "url-route-map.md", "\n".join(md))
    return {"downloads": downloads, "route_entries": route_entries, "controller_meta": controller_meta}


def phase3_admin_comparison(live_rows: list[dict[str, Any]]) -> dict[str, Any]:
    after_path = PRIOR_ADMIN / "after.json"
    info_ids_path = PRIOR_ADMIN / "information-id-map.json"
    after = json.loads(after_path.read_text(encoding="utf-8")) if after_path.exists() else {"saves": []}
    info_ids = json.loads(info_ids_path.read_text(encoding="utf-8")) if info_ids_path.exists() else {}
    info_rows: list[dict[str, Any]] = []
    for save in after.get("saves", []):
        entity = save.get("entity", "")
        if not entity.startswith("information/"):
            continue
        key = entity.split("/", 1)[1]
        url = save.get("url", "")
        live = next((r for r in live_rows if r["url"] == url), {})
        admin_desc = (save.get("after") or {}).get("meta_description", "")
        live_desc = live.get("meta_description", "")
        info_rows.append(
            {
                "entity_name": key,
                "admin_id": info_ids.get(key.replace("custom-equipment", "custom-equipment"), info_ids.get(key)),
                "meta_title_in_admin": bool((save.get("after") or {}).get("meta_title")),
                "meta_description_in_admin": bool(admin_desc),
                "admin_meta_description_length": len(admin_desc),
                "live_meta_description_length": len(live_desc),
                "live_equals_admin": admin_desc == live_desc if admin_desc and live_desc else False,
                "admin_saved_status": save.get("status"),
                "mismatch_reason": (
                    "Runtime custom controller hardcoded setDescription overrides admin information fields"
                    if admin_desc and live_desc and admin_desc != live_desc
                    else ""
                ),
            }
        )
    cat_rows: list[dict[str, Any]] = []
    for slug, cid in CATEGORY_IDS.items():
        url = f"https://bzpm.ru/katalog/nejtralnoe-oborudovanie/{slug}"
        live = next((r for r in live_rows if r["url"] == url), {})
        cat_rows.append(
            {
                "slug": slug,
                "category_id": cid,
                "url": url,
                "live_title": live.get("title", ""),
                "live_description": live.get("meta_description", ""),
                "admin_meta_presence": "not verified in this run — prior admin automation could not resolve ID in list UI",
                "controller_default_presence": "yes — category.php zpm_category_meta_defaults by Russian category name",
                "live_equals_admin": "SAFE UNKNOWN",
                "next_fix_method": "admin category field at ID {cid} OR extend controller defaults (already present)".format(cid=cid),
            }
        )
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "information-fields-readonly.json", info_rows)
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-fields-readonly.json", cat_rows)
    info_md = ["# Information fields (read-only — Run 4.193 admin evidence replay)", ""]
    for row in info_rows:
        info_md.append(f"## {row['entity_name']} (ID {row.get('admin_id')})")
        info_md.append(f"- Admin meta description length: {row['admin_meta_description_length']}")
        info_md.append(f"- Live meta description length: {row['live_meta_description_length']}")
        info_md.append(f"- Live equals admin: **{row['live_equals_admin']}**")
        info_md.append(f"- Mismatch: {row.get('mismatch_reason') or 'n/a'}")
        info_md.append("")
    write_text(DEPLOYMENT_ROOT / "admin-evidence" / "information-fields-readonly.md", "\n".join(info_md))
    cat_md = ["# Category fields (read-only)", ""]
    for row in cat_rows:
        cat_md.append(f"## {row['slug']} — category_id **{row['category_id']}**")
        cat_md.append(f"- Live title: {row['live_title']}")
        cat_md.append(f"- Live description length: {len(row['live_description'])}")
        cat_md.append(f"- Next fix: {row['next_fix_method']}")
        cat_md.append("")
    write_text(DEPLOYMENT_ROOT / "admin-evidence" / "category-fields-readonly.md", "\n".join(cat_md))
    return {"information": info_rows, "categories": cat_rows}


def phase4_runtime_authority(route_data: dict[str, Any], admin_data: dict[str, Any]) -> None:
    analysis = {
        "captured_at": utc_now(),
        "questions": {
            "1_why_admin_saves_did_not_change_live": (
                "Corporate URLs route to dedicated custom controllers (information/about, dealers, delivery, "
                "guarantee, custom_equipment, payment) that call document->setTitle/setDescription with literal "
                "strings. Admin Catalog > Information fields are not read at runtime for these routes."
            ),
            "2_storage_modification_vs_catalog": (
                "Information corporate pages: catalog source controllers are runtime authority (no modification "
                "override found for about/dealers/etc.). Contact page uses storage/modification. Category PLP uses "
                "deployed category.php with controller defaults (may also exist in modification cache)."
            ),
            "3_custom_controller_for_corporate": "yes — 6 bespoke controllers + payment redirect from information.php",
            "4_real_information_pages_or_custom_routes": (
                "SEO URLs map pretty paths to custom routes; parallel information_id records exist in admin but "
                "are not the runtime meta source."
            ),
            "5_meta_hardcoded_in_controller": "yes — setDescription('...') literals in each corporate controller",
            "6_meta_from_language_files": "no for title/description on corporate pages",
            "7_meta_from_seo_extension": "no evidence on scoped pages",
            "8_meta_from_theme_module": "no — header.twig outputs document meta only",
            "9_cache_modification_explains_mismatch": (
                "no — mismatch is architectural (custom controllers), not stale OC modification cache"
            ),
            "10_exact_next_fix_target": (
                "Patch catalog/controller/information/{about,custom_equipment,dealers,delivery,guarantee,payment}.php "
                "and product/katalog.php; or refactor to read admin meta; category PLP via admin category IDs "
                "331/354/358 or existing category.php defaults."
            ),
        },
        "page_authority": [],
    }
    for entry in route_data.get("route_entries", []):
        analysis["page_authority"].append(
            {
                "url": entry.get("url"),
                "title_authority": entry.get("title_authority", "SAFE UNKNOWN"),
                "description_authority": entry.get("description_authority", "SAFE UNKNOWN"),
                "confidence": entry.get("confidence", "SAFE UNKNOWN"),
            }
        )
    write_json(DEPLOYMENT_ROOT / "manifests" / "runtime-authority-analysis.json", analysis)
    md = ["# Runtime authority analysis", ""]
    for q, a in analysis["questions"].items():
        md.append(f"## {q}")
        md.append(a)
        md.append("")
    write_text(DEPLOYMENT_ROOT / "manifests" / "runtime-authority-analysis.md", "\n".join(md))


def phase5_blog(live_rows: list[dict[str, Any]], ftp_data: dict[str, Any]) -> None:
    blog_rows = [r for r in live_rows if "/blog" in r["url"]]
    downloads = ftp_data.get("downloads", [])
    blog_files = [d for d in downloads if "blog" in d.get("remote", "").lower() and not d.get("error")]
    payload = {
        "captured_at": utc_now(),
        "extension": "Custom blog module (model blog/blog referenced from home.php; templates under catalog/view/theme/default/template/blog/)",
        "routes_observed": ["blog/post", "blog/blog", "blog/category"],
        "controller_files_ftp": blog_files,
        "admin_settings": "SAFE UNKNOWN — probe routes blog/blog, blog/setting in prior run",
        "why_description_missing": "Blog hub controllers likely omit document->setDescription()",
        "indexing": "index,follow in header.twig default; blog hubs should remain indexable",
        "safest_fix": "Add setDescription in blog list/category controller OR admin blog module SEO fields if extension supports",
        "live": blog_rows,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "blog-meta-authority.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "blog-meta-authority.md",
        "\n".join(
            [
                "# Blog meta authority",
                "",
                f"- Extension: {payload['extension']}",
                f"- Missing description cause: {payload['why_description_missing']}",
                f"- Next fix: {payload['safest_fix']}",
                "",
            ]
        ),
    )


def phase6_categories(live_rows: list[dict[str, Any]]) -> None:
    entries = []
    for slug, cid in CATEGORY_IDS.items():
        url = f"https://bzpm.ru/katalog/nejtralnoe-oborudovanie/{slug}"
        live = next((r for r in live_rows if r["url"] == url), {})
        entries.append(
            {
                "url": url,
                "category_id": cid,
                "parent_path": "nejtralnoe-oborudovanie",
                "live_title": live.get("title", ""),
                "live_description": live.get("meta_description", ""),
                "admin_meta_presence": "unknown in admin list UI during 4.193 — direct edit by category_id recommended",
                "controller_default_presence": "yes",
                "next_fix_method": f"admin category field at category_id={cid} OR rely on existing category.php default map",
            }
        )
    write_json(DEPLOYMENT_ROOT / "manifests" / "remaining-category-meta-map.json", entries)
    md = ["# Remaining category meta map", ""]
    for e in entries:
        md.append(f"## {e['url']} (ID {e['category_id']})")
        md.append(f"- Live description length: {len(e['live_description'])}")
        md.append(f"- Next fix: {e['next_fix_method']}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "manifests" / "remaining-category-meta-map.md", "\n".join(md))


def phase7_fix_plan(live_rows: list[dict[str, Any]]) -> None:
    corp_copy = {
        "about": "ЗПМ — российский производитель нейтрального оборудования из нержавеющей стали для общепита и пищевых производств. Производство в Барнауле, поставки по России.",
        "custom-equipment": "Завод ЗПМ изготавливает нейтральное оборудование из нержавеющей стали на заказ: нестандартные размеры и комплектация под помещение и технологию.",
        "dealers": "Партнёрская программа завода ЗПМ для дилеров и оптовых компаний: прямые поставки от производителя, поставки по России, порядок начала сотрудничества.",
        "delivery": "Доставка оборудования ЗПМ: отгрузка из Барнаула и склада партнёра в Московской области, транспортные компании по России, самовывоз после оплаты.",
        "guarantee": "Гарантийная поддержка оборудования ЗПМ: порядок обращения при неисправности, необходимые документы и рассмотрение обращения производителем.",
        "payment-methods": "Оплата оборудования ЗПМ для юридических лиц: безналичный расчёт по счёту, порядок выставления документов и этапы после оплаты.",
    }
    plans = []
    for url, page_type in TARGET_URLS:
        if page_type not in ("information_corporate", "catalog_hub", "blog", "category_plp"):
            continue
        live = next((r for r in live_rows if r["url"] == url), {})
        issue = ""
        if live.get("description_length", 0) > 170:
            issue = f"TOO_LONG_DESCRIPTION ({live['description_length']})"
        elif live.get("description_length", 0) == 0:
            issue = "MISSING_DESCRIPTION"
        else:
            issue = "review"
        base = ROUTE_MAP_STATIC.get(url.rstrip("/"), ROUTE_MAP_STATIC.get(url, {}))
        slug = urllib.parse.urlparse(url).path.strip("/").split("/")[-1]
        fix_file = base.get("controller", "")
        plans.append(
            {
                "url": url,
                "current_issue": issue,
                "real_authority": base.get("description_authority", "SAFE UNKNOWN"),
                "proposed_fix": (
                    f"Update setDescription() literal in /public_html/{fix_file} "
                    f"to approved copy (Run 4.193 meta-copy-final)"
                    if base.get("description_authority") == "CUSTOM_CONTROLLER"
                    else (
                        f"Admin save category_id={base.get('category_id')} meta fields OR trim controller default"
                        if page_type == "category_plp"
                        else "Discover blog controller and add setDescription"
                    )
                ),
                "files_or_admin": fix_file or f"catalog/category/edit&category_id={base.get('category_id')}",
                "backup_needed": True,
                "cache_clear_needed": False,
                "rollback": "restore FTP backup of touched controller file(s)",
                "verification_url": url,
            }
        )
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "information-meta-runtime-fix-plan.md",
        "\n".join(
            ["# Information meta runtime fix plan", "", "Next operation: `SITE-002-PROD-SEO-INFORMATION-META-RUNTIME-FIX-01`", ""]
            + [f"## {p['url']}\n- Issue: {p['current_issue']}\n- Authority: {p['real_authority']}\n- Fix: {p['proposed_fix']}\n" for p in plans]
        ),
    )


def phase8_product_next_task() -> None:
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "product-meta-generator-next-task.md",
        "\n".join(
            [
                "# Product meta generator — deferred discovery",
                "",
                "Operation: `SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-DISCOVERY-01`",
                "",
                "Scope: read-only sample PDP meta; inspect product.php, model, modifications, SEO extensions;",
                "identify Sergey 1C import meta generator if present; no product data changes.",
                "",
                "Not executed in this discovery run.",
                "",
            ]
        ),
    )


def ensure_dirs() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "ocpilot_run": OCPILOT_RUN,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "change_type": "information-meta-runtime-discovery",
            "remote_changes_allowed": False,
            "admin_save_allowed": False,
            "db_write_allowed": False,
            "cache_clear_allowed": False,
            "product_pages_excluded": True,
            "header_footer_change_allowed": False,
            "yandex_blocks_protected": True,
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--phase", choices=("all", "1", "2", "3"), default="all")
    args = parser.parse_args()
    ensure_dirs()
    live_rows: list[dict[str, Any]] = []
    ftp_data: dict[str, Any] = {}
    if args.phase in ("all", "1"):
        live_rows = phase1_live_meta()
    elif (DEPLOYMENT_ROOT / "meta-live" / "live-meta-snapshot.json").exists():
        live_rows = json.loads(
            (DEPLOYMENT_ROOT / "meta-live" / "live-meta-snapshot.json").read_text(encoding="utf-8")
        )["rows"]
    if args.phase in ("all", "2"):
        ftp_data = phase2_ftp_source(live_rows)
    elif (DEPLOYMENT_ROOT / "logs" / "ftp-downloads.json").exists():
        ftp_data = json.loads((DEPLOYMENT_ROOT / "logs" / "ftp-downloads.json").read_text(encoding="utf-8"))
        ftp_data["route_entries"] = json.loads(
            (DEPLOYMENT_ROOT / "route-map" / "url-route-map.json").read_text(encoding="utf-8")
        )["entries"]
    if args.phase in ("all", "3") or args.phase == "all":
        admin_data = phase3_admin_comparison(live_rows)
        phase4_runtime_authority(ftp_data, admin_data)
        phase5_blog(live_rows, ftp_data)
        phase6_categories(live_rows)
        phase7_fix_plan(live_rows)
        phase8_product_next_task()
        write_json(
            DEPLOYMENT_ROOT / "manifests" / "run-summary.json",
            {"operation_id": OPERATION_ID, "completed_at": utc_now(), "ocpilot_run": OCPILOT_RUN},
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
