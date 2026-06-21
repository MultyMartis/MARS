#!/usr/bin/env python3
"""SITE-002 — read-only CATEGORY V2.2 stable baseline capture (FTP download only)."""
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
BACKUP_DIR = os.path.join(BASE, "backups", "stable-category-v2.2-2026-06-10")
REPORT_PATH = os.path.join(BASE, "reports", "SITE-002-STABLE-CATEGORY-V2.2-2026-06-10.md")
BASELINE_NAME = "SITE-002-STABLE-CATEGORY-V2.2-2026-06-10"

REMOTE_FILES = {
    "category.twig": "catalog/view/theme/default/template/product/category.twig",
    "productcard.twig": "catalog/view/theme/default/template/product/productcard.twig",
    "product_results.php": "catalog/controller/product/product_results.php",
    "style.css": "assets/css/style.css",
    "main.js": "assets/js/main.js",
}


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

    print("Downloading live CATEGORY V2.2 baseline files (read-only)...")
    for local_name, remote_path in REMOTE_FILES.items():
        data = ftp_download(remote_path)
        local_path = os.path.join(BACKUP_DIR, local_name)
        with open(local_path, "wb") as f:
            f.write(data)
        entry = {
            "local_name": local_name,
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
        "stable_state": [
            "category grid mode works",
            "category list mode works",
            "view switcher Grid/List works",
            "localStorage zpm_category_view works",
            "list-card compactness pass applied",
            "primary specs in list mode work",
            "grid/mobile not broken",
            "PDP V4 not affected",
        ],
        "rollback_procedure": [
            f"Upload {BACKUP_DIR}/category.twig -> catalog/view/theme/default/template/product/category.twig",
            f"Upload {BACKUP_DIR}/productcard.twig -> catalog/view/theme/default/template/product/productcard.twig",
            f"Upload {BACKUP_DIR}/product_results.php -> catalog/controller/product/product_results.php",
            f"Upload {BACKUP_DIR}/style.css -> assets/css/style.css",
            f"Upload {BACKUP_DIR}/main.js -> assets/js/main.js",
            "Clear system/storage/cache/template/ on FTP",
            "Verify category PLP grid + list modes at Premium-600 URL",
            "Verify view switcher and zpm_category_view localStorage",
            "Verify PDP V4 regression on SPKB SKU",
        ],
    }
    manifest_path = os.path.join(BACKUP_DIR, "stable-category-v2.2-manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("Manifest:", manifest_path)

    write_report(manifest, manifest_path)
    print("Report:", REPORT_PATH)
    print("Baseline successfully captured")


def write_report(manifest, manifest_path):
    lines = [
        "# REPORT — SITE-002 STABLE CATEGORY V2.2 BASELINE",
        "",
        f"**Baseline name:** `{manifest['baseline_name']}`",
        "**Site:** SITE-002 (BZPM / ЗПМ TEST)",
        f"**Environment:** {manifest['environment']}",
        f"**Captured at (UTC):** {manifest['captured_at']}",
        "**Mode:** Read-only — no FTP writes, no deploy, no rollback",
        "",
        "---",
        "",
        "## 1. Backup folder",
        "",
        f"`{manifest['backup_dir']}`",
        "",
        "## 2. Included files",
        "",
        "| Local name | Remote path | Size (bytes) |",
        "|------------|-------------|--------------|",
    ]
    for e in manifest["files"]:
        lines.append(f"| `{e['local_name']}` | `{e['remote_path']}` | {e['size']} |")

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
        lines.append(f"| `{e['local_name']}` | `{e['sha256']}` |")

    lines.extend([
        "",
        "## 4. Стабильное состояние (Stable Category V2.2)",
        "",
        "Зафиксировано live-состояние **после** CATEGORY V2.2 list-card compactness pass, **перед** работой над блоком «Подкатегории»:",
        "",
    ])
    for item in manifest["stable_state"]:
        lines.append(f"- {item.capitalize() if item[0].islower() else item}.")

    lines.extend([
        "",
        "**Included scope:** category PLP (grid + list), view switcher, list-card layout/commerce/compactness, primary specs in list mode.",
        "",
        "**Out of scope / unchanged:** PDP V4 templates and assets not in this backup set.",
        "",
        "## 5. Rollback instructions",
        "",
        "Use when subcategory block work must be reverted to pre-subcategory stable V2.2 state.",
        "",
        "1. Verify SHA256 of backup files match §3.",
        "2. Upload each file from backup folder to matching remote path on FTP (`polygonws.beget.tech`):",
        "",
    ])
    for e in manifest["files"]:
        lines.append(f"   - `{e['local_name']}` → `{e['remote_path']}`")

    lines.extend([
        "",
        "3. Clear Twig cache — delete contents of `system/storage/cache/template/`.",
        "4. Hard-refresh browser (CSS/JS cache).",
        "5. Verify category PLP:",
        "   - Grid mode — card grid, commerce, no list-only compact layout.",
        "   - List mode — compact list cards, primary specs visible, no overlap.",
        "   - View switcher — Grid/List toggle; `localStorage` key `zpm_category_view` persists choice.",
        "6. Verify mobile category layout (grid stack, no horizontal overflow).",
        "7. Verify PDP V4 — hero, commerce, documents sidebar unchanged (SPKB SKU).",
        "",
        "## 6. QA summary",
        "",
        "Last verified pass before this baseline: **CATEGORY V2.2 LIST CARD COMPACTNESS** (2026-06-09).",
        "",
        "Reference QA artifact:",
        "`projects/ocpilot/sites/site-002/qa/category-v2.2-list-card-compactness/category-v2.2-list-card-compactness-qa-result.json`",
        "",
        "| Area | Status at capture |",
        "|------|-------------------|",
        "| Grid mode (desktop + mobile) | PASS — card grid, commerce intact |",
        "| List mode (desktop) | PASS — compact cards, primary specs, no overlap |",
        "| View switcher | PASS — Grid/List toggle active |",
        "| localStorage `zpm_category_view` | PASS — persists view choice |",
        "| PDP V4 | PASS — not touched by category V2.2 passes |",
        "",
        "Category probe URL: `https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/`",
        "",
        "## 7. Confirmation",
        "",
        "**Stable Category V2.2 baseline successfully captured**",
        "",
        f"*Generated {manifest['captured_at']} — read-only capture; site unchanged.*",
    ])

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
