# REPORT — FP-0002 V9-06E60 Navigation/Breadcrumb Restore, CTA Unification and Service Links

**Date:** 2026-07-17  
**Runtime:** `http://shpigovsky.test/`  
**Database:** `mars_wp_fp0002`  
**Evidence:** `REPORTS/evidence/v9-06e60-nav-breadcrumb-cta-service-links/`  
**Backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e60-before-nav-breadcrumb-cta-service-links-20260717-015352`

---

## 1. Status

| Item | Result |
|------|--------|
| Overall | **PASS** |
| Operator review | **pending** |
| DB writes | **0** (CTA option fields already populated; seed skipped) |
| Commit / push / freeze | **no** |

---

## 2. Pre-Change Backup

| Item | Value |
|------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e60-before-nav-breadcrumb-cta-service-links-20260717-015352` |
| DB dump | `db/mars_wp_fp0002.sql` — 4 063 340 bytes — SHA256 `6CDC0FE766553B08BB1B06BAC62B126B30A4E09534453CF386C573C52E806F7E` |
| Validation | **PASS** (`CREATE TABLE` + `INSERT` present; `BACKUP-OK.txt`) |
| Hashes / manifest | `hashes.csv`, `operator-change-manifest.csv` |

---

## 3. Latest Operator Changes Canonized

| File | Classification | Action |
|------|----------------|--------|
| `assets/css/v9-style.css` | operator CSS | runtime `C8AE0923299B…` promoted to source (blog-article-hero padding/media only drift) |
| theme/plugin otherwise | MATCH | no other theme/plugin drift |
| `group_fp02_block_cta_bands.json` | SRC then delivered | synced into runtime ACF JSON in this wave |

**Post-wave CSS hash prefix:** `B60D01A404FA…`  
**Unresolved theme drift:** **0**

---

## 4. Navigation and Breadcrumb Audit

**Verdict:** prior E58 visual-audit / E59 polish waves did **not** change primary navigation or general breadcrumb typography. No unwanted automated typography restoration was required.

| selector | viewport | pre-intervention | intervention | current | final | evidence | action |
|----------|----------|------------------|--------------|---------|-------|----------|--------|
| `.site-header__nav-link` (`--font-size-nav` / `--line-height-nav`) | all | 16px / 20px | unchanged E58→E59→now | 16/20 | 16/20 | E58/E59 backups, V9 static, viewport JSON | NO_RESTORE |
| `.offcanvas__nav-link` | all | 16px / 20px | unchanged | 16/20 | 16/20 | same | NO_RESTORE |
| `.internal-page-nav .breadcrumbs__*` | desktop+ | 14px / 18px | unchanged | 14/18 | 14/18 | same | NO_RESTORE |
| `.page-blog` / article breadcrumbs `@max-width:1024` | ≤1024 | 8px / 12px | V9 Figma `EXACT_GEOMETRY` (not E58) | 8/12 | 8/12 | `fp-0002-shpigovsky-v9/src/scss/style.scss` | NO_RESTORE |
| commented SCSS 11px mobile breadcrumb | mobile | never shipped | commented-only | n/a | n/a | V9 SCSS comments | SAFE UNKNOWN / inactive |

Hover color for breadcrumbs was updated to `var(--color-accent-hover)` under Task 03 (not a typography restore).

---

## 5. Navigation and Breadcrumb Restoration

| Item | Detail |
|------|--------|
| Files | none for typography restore |
| Selectors restored | **none** |
| Preserved | floating header, offcanvas, layout, colors, operator CSS |
| Viewport validation | 1440 / 1024 / 480 / 370 — nav 16/20; crumbs 14/18 on `/uslugi/` |

---

## 6. Canonical CTA Unification

