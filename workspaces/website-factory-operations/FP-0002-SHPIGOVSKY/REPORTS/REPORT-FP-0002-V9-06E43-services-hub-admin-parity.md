# REPORT — FP-0002 V9-06E43 SERVICES HUB ADMIN PARITY

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | X:\AI MARS |
| Branch | mars/canonical-post-recovery |
| HEAD | e9d12305ca67fa7205f1215533194e20936855b0 |
| Staged files before | (empty) |
| WIP count only | ~752–759 (foreign WIP present; not touched) |
| Runtime/source canon detected | YES — runtime `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky`; source `workspaces/.../FP-0002-SHPIGOVSKY/WORDPRESS` |
| Home frozen state untouched | YES |
| Commit allowed | NO |
| Result | PASS (local task; no commit/push; remote/HEAD mismatch + unpushed foreign commits noted, not reconciled) |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e43-services-hub-admin-parity-before-20260714-040826\` |
| DB dump | `mars_wp_fp0002.sql` (3 717 770 bytes; `--no-tablespaces`; SHA256 prefix `F66673F8B6D0EB42`) |
| Theme backup/hash | `theme/shpigovsky` + `inventories/theme-sha256.txt` (633 files) |
| Plugin backup/hash | `plugin/shpigovsky-core` + `inventories/plugin-sha256.txt` (22 files) |
| ACF JSON backup/hash | `acf-json/` + `inventories/acf-json-sha256.txt` (9 files) |
| Uploads/media manifest/copy | Manifest only (`inventories/uploads-manifest.txt`); full uploads copy not required (no new Media Library uploads) |
| Services page meta export before | `inventories/services-page-meta-before.json` |
| Services ACF group export before | `inventories/services-acf-groups-before.json` (4 duplicate groups × 8 fields) |
| Services frontend snapshot before | `snapshots/uslugi-frontend-before.html` (HTTP 200) |
| Services admin inventory before | `inventories/services-admin-inventory-before.json` |
| Services/category inventory before | `inventories/services-category-inventory-before.json` (29 services) |
| Result | PASS |

## 3. Services hub discovery

| Area | Finding |
|---|---|
| `/uslugi/` route type | Normal WordPress **page** with custom template |
| Page ID / owner | `#5` — title «Услуги», slug `uslugi` |
| Template/source | `page-templates/services-hub.php` |
| Current ACF group(s) | Before: 4 duplicate `group_fp02_page_services_hub`; After: publish `#1628` only |
| Current admin model | Before: 8 EN/partial fields; After: 38 RU/i18n fields ordered by frontend |
| Existing service generated blocks | Category sections + galleries from CPT (E30/E33/E38) |
| Existing sliders | Category galleries (Swiper dots); hero was single-slide |
| Files to change | Theme services-hub/home/shared partials, helpers, admin CSS/JS, plugin FieldGroups, ACF JSON |

## 4. Frontend block audit

| Order | Frontend block/class | Template/partial | Source before | Classification | Required admin control | Action |
|---:|---|---|---|---|---|---|
| 1 | `services-inner-hero-v2` | `services-hub/hero.php` | ACF scalars + fallback | direct | slides + settings | implemented |
| 2 | `internal-page-nav` | `components/internal-page-nav` | CPT parents | automated | toggle + notice | implemented |
| 3 | `services-category-section-v2` | `service-groups` / `service-group` | Service CPT | repeated/generated | toggle + settings + notice | implemented |
| 4 | `services-program-v2` | `rehabilitation-program.php` | V9 static + program pages | partial | copy fields + toggle | implemented |
| 5 | `founder-quote` | `home/founder-quote.php` | shared static | automated | toggle | implemented |
| 6 | `comfort` | `home/comfort.php` | reusable block | automated | toggle | implemented |
| 7 | secondary CTA band | `program-cta-band` | V9 static | direct | CTA fields + toggle | implemented |
| 8 | `faq` | `services-hub/faq.php` | ACF FAQ repeater | direct | heading + repeater + toggle | implemented |
| 9 | final form | `components/final-form` | reusable block | automated | toggle + notice | implemented |

Full CSV: `REPORTS/evidence/v9-06e43-services-hub-frontend-block-audit.csv`

## 5. Services hub ACF/admin model

