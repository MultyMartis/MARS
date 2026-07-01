#!/usr/bin/env python3
"""Corvonero post-project closure — verified pre-change backup (read-only sources)."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"X:\AI MARS")
STORAGE = Path(r"X:\AI MARS STORAGE")
BACKUP_ROOT = STORAGE / "backups" / "search-ppc"
PILOT = REPO / "projects" / "mars-search-ppc-production" / "pilots" / "corvonero"
CT = REPO / "projects" / "mars-search-ppc-production" / "tools" / "commander-transport"
DOCS = REPO / "projects" / "mars-search-ppc-production" / "docs"
REPORTS = REPO / "projects" / "mars-search-ppc-production" / "reports"
EXPORTS = STORAGE / "exports" / "corvonero"

STORAGE_INCLUDE_DIRS = [
    "CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30",
    "CORVONERO-CLIENT-APPROVAL-PACK-2026-07-01",
    "CORVONERO-FINAL-LANDING-PAGES-TEXT-DOCX-PACK-2026-07-01",
    "CORVONERO-ROMAN-LANDING-PAGES-DOCX-PACK-2026-07-01",
]

CORVONERO_REPORT_PREFIXES = ("REPORT-corvonero-",)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run_git(*args: str) -> str:
    r = subprocess.run(
        ["git", *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=False,
    )
    return r.stdout if r.returncode == 0 else (r.stdout + r.stderr)


def collect_repo_files() -> list[Path]:
    files: list[Path] = []
    for root in (PILOT, CT, DOCS):
        if not root.exists():
            continue
        for p in root.rglob("*"):
            if p.is_file() and ".tools-test-output" not in str(p):
                files.append(p)
    if REPORTS.exists():
        for p in REPORTS.iterdir():
            if p.is_file() and any(p.name.startswith(px) for px in CORVONERO_REPORT_PREFIXES):
                files.append(p)
    return sorted(set(files))


def collect_storage_files() -> list[Path]:
    files: list[Path] = []
    for dname in STORAGE_INCLUDE_DIRS:
        d = EXPORTS / dname
        if not d.exists():
            continue
        for p in d.rglob("*"):
            if p.is_file():
                files.append(p)
    return sorted(files)


def zip_paths(zip_path: Path, base: Path, paths: list[Path]) -> dict:
    entries = []
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in paths:
            arc = p.relative_to(base).as_posix()
            zf.write(p, arc)
            entries.append({"path": arc, "sha256": sha256_file(p), "size_bytes": p.stat().st_size})
    return {"archive": zip_path.name, "file_count": len(entries), "size_bytes": zip_path.stat().st_size, "entries": entries}


def verify_zip(zip_path: Path) -> bool:
    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            bad = zf.testzip()
            return bad is None
    except zipfile.BadZipFile:
        return False


def corvonero_untracked() -> str:
    status = run_git("status", "--short")
    lines = [ln for ln in status.splitlines() if "corvonero" in ln.lower() or "search-ppc" in ln.lower()]
    return "\n".join(lines) + ("\n" if lines else "")


def main() -> int:
    ts = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    backup_dir = BACKUP_ROOT / f"CORVONERO-POST-PROJECT-CLOSURE-PRECHANGE-{ts}"
    if backup_dir.exists():
        print(f"STOP: backup directory already exists: {backup_dir}")
        return 1

    backup_dir.mkdir(parents=True, exist_ok=False)
    head = run_git("rev-parse", "HEAD").strip()
    branch = run_git("branch", "--show-current").strip()

    # Git evidence
    (backup_dir / "GIT-STATUS-PRE-CLOSURE.txt").write_text(run_git("status", "--short"), encoding="utf-8")
    (backup_dir / "GIT-HEAD-PRE-CLOSURE.txt").write_text(head + "\n", encoding="utf-8")
    (backup_dir / "GIT-LOG-PRE-CLOSURE.txt").write_text(run_git("log", "-24", "--oneline", "--decorate"), encoding="utf-8")
    (backup_dir / "GIT-DIFF-STAT-PRE-CLOSURE.txt").write_text(run_git("diff", "--stat"), encoding="utf-8")
    (backup_dir / "GIT-CORVONERO-UNTRACKED-PRE-CLOSURE.txt").write_text(corvonero_untracked(), encoding="utf-8")

    repo_files = collect_repo_files()
    storage_files = collect_storage_files()

    repo_zip = backup_dir / "CORVONERO-REPOSITORY-EVIDENCE-PRE-CLOSURE-v1.zip"
    storage_zip = backup_dir / "CORVONERO-STORAGE-EVIDENCE-PRE-CLOSURE-v1.zip"

    repo_meta = zip_paths(repo_zip, REPO, repo_files)
    storage_meta = zip_paths(storage_zip, STORAGE, storage_files)

    verified = verify_zip(repo_zip) and verify_zip(storage_zip)
    if not verified:
        print("STOP: archive verification failed")
        return 1

    manifest = {
        "schema_version": "corvonero-pre-closure-backup-manifest-v1",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "backup_directory": str(backup_dir),
        "repository_head": head,
        "branch": branch,
        "volume_label": "AI WS",
        "drive": "X:",
        "BACKUP_VERIFIED": True,
        "included_roots": {
            "repository": [
                str(PILOT.relative_to(REPO)),
                str(CT.relative_to(REPO)),
                str(DOCS.relative_to(REPO)),
                "projects/mars-search-ppc-production/reports/REPORT-corvonero-*",
            ],
            "storage": [f"exports/corvonero/{d}" for d in STORAGE_INCLUDE_DIRS],
        },
        "excluded_paths": [
            ".recovery-temp/",
            "workspaces/",
            "unrelated pilot WIP",
            "debug temp files under exports/corvonero/_*",
            "historical campaign packages V2.1-V2.6.1 (storage backup scope = current delivery only)",
        ],
        "archives": {
            "repository": {
                "path": repo_zip.name,
                "sha256": sha256_file(repo_zip),
                "size_bytes": repo_meta["size_bytes"],
                "file_count": repo_meta["file_count"],
            },
            "storage": {
                "path": storage_zip.name,
                "sha256": sha256_file(storage_zip),
                "size_bytes": storage_meta["size_bytes"],
                "file_count": storage_meta["file_count"],
            },
        },
        "protected_manual_files": [
            "02-CORVONERO-CAMPAIGN-STRATEGY-AND-RESEARCH-v1.html",
        ],
        "client_sent_files": [
            "01-CORVONERO-ADS-FOR-CLIENT-APPROVAL-v1.xlsx",
            "02-CORVONERO-CAMPAIGN-STRATEGY-AND-RESEARCH-v1.html",
            "03-CORVONERO-SEMANTIC-APPENDIX-v1.xlsx",
        ],
        "current_deployable_package": "CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30",
        "semantic_authority": "V2.6",
    }

    manifest_path = backup_dir / "CORVONERO-PRE-CLOSURE-BACKUP-MANIFEST-v1.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    sums_lines = []
    for p in sorted(backup_dir.iterdir()):
        if p.is_file():
            sums_lines.append(f"{sha256_file(p)}  {p.name}")
    (backup_dir / "CORVONERO-PRE-CLOSURE-BACKUP-SHA256SUMS-v1.txt").write_text(
        "\n".join(sums_lines) + "\n", encoding="utf-8"
    )

    readme = f"""# Corvonero pre-closure backup

**Created:** {manifest['timestamp']}
**Branch:** {branch}
**HEAD:** {head}
**Volume:** X: (AI WS)

## Archives

| Archive | Files | Size |
|---------|-------|------|
| {repo_zip.name} | {repo_meta['file_count']} | {repo_meta['size_bytes']} bytes |
| {storage_zip.name} | {storage_meta['file_count']} | {storage_meta['size_bytes']} bytes |

## Verification

- Both ZIP archives reopen successfully: **{verified}**
- `BACKUP_VERIFIED`: **true**

## Scope

Current delivery evidence only. Historical packages V2.1–V2.6.1 excluded from storage archive.
Unrelated repository WIP excluded from repository archive.

## Protected artifacts referenced

- Manual-stable strategy HTML
- Client approval pack (2026-07-01)
- V2.6.2 deployable Commander package
- Final landing-page text pack
- Roman production brief pack
"""
    (backup_dir / "README-CORVONERO-PRE-CLOSURE-BACKUP-v1.md").write_text(readme, encoding="utf-8")

    print(json.dumps({"backup_dir": str(backup_dir), "verified": verified, "head": head}, indent=2))
    return 0 if verified else 1


if __name__ == "__main__":
    sys.exit(main())
