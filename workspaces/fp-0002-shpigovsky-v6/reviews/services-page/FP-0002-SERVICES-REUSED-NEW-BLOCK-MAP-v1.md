# FP-0002 Services Reused/New Block Map v1

**Page:** FP-0002-PG-002 Услуги — хаб  
**Mockup authority:** Figma/PDF «Услуги хаб» + `FP-0002-BLOCK-INVENTORY-v1.md` §6 G-SERVICE  
**Task PNG names `Услуги - раздел*.png`:** NOT FOUND — block order from G-SERVICE register

| Order | Mockup block | Existing partial/component | Reuse status | Included now | Future task |
| ----: | ------------ | -------------------------- | ------------ | -----------: | ----------: |
| 1 | Header top + main nav | `partials/layout/header.html` | EXACT_REUSE | YES | — |
| 2 | Mobile menu | `partials/layout/header.html` (offcanvas) | EXACT_REUSE | YES | — |
| 3 | Breadcrumbs BLK-005 | — | NEW_UNIQUE_BLOCK | NO | Breadcrumbs partial |
| 4 | In-page anchor nav BLK-006 | — | NEW_UNIQUE_BLOCK | NO | Anchor nav partial |
| 5 | Service hero BLK-007 | `partials/sections/hero.html` | REUSE CANDIDATE — DEFERRED | NO | Parameterize service hero variant |
| 6 | Service catalog grid BLK-011 | — | NEW_UNIQUE_BLOCK | NO | Category cards task |
| 7 | «Зависимости и пристрастия» promo | — | NEW_UNIQUE_BLOCK | NO | Unique hub section |
| 8 | «Психическое здоровье» promo | — | NEW_UNIQUE_BLOCK | NO | Unique hub section |
| 9 | «Расстройства пищевого поведения» promo | — | NEW_UNIQUE_BLOCK | NO | Unique hub section |
| 10 | Feature cards BLK-014 | `home-feature-grid.html` | REUSE CANDIDATE — DEFERRED | NO | Confirm hub placement |
| 11 | Program four directions BLK-020 | `home-rehabilitation-program.html` | EXACT_REUSE | YES | — |
| 12 | Rehabilitation steps BLK-018 | `home-rehabilitation-requirements.html` | REUSE CANDIDATE — DEFERRED | NO | Hub-specific copy/layout |
| 13 | Expert opinion BLK-022 | `home-founder-quote.html` | REUSE_WITH_CONTENT_PARAMETERS | YES | `modalSource` param |
| 14 | Comfort gallery BLK-023 | `home-comfort.html` | EXACT_REUSE | YES | — |
| 15 | Specialists preview BLK-026 | `home-specialists.html` | REUSE CANDIDATE — DEFERRED | NO | Hub placement |
| 16 | Reviews preview BLK-015 | `home-reviews.html` | REUSE CANDIDATE — DEFERRED | NO | Hub placement |
| 17 | FAQ BLK-034 | `home-faq.html` | EXACT_REUSE | YES | — |
| 18 | Contact form BLK-035 | `home-final-form.html` | EXACT_REUSE | YES | — |
| 19 | Guest visit CTA BLK-019 | embedded in `home-rehabilitation-requirements` | REUSE CANDIDATE — DEFERRED | NO | Extract or hub-specific CTA |
| 20 | Footer BLK-003 | `partials/layout/footer.html` | EXACT_REUSE | YES | — |
| 21 | Modal consultation | `partials/components/modal-consultation.html` | EXACT_REUSE | YES | — |

## Foundation gaps (not rendered on page)

| After existing block | Missing unique mockup block | Future partial |
| -------------------- | --------------------------- | -------------- |
| Header | Service hero BLK-007 | `hero` service variant |
| Header | Service catalog BLK-011 | `services-category-grid` |
| Header | Dependencies / mental health / RPP promos | Unique hub sections |
| Program | Rehabilitation steps BLK-018 (if required on hub) | Optional reuse |
| Comfort | Specialists / reviews previews | Deferred shared blocks |
| Final form | Guest visit CTA BLK-019 | Dark CTA band task |

## Services foundation scroll order (implemented)

1. Header (+ mobile menu)  
2. `home-rehabilitation-program`  
3. `home-founder-quote` (`modalSource: services-founder`)  
4. `home-comfort`  
5. `home-faq`  
6. `home-final-form`  
7. Footer  
8. Modal (once)
