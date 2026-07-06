#!/usr/bin/env python3
"""SITE-002 neutral category images white-background refresh — image-only production deploy."""
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

OPERATION_ID = "SITE-002-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-REFRESH-01"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
PARENT_CHECKPOINT = "SITE-002-STABLE-PROD-NEUTRAL-PARENT-CATEGORIES-01"
CHECKPOINT_AFTER = "SITE-002-STABLE-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-REFRESH-01"
)
STORAGE_BASELINE = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-01"
)
COMPOSER_ASSETS = Path(r"C:\Users\MetaCODE ONE\.cursor\projects\x-AI-MARS\assets")
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"

AUDIT_CATEGORIES = {
    331: {
        "name": "Полки настенные и настольные",
        "slug": "polki-nastennye-i-nastolnye",
        "filename": "polki-nastennye-i-nastolnye.webp",
        "oc_image": "catalog/Category-image/polki-nastennye-i-nastolnye.webp",
    },
    354: {
        "name": "Тележки-шпильки и противни",
        "slug": "telezhki-shpilki-i-protivni",
        "filename": "telezhki-shpilki-i-protivni.webp",
        "oc_image": "catalog/Category-image/telezhki-shpilki-i-protivni.webp",
    },
    358: {
        "name": "Шкафы и лари",
        "slug": "shkafy-i-lari",
        "filename": "shkafy-i-lari.webp",
        "oc_image": "catalog/Category-image/shkafy-i-lari.webp",
    },
    86: {
        "name": "Стеллажи",
        "slug": "stellazhi",
        "filename": "stellazhi.webp",
        "oc_image": "catalog/Category-image/stellazhi.webp",
    },
}

APPROVED_STYLE_SLUGS = (
    "podtovarniki-i-podstavki",
    "stoly",
    "telezhki-servirovochnye",
    "zonty-vytyazhnye",
    "moechnye-vanny",
)

REMOTE_IMAGE_DIR = "/public_html/image/catalog/Category-image/"

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
    "admin-evidence",
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
    """Heuristic: sample border/corner pixels for white vs gray/dark backgrounds."""
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


