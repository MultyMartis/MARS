#!/usr/bin/env python3
"""SITE-002 child category tile images wave — image-only production deploy."""
from __future__ import annotations

import argparse
import ftplib
import hashlib
import io
import json
import re
import shutil
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-CHILD-CATEGORY-IMAGES-WAVE-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
WRONG_BRAND = "БЗПМ"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-CHILD-CATEGORY-IMAGES-WAVE-01"
)
MANIFEST_PATH = DEPLOYMENT_ROOT / "manifests" / "category-wave-manifest.json"
COMPOSER_ASSETS = Path(r"C:\Users\MetaCODE ONE\.cursor\projects\x-AI-MARS\assets")
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

PARENT_PLP_URLS: dict[int, str] = {
    90: "https://bzpm.ru/katalog/teplovoe-oborudovanie/",
    95: "https://bzpm.ru/katalog/holodilnoe-oborudovanie/",
    186: "https://bzpm.ru/katalog/hlebopekarnoe-oborudovanie/",
    373: "https://bzpm.ru/katalog/myasopererabatyvayuschee/",
    375: "https://bzpm.ru/katalog/elektromehanicheskoe/",
}

APPROVED_STYLE_SLUGS = (
    "stoly",
    "moechnye-vanny",
    "podtovarniki-i-podstavki",
    "telezhki-servirovochnye",
    "zonty-vytyazhnye",
)

REMOTE_IMAGE_DIR = "/public_html/image/catalog/Category-image/"
REMOTE_CACHE_DIR = "/public_html/image/cache/catalog/Category-image/"
TARGET_W, TARGET_H = 1800, 1200
PREVIEW = 300
CREATE_DECISION = "CREATE_NEW_IMAGE"

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "image-reference",
    "image-generation",
    "image-work",
    "image-final",
    "image-qa",
    "image-upload",
    "admin-evidence",
    "verification",
    "screenshots",
    "manifests",
    "logs",
    "html-before",
    "html-after",
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


def parse_production_section(path: Path, subsection: str) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    sub = re.search(
        rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)",
        block,
        re.MULTILINE,
    )
    if not sub:
        raise RuntimeError(f"PRODUCTION subsection not found: {subsection}")
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in sub.group(1).splitlines():
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


def http_get(url: str, timeout: int = 45) -> tuple[int, str, dict[str, str]]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read().decode("utf-8", errors="replace")
        headers = {k.lower(): v for k, v in resp.headers.items()}
        return resp.status, body, headers


def http_get_bytes(url: str, timeout: int = 45) -> tuple[int, bytes, dict[str, str]]:
    if url.startswith("/"):
        url = PRODUCTION_URL.rstrip("/") + url
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
        headers = {k.lower(): v for k, v in resp.headers.items()}
        return resp.status, data, headers


def http_head_ok(url: str, timeout: int = 20) -> bool:
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return 200 <= resp.status < 300
    except Exception:
        try:
            status, _, _ = http_get_bytes(url, timeout=timeout)
            return 200 <= status < 300
        except Exception:
            return False


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


def ftp_exists(ftp: ftplib.FTP, remote_path: str) -> bool:
    try:
        ftp.size(remote_path)
        return True
    except Exception:
        return False


def parse_hub_cards(html: str) -> list[dict[str, Any]]:
    cards: list[dict[str, Any]] = []
    for block in re.findall(
        r'<a[^>]+class="[^"]*zpm-cat-card[^"]*"[^>]*>.*?</a>',
        html,
        re.DOTALL | re.IGNORECASE,
    ):
        href_m = re.search(r'href="([^"]+)"', block)
        name_m = re.search(r'class="[^"]*zpm-cat-card__title[^"]*"[^>]*>([^<]+)<', block)
        img_m = re.search(r'<img[^>]+src="([^"]+)"', block)
        if not href_m:
            continue
        href = href_m.group(1)
        slug = href.rstrip("/").split("/")[-1]
        cards.append(
            {
                "name": name_m.group(1).strip() if name_m else "",
                "href": href,
                "slug": slug,
                "img": img_m.group(1) if img_m else "",
            }
        )
    return cards


