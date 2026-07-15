# REPORT — FP-0002 V9-06E41 HOME ADMIN HERO SLIDER TOGGLES AND RECOVERY LIFE STAGES

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | 1b7cda593165eb4a7b8b745d6b416b18fcbcc7f2 |
| Staged files before | (empty) |
| WIP count only | ~731–739 (foreign monorepo WIP; MetaBOT commits ahead of origin) |
| Runtime/source canon detected | YES — `WORDPRESS/` → runtime `shpigovsky` / `shpigovsky-core` / `acf-json` |
| Commit allowed | NO |
| Result | PASS (local bounded writes only; commit skipped; no git reconciliation) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e41-home-admin-hero-toggles-recovery-life-before-20260714-015935\` |
| DB dump | `mars_wp_fp0002.sql` (2 139 092 bytes; `--no-tablespaces`; hash prefix `0AEEEA656476DF68`) |
| Theme backup/hash | theme / 632 files; CSS hash prefix `A0091D53C19F4710` (pre-change) |
| Plugin backup/hash | plugin / 22 files; FieldGroups prefix `F0F83B897687C66A` (pre-change) |
| ACF JSON backup/hash | acf-json / 9 files; home JSON prefix `123E016E039D36B1` (pre-change) |
| Home meta export before | `exports/home-meta-before.tsv` |
| Home ACF group export before | (via probe + pre-E41 group `#1244`) |
| Home admin inventory before | E40 inventory 55 fields; hero slides=2 confirmed |
| Home frontend snapshot before | `snapshots/home-before.html` (HTTP 200, 165 543 bytes) |
| Hero slides export before | `exports/home-hero-slides-before.tsv` (titles: «Шпиговский дом 1», «Шпиговский дом 2») |
| Recovery life stages export before | `exports/home-recovery-life-stages-before.tsv` (3 stages) |
| Result | PASS |

## 3. Pre-implementation audit

| Area | Finding |
|---|---|
| Home admin section title source | Field/repeater/message labels in `group_fp02_page_home` (e.g. recovery intro heading, intro bands, gallery mode) |
| Admin CSS/enqueue path | New `assets/css/admin-home-acf.css`; enqueue in `inc/admin-editor.php` for front-page edit only |
| Hero render source | `template-parts/home/hero.php` previously rendered **only** `$slides[0]` |
| Hero slides count/data | 2 slides; titles «Шпиговский дом 1» / «Шпиговский дом 2»; both images attachment `#89` |
| Standalone Hero image usage | `hero_media` = `#302`; previously preferred over slide images — retired/hidden |
| Slider JS/vendor source | Local Swiper via `home-vendors.php` (already on front page) |
| Automated blocks needing toggles | Founder quote, treatment, gallery, reviews, rehab requirements, rehab program, comfort, specialists, articles |
| Recovery life render source | `template-parts/home/recovery-life.php` + `.home-recovery-life__stage` card CSS |
| Files to change | FieldGroups, ACF JSON, hero/recovery/toggled partials, helpers, admin CSS/JS/CSS, report/evidence/status |
| Source/runtime differences | Pre-task FieldGroups matched; post-task MATCH for all E41 deliverables |

## 4. Admin UX heading implementation

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Section/block titles ~20px | `.acf-field.fp02-acf-section-title > .acf-label > label { font-size:20px }` | PASS | Nested repeater labels forced back to 13px |
| Scoped to Home admin | Enqueue only when editing `page_on_front` | PASS | `shpigovsky_enqueue_home_acf_admin_css` |
| Normal labels unaffected | No global `.acf-label label` rule | PASS | Wrapper class only |
| Russian/i18n-ready labels preserved | Existing `__()` + `shpigovsky-core` | PASS | New strings also wrapped |

**Selectors:** `.acf-field.fp02-acf-section-title > .acf-label > label`; message fields same; nested `.acf-fields > .acf-field > .acf-label > label` remain normal.

