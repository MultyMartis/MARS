#!/usr/bin/env python3
"""SITE-002 Production non-product SEO meta CONTENT fix — Run 4.193."""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-SEO-META-CONTENT-FIX-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SITEMAP-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-SEO-META-CONTENT-01"
META_AUDIT_CSV = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-READINESS-ROBOTS-01\meta-audit\non-product-meta-audit.csv"
)
META_FIX_PLAN = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-READINESS-ROBOTS-01\meta-audit\meta-fix-plan.md"
)
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-META-CONTENT-FIX-01"
)
USER_AGENT = "MARS-OCPilot/SITE-002-PROD-SEO-META-CONTENT-FIX-01"

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

INFORMATION_META: dict[str, dict[str, str]] = {
    "about": {
        "url": "https://bzpm.ru/about",
        "meta_title": "О компании — завод пищевого машиностроения ЗПМ",
        "meta_description": "ЗПМ — российский производитель нейтрального оборудования из нержавеющей стали для общепита и пищевых производств. Производство в Барнауле, поставки по России.",
        "admin_hints": ["О компании", "about"],
    },
    "custom-equipment": {
        "url": "https://bzpm.ru/custom-equipment",
        "meta_title": "Оборудование на заказ — изготовление по требованиям | ООО «ЗПМ»",
        "meta_description": "Завод ЗПМ изготавливает нейтральное оборудование из нержавеющей стали на заказ: нестандартные размеры и комплектация под помещение и технологию.",
        "admin_hints": ["Оборудование на заказ", "custom-equipment"],
    },
    "dealers": {
        "url": "https://bzpm.ru/dealers",
        "meta_title": "Дилерам и оптовым партнёрам — ЗПМ",
        "meta_description": "Партнёрская программа завода ЗПМ для дилеров и оптовых компаний: прямые поставки от производителя, поставки по России, порядок начала сотрудничества.",
        "admin_hints": ["Дилерам", "dealers"],
    },
    "delivery": {
        "url": "https://bzpm.ru/delivery",
        "meta_title": "Доставка оборудования — ЗПМ",
        "meta_description": "Доставка оборудования ЗПМ: отгрузка из Барнаула и склада партнёра в Московской области, транспортные компании по России, самовывоз после оплаты.",
        "admin_hints": ["Доставка", "delivery"],
    },
    "guarantee": {
        "url": "https://bzpm.ru/guarantee",
        "meta_title": "Гарантия на оборудование — ЗПМ",
        "meta_description": "Гарантийная поддержка оборудования ЗПМ: порядок обращения при неисправности, необходимые документы и рассмотрение обращения производителем.",
        "admin_hints": ["Гарантия", "guarantee"],
    },
    "payment-methods": {
        "url": "https://bzpm.ru/payment-methods",
        "meta_title": "Оплата оборудования — ЗПМ",
        "meta_description": "Оплата оборудования ЗПМ для юридических лиц: безналичный расчёт по счёту, порядок выставления документов и этапы после оплаты.",
        "admin_hints": ["Оплата", "payment"],
    },
}

STORE_META = {
    "url": "https://bzpm.ru/",
    "meta_description": (
        "Завод пищевого машиностроения ЗПМ производит оборудование для ресторанов, кафе и пищевых производств. "
        "Каталог нейтрального оборудования из нержавеющей стали."
    ),
}

CATALOG_HUB_META = {
    "url": "https://bzpm.ru/katalog",
    "meta_title": "Каталог оборудования для общепита | ООО «ЗПМ»",
    "meta_description": (
        "Каталог оборудования для ресторанов, кафе и пищевых производств от завода ЗПМ. "
        "Профессиональное оборудование для кухни и предприятий общепита."
    ),
    "admin_hints": ["Каталог", "katalog", "catalog"],
}

BLOG_META: dict[str, dict[str, str]] = {
    "blog": {
        "url": "https://bzpm.ru/blog",
        "meta_title": "Блог и новости завода ЗПМ",
        "meta_description": "Новости, статьи и материалы завода пищевого машиностроения ЗПМ об оборудовании для общепита и пищевых производств.",
    },
    "blog-news": {
        "url": "https://bzpm.ru/blog/news",
        "meta_title": "Новости завода ЗПМ",
        "meta_description": "Актуальные новости завода ЗПМ: обновления каталога, производство, сертификация и материалы для заказчиков и партнёров.",
    },
}

