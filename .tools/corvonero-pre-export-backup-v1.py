#!/usr/bin/env python3
"""Corvonero pre-export production backup — inventory, matrices, external ZIP."""
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
STORAGE_ROOT = Path(r"X:\AI MARS STORAGE")
STORAGE_DIR = STORAGE_ROOT / "backups/corvonero/CORVONERO-PRE-EXPORT-PRODUCTION-2026-06-29"
ARCHIVE_NAME = "CORVONERO-PRE-EXPORT-PRODUCTION-2026-06-29.zip"
PRIOR_COMMIT = "4472be53ee6475665fa5c37ebd46f430f919e8bf"
PRIOR_TAG = "corvonero-lp01-final-copy-v3-2026-06"
PLANNED_TAG = "corvonero-pre-export-production-2026-06"
BRANCH = "mars/canonical-post-recovery"

PILOT = REPO / "projects/mars-search-ppc-production/pilots/corvonero"
REPORTS = REPO / "projects/mars-search-ppc-production/reports"
WORKSPACE = REPO / "workspaces/corvonero-yandex-direct"
MIG = REPO / "incoming/mig/pilots/corvonero"
ORCA_CLEAN = REPO / "projects/orca/projects/corvonero-direct-v2-clean-room"

SECRET_PATH_PATTERNS = [
    re.compile(r"\.env$", re.I),
    re.compile(r"[/\\]\.secrets[/\\]", re.I),
    re.compile(r"credentials\.json$", re.I),
]

SECRET_CONTENT_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._-]{30,}"),
]

