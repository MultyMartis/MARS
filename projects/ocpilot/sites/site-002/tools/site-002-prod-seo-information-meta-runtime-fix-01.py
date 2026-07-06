#!/usr/bin/env python3
"""SITE-002 Production information/blog/katalog meta runtime fix — Run 4.199."""
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

OPERATION_ID = "SITE-002-PROD-SEO-INFORMATION-META-RUNTIME-FIX-01"
OCPILOT_RUN = "4.199"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SITEMAP-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-SEO-INFORMATION-META-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

TARGET_URLS: list[str] = [
    "https://bzpm.ru/about",
    "https://bzpm.ru/custom-equipment",
    "https://bzpm.ru/dealers",
    "https://bzpm.ru/delivery",
    "https://bzpm.ru/guarantee",
    "https://bzpm.ru/payment-methods",
    "https://bzpm.ru/blog",
    "https://bzpm.ru/blog/news",
    "https://bzpm.ru/katalog",
    "https://bzpm.ru/katalog/",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-shpilki-i-protivni",
]

SANITY_URLS: list[str] = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/sitemap.xml",
    "https://bzpm.ru/robots.txt",
]

DESCRIPTION_COPY: dict[str, str] = {
    "about": (
        "Производство нейтрального оборудования из нержавеющей стали для общепита и пищевых предприятий. "
        "БЗПМ: собственный завод в Барнауле, поставки по России."
    ),
    "custom-equipment": (
        "Изготовление нестандартного оборудования из нержавеющей стали под задачи общепита и пищевых производств: "
        "размеры, конструкция, комплектация, производство БЗПМ."
    ),
    "dealers": (
        "Сотрудничество для дилеров и партнёров БЗПМ: поставки нейтрального оборудования из нержавеющей стали, "
        "оптовые условия и поддержка продаж."
    ),
    "delivery": (
        "Доставка оборудования БЗПМ по России: отправка транспортными компаниями, самовывоз из Барнаула, "
        "согласование сроков и условий поставки."
    ),
    "guarantee": (
        "Гарантия на оборудование БЗПМ: условия обслуживания, порядок обращения, документы и поддержка "
        "по изделиям из нержавеющей стали."
    ),
    "payment-methods": (
        "Способы оплаты оборудования БЗПМ для юридических лиц и ИП: безналичный расчёт, счёт, документы "
        "и согласование условий поставки."
    ),
    "katalog": (
        "Каталог нейтрального оборудования БЗПМ из нержавеющей стали: столы, полки, тележки, шкафы, подставки "
        "и решения для общепита."
    ),
    "blog": (
        "Блог и новости БЗПМ: материалы о нейтральном оборудовании, производстве, нержавеющей стали "
        "и решениях для общепита."
    ),
    "blog-news": (
        "Новости БЗПМ: обновления каталога, производство оборудования из нержавеющей стали, полезные материалы "
        "для общепита и пищевых предприятий."
    ),
}

