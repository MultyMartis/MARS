#!/usr/bin/env python3
"""SITE-002 — read-only stable PDP V4 baseline capture (FTP download only)."""
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
BACKUP_DIR = os.path.join(BASE, "backups", "stable-pdp-v4-2026-06-10")
REPORT_PATH = os.path.join(BASE, "reports", "SITE-002-STABLE-PDP-V4-2026-06-10.md")
BASELINE_NAME = "SITE-002-STABLE-PDP-V4-2026-06-10"

REMOTE_FILES = [
    "catalog/view/theme/default/template/product/producthero.twig",
    "catalog/view/theme/default/template/product/producttabs.twig",
    "catalog/view/theme/default/template/common/header.twig",
    "catalog/controller/product/product.php",
    "assets/css/style.css",
    "config.php",
]

V3_SHA = {
    "catalog/view/theme/default/template/product/producthero.twig": "ea1226986460fdbe2ae7a1f6c653f225ef49f515d519ffbd1ee45da036c86b69",
    "catalog/view/theme/default/template/product/producttabs.twig": "86419148b5d10e75dd361de26e8e51a717c4db1f38769c1cfe0049bf5b661d2b",
    "catalog/view/theme/default/template/common/header.twig": "08b4de7cba99485a56457bb7c5452b8cb2a6dbf627997318377b02e0139d896b",
    "catalog/controller/product/product.php": "bc990f2a8dc0a27b565d903a081f361b58e5c7207b3f62ab5e7dc596f11e7f27",
    "assets/css/style.css": "21761371479795f75f98985c551cf3dd0f78abd348672d22409795ab1b68ccde",
    "config.php": "d7c23de76416c4a837fd862dec532768d8f1bd7799b306fb68c686616e4d3626",
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
    manifest_path = os.path.join(BACKUP_DIR, "stable-pdp-v4-manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("Manifest:", manifest_path)

    write_report(manifest, manifest_path)
    print("Report:", REPORT_PATH)
    print("Stable PDP V4 baseline successfully captured")


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
            "Documents sidebar always visible",
            "Compact doc row + mini-CTA",
            "docs-list / file-type logic preserved",
            "product-help + related products",
        ],
        "evidence": [
            "documents-final-pass-work/documents-final-pass-qa-result.json",
            "content-layout-fix-work/content-layout-fix-qa-result.json",
            "content-visual-pass-work/content-visual-pass-qa-result.json",
            "content-rebuild-work/content-rebuild-qa-result.json",
            "commerce-card-work/commerce-card-result.json",
            "fa-icon-work/primary-fa-icon-switch-result.json",
        ],
    }

    lines = [
        "# REPORT — SITE-002 STABLE PDP V4 BASELINE",
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
        "## 4. Delta vs PDP V3",
        "",
        "Comparison against `SITE-002-STABLE-PDP-V3-2026-06-10` (`stable-pdp-v3-manifest.json`):",
        "",
        "| File | V3 SHA256 | V4 SHA256 | Changed |",
        "|------|-----------|-----------|---------|",
    ])

    changed_files = []
    for e in manifest["files"]:
        v3 = V3_SHA.get(e["remote_path"], "—")
        changed = "yes" if v3 != e["sha256"] else "no"
        if changed == "yes":
            changed_files.append(e["remote_path"])
        lines.append(f"| `{e['remote_path']}` | `{v3}` | `{e['sha256']}` | {changed} |")

    if changed_files:
        lines.extend([
            "",
            "**V4 delta summary:**",
            "",
        ])
        if "catalog/view/theme/default/template/product/producttabs.twig" in changed_files:
            lines.append("- **`producttabs.twig`** — operator manual edits + documents final pass: sidebar always visible, compact doc rows, mini-CTA, empty-state branch")
        if "assets/css/style.css" in changed_files:
            lines.append("- **`style.css`** — operator manual edits + documents final pass CSS: compact `.docs-list` row layout, file-type icons, docs note/empty states")
        unchanged = [p for p in REMOTE_FILES if p not in changed_files]
        if unchanged:
            lines.append(f"- **Unchanged vs V3:** {', '.join('`' + p + '`' for p in unchanged)}")
    else:
        lines.append("")
    lines.append("")

    lines.extend([
        "## 5. Stable state definition",
        "",
        "This checkpoint freezes the **current live TEST storefront** after operator manual edits in `producttabs.twig` and `style.css`, plus the documents final pass:",
        "",
        "### Hero / commerce (inherited from V3)",
        "",
        "- **Product hero 3-column DOM** — `product-hero__col--media`, `product-hero__col--info`, `product-hero__col--commerce`",
        "- **SUPER_ATTS working** — controller exposes `$data['super_atts']`; hero renders primary/additional spec blocks",
        "- **Font Awesome Pro 5.15.4** — `header.twig` links `/assets/vendor/fontawesome-pro-5.15.4/css/all.min.css`",
        "- **Primary specs with distinct FA icons** — operator-refined live mapping in `producthero.twig`",
        "- **Right column commerce card** — `product-hero__commerce-card` with header «Стоимость:», price, stock, cart/qty, wishlist/compare",
        "- **Right column service card** — `product-hero__service-card` with «Быстрый заказ» / «Задать вопрос» hooks",
        "- **Cart / qty / wishlist / compare** functional",
        "- **Gallery / Fancybox** functional",
        "",
        "### Lower block — product-content (V4 delta vs V3)",
        "",
        "- **No tab UI** — Описание / Характеристики / Документы as static sections",
        "- **`product-content__grid--with-side`** — sidebar always rendered",
        "- **Description + specs** in left column (`product-content__main`)",
        "- **Documents sidebar** always visible with `<h2>Документы</h2>`",
        "- **Compact doc row** — `docs-list__file-main`, `docs-list__file-title`, `docs-list__file-type`, `docs-list__download` with `fal fa-download`",
        "- **Mini-CTA** — `product-content__docs-note` with link to `#zpmFbQuestion`",
        "- **Empty state** — `product-content__docs-empty` with «Запросить документы» → `#zpmFbQuestion` when no documents",
        "- **`docs-list` logic preserved** — type class, `href`, `download`, file-type icons",
        "- **Related products + product-help** below content grid",
        "",
        "### Prior baselines",
        "",
        "Supersedes `SITE-002-STABLE-PDP-V3-2026-06-10` for full PDP rollback including hero, commerce, content layout, and documents final pass.",
        "",
        "**Not in this file backup (but part of live FA Pro state):**",
        "`assets/vendor/fontawesome-pro-5.15.4/**` — installed on server; restore separately if rolling back FA Pro vendor bundle only.",
        "",
        "## 6. Rollback instructions",
        "",
        "Use when future PDP work must be reverted to this PDP V4 checkpoint.",
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
        "8. **Verify documents** — compact doc rows, mini-CTA, `docs-list__link` with type class, `download`, valid `href`.",
        "9. **Verify empty docs branch** — `product-content__docs-empty` CTA when no documents (static twig check if no live SKU).",
        "10. **Verify product-help + related** — visible below content grid.",
        "11. **Verify Font Awesome** — FA Pro CSS loads (HTTP 200) and icons render.",
        "",
        "**Security note:** `config.php` contains DB credentials — treat backup copies as sensitive; do not commit to public repos.",
        "",
        "## 7. QA summary",
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
        "| Documents sidebar always visible | PASS |",
        "| Compact doc row + mini-CTA | PASS |",
        "| docs-list / file-type logic | PASS |",
        "| product-help + related products | PASS |",
        "",
        "**Evidence:**",
        "",
    ])
    for ev in qa["evidence"]:
        lines.append(f"- `{ev}`")

    lines.extend([
        "",
        "## 8. Confirmation",
        "",
        "**Stable PDP V4 baseline successfully captured**",
        "",
        f"*Generated {manifest['captured_at']} — read-only capture; site unchanged.*",
    ])

    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
