# FP-0002 — Service General Admin Parity Model v1

**Status:** ACCEPTED / FROZEN (local) — V9-06E47 + **E47-FIX01** + **E47-FIX02** + **E47-FIX03** + **E47-FIX04** + **V9-06E47 freeze** + **V9-06E48 representative content rollout** + **V9-06E49 full service content rollout** + **V9-06E49 FULL SERVICE ROLLOUT FREEZE** + **V9-06E49-FIX01 restore #315** + **V9-06E49 FULL SERVICE ROLLOUT FREEZE AFTER FIX01** + **V9-06E51 placeholder layout mode restore** + **V9-06E51-FIX01** + **V9-06E51-FIX02 real admin switch** + **V9-06E51 Placeholder Mode FREEZE**  
**Date:** 2026-07-16  
**Operator acceptance:** E47-FIX04 — «Да всё гуд.» (model); E48 — «Всё супер» (representatives); E49 — full service ACF content rollout accepted; E49 freeze PARTIAL closed by **E49-FIX01** + **E49 freeze after FIX01 PASS**; E51-FIX02 — «Да, теперь всё гуд» (Placeholder Mode)  
**Freeze marker (Услуга field model):** `REPORTS/FREEZE-FP-0002-V9-06E47-SERVICE-GENERAL-ACCEPTED.md`  
**Freeze marker (Full Услуга rollout):** `REPORTS/FREEZE-FP-0002-V9-06E49-FULL-SERVICE-ROLLOUT-ACCEPTED-AFTER-FIX01.md` (canonical after FIX01; prior PARTIAL marker retained historically)  
**Freeze marker (Placeholder Mode):** `REPORTS/FREEZE-FP-0002-V9-06E51-PLACEHOLDER-MODE-ACCEPTED.md`  
**Freeze backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e47-service-general-freeze-accepted-before-next-phase-20260715-175228\`  
**E48 backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e48-representative-services-rollout-before-20260715-203048\`  
**E49 backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e49-full-service-rollout-before-20260715-212933\`  
**E49 freeze backup (PARTIAL):** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e49-full-service-rollout-freeze-accepted-before-next-phase-20260716-021704\`  
**E49-FIX01 backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e49-fix01-restore-315-service-layout-before-20260716-023509\`  
**E49 freeze after FIX01 backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e49-full-service-rollout-freeze-accepted-after-fix01-before-next-phase-20260716-025224\`  
**E51 backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e51-placeholder-layout-mode-restore-before-20260715-234500\`  
**E51-FIX01 backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e51-fix01-placeholder-manual-switch-persistence-before-20260716-001214\`  
**E51-FIX02 backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e51-fix02-real-admin-placeholder-switch-before-20260716-010437\`  
**E51 freeze backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e51-placeholder-mode-freeze-accepted-before-next-phase-20260716-013604\`  
**Base page:** `#74` Лечение алкогольной зависимости (`/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`)  
**Page type:** Услуга (`service_editor_role=service` → stack `service_general`)  
**Canonical ACF group (service blocks):** `group_fp02_service_general_parity` (68 fields after FIX01; FE order 1–18)  
**Layout group:** `group_fp02_service_layout_hero` (visible title **Макет страницы услуги**)  
**Hero group:** `group_fp02_service_hero` (title **Hero страницы услуги**) — shared for Раздел and Услуга  
**Applies to:** service pages with editor role Услуга (first-level and nested)  
**Layout note (E51 / E51-FIX01 / E51-FIX02 / E51 freeze):** editor role may also be **Заглушка** (`placeholder`) — frontend stub only; ACF content groups remain editable and are not deleted. Manual switch Заглушка↔Услуга must persist via **real wp-admin POST** (`acf[field_…]` input names; never rewrite prepared ACF `name` in `prepare_field`). E51-FIX01 WP-CLI/meta simulation was insufficient. Placeholder Mode is **frozen locally** after operator acceptance of FIX02. Test page `#78` Депрессия final freeze state = **Услуга**.  
**E49 freeze note (AFTER FIX01):** Full individual Услуга ACF rollout is **frozen locally** (canonical backup `v9-06e49-full-service-rollout-freeze-accepted-after-fix01-before-next-phase-20260716-025224`). `#315` restored to `service`/`service_general` by E49-FIX01; freeze retry: 26/26 individuals Услуга; unintended placeholders **0**. Prior PARTIAL freeze (backup `…021704`) retained as historical evidence only.