CLASSIFICATION_ORDER = [
    "SEMANTIC_SOURCE",
    "SEMANTIC_AUTHORITY",
    "SERP_AND_RESEARCH",
    "CAMPAIGN_ARCHITECTURE",
    "LANDING_PAGE_REQUIREMENTS",
    "LP01_FINAL_COPY",
    "PHASE7A_ROMAN_HANDOFF",
    "REPORT",
    "TOOL",
    "CHECKPOINT",
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


def git_state(rel: str) -> str:
    tracked = subprocess.run(
        ["git", "ls-files", "--error-unmatch", rel],
        cwd=REPO,
        capture_output=True,
    )
    if tracked.returncode != 0:
        return "??"
    diff = subprocess.run(
        ["git", "diff", "--quiet", "--", rel],
        cwd=REPO,
        capture_output=True,
    )
    if diff.returncode != 0:
        return "M"
    staged = subprocess.run(
        ["git", "diff", "--cached", "--quiet", "--", rel],
        cwd=REPO,
        capture_output=True,
    )
    if staged.returncode != 0:
        return "A/M staged"
    return "tracked"


def classify(rel: str) -> str:
    p = rel.replace("\\", "/").lower()
    base = os.path.basename(p)

    if "checkpoint" in base or "-checkpoint-" in p:
        return "CHECKPOINT"
    if "/pilots/corvonero/tools/" in p and p.endswith(".mjs"):
        return "TOOL"
    if "/reports/report-corvonero" in p:
        return "REPORT"
    if "phase-7a" in p:
        return "PHASE7A_ROMAN_HANDOFF"
    if any(
        k in p
        for k in [
            "phase-6.6-lp01-final",
            "phase-6.5-lp01",
            "lp01-final-copy-v3",
        ]
    ):
        return "LP01_FINAL_COPY"
    if "phase-6.2" in p and "requirements" in p:
        return "LANDING_PAGE_REQUIREMENTS"
    if any(
        k in p
        for k in [
            "phase-6.1",
            "phase-6.2",
            "phase-6-partial",
            "phase-6-exclusion",
            "group-to-lp",
            "campaign-architecture",
            "campaign-readiness",
            "website-implementation-handoff",
            "phase-6.3",
            "phase-6.4",
            "post-phase-6.4",
        ]
    ):
        return "CAMPAIGN_ARCHITECTURE"
    if any(
        k in p
        for k in [
            "/evidence/serp",
            "serp_r",
            "wordstat",
            "research_pack",
            "mig-source",
            "demand_surface",
            "keyword_registry",
            "mig-research",
        ]
    ):
        return "SERP_AND_RESEARCH"
    if any(
        k in p
        for k in [
            "phase-5.2",
            "phase-5.1",
            "partial-semantic",
            "reviewed-registry",
            "operator-decision",
            "accept-v",
            "reject-v",
            "abstain-v",
            "correction-ledger",
            "unprocessed-ids",
            "processed-ids",
            "commercial-eligibility",
            "intent-screening",
            "canonical-phrase",
            "semantic-sign-off",
        ]
    ):
        return "SEMANTIC_AUTHORITY"
    if any(
        k in p
        for k in [
            "incoming/mig/pilots/corvonero",
            "orca/projects/corvonero-direct",
            "normalized-corpus",
            "semantic-core",
            "new-controlled-semantic",
            "run-004",
            "corvonero-yandex-direct",
        ]
    ):
        return "SEMANTIC_SOURCE"
    if p.startswith("projects/mars-search-ppc-production/pilots/corvonero/"):
        return "SEMANTIC_AUTHORITY"
    return "SEMANTIC_SOURCE"


def scan_secret(path: Path, *, content_scan: bool = False) -> bool:
    rel = str(path).replace("\\", "/")
    if any(p.search(rel) for p in SECRET_PATH_PATTERNS):
        return True
    if not content_scan:
        return False
    if path.suffix.lower() in {".html", ".htm"}:
        return False
    try:
        if path.stat().st_size > 500_000:
            return False
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False
    return any(p.search(text) for p in SECRET_CONTENT_PATTERNS)


def audit_secret_reference(path: Path) -> bool:
    """Broad documentation audit — path names and references, not live credentials."""
    rel = str(path).replace("\\", "/").lower()
    if scan_secret(path, content_scan=False):
        return True
    if rel.endswith((".env",)) or "/.secrets/" in rel:
        return True
    try:
        if path.stat().st_size > 500_000:
            return False
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
    except OSError:
        return False
    return ".secrets/" in text or "openrouter" in text and "api" in text


def collect_inventory_paths() -> list[str]:
    paths: set[str] = set()

    for root in [PILOT, REPORTS, WORKSPACE, MIG, ORCA_CLEAN]:
        if not root.exists():
            continue
        if root == REPORTS:
            for f in root.glob("REPORT-corvonero*"):
                if f.is_file():
                    paths.add(str(f.relative_to(REPO)).replace("\\", "/"))
        else:
            for f in root.rglob("*"):
                if f.is_file():
                    rel = str(f.relative_to(REPO)).replace("\\", "/")
                    if "node_modules" in rel or ".git" in rel:
                        continue
                    paths.add(rel)

    return sorted(paths)


def archive_roots() -> list[tuple[Path, str]]:
    """Local path -> zip prefix inside archive."""
    roots = [
        (PILOT, "repository/projects/mars-search-ppc-production/pilots/corvonero"),
        (WORKSPACE, "repository/workspaces/corvonero-yandex-direct"),
        (MIG, "repository/incoming/mig/pilots/corvonero"),
        (ORCA_CLEAN, "repository/projects/orca/projects/corvonero-direct-v2-clean-room"),
    ]
    report_files = sorted(REPORTS.glob("REPORT-corvonero*"))
    return roots, report_files


def build_export_matrix() -> dict:
    return {
        "matrix_id": "corvonero-export-readiness-matrix-v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "prior_checkpoint": {
            "commit": PRIOR_COMMIT,
            "tag": PRIOR_TAG,
        },
        "semantic_boundary": {
            "canonical_total": 2368,
            "assessed": 1599,
            "unprocessed_backlog": 769,
            "partial_semantic_authority": True,
            "serp_queries_captured": 5,
            "serp_queries_planned": 10,
        },
        "deliverables": {
            "D1_advertisements_word": {
                "id": "D1",
                "name": "Advertisements Word document",
                "readiness": "NOT_READY — ADS_NOT_CREATED",
                "required_columns": [
                    "start phrase",
                    "campaign",
                    "ad group",
                    "headline",
                    "description",
                    "landing-page URL",
                ],
                "available_sources": [
                    "CORVONERO-PHASE-6.2-GROUP-TO-LP-MAP-v1.json",
                    "CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json",
                    "CORVONERO-PHASE-6.6-LP01-FINAL-PRODUCTION-COPY-v3 (LP-01 only)",
                ],
                "missing_components": [
                    "ad headlines and descriptions not authored",
                    "final published landing-page URLs (staging only for LP-01)",
                    "negative keyword import set for Commander",
                    "ad extensions profile",
                    "multi-LP URL mapping for LP-02..LP-06",
                ],
            },
            "D2_landing_page_word_roman": {
                "id": "D2",
                "name": "Landing-page Word files for Roman",
                "pages": {
                    "LP-01": {
                        "readiness": "READY_FOR_DOCX_EXPORT",
                        "authority": [
                            "CORVONERO-PHASE-6.6-LP01-FINAL-PRODUCTION-COPY-v3",
                            "CORVONERO-PHASE-7A-LP01-BUILD-AUTHORITY-MANIFEST-v1",
                        ],
                    },
                    "LP-02": {"readiness": "REQUIRE_FINAL_COPY"},
                    "LP-03": {"readiness": "REQUIRE_FINAL_COPY"},
                    "LP-04": {"readiness": "REQUIRE_FINAL_COPY"},
                    "LP-05": {"readiness": "REQUIRE_FINAL_COPY"},
                    "LP-06": {"readiness": "DEFERRED / REQUIRE_FINAL_COPY"},
                },
            },
            "D3_yandex_direct_commander_excel": {
                "id": "D3",
                "name": "Yandex Direct Commander Excel",
                "readiness": "NOT_READY — REQUIRES ADS, FINAL URLS, NEGATIVES, EXTENSIONS AND IMPORT PROFILE",
                "required_components": [
                    "campaign structure",
                    "ad groups",
                    "keywords / start phrases",
                    "ads (headlines + descriptions)",
                    "final landing URLs",
                    "negative keywords",
                    "extensions",
                    "Commander import profile",
                ],
                "available": [
                    "partial semantic accept registry (1599 phrases)",
                    "campaign architecture CA-01..CA-06 outlines",
                    "LP-01 staging URL direction only (unpublished)",
                ],
                "missing": [
                    "authored ads",
                    "published URLs",
                    "Commander workbook",
                    "extensions pack",
                ],
            },
            "D4_consolidated_research_excel": {
                "id": "D4",
                "name": "Consolidated Research Excel",
                "readiness": "READY_FOR_PARTIAL-COVERAGE XLSX EXPORT",
                "limitations": {
                    "serp": "5 / 10 queries",
                    "assessed_semantics": "1599 / 2368",
                    "unprocessed_backlog": 769,
                },
                "available_data": [
                    "Wordstat (MIG source ledger)",
                    "normalized corpus",
                    "canonical corpus / phrase registry",
                    "semantic verdicts (accept/reject/abstain)",
                    "campaign allocation / group-to-LP map",
                    "SERP evidence (partial)",
                    "competitor/search observations",
                    "LP research requirements",
                    "risk and coverage notes",
                ],
            },
        },
        "website": {"changed": False, "tilda_build": "NOT_STARTED"},
        "advertising": {"started": False},
    }


