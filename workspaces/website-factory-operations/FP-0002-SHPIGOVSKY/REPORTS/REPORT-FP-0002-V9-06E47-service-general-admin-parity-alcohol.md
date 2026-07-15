# REPORT — FP-0002 V9-06E47 SERVICE GENERAL ADMIN PARITY — ALCOHOL

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | 8341f5690827df2c43d4f552132f9ca56426cfb7 |
| Staged files before | (empty) |
| WIP count only | 799 → ~806 after task files |
| Runtime/source canon detected | YES — FP-0002 `WORDPRESS/` + local `http://shpigovsky.test` |
| Home frozen state untouched | YES |
| Services hub frozen visual untouched | YES |
| Section model untouched/regression-free | YES |
| Commit allowed | NO |
| Result | PASS (HEAD ahead of origin — MetaBOT docs; no commit/push; foreign WIP left untouched) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e47-service-general-admin-parity-alcohol-before-20260715-114038\` |
| DB dump | `mars_wp_fp0002.sql` (~3.20MB; SHA256 `ECF6AD8C30DF41097D5D718D2F1C69E6F6979C6ECF44663D82E40CD53ECC36FF`; `--no-tablespaces`) |
| Theme backup/hash | copied; aggregate md5 `036c32c3d451d538f2d3fa9ac95156da` |
| Plugin backup/hash | copied; aggregate md5 `b2990778e70a95bc2bd897e04850db08` |
| ACF JSON backup/hash | copied; aggregate md5 `448f03d085b3e6cae5748d65186de783` |
| Service ACF export before | layout/hero/section/structured JSON `.BEFORE` copies |
| Base + representative meta exports before | `meta/postmeta-74-314-78-73-before.tsv` |
| Frontend snapshots before | `/`, `/uslugi/`, zavisimosti, alcohol, #314, depression |
| Image/source exports before | `images/alcohol-image-srcs-before.txt` + home image metas |
| Result | PASS |

## 3. Page discovery

| Area | Finding |
|---|---|
| Base page | Лечение алкогольной зависимости |
| Post ID | **74** (confirmed) |
| URL | `http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` |
| Parent/depth | parent `#73` Зависимости; depth 1 |
| Editor role | `service` (Услуга) |
| Effective layout | `service_general` (resolved stack `service-general` / alcohol-stack) |
| Template/render source | `single-service.php` → `alcohol-stack.php` → `alcohol-direct-v9.php` |
| Existing ACF groups | Layout, Hero, Structured Sections, FAQ, Relationships + new **Услуга — блоки страницы**; Раздел group filtered out for role=service |

## 4. Frontend block audit

| Order | Frontend block/class | Template/partial | Current source | Classification | Required admin control | Action |
|---:|---|---|---|---|---|---|
| 1 | services-inner-hero-v2 | inner-hero | Hero ACF | ACF | Hero group | keep |
| 2 | subnav | subnav | template anchors | hardcoded/auto | toggle+notice | toggle |
| 3 | service-leaf-intro-v1 | intro | ACF seeded | ACF | heading+highlight | seeded |
| 4 | service-leaf-bordered-info-v1 | bordered-info | ACF repeater | ACF | repeater | seeded |
| 5 | mid-cta | mid-cta | phone + shared chrome | shared | toggle+notice | toggle |
| 6 | service-leaf-signs-v1 | signs | ACF | ACF | heading/items/editorial | seeded |
| 7 | service-leaf-approach-v1 | alcohol-direct-v9/approach | ACF + team image | ACF | fields+cards+image | seeded |
| 8 | clinic-landscape | home/clinic-landscape | service ACF image | ACF | image+toggle | seeded |
| 9 | services-program-v2 | program | ACF chrome + catalog tiles | ACF + shared | chrome fields | seeded |
| 10 | service-leaf-stages-v1 | alcohol-direct-v9/stages | ACF | ACF | stages+support | seeded |
| 11 | service-leaf-corridor-v1 | corridor | ACF image | ACF | image+toggle | seeded |
| 12 | specialists | alcohol-direct-v9/specialists | specialists children | automatic | toggle+notice | toggle |
| 13 | founder-quote | home/founder-quote | shared template | global | toggle | toggle |
| 14 | comfort | home/comfort | Comfort options | global | toggle | toggle |
| 15 | reviews | home/reviews | reviews source | global | toggle | toggle |
| 16 | service-child-services | child-services | CPT children | automatic | toggle | toggle |
| 17 | faq | alcohol-direct-v9/faq | ACF FAQ | ACF | heading+items | seeded |
| 18 | final-form | final-form | Final Form options | global | toggle | toggle |

## 5. Admin model

