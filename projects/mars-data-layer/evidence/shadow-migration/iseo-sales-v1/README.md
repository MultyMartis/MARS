# Evidence index — ISEO Sales shadow migration v1

## Committed (sanitized)

- `RECONCILIATION-MATRIX-v1.md`
- `IDEMPOTENCY-v1.json`
- `DELTA-IMPORT-DESIGN-v1.md`
- `SAMPLE-VALIDATION-v1.md`
- `PROVE-LIVE-v1.json`
- `CUTOVER-BLOCKERS-v1.md`
- Selected run artifacts without customer payloads:
  - `run_apply_20260903T091128Z/transform_counters.json`
  - `run_apply_20260903T091128Z/sheet_raw_headers.json`
  - `run_apply_20260903T091128Z/sheet_clean_headers.json`
  - `run_apply_20260903T091128Z/apply_sql_meta.json`
  - `run_dry-run_20260903T090702Z/transform_counters.json`
  - `run_prove-live_20260903T090906Z/result.json`

## Host-only (not committed)

- Full `inventory_sanitized.json` / `result.json` apply dumps (may contain residual display strings)
- `apply.sql` and logical dumps under `/root/mars-backups/postgres/`
- n8n encryption material / OAuth tokens

Operator may retain host `/tmp/mars-iseo-shadow-*` workdirs for offline audit.