| Item | Detail |
|------|--------|
| Canon | `.home-rehabilitation-requirements__cta-band` (operator wrap01/wrap02 + lead / lead-txt / button / phone column) |
| Identical variants | all `.program-cta-band` usages via shared partial |
| Template | `template-parts/components/program-cta-band.php` rebuilt one-to-one |
| Structure | `__wrap01` → `__lead` + `__lead-txt`; `__wrap02` → button + phone/`span` hint |
| Shared CSS | program band visual model aligned to Home Comfort CTA |
| Visual / responsive | desktop grid + ≤1024 stack matching Home CTA pattern; blog mobile overrides remapped to new classes |
| Old classes removed from FE | `__title`, `__subtitle`, `__copy`, `__phone-hint`, `--button-first` ordering |

---

## 7. CTA Admin Parity

| Item | Detail |
|------|--------|
| Field group | `group_fp02_block_cta_bands` (`fp02-block-cta-bands`) |
| Fields (reused, labels aligned) | `cta_band_default_title` → «CTA лид»; `cta_band_default_subtitle` → «Текст CTA»; `cta_band_phone_hint`; `cta_band_default_button_label` |
| Page/service ownership | service `cta_title` / `cta_text` / `cta_button_label` / `cta_button_target`; blog archive/article final CTA fields; block defaults as fallback |
| Button URL | optional `button_url` / `cta_button_target` → `<a>`; empty → consultation modal (Home model) |
| Seeded values | **none** — block options already non-empty |
| Current block values | title «Остались вопросы?»; subtitle present; hint «Или позвоните нам»; button «Заказать звонок» |
| Duplicates avoided | no new field keys |

---

## 8. Service Name Links

| Item | Detail |
|------|--------|
| Templates | `service-card.php` (hub v2); `children.php` (section children) |
| Markup | `<a class="services-category-section-v2__service-name" href="…">` or `<span>` if no URL |
| Data source | CPT permalink via `get_permalink()` / card URL query var |
| Routes validated | `/uslugi/` (8 sample links); `/uslugi/zavisimosti/` (6 links) |
| Nested anchors | none (separate «узнать больше» link remains sibling) |
| Fallback | empty permalink → non-link span |

---

## 9. Hover/Focus Audit

| selector/component | prior | classification | final | a11y |
|--------------------|-------|----------------|-------|------|
| `.site-header__nav-link:hover` | accent + `::after` bar | NAVIGATION | `accent-hover`; bar opacity 0 | focus-visible outline kept |
| `.offcanvas__nav-link:hover` | accent | NAVIGATION | `accent-hover` | outline kept |
| `.site-footer__nav-link:hover` | accent + underline | NAVIGATION | `accent-hover`; no underline | outline kept |
| `.site-footer__nav-heading-link` | E59 accent-hover | NAVIGATION | unchanged | ok |
| `a.services-category-section-v2__service-name` | child `.service-name-link` | CARD TITLE | class on `<a>`; accent-hover | ok |
| `.service-child-link` | dotted border underline | CARD TITLE | accent-hover; border 0 | ok |
| direction / program title links | underline | HEADING | accent-hover; no underline | ok |
| specialists card name hover | underline | CARD TITLE | accent-hover | permanent base underline on `.specialists__name` retained (SAFE UNKNOWN) |
| breadcrumbs links | accent | NAVIGATION | accent-hover | ok |
| consent / legal / body links | underline | INLINE/LEGAL | unchanged | readability |

---

## 10. Database Changes

| Item | Detail |
|------|--------|
| Exact writes | **0** |
| Skipped seed | `cta_band_phone_hint` already «Или позвоните нам» |
| Idempotency | validate script skips nonempty |
| Unrelated writes | none |

---

## 11. Exact Files Changed