| Order | Admin section | Source of truth | Fields/settings | Toggle | Result | Notes |
|---:|---|---|---|---|---|---|
| 1 | Hero | Hero group | pointer notice | — | PASS | shared |
| 2 | Навигация | template anchors | notice | nav_visible | PASS | auto |
| 3 | Intro | page ACF | heading, highlight | intro_visible | PASS | seeded |
| 4 | Bordered info | page ACF | repeater | bordered_visible | PASS | seeded |
| 5 | Mid CTA | shared chrome + phone | notice | mid_cta_visible | PASS | no content fields |
| 6 | Signs | page ACF | heading/intro/items/editorial | signs_visible | PASS | seeded |
| 7 | Approach | page ACF | texts+cards+team image | approach_visible | PASS | seeded |
| 8 | Landscape | page ACF | clinic landscape image | landscape_visible | PASS | not Home |
| 9 | Program | page ACF + catalog | heading/lead/intros | program_visible | PASS | tiles automatic |
| 10 | Stages | page ACF | steps+support | stages_visible | PASS | seeded |
| 11 | Corridor | page ACF | corridor image | corridor_visible | PASS | seeded |
| 12–15 | Specialists/Founder/Comfort/Reviews | shared/auto | notices | toggles | PASS | |
| 16 | Children tiles | CPT children | notice | children_visible | PASS | |
| 17 | FAQ | page ACF | heading+items | faq_visible | PASS | seeded |
| 18 | Final form | shared | notice | final_form_visible | PASS | |

## 6. Template fallback removal / ACF seeding

| Block | Fallback before | ACF field after | Seeded | Remaining fallback | Result | Notes |
|---|---|---|---|---|---|---|
| Intro | PHP alcohol static | `service_general_intro_*` | yes #74 | emergency alcohol only | PASS | |
| Bordered | PHP alcohol static | `service_general_bordered_info_items` | yes | emergency | PASS | |
| Signs | PHP alcohol static | `service_general_signs_*` | yes | emergency | PASS | |
| Approach | PHP alcohol static | `service_general_approach_*` | yes | emergency | PASS | |
| Program chrome | PHP alcohol demo | `service_general_program_*` | yes | emergency | PASS | tiles stay catalog |
| Stages | PHP alcohol static | `service_general_stages_*` | yes | emergency | PASS | |
| FAQ | PHP alcohol static | `service_general_faq_*` | yes | emergency | PASS | |
| Team image | theme asset | `service_general_team_image` | `#1238` | emergency theme | PASS | |
| Landscape | Home helper | `service_general_clinic_landscape_image` | `#1239` | emergency theme | PASS | Home meta untouched |
| Corridor | theme asset | `service_general_corridor_image` | `#1709` | emergency theme | PASS | |

## 7. Repeater conversions

| Block | Before | After repeater | Seeded rows | Frontend preserved | Result | Notes |
|---|---|---|---:|---|---|---|
| Bordered info | PHP array | `service_general_bordered_info_items` | 3 | yes | PASS | |
| Signs list | PHP array | `service_general_signs_items` | 9 | yes | PASS | |
| Approach cards | PHP array | `service_general_approach_cards` | 4 | yes | PASS | |
| Program intros | PHP scalars | `service_general_program_intro_items` | 2 | yes | PASS | |
| Stages | PHP array | `service_general_stages_items` | 4 | yes | PASS | |
| Stages support | PHP array | `service_general_stages_support_items` | 4 | yes | PASS | |
| FAQ | PHP array | `service_general_faq_items` | 10 | yes | PASS | answers via blank-line split |

## 8. Service image fields

| Image block | Before source | New/current field | Seeded image ID | Home/theme dependency removed | Frontend unchanged | Result |
|---|---|---|---:|---|---|---|
| Команда | theme staff-group.webp | `service_general_team_image` | 1238 | YES (ACF primary) | YES (uploads URL) | PASS |
| Территория | Home helper | `service_general_clinic_landscape_image` | 1239 | YES | YES | PASS |
| Коридор | theme corridor.webp | `service_general_corridor_image` | 1709 | YES | YES | PASS |

## 9. Automatic/shared block controls

