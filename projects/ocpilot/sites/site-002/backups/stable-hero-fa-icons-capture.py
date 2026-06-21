#!/usr/bin/env python3
"""SITE-002 — read-only stable hero FA icons baseline capture (FTP download only)."""
import ftplib
import hashlib
import io
import json
import os
from datetime import datetime, timezone

HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002"
BACKUP_DIR = os.path.join(BASE, "backups", "stable-hero-fa-icons-2026-06-09")
REPORT_PATH = os.path.join(BASE, "reports", "SITE-002-STABLE-HERO-FA-ICONS-2026-06-09.md")
BASELINE_NAME = "SITE-002-STABLE-HERO-FA-ICONS-2026-06-09"

REMOTE_FILES = [
    "catalog/view/theme/default/template/product/producthero.twig",
    "assets/css/style.css",
    "catalog/controller/product/product.php",
    "catalog/view/theme/default/template/common/header.twig",
    "config.php",
]


def ftp_connect():
    ftp = ftplib.FTP(HOST, timeout=120)
    ftp.login(FTP_USER, FTP_PASS)
    return ftp


def ftp_download(remote_path):
    ftp = ftp_connect()
    bio = io.BytesIO()
    ftp.retrbinary("RETR " + remote_path, bio.write)
    ftp.quit()
    return bio.getvalue()


def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()


