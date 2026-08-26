# CLEANUP-BACKUP-MANIFEST-v1

## Private local backup (outside Git)

| Field | Value |
|-------|-------|
| Wave root | `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\group-filter-test-cleanup-20260826-local\` |
| Private dir | `...\private-cleanup\` |
| Dry inventory | `forensic\CLEANUP-DRY-INVENTORY-2026-08-26T09-50-09-718Z.json` |
| Pass1 sanitized result | `forensic\CLEANUP-RESULT-SANITIZED-2026-08-26T09-50-09-718Z.json` |
| Pass2 row result | `forensic\CLEANUP-ROW-RESULT-2026-08-26T09-54-53-609Z.json` |
| PRE Admin workflow | `backups\Admin.dev.PRE-PATCH-2026-08-26T09-48-02-505Z.raw.json` |
| POST Admin workflow | `backups\Admin.dev.POST-FINAL-2026-08-26T10-01-21-851Z.raw.json` |

## Record counts (logical)

| Item | Count |
|------|------:|
| CLEAN rows at inventory | 155 |
| Proven pending unique (dry) | 49 |
| Pass2 additional rows by row_number | 23 |
| Proven pending after cleanup | **0** |

Checksums: workflow `sha16_nodes` post-patch/post-final = `62CB6CEC5ED92C86`.

No PII / secrets committed to Git.
