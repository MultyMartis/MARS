# REPORT — FP-0002 V9-07A01 Production Upload Pack

**Date:** 2026-07-23  
**Status:** PASS (package prepared; **not** uploaded)  
**Production connection:** none  
**Commit / push / freeze:** none

---

## 1. Pack location

| Item | Path |
|------|------|
| Folder | `X:\AI MARS STORAGE\deployment-packs\fp-0002\v9-07a01-production-upload-20260723-222232\` |
| Optional ZIP | `X:\AI MARS STORAGE\deployment-packs\fp-0002\v9-07a01-production-upload-20260723-222232.zip` |
| Product files | 14 |
| Product bytes | 346 547 (~339 KB) |
| ZIP size | ~75 KB (includes manifests) |

---

## 2. Diff authority

`REPORTS/DEPLOY/V9-07A01-PRODUCTION-FILE-DIFF.csv`  
Compared Stable v1 freeze canonical `WORDPRESS/` vs current canonical source for V9-07A01 product files only.

Mode: **exact changed files only** (not full theme/plugin).

Fancybox vendor (`assets/vendor/fancybox/*`) already identical in Stable v1 → **excluded** from pack.

---

## 3. Exact upload files

1. `wp-content/themes/shpigovsky/inc/fancybox-vendors.php` (CREATE)
2. `wp-content/themes/shpigovsky/functions.php`
3. `wp-content/themes/shpigovsky/inc/program-direction-helpers.php`
4. `wp-content/themes/shpigovsky/inc/institutional-helpers.php`
5. `wp-content/themes/shpigovsky/inc/service-helpers.php`
6. `wp-content/themes/shpigovsky/inc/institutional-about-v9-content.php`
7. `wp-content/themes/shpigovsky/inc/services-hub-vendors.php`
8. `wp-content/themes/shpigovsky/inc/service-subdivision-vendors.php`
9. `wp-content/themes/shpigovsky/inc/alcohol-direct-v9-vendors.php`
10. `wp-content/themes/shpigovsky/assets/js/v9-shell.js`
11. `wp-content/themes/shpigovsky/template-parts/service/program.php`
12. `wp-content/themes/shpigovsky/template-parts/service/approach.php`
13. `wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php`
14. `wp-content/acf-json/group_fp02_page_ocentre_hub.json`

Hashes: pack `FILE-HASHES-SHA256.csv` == canonical source.

---

## 4. Pack contents

- `files/` (server-relative tree)
- `UPLOAD-MANIFEST.md`
- `UPLOAD-ALLOWLIST.txt`
- `DESTINATION-MAP.csv`
- `FILE-HASHES-SHA256.csv`
- `PRE-UPLOAD-CHECKLIST.md`
- `POST-UPLOAD-SMOKE.md`
- `ROLLBACK.md`
- `CONTENT-AND-DB-ACTIONS.md`
- `PACKAGE-OK.txt`
- copy of production file diff CSV

Validation: no secrets, no backups, no `.bak`, no `node_modules`, no absolute Windows paths in deployable tree, dependencies complete, source/runtime parity still PASS after cleanup.

---

## 5. Content vs code

Code pack alone enables live Program auto-source + Comfort Fancybox enqueue.  
Renamed page title/slug/mini-description require Scenario A verify or Scenario B manual admin edit — see pack `CONTENT-AND-DB-ACTIONS.md`.

---

## 6. Operator next step

1. Production backup  
2. Choose Scenario A/B  
3. Upload allowlisted files in manifest order  
4. Cache clear (conditional)  
5. Smoke checklist  
6. Optional old-URL 301 (separate authorization)

**Do not** treat this report as proof of production deployment.
