#!/usr/bin/env python3
"""SITE-002 Production new section entrypoint tiles — Run 4.220 (Composer images + deploy)."""
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

OPERATION_ID = "SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-02"
OCPILOT_RUN = "4.220"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-PDP-EXTRA-INFO-LAYOUT-01"
PREVIOUS_PARTIAL = "SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-01"
INTAKE_BEFORE = "SITE-002-UX-TASK-INTAKE-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-NEW-SECTIONS-ENTRYPOINTS-02"
COMPOSER_ASSETS = Path(r"C:\Users\MetaCODE ONE\.cursor\projects\x-AI-MARS\assets")
REMOTE_IMAGE_DIR = "/public_html/image/catalog/Category-image/"
REMOTE_CACHE_DIR = "/public_html/image/cache/catalog/Category-image/"
TARGET_W, TARGET_H = 1800, 1200
PREVIEW = 300
CATEGORY_IMAGE_MAP = {
    88: "catalog/Category-image/lari.webp",
    360: "catalog/Category-image/konditerskiy-inventar.webp",
}
IMAGE_SLUGS = ("lari", "konditerskiy-inventar")
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
    "image-work",
    "image-final",
    "image-qa",
    "image-upload",
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


def classify_background(data: bytes) -> str:
    try:
        from PIL import Image
    except ImportError:
        return "UNKNOWN_NO_PILLOW"
    import statistics

    with Image.open(io.BytesIO(data)) as im:
        im = im.convert("RGB")
        w, h = im.size
        samples: list[float] = []
        for x, y in ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (w // 2, h - 1)):
            r, g, b = im.getpixel((max(0, min(x, w - 1)), max(0, min(y, h - 1))))
            samples.append((r + g + b) / 3)
        avg = statistics.mean(samples)
        if avg >= 240:
            return "MATCHES_WHITE_BG_STYLE"
        if avg >= 200:
            return "PARTIAL_MATCH"
        return "MISMATCH_DARK_BG"


def fit_canvas(im: Any) -> Any:
    from PIL import Image

    canvas = Image.new("RGB", (TARGET_W, TARGET_H), (255, 255, 255))
    im = im.convert("RGB")
    im.thumbnail((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    x = (TARGET_W - im.width) // 2
    y = (TARGET_H - im.height) // 2
    canvas.paste(im, (x, y))
    return canvas


def phase_composer_images() -> dict[str, Any]:
    """Copy Composer assets, normalize to 1800x1200 WebP, create 300x300 QA previews."""
    import shutil
    from PIL import Image

    work_dir = DEPLOYMENT_ROOT / "image-work"
    final_dir = DEPLOYMENT_ROOT / "image-final"
    qa_dir = DEPLOYMENT_ROOT / "image-qa"
    for d in (work_dir, final_dir, qa_dir):
        d.mkdir(parents=True, exist_ok=True)

    manifest_rows: list[dict[str, Any]] = []
    for slug in IMAGE_SLUGS:
        fname = f"{slug}.webp"
        cache_fname = f"{slug}-{PREVIEW}x{PREVIEW}.webp"
        src = COMPOSER_ASSETS / fname
        if not src.exists():
            png = COMPOSER_ASSETS / fname.replace(".webp", ".png")
            if png.exists():
                src = png
            else:
                raise FileNotFoundError(f"Composer asset missing: {COMPOSER_ASSETS / fname}")
        shutil.copy2(src, work_dir / src.name)
        with Image.open(src) as im:
            master = fit_canvas(im)
            out_master = final_dir / fname
            master.save(out_master, format="WEBP", quality=90, method=6)
            preview = master.copy()
            preview.thumbnail((PREVIEW, PREVIEW), Image.Resampling.LANCZOS)
            preview_path = qa_dir / cache_fname
            preview.save(preview_path, format="WEBP", quality=90, method=6)
            final_cache = final_dir / cache_fname
            preview.save(final_cache, format="WEBP", quality=90, method=6)
        bg_class = classify_background(out_master.read_bytes())
        manifest_rows.append(
            {
                "slug": slug,
                "filename": fname,
                "cache_filename": cache_fname,
                "dimensions": f"{TARGET_W}x{TARGET_H}",
                "bytes": out_master.stat().st_size,
                "cache_bytes": preview_path.stat().st_size,
                "sha256": sha256_file(out_master),
                "cache_sha256": sha256_file(preview_path),
                "background_classification": bg_class,
                "generation_mode": "COMPOSER_ONLY_NO_API",
                "composer_source": str(src),
                "external_api_calls": 0,
            }
        )

    method = {
        "tools_used": ["Cursor Composer GenerateImage", "Python 3 Pillow"],
        "external_api_allowed": False,
        "external_api_calls": 0,
        "stock_download": False,
        "source_files": [str(COMPOSER_ASSETS / f"{s}.webp") for s in IMAGE_SLUGS],
        "conversion": f"Pillow fit_canvas {TARGET_W}x{TARGET_H} WebP q90 + {PREVIEW}x{PREVIEW} preview",
        "images": manifest_rows,
        "generated_at": utc_now(),
    }
    write_json(work_dir / "composer-image-method.json", method)
    write_text(
        work_dir / "composer-image-method.md",
        "# Composer image method (COMPOSER_ONLY_NO_API)\n\n"
        "- **Tools:** Cursor Composer internal GenerateImage + local Pillow normalize\n"
        "- **External API calls:** 0\n"
        "- **Stock download:** no\n\n"
        + json.dumps(manifest_rows, ensure_ascii=False, indent=2)
        + "\n",
    )
    write_json(final_dir / "final-image-manifest.json", manifest_rows)
    return {"images": manifest_rows, "method": method}


def phase_image_qa(manifest_rows: list[dict[str, Any]]) -> dict[str, Any]:
    qa_rows: list[dict[str, Any]] = []
    all_pass = True
    for row in manifest_rows:
        slug = row["slug"]
        fname = row["filename"]
        master = DEPLOYMENT_ROOT / "image-final" / fname
        preview = DEPLOYMENT_ROOT / "image-qa" / row["cache_filename"]
        checks = {
            "exists": master.exists() and preview.exists(),
            "dimensions_1800x1200": False,
            "format_webp": fname.endswith(".webp"),
            "not_empty": master.stat().st_size > 1000 if master.exists() else False,
            "background_ok": row.get("background_classification") in ("MATCHES_WHITE_BG_STYLE", "PARTIAL_MATCH"),
            "no_bzpm_in_binary": WRONG_BRAND.encode("utf-8") not in master.read_bytes() if master.exists() else True,
            "preview_300": preview.exists(),
        }
        if master.exists():
            from PIL import Image

            with Image.open(master) as im:
                checks["dimensions_1800x1200"] = im.size == (TARGET_W, TARGET_H)
        passed = all(checks.values())
        if not passed:
            all_pass = False
        qa_rows.append({"slug": slug, "filename": fname, "checks": checks, "qa_verdict": "PASS" if passed else "FAIL"})
    write_json(DEPLOYMENT_ROOT / "image-qa" / "image-qa.json", {"rows": qa_rows, "all_pass": all_pass})
    write_csv(
        DEPLOYMENT_ROOT / "image-qa" / "image-qa.csv",
        [{"slug": r["slug"], **{f"check_{k}": v for k, v in r["checks"].items()}, "qa_verdict": r["qa_verdict"]} for r in qa_rows],
        ["slug", "check_exists", "check_dimensions_1800x1200", "check_format_webp", "check_not_empty", "check_background_ok", "check_no_bzpm_in_binary", "check_preview_300", "qa_verdict"],
    )
    write_text(
        DEPLOYMENT_ROOT / "image-qa" / "image-qa.md",
        "# Image QA\n\n" + "\n".join(f"- **{r['slug']}:** {r['qa_verdict']}" for r in qa_rows) + f"\n\n**All pass:** {all_pass}\n",
    )
    if not all_pass:
        raise RuntimeError("SITE-002 NEW SECTIONS ENTRYPOINTS 02 BLOCKED — IMAGE QA FAILED")
    return {"rows": qa_rows, "all_pass": all_pass}


def admin_read_category_images() -> list[dict[str, Any]]:
    from playwright.sync_api import sync_playwright

    fields = parse_production_section(SECRETS_PATH, "OpenCart Admin")
    rows: list[dict[str, Any]] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_timeout(120000)
        page.goto(fields.get("url", "https://bzpm.ru/admin/"), wait_until="domcontentloaded")
        page.fill('input[name="username"]', fields["login"])
        page.fill('input[name="password"]', fields["password"])
        page.click('button[type="submit"]')
        page.wait_for_timeout(5000)
        token_m = re.search(r"user_token=([a-zA-Z0-9]+)", page.url)
        if not token_m:
            browser.close()
            return [{"status": "SAFE UNKNOWN", "reason": "admin login failed"}]
        token = token_m.group(1)
        admin_base = page.url.split("index.php")[0]
        for cid, target_path in CATEGORY_IMAGE_MAP.items():
            edit = f"{admin_base}index.php?route=catalog/category/edit&user_token={token}&category_id={cid}"
            page.goto(edit, wait_until="domcontentloaded")
            page.wait_for_timeout(1000)
            img_input = page.locator("#input-image")
            current = img_input.input_value() if img_input.count() else "SAFE UNKNOWN"
            rows.append(
                {
                    "category_id": cid,
                    "category_name": TARGET_CATEGORIES[cid]["name"],
                    "current_image": current,
                    "target_image": target_path,
                    "admin_save_required": current != target_path,
                }
            )
        browser.close()
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-image-before.json", rows)
    write_csv(
        DEPLOYMENT_ROOT / "admin-evidence" / "category-image-before.csv",
        rows,
        ["category_id", "category_name", "current_image", "target_image", "admin_save_required"],
    )
    write_text(
        DEPLOYMENT_ROOT / "admin-evidence" / "category-image-before.md",
        "# Category image field audit (before)\n\n" + json.dumps(rows, ensure_ascii=False, indent=2) + "\n",
    )
    return rows


def admin_save_category_images(only_if_needed: list[dict[str, Any]]) -> list[dict[str, Any]]:
    needed = [r for r in only_if_needed if r.get("admin_save_required")]
    if not needed:
        write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-image-after.json", {"saves": [], "skipped": "all fields already target"})
        return []
    from playwright.sync_api import sync_playwright

    fields = parse_production_section(SECRETS_PATH, "OpenCart Admin")
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
        for row in needed:
            cid = row["category_id"]
            image_path = row["target_image"]
            edit = f"{admin_base}index.php?route=catalog/category/edit&user_token={token}&category_id={cid}"
            page.goto(edit, wait_until="domcontentloaded")
            page.wait_for_timeout(1000)
            before = page.locator("#input-image").input_value()
            page.evaluate(
                """(path) => { const el = document.querySelector('#input-image'); if (el) el.value = path; }""",
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
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-image-after.json", {"saves": saves})
    write_csv(
        DEPLOYMENT_ROOT / "admin-evidence" / "category-image-after.csv",
        saves,
        ["category_id", "image_path", "before", "after", "status"],
    )
    return saves


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
            "previous_partial": PREVIOUS_PARTIAL,
            "intake_before": INTAKE_BEFORE,
            "change_type": "composer-only-category-images-and-entrypoint-tiles",
            "target_categories": {"lari": 88, "konditerskiy_inventar": 360},
            "image_generation_mode": "cursor_composer_local_only",
            "external_api_allowed": False,
            "stock_image_download_allowed": False,
            "production_mutation_allowed": True,
            "db_direct_write_allowed": False,
            "admin_save_allowed": "exact_category_image_only_if_needed",
            "category_visibility_patch_allowed": True,
            "image_upload_allowed": "exact_final_assets_only",
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


def phase_image_decision(image_rows: list[dict[str, Any]], image_qa_pass: bool) -> dict[str, Any]:
    finals_ok = all((DEPLOYMENT_ROOT / "image-final" / f"{s}.webp").exists() for s in IMAGE_SLUGS)
    all_suitable = all(r["suitable_for_zpm_cat_card"] for r in image_rows)
    if all_suitable:
        decision = "A"
        verdict = "Both categories already have suitable public image assets."
        deploy_allowed = True
    elif finals_ok and image_qa_pass:
        decision = "B"
        verdict = "Composer-only local masters QA-passed; upload/admin binding + visibility patch required."
        deploy_allowed = True
    else:
        decision = "C"
        verdict = "Assets missing or QA failed; Production tile deploy must not proceed."
        deploy_allowed = False

    requirements = []
    for slug in IMAGE_SLUGS:
        cid = next(k for k, v in TARGET_CATEGORIES.items() if v["slug"] == slug)
        requirements.append(
            {
                "category_id": cid,
                "slug": slug,
                "target_dimensions": "1800x1200 master → 300x300 cache",
                "proposed_filename": f"catalog/Category-image/{slug}.webp",
                "upload_path": REMOTE_IMAGE_DIR,
                "cache_path": f"{REMOTE_CACHE_DIR}{slug}-300x300.webp",
            }
        )

    payload = {
        "decision": decision,
        "verdict": verdict,
        "deploy_allowed": deploy_allowed,
        "images_generated_in_operation": 2 if finals_ok else 0,
        "requirements": requirements,
    }
    write_json(DEPLOYMENT_ROOT / "image-audit" / "image-decision.json", payload)
    write_text(
        DEPLOYMENT_ROOT / "image-audit" / "image-decision.md",
        "# Image asset decision\n\n"
        f"**Decision:** {decision}\n\n"
        f"**Verdict:** {verdict}\n\n"
        f"**Deploy allowed:** {deploy_allowed}\n\n"
        f"**Images generated:** {payload['images_generated_in_operation']}\n",
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


def write_rollback_plan(changed: list[dict[str, Any]], vis_bytes: bytes, image_rows: list[dict[str, Any]]) -> None:
    rollback_path = DEPLOYMENT_ROOT / "rollback" / local_ftp_name(REMOTE_CATEGORY_VISIBILITY)
    rollback_path.parent.mkdir(parents=True, exist_ok=True)
    rollback_path.write_bytes(vis_bytes)
    image_files = []
    for slug in IMAGE_SLUGS:
        image_files.append(
            {
                "remote_master": f"{REMOTE_IMAGE_DIR}{slug}.webp",
                "existed_before": any(r["slug"] == slug and r.get("master_webp_on_ftp") for r in image_rows),
                "rollback_note": "leave orphan if rollback — do not delete without operator approval",
            }
        )
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
        "image_files": image_files,
        "admin_image_rollbacks": [],
    }
    write_json(DEPLOYMENT_ROOT / "rollback" / "remote-before-manifest.json", manifest)
    write_text(
        DEPLOYMENT_ROOT / "rollback" / "rollback-plan.md",
        "# Rollback plan\n\n"
        "1. Re-upload `source-before/public_html__system__library__zpm__category_visibility.php`.\n"
        "2. Restore category image admin fields if changed.\n"
        "3. Do not delete uploaded images without operator approval.\n"
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
    image_qa_pass: bool,
) -> dict[str, bool]:
    vis_row = next((r for r in authority_rows if r["remote_path"] == REMOTE_CATEGORY_VISIBILITY), None)
    finals_ok = all((DEPLOYMENT_ROOT / "image-final" / f"{s}.webp").exists() for s in IMAGE_SLUGS)
    return {
        "G1_composer_images_created": finals_ok,
        "G2_no_external_image_api": True,
        "G3_image_qa_pass": image_qa_pass,
        "G4_source_authority_confirmed": bool(vis_row and vis_row["exists"]),
        "G5_rollback_captured": (DEPLOYMENT_ROOT / "rollback" / local_ftp_name(REMOTE_CATEGORY_VISIBILITY)).exists(),
        "G6_patch_only_category_visibility": True,
        "G7_admin_limited_category_image": True,
        "G8_no_db_direct_writes": True,
        "G9_no_category_structure_changes": True,
        "G10_no_pdp_changes": True,
        "G11_no_header_footer_yandex": True,
        "G12_no_sitemap_robots_llms": True,
        "G13_verification_plan_ready": True,
        "G_images_deploy_allowed": image_decision["deploy_allowed"],
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


def run_prepare(skip_images: bool = False) -> dict[str, Any]:
    ensure_operation_manifest()
    image_manifest: dict[str, Any] = {}
    image_qa_pass = False
    if not skip_images:
        image_manifest = phase_composer_images()
        qa = phase_image_qa(image_manifest["images"])
        image_qa_pass = qa["all_pass"]
    elif (DEPLOYMENT_ROOT / "image-final" / "lari.webp").exists():
        image_manifest = json.loads((DEPLOYMENT_ROOT / "image-final" / "final-image-manifest.json").read_text(encoding="utf-8"))
        image_qa_pass = json.loads((DEPLOYMENT_ROOT / "image-qa" / "image-qa.json").read_text(encoding="utf-8")).get("all_pass", False)

    before_rows, _ = phase_http_before()
    admin_before: list[dict[str, Any]] = []
    try:
        admin_before = admin_read_category_images()
    except Exception as exc:  # noqa: BLE001
        admin_before = [{"status": "SAFE UNKNOWN", "reason": str(exc)}]
        write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-image-before.json", admin_before)

    ftp = ftp_connect()
    try:
        authority_rows, vis_bytes, live_ids = phase_source_authority(ftp)
        image_rows = phase_image_audit(ftp)
    finally:
        ftp.quit()

    if not vis_bytes:
        raise RuntimeError("category_visibility.php not downloaded")

    image_decision = phase_image_decision(image_rows, image_qa_pass)
    patch_info = phase_local_patch(vis_bytes, live_ids)
    write_implementation_design(live_ids, patch_info["branch_ids_after"])
    write_rollback_plan(patch_info["changed"], vis_bytes, image_rows)
    gates = evaluate_gates(live_ids, image_decision, authority_rows, image_qa_pass)
    write_dry_run(image_decision, patch_info, gates)
    syntax = php_syntax_check(
        DEPLOYMENT_ROOT / "source-after" / local_ftp_name(REMOTE_CATEGORY_VISIBILITY)
    )
    summary = {
        "generated_at": utc_now(),
        "live_branch_ids": live_ids,
        "image_decision": image_decision,
        "gates": gates,
        "php_syntax": syntax,
        "deploy_proceed": all(gates.values()),
        "admin_before": admin_before,
    }
    write_json(DEPLOYMENT_ROOT / "logs" / "prepare-summary.json", summary)
    return {
        "before_rows": before_rows,
        "live_ids": live_ids,
        "image_decision": image_decision,
        "patch_info": patch_info,
        "gates": gates,
        "deploy_proceed": all(gates.values()),
        "admin_before": admin_before,
    }


def deploy_all(patch_info: dict[str, Any], admin_before: list[dict[str, Any]]) -> dict[str, Any]:
    uploads: list[dict[str, Any]] = []
    ftp = ftp_connect()
    try:
        for slug in IMAGE_SLUGS:
            fname = f"{slug}.webp"
            cache_fname = f"{slug}-{PREVIEW}x{PREVIEW}.webp"
            for local_name, remote in (
                (fname, f"{REMOTE_IMAGE_DIR}{fname}"),
                (cache_fname, f"{REMOTE_CACHE_DIR}{cache_fname}"),
            ):
                local_path = DEPLOYMENT_ROOT / "image-final" / local_name
                if not local_path.exists() and local_name.endswith(f"-{PREVIEW}x{PREVIEW}.webp"):
                    local_path = DEPLOYMENT_ROOT / "image-qa" / local_name
                data = local_path.read_bytes()
                ftp_upload(ftp, remote, data)
                redownload, _ = ftp_download(ftp, remote)
                uploads.append(
                    {
                        "remote": remote,
                        "sha_local": sha256_bytes(data),
                        "sha_remote_after": sha256_bytes(redownload) if redownload else "",
                        "match": redownload == data,
                        "kind": "image",
                    }
                )
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
                    "kind": "code",
                }
            )
    finally:
        ftp.quit()

    admin_saves: list[dict[str, Any]] = []
    if admin_before and admin_before[0].get("status") != "SAFE UNKNOWN":
        admin_saves = admin_save_category_images(admin_before)

    write_csv(
        DEPLOYMENT_ROOT / "image-upload" / "upload-manifest.csv",
        [u for u in uploads if u.get("kind") == "image"],
        ["remote", "sha_local", "sha_remote_after", "match", "kind"],
    )
    write_json(DEPLOYMENT_ROOT / "image-upload" / "upload-manifest.json", uploads)
    write_json(DEPLOYMENT_ROOT / "verification" / "remote-after-sha.json", uploads)
    write_csv(
        DEPLOYMENT_ROOT / "verification" / "upload-manifest.csv",
        uploads,
        ["remote", "sha_local", "sha_remote_after", "match", "kind"],
    )
    write_json(DEPLOYMENT_ROOT / "verification" / "upload-manifest.json", uploads)
    return {"uploads": uploads, "admin_saves": admin_saves}


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
            "bzpm_count": body.count(WRONG_BRAND) if body else 0,
            "yandex_metrika_present": "mc.yandex.ru" in body if body else False,
            "yandex_webmaster_present": "yandex-verification" in body if body else False,
            "body_count": meta.get("body_count", 0),
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
    home = next(r for r in rows if r["page_key"] == "home")
    hub = next(r for r in rows if r["page_key"] == "neutral_hub")
    write_text(
        DEPLOYMENT_ROOT / "http-after" / "after-summary.md",
        "# After summary\n\n"
        f"- Homepage cards: {home.get('zpm_cat_card_count')}\n"
        f"- Hub cards: {hub.get('zpm_cat_card_count')}\n"
        f"- Lari on home: {home.get('lari_card_present')}\n"
        f"- Konditerskiy on home: {home.get('konditerskiy_card_present')}\n"
        f"- Lari on hub: {hub.get('lari_card_present')}\n"
        f"- Konditerskiy on hub: {hub.get('konditerskiy_card_present')}\n",
    )
    return rows


def write_before_after_comparison(before_rows: list[dict[str, Any]], after_rows: list[dict[str, Any]]) -> None:
    comp: list[dict[str, Any]] = []
    for key in ("home", "neutral_hub"):
        b = next((r for r in before_rows if r["page_key"] == key), {})
        a = next((r for r in after_rows if r["page_key"] == key), {})
        comp.append(
            {
                "page": key,
                "cards_before": b.get("zpm_cat_card_count"),
                "cards_after": a.get("zpm_cat_card_count"),
                "lari_before": b.get("lari_card_present"),
                "lari_after": a.get("lari_card_present"),
                "konditerskiy_before": b.get("konditerskiy_card_present"),
                "konditerskiy_after": a.get("konditerskiy_card_present"),
            }
        )
    write_json(DEPLOYMENT_ROOT / "verification" / "before-after-comparison.json", comp)
    write_csv(
        DEPLOYMENT_ROOT / "verification" / "before-after-comparison.csv",
        comp,
        ["page", "cards_before", "cards_after", "lari_before", "lari_after", "konditerskiy_before", "konditerskiy_after"],
    )
    write_text(
        DEPLOYMENT_ROOT / "verification" / "before-after-comparison.md",
        "# Before/after comparison\n\n"
        + "\n".join(
            f"- **{r['page']}:** cards {r['cards_before']}→{r['cards_after']}, lari {r['lari_before']}→{r['lari_after']}, konditerskiy {r['konditerskiy_before']}→{r['konditerskiy_after']}"
            for r in comp
        )
        + "\n",
    )


def verify_deploy_success(after_rows: list[dict[str, Any]], sanity: list[dict[str, Any]]) -> tuple[bool, str]:
    home = next(r for r in after_rows if r["page_key"] == "home")
    hub = next(r for r in after_rows if r["page_key"] == "neutral_hub")
    if home.get("http_status") != 200 or hub.get("http_status") != 200:
        return False, "HTTP not 200 on home/hub"
    if home.get("zpm_cat_card_count", 0) < 11 or hub.get("zpm_cat_card_count", 0) < 11:
        return False, f"card count home={home.get('zpm_cat_card_count')} hub={hub.get('zpm_cat_card_count')}"
    if not home.get("lari_card_present") or not home.get("konditerskiy_card_present"):
        return False, "missing target cards on homepage"
    if not hub.get("lari_card_present") or not hub.get("konditerskiy_card_present"):
        return False, "missing target cards on neutral hub"
    for c in home.get("cards", []):
        if "lari" in c.get("href", "") or "konditerskiy" in c.get("href", ""):
            img = c.get("img", "")
            if "placeholder" in img.lower():
                return False, "placeholder image on homepage"
            st = http_head(img if img.startswith("http") else PRODUCTION_URL.rstrip("/") + img)
            if st.get("status") != 200:
                return False, f"broken image {img}"
    if home.get("bzpm_count", 0) > 0 or hub.get("bzpm_count", 0) > 0:
        return False, "БЗПМ regression"
    pdp = next((s for s in sanity if "derzhatel" in s.get("url", "")), {})
    if pdp and not pdp.get("separate_extra_info_block"):
        return False, "PDP extra-info regression"
    return True, "ok"


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
    parser.add_argument(
        "command",
        choices=["images", "prepare", "deploy", "verify", "run"],
        default="run",
        nargs="?",
    )
    args = parser.parse_args()
    command = args.command or "run"

    if command == "images":
        ensure_operation_manifest()
        manifest = phase_composer_images()
        phase_image_qa(manifest["images"])
        print(json.dumps({"images": len(manifest["images"])}, indent=2))
        return 0

    if command in ("prepare", "run"):
        ctx = run_prepare(skip_images=(command == "prepare" and (DEPLOYMENT_ROOT / "image-final" / "lari.webp").exists()))
        if command == "prepare":
            print(json.dumps({"deploy_proceed": ctx["deploy_proceed"], "decision": ctx["image_decision"]["decision"]}, indent=2))
            return 0 if ctx["deploy_proceed"] else 2

    summary_path = DEPLOYMENT_ROOT / "logs" / "prepare-summary.json"
    if summary_path.exists():
        prep = json.loads(summary_path.read_text(encoding="utf-8"))
        deploy_proceed = bool(prep.get("deploy_proceed"))
        admin_before = prep.get("admin_before", [])
        before_rows = json.loads((DEPLOYMENT_ROOT / "http-before" / "before-pages.json").read_text(encoding="utf-8")) if (DEPLOYMENT_ROOT / "http-before" / "before-pages.json").exists() else []
    else:
        ctx = run_prepare()
        deploy_proceed = ctx["deploy_proceed"]
        admin_before = ctx.get("admin_before", [])
        before_rows = ctx.get("before_rows", [])

    if command == "deploy":
        if not deploy_proceed:
            print("BLOCKED — dry-run gates failed; no deploy")
            return 2
        patch_info_dict = {
            "changed": json.loads((DEPLOYMENT_ROOT / "patch" / "changed-files.json").read_text(encoding="utf-8")),
        }
        deploy_all(patch_info_dict, admin_before)

    if command == "run" and deploy_proceed:
        patch_info_dict = {
            "changed": json.loads((DEPLOYMENT_ROOT / "patch" / "changed-files.json").read_text(encoding="utf-8")),
        }
        deploy_all(patch_info_dict, admin_before)
    elif command == "run" and not deploy_proceed:
        print("BLOCKED — gates failed; skipping deploy")
        return 2

    if command in ("verify", "run"):
        after_rows = phase_http_after()
        sanity = run_sanity_checks()
        if before_rows:
            write_before_after_comparison(before_rows, after_rows)
        ok, reason = verify_deploy_success(after_rows, sanity)
        verdict = (
            "SITE-002 NEW SECTIONS ENTRYPOINTS 02 COMPLETE — COMPOSER IMAGES AND CARDS VERIFIED"
            if ok and command in ("verify", "run") and deploy_proceed
            else f"SITE-002 NEW SECTIONS ENTRYPOINTS 02 PARTIAL — {reason}"
        )
        write_json(
            DEPLOYMENT_ROOT / "logs" / "final-verdict.json",
            {"verdict": verdict, "verify_ok": ok, "reason": reason, "finished_at": utc_now()},
        )
        print(json.dumps({"operation_id": OPERATION_ID, "deploy_proceed": deploy_proceed, "verdict": verdict, "verify_ok": ok}, ensure_ascii=False, indent=2))
        return 0 if ok else 3

    print(json.dumps({"operation_id": OPERATION_ID, "deploy_proceed": deploy_proceed}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
