# FP-0002 V9-06E29B-FIX — Full Backup

**Generated:** 2026-07-10T13:43:32.301072+07:00

## Backup path

`X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-fix-ocentre-admin-ui-pre-20260710-134255`

## DB dump

- Path: `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-fix-ocentre-admin-ui-pre-20260710-134255/mars_wp_fp0002.sql`
- SHA256: `5d836ecfa89300483a2aed92afcf6ca7f9e8be2df1540d93baeaa2beec9da0a8`
- Database: `mars_wp_fp0002`

## Page #11 pre-state

`X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-fix-ocentre-admin-ui-pre-20260710-134255/page-11-pre-state.json`

## `/o-centre/` HTML snapshot

`X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-fix-ocentre-admin-ui-pre-20260710-134255/o-centre-html-pre.html`

## Restore

{
  "db": "mysql -h127.0.0.1 -uroot mars_wp_fp0002 < \"X:\\MARS-Localhost\\backups\\wordpress\\projects\\shpigovsky\\v9-06e29b-fix-ocentre-admin-ui-pre-20260710-134255\\mars_wp_fp0002.sql\"",
  "page_11_postmeta": "Restore from X:\\MARS-Localhost\\backups\\wordpress\\projects\\shpigovsky\\v9-06e29b-fix-ocentre-admin-ui-pre-20260710-134255\\page-11-pre-state.json",
  "source_files": "git checkout -- exact paths",
  "runtime_files": "Copy from runtime_candidate_snapshot pre hashes"
}

**Result:** PASS