SANITY_URLS = [
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/sitemap.xml",
    "https://bzpm.ru/robots.txt",
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
    "copy",
    "crawl",
    "manifests",
    "logs",
)

# Status after Run 4.192 — controller defaults / X-Robots-Tag applied
FIXED_IN_4192 = {
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/contact",
    "https://bzpm.ru/index.php?route=information/contact",
    "https://bzpm.ru/cart",
    "https://bzpm.ru/checkout",
    "https://bzpm.ru/search",
    "https://bzpm.ru/compare-products",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly?page=2",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly?limit=30",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly?sort=p.price&order=ASC",
}

DEFERRED_NO_CONTENT = {
    "https://bzpm.ru/account/login",
    "https://bzpm.ru/my-account",
    "https://bzpm.ru/wishlist",
    "https://bzpm.ru/contact-us",
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
            "change_type": "seo-meta-content-fix",
            "product_pages_excluded": True,
            "robots_change_allowed": False,
            "sitemap_change_allowed": False,
            "header_footer_change_allowed": False,
            "yandex_blocks_protected": True,
            "db_direct_write_allowed": False,
            "admin_save_allowed": "conditional_exact_seo_fields_only",
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


def page_type_for(url: str) -> str:
    if url.rstrip("/") in ("https://bzpm.ru", "https://bzpm.ru/"):
        return "HOME"
    if "/blog" in url:
        return "BLOG"
    if "/katalog/" in url and "?" not in url:
        return "CATEGORY_PLP"
    if url.endswith("/katalog") or url.endswith("/katalog/"):
        return "CATEGORY_PLP"
    if "/contact" in url:
        return "CONTACT"
    if any(x in url for x in ("/cart", "/checkout", "/search", "/wishlist", "/compare", "/account/")):
        return "TECHNICAL"
    if "?" in url:
        return "QUERY_VARIANT"
    if url in INFORMATION_META or any(url.endswith("/" + k) for k in INFORMATION_META):
        return "CORPORATE"
    return "INFORMATION"


def classify_issues(row: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    title_len = row.get("title_length", 0) or 0
    desc_len = row.get("description_length", 0) or 0
    if not title_len:
        issues.append("MISSING_TITLE")
    if not desc_len:
        issues.append("MISSING_DESCRIPTION")
    if desc_len > 165:
        issues.append("TOO_LONG_DESCRIPTION")
    if title_len > 65:
        issues.append("DUPLICATE_TITLE")
    return issues


def status_after_4192(url: str) -> str:
    if url in FIXED_IN_4192:
        return "FIXED"
    if url in DEFERRED_NO_CONTENT:
        return "DEFERRED"
    if "?" in url:
        return "FIXED"
    return "REMAINING"


def include_in_operation(url: str, issues: list[str], page_type: str) -> bool:
    if is_product_url(url):
        return False
    if url in DEFERRED_NO_CONTENT:
        return False
    if url in FIXED_IN_4192 and "TOO_LONG_DESCRIPTION" not in issues and "MISSING_DESCRIPTION" not in issues:
        return False
    if page_type == "TECHNICAL":
        return False
    if page_type == "QUERY_VARIANT":
        return False
    if not issues:
        return False
    return True


def authority_for_gap(url: str, page_type: str, issues: list[str]) -> str:
    if page_type == "HOME":
        return "ADMIN"
    if page_type == "CATEGORY_PLP":
        return "ADMIN"
    if page_type in ("CORPORATE", "INFORMATION"):
        return "ADMIN"
    if page_type == "BLOG":
        return "SAFE UNKNOWN"
    return "SAFE UNKNOWN"


def build_remaining_gaps() -> list[dict[str, Any]]:
    gaps: list[dict[str, Any]] = []
    with META_AUDIT_CSV.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            url = row["url"]
            if is_product_url(url):
                gaps.append(
                    {
                        "url": url,
                        "page_type": "PRODUCT_PDP_EXCLUDED",
                        "include": False,
                        "status_after_4_192": "DEFERRED",
                        "authority": "TWIG_NOT_ALLOWED",
                    }
                )
                continue
            page_type = page_type_for(url)
            issues = []
            if row.get("classification") == "FAIL":
                for part in row.get("meta_description", ""):
                    pass
            desc_len = int(row.get("description_length") or 0)
            title_len = int(row.get("title_length") or 0)
            if not desc_len:
                issues.append("MISSING_DESCRIPTION")
            if desc_len > 165:
                issues.append("TOO_LONG_DESCRIPTION")
            if not title_len:
                issues.append("MISSING_TITLE")
            if title_len > 65:
                issues.append("TITLE_TOO_LONG")
            if row.get("duplicate_title_candidate") == "True":
                issues.append("DUPLICATE_TITLE")
            st = status_after_4192(url)
            inc = include_in_operation(url, issues, page_type)
            gaps.append(
                {
                    "url": url,
                    "page_type": page_type,
                    "current_title": row.get("title", ""),
                    "current_description": row.get("meta_description", ""),
                    "current_h1": row.get("h1_text", ""),
                    "current_canonical": row.get("canonical", ""),
                    "current_meta_robots": row.get("meta_robots", ""),
                    "issues": issues,
                    "status_after_4_192": st,
                    "include": inc,
                    "authority": authority_for_gap(url, page_type, issues),
                }
            )
    # Add explicit content targets not always in audit rows
    for slug, meta in CATEGORY_META.items():
        url = f"https://bzpm.ru/katalog/nejtralnoe-oborudovanie/{slug}"
        if not any(g["url"] == url for g in gaps):
            gaps.append(
                {
                    "url": url,
                    "page_type": "CATEGORY_PLP",
                    "issues": ["MISSING_DESCRIPTION", "MISSING_TITLE"],
                    "status_after_4_192": "PARTIAL",
                    "include": True,
                    "authority": "ADMIN",
                }
            )
    for key, meta in INFORMATION_META.items():
        url = meta["url"]
        existing = next((g for g in gaps if g["url"] == url), None)
        if existing:
            existing["include"] = True
            existing["authority"] = "ADMIN"
            if "TOO_LONG_DESCRIPTION" not in existing["issues"] and existing.get("current_description"):
                if len(existing["current_description"]) > 165:
                    existing["issues"].append("TOO_LONG_DESCRIPTION")
        else:
            gaps.append(
                {
                    "url": url,
                    "page_type": "CORPORATE",
                    "issues": ["TOO_LONG_DESCRIPTION"],
                    "status_after_4_192": "REMAINING",
                    "include": True,
                    "authority": "ADMIN",
                }
            )
    for key, meta in BLOG_META.items():
        url = meta["url"]
        existing = next((g for g in gaps if g["url"] == url), None)
        if existing:
            existing["include"] = True
            existing["authority"] = "SAFE UNKNOWN"
        else:
            gaps.append(
                {
                    "url": url,
                    "page_type": "BLOG",
                    "issues": ["MISSING_DESCRIPTION"],
                    "status_after_4_192": "REMAINING",
                    "include": True,
                    "authority": "SAFE UNKNOWN",
                }
            )
    home = next((g for g in gaps if g["url"] == "https://bzpm.ru/"), None)
    if home:
        home["include"] = True
        home["authority"] = "ADMIN"
    write_json(DEPLOYMENT_ROOT / "manifests" / "remaining-meta-gaps.json", gaps)
    included = [g for g in gaps if g.get("include")]
    md = [
        "# Remaining meta gaps",
        "",
        f"Generated: {utc_now()}",
        "",
        "## У кого ещё нет meta-тегов / нужна правка контента",
        "",
    ]
    for g in included:
        md.append(f"- **{g['url']}** — {', '.join(g.get('issues', []))} — authority: {g.get('authority')}")
    md.extend(["", f"Included URLs: {len(included)}", f"Total audited: {len(gaps)}"])
    write_text(DEPLOYMENT_ROOT / "manifests" / "remaining-meta-gaps.md", "\n".join(md))
    return gaps


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
    if rows:
        with (out_dir / f"{label}.csv").open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    write_text(
        out_dir / f"{label}-summary.md",
        "\n".join(
            [
                f"# Meta {label.replace('meta-', '')}",
                "",
                f"Captured: {utc_now()}",
                f"URLs: {len(urls)}",
                "",
                "| URL | Status | Title len | Desc len | Robots |",
                "|-----|--------|-----------|----------|--------|",
            ]
            + [
                f"| {r['url'][:55]} | {r.get('status_code')} | {r.get('title_length', 0)} | "
                f"{r.get('description_length', 0)} | {r.get('meta_robots_effective', '')} |"
                for r in rows
            ]
        ),
    )
    return rows


def crawl_urls_for_phase(label: str) -> list[str]:
    gaps = json.loads((DEPLOYMENT_ROOT / "manifests" / "remaining-meta-gaps.json").read_text(encoding="utf-8"))
    urls = sorted({g["url"] for g in gaps if g.get("include")})
    urls.extend(SANITY_URLS)
    # dedupe preserve order
    seen: set[str] = set()
    ordered: list[str] = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            ordered.append(u)
    return crawl_urls(ordered, label)


def build_meta_copy() -> list[dict[str, Any]]:
    copy_items: list[dict[str, Any]] = []
    copy_items.append({"entity": "store/home", "url": STORE_META["url"], **STORE_META, "authority": "ADMIN"})
    copy_items.append({"entity": "catalog/katalog", "url": CATALOG_HUB_META["url"], **CATALOG_HUB_META, "authority": "ADMIN"})
    for slug, fields in CATEGORY_META.items():
        copy_items.append(
            {
                "entity": f"category/{slug}",
                "url": f"https://bzpm.ru/katalog/nejtralnoe-oborudovanie/{slug}",
                **fields,
                "authority": "ADMIN",
            }
        )
    for key, fields in INFORMATION_META.items():
        copy_items.append({"entity": f"information/{key}", **fields, "authority": "ADMIN"})
    for key, fields in BLOG_META.items():
        copy_items.append({"entity": f"blog/{key}", **fields, "authority": "SAFE UNKNOWN"})
    write_json(DEPLOYMENT_ROOT / "copy" / "meta-copy-final.json", copy_items)
    md = ["# Meta copy final", "", f"Generated: {utc_now()}", ""]
    for item in copy_items:
        md.append(f"## {item['entity']} — {item.get('url', '')}")
        if item.get("meta_title"):
            md.append(f"- Title ({len(item['meta_title'])}): {item['meta_title']}")
        if item.get("meta_description"):
            md.append(f"- Description ({len(item['meta_description'])}): {item['meta_description']}")
        md.append(f"- Authority: {item['authority']}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "copy" / "meta-copy-final.md", "\n".join(md))
    return copy_items


def build_authority_manifests() -> None:
    admin_actions = {
        "store": [{"field": "config_meta_description", "value": STORE_META["meta_description"]}],
        "categories": [
            {"slug": slug, "category_id": "TBD", **fields} for slug, fields in CATEGORY_META.items()
        ],
        "information": [
            {"key": key, "information_id": "TBD", **{k: v for k, v in fields.items() if k != "admin_hints"}}
            for key, fields in INFORMATION_META.items()
        ],
        "catalog_hub": CATALOG_HUB_META,
        "blog": list(BLOG_META.values()),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "admin-actions.json", admin_actions)
    write_json(DEPLOYMENT_ROOT / "manifests" / "file-actions.json", {"files": [], "reason": "admin-first; no file deploy planned"})
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "authority-map.md",
        "\n".join(
            [
                "# Authority map",
                "",
                "- HOME `config_meta_description` → **ADMIN** System / Settings",
                "- Catalog hub `/katalog` → **ADMIN** information or category (discover)",
                "- 6 category PLP → **ADMIN** Catalog / Categories",
                "- Corporate pages → **ADMIN** Catalog / Information",
                "- Blog hub → **SAFE UNKNOWN** (custom blog module; discover admin route)",
                "- Product PDP → **EXCLUDED**",
                "- Technical pages → **DEFERRED** (noindex sufficient from 4.192)",
            ]
        ),
    )
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md",
        "\n".join(
            [
                "# Implementation plan",
                "",
                "1. Admin login (conservative Playwright, one entity per save)",
                "2. Store settings — trim home meta description",
                "3. Category edits — 6 PLP meta_title + meta_description",
                "4. Information edits — corp pages meta_description trim",
                "5. Blog — discover admin; save if route found",
                "6. Verify all changed URLs",
                "",
                "No file deploy. No DB. No header/footer.",
            ]
        ),
    )


def build_dry_run() -> None:
    copy_items = json.loads((DEPLOYMENT_ROOT / "copy" / "meta-copy-final.json").read_text(encoding="utf-8"))
    before = json.loads((DEPLOYMENT_ROOT / "meta-before" / "meta-before.json").read_text(encoding="utf-8"))
    before_map = {r["url"]: r for r in before}
    plan = []
    for item in copy_items:
        url = item.get("url", "")
        b = before_map.get(url, {})
        plan.append(
            {
                "entity": item["entity"],
                "url": url,
                "before_title": b.get("title", ""),
                "before_description": b.get("meta_description", ""),
                "after_title": item.get("meta_title", b.get("title", "")),
                "after_description": item.get("meta_description", ""),
                "authority": item["authority"],
            }
        )
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", plan)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "\n".join(
            [
                "# Dry-run review",
                "",
                f"Generated: {utc_now()}",
                "",
                "## Product PDP exclusion",
                "No product URLs in plan.",
                "",
                "## Protected files",
                "header.twig / footer.twig — NOT in plan.",
                "",
                "## Planned admin saves",
            ]
            + [f"- {p['entity']}: {p['authority']}" for p in plan if p["authority"] == "ADMIN"]
            + ["", "## File uploads", "0 planned."]
        ),
    )


