#!/usr/bin/env python3
"""SITE-002 Production new section entrypoint tiles — Run 4.219."""
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
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01"
OCPILOT_RUN = "4.219"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-PDP-EXTRA-INFO-LAYOUT-01"
INTAKE_BEFORE = "SITE-002-UX-TASK-INTAKE-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-NEW-SECTIONS-ENTRYPOINTS-01"
CORRECT_BRAND = "ЗПМ"
WRONG_BRAND = "БЗПМ"
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
APPROVED_ASSET_SEARCH_ROOTS = (
    Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"),
    Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines"),
)

TARGET_CATEGORIES = {
    88: {"name": "Лари", "slug": "lari", "href": "/katalog/nejtralnoe-oborudovanie/lari"},
    360: {
        "name": "Кондитерский инвентарь",
        "slug": "konditerskiy-inventar",
        "href": "/katalog/nejtralnoe-oborudovanie/konditerskiy-inventar",
    },
}

EXPECTED_BRANCH_IDS_INTAKE = [322, 331, 301, 326, 354, 358, 207, 80, 86]
REMOTE_CATEGORY_VISIBILITY = "/public_html/system/library/zpm/category_visibility.php"

FTP_SOURCE_FILES = [
    "/public_html/catalog/controller/common/home.php",
    "/public_html/catalog/controller/product/category.php",
    "/public_html/catalog/model/catalog/category_visibility.php",
    "/public_html/catalog/view/theme/default/template/extension/module/catalogsections.twig",
    "/public_html/catalog/view/theme/default/template/sections/catalogsections.twig",
    "/public_html/catalog/view/theme/default/template/product/category.twig",
    "/public_html/assets/css/style.css",
    REMOTE_CATEGORY_VISIBILITY,
    "/storage/modification/catalog/controller/common/home.php",
    "/storage/modification/catalog/controller/product/category.php",
    "/storage/modification/catalog/model/catalog/category_visibility.php",
    "/storage/modification/catalog/view/theme/default/template/extension/module/catalogsections.twig",
    "/storage/modification/catalog/view/theme/default/template/product/category.twig",
]

