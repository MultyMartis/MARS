# REPORT — FP-0002 V9-06E15 SERVICE MINI-DESCRIPTION SOURCE + SUBDIVISION SLIDERS REGRESSION REPAIR

**Wave:** V9-06E15  
**Date:** 2026-07-07  
**Baseline:** E14 @ `2c4ba6a7` (ancestor PASS; HEAD `a9d4e501`)

## 1. Safety preflight

| Item | Value |
|---|---|
| Volume | X |
| Label | AI WS |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| Local HEAD | `a9d4e501813977ef1edb2dc7b7ce7a5fb162fa48` |
| Local short HEAD | `a9d4e501` |
| Remote HEAD | `a9d4e501813977ef1edb2dc7b7ce7a5fb162fa48` |
| Remote short HEAD | `a9d4e501` |
| Ahead | 0 |
| Behind | 0 |
| Foreign WIP | Present (unrelated; untouched) |
| Pre-existing staged files | None |
| E14 ancestor check | PASS |
| Result | **PASS** |

## 2. Authorization and scope

| Scope item | Result |
|---|---|
| Operator authorization | YES — V9-06E15 charter |
| Task mode | CORRECTIVE REPAIR + E14 operator QA follow-up |
| DB checkpoint | YES |
| DB writes | YES — `service_short_description` seed repair only (**2** writes: restore E15 probe markers on IDs 74/75) |
| Source/theme changes | YES — **3** files |
| Project plugin changes | 0 |
| Third-party plugin changes | 0 |
| ACF JSON changes | 0 |
| Runtime delivery | YES — bounded theme copy |
| ACF value writes | 2 |
| Native content writes | 0 |
| Legal text writes | 0 |
| Reviews data writes | 0 |
| Media uploads | 0 |
| Service tree writes | 0 |
| Menu writes | 0 |
| Privacy setting writes | 0 |
| Rewrite/permalink changes | 0 |
| Plugin install/update/delete | 0 |
| OCPilot writes | 0 |
| Documentation/evidence writes | YES |
| Result | **PASS** |

## 3. Baseline corrective audit

| Area | Result | Root cause | Notes |
|---|---|---|---|
| Mini-description admin source | PARTIAL (operator) / PASS (technical) | E14 seeded EXACT_V9 text identical to V9 static map; operator could not distinguish admin vs HTML. Profilakticheskiy DEMO text was visually distinct. | DB had all `service_short_description` values with ACF refs; rendering already ACF-first but `get_field` lacked post_meta fallback hardening |
| Hub grouped mode | PASS | V9 card title aliases (`Алкогольная зависимость`, `Нервная анорексия`) differ from CPT post_title — validation matcher issue only | All 14 visible cards render admin values |
| Hub flat mode | PASS | Same alias/title mapping | All 17 cards render admin values |
| Zavisimosti specialists__slider | FAIL | Swiper gated to `is_front_page()` + alcohol leaf only | DOM present; vendor missing |
| Zavisimosti reviews__slider | FAIL | Same vendor gate | DOM present; vendor missing |

Evidence: `validation/v9-06e15-service-mini-description-source-subdivision-sliders-regression-repair/baseline-corrective-audit.json`

## 4. DB checkpoint

