# FP-0002 V9-06E29B Full Site Backup

**Task:** V9-06E29B O-Centre Admin Parity Implementation  
**Generated:** 2026-07-10T03:53:18.347300+07:00

## Backup path

`X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-full-site-backup-pre-20260710-035311`

## Contents

| Item | Result |
|---|---|
| DB dump | `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-full-site-backup-pre-20260710-035311/mars_wp_fp0002.sql` SHA256 `478e95a8b4694ff9…` |
| Runtime filesystem | `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-full-site-backup-pre-20260710-035311/runtime-site` (6857 files) |
| Page #11 pre-state | `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-full-site-backup-pre-20260710-035311/page-11-pre-state.json` |
| `/o-centre/` HTML pre | `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-full-site-backup-pre-20260710-035311/o-centre-html-pre.html` |

## Restore

- **DB only:** `mysql -h127.0.0.1 -uroot mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e29b-full-site-backup-pre-20260710-035311\mars_wp_fp0002.sql"`
- **Runtime only:** operator-approved copy from backup runtime folder
- **Full:** DB restore then runtime copy
- **Page #11 partial:** restore postmeta from page-11-pre-state.json

**Result:** PASS
