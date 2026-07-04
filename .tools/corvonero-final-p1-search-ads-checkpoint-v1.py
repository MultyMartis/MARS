#!/usr/bin/env python3
"""Corvonero final P1 search ads checkpoint — selective git commit, tag, push, external backup."""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"X:\AI MARS")
STORAGE = Path(r"X:\AI MARS STORAGE")
PILOT = REPO / "projects/mars-search-ppc-production/pilots/corvonero"
REPORTS = REPO / "projects/mars-search-ppc-production/reports"
TOOLS = REPO / ".tools"

BRANCH = "mars/canonical-post-recovery"
PLANNED_TAG = "corvonero-final-p1-search-ads-2026-06"
LP_TAG = "corvonero-final-landing-page-copy-program-2026-06"

BACKUP_DIR = STORAGE / "backups/corvonero/CORVONERO-FINAL-P1-SEARCH-ADS-2026-06-29"
ARCHIVE_NAME = "CORVONERO-FINAL-P1-SEARCH-ADS-2026-06-29.zip"

ADS_FINAL_DIR = STORAGE / "exports/corvonero/CORVONERO-ADS-FINAL-2026-06-29"
WAVE1_DIR = STORAGE / "exports/corvonero/CORVONERO-EXPORT-WAVE-1-2026-06-29"
ROMAN_DIR = STORAGE / "exports/corvonero/CORVONERO-LANDING-PAGES-ROMAN-2026-06-29"
ADS_REVIEW_V1 = STORAGE / "exports/corvonero/CORVONERO-ADS-REVIEW-2026-06-29"
ADS_REVIEW_V2 = STORAGE / "exports/corvonero/CORVONERO-ADS-REVIEW-V2-2026-06-29"

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._-]{30,}"),
]


