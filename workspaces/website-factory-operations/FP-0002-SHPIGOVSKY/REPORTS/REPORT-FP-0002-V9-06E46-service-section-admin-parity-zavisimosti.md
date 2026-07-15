# REPORT — FP-0002 V9-06E46 SERVICE SECTION ADMIN PARITY — ЗАВИСИМОСТИ

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | 8341f5690827df2c43d4f552132f9ca56426cfb7 |
| Staged files before | (empty) |
| WIP count only | ~785 (foreign WIP present; not touched) |
| Runtime/source canon detected | YES — FP-0002 WORDPRESS + local shpigovsky runtime |
| Home frozen state untouched | YES |
| Services hub frozen visual untouched | YES |
| Commit allowed | NO |
| Result | PASS |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e46-service-section-admin-parity-zavisimosti-before-20260714-210729\` |
| DB dump | `db\mars_wp_fp0002.sql` (~4.3 MB; tablespace warning only) |
| Theme backup/hash | `theme\shpigovsky` + `inventories\theme-sha256.txt` |
| Plugin backup/hash | `plugin\shpigovsky-core` + `inventories\plugin-sha256.txt` |
| ACF JSON backup/hash | `acf-json\` + `inventories\acf-json-sha256.txt` |
| Service section exports before | postmeta inventories for #73/#77/#84 + hierarchy CSV |
| Frontend snapshots before | home, uslugi, zavisimosti, psihicheskoe-zdorovie, rasstroystva |
| Admin inventory before | `inventories\admin-zavisimosti-before.json` |
| Service hierarchy inventory before | `inventories\service-hierarchy-before.csv` |
| Result | PASS |

## 3. Page discovery

| Area | Finding |
|---|---|
| Base page | Зависимости |
| Post ID | 73 |
| URL | http://shpigovsky.test/uslugi/zavisimosti/ |
| Editor role | section (Раздел) |
| Effective layout | subdivision |
| Template/render source | `single-service.php` → `subdivision-stack.php` |
| Existing ACF groups | layout_hero, structured_sections, faq, relationships (+ new section_parity) |
| Current hardcoded sources | nature.php, team-stats.php, program intros, stages chrome, dependencies heading/footer |

## 4. Frontend block audit

| Order | Frontend block/class | Template/partial | Current source | Classification | Required admin control | Action |
|---:|---|---|---|---|---|---|
| 1 | `.services-inner-hero-v2` | inner-hero | ACF hero fields | direct (existing) | pointer notice | keep |
| 2 | subnav / breadcrumbs | subnav | automatic + helper labels | automatic | toggle | toggle |
| 3 | `#service-subdivision-dependencies` | children | child CPT + ACF chrome | automatic + direct | toggle + heading/lead/footer | ACF |
| 4 | `#service-subdivision-nature` | nature | ACF (was hardcoded) | direct | full fields | ACF |
| 5 | mid CTA | mid-cta | structured CTA + site phone | direct/site | toggle | toggle |
| 6 | `#service-subdivision-program` | program | ACF intros + programme_items | direct + repeated | fields + toggle | ACF |
| 7 | stages | stages | stages repeater + ACF chrome | direct + repeated | fields + toggle | ACF |
| 8 | `#service-subdivision-approach` | team-stats | ACF (was hardcoded) | direct | full fields | ACF |
| 9 | clinic-landscape | home/clinic-landscape | Home image | shared | toggle + notice | toggle |
| 10 | specialists | home/specialists | specialists pages | automatic | toggle + notice | toggle |
| 11 | founder-quote | home/founder-quote | static shared | shared static | toggle + notice | toggle |
| 12 | comfort | home/comfort | Comfort options | shared | toggle + notice | toggle |
| 13 | reviews | home/reviews | reviews options | shared | toggle + notice | toggle + gate fix |
| 14 | FAQ | faq | faq_items + heading | repeated | heading + toggle | ACF |
| 15 | final-form | final-form | Final Form options | shared | toggle + notice | toggle |

Evidence: `REPORTS/evidence/v9-06e46-service-section-zavisimosti-frontend-block-audit.csv`

## 5. Admin model

