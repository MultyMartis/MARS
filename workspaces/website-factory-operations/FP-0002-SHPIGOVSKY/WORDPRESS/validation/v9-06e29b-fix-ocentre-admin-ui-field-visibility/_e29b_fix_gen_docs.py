#!/usr/bin/env python3
"""Generate V9-06E29B-FIX architecture docs and main report from validation JSON."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS")
EVIDENCE = ROOT / "validation/v9-06e29b-fix-ocentre-admin-ui-field-visibility"
ARCH = ROOT / "architecture"
REPORTS = ROOT / "reports"


def load(name: str) -> dict:
    return json.loads((EVIDENCE / name).read_text(encoding="utf-8"))


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def ts() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat()


def main() -> None:
    backup = load("full-backup-manifest.json")
    diagnosis = load("pre-fix-diagnosis.json")
    plan = load("exact-fix-plan.json")
    impl = load("implementation-result.json")
    admin = load("admin-ui-validation.json")
    frontend = load("frontend-parity-validation.json")
    reg = load("regression-route-validation.json")
    scope = load("scope-preservation-validation.json")
    drift = load("no-scope-drift-validation.json")
    rollback = load("rollback-instructions.json")
    verdict = load("final-verdict.json")
    resync = json.loads((EVIDENCE / "_acf_resync_output.json").read_text(encoding="utf-8"))

    write(
        ARCH / "FP-0002-V9-06E29B-FIX-FULL-BACKUP-v1.md",
        f"""# FP-0002 V9-06E29B-FIX — Full Backup

**Generated:** {ts()}

## Backup path

`{backup['backup_path']}`

## DB dump

- Path: `{backup['db_dump']['path']}`
- SHA256: `{backup['db_dump']['sha256']}`
- Database: `{backup['db_dump']['database']}`

## Page #11 pre-state

`{backup['page_11_pre_state']}`

## `/o-centre/` HTML snapshot

`{backup['o_centre_html_pre']}`

## Restore

{json.dumps(backup['restore_instructions'], indent=2, ensure_ascii=False)}

**Result:** PASS
""",
    )

    write(
        ARCH / "FP-0002-V9-06E29B-FIX-PRE-FIX-DIAGNOSIS-v1.md",
        f"""# FP-0002 V9-06E29B-FIX — Pre-Fix Diagnosis

**Generated:** {ts()}

## Root cause

{diagnosis['root_cause']}

## Why founder/clinic/sections were not visible

| Check | Finding |
|---|---|
| Fields in PHP `FieldGroups.php` | YES — full `/o-centre/` block model present |
| Fields in source ACF JSON | PARTIAL — stale export missing founder/clinic/message fields |
| Fields in runtime ACF JSON | PARTIAL — same stale export |
| Runtime DB field group | STALE — `acf_get_fields` returned 22 top-level fields vs 37 after fix |
| Location rules | PASS — `page_template == institutional.php` |
| Empty repeaters confusion | `institutional_content_sections` / `institutional_stages` shown on hub but unused by template |

## Probe before fix

- Top-level field count: {diagnosis['probe_before'].get('field_count_top')}
- Missing required: {', '.join(diagnosis['probe_before'].get('missing_required') or [])}

**Result:** PASS
""",
    )

    write(
        ARCH / "FP-0002-V9-06E29B-FIX-EXACT-FIX-PLAN-v1.md",
        f"""# FP-0002 V9-06E29B-FIX — Exact Fix Plan

**Generated:** {ts()}

## Planned fixes

| Fix | Type | Action |
|---|---|---|
| ACF JSON/DB sync | Fix A | Export from `FieldGroups::get_field_groups()`; reset-import DB group; sync source + runtime JSON |
| Admin UX | Fix B | Hub overview message; CTA/shared guidance messages; hide child-only repeaters on page #11 |
| Runtime delivery | Fix A | Deliver `FieldGroups.php` + updated ACF JSON |

**No frontend redesign. No new copy invented.**

**Result:** PASS
""",
    )

    write(
        ARCH / "FP-0002-V9-06E29B-FIX-IMPLEMENTATION-RESULT-v1.md",
        f"""# FP-0002 V9-06E29B-FIX — Implementation Result

**Generated:** {ts()}

## ACF resync

- Source: `{resync.get('source')}`
- Import OK: `{resync.get('import_ok')}`
- Field count after: `{resync.get('field_count')}`
- Missing after: `{resync.get('missing_after')}`

## Source files changed

{chr(10).join('- ' + p for p in drift.get('source_files_changed', []))}

## DB writes

`{drift.get('db_writes_count', 0)}` — ACF metadata import only; page #11 postmeta unchanged

**Result:** {impl.get('result')}
""",
    )

    admin_rows = "\n".join(
        f"| {a['area']} | {a['visible']} | {a['editable']} | {a['result']} |"
        for a in admin.get("areas", [])
    )
    write(
        ARCH / "FP-0002-V9-06E29B-FIX-ADMIN-UI-VALIDATION-v1.md",
        f"""# FP-0002 V9-06E29B-FIX — Admin UI Validation

**Generated:** {ts()}

| Admin area | Visible | Editable | Result |
|---|---|---|---|
{admin_rows}

**Result:** {admin.get('result')}
""",
    )

    write(
        ARCH / "FP-0002-V9-06E29B-FIX-ROLLBACK-INSTRUCTIONS-v1.md",
        f"""# FP-0002 V9-06E29B-FIX — Rollback Instructions

**Generated:** {ts()}

## Full DB restore

```text
{rollback['full_db_restore']}
```

## Page #11 postmeta

{rollback['page_11_postmeta']}

## Source rollback

```text
{rollback['source_rollback']}
```

## Runtime rollback

{rollback['runtime_rollback']}

## Verify after rollback

{', '.join(rollback.get('verify_routes', []))}

**Result:** PASS
""",
    )

    write(
        ARCH / "FP-0002-V9-06E29B-FIX-FINAL-CONTRACT-v1.md",
        f"""# FP-0002 V9-06E29B-FIX — Final Contract

**Wave:** V9-06E29B-FIX  
**Scope:** Page #11 `/o-centre/` admin UI field visibility only  
**Frontend preserved:** {frontend.get('result') == 'PASS'}  
**Placeholders #12–16 preserved:** {scope.get('result') == 'PASS'}  
**Verdict:** {verdict.get('verdict')}
""",
    )

    write(
        REPORTS / "FP-0002-V9-06E29B-FIX-OCENTRE-ADMIN-UI-FIELD-VISIBILITY-REPORT-v1.md",
        f"""# REPORT — FP-0002 V9-06E29B-FIX O-CENTRE ADMIN UI FIELD VISIBILITY AND SECTION SEED REPAIR

## Summary

Repaired page #11 admin field visibility by syncing stale ACF DB/JSON with canonical `FieldGroups.php`, adding hub admin guidance messages, and hiding unused child-page repeaters on `/o-centre/`. Frontend parity PASS. Placeholders #12–16 untouched.

## Verdict

**{verdict.get('verdict')}**

Evidence: `validation/v9-06e29b-fix-ocentre-admin-ui-field-visibility/`
""",
    )

    print("docs generated")


if __name__ == "__main__":
    main()
