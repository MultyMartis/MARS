#!/usr/bin/env python3
"""SITE-002 neutral parent categories rollout — controlled production deploy."""
from __future__ import annotations

import argparse
import ftplib
import hashlib
import io
import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-NEUTRAL-PARENT-CATEGORIES-ROLLOUT-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-CRON-SCHEDULED-RUN-01"
SEO_BASELINE_BEFORE = "SITE-002-STABLE-PROD-SITEMAP-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-NEUTRAL-PARENT-CATEGORIES-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEUTRAL-PARENT-CATEGORIES-ROLLOUT-01"
)
STORAGE_BASELINE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-NEUTRAL-PARENT-CATEGORIES-01"
)
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

KNOWN_BRANCH_IDS = [301, 80, 322, 207, 326]
NEW_BRANCH_IDS = [331, 354, 358, 86]  # polki-nastennye, telezhki-shpilki, shkafy-i-lari, stellazhi
ROLLOUT_BRANCH_IDS = [322, 331, 301, 326, 354, 358, 207, 80, 86]  # megamenu/catalog live order
CATEGORY_IMAGE_MAP = {
    86: "catalog/Category-image/stellazhi.webp",
    331: "catalog/Category-image/polki-nastennye-i-nastolnye.webp",
    358: "catalog/Category-image/shkafy-i-lari.webp",
    354: "catalog/Category-image/telezhki-shpilki-i-protivni.webp",
}
NEUTRAL_HUB_ID = 79

REMOTE_CATEGORY_VISIBILITY = "/public_html/system/library/zpm/category_visibility.php"

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "verification",
    "screenshots",
    "category-inventory",
    "image-reference",
    "image-generation",
    "image-final",
    "admin-evidence",
    "html-before",
    "html-after",
    "manifests",
    "logs",
    "verification/pre-upload",
)