def init_storage() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    manifest = {
        "operation_id": OPERATION_ID,
        "site_id": SITE_ID,
        "environment": ENVIRONMENT,
        "production_url": PRODUCTION_URL,
        "parent_checkpoint": PARENT_CHECKPOINT,
        "change_type": "category_image_refresh_white_background",
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

    audit_rows: list[dict[str, Any]] = []
    for cid, meta in AUDIT_CATEGORIES.items():
        slug = meta["slug"]
        home = home_cards.get(slug, {})
        hub = hub_cards.get(slug, {})
        img_url = home.get("img") or hub.get("img") or ""
        master_url = f"{PRODUCTION_URL.rstrip('/')}/image/{meta['oc_image']}"
        cache_url = img_url
        downloaded: bytes | None = None
        source_url = master_url
        try:
            st, data, _ = http_get_bytes(master_url)
            if st == 200 and data:
                downloaded = data
        except Exception:
            pass
        if not downloaded and cache_url:
            try:
                st, data, _ = http_get_bytes(cache_url)
                if st == 200 and data:
                    downloaded = data
                    source_url = cache_url
            except Exception:
                pass

        row: dict[str, Any] = {
            "category_id": cid,
            "category_name": meta["name"],
            "slug": slug,
            "oc_category_image": meta["oc_image"],
            "remote_filename": meta["filename"],
            "remote_path": f"{REMOTE_IMAGE_DIR}{meta['filename']}",
            "master_url": master_url,
            "cache_url": cache_url,
            "shown_on_homepage": bool(home),
            "shown_on_neutral_hub": bool(hub),
            "download_source": source_url,
        }
        if downloaded:
            local_name = f"audit-{cid}-{meta['filename']}"
            out = DEPLOYMENT_ROOT / "image-reference" / local_name
            out.write_bytes(downloaded)
            row["bytes"] = len(downloaded)
            row["sha256"] = sha256_bytes(downloaded)
            row["visual_classification"] = classify_background(downloaded)
            try:
                from PIL import Image

                with Image.open(io.BytesIO(downloaded)) as im:
                    row["dimensions"] = f"{im.width}x{im.height}"
                    row["format"] = (im.format or "").lower()
            except Exception as exc:
                row["dimensions_error"] = str(exc)
        else:
            row["visual_classification"] = "DOWNLOAD_FAILED"
        audit_rows.append(row)

    write_json(DEPLOYMENT_ROOT / "image-reference" / "current-new-category-images-audit.json", audit_rows)
    md = [
        "# Current new category images audit",
        "",
        f"Generated: {utc_now()}",
        "",
        "| ID | Name | Classification | Dimensions | Bytes | Remote file |",
        "|---:|------|----------------|------------|------:|-------------|",
    ]
    for r in audit_rows:
        md.append(
            f"| {r['category_id']} | {r['category_name']} | {r.get('visual_classification','')} | "
            f"{r.get('dimensions','')} | {r.get('bytes','')} | `{r['remote_filename']}` |"
        )
    write_text(DEPLOYMENT_ROOT / "image-reference" / "current-new-category-images-audit.md", "\n".join(md) + "\n")
    return {"audit": audit_rows, "home_status": home_status, "hub_status": hub_status}


def phase_style_reference() -> dict[str, Any]:
    home_html = (DEPLOYMENT_ROOT / "html-before" / "home.html").read_text(encoding="utf-8")
    cards = parse_hub_cards(home_html)
    refs: list[dict[str, Any]] = []
    for card in cards:
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
            entry: dict[str, Any] = {
                "slug": card["slug"],
                "name": card["name"],
                "url": img_url,
                "filename": fname,
                "bytes": len(data),
                "sha256": sha256_bytes(data),
                "visual_classification": classify_background(data),
            }
            try:
                from PIL import Image

                with Image.open(io.BytesIO(data)) as im:
                    entry["dimensions"] = f"{im.width}x{im.height}"
            except Exception:
                pass
            refs.append(entry)
        except Exception as exc:
            refs.append({"slug": card["slug"], "error": str(exc)})

    write_json(DEPLOYMENT_ROOT / "image-reference" / "approved-style-reference.json", refs)
    md = ["# Approved style reference", "", "| Slug | Name | Classification | Dimensions |", "|------|------|----------------|------------|"]
    for r in refs:
        md.append(f"| {r.get('slug','')} | {r.get('name','')} | {r.get('visual_classification','')} | {r.get('dimensions','')} |")
    write_text(DEPLOYMENT_ROOT / "image-reference" / "approved-style-reference.md", "\n".join(md) + "\n")
    return {"references": refs}


def phase_refresh_scope() -> dict[str, Any]:
    audit = json.loads(
        (DEPLOYMENT_ROOT / "image-reference" / "current-new-category-images-audit.json").read_text(encoding="utf-8")
    )
    scope: list[dict[str, Any]] = []
    for row in audit:
        cid = row["category_id"]
        meta = AUDIT_CATEGORIES[cid]
        vc = row.get("visual_classification", "")
        refresh = vc not in ("MATCHES_WHITE_BG_STYLE",)
        reason = {
            "MATCHES_WHITE_BG_STYLE": "Already matches white-background tile style",
            "PARTIAL_MATCH": "Near-white but inconsistent with approved anchors — refresh for parity",
            "MISMATCH_INTERIOR_BG": "Interior/gray scene background — refresh required",
            "MISMATCH_DARK_BG": "Dark background — refresh required",
            "DOWNLOAD_FAILED": "Cannot verify — manual review",
            "UNKNOWN_NO_PILLOW": "Pillow missing — default refresh for safety",
        }.get(vc, f"Classification {vc}")
        if cid == 331 and vc == "MATCHES_WHITE_BG_STYLE":
            refresh = False
        elif cid == 331 and vc == "PARTIAL_MATCH":
            refresh = False  # keep unless clearly mismatched
        scope.append(
            {
                "category_id": cid,
                "category_name": meta["name"],
                "refresh": refresh,
                "reason": reason,
                "visual_classification": vc,
                "target_output_filename": meta["filename"],
                "target_remote_path": f"{REMOTE_IMAGE_DIR}{meta['filename']}",
                "overwrite_existing": refresh,
                "rollback_file": f"rollback/{meta['filename']}",
            }
        )
    write_json(DEPLOYMENT_ROOT / "manifests" / "refresh-scope.json", scope)
    md = ["# Refresh scope", "", "| ID | Name | Refresh | Reason |", "|---:|------|---------|--------|"]
    for s in scope:
        md.append(f"| {s['category_id']} | {s['category_name']} | {'yes' if s['refresh'] else 'no'} | {s['reason']} |")
    write_text(DEPLOYMENT_ROOT / "manifests" / "refresh-scope.md", "\n".join(md) + "\n")
    return {"scope": scope}


def phase_image_spec() -> dict[str, Any]:
    spec = {
        "target_dimensions": f"{TARGET_W}x{TARGET_H}",
        "cache_dimensions": f"{PREVIEW}x{PREVIEW}",
        "target_format": "webp",
        "target_compression": "quality=90, method=6",
        "naming_convention": "{slug}.webp master; OpenCart cache {slug}-300x300.webp",
        "background_requirement": "white / near-white (#FFFFFF canvas)",
        "subject_framing": "centered product cutout, studio-like",
        "margins_crop": "fit within canvas preserving aspect ratio, white letterbox",
        "visual_consistency_notes": "Match podtovarniki/stoly/telezhki-servirovochnye/zonty/moechnye-vanny tiles",
        "generation_mode": "COMPOSER_ONLY_NO_API",
    }
    write_json(DEPLOYMENT_ROOT / "image-generation" / "image-spec.json", spec)
    write_text(
        DEPLOYMENT_ROOT / "image-generation" / "image-spec.md",
        "# Image spec\n\n" + "\n".join(f"- **{k}:** {v}" for k, v in spec.items()) + "\n",
    )
    return spec


def phase_composer_briefs() -> dict[str, Any]:
    scope = json.loads((DEPLOYMENT_ROOT / "manifests" / "refresh-scope.json").read_text(encoding="utf-8"))
    briefs: list[dict[str, Any]] = []
    subjects = {
        354: "clean stainless steel bakery rack trolley / pin cart with sheet pans, white background, clear product silhouette",
        358: "stainless steel storage cabinet and chest-type neutral storage unit, clean white background, no kitchen scene",
        86: "stainless steel shelving rack, white background, clean frontal or 3/4 product view",
        331: "stainless wall shelves and tabletop shelves, white background",
    }
    forbidden = [
        "dark background",
        "kitchen interior",
        "room scene dominance",
        "text",
        "logos",
        "watermark",
        "low-detail CGI",
        "visible AI artifacts",
    ]
    for row in scope:
        if not row["refresh"]:
            continue
        cid = row["category_id"]
        meta = AUDIT_CATEGORIES[cid]
        briefs.append(
            {
                "category_id": cid,
                "category_name": meta["name"],
                "desired_equipment_visual": subjects.get(cid, meta["name"]),
                "white_background_requirement": True,
                "style_anchor_reference": list(APPROVED_STYLE_SLUGS),
                "forbidden_traits": forbidden,
                "output_filename": meta["filename"],
                "generation_mode": "COMPOSER_ONLY_NO_API",
            }
        )
    write_json(DEPLOYMENT_ROOT / "image-generation" / "composer-briefs.json", briefs)
    md = ["# Composer briefs (COMPOSER_ONLY_NO_API)", ""]
    for b in briefs:
        md += [
            f"## {b['category_name']} ({b['category_id']})",
            f"- Visual: {b['desired_equipment_visual']}",
            f"- Output: `{b['output_filename']}`",
            f"- Forbidden: {', '.join(b['forbidden_traits'])}",
            "",
        ]
    write_text(DEPLOYMENT_ROOT / "image-generation" / "composer-briefs.md", "\n".join(md) + "\n")
    return {"briefs": briefs}


def fit_canvas(im: Any) -> Any:
    from PIL import Image

    canvas = Image.new("RGB", (TARGET_W, TARGET_H), (255, 255, 255))
    im = im.convert("RGB")
    im.thumbnail((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    x = (TARGET_W - im.width) // 2
    y = (TARGET_H - im.height) // 2
    canvas.paste(im, (x, y))
    return canvas


def phase_normalize_images() -> dict[str, Any]:
    """Normalize Composer-generated assets from assets folder to image-final."""
    from PIL import Image

    scope = json.loads((DEPLOYMENT_ROOT / "manifests" / "refresh-scope.json").read_text(encoding="utf-8"))
    to_refresh = [s for s in scope if s["refresh"]]
    if not to_refresh:
        return {"processed": 0, "message": "No images to refresh"}

    COMPOSER_ASSETS.mkdir(parents=True, exist_ok=True)
    gen_dir = DEPLOYMENT_ROOT / "image-generation"
    out_dir = DEPLOYMENT_ROOT / "image-final"
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest: list[dict[str, Any]] = []
    for row in to_refresh:
        cid = row["category_id"]
        meta = AUDIT_CATEGORIES[cid]
        fname = meta["filename"]
        src = COMPOSER_ASSETS / fname
        if not src.exists():
            # try png variant
            png = COMPOSER_ASSETS / fname.replace(".webp", ".png")
            if png.exists():
                src = png
            else:
                raise FileNotFoundError(f"Composer asset missing for {fname}: expected {COMPOSER_ASSETS / fname}")

        import shutil

        shutil.copy2(src, gen_dir / src.name)
        with Image.open(src) as im:
            master = fit_canvas(im)
            out_master = out_dir / fname
            master.save(out_master, format="WEBP", quality=90, method=6)
            preview = master.copy()
            preview.thumbnail((PREVIEW, PREVIEW), Image.Resampling.LANCZOS)
            preview_path = out_dir / f"{meta['slug']}-{PREVIEW}x{PREVIEW}.webp"
            preview.save(preview_path, format="WEBP", quality=90, method=6)

        qa = "PASS" if classify_background(out_master.read_bytes()) in ("MATCHES_WHITE_BG_STYLE", "PARTIAL_MATCH") else "REVIEW"
        manifest.append(
            {
                "category_id": cid,
                "category_name": meta["name"],
                "filename": fname,
                "dimensions": f"{TARGET_W}x{TARGET_H}",
                "bytes": out_master.stat().st_size,
                "sha256": sha256_file(out_master),
                "generation_mode": "COMPOSER_ONLY_NO_API",
                "target_remote_path": f"{REMOTE_IMAGE_DIR}{fname}",
                "oc_category_image": meta["oc_image"],
                "qa_note": qa,
            }
        )

    write_json(out_dir / "final-image-manifest.json", manifest)
    md = ["# Final image manifest", "", "| Category | File | QA | SHA-256 | Bytes |", "|---|---|---|---|---:|"]
    for row in manifest:
        md.append(
            f"| {row['category_name']} | {row['filename']} | {row['qa_note']} | `{row['sha256'][:16]}…` | {row['bytes']} |"
        )
    write_text(out_dir / "final-image-manifest.md", "\n".join(md) + "\n")
    review = [m for m in manifest if m["qa_note"] != "PASS"]
    if review:
        raise RuntimeError(f"QA REVIEW required for: {[r['filename'] for r in review]}")
    return {"processed": len(manifest), "manifest": manifest}


def phase_implementation_plan() -> None:
    scope = json.loads((DEPLOYMENT_ROOT / "manifests" / "refresh-scope.json").read_text(encoding="utf-8"))
    refresh_files = [s["target_output_filename"] for s in scope if s["refresh"]]
    plan = {
        "approach": "A_overwrite_existing_masters",
        "rationale": "oc_category.image already points to Category-image/*.webp from Run 4.195; overwrite masters only",
        "admin_saves_required": False,
        "category_visibility_change": False,
        "steps": [
            "backup remote masters via FTP",
            "upload refreshed webp to /public_html/image/catalog/Category-image/",
            "verify homepage + neutral hub tile images HTTP 200",
        ],
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "implementation-plan.json", plan)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md",
        "# Implementation plan\n\nOverwrite existing category WebP masters; no admin field changes.\n",
    )
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "files-to-change.json",
        {"remote_files": [f"{REMOTE_IMAGE_DIR}{f}" for f in refresh_files]},
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "admin-actions.json", {"category_image_fields": [], "admin_saves_by_cursor": 0})
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.json",
        {
            "categories_refreshed": [s["category_id"] for s in scope if s["refresh"]],
            "files_to_overwrite": refresh_files,
            "admin_saves": 0,
            "layout_changes": 0,
            "seo_changes": 0,
            "rollback": "restore backup/*.webp",
        },
    )
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "dry-run.md",
        "# Dry-run\n\n"
        + "\n".join(f"- Overwrite `{f}`" for f in refresh_files)
        + "\n- No admin / layout / SEO changes\n",
    )


