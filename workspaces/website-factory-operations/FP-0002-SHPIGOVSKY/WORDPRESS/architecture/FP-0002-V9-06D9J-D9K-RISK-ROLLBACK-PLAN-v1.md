# FP-0002 V9-06D9J D9-K Risk Rollback Plan v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9j-media-selection-upload-plan/d9k-risk-rollback-plan.json`

## Preconditions (K1)

1. **DB checkpoint** — full `mars_wp_fp0002` mysqldump before any upload/seed.
2. **Pre-values JSON** — `home_hero_slides`, `home_gallery_media` on page #4.
3. **Uploads manifest template** — empty attachment ID list to fill during K2.

## Rollback methods

| Method | When | Action |
|--------|------|--------|
| DB restore | Preferred | Restore K1 mysqldump |
| Attachment delete | Partial, operator-approved list only | Delete manifest attachment IDs; **does not** revert ACF without DB restore |

## Forbidden rollback actions

- Broad uploads directory cleanup
- Full uploads deletion
- `wp media regenerate` without separate approval

## Risks

| Risk | Prevention | Rollback |
|------|------------|----------|
| Wrong hero image | SHA256 verify against V9 src `48CBA0B7509915E3E2CEDB1C5239FF594B9070A5908FC937E345C8517AF0BEA1` | DB restore |
| Gallery order mismatch | Seed order = fallback order | DB restore or clear repeater |
| Orphan attachments | Record all new attachment IDs in manifest | Delete manifest IDs only |

## Post-K evidence required

- Attachment IDs manifest
- Post-seed ACF verification JSON
- Visual regression vs D9-J screenshots