## 5. Hero slider implementation

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Slides from repeater | `home_hero_slides` loop in `hero.php` | PASS | |
| Second slide visible | «Шпиговский дом 2» in HTML | PASS | validated |
| Horizontal animation | Swiper `direction:'horizontal'`, `effect:'slide'` | PASS | `initHomeHeroSlider` in `v9-shell.js` |
| Autoplay setting | `home_hero_autoplay_enabled` + delay (default 5000) | PASS | default on |
| Arrows setting | `home_hero_arrows_enabled` | PASS | default on |
| Dots setting | `home_hero_dots_enabled` | PASS | default on |
| One-slide hides nav | `hero.php` sets `$is_slider = count > 1` | PASS | no arrows/dots/autoplay |
| Standalone Hero image retired/handled | Hidden via `.fp02-acf-legacy-retired`; priority now slides → legacy → theme | PASS | meta `#302` kept |

## 6. Automated block toggles

| Block | Source of truth | Toggle field | Default | Frontend behavior | Result | Notes |
|---|---|---|---|---|---|---|
| Founder quote | Site Settings / static V9 | `home_founder_quote_visible` | enabled | hide when off (front page only) | PASS | shared partial gated with `is_front_page()` |
| Treatment & prevention | CPT accordion + Home heading | `home_treatment_prevention_visible` | enabled | hide whole section | PASS | |
| Gallery | CPT services + Home modes | `home_gallery_visible` | enabled | hide gallery | PASS | mode settings retained |
| Reviews | Site Settings / Reviews | `home_reviews_visible` | enabled | hide reviews | PASS | |
| Rehab requirements | Reusable blocks | `home_rehab_requirements_visible` | enabled | hide section | PASS | notice added |
| Rehab program | Program pages helper | `home_rehab_program_visible` | enabled | hide section | PASS | notice added |
| Comfort | Reusable comfort block | `home_comfort_visible` | enabled | hide on front only | PASS | |
| Specialists | `/specyalisty/` children | `home_specialists_visible` | enabled | hide on front only | PASS | |
| Articles | WP posts | `home_articles_visible` | enabled | hide articles | PASS | heading still editable |
| Final form | Reusable + Home fallback | — | — | unchanged | N/A | STATIC_NO_TOGGLE_THIS_WAVE |

Evidence: `REPORTS/evidence/v9-06e41-home-automated-block-toggle-audit.csv`

## 7. Recovery life stage markup

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Outer wrapper | `.home-recovery-life__stage` | PASS | |
| Inner bordered card | `.home-recovery-life__stage-inner` | PASS | border/padding moved |
| Month labels | `.home-recovery-life__stage-label` | PASS | 1/2/3 месяц |
| Label style | `color: var(--color-accent)`; 18px; weight 700 | PASS | not outlined |
| Desktop preserved | flex row, align flex-end | PASS | |
| Mobile preserved | column stack; inner padding from E36 media queries | PASS | |
| ACF label field/fallback | `stage_label` + sequential fallback | PASS | seeded on 3 stages |

## 8. Home admin validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Home edit loads | yes | ACF group `#1338` publish; `acf_get_fields` = 70 | PASS |
| Section headings larger | yes | `.fp02-acf-section-title` + admin CSS | PASS |
| Normal labels normal | yes | nested label CSS reset | PASS |
| Hero slider settings visible | yes | autoplay/delay/arrows/dots present | PASS |
| Automated toggles visible | yes | 9 visibility toggles + notices | PASS |
| Recovery stage labels seeded | yes | `1 месяц`…`3 месяц` | PASS |
| Save validation | no errors | no required blockers added | PASS |

## 9. Home frontend validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| Home HTTP | 200 | 200 | PASS |
| Hero slider active | yes | `data-hero-slider` present | PASS |
| Second slide visible | yes | «Шпиговский дом 2» in HTML | PASS |
| Nav obeys settings | yes | arrows/dots present with defaults on | PASS |
| Founder quote toggle works | yes | off hides / on shows | PASS |
| All toggles restored enabled | yes | restored after validation | PASS |
| Recovery life labels visible | yes | 1/2/3 месяц + inner cards | PASS |
| Visual preserved | yes | structure/classes preserved; additive CSS | PASS |

Evidence: `REPORTS/evidence/v9-06e41-home-hero-slider-validation.csv`, `…-recovery-life-stage-markup-validation.csv`

## 10. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | |
| `/uslugi/` | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | no fatal |

