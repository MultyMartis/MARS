# FP-0002 V8 — Shared Include Registry v1

**Date:** 2026-06-28  
**Scope:** Read-only audit after CF-003 completion  
**Pages checked:** Home, Services Hub, Service Subdivision, Service Leaf  
**JSON:** `data/shared-include-registry-v1.json`

---

## Summary

| Metric | Count |
|--------|------:|
| Total candidate families | 13 |
| Universalized (complete) | 6 (CF-003, CF-004, CF-005, CF-006, CF-007, CF-014) |
| Shared but page-named | 4 |
| Duplicated shared family | 2 |
| Genuinely page-specific | 1 |
| Hold / unresolved | 1 |

---

## Registry

| ID | Current name | Pages | Classification | Priority | Recommended action |
|---|---|---:|---|---|---|
| CF-003 | internal-page-nav | 3 | UNIVERSALIZED | COMPLETE | NONE |
| CF-004 | founder-quote | 5 | UNIVERSALIZED | COMPLETE | NONE |
| CF-005 | specialists | 3 | UNIVERSALIZED | COMPLETE | NONE |
| CF-006 | comfort | 5 | UNIVERSALIZED | COMPLETE | NONE |
| CF-007 | reviews | 3 | UNIVERSALIZED | COMPLETE | NONE |
| CF-008 | home-faq | 5 | SHARED_BUT_PAGE_NAMED | P1 | RENAME_AND_UNIVERSALIZE |
| CF-009 | home-final-form | 5 | SHARED_BUT_PAGE_NAMED | P1 | RENAME_AND_UNIVERSALIZE |
| CF-010 | home-clinic-landscape | 3 | SHARED_BUT_PAGE_NAMED | P2 | RENAME_AND_UNIVERSALIZE |
| CF-011 | services-program-cta-band-v2 | 3+ | DUPLICATED_SHARED_FAMILY | P1 | COLLAPSE_WRAPPERS_KEEP_BAND |
| CF-012 | services-program-v2 | 3 | DUPLICATED_SHARED_FAMILY | P1 | COLLAPSE_REDUNDANT_MODIFIERS |
| CF-013 | services-inner-hero-v2 | 3 | GENUINELY_PAGE_SPECIFIC | P2 | HOLD |
| CF-014 | header/footer/modal | 4 | UNIVERSALIZED | COMPLETE | NONE |
| CF-015 | home-gallery | 1 | HOLD | HOLD | AUDIT_WHEN_O_CENTRE_STARTS |

---

## Founder quote family (CF-004 detail)

| Item | Value |
|------|-------|
| Canonical partial | `src/partials/sections/founder-quote.html` |
| Canonical root class | `.founder-quote` |
| Pages using | `index.html`, `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html`, `uslugi.html` |
| HTML copies | 0 — single include |
| CSS copies | 1 — `.founder-quote*` block in `style.scss` |
| Accessibility label | `founder-quote-label` |
| CTA drift | None |
| Old name retired | `home-founder-quote` |
| Aliases | 0 |
| Classification | UNIVERSALIZED |
| Implementation status | COMPLETE |

---

## Dark CTA band family (CF-011 detail)

| Item | Value |
|------|-------|
| Shared component | `services-program-cta-band-v2.html` |
| Wrapper partials | `service-subdivision-first-cta-v1`, `service-subdivision-second-cta-v1`, `service-leaf-cta-01-v1` |
| Problem | Same visual band wrapped in page-specific sections with duplicated page-scoped SCSS |
| Classification | DUPLICATED_SHARED_FAMILY |

---

## Buttons

`.btn`, `.btn_dark`, `.btn--primary` — used consistently across CTAs. No separate button partial family required; button classes are already neutral.

---

## Specialists family (CF-005 detail)

| Item | Value |
|------|-------|
| Canonical partial | `src/partials/sections/specialists.html` |
| Canonical root class | `.specialists` |
| Pages using | `index.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html` |
| HTML copies | 0 — single include |
| CSS copies | 1 — `.specialists*` in `style.scss` |
| JS init | 1 — `[data-specialists-slider]` in `main.js` |
| Old name retired | `home-specialists` |
| Aliases | 0 |
| Classification | UNIVERSALIZED |
| Implementation status | COMPLETE |

---

## Comfort gallery family (CF-006 detail)

| Item | Value |
|------|-------|
| Canonical partial | `src/partials/sections/comfort.html` |
| Canonical root class | `.comfort` |
| Pages using | `index.html`, `uslugi.html`, `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html` |
| HTML copies | 0 — single include |
| CSS copies | 1 — `.comfort*` in `style.scss` |
| JS init | 1 — `[data-fancybox="comfort"]` in `main.js` |
| Old name retired | `home-comfort` |
| Aliases | 0 |
| Historical asset path | `assets/img/content/home-comfort/` — preserved |
| Classification | UNIVERSALIZED |
| Implementation status | COMPLETE |

---

## Reviews family (CF-007 detail)

| Item | Value |
|------|-------|
| Canonical partial | `src/partials/sections/reviews.html` |
| Canonical root class | `.reviews` |
| Pages using | `index.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html` |
| HTML copies | 0 — single include |
| CSS copies | 1 — `.reviews*` in `style.scss` |
| JS init | 1 — `[data-reviews-slider]` in `main.js` (`initReviews`) |
| Old name retired | `home-reviews` |
| Aliases | 0 |
| Classification | UNIVERSALIZED |
| Implementation status | COMPLETE |

---

## Next recommended wave

**CF-008 — FAQ (`home-faq`)** — NOT AUTHORIZED

Reason: multi-page reuse; accordion init in main.js — verify single init path during wave.
