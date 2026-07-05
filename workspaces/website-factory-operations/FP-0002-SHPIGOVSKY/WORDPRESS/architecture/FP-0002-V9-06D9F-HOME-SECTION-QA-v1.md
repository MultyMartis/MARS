# FP-0002 V9-06D9F Home Section QA v1

**Date:** 2026-07-05  
**Task:** V9-06D9-F (read-only QA)  
**Authority:** static `fp-0002-shpigovsky-v9/dist/` vs runtime `http://shpigovsky.test/`

## Summary

| Gate | Result |
|------|--------|
| Main section count (19) | PASS |
| Section order parity | PASS (19/19) |
| Hero CTA label | PASS |
| FAQ heading/id typo | **MINOR_REPAIR_REQUIRED** |
| Duplicate `comfort-heading` id | FAIL (2 instances) |
| **Overall home section QA** | **PARTIAL** |

## Section order

Runtime `<main>` matches static V9 order exactly:

`home-recovery-intro` → `founder-quote` → `home-treatment-prevention` → `home-gallery` → `home-why-us` → `home-staff-photo` → `home-feature-grid` → `clinic-landscape` → `home-recovery-life` → `reviews` → `home-rehabilitation-requirements` → `home-rehabilitation-program` → `home-genotyping` → `comfort` → `home-videos` → `specialists` → `home-articles` → `faq` → `final-form`

## FAQ heading/id check (required)

| Check | Static V9 | Runtime D9-F | Result |
|-------|-----------|--------------|--------|
| `aria-labelledby` | `faq-heading` | `comfort-heading` | FAIL |
| Heading `id` | `faq-heading` | `comfort-heading` | FAIL |
| Heading text | Нас часто спрашивают | Комфорт, приватность, забота | FAIL |
| Classification | PASS | MINOR_REPAIR_REQUIRED | — |

**Source:** `theme/shpigovsky/template-parts/home/faq.php` lines 16–18 retain D9-D transplant placeholder tokens (`comfort-heading`, comfort copy).

D9-E repaired the same class of typo in `specialists.php` but explicitly left FAQ out of scope.

## Duplicate IDs

`id="comfort-heading"` appears twice on Home: once in `comfort.php` (correct) and once in `faq.php` (incorrect). Static V9 has one `comfort-heading` and one `faq-heading`.

## Evidence

`validation/v9-06d9f-home-footer-visual-parity-qa/home-section-qa.json`
