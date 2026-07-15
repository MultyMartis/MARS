# REPORT — FP-0002 V9-06E29C EXCEL STRUCTURE COMPLETION, GENERIC PAGES, FAVICON

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | 96a8f08f6dc44ee21a83cd13b4a7032b69587e3e |
| Staged files before | 0 |
| WIP count only | 649 (foreign + FP-0002 mixed) |
| Commit allowed | NO — foreign WIP present; selective commit not authorized in task with mixed tree |
| Result | PASS — volume/branch OK; proceed without git commit |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e29c-structure-completion-pre-20260710T133633Z |
| DB dump | mars_wp_fp0002.sql (2,142,727 bytes) |
| Theme backup/hash | 619 files manifest |
| Plugin backup/hash | 21 files manifest |
| ACF JSON backup/hash | 7 files manifest |
| Route inventory export | pre-mutation-inventory.json, post-mutation-inventory.json |
| Result | PASS |

## 3. Excel structure manifest

| Metric | Value |
|---|---|
| Excel path | X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\02_CONTENT\Предварит структура и спрос.xlsx |
| Sheet | Структура |
| Rows read | 52 |
| URLs found | 45 URL cells |
| Normalized unique routes | 41 (blog demo deduped) |
| Duplicates skipped | 2 (`/blog/nazvanie-stati/` repeated rows 50–51) |
| Ambiguous rows | 2 blank “Название” rows (16–17); legal row 53 excluded from public route set |
| Result | PASS |

## 4. Route reconciliation summary

| Classification | Count |
|---:|---:|
| EXISTS_OK | 18 |
| EXISTS_WRONG_TYPE | 0 |
| EXISTS_WRONG_TEMPLATE | 5 (o-centre children on institutional.php) |
| EXISTS_404 | 14 (pre-task) |
| CREATED_PAGE | 5 |
| CREATED_SERVICE | 9 |
| CREATED_SPECIALIST | 0 |
| UPDATED_TEMPLATE | 5 |
| UPDATED_CONTENT_PLACEHOLDER | 12 |
| DUPLICATE_SKIP | 13 trashed after repair |
| OPERATOR_DECISION_REQUIRED | 0 |

## 5. Created/updated objects

| Route | Action | Object type | ID | Parent | Template/model | Status | Placeholder |
|---|---|---|---:|---:|---|---|---|
| /specyalisty/ | CREATED_PAGE | page | 1030 | 0 | page-templates/generic.php | publish | yes |
| /specyalisty/shipovsky/ | CREATED_PAGE | page | 1031 | 1030 | page-templates/generic.php | publish | yes |
| /specyalisty/kazakov/ | CREATED_PAGE | page | 1032 | 1030 | page-templates/generic.php | publish | yes |
| /specyalisty/kostyuk/ | CREATED_PAGE | page | 1033 | 1030 | page-templates/generic.php | publish | yes |
| /o-centre/intervyu-i-smi/ | CREATED_PAGE | page | 1039 | 11 | page-templates/generic.php | publish | yes |
| /o-centre/o-nas/ | UPDATED_TEMPLATE | page | 12 | 11 | page-templates/generic.php | publish | if empty |
| /o-centre/programma-lecheniya/ | UPDATED_TEMPLATE | page | 13 | 11 | page-templates/generic.php | publish | if empty |
| /o-centre/galereya-o-dome/ | UPDATED_TEMPLATE | page | 14 | 11 | page-templates/generic.php | publish | if empty |
| /o-centre/specialistam/ | UPDATED_TEMPLATE | page | 15 | 11 | page-templates/generic.php | publish | if empty |
| /o-centre/rodstvennikam/ | UPDATED_TEMPLATE | page | 16 | 11 | page-templates/generic.php | publish | if empty |
| /uslugi/genotipirovanie/ | CREATED_SERVICE | service | 1029 | 0 | single-service.php / leaf | publish | yes |
| /uslugi/.../soli/ | CREATED_SERVICE | service | 1011 | 314 | single-service.php / leaf | publish | yes |
| /uslugi/.../matadon/ | CREATED_SERVICE | service | 1012 | 314 | single-service.php / leaf | publish | yes |
| /uslugi/.../geroin/ | CREATED_SERVICE | service | 1013 | 314 | single-service.php / leaf | publish | yes |
| /uslugi/.../lekarstva/ | RENAMED_SERVICE | service | 315 | 314 | single-service.php / leaf | publish | yes |
| /uslugi/.../ludomaniya/ | CREATED_SERVICE | service | 1016 | 316 | single-service.php / leaf | publish | yes |
| /uslugi/.../internet-zavisimost/ | CREATED_SERVICE | service | 1017 | 316 | single-service.php / leaf | publish | yes |
| /uslugi/.../sozavisimost/ | CREATED_SERVICE | service | 1018 | 316 | single-service.php / leaf | publish | yes |
| /uslugi/.../shopogolizm/ | CREATED_SERVICE | service | 1019 | 316 | single-service.php / leaf | publish | yes |
| /uslugi/.../lechenie-narkoticheskoy-zavisimosti/ | RENAMED_SERVICE | service | 314 | 73 | single-service.php / subdivision | publish | existing |
| /uslugi/.../lechenie-povedencheskoy-zavisimosti/ | RENAMED_SERVICE | service | 316 | 73 | single-service.php / subdivision | publish | existing |
| /uslugi/.../emotsionalnoe-vygoranie/ | RENAMED_SERVICE | service | 80 | 77 | single-service.php / leaf | publish | existing |
| /uslugi/.../buliniya/ | RENAMED_SERVICE | service | 86 | 84 | single-service.php / leaf | publish | existing |
| /uslugi/.../ptsr/ | RENAMED_SLUG | service | 79 | 77 | single-service.php / leaf | publish | existing (`ptrs`→`ptsr`) |

