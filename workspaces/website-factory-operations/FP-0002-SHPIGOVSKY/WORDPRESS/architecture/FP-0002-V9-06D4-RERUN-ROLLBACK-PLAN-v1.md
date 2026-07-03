# FP-0002 V9-06D.4 RERUN Rollback Plan v1

## Checkpoint

`X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06d4-rerun-minimal-content-seed-pre-20260704-054146\`

Database dump:

`database\mars_wp_fp0002-v9-06d4-rerun-pre.sql`

## Modified objects

- Pages: 4, 5, 20
- Services: 73, 74, 77, 84

## Restore procedure

1. Stop further content writes to the local FP-0002 runtime.
2. Restore only local DB `mars_wp_fp0002` from the checkpoint SQL dump.
3. Re-validate authorized object baseline hashes and global counts:
   - Pages total unchanged
   - Services total = 15
   - Posts total unchanged
   - Menus / options / rewrite_rules hashes match pre-write baseline
4. Confirm ACF content fields on authorized objects are empty/non-seeded again.

## Field-level alternative

Only if full DB restore is unavailable and field-level rollback is fully deterministic:

1. Clear ACF fields listed in `FP-0002-V9-06D4-RERUN-SEEDED-OBJECT-REGISTRY-v1.json`
2. Restore `migration_status`, `seeded_by_phase`, `skeleton_status` from pre-write baseline

Prefer full DB restore.

## Rollback execution status

- Apply succeeded
- Rollback **not executed**
- Rollback readiness: **READY**
