# REPORT — FP-0002 V9-06E31 PROGRAM PAGES, DIRECTION LINKS, SERVICE ADMIN VALIDATION RELAX

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | abfd6d1c844ce4ebbf15e714b010d3bf9fbbee23 |
| Staged files before | 0 |
| WIP count only | ~661 (foreign monorepo WIP ignored; MetaBOT unpushed commits present) |
| Runtime CSS canon detected | YES — runtime `v9-style.css` hash matched source at preflight (`3072104A…`); additive link styles only |
| Commit allowed | NO — REMOTE/HEAD mismatch (`origin` @ ba9743a8) + unpushed MetaBOT commits + large foreign WIP |
| Result | PASS — proceed with Localhost backup + bounded FP-0002 work |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e31-program-pages-links-validation-before-20260712-223200\` |
| DB dump | `mars_wp_fp0002.sql` (1 405 067 bytes) — PASS (tablespaces warning only; dump usable) |
| Theme backup/hash | `theme-shpigovsky.sha256.txt` (626 files) |
| Plugin backup/hash | `plugin-shpigovsky-core.sha256.txt` (21 files) |
| ACF JSON backup/hash | `acf-json-wp-content.sha256.txt` + `acf-json-root.sha256.txt` + copied trees |
| Service/page inventory export | `service-page-inventory-before.json` (44 services + program parent #13) |
| Result | PASS |

## 3. Pre-implementation audit

| Area | Finding |
|---|---|
| Canonical internet service | `#1017` `internet-zavisimost` publish, parent `#316` (behavioral), URL `/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/internet-zavisimost/`, slider=`0`, text_list=`1` |
| Duplicate internet service | `#1046` `lechenie-internet-zavisimosti` publish, parent `#73`, slider=`1`, text_list=`0` (E30 gallery card) |
| Genotyping service | `#1029` `genotipirovanie` publish top-level, URL `/uslugi/genotipirovanie/`, text_list=`1` |
| Program parent page | `#13` `/o-centre/programma-lecheniya/` template `page-templates/generic.php` |
| Existing program child pages | none before task |
| Home directions source file | `theme/.../template-parts/home/rehabilitation-program.php` |
| Service program grid source file | `template-parts/service/program.php` + `services-hub/rehabilitation-program.php` + `institutional/about-program.php` |
| Service admin validation source | ACF group `group_fp02_service_structured_sections` (live already `required=0`/`min=0`); `RepeaterValidation::is_within_max_rows` rejected empty non-array POST values; programme already had optional filter |

## 4. Service cleanup / move

| Item | Action | ID | Old URL | New/canonical URL | Status | Result |
|---|---|---:|---|---|---|---|
| Internet canonical | SLIDER_ON + TEXT_LIST_OFF | 1017 | `/uslugi/.../internet-zavisimost/` | same | publish | OK |
| Internet duplicate | TRASH (not permanent delete) | 1046 | `/uslugi/zavisimosti/lechenie-internet-zavisimosti/` | canonical 1017 | trash | OK |
| Genotyping service | TRASH (not permanent delete) | 1029 | `/uslugi/genotipirovanie/` | program page | trash | OK |
| 301 redirects | NOT ADDED | — | — | — | — | Documented: trashed routes 404 |

## 5. Program pages

| Page title | Action | ID | Parent ID | Template | URL | Placeholder | Result |
|---|---|---:|---:|---|---|---|---|
| Генотипирование | CREATED | 1053 | 13 | page-templates/generic.php | `/o-centre/programma-lecheniya/genotipirovanie/` | yes | OK |
| Нейропсихологическая коррекция | CREATED | 1054 | 13 | page-templates/generic.php | `/o-centre/programma-lecheniya/neyropsihologicheskaya-korrektsiya/` | yes | OK |
| Психокоррекция | CREATED | 1055 | 13 | page-templates/generic.php | `/o-centre/programma-lecheniya/psihokorrektsiya/` | yes | OK |
| Кинезиотерапия | CREATED | 1056 | 13 | page-templates/generic.php | `/o-centre/programma-lecheniya/kinezioterapiya/` | yes | OK |

## 6. Direction links implementation

