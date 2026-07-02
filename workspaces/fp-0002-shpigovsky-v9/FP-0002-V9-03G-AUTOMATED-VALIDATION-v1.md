# FP-0002 V9-03G Automated Validation v1

**Phase:** V9-03G  
**Date:** 2026-07-02  
**Command:** `npm run validate` (with `V9_PREVIEW_PORT=8797`)  
**Result:** **PASS**

## Summary

| Suite | Result |
|-------|--------|
| Manifest routes (31) | PASS |
| Assets | PASS |
| Links | PASS |
| Structure (H1/IDs) | PASS |
| Legal pages | PASS |
| Content hygiene | PASS |
| Forms / consent | PASS |
| Motion / preloader / modal contract | PASS |
| O-Centre G6 removal | PASS |
| Scroll-to-top (V9-03G) | PASS |
| HTTP runtime (31 routes) | PASS |

## Scroll-to-top checks (new)

- Exactly **1** `[data-scroll-to-top]` per emitted route (**31/31**)
- Semantic `<button type="button">`
- Accessible label present (`aria-label="Прокрутить страницу наверх"`)
- Shared partial exists
- JS: `initScrollToTop`, threshold `500`, reduced-motion scroll fallback
- CSS: `.scroll-to-top`, `.scroll-to-top--visible`, fixed positioning, z-index **900**
- No `transition: all` on scroll-to-top
- No translateY lift on scroll-to-top hover

## Protected contracts (unchanged)

- Modal emitted once per page
- Preloader absent (0 pages)
- G6 absent on `/o-centre/`
- Triumph modal runtime patterns present in JS/CSS
- `global-consultation-modal.html` hash unchanged: `D1FBC660C60911CFBA142B731CE219A20C4D19B961B044BFC14C1A43A14D9751`

## Dist hashes (post V9-03G build)

| Asset | SHA-256 |
|-------|---------|
| CSS | `F89FCB86A678C5FB4D4A94DB2E423095A23564B6C3BE19D7E39CF5AF0D30ABDE` |
| JS | `19518C4BF86FBDA4FD5128D67EF00CBF7A2BDC6000A571B65D75BFA6AF27DB8A` |

## Evidence copy

Also written to: `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v9\v9-03g-scroll-to-top\validation\`
