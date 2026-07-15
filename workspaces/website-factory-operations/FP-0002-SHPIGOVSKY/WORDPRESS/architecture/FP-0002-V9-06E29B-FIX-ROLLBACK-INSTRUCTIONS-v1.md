# FP-0002 V9-06E29B-FIX — Rollback Instructions

**Generated:** 2026-07-10T13:43:32.312532+07:00

## Full DB restore

```text
mysql -h127.0.0.1 -uroot mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e29b-fix-ocentre-admin-ui-pre-20260710-134255\mars_wp_fp0002.sql"
```

## Page #11 postmeta

Restore from X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e29b-fix-ocentre-admin-ui-pre-20260710-134255\page-11-pre-state.json

## Source rollback

```text
git checkout -- plugins/shpigovsky-core/src/Fields/FieldGroups.php acf-json/group_fp02_page_institutional.json
```

## Runtime rollback

Restore from X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-fix-ocentre-admin-ui-pre-20260710-134255/runtime-candidate-files

## Verify after rollback

/, /blog/, /uslugi/zavisimosti/, /privacy-policy/, /o-centre/

**Result:** PASS