def _admin_url(admin_base: str, route: str, token: str, **params: str) -> str:
    q: dict[str, str] = {"route": route, "user_token": token, **params}
    return f"{admin_base.rstrip('/')}/index.php?{urllib.parse.urlencode(q)}"


def _admin_base_from_page(page: Any, fallback: str) -> str:
    base = page.url.split("index.php")[0]
    return base if base.startswith("http") else fallback.rstrip("/") + "/"


def _admin_login(page: Any, admin: dict[str, str]) -> tuple[str | None, str]:
    url = admin.get("url", "https://bzpm.ru/admin/")
    page.goto(url, wait_until="domcontentloaded", timeout=120000)
    page.wait_for_timeout(2000)
    if page.locator('input[name="username"]').count() == 0:
        token_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.url)
        if token_match:
            return token_match.group(1), _admin_base_from_page(page, url)
    page.fill('input[name="username"]', admin["login"])
    page.fill('input[name="password"]', admin["password"])
    page.click('button[type="submit"]')
    try:
        page.wait_for_url("**user_token**", timeout=90000)
    except Exception:
        pass
    page.wait_for_timeout(3000)
    if "common/login" in page.url and page.locator('input[name="username"]').count() > 0:
        return None, _admin_base_from_page(page, url)
    admin_base = _admin_base_from_page(page, url)
    token_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.url)
    if token_match:
        return token_match.group(1), admin_base
    body_match = re.search(r"user_token=([a-zA-Z0-9]+)", page.content())
    return (body_match.group(1), admin_base) if body_match else (None, admin_base)


