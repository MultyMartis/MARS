#!/usr/bin/env python3
"""SITE-002 — read-only stable PDP baseline capture (FTP download only)."""
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
BACKUP_DIR = os.path.join(BASE, "backups", "stable-baseline-2026-06-09")
REPORT_PATH = os.path.join(BASE, "reports", "SITE-002-STABLE-PDP-BASELINE-2026-06-09.md")
BASELINE_NAME = "SITE-002-STABLE-PDP-BASELINE-2026-06-09"

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
            "path": remote_path,
            "local_path": local_path,
            "size": len(data),
            "sha256": sha256_hex(data),
            "timestamp": captured_at,
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
    manifest_path = os.path.join(BACKUP_DIR, "stable-baseline-manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("Manifest:", manifest_path)

    write_report(manifest, manifest_path)
    print("Report:", REPORT_PATH)
    print("Stable baseline successfully captured")


def write_report(manifest, manifest_path):
    lines = [
        "# REPORT — SITE-002 STABLE PDP BASELINE",
        "",
        f"**Baseline name:** `{manifest['baseline_name']}`",
        f"**Site:** SITE-002 (ЗПМ TEST)",
        f"**Environment:** {manifest['environment']}",
        f"**Captured at (UTC):** {manifest['captured_at']}",
        f"**Mode:** Read-only — no FTP writes, no deploy, no rollback performed",
        "",
        "---",
        "",
        "## 1. Backup folder",
        "",
        f"`{manifest['backup_dir']}`",
        "",
        "## 2. Manifest path",
        "",
        f"`{manifest_path}`",
        "",
        "## 3. Included files",
        "",
        "| Remote path | Local copy | Size (bytes) |",
        "|-------------|------------|--------------|",
    ]
    for e in manifest["files"]:
        lines.append(f"| `{e['path']}` | `{e['local_path']}` | {e['size']} |")

    lines.extend([
        "",
        "## 4. SHA256 summary",
        "",
        "| File | SHA256 |",
        "|------|--------|",
    ])
    for e in manifest["files"]:
        lines.append(f"| `{e['path']}` | `{e['sha256']}` |")

    lines.extend([
        "",
        "## 5. Working state captured in this baseline",
        "",
        "This checkpoint freezes the **current live TEST storefront** after operator-approved PDP work:",
        "",
        "- **Hero 3-column DOM structure** — `product-hero__col--media`, `product-hero__col--info`, `product-hero__col--commerce` as direct grid children",
        "- **Working SUPER_ATTS** — controller exposes `$data['super_atts']`; hero renders primary/additional spec blocks",
        "- **Font Awesome Pro 5.15.4** — `header.twig` links `/assets/vendor/fontawesome-pro-5.15.4/css/all.min.css`",
        "- **Operator manual edits** — all current live content in the five backed-up files",
        "- **Current `producthero.twig` and `style.css`** — post hero-3col baseline rollback state",
        "",
        "### Changes included in baseline (chronology)",
        "",
        "| Work stream | Scope | Evidence |",
        "|-------------|-------|----------|",
        "| Wave 1A / 1A.2 | PDP hero rebuild, scroll sections | `reports/SITE-002-WAVE-1A-*` |",
        "| Wave 1B / 1B.2 | Hero attributes, compactness | `reports/SITE-002-WAVE-1B*` |",
        "| SUPER_ATTS fix | `product.php` + hero presentation | `superatts-work/` |",
        "| Hero 3-column DOM fix | Twig + CSS grid columns | `hero-3col-work/hero-3col-dom-fix-*` |",
        "| Hero 3-col baseline rollback | Reverted quick-props / post-change experiments | `hero-3col-work/hero-3col-baseline-rollback-result.json` |",
        "| Font Awesome Pro install | Vendor bundle + `header.twig` | `fa-pro-work/fa-pro-install-result.json` |",
        "",
        "**Not in this file backup (but part of live FA Pro state):**",
        "`assets/vendor/fontawesome-pro-5.15.4/**` — installed on server; restore separately if rolling back FA Pro only.",
        "",
        "## 6. Full rollback procedure",
        "",
        "Use when future PDP work must be reverted to this checkpoint.",
        "",
        "1. **Verify manifest** — confirm SHA256 of local backup files match §4 before upload.",
        "2. **Upload each file** from the backup folder to the matching remote path on FTP (`polygonws.beget.tech`, account root = `public_html`):",
        "",
    ])
    for e in manifest["files"]:
        local_rel = os.path.relpath(e["local_path"], BACKUP_DIR).replace("\\", "/")
        lines.append(f"   - `{local_rel}` → `{e['path']}`")

    lines.extend([
        "",
        "3. **Clear Twig cache** — delete contents of `system/storage/cache/template/` on FTP.",
        "4. **Verify live PDP** — e.g. SPKB SKU hero: 3 columns, SUPER_ATTS visible, cart/wishlist/compare OK.",
        "5. **Verify Font Awesome** — home/catalog/PDP pages load FA Pro CSS (HTTP 200) and icons render.",
        "",
        "**Security note:** `config.php` contains DB credentials — treat backup copies as sensitive; do not commit to public repos.",
        "",
        "## 7. Confirmation",
        "",
        "**Stable baseline successfully captured**",
        "",
        f"*Generated {manifest['captured_at']} — read-only capture; site unchanged.*",
    ])

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
