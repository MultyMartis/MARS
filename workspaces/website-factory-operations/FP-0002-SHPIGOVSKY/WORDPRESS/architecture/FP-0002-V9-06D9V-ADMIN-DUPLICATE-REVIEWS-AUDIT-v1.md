# FP-0002 V9-06D9V — Admin Duplicate Reviews Audit

**Phase:** V9-06D9-V (read-only)  
**Date:** 2026-07-06

## Finding

Operator report **CONFIRMED**: duplicate **Site Options — Reviews** module still visible under **Настройки сайта** (`fp02-site-settings`).

## Canonical Git state

| Item | Value |
|---|---|
| Group key | `group_fp02_site_options_reviews` |
| Git JSON location | `options_page == fp02-reviews` |
| Runtime theme ACF JSON | Matches Git (`fp02-reviews`) |

Git JSON alone does **not** explain Site Settings duplicate — runtime DB is suspect.

## Duplicate source (most likely)

D9-U checkpoint (`db-checkpoint.json`) lists **two** `acf-field-group` posts with key `group_fp02_site_options_reviews` (count 15 groups, duplicate entry at lines 62–68).

**Mechanism:** D9-R placed the group on `fp02-site-settings`. D9-U relocated canonical JSON to `fp02-reviews` and imported/synced (import ID 274; prior active ID 250 noted in D9-U docs). A stale duplicate post may retain `fp02-site-settings` location while the synced copy targets `fp02-reviews`.

## Not the duplicate source

- `group_fp02_site_options_contacts` / `group_fp02_site_options_modal_cta` — legitimate Site Settings groups
- `group_fp02_page_reviews` — page template location (`page-templates/reviews.php`), not Site Settings
- `shpigovsky-core` OptionsPage — registers `fp02-site-settings` but does not register reviews fields in PHP groups reviewed

## Minimal D9-W repair

1. DB checkpoint.
2. Read-only probe: list all `acf-field-group` posts named `group_fp02_site_options_reviews` with serialized location.
3. Deactivate/trash stale duplicate still on `fp02-site-settings`.
4. Verify Site Settings admin has no reviews module; **Отзывы** retains single group.

**Risk:** LOW with checkpoint. **Git ACF JSON change:** not required if JSON already correct.

## Evidence

`validation/v9-06d9v-reviews-admin-static-layout-reconciliation-audit/admin-duplicate-reviews-audit.json`
