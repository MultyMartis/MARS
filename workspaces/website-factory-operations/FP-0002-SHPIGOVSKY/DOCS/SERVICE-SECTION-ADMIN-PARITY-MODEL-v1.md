# FP-0002 — Service Section Admin Parity Model v1

**Status:** **FROZEN (local)** — V9-06E46 + FIX01–FIX05 + **V9-06E50** + **V9-06E50 freeze** + note **V9-06E51** + **V9-06E51-FIX01** + **V9-06E51-FIX02** + **V9-06E51 Placeholder Mode FREEZE**  
**Date:** 2026-07-16  
**Base page:** `#73` Зависимости (`/uslugi/zavisimosti/`)  
**Page type:** Раздел (`service_editor_role=section` → stack `subdivision`)  
**Canonical ACF group (section blocks):** `group_fp02_service_section_parity` (55 fields; FIX05: `section_team_image` / `section_corridor_image` replace approach_* image names)  
**Layout group:** `group_fp02_service_layout_hero` (title **Макет страницы услуги**)  
**Hero group:** `group_fp02_service_hero` (title **Hero страницы услуги**) — shared for Раздел and Услуга  
**Applies to:** all first-level section pages (`#73`, `#77`, `#84`)  
**Freeze marker:** `REPORTS/FREEZE-FP-0002-V9-06E50-SERVICE-SECTIONS-DEMO-ACF-SOT-ACCEPTED.md`  
**Freeze backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e50-service-sections-demo-acf-sot-freeze-accepted-before-next-phase-20260715-230201\`  
**E51 layout note:** first-level selector also offers **Заглушка** (`placeholder`); `#73/#77/#84` remain `section` (not enabled). Placeholder mode does not delete section ACF content.  
**E51-FIX01 note:** manual layout role selection must persist (visible role wins over stale technical layout). Sections untouched in FIX01 validation.  
**E51-FIX02 note:** real wp-admin ACF input name fix for nested role selector; sections `#73/#77/#84` unchanged (still `section`).  
**E51 freeze note:** Placeholder Mode frozen after operator acceptance («Да, теперь всё гуд»); sections `#73/#77/#84` re-validated as `section`/`subdivision` and untouched. Freeze backup: `v9-06e51-placeholder-mode-freeze-accepted-before-next-phase-20260716-013604`.

This document describes admin/frontend parity for **service section (Раздел)** pages after V9-06E46 / FIX01–FIX05 and **V9-06E50** (strict ACF SoT / no normal empty-admin demo inject).  
It follows Home (`DOCS/HOME-PAGE-ADMIN-PARITY-MODEL-v1.md`) and Services hub (`DOCS/SERVICES-HUB-ADMIN-PARITY-MODEL-v1.md`) models.  
Page type **Раздел** is **frozen locally** pending an explicit change request.  
It is **not** a production/hosting claim, and **not** Услуга (`service_general`) page parity.

---

## Freeze status (V9-06E50 freeze)

| Item | Value |
|------|-------|
| Operator acceptance | E50: «Всё гуд!» |
| Frozen targets | `#73` / `#77` / `#84` |
| Normal text SoT | Page ACF only (seeded/demo/current) |
| Empty optional field | Hide / empty-safe — **no** normal hardcoded demo inject |
| Emergency fallback | Technical/legacy only |
| Do not change without charter | Section ACF group, FE empty-safe helpers/templates, admin help wording |
| Preserved | Home E42 · `/uslugi/` E44 · Услуга E47–E49 · operator `v9-style.css` drift |

---

## E50 updates (demo ACF SoT + empty-safe FE)

| Change | Detail |
|--------|--------|
| Normal text SoT | Frontend subdivision chrome reads **ACF on the section page** only |
| Empty admin field | Optional text/cards/intro/support hide or render empty-safe — **no hardcoded demo inject** |
| Emergency helpers | PHP `*_fallback()` functions remain in theme for catastrophic/legacy unseeded pages only; not called on normal path |
| Section-specific demo | `#77/#84` headings/intros/nature blocks/subnav no longer reuse dependency-specific «Зависимости» copy |
| Subnav | Subdivision subnav labels for deps/nature/approach resolve from ACF when filled |
| Admin wording | Cleared field → optional text may hide; emergency reserve = technical only |
| Images | Emergency theme-asset reserve remains when ACF image empty (`#1238/#1239/#1709` seeded) |

## FIX05 updates (demo seed + no template-fallback SoT)

| Change | Detail |
|--------|--------|
| Content SoT | Normal frontend content for Раздел blocks comes from **ACF on the section page**, not hardcoded template fallback |
| Demo seed | Empty fields on `#73/#77/#84` seeded from current FE fallback/demo output; meaningful `#73` operator values (ТЕСТ/000101) preserved |
| Team image | Field `section_team_image` («Изображение команды»); seeded `#1238` (same ML asset as Home staff; Home field untouched) |
| Corridor image | Field `section_corridor_image` («Изображение коридора»); seeded `#1709` (theme corridor asset registered in ML for admin selection) |
| Landscape | `section_clinic_landscape_image` still primary; wording updated (no Home-as-normal SoT) |
| Admin wording | Removed “fallback шаблона / theme asset / берётся с главной” as normal model; demo + emergency-reserve wording |
| Emergency fallback | PHP emergency helpers remain only to avoid blank critical markup on unseeded future pages — not normal SoT |
| Automatic blocks | Children CPT, specialists, comfort, reviews, final form, founder quote — still intentional shared/automatic |

## FIX04 updates (admin cleanup + section landscape + hide editor)