FETCH_URLS = (
    ("home", "https://bzpm.ru/"),
    ("katalog", "https://bzpm.ru/katalog"),
    ("katalog_slash", "https://bzpm.ru/katalog/"),
    ("neutral_hub", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie"),
)


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


def parse_production_secrets(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found in secrets file")
    block = match.group(1)
    ftp_match = re.search(r"^### FTP / SFTP\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
    if not ftp_match:
        raise RuntimeError("PRODUCTION FTP / SFTP subsection not found")
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in ftp_match.group(1).splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.endswith(":"):
            current_key = stripped[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current_key, "")
            continue
        if current_key:
            fields[current_key] = stripped
    required = ("host", "port", "username", "password")
    missing = [key for key in required if not fields.get(key) or fields.get(key) == "SAFE UNKNOWN"]
    if missing:
        raise RuntimeError("Missing PRODUCTION FTP fields: " + ", ".join(missing))
    return fields


def http_get(url: str, timeout: int = 45) -> tuple[int, str, dict[str, str]]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read().decode("utf-8", errors="replace")
        headers = {k.lower(): v for k, v in resp.headers.items()}
        return resp.status, body, headers


def ftp_connect(secrets: dict[str, str]) -> ftplib.FTP:
    ftp = ftplib.FTP()
    ftp.connect(secrets["host"], int(secrets.get("port") or 21), timeout=180)
    ftp.login(secrets["username"], secrets["password"])
    ftp.set_pasv(True)
    return ftp


def ftp_download(ftp: ftplib.FTP, remote_path: str) -> bytes:
    buf = io.BytesIO()
    ftp.retrbinary(f"RETR {remote_path}", buf.write)
    return buf.getvalue()


def ftp_upload(ftp: ftplib.FTP, remote_path: str, data: bytes) -> None:
    buf = io.BytesIO(data)
    ftp.storbinary(f"STOR {remote_path}", buf)


def ftp_ensure_dir(ftp: ftplib.FTP, remote_dir: str) -> None:
    parts = [p for p in remote_dir.strip("/").split("/") if p]
    path = ""
    for part in parts:
        path += "/" + part
        try:
            ftp.mkd(path)
        except ftplib.error_perm:
            pass


def extract_branch_ids_from_visibility_php(text: str) -> list[int]:
    m = re.search(r"\$neutral_hub_branch_ids\s*=\s*array\(([^)]+)\)", text)
    if not m:
        return []
    return [int(x) for x in re.findall(r"\d+", m.group(1))]


def parse_hub_cards(html: str) -> list[dict[str, Any]]:
    cards: list[dict[str, Any]] = []
    for block in re.findall(r'<a[^>]+class="[^"]*zpm-cat-card[^"]*"[^>]*>.*?</a>', html, re.DOTALL | re.IGNORECASE):
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


def parse_megamenu_neutral_children(html: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    neutral_block = re.search(
        r'nejtralnoe-oborudovanie[\s\S]{0,8000}?(?=<li class="menu-item"|</ul>)',
        html,
        re.IGNORECASE,
    )
    if not neutral_block:
        return items
    for href, name in re.findall(
        r'href="(/katalog/nejtralnoe-oborudovanie/[^"#?]+)"[^>]*>([^<]+)<',
        neutral_block.group(0),
    ):
        slug = href.rstrip("/").split("/")[-1]
        if slug == "nejtralnoe-oborudovanie":
            continue
        items.append({"name": name.strip(), "href": href, "slug": slug})
    return items


def sitemap_neutral_parent_slugs(xml_text: str) -> list[str]:
    slugs: set[str] = set()
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return []
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    for loc in root.findall(".//sm:loc", ns) if root.tag.endswith("urlset") else []:
        if loc.text and "/katalog/nejtralnoe-oborudovanie/" in loc.text:
            path = loc.text.split("bzpm.ru", 1)[-1].split("?")[0].strip("/")
            parts = path.split("/")
            if len(parts) >= 3 and parts[0] == "katalog" and parts[1] == "nejtralnoe-oborudovanie":
                slugs.add(parts[2])
    if not slugs:
        for loc in root.iter():
            if loc.tag.endswith("loc") and loc.text and "/katalog/nejtralnoe-oborudovanie/" in loc.text:
                path = loc.text.split("bzpm.ru", 1)[-1].split("?")[0].strip("/")
                parts = path.split("/")
                if len(parts) >= 3 and parts[0] == "katalog" and parts[1] == "nejtralnoe-oborudovanie":
                    slugs.add(parts[2])
    return sorted(slugs)


def init_storage() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "baseline_before": BASELINE_BEFORE,
        "seo_baseline_before": SEO_BASELINE_BEFORE,
        "change_type": "neutral-parent-category-rollout",
        "image_generation_mode": "composer_only_no_api",
        "product_pdp_change_allowed": False,
        "seo_meta_change_allowed": False,
        "robots_change_allowed": False,
        "sitemap_change_allowed": False,
        "header_footer_change_allowed": False,
        "yandex_blocks_protected": True,
        "cron_change_allowed": False,
        "import_execution_allowed": False,
        "mail_change_allowed": False,
        "db_direct_write_allowed": False,
        "admin_save_allowed": "exact_category_fields_only",
        "created_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)


def phase_discover() -> dict[str, Any]:
    init_storage()
    secrets = parse_production_secrets(SECRETS_PATH)
    pages: dict[str, Any] = {}
    for name, url in FETCH_URLS:
        status, body, headers = http_get(url)
        write_text(DEPLOYMENT_ROOT / "html-before" / f"{name}.html", body)
        pages[name] = {"url": url, "status": status, "body_len": len(body), "headers": headers}

    _, sitemap_body, _ = http_get("https://bzpm.ru/sitemap.xml")
    write_text(DEPLOYMENT_ROOT / "html-before" / "sitemap.xml", sitemap_body)
    sitemap_slugs = sitemap_neutral_parent_slugs(sitemap_body)

    home_cards = parse_hub_cards(pages["home"]["body"] if "body" in pages["home"] else "")
    # re-parse from saved html
    home_html = (DEPLOYMENT_ROOT / "html-before" / "home.html").read_text(encoding="utf-8")
    hub_html = (DEPLOYMENT_ROOT / "html-before" / "neutral_hub.html").read_text(encoding="utf-8")
    home_cards = parse_hub_cards(home_html)
    hub_cards = parse_hub_cards(hub_html)
    megamenu_children = parse_megamenu_neutral_children(home_html)

    ftp = ftp_connect(secrets)
    try:
        vis_bytes = ftp_download(ftp, REMOTE_CATEGORY_VISIBILITY)
    finally:
        ftp.quit()

    vis_text = vis_bytes.decode("utf-8", errors="replace")
    write_bytes = DEPLOYMENT_ROOT / "backup" / "category_visibility.php"
    write_bytes.parent.mkdir(parents=True, exist_ok=True)
    write_bytes.write_bytes(vis_bytes)
    live_branch_ids = extract_branch_ids_from_visibility_php(vis_text)

    live_home_hrefs = {c["href"].rstrip("/") for c in home_cards}
    live_hub_hrefs = {c["href"].rstrip("/") for c in hub_cards}
    megamenu_hrefs = {c["href"].rstrip("/") for c in megamenu_children}

    # Probe each sitemap slug for HTTP 200 and title
    slug_probe: list[dict[str, Any]] = []
    for slug in sitemap_slugs:
        url = f"https://bzpm.ru/katalog/nejtralnoe-oborudovanie/{slug}"
        try:
            st, body, _ = http_get(url)
            h1 = ""
            m = re.search(r"<h1[^>]*>([^<]+)</h1>", body, re.IGNORECASE)
            if m:
                h1 = m.group(1).strip()
            on_home = url.rstrip("/") in live_home_hrefs
            on_hub = url.rstrip("/") in live_hub_hrefs
            in_megamenu = url.rstrip("/") in megamenu_hrefs
            in_live_ids = False  # resolved later if we map slug->id
            slug_probe.append(
                {
                    "slug": slug,
                    "url": url,
                    "http_status": st,
                    "h1": h1,
                    "on_homepage": on_home,
                    "on_neutral_hub": on_hub,
                    "in_megamenu": in_megamenu,
                }
            )
        except Exception as exc:
            slug_probe.append({"slug": slug, "url": url, "error": str(exc)})

    # New = in sitemap/megamenu with products but not in live branch ids / not on tiles
    known_slug_set = set()
    for c in hub_cards:
        known_slug_set.add(c["href"].rstrip("/").split("/")[-1])

    new_candidates = []
    for row in slug_probe:
        if row.get("http_status") != 200:
            continue
        slug = row["slug"]
        if slug in known_slug_set and row.get("on_homepage") and row.get("on_neutral_hub"):
            continue
        if not row.get("on_homepage") or not row.get("on_neutral_hub"):
            new_candidates.append(row)

    inventory = {
        "generated_at": utc_now(),
        "neutral_hub_category_id": NEUTRAL_HUB_ID,
        "live_branch_ids": live_branch_ids,
        "known_repo_branch_ids": KNOWN_BRANCH_IDS,
        "homepage_cards": home_cards,
        "hub_cards": hub_cards,
        "megamenu_neutral_children": megamenu_children,
        "sitemap_neutral_parent_slugs": sitemap_slugs,
        "slug_probe": slug_probe,
        "new_parent_candidates": new_candidates,
        "visibility_remote_sha256": sha256_bytes(vis_bytes),
    }
    write_json(DEPLOYMENT_ROOT / "category-inventory" / "neutral-category-inventory-before.json", inventory)

    md_lines = [
        "# Neutral category inventory (before)",
        "",
        f"Generated: {inventory['generated_at']}",
        "",
        "## Live branch IDs (`category_visibility.php`)",
        "",
        ", ".join(str(x) for x in live_branch_ids) or "(none parsed)",
        "",
        "## Homepage cards",
        "",
        "| Name | href | img |",
        "|------|------|-----|",
    ]
    for c in home_cards:
        md_lines.append(f"| {c.get('name','')} | {c.get('href','')} | {c.get('img','')} |")
    md_lines += ["", "## Neutral hub cards", "", "| Name | href | img |", "|------|------|-----|"]
    for c in hub_cards:
        md_lines.append(f"| {c.get('name','')} | {c.get('href','')} | {c.get('img','')} |")
    md_lines += ["", "## Sitemap neutral parent slugs", ""]
    for s in sitemap_slugs:
        md_lines.append(f"- `{s}`")
    md_lines += ["", "## New parent candidates (not on homepage/hub tiles)", ""]
    if new_candidates:
        for row in new_candidates:
            md_lines.append(f"- **{row.get('h1') or row['slug']}** — {row['url']}")
    else:
        md_lines.append("- (none detected via sitemap/tile diff)")
    write_text(DEPLOYMENT_ROOT / "category-inventory" / "neutral-category-inventory-before.md", "\n".join(md_lines) + "\n")

    write_json(DEPLOYMENT_ROOT / "category-inventory" / "new-parent-categories.json", {"new_parent_categories": new_candidates})
    new_md = ["# New parent categories", ""]
    for row in new_candidates:
        new_md.append(f"## {row.get('h1') or row['slug']}")
        new_md.append(f"- URL: {row['url']}")
        new_md.append(f"- On homepage: {row.get('on_homepage')}")
        new_md.append(f"- On hub: {row.get('on_neutral_hub')}")
        new_md.append(f"- In megamenu: {row.get('in_megamenu')}")
        new_md.append("")
    write_text(DEPLOYMENT_ROOT / "category-inventory" / "new-parent-categories.md", "\n".join(new_md) + "\n")

    return inventory


def phase_image_reference() -> dict[str, Any]:
    """Download existing category tile images from live homepage/hub."""
    inv = json.loads(
        (DEPLOYMENT_ROOT / "category-inventory" / "neutral-category-inventory-before.json").read_text(
            encoding="utf-8"
        )
    )
    refs: list[dict[str, Any]] = []
    seen_urls: set[str] = set()
    for source, cards in (("homepage", inv.get("homepage_cards", [])), ("hub", inv.get("hub_cards", []))):
        for card in cards:
            img_url = card.get("img", "")
            if not img_url or img_url in seen_urls:
                continue
            seen_urls.add(img_url)
            if img_url.startswith("/"):
                img_url = PRODUCTION_URL.rstrip("/") + img_url
            try:
                req = urllib.request.Request(img_url, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req, timeout=30) as resp:
                    data = resp.read()
                fname = img_url.split("/")[-1].split("?")[0] or "image.webp"
                out = DEPLOYMENT_ROOT / "image-reference" / fname
                out.write_bytes(data)
                refs.append(
                    {
                        "source": source,
                        "url": img_url,
                        "filename": fname,
                        "bytes": len(data),
                        "sha256": sha256_bytes(data),
                    }
                )
            except Exception as exc:
                refs.append({"source": source, "url": img_url, "error": str(exc)})

    # Pillow dimensions if available
    try:
        from PIL import Image  # type: ignore

        for ref in refs:
            if "filename" not in ref:
                continue
            p = DEPLOYMENT_ROOT / "image-reference" / ref["filename"]
            if p.exists():
                with Image.open(p) as im:
                    ref["width"] = im.width
                    ref["height"] = im.height
                    ref["format"] = im.format
                    ref["aspect_ratio"] = round(im.width / im.height, 4) if im.height else None
    except ImportError:
        pass

    spec = {
        "target_dimensions": "300x300 (OpenCart resize cache)",
        "source_format": "webp preferred",
        "storage_path": "/public_html/image/catalog/Category-image/",
        "naming_convention": "{slug}.webp source; cache {slug}-300x300.webp",
        "max_filesize_target_bytes": 120000,
        "crop_rules": "square product photo, cool gray-blue industrial style",
        "references": refs,
    }
    write_json(DEPLOYMENT_ROOT / "image-reference" / "existing-category-image-style.json", spec)
    write_text(
        DEPLOYMENT_ROOT / "image-reference" / "existing-category-image-style.md",
        "# Existing category image style\n\n"
        + json.dumps(spec, ensure_ascii=False, indent=2)
        + "\n",
    )
    return spec


def prepare_category_visibility_patch() -> bytes:
    src = (DEPLOYMENT_ROOT / "backup" / "category_visibility.php").read_bytes()
    text = src.decode("utf-8")
    new_line = "\tprivate static $neutral_hub_branch_ids = array(" + ", ".join(str(x) for x in ROLLOUT_BRANCH_IDS) + ");"
    patched, count = re.subn(
        r"\tprivate static \$neutral_hub_branch_ids = array\([^)]+\);",
        new_line,
        text,
        count=1,
    )
    if count != 1:
        raise RuntimeError("Failed to patch neutral_hub_branch_ids")
    out = DEPLOYMENT_ROOT / "prepared" / "category_visibility.php"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(patched.encode("utf-8"))
    (DEPLOYMENT_ROOT / "rollback" / "category_visibility.php").write_bytes(src)
    return patched.encode("utf-8")


def phase_manifests() -> None:
    tile_map = {
        "homepage_cat_cards": {
            "source": "catalog/controller/common/home.php -> CategoryVisibility::buildHomepageCategoryCards()",
            "image_source": "oc_category.image via model_tool_image->resize(300,300)",
            "changed_file": "system/library/zpm/category_visibility.php",
        },
        "neutral_hub_cards": {
            "source": "catalog/controller/product/category.php hub mode -> getNeutralHubBranchIds()",
            "image_source": "oc_category.image via resize(300,300)",
            "changed_file": "system/library/zpm/category_visibility.php",
        },
        "catalog_megamenu_tiles": {
            "source": "cat-list-header cache + prepareMegamenuCategories()",
            "image_source": "oc_category.image",
            "changed_file": "none (already dynamic)",
        },
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "tile-authority-map.json", tile_map)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "tile-authority-map.md",
        "# Tile authority map\n\n" + json.dumps(tile_map, ensure_ascii=False, indent=2) + "\n",
    )
    plan = {
        "order": [
            "upload 4 webp masters to /public_html/image/catalog/Category-image/",
            "admin-save oc_category.image for categories 86,331,354,358",
            "upload patched category_visibility.php",
            "HTTP verify homepage/hub/catalog",
        ],
        "branch_ids_before": KNOWN_BRANCH_IDS,
        "branch_ids_after": ROLLOUT_BRANCH_IDS,
        "new_categories": [
            {"id": 331, "slug": "polki-nastennye-i-nastolnye"},
            {"id": 354, "slug": "telezhki-shpilki-i-protivni"},
            {"id": 358, "slug": "shkafy-i-lari"},
            {"id": 86, "slug": "stellazhi"},
        ],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "implementation-plan.json", plan)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "files-to-change.json",
        {
            "remote_files": [
                "/public_html/system/library/zpm/category_visibility.php",
                "/public_html/image/catalog/Category-image/stellazhi.webp",
                "/public_html/image/catalog/Category-image/polki-nastennye-i-nastolnye.webp",
                "/public_html/image/catalog/Category-image/shkafy-i-lari.webp",
                "/public_html/image/catalog/Category-image/telezhki-shpilki-i-protivni.webp",
            ]
        },
    )
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "admin-actions.json",
        {
            "category_image_fields": [
                {"category_id": cid, "image": path} for cid, path in CATEGORY_IMAGE_MAP.items()
            ]
        },
    )
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.json",
        {
            "tiles_before_home": 5,
            "tiles_after_home": 9,
            "tiles_before_hub": 5,
            "tiles_after_hub": 9,
            "image_uploads": 4,
            "remote_deletes": 0,
        },
    )


