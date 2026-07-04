#!/usr/bin/env python3
"""Corvonero production extensions final checkpoint — selective git, tag, push, external backup."""
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

BRANCH = "mars/canonical-post-recovery"
PLANNED_TAG = "corvonero-final-production-extensions-2026-06"
PRIOR_COMMIT = "508837a02658e357ce18dca777a46231d2575b25"
PRIOR_TAG = "corvonero-final-p1-search-ads-2026-06"

BACKUP_DIR = STORAGE / "backups/corvonero/CORVONERO-FINAL-PRODUCTION-EXTENSIONS-2026-06-29"
ARCHIVE_NAME = "CORVONERO-FINAL-PRODUCTION-EXTENSIONS-2026-06-29.zip"

ADS_FINAL_DIR = STORAGE / "exports/corvonero/CORVONERO-ADS-FINAL-2026-06-29"
WAVE1_DIR = STORAGE / "exports/corvonero/CORVONERO-EXPORT-WAVE-1-2026-06-29"
ROMAN_DIR = STORAGE / "exports/corvonero/CORVONERO-LANDING-PAGES-ROMAN-2026-06-29"

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._-]{30,}"),
]

V1_PREFIXES = [
    "CORVONERO-EXT-W1-FINAL-CAMPAIGN-REGISTER-v1",
    "CORVONERO-EXT-W1-URL-READINESS-v1",
    "CORVONERO-EXT-W1-DISPLAY-PATHS-v1",
    "CORVONERO-EXT-W1-SITELINKS-v1",
    "CORVONERO-EXT-W1-CALLOUTS-v1",
    "CORVONERO-EXT-W1-NEGATIVE-CANDIDATES-v1",
    "CORVONERO-EXT-W1-CROSS-NEGATIVES-v1",
    "CORVONERO-EXT-W1-NEGATIVE-RISK-AUDIT-v1",
    "CORVONERO-EXT-W1-UTM-POLICY-v1",
    "CORVONERO-EXT-W1-CAMPAIGN-SETTINGS-v1",
    "CORVONERO-EXT-W1-IMPORT-PROFILE-v1",
    "CORVONERO-EXT-W1-COMMANDER-READINESS-GATE-v1",
    "CORVONERO-EXT-W1-RESULT-v1",
]

V2_PREFIXES = [
    "CORVONERO-EXT-W1-SITELINKS-v2",
    "CORVONERO-EXT-W1-CALLOUTS-v2",
    "CORVONERO-EXT-W1-NEGATIVE-DEPLOYMENT-v1",
    "CORVONERO-EXT-W1-CROSS-NEGATIVES-v2",
    "CORVONERO-EXT-W1-UTM-POLICY-v2",
    "CORVONERO-EXT-W1-CAMPAIGN-SETTINGS-v2",
    "CORVONERO-EXT-W1-COMMANDER-READINESS-GATE-v2",
    "CORVONERO-EXT-W1-OPERATOR-DECISION-RECEIPT-v1",
    "CORVONERO-EXT-W1-RESULT-v2",
]

REPORT_FILES = [
    "REPORT-corvonero-production-extensions-wave-1-v1.md",
    "REPORT-corvonero-production-extensions-wave-1-operator-decisions-v2.md",
    "REPORT-corvonero-production-extensions-final-checkpoint-v1.md",
]

GENERATORS = [
    PILOT / "tools/execute-ext-wave-1-v1.mjs",
    PILOT / "tools/execute-ext-wave-1-v2-operator-decisions.mjs",
]

CHECKPOINT_FILES = [
    PILOT / "CORVONERO-PRODUCTION-EXTENSIONS-FINAL-CHECKPOINT-v1.md",
    PILOT / "CORVONERO-PRODUCTION-EXTENSIONS-FINAL-CHECKPOINT-v1.json",
]

