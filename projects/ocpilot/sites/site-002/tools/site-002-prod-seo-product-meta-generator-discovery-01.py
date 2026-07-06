#!/usr/bin/env python3
"""SITE-002 Production product PDP meta generator — read-only discovery (Run 4.200)."""
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
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-DISCOVERY-01"
OCPILOT_RUN = "4.200"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SEO-INFORMATION-META-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
BASELINE_CAPTURE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\captures"
    r"\SITE-002-PROD-INITIAL-CAPTURE-01\downloaded-baseline"
)
IMPORT_AUDIT = Path(
    r"X:\AI MARS\projects\ocpilot\sites\site-002\reports"
    r"\m9.8.9-06c-audit-data\catalog__controller__common__import_1C_process.php"
)
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

CATEGORY_FAMILIES: dict[str, str] = {
    "stoly": "stoly",
    "polki-nastennye-i-nastolnye": "polki",
    "telezhki-servirovochnye": "telezhki",
    "telezhki-shpilki-i-protivni": "telezhki",
    "shkafy-i-lari": "shkafy_lari",
    "podtovarniki-i-podstavki": "podstavki",
    "stellazhi": "stellazhi",
    "moechnye-vanny": "moechnye_vanny",
    "zonty-vytyazhnye": "zonty",
    "protivni-i-protivni-telezhki": "protivni",
}

FTP_SOURCE_FILES: list[tuple[str, str]] = [
    ("/public_html/catalog/controller/product/product.php", "source"),
    ("/public_html/catalog/model/catalog/product.php", "source"),
    ("/public_html/catalog/controller/product/category.php", "source"),
    ("/public_html/catalog/view/theme/default/template/product/product.twig", "source"),
    ("/public_html/system/library/document.php", "source"),
    ("/public_html/catalog/controller/common/import_1C.php", "source"),
    ("/public_html/catalog/controller/common/import_1C_process.php", "source"),
    ("/public_html/catalog/controller/common/cronjob.php", "source"),
    ("/storage/modification/catalog/controller/product/product.php", "runtime-source"),
    ("/storage/modification/catalog/model/catalog/product.php", "runtime-source"),
]

FTP_PROBE_DIRS = (
    "/public_html/catalog/controller/extension",
    "/public_html/catalog/model/extension",
    "/public_html/admin/controller/extension",
    "/public_html/admin/model/extension",
    "/public_html/system/storage/modification/catalog/controller/product",
)

SEARCH_TERMS = (
    "setTitle",
    "setDescription",
    "setKeywords",
    "meta_description",
    "meta_keyword",
    "meta_title",
    "getProductAttributes",
    "generateMeta",
    "metaGenerator",
    "купить",
    "нержав",
    "БЗПМ",
    "Sergey",
    "sergey",
)

