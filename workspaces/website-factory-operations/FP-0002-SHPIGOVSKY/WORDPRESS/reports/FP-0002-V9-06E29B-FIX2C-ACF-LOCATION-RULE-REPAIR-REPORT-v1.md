# REPORT — FP-0002 V9-06E29B-FIX2C ACF LOCATION RULE REPAIR AND DUPLICATE GROUP CLEANUP

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X |
| Label | AI WS |
| Repository | X:/AI MARS |
| Branch | mars/canonical-post-recovery |
| Local HEAD | e36ce56ed2343ec12d53c603d61cd84cd4fd3ebb |
| Remote HEAD | 876f6a932c5b1054f69afcb3d19d2fe40d8aa8de |
| Ahead / Behind | ahead 8 / behind 5 |
| Staged files | 0 |
| FP-0002 staged files | 0 |
| Foreign WIP | present (unrelated; preserved untouched) |
| Result | PASS |

## 2. Live instance reconfirmation

| Item | Value |
|---|---|
| URL | http://shpigovsky.test |
| Document root | X:/MARS-Localhost/sites/wordpress/projects/shpigovsky |
| ABSPATH | X:/MARS-Localhost/laragon/www/shpigovsky/ |
| DB_NAME | mars_wp_fp0002 |
| Table prefix | fp02_ |
| Active theme | shpigovsky |
| Active plugin path | X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/plugins/shpigovsky-core |
| ACF JSON path | X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/acf-json |
| Matches FIX2 live instance | YES |
| Result | PASS |

## 3. Backup and checkpoint

| Item | Result | Path/notes |
|---|---|---|
| Full DB dump | PASS | `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e29b-fix2c-acf-location-rule-repair-pre-20260710-152257/mars_wp_fp0002.sql` |
| SHA256 | PASS | `d28af9ea322d78faa295b3ab92a74922da880ac8353ab9707a879f920acc5abd` |
| ACF export snapshot | PASS | `.../acf-groups-export.json` |
| Page #11 pre-state | PASS | `.../page-11-pre-state.json` |
| `/o-centre/` HTML pre | PASS | `.../o-centre-html-pre.html` |
| Runtime file snapshot | PASS | `.../runtime-candidate-files/` |
| Manifest committed in-repo | PASS | `validation/v9-06e29b-fix2c-acf-location-rule-repair/full-backup-manifest.json` |

## 4. Pre-fix ACF state

| Item | Before |
|---|---|
| Groups attached to page #11 | 9× `group_fp02_page_institutional` (IDs 150,532,554,621,688,756,787,841,895) |
| Duplicate institutional groups | 9 |
| Hub fields visible by admin evidence | NO — invalid `param: page` field conditional logic hid hub `about_*` fields |
| Child repeaters visible by admin evidence | YES — empty `Content sections` / `Stages` shown on page #11 |
| Runtime JSON state | single stale `group_fp02_page_institutional.json` |
| Result | FAIL (root cause confirmed) |

## 5. Source repair

| Area | Before | After | Result | Notes |
|---|---|---|---|---|
| Group model | 1 mixed `group_fp02_page_institutional` with field conditional logic | `group_fp02_page_ocentre_hub` + `group_fp02_page_institutional_child` | PASS | Location rules only |
| Hub location | `page_template == institutional.php` + broken conditionals | `post_type == page` AND `page == 11` | PASS | |
| Child location | broken `page != 11` conditional | template + pages #12–#16 OR rules | PASS | |
| Field names | `hero_*`, `about_*`, etc. | preserved | PASS | No postmeta migration |
| Legacy group JSON | present | retired/removed | PASS | |

## 6. Duplicate ACF DB group cleanup

| Object | Before | After | Action | Result | Notes |
|---|---|---|---|---|---|
| `group_fp02_page_institutional` | 9 rows | 0 rows | hard delete groups + child fields | PASS | after backup |
| `group_fp02_page_ocentre_hub` | 0 | 1 row (ID 951) | import canonical | PASS | |
| `group_fp02_page_institutional_child` | 0 | 1 row (ID 996) | import canonical | PASS | |

## 7. ACF DB sync/import

| Group | Action | Field count | Attached where | Result | Notes |
|---|---|---:|---|---|---|
| `group_fp02_page_ocentre_hub` | import | 33 top | page #11 | PASS | |
| `group_fp02_page_institutional_child` | import | 4 top | pages #12–#16 | PASS | |
| `group_fp02_page_institutional` | delete all duplicates | — | nowhere | PASS | retired |

## 8. Runtime delivery

| File | Source | Runtime target | Delivered | Hash result |
|---|---|---|---|---|
| FieldGroups.php | WORDPRESS/plugins/.../FieldGroups.php | wp-content/plugins/shpigovsky-core/.../FieldGroups.php | YES | match |
| group_fp02_page_ocentre_hub.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | match |
| group_fp02_page_institutional_child.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | match |
| group_fp02_page_institutional.json | removed | removed at sync | YES | retired |

## 9. Live admin validation

| Admin area/check | Expected | Actual | Result | Evidence |
|---|---|---|---|---|
| Hero visible | visible | visible | PASS | API + HTML labels |
| founder quote visible | visible | visible | PASS | API + HTML labels |
| clinic landscape visible | visible | visible | PASS | API + HTML labels |
| narrative/about visible | visible | visible | PASS | API + HTML labels |
| who-we-treat visible | visible | visible | PASS | API + HTML labels |
| approach visible | visible | visible | PASS | API + HTML labels |
| program visible | visible | visible | PASS | API + HTML labels |
| infrastructure visible | visible | visible | PASS | API + HTML labels |
| shared guidance visible | visible | visible | PASS | label evidence |
| CTA/site phone guidance visible | visible | visible | PASS | label evidence |
| Content sections hidden | hidden | hidden | PASS | not on page #11 group |
| Stages hidden | hidden | hidden | PASS | not on page #11 group |
| Browser screenshot | captured | not captured | PARTIAL | operator recheck required |

