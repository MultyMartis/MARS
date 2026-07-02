# FP-0002 V9 — Focus State Audit v1

**Phase:** V9-03A  
**Result:** Existing `:focus-visible` patterns preserved; motion layer does not remove outlines.

## Verified controls

- `.btn` — `outline: 2px solid var(--color-accent)`
- `.site-header__nav-link`, footer links — accent outline on focus-visible
- `.modal-consultation__close` — background + focus ring
- Accordion `button[data-accordion-button]` — native button focus
- Offcanvas open/close buttons — focusable, trap focus when open
- Form inputs — `aria-invalid` + field error; focus not suppressed
- Pagination / breadcrumbs — inherit link focus styles

## No regressions introduced

- No `outline: none` without replacement added in V9-03A block.