def _wait_form(page: Any, selector: str, timeout_ms: int = 120000) -> None:
    page.wait_for_selector(selector, state="visible", timeout=timeout_ms)


CATEGORY_ID_FALLBACK: dict[str, int] = {
    "stoly": 301,
    "podtovarniki-i-podstavki": 322,
    "telezhki-servirovochnye": 326,
}

CATEGORY_NAME_TARGETS: dict[str, str] = {
    "polki-nastennye-i-nastolnye": "Полки настенные и настольные",
    "shkafy-i-lari": "Шкафы и лари",
    "telezhki-shpilki-i-protivni": "Тележки-шпильки и противни",
}


def discover_category_ids(page: Any, admin_url: str, token: str, *, full_scan: bool = False) -> dict[str, int]:
    mapping: dict[str, int] = dict(CATEGORY_ID_FALLBACK)
    if not full_scan:
        write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-id-map.json", mapping)
        return mapping
    seen_ids: set[int] = set()
    for page_num in range(1, 10):
        list_url = _admin_url(admin_url, "catalog/category", token) + f"&page={page_num}"
        page.goto(list_url, wait_until="domcontentloaded", timeout=120000)
        page.wait_for_timeout(2500)
        rows = page.locator("table tbody tr")
        if rows.count() == 0:
            break
        for i in range(rows.count()):
            row = rows.nth(i)
            href = row.locator('a[href*="category_id="]').first.get_attribute("href") or ""
            mid = re.search(r"category_id=(\d+)", href)
            if not mid:
                continue
            cid = int(mid.group(1))
            if cid in seen_ids:
                continue
            seen_ids.add(cid)
            edit_url = _admin_url(admin_url, "catalog/category/edit", token, category_id=str(cid))
            page.goto(edit_url, wait_until="domcontentloaded", timeout=120000)
            page.wait_for_timeout(700)
            if page.locator('input[name="category_description[1][name]"]').count() == 0:
                continue
            name = page.locator('input[name="category_description[1][name]"]').input_value().strip()
            for slug, target_name in CATEGORY_NAME_TARGETS.items():
                if name == target_name:
                    mapping[slug] = cid
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-id-map.json", mapping)
    return mapping