| Change | Detail |
|--------|--------|
| Program footer label | `section_program_footer_label` / «Текст нижней ссылки программы» **removed from admin UI**; meta kept; FE `program.php` still uses `shpigovsky_section_text(…, 'подробнее о программе')` (stored value or fallback) |
| Clinic landscape SoT | No longer Home `home_clinic_landscape_image` for Раздел pages |
| New field | `section_clinic_landscape_image` («Изображение территории клиники») + section-specific notice |
| Seed | `#73/#77/#84` seeded with attachment `#1239` (same as current Home landscape) |
| FE resolver | `clinic-landscape.php`: section context → `shpigovsky_section_image_or_asset(section_clinic_landscape_image)` → theme asset; Home unchanged |
| Classic editor | Hidden for **service CPT** edit screens via `remove_post_type_support` + `remove_meta_box('postdivrich')` + admin CSS; `post_content` preserved |

## FIX03 updates (CTA cleanup + program fallback)

| Change | Detail |
|--------|--------|
| Removed admin § CTA | `5. CTA «Раздел услуги»` notice + `section_mid_cta_visible` toggle removed from parity group UI |
| Mid-CTA SoT | Frontend mid-cta content: Structured Sections `cta_title` / `cta_text` / `cta_button_label` + site `phone_primary`; visibility default ON (`section_mid_cta_visible` meta kept legacy, no admin UI) |
| Section renumber | Former 6–15 → **5–14** (Program … Final form) |
| Program footer | Empty → FE fallback only; user value never replaced by demo; placeholder/instructions clarified |
| Program intros | Meaningful repeater rows win; empty rows ignored (no demo padding); managed empty → demo (not legacy fight); unmanaged → legacy → demo |
| Helpers | `shpigovsky_has_meaningful_repeater_rows()`, `shpigovsky_get_section_program_intro_demo_fallback()`, managed-repeater detection |

## FIX02 updates (repeaters + stages)

| Change | Detail |
|--------|--------|
| §3 label | `3. Дочерние услуги` (was «Зависимости / дочерние услуги»); children source notice unchanged |
| §5 label (historical) | Was `5. CTA «Раздел услуги»` — **removed in FIX03** |
| Nature text pairs | Repeater `section_nature_text_blocks` (heading/text + optional link_label/link_url/after_text); legacy neuro/geno scalar metas remain as fallback |
| Program intros | Repeater `section_program_intro_items` (text rows); legacy `section_program_intro` / `section_program_intro2` fallback when unmanaged |
| Stages items | Repeater `section_stages_items` (title/text/enabled) primary; fallback Structured Sections `stages` then theme defaults |
| Stages PHP bug | Removed premature `?>` in `template-parts/service/stages.php` that leaked PHP source onto frontend |

Helpers: `shpigovsky_get_section_nature_text_blocks()`, `shpigovsky_get_section_program_intro_items()`, `shpigovsky_get_section_stages_items()`, `shpigovsky_has_meaningful_repeater_rows()`.

---

## Architecture summary

### Frontend is canon

- Render order is defined by `template-parts/service/subdivision-stack.php`.
- Admin ACF field order in `group_fp02_service_section_parity` follows that sequence (numbered section notices **1–14** after FIX03; mid-cta has no parity admin block).
- Visual design for hero remains `services-inner-hero-v2` (not Home `.hero--home`).
- Stages visual pattern reuses Home `home-rehabilitation-requirements__*` markup.

### Admin group separation (FIX01)

| Group | Visible title | Responsibility |
|-------|---------------|----------------|
| `group_fp02_service_layout_hero` | Service — Layout | `Макет страницы услуги` + technical hidden fields + hub/catalog flags |
| `group_fp02_service_hero` | Hero страницы услуги | Shared hero fields (meta keys unchanged) |
| `group_fp02_service_section_parity` | Service — Раздел (…) | Blocks 1–14 for type Раздел only (mid-cta admin removed FIX03) |

Desired admin order on `#73`: Layout (0) → Hero (1) → Раздел parity (2).

### Direct-edit vs automated blocks

| Class | Meaning | Section page admin role |
|-------|---------|-------------------------|
| **Direct editable** | Values on this service post ACF | Nature text blocks + cards, approach, program intros, dependencies chrome, FAQ heading, stages items + chrome |
| **Automated / external** | CPT children, specialists, Comfort/Reviews/Final Form | Visibility toggle + source notice |
| **Section media** | Clinic landscape + team + corridor images | `section_clinic_landscape_image`, `section_team_image`, `section_corridor_image` (FIX04/FIX05) |
| **Shared static** | Founder quote template copy | Toggle + notice |
| **Shared hero** | Hero group | Edit in **Hero страницы услуги** |
| **Existing structured** | Structured Sections `stages` / programme_items + FAQ | Kept as complementary / fallback |

### Visibility toggles (default ON)

Missing meta = enabled. Explicit `0` hides the block. Helper: `shpigovsky_section_block_enabled()`.

### Per-page values

- `#73`: seeded including FIX02/FIX03 program intros repeater; FIX04 landscape `#1239`; FIX05 team `#1238` / corridor `#1709` + empty text/repeaters from FE demo; operator test strings preserved.
- `#77` / `#84`: FIX05 seeded empty section fields with shared demo (same visual fallbacks that previously drove FE); landscape `#1239`; team `#1238`; corridor `#1709`.

### Explicitly out of this model

- Full admin parity for `Услуга` / `service_general`
- Home product changes (frozen E42)
- Services hub redesign (frozen E44)
