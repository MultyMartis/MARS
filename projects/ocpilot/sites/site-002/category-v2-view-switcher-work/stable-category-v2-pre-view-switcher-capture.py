#!/usr/bin/env python3
"""SITE-002 — read-only CATEGORY V2 pre-view-switcher baseline capture (FTP download only)."""
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
BACKUP_DIR = os.path.join(BASE, "backups", "SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER")
REPORT_PATH = os.path.join(BASE, "reports", "SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER.md")
BASELINE_NAME = "SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER"

REMOTE_FILES = {
    "category.twig": "catalog/view/theme/default/template/product/category.twig",
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

    print("Downloading live category baseline files (read-only)...")
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
        "rollback_procedure": [
            f"Upload {BACKUP_DIR}/category.twig -> catalog/view/theme/default/template/product/category.twig",
            f"Upload {BACKUP_DIR}/style.css -> assets/css/style.css",
            f"Upload {BACKUP_DIR}/main.js -> assets/js/main.js",
            "Clear system/storage/cache/template/ on FTP",
            "Verify category PLP grid mode at Premium-600 URL",
            "Verify PDP V4 regression on SPKB SKU",
        ],
    }
    manifest_path = os.path.join(BACKUP_DIR, "stable-category-v2-pre-view-switcher-manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("Manifest:", manifest_path)

    write_report(manifest, manifest_path)
    print("Report:", REPORT_PATH)
    print("Baseline successfully captured")


def write_report(manifest, manifest_path):
    lines = [
        "# REPORT — SITE-002 STABLE CATEGORY V2 PRE-VIEW-SWITCHER BASELINE",
        "",
        f"**Baseline name:** `{manifest['baseline_name']}`",
        "**Site:** SITE-002 (ЗПМ TEST)",
        f"**Environment:** {manifest['environment']}",
        f"**Captured at (UTC):** {manifest['captured_at']}",
        "**Mode:** Read-only — no FTP writes, no deploy",
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
        "## 4. Rollback instructions",
        "",
        "Use when CATEGORY V2 view switcher work must be reverted to pre-pass state.",
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
        "4. Verify category PLP — grid layout unchanged, no view switcher in topbar.",
        "5. Verify PDP V4 — hero, commerce, documents sidebar unchanged.",
        "",
        "## 5. Confirmation",
        "",
        "**Stable CATEGORY V2 pre-view-switcher baseline successfully captured**",
        "",
        f"*Generated {manifest['captured_at']} — read-only capture; site unchanged.*",
    ])

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