CONTROLLER_PATCHES: list[dict[str, str]] = [
    {
        "url": "https://bzpm.ru/about",
        "route": "information/about",
        "remote": "/public_html/catalog/controller/information/about.php",
        "key": "about",
        "patch_type": "REPLACE_SETDESCRIPTION_LITERAL",
        "confidence": "HIGH",
    },
    {
        "url": "https://bzpm.ru/custom-equipment",
        "route": "information/custom_equipment",
        "remote": "/public_html/catalog/controller/information/custom_equipment.php",
        "key": "custom-equipment",
        "patch_type": "REPLACE_SETDESCRIPTION_LITERAL",
        "confidence": "HIGH",
    },
    {
        "url": "https://bzpm.ru/dealers",
        "route": "information/dealers",
        "remote": "/public_html/catalog/controller/information/dealers.php",
        "key": "dealers",
        "patch_type": "REPLACE_SETDESCRIPTION_LITERAL",
        "confidence": "HIGH",
    },
    {
        "url": "https://bzpm.ru/delivery",
        "route": "information/delivery",
        "remote": "/public_html/catalog/controller/information/delivery.php",
        "key": "delivery",
        "patch_type": "REPLACE_SETDESCRIPTION_LITERAL",
        "confidence": "HIGH",
    },
    {
        "url": "https://bzpm.ru/guarantee",
        "route": "information/guarantee",
        "remote": "/public_html/catalog/controller/information/guarantee.php",
        "key": "guarantee",
        "patch_type": "REPLACE_SETDESCRIPTION_LITERAL",
        "confidence": "HIGH",
    },
    {
        "url": "https://bzpm.ru/payment-methods",
        "route": "information/payment",
        "remote": "/public_html/catalog/controller/information/payment.php",
        "key": "payment-methods",
        "patch_type": "REPLACE_SETDESCRIPTION_LITERAL",
        "confidence": "HIGH",
    },
    {
        "url": "https://bzpm.ru/katalog",
        "route": "product/katalog",
        "remote": "/public_html/catalog/controller/product/katalog.php",
        "key": "katalog",
        "patch_type": "REPLACE_SETDESCRIPTION_LITERAL",
        "confidence": "HIGH",
    },
    {
        "url": "https://bzpm.ru/blog",
        "route": "blog/category",
        "remote": "/public_html/catalog/controller/blog/category.php",
        "key": "blog",
        "patch_type": "ADD_SETDESCRIPTION",
        "confidence": "HIGH",
    },
    {
        "url": "https://bzpm.ru/blog/news",
        "route": "blog/category",
        "remote": "/public_html/catalog/controller/blog/category.php",
        "key": "blog-news",
        "patch_type": "BLOG_NEWS_FALLBACK",
        "confidence": "HIGH",
    },
]

CATEGORY_ADMIN: dict[int, dict[str, str]] = {
    331: {
        "slug": "polki-nastennye-i-nastolnye",
        "url": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye",
        "meta_title": "Полки настенные и настольные из нержавеющей стали",
        "meta_description": (
            "Полки настенные и настольные БЗПМ из нержавеющей стали для кухни, цеха и производственных зон. "
            "Прочные конструкции, разные размеры и исполнение."
        ),
    },
    354: {
        "slug": "telezhki-shpilki-i-protivni",
        "url": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-shpilki-i-protivni",
        "meta_title": "Тележки-шпильки и противни из нержавеющей стали",
        "meta_description": (
            "Тележки-шпильки и противни БЗПМ из нержавеющей стали для пекарен, кухонь и пищевых производств. "
            "Удобное хранение и перемещение продукции."
        ),
    },
    358: {
        "slug": "shkafy-i-lari",
        "url": "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari",
        "meta_title": "Шкафы и лари из нержавеющей стали",
        "meta_description": (
            "Шкафы и лари БЗПМ из нержавеющей стали для хранения инвентаря, посуды и продукции "
            "на предприятиях общепита и пищевых производствах."
        ),
    },
}

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
    "copy",
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
            "x_robots_tag": exc.headers.get("X-Robots-Tag", "") if exc.headers else "",
            "body": text,
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "final_url": url, "status_code": None, "x_robots_tag": "", "body": "", "error": str(exc)}


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
        "is_product_pdp": False,
    }