This document describes admin/frontend parity for **service general (Услуга)** pages after V9-06E47, admin UX cleanup **E47-FIX01**, ACF render fix **E47-FIX02**, signs editorial read-more **E47-FIX03**, read-more toggle **E47-FIX04**, the **accepted freeze** checkpoint, **E48** staged representative content rollout, **E49** full remaining-service ACF content rollout, **E49-FIX01** `#315` restore, and the **E49 full service rollout freeze after FIX01** (ACF SoT; no alcohol copy-paste; no field-definition redesign).  
It follows the accepted **Раздел** model (`DOCS/SERVICE-SECTION-ADMIN-PARITY-MODEL-v1.md`) and Home/Services hub parity models.  
It is **not** a production/hosting claim and **not** a change to the accepted Раздел model. Product changes to the frozen Услуга **field model** require an explicit charter.

---

## Architecture summary

### Frontend is canon

- Render order is defined by `template-parts/service/alcohol-direct-v9.php` (stack filename legacy; content is `service_general`).
- Admin ACF field order in `group_fp02_service_general_parity` follows that sequence (numbered notices **1–18**).
- Visual design preserved for alcohol leaf stack.

### Admin group separation (E47-FIX01 clean UX)

| Group | Visible title | Responsibility | Visibility when role=Услуга |
|-------|---------------|----------------|----------------------------|
| `group_fp02_service_layout_hero` | **Макет страницы услуги** | Role selector + technical hidden fields + hub/catalog flags | keep |
| `group_fp02_service_hero` | Hero страницы услуги | Shared hero fields | keep |
| `group_fp02_service_general_parity` | Услуга — блоки страницы | Blocks 1–18 for type Услуга | keep |
| `group_fp02_service_section_parity` | Service — Раздел (…) | Раздел blocks | **hidden** |
| `group_fp02_service_structured_sections` | Service — Structured Sections | Legacy / section CTA shared meta | **hidden** (definitions + meta kept) |
| `group_fp02_service_faq` | Service — FAQ | Legacy FAQ repeater | **hidden** |
| `group_fp02_service_relationships` | Service — Relationships | Legacy related override | **hidden** |

Desired admin order on `#74` / Услуга: **Макет → Hero → Услуга — блоки страницы** (exactly three ACF groups). Default WP boxes **Редакция** / **Отрывок** are hidden (E47-FIX02).

Group visibility filter: `FieldGroups::filter_service_parity_groups_by_role` on `acf/load_field_groups` (+ `acf/get_field_groups`).

### Field visibility rule (E47-FIX02)

- **Do not** put field-level `conditional_logic` on `group_fp02_service_general_parity` fields that depends on `service_editor_role`.
- Nested services (depth 2+): E51 restored a real **button_group** for `service_editor_role` (Услуга | Заглушка). The FIX03 message-field conversion is **obsolete** and must not return — it broke ACF JS conditionals and value posting.
- **E51-FIX02:** `prepare_editor_role_field` must **not** reset `$field['name']` / `$field['key']` after `acf_prepare_field()` has rewritten the input name to `acf[field_fp02_service_editor_role]`. Overwriting with the bare meta name made radios post outside `$_POST['acf']`, so wp-admin Update never persisted the selector.
- Visibility for Услуга vs Раздел remains **group-level** via the role filter above. Заглушка keeps the same content groups as Услуга (content not deleted).

For **Раздел** (`role=section`): Услуга parity remains hidden; Structured Sections stays available for shared mid-cta meta (E46-FIX03).

DB duplicate ACF group posts for Structured / FAQ / Relationships were soft-disabled (`acf-disabled`) in FIX01 — definitions not deleted.

### Mid CTA (FIX01)

- Visibility toggle: `service_general_mid_cta_visible`
- Content fields in parity with **preserved meta keys**: `cta_title`, `cta_text`, `cta_button_label`, `cta_button_target`
- Frontend resolver unchanged: `shpigovsky_get_service_cta_band()` + site phone
- No normal editor dependence on Structured Sections for Услуга pages

### Content SoT (no normal template fallback)

| Class | Meaning | Admin role |
|-------|---------|------------|
| **Direct editable** | Values on this service post ACF | Intro, bordered info, signs, approach (+ team image), program chrome, stages, FAQ, landscape, corridor, mid-cta texts |
| **Automated / external** | Specialists CPT children, Comfort, Reviews, Final Form, child service tiles | Visibility toggle + source notice |
| **Shared static** | Founder quote template copy | Toggle + notice |
| **Shared hero** | Hero group | Edit in **Hero страницы услуги** |
| **Emergency PHP** | V9 alcohol static helpers / theme assets | Safety only when ACF empty (alcohol page) |

### Service media fields

| Field | Label | Seeded on #74 |
|-------|-------|---------------|
| `service_general_team_image` | Изображение команды | `#1238` |
| `service_general_clinic_landscape_image` | Изображение территории клиники | `#1239` |
| `service_general_corridor_image` | Изображение коридора | `#1709` |

