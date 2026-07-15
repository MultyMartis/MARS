# REPORT — FP-0002 V9-06E45-FIX01 SERVICE LAYOUT MODEL AND CHILD SERVICES

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | `X:` |
| Label | `AI WS` |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `8341f5690827df2c43d4f552132f9ca56426cfb7` |
| Staged files before | empty |
| WIP count only | ~769–777 (foreign + prior FP-0002 dirty tree; not reconciled) |
| Runtime/source canon detected | YES — runtime `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky`; source `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS` |
| Home frozen state untouched | YES (`#1338` not edited; hub CSS scoped away from `/`) |
| Services hub frozen visual untouched | YES (after scoping child CSS to `service` singular; hub norm length matches before) |
| Commit allowed | NO |
| Result | PASS (unpushed commits on branch noted; no git mutation per task) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e45-fix01-service-layout-model-before-20260714-180233\` |
| DB dump | `mars_wp_fp0002.sql` (2 731 441 bytes; SHA256 `35375666F035DE1706DD0B5A2A78A8CD339755FB8A618D68A569CF125636919D`; `--no-tablespaces`) |
| Theme backup/hash | `theme/shpigovsky` + `inventories/theme-sha256.txt` (633 files) |
| Plugin backup/hash | `plugin/shpigovsky-core` + `inventories/plugin-sha256.txt` (23 files) |
| ACF JSON backup/hash | `acf-json/` + `inventories/acf-json-sha256.txt` (10 files) |
| Service ACF group export before | `exports/acf-group-service-layout-hero-before.json` |
| Service inventory before | `inventories/service-inventory-before.csv` (29 services) |
| Frontend snapshots before | `snapshots/*-before.html` + `inventories/route-smoke-before.csv` |
| Result | PASS |

## 3. Operator model implementation

| Decision | Implementation | Result | Notes |
|---|---|---|---|
| Only two editor types | `service_editor_role` choices: section / service | PASS | Placeholder removed from choices |
| Root sections stay subdivision | `#73/#77/#84` role section, layout subdivision | PASS | |
| Service pages use alcohol_special stack | role service → effective `alcohol-special`; technical `alcohol_special` | PASS | Static alcohol copy gated to `#74` |
| Placeholder demoted from main type | Not in editor choices; pages migrated to service | PASS | Legacy technical value remains in advanced select |
| Override retained as advanced | Field kept; alcohol `#74` override turned off | PASS | Warning when override on |

## 4. Layout migration / seeding

| Group | Count | Role writes | Layout writes | Override writes | Result | Notes |
|---|---:|---:|---:|---:|---|---|
| Root sections | 3 | 0 | 0 | 0 | PASS | Already correct |
| Service pages | 7 | 0 | included in 25 | 0 | PASS | Empty→alcohol_special |
| Former placeholders | 16 | included in 18 | included in 25 | 0 | PASS | → service + alcohol_special |
| Alcohol page | 1 | 0 | 0 | 1 | PASS | Override off |
| Mismatch #314/#316 | 2 | 2 | 2 | 0 | PASS | Now service; child block expected |

Totals from seed summary: role_writes **18**, layout_writes **25**, override_writes **1**, child_enabled_writes **26**.

## 5. Effective layout logic

| Case | Expected effective stack | Actual | Result | Notes |
|---|---|---|---|---|
| role section, override off | subdivision | subdivision (`#73/#77/#84`) | PASS | |
| role service, override off | alcohol_special | alcohol-special | PASS | |
| override on | selected technical | (not required after seed) | PASS | Path retained in resolver |
| legacy/empty fallback | safe derived stack | alcohol-special / known roots subdivision | PASS | Children alone ≠ subdivision |

## 6. Admin conditional behavior

| Page | ID | Role | Effective stack | Fields visible | Warning | Result |
|---|---:|---|---|---|---|---|
| Зависимости | 73 | section | subdivision | role+layout+override+category_lead | — | PASS |
| Психическое здоровье | 77 | section | subdivision | same | — | PASS |
| РПП | 84 | section | subdivision | same | — | PASS |
| Alcohol | 74 | service | alcohol-special | +child_services | — | PASS |
| Narcotic dependency | 314 | service | alcohol-special | +child_services | service_with_children_ok | PASS |
| Depression | 78 | service | alcohol-special | +child_services | — | PASS |
| #314 | 314 | service | alcohol-special | +child_services | service_with_children_ok | PASS |
| #316 | 316 | service | alcohol-special | +child_services | service_with_children_ok | PASS |

Editor choices probe: `{"section":"Раздел","service":"Услуга"}` — placeholder choice **NO**.

## 7. Child services tile block

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Block before FAQ | `child-services` partial before FAQ/final-form in alcohol stack | PASS | Narcotic: block present; FAQ empty→hidden |
| Direct child query | `shpigovsky_get_service_children()` | PASS | Published only |
| Hidden if no children | early return | PASS | Alcohol/heroin/depression |
| Cards link to children | card permalinks | PASS | Narcotic 4 children |
| Mini descriptions | `service_short_description` / mini helper | PASS | When available |
| Admin toggle | `service_child_services_enabled` default on | PASS | |
| Admin heading | `service_child_services_heading` + fallback | PASS | «Направления внутри услуги» |
| Responsive styles | `service-child-services.css` | PASS | Scoped to service singular |

## 8. Frontend validation

| Route | Expected stack | HTTP | Child block | Result | Notes |
|---|---|---:|---|---|---|
| `/uslugi/` | services hub | 200 | n/a | PASS | size match after CSS scope |
| Зависимости | subdivision | 200 | n/a | PASS | |
| Психическое здоровье | subdivision | 200 | n/a | PASS | |
| РПП | subdivision | 200 | n/a | PASS | |
| Alcohol | alcohol_special/service | 200 | hidden | PASS | Static title + bordered info preserved |
| Narcotic dependency | alcohol_special/service | 200 | visible | PASS | 4 tiles |
| Heroin dependency | alcohol_special/service | 200 | hidden | PASS | |
| Depression | alcohol_special/service | 200 | hidden | PASS | No alcohol static title |

## 9. Services hub / Home validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| `/uslugi/` visual | unchanged | hub before/after2 length 123592; norm equal | PASS |
| `/` Home frozen | unchanged | 200; child CSS not loaded | PASS |
| Root intro/lead | preserved | subdivision roots unchanged | PASS |
| Services hub sliders | preserved | no hub product edits | PASS |

## 10. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | |
| alcohol URL | 200 | PASS | |
| narcotic URL | 200 | PASS | |
| heroin URL | 200 | PASS | |
| depressiya URL | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

## 11. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| ServiceLayoutGovernance.php | `WORDPRESS/plugins/.../Admin/` | `wp-content/plugins/shpigovsky-core/src/Admin/` | YES | PASS |
| FieldGroups.php | same tree | same | YES | PASS |
| EditorRestrictions.php | same | same | YES | PASS |
| group_fp02_service_layout_hero.json | `WORDPRESS/acf-json/` | `wp-content/acf-json/` | YES | PASS |
| service-helpers.php | theme `inc/` | runtime theme | YES | PASS |
| assets.php | theme `inc/` | runtime theme | YES | PASS |
| alcohol-direct-v9.php | template-parts | runtime | YES | PASS |
| child-services.php | template-parts (new) | runtime | YES | PASS |
| service-child-services.css | assets/css (new) | runtime | YES | PASS |
| intro/signs/bordered/program/inner-hero | template-parts | runtime | YES | PASS |
| v9-style.css | unchanged | matches FIX01 backup | YES | PASS (operator CSS preserved) |

## 12. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E45-FIX01-service-layout-model-and-child-services.md | created | PASS | this file |
| SERVICE-LAYOUT-VARIANT-GOVERNANCE-v1.md | updated | PASS | two-type model |
| PROJECT-STATUS.md | updated | PASS | |
| WORDPRESS/SOURCE-AUTHORITY.md | updated | PASS | FIX01 section |
| v9-06e45-fix01-service-hierarchy-layout-plan.csv | created | PASS | |
| v9-06e45-fix01-service-layout-migration-results.csv | created | PASS | |
| v9-06e45-fix01-child-services-block-validation.csv | created | PASS | |
| v9-06e45-fix01-service-admin-validation.csv | created | PASS | |
| v9-06e45-fix01-service-frontend-validation.csv | created | PASS | |
| v9-06e45-fix01-seed-summary.json | created | PASS | |

## 13. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local service layout model fix; persistence handled separately |
| Push attempted | NO |

### Intended FIX01 paths (not committed)

- Plugin: `ServiceLayoutGovernance.php`, `FieldGroups.php`, `EditorRestrictions.php`
- ACF JSON: `group_fp02_service_layout_hero.json`
- Theme: `service-helpers.php`, `assets.php`, `alcohol-direct-v9.php`, `child-services.php`, `service-child-services.css`, intro/signs/bordered/program/inner-hero
- Docs/evidence/report under FP-0002
- Runtime-only + DB writes under Localhost (expected)

Foreign WIP (~777 status lines) left untouched.

## 14. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Non-alcohol services share alcohol stack section order (clinic/reviews/program fallbacks) but content may be sparse | Medium | Accepted | Content fill / admin parity later |
| Subnav still lists alcohol anchors that may be empty on sparse pages | Low | Open | Soften subnav to existing sections in later task |
| Former placeholder pages now on service stack without full ACF content | Medium | Accepted | Hide-empty already; content wave later |
| Local WIP/unpushed commits not reconciled | Low | Accepted | Per task: no git reconciliation |

## 15. Final verdict

PASS

V9-06E45-FIX01 Service layout model / child services:
COMPLETE

Two-type editor model:
PASS

Subdivision roots:
PASS

General service stack:
PASS

Placeholder demotion:
PASS

Child services tile block:
PASS

Admin conditional behavior:
PASS

Frontend preserved:
PASS

Services hub frozen visual untouched:
PASS

Home frozen state untouched:
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
OPERATOR_REVIEW_REQUIRED

## 16. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 17. Final safety statement

Target folder:
X:\AI MARS

V9-06E45-FIX01 Service layout model / child services performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

DB writes:
70

Source changes:
YES

Runtime delivery:
YES

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