| Item | Result | Notes |
|---|---|---|
| Checkpoint path | PASS | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e15-service-mini-description-source-subdivision-sliders-regression-repair-pre-20260707T115433Z\` |
| Full dump | PASS | `mars_wp_fp0002.sql` |
| Service rows snapshot | PASS | `service-posts-before.json` |
| Postmeta snapshot | PASS | `service-postmeta-before.json` |
| Hub query mode before | `grouped_by_parent` | Restored after flat-mode test |
| Result | **PASS** |

## 5. Repair plan

| Component | Planned repair | Safety |
|---|---|---|
| Mini-description source | Harden `shpigovsky_get_service_field` with post_meta fallback; add `shpigovsky_resolve_service_mini_description_source` | No V9 static edits |
| Mini-description seed | Re-seed only empty/E15-test-marker values via `update_field` | Preserve operator values |
| Subdivision sliders | New `inc/service-subdivision-vendors.php`; enqueue Swiper on subdivision layout | Exclude home + alcohol leaf |
| Validation | Grouped + flat hub modes; slider vendor probe; regression routes | Restore hub mode after test |

## 6. Service mini-description source repair

| Area | Before | After | Result |
|---|---|---|---|
| Grouped by parent render path | ACF via `get_field` only | ACF → post_meta → V9 → DEMO | PASS |
| Flat render path | Same | Same priority | PASS |
| Source priority | Documented ACF-first | Enforced + validation resolver | PASS |
| Fallback behavior | V9 when ACF empty | Unchanged; only when admin empty | PASS |

Changed: `inc/services-hub-helpers.php`

## 7. Service mini-description seed repair

| Service | Before | After | Source | Result |
|---|---|---|---|---|
| Лечение алкогольной зависимости (74) | E15-ADMIN-MARKER-74 | EXACT_V9 alcohol text | EXACT_V9 | PASS |
| Профилактический анализ (75) | E15-ADMIN-MARKER-75 | DEMO mini text | DEMO | PASS |
| All other published services | Preserved | Preserved | PRESERVED | PASS |

**DB writes:** 2

## 8. Subdivision sliders repair

| Slider | Before | After | Vendor/init | Result |
|---|---|---|---|---|
| specialists__slider | DOM only; no Swiper | Swiper CSS/JS loaded | `service-subdivision-vendors.php` | PASS |
| reviews__slider | DOM only; no Swiper | Swiper CSS/JS loaded | same + `v9-shell.js` init | PASS |
| Route condition | N/A | `shpigovsky_is_service_subdivision_slider_page()` | subdivision layout only | PASS |
| Home regression | PASS | PASS | `is_front_page()` gate unchanged | PASS |
| Alcohol leaf regression | PASS | PASS | excluded via `shpigovsky_is_alcohol_direct_v9_page()` | PASS |

Changed: `inc/service-subdivision-vendors.php`, `functions.php`

## 9. Runtime delivery

| File | Delivered | Result | Notes |
|---|---:|---|---|
| `inc/services-hub-helpers.php` | YES | PASS | |
| `inc/service-subdivision-vendors.php` | YES | PASS | new |
| `functions.php` | YES | PASS | require subdivision vendors |

## 10. Post-repair mini-description validation

| Mode | Cards | Pass | Result |
|---|---:|---:|---|
| Grouped by parent | 14 | 14 | PASS |
| Flat | 17 | 17 | PASS |

All visible cards with non-empty admin field render that admin value. Source attribution: `ACF_FIELD`.

## 11. Post-repair subdivision sliders validation

| Check | specialists__slider | reviews__slider | Result | Notes |
|---|---|---|---|---|
| `/uslugi/zavisimosti/` | DOM + Swiper JS/CSS | DOM + Swiper JS/CSS | PASS | HTTP 200 |

## 12. Post-repair route/regression validation

| Route/check | Result | Notes |
|---|---|---|
| Required routes HTTP 200 | PASS | 13/13 |
| `/uslugi/zavisimosti/specialistam/` | PASS | not public |
| `/o-centre/specialistam/` | PASS | canonical unaffected |
| Home / alcohol / legal / contacts / reviews | PASS | regression |

## 13. Screenshots

| Screenshot | Captured | Result |
|---|---:|---|
| runtime-uslugi-grouped-mini-descriptions-e15.png | YES | PASS |
| runtime-uslugi-flat-mini-descriptions-e15.png | YES | PASS |
| runtime-zavisimosti-specialists-slider-e15.png | YES | PASS |
| runtime-zavisimosti-reviews-slider-e15.png | YES | PASS |
| runtime-zavisimosti-full-page-e15.png | YES | PASS |
| Regression set (6) | YES | PASS |
| Admin screenshots | NO | PARTIAL |

**Total:** 11/11 captured; admin PARTIAL

## 14. Final E15 inventory

See `validation/v9-06e15-service-mini-description-source-subdivision-sliders-regression-repair/final-e15-service-mini-description-and-slider-inventory.json`

## 15. No-scope-drift

| Check | Result |
|---|---|
| DB writes limited to mini-description | PASS (2) |
| Theme changes scoped | PASS (3) |
| Third-party / legal / reviews / tree / menu | 0 |
| V9 src/dist | 0 |
| Canonical `/o-centre/specialistam/` | UNAFFECTED |
| Result | **PASS** |

## 16. Documentation changes

| File | Action | Reason |
|---|---|---|
| `reports/FP-0002-V9-06E15-...-REPORT-v1.md` | created | E15 report |
| `architecture/FP-0002-V9-06E15-*.md` | created | audit/plan/repair/inventory |
| `validation/v9-06e15-.../` | created | evidence JSON + screenshots |
| `WORDPRESS/README.md` | updated | E15 status |
| `WORDPRESS/SOURCE-AUTHORITY.md` | updated | E15 authority note |
| `FP-0002-SHPIGOVSKY/PROJECT-STATUS.md` | updated | E15 status |

## 17. Git checkpoint

Staged: E15 theme source (3), report, architecture docs, validation JSON/screenshots (no helpers/temp), status docs.

## 18. Final verdict

**PASS**

V9-06E15 Service Mini-Description Source + Subdivision Sliders Regression Repair: **COMPLETE**

Operator E14 mini-description rejection: **ADDRESSED**

All service cards use admin mini-description when filled: **PASS**

Services hub grouped mode: **PASS**

Services hub flat mode: **PASS**

Zavisimosti specialists__slider: **PASS**

Zavisimosti reviews__slider: **PASS**

Canonical /o-centre/specialistam: **UNAFFECTED**

Alcohol leaf regression: **PASS**

Home slider regression: **PASS**

Accepted pages regression: **PASS**

No-scope-drift: **PASS**

Recommended next phase: **CREATE_V9_06E16_OPERATOR_SERVICE_TREE_VISUAL_QA_TASK**

## 19. Recommended next action

**CREATE_V9_06E16_OPERATOR_SERVICE_TREE_VISUAL_QA_TASK**

## 20. Final safety statement

Target folder: `X:\AI MARS`

V9-06E15 Service Mini-Description Source + Subdivision Sliders Regression Repair performed: **YES**

DB checkpoint: **YES**

DB writes: **2**

Source/theme changes: **3**

Project plugin changes: **0**

Third-party plugin changes: **0**

ACF JSON changes: **0**

Runtime delivery: **YES**

ACF value writes: **2**

Native content writes: **0**

Legal text writes: **0**

Reviews data writes: **0**

Media uploads: **0**

Attachment creation: **0**

Service tree writes: **0**

Menu writes: **0**

Privacy setting writes: **0**

Rewrite flush performed: **NO**

OCPilot writes: **0**

Production migration performed: **NO**

Canonical /o-centre/specialistam affected: **NO**

Hero system regression: **NO**

Alcohol leaf regression: **NO**

Home slider regression: **NO**

Accepted pages regression: **NO**

V9 source changed: **NO**

V9 dist changed: **NO**

DB dump committed: **NO**

Runtime snapshot committed: **NO**

Helper/temp committed: **NO**

Secrets committed: **0**