## 6. O-Centre child pages

| Route | ID | Before model | After model | Status | Result |
|---|---:|---|---|---|---|
| /o-centre/o-nas/ | 12 | page-templates/institutional.php | page-templates/generic.php | publish | PASS |
| /o-centre/programma-lecheniya/ | 13 | page-templates/institutional.php | page-templates/generic.php | publish | PASS |
| /o-centre/galereya-o-dome/ | 14 | page-templates/institutional.php | page-templates/generic.php | publish | PASS |
| /o-centre/specialistam/ | 15 | page-templates/institutional.php | page-templates/generic.php | publish | PASS |
| /o-centre/rodstvennikam/ | 16 | page-templates/institutional.php | page-templates/generic.php | publish | PASS |
| /o-centre/intervyu-i-smi/ | 1039 | MISSING | page-templates/generic.php | publish | PASS |

## 7. Service pages and deep service routes

| Route | ID | Level/depth | Parent | Template/model | Action | HTTP | Result |
|---|---:|---:|---:|---|---|---:|---|
| /uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/ | 314 | 2 | 73 | subdivision | RENAMED | 200 | PASS |
| /uslugi/.../soli/ | 1011 | 3 | 314 | leaf | CREATED | 200 | PASS |
| /uslugi/.../matadon/ | 1012 | 3 | 314 | leaf | CREATED | 200 | PASS |
| /uslugi/.../geroin/ | 1013 | 3 | 314 | leaf | CREATED | 200 | PASS |
| /uslugi/.../lekarstva/ | 315 | 3 | 314 | leaf | RENAMED/REPARENT | 200 | PASS |
| /uslugi/.../lechenie-povedencheskoy-zavisimosti/ | 316 | 2 | 73 | subdivision | RENAMED | 200 | PASS |
| /uslugi/.../ludomaniya/ | 1016 | 3 | 316 | leaf | CREATED | 200 | PASS |
| /uslugi/.../internet-zavisimost/ | 1017 | 3 | 316 | leaf | CREATED | 200 | PASS |
| /uslugi/.../sozavisimost/ | 1018 | 3 | 316 | leaf | CREATED | 200 | PASS |
| /uslugi/.../shopogolizm/ | 1019 | 3 | 316 | leaf | CREATED | 200 | PASS |
| /uslugi/genotipirovanie/ | 1029 | 1 | 0 | leaf | CREATED | 200 | PASS |

## 8. Specialists / reviews / contacts

| Route | ID | Object type | Template/model | Action | HTTP | Result |
|---|---:|---|---|---|---:|---|
| /specyalisty/ | 1030 | page | generic.php | CREATED | 200 | PASS |
| /specyalisty/shipovsky/ | 1031 | page | generic.php | CREATED | 200 | PASS |
| /specyalisty/kazakov/ | 1032 | page | generic.php | CREATED | 200 | PASS |
| /specyalisty/kostyuk/ | 1033 | page | generic.php | CREATED | 200 | PASS |
| /otzyvy/ | 18 | page | reviews.php | EXISTS_OK | 200 | PASS |
| /kontakty/ | 20 | page | contacts.php | EXISTS_OK | 200 | PASS |

## 9. Favicon