def admin_save_category_images() -> list[dict[str, Any]]:
    from playwright.sync_api import sync_playwright

    text = SECRETS_PATH.read_text(encoding="utf-8")
    block = re.search(r"## PRODUCTION\s*([\s\S]*?)(?=^## |\Z)", text, re.M).group(1)
    admin_block = re.search(r"### OpenCart Admin\s*([\s\S]*?)(?=^### |\Z)", block, re.M).group(1)
    fields: dict[str, str] = {}
    key = None
    for line in admin_block.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            key = s[:-1].strip().lower().replace(" ", "_")
            fields[key] = ""
        elif key:
            fields[key] = s
    saves: list[dict[str, Any]] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(120000)
        page.goto(fields.get("url", "https://bzpm.ru/admin/"), wait_until="domcontentloaded")
        page.fill('input[name="username"]', fields["login"])
        page.fill('input[name="password"]', fields["password"])
        page.click('button[type="submit"]')
        page.wait_for_timeout(5000)
        token = re.search(r"user_token=([a-zA-Z0-9]+)", page.url).group(1)
        admin_base = page.url.split("index.php")[0]
        for cid, image_path in CATEGORY_IMAGE_MAP.items():
            edit = f"{admin_base}index.php?route=catalog/category/edit&user_token={token}&category_id={cid}"
            page.goto(edit, wait_until="domcontentloaded")
            page.wait_for_timeout(1000)
            img_input = page.locator("#input-image")
            if img_input.count() == 0:
                saves.append({"category_id": cid, "status": "FAILED", "reason": "image input missing"})
                continue
            before = img_input.input_value()
            page.evaluate(
                """(path) => {
                    const el = document.querySelector('#input-image');
                    if (el) el.value = path;
                }""",
                image_path,
            )
            page.locator('button[type="submit"]').first.click()
            page.wait_for_timeout(2500)
            page.goto(edit, wait_until="domcontentloaded")
            page.wait_for_timeout(800)
            after = page.locator("#input-image").input_value()
            saves.append(
                {
                    "category_id": cid,
                    "image_path": image_path,
                    "before": before,
                    "after": after,
                    "status": "PASS" if after == image_path else "PARTIAL",
                }
            )
        browser.close()
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "after.json", {"saves": saves})
    return saves


