# FP-0002 V8 — Universalization Roadmap v1

**Date:** 2026-06-28  
**Prerequisite:** CF-003 COMPLETE  
**Status:** PLAN ONLY — no implementation in this pass

---

## Completed

| Wave | Family | Result |
|------|--------|--------|
| 1 | CF-003 internal-page-nav | COMPLETE — commit `361502bf` |
| 2 | CF-004 founder-quote | COMPLETE — commit `25f972f9` |
| 3 | CF-005 specialists | COMPLETE — commit `c6efb089` |
| 4 | CF-006 comfort | COMPLETE — commit `4737b020` |
| 5 | CF-007 reviews | COMPLETE — commit `4fe928f2` |
| 6 | CF-008 FAQ | COMPLETE — pending commit |
| CF-009 final form | COMPLETE — commit `ec5ff2c0` |
| Consolidation checkpoint CF-003–CF-009 | DOCUMENTED — page-wide DOM gate blocked (pre-existing subdivision ARIA) |

---

## Recommended sequence

| Wave | Family | Priority | Pages | Risk | Operator gate |
|------|--------|----------|------:|------|---------------|
| 3 | CF-011 dark CTA band wrappers | P1 | 3 | Medium CSS (page-scoped duplicates) | **COMPLETE** |
| 4 | CF-012 program block modifiers | P1 | 3 | Medium CSS | **COMPLETE** |
| 3 | CF-005 specialists | P1 | 3 | Low | **COMPLETE** |
| 4 | CF-006 comfort gallery | P1 | 5 | Low–medium | **COMPLETE** |
| 5 | CF-007 reviews | P1 | 3 | Medium JS (Swiper) | **COMPLETE** |
| 6 | CF-008 FAQ | P1 | 5 | Low JS (accordion) | **COMPLETE** |
| 7 | CF-009 final form | P1 | 5 | Low | **COMPLETE** |
| 10 | CF-010 clinic landscape | P2 | 3 | Low | Remove leaf modifier class — NOT AUTHORIZED |
| — | CF-013 inner hero | P2 | HOLD | Already shared on 3 templates | No wave unless Home unification requested |
| — | CF-015 home gallery | HOLD | 1 | Unknown until O-Centre | Defer |

---

## Completed wave: CF-004 Founder Quote

**Result:** COMPLETE

- Partial: `src/partials/sections/founder-quote.html`
- Root class: `.founder-quote`
- Retired: `home-founder-quote` (partial, classes, label id)
- Consumers: 5 pages
- Visual parity: PASS (before/after crop comparison)

---

## Completed wave: CF-005 Specialists

**Result:** COMPLETE

- Partial: `src/partials/sections/specialists.html`
- Root class: `.specialists`
- Retired: `home-specialists` (partial, classes)
- Consumers: 3 pages
- Visual parity: PASS (before/after crop comparison)
- Slider QA: PASS

---

## Completed wave: CF-006 Comfort gallery

**Result:** COMPLETE

- Partial: `src/partials/sections/comfort.html`
- Root class: `.comfort`
- Retired: `home-comfort` (partial, classes, fancybox group)
- Consumers: 5 pages
- Visual parity: PASS (context crops 10/10 exact)
- Gallery QA: PASS

---

## Completed wave: CF-007 Reviews

**Result:** COMPLETE

- Partial: `src/partials/sections/reviews.html`
- Root class: `.reviews`
- Retired: `home-reviews` (partial, classes, init name)
- Consumers: 3 pages
- Visual parity: PASS (crop + context 12/12 exact)
- Slider QA: PASS

---

## Completed wave: CF-008 FAQ

**Result:** COMPLETE

- Partial: `src/partials/sections/faq.html`
- Root class: `.faq`
- Retired: `home-faq` (partial, classes, component IDs)
- Consumers: 5 pages
- Visual parity: PASS (crop + context 40/40 exact)
- Accordion QA: PASS

---

## Completed wave: CF-009 Final form

**Result:** COMPLETE

- Partial: `src/partials/sections/final-form.html`
- Root class: `.final-form`
- Retired: `home-final-form` (partial, classes, component IDs)
- Consumers: 5 pages
- Visual parity: PASS (crop + context 20/20 exact)
- Form QA: PASS

---

## CF-011 Dark CTA wrappers

**Status:** COMPLETE (pending operator visual review)

Subdivision `aria-labelledby` blocker repaired. CF-012 program modifier consolidation **COMPLETE** (pending operator visual review). Next authorized family: **CF-010 — NOT AUTHORIZED**.

---

## CF-012 Program modifier consolidation

**Status:** COMPLETE (pending operator visual review)

- Canonical partial: `services-program-v2.html`
- Page-named modifiers removed; functional modifiers only
- Page-scoped duplicate CSS removed from `style.scss`
- CF-011 `program-cta-band` unchanged
- Page-wide DOM gate: PASS

---

## Next wave: CF-010 Clinic landscape

**Status:** NOT AUTHORIZED

Operator gate required before any `home-clinic-landscape` rename.

---

## Next wave: CF-009 Final form (archive)

<details>
<summary>Original CF-009 plan (superseded)</summary>

**Status:** NOT AUTHORIZED

Operator gate required before any `home-final-form` rename.

</details>

---

## CF-004 archive (plan reference)

<details>
<summary>Original CF-004 plan (superseded)</summary>

- Rename partial: `home-founder-quote.html` → `founder-quote.html` — **DONE**
- Rename root class: `.home-founder-quote` → `.founder-quote` — **DONE**
- Update includes on all five consumer pages — **DONE**
- Retire `home-founder-quote` entirely — **DONE**
- Browser QA desktop + mobile — **DONE**

</details>

---

## O-Centre position

O-Centre (`o-centre-v1.html`) is **DEFERRED**. Universalization waves 2–10 prepare shared neutral families that O-Centre should consume via includes — not re-copy.

Do not start O-Centre implementation until operator charters it separately.

---

## V7 / deployment

- V7: immutable — no changes
- Deploy ZIP: not created
- Deployment: not performed
- WordPress: not started