def ensure_dirs() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)


def load_manifest() -> dict[str, Any]:
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(f"Manifest not found: {MANIFEST_PATH}")
    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if "categories" not in data or not isinstance(data["categories"], list):
        raise RuntimeError("Manifest must contain a categories array")
    return data


def category_meta(entry: dict[str, Any]) -> dict[str, Any]:
    slug = str(entry["slug"])
    return {
        "category_id": int(entry["category_id"]),
        "name": str(entry.get("name") or slug),
        "slug": slug,
        "parent_id": int(entry.get("parent_id") or 0),
        "parent_name": str(entry.get("parent_name") or ""),
        "decision": str(entry.get("decision") or ""),
        "filename": f"{slug}.webp",
        "oc_image": f"catalog/Category-image/{slug}.webp",
    }


def load_target_categories() -> dict[int, dict[str, Any]]:
    manifest = load_manifest()
    targets: dict[int, dict[str, Any]] = {}
    for entry in manifest["categories"]:
        meta = category_meta(entry)
        if meta["decision"] != CREATE_DECISION:
            continue
        targets[meta["category_id"]] = meta
    if not targets:
        raise RuntimeError(f"No categories with decision={CREATE_DECISION} in manifest")
    return targets


def parent_fetch_urls(targets: dict[int, dict[str, Any]]) -> dict[str, str]:
    parent_ids = sorted({meta["parent_id"] for meta in targets.values() if meta["parent_id"]})
    urls: dict[str, str] = {}
    for pid in parent_ids:
        url = PARENT_PLP_URLS.get(pid)
        if not url:
            raise RuntimeError(f"No PARENT_PLP_URLS entry for parent_id={pid}")
        key = f"parent_{pid}"
        urls[key] = url
    return urls


