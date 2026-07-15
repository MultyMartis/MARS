# REPORT — FP-0002 V9-06E32 HOME SERVICES ACCORDION, HOME GALLERY SERVICE LINKS, SERVICE PLACEHOLDER

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | dc3c17736c235f6b4c81f6ac6acecdea5a8a5f68 |
| Staged files before | (empty) |
| WIP count only | 671+ (foreign monorepo WIP present; MetaBOT commits ahead of origin) |
| Runtime CSS canon detected | YES — source/runtime `v9-style.css` MATCH before edits; additive CSS only |
| Commit allowed | NO — remote/HEAD mismatch + foreign WIP |
| Result | PASS (proceed with local bounded writes; commit skipped) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e32-home-services-gallery-before-20260713-003442` |
| DB dump | `mars_wp_fp0002.sql` (2 078 584 bytes) |
| Theme backup/hash | theme-shpigovsky / `51efee9dbf92daec` (627 files) |
| Plugin backup/hash | plugin-shpigovsky-core / `079ccfe4a5db02e4` (21 files) |
| ACF JSON backup/hash | acf-json / `6358b25ba5b1b080` |
| Home/service inventory export | `inventory-before.json`, `home-route-snapshot.html`, `uslugi-route-snapshot.html` |
| Result | PASS |

## 3. Pre-implementation audit

| Area | Finding |
|---|---|
| Home accordion source | `template-parts/home/treatment-prevention.php` had **hardcoded** static HTML; unused helper `shpigovsky_get_home_service_accordion_groups()` already existed in `inc/home-helpers.php` |
| Home accordion ACF/admin fields | Broken/unused repeater `home_service_nav_items` (`field_fp02_home_service_nav_items`) on `group_fp02_page_home` — not driving render |
| Service tree model | 3 roots (Зависимости #73, Психическое здоровье #77, РПП #84); depth-1 children; depth-2 under narcotic/behavioral hubs |
| Home gallery source | `template-parts/home/gallery.php` + ACF `home_gallery_media` / static fallbacks — photo gallery, not service links |
| Home gallery eligibility rule | **Conservative:** publish + depth===1 (parent is root hub) + `service_show_on_home_gallery` true (default true when unset). Roots and depth≥2 excluded |
| Existing service image fields | `service_slider_image`, featured image, `hero_media`, theme slug fallbacks (E30) |
| Placeholder asset plan | New SVG `assets/images/service-placeholder.svg` + central helper `shpigovsky_get_service_image_or_placeholder()` |
| Source/runtime differences | Preflight MATCH on key theme files (incl. CSS); no stale CSS overwrite risk |

## 4. Home accordion automation

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Static HTML removed/replaced | Rewrote `treatment-prevention.php` to render from CPT helper | PASS | |
| Service tree output | Roots = accordion groups; depth-1 = links | PASS | 3 groups / 18 primary + nested children |
| Child/subservice links | Nested `<ul class="...__service-list--children">` for depth-2 | PASS | e.g. under narcotic/behavioral |
| Current classes preserved | Same accordion/item/toggle/panel/service classes | PASS | Additive nested class only |
| Broken ACF admin block removed/hidden | Removed from FieldGroups + ACF JSON; trashed 12 DB `acf-field` posts | PASS | `acf_get_field(...nav...)` now null |

## 5. Home gallery service slider

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Slides from service CPT | `shpigovsky_get_home_gallery_service_slides()` | PASS | 18 slides |
| Service links | `<a class="home-gallery__link">` wrapping image+caption | PASS | Swiper intact |
| Admin hide/show flag | `service_show_on_home_gallery` | PASS | Separate from `/uslugi/` slider flag |
| Default eligibility applied | depth-1 → true; others → false seeded | PASS | 18 true / 11 false among publish |
| Placeholder fallback | Used when no slider/featured/hero/theme fallback | PASS | 12/18 slides use placeholder |
| Visual classes preserved | `.home-gallery` / slide / image / caption / pagination | PASS | aria-label updated to «Услуги центра» |

## 6. Service admin controls

| Field/control | Storage | Default | Applied to | Result | Notes |
|---|---|---|---|---|---|
| `service_show_on_home_gallery` / «Показывать в слайдере на главной» | ACF true/false + postmeta | 1 (true) for depth-1 eligible | all published services seeded | PASS | key `field_fp02_service_show_on_home_gallery` |
| `service_show_in_slider` (E30) | unchanged | false | `/uslugi/` cards | PASS | instructions clarify separation |
| `service_show_in_text_list` (E30) | unchanged | true | `/uslugi/` text list | PASS | |

## 7. Home gallery included services

| ID | Title | URL | Parent | Depth | Flag | Image source | HTTP | Result |
|---:|---|---|---:|---:|---|---|---:|---|
| 74 | Лечение алкогольной зависимости | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | 73 | 1 | 1 | hero_media | 200 | PASS |
| 314 | Лечение наркотической зависимости | /uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/ | 73 | 1 | 1 | placeholder | 200 | PASS |
| 316 | Поведенческие зависимости | /uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/ | 73 | 1 | 1 | placeholder | 200 | PASS |
| 75 | Профилактический анализ | /uslugi/zavisimosti/profilakticheskiy-analiz/ | 73 | 1 | 1 | placeholder | 200 | PASS |
| 1047 | Компьютерная зависимость | /uslugi/zavisimosti/kompyuternaya-zavisimost/ | 73 | 1 | 1 | theme_slug_fallback | 200 | PASS |
| 1048 | Лечение опиумной зависимости | /uslugi/zavisimosti/lechenie-opiumnoy-zavisimosti/ | 73 | 1 | 1 | theme_slug_fallback | 200 | PASS |
| 78 | Депрессия | /uslugi/psihicheskoe-zdorovie/depressiya/ | 77 | 1 | 1 | placeholder | 200 | PASS |
| 79 | ПТСР | /uslugi/psihicheskoe-zdorovie/ptsr/ | 77 | 1 | 1 | placeholder | 200 | PASS |
| 80 | Эмоциональное выгорание | /uslugi/psihicheskoe-zdorovie/emotsionalnoe-vygoranie/ | 77 | 1 | 1 | placeholder | 200 | PASS |
| 81 | Тревожные расстройства | /uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/ | 77 | 1 | 1 | placeholder | 200 | PASS |
| 82 | Расстройства сна | /uslugi/psihicheskoe-zdorovie/rasstroystva-sna/ | 77 | 1 | 1 | placeholder | 200 | PASS |
| 83 | Травма | /uslugi/psihicheskoe-zdorovie/travma/ | 77 | 1 | 1 | placeholder | 200 | PASS |
| 1049 | Хроническая усталость | /uslugi/psihicheskoe-zdorovie/hronicheskaya-ustalost/ | 77 | 1 | 1 | theme_slug_fallback | 200 | PASS |
| 1050 | Стресс | /uslugi/psihicheskoe-zdorovie/stress/ | 77 | 1 | 1 | theme_slug_fallback | 200 | PASS |
| 1051 | Нарциссизм | /uslugi/psihicheskoe-zdorovie/nartsissizm/ | 77 | 1 | 1 | theme_slug_fallback | 200 | PASS |
| 85 | Анорексия | /uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/ | 84 | 1 | 1 | placeholder | 200 | PASS |
| 86 | Булимия | /uslugi/rasstroystva-pischevogo-povedeniya/buliniya/ | 84 | 1 | 1 | placeholder | 200 | PASS |
| 87 | Компульсивное переедание | /uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/ | 84 | 1 | 1 | placeholder | 200 | PASS |

## 8. Placeholder image

| Asset | Source path | Runtime path | URL | HTTP | Result | Notes |
|---|---|---|---|---:|---|---|
| service-placeholder.svg | `WORDPRESS/theme/shpigovsky/assets/images/service-placeholder.svg` | `wp-content/themes/shpigovsky/assets/images/service-placeholder.svg` | `/wp-content/themes/shpigovsky/assets/images/service-placeholder.svg` | 200 | PASS | Neutral grid + «Фото скоро будет»; no external deps |

## 9. Home validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Home HTTP | 200 | 200 | PASS |
| Accordion uses service tree | yes | CPT groups/links present; static «Специалистам» not in accordion | PASS |
| Accordion links 200 | yes | 25/25 sampled 200 | PASS |
| Home gallery service slides | yes | 18 `home-gallery__link` slides | PASS |
| Gallery links 200 | yes | 18/18 | PASS |
| Placeholder used where needed | yes | present in Home HTML; 12 slides | PASS |
| Broken ACF admin block gone | yes | field gone after DB trash | PASS |
| Visual style preserved | yes | classes retained; additive CSS only | PASS |

## 10. Admin validation

| Area | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| Home admin | no broken accordion fields | `home_service_nav_items` removed | PASS | Unrelated Home fields retained |
| Service admin | home gallery flag visible | ACF field registered | PASS | label «Показывать в слайдере на главной» |
| Service admin validation | E31 relaxed save remains OK | FieldGroups/validation not tightened | PASS | No E31 regression changes |

## 11. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| / | 200 | PASS | no fatal |
| /uslugi/ | 200 | PASS | no fatal |
| /uslugi/zavisimosti/ | 200 | PASS | |
| /uslugi/psihicheskoe-zdorovie/ | 200 | PASS | |
| /uslugi/rasstroystva-pischevogo-povedeniya/ | 200 | PASS | |
| /o-centre/ | 200 | PASS | |
| /o-centre/programma-lecheniya/ | 200 | PASS | |
| /blog/ | 200 | PASS | |
| /kontakty/ | 200 | PASS | |

## 12. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| home-helpers.php | WORDPRESS/theme/.../inc/home-helpers.php | themes/shpigovsky/inc/ | YES | PASS |
| service-helpers.php | .../inc/service-helpers.php | themes/shpigovsky/inc/ | YES | PASS |
| services-hub-helpers.php | .../inc/services-hub-helpers.php | themes/shpigovsky/inc/ | YES | PASS |
| treatment-prevention.php | .../home/treatment-prevention.php | themes/.../home/ | YES | PASS |
| gallery.php | .../home/gallery.php | themes/.../home/ | YES | PASS |
| v9-style.css | .../assets/css/v9-style.css | themes/.../css/ | YES | PASS |
| service-placeholder.svg | .../assets/images/service-placeholder.svg | themes/.../images/ | YES | PASS |
| FieldGroups.php | plugins/shpigovsky-core/.../FieldGroups.php | plugins/.../ | YES | PASS |
| RepeaterValidation.php | plugins/.../RepeaterValidation.php | plugins/.../ | YES | PASS |
| group_fp02_service_layout_hero.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | PASS |
| group_fp02_page_home.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | PASS |

## 13. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | — |
| Commit skipped reason | Remote/HEAD mismatch (HEAD ahead with MetaBOT docs) + large foreign WIP; task forbids unsafe commit |
| Push attempted | NO |

## 14. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Duplicate DB `Page — Home` ACF groups (114/483/581/639) | Medium | Open (pre-existing) | Operator ACF cleanup wave; only nav fields trashed here |
| Home gallery shows many placeholder slides until real images uploaded | Low | Accepted | Operator can upload `service_slider_image` / featured |
| Depth rule excludes depth-2 leaves from Home gallery | Low | By design | Expand eligibility only with operator charter |
| Git persistence of E32 source not committed | Medium | Open | `CREATE_V9_06E29C_E32_COMMIT_PERSISTENCE_TASK` after WIP quarantine |

## 15. Final verdict

PASS

V9-06E32 Home Services Accordion / Gallery:
COMPLETE

Home accordion automation:
PASS

Home gallery service links:
PASS

Service admin controls:
PASS

Placeholder image:
PASS

Home admin cleanup:
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

V9-06E32 Home Services Accordion / Gallery performed:
YES

DB writes:
41

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
