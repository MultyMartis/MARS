# PROD-P07 — Ownership Map (Stage A)

**Date:** 2026-08-14  
**Host:** `http://shpigovsky.beget.tech/`  
**Wave:** FP-0002 PROD-P07 Olya UX/Admin Refinement  
**Method:** local source + live HTML READ (no production writes)

Authority:
- Beget FS = LIVE RUNTIME TRUTH  
- Beget DB = LIVE CONTENT / ADMIN AUTHORITY  
- Local `WORDPRESS/` = CODE / SOURCE AUTHORITY  

---

## 1. Approach / rehabilitation cards (program cards with images)

| Surface | Owner |
|---------|--------|
| Frontend | `template-parts/service/program.php`, `services-hub/rehabilitation-program.php`, `institutional/about-program.php`, `home/rehabilitation-program.php` |
| Helpers | `inc/program-direction-helpers.php` (`shpigovsky_get_program_direction_items`, treatment-program children of page `#13`) |
| Content | Child pages under `/o-centre/programma-lecheniya/` + ACF `treatment_program_short_description` (`group_fp02_treatment_program_child`) |
| Images | Per-item media from program helpers / static asset paths |
| CSS | `assets/css/v9-style.css` — `.services-program-v2__*` |
| JS | none (layout) |
| Shared | YES — same program cards reused across hub / section / leaf / o-centre |

**Equal-height target:** `.services-program-v2__item` (text + bottom media). Live evidence: variable `item-text` lengths; media not row-aligned.

---

## 2. Image alignment / equal-height layout

| Surface | Owner |
|---------|--------|
| CSS | `WORDPRESS/theme/shpigovsky/assets/css/v9-style.css` |
| Selectors | `.services-program-v2__grid`, `__item`, `__item-body`, `__item-media`, `--media-frame-fixed` |
| Fallback | none |
| JS | none |

**Gap:** item is flex column, but body does not grow and media is not `margin-top: auto`, so images misalign across a desktop row.

---

## 3. Guest Visit CTA

| Surface | Owner |
|---------|--------|
| Canonical copy | `inc/institutional-about-v9-content.php` → `shpigovsky_get_v9_about_guest_cta_copy()` |
| Helper | `inc/institutional-helpers.php` → `shpigovsky_get_about_guest_cta_band()` |
| Options overlay | `group_fp02_block_cta_bands` / `fp02-block-cta-bands` (`cta_band_default_*`) |
| Component | `template-parts/components/program-cta-band.php` |
| Correct usages (live) | Home rehab requirements CTA fields; `/uslugi/` program CTA; contacts; service **leaf** stages (`alcohol-direct-v9/stages.php` hardcodes guest visit) |

---

## 4. Generic “Остались вопросы?” CTA

| Surface | Owner |
|---------|--------|
| Final form | `template-parts/components/final-form.php` + `group_fp02_block_final_form` |
| Service mid-CTA / default band | `shpigovsky_get_service_cta_band()` → page `cta_*` else `cta_band_default_*` options |
| Live | Final form heading “Остались вопросы?” on Home / hub / section / leaf |

**Do not globally replace.**

---

## 5. “Что нужно для прохождения реабилитации и лечения”

| Context | Frontend | CTA today (live) | Desired CTA |
|---------|----------|------------------|-------------|
| Home Comfort block | `home/rehabilitation-requirements.php` + `fp02-block-comfort` options | Guest Visit (via rehab CTA fields) | keep |
| Service **subdivision** stages | `service/stages.php` | `shpigovsky_get_service_cta_band()` → **“Остались вопросы?”** | Guest Visit |
| Service **leaf** stages | `alcohol-direct-v9/stages.php` | Guest Visit (hardcoded) | keep; prefer shared helper |
| Support list | same stages / home block — “Поддержка осуществляется на всех этапах” | ACF / options | keep |

**Bug owner:** subdivision `stages.php` CTA selection (not final-form).

---

## 6. Generic Content main text

| Surface | Owner |
|---------|--------|
| Template | `page-templates/generic.php` |
| Partial | `template-parts/generic/content-page.php` |
| ACF | `group_fp02_page_generic_content` — `generic_page_lead`, `generic_page_body` |
| CSS | `.plain-page-content`, `.plain-page-content__body` (minimal; weak H2/H3/list rhythm) |
| Page | `/o-centre/programma-lecheniya/` uses Generic Content (`generic_body_present=true`) |

---

## 7. Reusable blocks on program-type / Generic pages

| Surface | Owner |
|---------|--------|
| Existing reusable IDs | `fp02-block-comfort*` (requirements/gallery/intro), infrastructure narrative (`institutional/infrastructure-narrative.php`), specialists, CTA bands, final form |
| Generic template today | **no** selector — body only |
| Preferred model | page-level toggles/order storing **selection only**; render shared partials |

Minimum justified:
1. treatment/rehab requirements (`home/rehabilitation-requirements.php`)
2. “О доме” / territory — Comfort gallery or infrastructure narrative (canonical shared)

---

## 8. Approach cards Admin UI (“Карточки подхода”)

| Stack | Admin field | Frontend |
|-------|-------------|----------|
| Раздел (subdivision) | `group_fp02_service_section_parity` → `section_approach_cards` | `template-parts/service/team-stats.php` |
| Услуга (leaf) | `group_fp02_service_general_parity` → `service_general_approach_cards` | `alcohol-direct-v9/approach.php` via `shpigovsky_get_general_approach_copy()` |
| Legacy leaf approach | `service/approach.php` reads treatment-program children (not the repeater) | dormant for leaf stack when general parity used |

**Live `/uslugi/zavisimosti/`:** `team-stats` present (2 images) but **0 approach card nodes** — repeater empty or not meaningful; images alone look like a static demo composition.

---

## 9. “Поддержка осуществляется на всех этапах”

| Context | Owner |
|---------|--------|
| Home / Comfort | `rehab_requirements_support_*` on `fp02-block-comfort` |
| Subdivision stages | `section_stages_support_heading` / `section_stages_support_items` |
| Leaf stages | `service_general_stages_support_*` via `shpigovsky_get_general_stages_copy()` |
| CSS | `.home-rehabilitation-requirements__support*` |

---

## 10. Visible TEST / DEMO markers

| Finding | Classification | Action intent |
|---------|----------------|---------------|
| Foot link text `подробнее о программе ТЕСТ` on `/uslugi/zavisimosti/` | technical marker (frontend-visible) | remove `ТЕСТ` from owned field/value |
| Broad `тест` substring hits | often inside real words (e.g. выработку) | **preserve** — do not global-strip |
| `DEMO` in live audited routes | not found as visible marker in sampled HTML | no action |
| `001тест` / `002ТЕСТ` / `тест03` | not found in sampled live HTML | SAFE UNKNOWN pending DB scan |

---

## Ambiguity / STOP notes

| Item | Status |
|------|--------|
| Equal-height owner | CLEAR → CSS `services-program-v2` |
| Guest Visit in subdivision stages | CLEAR → change CTA source in `stages.php` |
| Approach cards empty on section #73 | CLEAR problem; DB values must be READ before content write |
| Reusable selector on Generic | CLEAR gap; bounded ACF + template render — no full page builder |
| Demo visual for approach | Images render without cards — classify as empty structured data + asset fallbacks, not a separate mock screenshot URL |

**No competing SoT created in this map.**
