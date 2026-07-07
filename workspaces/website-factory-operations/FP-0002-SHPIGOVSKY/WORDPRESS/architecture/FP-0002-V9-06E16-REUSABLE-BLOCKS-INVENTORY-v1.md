# FP-0002 V9-06E16 — Reusable Blocks Inventory

**Evidence:** `validation/v9-06e16-operator-qa-closure-reusable-blocks-clone-cleanup-audit/reusable-blocks-inventory.json`

## Summary

14 block patterns inventoried across home, services hub, subdivision/leaf stacks, alcohol direct V9, contacts, reviews, legal shell, header, and footer.

## Priority 1 (global, high operator value)

| Block ID | Routes | Editable today | Proposed admin |
|----------|--------|----------------|----------------|
| rb-final-form | Most stacks | PARTIAL | Повторяемые блоки → Финальная форма |
| rb-specialists-slider | Home, subdivisions | NO | Повторяемые блоки → Специалисты |
| rb-reviews-slider | Home, zavisimosti, /otzyvy/ | YES | Повторяемые блоки → Отзывы |

## Priority 2–3

Header/footer chrome (PARTIAL), consultation modal, program-cta-band, comfort gallery, hero fallbacks.

## Page-local (not global reusable)

- Service cards (`service_short_description` on CPT)
- Legal document content per page
- Home hero repeaters (front page ACF)

## Key finding

Specialists and comfort blocks are **hardcoded** in theme PHP with V9 asset paths; only reviews block has full options admin today (`fp02-reviews`).
