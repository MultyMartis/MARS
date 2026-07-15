#!/usr/bin/env python3
"""FP-0002 V9-06E29C — backup + source/runtime sync helper."""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY")
EVIDENCE = ROOT / "WORDPRESS/validation/v9-06e29c-excel-structure-completion"
SOURCE_THEME = ROOT / "WORDPRESS/theme/shpigovsky"
SOURCE_PLUGIN = ROOT / "WORDPRESS/plugins/shpigovsky-core"
RUNTIME = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky")
RUNTIME_THEME = RUNTIME / "wp-content/themes/shpigovsky"
RUNTIME_PLUGIN = RUNTIME / "wp-content/plugins/shpigovsky-core"
RUNTIME_ACF = RUNTIME / "wp-content/acf-json"
MYSQLDUMP = Path(r"X:/MARS-Localhost/laragon/bin/mysql/mysql-8.4.3-winx64/bin/mysqldump.exe")
PHP = Path(r"X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe")
V9_FAVICON = Path(r"X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/src/favicon")


def now_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def copy_tree_manifest(src: Path, dst: Path) -> dict:
    dst.mkdir(parents=True, exist_ok=True)
    manifest = {}
    if not src.exists():
        return manifest
    for p in sorted(src.rglob("*")):
        if p.is_file():
            rel = p.relative_to(src).as_posix()
            target = dst / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, target)
            manifest[rel] = sha256_file(p)
    return manifest


def sync_theme_files() -> list[dict]:
    files = [
        "page-templates/generic.php",
        "template-parts/generic/content-page.php",
        "inc/favicon.php",
        "inc/admin-editor.php",
        "functions.php",
    ]
    rows = []
    for rel in files:
        src = SOURCE_THEME / rel
        dst = RUNTIME_THEME / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        rows.append(
            {
                "file": rel,
                "source": str(src),
                "runtime": str(dst),
                "hash": sha256_file(src),
                "match": sha256_file(src) == sha256_file(dst),
            }
        )
    fav_dst = RUNTIME_THEME / "assets/favicon"
    fav_dst.mkdir(parents=True, exist_ok=True)
    for name in ["favicon.svg", "favicon-32x32.png", "favicon.ico", "apple-touch-icon.png"]:
        src = V9_FAVICON / name
        dst = fav_dst / name
        if src.exists():
            shutil.copy2(src, dst)
            (SOURCE_THEME / "assets/favicon").mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, SOURCE_THEME / "assets/favicon" / name)
    return rows


def create_backup(backup_root: Path) -> dict:
    backup_root.mkdir(parents=True, exist_ok=True)
    sql_path = backup_root / "mars_wp_fp0002.sql"
    cmd = [
        str(MYSQLDUMP),
        "-h127.0.0.1",
        "-uroot",
        "mars_wp_fp0002",
        f"--result-file={sql_path}",
    ]
    subprocess.run(cmd, check=True)
    theme_manifest = copy_tree_manifest(RUNTIME_THEME, backup_root / "theme-shpigovsky")
    plugin_manifest = copy_tree_manifest(RUNTIME_PLUGIN, backup_root / "plugin-shpigovsky-core")
    acf_manifest = copy_tree_manifest(RUNTIME_ACF, backup_root / "acf-json")
    return {
        "backup_path": str(backup_root),
        "db_dump": str(sql_path),
        "db_dump_bytes": sql_path.stat().st_size if sql_path.exists() else 0,
        "theme_files": len(theme_manifest),
        "plugin_files": len(plugin_manifest),
        "acf_files": len(acf_manifest),
        "theme_manifest": theme_manifest,
        "plugin_manifest": plugin_manifest,
        "acf_manifest": acf_manifest,
    }


def main() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    stamp = now_stamp()
    backup_root = Path(
        rf"X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29c-structure-completion-pre-{stamp}"
    )
    backup = create_backup(backup_root)
    sync = sync_theme_files()
    runner = EVIDENCE / "_e29c_runner.php"
    proc = subprocess.run(
        [str(PHP), str(runner), "all"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    summary = {
        "backup": backup,
        "sync": sync,
        "runner_exit": proc.returncode,
        "runner_stdout": proc.stdout,
        "runner_stderr": proc.stderr,
    }
    out = EVIDENCE / "execution-summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"backup": backup["backup_path"], "runner_exit": proc.returncode}, ensure_ascii=False))
    if proc.returncode != 0:
        print(proc.stderr)
        raise SystemExit(proc.returncode)


if __name__ == "__main__":
    main()
