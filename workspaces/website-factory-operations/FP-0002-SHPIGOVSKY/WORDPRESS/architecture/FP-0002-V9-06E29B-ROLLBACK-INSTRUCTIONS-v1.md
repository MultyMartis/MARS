# FP-0002 V9-06E29B Rollback Instructions

## Full site restore

1. Restore DB: `mysql -h127.0.0.1 -uroot mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e29b-full-site-backup-pre-20260710-035311\mars_wp_fp0002.sql"`
2. Restore runtime files from `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-full-site-backup-pre-20260710-035311/runtime-site`
3. Verify: `/o-centre/` and regression routes

## DB-only restore

Use checkpoint SQL at `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-full-site-backup-pre-20260710-035311/mars_wp_fp0002.sql`

## Page #11 postmeta partial

Restore from `Restore postmeta from X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e29b-full-site-backup-pre-20260710-035311\page-11-pre-state.json`

## Source/runtime rollback

Redeploy pre-E29B theme/plugin hashes from full site backup manifest or git parent commit.

**Verification routes:** /, /blog/, /blog/nazvanie-stati/, /uslugi/, /uslugi/zavisimosti/, /kontakty/, /privacy-policy/, /o-centre/