## 11. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| hero.php | WORDPRESS/theme/.../home/hero.php | themes/shpigovsky/.../hero.php | YES | PASS |
| recovery-life.php | WORDPRESS/theme/.../home/recovery-life.php | runtime same | YES | PASS |
| founder-quote.php | WORDPRESS/theme/.../home/founder-quote.php | runtime same | YES | PASS |
| gallery.php | WORDPRESS/theme/.../home/gallery.php | runtime same | YES | PASS |
| treatment-prevention.php | WORDPRESS/theme/.../ | runtime same | YES | PASS |
| reviews.php | WORDPRESS/theme/.../ | runtime same | YES | PASS |
| comfort.php | WORDPRESS/theme/.../ | runtime same | YES | PASS |
| specialists.php | WORDPRESS/theme/.../ | runtime same | YES | PASS |
| articles-teaser.php | WORDPRESS/theme/.../ | runtime same | YES | PASS |
| rehabilitation-program.php | WORDPRESS/theme/.../ | runtime same | YES | PASS |
| rehabilitation-requirements.php | WORDPRESS/theme/.../ | runtime same | YES | PASS |
| hero-helpers.php | WORDPRESS/theme/.../inc/ | runtime same | YES | PASS |
| home-fallbacks.php | WORDPRESS/theme/.../inc/ | runtime same | YES | PASS |
| admin-editor.php | WORDPRESS/theme/.../inc/ | runtime same | YES | PASS |
| v9-style.css | WORDPRESS/theme/.../assets/css/ | runtime same | YES | PASS |
| admin-home-acf.css | WORDPRESS/theme/.../assets/css/ | runtime same | YES | PASS |
| v9-shell.js | WORDPRESS/theme/.../assets/js/ | runtime same | YES | PASS |
| FieldGroups.php | WORDPRESS/plugins/.../Fields/ | runtime same | YES | PASS |
| group_fp02_page_home.json | WORDPRESS/acf-json/ | runtime acf-json | YES | PASS |

## 12. Git result

| Item | Value |
|---|---|
| Staged before | (empty) |
| Staged after | (empty) |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local Home polish/admin task; persistence handled separately |
| Push attempted | NO |

### Git classification (read-only)

| Class | Notes |
|---|---|
| Intended FP-0002 changes | `FP-0002-SHPIGOVSKY` theme/plugin/ACF/report/evidence/status under WORDPRESS + REPORTS |
| Runtime-only changes | Localhost theme/plugin/acf-json/DB (outside git or mirrored via sync) |
| DB changes | Home meta toggles/stage labels; ACF group `#1338` ( `#1244` trashed) |
| Media changes | none |
| Foreign WIP | large monorepo WIP (~739); v7/v8/MetaBOT noise untouched |

## 13. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Duplicate ACF Home groups during import | Medium | Mitigated | `#1244` trashed; `#1338` keep (70 fields) |
| Shared founder-quote partial affecting other routes | Medium | Mitigated | toggle gated with `is_front_page()` |
| Hero layout regression with Swiper wrapper | Medium | Mitigated | single-slide path preserves non-swiper markup; multi-slide validated |
| Operator visual of label weight | Low | Accepted | 700 / 18px / accent; not outlined |
| Unpersisted local work vs remote HEAD drift | Medium | Known | CREATE persistence task when operator requests |

## 14. Final verdict

PASS

V9-06E41 Home admin hero slider / toggles / recovery life stages:
COMPLETE

Admin heading readability:
PASS

Hero slider:
PASS

Hero admin settings:
PASS

Automated block toggles:
PASS

Recovery life stage markup:
PASS

Home frontend preserved:
PASS

Home admin validation:
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

## 15. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 16. Final safety statement

Target folder:
X:\AI MARS

V9-06E41 Home admin hero slider / toggles / recovery life stages performed:
YES

DB writes:
~30 (ACF group reimport/repair; toggle seeds; stage_label seeds; founder toggle off/on validation restore)

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

## Execution safety
- cwd: X:\AI MARS
- scope lock honored: yes (`X:\AI MARS`, `X:\MARS-Localhost`)
- destructive ops: none (ACF duplicate group trash only within WordPress ACF posts; no filesystem delete)
- protected zone touch: none
