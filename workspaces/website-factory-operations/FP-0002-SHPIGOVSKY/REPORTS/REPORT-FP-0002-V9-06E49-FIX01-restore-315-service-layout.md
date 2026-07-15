# REPORT — FP-0002 V9-06E49-FIX01 RESTORE #315 SERVICE LAYOUT

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | `X:` |
| Label | `AI WS` |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `8341f5690827df2c43d4f552132f9ca56426cfb7` |
| Staged files before | empty |
| WIP count only | ~836–837 short-status lines (foreign + FP-0002 product WIP) |
| Runtime/source canon detected | YES — runtime `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky`; source `workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS` |
| E49 freeze blocker #315 | CONFIRMED (`placeholder`/`placeholder`; FE ~55KB + `placeholder-stack`; ACF content present) |
| Home frozen state untouched | YES |
| Services hub frozen visual untouched | YES |
| Sections preserved | YES |
| Services preserved except #315 layout fix | YES |
| Commit allowed | NO |
| Result | PASS (remote/HEAD diverge + unpushed foreign commits noted; commit/push skipped per charter) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e49-fix01-restore-315-service-layout-before-20260716-023509\` |
| DB dump | `db/mars_wp_fp0002.sql` (~5.99 MB); SHA256 `19F22823B3D642ED…F3FDD3` |
| Theme backup/hash | `theme/shpigovsky\` — 638 files; tree SHA256 `9031E38F…9A76D4` |
| Plugin backup/hash | `plugin/shpigovsky-core\` — 25 files; tree SHA256 `1692B76F…025A55` |
| ACF JSON backup/hash | `acf-json\` — 14 files; tree SHA256 `01C1EE4E…75B968` |
| Postmeta exports before | `#315/#78/#74/#314/#81/#85/#73/#77/#84` under `postmeta/` + `post_content/` + layout-summary + `#315` content fingerprint |
| Frontend snapshots before | 11 routes under `frontend/before-*.html` (incl. `#315` ~55KB placeholder) |
| Result | PASS |

## 3. #315 layout fix

| Item | Before | After | Result | Notes |
|---|---|---|---|---|
| service_editor_role | placeholder | service | PASS | real wp-admin form POST |
| service_layout_variant | placeholder | service_general | PASS | ACF sync on role save |
| Frontend stack | placeholder-stack (~55KB) | full service (~113KB) | PASS | no `placeholder-stack` |
| Content fields | preserved | preserved | PASS | +4 empty ACF refs only (allowed) |

Path used: `wp-admin-form-post` (authenticated cookie + full form + `_acf_nonce` + `acf[field_fp02_service_editor_role]=service`); HTTP 302 `message=1`. Fallback to `update_field` not required.

## 4. #315 content preservation

| Check | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| service_general fields | preserved | prior content keys intact | PASS | see evidence CSV |
| hero fields | preserved | match | PASS | |
| images/repeaters | preserved | heuristic count match | PASS | |
| post status/url/seo | unchanged | publish / `lekarstva` / same permalink | PASS | |
| Allowed ACF refs | may appear | +`service_category_section_lead` / +`service_child_services_heading` (empty) + `_` refs | PASS | admin save side-effect; not content deletion |

CSV: `REPORTS/evidence/v9-06e49-fix01-315-content-preservation.csv`.

## 5. Control validation

| Page/Route | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| #78 | Услуга | service/service_general; FE no ph | PASS | |
| #74 | full service | service/service_general; 200 | PASS | |
| #314 | full service + child tiles | service/service_general; child_tiles=yes | PASS | |
| #81/#85 | full service | service/service_general; 200 | PASS | |
| #73/#77/#84 | full sections | section/subdivision; 200 | PASS | |
| Home `/` | unchanged | 200 | PASS | HTTP/smoke; freeze untouched |
| Services hub `/uslugi/` | unchanged | 200 | PASS | HTTP/smoke; freeze untouched |

## 6. Freeze blocker recheck

| Check | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| Unintended placeholders among individual services | 0 | 0 | PASS | |
| #315 state | service/service_general | service/service_general | PASS | FE ph=no |
| All individual services | service/service_general | 26/26 PASS | PASS | sections excluded as section/subdivision |

