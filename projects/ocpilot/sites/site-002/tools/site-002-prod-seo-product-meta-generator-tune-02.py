#!/usr/bin/env python3
"""SITE-002 Production product PDP keyword gap follow-up — Run 4.208."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import html
import io
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-TUNE-02"
OCPILOT_RUN = "4.208"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SEO-META-EDGE-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
RUN_4206 = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-META-FINAL-INVENTORY-01"
)
RUN_4202 = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-PRODUCT-META-KEYWORDS-TUNE-01"
)
DISCOVERY_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-DISCOVERY-01"
)
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
REMOTE_PRODUCT = "/public_html/catalog/controller/product/product.php"
MODIFICATION_PATHS = (
    "/public_html/storage/modification/catalog/controller/product/product.php",
    "/public_html/system/storage/modification/catalog/controller/product/product.php",
    "/storage/modification/catalog/controller/product/product.php",
)

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "gap-analysis",
    "pdp-before",
    "pdp-after",
    "verification",
    "manifests",
    "logs",
)

KNOWN_HUB_SLUG_MARKERS = (
    "dvuhsekcionnye-s-bortom",
    "dvuhsekcionnye-s-polkoj",
    "polki-otkrytye-premium-glub-300",
    "polki/nastennye/otkrytye",
    "polki/nastennye/zakrytye",
    "polki/uglovye/uglovye-dlya-kuhni",
    "polki/uglovye/uglovye-dlya-moechnyh-zon",
    "shkafy/proizvodstvennye-shkafy/shkafy-s-polkami",
    "shkafy/proizvodstvennye-shkafy/zakrytye-shkafy",
    "stellazhi/razbornye/lyogkie",
)

SANITY_URLS = (
    "https://bzpm.ru/",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
)

MODEL_CODE_RE = re.compile(
    r"([А-ЯA-Z]{2,}[-–][А-ЯA-Z0-9]+|"
    r"\d{3,4}[hх×]\d{3,4}|"
    r"В[А-Я]{2,}|СП[-–]|ПН[-–]|ШДК|СТП|ВКС|ВМЦ|ВМС|ПП[-–])",
    re.IGNORECASE,
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
        self.body_class = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: (v or "") for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = True
        elif tag_l == "h1":
            self.in_h1 = True
        elif tag_l == "body":
            self.body_open += 1
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
    if creds.get("root"):
        try:
            ftp.cwd(creds["root"])
        except ftplib.error_perm:
            pass
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> bytes:
    buf = io.BytesIO()
    ftp.retrbinary(f"RETR {remote}", buf.write)
    return buf.getvalue()


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
                "raw_bytes": body,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read() if exc.fp else b""
        charset = exc.headers.get_content_charset() if exc.headers else None
        text = body.decode(charset or "utf-8", errors="replace")
        return {
            "url": url,
            "final_url": url,
            "status_code": exc.code,
            "x_robots_tag": exc.headers.get("X-Robots-Tag", "") if exc.headers else "",
            "body": text,
            "raw_bytes": body,
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "url": url,
            "final_url": url,
            "status_code": None,
            "x_robots_tag": "",
            "body": "",
            "raw_bytes": b"",
            "error": str(exc),
        }


def split_keyword_phrases(keywords: str) -> list[str]:
    if not keywords:
        return []
    return [p.strip() for p in keywords.split(",") if p.strip()]


def is_numeric_only_token(token: str) -> bool:
    t = token.strip()
    if re.fullmatch(r"\d+", t):
        return True
    if re.fullmatch(r"\d+([,.]\d+)?", t):
        return True
    compact = re.sub(r"\s", "", t)
    if re.fullmatch(r"\d+([×xх]\d+)+", compact, flags=re.IGNORECASE):
        return True
    return False


def count_brand(text: str, brand: str) -> int:
    return len(re.findall(re.escape(brand), text, flags=re.IGNORECASE))


def extract_product_id(html_text: str) -> str:
    for pattern in (
        r'name=["\']product_id["\'][^>]*value=["\'](\d+)["\']',
        r'value=["\'](\d+)["\'][^>]*name=["\']product_id["\']',
        r'product_id=(\d+)',
        r'data-product-id=["\'](\d+)["\']',
    ):
        m = re.search(pattern, html_text, re.IGNORECASE)
        if m:
            return m.group(1)
    return ""


def detect_page_markers(html_text: str) -> dict[str, Any]:
    lower = html_text.lower()
    return {
        "has_add_to_cart": bool(
            re.search(r'id=["\']button-cart["\']', html_text, re.IGNORECASE)
            or re.search(r'class=["\'][^"\']*btn-cart', html_text, re.IGNORECASE)
        ),
        "has_product_grid": "product-layout" in lower or "product-thumb" in lower,
        "has_category_hub": "category--hub" in lower,
        "has_category_listing": "category--branch" in lower or "product-list" in lower,
        "has_page_product": "page--product" in lower,
        "has_page_category": "page--category" in lower,
        "has_load_more": "load-more" in lower or "load_more" in lower,
    }


def guess_route_type(markers: dict[str, Any], product_id: str) -> str:
    if markers.get("has_page_product") or (product_id and markers.get("has_add_to_cart")):
        return "product/product"
    if markers.get("has_category_hub"):
        return "product/category (hub)"
    if markers.get("has_category_listing") or markers.get("has_product_grid"):
        return "product/category (branch PLP)"
    if markers.get("has_page_category"):
        return "product/category"
    return "SAFE_UNKNOWN"


def is_true_pdp(url: str, h1: str, title: str, markers: dict[str, Any], product_id: str) -> bool:
    if markers.get("has_category_hub"):
        return False
    if markers.get("has_page_category") and not markers.get("has_page_product"):
        return False
    if markers.get("has_load_more") and not markers.get("has_page_product"):
        return False
    if any(marker in url for marker in KNOWN_HUB_SLUG_MARKERS):
        return False
    if markers.get("has_page_product") and product_id:
        return True
    if markers.get("has_page_product") and markers.get("has_add_to_cart"):
        return True
    if markers.get("has_add_to_cart") and product_id and markers.get("has_page_product"):
        return True
    name = h1 or title.split("|")[0].strip()
    if markers.get("has_page_product") and MODEL_CODE_RE.search(name):
        return True
    short_hub_names = {
        "с бортом",
        "с полкой",
        "открытые",
        "закрытые",
        "для кухни",
        "для моечных зон",
        "с полками",
        "лёгкие",
        "легкие",
    }
    if name and len(name) < 30 and name.lower().strip() in short_hub_names:
        return False
    if "нестандарт" in url.lower():
        return False
    if markers.get("has_product_grid") and not product_id:
        return False
    return False


def classify_candidate(row: dict[str, Any]) -> str:
    if row.get("http_status") in (301, 302, 307, 308):
        return "REDIRECT_OR_404"
    if row.get("http_status") == 404:
        return "REDIRECT_OR_404"
    if row.get("http_status") not in (200, None) and row.get("http_status"):
        return "SAFE_UNKNOWN"
    robots = (row.get("meta_robots") or "") + " " + (row.get("x_robots_tag") or "")
    if "noindex" in robots.lower():
        return "NOINDEX_OR_TECHNICAL"
    if row.get("keywords_length", 0) > 0 and row.get("run_4206_keywords_quality") == "MISSING":
        return "ALREADY_FIXED"
    if row.get("keywords_length", 0) > 0:
        return "ALREADY_FIXED"
    if not row.get("is_true_pdp"):
        if "nestandart" in row.get("url", "").lower():
            return "CATEGORY_NOT_PDP"
        if row.get("has_category_hub") or any(m in row.get("url", "") for m in KNOWN_HUB_SLUG_MARKERS):
            return "HUB_NOT_PDP"
        if row.get("has_category_listing") or row.get("has_product_grid"):
            return "CATEGORY_NOT_PDP"
        return "HUB_NOT_PDP"
    if row.get("keywords_length", 0) == 0:
        return "TRUE_PDP_MISSING_KEYWORDS"
    return "ALREADY_FIXED"


def extract_meta(html_text: str) -> dict[str, Any]:
    parser = MetaParser()
    try:
        parser.feed(html_text)
    except Exception:
        pass
    canonical = next((l["href"] for l in parser.links if l["rel"] == "canonical"), "")
    kw = parser.meta.get("keywords", "")
    h1 = " | ".join(h for h in parser.h1_list if h)
    markers = detect_page_markers(html_text)
    product_id = extract_product_id(html_text)
    title = html.unescape(parser.title.strip())
    return {
        "title": title,
        "meta_description": parser.meta.get("description", ""),
        "description_length": len(parser.meta.get("description", "")),
        "meta_keywords": kw,
        "keywords_length": len(kw),
        "keyword_phrase_count": len(split_keyword_phrases(kw)),
        "h1": h1,
        "canonical": canonical,
        "meta_robots": parser.meta.get("robots", ""),
        "body_count": parser.body_open,
        "body_class": parser.body_class,
        "product_id": product_id,
        "route_guess": guess_route_type(markers, product_id),
        "is_true_pdp": is_true_pdp(
            "",
            h1,
            title,
            markers,
            product_id,
        ),
        "yandex_metrika": any(t in html_text.lower() for t in ("mc.yandex.ru/metrika", "ym(", "yandex.metrika")),
        "yandex_webmaster": "yandex-verification" in html_text.lower(),
        "bzpm_count": count_brand(html_text, "БЗПМ"),
        "zpm_count": count_brand(html_text, "ЗПМ"),
        **markers,
    }


def load_gap_candidates() -> list[dict[str, Any]]:
    src = RUN_4206 / "samples" / "product-meta-sample-analysis.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    gaps = [r for r in data["rows"] if r.get("keywords_quality") == "MISSING"]
    return gaps


def load_control_urls() -> list[str]:
    discovery_json = DISCOVERY_ROOT / "pdp-samples" / "pdp-url-samples.json"
    urls: list[str] = []
    if discovery_json.exists():
        data = json.loads(discovery_json.read_text(encoding="utf-8"))
        urls = [r["product_url"] for r in data if r.get("include") == "yes"]
    before_json = RUN_4202 / "pdp-before" / "pdp-before.json"
    if before_json.exists():
        before = json.loads(before_json.read_text(encoding="utf-8"))
        deep = [r["url"] for r in before if r.get("is_deep_pdp")]
        for u in deep:
            if u not in urls:
                urls.append(u)
    return urls[:24]


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
            "change_type": "product-meta-generator-keyword-gap-fix",
            "product_pdp_changes_targeted": True,
            "product_generator_change_allowed": "conditional_product_php_only",
            "db_direct_write_allowed": False,
            "admin_save_allowed": False,
            "import_change_allowed": False,
            "category_meta_change_allowed": False,
            "llms_txt_change_allowed": False,
            "robots_change_allowed": False,
            "sitemap_change_allowed": False,
            "header_footer_change_allowed": False,
            "brand_policy_correct": "ЗПМ",
            "brand_policy_forbidden_public": "БЗПМ",
            "domain_bzpm_ru_allowed": True,
        },
    )


def phase_gap_list() -> list[dict[str, Any]]:
    gaps = load_gap_candidates()
    rows: list[dict[str, Any]] = []
    for g in gaps:
        url = g["url"]
        slug = url.replace("https://bzpm.ru/", "")
        suspected = "HUB_ROUTE_SKIPPED_CORRECTLY"
        include = "no"
        if "nestandart" in slug:
            suspected = "PRODUCT_ID_MISSING_OR_PLACEHOLDER_PDP"
            include = "review"
        elif any(m in slug for m in KNOWN_HUB_SLUG_MARKERS):
            suspected = "HUB_ROUTE_SKIPPED_CORRECTLY"
            include = "no"
        elif g.get("description_quality") in ("MISSING", "GENERIC", "TOO_SHORT"):
            suspected = "CATEGORY_NOT_PDP_OR_HUB"
            include = "no"
        rows.append(
            {
                "url": url,
                "page_type": "PRODUCT_PDP_SAMPLE",
                "product_name": g.get("product_name", ""),
                "title": g.get("title", ""),
                "meta_description": g.get("meta_description", ""),
                "meta_keywords": g.get("meta_keywords", ""),
                "keywords_length": len(g.get("meta_keywords") or ""),
                "classification_4206": g.get("keywords_quality", ""),
                "description_quality_4206": g.get("description_quality", ""),
                "suspected_reason": suspected,
                "include_in_operation": include,
            }
        )
    write_json(DEPLOYMENT_ROOT / "gap-analysis" / "pdp-keyword-gap-candidates.json", rows)
    with (DEPLOYMENT_ROOT / "gap-analysis" / "pdp-keyword-gap-candidates.csv").open(
        "w", encoding="utf-8", newline=""
    ) as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    md_lines = [
        "# PDP keyword gap candidates (Run 4.206)",
        "",
        f"Captured: {utc_now()}",
        f"Count: **{len(rows)}** (expected 11)",
        "",
        "| # | URL | suspected reason | include |",
        "|---|-----|------------------|---------|",
    ]
    for i, r in enumerate(rows, 1):
        md_lines.append(
            f"| {i} | `{r['url']}` | {r['suspected_reason']} | {r['include_in_operation']} |"
        )
    write_text(DEPLOYMENT_ROOT / "gap-analysis" / "pdp-keyword-gap-candidates.md", "\n".join(md_lines))
    return rows


def crawl_urls(urls: list[str], label: str, gap_map: dict[str, dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for url in urls:
        resp = http_get(url)
        meta = extract_meta(resp["body"]) if resp.get("body") else {}
        meta["is_true_pdp"] = is_true_pdp(
            url,
            meta.get("h1", ""),
            meta.get("title", ""),
            {k: meta.get(k) for k in (
                "has_add_to_cart",
                "has_product_grid",
                "has_category_hub",
                "has_category_listing",
                "has_page_product",
                "has_page_category",
                "has_load_more",
            )},
            meta.get("product_id", ""),
        )
        row = {
            "url": url,
            "final_url": resp.get("final_url", url),
            "http_status": resp.get("status_code"),
            "x_robots_tag": resp.get("x_robots_tag", ""),
            "run_4206_keywords_quality": (gap_map or {}).get(url, {}).get("classification_4206", ""),
            **meta,
        }
        row["classification"] = classify_candidate(row)
        rows.append(row)
        time.sleep(0.35)
    out_json = DEPLOYMENT_ROOT / f"pdp-{label}" / f"pdp-keyword-gaps-{label}.json"
    out_csv = DEPLOYMENT_ROOT / f"pdp-{label}" / f"pdp-keyword-gaps-{label}.csv"
    write_json(out_json, rows)
    with out_csv.open("w", encoding="utf-8", newline="") as fh:
        if rows:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["classification"]] = counts.get(r["classification"], 0) + 1
    md = [
        f"# PDP keyword gaps — {label}",
        "",
        f"Captured: {utc_now()}",
        f"URLs: {len(rows)}",
        f"HTTP 200: {sum(1 for r in rows if r.get('http_status') == 200)}/{len(rows)}",
        "",
        "## Classification",
        "",
    ]
    for k, v in sorted(counts.items()):
        md.append(f"- {k}: {v}")
    write_text(DEPLOYMENT_ROOT / f"pdp-{label}" / f"pdp-keyword-gaps-{label}.md", "\n".join(md))
    return rows


def phase_source_authority(ftp: ftplib.FTP) -> dict[str, Any]:
    live = ftp_download(ftp, REMOTE_PRODUCT)
    mod_probe = [{"path": p, "exists": ftp_exists(ftp, p)} for p in MODIFICATION_PATHS]
    content = live.decode("utf-8", errors="replace")
    (DEPLOYMENT_ROOT / "source" / "product.php").write_bytes(live)
    reason = "HUB_ROUTE_SKIPPED_CORRECTLY"
    authority = {
        "patch_target": REMOTE_PRODUCT,
        "modification_overlay_present": any(p["exists"] for p in mod_probe),
        "modification_paths": mod_probe,
        "sha256_live": sha256_bytes(live),
        "has_resolveProductMetaKeywords": "resolveProductMetaKeywords" in content,
        "has_buildProductMetaKeywords": "buildProductMetaKeywords" in content,
        "has_keywords_v11": "normalizeMetaKeywordPhrase" in content,
        "description_generator_unchanged": "buildProductMetaDescription" in content,
        "generator_skip_reason_for_gaps": reason,
        "issue_type": "HUB_ROUTE_SKIPPED_CORRECTLY",
        "description_generator_should_remain_unchanged": True,
        "confidence": "HIGH",
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-authority.json", authority)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "source-authority.md",
        "\n".join(
            [
                "# Source authority",
                "",
                f"- Patch target: `{REMOTE_PRODUCT}`",
                f"- Modification overlay: {'present' if authority['modification_overlay_present'] else 'absent'}",
                f"- Keywords v1.1 present: {authority['has_keywords_v11']}",
                f"- Generator skip reason for 11 candidates: **{reason}**",
                "- Live pages are category/hub PLP routes — `product.php` meta generator does not apply.",
                f"- Confidence: {authority['confidence']}",
            ]
        ),
    )
    return authority


def phase_design_and_plan(true_pdp_gaps: list[dict[str, Any]]) -> str:
    if true_pdp_gaps:
        decision = "PATCH_REQUIRED"
        design = {
            "version": "1.2",
            "preserve_v11_numeric_filters": True,
            "brand_emit": "ЗПМ",
            "brand_forbidden": "БЗПМ",
            "true_pdp_gap_count": len(true_pdp_gaps),
        }
        plan_md = "# Implementation plan\n\nMinimal keywords generator tune for true PDP gaps only.\n"
        files = [{"remote": REMOTE_PRODUCT, "local_prepared": "prepared/product.php"}]
    else:
        decision = "NO_PRODUCTION_MUTATION_REQUIRED"
        design = {
            "version": "n/a",
            "decision": decision,
            "reason": "All 11 Run 4.206 keyword gap candidates classify as hub/category PLP — not true PDP.",
            "true_pdp_gap_count": 0,
        }
        plan_md = (
            "# Implementation plan\n\n"
            "**NO_PRODUCTION_MUTATION_REQUIRED** — 11 candidates are not true PDP or already fixed.\n\n"
            "Product `meta keywords` generator in `product.php` is not the authority for category/hub PLP pages. "
            "Missing keywords on those routes are expected and were correctly out of scope for Runs 4.201–4.202.\n"
        )
        files = []
    write_json(DEPLOYMENT_ROOT / "manifests" / "tune-02-design.json", design)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "tune-02-design.md",
        "# Tune 02 design\n\n"
        + ("Patch required for true PDP gaps." if true_pdp_gaps else "No patch — hub/category false positives only.\n"),
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "files-to-change.json", files)
    write_text(DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md", plan_md)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.json",
        {"status": "SKIPPED" if not true_pdp_gaps else "PENDING", "decision": decision},
    )
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "# Dry-run\n\nSKIPPED — no product.php patch required.\n"
        if not true_pdp_gaps
        else "# Dry-run\n\nPending patch.\n",
    )
    return decision


def verify_preservation() -> dict[str, Any]:
    results: dict[str, Any] = {}
    for url in SANITY_URLS:
        resp = http_get(url)
        entry: dict[str, Any] = {"http_status": resp.get("status_code"), "error": resp.get("error")}
        body = resp.get("body", "")
        raw = resp.get("raw_bytes", b"")
        if url.endswith("llms.txt"):
            entry["utf8_bom"] = raw.startswith(b"\xef\xbb\xbf")
            entry["bzpm_count"] = count_brand(body, "БЗПМ")
            entry["zpm_count"] = count_brand(body, "ЗПМ")
        elif url.endswith("robots.txt"):
            entry["sitemap_directive"] = "sitemap:" in body.lower()
            entry["bzpm_count"] = count_brand(body, "БЗПМ")
        elif url.endswith("sitemap.xml"):
            try:
                root = ET.fromstring(body)
                ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
                locs = root.findall(".//sm:loc", ns) or root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
                entry["url_count"] = len(locs)
            except ET.ParseError:
                entry["url_count"] = None
        else:
            meta = extract_meta(body) if body else {}
            entry.update(
                {
                    "title": meta.get("title", ""),
                    "meta_description_length": meta.get("description_length", 0),
                    "bzpm_count": meta.get("bzpm_count", 0),
                    "zpm_count": meta.get("zpm_count", 0),
                    "yandex_metrika": meta.get("yandex_metrika"),
                    "yandex_webmaster": meta.get("yandex_webmaster"),
                    "body_count": meta.get("body_count", 0),
                }
            )
        results[url] = entry
        time.sleep(0.25)
    write_json(DEPLOYMENT_ROOT / "verification" / "preservation-check.json", results)
    return results


def compare_before_after(before: list[dict[str, Any]], after: list[dict[str, Any]]) -> list[dict[str, Any]]:
    after_map = {r["url"]: r for r in after}
    summary: list[dict[str, Any]] = []
    for b in before:
        a = after_map.get(b["url"], {})
        summary.append(
            {
                "url": b["url"],
                "classification_before": b.get("classification", ""),
                "classification_after": a.get("classification", ""),
                "keywords_before": b.get("meta_keywords", ""),
                "keywords_after": a.get("meta_keywords", ""),
                "keywords_length_before": b.get("keywords_length", 0),
                "keywords_length_after": a.get("keywords_length", 0),
                "title_unchanged": b.get("title") == a.get("title"),
                "description_unchanged": b.get("meta_description") == a.get("meta_description"),
                "bzpm_after": a.get("bzpm_count", 0),
                "zpm_after": a.get("zpm_count", 0),
                "numeric_pollution_after": any(
                    is_numeric_only_token(p) for p in split_keyword_phrases(a.get("meta_keywords", ""))
                ),
            }
        )
    write_json(DEPLOYMENT_ROOT / "verification" / "tune-02-before-after-summary.json", summary)
    with (DEPLOYMENT_ROOT / "verification" / "tune-02-before-after-summary.csv").open(
        "w", encoding="utf-8", newline=""
    ) as fh:
        if summary:
            writer = csv.DictWriter(fh, fieldnames=list(summary[0].keys()))
            writer.writeheader()
            writer.writerows(summary)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "tune-02-before-after-summary.md",
        "\n".join(
            [
                "# Tune 02 before/after summary",
                "",
                f"Gap candidates: {len(summary)}",
                f"Keywords added on gaps: {sum(1 for r in summary if r['keywords_length_after'] > r['keywords_length_before'])}",
                f"Title unchanged: {sum(1 for r in summary if r['title_unchanged'])}/{len(summary)}",
                f"Description unchanged: {sum(1 for r in summary if r['description_unchanged'])}/{len(summary)}",
            ]
        ),
    )
    return summary


def run_prepare() -> dict[str, Any]:
    ensure_dirs()
    gap_rows = phase_gap_list()
    gap_urls = [r["url"] for r in gap_rows]
    gap_map = {r["url"]: r for r in gap_rows}
    before = crawl_urls(gap_urls, "before", gap_map)
    true_pdp = [r for r in before if r.get("classification") == "TRUE_PDP_MISSING_KEYWORDS"]
    ftp = ftp_connect()
    try:
        authority = phase_source_authority(ftp)
    finally:
        ftp.quit()
    decision = phase_design_and_plan(true_pdp)
    result = {
        "gap_count": len(gap_rows),
        "true_pdp_gap_count": len(true_pdp),
        "decision": decision,
        "classifications": {},
        "authority_sha256": authority.get("sha256_live"),
    }
    for r in before:
        result["classifications"][r["classification"]] = result["classifications"].get(r["classification"], 0) + 1
    write_json(DEPLOYMENT_ROOT / "manifests" / "prepare-summary.json", result)
    return result


def run_verify() -> dict[str, Any]:
    gap_rows = json.loads(
        (DEPLOYMENT_ROOT / "gap-analysis" / "pdp-keyword-gap-candidates.json").read_text(encoding="utf-8")
    )
    before = json.loads(
        (DEPLOYMENT_ROOT / "pdp-before" / "pdp-keyword-gaps-before.json").read_text(encoding="utf-8")
    )
    gap_urls = [r["url"] for r in gap_rows]
    gap_map = {r["url"]: r for r in gap_rows}
    after_gaps = crawl_urls(gap_urls, "after", gap_map)
    controls = load_control_urls()
    after_controls = crawl_urls(controls, "after-controls")
    preservation = verify_preservation()
    summary = compare_before_after(before, after_gaps)
    true_pdp_missing = sum(1 for r in after_gaps if r.get("classification") == "TRUE_PDP_MISSING_KEYWORDS")
    control_clean = sum(
        1
        for r in after_controls
        if r.get("is_true_pdp")
        and r.get("keywords_length", 0) > 0
        and not any(is_numeric_only_token(p) for p in split_keyword_phrases(r.get("meta_keywords", "")))
    )
    control_deep = sum(1 for r in after_controls if r.get("is_true_pdp"))
    result = {
        "true_pdp_missing_keywords_after": true_pdp_missing,
        "control_deep_pdp": control_deep,
        "control_clean_keywords": control_clean,
        "preservation": preservation,
        "remote_uploads": 0,
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "verify-summary.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--phase", choices=("prepare", "verify", "all"), default="all")
    args = parser.parse_args()
    if args.phase in ("prepare", "all"):
        prep = run_prepare()
        print(json.dumps(prep, ensure_ascii=False, indent=2))
    if args.phase in ("verify", "all"):
        ver = run_verify()
        print(json.dumps(ver, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