def phase_backup() -> dict[str, Any]:
    secrets = parse_production_secrets(SECRETS_PATH)
    scope = json.loads((DEPLOYMENT_ROOT / "manifests" / "refresh-scope.json").read_text(encoding="utf-8"))
    ftp = ftp_connect(secrets)
    backups: list[dict[str, Any]] = []
    try:
        for row in scope:
            fname = row["target_output_filename"]
            remote = f"{REMOTE_IMAGE_DIR}{fname}"
            try:
                data = ftp_download(ftp, remote)
            except ftplib.error_perm as exc:
                backups.append({"filename": fname, "error": str(exc)})
                continue
            backup_path = DEPLOYMENT_ROOT / "backup" / fname
            rollback_path = DEPLOYMENT_ROOT / "rollback" / fname
            backup_path.write_bytes(data)
            rollback_path.write_bytes(data)
            pre_path = DEPLOYMENT_ROOT / "verification" / "pre-upload" / fname
            pre_path.write_bytes(data)
            backups.append(
                {
                    "filename": fname,
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                    "backup_path": str(backup_path),
                    "rollback_path": str(rollback_path),
                }
            )
    finally:
        ftp.quit()
    write_json(DEPLOYMENT_ROOT / "backup" / "backup-manifest.json", backups)
    return {"backups": backups}