| Order | Admin section | Source of truth | Fields/settings | Toggle | Result | Notes |
|---:|---|---|---|---|---|---|
| 1 | Hero | layout_hero group | existing hero_* | — | PASS | notice pointer |
| 2 | Nav | template anchors | — | section_nav_visible | PASS | |
| 3 | Dependencies | child services CPT | heading/lead/footer | section_dependencies_visible | PASS | seeded #73 |
| 4 | Nature | this page ACF | heading/lead/subsections/cards | section_nature_visible | PASS | seeded #73 |
| 5 | Mid CTA | structured CTA | cta_* | section_mid_cta_visible | PASS | |
| 6 | Program | this page + programme_items | heading/intros/labels | section_program_visible | PASS | seeded #73 |
| 7 | Stages | stages repeater + chrome | heading/lead/support | section_stages_visible | PASS | seeded #73 |
| 8 | Approach | this page ACF + media | heading/texts/images/cards | section_approach_visible | PASS | seeded #73 |
| 9 | Clinic | Home ACF | — | section_clinic_landscape_visible | PASS | shared |
| 10 | Specialists | specialists pages | — | section_specialists_visible | PASS | shared |
| 11 | Founder | static template | — | section_founder_quote_visible | PASS | shared static |
| 12 | Comfort | Comfort options | — | section_comfort_visible | PASS | shared |
| 13 | Reviews | reviews options | — | section_reviews_visible | PASS | shared |
| 14 | FAQ | faq_items | section_faq_heading | section_faq_visible | PASS | |
| 15 | Final form | Final Form options | — | section_final_form_visible | PASS | shared |

## 6. Hardcoded HTML/text migration

| Block | Source before | ACF field(s) after | Seeded | Render method | Result | Notes |
|---|---|---|---|---|---|---|
| Nature | nature.php hardcoded | section_nature_* | YES #73 | ACF → fallback | PASS | |
| Approach | team-stats.php hardcoded | section_approach_* | YES #73 | ACF → fallback | PASS | images Media Library capable |
| Dependencies chrome | helpers + children.php | section_dependencies_* | YES #73 | ACF → fallback | PASS | list still from children |
| Program intros | program.php hardcoded | section_program_* | YES #73 | ACF → fallback | PASS | cards still programme_items/assets |
| Stages chrome | stages.php hardcoded | section_stages_* | YES #73 | ACF → fallback | PASS | stages repeater unchanged |
| FAQ heading | faq.php hardcoded | section_faq_heading | YES #73 | ACF → fallback | PASS | |
| Founder copy | founder-quote.php | toggle only | N/A | shared static | PASS by design | not duplicated |

## 7. Repeated/automatic block controls

| Block | Source of truth | Toggle/settings | Default | Source notice/link | Result | Notes |
|---|---|---|---|---|---|---|
| Child services list | child CPT / manual_related | section_dependencies_visible + chrome fields | ON | yes (CPT admin link) | PASS | |
| Program cards | programme_items + direction assets | section_program_visible | ON | yes | PASS | |
| Stages list | stages repeater | section_stages_visible | ON | yes | PASS | |
| Specialists | /specyalisty/ children | section_specialists_visible | ON | yes | PASS | |
| Comfort | Comfort options | section_comfort_visible | ON | yes | PASS | |
| Reviews | site reviews | section_reviews_visible | ON | yes | PASS | home toggle no longer leaks |
| Clinic | Home image | section_clinic_landscape_visible | ON | yes | PASS | |
| Final form | Final Form options | section_final_form_visible | ON | yes | PASS | |
| Founder | static template | section_founder_quote_visible | ON | yes | PASS | |

## 8. ACF fields added/updated

| Field | Type | Section | Seeded value preview | i18n-ready | Result | Notes |
|---|---|---|---|---|---|---|
| group_fp02_service_section_parity | group | Раздел | 63 fields | YES | PASS | new group |
| section_*_visible (14) | true_false | all blocks | 1 on #73/#77/#84 | YES | PASS | |
| section_nature_* | text/textarea/repeater | Nature | Зависимости lorem stack | YES | PASS | #73 |
| section_approach_* | text/textarea/image/repeater | Approach | seeded #73 | YES | PASS | |
| section_dependencies_* | text/textarea | Dependencies | seeded #73 | YES | PASS | |
| section_program_* | text/textarea | Program | seeded #73 | YES | PASS | |
| section_stages_* | text/textarea/repeater | Stages | seeded #73 | YES | PASS | |
| section_faq_heading | text | FAQ | Нас часто спрашивают | YES | PASS | |

Evidence: `REPORTS/evidence/v9-06e46-service-section-acf-fields-added.csv`

## 9. Admin validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Edit screen loads | yes | group registered for post 73 | PASS |
| Role remains Раздел | yes | section | PASS |
| Admin order = frontend order | yes | numbered 1–15 | PASS |
| New fields visible | yes | 63 fields when role=section | PASS |
| Values seeded | yes | #73 content; #77/#84 toggles | PASS |
| Toggles/settings visible | yes | 14 toggles | PASS |
| Notices clear | yes | RU + danger source pattern | PASS |
| Save validation | no errors | repeater limits added | PASS |