Home image metas are **not** the normal SoT for Услуга pages and were not modified.

### Repeaters

| Field | Purpose |
|-------|---------|
| `service_general_bordered_info_items` | Heading + text bands |
| `service_general_signs_items` | Signs list rows |
| `service_general_approach_cards` | Approach cards |
| `service_general_program_intro_items` | Program intro paragraphs |
| `service_general_stages_items` | Stages (title/text/enabled) |
| `service_general_stages_support_items` | Support bullets |
| `service_general_faq_items` | FAQ question + answer (paragraphs by blank line) |

### Representative pages

- **E47:** `#314`, `#78`: landscape/corridor images seeded where empty; specialists toggle seeded OFF to preserve historic no-specialists leaf layout; alcohol-specific copy **not** copied.
- **E48 staged rollout:** `#74` (control), `#314` (child tiles), `#78` (ordinary nested), `#81` (psych), `#85` (RPP). Missing `service_general_*` fields seeded with **page-title / neutral DEMO** packs (not `#74` alcohol text). Shared demo images `#1238/#1239/#1709` where empty. Automatic child tiles on `#314` preserved. Full catalog mass rollout is **out of scope** for E48.
- **E49 full remaining rollout:** 21 remaining `service_general` pages seeded with page-title / parent-section / neutral `DEMO —` packs; meaningful values preserved; controls `#74/#314/#78/#81/#85` validate-only (no mutation); sections `#73/#77/#84` untouched; child tiles on `#316` preserved; images `#1238/#1239/#1709` where empty; **no alcohol copy-paste**. Field model unchanged. Report: `REPORTS/REPORT-FP-0002-V9-06E49-full-service-rollout.md`.

### Explicitly out of this model

- Hosting preview / production
- Home product changes (frozen E42)
- Services hub redesign (frozen E44)
- Раздел redesign after accepted E46
- Redesign of frozen Услуга model without a new charter (freeze E47 complete)
- Final clinical copy (DEMO/neutral seeds require operator editorial review before production claim)

### Signs editorial FE behavior (E47-FIX03 + E47-FIX04)

- Field: `service_general_signs_editorial` («Редакционный текст после признаков»).
- Markup: `.service-leaf-signs-v1__editorial` + `.service-leaf-signs-v1__read-more` (real `<button>`).
- If text height ≤ ~5 lines: full text; button hidden.
- If taller: clamp to 5 lines; show «Читать больше» (`aria-expanded="false"`).
- Toggle (FIX04): click expands smoothly → label «Скрыть» (`aria-expanded="true"`, button stays visible); click again collapses to 5 lines → «Читать больше».
- Resize recalculates overflow; preserves expanded/collapsed when still overflowing; hides button when no longer overflowing.
- No admin field changes; no DB writes for FIX03/FIX04 waves.

### Reports

- E47: `REPORTS/REPORT-FP-0002-V9-06E47-service-general-admin-parity-alcohol.md`
- E47-FIX01: `REPORTS/REPORT-FP-0002-V9-06E47-FIX01-service-general-admin-ux-cleanup.md`
- E47-FIX02: `REPORTS/REPORT-FP-0002-V9-06E47-FIX02-service-general-acf-render.md`
- E47-FIX03: `REPORTS/REPORT-FP-0002-V9-06E47-FIX03-service-signs-readmore.md`
- E47-FIX04: `REPORTS/REPORT-FP-0002-V9-06E47-FIX04-service-signs-readmore-toggle.md`
- Freeze: `REPORTS/REPORT-FP-0002-V9-06E47-service-general-freeze.md`
- Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E47-SERVICE-GENERAL-ACCEPTED.md`
- E48 representative rollout: `REPORTS/REPORT-FP-0002-V9-06E48-representative-services-rollout.md`
- E49 full service rollout: `REPORTS/REPORT-FP-0002-V9-06E49-full-service-rollout.md`
- E49 freeze (PARTIAL): `REPORTS/REPORT-FP-0002-V9-06E49-full-service-rollout-freeze.md`
- E49-FIX01 restore #315: `REPORTS/REPORT-FP-0002-V9-06E49-FIX01-restore-315-service-layout.md`
- E49 freeze after FIX01: `REPORTS/REPORT-FP-0002-V9-06E49-full-service-rollout-freeze-after-fix01.md`
- E49 freeze after FIX01 marker: `REPORTS/FREEZE-FP-0002-V9-06E49-FULL-SERVICE-ROLLOUT-ACCEPTED-AFTER-FIX01.md`
