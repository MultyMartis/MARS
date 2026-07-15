# PC14-FU03 Production Apply — Rollback Notes

**Date:** 2026-07-16

## Backup

| Field | Value |
|-------|-------|
| Raw backup | `local/pc14-fu03-production-apply-2026-07-16/rollback/worker-before-pc14-fu03.raw.json` |
| Production id | `p4mqb4VuPcemIDlC` |
| updatedAt before | `2026-07-13T21:49:02.829Z` |
| Node count before | `92` (92) |
| After updatedAt | `2026-07-15T21:09:45.123Z` |
| After node count | `101` |

## Restore strategy

If rollback is required:

1. Load raw backup JSON from the path above.
2. PUT `name` + `nodes` + `connections` + `settings` to workflow `p4mqb4VuPcemIDlC` (same safe payload shape as apply).
3. Re-GET and verify: active=true, node count=92, 0 FU03 nodes, TZ HOTFIX01 intact, PC-07 mapping intact.
4. Do **not** activate/deactivate as a separate step.
5. Do **not** use sanitized exports for restore (credentials are redacted).

## Do not

- Prefer git history over raw backup for live restore
- Copy sandbox workflow as restore source
- Mutate Intake/Admin during rollback
