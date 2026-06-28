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
| Universalized (complete) | 9 (CF-003, CF-004, CF-005, CF-006, CF-007, CF-008, CF-009, CF-011, CF-012) |
| Shared but page-named | 2 |
| Duplicated shared family | 1 |
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
| CF-008 | faq | 5 | UNIVERSALIZED | COMPLETE | NONE |
| CF-009 | final-form | 5 | UNIVERSALIZED | COMPLETE | NONE |
| CF-010 | home-clinic-landscape | 3 | SHARED_BUT_PAGE_NAMED | P2 | RENAME_AND_UNIVERSALIZE |
| CF-011 | program-cta-band | 3+ | UNIVERSALIZED | COMPLETE | NONE |
| CF-012 | services-program-v2 | 3 | UNIVERSALIZED | COMPLETE | NONE |
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
| Canonical component | `program-cta-band.html` |
| Root class | `.program-cta-band` |
| Retired component | `services-program-cta-band-v2.html` |
| Removed wrappers | `service-subdivision-first-cta-v1`, `service-subdivision-second-cta-v1`, `service-leaf-cta-01-v1` |
| Subdivision ARIA blocker | REPAIRED (`service-subdivision-start-heading`) |
| Page-wide DOM gate | PASS |
| Problem | Same visual band wrapped in page-specific sections with duplicated page-scoped SCSS |
| Classification | UNIVERSALIZED |
| Implementation status | COMPLETE |

---

## Program block family (CF-012 detail)

| Item | Value |
|------|-------|
| Canonical partial | `src/partials/sections/services-program-v2.html` |
| Canonical root class | `.services-program-v2` |
| Consumers | `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html` |
| Functional modifiers | `--media-frame-fixed`, `--item-image-stack-tall`, `--item-body-mobile-pad`, `--item-media-mobile-pad`, `--play-link`, `--intro-stacked`, `--grid-compact`, `--media-contain`, `--title-block`, `--title-flush`, `--item-body-spaced`, `--item-image-mobile-short` |
| Retired modifiers | `services-program-v2--subdivision`, `service-subdivision-program-v1`, `service-leaf-program-v1` |
| Page-scoped program CSS | 0 |
| Duplicate partials removed | 0 (single canonical partial retained) |
| CF-011 protection | PASS |
| Page-wide DOM gate | PASS |
| Classification | UNIVERSALIZED |
| Implementation status | COMPLETE |

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

## FAQ family (CF-008 detail)

| Item | Value |
|------|-------|
| Canonical partial | `src/partials/sections/faq.html` |
| Canonical root class | `.faq` |
| Pages using | `index.html`, `uslugi.html`, `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html` |
| HTML copies | 0 — single include |
| CSS copies | 1 — `.faq*` in `style.scss` |
| JS init | 1 — global `[data-accordion]` in `main.js` |
| Old name retired | `home-faq` |
| Aliases | 0 |
| Classification | UNIVERSALIZED |
| Implementation status | COMPLETE |

---

## Final form family (CF-009 detail)

| Item | Value |
|------|-------|
| Canonical partial | `src/partials/sections/final-form.html` |
| Canonical root class | `.final-form` |
| Pages using | `index.html`, `uslugi.html`, `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html` |
| HTML copies | 0 — single include |
| CSS copies | 1 — `.final-form*` in `style.scss` |
| JS init | 1 — global `[data-lead-form]` in `main.js` |
| Old name retired | `home-final-form` |
| Aliases | 0 |
| Classification | UNIVERSALIZED |
| Implementation status | COMPLETE |

---

## Next recommended wave

**CF-010 — Clinic landscape (`home-clinic-landscape`)** — NOT AUTHORIZED

Reason: shared on 3 templates; page-specific name; operator gate required before wave 10.