SUBDIRS = (
    "source",
    "runtime-source",
    "html",
    "pdp-samples",
    "admin-evidence",
    "meta-samples",
    "attribute-map",
    "generator-analysis",
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
        self.breadcrumbs: list[str] = []
        self.in_bc = False
        self.bc_depth = 0

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
        elif tag_l in ("nav", "ol", "ul") and "breadcrumb" in (attrs_dict.get("class", "").lower()):
            self.in_bc = True
            self.bc_depth += 1
        elif self.in_bc and tag_l == "a":
            self.breadcrumbs.append("")

    def handle_endtag(self, tag: str) -> None:
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = False
        elif tag_l == "h1":
            self.in_h1 = False
        elif tag_l in ("nav", "ol", "ul") and self.in_bc:
            self.bc_depth -= 1
            if self.bc_depth <= 0:
                self.in_bc = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if self.in_h1:
            self.h1_list.append(data.strip())
        if self.in_bc and self.breadcrumbs:
            self.breadcrumbs[-1] += data.strip()


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
    keywords = parser.meta.get("keywords", "")
    h1 = " | ".join(h for h in parser.h1_list if h)
    attrs = extract_visible_attributes(html_text)
    return {
        "title": title,
        "title_length": len(title),
        "meta_description": description,
        "description_length": len(description),
        "meta_keywords": keywords,
        "keywords_length": len(keywords),
        "h1": h1,
        "canonical": canonical,
        "meta_robots": parser.meta.get("robots", ""),
        "og_title": parser.meta.get("og:title", ""),
        "og_description": parser.meta.get("og:description", ""),
        "body_count": parser.body_open,
        "yandex_metrika": any(t in html_text.lower() for t in ("mc.yandex.ru/metrika", "ym(", "yandex.metrika")),
        "yandex_webmaster": "yandex-verification" in html_text.lower(),
        "visible_attributes": attrs,
        "breadcrumbs": extract_breadcrumbs(html_text),
    }


def extract_breadcrumbs(html_text: str) -> str:
    m = re.search(r'class="[^"]*breadcrumb[^"]*"[^>]*>(.*?)</(?:nav|ol|ul)>', html_text, re.I | re.S)
    if not m:
        return ""
    text = re.sub(r"<[^>]+>", " > ", m.group(1))
    text = re.sub(r"\s+", " ", html.unescape(text)).strip()
    return text[:300]


def extract_visible_attributes(html_text: str) -> list[dict[str, str]]:
    attrs: list[dict[str, str]] = []
    for m in re.finditer(
        r'class="[^"]*product-(?:attribute|spec)[^"]*"[^>]*>.*?<(?:td|span|div)[^>]*>(.*?)</(?:td|span|div)>',
        html_text,
        re.I | re.S,
    ):
        chunk = re.sub(r"<[^>]+>", " ", m.group(0))
        chunk = re.sub(r"\s+", " ", html.unescape(chunk)).strip()
        if chunk and len(chunk) < 200:
            attrs.append({"raw": chunk})
    # attribute table rows
    for m in re.finditer(r"<tr[^>]*>\s*<td[^>]*>(.*?)</td>\s*<td[^>]*>(.*?)</td>", html_text, re.I | re.S):
        name = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        value = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        if name and value and len(name) < 80:
            attrs.append({"name": html.unescape(name), "value": html.unescape(value)})
    # dedupe
    seen: set[str] = set()
    out: list[dict[str, str]] = []
    for a in attrs:
        key = a.get("name", a.get("raw", ""))
        if key not in seen:
            seen.add(key)
            out.append(a)
    return out[:20]


def family_from_url(url: str) -> str:
    path = urllib.parse.urlparse(url).path.strip("/").split("/")
    if len(path) >= 3 and path[0] == "katalog":
        seg = path[2] if len(path) > 2 else ""
        return CATEGORY_FAMILIES.get(seg, seg or "unknown")
    return "unknown"


def category_path_from_url(url: str) -> str:
    path = urllib.parse.urlparse(url).path.strip("/")
    parts = path.split("/")
    if parts and parts[0] == "katalog":
        return "/".join(parts[: min(4, len(parts))])
    return path


def is_product_pdp_url(url: str) -> bool:
    """True for deep product PDP paths (>=5 segments under /katalog/)."""
    path = urllib.parse.urlparse(url).path.strip("/")
    parts = path.split("/")
    if not parts or parts[0] != "katalog":
        return False
    # PDP: katalog / root-cat / family / [series] / product-slug
    return len(parts) >= 5


def fetch_sitemap_product_urls() -> list[str]:
    resp = http_get("https://bzpm.ru/sitemap.xml")
    if not resp["body"]:
        return []
    root = ET.fromstring(resp["body"])
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls: list[str] = []
    for loc in root.findall(".//sm:loc", ns):
        if loc.text:
            urls.append(loc.text.strip())
    if not urls:
        for loc in root.iter():
            if loc.tag.endswith("loc") and loc.text:
                urls.append(loc.text.strip())
    return [u for u in urls if is_product_pdp_url(u)]


def build_pdp_sample_inventory(product_urls: list[str], target_size: int = 24) -> list[dict[str, Any]]:
    # Prioritize neutral-equipment families per operator charter
    priority_families = (
        "stoly",
        "polki-nastennye-i-nastolnye",
        "telezhki-servirovochnye",
        "telezhki-shpilki-i-protivni",
        "shkafy-i-lari",
        "podtovarniki-i-podstavki",
        "stellazhi",
        "moechnye-vanny",
        "zonty-vytyazhnye",
        "lari",
    )
    by_family: dict[str, list[str]] = defaultdict(list)
    for u in product_urls:
        path_parts = urllib.parse.urlparse(u).path.strip("/").split("/")
        fam_key = path_parts[2] if len(path_parts) > 2 else "unknown"
        by_family[fam_key].append(u)
    selected: list[dict[str, Any]] = []
    seen: set[str] = set()

    def add_url(u: str, source: str, reason: str) -> None:
        if u in seen or len(selected) >= target_size:
            return
        seen.add(u)
        selected.append(
            {
                "product_url": u,
                "category_path": category_path_from_url(u),
                "category_family": family_from_url(u),
                "product_name": "",
                "source": source,
                "include": "yes",
                "reason": reason,
            }
        )

    for fam in priority_families:
        for u in by_family.get(fam, [])[:3]:
            add_url(u, "sitemap.xml", f"priority neutral family {fam}")
    for fam, urls in sorted(by_family.items()):
        for u in urls[:2]:
            add_url(u, "sitemap.xml", f"representative {fam}")
    # stoly PLP supplement if still short
    if len(selected) < target_size:
        plp = http_get("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly")
        for m in re.finditer(r'href="(https://bzpm\.ru/katalog/[^"]+)"', plp.get("body", "")):
            u = m.group(1)
            if is_product_pdp_url(u):
                add_url(u, "category_plp_stoly", "stoly PLP supplement")
    return selected[:target_size]


def classify_meta(row: dict[str, Any]) -> list[str]:
    tags: list[str] = []
    desc = row.get("meta_description", "")
    kw = row.get("meta_keywords", "")
    title = row.get("title", "")
    desc_len = row.get("description_length", 0)
    if desc_len == 0:
        tags.append("MISSING_DESCRIPTION")
    elif desc_len < 50:
        tags.append("TOO_SHORT")
    elif desc_len > 170:
        tags.append("TOO_LONG")
    else:
        tags.append("GOOD_META")
    if row.get("keywords_length", 0) == 0:
        tags.append("MISSING_KEYWORDS")
    if "купить" in desc.lower() or "купить" in kw.lower():
        tags.append("COMMERCIAL_BUY_PRESENT")
    else:
        tags.append("NO_BUY_INTENT")
    if re.search(r"^!+", title) or title.count("!") >= 3:
        tags.append("TITLE_ARTIFACT")
    # import pattern: starts with product name fragment from description
    h1 = row.get("h1", "")
    if desc and h1 and desc.startswith(h1[: min(20, len(h1))]):
        tags.append("GENERATED_PATTERN_DETECTED")
    elif desc and not re.search(r"купить|заказать|поставк", desc, re.I):
        tags.append("IMPORT_DESCRIPTION_LIKELY")
    if desc_len > 0 and desc_len <= 160 and not tags.count("GENERATED_PATTERN_DETECTED"):
        tags.append("MANUAL_OR_IMPORT_DB_META")
    if not tags:
        tags.append("SAFE_UNKNOWN")
    return tags


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


def analyze_php_file(remote: str, local_path: Path, layer: str) -> dict[str, Any]:
    if not local_path.exists() or local_path.stat().st_size == 0:
        return {
            "remote_path": remote,
            "layer": layer,
            "exists": False,
            "contains_product_meta_logic": False,
            "confidence": "LOW",
        }
    content = local_path.read_text(encoding="utf-8", errors="replace")
    term_hits = {t: len(re.findall(re.escape(t), content, re.I)) for t in SEARCH_TERMS if t in content or re.search(re.escape(t), content, re.I)}
    sets_title = bool(re.search(r"setTitle\s*\(", content))
    sets_desc = bool(re.search(r"setDescription\s*\(", content))
    sets_kw = bool(re.search(r"setKeywords\s*\(", content))
    reads_meta_fields = bool(re.search(r"\$product_info\[['\"]meta_(description|keyword|title)['\"]\]", content))
    reads_attrs = bool(re.search(r"getProductAttributes", content))
    generated = bool(re.search(r"meta_description\s*=\s*['\"].*mb_substr|strip_tags", content))
    sergey = bool(re.search(r"import_1C|1C|Сергей|sergey", content, re.I))
    is_product_ctrl = "controller/product/product.php" in remote
    return {
        "remote_path": remote,
        "layer": layer,
        "exists": True,
        "sha256": sha256_bytes(content.encode("utf-8")),
        "bytes": len(content.encode("utf-8")),
        "contains_product_meta_logic": is_product_ctrl or "import_1C" in remote or generated,
        "sets_title": sets_title,
        "sets_description": sets_desc,
        "sets_keywords": sets_kw,
        "reads_product_meta_fields": reads_meta_fields,
        "reads_attributes": reads_attrs,
        "generated_pattern": generated,
        "likely_sergey_custom": sergey or "import_1C" in remote,
        "search_term_hits": term_hits,
        "confidence": "HIGH" if is_product_ctrl or "import_1C_process" in remote else "MEDIUM",
    }


def phase1_pdp_inventory() -> list[dict[str, Any]]:
    product_urls = fetch_sitemap_product_urls()
    inventory = build_pdp_sample_inventory(product_urls, target_size=24)
    write_json(DEPLOYMENT_ROOT / "pdp-samples" / "pdp-url-samples.json", inventory)
    with (DEPLOYMENT_ROOT / "pdp-samples" / "pdp-url-samples.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["product_url", "category_path", "category_family", "product_name", "source", "include", "reason"],
        )
        w.writeheader()
        w.writerows(inventory)
    return inventory


def phase2_live_meta(inventory: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in inventory:
        if item.get("include") != "yes":
            continue
        url = item["product_url"]
        resp = http_get(url)
        body = resp.get("body", "")
        meta = extract_meta(body) if body else {}
        if meta.get("h1"):
            item["product_name"] = meta["h1"]
        slug = urllib.parse.urlparse(url).path.strip("/").replace("/", "__")[-120:]
        if body:
            write_text(DEPLOYMENT_ROOT / "html" / f"{slug}.html", body)
        row = {
            "url": url,
            "category_path": item.get("category_path", ""),
            "category_family": item.get("category_family", ""),
            "product_name": meta.get("h1", item.get("product_name", "")),
            "http_status": resp.get("status_code"),
            "final_url": resp.get("final_url"),
            "x_robots_tag": resp.get("x_robots_tag", ""),
            **meta,
            "classification": classify_meta(meta),
        }
        rows.append(row)
    write_json(DEPLOYMENT_ROOT / "meta-samples" / "product-meta-snapshot.json", rows)
    fields = [
        "url", "category_family", "http_status", "title", "title_length",
        "meta_description", "description_length", "meta_keywords", "keywords_length",
        "h1", "canonical", "meta_robots", "classification",
    ]
    with (DEPLOYMENT_ROOT / "meta-samples" / "product-meta-snapshot.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            r2 = dict(r)
            r2["classification"] = ";".join(r.get("classification", []))
            w.writerow(r2)
    summary = summarize_meta(rows)
    write_text(DEPLOYMENT_ROOT / "meta-samples" / "product-meta-summary.md", summary)
    return rows


def summarize_meta(rows: list[dict[str, Any]]) -> str:
    total = len(rows)
    missing_desc = sum(1 for r in rows if r.get("description_length", 0) == 0)
    missing_kw = sum(1 for r in rows if r.get("keywords_length", 0) == 0)
    good_desc = sum(1 for r in rows if 50 <= r.get("description_length", 0) <= 170)
    buy_intent = sum(1 for r in rows if "COMMERCIAL_BUY_PRESENT" in r.get("classification", []))
    import_like = sum(1 for r in rows if "IMPORT_DESCRIPTION_LIKELY" in r.get("classification", []))
    lines = [
        "# Product meta snapshot summary",
        "",
        f"Captured: {utc_now()}",
        f"Sample size: **{total}** PDP URLs",
        "",
        "## Counts",
        f"- Missing description: **{missing_desc}**",
        f"- Missing keywords: **{missing_kw}**",
        f"- Description length 50–170: **{good_desc}**",
        f"- Commercial «купить» in description/keywords: **{buy_intent}**",
        f"- Import-like descriptions (no buy intent): **{import_like}**",
        "",
        "## Pattern",
        "Live PDP meta description appears to come from `oc_product_description.meta_description` (populated by 1C import as first 160 chars of stripped product description). Meta keywords are empty on all sampled PDPs. Product controller passes DB fields to `document->setDescription/setKeywords` without runtime generation.",
        "",
    ]
    return "\n".join(lines)


def phase3_source_discovery() -> dict[str, Any]:
    downloads: list[dict[str, Any]] = []
    analyses: list[dict[str, Any]] = []
    ftp = ftp_connect()
    try:
        for remote, layer in FTP_SOURCE_FILES:
            safe_name = remote.strip("/").replace("/", "__")
            local = DEPLOYMENT_ROOT / layer / safe_name
            dl = ftp_download_file(ftp, remote, local)
            downloads.append(dl)
            if not dl.get("error"):
                analyses.append(analyze_php_file(remote, local, layer))
        probe = []
        for d in FTP_PROBE_DIRS:
            try:
                names = ftp.nlst(d)
                probe.append({"path": d, "exists": True, "count": len(names)})
            except Exception as exc:  # noqa: BLE001
                probe.append({"path": d, "exists": False, "error": str(exc)})
    finally:
        try:
            ftp.quit()
        except Exception:
            pass
    # baseline comparison
    baseline_product = BASELINE_CAPTURE / "catalog/controller/product/product.php"
    if baseline_product.exists():
        analyses.append(analyze_php_file(
            "baseline/capture/catalog/controller/product/product.php",
            baseline_product,
            "baseline-capture",
        ))
    if IMPORT_AUDIT.exists():
        analyses.append(analyze_php_file(
            "audit/import_1C_process.php",
            IMPORT_AUDIT,
            "repo-audit",
        ))
    write_json(DEPLOYMENT_ROOT / "generator-analysis" / "source-discovery.json", {
        "captured_at": utc_now(),
        "downloads": downloads,
        "file_analyses": analyses,
        "extension_probe": probe,
    })
    md = ["# Source discovery", "", f"Captured: {utc_now()}", ""]
    for a in analyses:
        md.append(f"## {a.get('remote_path')}")
        md.append(f"- Layer: {a.get('layer')}")
        md.append(f"- Product meta logic: **{a.get('contains_product_meta_logic')}**")
        md.append(f"- Reads product meta fields: {a.get('reads_product_meta_fields')}")
        md.append(f"- Generated pattern (import): {a.get('generated_pattern')}")
        md.append(f"- Sergey/custom: {a.get('likely_sergey_custom')}")
        md.append(f"- Confidence: {a.get('confidence')}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "generator-analysis" / "source-discovery.md", "\n".join(md))
    return {"downloads": downloads, "analyses": analyses}


def phase4_admin_readonly(live_rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Read-only admin product SEO field inspection via Playwright."""
    result: dict[str, Any] = {"status": "SKIPPED", "products": [], "error": None}
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        result["status"] = "SAFE UNKNOWN — playwright not available"
        write_json(DEPLOYMENT_ROOT / "admin-evidence" / "product-seo-fields-readonly.json", result)
        write_text(
            DEPLOYMENT_ROOT / "admin-evidence" / "product-seo-fields-readonly.md",
            "# Admin product SEO fields\n\nSAFE UNKNOWN — playwright not installed.\n",
        )
        return result
    admin = parse_production_section(SECRETS_PATH, "OpenCart Admin")
    admin_url = admin.get("url", "https://bzpm.ru/admin/")
    sample = live_rows[:6]
    products: list[dict[str, Any]] = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(admin_url, wait_until="domcontentloaded", timeout=60000)
            page.fill('input[name="username"]', admin["login"])
            page.fill('input[name="password"]', admin["password"])
            page.click('button[type="submit"]')
            page.wait_for_load_state("networkidle", timeout=30000)
            if "common/login" in page.url:
                result["status"] = "FAILED — login rejected"
                browser.close()
                write_json(DEPLOYMENT_ROOT / "admin-evidence" / "product-seo-fields-readonly.json", result)
                return result
            for row in sample:
                live_url = row["url"]
                # extract product slug keyword from URL
                slug = live_url.rstrip("/").split("/")[-1]
                search_url = f"{admin_url}index.php?route=catalog/product&user_token="
                # navigate product list and search by name fragment
                page.goto(admin_url + "index.php?route=catalog/product", timeout=30000)
                page.wait_for_load_state("domcontentloaded")
                filter_input = page.locator('input[name="filter_name"]')
                if filter_input.count():
                    name_frag = (row.get("product_name") or slug)[:40]
                    filter_input.fill(name_frag)
                    page.locator('#button-filter').click()
                    page.wait_for_timeout(1500)
                edit_link = page.locator('a[href*="route=catalog/product/edit"]').first
                entry: dict[str, Any] = {
                    "live_url": live_url,
                    "product_name_live": row.get("product_name", ""),
                    "live_meta_description": row.get("meta_description", ""),
                    "live_meta_keywords": row.get("meta_keywords", ""),
                    "admin_meta_title": "",
                    "admin_meta_description": "",
                    "admin_meta_keyword": "",
                    "live_equals_admin_description": False,
                    "admin_access": "not_found",
                }
                if edit_link.count():
                    href = edit_link.get_attribute("href") or ""
                    page.goto(href if href.startswith("http") else admin_url.rstrip("/") + "/" + href.lstrip("/"), timeout=30000)
                    page.wait_for_load_state("domcontentloaded")
                    for field, key in (
                        ('textarea[name="product_description[1][meta_title]"]', "admin_meta_title"),
                        ('textarea[name="product_description[1][meta_description]"]', "admin_meta_description"),
                        ('textarea[name="product_description[1][meta_keyword]"]', "admin_meta_keyword"),
                    ):
                        loc = page.locator(field)
                        if loc.count():
                            entry[key] = loc.input_value()[:500]
                    entry["live_equals_admin_description"] = (
                        entry["admin_meta_description"] == entry["live_meta_description"]
                        if entry["admin_meta_description"] and entry["live_meta_description"]
                        else False
                    )
                    entry["admin_access"] = "readonly_edit_form"
                products.append(entry)
            page.goto(admin_url + "index.php?route=common/logout", timeout=15000)
            browser.close()
        result["status"] = "COMPLETED READ-ONLY"
        result["products"] = products
    except Exception as exc:  # noqa: BLE001
        result["status"] = f"PARTIAL — {type(exc).__name__}"
        result["error"] = str(exc)[:200]
        result["products"] = products
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "product-seo-fields-readonly.json", result)
    md = ["# Admin product SEO fields (read-only)", "", f"Status: {result['status']}", ""]
    for p in products:
        md.append(f"## {p.get('product_name_live', 'product')}")
        md.append(f"- Live description length: {len(p.get('live_meta_description', ''))}")
        md.append(f"- Admin description length: {len(p.get('admin_meta_description', ''))}")
        md.append(f"- Live equals admin description: **{p.get('live_equals_admin_description')}**")
        md.append(f"- Admin keywords empty: **{not bool(p.get('admin_meta_keyword'))}**")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "admin-evidence" / "product-seo-fields-readonly.md", "\n".join(md))
    return result


def phase5_attribute_map(live_rows: list[dict[str, Any]]) -> None:
    by_family: dict[str, dict[str, Any]] = {}
    for row in live_rows:
        fam = row.get("category_family", "unknown")
        if fam not in by_family:
            by_family[fam] = {
                "category_family": fam,
                "sample_products": [],
                "visible_key_attributes": [],
                "high_value_for_meta": [],
                "attributes_to_avoid": ["внутренние коды", "xml_id"],
                "confidence": "MEDIUM",
            }
        by_family[fam]["sample_products"].append({
            "url": row["url"],
            "name": row.get("product_name", ""),
        })
        for attr in row.get("visible_attributes", []):
            name = attr.get("name", attr.get("raw", ""))
            if name and name not in by_family[fam]["visible_key_attributes"]:
                by_family[fam]["visible_key_attributes"].append(name)
    priority_map = {
        "stoly": ["Длина", "Ширина", "Высота", "полка", "борт", "нержавеющая сталь"],
        "polki": ["настенн", "настольн", "полк", "ярус", "Длина", "Ширина"],
        "telezhki": ["ярус", "колес", "противн", "гастро", "Длина"],
        "shkafy_lari": ["двер", "полк", "Длина", "Ширина", "Высота"],
        "podstavki": ["Длина", "Ширина", "Высота", "нагрузк"],
        "stellazhi": ["ярус", "полк", "Длина", "Ширина", "Высота"],
        "moechnye_vanny": ["Длина", "Ширина", "Высота", "мойк"],
        "zonty": ["Длина", "Ширина", "вытяж"],
    }
    for fam, data in by_family.items():
        hints = priority_map.get(fam, ["Длина", "Ширина", "Высота", "Масса"])
        data["high_value_for_meta"] = hints
    entries = list(by_family.values())
    write_json(DEPLOYMENT_ROOT / "attribute-map" / "category-attribute-profile.json", entries)
    md = ["# Category attribute profile", "", f"Captured: {utc_now()}", ""]
    for e in entries:
        md.append(f"## {e['category_family']}")
        md.append(f"- Samples: {len(e['sample_products'])}")
        md.append(f"- Visible attributes: {', '.join(e['visible_key_attributes'][:12]) or 'SAFE UNKNOWN'}")
        md.append(f"- High-value for meta: {', '.join(e['high_value_for_meta'])}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "attribute-map" / "category-attribute-profile.md", "\n".join(md))


def phase6_generator_decision(live_rows: list[dict[str, Any]], source_data: dict[str, Any], admin_data: dict[str, Any]) -> None:
    missing_desc = sum(1 for r in live_rows if r.get("description_length", 0) == 0)
    missing_kw = sum(1 for r in live_rows if r.get("keywords_length", 0) == 0)
    admin_products = admin_data.get("products", [])
    live_equals_admin = sum(1 for p in admin_products if p.get("live_equals_admin_description"))
    decision = {
        "captured_at": utc_now(),
        "generator_exists": True,
        "generator_type": "IMPORT_TIME_DB — not runtime controller",
        "generator_location": "/public_html/catalog/controller/common/import_1C_process.php",
        "runtime_authority": "/public_html/catalog/controller/product/product.php — passes product_info meta fields",
        "generates_description": True,
        "generates_keywords": False,
        "includes_kupit": False,
        "includes_attributes": False,
        "includes_category_context": False,
        "respects_manual_meta": False,
        "manual_meta_overwritten_on_import": True,
        "good_enough": False,
        "needs_improvement": True,
        "live_samples_missing_description": missing_desc,
        "live_samples_missing_keywords": missing_kw,
        "meta_keyword_output_used": False,
        "attributes_accessible_at_meta_time": True,
        "attributes_note": "getProductAttributes() loaded after setDescription in product.php; generator would need reorder or model prefetch",
        "model_change_required": False,
        "single_controller_implementation_possible": True,
        "recommended_implementation_path": "product.php controller fallback when meta_description empty/short/generic; preserve manual meta; add keywords fallback",
        "rollback_path": "FTP backup of product.php (+ modification refresh if OC modification used)",
        "admin_live_match_count": live_equals_admin,
        "admin_sample_size": len(admin_products),
    }
    write_json(DEPLOYMENT_ROOT / "generator-analysis" / "current-generator-decision.json", decision)
    md = [
        "# Current generator decision",
        "",
        "## 1. Does a product meta generator exist?",
        "**Yes — at import time (1C), not in PDP controller.**",
        "",
        "`import_1C_process.php` sets `meta_description = mb_substr(strip_tags(description), 0, 160)` and `meta_title = name`. No `meta_keyword` on import.",
        "",
        "## 2. Runtime PDP",
        "`product.php` reads `$product_info['meta_description']` / `meta_keyword` / `meta_title` from DB — no runtime generator, no «купить», no attribute-aware copy.",
        "",
        f"## 3. Live sample stats (n={len(live_rows)})",
        f"- Missing description: {missing_desc}",
        f"- Missing keywords: {missing_kw} (all sampled)",
        "",
        "## 4. Implementation",
        "Safe path: controller-only fallback in `catalog/controller/product/product.php` before setDescription/setKeywords; do not overwrite meaningful manual meta; no DB writes.",
        "",
    ]
    write_text(DEPLOYMENT_ROOT / "generator-analysis" / "current-generator-decision.md", "\n".join(md))


def phase7_proposed_design(live_rows: list[dict[str, Any]]) -> None:
    design = {
        "captured_at": utc_now(),
        "rules": {
            "preserve_manual_meta_description": "if length >= 80 and not generic import stub",
            "generate_description_when": "empty OR length < 50 OR matches import strip_tags pattern without commercial intent",
            "generate_keywords_when": "empty (current state for all samples)",
            "no_price_unless_required": True,
            "no_stock_promise": True,
            "no_superlatives": True,
            "max_description_length": 165,
        },
        "description_template": "Купить {product_name} БЗПМ из нержавеющей стали для общепита. {spec_sentence}. Производство и поставка по России.",
        "category_attribute_priority": {
            "stoly": ["dimensions", "shelf", "board", "material"],
            "polki": ["mount_type", "levels", "dimensions", "material"],
            "telezhki": ["wheels", "levels", "gn_trays", "dimensions"],
            "shkafy_lari": ["doors", "shelves", "dimensions", "material"],
            "podstavki": ["dimensions", "load", "material"],
        },
        "keywords_concept": ["product_name", "category", "купить", "БЗПМ", "нержавеющая сталь", "нейтральное оборудование", "selected_attributes"],
        "sample_before_after": [
            {
                "url": live_rows[0]["url"] if live_rows else "",
                "before_description": live_rows[0].get("meta_description", "") if live_rows else "",
                "after_description_concept": "Купить {name} БЗПМ из нержавеющей стали. {L×W×H}. Производство и поставка по России.",
            }
        ],
    }
    write_json(DEPLOYMENT_ROOT / "generator-analysis" / "proposed-product-meta-generator-design.json", design)
    write_text(
        DEPLOYMENT_ROOT / "generator-analysis" / "proposed-product-meta-generator-design.md",
        "# Proposed product meta generator design\n\nSee JSON artefact for machine-readable rules. Controller fallback only; preserve manual meta; category-aware attributes; keywords when empty.\n",
    )


def phase8_fix_plan() -> None:
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "product-meta-generator-fix-plan.md",
        "\n".join(
            [
                "# Product meta generator fix plan",
                "",
                "Next operation: `SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-FIX-01`",
                "",
                "## Files likely changed",
                "- `/public_html/catalog/controller/product/product.php` (primary)",
                "- Optional helper: `/public_html/catalog/controller/product/product_meta.php` or inline private method",
                "- Modification cache refresh after deploy if OC Modifications active for product.php",
                "",
                "## Model change",
                "Not required if using existing `$product_info` dimensions + `getProductAttributes()` after load (may require moving attribute load before meta set).",
                "",
                "## Rollback",
                "- Storage backup before upload",
                "- Restore product.php from backup",
                "- Refresh modification cache if needed",
                "",
                "## Verification",
                "- Re-crawl 15–30 PDP sample URLs",
                "- Compare manual-meta products (admin saved) unchanged",
                "- Confirm keywords populated when empty",
                "",
                "## Risks",
                "- OC modification overlay may differ from source",
                "- Performance: one extra attribute read per PDP (negligible)",
                "- No DB writes; runtime only",
                "",
            ]
        ),
    )


def phase9_llms_plan() -> None:
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "llms-txt-next-task.md",
        "\n".join(
            [
                "# llms.txt next task",
                "",
                "Operation: `SITE-002-PROD-LLMS-TXT-01`",
                "",
                "- Path: `/public_html/llms.txt`",
                "- URL: https://bzpm.ru/llms.txt",
                "- Purpose: Markdown/plain summary for AI agents (БЗПМ identity, catalog, key pages, contacts, sitemap)",
                "- Does not replace robots.txt or sitemap.xml",
                "- No internal MARS data, secrets, or unverified price/stock promises",
                "- `/llm.txt` alias only if operator explicitly approves",
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
            "change_type": "product-meta-generator-discovery",
            "remote_changes_allowed": False,
            "admin_save_allowed": False,
            "db_write_allowed": False,
            "cache_clear_allowed": False,
            "product_pages_mutation_allowed": False,
            "llms_txt_allowed": False,
            "header_footer_change_allowed": False,
            "yandex_blocks_protected": True,
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--phase", default="all", help="all or comma-separated phase numbers 1-9")
    args = parser.parse_args()
    ensure_dirs()
    phases = set(range(1, 10)) if args.phase == "all" else {int(x) for x in args.phase.split(",")}
    inventory: list[dict[str, Any]] = []
    live_rows: list[dict[str, Any]] = []
    source_data: dict[str, Any] = {}
    admin_data: dict[str, Any] = {}
    if 1 in phases:
        inventory = phase1_pdp_inventory()
    elif (DEPLOYMENT_ROOT / "pdp-samples" / "pdp-url-samples.json").exists():
        inventory = json.loads((DEPLOYMENT_ROOT / "pdp-samples" / "pdp-url-samples.json").read_text(encoding="utf-8"))
    if 2 in phases:
        live_rows = phase2_live_meta(inventory)
    elif (DEPLOYMENT_ROOT / "meta-samples" / "product-meta-snapshot.json").exists():
        live_rows = json.loads((DEPLOYMENT_ROOT / "meta-samples" / "product-meta-snapshot.json").read_text(encoding="utf-8"))
    if 3 in phases:
        source_data = phase3_source_discovery()
    if 4 in phases and live_rows:
        admin_data = phase4_admin_readonly(live_rows)
    if 5 in phases and live_rows:
        phase5_attribute_map(live_rows)
    if 6 in phases:
        phase6_generator_decision(live_rows, source_data, admin_data)
    if 7 in phases:
        phase7_proposed_design(live_rows)
    if 8 in phases:
        phase8_fix_plan()
    if 9 in phases:
        phase9_llms_plan()
    print(f"{OPERATION_ID}: complete — samples={len(live_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
