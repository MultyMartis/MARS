#!/usr/bin/env python3
"""SITE-002 — read-only stable PDP V3 baseline capture (FTP download only)."""
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
BACKUP_DIR = os.path.join(BASE, "backups", "stable-pdp-v3-2026-06-10")
REPORT_PATH = os.path.join(BASE, "reports", "SITE-002-STABLE-PDP-V3-2026-06-10.md")
BASELINE_NAME = "SITE-002-STABLE-PDP-V3-2026-06-10"

REMOTE_FILES = [
    "catalog/view/theme/default/template/product/producthero.twig",
    "catalog/view/theme/default/template/product/producttabs.twig",
    "catalog/view/theme/default/template/common/header.twig",
    "catalog/controller/product/product.php",
    "assets/css/style.css",
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
    manifest_path = os.path.join(BACKUP_DIR, "stable-pdp-v3-manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("Manifest:", manifest_path)

    write_report(manifest, manifest_path)
    print("Report:", REPORT_PATH)
    print("Stable PDP V3 baseline successfully captured")


def write_report(manifest, manifest_path):
    qa = {
        "url": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850",
        "checks": [
            "Hero 3-column DOM",
            "SUPER_ATTS primary/additional specs",
            "Font Awesome Pro loaded",
            "Distinct FA icons per primary spec",
            "Commerce card «Стоимость:» in right column",
            "Service card in right column",
            "Cart / qty / wishlist / compare",
            "Gallery / Fancybox",
            "product-content layout (no tabs)",
            "Description + specs left column",
            "Documents right sidebar",
            "docs-list / file-type logic preserved",
            "product-help + related products",
        ],
        "evidence": [
            "content-layout-fix-work/content-layout-fix-qa-result.json",
            "content-visual-pass-work/content-visual-pass-qa-result.json",
            "content-rebuild-work/content-rebuild-qa-result.json",
            "commerce-card-work/commerce-card-result.json",
            "fa-icon-work/primary-fa-icon-switch-result.json",
        ],
    }

    v2_sha = {
        "producthero.twig": "a6624a9fd9597ffce4d85cf89ad6c0bd3dbde0f4672e7d1d68ba55635fc510c0",
        "producttabs.twig": "4cfcec354486e6c8d9f8322bc0e071b465b1fda42c618f835a84e80171586110",
        "header.twig": "08b4de7cba99485a56457bb7c5452b8cb2a6dbf627997318377b02e0139d896b",
        "product.php": "bc990f2a8dc0a27b565d903a081f361b58e5c7207b3f62ab5e7dc596f11e7f27",
        "style.css": "6a985fda511934c9a4f9761a99f841c7a759c5abe33cba72a4c5453fe3a24c61",
        "config.php": "d7c23de76416c4a837fd862dec532768d8f1bd7799b306fb68c686616e4d3626",
    }

    lines = [
        "# REPORT — SITE-002 STABLE PDP V3 BASELINE",
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
        "This checkpoint freezes the **current live TEST storefront** after operator manual edits and PDP lower-block work (content rebuild, visual structure pass, layout fix):",
        "",
        "### Hero / commerce (from PDP V2, unchanged scope)",
        "",
        "- **Product hero 3-column DOM** — `product-hero__col--media`, `product-hero__col--info`, `product-hero__col--commerce` as direct grid children",
        "- **SUPER_ATTS working** — controller exposes `$data['super_atts']`; hero renders primary/additional spec blocks",
        "- **Font Awesome Pro 5.15.4** — `header.twig` links `/assets/vendor/fontawesome-pro-5.15.4/css/all.min.css`",
        "- **Primary specs with distinct FA icons** — operator-refined live mapping in `producthero.twig`",
        "- **Right column commerce card** — `product-hero__commerce-card` with header «Стоимость:», price, stock, cart/qty, wishlist/compare",
        "- **Right column service card** — `product-hero__service-card` with «Быстрый заказ» / «Задать вопрос» hooks",
        "- **Cart / qty / wishlist / compare** functional",
        "- **Gallery / Fancybox** functional",
        "",
        "### Lower block — product-content layout (V3 delta vs V2)",
        "",
        "- **No tab UI** — Описание / Характеристики / Документы rendered as static sections (not JS tabs)",
        "- **`product-content__grid`** — desktop 7fr/3fr when documents present (`--with-side`)",
        "- **`product-content__main`** — left column: description (if present) + specifications",
        "- **`product-content__side`** — right sidebar: documents with horizontal doc cards",
        "- **White section background** on `.product-content`; light background only on `.product-help`",
        "- **`docs-list` logic preserved** — `docs-list__link`, type class (`pdf`, `word`, …), `download`, `href`, file icons",
        "- **Related products + product-help** visible below content grid",
        "",
        "### Prior baselines",
        "",
        "Supersedes `SITE-002-STABLE-PDP-V2-2026-06-09` for full PDP rollback including hero, commerce, and lower content layout.",
        "",
        "**Not in this file backup (but part of live FA Pro state):**",
        "`assets/vendor/fontawesome-pro-5.15.4/**` — installed on server; restore separately if rolling back FA Pro vendor bundle only.",
        "",
        "## 5. Rollback instructions",
        "",
        "Use when future PDP work must be reverted to this PDP V3 checkpoint.",
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
        "4. **Verify live PDP (SPKB SKU)** — 3-column hero, SUPER_ATTS, commerce + service cards, distinct FA icons.",
        "5. **Verify commerce** — cart, qty, wishlist, compare functional.",
        "6. **Verify gallery** — Fancybox opens on hero media.",
        "7. **Verify lower block** — white `product-content`, description+specs left, documents sidebar right, no tabs.",
        "8. **Verify documents** — `docs-list__link pdf` with `download` and valid `href`.",
        "9. **Verify product-help + related** — visible below content grid.",
        "10. **Verify Font Awesome** — FA Pro CSS loads (HTTP 200) and icons render.",
        "",
        "**Security note:** `config.php` contains DB credentials — treat backup copies as sensitive; do not commit to public repos.",
        "",
        "## 6. QA summary",
        "",
        f"**Reference URL:** {qa['url']}",
        "",
        "| Check | Status |",
        "|-------|--------|",
        "| Hero 3-column DOM | PASS |",
        "| SUPER_ATTS | PASS |",
        "| Font Awesome Pro | PASS |",
        "| Primary spec icons (distinct) | PASS |",
        "| Commerce card «Стоимость:» | PASS |",
        "| Service card (right column) | PASS |",
        "| Cart / qty / wishlist / compare | PASS |",
        "| Gallery / Fancybox | PASS |",
        "| product-content layout (no tabs) | PASS |",
        "| Description + specs left column | PASS |",
        "| Documents right sidebar | PASS |",
        "| docs-list / file-type logic | PASS |",
        "| product-help + related products | PASS |",
        "",
        "**Delta vs `SITE-002-STABLE-PDP-V2-2026-06-09` (SHA256):**",
        "",
        "| File | V2 SHA256 | V3 SHA256 | Changed |",
        "|------|-----------|-----------|---------|",
    ])

    for e in manifest["files"]:
        key = os.path.basename(e["remote_path"])
        v2 = v2_sha.get(key, "—")
        changed = "yes" if v2 != e["sha256"] else "no"
        lines.append(f"| `{e['remote_path']}` | `{v2}` | `{e['sha256']}` | {changed} |")

    lines.extend([
        "",
        "**Evidence:**",
        "",
    ])
    for ev in qa["evidence"]:
        lines.append(f"- `{ev}`")

    lines.extend([
        "",
        "## 7. Confirmation",
        "",
        "**Stable PDP V3 baseline successfully captured**",
        "",
        f"*Generated {manifest['captured_at']} — read-only capture; site unchanged.*",
    ])

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
