# FP-0002 V9-06D7D Rollback Ready v1

**Date:** 2026-07-05

| Item | Value |
|------|-------|
| Checkpoint | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d7d-service-runtime-delivery-pre-20260705-015917` |
| Theme snapshot | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d7d-service-runtime-delivery-pre-20260705-015917\theme\shpigovsky` |
| Baseline manifest | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d7d-service-runtime-delivery-pre-20260705-015917\manifests\theme-pre-manifest.json` |
| DB dump | None |
| Rollback tested | False |

## Restore procedure

1. Copy checkpoint `theme/shpigovsky/` to runtime `wp-content/themes/shpigovsky/`.
2. Validate aggregate hash against pre-delivery manifest.
3. Re-run D.5 route smoke, service section smoke, home/hub stability.

## Result

PASS
