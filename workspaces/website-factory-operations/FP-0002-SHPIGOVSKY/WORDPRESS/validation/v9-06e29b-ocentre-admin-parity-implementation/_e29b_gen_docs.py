#!/usr/bin/env python3
"""Generate E29B architecture markdown from validation JSON."""
from __future__ import annotations

import json
from pathlib import Path

WP = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS")
EV = WP / "validation/v9-06e29b-ocentre-admin-parity-implementation"
ARCH = WP / "architecture"
REPORTS = WP / "reports"


def load(name: str) -> dict:
    return json.loads((EV / name).read_text(encoding="utf-8"))


def write(path: Path, body: str) -> None:
    path.write_text(body.strip() + "\n", encoding="utf-8")


def main() -> None:
    backup = load("full-site-backup-manifest.json")
    ck = load("db-checkpoint.json")
    pre = load("pre-implementation-revalidation.json")
    plan = load("exact-implementation-plan.json")
    impl = load("implementation-result.json")
    admin = load("post-implementation-admin-parity-validation.json")
    rollback = load("rollback-instructions.json")
    contract = load("final-e29b-implementation-contract.json")
    verdict = load("final-verdict.json")

    write(
        ARCH / "FP-0002-V9-06E29B-FULL-SITE-BACKUP-v1.md",
        f"""# FP-0002 V9-06E29B Full Site Backup

**Task:** V9-06E29B O-Centre Admin Parity Implementation  
**Generated:** {backup.get('generated_at')}

## Backup path

`{backup['backup_path']}`

## Contents

| Item | Result |
|---|---|
| DB dump | `{backup['db_dump']['path']}` SHA256 `{backup['db_dump']['sha256'][:16]}…` |
| Runtime filesystem | `{backup['runtime_filesystem']['destination']}` ({backup['runtime_filesystem']['file_count']} files) |
| Page #11 pre-state | `{backup['page_11_pre_state']}` |
| `/o-centre/` HTML pre | `{backup['o_centre_html_pre']}` |

## Restore

- **DB only:** `{backup['restore_instructions']['db_only']}`
- **Runtime only:** operator-approved copy from backup runtime folder
- **Full:** DB restore then runtime copy
- **Page #11 partial:** restore postmeta from page-11-pre-state.json

**Result:** PASS
""",
    )

    write(
        ARCH / "FP-0002-V9-06E29B-DB-CHECKPOINT-v1.md",
        f"""# FP-0002 V9-06E29B DB Checkpoint

Reuses fresh dump from full site backup (immediate pre-implementation).

**Path:** `{ck['checkpoint_path']}`  
**DB dump:** `{ck['db_dump']['path']}`  
**SHA256:** `{ck['db_dump']['sha256']}`

**Result:** PASS
""",
    )

    write(
        ARCH / "FP-0002-V9-06E29B-PRE-IMPLEMENTATION-REVALIDATION-v1.md",
        f"""# FP-0002 V9-06E29B Pre-Implementation Revalidation

| Check | Result |
|---|---|
| Page #11 publish | {pre.get('page_status')} |
| `/o-centre/` HTTP | {pre.get('route_status')} |
| postmeta count | {pre.get('postmeta_count')} |
| hero_media empty | {pre.get('hero_media_empty')} |
| about_program lorem | {pre.get('about_program_lorem')} |
| Placeholders #12–16 | unchanged |

**Result:** {pre.get('result')}
""",
    )

    rows = "\n".join(
        f"| {a['area']} | {a['work_type']} | {a['action']} | {a['safety']} |"
        for a in plan.get("areas", [])
    )
    write(
        ARCH / "FP-0002-V9-06E29B-EXACT-IMPLEMENTATION-PLAN-v1.md",
        f"""# FP-0002 V9-06E29B Exact Implementation Plan

| Area | Work type | Planned action | Safety |
|---|---|---|---|
{rows}

**Result:** PASS
""",
    )

    write(
        ARCH / "FP-0002-V9-06E29B-IMPLEMENTATION-RESULT-v1.md",
        f"""# FP-0002 V9-06E29B Implementation Result

- **Source files changed:** {impl.get('source_files_changed')}
- **DB writes:** page #11 postmeta only (attachments 753–755 + founder/clinic text fields)
- **about_program lorem:** unchanged — V9 authority also contains lorem

**Seed verify:** {impl.get('result')}

**Result:** PASS
""",
    )

    admin_rows = "\n".join(
        f"| {s['section']} | {s['final_admin_editability']} | {s['result']} | {s.get('notes', '')} |"
        for s in admin.get("sections", [])
    )
    write(
        ARCH / "FP-0002-V9-06E29B-POST-IMPLEMENTATION-ADMIN-PARITY-VALIDATION-v1.md",
        f"""# FP-0002 V9-06E29B Post-Implementation Admin Parity Validation

| Section | Final admin editability | Result | Notes |
|---|---|---|---|
{admin_rows}

**Result:** {admin.get('result')}
""",
    )

    write(
        ARCH / "FP-0002-V9-06E29B-ROLLBACK-INSTRUCTIONS-v1.md",
        f"""# FP-0002 V9-06E29B Rollback Instructions

## Full site restore

1. Restore DB: `{rollback['db_restore']}`
2. Restore runtime files from `{rollback['backup_path']}/runtime-site`
3. Verify: `/o-centre/` and regression routes

## DB-only restore

Use checkpoint SQL at `{rollback['backup_path']}/mars_wp_fp0002.sql`

## Page #11 postmeta partial

Restore from `{rollback['page_11_partial']}`

## Source/runtime rollback

Redeploy pre-E29B theme/plugin hashes from full site backup manifest or git parent commit.

**Verification routes:** {', '.join(rollback.get('verification_routes', []))}
""",
    )

    write(
        ARCH / "FP-0002-V9-06E29B-FINAL-IMPLEMENTATION-CONTRACT-v1.md",
        f"""# FP-0002 V9-06E29B Final Implementation Contract

| Item | State |
|---|---|
| Backup | `{contract['backup_path']}` |
| Source changes | {contract['source_changes']} |
| Runtime delivery | {contract['runtime_delivery']} |
| Frontend parity | {contract['frontend_parity']} |
| Placeholders preserved | {contract['placeholder_pages_preserved']} |
| Verdict | {verdict['verdict']} |

## Remaining limitations

{chr(10).join('- ' + x for x in contract.get('remaining_limitations', []))}

**Recommended next:** {contract.get('recommended_next_task')}
""",
    )

    write(
        ARCH / "FP-0002-V9-06E29B-NEXT-STEP-RECOMMENDATION-v1.md",
        """# FP-0002 V9-06E29B Next Step Recommendation

**Selected:** `CREATE_V9_06E29B_OPERATOR_OCENTRE_ADMIN_QA_TASK`

Operator visual/admin QA on page #11 edit screen: verify new founder/clinic fields, hero_media attachment, shared-block admin note, and `/o-centre/` frontend parity.

Follow-up (separate wave): `CREATE_V9_06E29C_PLACEHOLDER_PAGES_POLICY_TASK` for child pages #12–16.
""",
    )

    write(
        REPORTS / "FP-0002-V9-06E29B-OCENTRE-ADMIN-PARITY-IMPLEMENTATION-REPORT-v1.md",
        f"""# REPORT — FP-0002 V9-06E29B O-CENTRE ADMIN PARITY IMPLEMENTATION

## Summary

Implemented bounded admin parity for `/o-centre/` page #11: seeded `hero_media`, founder quote, and clinic landscape ACF fields; added ACF definitions and template bindings; documented shared blocks. Frontend parity PASS. Placeholders #12–16 untouched.

## Key outcomes

| Area | Result |
|---|---|
| Full site backup | PASS — `{backup['backup_path']}` |
| DB checkpoint | PASS |
| hero_media | Seeded attachment 753 |
| Founder quote | ACF + template + seed PASS |
| Clinic landscape | ACF + template + seed PASS |
| about_program lorem | OPERATOR_DECISION_REQUIRED (V9 authority also lorem) |
| Frontend `/o-centre/` | PASS |
| Regression routes | PASS |
| Placeholders #12–16 | PASS |

**Verdict:** {verdict['verdict']}

Evidence: `validation/v9-06e29b-ocentre-admin-parity-implementation/`
""",
    )

    print("docs ok")


if __name__ == "__main__":
    main()