| Area | File | Links added | Подробнее link | Result | Notes |
|---|---|---|---|---|---|
| Home directions | `template-parts/home/rehabilitation-program.php` + `inc/program-direction-helpers.php` | title + image → program URLs | YES (`Подробнее >`) | PASS | data-driven via helper map |
| Service program grid | `template-parts/service/program.php`, `services-hub/rehabilitation-program.php`, `institutional/about-program.php`, `inc/service-helpers.php`, `inc/institutional-helpers.php` | title + image links | NO (Home-only per charter) | PASS | shared helper URLs |
| Slider asset map | `inc/services-hub-helpers.php` | canonical `internet-zavisimost` asset key | n/a | PASS | removed duplicate slug key |
| CSS additive | `assets/css/v9-style.css` | link/more styles | yes | PASS | additive only; no wipe |

## 7. Service admin validation relax

| Field/section | Previous behavior | New behavior | Source file/field | Result |
|---|---|---|---|---|
| Признаки / симптомы (`signs_items`) | Live ACF already `min=0`/`required=0`; empty non-array could fail max-row helper; label may be read as «Причины» | Explicit optional instructions; `acf/validate_value` always allow; empty non-array treated as 0 rows | `FieldGroups.php`, `RepeaterValidation.php`, ACF JSON | PASS |
| Пункты программы (`programme_items`) | Already optional (E24A) | Kept optional + empty non-array fix | same | PASS |
| Этапы (`stages`) | Same as signs | Explicit optional + allow-empty filter | same | PASS |

## 8. Route validation

| Route | Expected | HTTP | Final URL | Result | Notes |
|---|---|---:|---|---|---|
| `/o-centre/programma-lecheniya/` | 200 | 200 | same | PASS | |
| `/o-centre/programma-lecheniya/genotipirovanie/` | 200 | 200 | same | PASS | |
| `/o-centre/programma-lecheniya/neyropsihologicheskaya-korrektsiya/` | 200 | 200 | same | PASS | |
| `/o-centre/programma-lecheniya/psihokorrektsiya/` | 200 | 200 | same | PASS | |
| `/o-centre/programma-lecheniya/kinezioterapiya/` | 200 | 200 | same | PASS | |
| `/uslugi/.../internet-zavisimost/` | 200 | 200 | same | PASS | canonical |
| `/uslugi/zavisimosti/lechenie-internet-zavisimosti/` | 404 | 404 | same | PASS | trashed; no 301 |
| `/uslugi/genotipirovanie/` | 404 | 404 | same | PASS | trashed |
| `/` | 200 | 200 | same | PASS | |
| `/uslugi/` | 200 | 200 | same | PASS | |
| `/uslugi/zavisimosti/` | 200 | 200 | same | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | 200 | same | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | 200 | same | PASS | |
| `/o-centre/` | 200 | 200 | same | PASS | |
| `/blog/` | 200 | 200 | same | PASS | |
| `/kontakty/` | 200 | 200 | same | PASS | |

## 9. `/uslugi/` validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Genotyping removed from services catalog | yes | category block absent; markers `01,02,03` | PASS |
| Category marker sequence | sequential | `01,02,03` | PASS |
| Internet canonical route used | `internet-zavisimost` | present in HTML | PASS |
| Duplicate internet route removed | yes | absent from HTML; route 404 | PASS |
| Slider cards link correctly | yes | canonical internet + computer + opium | PASS |
| Service names clickable | yes | child menu present | PASS |
| Child menus still work | yes | `HAS_CHILD_MENU=YES` | PASS |

## 10. Home/service program block validation

| Page | Block | Items | Title links | Image links | Подробнее links | Result |
|---|---|---:|---|---|---|---|
| `/` | `.home-rehabilitation-program__directions` | 4 | 4 | 4 | 4 | PASS |
| `/uslugi/` | `.services-program-v2__grid` | 4 | 4 | 4 | n/a | PASS |
| `/uslugi/zavisimosti/` | `.services-program-v2__grid` | 4 | 4 | 4 | n/a | PASS |
| `/uslugi/psihicheskoe-zdorovie/` | `.services-program-v2__grid` | 4 | 4 | 4 | n/a | PASS |

## 11. Admin save validation evidence