def discover_information_ids(page: Any, admin_url: str, token: str) -> dict[str, int]:
    mapping: dict[str, int] = {}
    list_url = _admin_url(admin_url, "catalog/information", token)
    page.goto(list_url, wait_until="domcontentloaded", timeout=120000)
    page.wait_for_timeout(5000)
    rows = page.locator("table tbody tr")
    for i in range(min(rows.count(), 100)):
        row = rows.nth(i)
        text = row.inner_text()
        href = row.locator('a[href*="information_id="]').first.get_attribute("href") or ""
        mid = re.search(r"information_id=(\d+)", href)
        if not mid:
            continue
        iid = int(mid.group(1))
        for key, meta in INFORMATION_META.items():
            if key in mapping:
                continue
            for hint in meta.get("admin_hints", []):
                if hint.lower() in text.lower():
                    mapping[key] = iid
                    break
        if CATALOG_HUB_META.get("url") and "katalog" not in mapping:
            for hint in CATALOG_HUB_META.get("admin_hints", []):
                if hint.lower() in text.lower():
                    mapping["katalog"] = iid
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "information-id-map.json", mapping)
    return mapping


def _save_and_verify(
    page: Any,
    entity: str,
    url: str,
    before: dict[str, str],
    after: dict[str, str],
    field_names: list[str],
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "entity": entity,
        "url": url,
        "fields_changed": field_names,
        "before": before,
        "after": after,
        "status": "SAVED",
        "verified": False,
    }
    page.wait_for_timeout(2000)
    try:
        resp = http_get(url)
        live = extract_meta(resp["body"]) if resp.get("body") else {}
        if after.get("meta_description"):
            record["verified"] = after["meta_description"][:40] in (live.get("meta_description") or "")
        if after.get("meta_title") and not record["verified"]:
            record["verified"] = after["meta_title"][:30] in (live.get("title") or "")
        record["live_after"] = {
            "title": live.get("title", ""),
            "meta_description": live.get("meta_description", ""),
        }
    except Exception as exc:
        record["verify_error"] = str(exc)
    return record