BACKUP_EXTRA_PILOT_FILES = [
    "CORVONERO-AD-WAVE-1-FINAL-PHRASE-ALLOCATION-v1.json",
    "CORVONERO-AD-WAVE-1-FINAL-PHRASE-ALLOCATION-v1.md",
    "CORVONERO-AD-WAVE-1-FINAL-DEPLOYABILITY-OVERLAY-v1.json",
    "CORVONERO-AD-WAVE-1-FINAL-DEPLOYABILITY-OVERLAY-v1.md",
    "CORVONERO-AD-WAVE-1-P1-FINAL-RESULT-v1.json",
    "CORVONERO-AD-WAVE-1-P1-FINAL-RESULT-v1.md",
    "CORVONERO-LANDING-PAGE-COPY-PROGRAM-CHECKPOINT-v1.json",
    "CORVONERO-LANDING-PAGE-COPY-PROGRAM-CHECKPOINT-v1.md",
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
    if path.suffix.lower() in {".env", ".pem", ".key"}:
        return ["forbidden extension"]
    if re.search(r"credentials|\.secrets|api[_-]?key", path.name, re.I):
        return ["forbidden name pattern"]
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []
    hits = []
    for pat in SECRET_PATTERNS:
        if pat.search(text):
            hits.append(pat.pattern)
    return hits


def collect_selective_paths() -> list[Path]:
    paths: list[Path] = []
    for prefix in V1_PREFIXES:
        paths.extend(sorted(PILOT.glob(f"{prefix}.*")))
    paths.append(PILOT / "CORVONERO-EXT-W1-OPERATOR-DECISION-PACKET-v1.md")
    for prefix in V2_PREFIXES:
        paths.extend(sorted(PILOT.glob(f"{prefix}.*")))
    for name in REPORT_FILES:
        p = REPORTS / name
        if p.exists():
            paths.append(p)
    paths.extend(GENERATORS)
    paths.extend(CHECKPOINT_FILES)
    return [p for p in paths if p.is_file()]


def selective_stage() -> list[str]:
    staged: list[str] = []
    for path in collect_selective_paths():
        hits = scan_secrets(path)
        if hits:
            raise RuntimeError(f"Secret scan failed for {path}: {hits}")
        rel = path.relative_to(REPO).as_posix()
        run_git("add", "--", rel)
        staged.append(rel)
    return staged


def update_receipt(commit_sha: str, head_before: str) -> None:
    receipt_path = PILOT / "CORVONERO-PRODUCTION-EXTENSIONS-FINAL-CHECKPOINT-v1.json"
    data = json.loads(receipt_path.read_text(encoding="utf-8"))
    data["generated_at"] = datetime.now(timezone.utc).isoformat()
    data["git"]["pre_commit_head"] = head_before
    data["git"]["git_commit_sha"] = commit_sha
    receipt_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    run_git("add", "--", receipt_path.relative_to(REPO).as_posix())


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

    gen_dest = staging / "repository/projects/mars-search-ppc-production/pilots/corvonero/tools"
    gen_dest.mkdir(parents=True, exist_ok=True)
    for g in GENERATORS:
        if g.exists():
            shutil.copy2(g, gen_dest / g.name)

    exports_dest = staging / "exports"
    for export_dir in [ADS_FINAL_DIR, WAVE1_DIR, ROMAN_DIR]:
        if export_dir.exists():
            copy_tree(export_dir, f"exports/{export_dir.name}")

    git_meta = staging / "git-metadata"
    git_meta.mkdir(parents=True)
    meta = {
        "branch": BRANCH,
        "checkpoint_commit": commit_sha,
        "prior_final_ad_checkpoint_commit": PRIOR_COMMIT,
        "prior_final_ad_checkpoint_tag": PRIOR_TAG,
        "tag": PLANNED_TAG,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    (git_meta / "checkpoint-git-metadata-v1.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (git_meta / "commit-log-v1.txt").write_text(
        run_git("log", "-1", "--format=fuller", commit_sha), encoding="utf-8"
    )

    manifest_entries: list[dict] = []
    archive_path = BACKUP_DIR / ARCHIVE_NAME
    if archive_path.exists():
        archive_path.unlink()

    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(staging.rglob("*")):
            if not file_path.is_file():
                continue
            if scan_secrets(file_path):
                continue
            arc = file_path.relative_to(staging).as_posix()
            zf.write(file_path, arc)
            manifest_entries.append(
                {
                    "path": arc,
                    "size_bytes": file_path.stat().st_size,
                    "sha256": sha256_file(file_path),
                }
            )

    archive_sha = sha256_file(archive_path)

    with zipfile.ZipFile(archive_path) as zf:
        names = zf.namelist()
        docx_files = [n for n in names if n.lower().endswith(".docx")]
        xlsx_files = [n for n in names if n.lower().endswith(".xlsx")]
        ext_v2 = [n for n in names if "CORVONERO-EXT-W1" in n and "-v2." in n]

    forbidden_roots = [n for n in names if n.startswith(("workspaces/", "projects/ocpilot/", ".recovery-temp/"))]

    manifest = {
        "manifest_id": "corvonero-final-production-extensions-2026-06-29",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "archive": ARCHIVE_NAME,
        "archive_sha256": archive_sha,
        "file_count": len(manifest_entries),
        "git_commit": commit_sha,
        "tag": PLANNED_TAG,
        "prior_final_ad_checkpoint_commit": PRIOR_COMMIT,
        "prior_final_ad_checkpoint_tag": PRIOR_TAG,
        "docx_in_archive": len(docx_files),
        "xlsx_in_archive": len(xlsx_files),
        "extensions_v2_files_in_archive": len(ext_v2),
        "validation": {
            "campaigns": 5,
            "deployable_groups": 15,
            "deployable_phrases": 895,
            "sitelinks": "20/20",
            "callout_sets": "5/5",
            "cross_negatives_deployed": 0,
        },
        "boundaries": {
            "commander_xlsx": "NOT CREATED",
            "advertising": "NOT STARTED",
        },
        "files": manifest_entries,
    }
    base = ARCHIVE_NAME.replace(".zip", "")
    manifest_path = BACKUP_DIR / f"{base}-MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest_sha = sha256_file(manifest_path)

    sha_path = BACKUP_DIR / f"{base}-SHA256.txt"
    sha_path.write_text(
        "\n".join(
            [
                f"# CORVONERO FINAL PRODUCTION EXTENSIONS SHA-256",
                f"created: {datetime.now(timezone.utc).isoformat()}",
                f"archive: {archive_sha}  {ARCHIVE_NAME}",
                f"manifest: {manifest_sha}  {manifest_path.name}",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    readme_path = BACKUP_DIR / f"{base}-README.md"
    readme_path.write_text(
        f"""# CORVONERO Final Production Extensions Backup

Date: 2026-06-29
Git commit: `{commit_sha}`
Tag: `{PLANNED_TAG}`
Prior final-ad checkpoint: `{PRIOR_COMMIT}` (`{PRIOR_TAG}`)

## Contents

- Corvonero canonical authority (full pilot tree)
- Extensions Wave 1 v1 and operator-approved v2
- Final landing-page copy authority
- Five Roman LP DOCX files
- Research XLSX
- Final Ads DOCX
- Phrase allocation and deployability overlay
- Import profile and Commander readiness gates
- Corvonero reports and extension generators

## Boundaries

- Commander XLSX: NOT CREATED
- Advertising: NOT STARTED
- Cross-campaign negatives: 0 deployed

Archive SHA-256: `{archive_sha}`
Manifest file count: {len(manifest_entries)}
DOCX in archive: {len(docx_files)}
XLSX in archive: {len(xlsx_files)}
Extensions v2 files: {len(ext_v2)}
""",
        encoding="utf-8",
    )

    verify_ok = (
        sha256_file(archive_path) == archive_sha
        and len(docx_files) >= 6
        and len(xlsx_files) >= 1
        and len(ext_v2) >= 8
        and len(forbidden_roots) == 0
        and len(manifest_entries) == len(names)
    )

    return {
        "archive": str(archive_path),
        "archive_sha256": archive_sha,
        "manifest_file_count": len(manifest_entries),
        "zip_entry_count": len(names),
        "docx_in_zip": len(docx_files),
        "xlsx_in_zip": len(xlsx_files),
        "extensions_v2_in_zip": len(ext_v2),
        "forbidden_roots": forbidden_roots,
        "verify_ok": verify_ok,
    }


def main() -> None:
    if os.environ.get("CORVONERO_OPERATOR_GATE") != "APPROVED":
        raise SystemExit(
            "STOP: CORVONERO_OPERATOR_GATE=APPROVED required. "
            "This script is not safe for casual execution."
        )

    head_before = run_git("rev-parse", "HEAD")
    branch = run_git("branch", "--show-current")
    if branch != BRANCH:
        raise RuntimeError(f"Wrong branch: {branch}")
    subprocess.run(
        ["git", "merge-base", "--is-ancestor", PRIOR_COMMIT, "HEAD"],
        cwd=REPO,
        check=True,
    )
    if run_git("tag", "-l", PLANNED_TAG):
        raise RuntimeError(f"Tag already exists: {PLANNED_TAG}")

    staged = selective_stage()
    print(f"STAGED_COUNT={len(staged)}")
    print(run_git("diff", "--cached", "--name-status"))
    print(run_git("diff", "--cached", "--stat"))

    commit_body = """Production extensions approved for 5 P1 campaigns
20 sitelinks and 5 callout sets finalized
Controlled shared and campaign negatives approved
Cross-campaign negatives disabled
Base UTM policy approved without dynamic keyword macro
15 groups and 895 phrases remain deployable
Commander XLSX not created
Advertising not launched"""

    run_git(
        "commit",
        "-m",
        "checkpoint(corvonero): preserve production extensions",
        "-m",
        commit_body,
    )
    commit_sha = run_git("rev-parse", "HEAD")
    print(f"COMMIT_SHA={commit_sha}")

    update_receipt(commit_sha, head_before)
    run_git(
        "commit",
        "--amend",
        "--no-edit",
    )
    commit_sha = run_git("rev-parse", "HEAD")
    print(f"AMENDED_COMMIT_SHA={commit_sha}")

    tag_msg = """Corvonero final production extensions checkpoint.
Sitelinks, callouts, controlled negatives and base UTM approved.
Search only; networks and auto-targeting disabled.
Commander XLSX not created.
Advertising not launched."""
    run_git("tag", "-a", PLANNED_TAG, "-m", tag_msg)

    push_branch = subprocess.run(
        ["git", "push", "origin", BRANCH],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    print(f"PUSH_BRANCH_EXIT={push_branch.returncode}")
    if push_branch.stderr:
        print(push_branch.stderr)

    push_tag = subprocess.run(
        ["git", "push", "origin", PLANNED_TAG],
        cwd=REPO,
        capture_output=True,
        text=True,
    )
    print(f"PUSH_TAG_EXIT={push_tag.returncode}")
    if push_tag.stderr:
        print(push_tag.stderr)

    remote_branch = run_git("ls-remote", "--heads", "origin", BRANCH)
    remote_tag = run_git("ls-remote", "--tags", "origin", PLANNED_TAG)
    print(f"REMOTE_BRANCH={remote_branch}")
    print(f"REMOTE_TAG={remote_tag}")

    backup = create_backup(commit_sha)
    print(json.dumps({"commit_sha": commit_sha, "backup": backup}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