## 10. Frontend validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| `/uslugi/zavisimosti/` HTTP | 200 | 200 | PASS |
| Visual preserved | yes | stack markers present | PASS |
| Direct fields render from ACF | yes | seeded values render | PASS |
| Hardcoded HTML reduced | yes/where implemented | nature/approach/program/stages/deps/faq | PASS |
| Repeated blocks work | yes | children/specialists/etc. | PASS |
| Toggles restored enabled | yes | nature OFF→ON verified | PASS |
| No broken media | yes | corridor/staff/assets | PASS |
| No debug/test text | yes | none | PASS |

## 11. Other section pages validation

| Route | HTTP | Layout stack | Result | Notes |
|---|---:|---|---|---|
| `/uslugi/psihicheskoe-zdorovie/` | 200 | subdivision | PASS | content via fallbacks; toggles ON |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | subdivision | PASS | same |

## 12. Frozen pages validation

| Page | Expected | Actual | Result |
|---|---|---|---|
| Home `/` | unchanged | HTTP 200; home ACF fields still 74; len delta ~41 B | PASS |
| Services hub `/uslugi/` | unchanged | HTTP 200; len delta ~-2 B | PASS |

## 13. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | |
| `#314` narcotic service URL | 200 | PASS | `/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/` |
| `#74` alcohol URL | 200 | PASS | |
| depression URL | 200 | PASS | `/uslugi/psihicheskoe-zdorovie/depressiya/` |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

## 14. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| ServiceSectionParity.php | WORDPRESS/plugins/.../Fields/ | wp-content/plugins/.../Fields/ | YES | PASS |
| FieldGroups.php | WORDPRESS/plugins/.../Fields/ | runtime | YES | PASS |
| RepeaterValidation.php | WORDPRESS/plugins/.../Fields/ | runtime | YES | PASS |
| service-section-helpers.php | WORDPRESS/theme/shpigovsky/inc/ | runtime | YES | PASS |
| subdivision-stack.php | theme template-parts | runtime | YES | PASS |
| nature/children/team-stats/stages/program/faq | theme | runtime | YES | PASS |
| reviews.php | theme | runtime | YES | PASS |
| functions.php | theme | runtime | YES | PASS |
| group_fp02_service_section_parity.json | WORDPRESS/acf-json/ | wp-content/acf-json/ | YES | PASS |
| v9-style.css | (not modified in E46) | runtime == backup | YES | PASS |

## 15. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E46-service-section-admin-parity-zavisimosti.md | created | PASS | this file |
| SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md | created | PASS | |
| v9-06e46-service-section-zavisimosti-frontend-block-audit.csv | created | PASS | |
| v9-06e46-service-section-zavisimosti-admin-field-audit.csv | created | PASS | |
| v9-06e46-service-section-hardcoded-html-audit.csv | created | PASS | |
| v9-06e46-service-section-acf-fields-added.csv | created | PASS | |
| v9-06e46-service-section-admin-validation.csv | created | PASS | |
| v9-06e46-service-section-frontend-validation.csv | created | PASS | |
| PROJECT-STATUS.md | updated | PASS | |
| WORDPRESS/SOURCE-AUTHORITY.md | updated | PASS | |

## 16. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local service section admin parity task; persistence handled separately |
| Push attempted | NO |

## 17. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Psych/RPP pages still show addiction-centric nature fallback copy when fields empty | Medium | Accepted (pre-existing demo content) | Seed/customize per page later if needed |
| Founder quote still template-static (toggle only) | Low | By design | Optional later shared-block migration |
| Subnav anchor labels still hardcoded for «Зависимости» wording | Low | Accepted | Optional per-page subnav labels later |
| Duplicate ACF group keys in acf_get_field_groups (JSON+local) | Low | Pre-existing | Separate hygiene task |
| Foreign WIP volume high | Info | Untouched | No git reconciliation |

## 18. Final verdict

PASS

V9-06E46 Service section admin parity — Зависимости:
COMPLETE

Frontend block audit:
PASS

Admin parity implementation:
PASS

Hardcoded HTML migration:
PASS

Repeated/automatic settings:
PASS

Base page frontend preserved:
PASS

Other section pages preserved:
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

## 19. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 20. Final safety statement

Target folder:
X:\AI MARS

V9-06E46 Service section admin parity — Зависимости performed:
YES

Home frozen state touched:
NO

Services hub frozen visual touched:
NO

DB writes:
74

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
