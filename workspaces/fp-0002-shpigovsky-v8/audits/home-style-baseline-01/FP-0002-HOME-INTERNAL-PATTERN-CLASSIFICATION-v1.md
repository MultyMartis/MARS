# FP-0002 — Home Internal Pattern Classification v1

**Audit ID:** `home-style-baseline-01`  
**Authority:** `f5a9ecd7`  
**Date:** 2026-06-26

---

## Classification key

| Status | Meaning |
|--------|---------|
| KEEP_HOME_SCOPED | Leave selector and scope unchanged |
| SAFE_TO_ALIAS | Add parallel universal class later without breaking Home |
| EXTRACT_LATER | Good universal candidate; defer until second page block built |
| ALREADY_EFFECTIVELY_GLOBAL | Used across sections/pages despite `home-` prefix |
| DO_NOT_REUSE | Too coupled or incorrect markup |

---

## Internal pattern table

| Existing selector | Visual role | Repeated evidence | Classification | Proposed universal role | Extraction timing |
| ----------------- | ----------- | ----------------- | -------------- | ----------------------- | ----------------- |
| `.home-treatment-prevention__lead` | Accent-bar uppercase lead | Also mirrored in program/comfort/genotyping `__lead`, `.rehub-universal-decor` | EXTRACT_LATER | `section-lead` / decor alias | Services General build |
| `.home-treatment-prevention__services` | — (not in source) | N/A | DO_NOT_REUSE | — | — |
| `.home-treatment-prevention__service` | Dotted leader link row | Used inside `.home-why-us` | ALREADY_EFFECTIVELY_GLOBAL | Service link row | Document only; alias optional |
| `.home-treatment-prevention__service-item` | Grid link row 3-col | Treatment + Why us | ALREADY_EFFECTIVELY_GLOBAL | Link row pattern | After Services hub |
| `.home-treatment-prevention__accordion` | FAQ-style accordion | Same JS as FAQ | EXTRACT_LATER | Accordion container | Phase 2 Services |
| `.home-feature-grid__card-grid` | 3-col outline grid | Same as recovery-intro card grid | EXTRACT_LATER | `card-grid--3` | If Services mock confirms |
| `.home-feature-grid__card` | Outline card | Intro cards, reviews cards share border language | EXTRACT_LATER | `card--outlined` | After 2nd use on Services |
| `.home-recovery-intro__benefits` | Accent dot list | Genotyping/support lists same dot | EXTRACT_LATER | `list--accent-dot` | Low priority |
| `.home-recovery-intro__card-grid` | 3-col grid | Duplicate geometry to feature-grid | EXTRACT_LATER | Shared grid | With feature-grid |
| `.home-recovery-intro__card` | Icon+title+text card | Unique icon wrapper markup | KEEP_HOME_SCOPED | — | — |
| `.home-why-us__grid` | — (not defined) | `.home-why-us__card-grid` only sets margin-top | KEEP_HOME_SCOPED | — | — |
| `.home-reviews__slider` | Swiper root | Gallery, specialists parallel | EXTRACT_LATER | Slider shell | When 3+ sliders on one page |
| `.home-reviews__card` | Bordered review card | Shares Family A card | SAFE_TO_ALIAS | Card variant | Services if reviews block added |
| `.home-specialists__slider` | Swiper root | Shared pagination CSS | EXTRACT_LATER | Slider shell | With reviews |
| `.home-gallery__slider` | Swiper root | Shared pagination CSS | EXTRACT_LATER | Slider shell | — |
| `.home-videos__grid` | 2-col media grid | Comfort gallery 3-col related | EXTRACT_LATER | Media grid | If Services has video row |
| `.home-faq__list` | FAQ stack | Treatment accordion list differs | KEEP_HOME_SCOPED | — | — |
| `.home-rehabilitation-program__head` | H2 + all link row | 5 sections share grouped head rules | ALREADY_EFFECTIVELY_GLOBAL | Section head | Services — copy pattern first |
| `.home-rehabilitation-program__all-link` | Uppercase “all” CTA | 5+ sections | ALREADY_EFFECTIVELY_GLOBAL | Section all-link | Strategy A alias |
| `.home-rehabilitation-program__direction` | Horizontal direction card | Program-specific layout | KEEP_HOME_SCOPED | — | Reuse via partial |
| `.home-rehabilitation-requirements__cta-band` | Dark 3-col CTA | Final form band shares visual | EXTRACT_LATER | `band--dark-cta` | Later |
| `.home-final-form__band` | Dark 2-col form band | Live on Services | ALREADY_EFFECTIVELY_GLOBAL | Footer CTA band | Keep class name |
| `.home-final-form__row` | 2-col form fields | Modal shares field logic | ALREADY_EFFECTIVELY_GLOBAL | Form row | Keep |
| `.block-whith-red-line` | Uppercase accent lead | Requirements block | SAFE_TO_ALIAS | Typo preserved — alias later | Operator approval |
| `.rehub-universal-decor` | Lead accent bar | Operator-started universal | SAFE_TO_ALIAS | Universal lead | Use on Services first |
| `.home-reviews__pagination` (+ gallery, specialists) | Slider dots | Triple-grouped in SCSS | ALREADY_EFFECTIVELY_GLOBAL | Pagination bullets | Do not split yet |
| `.btn.btn_dark.btn--primary` | Primary CTA | Hero, bands, modal triggers | ALREADY_EFFECTIVELY_GLOBAL | Button system | None |
| `.home-founder-quote__layout` | 2-col quote+photo | Variant A/B differ | KEEP_HOME_SCOPED | — | Partial params |
| `.home-comfort__gallery` | 3-col Fancybox grid | Services reuses whole | KEEP_HOME_SCOPED | — | Partial reuse |
| `.home-articles__card` | Image+meta+title | Distinct from outline cards | KEEP_HOME_SCOPED | — | Blog only |
| `.UNIVERSAL-requirements__support` | Support box duplicate | Experimental mirror | DO_NOT_REUSE | Remove only with operator | — |

---

## Cross-section coupling (documented)

**`.home-why-us` → `.home-treatment-prevention__*`:** Why-us section embeds treatment service-list markup without accordion wrapper. Styles come from treatment block. **Do not extract without fixing HTML coupling.**

---

## Strategy summary

| Pattern group | Strategy |
|---------------|----------|
| Section head + all link | **A** — optional alias class on existing element |
| Lead accent bar | **A** — promote `.rehub-universal-decor` |
| Outline card / grid | **C** — shared SCSS block, keep BEM roots |
| Whole sections on Services | **B** — parameterized includes (proven) |
| Hero | **D** — separate inner hero partial |
| Accordion lists | **C** — shared JS; keep section-specific roots |

---

*End of internal pattern classification v1.*
