# FP-0002 V9-06E16 — Pre-Change Backup Checkpoint

**Evidence:** `validation/v9-06e16-operator-qa-closure-reusable-blocks-clone-cleanup-audit/pre-change-backup-checkpoint.json`

## Backup root

`X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e16-pre-admin-architecture-and-cleanup-audit-20260707-223340`

## Contents

| Item | Path | Result |
|------|------|--------|
| Full DB dump | `mars_wp_fp0002.sql` (~2.1 MB) | PASS |
| Page snapshot | `db-snapshots/pages-posts.json` | PASS |
| Service CPT snapshot | `db-snapshots/service-posts.json` | PASS |
| Options/menus probe | `db-snapshots/options-menus-meta-counts.txt` | PASS |
| Route probes | `db-snapshots/route-probe-e16.json` | PASS |
| Runtime theme hashes | `runtime-theme/inventory-hash.json` | PASS |
| Runtime plugin hashes | `runtime-plugin/inventory-hash.json` | PASS |
| Repo ACF JSON hashes | `acf-json/inventory-hash.json` | PASS |
| Restore instructions | `RESTORE-INSTRUCTIONS.md` | PASS |
| Manifest | `backup-manifest.json` | PASS |

## Restore (summary)

1. Stop WordPress writes.
2. `mysql mars_wp_fp0002 < mars_wp_fp0002.sql`
3. Verify theme/plugin hash inventories if source drift suspected.

**Not committed to Git:** dump and backup payload remain on `X:\MARS-Localhost` only.
