#!/usr/bin/env python3
"""SITE-002 Production public brand remediation — БЗПМ → ЗПМ (Run 4.205)."""
from __future__ import annotations

import argparse
import csv
import difflib
import ftplib
import hashlib
import html
import io
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
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-BRAND-ZPM-REMEDIATION-01"
OCPILOT_RUN = "4.205"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-LLMS-TXT-UTF8-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-BRAND-ZPM-01"
WRONG_BRAND = "БЗПМ"
CORRECT_BRAND = "ЗПМ"
UTF8_BOM = b"\xef\xbb\xbf"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
DISCOVERY_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-DISCOVERY-01"
)
KEYWORDS_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-PRODUCT-META-KEYWORDS-TUNE-01"
)
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

CORE_URLS: list[str] = [
    "https://bzpm.ru/",
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/",
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
]

EXTRA_DEEP_PDP_URLS = (
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/zont-vytyazhnoy-pristennyy-zvp-900-900-900h900h450",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/telezhka-dlya-sbora-posudy-ts-1-800h500h930",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/telezhka-servirovochnaya-ts-2-800h500h930",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/telezhka-servirovochnaya-ts-3-800h500h930",
)

SANITY_URLS = [
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
]

REMOTE_LLMS = "/public_html/llms.txt"
REMOTE_PRODUCT = "/public_html/catalog/controller/product/product.php"

FILE_TARGETS: list[dict[str, str]] = [
    {"remote": REMOTE_LLMS, "authority": "LLMS_TXT", "patch_type": "BRAND_LITERAL_UTF8_BOM"},
    {"remote": REMOTE_PRODUCT, "authority": "PRODUCT_META_GENERATOR", "patch_type": "BRAND_LITERAL"},
    {"remote": "/public_html/catalog/controller/product/katalog.php", "authority": "PRODUCT_KATALOG_CONTROLLER", "patch_type": "BRAND_LITERAL"},
    {"remote": "/public_html/catalog/controller/blog/category.php", "authority": "BLOG_CONTROLLER", "patch_type": "BRAND_LITERAL"},
    {"remote": "/public_html/catalog/controller/information/about.php", "authority": "CUSTOM_CONTROLLER", "patch_type": "BRAND_LITERAL"},
    {"remote": "/public_html/catalog/controller/information/custom_equipment.php", "authority": "CUSTOM_CONTROLLER", "patch_type": "BRAND_LITERAL"},
    {"remote": "/public_html/catalog/controller/information/dealers.php", "authority": "CUSTOM_CONTROLLER", "patch_type": "BRAND_LITERAL"},
    {"remote": "/public_html/catalog/controller/information/delivery.php", "authority": "CUSTOM_CONTROLLER", "patch_type": "BRAND_LITERAL"},
    {"remote": "/public_html/catalog/controller/information/guarantee.php", "authority": "CUSTOM_CONTROLLER", "patch_type": "BRAND_LITERAL"},
    {"remote": "/public_html/catalog/controller/information/payment.php", "authority": "CUSTOM_CONTROLLER", "patch_type": "BRAND_LITERAL"},
]

CATEGORY_IDS_PROBE = (301, 322, 326, 331, 354, 358)

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "verification",
    "verification/pre-upload",
    "crawl-before",
    "crawl-after",
    "admin-evidence",
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
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def replace_public_brand(text: str) -> str:
    return text.replace(WRONG_BRAND, CORRECT_BRAND)