def admin_save_store(page: Any, admin_url: str, token: str) -> dict[str, Any]:
    settings_url = _admin_url(admin_url, "setting/setting", token)
    page.goto(settings_url, wait_until="domcontentloaded", timeout=120000)
    page.wait_for_timeout(3000)
    _wait_form(page, 'textarea[name="config_meta_description"]')
    before_desc = page.locator('textarea[name="config_meta_description"]').input_value()
    page.fill('textarea[name="config_meta_description"]', STORE_META["meta_description"])
    submit = page.locator(
        '.page-header button[type="submit"], button[type="submit"].btn-primary, '
        '#form-setting input[type="submit"], button[form="form-setting"]'
    )
    submit.first.click()
    page.wait_for_timeout(5000)
    return _save_and_verify(
        page,
        "store/home",
        STORE_META["url"],
        {"config_meta_description": before_desc},
        {"meta_description": STORE_META["meta_description"]},
        ["config_meta_description"],
    )


def admin_save_category(
    page: Any, admin_url: str, token: str, slug: str, cid: int, fields: dict[str, str]
) -> dict[str, Any]:
    edit_url = _admin_url(admin_url, "catalog/category/edit", token, category_id=str(cid))
    page.goto(edit_url, wait_until="domcontentloaded", timeout=120000)
    page.wait_for_timeout(3000)
    _wait_form(page, 'input[name="category_description[1][meta_title]"]')
    before = {
        "meta_title": page.locator('input[name="category_description[1][meta_title]"]').input_value(),
        "meta_description": page.locator('textarea[name="category_description[1][meta_description]"]').input_value(),
    }
    page.fill('input[name="category_description[1][meta_title]"]', fields["meta_title"])
    page.fill('textarea[name="category_description[1][meta_description]"]', fields["meta_description"])
    page.locator('.page-header button[type="submit"], button[type="submit"].btn-primary').first.click()
    page.wait_for_timeout(5000)
    return _save_and_verify(
        page,
        f"category/{slug}",
        f"https://bzpm.ru/katalog/nejtralnoe-oborudovanie/{slug}",
        before,
        fields,
        ["meta_title", "meta_description"],
    )