def phase_admin_only() -> dict[str, Any]:
    saves = admin_save_category_images()
    return {"admin_saves": saves}


def phase_deploy() -> dict[str, Any]:
    secrets = parse_production_secrets(SECRETS_PATH)
    phase_manifests()
    patched = prepare_category_visibility_patch()
    ftp = ftp_connect(secrets)
    try:
        pre = ftp_download(ftp, REMOTE_CATEGORY_VISIBILITY)
        backup_sha = sha256_bytes((DEPLOYMENT_ROOT / "backup" / "category_visibility.php").read_bytes())
        if pre and sha256_bytes(pre) != backup_sha:
            raise RuntimeError("STOP — LIVE FILE CHANGED SINCE BACKUP")
        (DEPLOYMENT_ROOT / "verification" / "pre-upload" / "category_visibility.php").write_bytes(pre or b"")
        for fname in (
            "stellazhi.webp",
            "polki-nastennye-i-nastolnye.webp",
            "shkafy-i-lari.webp",
            "telezhki-shpilki-i-protivni.webp",
        ):
            local = DEPLOYMENT_ROOT / "image-final" / fname
            if not local.exists():
                raise FileNotFoundError(local)
            remote = f"/public_html/image/catalog/Category-image/{fname}"
            ftp_upload(ftp, remote, local.read_bytes())
        ftp_upload(ftp, REMOTE_CATEGORY_VISIBILITY, patched)
    finally:
        ftp.quit()
    return {"branch_ids": ROLLOUT_BRANCH_IDS, "ftp": "PASS"}


