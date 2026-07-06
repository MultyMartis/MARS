#!/usr/bin/env python3
"""SITE-002 polki category image fix — single-category image-only production deploy."""
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
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-NEUTRAL-CATEGORY-IMAGE-POLKI-FIX-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
PARENT_CHECKPOINT = "SITE-002-STABLE-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-POLKI-CATEGORY-IMAGE-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEUTRAL-CATEGORY-IMAGE-POLKI-FIX-01"
)
STORAGE_BASELINE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-POLKI-CATEGORY-IMAGE-01"
)
COMPOSER_ASSETS = Path(r"C:\Users\MetaCODE ONE\.cursor\projects\x-AI-MARS\assets")
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

CATEGORY_ID = 331
CATEGORY = {
    "name": "Полки настенные и настольные",
    "slug": "polki-nastennye-i-nastolnye",
    "filename": "polki-nastennye-i-nastolnye.webp",
    "oc_image": "catalog/Category-image/polki-nastennye-i-nastolnye.webp",
}

APPROVED_STYLE_SLUGS = (
    "podtovarniki-i-podstavki",
    "stoly",
    "telezhki-servirovochnye",
    "zonty-vytyazhnye",
    "moechnye-vanny",
    "stellazhi",
    "shkafy-i-lari",
    "telezhki-shpilki-i-protivni",
)

REMOTE_IMAGE_DIR = "/public_html/image/catalog/Category-image/"
REMOTE_CACHE_DIR = "/public_html/image/cache/catalog/Category-image/"

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "image-reference",
    "image-generation",
    "image-final",
    "verification",
    "screenshots",
    "manifests",
    "logs",
    "verification/pre-upload",
    "html-before",
    "html-after",
)

FETCH_URLS = (
    ("home", "https://bzpm.ru/"),
    ("neutral_hub", "https://bzpm.ru/katalog/nejtralnoe-oborudovanie"),
)

TARGET_W, TARGET_H = 1800, 1200
PREVIEW = 300


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


def http_get_bytes(url: str, timeout: int = 45) -> tuple[int, bytes, dict[str, str]]:
    if url.startswith("/"):
        url = PRODUCTION_URL.rstrip("/") + url
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read()
        headers = {k.lower(): v for k, v in resp.headers.items()}
        return resp.status, data, headers


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