### Canonical source
- `WORDPRESS/theme/shpigovsky/assets/css/v9-style.css`
- `WORDPRESS/theme/shpigovsky/template-parts/components/program-cta-band.php`
- `WORDPRESS/theme/shpigovsky/template-parts/components/service-card.php`
- `WORDPRESS/theme/shpigovsky/template-parts/service/children.php`
- `WORDPRESS/theme/shpigovsky/template-parts/service/mid-cta.php`
- `WORDPRESS/theme/shpigovsky/inc/service-helpers.php`
- `WORDPRESS/theme/shpigovsky/inc/blog-helpers.php`
- `WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php`
- `WORDPRESS/acf-json/group_fp02_block_cta_bands.json`
- `WORDPRESS/validation/v9-06e60-nav-cta-links/_e60_validate.php`
- `WORDPRESS/validation/v9-06e60-nav-cta-links/_e60_viewports.cjs`

### Runtime (exact deliver)
- matching theme/plugin/ACF paths under `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\`

### Reports / evidence
- `REPORTS/REPORT-FP-0002-V9-06E60-nav-breadcrumb-cta-service-links.md`
- `REPORTS/evidence/v9-06e60-nav-breadcrumb-cta-service-links/*`
- `PROJECT-STATUS.md`
- `WORDPRESS/SOURCE-AUTHORITY.md` (E60 note)

---

## 12. Source-to-Runtime Delivery

| Item | Result |
|------|--------|
| Exact files | 9 delivered; theme tree drift after = **0** |
| Hashes | `evidence/.../source-runtime-hashes.csv` |
| Broad sync | **no** |
| Operator CSS | promoted then additive E60 edits preserved |

---

## 13. Validation

| Area | Result |
|------|--------|
| Navigation typography | 16/20 at all tested viewports |
| Breadcrumbs | 14/18 on service routes; blog mobile 8/12 retained (Figma) |
| CTA blocks | Home canonical present; program wrap01/wrap02/lead on hub/section/service/blog/contacts/reviews |
| Service links | hub + section anchors resolve to service permalinks |
| Admin fields | existing block options populated; labels updated in PHP+JSON |
| HTTP | required routes 200 |
| PHP noise / JS errors | 0 on probed pages |
| Overflow | 0 on Playwright samples |

---

## 14. Regression

| Route / surface | Result |
|-----------------|--------|
| `/`, `/uslugi/`, section, alcohol service, `/o-centre/`, `/kontakty/`, `/blog/`, blog single, `/otzyvy/` | 200 |
| Header / floating header / offcanvas | preserved (hover color only) |
| Forms / galleries / lifebuoy / maps / video / heroes | not modified |

---

## 15. Risks and Tails

- **SAFE UNKNOWN:** inactive commented 11px breadcrumb SCSS never proven as live regression; permanent `.specialists__name` underline base style left intact.
- CTA ownership remains multi-scope (block defaults + page/service + blog fields) by design.
- Hover accessibility: focus-visible outlines retained where previously present; no global `outline: none`.
- Operator visual acceptance still required for CTA band parity and service-name link styling.

---

## 16. Git Status

- **no commit / no push / no freeze**
- Exact FP-0002 scope only
- Foreign WIP untouched
- Branch `mars/canonical-post-recovery` (HEAD ahead of origin; not pushed)

---

## 17. Operator Review Pages

1. `http://shpigovsky.test/` — Home Comfort CTA (canon unchanged) + header nav hover  
2. `http://shpigovsky.test/uslugi/` — service-name links + program CTA band  
3. `http://shpigovsky.test/uslugi/zavisimosti/` — section child service-name links + CTA  
4. `http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` — mid CTA  
5. `http://shpigovsky.test/o-centre/` — program CTA  
6. `http://shpigovsky.test/kontakty/` — contacts CTA  
7. `http://shpigovsky.test/blog/` — blog CTA + breadcrumbs @1024  
8. One blog single — article CTA  
9. `http://shpigovsky.test/otzyvy/` — reviews CTA wrap  
10. Admin → **Reusable Block — CTA Bands** (`fp02-block-cta-bands`) — field labels  
11. Admin → one Услуга mid-CTA fields (`cta_title` / `cta_text` / `cta_button_label` / `cta_button_target`)  
12. Viewports 1440 / 1024 / 480 / 370 — header nav + breadcrumbs  
