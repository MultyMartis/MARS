# FP-0002 V9-06D8B Rollback Ready v1

**Date:** 2026-07-05

## Checkpoint

- **Name:** `v9-06d8b-home-content-seed-pre-20260704-204316`
- **Root:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d8b-home-content-seed-pre-20260704-204316\`
- **DB dump:** `mars_wp_fp0002.sql`
- **Pre-values:** `home-page-4-pre-values.json`

## Changed Home fields (post-seed)

| Field | Rollback |
|---|---|
| `home_advantages` | Restore empty/null from pre-values |
| `home_faq_items` | Restore empty/null from pre-values |

## Procedures

1. **Per-field:** `update_field` from `home-page-4-pre-values.json`
2. **Full DB:** `mysql -u root mars_wp_fp0002 < mars_wp_fp0002.sql`
3. **Post-rollback validation:** Home `/` + seven route smoke + options snapshot

Rollback not executed — seed succeeded.

Evidence: `validation/v9-06d8b-home-content-seed/rollback-readiness.json`