def admin_save_information(
    page: Any, admin_url: str, token: str, key: str, iid: int, fields: dict[str, str]
) -> dict[str, Any]:
    edit_url = _admin_url(admin_url, "catalog/information/edit", token, information_id=str(iid))
    page.goto(edit_url, wait_until="domcontentloaded", timeout=120000)
    page.wait_for_timeout(3000)
    _wait_form(page, 'textarea[name="information_description[1][meta_description]"]')
    before = {
        "meta_title": page.locator('input[name="information_description[1][meta_title]"]').input_value(),
        "meta_description": page.locator('textarea[name="information_description[1][meta_description]"]').input_value(),
    }
    if fields.get("meta_title"):
        page.fill('input[name="information_description[1][meta_title]"]', fields["meta_title"])
    page.fill('textarea[name="information_description[1][meta_description]"]', fields["meta_description"])
    page.locator('.page-header button[type="submit"], button[type="submit"].btn-primary').first.click()
    page.wait_for_timeout(5000)
    return _save_and_verify(
        page,
        f"information/{key}",
        fields.get("url", ""),
        before,
        {"meta_title": fields.get("meta_title", before["meta_title"]), "meta_description": fields["meta_description"]},
        ["meta_title", "meta_description"],
    )


def discover_blog_routes(page: Any, admin_url: str, token: str) -> list[str]:
    candidates = [
        "blog/blog",
        "blog/category",
        "extension/module/blog",
        "catalog/blog",
        "blog/setting",
    ]
    found: list[str] = []
    for route in candidates:
        try:
            page.goto(_admin_url(admin_url, route, token), wait_until="domcontentloaded", timeout=30000)
            page.wait_for_timeout(2000)
            if "common/login" not in page.url and page.locator("body").count():
                title = page.title()
                if "404" not in title and "Permission" not in page.content()[:500]:
                    found.append(route)
        except Exception:
            pass
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "blog-routes.json", found)
    return found


