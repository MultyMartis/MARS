# FP-0002 V9-06E29B-FIX2C Rollback Instructions

1. Restore DB: `mysql -h127.0.0.1 -uroot mars_wp_fp0002 < "X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-fix2c-acf-location-rule-repair-pre-20260710-152257/mars_wp_fp0002.sql"`
2. Restore runtime files from `.../runtime-candidate-files/`
3. Restore source: revert `FieldGroups.php`; restore `group_fp02_page_institutional.json` from backup; remove hub/child JSON
4. Validate `/o-centre/` and page #11 admin

JSON manifest: `validation/v9-06e29b-fix2c-acf-location-rule-repair/rollback-instructions.json`