def phase_verify() -> dict[str, Any]:
    results: dict[str, Any] = {"urls": {}, "checks": {}}
    for name, url in FETCH_URLS:
        status, body, headers = http_get(url)
        write_text(DEPLOYMENT_ROOT / "html-after" / f"{name}.html", body)
        home_cards = parse_hub_cards(body) if name == "home" else []
        hub_cards = parse_hub_cards(body) if name == "neutral_hub" else []
        catalog_tiles = []
        if name in ("home", "katalog", "katalog_slash", "neutral_hub"):
            for m in re.finditer(
                r'<a class="zpm-catalog__tile" href="([^"]+)"[\s\S]*?src="([^"]+)"[\s\S]*?zpm-catalog__tile-title">([^<]+)</span>',
                body,
            ):
                catalog_tiles.append({"href": m.group(1), "img": m.group(2), "title": m.group(3).strip()})
        results["urls"][name] = {
            "status": status,
            "home_cat_cards": len(home_cards) if name == "home" else None,
            "hub_cat_cards": len(hub_cards) if name == "neutral_hub" else None,
            "catalog_tiles": len(catalog_tiles) if catalog_tiles else None,
        }
    _, robots_body, _ = http_get("https://bzpm.ru/robots.txt")
    _, sitemap_body, _ = http_get("https://bzpm.ru/sitemap.xml")
    home_html = (DEPLOYMENT_ROOT / "html-after" / "home.html").read_text(encoding="utf-8")
    results["checks"] = {
        "body_count_home": home_html.lower().count("<body"),
        "yandex_verification": "yandex-verification" in home_html,
        "metrika": "mc.yandex.ru" in home_html or "ym(" in home_html,
        "robots_200": "Sitemap:" in robots_body,
        "sitemap_xml": sitemap_body.strip().startswith("<?xml"),
        "home_cat_cards": len(parse_hub_cards(home_html)),
        "hub_cat_cards": len(parse_hub_cards((DEPLOYMENT_ROOT / "html-after" / "neutral_hub.html").read_text(encoding="utf-8"))),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "post-deploy-verification.json", results)
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "phase",
        choices=["discover", "image-reference", "manifests", "deploy", "admin-only", "verify", "all"],
        default="all",
        nargs="?",
    )
    args = parser.parse_args()
    phase = args.phase or "all"
    if phase in ("discover", "all"):
        inv = phase_discover()
        print(json.dumps({"phase": "discover", "home_cards": len(inv["homepage_cards"]), "new_candidates": len(inv["new_parent_candidates"])}, ensure_ascii=False))
    if phase in ("image-reference", "all"):
        spec = phase_image_reference()
        print(json.dumps({"phase": "image-reference", "refs": len(spec.get("references", []))}, ensure_ascii=False))
    if phase in ("manifests", "all"):
        phase_manifests()
        print(json.dumps({"phase": "manifests"}, ensure_ascii=False))
    if phase == "deploy":
        out = phase_deploy()
        print(json.dumps(out, ensure_ascii=False))
    if phase == "admin-only":
        out = phase_admin_only()
        print(json.dumps(out, ensure_ascii=False))
    if phase in ("verify", "all"):
        if phase == "all":
            pass
        else:
            out = phase_verify()
            print(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