def parse_hub_cards(html: str) -> list[dict[str, Any]]:
    cards: list[dict[str, Any]] = []
    for block in re.findall(r'<a[^>]+class="[^"]*zpm-cat-card[^"]*"[^>]*>.*?</a>', html, re.DOTALL | re.IGNORECASE):
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
        for x, y in (
            (2, 2),
            (w - 3, 2),
            (2, h - 3),
            (w - 3, h - 3),
            (w // 2, 2),
            (w // 2, h - 3),
        ):
            r, g, b = im.getpixel((max(0, min(x, w - 1)), max(0, min(y, h - 1))))
            lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
            samples.append(lum)
        avg = statistics.mean(samples)
        spread = max(samples) - min(samples)
        if avg >= 230 and spread < 35:
            return "MATCHES_WHITE_BG_STYLE"
        if avg >= 200:
            return "PARTIAL_MATCH"
        if avg >= 120:
            return "MISMATCH_INTERIOR_BG"
        return "MISMATCH_DARK_BG"


def luminance_audit(data: bytes) -> dict[str, Any]:
    try:
        from PIL import Image
    except ImportError:
        return {"error": "no_pillow"}
    with Image.open(io.BytesIO(data)) as im:
        im = im.convert("RGB")
        w, h = im.size
        cx, cy = w // 2, h // 2
        center = im.getpixel((cx, cy))
        edge = im.getpixel((max(0, w - 5), max(0, h // 2)))
        def lum(px: tuple[int, int, int]) -> float:
            return 0.2126 * px[0] + 0.7152 * px[1] + 0.0722 * px[2]
        return {
            "center_lum": round(lum(center), 1),
            "edge_lum": round(lum(edge), 1),
            "corner_classification": classify_background(data),
        }


def init_storage() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "parent_checkpoint": PARENT_CHECKPOINT,
        "change_type": "single_category_image_refresh_polki",
        "category_id": CATEGORY_ID,
        "category_name": CATEGORY["name"],
        "image_generation_mode": "composer_only_no_api",
        "layout_change_allowed": False,
        "category_structure_change_allowed": False,
        "seo_change_allowed": False,
        "robots_sitemap_change_allowed": False,
        "header_footer_change_allowed": False,
        "product_pdp_change_allowed": False,
        "cron_mail_import_change_allowed": False,
        "db_direct_write_allowed": False,
        "created_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "operation.json", manifest)


def phase_audit() -> dict[str, Any]:
    init_storage()
    home_status, home_html, _ = http_get(FETCH_URLS[0][1])
    hub_status, hub_html, _ = http_get(FETCH_URLS[1][1])
    write_text(DEPLOYMENT_ROOT / "html-before" / "home.html", home_html)
    write_text(DEPLOYMENT_ROOT / "html-before" / "neutral_hub.html", hub_html)

    home_cards = {c["slug"]: c for c in parse_hub_cards(home_html)}
    hub_cards = {c["slug"]: c for c in parse_hub_cards(hub_html)}
    slug = CATEGORY["slug"]
    home = home_cards.get(slug, {})
    hub = hub_cards.get(slug, {})
    master_url = f"{PRODUCTION_URL.rstrip('/')}/image/{CATEGORY['oc_image']}"
    cache_url = home.get("img") or hub.get("img") or ""
    cache_path = f"{REMOTE_CACHE_DIR}{CATEGORY['slug']}-{PREVIEW}x{PREVIEW}.webp"

    downloaded: bytes | None = None
    source_url = master_url
    try:
        st, data, _ = http_get_bytes(master_url)
        if st == 200 and data:
            downloaded = data
    except Exception:
        pass

    cache_data: bytes | None = None
    if cache_url:
        try:
            st, data, _ = http_get_bytes(cache_url)
            if st == 200 and data:
                cache_data = data
        except Exception:
            pass

    row: dict[str, Any] = {
        "category_id": CATEGORY_ID,
        "category_name": CATEGORY["name"],
        "slug": slug,
        "oc_category_image": CATEGORY["oc_image"],
        "remote_filename": CATEGORY["filename"],
        "remote_master_path": f"{REMOTE_IMAGE_DIR}{CATEGORY['filename']}",
        "remote_cache_path": cache_path,
        "master_url": master_url,
        "cache_url": cache_url,
        "shown_on_homepage": bool(home),
        "shown_on_neutral_hub": bool(hub),
        "download_source": source_url,
        "refresh_reason": "Operator confirmed old/interior-scene tile not replaced in Run 4.196; refresh for white-bg parity",
    }

    if downloaded:
        master_local = DEPLOYMENT_ROOT / "source" / CATEGORY["filename"]
        backup_local = DEPLOYMENT_ROOT / "backup" / CATEGORY["filename"]
        rollback_local = DEPLOYMENT_ROOT / "rollback" / CATEGORY["filename"]
        master_local.write_bytes(downloaded)
        backup_local.write_bytes(downloaded)
        rollback_local.write_bytes(downloaded)
        row["master_bytes"] = len(downloaded)
        row["master_sha256"] = sha256_bytes(downloaded)
        row["master_dimensions"] = ""
        row["visual_classification"] = classify_background(downloaded)
        row["luminance_audit"] = luminance_audit(downloaded)
        try:
            from PIL import Image

            with Image.open(io.BytesIO(downloaded)) as im:
                row["master_dimensions"] = f"{im.width}x{im.height}"
                row["format"] = (im.format or "").lower()
        except Exception as exc:
            row["dimensions_error"] = str(exc)
    else:
        row["visual_classification"] = "DOWNLOAD_FAILED"

    if cache_data:
        cache_fname = f"{CATEGORY['slug']}-{PREVIEW}x{PREVIEW}.webp"
        (DEPLOYMENT_ROOT / "source" / cache_fname).write_bytes(cache_data)
        (DEPLOYMENT_ROOT / "backup" / cache_fname).write_bytes(cache_data)
        (DEPLOYMENT_ROOT / "rollback" / cache_fname).write_bytes(cache_data)
        row["cache_bytes"] = len(cache_data)
        row["cache_sha256"] = sha256_bytes(cache_data)
        row["cache_classification"] = classify_background(cache_data)
        try:
            from PIL import Image

            with Image.open(io.BytesIO(cache_data)) as im:
                row["cache_dimensions"] = f"{im.width}x{im.height}"
        except Exception:
            pass

    write_json(DEPLOYMENT_ROOT / "image-reference" / "polki-current-image-audit.json", row)
    md = [
        "# Polki current image audit",
        "",
        f"Generated: {utc_now()}",
        "",
        f"- **Category ID:** {CATEGORY_ID}",
        f"- **Name:** {CATEGORY['name']}",
        f"- **Master path:** `{row.get('remote_master_path','')}`",
        f"- **Cache path:** `{row.get('remote_cache_path','')}`",
        f"- **Master SHA-256:** `{row.get('master_sha256','')}`",
        f"- **Cache SHA-256:** `{row.get('cache_sha256','')}`",
        f"- **Dimensions:** {row.get('master_dimensions','')}",
        f"- **Classification:** {row.get('visual_classification','')}",
        f"- **Luminance:** {json.dumps(row.get('luminance_audit', {}), ensure_ascii=False)}",
        f"- **Refresh reason:** {row.get('refresh_reason','')}",
        "",
    ]
    write_text(DEPLOYMENT_ROOT / "image-reference" / "polki-current-image-audit.md", "\n".join(md))

    refs: list[dict[str, Any]] = []
    for card in parse_hub_cards(home_html):
        if card["slug"] not in APPROVED_STYLE_SLUGS:
            continue
        img_url = card.get("img", "")
        if not img_url:
            continue
        try:
            st, data, _ = http_get_bytes(img_url)
            if st != 200:
                continue
            fname = f"ref-{card['slug']}.webp"
            out = DEPLOYMENT_ROOT / "image-reference" / fname
            out.write_bytes(data)
            refs.append(
                {
                    "slug": card["slug"],
                    "name": card["name"],
                    "url": img_url,
                    "filename": fname,
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                    "visual_classification": classify_background(data),
                }
            )
        except Exception as exc:
            refs.append({"slug": card["slug"], "error": str(exc)})
    write_json(DEPLOYMENT_ROOT / "image-reference" / "approved-style-reference.json", refs)

    return {"audit": row, "references": len(refs), "home_status": home_status, "hub_status": hub_status}


def phase_image_spec() -> dict[str, Any]:
    spec = {
        "category_id": CATEGORY_ID,
        "category_name": CATEGORY["name"],
        "target_dimensions": f"{TARGET_W}x{TARGET_H}",
        "cache_dimensions": f"{PREVIEW}x{PREVIEW}",
        "target_format": "webp",
        "target_compression": "quality=90, method=6",
        "output_filename": CATEGORY["filename"],
        "cache_filename": f"{CATEGORY['slug']}-{PREVIEW}x{PREVIEW}.webp",
        "background_requirement": "white / near-white (#FFFFFF canvas)",
        "subject_framing": "stainless steel wall shelves and tabletop shelves, centered product cutout",
        "visual_consistency_notes": "Match podtovarniki/stoly/telezhki/zonty/moechnye-vanny and refreshed 354/358/86 tiles",
        "generation_mode": "COMPOSER_ONLY_NO_API",
    }
    write_json(DEPLOYMENT_ROOT / "image-generation" / "polki-image-spec.json", spec)
    write_text(
        DEPLOYMENT_ROOT / "image-generation" / "polki-image-spec.md",
        "# Polki image spec\n\n" + "\n".join(f"- **{k}:** {v}" for k, v in spec.items()) + "\n",
    )
    return spec


def phase_composer_brief() -> dict[str, Any]:
    brief = {
        "category_id": CATEGORY_ID,
        "category_name": CATEGORY["name"],
        "desired_equipment_visual": (
            "stainless steel wall shelves and tabletop shelves for professional kitchen / food-service equipment"
        ),
        "white_background_requirement": True,
        "style_anchor_reference": list(APPROVED_STYLE_SLUGS),
        "forbidden_traits": [
            "dark background",
            "kitchen interior",
            "gray interior scene",
            "room scene dominance",
            "text",
            "logos",
            "watermark",
            "people",
            "cartoon/CGI look",
            "visible AI artifacts",
        ],
        "output_filename": CATEGORY["filename"],
        "generation_mode": "COMPOSER_ONLY_NO_API",
    }
    write_json(DEPLOYMENT_ROOT / "image-generation" / "polki-composer-brief.json", brief)
    write_text(
        DEPLOYMENT_ROOT / "image-generation" / "polki-composer-brief.md",
        "# Polki composer brief (COMPOSER_ONLY_NO_API)\n\n"
        f"- **Visual:** {brief['desired_equipment_visual']}\n"
        f"- **Output:** `{brief['output_filename']}`\n"
        f"- **Forbidden:** {', '.join(brief['forbidden_traits'])}\n",
    )
    return brief


def fit_canvas(im: Any) -> Any:
    from PIL import Image

    canvas = Image.new("RGB", (TARGET_W, TARGET_H), (255, 255, 255))
    im = im.convert("RGB")
    im.thumbnail((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    x = (TARGET_W - im.width) // 2
    y = (TARGET_H - im.height) // 2
    canvas.paste(im, (x, y))
    return canvas


def phase_normalize() -> dict[str, Any]:
    from PIL import Image
    import shutil

    fname = CATEGORY["filename"]
    cache_fname = f"{CATEGORY['slug']}-{PREVIEW}x{PREVIEW}.webp"
    src = COMPOSER_ASSETS / fname
    if not src.exists():
        png = COMPOSER_ASSETS / fname.replace(".webp", ".png")
        if png.exists():
            src = png
        else:
            raise FileNotFoundError(f"Composer asset missing: {COMPOSER_ASSETS / fname}")

    gen_dir = DEPLOYMENT_ROOT / "image-generation"
    out_dir = DEPLOYMENT_ROOT / "image-final"
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, gen_dir / src.name)

    with Image.open(src) as im:
        master = fit_canvas(im)
        out_master = out_dir / fname
        master.save(out_master, format="WEBP", quality=90, method=6)
        preview = master.copy()
        preview.thumbnail((PREVIEW, PREVIEW), Image.Resampling.LANCZOS)
        preview_path = out_dir / cache_fname
        preview.save(preview_path, format="WEBP", quality=90, method=6)

    qa = "PASS" if classify_background(out_master.read_bytes()) in ("MATCHES_WHITE_BG_STYLE", "PARTIAL_MATCH") else "REVIEW"
    manifest = {
        "filename": fname,
        "cache_filename": cache_fname,
        "category_id": CATEGORY_ID,
        "category_name": CATEGORY["name"],
        "dimensions": f"{TARGET_W}x{TARGET_H}",
        "cache_dimensions": f"{PREVIEW}x{PREVIEW}",
        "bytes": out_master.stat().st_size,
        "cache_bytes": preview_path.stat().st_size,
        "sha256": sha256_file(out_master),
        "cache_sha256": sha256_file(preview_path),
        "generation_mode": "COMPOSER_ONLY_NO_API",
        "target_master_path": f"{REMOTE_IMAGE_DIR}{fname}",
        "target_cache_path": f"{REMOTE_CACHE_DIR}{cache_fname}",
        "oc_category_image": CATEGORY["oc_image"],
        "visual_qa": qa,
    }
    write_json(out_dir / "final-image-manifest.json", manifest)
    write_text(
        out_dir / "final-image-manifest.md",
        "# Final image manifest\n\n"
        f"- **File:** {fname}\n"
        f"- **Dimensions:** {manifest['dimensions']}\n"
        f"- **Bytes:** {manifest['bytes']}\n"
        f"- **SHA-256:** `{manifest['sha256']}`\n"
        f"- **Cache:** {cache_fname} ({manifest['cache_bytes']} bytes)\n"
        f"- **QA:** {qa}\n"
        f"- **Mode:** COMPOSER_ONLY_NO_API\n",
    )
    if qa != "PASS":
        raise RuntimeError("POLKI IMAGE FIX PARTIAL — OPERATOR VISUAL REVIEW REQUIRED")
    return manifest


def phase_implementation_plan() -> None:
    fname = CATEGORY["filename"]
    cache_fname = f"{CATEGORY['slug']}-{PREVIEW}x{PREVIEW}.webp"
    plan = {
        "approach": "overwrite_master_and_cache",
        "rationale": "OpenCart does not auto-regenerate cache on master replace (Run 4.196 lesson)",
        "admin_saves_required": False,
        "steps": [
            "backup remote master + cache via FTP",
            f"upload {fname} to {REMOTE_IMAGE_DIR}",
            f"upload {cache_fname} to {REMOTE_CACHE_DIR}",
            "verify homepage + neutral hub",
        ],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "implementation-plan.json", plan)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md",
        "# Implementation plan\n\nOverwrite master and cache WebP for category 331 only.\n",
    )
    files = {
        "remote_files": [
            f"{REMOTE_IMAGE_DIR}{fname}",
            f"{REMOTE_CACHE_DIR}{cache_fname}",
        ]
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "files-to-change.json", files)

    audit = json.loads(
        (DEPLOYMENT_ROOT / "image-reference" / "polki-current-image-audit.json").read_text(encoding="utf-8")
    )
    dry = {
        "category_id": CATEGORY_ID,
        "files_to_overwrite": [fname, cache_fname],
        "backup_master_sha256": audit.get("master_sha256"),
        "backup_cache_sha256": audit.get("cache_sha256"),
        "prepared_master_sha256": sha256_file(DEPLOYMENT_ROOT / "image-final" / fname)
        if (DEPLOYMENT_ROOT / "image-final" / fname).exists()
        else None,
        "prepared_cache_sha256": sha256_file(DEPLOYMENT_ROOT / "image-final" / cache_fname)
        if (DEPLOYMENT_ROOT / "image-final" / cache_fname).exists()
        else None,
        "admin_saves": 0,
        "layout_changes": 0,
        "seo_changes": 0,
        "rollback": f"restore rollback/{fname} and rollback/{cache_fname}",
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", dry)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "# Dry-run\n\n"
        f"- Overwrite master `{fname}`\n"
        f"- Overwrite cache `{cache_fname}`\n"
        "- No admin / layout / SEO changes\n",
    )


def phase_backup() -> dict[str, Any]:
    secrets = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(secrets)
    fname = CATEGORY["filename"]
    cache_fname = f"{CATEGORY['slug']}-{PREVIEW}x{PREVIEW}.webp"
    backups: list[dict[str, Any]] = []
    try:
        for remote, local_name in (
            (f"{REMOTE_IMAGE_DIR}{fname}", fname),
            (f"{REMOTE_CACHE_DIR}{cache_fname}", cache_fname),
        ):
            try:
                data = ftp_download(ftp, remote)
            except ftplib.error_perm as exc:
                backups.append({"filename": local_name, "remote": remote, "error": str(exc)})
                continue
            for folder in ("backup", "rollback", "verification/pre-upload"):
                (DEPLOYMENT_ROOT / folder / local_name).write_bytes(data)
            backups.append(
                {
                    "filename": local_name,
                    "remote": remote,
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                }
            )
    finally:
        ftp.quit()
    write_json(DEPLOYMENT_ROOT / "backup" / "backup-manifest.json", backups)
    return {"backups": backups}


def phase_deploy() -> dict[str, Any]:
    secrets = parse_production_secrets(SECRETS_PATH)
    ftp = ftp_connect(secrets)
    fname = CATEGORY["filename"]
    cache_fname = f"{CATEGORY['slug']}-{PREVIEW}x{PREVIEW}.webp"
    uploads: list[dict[str, Any]] = []
    try:
        for remote, local_name in (
            (f"{REMOTE_IMAGE_DIR}{fname}", fname),
            (f"{REMOTE_CACHE_DIR}{cache_fname}", cache_fname),
        ):
            backup_path = DEPLOYMENT_ROOT / "backup" / local_name
            local = DEPLOYMENT_ROOT / "image-final" / local_name
            if not backup_path.exists():
                raise RuntimeError(f"STOP — backup missing for {local_name}")
            if not local.exists():
                raise FileNotFoundError(local)
            try:
                live = ftp_download(ftp, remote)
            except ftplib.error_perm:
                live = b""
            backup_sha = sha256_file(backup_path)
            if live and sha256_bytes(live) != backup_sha:
                raise RuntimeError(f"STOP — LIVE IMAGE CHANGED SINCE BACKUP: {local_name}")
            ftp_upload(ftp, remote, local.read_bytes())
            uploads.append(
                {
                    "filename": local_name,
                    "remote": remote,
                    "local_sha256": sha256_file(local),
                    "backup_sha256": backup_sha,
                    "action": "overwrite",
                }
            )
    finally:
        ftp.quit()
    write_json(DEPLOYMENT_ROOT / "logs" / "deploy.json", {"uploads": uploads, "at": utc_now()})
    return {"uploads": len(uploads), "files": uploads}


def phase_verify() -> dict[str, Any]:
    results: dict[str, Any] = {"urls": {}, "checks": {}, "images": {}}
    for name, url in FETCH_URLS:
        status, body, _ = http_get(url)
        write_text(DEPLOYMENT_ROOT / "html-after" / f"{name}.html", body)
        cards = parse_hub_cards(body)
        results["urls"][name] = {"status": status, "cat_cards": len(cards)}

    home_html = (DEPLOYMENT_ROOT / "html-after" / "home.html").read_text(encoding="utf-8")
    hub_html = (DEPLOYMENT_ROOT / "html-after" / "neutral_hub.html").read_text(encoding="utf-8")
    slug = CATEGORY["slug"]

    for cards, where in ((parse_hub_cards(home_html), "homepage"), (parse_hub_cards(hub_html), "neutral_hub")):
        card = next((c for c in cards if c["slug"] == slug), None)
        if not card:
            continue
        img_url = card.get("img", "")
        try:
            st, data, _ = http_get_bytes(img_url)
            results["images"][f"{slug}_{where}"] = {
                "url": img_url,
                "http_status": st,
                "bytes": len(data),
                "classification": classify_background(data) if data else "EMPTY",
                "sha256": sha256_bytes(data) if data else None,
            }
        except Exception as exc:
            results["images"][f"{slug}_{where}"] = {"url": img_url, "error": str(exc)}

    _, robots_body, _ = http_get("https://bzpm.ru/robots.txt")
    _, sitemap_body, _ = http_get("https://bzpm.ru/sitemap.xml")
    results["checks"] = {
        "body_count_home": home_html.lower().count("<body"),
        "yandex_verification": "yandex-verification" in home_html,
        "metrika": "mc.yandex.ru" in home_html or "ym(" in home_html,
        "robots_200": "Sitemap:" in robots_body,
        "sitemap_xml": sitemap_body.strip().startswith("<?xml"),
        "home_cat_cards": len(parse_hub_cards(home_html)),
        "hub_cat_cards": len(parse_hub_cards(hub_html)),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "post-deploy-verification.json", results)
    md = ["# Post-deploy verification", "", "## Checks", ""]
    for k, v in results["checks"].items():
        md.append(f"- {k}: {v}")
    md += ["", "## Polki images", ""]
    for k, v in results["images"].items():
        md.append(f"- **{k}:** {json.dumps(v, ensure_ascii=False)}")
    write_text(DEPLOYMENT_ROOT / "verification" / "post-deploy-verification.md", "\n".join(md))
    return results


def phase_baseline_copy() -> None:
    STORAGE_BASELINE.mkdir(parents=True, exist_ok=True)
    import shutil

    for name in (
        "manifests/operation.json",
        "image-final/final-image-manifest.json",
        "verification/post-deploy-verification.json",
        "backup/backup-manifest.json",
        "logs/deploy.json",
    ):
        src = DEPLOYMENT_ROOT / name
        if src.exists():
            dst = STORAGE_BASELINE / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "phase",
        choices=[
            "init",
            "audit",
            "image-spec",
            "composer-brief",
            "normalize",
            "implementation-plan",
            "backup",
            "deploy",
            "verify",
            "baseline",
            "preflight",
        ],
        nargs="?",
        default="preflight",
    )
    args = parser.parse_args()
    phase = args.phase

    if phase == "preflight":
        init_storage()
        print(json.dumps({"operation_id": OPERATION_ID, "deployment_root": str(DEPLOYMENT_ROOT)}, ensure_ascii=False))
        return 0
    if phase == "init":
        init_storage()
        return 0
    if phase == "audit":
        out = phase_audit()
        print(json.dumps({"audit": out["audit"].get("master_sha256", "")[:16]}, ensure_ascii=False))
        return 0
    if phase == "image-spec":
        phase_image_spec()
        return 0
    if phase == "composer-brief":
        phase_composer_brief()
        return 0
    if phase == "normalize":
        out = phase_normalize()
        print(json.dumps(out, ensure_ascii=False))
        return 0
    if phase == "implementation-plan":
        phase_implementation_plan()
        return 0
    if phase == "backup":
        out = phase_backup()
        print(json.dumps(out, ensure_ascii=False))
        return 0
    if phase == "deploy":
        out = phase_deploy()
        print(json.dumps(out, ensure_ascii=False))
        return 0
    if phase == "verify":
        out = phase_verify()
        print(json.dumps({"checks": out["checks"]}, ensure_ascii=False))
        return 0
    if phase == "baseline":
        phase_baseline_copy()
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