| Area | Implementation | Asset | URL/Path | HTTP | Result |
|---|---|---|---|---:|---|
| Frontend | WP Site Icon (attachment 1040) + theme fallback hooks | apple-touch-icon.png + V9 pack | /wp-content/uploads/... + /wp-content/themes/shpigovsky/assets/favicon/ | 200 | PASS |
| Admin | site_icon + `admin_head` theme fallback | same | same | 200 | PASS |
| Login | site_icon + `login_head` theme fallback | same | same | 200 | PASS |

## 10. Full route validation

All 41 canonical Excel routes after dedupe: **HTTP 200**. Evidence: `WORDPRESS/validation/v9-06e29c-excel-structure-completion/http-validation.json`.

| Route | Expected | Actual HTTP | Object type | Template/model | Result | Notes |
|---|---|---:|---|---|---|---|
| / | 200 | 200 | page | front-page | PASS | |
| /uslugi/ | 200 | 200 | page | services-hub.php | PASS | |
| … (all Excel routes) | 200 | 200 | mixed | per section | PASS | see JSON evidence |
| /uslugi/psihicheskoe-zdorovie/ptsr/ | 200 | 200 | service | leaf | PASS | slug corrected `ptrs`→`ptsr` |

## 11. Regression validation

| Route/check | HTTP | Result | Notes |
|---|---:|---|---|
| / | 200 | PASS | |
| /o-centre/ | 200 | PASS | hub institutional unchanged |
| /blog/ | 200 | PASS | |
| /blog/nazvanie-stati/ | 200 | PASS | |
| /uslugi/zavisimosti/ | 200 | PASS | |
| /uslugi/psihicheskoe-zdorovie/ | 200 | PASS | |
| /uslugi/rasstroystva-pischevogo-povedeniya/ | 200 | PASS | |
| /privacy-policy/ | 200 | PASS | |

## 12. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| page-templates/generic.php | WORDPRESS/theme/shpigovsky/... | wp-content/themes/shpigovsky/... | yes | PASS |
| template-parts/generic/content-page.php | WORDPRESS/theme/shpigovsky/... | wp-content/themes/shpigovsky/... | yes | PASS |
| inc/favicon.php | WORDPRESS/theme/shpigovsky/... | wp-content/themes/shpigovsky/... | yes | PASS |
| functions.php | WORDPRESS/theme/shpigovsky/... | wp-content/themes/shpigovsky/... | yes | PASS |
| inc/admin-editor.php | WORDPRESS/theme/shpigovsky/... | wp-content/themes/shpigovsky/... | yes | PASS |
| ServicePermalinks.php | WORDPRESS/plugins/shpigovsky-core/... | wp-content/plugins/shpigovsky-core/... | yes | PASS |
| RepeaterValidation.php | WORDPRESS/plugins/shpigovsky-core/... | wp-content/plugins/shpigovsky-core/... | yes | PASS |
| assets/favicon/* | WORDPRESS/theme/shpigovsky/assets/favicon/ | wp-content/themes/shpigovsky/assets/favicon/ | yes | PASS |

## 13. Git result

| Item | Value |
|---|---|
| Git staged before | 0 |
| Git staged after | 0 |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | COMMIT SKIPPED DUE FOREIGN WIP (649 unrelated/stale entries in working tree) |
| Push attempted | NO |

## 14. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Depth-3 service URLs exceed prior V9-06C depth-2 contract | medium | mitigated | ServicePermalinks depth-3 rewrite + request resolver added; operator contract update later |
| 13 duplicate service rows trashed during repair | low | closed | Trash slugs renamed; no permanent delete |
| `profilakticheskiy-analiz` (ID 75) not in Excel | low | accepted | kept per operator non-deletion policy |
| Institutional child ACF groups still target old template IDs | low | open | migrate ACF locations to generic.php in follow-up if operators need child ACF on generic pages |

## 15. Final verdict

PASS

V9-06E29C Excel Structure Completion:
COMPLETE

Excel route reconciliation:
PASS

Missing pages:
PASS

Generic page shells:
PASS

Deep service routes:
PASS

Favicon:
PASS

Regression:
PASS

Source/runtime sync:
PASS

Git commit:
SKIPPED

No foreign project work:
PASS

Recommended next phase:
CREATE_V9_06E29_FINAL_WORDPRESS_READINESS_GATE_TASK

## 16. Recommended next action

CREATE_V9_06E29_FINAL_WORDPRESS_READINESS_GATE_TASK

## 17. Final safety statement

Target folder:
X:\AI MARS

V9-06E29C Excel Structure Completion performed:
YES

Excel file read:
YES

DB writes:
47

Source changes:
YES

Runtime delivery:
YES

WordPress changes:
YES

Favicon implemented:
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

FP-0002 product contaminated:
NO

WPilot confused with OCPilot:
NO

Secrets committed:
0