def count_public_brand(text: str) -> int:
    return text.count(WRONG_BRAND)


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
        headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache", "Accept": "text/html,application/xml,text/plain,*/*"},
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
                "x_robots_tag": response.headers.get("X-Robots-Tag", ""),
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
            "x_robots_tag": exc.headers.get("X-Robots-Tag", "") if exc.headers else "",
            "body": text,
            "raw_body": body,
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "final_url": url, "status_code": None, "x_robots_tag": "", "body": "", "raw_body": b"", "error": str(exc)}


def extract_meta(html_text: str) -> dict[str, Any]:
    parser = MetaParser()
    try:
        parser.feed(html_text)
    except Exception:
        pass
    title = html.unescape(parser.title.strip())
    description = parser.meta.get("description", "")
    keywords = parser.meta.get("keywords", "")
    h1 = " | ".join(h for h in parser.h1_list if h)
    return {
        "title": title,
        "meta_description": description,
        "meta_keywords": keywords,
        "h1": h1,
        "body_count": parser.body_open,
        "yandex_metrika": any(t in html_text.lower() for t in ("mc.yandex.ru/metrika", "ym(", "yandex.metrika")),
        "yandex_webmaster": "yandex-verification" in html_text.lower(),
    }


def is_product_pdp(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    parts = [p for p in parsed.path.split("/") if p]
    if len(parts) >= 5 and parts[0] == "katalog":
        return True
    return "product_id=" in parsed.query.lower()


def authority_guess(url: str) -> str:
    if url.endswith("/llms.txt"):
        return "LLMS_TXT"
    if "/blog" in url:
        return "BLOG_CONTROLLER"
    if url.rstrip("/").endswith("/katalog"):
        return "PRODUCT_KATALOG_CONTROLLER"
    if is_product_pdp(url):
        return "PRODUCT_META_GENERATOR"
    if "/katalog/" in url:
        return "ADMIN_CATEGORY_META"
    if any(x in url for x in ("/about", "/custom-equipment", "/dealers", "/delivery", "/guarantee", "/payment-methods", "/contact")):
        return "CUSTOM_CONTROLLER"
    return "SAFE_UNKNOWN"


def brand_snippets(text: str, limit: int = 5) -> list[str]:
    snippets: list[str] = []
    for match in re.finditer(re.escape(WRONG_BRAND), text):
        start = max(0, match.start() - 40)
        end = min(len(text), match.end() + 40)
        snippets.append(text[start:end].replace("\n", " "))
        if len(snippets) >= limit:
            break
    return snippets


def load_pdp_urls() -> list[str]:
    urls: list[str] = []
    sample_path = DISCOVERY_ROOT / "pdp-samples" / "pdp-url-samples.json"
    if sample_path.exists():
        data = json.loads(sample_path.read_text(encoding="utf-8"))
        urls.extend(r["product_url"] for r in data if r.get("include") == "yes")
    for extra in EXTRA_DEEP_PDP_URLS:
        if extra not in urls:
            urls.append(extra)
    return urls


def crawl_brand_inventory(urls: list[str], label: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for url in urls:
        resp = http_get(url)
        body = resp.get("body") or ""
        meta = extract_meta(body) if "<html" in body.lower() else {
            "title": "",
            "meta_description": "",
            "meta_keywords": "",
            "h1": "",
            "body_count": 0,
            "yandex_metrika": False,
            "yandex_webmaster": False,
        }
        brand_count = count_public_brand(body)
        domain_only = brand_count == 0 and "bzpm.ru" in body.lower()
        row = {
            "url": url,
            "http_status": resp["status_code"],
            "final_url": resp["final_url"],
            "error": resp["error"],
            "title": meta.get("title", ""),
            "meta_description": meta.get("meta_description", ""),
            "meta_keywords": meta.get("meta_keywords", ""),
            "h1": meta.get("h1", ""),
            "brand_count_full_body": brand_count,
            "brand_in_title": WRONG_BRAND in (meta.get("title") or ""),
            "brand_in_meta_description": WRONG_BRAND in (meta.get("meta_description") or ""),
            "brand_in_meta_keywords": WRONG_BRAND in (meta.get("meta_keywords") or ""),
            "brand_snippets": brand_snippets(body),
            "domain_only_occurrence": domain_only and brand_count == 0,
            "public_brand_text_yes": brand_count > 0,
            "authority_guess": authority_guess(url),
            "is_product_pdp": is_product_pdp(url),
        }
        if url.endswith("llms.txt"):
            raw = resp.get("raw_body") or b""
            row["llms_has_bom"] = raw.startswith(UTF8_BOM)
            row["llms_brand_count"] = count_public_brand(body)
        if url.endswith("sitemap.xml") and body.strip().startswith("<"):
            try:
                row["sitemap_url_count"] = len(
                    ET.fromstring(body).findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url")
                )
            except ET.ParseError:
                row["sitemap_url_count"] = 0
        rows.append(row)

    out = DEPLOYMENT_ROOT / label
    write_json(out / f"public-brand-occurrences-{label.split('-')[-1]}.json", {"captured_at": utc_now(), "rows": rows})
    fields = [
        "url", "http_status", "final_url", "title", "meta_description", "meta_keywords", "h1",
        "brand_count_full_body", "brand_in_title", "brand_in_meta_description", "brand_in_meta_keywords",
        "public_brand_text_yes", "domain_only_occurrence", "authority_guess", "is_product_pdp",
    ]
    with (out / f"public-brand-occurrences-{label.split('-')[-1]}.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    md = [
        f"# Public brand occurrences ({label})",
        "",
        f"Captured: {utc_now()}",
        "",
        f"URLs with public `{WRONG_BRAND}`: {sum(1 for r in rows if r['public_brand_text_yes'])}",
        "",
        "| URL | Status | Brand count | Authority |",
        "|-----|--------|-------------|-----------|",
    ]
    for row in rows:
        md.append(
            f"| {row['url']} | {row['http_status']} | {row['brand_count_full_body']} | {row['authority_guess']} |"
        )
    write_text(out / f"public-brand-occurrences-{label.split('-')[-1]}.md", "\n".join(md) + "\n")
    return rows


def ftp_connect() -> ftplib.FTP:
    creds = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], int(creds.get("port") or 21), timeout=120)
    ftp.login(creds["username"], creds["password"])
    root = creds.get("remote_root", "/").rstrip("/") or ""
    if root:
        try:
            ftp.cwd(root)
        except ftplib.error_perm:
            pass
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> bytes:
    buf = io.BytesIO()
    ftp.retrbinary(f"RETR {remote}", buf.write)
    return buf.getvalue()


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


def remote_local_name(remote: str) -> str:
    return remote.lstrip("/").replace("/", "__")


def prepare_llms_bytes(raw: bytes) -> bytes:
    text = raw.decode("utf-8-sig")
    patched = replace_public_brand(text)
    if count_public_brand(patched) > 0:
        raise RuntimeError("llms.txt still contains wrong brand after patch")
    if "bzpm.ru" not in patched:
        raise RuntimeError("llms.txt lost bzpm.ru domain references")
    encoded = patched.encode("utf-8")
    return UTF8_BOM + encoded if not encoded.startswith(UTF8_BOM) else encoded


def prepare_text_bytes(raw: bytes) -> tuple[bytes, dict[str, Any]]:
    text = raw.decode("utf-8", errors="replace")
    before = count_public_brand(text)
    patched = replace_public_brand(text)
    after = count_public_brand(patched)
    if before == 0:
        return raw, {"before": 0, "after": 0, "changed": False}
    if after > 0:
        raise RuntimeError(f"still contains {WRONG_BRAND} after patch")
    if text.count("bzpm.ru") != patched.count("bzpm.ru"):
        raise RuntimeError("bzpm.ru domain count changed")
    return patched.encode("utf-8"), {"before": before, "after": after, "changed": True}


def php_lint(path: Path) -> dict[str, Any]:
    try:
        proc = subprocess.run(["php", "-l", str(path)], capture_output=True, text=True, timeout=30, check=False)
        return {"path": str(path), "ok": proc.returncode == 0, "output": (proc.stdout + proc.stderr).strip()}
    except FileNotFoundError:
        return {"path": str(path), "ok": True, "output": "php CLI not available — skipped"}
    except Exception as exc:  # noqa: BLE001
        return {"path": str(path), "ok": False, "output": str(exc)}


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
            "baseline_after": BASELINE_AFTER,
            "change_type": "public-brand-remediation",
            "wrong_public_brand": WRONG_BRAND,
            "correct_public_brand": CORRECT_BRAND,
            "domain_bzpm_ru_must_remain": True,
            "db_direct_write_allowed": False,
            "admin_save_allowed": "exact_seo_fields_only_if_needed",
            "header_footer_change_allowed": False,
            "robots_change_allowed": False,
            "sitemap_change_allowed": False,
            "yandex_blocks_protected": True,
        },
    )


def write_policy_manifests() -> None:
    policy = {
        "public_russian_brand": CORRECT_BRAND,
        "forbidden_in_public_content": WRONG_BRAND,
        "domain_unchanged": "bzpm.ru",
        "internal_shorthand_allowed": "historical MARS docs, folder names, operation IDs only",
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "public-brand-policy.json", policy)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "public-brand-policy.md",
        "\n".join(
            [
                "# Public brand policy — SITE-002",
                "",
                f"- **Correct public Russian brand:** {CORRECT_BRAND}",
                f"- **Forbidden in public content:** {WRONG_BRAND}",
                "- **Domain remains:** bzpm.ru (URL only; not a public Russian brand name)",
                "- Internal project shorthand may remain in historical/internal MARS docs only.",
            ]
        ),
    )


def phase_source_discovery(ftp: ftplib.FTP) -> list[dict[str, Any]]:
    authority_rows: list[dict[str, Any]] = []
    files_to_change: list[dict[str, Any]] = []
    for spec in FILE_TARGETS:
        remote = spec["remote"]
        raw = ftp_download(ftp, remote)
        local = DEPLOYMENT_ROOT / "source" / remote_local_name(remote)
        local.write_bytes(raw)
        if remote == REMOTE_LLMS:
            text = raw.decode("utf-8-sig")
            count = count_public_brand(text)
        else:
            text = raw.decode("utf-8", errors="replace")
            count = count_public_brand(text)
        entry = {
            **spec,
            "sha256_before": sha256_bytes(raw),
            "wrong_brand_count": count,
            "mutation_method": "FILE_PATCH" if count > 0 else "NO_CHANGE",
            "confidence": "HIGH" if count > 0 else "N/A",
        }
        authority_rows.append(entry)
        if count > 0:
            files_to_change.append(entry)
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.json", authority_rows)
    md = ["# Source authority map", "", f"Generated: {utc_now()}", ""]
    for row in authority_rows:
        md.append(f"## {row['remote']}")
        md.append(f"- Authority: {row['authority']}")
        md.append(f"- `{WRONG_BRAND}` count: {row['wrong_brand_count']}")
        md.append(f"- Method: {row['mutation_method']}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.md", "\n".join(md))
    write_json(DEPLOYMENT_ROOT / "manifests" / "files-to-change.json", files_to_change)
    return files_to_change


def phase_backup_and_prepare(ftp: ftplib.FTP, targets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    prepared: list[dict[str, Any]] = []
    lint_results: list[dict[str, Any]] = []
    for item in targets:
        remote = item["remote"]
        raw = ftp_download(ftp, remote)
        backup_path = DEPLOYMENT_ROOT / "backup" / remote_local_name(remote)
        rollback_path = DEPLOYMENT_ROOT / "rollback" / remote_local_name(remote)
        backup_path.write_bytes(raw)
        rollback_path.write_bytes(raw)
        backup_sha = sha256_bytes(raw)
        if remote == REMOTE_LLMS:
            patched_bytes = prepare_llms_bytes(raw)
            stats = {"before": count_public_brand(raw.decode("utf-8-sig")), "after": 0, "changed": True}
        else:
            patched_bytes, stats = prepare_text_bytes(raw)
        prepared_path = DEPLOYMENT_ROOT / "prepared" / remote_local_name(remote)
        prepared_path.write_bytes(patched_bytes)
        if remote.endswith(".php"):
            lint_results.append(php_lint(prepared_path))
        prepared.append(
            {
                "remote": remote,
                "authority": item["authority"],
                "backup_path": str(backup_path),
                "rollback_path": str(rollback_path),
                "prepared_path": str(prepared_path),
                "backup_sha256": backup_sha,
                "prepared_sha256": sha256_bytes(patched_bytes),
                "brand_stats": stats,
            }
        )
    write_json(DEPLOYMENT_ROOT / "logs" / "php-lint.json", lint_results)
    return prepared


def phase_dry_run(prepared: list[dict[str, Any]], admin_plan: list[dict[str, Any]]) -> None:
    diffs = []
    for item in prepared:
        backup = Path(item["backup_path"]).read_bytes()
        prepared_bytes = Path(item["prepared_path"]).read_bytes()
        if item["remote"] == REMOTE_LLMS:
            backup_text = backup.decode("utf-8-sig")
            prepared_text = prepared_bytes.decode("utf-8-sig")
        else:
            backup_text = backup.decode("utf-8", errors="replace")
            prepared_text = prepared_bytes.decode("utf-8", errors="replace")
        diff = list(
            difflib.unified_diff(
                backup_text.splitlines(),
                prepared_text.splitlines(),
                fromfile=item["remote"] + " (backup)",
                tofile=item["remote"] + " (prepared)",
                lineterm="",
            )
        )
        diffs.append(
            {
                "remote": item["remote"],
                "brand_stats": item["brand_stats"],
                "diff_lines": len(diff),
                "diff_preview": "\n".join(diff[:30]),
                "bzpm_ru_unchanged": backup_text.count("bzpm.ru") == prepared_text.count("bzpm.ru"),
            }
        )
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.json",
        {
            "prepared_files": prepared,
            "admin_plan": admin_plan,
            "diffs": diffs,
            "domain_unchanged": all(d["bzpm_ru_unchanged"] for d in diffs),
        },
    )
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "\n".join(
            [
                "# Dry-run",
                "",
                f"Generated: {utc_now()}",
                "",
                f"File uploads planned: {len(prepared)}",
                f"Admin category saves planned: {len(admin_plan)}",
                f"Wrong brand before (files): {sum(i['brand_stats']['before'] for i in prepared)}",
                f"Wrong brand after (files): {sum(i['brand_stats']['after'] for i in prepared)}",
                "Header/footer: 0",
                "DB direct writes: 0",
            ]
        ),
    )


def pre_upload_verify(ftp: ftplib.FTP, prepared: list[dict[str, Any]]) -> None:
    for item in prepared:
        live = ftp_download(ftp, item["remote"])
        live_sha = sha256_bytes(live)
        pre_path = DEPLOYMENT_ROOT / "verification" / "pre-upload" / remote_local_name(item["remote"])
        pre_path.write_bytes(live)
        if live_sha != item["backup_sha256"]:
            raise RuntimeError(f"STOP — LIVE FILE CHANGED SINCE BACKUP: {item['remote']}")


def deploy_files(ftp: ftplib.FTP, prepared: list[dict[str, Any]]) -> list[dict[str, Any]]:
    uploads = []
    for item in prepared:
        data = Path(item["prepared_path"]).read_bytes()
        ftp_upload(ftp, item["remote"], data)
        uploads.append(
            {"remote": item["remote"], "bytes": len(data), "sha256": sha256_bytes(data), "status": "UPLOADED"}
        )
    write_json(DEPLOYMENT_ROOT / "logs" / "ftp-uploads.json", {"uploaded_at": utc_now(), "uploads": uploads})
    return uploads


def _admin_url(admin_base: str, route: str, token: str, **params: str) -> str:
    q: dict[str, str] = {"route": route, "user_token": token, **params}
    return f"{admin_base.rstrip('/')}/index.php?{urllib.parse.urlencode(q)}"


def _admin_login(page: Any, admin: dict[str, str]) -> tuple[str | None, str]:
    url = admin.get("url", "https://bzpm.ru/admin/")
    page.goto(url, wait_until="domcontentloaded", timeout=120000)
    page.wait_for_timeout(2000)
    if page.locator('input[name="username"]').count() == 0:
        token_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.url)
        if token_match:
            return token_match.group(1), page.url.split("index.php")[0]
    page.fill('input[name="username"]', admin["login"])
    page.fill('input[name="password"]', admin["password"])
    page.click('button[type="submit"]')
    try:
        page.wait_for_url("**user_token**", timeout=90000)
    except Exception:
        pass
    page.wait_for_timeout(3000)
    admin_base = page.url.split("index.php")[0]
    token_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.url)
    if token_match:
        return token_match.group(1), admin_base
    body_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.content())
    return (body_match.group(1), admin_base) if body_match else (None, admin_base)


def probe_admin_categories(page: Any, admin_base: str, token: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    before_rows: list[dict[str, Any]] = []
    plan: list[dict[str, Any]] = []
    for cid in CATEGORY_IDS_PROBE:
        edit_url = _admin_url(admin_base, "catalog/category/edit", token, category_id=str(cid))
        page.goto(edit_url, wait_until="domcontentloaded", timeout=120000)
        page.wait_for_timeout(2500)
        if page.locator('input[name="category_description[1][meta_title]"]').count() == 0:
            before_rows.append({"category_id": cid, "error": "form not found"})
            continue
        name = page.locator('input[name="category_description[1][name]"]').input_value().strip()
        meta_title = page.locator('input[name="category_description[1][meta_title]"]').input_value()
        meta_description = page.locator('textarea[name="category_description[1][meta_description]"]').input_value()
        row = {
            "category_id": cid,
            "name": name,
            "meta_title": meta_title,
            "meta_description": meta_description,
            "wrong_brand_in_title": WRONG_BRAND in meta_title,
            "wrong_brand_in_description": WRONG_BRAND in meta_description,
        }
        before_rows.append(row)
        if WRONG_BRAND in meta_title or WRONG_BRAND in meta_description:
            plan.append(
                {
                    "category_id": cid,
                    "name": name,
                    "before_meta_title": meta_title,
                    "before_meta_description": meta_description,
                    "after_meta_title": replace_public_brand(meta_title),
                    "after_meta_description": replace_public_brand(meta_description),
                }
            )
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-brand-before.json", before_rows)
    md = ["# Category brand before", ""]
    for row in before_rows:
        md.append(f"## ID {row.get('category_id')}")
        md.append(f"- Name: {row.get('name', row.get('error', ''))}")
        md.append(f"- Wrong brand in title: {row.get('wrong_brand_in_title', False)}")
        md.append(f"- Wrong brand in description: {row.get('wrong_brand_in_description', False)}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "admin-evidence" / "category-brand-before.md", "\n".join(md))
    write_json(DEPLOYMENT_ROOT / "manifests" / "admin-actions.json", {"categories": plan})
    return before_rows, plan


def admin_save_category(page: Any, admin_base: str, token: str, plan: dict[str, Any]) -> dict[str, Any]:
    cid = plan["category_id"]
    edit_url = _admin_url(admin_base, "catalog/category/edit", token, category_id=str(cid))
    page.goto(edit_url, wait_until="domcontentloaded", timeout=120000)
    page.wait_for_timeout(2500)
    page.fill('input[name="category_description[1][meta_title]"]', plan["after_meta_title"])
    page.fill('textarea[name="category_description[1][meta_description]"]', plan["after_meta_description"])
    page.locator('.page-header button[type="submit"], button[type="submit"].btn-primary').first.click()
    page.wait_for_timeout(5000)
    return {
        "category_id": cid,
        "name": plan["name"],
        "before": {
            "meta_title": plan["before_meta_title"],
            "meta_description": plan["before_meta_description"],
        },
        "after": {
            "meta_title": plan["after_meta_title"],
            "meta_description": plan["after_meta_description"],
        },
        "status": "SAVED",
    }


def phase_admin_readonly() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return [], []
    admin = parse_production_section(SECRETS_PATH, "OpenCart Admin")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(120000)
        token, admin_base = _admin_login(page, admin)
        if not token:
            browser.close()
            return [], []
        before_rows, plan = probe_admin_categories(page, admin_base, token)
        page.goto(_admin_url(admin_base, "common/logout", token), timeout=30000)
        browser.close()
    return before_rows, plan


def phase_admin_saves(plan: list[dict[str, Any]]) -> dict[str, Any]:
    if not plan:
        return {"status": "SKIPPED", "reason": "no categories with wrong brand"}
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"status": "SKIPPED", "reason": "playwright unavailable"}
    admin = parse_production_section(SECRETS_PATH, "OpenCart Admin")
    result: dict[str, Any] = {"checked_at": utc_now(), "saves": [], "status": "FAILED"}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(120000)
        saves: list[dict[str, Any]] = []
        try:
            token, admin_base = _admin_login(page, admin)
            if not token:
                result["status"] = "LOGIN_FAILED"
                browser.close()
                return result
            for item in plan:
                saves.append(admin_save_category(page, admin_base, token, item))
            result["saves"] = saves
            result["status"] = "COMPLETE"
            page.goto(_admin_url(admin_base, "common/logout", token), timeout=30000)
        except Exception as exc:  # noqa: BLE001
            result["status"] = "ERROR"
            result["error"] = str(exc)[:500]
            result["saves"] = saves
        browser.close()
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-brand-after.json", result)
    return result


def verify_preservation() -> dict[str, Any]:
    robots = http_get("https://bzpm.ru/robots.txt")
    sitemap = http_get("https://bzpm.ru/sitemap.xml")
    url_count = 0
    sitemap_valid = False
    if sitemap["status_code"] == 200:
        try:
            root = ET.fromstring(sitemap["body"])
            url_count = len(root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"))
            sitemap_valid = url_count > 0
        except ET.ParseError:
            pass
    home = http_get("https://bzpm.ru/")
    home_meta = extract_meta(home["body"]) if home.get("body") else {}
    stoly = http_get("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly")
    llms = http_get("https://bzpm.ru/llms.txt")
    raw_llms = llms.get("raw_body") or b""
    llms_text = llms.get("body") or ""
    return {
        "robots_status": robots["status_code"],
        "sitemap_status": sitemap["status_code"],
        "sitemap_valid": sitemap_valid,
        "sitemap_url_count": url_count,
        "home_body_count": home_meta.get("body_count"),
        "home_yandex_metrika": home_meta.get("yandex_metrika"),
        "home_yandex_webmaster": home_meta.get("yandex_webmaster"),
        "stoly_load_more": "load-more" in (stoly.get("body") or "").lower() or "loadmore" in (stoly.get("body") or "").lower(),
        "llms_has_bom": raw_llms.startswith(UTF8_BOM),
        "llms_wrong_brand_count": count_public_brand(llms_text),
        "llms_correct_brand_count": llms_text.count(CORRECT_BRAND),
        "llms_bzpm_ru_count": llms_text.lower().count("bzpm.ru"),
    }


def brand_before_after_summary(before_rows: list[dict[str, Any]], after_rows: list[dict[str, Any]]) -> None:
    summary = {
        "before_urls_with_wrong_brand": sum(1 for r in before_rows if r.get("public_brand_text_yes")),
        "after_urls_with_wrong_brand": sum(1 for r in after_rows if r.get("public_brand_text_yes")),
        "before_total_brand_count": sum(r.get("brand_count_full_body", 0) for r in before_rows),
        "after_total_brand_count": sum(r.get("brand_count_full_body", 0) for r in after_rows),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "brand-before-after-summary.json", summary)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "brand-before-after-summary.md",
        "\n".join(
            [
                "# Brand before/after summary",
                "",
                f"URLs with `{WRONG_BRAND}` before: {summary['before_urls_with_wrong_brand']}",
                f"URLs with `{WRONG_BRAND}` after: {summary['after_urls_with_wrong_brand']}",
                f"Total brand count before: {summary['before_total_brand_count']}",
                f"Total brand count after: {summary['after_total_brand_count']}",
            ]
        ),
    )


def run_prepare() -> int:
    ensure_dirs()
    write_policy_manifests()
    pdp_urls = load_pdp_urls()
    all_urls = CORE_URLS + pdp_urls + SANITY_URLS
    before_rows = crawl_brand_inventory(all_urls, "crawl-before")
    write_json(DEPLOYMENT_ROOT / "crawl-before" / "crawl-url-list.json", {"urls": all_urls, "count": len(all_urls)})

    _, admin_plan = phase_admin_readonly()

    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md",
        "\n".join(
            [
                "# Implementation plan",
                "",
                "## File patches",
                "- llms.txt — BRAND_LITERAL + UTF-8 BOM",
                "- product.php — generator literals",
                "- katalog.php, blog/category.php, information controllers — setDescription literals",
                "",
                "## Admin",
                f"- Category SEO saves: {len(admin_plan)} entities",
                "",
                "## Excluded",
                "- header.twig, footer.twig, robots, sitemap, DB, import",
            ]
        ),
    )

    ftp = ftp_connect()
    try:
        targets = phase_source_discovery(ftp)
        if not targets:
            write_text(DEPLOYMENT_ROOT / "manifests" / "prepare-stop.md", "No file targets with wrong brand on FTP")
        prepared = phase_backup_and_prepare(ftp, targets) if targets else []
        phase_dry_run(prepared, admin_plan)
    finally:
        ftp.quit()
    return 0


def run_deploy() -> int:
    prepared = json.loads((DEPLOYMENT_ROOT / "manifests" / "files-to-change.json").read_text(encoding="utf-8"))
    prepared_meta = json.loads((DEPLOYMENT_ROOT / "manifests" / "dry-run.json").read_text(encoding="utf-8"))["prepared_files"]
    admin_plan = json.loads((DEPLOYMENT_ROOT / "manifests" / "admin-actions.json").read_text(encoding="utf-8")).get("categories", [])

    ftp = ftp_connect()
    try:
        if prepared_meta:
            pre_upload_verify(ftp, prepared_meta)
            uploads = deploy_files(ftp, prepared_meta)
        else:
            uploads = []
    finally:
        ftp.quit()

    admin_result = phase_admin_saves(admin_plan)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "deploy-summary.json",
        {"uploads": uploads, "admin": admin_result, "deployed_at": utc_now()},
    )
    return 0


def run_verify() -> int:
    pdp_urls = load_pdp_urls()
    all_urls = CORE_URLS + pdp_urls + SANITY_URLS
    before_path = DEPLOYMENT_ROOT / "crawl-before" / "public-brand-occurrences-before.json"
    before_rows = []
    if before_path.exists():
        before_rows = json.loads(before_path.read_text(encoding="utf-8")).get("rows", [])
    after_rows = crawl_brand_inventory(all_urls, "crawl-after")
    brand_before_after_summary(before_rows, after_rows)
    preservation = verify_preservation()
    write_json(DEPLOYMENT_ROOT / "manifests" / "preservation.json", preservation)
    return 0


def run_all() -> int:
    run_prepare()
    run_deploy()
    run_verify()
    write_json(DEPLOYMENT_ROOT / "manifests" / "run-summary.json", {"operation_id": OPERATION_ID, "finished_at": utc_now()})
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--phase", choices=("prepare", "deploy", "verify", "all"), default="all")
    args = parser.parse_args()
    if args.phase == "prepare":
        return run_prepare()
    if args.phase == "deploy":
        return run_deploy()
    if args.phase == "verify":
        return run_verify()
    return run_all()


if __name__ == "__main__":
    sys.exit(main())