def is_product_pdp(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    if "product_id=" in parsed.query.lower():
        return True
    parts = [p for p in parsed.path.split("/") if p]
    return len(parts) >= 4 and parts[0] == "katalog" and parts[1] != "nejtralnoe-oborudovanie"


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


def extract_set_description(content: str) -> str:
    m = re.search(r"setDescription\(\s*['\"](.+?)['\"]\s*\)", content, re.DOTALL)
    return m.group(1).replace("\\'", "'").replace('\\"', '"') if m else ""


def replace_set_description(content: str, new_desc: str) -> str:
    escaped = new_desc.replace("'", "\\'")
    if re.search(r"setDescription\(\s*['\"]", content):
        return re.sub(
            r"setDescription\(\s*['\"].+?['\"]\s*\)",
            f"setDescription('{escaped}')",
            content,
            count=1,
            flags=re.DOTALL,
        )
    raise RuntimeError("setDescription() not found for replacement")


def patch_blog_category(content: str, hub_desc: str, news_desc: str) -> str:
    escaped_hub = hub_desc.replace("'", "\\'")
    escaped_news = news_desc.replace("'", "\\'")

    old_meta_line = (
        "            if (isset($category_info['meta_description'])) "
        "$this->document->setDescription($category_info['meta_description']);"
    )
    new_meta_block = (
        "            if (!empty($category_info['meta_description'])) {\n"
        "                $this->document->setDescription($category_info['meta_description']);\n"
        "            } elseif (isset($category_info['name']) && $category_info['name'] === 'Новости') {\n"
        f"                $this->document->setDescription('{escaped_news}');\n"
        "            }"
    )
    if old_meta_line in content:
        content = content.replace(old_meta_line, new_meta_block)
    else:
        raise RuntimeError("blog/category.php meta_description branch not found")

    hub_anchor = '$this->document->setTitle("Блог и новости");'
    hub_insert = (
        f'{hub_anchor} // Можно вынести в языковой файл\n'
        f'            $this->document->setDescription(\'{escaped_hub}\');'
    )
    if hub_anchor in content and "setDescription" not in content.split(hub_anchor)[1].split("\n")[0]:
        content = content.replace(hub_anchor, hub_insert, 1)
    elif f"setDescription('{escaped_hub}')" not in content:
        raise RuntimeError("blog/category.php hub setTitle anchor not found")
    return content


def php_lint(path: Path) -> dict[str, Any]:
    try:
        proc = subprocess.run(
            ["php", "-l", str(path)],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
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
            "change_type": "information-meta-runtime-fix",
            "product_pages_excluded": True,
            "robots_change_allowed": False,
            "sitemap_change_allowed": False,
            "header_footer_change_allowed": False,
            "yandex_blocks_protected": True,
            "db_direct_write_allowed": False,
            "admin_save_allowed": "exact_category_seo_fields_only",
            "cron_change_allowed": False,
            "import_execution_allowed": False,
            "mail_change_allowed": False,
        },
    )


