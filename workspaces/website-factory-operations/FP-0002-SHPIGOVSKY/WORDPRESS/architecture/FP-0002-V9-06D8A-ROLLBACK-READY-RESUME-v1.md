# FP-0002 V9-06D8A Rollback Ready Resume v1

**Date:** 2026-07-05  
**Status:** READY — rollback not executed

---

## Checkpoint

- **Root:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d8a-site-options-seed-pre-20260705-033228\`
- **Dump:** `mars_wp_fp0002.sql` (~1.07 MB)
- **Pre-values:** all 16 allowlisted option fields empty

## Per-field rollback

For each of 11 changed fields: `update_field($name, null, 'option')` or restore empty pre-seed state from dry-run rollback_value.

## Full DB rollback

```text
mysql -h 127.0.0.1 -u mli_shpigovsky_app -p mars_wp_fp0002 < mars_wp_fp0002.sql
```

## Post-rollback validation

1. Verify 16 option field states
2. Seven-route smoke
3. Object counts (pages 22, services 15, menus 3)

Rollback not tested — seed succeeded and site healthy.

Evidence: `validation/v9-06d8a-site-options-seed/rollback-readiness-resume.json`