| Block | Source of truth | Toggle/settings | Default | Source notice | Result | Notes |
|---|---|---|---|---|---|---|
| Subnav | template anchors | `service_general_nav_visible` | ON | yes | PASS | |
| Mid CTA | shared chrome + phone | `service_general_mid_cta_visible` | ON | yes | PASS | |
| Specialists | specialists child pages | `service_general_specialists_visible` | ON (#74); OFF (#314/#78) | yes | PASS | preserve non-alcohol layout |
| Founder/Comfort/Reviews/Final | shared | visible toggles | ON | yes | PASS | |
| Children tiles | CPT children | `service_general_children_visible` | ON | yes | PASS | empty if no children |

## 10. Admin validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Base edit loads | yes | groups resolve via wp bootstrap | PASS |
| Role is Услуга | yes | `service` | PASS |
| Hero visible/populated | yes | Hero group present | PASS |
| Service general group visible | yes | «Услуга — блоки страницы» | PASS |
| Section group hidden | yes | filtered out for #74 | PASS |
| Fields ordered by frontend | yes | notices 1–18 match stack | PASS |
| Demo/current data seeded | yes | intro/signs/FAQ/stages populated | PASS |
| Repeaters visible | yes | 7 repeater fields | PASS |
| No normal template fallback wording | yes | demo + emergency reserve copy | PASS |
| Classic editor hidden | yes | FIX04 helpers remain (`admin-editor.php`) | PASS |
| Save validation | no errors | `update_field` seed OK | PASS |

## 11. Frontend validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Alcohol service HTTP | 200 | 200 | PASS |
| Visual preserved | yes | content markers present; bytes ~119492 vs before ~119498 | PASS |
| ACF-driven content | yes | resolve sources `acf:service_general_*` for images | PASS |
| Images present | yes | uploads staff/landscape/corridor | PASS |
| No broken empty blocks | yes | intro/signs/approach/stages/faq present | PASS |
| No debug/test text | yes | none introduced | PASS |

## 12. Representative service validation

| Page/route | HTTP | Admin compatible | Frontend result | Notes |
|---|---:|---|---|---|
| #314 child-tile service | 200 | yes (role=service) | PASS | landscape/corridor seeded; specialists OFF |
| depression #78 | 200 | yes | PASS | same |
| (other nested) | — | — | SKIPPED | not required beyond #78 |

## 13. Accepted/frozen pages validation

| Page | Expected | Actual | Result |
|---|---|---|---|
| Home `/` | unchanged | HTTP 200; Home landscape meta still `#1239` | PASS |
| Services hub `/uslugi/` | unchanged | HTTP 200 | PASS |
| Section `/uslugi/zavisimosti/` | unchanged | HTTP 200 | PASS |
| Section #77/#84 | unchanged | HTTP 200 on psih/rpp routes | PASS |

## 14. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | |
| alcohol `#74` | 200 | PASS | |
| `#314` | 200 | PASS | |
| depression `#78` | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

## 15. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| ServiceGeneralParity.php | WORDPRESS/plugins/.../ServiceGeneralParity.php | runtime plugin | YES | PASS |
| FieldGroups.php | WORDPRESS/plugins/.../FieldGroups.php | runtime plugin | YES | PASS |
| service-general-helpers.php | WORDPRESS/theme/.../service-general-helpers.php | runtime theme | YES | PASS |
| alcohol-direct-v9.php + approach/stages/faq | WORDPRESS/theme/... | runtime theme | YES | PASS |
| intro/signs/bordered/corridor/program/clinic-landscape | WORDPRESS/theme/... | runtime theme | YES | PASS |
| group_fp02_service_general_parity.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | PASS |
| v9-style.css (operator) | source differs historically | runtime `C858903F…` | runtime preserved | PASS |

## 16. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E47-service-general-admin-parity-alcohol.md | created | PASS | this file |
| SERVICE-GENERAL-ADMIN-PARITY-MODEL-v1.md | created | PASS | |
| PROJECT-STATUS.md | updated | PASS | |
| SOURCE-AUTHORITY.md | updated | PASS | |
| v9-06e47-service-general-*.csv (9 evidence files) | created | PASS | under REPORTS/evidence/ |

## 17. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local service general admin parity task; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only)

| Class | Examples |
|---|---|
| Intended FP-0002 E47 | ServiceGeneralParity.php, FieldGroups.php, service-general-helpers.php, alcohol stack templates, acf-json group, REPORT/DOCS/evidence, PROJECT-STATUS, SOURCE-AUTHORITY |
| Runtime-only | copies under `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` |
| DB changes | 34 ACF field seeds on #74/#314/#78 |
| Media changes | none new (reused #1238/#1239/#1709) |
| Docs/evidence | REPORT + model + evidence CSVs |
| Foreign WIP | MetaBOT, OCP, fp-0002-v7/v8, forge reports — untouched |

## 18. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Unseeded future Услуга pages still hit emergency alcohol helpers only on known alcohol page | low | accepted | seed on rollout / E48 |
| Mid-CTA chrome still partially hardcoded | medium | accepted | optional later content fields |
| Program direction tiles remain catalog fallback | low | accepted | documented automatic |
| Source `v9-style.css` historically drifted from runtime | low | accepted | do not overwrite operator runtime CSS |
| Operator must review admin UX for Olga | medium | open | OPERATOR_REVIEW |

## 19. Final verdict

PASS

V9-06E47 Service general admin parity — Alcohol:
COMPLETE

Backup:
PASS

Frontend block audit:
PASS

Admin parity implementation:
PASS

Template fallback dependency removal:
PASS

Demo/current data seeding:
PASS

Repeater conversions:
PASS

Service image fields:
PASS

Automatic/shared block controls:
PASS

Base service frontend preserved:
PASS

Representative services preserved:
PASS

Section accepted model preserved:
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

## 20. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 21. Final safety statement

Target folder:
X:\AI MARS

V9-06E47 Service general admin parity — Alcohol performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

Section accepted model touched:
NO

DB writes:
34

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