def phase_deploy() -> dict[str, Any]:
    secrets = parse_production_secrets(SECRETS_PATH)
    scope = json.loads((DEPLOYMENT_ROOT / "manifests" / "refresh-scope.json").read_text(encoding="utf-8"))
    to_refresh = [s for s in scope if s["refresh"]]
    if not to_refresh:
        return {"uploads": 0, "message": "nothing to deploy"}

    ftp = ftp_connect(secrets)
    uploads: list[dict[str, Any]] = []
    try:
        for row in to_refresh:
            fname = row["target_output_filename"]
            remote = f"{REMOTE_IMAGE_DIR}{fname}"
            backup_path = DEPLOYMENT_ROOT / "backup" / fname
            local = DEPLOYMENT_ROOT / "image-final" / fname
            if not backup_path.exists():
                raise RuntimeError(f"STOP — backup missing for {fname}")
            if not local.exists():
                raise FileNotFoundError(local)
            try:
                live = ftp_download(ftp, remote)
            except ftplib.error_perm:
                live = b""
            backup_sha = sha256_file(backup_path)
            if live and sha256_bytes(live) != backup_sha:
                raise RuntimeError(f"STOP — LIVE IMAGE CHANGED SINCE BACKUP: {fname}")
            ftp_upload(ftp, remote, local.read_bytes())
            uploads.append(
                {
                    "filename": fname,
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
    scope = json.loads((DEPLOYMENT_ROOT / "manifests" / "refresh-scope.json").read_text(encoding="utf-8"))
    manifest = []
    if (DEPLOYMENT_ROOT / "image-final" / "final-image-manifest.json").exists():
        manifest = json.loads((DEPLOYMENT_ROOT / "image-final" / "final-image-manifest.json").read_text(encoding="utf-8"))

    for row in scope:
        if not row["refresh"]:
            continue
        slug = AUDIT_CATEGORIES[row["category_id"]]["slug"]
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
        "refreshed_count": len([s for s in scope if s["refresh"]]),
    }
    write_json(DEPLOYMENT_ROOT / "verification" / "post-deploy-verification.json", results)
    md = ["# Post-deploy verification", "", "## Checks", ""]
    for k, v in results["checks"].items():
        md.append(f"- {k}: {v}")
    md += ["", "## Refreshed images", ""]
    for k, v in results["images"].items():
        md.append(f"- **{k}:** {json.dumps(v, ensure_ascii=False)}")
    write_text(DEPLOYMENT_ROOT / "verification" / "post-deploy-verification.md", "\n".join(md) + "\n")
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "phase",
        choices=[
            "init",
            "audit",
            "style-reference",
            "refresh-scope",
            "image-spec",
            "composer-briefs",
            "normalize",
            "implementation-plan",
            "backup",
            "deploy",
            "verify",
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
        print(json.dumps({"audit_rows": len(out["audit"])}, ensure_ascii=False))
        return 0
    if phase == "style-reference":
        out = phase_style_reference()
        print(json.dumps({"refs": len(out["references"])}, ensure_ascii=False))
        return 0
    if phase == "refresh-scope":
        out = phase_refresh_scope()
        print(json.dumps({"scope": out["scope"]}, ensure_ascii=False))
        return 0
    if phase == "image-spec":
        phase_image_spec()
        return 0
    if phase == "composer-briefs":
        phase_composer_briefs()
        return 0
    if phase == "normalize":
        out = phase_normalize_images()
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
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