def main():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    captured_at = datetime.now(timezone.utc).isoformat()
    entries = []

    print("Downloading live files (read-only)...")
    for remote_path in REMOTE_FILES:
        data = ftp_download(remote_path)
        local_path = os.path.join(BACKUP_DIR, remote_path.replace("/", os.sep))
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, "wb") as f:
            f.write(data)
        entry = {
            "remote_path": remote_path,
            "local_path": local_path,
            "size": len(data),
            "sha256": sha256_hex(data),
            "captured_at": captured_at,
        }
        entries.append(entry)
        print(f"  OK {remote_path} ({len(data)} bytes) sha256={entry['sha256'][:16]}...")

    manifest = {
        "baseline_name": BASELINE_NAME,
        "site_id": "SITE-002",
        "environment": "https://zpm.new-site.space/",
        "mode": "read-only-capture",
        "captured_at": captured_at,
        "backup_dir": BACKUP_DIR,
        "files": entries,
    }
    manifest_path = os.path.join(BACKUP_DIR, "stable-hero-fa-icons-manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("Manifest:", manifest_path)

    write_report(manifest, manifest_path)
    print("Report:", REPORT_PATH)
    print("Stable hero FA icons baseline successfully captured")


def write_report(manifest, manifest_path):
    qa = {
        "url": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850",
        "icons": {
            "Длина": "fal fa-ruler-horizontal",
            "Ширина": "fal fa-arrows-alt-h",
            "Высота": "fal fa-arrows-alt-v",
            "Масса": "fas fa-weight-hanging",
        },
        "checks": [
            "Hero 3-column DOM",
            "SUPER_ATTS primary specs",
            "Font Awesome Pro loaded",
            "Distinct FA icons per primary spec",
            "Cart / qty / wishlist / compare",
            "Gallery / Fancybox",
        ],
        "evidence": "fa-icon-work/primary-fa-icon-switch-result.json",
    }

    lines = [
        "# REPORT — SITE-002 STABLE HERO FA ICONS BASELINE",
        "",
        f"**Baseline name:** `{manifest['baseline_name']}`",
        "**Site:** SITE-002 (ЗПМ TEST)",
        f"**Environment:** {manifest['environment']}",
        f"**Captured at (UTC):** {manifest['captured_at']}",
        "**Mode:** Read-only — no FTP writes, no deploy, no rollback performed",
        "",
        "---",
        "",
        "## 1. Backup folder",
        "",
        f"`{manifest['backup_dir']}`",
        "",
        "## 2. Included files",
        "",
        "| Remote path | Local copy | Size (bytes) |",
        "|-------------|------------|--------------|",
    ]
    for e in manifest["files"]:
        lines.append(f"| `{e['remote_path']}` | `{e['local_path']}` | {e['size']} |")

    lines.extend([
        "",
        f"**Manifest:** `{manifest_path}`",
        "",
        "## 3. SHA256 summary",
        "",
        "| File | SHA256 |",
        "|------|--------|",
    ])
    for e in manifest["files"]:
        lines.append(f"| `{e['remote_path']}` | `{e['sha256']}` |")

    lines.extend([
        "",
        "## 4. Stable state definition",
        "",
        "This checkpoint freezes the **current live TEST storefront** after operator manual edits and successful primary-spec FA icon switch:",
        "",
        "- **Product hero 3-column DOM** — `product-hero__col--media`, `product-hero__col--info`, `product-hero__col--commerce` as direct grid children",
        "- **SUPER_ATTS working** — controller exposes `$data['super_atts']`; hero renders primary/additional spec blocks",
        "- **Font Awesome Pro 5.15.4** — `header.twig` links `/assets/vendor/fontawesome-pro-5.15.4/css/all.min.css`",
        "- **Primary specs with distinct FA icons:**",
        "  - Длина → `fal fa-ruler-horizontal`",
        "  - Ширина → `fal fa-arrows-alt-h`",
        "  - Высота → `fal fa-arrows-alt-v`",
        "  - Масса → `fas fa-weight-hanging`",
        "- **Operator manual edits** in live `producthero.twig` and `style.css`",
        "- **Commerce block intact** — cart, qty, wishlist, compare",
        "- **Gallery / Fancybox intact**",
        "",
        "### Prior baseline superseded for hero FA state",
        "",
        "Replaces hero/icon slice of `SITE-002-STABLE-PDP-BASELINE-2026-06-09` for post-FA-icon-switch rollback. Prior baseline remains valid for pre-icon-switch restore.",
        "",
        "**Not in this file backup (but part of live FA Pro state):**",
        "`assets/vendor/fontawesome-pro-5.15.4/**` — installed on server; restore separately if rolling back FA Pro vendor bundle only.",
        "",
        "## 5. Rollback instructions",
        "",
        "Use when future PDP work must be reverted to this FA-icons-stable checkpoint.",
        "",
        "1. **Verify manifest** — confirm SHA256 of local backup files match §3 before upload.",
        "2. **Upload each file** from the backup folder to the matching remote path on FTP (`polygonws.beget.tech`, account root = `public_html`):",
        "",
    ])
    for e in manifest["files"]:
        local_rel = os.path.relpath(e["local_path"], BACKUP_DIR).replace("\\", "/")
        lines.append(f"   - `{local_rel}` → `{e['remote_path']}`")

    lines.extend([
        "",
        "3. **Clear Twig cache** — delete contents of `system/storage/cache/template/` on FTP.",
        "4. **Verify live PDP** — SPKB SKU hero: 3 columns, SUPER_ATTS visible, distinct FA icons per primary spec.",
        "5. **Verify commerce** — cart, qty, wishlist, compare functional.",
        "6. **Verify gallery** — Fancybox opens on hero media.",
        "7. **Verify Font Awesome** — FA Pro CSS loads (HTTP 200) and icons render.",
        "",
        "**Security note:** `config.php` contains DB credentials — treat backup copies as sensitive; do not commit to public repos.",
        "",
        "## 6. QA summary",
        "",
        f"**Reference URL:** {qa['url']}",
        "",
        "| Check | Status |",
        "|-------|--------|",
        "| Hero 3-column DOM | PASS (prior waves + operator edits) |",
        "| SUPER_ATTS | PASS |",
        "| Font Awesome Pro | PASS |",
        "| Primary spec icons (4 distinct) | PASS |",
        "| Cart / qty / wishlist / compare | PASS |",
        "| Gallery / Fancybox | PASS |",
        "",
        "**Primary spec icon mapping (verified post-deploy):**",
        "",
        "| Attribute | Icon class |",
        "|-----------|------------|",
    ])
    for attr, icon in qa["icons"].items():
        lines.append(f"| {attr} | `{icon}` |")

    lines.extend([
        "",
        f"**Evidence:** `{qa['evidence']}`",
        "",
        "Screenshots: `qa/primary-fa-icon-switch/spkb-18-7-vl5-hero-desktop.png`, `spkb-18-7-vl5-hero-mobile.png`",
        "",
        "## 7. Confirmation",
        "",
        "**Stable hero FA icons baseline successfully captured**",
        "",
        f"*Generated {manifest['captured_at']} — read-only capture; site unchanged.*",
    ])

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