| Order | Admin section | Source of truth | Fields/settings | Toggle | Result | Notes |
|---:|---|---|---|---|---|---|
| 1 | Hero | page #5 ACF | `services_hero_slides`, CTA, autoplay/delay/arrows/dots | hero settings | PASS | legacy scalars hidden |
| 2 | Навигация | service CPT parents | notice | `services_hub_nav_visible` | PASS | |
| 3 | Каталог | service CPT | query_mode, placeholders, gallery dots | `services_hub_catalog_visible` | PASS | red notice + link |
| 4 | Программа | hub ACF + program pages | heading/lead/intro/CTA | `services_hub_program_visible` | PASS | cards automatic |
| 5 | Цитата | shared partial | notice | `services_hub_founder_quote_visible` | PASS | |
| 6 | Комфорт | reusable Comfort | notice | `services_hub_comfort_visible` | PASS | |
| 7 | Второй CTA | hub ACF | title/subtitle/button | `services_hub_secondary_cta_visible` | PASS | |
| 8 | FAQ | hub ACF | heading + `services_hub_faq_items` | `services_hub_faq_visible` | PASS | |
| 9 | Финальная форма | reusable Final Form | notice | `services_hub_final_form_visible` | PASS | |

## 6. Services hero slider

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Page-specific design preserved | `services-inner-hero-v2` classes | PASS | Not Home hero |
| Slide repeater | `services_hero_slides` | PASS | max 5 |
| Seeded first slide | from intro/title/eyebrow + media `#303` | PASS | |
| Multi-slide frontend | Swiper + `data-services-hero-slider` | PASS | probe then restored |
| Autoplay setting | `services_hero_autoplay_*` | PASS | |
| Arrows setting | `services_hero_arrows_enabled` | PASS | |
| Dots setting | `services_hero_dots_enabled` | PASS | |
| One-slide hides nav | no slider attrs when count=1 | PASS | |
| Height preserved | CSS `min-height: 320px` on slider shell | PASS | avoid Home height bug |

## 7. Non-repeated editable blocks

| Block | Field(s) | Seeded | Rendered from ACF | Result | Notes |
|---|---|---|---|---|---|
| Hero | `services_hero_slides`, `hero_cta_label` | yes | yes (+ fallback) | PASS | |
| Program copy/CTA | `services_hub_program_*` | yes (V9) | yes (+ fallback) | PASS | cards remain automatic |
| Secondary CTA | `services_hub_secondary_cta_*` | yes (V9) | yes | PASS | |
| FAQ | heading + items | heading seeded; items existing | yes | PASS | |

## 8. Repeated/automatic block controls

| Block | Source of truth | Toggle/settings | Default | Source notice/link | Result | Notes |
|---|---|---|---|---|---|---|
| Nav subnav | parent services CPT | `services_hub_nav_visible` | ON | CPT edit.php link | PASS | |
| Catalog + galleries | service CPT + flags | catalog visible, query_mode, placeholders, dots | ON | CPT link (red/bold) | PASS | E33 dots preserved |
| Program cards | program pages | program visible | ON | program page edit link | PASS | |
| Founder quote | shared partial | founder visible | ON | notice | PASS | |
| Comfort | reusable Comfort | comfort visible | ON | notice | PASS | |
| Final form | reusable Final Form | final_form visible | ON | notice | PASS | |

## 9. Admin UX/i18n

| Check | Expected | Actual | Result |
|---|---|---|---|
| Admin order = frontend order | yes | yes (FieldGroups stack) | PASS |
| Section titles readable | yes | `.fp02-acf-section-title` ~20px on hub edit | PASS |
| Labels Russian | yes | group title + field labels RU | PASS |
| Strings i18n-ready | yes | `__()` / `shpigovsky-core` | PASS |
| Automated notices clear | yes | message fields + danger class | PASS |
| Source links valid | yes/where applicable | CPT + program edit URLs | PASS |
| Save validation | no errors | ACF group reimport clean; 1 attached group | PASS |

## 10. `/uslugi/` frontend validation

| Check | Expected | Actual | Result |
|---|---|---|---|
| HTTP | 200 | 200 | PASS |
| Visual preserved | yes | single-slide shell + copy preserved | PASS |
| Hero slider works | yes | multi-slide probe PASS; restored | PASS |
| Hero height preserved | yes | min-height CSS | PASS |
| Generated service blocks work | yes | category sections present | PASS |
| Category links work | yes | heading-link marker present | PASS |
| Sliders work | yes | `data-services-category-gallery` present | PASS |
| No broken media | yes | hero image attachment reused | PASS |
| No debug/test text | yes | probe title removed after restore | PASS |

