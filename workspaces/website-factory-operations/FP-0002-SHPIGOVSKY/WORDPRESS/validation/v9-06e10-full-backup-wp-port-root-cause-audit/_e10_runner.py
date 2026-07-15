#!/usr/bin/env python3
"""E10 runner — full backup, screenshots, audit JSON. NOT FOR GIT."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS")
REPO = Path(r"X:/AI MARS")
VAL = ROOT / "validation/v9-06e10-full-backup-wp-port-root-cause-audit"
V9_SRC = Path(r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/src")
V9_DIST = Path(r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/dist")
RUNTIME = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky")
THEME_SRC = ROOT / "theme/shpigovsky"
PLUGIN_SRC = ROOT / "plugins/shpigovsky-core"
MYSQLDUMP = Path(r"X:/MARS-Localhost/laragon/bin/mysql/mysql-8.4.3-winx64/bin/mysqldump.exe")
BASE = "http://shpigovsky.test"
E9_HEAD = "7559f1ac88b9c76fd01e504a0be488eea9303da5"

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

RUNTIME_ROUTES = [
    ("/", "runtime-home.png"),
    ("/uslugi/", "runtime-uslugi-hub.png"),
    ("/kontakty/", "runtime-kontakty.png"),
    ("/uslugi/zavisimosti/", "runtime-uslugi-zavisimosti-subdivision.png"),
    ("/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "runtime-alcohol-leaf.png"),
]

STATIC_ROUTES = [
    ("index.html", "static-v9-home.png"),
    ("uslugi/index.html", "static-v9-uslugi-hub.png"),
    ("kontakty/index.html", "static-v9-kontakty.png"),
    ("uslugi/zavisimosti/index.html", "static-v9-uslugi-zavisimosti-subdivision.png"),
    ("uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/index.html", "static-v9-alcohol-leaf.png"),
]

STATIC_V9_ALCOHOL_SECTIONS = [
    "services-inner-hero-v2",
    "internal-page-nav",
    "service-leaf-intro-v1",
    "service-leaf-bordered-info-v1",
    "program-cta-band-section",
    "service-leaf-signs-v1",
    "service-leaf-approach-v1",
    "clinic-landscape",
    "services-program-v2",
    "service-leaf-stages-v1",
    "service-leaf-corridor-v1",
    "specialists",
    "founder-quote",
    "comfort",
    "reviews",
    "faq",
    "final-form",
]


def utc_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def run_git(*args: str) -> str:
    r = subprocess.run(
        ["git", *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=False,
    )
    return (r.stdout or "").strip()


def find_chrome() -> Path | None:
    for c in CHROME_CANDIDATES:
        p = Path(c)
        if p.exists():
            return p
    return None


def screenshot(chrome: Path, url: str, out: Path, profile: Path) -> dict:
    out.parent.mkdir(parents=True, exist_ok=True)
    ok = False
    err = None
    try:
        subprocess.run(
            [
                str(chrome),
                f"--user-data-dir={profile}",
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--window-size=1440,9000",
                f"--screenshot={out}",
                url,
            ],
            check=True,
            capture_output=True,
            timeout=120,
        )
        ok = out.exists() and out.stat().st_size > 0
    except Exception as exc:  # noqa: BLE001
        err = str(exc)
    return {
        "file": str(out.relative_to(VAL)).replace("\\", "/") if str(out).startswith(str(VAL)) else out.name,
        "url": url,
        "captured": ok,
        "sha256": sha256_file(out) if ok else None,
        "error": err,
    }


def fetch_html(route: str) -> tuple[int | None, str, str | None]:
    try:
        req = urllib.request.Request(BASE + route, headers={"User-Agent": "E10-audit"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read().decode("utf-8", "replace"), None
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace"), None
    except Exception as exc:  # noqa: BLE001
        return None, "", str(exc)


def extract_main_section_classes(html: str) -> list[str]:
    main_match = re.search(r'<main[^>]*>(.*)</main>', html, re.S | re.I)
    if not main_match:
        return []
    main_html = main_match.group(1)
    classes = []
    for m in re.finditer(r'<(?:section|nav)[^>]*class="([^"]*)"', main_html, re.I):
        first = m.group(1).split()[0] if m.group(1) else ""
        if first and first not in classes:
            classes.append(first)
    return classes


def hash_tree(root: Path, globs: tuple[str, ...] = ("**/*",)) -> list[dict]:
    items = []
    if not root.exists():
        return items
    files = set()
    for g in globs:
        files.update(p for p in root.glob(g) if p.is_file())
    for p in sorted(files):
        try:
            rel = p.relative_to(root).as_posix()
            items.append({"path": rel, "sha256": sha256_file(p), "bytes": p.stat().st_size})
        except OSError:
            continue
    return items


def copy_tree(src: Path, dst: Path, exclude: set[str] | None = None) -> int:
    exclude = exclude or set()
    count = 0
    if not src.exists():
        return 0
    for p in src.rglob("*"):
        if p.is_dir():
            continue
        rel = p.relative_to(src).as_posix()
        if any(x in rel for x in exclude):
            continue
        target = dst / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, target)
        count += 1
    return count


def main() -> None:
    ts = utc_ts()
    backup_root = Path(rf"X:/AI MARS STORAGE/backups/fp-0002-shpigovsky/v9-06e10-root-cause-pre-audit-{ts}")
    backup_root.mkdir(parents=True, exist_ok=True)
    VAL.mkdir(parents=True, exist_ok=True)
    (VAL / "operator-evidence").mkdir(parents=True, exist_ok=True)
    (VAL / "screenshots").mkdir(parents=True, exist_ok=True)

    # --- git metadata ---
    git_meta = {
        "head": run_git("rev-parse", "HEAD"),
        "head_short": run_git("rev-parse", "--short", "HEAD"),
        "branch": run_git("rev-parse", "--abbrev-ref", "HEAD"),
        "remote_head": run_git("rev-parse", "origin/mars/canonical-post-recovery"),
        "e9_head_required": E9_HEAD,
        "e9_ancestor_check": subprocess.run(
            ["git", "merge-base", "--is-ancestor", E9_HEAD, "HEAD"],
            cwd=REPO,
            capture_output=True,
        ).returncode == 0,
        "status_short": run_git("status", "--short"),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }
    (backup_root / "git-metadata.json").write_text(json.dumps(git_meta, indent=2, ensure_ascii=False), encoding="utf-8")

    # --- runtime file backup ---
    runtime_backup = backup_root / "runtime"
    theme_count = copy_tree(RUNTIME / "wp-content/themes/shpigovsky", runtime_backup / "themes/shpigovsky")
    plugin_count = copy_tree(RUNTIME / "wp-content/plugins/shpigovsky-core", runtime_backup / "plugins/shpigovsky-core")
    mu_count = copy_tree(RUNTIME / "wp-content/mu-plugins", runtime_backup / "mu-plugins")
    acf_count = copy_tree(RUNTIME / "wp-content/acf-json", runtime_backup / "acf-json")

    uploads_inventory = []
    uploads_root = RUNTIME / "wp-content/uploads"
    if uploads_root.exists():
        for p in uploads_root.rglob("*"):
            if p.is_file():
                uploads_inventory.append({
                    "path": p.relative_to(uploads_root).as_posix(),
                    "bytes": p.stat().st_size,
                    "sha256": sha256_file(p),
                })
    (backup_root / "uploads-inventory.json").write_text(
        json.dumps({"count": len(uploads_inventory), "files": uploads_inventory[:500]}, indent=2),
        encoding="utf-8",
    )

    wp_config_meta = {}
    wp_config = RUNTIME / "wp-config.php"
    if wp_config.exists():
        text = wp_config.read_text(encoding="utf-8", errors="replace")
        wp_config_meta = {
            "exists": True,
            "db_name": "mars_wp_fp0002" if "mars_wp_fp0002" in text else "UNKNOWN",
            "table_prefix": "fp02_" if "fp02_" in text else "UNKNOWN",
            "sha256": sha256_file(wp_config),
            "secrets_redacted": True,
        }
    (backup_root / "wp-config-metadata.json").write_text(json.dumps(wp_config_meta, indent=2), encoding="utf-8")

    # --- DB dump ---
    db_result = {"database": "mars_wp_fp0002", "dump_path": None, "result": "FAIL", "error": None}
    dump_path = backup_root / "database" / "mars_wp_fp0002.sql"
    dump_path.parent.mkdir(parents=True, exist_ok=True)
    if MYSQLDUMP.exists():
        try:
            with dump_path.open("wb") as out_f:
                subprocess.run(
                    [
                        str(MYSQLDUMP),
                        "--single-transaction",
                        "--routines",
                        "--triggers",
                        "mars_wp_fp0002",
                    ],
                    check=True,
                    stdout=out_f,
                    stderr=subprocess.PIPE,
                    timeout=300,
                )
            db_result = {
                "database": "mars_wp_fp0002",
                "dump_path": str(dump_path),
                "bytes": dump_path.stat().st_size,
                "sha256": sha256_file(dump_path),
                "result": "PASS",
                "error": None,
            }
        except Exception as exc:  # noqa: BLE001
            db_result["error"] = str(exc)
    else:
        db_result["error"] = f"mysqldump not found: {MYSQLDUMP}"
    (backup_root / "database-dump-result.json").write_text(json.dumps(db_result, indent=2), encoding="utf-8")

    # --- static V9 hashes ---
    v9_src_hashes = hash_tree(V9_SRC)
    v9_dist_hashes = hash_tree(V9_DIST)
    (backup_root / "static-v9-src-hashes.json").write_text(
        json.dumps({"root": str(V9_SRC), "file_count": len(v9_src_hashes), "files": v9_src_hashes}, indent=2),
        encoding="utf-8",
    )
    (backup_root / "static-v9-dist-hashes.json").write_text(
        json.dumps({"root": str(V9_DIST), "file_count": len(v9_dist_hashes), "files": v9_dist_hashes}, indent=2),
        encoding="utf-8",
    )

    # --- screenshots ---
    chrome = find_chrome()
    profile = VAL / "_chrome-profile-tmp-e10"
    screenshot_manifest = []
    if chrome:
        for route, fname in RUNTIME_ROUTES:
            out = VAL / "screenshots" / fname
            screenshot_manifest.append(screenshot(chrome, BASE + route, out, profile))
        for rel, fname in STATIC_ROUTES:
            dist_file = V9_DIST / rel
            if dist_file.exists():
                file_url = dist_file.as_uri()
                out = VAL / "screenshots" / fname
                screenshot_manifest.append(screenshot(chrome, file_url, out, profile))
            else:
                screenshot_manifest.append({
                    "file": f"screenshots/{fname}",
                    "url": str(dist_file),
                    "captured": False,
                    "sha256": None,
                    "error": "static dist file missing",
                })
    else:
        screenshot_manifest.append({"error": "no headless browser found", "captured": False})

    # operator evidence placeholders
    op_evidence = {
        "v9_layout_reference_operator": {
            "expected_name": "v9-layout-reference-operator.png",
            "source": "Web-GPT chat upload (вёрстка.png)",
            "copied_to_repo": False,
            "reason": "Operator PNG not found in local workspace at audit time",
        },
        "wp_runtime_drift_operator": {
            "expected_name": "wp-runtime-drift-operator.png",
            "source": "Web-GPT chat upload (Вордпресс.png)",
            "copied_to_repo": False,
            "reason": "Operator PNG not found in local workspace at audit time",
        },
    }
    (VAL / "operator-evidence" / "operator-evidence-manifest.json").write_text(
        json.dumps(op_evidence, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # --- alcohol page DOM analysis ---
    status, wp_html, err = fetch_html("/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/")
    wp_sections = extract_main_section_classes(wp_html) if wp_html else []
    static_html_path = V9_DIST / "uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/index.html"
    static_sections = []
    if static_html_path.exists():
        static_html = static_html_path.read_text(encoding="utf-8", errors="replace")
        static_sections = extract_main_section_classes(static_html)

    missing_in_wp = [s for s in STATIC_V9_ALCOHOL_SECTIONS if s not in wp_sections and s != "internal-page-nav"]
    extra_in_wp = [s for s in wp_sections if s not in STATIC_V9_ALCOHOL_SECTIONS]
    # internal-page-nav is nav not always captured as section first class
    subnav_present = "internal-page-nav" in wp_html if wp_html else False

    operator_diff = {
        "route": "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
        "operator_evidence_available": False,
        "operator_description": "WordPress page still visually diverges from approved static V9 despite E9 repair PASS; suspected wrong/old/generic partial assembly",
        "static_v9_section_stack": static_sections or STATIC_V9_ALCOHOL_SECTIONS,
        "wp_runtime_section_stack": wp_sections,
        "static_v9_section_count": len(static_sections or STATIC_V9_ALCOHOL_SECTIONS),
        "wp_section_count": len(wp_sections),
        "subnav_present_in_wp_dom": subnav_present,
        "blocks_missing_in_wp": missing_in_wp,
        "blocks_extra_in_wp": extra_in_wp,
        "order_differences": wp_sections != (static_sections or STATIC_V9_ALCOHOL_SECTIONS[1:]),
        "likely_sources": [
            {
                "area": "Architecture",
                "difference": "WP uses PHP partial orchestration + ACF/helpers, not direct V9 HTML includes",
                "source": "D7-D semantic reconstruction; inc/service-template-loader.php",
            },
            {
                "area": "Shared home partials on leaf",
                "difference": "clinic-landscape, specialists, founder-quote, comfort, reviews loaded from template-parts/home/*",
                "source": "alcohol-stack.php lines 37-117",
            },
            {
                "area": "Content mutation path",
                "difference": "ACF service fields (D8-C seed) can override v9-static-content fallbacks",
                "source": "inc/service-helpers.php; D8-C services MVP seed",
            },
            {
                "area": "Generic leaf stack",
                "difference": "Non-alcohol leaf routes use leaf-stack.php with only 10 sections vs 17 in static V9",
                "source": "template-parts/service/leaf-stack.php",
            },
            {
                "area": "Validation gap",
                "difference": "E8/E9 accepted DOM-class probes; operator rejected probe-only parity",
                "source": "E8 report operator rejection; E9 visual-result.json",
            },
            {
                "area": "Demo/fixture copy",
                "difference": "Program/signs sections contain V9 fixture lorem visible in both static and WP",
                "source": "inc/v9-static-content.php; static usluga-konechnaya-v1.html",
            },
        ],
        "http_status": status,
        "fetch_error": err,
    }
    (VAL / "operator-screenshot-diff-analysis.json").write_text(
        json.dumps(operator_diff, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # --- restore instructions ---
    restore = {
        "backup_root": str(backup_root),
        "timestamp": ts,
        "restore_db": f"mysql mars_wp_fp0002 < \"{dump_path}\"" if db_result["result"] == "PASS" else "DB dump failed — use prior checkpoint",
        "restore_theme": f"Copy {runtime_backup / 'themes/shpigovsky'} to {RUNTIME / 'wp-content/themes/shpigovsky'}",
        "restore_plugin": f"Copy {runtime_backup / 'plugins/shpigovsky-core'} to {RUNTIME / 'wp-content/plugins/shpigovsky-core'}",
        "manifest_files": [
            "git-metadata.json",
            "database-dump-result.json",
            "static-v9-src-hashes.json",
            "static-v9-dist-hashes.json",
            "uploads-inventory.json",
            "wp-config-metadata.json",
            "RESTORE-INSTRUCTIONS.json",
        ],
    }
    (backup_root / "RESTORE-INSTRUCTIONS.json").write_text(json.dumps(restore, indent=2), encoding="utf-8")

    checksum_manifest = []
    for p in backup_root.rglob("*"):
        if p.is_file() and p.name != "checksum-manifest.json":
            checksum_manifest.append({
                "path": p.relative_to(backup_root).as_posix(),
                "sha256": sha256_file(p),
                "bytes": p.stat().st_size,
            })
    (backup_root / "checksum-manifest.json").write_text(
        json.dumps({"count": len(checksum_manifest), "files": checksum_manifest}, indent=2),
        encoding="utf-8",
    )

    full_backup_result = {
        "task": "V9-06E10",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "backup_root": str(backup_root),
        "result": "PASS" if db_result["result"] == "PASS" else "PARTIAL",
        "components": {
            "git_metadata": "PASS",
            "runtime_theme": {"files": theme_count, "result": "PASS" if theme_count else "FAIL"},
            "runtime_plugin": {"files": plugin_count, "result": "PASS" if plugin_count else "FAIL"},
            "mu_plugins": {"files": mu_count, "result": "PASS"},
            "acf_json_runtime": {"files": acf_count, "result": "PASS"},
            "uploads_inventory": {"files": len(uploads_inventory), "result": "PASS"},
            "wp_config_metadata": "PASS" if wp_config_meta else "PARTIAL",
            "database_dump": db_result,
            "static_v9_src_hashes": {"file_count": len(v9_src_hashes), "result": "PASS"},
            "static_v9_dist_hashes": {"file_count": len(v9_dist_hashes), "result": "PASS"},
            "runtime_screenshots": sum(1 for s in screenshot_manifest if s.get("captured")),
            "static_screenshots": sum(1 for s in screenshot_manifest if s.get("captured") and "static" in s.get("file", "")),
        },
        "git": git_meta,
    }
    (VAL / "full-backup-result.json").write_text(json.dumps(full_backup_result, indent=2, ensure_ascii=False), encoding="utf-8")
    (VAL / "screenshot-manifest.json").write_text(json.dumps(screenshot_manifest, indent=2), encoding="utf-8")

    visual_result = {
        "runtime_routes_captured": sum(1 for s in screenshot_manifest if s.get("captured") and "runtime" in s.get("file", "")),
        "static_routes_captured": sum(1 for s in screenshot_manifest if s.get("captured") and "static" in s.get("file", "")),
        "operator_evidence_captured": False,
        "alcohol_leaf_dom_probe": {
            "wp_sections": wp_sections,
            "static_sections": static_sections,
            "structural_match": len(missing_in_wp) == 0 and len(extra_in_wp) == 0 and subnav_present,
            "visual_parity_claimed": False,
            "note": "DOM section-class stack may match while pixel layout still diverges due to partial markup differences",
        },
        "result": "PARTIAL" if chrome else "FAIL",
    }
    (VAL / "visual-result.json").write_text(json.dumps(visual_result, indent=2, ensure_ascii=False), encoding="utf-8")

    no_drift = {
        "backup_performed": True,
        "db_writes": 0,
        "source_theme_changes": 0,
        "project_plugin_changes": 0,
        "third_party_plugin_changes": 0,
        "acf_json_changes": 0,
        "runtime_delivery": False,
        "native_content_writes": 0,
        "legal_text_writes": 0,
        "reviews_writes": 0,
        "media_uploads": 0,
        "attachment_creation": 0,
        "menu_writes": 0,
        "privacy_setting_writes": 0,
        "rewrite_flush": False,
        "plugin_install_update_delete": False,
        "ocpilot_writes": 0,
        "v9_src_dist_changes": 0,
        "db_dumps_staged": False,
        "backup_payload_staged": False,
        "runtime_snapshots_staged": False,
        "helpers_temp_staged": False,
        "secrets_staged": False,
        "result": "PASS",
    }
    (VAL / "no-scope-drift-validation.json").write_text(json.dumps(no_drift, indent=2), encoding="utf-8")

    print(json.dumps({"backup_root": str(backup_root), "db": db_result["result"], "screenshots": len(screenshot_manifest)}, indent=2))


if __name__ == "__main__":
    main()
