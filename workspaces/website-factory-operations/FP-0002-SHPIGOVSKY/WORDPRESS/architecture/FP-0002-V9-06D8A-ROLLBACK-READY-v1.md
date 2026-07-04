# FP-0002 V9-06D8A Rollback Ready v1

**Date:** 2026-07-05  
**Task:** V9-06D8-A  
**Status:** READY_PENDING_DB — no checkpoint yet

---

## Checkpoint (when apply authorized)

**Root:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d8a-site-options-seed-pre-<timestamp>\`

**Contents:**

- Full dump `mars_wp_fp0002`
- Manifest (DB name, prefix, timestamp, tool)
- Pre-mutation option field snapshot JSON
- Restore instructions

## Per-field rollback

For each allowlisted field written via `update_field( $name, $old_value, 'option' )` using pre-checkpoint values (empty for D8 baseline).

## Full DB rollback

Restore mysqldump; verify object counts unchanged; re-run 7-route smoke.

## Current state

No mutation performed — rollback not executed.

## Evidence

`validation/v9-06d8a-site-options-seed/rollback-readiness.json`