## 11. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| `/` | 200 | PASS | Home freeze intact (`hero--home`) |
| `/uslugi/` | 200 | PASS | |
| `/uslugi/zavisimosti/` | 200 | PASS | |
| `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS | |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS | |
| `/blog/` | 200 | PASS | |
| `/specyalisty/` | 200 | PASS | |
| `/o-centre/` | 200 | PASS | |
| `/kontakty/` | 200 | PASS | |

## 12. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| services-hub.php | WORDPRESS/theme/... | runtime theme | YES | PASS |
| hero.php / service-* / faq / rehab | WORDPRESS/theme/... | runtime theme | YES | PASS |
| services-inner-hero-v2.php | WORDPRESS/theme/... | runtime theme | YES | PASS |
| founder-quote.php / comfort.php | WORDPRESS/theme/... | runtime theme | YES | PASS |
| services-hub-helpers.php / admin-editor.php | WORDPRESS/theme/... | runtime theme | YES | PASS |
| v9-shell.js | WORDPRESS/theme/... | runtime theme | YES | PASS |
| admin-home-acf.css | WORDPRESS/theme/... | runtime theme | YES | PASS |
| FieldGroups.php / RepeaterValidation.php | WORDPRESS/plugins/... | runtime plugin | YES | PASS |
| v9-style.css | WORDPRESS/theme/... | runtime theme | operator additive (hashes differ) | PASS_OPERATOR_PRESERVED |
| group_fp02_page_services_hub.json | WORDPRESS/acf-json + runtime acf-json | exported both | YES | PASS |

CSV: `REPORTS/evidence/v9-06e43-source-runtime-sync.csv`

## 13. Documentation/evidence

| File | Action | Result | Notes |
|---|---|---|---|
| REPORT-FP-0002-V9-06E43-services-hub-admin-parity.md | created | PASS | this file |
| SERVICES-HUB-ADMIN-PARITY-MODEL-v1.md | created | PASS | |
| v9-06e43-services-hub-frontend-block-audit.csv | created | PASS | |
| v9-06e43-services-hub-block-model.csv | created | PASS | |
| v9-06e43-services-hub-acf-fields-added.csv | created | PASS | |
| v9-06e43-services-hub-hero-slider-validation.csv | created | PASS | |
| v9-06e43-services-hub-generated-block-settings-validation.csv | created | PASS | |
| PROJECT-STATUS.md / SOURCE-AUTHORITY.md | updated | PASS | E43 notes |

## 14. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | NO |
| Commit skipped reason | Local Services hub admin parity task; persistence handled separately |
| Push attempted | NO |

### Classification of tree changes

- **Intended FP-0002 E43:** theme/plugin/ACF Services hub files, docs/evidence, PROJECT-STATUS/SOURCE-AUTHORITY
- **Runtime-only:** delivered copies under `X:\MARS-Localhost\...`; operator CSS additive
- **DB:** ACF group `#1628`, page #5 meta seeds/toggles; duplicate groups trashed
- **Media:** none new (reused `#303`)
- **Foreign WIP:** remaining monorepo dirty files untouched

## 15. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Duplicate ACF groups can recur from old imports | medium | mitigated (trashed to `#1628`) | watch admin panels; persistence charter |
| Operator `v9-style.css` diverges from source | low | accepted | keep additive-only policy |
| Query_mode meta historically multi-valued | low | normalized | re-check after operator save |
| Monorepo foreign WIP + unpushed commits | medium | acknowledged | selective persistence task only |

## 16. Final verdict

PASS

V9-06E43 Services hub admin parity:
COMPLETE

Services hub discovery:
PASS

Services hero slider:
PASS

Non-repeated block editability:
PASS

Repeated/automatic block controls:
PASS

Admin UX/i18n:
PASS

Services frontend preserved:
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

## 17. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 18. Final safety statement

Target folder:
X:\AI MARS

V9-06E43 Services hub admin parity performed:
YES

Home frozen state touched:
NO

DB writes:
58 (approx; group import/hygiene + seeds + toggle validation restore)

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
