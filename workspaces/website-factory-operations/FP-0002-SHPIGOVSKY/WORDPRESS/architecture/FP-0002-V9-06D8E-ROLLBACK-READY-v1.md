# FP-0002 V9-06D8-E — Rollback Ready v1

**Checkpoint:** `v9-06d8e-contacts-content-seed-pre-20260704-211441`  
**Root:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d8e-contacts-content-seed-pre-20260704-211441\`

## Changed fields (3)

- `contacts_form_intro`
- `contacts_address`
- `contacts_blocks`

## Rollback paths

1. **Per-field:** `contacts-page-20-pre-values.json` + `update_field` on page 20
2. **Full DB:** restore `mars_wp_fp0002.sql` from checkpoint

## D8-A snapshot

Read-only copy: `d8a-site-options-snapshot-readonly.json` in checkpoint root.

Rollback not executed — seed succeeded.

Evidence: `validation/v9-06d8e-contacts-content-seed/rollback-readiness.json`