Evidence files:
- `validation/v9-06e29b-fix2c-acf-location-rule-repair/live-admin-validation.json`
- `validation/v9-06e29b-fix2c-acf-location-rule-repair/admin-page-11-field-labels.html`

## 10. Frontend parity validation

| Route/section | Result | Notes |
|---|---|---|
| `/o-centre/` HTTP 200 | PASS | |
| hero / founder / clinic / narrative / infrastructure / final form markers | PASS | all present |
| html_length_delta | PASS | 0 |
| PHP fatals | PASS | none |

## 11. Regression route validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/privacy-policy/` | 200 | PASS | |

## 12. Scope preservation

| Object/scope | Before | After | Result | Notes |
|---|---|---|---|---|
| pages #12–#16 postmeta | unchanged | unchanged | PASS | |
| page #11 postmeta content | seeded | unchanged | PASS | 0 content writes |
| menu / services / blog / legal | unchanged | unchanged | PASS | |

## 13. No-scope-drift validation

| Check | Result | Notes |
|---|---|---|
| placeholder pages unchanged | PASS | |
| no menu/permalink/redirect/rewrite changes | PASS | |
| foreign project files untouched | PASS | |

## 14. Evidence

| Evidence | Captured | Result | Notes |
|---|---:|---|---|
| full-backup-manifest.json | 1 | PASS | |
| source-repair-result.json | 1 | PASS | |
| runtime-delivery-result.json | 1 | PASS | |
| duplicate-acf-group-cleanup.json | 1 | PASS | |
| acf-db-sync-result.json | 1 | PASS | |
| live-admin-validation.json | 1 | PARTIAL | no screenshot |
| admin HTML labels | 1 | PASS | |
| frontend/regression JSON | 2 | PASS | |

## 15. Rollback instructions

| Rollback type | Method | Validation | Notes |
|---|---|---|---|
| Full DB | restore pre-fix SQL dump | `/o-centre/` + admin | see `rollback-instructions.json` |
| Runtime files | copy from backup snapshot | hash compare | |
| Source | git checkout FIX2C paths + restore legacy JSON from backup | build safe | |

## 16. Documentation changes

| File | Action | Reason |
|---|---|---|
| reports/FP-0002-V9-06E29B-FIX2C-ACF-LOCATION-RULE-REPAIR-REPORT-v1.md | created | task report |
| architecture/FP-0002-V9-06E29B-FIX2C-*.md | created | FIX2C evidence pack |
| validation/v9-06e29b-fix2c-acf-location-rule-repair/*.json | created | validation contract |
| WORDPRESS/README.md | updated | FIX2C status |
| WORDPRESS/SOURCE-AUTHORITY.md | updated | FIX2C status |
| FP-0002-SHPIGOVSKY/PROJECT-STATUS.md | updated | FIX2C status |

## 17. Git checkpoint

| Item | Value |
|---|---|
| Exact staged files | 0 (commit not executed — operator/git wave separate) |
| Staged list inspected | yes |
| Source files staged | 0 |
| ACF JSON staged | 0 |
| Runtime files staged | 0 |
| DB dumps staged | 0 |
| Backup payload staged | 0 |
| Foreign project files staged | 0 |
| Unrelated FP-0002 WIP staged | 0 |
| Commit | not performed |
| Commit hash | — |
| Push | NO (branch diverged; no force) |
| Local HEAD | e36ce56ed2343ec12d53c603d61cd84cd4fd3ebb |
| Remote HEAD | 876f6a932c5b1054f69afcb3d19d2fe40d8aa8de |
| Result | PASS (no unsafe staging) |

## 18. Final verdict

**PARTIAL PASS**

V9-06E29B-FIX2C ACF Location Rule Repair:
PARTIAL

Backup:
PASS

DB checkpoint:
PASS

Source repair:
PASS

Duplicate ACF cleanup:
PASS

Live admin visibility:
PARTIAL

Frontend parity:
PASS

No foreign project work:
PASS

No-scope-drift:
PASS

Recommended next phase:
CREATE_V9_06E29B_OPERATOR_OCENTRE_ADMIN_RECHECK_TASK

## 19. Recommended next action

CREATE_V9_06E29B_OPERATOR_OCENTRE_ADMIN_RECHECK_TASK

## 20. Final safety statement

Target folder:
X:\AI MARS

V9-06E29B-FIX2C ACF Location Rule Repair performed:
PARTIAL

Backup:
YES

DB checkpoint:
YES

DB writes:
257

Source changes:
3

Runtime delivery:
YES

WordPress changes:
3

Page #11 changed:
NO

Placeholder pages #12-#16 changed:
NO

Menu changes:
0

Redirects:
0

Permalink changes:
NO

Rewrite flush:
NO

Foreign project work:
NO

Git commits:
0

Git push:
NO

FP-0002 files staged:
0

Foreign files staged:
0

Unrelated FP-0002 WIP staged:
0

DB dump committed:
NO

Backup payload committed:
NO

Runtime files committed:
NO

Secrets committed:
0
