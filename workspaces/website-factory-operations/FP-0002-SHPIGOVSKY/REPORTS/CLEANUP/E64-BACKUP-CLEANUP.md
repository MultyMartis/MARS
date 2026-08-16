# E64 Backup Cleanup

## Scope

Root: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\`  
Before: **155** directories, **~14.66 GB**  
After: **139** directories, **~12.60 GB** (includes new E64 docs safety snapshot + post-cleanup pack)

## Protected checkpoints (retained)

1. `v9-stable-v1-near-production-freeze-20260718-004137` (~1.17 GB)
2. `v9-06e63-before-stable-v1-closeout-20260718-003355` (~1.44 GB) — KEEP_UNTIL_PRODUCTION
3. `v9-06e58-current-baseline-freeze-before-visual-audit-20260716-225434` (~1.33 GB)
4. `v9-06e53-admin-ux-section-styling-freeze-accepted-before-experience-pack-20260716-053214` (~116 MB)

## Deleted (exact allowlist — 17 directories)

From `E64-BACKUP-DELETION-ALLOWLIST.txt`:

- E54 full + FIX01 tiny
- E55 tiny
- E56 full + FU01/FU02 tiny
- E57 + FIX01/FIX02 tiny
- E60 + FIX01 tiny
- E62A–E62E + E62E-FIX01 tiny

**Reclaimed backups:** **2,211,034,969 bytes (~2.06 GB)**

Each deletion used literal absolute path. Protected paths re-validated every 5 deletions.

## Manual review (retained this wave)

- `v9-06e59-before-layout-polish-maps-footer-comfort-admin-20260717-001046` (~280 MB)
- `v9-06e59-fix01-before-comfort-contacts-footer-corrections-20260717-013408` (~282 MB)
- `v9-06e61-before-admin-controls-contacts-blog-reviews-ocentre-home-20260717-141747` (~281 MB)
- All **pre-E54** backup directories (~132) — deferred per Phase 2 policy

## Not deleted

No wildcard / parent-root deletion. No Stable / E63 / E58 / E53 paths touched.
