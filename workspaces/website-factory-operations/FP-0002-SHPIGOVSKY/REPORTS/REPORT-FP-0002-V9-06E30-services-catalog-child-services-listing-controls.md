# REPORT — FP-0002 V9-06E30 SERVICES CATALOG CHILD SERVICES AND DISPLAY CONTROLS

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | abfd6d1c844ce4ebbf15e714b010d3bf9fbbee23 (at close; preflight started at bc8e63fb) |
| Staged files before | 0 |
| WIP count only | ~654–660 (foreign monorepo WIP ignored) |
| Runtime CSS canon detected | YES — runtime `v9-style.css` differed from source before task; preserved |
| Commit allowed | NO — unpushed MetaBOT commits + REMOTE/HEAD mismatch + foreign WIP |
| Result | PASS — proceed with Localhost backup + bounded FP-0002 work |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e30-services-catalog-before-20260712-213642\` |
| DB dump | `mars_wp_fp0002.sql` (1 389 922 bytes) — PASS |
| Theme backup/hash | `theme-shpigovsky.sha256.txt` (626 files) |
| Plugin backup/hash | `plugin-shpigovsky-core.sha256.txt` (21 files) |
| ACF JSON backup/hash | `acf-json.sha256.txt` (7 files) |
| Service inventory export | `service-inventory-before.txt` + after + seed JSON copies |
| Result | PASS |

## 3. Pre-implementation audit

| Area | Finding |
|---|---|
| Service CPT hierarchy | Top parents: `zavisimosti` (73), `psihicheskoe-zdorovie` (77), `rasstroystva-pischevogo-povedeniya` (84), `genotipirovanie` (1029). Narcotic children under 314. Existing `internet-zavisimost` (1017) under behavioral — kept; separate from new gallery service. |
| `/uslugi/` template/render file | `page-templates/services-hub.php` → `service-groups.php` → `service-group.php` + `inc/services-hub-helpers.php` |
| Marker numbering source | Was hardcoded slug→01..04 map; genotyping had marker 04 while `menu_order=0` put it first |
| Gallery/card source | Hardcoded static image+caption map in helpers (not CPT links) |
| Existing display meta/ACF | No text-list/slider flags; `service_short_description` existed in `group_fp02_service_layout_hero` |
| Source/runtime differences | PHP hub files matched; **CSS diverged** (operator runtime edits) |
| Operator CSS preservation plan | Patch runtime CSS only for new classes; sync runtime→source after |

## 4. Service objects created/updated

| Service title | Action | ID | Parent ID | Slug | Final URL | Text list | Slider | Demo content source | Result |
|---|---|---:|---:|---|---|---|---|---|---|
| Лечение интернет зависимости | CREATED | 1046 | 73 | lechenie-internet-zavisimosti | /uslugi/zavisimosti/lechenie-internet-zavisimosti/ | no | yes | placeholder leaf under zavisimosti | OK |
| Компьютерная зависимость | CREATED | 1047 | 73 | kompyuternaya-zavisimost | /uslugi/zavisimosti/kompyuternaya-zavisimost/ | no | yes | placeholder leaf under zavisimosti | OK |
| Лечение опиумной зависимости | CREATED | 1048 | 73 | lechenie-opiumnoy-zavisimosti | /uslugi/zavisimosti/lechenie-opiumnoy-zavisimosti/ | no | yes | placeholder leaf under zavisimosti | OK |
| Хроническая усталость | CREATED | 1049 | 77 | hronicheskaya-ustalost | /uslugi/psihicheskoe-zdorovie/hronicheskaya-ustalost/ | no | yes | placeholder leaf under mental health | OK |
| Стресс | CREATED | 1050 | 77 | stress | /uslugi/psihicheskoe-zdorovie/stress/ | no | yes | placeholder leaf under mental health | OK |
| Нарциссизм | CREATED | 1051 | 77 | nartsissizm | /uslugi/psihicheskoe-zdorovie/nartsissizm/ | no | yes | placeholder leaf under mental health | OK |
| Генотипирование | REORDERED | 1029 | 0 | genotipirovanie | /uslugi/genotipirovanie/ | yes (parent card) | no | existing | menu_order 0→200 |

Decision: gallery-card services = slider yes / text list no (matches prior visual model). Existing published non-slider services seeded text list yes / slider no. Existing `internet-zavisimost` under behavioral left intact (different slug/title/path).

## 5. Admin display controls

| Field/control | Storage | Default | Applied to | Result | Notes |
|---|---|---|---|---|---|
| `service_show_in_text_list` | ACF true/false + postmeta | true | all published services | PASS | label «Показывать в текстовом списке» |
| `service_show_in_slider` | ACF true/false + postmeta | false | all published services | PASS | label «Показывать в слайдере» |
| `service_slider_image` | ACF image | empty | available | PASS | optional; slug→theme asset fallback used for 6 cards |

Source: `FieldGroups.php` + `acf-json/group_fp02_service_layout_hero.json` (runtime synced).

## 6. `/uslugi/` render changes

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Genotyping last | `menu_order=200` on ID 1029; parents ordered by menu_order | PASS | |
| Automatic marker numbering | `shpigovsky_format_services_hub_group_marker($index)` after sort | PASS | 01–04 match render order |
| Service name links | `.services-category-section-v2__service-name-link` → permalink | PASS | style preserved via inherit CSS |
| Child inline menu | auto children of each listed service under text | PASS | narcotic + behavioral children present |
| Slider/gallery cards as service links | gallery built from `show_in_slider` services; whole card linked | PASS | 6 gallery links |
| Text list / slider options | filter children by meta flags | PASS | |

## 7. Route validation

| Route | HTTP | Object ID | Template/model | Result | Notes |
|---|---:|---|---|---|---|
| / | 200 | — | home | PASS | |
| /uslugi/ | 200 | page hub | services-hub | PASS | |
| /uslugi/zavisimosti/ | 200 | 73 | service | PASS | |
| /uslugi/psihicheskoe-zdorovie/ | 200 | 77 | service | PASS | |
| /uslugi/rasstroystva-pischevogo-povedeniya/ | 200 | 84 | service | PASS | |
| /uslugi/genotipirovanie/ | 200 | 1029 | service | PASS | |
| /uslugi/zavisimosti/lechenie-internet-zavisimosti/ | 200 | 1046 | service | PASS | new |
| /uslugi/zavisimosti/kompyuternaya-zavisimost/ | 200 | 1047 | service | PASS | new |
| /uslugi/zavisimosti/lechenie-opiumnoy-zavisimosti/ | 200 | 1048 | service | PASS | new |
| /uslugi/psihicheskoe-zdorovie/hronicheskaya-ustalost/ | 200 | 1049 | service | PASS | new |
| /uslugi/psihicheskoe-zdorovie/stress/ | 200 | 1050 | service | PASS | new |
| /uslugi/psihicheskoe-zdorovie/nartsissizm/ | 200 | 1051 | service | PASS | new |
| /uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/ | 200 | 314 | service | PASS | |
| /uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/geroin/ | 200 | 1013 | service | PASS | |
| /uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/matadon/ | 200 | 1012 | service | PASS | |
| /uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/soli/ | 200 | 1011 | service | PASS | |
| /uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/lekarstva/ | 200 | 315 | service | PASS | |
| /o-centre/ | 200 | — | institutional | PASS | |
| /blog/ | 200 | — | blog | PASS | |
| /kontakty/ | 200 | — | contacts | PASS | |

No PHP fatals observed.

## 8. `/uslugi/` visual/DOM validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Category order | Genotyping bottom | addictions → mental → eating → genotyping | PASS |
| Marker sequence | 01, 02, 03, 04 | 01, 02, 03, 04 | PASS |
| Child services under parent | present | `__service-children` + geroin link | PASS |
| Gallery cards clickable | yes | 6 `__gallery-link` | PASS |
| Service names clickable | yes | 14 `__service-name-link` | PASS |
| Current visual style preserved | yes | operator CSS kept; additive E30 rules only | PASS |

## 9. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| / | 200 | PASS | |
| /uslugi/ | 200 | PASS | |
| /uslugi/zavisimosti/ | 200 | PASS | |
| /uslugi/psihicheskoe-zdorovie/ | 200 | PASS | |
| /uslugi/rasstroystva-pischevogo-povedeniya/ | 200 | PASS | |
| /uslugi/genotipirovanie/ | 200 | PASS | |
| /o-centre/ | 200 | PASS | |
| /blog/ | 200 | PASS | |
| /kontakty/ | 200 | PASS | |

## 10. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| services-hub-helpers.php | WORDPRESS/theme/.../inc/ | wp-content/themes/.../inc/ | YES | PASS |
| service-card.php | WORDPRESS/theme/.../components/ | runtime same | YES | PASS |
| service-group.php | WORDPRESS/theme/.../services-hub/ | runtime same | YES | PASS |
| v9-style.css | WORDPRESS/theme/.../assets/css/ | runtime same | YES | PASS — runtime→source (operator canon) |
| FieldGroups.php | WORDPRESS/plugins/shpigovsky-core/... | runtime same | YES | PASS |
| group_fp02_service_layout_hero.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | PASS |

## 11. Git result

| Item | Value |
|---|---|
| Staged before | 0 |
| Staged after | 0 |
| Commit attempted | NO |
| Commit hash | — |
| Commit skipped reason | COMMIT SKIPPED DUE UNPUSHED FOREIGN COMMITS (MetaBOT) + REMOTE/HEAD MISMATCH + foreign monorepo WIP; exact FP-0002 files remain unstaged for operator-controlled commit wave |
| Push attempted | NO |

### Git classification (end of task)

- **Intended FP-0002 changes:** theme helpers/templates, `v9-style.css` (runtime canon sync), FieldGroups, ACF JSON, PROJECT-STATUS, SOURCE-AUTHORITY, E30 validation helpers/evidence, this report.
- **Runtime-only:** DB posts/meta (Localhost); backup under `X:\MARS-Localhost\backups\...` (not git).
- **DB changes:** 6 service creates + genotyping reorder + display meta seed across published services.
- **Foreign WIP:** MetaBOT docs commits ahead of origin; `.recovery-temp/`; other non-E30 FP-0002 dirty files — ignored.

## 12. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Dual internet-related services (`internet-zavisimost` vs `lechenie-internet-zavisimosti`) | Low | Accepted | Operator decide merge/redirect later |
| ACF JSON vs local PHP registration drift until admin sync | Low | Mitigated | Local FieldGroups registers on `acf/init` |
| CSS sync brought operator edits into git source | Info | Intended | Do not overwrite runtime with older source |
| Uncommitted E30 source on branch with MetaBOT ahead | Medium | Open | Operator selective commit after MetaBOT reconcile |

## 13. Final verdict

PASS

V9-06E30 Services Catalog:
COMPLETE

New service pages:
PASS

Admin display controls:
PASS

/uslugi/ render logic:
PASS

Child inline menus:
PASS

Slider service cards:
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

## 14. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 15. Final safety statement

Target folder:
X:\AI MARS

V9-06E30 Services Catalog performed:
YES

DB writes:
~40+ (6 creates + 1 reorder + display-flag seed across published services + ACF refs)

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
