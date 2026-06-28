# FP-0002 V8 — Component Family Registry v1

**Status:** READ-ONLY bootstrap registry (no renames applied)  
**Authority:** V8 bootstrap @ `fp-0002-v7-four-template-canonical-demo-baseline-01`  
**Date:** 2026-06-28

Registry of visually recurring families across the four canonical templates. Each row lists **current** V7-derived class/partial names — consolidation targets are proposed, not applied.

---

## CF-001 — Site chrome

| Field | Value |
| ----- | ----- |
| Visual role | Header, footer, head meta, consultation modal |
| Shared partials | `partials/layout/head.html`, `header.html`, `footer.html`, `partials/components/modal-consultation.html` |
| Class family | `.site-header*`, `.site-footer*`, `.modal-consultation*` |
| Pages | All four templates |
| Duplication | Low — single layout partials |
| Consolidation priority | P3 — stable |

---

## CF-002 — Inner hero band

| Field | Value |
| ----- | ----- |
| Visual role | Full-width inner page hero with image, overlay, eyebrow, H1, lead, CTA |
| Shared partial | `partials/sections/services-inner-hero-v2.html` |
| Class family | `.services-inner-hero-v2*` |
| Pages | `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html` |
| Page-scoped overrides | `.page-service-subdivision-v1 .services-inner-hero-v2__container`, `.page-service-leaf-v1 .services-inner-hero-v2__container` (container width/padding) |
| Duplication | Medium — shared partial, page-root CSS overrides |
| Consolidation priority | P2 |

---

## CF-003 — Upper page nav band (breadcrumbs + local subnav)

| Field | Value |
| ----- | ----- |
| Visual role | Breadcrumbs + pill subnav inside `.container` below hero |
| Shared partials | `partials/components/breadcrumbs.html`, `services-page-subnav.html` |
| **Page-specific wrappers (DRIFT)** | `.page-uslugi-v2__upper-nav`, `.page-service-subdivision-v1__upper-nav`, `.page-service-leaf-v1__upper-nav` |
| Wrapper CSS drift | uslugi-v2 + subdivision: `gap:15px; padding:0` — leaf: `gap:12px; padding-top:16px; padding-bottom:8px` |
| Nested CSS duplication | Subdivision + leaf re-declare `.breadcrumbs__*` and `.services-page-subnav__*` under page roots; leaf uses 12px breadcrumb type vs 14px on subdivision |
| Pages | All three internal service templates |
| Consolidation priority | **P1 — primary drift example** |
| Target (future) | One partial e.g. `partials/components/page-upper-nav.html` + one class family e.g. `.page-upper-nav*` |

---

## CF-004 — Category / services list section

| Field | Value |
| ----- | ----- |
| Visual role | Numbered category block with services list and optional gallery |
| Shared partial | `partials/sections/services-category-section-v2.html` |
| Class family | `.services-category-section-v2*` |
| Pages | `uslugi-v2.html`, `usluga-podrazdel-v1.html` |
| Page modifiers | `.service-subdivision-dependencies-v1`, `.services-category-section-v2--*` |
| Consolidation priority | P2 |

---

## CF-005 — Program block (4 directions)

| Field | Value |
| ----- | ----- |
| Visual role | Four program cards + optional guest CTA band |
| Shared partials | `services-program-v2.html`, `services-program-cta-band-v2.html` |
| Class family | `.services-program-v2*` |
| Pages | All four templates (home uses `home-rehabilitation-program.html` — parallel family) |
| Page modifiers | `.services-program-v2--subdivision`, `.service-subdivision-program-v1`, `.service-leaf-program-v1` |
| Duplication | High — same visual system, multiple modifier stacks |
| Consolidation priority | P1 |

---

## CF-006 — Founder quote

| Field | Value |
| ----- | ----- |
| Shared partial | `partials/sections/home-founder-quote.html` |
| Class family | `.home-founder-quote*` (+ `--variant-b`) |
| Pages | `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html` |
| Consolidation priority | P2 — rename to neutral family deferred |

---

## CF-007 — Comfort gallery

| Field | Value |
| ----- | ----- |
| Shared partial | `partials/sections/home-comfort.html` |
| Class family | `.home-comfort*` |
| Pages | All three internal service templates |
| Consolidation priority | P2 |

---

## CF-008 — FAQ accordion

| Field | Value |
| ----- | ----- |
| Shared partial | `partials/sections/home-faq.html` |
| Class family | `.home-faq*` |
| Pages | All three internal service templates |
| Consolidation priority | P2 |

---

## CF-009 — Final lead form

| Field | Value |
| ----- | ----- |
| Shared partial | `partials/sections/home-final-form.html` |
| Class family | `.home-final-form*` |
| Pages | All four templates |
| Consolidation priority | P2 |

---

## CF-010 — Reviews slider

| Field | Value |
| ----- | ----- |
| Shared partial | `partials/sections/home-reviews.html` |
| Class family | `.home-reviews*` |
| Pages | `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html` |
| Consolidation priority | P3 |

---

## CF-011 — Specialists slider

| Field | Value |
| ----- | ----- |
| Shared partial | `partials/sections/home-specialists.html` |
| Class family | `.home-specialists*` |
| Pages | Subdivision + leaf |
| Consolidation priority | P3 |

---

## CF-012 — Clinic landscape bleed

| Field | Value |
| ----- | ----- |
| Shared partial | `partials/sections/home-clinic-landscape.html` |
| Class family | `.home-clinic-landscape*` |
| Pages | Subdivision + leaf |
| Consolidation priority | P3 |

---

## CF-013 — Home-only blocks (reference)

Blocks on `index.html` without equivalents on service templates: `hero.html`, `home-recovery-intro`, `home-treatment-prevention`, `home-gallery`, `home-why-us`, `home-recovery-life`, etc.

**Consolidation note:** Do not merge with service templates until a new page genuinely reuses the visual.

---

## Summary counts

| Metric | Value |
| ------ | ----- |
| Shared partial families (cross-template) | 12 |
| P1 consolidation targets | CF-003, CF-005 |
| Page-specific upper-nav wrappers | 3 |
| `home-*` prefixed blocks reused on service pages | 7 |
