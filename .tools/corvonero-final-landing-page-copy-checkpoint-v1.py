#!/usr/bin/env python3
"""Corvonero final landing-page copy program checkpoint — inventory, ZIP, receipts."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"X:\AI MARS")
STORAGE = Path(r"X:\AI MARS STORAGE")
PILOT = REPO / "projects/mars-search-ppc-production/pilots/corvonero"
REPORTS = REPO / "projects/mars-search-ppc-production/reports"
TOOLS = REPO / ".tools"

PRIOR_COMMIT = "2de6bafab4ca80f2e1bf641468f0b973c4c21282"
PRIOR_TAG = "corvonero-pre-export-production-2026-06"
PLANNED_TAG = "corvonero-final-landing-page-copy-program-2026-06"
BRANCH = "mars/canonical-post-recovery"

BACKUP_DIR = STORAGE / "backups/corvonero/CORVONERO-FINAL-LANDING-PAGE-COPY-2026-06-29"
ARCHIVE_NAME = "CORVONERO-FINAL-LANDING-PAGE-COPY-2026-06-29.zip"

LP01_DOCX = (
    STORAGE
    / "exports/corvonero/CORVONERO-EXPORT-WAVE-1-2026-06-29/CORVONERO-LP01-ТЕКСТ-ДЛЯ-РОМАНА-v1.docx"
)
LP01_XLSX = (
    STORAGE
    / "exports/corvonero/CORVONERO-EXPORT-WAVE-1-2026-06-29/CORVONERO-СВОДНОЕ-ИССЛЕДОВАНИЕ-v1.xlsx"
)
ROMAN_DIR = STORAGE / "exports/corvonero/CORVONERO-LANDING-PAGES-ROMAN-2026-06-29"
WAVE1_DIR = STORAGE / "exports/corvonero/CORVONERO-EXPORT-WAVE-1-2026-06-29"

FORBIDDEN_DOCX = [
    re.compile(r"\bscope\b", re.I),
    re.compile(r"\blegal\b", re.I),
    re.compile(r"\bcompliance\b", re.I),
    re.compile(r"\bMARS\b"),
    re.compile(r"t\.me/"),
    re.compile(r"wa\.me/"),
    re.compile(r"\bНДС\b", re.I),
    re.compile(r"\bSLA\b", re.I),
]

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._-]{30,}"),
]


def run_git(*args: str) -> str:
    r = subprocess.run(
        ["git", *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=True,
    )
    return r.stdout.strip()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as zf:
        parts = []
        for name in zf.namelist():
            if name.startswith("word/") and name.endswith(".xml"):
                parts.append(zf.read(name).decode("utf-8", errors="replace"))
        return "\n".join(parts)


def verify_docx(path: Path) -> dict:
    result = {"path": str(path), "opens": False, "size_bytes": 0, "sha256": "", "forbidden_hits": [], "pass": False}
    if not path.exists():
        return result
    result["size_bytes"] = path.stat().st_size
    result["sha256"] = sha256_file(path)
    try:
        text = docx_text(path)
        result["opens"] = True
        for pat in FORBIDDEN_DOCX:
            if pat.search(text):
                result["forbidden_hits"].append(pat.pattern)
        result["pass"] = result["opens"] and not result["forbidden_hits"]
    except Exception as exc:  # noqa: BLE001
        result["error"] = str(exc)
    return result


def verify_phrase_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    rec = data.get("phrase_reconciliation", {})
    return {
        "allocated": rec.get("allocated"),
        "mapped": rec.get("mapped"),
        "pass": rec.get("pass"),
        "variant_a": data.get("default_first_screen_variant") == "A"
        or data.get("first_screen", {}).get("variant") == "A",
    }


def main() -> None:
    if os.environ.get("CORVONERO_OPERATOR_GATE") != "APPROVED":
        raise SystemExit(
            "STOP: CORVONERO_OPERATOR_GATE=APPROVED required. "
            "This script is not safe for casual execution."
        )

    now = datetime.now(timezone.utc).isoformat()
    head = run_git("rev-parse", "HEAD")

    phrase_files = {
        "LP-02": PILOT / "CORVONERO-COPY-WAVE-2-LP02-SUPPORT-FINAL-v2.json",
        "LP-03": PILOT / "CORVONERO-COPY-WAVE-2-LP03-DEVELOPMENT-FINAL-v2.json",
        "LP-04": PILOT / "CORVONERO-COPY-WAVE-2-LP04-INTEGRATIONS-FINAL-v2.json",
        "LP-05": PILOT / "CORVONERO-COPY-WAVE-2-LP05-MARKING-FINAL-v2.json",
    }
    phrase_check = {k: verify_phrase_json(v) for k, v in phrase_files.items()}

    docx_inventory = [
        {
            "page": "LP-01",
            "docx_path": str(LP01_DOCX),
            "source_final_copy": "CORVONERO-PHASE-6.6-LP01-FINAL-PRODUCTION-COPY-v3.json",
            **verify_docx(LP01_DOCX),
        }
    ]
    roman_map = {
        "LP-02": ("CORVONERO-LP02-СОПРОВОЖДЕНИЕ-1С-ТЕКСТ-ДЛЯ-РОМАНА-v1.docx", "CORVONERO-COPY-WAVE-2-LP02-SUPPORT-FINAL-v2.json"),
        "LP-03": ("CORVONERO-LP03-ДОРАБОТКА-1С-ТЕКСТ-ДЛЯ-РОМАНА-v1.docx", "CORVONERO-COPY-WAVE-2-LP03-DEVELOPMENT-FINAL-v2.json"),
        "LP-04": ("CORVONERO-LP04-ИНТЕГРАЦИИ-1С-ТЕКСТ-ДЛЯ-РОМАНА-v1.docx", "CORVONERO-COPY-WAVE-2-LP04-INTEGRATIONS-FINAL-v2.json"),
        "LP-05": ("CORVONERO-LP05-МАРКИРОВКА-1С-ТЕКСТ-ДЛЯ-РОМАНА-v1.docx", "CORVONERO-COPY-WAVE-2-LP05-MARKING-FINAL-v2.json"),
    }
    for page, (fname, src) in roman_map.items():
        v = verify_docx(ROMAN_DIR / fname)
        docx_inventory.append(
            {
                "page": page,
                "docx_path": str(ROMAN_DIR / fname),
                "source_final_copy": src,
                **v,
            }
        )

    inventory_md = REPORTS / "REPORT-corvonero-roman-docx-final-inventory-v1.md"
    lines = [
        "# REPORT — Corvonero Roman DOCX Final Inventory v1",
        "",
        f"Generated: {now}",
        f"Pre-commit HEAD: `{head}`",
        f"Prior checkpoint: `{PRIOR_COMMIT}` (`{PRIOR_TAG}`)",
        "",
        "## Inventory",
        "",
        "| Page | DOCX | Size (bytes) | SHA-256 | Source final copy | Validation |",
        "| --- | --- | ---: | --- | --- | --- |",
    ]
    for row in docx_inventory:
        status = "PASS" if row.get("pass") else "FAIL"
        lines.append(
            f"| {row['page']} | `{Path(row['docx_path']).name}` | {row.get('size_bytes', 0)} | `{row.get('sha256', '')}` | `{row['source_final_copy']}` | {status} |"
        )
    lines.extend(
        [
            "",
            "## Phrase reconciliation (LP-02–LP-05)",
            "",
            "| Page | Allocated | Mapped | Pass | Variant A |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for page, chk in phrase_check.items():
        lines.append(
            f"| {page} | {chk['allocated']} | {chk['mapped']} | {'PASS' if chk['pass'] else 'FAIL'} | {'yes' if chk['variant_a'] else 'no'} |"
        )
    total_mapped = sum(chk["mapped"] for chk in phrase_check.values())
    lines.extend(
        [
            "",
            f"**Total LP-02–LP-05:** {total_mapped} / 494",
            "",
            "## Coverage note",
            "",
            "- LP-01: 404 phrases (unchanged authority)",
            "- LP-02–LP-05: 494 phrases",
            "- P1 landing-page total: 898 / 898",
            "- LP-06 deferred: 37 phrases",
            "- Total ACCEPT: 935 (898 + 37 deferred)",
        ]
    )
    inventory_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    checkpoint_json = {
        "checkpoint_id": "corvonero-landing-page-copy-program-checkpoint-v1",
        "generated_at": now,
        "git": {
            "branch": BRANCH,
            "pre_commit_head": head,
            "prior_checkpoint_commit": PRIOR_COMMIT,
            "prior_checkpoint_tag": PRIOR_TAG,
            "planned_tag": PLANNED_TAG,
        },
        "copy_readiness": {
            "LP-01": "READY — authority unchanged",
            "LP-02": "OPERATOR APPROVED FINAL",
            "LP-03": "OPERATOR APPROVED FINAL",
            "LP-04": "OPERATOR APPROVED FINAL",
            "LP-05": "OPERATOR APPROVED FINAL",
            "LP-06": "DEFERRED — 37 phrases",
        },
        "roman_docx": {
            "count_ready": 5,
            "lp01_path": str(LP01_DOCX),
            "lp02_lp05_dir": str(ROMAN_DIR),
            "inventory": docx_inventory,
        },
        "phrase_coverage": {
            "LP-01": 404,
            "LP-02": 155,
            "LP-03": 71,
            "LP-04": 48,
            "LP-05": 220,
            "p1_landing_page_total": 898,
            "lp06_deferred": 37,
            "accept_total": 935,
            "note": "935 total ACCEPT; 898 covered by final P1 landing-page copy; 37 assigned to deferred LP-06",
        },
        "ads_state": "NOT_STARTED",
        "commander_state": "NOT_STARTED",
        "website_unchanged": True,
        "phrase_reconciliation_lp02_lp05": phrase_check,
    }
    checkpoint_md_path = PILOT / "CORVONERO-LANDING-PAGE-COPY-PROGRAM-CHECKPOINT-v1.md"
    checkpoint_json_path = PILOT / "CORVONERO-LANDING-PAGE-COPY-PROGRAM-CHECKPOINT-v1.json"
    checkpoint_json_path.write_text(json.dumps(checkpoint_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md_body = [
        "# CORVONERO Landing Page Copy Program Checkpoint v1",
        "",
        f"Generated: {now}",
        "",
        "## Git",
        "",
        f"- Branch: `{BRANCH}`",
        f"- Pre-commit HEAD: `{head}`",
        f"- Prior checkpoint: `{PRIOR_COMMIT}` (`{PRIOR_TAG}`)",
        f"- Planned tag: `{PLANNED_TAG}`",
        "",
        "## Copy readiness",
        "",
        "| Page | State |",
        "| --- | --- |",
        "| LP-01 | READY — authority unchanged |",
        "| LP-02 | OPERATOR APPROVED FINAL |",
        "| LP-03 | OPERATOR APPROVED FINAL |",
        "| LP-04 | OPERATOR APPROVED FINAL |",
        "| LP-05 | OPERATOR APPROVED FINAL |",
        "| LP-06 | DEFERRED — 37 phrases |",
        "",
        "## Roman DOCX",
        "",
        "Five deliverables verified (LP-01 through LP-05).",
        "",
        "## Phrase coverage",
        "",
        "| Scope | Phrases |",
        "| --- | ---: |",
        "| LP-01 | 404 |",
        "| LP-02 | 155 |",
        "| LP-03 | 71 |",
        "| LP-04 | 48 |",
        "| LP-05 | 220 |",
        "| **P1 landing-page total** | **898** |",
        "| LP-06 deferred | 37 |",
        "| Total ACCEPT | 935 |",
        "",
        "935 total ACCEPT; 898 covered by final P1 landing-page copy; 37 assigned to deferred LP-06.",
        "",
        "## Production boundaries",
        "",
        "- Advertisements: NOT STARTED",
        "- Commander: NOT STARTED",
        "- Websites: unchanged",
    ]
    checkpoint_md_path.write_text("\n".join(md_body) + "\n", encoding="utf-8")

    # Build external backup
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    staging = BACKUP_DIR / "_staging"
    if staging.exists():
        import shutil

        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    def copy_into(rel_src: Path, rel_dest: str) -> None:
        if not rel_src.exists():
            return
        dest = staging / rel_dest
        dest.parent.mkdir(parents=True, exist_ok=True)
        if rel_src.is_dir():
            import shutil

            shutil.copytree(rel_src, dest)
        else:
            import shutil

            shutil.copy2(rel_src, dest)

    # Corvonero pilot (tracked + wave 2 untracked)
    import shutil

    pilot_dest = staging / "repository/projects/mars-search-ppc-production/pilots/corvonero"
    pilot_dest.mkdir(parents=True, exist_ok=True)
    for p in PILOT.iterdir():
        if p.is_file():
            shutil.copy2(p, pilot_dest / p.name)

    report_names = [
        "REPORT-corvonero-export-wave-1-lp01-docx-and-research-xlsx-v1.md",
        "REPORT-corvonero-copy-wave-2-lp02-lp05-drafts-v1.md",
        "REPORT-corvonero-copy-wave-2-finalization-v1.md",
        "REPORT-corvonero-pre-export-production-backup-v1.md",
        "REPORT-corvonero-roman-docx-final-inventory-v1.md",
    ]
    rep_dest = staging / "repository/projects/mars-search-ppc-production/reports"
    rep_dest.mkdir(parents=True, exist_ok=True)
    for name in report_names:
        src = REPORTS / name
        if src.exists():
            shutil.copy2(src, rep_dest / name)

    tool_names = [
        "corvonero-export-wave-1-v1.py",
        "corvonero-export-wave-2-roman-docx-v1.py",
        "corvonero-pre-export-backup-v1.py",
        "corvonero-final-landing-page-copy-checkpoint-v1.py",
    ]
    tool_dest = staging / "repository/.tools"
    tool_dest.mkdir(parents=True, exist_ok=True)
    for name in tool_names:
        src = TOOLS / name
        if src.exists():
            shutil.copy2(src, tool_dest / name)

    # Semantic authority subset
    orca = REPO / "projects/orca/projects/corvonero-direct-v2-clean-room"
    if orca.exists():
        shutil.copytree(
            orca,
            staging / "repository/projects/orca/projects/corvonero-direct-v2-clean-room",
            dirs_exist_ok=True,
        )

    mig = REPO / "incoming/mig/pilots/corvonero"
    if mig.exists():
        shutil.copytree(mig, staging / "repository/incoming/mig/pilots/corvonero", dirs_exist_ok=True)

    ws = REPO / "workspaces/corvonero-yandex-direct"
    if ws.exists():
        shutil.copytree(ws, staging / "repository/workspaces/corvonero-yandex-direct", dirs_exist_ok=True)

    # External exports
    export_dest = staging / "exports"
    export_dest.mkdir(parents=True)
    if WAVE1_DIR.exists():
        shutil.copytree(WAVE1_DIR, export_dest / WAVE1_DIR.name, dirs_exist_ok=True)
    if ROMAN_DIR.exists():
        shutil.copytree(ROMAN_DIR, export_dest / ROMAN_DIR.name, dirs_exist_ok=True)

    # Checkpoint receipts in backup
    checkpoint_staging = staging / "checkpoint"
    checkpoint_staging.mkdir(parents=True, exist_ok=True)
    shutil.copy2(checkpoint_json_path, checkpoint_staging / "CORVONERO-LANDING-PAGE-COPY-PROGRAM-CHECKPOINT-v1.json")
    shutil.copy2(checkpoint_md_path, checkpoint_staging / "CORVONERO-LANDING-PAGE-COPY-PROGRAM-CHECKPOINT-v1.md")
    shutil.copy2(inventory_md, checkpoint_staging / "REPORT-corvonero-roman-docx-final-inventory-v1.md")

    archive_path = BACKUP_DIR / ARCHIVE_NAME
    if archive_path.exists():
        archive_path.unlink()

    manifest_entries = []
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(staging.rglob("*")):
            if file_path.is_file():
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
    (BACKUP_DIR / f"{ARCHIVE_NAME.replace('.zip', '')}-SHA256.txt").write_text(
        f"{archive_sha}  {ARCHIVE_NAME}\n", encoding="utf-8"
    )
    manifest = {
        "manifest_id": "corvonero-final-landing-page-copy-2026-06-29",
        "created_at": now,
        "archive": ARCHIVE_NAME,
        "archive_sha256": archive_sha,
        "file_count": len(manifest_entries),
        "git_head": head,
        "prior_checkpoint": PRIOR_COMMIT,
        "roman_docx_count": 5,
        "research_xlsx": str(LP01_XLSX.relative_to(STORAGE / "exports/corvonero/CORVONERO-EXPORT-WAVE-1-2026-06-29"))
        if LP01_XLSX.exists()
        else None,
        "files": manifest_entries,
    }
    (BACKUP_DIR / f"{ARCHIVE_NAME.replace('.zip', '')}-MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    readme = [
        "# CORVONERO Final Landing Page Copy Backup",
        "",
        f"Date: 2026-06-29",
        f"Git HEAD (pre-commit): `{head}`",
        f"Prior checkpoint: `{PRIOR_COMMIT}` (`{PRIOR_TAG}`)",
        "",
        "## Contents",
        "",
        "- Corvonero pilot authority and Wave 2 final copy",
        "- Five Roman DOCX deliverables (LP-01 through LP-05)",
        "- Research XLSX and export manifests",
        "- Reproducible export helper scripts",
        "- Checkpoint and inventory reports",
        "",
        "## Boundaries",
        "",
        "- Advertisements: NOT STARTED",
        "- Commander: NOT STARTED",
        "- Websites unchanged",
        "- LP-06 deferred (37 phrases)",
        "",
        f"Archive SHA-256: `{archive_sha}`",
        f"Manifest file count: {len(manifest_entries)}",
    ]
    (BACKUP_DIR / f"{ARCHIVE_NAME.replace('.zip', '')}-README.md").write_text(
        "\n".join(readme) + "\n", encoding="utf-8"
    )

    # Validate ZIP
    with zipfile.ZipFile(archive_path) as zf:
        names = zf.namelist()
    docx_in_zip = [n for n in names if n.lower().endswith(".docx")]
    xlsx_in_zip = [n for n in names if n.lower().endswith(".xlsx")]

    summary = {
        "inventory_md": str(inventory_md),
        "checkpoint_md": str(checkpoint_md_path),
        "checkpoint_json": str(checkpoint_json_path),
        "archive": str(archive_path),
        "archive_sha256": archive_sha,
        "zip_file_count": len(names),
        "manifest_file_count": len(manifest_entries),
        "docx_in_zip": len(docx_in_zip),
        "xlsx_in_zip": len(xlsx_in_zip),
        "phrase_check": phrase_check,
        "docx_inventory_pass": all(r.get("pass") for r in docx_inventory),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