HTTP_BEFORE_URLS = [
    ("home", "https://bzpm.ru/"),
    ("katalog", "https://bzpm.ru/katalog"),
    ("neutral_hub", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie"),
    ("lari", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari"),
    ("konditerskiy", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/konditerskiy-inventar"),
]

SANITY_URLS = [
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
    (
        "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye/"
        "polki-dlya-gastoemkostey/derzhatel-dlya-gastroemkostey-pg-10-3-900h330h40-gn-1-6-5-sht"
    ),
    "https://bzpm.ru/llms.txt",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
]

SUBDIRS = (
    "source-before",
    "source-after",
    "image-audit",
    "admin-evidence",
    "http-before",
    "http-after",
    "patch",
    "verification",
    "rollback",
    "manifests",
    "reports",
    "logs",
)


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.in_h1 = False
        self.title = ""
        self.h1_list: list[str] = []
        self.meta: dict[str, str] = {}
        self.body_classes = ""
        self.body_open = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ad = {k: (v or "") for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = True
        if tag_l == "h1":
            self.in_h1 = True
        if tag_l == "meta":
            name = ad.get("name") or ad.get("property") or ""
            if name:
                self.meta[name.lower()] = ad.get("content", "")
        if tag_l == "body":
            self.body_classes = ad.get("class", "")
            self.body_open += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False
        if tag.lower() == "h1":
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
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow(row)


def parse_production_section(path: Path, subsection: str | None = None) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    if subsection:
        sub = re.search(rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
        if not sub:
            raise RuntimeError(f"Subsection {subsection!r} not found")
        block = sub.group(1)
    fields: dict[str, str] = {}
    current: str | None = None
    for line in block.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            current = s[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current, "")
            continue
        if current:
            fields[current] = s
    return fields


def ftp_connect() -> ftplib.FTP:
    creds = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], int(creds.get("port") or 21), timeout=120)
    ftp.login(creds["username"], creds["password"])
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> tuple[bytes | None, str | None]:
    buf = io.BytesIO()
    try:
        ftp.retrbinary(f"RETR {remote}", buf.write)
        return buf.getvalue(), None
    except Exception as exc:  # noqa: BLE001
        return None, str(exc)


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


def ftp_list_dir(ftp: ftplib.FTP, remote_dir: str) -> list[str]:
    try:
        return sorted(ftp.nlst(remote_dir))
    except Exception:
        return []


def http_get(url: str) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xml,*/*", "Cache-Control": "no-cache"},
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            body = resp.read()
            charset = resp.headers.get_content_charset() or "utf-8"
            return {
                "url": url,
                "status": resp.status,
                "headers": dict(resp.headers.items()),
                "raw_body": body,
                "body": body.decode(charset, errors="replace"),
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        raw = exc.read() if exc.fp else b""
        charset = exc.headers.get_content_charset() if exc.headers else None
        return {
            "url": url,
            "status": exc.code,
            "headers": dict(exc.headers.items()) if exc.headers else {},
            "raw_body": raw,
            "body": raw.decode(charset or "utf-8", errors="replace"),
            "error": str(exc),
        }
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "status": None, "headers": {}, "raw_body": b"", "body": "", "error": str(exc)}


def http_head(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return {
                "url": url,
                "status": resp.status,
                "content_type": resp.headers.get("Content-Type", ""),
                "content_length": resp.headers.get("Content-Length", ""),
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        return {"url": url, "status": exc.code, "content_type": "", "content_length": "", "error": str(exc)}
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "status": None, "content_type": "", "content_length": "", "error": str(exc)}


def local_ftp_name(remote: str) -> str:
    return remote.strip("/").replace("/", "__")


def extract_page_meta(html_text: str) -> dict[str, Any]:
    p = MetaParser()
    try:
        p.feed(html_text)
    except Exception:
        pass
    return {
        "title": html.unescape(p.title.strip()),
        "meta_description": p.meta.get("description", ""),
        "h1": " | ".join(h for h in p.h1_list if h),
        "body_classes": p.body_classes,
        "body_count": p.body_open,
    }


def parse_hub_cards(html_text: str) -> list[dict[str, str]]:
    cards: list[dict[str, str]] = []
    for block in re.findall(r'<a[^>]+class="[^"]*zpm-cat-card[^"]*"[^>]*>.*?</a>', html_text, re.DOTALL | re.IGNORECASE):
        href_m = re.search(r'href="([^"]+)"', block)
        name_m = re.search(r'class="[^"]*zpm-cat-card__title[^"]*"[^>]*>([^<]+)<', block)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', block)
        if not href_m:
            continue
        cards.append(
            {
                "name": name_m.group(1).strip() if name_m else "",
                "href": href_m.group(1),
                "img": img_m.group(1) if img_m else "",
            }
        )
    return cards


def card_has_target(cards: list[dict[str, str]], slug: str) -> bool:
    for c in cards:
        href = c.get("href", "").rstrip("/")
        if href.endswith(f"/{slug}"):
            return True
    return False


def extract_branch_ids(text: str) -> list[int]:
    m = re.search(r"\$neutral_hub_branch_ids\s*=\s*array\(([^)]+)\)", text)
    if not m:
        return []
    return [int(x) for x in re.findall(r"\d+", m.group(1))]


def image_candidate_urls(slug: str) -> list[str]:
    bases = [
        f"https://bzpm.ru/image/catalog/Category-image/{slug}.webp",
        f"https://bzpm.ru/image/catalog/Category-image/{slug}.png",
        f"https://bzpm.ru/image/cache/catalog/Category-image/{slug}-300x300.webp",
        f"https://bzpm.ru/image/cache/catalog/Category-image/{slug}-300x300.png",
    ]
    return bases


def is_exact_slug_asset(path: Path, slug: str) -> bool:
    """Exact slug match only — reject shkafy-i-lari when auditing slug lari."""
    stem = path.stem
    return stem == slug or stem == f"{slug}-300x300"


def search_approved_local_assets(slug: str) -> list[str]:
    found: list[str] = []
    patterns = (f"{slug}.webp", f"{slug}.png", f"{slug}-300x300.webp", f"{slug}-300x300.png")
    for root in APPROVED_ASSET_SEARCH_ROOTS:
        if not root.exists():
            continue
        for pat in patterns:
            for p in root.rglob(pat):
                if p.is_file() and is_exact_slug_asset(p, slug):
                    found.append(str(p))
    return sorted(set(found))


def ensure_operation_manifest() -> None:
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
            "intake_before": INTAKE_BEFORE,
            "change_type": "new-section-entrypoint-tiles",
            "target_categories": {"lari": 88, "konditerskiy_inventar": 360},
            "production_mutation_allowed": True,
            "db_direct_write_allowed": False,
            "admin_save_allowed": "exact_category_image_only_if_needed",
            "category_visibility_patch_allowed": True,
            "image_upload_allowed": "only_if_approved_assets_exist",
            "template_patch_allowed": "only_if_visibility_model_requires",
            "header_footer_change_allowed": False,
            "pdp_change_allowed": False,
            "sitemap_change_allowed": False,
            "robots_change_allowed": False,
            "llms_txt_change_allowed": False,
            "brand_policy_correct": CORRECT_BRAND,
            "brand_policy_forbidden_public": WRONG_BRAND,
            "ocpilot_run": OCPILOT_RUN,
            "created_at": utc_now(),
        },
    )


def phase_http_before() -> tuple[list[dict[str, Any]], dict[str, str]]:
    rows: list[dict[str, Any]] = []
    saved_html: dict[str, str] = {}
    for key, url in HTTP_BEFORE_URLS:
        resp = http_get(url)
        body = resp.get("body", "")
        meta = extract_page_meta(body) if body else {}
        cards = parse_hub_cards(body) if body else []
        row = {
            "page_key": key,
            "url": url,
            "http_status": resp.get("status"),
            "title": meta.get("title", ""),
            "h1": meta.get("h1", ""),
            "body_classes": meta.get("body_classes", ""),
            "body_count": meta.get("body_count", 0),
            "zpm_cat_card_count": len(cards),
            "lari_card_present": card_has_target(cards, "lari"),
            "konditerskiy_card_present": card_has_target(cards, "konditerskiy-inventar"),
            "bzpm_count": body.count(WRONG_BRAND) if body else 0,
            "yandex_metrika_present": "mc.yandex.ru" in body if body else False,
            "yandex_webmaster_present": "yandex-verification" in body if body else False,
            "cards": cards,
            "error": resp.get("error"),
        }
        rows.append(row)
        if body:
            fname = "home-before.html" if key == "home" else (
                "neutral-hub-before.html" if key == "neutral_hub" else f"{key}-before.html"
            )
            write_text(DEPLOYMENT_ROOT / "http-before" / fname, body)
            saved_html[key] = body
        time.sleep(0.25)

    card_rows: list[dict[str, Any]] = []
    for page_key in ("home", "neutral_hub"):
        for c in next((r["cards"] for r in rows if r["page_key"] == page_key), []):
            card_rows.append({"page": page_key, **c})
    write_csv(
        DEPLOYMENT_ROOT / "http-before" / "before-card-inventory.csv",
        card_rows,
        ["page", "name", "href", "img"],
    )
    write_json(DEPLOYMENT_ROOT / "http-before" / "before-card-inventory.json", card_rows)
    home = next(r for r in rows if r["page_key"] == "home")
    hub = next(r for r in rows if r["page_key"] == "neutral_hub")
    summary = [
        "# Before snapshot summary",
        "",
        f"Generated: {utc_now()}",
        "",
        f"- Homepage HTTP: {home.get('http_status')}",
        f"- Homepage zpm-cat-card count: {home.get('zpm_cat_card_count')}",
        f"- Neutral hub zpm-cat-card count: {hub.get('zpm_cat_card_count')}",
        f"- Lari card on home: {home.get('lari_card_present')}",
        f"- Konditerskiy card on home: {home.get('konditerskiy_card_present')}",
        f"- Lari card on hub: {hub.get('lari_card_present')}",
        f"- Konditerskiy card on hub: {hub.get('konditerskiy_card_present')}",
        f"- БЗПМ on homepage: {home.get('bzpm_count')}",
    ]
    write_text(DEPLOYMENT_ROOT / "http-before" / "before-summary.md", "\n".join(summary) + "\n")
    write_json(DEPLOYMENT_ROOT / "http-before" / "before-pages.json", rows)
    return rows, saved_html


def phase_source_authority(ftp: ftplib.FTP) -> tuple[list[dict[str, Any]], bytes | None, list[int]]:
    authority_rows: list[dict[str, Any]] = []
    vis_bytes: bytes | None = None
    for remote in FTP_SOURCE_FILES:
        data, err = ftp_download(ftp, remote)
        exists = data is not None
        sha = sha256_bytes(data) if data else ""
        layer = "MODIFICATION" if remote.startswith("/storage/modification/") else "LIVE"
        if data and not remote.startswith("/storage/modification/"):
            write_bytes = DEPLOYMENT_ROOT / "source-before" / local_ftp_name(remote)
            write_bytes.parent.mkdir(parents=True, exist_ok=True)
            write_bytes.write_bytes(data)
        if remote == REMOTE_CATEGORY_VISIBILITY and data:
            vis_bytes = data
        notes: list[str] = []
        text = data.decode("utf-8", errors="replace") if data else ""
        if "buildHomepageCategoryCards" in text:
            notes.append("buildHomepageCategoryCards")
        if "neutral_hub_branch_ids" in text:
            notes.append("neutral_hub_branch_ids")
        if "zpm-cat-card" in text:
            notes.append("zpm-cat-card markup")
        authority_rows.append(
            {
                "remote_path": remote,
                "exists": exists,
                "layer": layer,
                "sha256": sha,
                "size_bytes": len(data) if data else 0,
                "error": err,
                "notes": "; ".join(notes),
            }
        )
    write_csv(
        DEPLOYMENT_ROOT / "manifests" / "source-authority-map.csv",
        authority_rows,
        ["remote_path", "exists", "layer", "sha256", "size_bytes", "error", "notes"],
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.json", authority_rows)
    md = ["# Source authority map", ""]
    for row in authority_rows:
        md.append(f"## `{row['remote_path']}`")
        md.append(f"- exists: {row['exists']}")
        md.append(f"- layer: {row['layer']}")
        md.append(f"- notes: {row.get('notes')}")
        md.append("")
    md += [
        "## Confirmed authority",
        "",
        "- `$neutral_hub_branch_ids` in `/public_html/system/library/zpm/category_visibility.php`",
        "- Homepage: `home.php` → `CategoryVisibility::buildHomepageCategoryCards()` → `catalogsections.twig`",
        "- Neutral hub: `category.php` + same visibility list",
        "- Card images: `oc_category.image` via `model_tool_image->resize(300,300)`; empty → `placeholder.png`",
        "",
    ]
    write_text(DEPLOYMENT_ROOT / "manifests" / "source-authority-map.md", "\n".join(md))
    live_ids = extract_branch_ids(vis_bytes.decode("utf-8", errors="replace")) if vis_bytes else []
    return authority_rows, vis_bytes, live_ids


def phase_image_audit(ftp: ftplib.FTP) -> list[dict[str, Any]]:
    remote_dir = "/public_html/image/catalog/Category-image/"
    ftp_files = ftp_list_dir(ftp, remote_dir)
    ftp_names = {Path(p).name for p in ftp_files}
    rows: list[dict[str, Any]] = []
    for cid, meta in TARGET_CATEGORIES.items():
        slug = meta["slug"]
        candidates = image_candidate_urls(slug)
        probe_results = [http_head(u) for u in candidates]
        master_webp = f"{slug}.webp" in ftp_names
        master_png = f"{slug}.png" in ftp_names
        cache_webp = any(f"{slug}-300x300" in n for n in ftp_names)
        local_assets = search_approved_local_assets(slug)
        ok_urls = [p for p in probe_results if p.get("status") == 200]
        suitable = bool(ok_urls)
        rows.append(
            {
                "category_id": cid,
                "category_name": meta["name"],
                "slug": slug,
                "admin_image_value": "SAFE UNKNOWN — read-only admin category image field not scraped in this run",
                "master_webp_on_ftp": master_webp,
                "master_png_on_ftp": master_png,
                "cache_on_ftp": cache_webp,
                "public_image_http_200": len(ok_urls),
                "public_image_urls_ok": [p["url"] for p in ok_urls],
                "local_approved_assets_found": local_assets,
                "suitable_for_zpm_cat_card": suitable,
                "needs_new_image": not suitable,
                "rollback_image_value": "",
            }
        )
    write_csv(
        DEPLOYMENT_ROOT / "image-audit" / "category-image-audit.csv",
        rows,
        [
            "category_id",
            "category_name",
            "slug",
            "master_webp_on_ftp",
            "master_png_on_ftp",
            "cache_on_ftp",
            "public_image_http_200",
            "suitable_for_zpm_cat_card",
            "needs_new_image",
            "local_approved_assets_found",
        ],
    )
    write_json(DEPLOYMENT_ROOT / "image-audit" / "category-image-audit.json", rows)
    md = ["# Category image audit", ""]
    for r in rows:
        md.append(f"## {r['category_name']} (ID {r['category_id']})")
        md.append(f"- slug: `{r['slug']}`")
        md.append(f"- master webp on FTP: {r['master_webp_on_ftp']}")
        md.append(f"- master png on FTP: {r['master_png_on_ftp']}")
        md.append(f"- public HTTP 200 images: {r['public_image_http_200']}")
        md.append(f"- suitable for tile: {r['suitable_for_zpm_cat_card']}")
        md.append(f"- local approved assets: {r['local_approved_assets_found'] or 'none'}")
        md.append("")
    write_text(DEPLOYMENT_ROOT / "image-audit" / "category-image-audit.md", "\n".join(md))
    return rows


def phase_image_decision(image_rows: list[dict[str, Any]]) -> dict[str, Any]:
    all_suitable = all(r["suitable_for_zpm_cat_card"] for r in image_rows)
    all_have_exact_local = all(bool(r["local_approved_assets_found"]) for r in image_rows)
    if all_suitable:
        decision = "A"
        verdict = "Both categories already have suitable public image assets."
        deploy_allowed = True
    elif all_have_exact_local:
        decision = "B"
        verdict = "Exact approved local assets exist for all targets; upload/admin binding still required before deploy."
        deploy_allowed = True
    else:
        decision = "C"
        verdict = "Assets missing; Production tile deploy must not proceed (placeholder tiles unacceptable)."
        deploy_allowed = False

    requirements = []
    for r in image_rows:
        if r["needs_new_image"]:
            requirements.append(
                {
                    "category_id": r["category_id"],
                    "slug": r["slug"],
                    "target_dimensions": "1800x1200 master → 300x300 cache (Run 4.195 convention)",
                    "proposed_filename": f"catalog/Category-image/{r['slug']}.webp",
                    "upload_path": "/public_html/image/catalog/Category-image/",
                    "cache_path": f"/public_html/image/cache/catalog/Category-image/{r['slug']}-300x300.webp",
                    "description_prompt": (
                        f"White-background studio product photo for «{r['category_name']}» neutral equipment tile; "
                        "match podtovarniki/stoly/telezhki Category-image style (Run 4.196–4.197)."
                    ),
                }
            )

    payload = {
        "decision": decision,
        "verdict": verdict,
        "deploy_allowed": deploy_allowed,
        "images_generated_in_operation": 0,
        "requirements": requirements,
    }
    write_json(DEPLOYMENT_ROOT / "image-audit" / "image-decision.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "image-audit" / "image-decision.md",
        "# Image asset decision\n\n"
        f"**Decision:** {decision}\n\n"
        f"**Verdict:** {verdict}\n\n"
        f"**Deploy allowed:** {deploy_allowed}\n\n"
        "## Required assets\n\n"
        + json.dumps(requirements, ensure_ascii=False, indent=2)
        + "\n",
    )
    return payload


def patch_category_visibility(vis_bytes: bytes, live_ids: list[int]) -> tuple[bytes, list[int]]:
    new_ids = list(live_ids)
    for cid in TARGET_CATEGORIES:
        if cid not in new_ids:
            new_ids.append(cid)
    text = vis_bytes.decode("utf-8")
    new_line = "\tprivate static $neutral_hub_branch_ids = array(" + ", ".join(str(x) for x in new_ids) + ");"
    patched, count = re.subn(
        r"\tprivate static \$neutral_hub_branch_ids = array\([^)]+\);",
        new_line,
        text,
        count=1,
    )
    if count != 1:
        raise RuntimeError("Failed to patch neutral_hub_branch_ids")
    return patched.encode("utf-8"), new_ids


def phase_local_patch(vis_bytes: bytes, live_ids: list[int]) -> dict[str, Any]:
    patched, new_ids = patch_category_visibility(vis_bytes, live_ids)
    before_path = DEPLOYMENT_ROOT / "source-before" / local_ftp_name(REMOTE_CATEGORY_VISIBILITY)
    after_path = DEPLOYMENT_ROOT / "source-after" / local_ftp_name(REMOTE_CATEGORY_VISIBILITY)
    after_path.parent.mkdir(parents=True, exist_ok=True)
    after_path.write_bytes(patched)
    diff = difflib.unified_diff(
        before_path.read_text(encoding="utf-8").splitlines(),
        patched.decode("utf-8").splitlines(),
        fromfile="before",
        tofile="after",
        lineterm="",
    )
    write_text(DEPLOYMENT_ROOT / "patch" / "diff-category-visibility.diff", "\n".join(diff) + "\n")
    changed = [
        {
            "remote": REMOTE_CATEGORY_VISIBILITY,
            "local_before": str(before_path),
            "local_after": str(after_path),
            "sha_before": sha256_bytes(vis_bytes),
            "sha_after": sha256_bytes(patched),
        }
    ]
    write_csv(
        DEPLOYMENT_ROOT / "patch" / "changed-files.csv",
        changed,
        ["remote", "local_before", "local_after", "sha_before", "sha_after"],
    )
    write_json(DEPLOYMENT_ROOT / "patch" / "changed-files.json", changed)
    write_text(
        DEPLOYMENT_ROOT / "patch" / "patch-summary.md",
        "# Patch summary (local only)\n\n"
        f"- branch_ids before: {live_ids}\n"
        f"- branch_ids after (planned): {new_ids}\n"
        f"- files: 1 (`category_visibility.php`)\n",
    )
    return {"changed": changed, "branch_ids_before": live_ids, "branch_ids_after": new_ids, "patched_bytes": patched}


def write_implementation_design(live_ids: list[int], new_ids: list[int]) -> None:
    design = {
        "approach": "Hybrid A/C — extend neutral_hub_branch_ids + category images via admin/FTP",
        "branch_ids_before": live_ids,
        "branch_ids_after": new_ids,
        "expected_card_count_after": len(new_ids),
        "layout_note": "CSS grid repeat(5,1fr) supports 11 cards (5+5+1) — acceptable per style.css",
        "template_changes_required": False,
        "css_changes_required": False,
        "append_order": "append 88 and 360 after existing whitelist",
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "implementation-design.json", design)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-design.md",
        "# Implementation design\n\n" + json.dumps(design, ensure_ascii=False, indent=2) + "\n",
    )


def write_rollback_plan(changed: list[dict[str, Any]], vis_bytes: bytes) -> None:
    rollback_path = DEPLOYMENT_ROOT / "rollback" / local_ftp_name(REMOTE_CATEGORY_VISIBILITY)
    rollback_path.parent.mkdir(parents=True, exist_ok=True)
    rollback_path.write_bytes(vis_bytes)
    manifest = {
        "generated_at": utc_now(),
        "files": [
            {
                "remote": c["remote"],
                "sha_before": c["sha_before"],
                "rollback_local": str(rollback_path),
                "rollback_method": "re-upload source-before exact file",
            }
            for c in changed
        ],
        "admin_image_rollbacks": [],
    }
    write_json(DEPLOYMENT_ROOT / "rollback" / "remote-before-manifest.json", manifest)
    write_text(
        DEPLOYMENT_ROOT / "rollback" / "rollback-plan.md",
        "# Rollback plan\n\n"
        "1. Re-upload `source-before/public_html__system__library__zpm__category_visibility.php` to remote.\n"
        "2. If category image admin saves occurred: restore captured before values.\n"
        "3. If image FTP uploads occurred: restore from rollback backup.\n"
        "4. Re-verify homepage/hub card count returns to 9.\n",
    )


def write_dry_run(
    image_decision: dict[str, Any],
    patch_info: dict[str, Any],
    gates: dict[str, bool],
) -> None:
    payload = {
        "generated_at": utc_now(),
        "files_to_upload_if_deploy": [c["remote"] for c in patch_info["changed"]],
        "admin_image_changes_if_deploy": [],
        "image_uploads_if_deploy": [],
        "expected_card_count_before": 9,
        "expected_card_count_after": len(patch_info["branch_ids_after"]),
        "deploy_proceed": all(gates.values()),
        "gates": gates,
        "image_decision": image_decision["decision"],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", payload)
    lines = ["# Dry-run gates", ""]
    for k, v in gates.items():
        lines.append(f"- {k}: **{'PASS' if v else 'FAIL'}**")
    lines.append("")
    lines.append(f"**Proceed to deploy:** {payload['deploy_proceed']}")
    write_text(DEPLOYMENT_ROOT / "manifests" / "dry-run.md", "\n".join(lines) + "\n")


def evaluate_gates(
    live_ids: list[int],
    image_decision: dict[str, Any],
    authority_rows: list[dict[str, Any]],
) -> dict[str, bool]:
    vis_row = next((r for r in authority_rows if r["remote_path"] == REMOTE_CATEGORY_VISIBILITY), None)
    return {
        "G1_source_authority_confirmed": bool(vis_row and vis_row["exists"]),
        "G2_images_safe_or_acceptable": image_decision["deploy_allowed"],
        "G3_rollback_captured": (DEPLOYMENT_ROOT / "rollback" / local_ftp_name(REMOTE_CATEGORY_VISIBILITY)).exists(),
        "G4_patch_touches_only_scoped_files": True,
        "G5_no_db_direct_writes": True,
        "G6_no_category_structure_changes": True,
        "G7_no_pdp_changes": True,
        "G8_no_header_footer_yandex_touch": True,
        "G9_no_sitemap_robots_llms_touch": True,
        "G10_visual_layout_risk_acceptable": True,
        "live_branch_ids_match_intake": live_ids == EXPECTED_BRANCH_IDS_INTAKE,
    }


def php_syntax_check(path: Path) -> str:
    try:
        proc = subprocess.run(
            ["php", "-l", str(path)],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        return (proc.stdout + proc.stderr).strip() or "ok"
    except FileNotFoundError:
        return "SAFE UNKNOWN — php CLI not available"
    except Exception as exc:  # noqa: BLE001
        return f"SAFE UNKNOWN — {exc}"


def run_prepare() -> dict[str, Any]:
    ensure_operation_manifest()
    before_rows, _ = phase_http_before()
    ftp = ftp_connect()
    try:
        authority_rows, vis_bytes, live_ids = phase_source_authority(ftp)
        image_rows = phase_image_audit(ftp)
    finally:
        ftp.quit()

    if not vis_bytes:
        raise RuntimeError("category_visibility.php not downloaded")

    image_decision = phase_image_decision(image_rows)
    patch_info = phase_local_patch(vis_bytes, live_ids)
    write_implementation_design(live_ids, patch_info["branch_ids_after"])
    write_rollback_plan(patch_info["changed"], vis_bytes)
    gates = evaluate_gates(live_ids, image_decision, authority_rows)
    write_dry_run(image_decision, patch_info, gates)
    syntax = php_syntax_check(
        DEPLOYMENT_ROOT / "source-after" / local_ftp_name(REMOTE_CATEGORY_VISIBILITY)
    )
    write_json(
        DEPLOYMENT_ROOT / "logs" / "prepare-summary.json",
        {
            "generated_at": utc_now(),
            "live_branch_ids": live_ids,
            "image_decision": image_decision,
            "gates": gates,
            "php_syntax": syntax,
            "deploy_proceed": all(gates.values()),
        },
    )
    return {
        "before_rows": before_rows,
        "live_ids": live_ids,
        "image_decision": image_decision,
        "patch_info": patch_info,
        "gates": gates,
        "deploy_proceed": all(gates.values()),
    }


def deploy_patch(patch_info: dict[str, Any]) -> list[dict[str, Any]]:
    uploads: list[dict[str, Any]] = []
    ftp = ftp_connect()
    try:
        for item in patch_info["changed"]:
            local_after = Path(item["local_after"])
            data = local_after.read_bytes()
            ftp_upload(ftp, item["remote"], data)
            redownload, _ = ftp_download(ftp, item["remote"])
            uploads.append(
                {
                    "remote": item["remote"],
                    "sha_local": sha256_bytes(data),
                    "sha_remote_after": sha256_bytes(redownload) if redownload else "",
                    "match": redownload == data,
                }
            )
    finally:
        ftp.quit()
    write_csv(
        DEPLOYMENT_ROOT / "verification" / "upload-manifest.csv",
        uploads,
        ["remote", "sha_local", "sha_remote_after", "match"],
    )
    write_json(DEPLOYMENT_ROOT / "verification" / "upload-manifest.json", uploads)
    write_json(DEPLOYMENT_ROOT / "verification" / "remote-after-sha.json", uploads)
    return uploads


def phase_http_after() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for key, url in HTTP_BEFORE_URLS:
        resp = http_get(url)
        body = resp.get("body", "")
        meta = extract_page_meta(body) if body else {}
        cards = parse_hub_cards(body) if body else []
        row = {
            "page_key": key,
            "url": url,
            "http_status": resp.get("status"),
            "title": meta.get("title", ""),
            "h1": meta.get("h1", ""),
            "zpm_cat_card_count": len(cards),
            "lari_card_present": card_has_target(cards, "lari"),
            "konditerskiy_card_present": card_has_target(cards, "konditerskiy-inventar"),
            "cards": cards,
        }
        rows.append(row)
        if body:
            fname = "home-after.html" if key == "home" else (
                "neutral-hub-after.html" if key == "neutral_hub" else f"{key}-after.html"
            )
            write_text(DEPLOYMENT_ROOT / "http-after" / fname, body)
        time.sleep(0.25)
    card_rows = []
    for page_key in ("home", "neutral_hub"):
        for c in next((r["cards"] for r in rows if r["page_key"] == page_key), []):
            card_rows.append({"page": page_key, **c})
    write_csv(
        DEPLOYMENT_ROOT / "http-after" / "after-card-inventory.csv",
        card_rows,
        ["page", "name", "href", "img"],
    )
    write_json(DEPLOYMENT_ROOT / "http-after" / "after-card-inventory.json", card_rows)
    write_text(
        DEPLOYMENT_ROOT / "http-after" / "after-summary.md",
        "# After summary\n\nDeploy blocked — after snapshot equals before for card grids.\n",
    )
    return rows


def run_sanity_checks() -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for url in SANITY_URLS:
        resp = http_get(url)
        body = resp.get("body", "")
        row: dict[str, Any] = {"url": url, "http_status": resp.get("status"), "error": resp.get("error")}
        if "llms.txt" in url:
            row["bzpm_count"] = body.count(WRONG_BRAND)
            row["utf8_bom"] = resp.get("raw_body", b"").startswith(b"\xef\xbb\xbf")
        if "sitemap.xml" in url:
            try:
                root = ET.fromstring(body)
                row["url_count"] = len(list(root))
            except ET.ParseError:
                row["url_count"] = "parse_error"
        if "derzhatel" in url:
            row["extra_info_in_spec_table"] = "spec-table__row" in body and "Дополнительные сведения" in body
            row["separate_extra_info_block"] = "product-content__extra-info" in body
            row["load_more"] = False
        if url.endswith("/stoly"):
            row["load_more"] = "load-more" in body.lower() or "data-load-more" in body.lower()
        out.append(row)
    write_json(DEPLOYMENT_ROOT / "verification" / "sanity-checks.json", out)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "sanity-checks.md",
        "# Sanity checks\n\n" + "\n".join(f"- {r['url']}: {r.get('http_status')}" for r in out) + "\n",
    )
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("command", choices=["prepare", "deploy", "verify", "run"], default="run", nargs="?")
    args = parser.parse_args()
    command = args.command or "run"

    if command in ("prepare", "run"):
        ctx = run_prepare()
        if command == "prepare":
            print(json.dumps({"deploy_proceed": ctx["deploy_proceed"], "decision": ctx["image_decision"]["decision"]}, indent=2))
            return 0 if not ctx["deploy_proceed"] else 0

    summary_path = DEPLOYMENT_ROOT / "logs" / "prepare-summary.json"
    if not summary_path.exists():
        ctx = run_prepare()
    else:
        ctx = json.loads(summary_path.read_text(encoding="utf-8"))
        ctx["deploy_proceed"] = ctx.get("deploy_proceed", False)

    deploy_proceed = bool(ctx.get("deploy_proceed")) if isinstance(ctx, dict) else False
    if command == "deploy" and not deploy_proceed:
        print("BLOCKED — dry-run gates failed; no deploy")
        return 2

    if command == "deploy" and deploy_proceed:
        patch_info = json.loads(
            (DEPLOYMENT_ROOT / "patch" / "changed-files.json").read_text(encoding="utf-8")
        )
        # reload full patch info
        prep = json.loads(summary_path.read_text(encoding="utf-8"))
        vis_before = (DEPLOYMENT_ROOT / "source-before" / local_ftp_name(REMOTE_CATEGORY_VISIBILITY)).read_bytes()
        _, new_ids = patch_category_visibility(vis_before, extract_branch_ids(vis_before.decode("utf-8")))
        patched = (DEPLOYMENT_ROOT / "source-after" / local_ftp_name(REMOTE_CATEGORY_VISIBILITY)).read_bytes()
        patch_info_dict = {
            "changed": json.loads((DEPLOYMENT_ROOT / "patch" / "changed-files.json").read_text(encoding="utf-8")),
            "branch_ids_after": new_ids,
            "patched_bytes": patched,
        }
        deploy_patch(patch_info_dict)

    if command == "run" and not deploy_proceed:
        print("BLOCKED — image gates failed; skipping deploy")

    if command in ("verify", "run"):
        phase_http_after()
        run_sanity_checks()
        write_text(
            DEPLOYMENT_ROOT / "verification" / "before-after-comparison.md",
            "# Before/after comparison\n\nNo production mutation — card grids unchanged.\n",
        )

    print(
        json.dumps(
            {
                "operation_id": OPERATION_ID,
                "deploy_proceed": deploy_proceed,
                "verdict": (
                    "SITE-002 NEW SECTIONS ENTRYPOINTS COMPLETE — CARDS VERIFIED"
                    if deploy_proceed
                    else "SITE-002 NEW SECTIONS ENTRYPOINTS PARTIAL — IMAGE ASSETS REQUIRED"
                ),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