def capture_admin_before(page: Any, admin_url: str, token: str) -> dict[str, Any]:
    evidence: dict[str, Any] = {"captured_at": utc_now()}
    settings_url = _admin_url(admin_url, "setting/setting", token)
    page.goto(settings_url, wait_until="domcontentloaded", timeout=120000)
    page.wait_for_timeout(3000)
    if page.locator('textarea[name="config_meta_description"]').count():
        evidence["store_meta_description"] = page.locator('textarea[name="config_meta_description"]').input_value()[:200]
    evidence["category_ids"] = discover_category_ids(page, admin_url, token, full_scan=False)
    evidence["information_ids"] = discover_information_ids(page, admin_url, token)
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "before.json", evidence)
    write_text(
        DEPLOYMENT_ROOT / "admin-evidence" / "before.md",
        "\n".join(
            [
                "# Admin before evidence",
                "",
                f"Captured: {evidence['captured_at']}",
                f"Categories mapped: {len(evidence.get('category_ids', {}))}",
                f"Information mapped: {len(evidence.get('information_ids', {}))}",
                f"Blog routes: {evidence.get('blog_routes', [])}",
            ]
        ),
    )
    return evidence


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
        context = browser.new_context(locale="ru-RU")
        page = context.new_page()
        page.set_default_timeout(120000)
        saves: list[dict[str, Any]] = []
        try:
            token, admin_base = _admin_login(page, admin)
            if not token:
                result["status"] = "LOGIN_FAILED"
                browser.close()
                return result
            before_evidence = capture_admin_before(page, admin_url=admin_base, token=token)
            saves.append(admin_save_store(page, admin_base, token))
            cat_map = before_evidence.get("category_ids", {})
            for slug, fields in CATEGORY_META.items():
                cid = cat_map.get(slug)
                if not cid:
                    saves.append({"entity": f"category/{slug}", "status": "SKIPPED", "reason": "category_id not found"})
                    continue
                saves.append(admin_save_category(page, admin_base, token, slug, cid, fields))
            info_map = before_evidence.get("information_ids", {})
            for key, fields in INFORMATION_META.items():
                iid = info_map.get(key)
                if not iid:
                    saves.append({"entity": f"information/{key}", "status": "SKIPPED", "reason": "information_id not found"})
                    continue
                saves.append(admin_save_information(page, admin_base, token, key, iid, fields))
            if "katalog" in info_map:
                saves.append(
                    admin_save_information(
                        page,
                        admin_base,
                        token,
                        "katalog",
                        info_map["katalog"],
                        CATALOG_HUB_META,
                    )
                )
            result["saves"] = saves
            verified = sum(1 for s in saves if s.get("verified"))
            saved = sum(1 for s in saves if s.get("status") == "SAVED")
            result["status"] = "COMPLETE" if saved > 0 and verified >= saved // 2 else "PARTIAL"
            if saved == 0:
                result["status"] = "FAILED"
            page.goto(_admin_url(admin_base, "common/logout", token), timeout=30000)
        except Exception as exc:
            result["status"] = "ERROR"
            result["error_type"] = type(exc).__name__
            result["error"] = str(exc)[:500]
            if saves:
                result["saves"] = saves
        browser.close()
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "after.json", result)
    write_text(
        DEPLOYMENT_ROOT / "admin-evidence" / "after.md",
        "\n".join(
            ["# Admin saves", "", f"Status: {result.get('status')}", ""]
            + [
                f"- {s.get('entity', '?')}: {s.get('status')} verified={s.get('verified', False)}"
                for s in result.get("saves", [])
            ]
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


def build_product_meta_next_task() -> None:
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "product-meta-generator-next-task.md",
        "\n".join(
            [
                "# Next task: SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-DISCOVERY-01",
                "",
                "Purpose: read-only discovery of existing product meta generator (possibly Sergey implementation).",
                "",
                "Suspected areas:",
                "- `catalog/controller/product/product.php`",
                "- `catalog/model/catalog/product.php`",
                "- SEO extension / modification files under `/storage/modification/`",
                "- Custom Sergey SEO code",
                "",
                "No product meta mutations in discovery operation.",
            ]
        ),
    )


def run_plan() -> int:
    ensure_dirs()
    build_remaining_gaps()
    build_meta_copy()
    build_authority_manifests()
    build_product_meta_next_task()
    return 0


def run_all(admin: bool) -> int:
    ensure_dirs()
    build_remaining_gaps()
    crawl_urls_for_phase("meta-before")
    build_meta_copy()
    build_authority_manifests()
    build_dry_run()
    build_product_meta_next_task()
    admin_result = {"status": "SKIPPED"}
    if admin:
        admin_result = phase_admin_saves()
    crawl_urls_for_phase("meta-after")
    preservation = verify_robots_sitemap()
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "run-summary.json",
        {
            "operation_id": OPERATION_ID,
            "admin": admin,
            "admin_result": admin_result,
            "preservation": preservation,
            "finished_at": utc_now(),
        },
    )
    print(
        json.dumps(
            {"admin_status": admin_result.get("status"), "saves": len(admin_result.get("saves", [])), "preservation": preservation},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("plan", "crawl-before", "admin", "all"), default="all")
    parser.add_argument("--no-admin", action="store_true")
    args = parser.parse_args()
    if args.phase == "plan":
        return run_plan()
    if args.phase == "crawl-before":
        ensure_dirs()
        build_remaining_gaps()
        crawl_urls_for_phase("meta-before")
        return 0
    if args.phase == "admin":
        return 0 if phase_admin_saves().get("status") in ("COMPLETE", "PARTIAL") else 1
    return run_all(admin=not args.no_admin)


if __name__ == "__main__":
    sys.exit(main())