def classify_background(data: bytes) -> str:
    from PIL import Image
    import statistics

    im = Image.open(io.BytesIO(data)).convert("RGB")
    w, h = im.size
    px = list(im.getdata())

    def lum(rgb: tuple[int, int, int]) -> float:
        r, g, b = rgb
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    corners = [px[0], px[w - 1], px[w * (h - 1)], px[w * h - 1]]
    edge_lum = statistics.mean(lum(c) for c in corners)
    cx0, cy0 = w // 4, h // 4
    center = [px[y * w + x] for y in range(cy0, cy0 * 3) for x in range(cx0, cx0 * 3)]
    center_lum = statistics.mean(lum(c) for c in center)
    uniq = len(set(px[:: max(1, len(px) // 4000)]))
    if edge_lum >= 245 and uniq < 150 and center_lum >= 210:
        return "PLACEHOLDER_OR_ICON"
    if edge_lum >= 230:
        return "MATCHES_WHITE_BG_STYLE"
    if edge_lum >= 200:
        return "PARTIAL_MATCH"
    return "MISMATCH_DARK_OR_SCENE"


def fit_canvas(im: Any) -> Any:
    from PIL import Image

    canvas = Image.new("RGB", (TARGET_W, TARGET_H), (255, 255, 255))
    im = im.convert("RGB")
    im.thumbnail((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    x = (TARGET_W - im.width) // 2
    y = (TARGET_H - im.height) // 2
    canvas.paste(im, (x, y))
    return canvas


def phase_audit() -> dict[str, Any]:
    ensure_dirs()
    targets = load_target_categories()
    ref_dir = DEPLOYMENT_ROOT / "image-reference"
    fetch_urls = parent_fetch_urls(targets)

    html_before: dict[str, Any] = {}
    surface_cards: dict[str, list[dict[str, Any]]] = {}
    for key, url in fetch_urls.items():
        status, html, _ = http_get(url)
        (DEPLOYMENT_ROOT / "html-before" / f"{key}.html").write_text(html, encoding="utf-8")
        cards = parse_hub_cards(html)
        surface_cards[key] = cards
        html_before[key] = {"status": status, "card_count": len(cards), "url": url}

    target_audit: list[dict[str, Any]] = []
    for cid, meta in targets.items():
        slug = meta["slug"]
        parent_id = meta["parent_id"]
        parent_key = f"parent_{parent_id}"
        cards = surface_cards.get(parent_key, [])
        hit = next((c for c in cards if c["slug"] == slug), None)
        cache_url = f"https://bzpm.ru/image/cache/catalog/Category-image/{slug}-300x300.webp"
        master_url = f"https://bzpm.ru/image/catalog/Category-image/{slug}.webp"
        placeholder = False
        classification = "MISSING"
        sizes: dict[str, Any] = {}
        for label, url in (("cache", cache_url), ("master", master_url)):
            try:
                st, data, _ = http_get_bytes(url)
                path = ref_dir / f"live-{label}-{slug}.webp"
                path.write_bytes(data)
                sizes[label] = {"http": st, "bytes": len(data), "sha256": sha256_bytes(data)}
                if label == "cache":
                    classification = classify_background(data)
            except Exception as exc:
                sizes[label] = {"error": str(exc)}
                if label == "cache" and hit and "placeholder" in (hit.get("img") or ""):
                    placeholder = True
                    classification = "PLACEHOLDER_PNG"
                    try:
                        st, data, _ = http_get_bytes(hit["img"])
                        (ref_dir / f"live-placeholder-{slug}.png").write_bytes(data)
                        sizes["placeholder"] = {"http": st, "bytes": len(data)}
                    except Exception as exc2:
                        sizes["placeholder"] = {"error": str(exc2)}
        needs_replace = classification in (
            "PLACEHOLDER_OR_ICON",
            "PLACEHOLDER_PNG",
            "MISSING",
            "MISMATCH_DARK_OR_SCENE",
        ) or placeholder
        target_audit.append(
            {
                "category_id": cid,
                "name": meta["name"],
                "slug": slug,
                "parent_id": parent_id,
                "parent_name": meta["parent_name"],
                "decision": meta["decision"],
                "oc_image_target": meta["oc_image"],
                "parent_plp": PARENT_PLP_URLS.get(parent_id),
                "surface": {
                    "present": bool(hit),
                    "href": (hit or {}).get("href"),
                    "img": (hit or {}).get("img"),
                },
                "sizes": sizes,
                "classification": classification,
                "needs_replace": needs_replace,
                "action": "replace" if needs_replace else "keep",
            }
        )

    style_refs = []
    for slug in APPROVED_STYLE_SLUGS:
        url = f"https://bzpm.ru/image/cache/catalog/Category-image/{slug}-300x300.webp"
        st, data, _ = http_get_bytes(url)
        path = ref_dir / f"ref-{slug}-300x300.webp"
        path.write_bytes(data)
        style_refs.append(
            {
                "slug": slug,
                "url": url,
                "bytes": len(data),
                "sha256": sha256_bytes(data),
                "classification": classify_background(data),
            }
        )

    secrets = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(secrets)
    try:
        vis = ftp_download(ftp, "/public_html/system/library/zpm/category_visibility.php")
        (DEPLOYMENT_ROOT / "source" / "category_visibility.php").write_bytes(vis)
        vis_text = vis.decode("utf-8", errors="replace")
        id_hits = {cid: (str(cid) in vis_text) for cid in targets}
        for cid, meta in targets.items():
            remote = REMOTE_IMAGE_DIR + meta["filename"]
            if ftp_exists(ftp, remote):
                data = ftp_download(ftp, remote)
                bak = DEPLOYMENT_ROOT / "backup" / f"pre-{meta['filename']}"
                bak.write_bytes(data)
                (DEPLOYMENT_ROOT / "rollback" / meta["filename"]).write_bytes(data)
            cache_remote = REMOTE_CACHE_DIR + f"{meta['slug']}-{PREVIEW}x{PREVIEW}.webp"
            if ftp_exists(ftp, cache_remote):
                data = ftp_download(ftp, cache_remote)
                (DEPLOYMENT_ROOT / "backup" / f"pre-{meta['slug']}-{PREVIEW}x{PREVIEW}.webp").write_bytes(data)
                (DEPLOYMENT_ROOT / "rollback" / f"{meta['slug']}-{PREVIEW}x{PREVIEW}.webp").write_bytes(data)
    finally:
        ftp.quit()

    report = {
        "operation_id": OPERATION_ID,
        "audited_at": utc_now(),
        "manifest_path": str(MANIFEST_PATH),
        "create_new_image_count": len(targets),
        "html_before": html_before,
        "style_refs": style_refs,
        "target_audit": target_audit,
        "visibility_contains_target_ids": id_hits,
        "replace_count": sum(1 for r in target_audit if r["action"] == "replace"),
        "keep_count": sum(1 for r in target_audit if r["action"] == "keep"),
    }
    write_json(DEPLOYMENT_ROOT / "image-reference" / "current-child-category-images-audit.json", report)
    write_json(DEPLOYMENT_ROOT / "image-reference" / "approved-style-reference.json", style_refs)
    md = [
        "# Child category images audit",
        "",
        f"Audited at: {report['audited_at']}",
        "",
        "| ID | Name | Parent | Classification | Action |",
        "|---:|------|--------|----------------|--------|",
    ]
    for r in target_audit:
        md.append(
            f"| {r['category_id']} | {r['name']} | {r['parent_name']} | {r['classification']} | {r['action']} |"
        )
    write_text(DEPLOYMENT_ROOT / "image-reference" / "current-child-category-images-audit.md", "\n".join(md) + "\n")
    return report


def phase_normalize_composer_assets(
    targets: dict[int, dict[str, Any]],
    source_map: dict[str, Path],
) -> list[dict[str, Any]]:
    from PIL import Image

    work_dir = DEPLOYMENT_ROOT / "image-work"
    final_dir = DEPLOYMENT_ROOT / "image-final"
    qa_dir = DEPLOYMENT_ROOT / "image-qa"
    for d in (work_dir, final_dir, qa_dir):
        d.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, Any]] = []
    for cid, meta in targets.items():
        slug = meta["slug"]
        src = source_map[slug]
        shutil.copy2(src, work_dir / src.name)
        with Image.open(src) as im:
            master = fit_canvas(im)
            out_master = final_dir / meta["filename"]
            master.save(out_master, format="WEBP", quality=90, method=6)
            preview = master.copy()
            preview.thumbnail((PREVIEW, PREVIEW), Image.Resampling.LANCZOS)
            cache_name = f"{slug}-{PREVIEW}x{PREVIEW}.webp"
            preview_path = qa_dir / cache_name
            final_cache = final_dir / cache_name
            preview.save(preview_path, format="WEBP", quality=90, method=6)
            preview.save(final_cache, format="WEBP", quality=90, method=6)
        bg = classify_background(out_master.read_bytes())
        row = {
            "category_id": cid,
            "name": meta["name"],
            "slug": slug,
            "parent_id": meta["parent_id"],
            "parent_name": meta["parent_name"],
            "filename": meta["filename"],
            "cache_filename": cache_name,
            "oc_image": meta["oc_image"],
            "dimensions": f"{TARGET_W}x{TARGET_H}",
            "bytes": out_master.stat().st_size,
            "cache_bytes": preview_path.stat().st_size,
            "sha256": sha256_file(out_master),
            "cache_sha256": sha256_file(preview_path),
            "background_classification": bg,
            "composer_source": str(src),
            "generation_mode": "COMPOSER_ONLY_NO_API",
            "external_api_calls": 0,
        }
        rows.append(row)
    write_json(DEPLOYMENT_ROOT / "image-final" / "final-image-manifest.json", rows)
    write_json(
        DEPLOYMENT_ROOT / "image-generation" / "composer-image-method.json",
        {
            "tools_used": ["Cursor Composer GenerateImage", "Python 3 Pillow"],
            "external_api_calls": 0,
            "images": rows,
            "generated_at": utc_now(),
        },
    )
    return rows


def phase_image_qa(rows: list[dict[str, Any]]) -> dict[str, Any]:
    from PIL import Image

    qa_rows = []
    all_pass = True
    for row in rows:
        master = DEPLOYMENT_ROOT / "image-final" / row["filename"]
        preview = DEPLOYMENT_ROOT / "image-final" / row["cache_filename"]
        checks = {
            "exists": master.exists() and preview.exists(),
            "dimensions_1800x1200": False,
            "format_webp": row["filename"].endswith(".webp"),
            "not_empty": master.stat().st_size > 8000 if master.exists() else False,
            "background_ok": row.get("background_classification")
            in ("MATCHES_WHITE_BG_STYLE", "PARTIAL_MATCH"),
            "no_bzpm_in_binary": WRONG_BRAND.encode("utf-8") not in master.read_bytes()
            if master.exists()
            else True,
            "not_icon_class": row.get("background_classification") != "PLACEHOLDER_OR_ICON",
        }
        if master.exists():
            with Image.open(master) as im:
                checks["dimensions_1800x1200"] = im.size == (TARGET_W, TARGET_H)
        passed = all(checks.values())
        if not passed:
            all_pass = False
        qa_rows.append(
            {"slug": row["slug"], "checks": checks, "qa_verdict": "PASS" if passed else "FAIL"}
        )
    result = {"rows": qa_rows, "all_pass": all_pass, "checked_at": utc_now()}
    write_json(DEPLOYMENT_ROOT / "image-qa" / "image-qa.json", result)
    if not all_pass:
        raise RuntimeError("IMAGE QA FAILED — see image-qa/image-qa.json")
    return result


def admin_read_category_images(targets: dict[int, dict[str, Any]]) -> list[dict[str, Any]]:
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
            raise RuntimeError("admin login failed")
        token = token_m.group(1)
        admin_base = page.url.split("index.php")[0]
        for cid, meta in targets.items():
            edit = f"{admin_base}index.php?route=catalog/category/edit&user_token={token}&category_id={cid}"
            page.goto(edit, wait_until="domcontentloaded")
            page.wait_for_timeout(1000)
            name = page.locator("#input-name1").input_value() if page.locator("#input-name1").count() else meta["name"]
            img_input = page.locator("#input-image")
            current = img_input.input_value() if img_input.count() else ""
            rows.append(
                {
                    "category_id": cid,
                    "category_name": name,
                    "expected_name": meta["name"],
                    "current_image": current,
                    "target_image": meta["oc_image"],
                    "admin_save_required": current != meta["oc_image"],
                }
            )
        browser.close()
    write_json(DEPLOYMENT_ROOT / "admin-evidence" / "category-image-before.json", rows)
    return rows


def admin_save_category_images(before_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    needed = [r for r in before_rows if r.get("admin_save_required")]
    if not needed:
        write_json(
            DEPLOYMENT_ROOT / "admin-evidence" / "category-image-after.json",
            {"saves": [], "skipped": "all fields already target"},
        )
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
    return saves


def phase_deploy(rows: list[dict[str, Any]]) -> dict[str, Any]:
    secrets = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(secrets)
    uploads = []
    try:
        for row in rows:
            master_local = DEPLOYMENT_ROOT / "image-final" / row["filename"]
            cache_local = DEPLOYMENT_ROOT / "image-final" / row["cache_filename"]
            master_remote = REMOTE_IMAGE_DIR + row["filename"]
            cache_remote = REMOTE_CACHE_DIR + row["cache_filename"]
            master_bytes = master_local.read_bytes()
            cache_bytes = cache_local.read_bytes()
            ftp_upload(ftp, master_remote, master_bytes)
            ftp_upload(ftp, cache_remote, cache_bytes)
            remote_master = ftp_download(ftp, master_remote)
            remote_cache = ftp_download(ftp, cache_remote)
            uploads.append(
                {
                    "slug": row["slug"],
                    "master_remote": master_remote,
                    "cache_remote": cache_remote,
                    "master_sha256_local": sha256_bytes(master_bytes),
                    "master_sha256_remote": sha256_bytes(remote_master),
                    "cache_sha256_local": sha256_bytes(cache_bytes),
                    "cache_sha256_remote": sha256_bytes(remote_cache),
                    "master_match": sha256_bytes(master_bytes) == sha256_bytes(remote_master),
                    "cache_match": sha256_bytes(cache_bytes) == sha256_bytes(remote_cache),
                }
            )
    finally:
        ftp.quit()
    result = {"uploaded_at": utc_now(), "uploads": uploads}
    write_json(DEPLOYMENT_ROOT / "logs" / "deploy.json", result)
    return result


def phase_verify() -> dict[str, Any]:
    ensure_dirs()
    targets = load_target_categories()
    fetch_urls = parent_fetch_urls(targets)
    slugs_by_parent: dict[int, list[dict[str, Any]]] = {}
    for cid, meta in targets.items():
        slugs_by_parent.setdefault(meta["parent_id"], []).append({**meta, "category_id": cid})

    surfaces: dict[str, Any] = {}
    for key, url in fetch_urls.items():
        parent_id = int(key.replace("parent_", ""))
        status, html, _ = http_get(url)
        (DEPLOYMENT_ROOT / "html-after" / f"{key}.html").write_text(html, encoding="utf-8")
        cards = parse_hub_cards(html)
        child_checks = []
        for meta in slugs_by_parent.get(parent_id, []):
            slug = meta["slug"]
            hit = next((c for c in cards if c["slug"] == slug), None)
            img = (hit or {}).get("img") or ""
            ok = bool(hit) and "placeholder" not in img.lower() and slug in img
            cls = "MISSING"
            http_img = None
            if img:
                try:
                    img_url = img if img.startswith("http") else PRODUCTION_URL.rstrip("/") + img
                    http_img, data, _ = http_get_bytes(img_url)
                    cls = classify_background(data)
                    (DEPLOYMENT_ROOT / "verification" / f"after-{slug}.webp").write_bytes(data)
                except Exception as exc:
                    cls = f"ERROR:{exc}"
            child_checks.append(
                {
                    "category_id": meta["category_id"],
                    "name": meta["name"],
                    "slug": slug,
                    "parent_id": parent_id,
                    "present": bool(hit),
                    "img": img,
                    "no_placeholder": "placeholder" not in img.lower(),
                    "slug_in_img": slug in img,
                    "image_http": http_img,
                    "classification": cls,
                    "pass": ok and cls in ("MATCHES_WHITE_BG_STYLE", "PARTIAL_MATCH"),
                }
            )
        bzpm_count = html.count(WRONG_BRAND)
        surfaces[key] = {
            "status": status,
            "url": url,
            "parent_id": parent_id,
            "card_count": len(cards),
            "child_cards": child_checks,
            "public_bzpm_count": bzpm_count,
            "all_children_pass": all(c["pass"] for c in child_checks),
        }

    asset_checks = []
    for cid, meta in targets.items():
        slug = meta["slug"]
        master = f"https://bzpm.ru/image/catalog/Category-image/{meta['filename']}"
        cache = f"https://bzpm.ru/image/cache/catalog/Category-image/{slug}-{PREVIEW}x{PREVIEW}.webp"
        asset_checks.append(
            {
                "category_id": cid,
                "slug": slug,
                "master_ok": http_head_ok(master),
                "cache_ok": http_head_ok(cache),
                "master_url": master,
                "cache_url": cache,
            }
        )

    result = {
        "verified_at": utc_now(),
        "surfaces": surfaces,
        "asset_checks": asset_checks,
        "verdict": (
            "PASS"
            if all(s["all_children_pass"] for s in surfaces.values())
            and all(a["master_ok"] and a["cache_ok"] for a in asset_checks)
            and all(s["public_bzpm_count"] == 0 for s in surfaces.values())
            else "FAIL"
        ),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "post-deploy-verification.json", result)
    return result


def build_source_map(
    targets: dict[int, dict[str, Any]],
    map_pairs: list[str] | None,
) -> dict[str, Path]:
    explicit: dict[str, Path] = {}
    if map_pairs:
        for pair in map_pairs:
            slug, path = pair.split("=", 1)
            explicit[slug.strip()] = Path(path.strip())

    source_map: dict[str, Path] = {}
    for cid, meta in targets.items():
        slug = meta["slug"]
        candidates = [
            explicit.get(slug),
            COMPOSER_ASSETS / f"{slug}.png",
            COMPOSER_ASSETS / f"{slug}.webp",
            COMPOSER_ASSETS / f"{slug}.jpg",
            DEPLOYMENT_ROOT / "image-generation" / f"{slug}.png",
            DEPLOYMENT_ROOT / "image-generation" / f"{slug}.webp",
        ]
        found = next((p for p in candidates if p and p.exists()), None)
        if not found:
            tried = [str(p) for p in candidates if p]
            raise FileNotFoundError(f"Missing composer asset for {slug}. Tried: {tried}")
        source_map[slug] = found
    return source_map


def cmd_audit(_: argparse.Namespace) -> int:
    report = phase_audit()
    print(
        json.dumps(
            {
                "create_new_image_count": report["create_new_image_count"],
                "replace_count": report["replace_count"],
                "keep_count": report["keep_count"],
                "ids": report["visibility_contains_target_ids"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def cmd_normalize(args: argparse.Namespace) -> int:
    targets = load_target_categories()
    source_map = build_source_map(targets, args.map)
    rows = phase_normalize_composer_assets(targets, source_map)
    qa = phase_image_qa(rows)
    print(json.dumps({"normalized": len(rows), "qa": qa["all_pass"]}, ensure_ascii=False, indent=2))
    return 0


def cmd_deploy(_: argparse.Namespace) -> int:
    targets = load_target_categories()
    manifest = json.loads((DEPLOYMENT_ROOT / "image-final" / "final-image-manifest.json").read_text(encoding="utf-8"))
    before = admin_read_category_images(targets)
    deploy = phase_deploy(manifest)
    saves = admin_save_category_images(before)
    verify = phase_verify()
    summary = {
        "ftp_master_uploads": len(deploy["uploads"]),
        "ftp_cache_uploads": len(deploy["uploads"]),
        "admin_saves": len(saves),
        "verify": verify["verdict"],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "deploy-summary.json", summary)
    print(json.dumps({"summary": summary, "saves": saves, "verify": verify}, ensure_ascii=False, indent=2))
    return 0 if verify["verdict"] == "PASS" else 2


def cmd_verify(_: argparse.Namespace) -> int:
    verify = phase_verify()
    print(json.dumps(verify, ensure_ascii=False, indent=2))
    return 0 if verify["verdict"] == "PASS" else 2


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("audit").set_defaults(func=cmd_audit)
    p_norm = sub.add_parser("normalize")
    p_norm.add_argument("--map", action="append", help="slug=path mapping for composer sources")
    p_norm.set_defaults(func=cmd_normalize)
    sub.add_parser("deploy").set_defaults(func=cmd_deploy)
    sub.add_parser("verify").set_defaults(func=cmd_verify)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