| Test target | Method | Result | Notes |
|---|---|---|---|
| Draft service `#1073` (trashed after) | empty `signs_items` / `programme_items` / `stages` + `acf_validate_value([])` + `is_within_max_rows('', …)` + `wp_update_post` | PASS | Evidence: `validation/.../e31-mutation-result.json` → `admin_evidence` |

## 12. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| Core route set (section 8) | 200/404 as expected | PASS | no PHP fatal observed |
| UTF-8 page titles | OK | PASS | titles verified via PHP UTF-8 probe |
| Operator CSS | preserved + additive | PASS | preflight hash match; additive link CSS only |

## 13. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| program-direction-helpers.php | `WORDPRESS/theme/shpigovsky/inc/` | `wp-content/themes/shpigovsky/inc/` | yes | PASS |
| rehabilitation-program.php (home) | theme template-parts | runtime theme | yes | PASS |
| rehabilitation-program.php (hub) | theme template-parts | runtime theme | yes | PASS |
| program.php (service) | theme template-parts | runtime theme | yes | PASS |
| about-program.php | theme template-parts | runtime theme | yes | PASS |
| service-helpers.php | theme inc | runtime | yes | PASS |
| services-hub-helpers.php | theme inc | runtime | yes | PASS |
| institutional-helpers.php | theme inc | runtime | yes | PASS |
| functions.php | theme | runtime | yes | PASS |
| v9-style.css | theme assets | runtime | yes | PASS |
| FieldGroups.php | plugin | runtime | yes | PASS |
| RepeaterValidation.php | plugin | runtime | yes | PASS |
| group_fp02_service_structured_sections.json | `WORDPRESS/acf-json/` | `wp-content/acf-json/` + ACF import | yes | PASS |

## 14. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | — |
| Commit skipped reason | REMOTE/HEAD mismatch + unpushed MetaBOT commits + large foreign WIP; charter forbids unsafe commit |
| Push attempted | NO |

### Git classification (post-task)

| Class | Paths |
|---|---|
| Intended FP-0002 source | `theme/.../program-direction-helpers.php` (new); home/hub/service/about program templates; `service-helpers.php`; `services-hub-helpers.php`; `institutional-helpers.php`; `functions.php`; `v9-style.css` (additive); `FieldGroups.php`; `RepeaterValidation.php`; `acf-json/group_fp02_service_structured_sections.json`; `REPORTS/REPORT-FP-0002-V9-06E31-...md`; `validation/v9-06e31-.../` |
| Runtime-only | Localhost theme/plugin/acf delivery (synced hashes) |
| DB changes | trash 1046/1029; slider flags on 1017; pages 1053–1056; ACF import; temp draft 1073 trashed |
| Foreign / prior WIP | MetaBOT docs/commits; E30/other dirty FP-0002 files (`PROJECT-STATUS.md`, `SOURCE-AUTHORITY.md`, hero ACF, `ServicePermalinks.php`, unrelated templates/reports, INCOMING, etc.) — **not touched** |
| Status docs | **not updated** — already dirty unrelated WIP |

## 15. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| No 301 from trashed duplicate/geno routes | Low | Accepted | Optional later redirect wave if SEO needs it |
| Operator may still see stale admin browser cache for ACF | Low | Mitigated | Hard refresh / re-open service edit; ACF re-imported |
| Temporary draft `#1073` in trash | Info | Contained | Already trashed; empty trash optional later |
| Unsafe git commit environment | Medium | Mitigated | Commit skipped; create persistence task later |

## 16. Final verdict

PASS

V9-06E31 Program Pages / Direction Links / Admin Validation:
COMPLETE

Internet duplicate cleanup:
PASS

Genotyping move:
PASS

Program pages:
PASS

Home direction links:
PASS

Service program links:
PASS

Service admin validation:
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
CREATE_OPERATOR_REVIEW_CHECKLIST

## 17. Recommended next action

CREATE_OPERATOR_REVIEW_CHECKLIST

## 18. Final safety statement

Target folder:
X:\AI MARS

V9-06E31 Program Pages / Direction Links / Admin Validation performed:
YES

DB writes:
28

Source changes:
YES

Runtime delivery:
YES

WordPress changes:
YES

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