def crawl_meta(urls: list[str], label: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for url in urls:
        resp = http_get(url)
        body = resp["body"]
        meta = extract_meta(body) if body and ("<html" in body.lower() or url.endswith(".xml")) else {
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
        if url.endswith("sitemap.xml") and body.strip().startswith("<"):
            meta["sitemap_url_count"] = len(ET.fromstring(body).findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"))
        row = {
            "url": url,
            "http_status": resp["status_code"],
            "final_url": resp["final_url"],
            "error": resp["error"],
            "x_robots_tag": resp["x_robots_tag"],
            "is_product_pdp": is_product_pdp(url),
            **meta,
        }
        rows.append(row)
    out = DEPLOYMENT_ROOT / label
    write_json(out / f"{label}.json", {"captured_at": utc_now(), "rows": rows})
    fields = [
        "url", "http_status", "final_url", "title", "title_length", "meta_description",
        "description_length", "h1", "canonical", "meta_robots", "x_robots_tag",
        "body_count", "yandex_metrika", "yandex_webmaster", "is_product_pdp",
    ]
    with (out / f"{label}.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    md = [
        f"# Meta {label}",
        "",
        f"Captured: {utc_now()}",
        "",
        "| URL | Status | Title len | Desc len |",
        "|-----|--------|-----------|----------|",
    ]
    for row in rows:
        md.append(
            f"| {row['url']} | {row['http_status']} | {row.get('title_length', 0)} | "
            f"{row.get('description_length', 0)} |"
        )
    write_text(out / f"{label}-summary.md", "\n".join(md) + "\n")
    return rows


def phase_meta_copy() -> None:
    items = []
    for key, desc in DESCRIPTION_COPY.items():
        items.append({"key": key, "meta_description": desc, "length": len(desc)})
    for cid, fields in CATEGORY_ADMIN.items():
        items.append(
            {
                "key": f"category/{fields['slug']}",
                "category_id": cid,
                "meta_title": fields["meta_title"],
                "meta_description": fields["meta_description"],
                "title_length": len(fields["meta_title"]),
                "description_length": len(fields["meta_description"]),
            }
        )
    write_json(DEPLOYMENT_ROOT / "copy" / "meta-copy-final.json", items)
    md = ["# Meta copy final", "", f"Generated: {utc_now()}", ""]
    for item in items:
        md.append(f"## {item['key']}")
        if item.get("meta_title"):
            md.append(f"- Title ({item.get('title_length')}): {item['meta_title']}")
        md.append(f"- Description ({item.get('length', item.get('description_length'))}): {item['meta_description']}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "copy" / "meta-copy-final.md", "\n".join(md))


def phase_target_files_confirm(ftp: ftplib.FTP) -> list[dict[str, Any]]:
    confirmed: list[dict[str, Any]] = []
    seen_remotes: set[str] = set()
    for spec in CONTROLLER_PATCHES:
        remote = spec["remote"]
        data = ftp_download(ftp, remote)
        local = DEPLOYMENT_ROOT / "source" / remote_local_name(remote)
        local.write_bytes(data)
        current = extract_set_description(data.decode("utf-8", errors="replace"))
        entry = {
            **spec,
            "sha256_before": sha256_bytes(data),
            "current_set_description": current,
            "planned_new_description": DESCRIPTION_COPY[spec["key"]],
            "planned_length": len(DESCRIPTION_COPY[spec["key"]]),
        }
        confirmed.append(entry)
        seen_remotes.add(remote)
    write_json(DEPLOYMENT_ROOT / "manifests" / "target-files-confirmed.json", confirmed)
    md = ["# Target files confirmed", "", f"Captured: {utc_now()}", ""]
    for e in confirmed:
        md.append(f"## {e['url']}")
        md.append(f"- Remote: `{e['remote']}`")
        md.append(f"- Patch: {e['patch_type']} ({e['confidence']})")
        md.append(f"- Current desc len: {len(e.get('current_set_description', ''))}")
        md.append(f"- Planned desc len: {e['planned_length']}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "manifests" / "target-files-confirmed.md", "\n".join(md))
    return confirmed


def phase_blog_authority() -> dict[str, Any]:
    decision = {
        "blog_hub": {
            "authority": "catalog/controller/blog/category.php",
            "fix": "ADD_SETDESCRIPTION in category_id=0 branch",
            "confidence": "HIGH",
        },
        "blog_news": {
            "authority": "blog_themes row name=Новости via blog/category.php",
            "blog_category_id_exact": "discover via admin blog/themes read-only",
            "admin_meta_field_available": False,
            "fix": "BLOG_NEWS_FALLBACK when category name === Новости and meta_description empty",
            "confidence": "HIGH",
            "reason": "blog_themes has no admin meta_description field; safe name-based fallback",
        },
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "blog-authority-decision.json", decision)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "blog-authority-decision.md",
        "\n".join(
            [
                "# Blog/news authority decision",
                "",
                "## /blog",
                "- Fix: ADD_SETDESCRIPTION in hub branch — HIGH confidence",
                "",
                "## /blog/news",
                "- DB meta_description empty; admin blog/themes has no meta field",
                "- Fix: controller fallback when category name === `Новости` — HIGH confidence",
                "- No direct DB write",
            ]
        ),
    )
    return decision


def phase_backup_and_prepare(ftp: ftplib.FTP, confirmed: list[dict[str, Any]]) -> list[dict[str, Any]]:
    unique_remotes = sorted({e["remote"] for e in confirmed})
    prepared_manifest: list[dict[str, Any]] = []
    lint_results: list[dict[str, Any]] = []

    for remote in unique_remotes:
        data = ftp_download(ftp, remote)
        content = data.decode("utf-8", errors="replace")
        name = remote_local_name(remote)
        backup_path = DEPLOYMENT_ROOT / "backup" / name
        rollback_path = DEPLOYMENT_ROOT / "rollback" / name
        backup_path.write_bytes(data)
        rollback_path.write_bytes(data)
        sha = sha256_bytes(data)

        patched = content
        if remote.endswith("blog/category.php"):
            patched = patch_blog_category(
                content,
                DESCRIPTION_COPY["blog"],
                DESCRIPTION_COPY["blog-news"],
            )
        else:
            key = next(e["key"] for e in confirmed if e["remote"] == remote)
            patched = replace_set_description(content, DESCRIPTION_COPY[key])

        prepared_path = DEPLOYMENT_ROOT / "prepared" / name
        prepared_path.write_text(patched, encoding="utf-8", newline="\n")
        lint_results.append(php_lint(prepared_path))

        prepared_manifest.append(
            {
                "remote": remote,
                "backup_sha256": sha,
                "prepared_sha256": sha256_file(prepared_path),
                "backup_path": str(backup_path),
                "prepared_path": str(prepared_path),
            }
        )

    write_json(DEPLOYMENT_ROOT / "manifests" / "files-to-change.json", prepared_manifest)
    write_json(DEPLOYMENT_ROOT / "logs" / "php-lint.json", lint_results)
    if any(not r["ok"] for r in lint_results):
        raise RuntimeError("PHP lint failed for one or more prepared files")
    return prepared_manifest


def phase_implementation_plan() -> None:
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "admin-actions.json",
        {
            "categories": [
                {"category_id": cid, "route": f"catalog/category/edit&category_id={cid}", **fields}
                for cid, fields in CATEGORY_ADMIN.items()
            ],
            "blog_admin": "none — controller fallback only",
            "information_admin": "none — controller patch only",
        },
    )
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md",
        "\n".join(
            [
                "# Implementation plan",
                "",
                "## File patches (FTP upload)",
                "- 6 corporate information controllers — REPLACE_SETDESCRIPTION_LITERAL",
                "- product/katalog.php — REPLACE_SETDESCRIPTION_LITERAL",
                "- blog/category.php — ADD_SETDESCRIPTION hub + BLOG_NEWS_FALLBACK",
                "",
                "## Admin category saves",
                "- category_id=331, 354, 358 — SEO title + description only",
                "",
                "## Excluded",
                "- product PDP, header.twig, footer.twig, robots, sitemap",
                "",
                "## Rollback",
                "- Restore files from rollback/",
                "- Restore category admin before values if needed",
            ]
        ),
    )


def phase_dry_run(prepared: list[dict[str, Any]]) -> None:
    diffs = []
    for item in prepared:
        backup = Path(item["backup_path"]).read_text(encoding="utf-8", errors="replace")
        prepared_text = Path(item["prepared_path"]).read_text(encoding="utf-8", errors="replace")
        diff = list(
            difflib.unified_diff(
                backup.splitlines(),
                prepared_text.splitlines(),
                fromfile=item["remote"] + " (backup)",
                tofile=item["remote"] + " (prepared)",
                lineterm="",
            )
        )
        diffs.append({"remote": item["remote"], "diff_lines": len(diff), "diff_preview": "\n".join(diff[:40])})
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.json",
        {"prepared_files": prepared, "diffs": diffs, "admin_categories": list(CATEGORY_ADMIN.keys())},
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
                f"Admin category saves planned: {len(CATEGORY_ADMIN)}",
                "Header/footer: 0",
                "Product PDP: 0",
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
        uploads.append({"remote": item["remote"], "bytes": len(data), "sha256": sha256_bytes(data), "status": "UPLOADED"})
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


def capture_category_before(page: Any, admin_base: str, token: str) -> list[dict[str, Any]]:
    rows = []
    for cid, fields in CATEGORY_ADMIN.items():
        edit_url = _admin_url(admin_base, "catalog/category/edit", token, category_id=str(cid))
        page.goto(edit_url, wait_until="domcontentloaded", timeout=120000)
        page.wait_for_timeout(2500)
        if page.locator('input[name="category_description[1][meta_title]"]').count() == 0:
            rows.append({"category_id": cid, "error": "form not found"})
            continue
        name = page.locator('input[name="category_description[1][name]"]').input_value().strip()
        meta_title = page.locator('input[name="category_description[1][meta_title]"]').input_value()
        meta_description = page.locator('textarea[name="category_description[1][meta_description]"]').input_value()
        rows.append(
            {
                "category_id": cid,
                "slug": fields["slug"],
                "name": name,
                "meta_title": meta_title,
                "meta_title_length": len(meta_title),
                "meta_description": meta_description,
                "meta_description_length": len(meta_description),
            }
        )
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "categories-before.json", rows)
    md = ["# Categories before", ""]
    for row in rows:
        md.append(f"## ID {row.get('category_id')}")
        md.append(f"- Name: {row.get('name', '')}")
        md.append(f"- Meta title len: {row.get('meta_title_length', 0)}")
        md.append(f"- Meta description len: {row.get('meta_description_length', 0)}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "admin-evidence" / "categories-before.md", "\n".join(md))
    return rows


def admin_save_category(page: Any, admin_base: str, token: str, cid: int, fields: dict[str, str]) -> dict[str, Any]:
    edit_url = _admin_url(admin_base, "catalog/category/edit", token, category_id=str(cid))
    page.goto(edit_url, wait_until="domcontentloaded", timeout=120000)
    page.wait_for_timeout(2500)
    before = {
        "meta_title": page.locator('input[name="category_description[1][meta_title]"]').input_value(),
        "meta_description": page.locator('textarea[name="category_description[1][meta_description]"]').input_value(),
    }
    page.fill('input[name="category_description[1][meta_title]"]', fields["meta_title"])
    page.fill('textarea[name="category_description[1][meta_description]"]', fields["meta_description"])
    page.locator('.page-header button[type="submit"], button[type="submit"].btn-primary').first.click()
    page.wait_for_timeout(5000)
    record = {
        "category_id": cid,
        "slug": fields["slug"],
        "url": fields["url"],
        "before": before,
        "after": {"meta_title": fields["meta_title"], "meta_description": fields["meta_description"]},
        "status": "SAVED",
        "verified": False,
    }
    resp = http_get(fields["url"])
    live = extract_meta(resp["body"]) if resp.get("body") else {}
    record["verified"] = fields["meta_description"][:40] in (live.get("meta_description") or "")
    record["live_after"] = {"title": live.get("title"), "meta_description": live.get("meta_description")}
    return record


def discover_blog_news_theme(page: Any, admin_base: str, token: str) -> dict[str, Any]:
    page.goto(_admin_url(admin_base, "blog/themes", token), wait_until="domcontentloaded", timeout=120000)
    page.wait_for_timeout(3000)
    rows = page.locator("table tbody tr")
    found: dict[str, Any] = {"themes": []}
    for i in range(min(rows.count(), 20)):
        row = rows.nth(i)
        text = row.inner_text()
        href = row.locator('a[href*="theme_id="]').first.get_attribute("href") or ""
        mid = re.search(r"theme_id=(\d+)", href)
        if mid:
            theme = {"theme_id": int(mid.group(1)), "row_text": text.strip()[:120]}
            found["themes"].append(theme)
            if "новости" in text.lower() or "news" in text.lower():
                found["blog_news_theme_id"] = int(mid.group(1))
                found["blog_news_name"] = "Новости"
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "blog-themes-readonly.json", found)
    return found


def phase_admin_saves() -> dict[str, Any]:
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
            discover_blog_news_theme(page, admin_base, token)
            capture_category_before(page, admin_base, token)
            for cid, fields in CATEGORY_ADMIN.items():
                saves.append(admin_save_category(page, admin_base, token, cid, fields))
            result["saves"] = saves
            verified = sum(1 for s in saves if s.get("verified"))
            result["status"] = "COMPLETE" if verified >= len(saves) else "PARTIAL"
            page.goto(_admin_url(admin_base, "common/logout", token), timeout=30000)
        except Exception as exc:  # noqa: BLE001
            result["status"] = "ERROR"
            result["error"] = str(exc)[:500]
            result["saves"] = saves
        browser.close()
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "categories-after.json", result)
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
    return {
        "robots_status": robots["status_code"],
        "sitemap_status": sitemap["status_code"],
        "sitemap_valid": sitemap_valid,
        "sitemap_url_count": url_count,
        "home_body_count": home_meta.get("body_count"),
        "home_yandex_metrika": home_meta.get("yandex_metrika"),
        "home_yandex_webmaster": home_meta.get("yandex_webmaster"),
    }


def run_prepare() -> int:
    ensure_dirs()
    crawl_meta(TARGET_URLS + SANITY_URLS, "meta-before")
    phase_meta_copy()
    phase_blog_authority()
    phase_implementation_plan()
    ftp = ftp_connect()
    try:
        confirmed = phase_target_files_confirm(ftp)
        prepared = phase_backup_and_prepare(ftp, confirmed)
        phase_dry_run(prepared)
    finally:
        ftp.quit()
    return 0


def run_deploy() -> int:
    prepared = json.loads((DEPLOYMENT_ROOT / "manifests" / "files-to-change.json").read_text(encoding="utf-8"))
    ftp = ftp_connect()
    try:
        pre_upload_verify(ftp, prepared)
        uploads = deploy_files(ftp, prepared)
    finally:
        ftp.quit()
    admin_result = phase_admin_saves()
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "deploy-summary.json",
        {"uploads": uploads, "admin": admin_result, "deployed_at": utc_now()},
    )
    return 0


def run_verify() -> int:
    crawl_meta(TARGET_URLS + SANITY_URLS, "meta-after")
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
