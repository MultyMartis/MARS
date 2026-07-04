# FP-0002 V9-06D7E Rollback Ready v1

**Date:** 2026-07-05

| Item | Value |
|------|-------|
| Checkpoint | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d7e-contacts-runtime-delivery-pre-20260705-022630` |
| Theme snapshot | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d7e-contacts-runtime-delivery-pre-20260705-022630\theme\shpigovsky` |
| Baseline manifest | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d7e-contacts-runtime-delivery-pre-20260705-022630\manifests\theme-pre-manifest.json` |
| DB dump | None |
| Rollback tested | False |

## Restore procedure

1. Copy checkpoint `theme/shpigovsky/` to runtime `wp-content/themes/shpigovsky/`.
2. Validate aggregate hash against pre-delivery manifest.
3. Re-run D.5 route smoke, contacts section smoke, home/hub/service stability.

## Result

PASS
