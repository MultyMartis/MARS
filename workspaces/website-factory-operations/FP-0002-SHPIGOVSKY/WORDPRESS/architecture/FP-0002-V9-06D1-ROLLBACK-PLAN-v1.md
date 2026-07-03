# FP-0002 V9-06D.1 Rollback Plan v1

**Result:** READY — rollback not executed because delivery validated successfully.

## Checkpoint

- Root: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d1-rerun-runtime-delivery-pre-20260704-032355`
- Theme snapshot: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d1-rerun-runtime-delivery-pre-20260704-032355\theme`
- Plugin snapshot: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d1-rerun-runtime-delivery-pre-20260704-032355\plugin`
- ACF JSON snapshot: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d1-rerun-runtime-delivery-pre-20260704-032355\acf-json`
- Manifest count: 3
- DB dump: not created; filesystem-only delivery, no intentional DB writes, no rewrite flush.

## Restore procedure

1. Restore checkpoint `theme/` only to `wp-content/themes/shpigovsky/`.
2. Restore checkpoint `plugin/` only to `wp-content/plugins/shpigovsky-core/`.
3. Restore checkpoint `acf-json/` only to `wp-content/acf-json/`.
4. Validate restored aggregate hashes against checkpoint `manifests/`.
5. Run frontend/admin smoke and object immutability checks.

## Trigger conditions

- Runtime PHP lint failure.
- Frontend/wp-admin fatal after delivery.
- Hash mismatch in delivered files.
- Unexpected WordPress object mutation.
- External plugin or WordPress core drift.

## Verdict

Rollback readiness: READY. Rollback was not executed because V9-06D.1 rerun passed.
