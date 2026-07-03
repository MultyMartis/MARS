# FP-0002 V9-06D.3 Future Migration Rollback Plan v1

Planning only for later writable phases.

## Requirements before any content write

1. DB dump checkpoint under `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\`
2. Exact created/modified object ID list
3. Exact ACF field keys written
4. Options keys written (if any)
5. Media attachment IDs (if any)
6. Whether rewrite flush occurred

## Rollback steps

1. Stop writes
2. Restore DB dump
3. If media uploaded, remove listed attachments only
4. If rewrite flushed, re-evaluate permalinks; do not blindly re-flush
5. Validate object counts, templates, menus, empty/non-empty ACF expectations

## Checkpoint naming

`v9-06d4-minimal-content-seed-pre-YYYYMMDD-HHMMSS`

## Result

DEFINED — not executed in D.3.
