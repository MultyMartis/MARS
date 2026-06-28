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
| Universalized (complete) | 2 (CF-003, CF-014) |
| Shared but page-named | 8 |
| Duplicated shared family | 2 |
| Genuinely page-specific | 1 |
| Hold / unresolved | 1 |

---

## Registry

| ID | Current name | Pages | Classification | Priority | Recommended action |
|---|---|---:|---|---|---|
| CF-003 | internal-page-nav | 3 | UNIVERSALIZED | COMPLETE | NONE |
| CF-004 | home-founder-quote | 5 | SHARED_BUT_PAGE_NAMED | P1 | RENAME_AND_UNIVERSALIZE |
| CF-005 | home-specialists | 3 | SHARED_BUT_PAGE_NAMED | P1 | RENAME_AND_UNIVERSALIZE |
| CF-006 | home-comfort | 5 | SHARED_BUT_PAGE_NAMED | P1 | RENAME_AND_UNIVERSALIZE |
| CF-007 | home-reviews | 3 | SHARED_BUT_PAGE_NAMED | P1 | RENAME_AND_UNIVERSALIZE |
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
| Current partial | `src/partials/sections/home-founder-quote.html` |
| Current root class | `.home-founder-quote` |
| Pages using | `index.html`, `uslugi-v2.html`, `usluga-podrazdel-v1.html`, `usluga-konechnaya-v1.html`, `uslugi.html` |
| HTML copies | 0 — single include |
| CSS copies | 1 — `.home-founder-quote*` block in `style.scss` |
| Accessibility drift | Low — `aria-labelledby="home-founder-quote-label"` is page-neutral but name is not |
| CTA drift | None |
| Classification | SHARED_BUT_PAGE_NAMED |
| Implementation status | NOT_STARTED |

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

## Next recommended wave

**CF-004 — Founder/Expert quote (`home-founder-quote`)**

Reason: multi-page reuse, page-specific naming only, no complex JS, direct benefit for future O-Centre page.