def write_inventory(records: list[dict], head: str) -> Path:
    out = REPORTS / "REPORT-corvonero-current-state-pre-export-inventory-v1.md"
    lines = [
        "# REPORT — Corvonero Current-State Pre-Export Inventory v1",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"Repository: `{REPO}`",
        f"Pre-commit HEAD: `{head}`",
        f"Prior protected checkpoint: `{PRIOR_COMMIT}` (tag: `{PRIOR_TAG}`)",
        f"Eligible file count: {len(records)}",
        "",
        "## Classification families",
        "",
    ]
    for c in CLASSIFICATION_ORDER:
        count = sum(1 for r in records if r["classification"] == c)
        lines.append(f"- **{c}**: {count} files")

    lines.extend(
        [
            "",
            "## Archive inclusion",
            "",
            "- `projects/mars-search-ppc-production/pilots/corvonero/**`",
            "- `projects/mars-search-ppc-production/reports/REPORT-corvonero-*`",
            "- `workspaces/corvonero-yandex-direct/**`",
            "- `incoming/mig/pilots/corvonero/**`",
            "- `projects/orca/projects/corvonero-direct-v2-clean-room/**`",
            "",
            "## Excluded patterns",
            "",
            "- `.git`, secrets, `.env`, credentials",
            "- Unrelated OCPilot, FP-0002, Website Factory WIP",
            "- `projects/projects/` duplicate tree",
            "- Unreferenced ORCA live-model report directories",
            "- Recovery temp, node_modules, runtime locks",
            "",
            "## File inventory",
            "",
            "| Path | Classification | Git | Size | SHA-256 | In archive | Staged this commit |",
            "|------|----------------|-----|------|---------|------------|-------------------|",
        ]
    )

    commit_stage_paths = {
        p.replace("\\", "/")
        for p in [
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PHASE-7A-LP01-BUILD-AUTHORITY-MANIFEST-v1.json",
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PHASE-7A-LP01-BUILD-AUTHORITY-MANIFEST-v1.md",
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PHASE-7A-LP01-ROMAN-BUILD-CHECKLIST-v1.md",
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PHASE-7A-LP01-STAGING-QA-CHECKLIST-v1.json",
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PHASE-7A-LP01-STAGING-QA-CHECKLIST-v1.md",
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PHASE-7A-LP01-IMPLEMENTATION-INPUTS-v1.json",
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PHASE-7A-LP01-IMPLEMENTATION-INPUTS-v1.md",
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PHASE-7A-LP01-OPERATOR-REVIEW-PACKET-v1.md",
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PHASE-7A-LP01-RESULT-v1.json",
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PHASE-7A-LP01-RESULT-v1.md",
            "projects/mars-search-ppc-production/reports/REPORT-corvonero-phase-7a-lp01-tilda-staging-preparation-v1.md",
            "projects/mars-search-ppc-production/reports/REPORT-corvonero-lp01-final-copy-v3-selective-checkpoint-v1.md",
            "projects/mars-search-ppc-production/reports/REPORT-corvonero-current-state-pre-export-inventory-v1.md",
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-EXPORT-READINESS-MATRIX-v1.md",
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-EXPORT-READINESS-MATRIX-v1.json",
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PRE-EXPORT-PRODUCTION-CHECKPOINT-v1.md",
            "projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-PRE-EXPORT-PRODUCTION-CHECKPOINT-v1.json",
        ]
    }

    for r in records:
        staged = "yes" if r["path"] in commit_stage_paths else "no"
        lines.append(
            f"| `{r['path']}` | {r['classification']} | {r['git']} | {r['size']} | `{r['sha256']}` | {r['in_archive']} | {staged} |"
        )

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def write_checkpoint(head: str, matrix: dict, inventory_path: str, file_count: int) -> None:
    checkpoint = {
        "checkpoint_id": "corvonero-pre-export-production-checkpoint-v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "git": {
            "branch": BRANCH,
            "pre_commit_head": head,
            "prior_checkpoint_commit": PRIOR_COMMIT,
            "prior_checkpoint_tag": PRIOR_TAG,
            "planned_tag": PLANNED_TAG,
        },
        "phase_7a_included": [
            "CORVONERO-PHASE-7A-LP01-BUILD-AUTHORITY-MANIFEST-v1",
            "CORVONERO-PHASE-7A-LP01-ROMAN-BUILD-CHECKLIST-v1",
            "CORVONERO-PHASE-7A-LP01-STAGING-QA-CHECKLIST-v1",
            "CORVONERO-PHASE-7A-LP01-IMPLEMENTATION-INPUTS-v1",
            "CORVONERO-PHASE-7A-LP01-OPERATOR-REVIEW-PACKET-v1",
            "CORVONERO-PHASE-7A-LP01-RESULT-v1",
            "REPORT-corvonero-phase-7a-lp01-tilda-staging-preparation-v1",
        ],
        "export_readiness_matrix": "CORVONERO-EXPORT-READINESS-MATRIX-v1",
        "semantic_boundary": matrix["semantic_boundary"],
        "lp01_final_copy": {
            "state": "FINAL v3 — operator approved",
            "authority_commit": PRIOR_COMMIT,
            "authority_tag": PRIOR_TAG,
            "docx_export": "READY_FOR_DOCX_EXPORT",
        },
        "lp02_to_lp06": {
            "LP-02": "REQUIRE_FINAL_COPY",
            "LP-03": "REQUIRE_FINAL_COPY",
            "LP-04": "REQUIRE_FINAL_COPY",
            "LP-05": "REQUIRE_FINAL_COPY",
            "LP-06": "DEFERRED / REQUIRE_FINAL_COPY",
        },
        "ads_state": "NOT_CREATED",
        "commander_state": "NOT_CREATED",
        "research_workbook_state": "READY_FOR_PARTIAL-COVERAGE XLSX EXPORT",
        "website_unchanged": True,
        "advertising_not_started": True,
        "inventory_reference": inventory_path,
        "canonical_inventory_file_count": file_count,
        "excluded_unrelated_wip": [
            "workspaces/fp-0002-*",
            "projects/ocpilot/*",
            "workspaces/website-factory-operations/*",
            "unreferenced ORCA live-model reports",
            "projects/projects/",
            ".recovery-temp/",
        ],
    }

    md_path = PILOT / "CORVONERO-PRE-EXPORT-PRODUCTION-CHECKPOINT-v1.md"
    json_path = PILOT / "CORVONERO-PRE-EXPORT-PRODUCTION-CHECKPOINT-v1.json"

    json_path.write_text(json.dumps(checkpoint, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    md_lines = [
        "# CORVONERO Pre-Export Production Checkpoint v1",
        "",
        f"Generated: {checkpoint['generated_at']}",
        "",
        "## Git",
        "",
        f"- Branch: `{BRANCH}`",
        f"- Pre-commit HEAD: `{head}`",
        f"- Prior checkpoint: `{PRIOR_COMMIT}` (`{PRIOR_TAG}`)",
        f"- Planned tag: `{PLANNED_TAG}`",
        "",
        "## Phase 7A scope preserved",
        "",
    ]
    for item in checkpoint["phase_7a_included"]:
        md_lines.append(f"- {item}")

    md_lines.extend(
        [
            "",
            "## Export readiness",
            "",
            f"- Matrix: `{checkpoint['export_readiness_matrix']}`",
            f"- LP-01 DOCX: **{checkpoint['lp01_final_copy']['docx_export']}**",
            f"- Research XLSX: **{checkpoint['research_workbook_state']}**",
            f"- Ads DOCX: **NOT_READY — ADS_NOT_CREATED**",
            f"- Commander XLSX: **NOT_READY**",
            "",
            "## Semantic boundary",
            "",
            f"- Assessed: **1599 / 2368**",
            f"- Unprocessed backlog: **769**",
            f"- SERP: **5 / 10 queries**",
            "",
            "## Boundaries",
            "",
            "- Website unchanged",
            "- Advertising not started",
            "- Tilda staging build authorized but not executed",
            "",
            f"Inventory: `{inventory_path}` ({file_count} files)",
        ]
    )
    md_path.write_text("\n".join(md_lines) + "\n", encoding="utf-8")


def create_archive(head: str, commit_sha: str | None = None) -> dict:
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    archive_path = STORAGE_DIR / ARCHIVE_NAME
    if archive_path.exists():
        raise FileExistsError(f"Archive already exists: {archive_path}")

    roots, report_files = archive_roots()
    manifest_files: list[dict] = []
    secret_hits: list[str] = []

    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as zf:
        git_meta = {
            "branch": BRANCH,
            "pre_export_head": head,
            "checkpoint_commit": commit_sha or "PENDING",
            "tag": PLANNED_TAG,
            "prior_checkpoint_commit": PRIOR_COMMIT,
            "prior_checkpoint_tag": PRIOR_TAG,
        }
        meta_json = json.dumps(git_meta, indent=2)
        zf.writestr("repository/git-metadata/checkpoint-git-metadata-v1.json", meta_json)
        manifest_files.append(
            {
                "path": "repository/git-metadata/checkpoint-git-metadata-v1.json",
                "size_bytes": len(meta_json.encode()),
                "sha256": hashlib.sha256(meta_json.encode()).hexdigest(),
            }
        )

        for root, prefix in roots:
            if not root.exists():
                continue
            for f in root.rglob("*"):
                if not f.is_file():
                    continue
                rel = f.relative_to(root).as_posix()
                arc = f"{prefix}/{rel}"
                if scan_secret(f, content_scan=True):
                    secret_hits.append(arc)
                    continue
                zf.write(f, arc)
                manifest_files.append(
                    {
                        "path": arc,
                        "size_bytes": f.stat().st_size,
                        "sha256": sha256_file(f),
                    }
                )

        for rf in report_files:
            if not rf.is_file():
                continue
            arc = f"repository/projects/mars-search-ppc-production/reports/{rf.name}"
            if scan_secret(rf, content_scan=True):
                secret_hits.append(arc)
                continue
            zf.write(rf, arc)
            manifest_files.append(
                {
                    "path": arc,
                    "size_bytes": rf.stat().st_size,
                    "sha256": sha256_file(rf),
                }
            )

    archive_sha = sha256_file(archive_path)
    archive_size = archive_path.stat().st_size

    manifest = {
        "archive_filename": ARCHIVE_NAME,
        "archive_path": str(archive_path),
        "archive_byte_size": archive_size,
        "archive_sha256": archive_sha,
        "file_count": len(manifest_files),
        "branch": BRANCH,
        "commit": commit_sha or head,
        "tag": PLANNED_TAG,
        "prior_checkpoint_commit": PRIOR_COMMIT,
        "prior_checkpoint_tag": PRIOR_TAG,
        "semantic_coverage": {
            "assessed": 1599,
            "canonical_total": 2368,
            "unprocessed_backlog": 769,
            "serp_queries": "5/10",
        },
        "key_checkpoint_references": [
            PRIOR_TAG,
            PLANNED_TAG,
            "CORVONERO-PRE-EXPORT-PRODUCTION-CHECKPOINT-v1",
            "CORVONERO-EXPORT-READINESS-MATRIX-v1",
        ],
        "excluded_scopes": [
            ".git",
            "secrets and .env",
            "unrelated projects (OCPilot, FP-0002, Website Factory)",
            "projects/projects/",
            "recovery temp directories",
            "node_modules and runtime locks",
            "unreferenced ORCA live-model reports",
        ],
        "secret_scan_excluded_files": secret_hits,
        "creation_timestamp": datetime.now(timezone.utc).isoformat(),
        "files": manifest_files,
    }

    manifest_path = STORAGE_DIR / "CORVONERO-PRE-EXPORT-PRODUCTION-2026-06-29-MANIFEST.json"
    sha_path = STORAGE_DIR / "CORVONERO-PRE-EXPORT-PRODUCTION-2026-06-29-SHA256.txt"
    readme_path = STORAGE_DIR / "CORVONERO-PRE-EXPORT-PRODUCTION-2026-06-29-README.md"

    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    sha_path.write_text(f"{archive_sha}  {ARCHIVE_NAME}\n", encoding="utf-8")
    readme_path.write_text(
        "\n".join(
            [
                "# CORVONERO PRE-EXPORT PRODUCTION ARCHIVE",
                "",
                f"Date: 2026-06-29",
                f"Git commit: {commit_sha or head}",
                f"Tag: {PLANNED_TAG}",
                f"Prior checkpoint: {PRIOR_TAG} @ {PRIOR_COMMIT}",
                "",
                "Contents: Corvonero pilot, reports, workspace intake, MIG research, ORCA clean-room semantic core.",
                "Phase 7A staging preparation preserved. No ads, Commander import, or advertising.",
                "",
                "Verify: compare SHA256 in CORVONERO-PRE-EXPORT-PRODUCTION-2026-06-29-SHA256.txt before restore.",
                f"File count in manifest: {len(manifest_files)}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    # Validation
    with zipfile.ZipFile(archive_path, "r") as zf:
        names = zf.namelist()
        required = [
            "repository/projects/mars-search-ppc-production/pilots/corvonero/",
            "repository/workspaces/corvonero-yandex-direct/",
        ]
        for req in required:
            if not any(n.startswith(req) for n in names):
                raise RuntimeError(f"Missing expected root in archive: {req}")
        forbidden = ["projects/ocpilot/", "workspaces/fp-0002", "projects/projects/"]
        for bad in forbidden:
            if any(bad in n for n in names):
                raise RuntimeError(f"Forbidden path in archive: {bad}")

    recomputed = sha256_file(archive_path)
    if recomputed != archive_sha:
        raise RuntimeError("Archive SHA-256 mismatch on recomputation")

    with zipfile.ZipFile(archive_path, "r") as zf:
        zip_count = sum(1 for n in zf.namelist() if not n.endswith("/"))
    if zip_count != len(manifest_files):
        raise RuntimeError(f"Manifest count {len(manifest_files)} != zip file count {zip_count}")

    return {
        "archive_path": str(archive_path),
        "archive_sha256": archive_sha,
        "archive_size": archive_size,
        "file_count": len(manifest_files),
        "secret_hits": secret_hits,
    }


def main() -> None:
    if os.environ.get("CORVONERO_OPERATOR_GATE") != "APPROVED":
        raise SystemExit(
            "STOP: CORVONERO_OPERATOR_GATE=APPROVED required. "
            "This script is not safe for casual execution."
        )

    head = run_git("rev-parse", "HEAD")
    print(f"HEAD={head}")

    rel_paths = collect_inventory_paths()
    archive_prefixes = (
        "projects/mars-search-ppc-production/pilots/corvonero/",
        "projects/mars-search-ppc-production/reports/REPORT-corvonero",
        "workspaces/corvonero-yandex-direct/",
        "incoming/mig/pilots/corvonero/",
        "projects/orca/projects/corvonero-direct-v2-clean-room/",
    )

    records = []
    secret_audit: list[str] = []
    for rel in rel_paths:
        path = REPO / rel
        if not path.is_file():
            continue
        if audit_secret_reference(path):
            secret_audit.append(rel)
        records.append(
            {
                "path": rel,
                "classification": classify(rel),
                "git": git_state(rel),
                "size": path.stat().st_size,
                "sha256": sha256_file(path),
                "in_archive": "yes"
                if any(rel.startswith(p) for p in archive_prefixes)
                else "no",
            }
        )

    matrix = build_export_matrix()
    matrix_json = PILOT / "CORVONERO-EXPORT-READINESS-MATRIX-v1.json"
    matrix_md = PILOT / "CORVONERO-EXPORT-READINESS-MATRIX-v1.md"
    matrix_json.write_text(json.dumps(matrix, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    md = [
        "# CORVONERO Export Readiness Matrix v1",
        "",
        f"Generated: {matrix['generated_at']}",
        "",
        "## Semantic boundary",
        "",
        "- Assessed semantics: **1599 / 2368**",
        "- Unprocessed backlog: **769**",
        "- SERP coverage: **5 / 10 queries**",
        "",
        "## D1 — Advertisements Word document",
        "",
        f"**Readiness:** `{matrix['deliverables']['D1_advertisements_word']['readiness']}`",
        "",
        "### Available sources",
    ]
    for s in matrix["deliverables"]["D1_advertisements_word"]["available_sources"]:
        md.append(f"- {s}")
    md.append("\n### Missing components")
    for s in matrix["deliverables"]["D1_advertisements_word"]["missing_components"]:
        md.append(f"- {s}")

    md.extend(["", "## D2 — Landing-page Word files for Roman", ""])
    for lp, info in matrix["deliverables"]["D2_landing_page_word_roman"]["pages"].items():
        md.append(f"- **{lp}**: `{info['readiness']}`")

    d3 = matrix["deliverables"]["D3_yandex_direct_commander_excel"]
    md.extend(
        [
            "",
            "## D3 — Yandex Direct Commander Excel",
            "",
            f"**Readiness:** `{d3['readiness']}`",
            "",
            "## D4 — Consolidated Research Excel",
            "",
            f"**Readiness:** `{matrix['deliverables']['D4_consolidated_research_excel']['readiness']}`",
            "",
            "### Limitations",
            "- SERP: 5 / 10 queries",
            "- Assessed semantics: 1599 / 2368",
            "- Unprocessed backlog: 769",
        ]
    )
    matrix_md.write_text("\n".join(md) + "\n", encoding="utf-8")

    inv_path = write_inventory(records, head)
    write_checkpoint(
        head,
        matrix,
        str(inv_path.relative_to(REPO)).replace("\\", "/"),
        len(records),
    )

    print(f"Inventory records: {len(records)}")
    print(f"Secret audit hits in canonical scope: {len(secret_audit)}")
    if secret_audit:
        print("SECRET HITS:", secret_audit[:10])

    summary = {
        "head": head,
        "inventory_count": len(records),
        "inventory_path": str(inv_path),
        "secret_hits": secret_audit,
    }
    (REPO / ".tools" / "corvonero-pre-export-backup-summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