CSV: `REPORTS/evidence/v9-06e49-fix01-freeze-blocker-recheck.csv` (29/29 PASS).

## 7. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | |
| #315 | 200 | PASS | full service |
| #78 | 200 | PASS | Услуга |
| #74 | 200 | PASS | |
| #314 | 200 | PASS | |
| #81 | 200 | PASS | |
| #85 | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

CSV: `REPORTS/evidence/v9-06e49-fix01-route-smoke.csv` (15/15 PASS; no fatal markers).

## 8. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result | Notes |
|---|---|---|---|---|---|
| ServiceLayoutGovernance.php | WORDPRESS/plugins/.../ServiceLayoutGovernance.php | plugins/.../ServiceLayoutGovernance.php | YES | PASS | unchanged this FIX |
| v9-style.css | WORDPRESS/theme(...)/v9-style.css | themes/.../v9-style.css | NO (prior drift) | PASS | runtime vs FIX01 backup MATCH `11A45ABE…` |
| group_fp02_service_layout_hero.json | WORDPRESS/acf-json/... | acf-json/... | YES | PASS | unchanged |

CSV: `REPORTS/evidence/v9-06e49-fix01-source-runtime-sync.csv`.

## 9. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E49-FIX01-restore-315-service-layout.md | created | PASS | this file |
| PROJECT-STATUS.md | updated | PASS | current phase FIX01 |
| SOURCE-AUTHORITY.md | updated | PASS | FIX01 entry + freeze note |
| evidence CSVs | created | PASS | content/admin/frontend/blocker/smoke/sync + restore-trace |

Validation helpers (local only, not product runtime delivery):

- `WORDPRESS/validation/v9-06e49-fix01-restore-315/_e49_fix01_backup_exports.php`
- `WORDPRESS/validation/v9-06e49-fix01-restore-315/_e49_fix01_restore_315_admin.php`
- `WORDPRESS/validation/v9-06e49-fix01-restore-315/_e49_fix01_validate.php`
- `WORDPRESS/validation/v9-06e49-fix01-restore-315/_e49_fix01_fix_evidence.php`

## 10. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local #315 service layout restore; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only `git status --short`)

| Class | Items |
|---|---|
| Intended FP-0002 E49-FIX01 report/evidence/docs | REPORT FIX01 + evidence `v9-06e49-fix01-*` + validation scripts + PROJECT-STATUS / SOURCE-AUTHORITY updates |
| #315 DB layout state change | runtime DB only (not git) |
| Existing uncommitted product (E46–E51) | prior FP-0002 REPORTS/WORDPRESS/DOCS/theme/plugin WIP |
| Foreign WIP | MetaBOT / other workspace noise (~837 lines total); not touched |

## 11. Final verdict

PASS

V9-06E49-FIX01 Restore #315 service layout:
COMPLETE

Backup:
PASS

#315 restored to service:
PASS

#315 content preserved:
PASS

Freeze blocker resolved:
PASS

Controls preserved:
PASS

Home preserved:
PASS

Services hub preserved:
PASS

Sections preserved:
PASS

Regression:
PASS

Source/runtime sync:
PASS

Operator CSS preserved:
PASS

Git commit:
SKIPPED

No foreign project work:
PASS

Recommended next phase:
CREATE_V9_06E49_FULL_SERVICE_ROLLOUT_FREEZE_TASK

## 12. Recommended next action

CREATE_V9_06E49_FULL_SERVICE_ROLLOUT_FREEZE_TASK

## 13. Final safety statement

Target folder:
X:\AI MARS

V9-06E49-FIX01 Restore #315 service layout performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

Section pages touched:
NO

Service pages touched:
YES_ONLY_#315_LAYOUT_RESTORE

#315 final state:
УСЛУГА

DB writes:
2

Source changes:
YES

Runtime delivery:
NO

WordPress changes:
YES

Media Library changes:
NO

Backup created:
YES

Git mutation:
NO

Git commit:
NO

Git push:
NO

Reset:
NO

Rebase:
NO

Stash:
NO

Cleanup:
NO

Foreign project work:
NO

Operator runtime CSS preserved:
YES

FP-0002 product contaminated:
NO

WPilot confused with OCPilot:
NO

Secrets committed:
0