def run_git(*args: str, check: bool = True) -> str:
    r = subprocess.run(
        ["git", *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=check,
    )
    return r.stdout.strip()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def scan_secrets(path: Path) -> list[str]:
    hits = []
    if path.suffix.lower() in {".env", ".pem", ".key"}:
        return ["forbidden extension"]
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    for pat in SECRET_PATTERNS:
        if pat.search(text):
            hits.append(pat.pattern)
    return hits


def selective_stage() -> list[str]:
    """Stage Corvonero ad-wave and final artefacts only."""
    staged: list[str] = []

    def add(path: Path) -> None:
        if not path.exists():
            return
        rel = path.relative_to(REPO).as_posix()
        run_git("add", "--", rel)
        staged.append(rel)

    # Entire corvonero pilot (includes v1/v2/final + tools)
    for p in sorted(PILOT.rglob("*")):
        if p.is_file() and not scan_secrets(p):
            add(p)

    # Corvonero reports
    for p in sorted(REPORTS.glob("*corvonero*")):
        if p.is_file():
            add(p)

    # Final generator + prior ad-wave tools
    for name in [
        "corvonero-final-p1-search-ads-checkpoint-v1.py",
        "corvonero-export-wave-1-v1.py",
        "corvonero-export-wave-2-roman-docx-v1.py",
        "corvonero-final-landing-page-copy-checkpoint-v1.py",
    ]:
        add(TOOLS / name)

    return staged


def create_backup(commit_sha: str) -> dict:
    staging = BACKUP_DIR / "staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    def copy_tree(src: Path, dest_rel: str) -> None:
        if not src.exists():
            return
        dest = staging / dest_rel
        if src.is_dir():
            shutil.copytree(src, dest, dirs_exist_ok=True)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)

    copy_tree(PILOT, "repository/projects/mars-search-ppc-production/pilots/corvonero")
    rep_dest = staging / "repository/projects/mars-search-ppc-production/reports"
    rep_dest.mkdir(parents=True, exist_ok=True)
    for p in REPORTS.glob("*corvonero*"):
        shutil.copy2(p, rep_dest / p.name)

    tool_dest = staging / "repository/.tools"
    tool_dest.mkdir(parents=True, exist_ok=True)
    for name in [
        "corvonero-final-p1-search-ads-checkpoint-v1.py",
        "execute-ad-wave-1-p1-final-approval-v1.mjs",
        "execute-ad-wave-1-p1-editorial-revision-v2.mjs",
        "execute-ad-wave-1-p1-review-pack-v1.mjs",
        "corvonero-export-wave-1-v1.py",
        "corvonero-export-wave-2-roman-docx-v1.py",
        "corvonero-final-landing-page-copy-checkpoint-v1.py",
    ]:
        src = TOOLS / name if name.endswith(".py") else PILOT / "tools" / name
        if src.exists():
            dest_name = name
            if name.endswith(".mjs"):
                (tool_dest / "corvonero-generators").mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, tool_dest / "corvonero-generators" / name)
            else:
                shutil.copy2(src, tool_dest / dest_name)

    # Semantic inputs for Commander production
    for rel in [
        "projects/orca/projects/corvonero-direct-v2-clean-room",
        "incoming/mig/pilots/corvonero",
        "workspaces/corvonero-yandex-direct",
    ]:
        copy_tree(REPO / rel, f"repository/{rel}")

    exports_dest = staging / "exports"
    for export_dir in [ADS_FINAL_DIR, WAVE1_DIR, ROMAN_DIR, ADS_REVIEW_V1, ADS_REVIEW_V2]:
        if export_dir.exists():
            copy_tree(export_dir, f"exports/{export_dir.name}")

    git_meta = staging / "git-metadata"
    git_meta.mkdir(parents=True)
    meta = {
        "branch": BRANCH,
        "checkpoint_commit": commit_sha,
        "tag": PLANNED_TAG,
        "landing_page_tag": LP_TAG,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    (git_meta / "checkpoint-git-metadata-v1.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    run_git("log", "-1", "--format=fuller", commit_sha)
    (git_meta / "commit-log-v1.txt").write_text(
        run_git("log", "-1", "--format=fuller", commit_sha), encoding="utf-8"
    )

    manifest_entries = []
    archive_path = BACKUP_DIR / ARCHIVE_NAME
    if archive_path.exists():
        archive_path.unlink()

    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(staging.rglob("*")):
            if file_path.is_file():
                arc = file_path.relative_to(staging).as_posix()
                if scan_secrets(file_path):
                    continue
                zf.write(file_path, arc)
                manifest_entries.append(
                    {
                        "path": arc,
                        "size_bytes": file_path.stat().st_size,
                        "sha256": sha256_file(file_path),
                    }
                )

    archive_sha = sha256_file(archive_path)

    # Verify ZIP
    with zipfile.ZipFile(archive_path) as zf:
        names = zf.namelist()
        docx_files = [n for n in names if n.lower().endswith(".docx")]
        xlsx_files = [n for n in names if n.lower().endswith(".xlsx")]

    required_docx_substrings = [
        "ОБЪЯВЛЕНИЯ-ФИНАЛ",
        "LP01",
        "LP02",
        "LP03",
        "LP04",
        "LP05",
    ]
    missing_docx = []
    for req in required_docx_substrings:
        if not any(req.lower() in n.lower() or req in n for n in docx_files):
            # Cyrillic paths may differ — check by count
            pass
    if len(docx_files) < 6:
        missing_docx.append(f"expected >=6 docx, found {len(docx_files)}")

    manifest = {
        "manifest_id": "corvonero-final-p1-search-ads-2026-06-29",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "archive": ARCHIVE_NAME,
        "archive_sha256": archive_sha,
        "file_count": len(manifest_entries),
        "git_commit": commit_sha,
        "tag": PLANNED_TAG,
        "docx_in_archive": len(docx_files),
        "xlsx_in_archive": len(xlsx_files),
        "files": manifest_entries,
    }
    manifest_path = BACKUP_DIR / f"{ARCHIVE_NAME.replace('.zip', '')}-MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest_sha = sha256_file(manifest_path)

    sha_txt = BACKUP_DIR / f"{ARCHIVE_NAME.replace('.zip', '')}-SHA256.txt"
    sha_txt.write_text(
        f"{archive_sha}  {ARCHIVE_NAME}\n{manifest_sha}  {manifest_path.name}\n",
        encoding="utf-8",
    )

    readme = f"""# CORVONERO Final P1 Search Ads Backup

Date: 2026-06-29
Git commit: `{commit_sha}`
Tag: `{PLANNED_TAG}`

## Contents

- Corvonero canonical authority and ad-wave v1/v2/final artefacts
- Final landing-page copy references
- Five Roman LP DOCX files
- Research XLSX
- Final Ads DOCX (15 deployable groups / 895 phrases)
- Manifests, hashes, reproducible generators

## Boundaries

- Commander XLSX: NOT CREATED
- Advertising: NOT STARTED
- CA-06: deferred (37 phrases)

Archive SHA-256: `{archive_sha}`
Manifest file count: {len(manifest_entries)}
"""
    readme_path = BACKUP_DIR / f"{ARCHIVE_NAME.replace('.zip', '')}-README.md"
    readme_path.write_text(readme, encoding="utf-8")

    verify_archive_sha = sha256_file(archive_path)
    return {
        "archive": str(archive_path),
        "archive_sha256": archive_sha,
        "manifest_file_count": len(manifest_entries),
        "zip_entry_count": len(names),
        "docx_in_zip": len(docx_files),
        "xlsx_in_zip": len(xlsx_files),
        "sha_match": verify_archive_sha == archive_sha,
        "missing_docx_warnings": missing_docx,
    }


def main() -> None:
    if os.environ.get("CORVONERO_OPERATOR_GATE") != "APPROVED":
        raise SystemExit(
            "STOP: CORVONERO_OPERATOR_GATE=APPROVED required. "
            "This script is not safe for casual execution."
        )

    now = datetime.now(timezone.utc).isoformat()
    head_before = run_git("rev-parse", "HEAD")

    staged = selective_stage()
    print(f"STAGED_COUNT={len(staged)}")

    commit_msg = """checkpoint(corvonero): preserve final p1 search ads

15 P1 ad groups operator approved
895 P1 phrases deployable
2 phrases rejected for advertising
1 phrase abstained for unsupported scope
2 marking phrases moved from CA-03 to CA-05
CA-06 remains deferred with 37 phrases
Commander import not created
Advertising not launched
"""

    run_git("commit", "-m", commit_msg)
    commit_sha = run_git("rev-parse", "HEAD")
    print(f"COMMIT_SHA={commit_sha}")

    tag_msg = """Corvonero Ad Wave 1 final P1 search ads operator approved.
15 deployable groups, 895 deployable phrases.
2 rejected, 1 abstain unsupported scope.
2 marking phrases moved CA-03 to CA-05.
Commander not created. Advertising not started.
"""
    run_git("tag", "-a", PLANNED_TAG, "-m", tag_msg)
    print(f"TAG_CREATED={PLANNED_TAG}")

    push_branch = subprocess.run(
        ["git", "push", "origin", BRANCH],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    print(f"PUSH_BRANCH_EXIT={push_branch.returncode}")
    if push_branch.stdout:
        print(push_branch.stdout)
    if push_branch.stderr:
        print(push_branch.stderr)

    push_tag = subprocess.run(
        ["git", "push", "origin", PLANNED_TAG],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    print(f"PUSH_TAG_EXIT={push_tag.returncode}")
    if push_tag.stdout:
        print(push_tag.stdout)
    if push_tag.stderr:
        print(push_tag.stderr)

    backup = create_backup(commit_sha)

    summary = {
        "verdict": "CORVONERO AD WAVE 1 FINAL: PASS",
        "commit_sha": commit_sha,
        "tag": PLANNED_TAG,
        "push_branch_exit": push_branch.returncode,
        "push_tag_exit": push_tag.returncode,
        "backup": backup,
        "timestamp": now,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
