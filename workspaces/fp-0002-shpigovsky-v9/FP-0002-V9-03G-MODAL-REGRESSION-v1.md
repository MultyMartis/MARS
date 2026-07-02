# FP-0002 V9-03G Modal Regression v1

**Phase:** V9-03G  
**Modal authority:** V9-03F Triumph-derived runtime (protected)

## Source integrity

| File | Pre-V9-03G hash | Post-V9-03G hash | Changed |
|------|-----------------|------------------|---------|
| `global-consultation-modal.html` | `D1FBC660…` | `D1FBC660…` | **No** |
| Modal SCSS block (10b) | unchanged section | unchanged section | **No** |
| Modal JS (`bindModalSystem` region) | unchanged core | append-only `initScrollToTop` at file end | **No modal logic edits** |

## Automated regression checks

| Check | Result |
|-------|--------|
| Modal emitted once per route (31/31) | PASS |
| `lockBodyScroll` / `unlockBodyScroll` present | PASS |
| `is-modal-scroll-locked` CSS + JS | PASS |
| No rejected V9-03D/03E shell-fixed runtime | PASS |
| Scroll-to-top z-index 900 < modal 1200 | PASS |
| Preloader absent | PASS |

## Expected operator test sequence

1. Scroll below 500px — scroll-to-top appears
2. Open consultation modal from footer CTA
3. Confirm modal opens; background locked; scroll-to-top **behind** overlay
4. Close modal — background scroll position preserved
5. Scroll-to-top still in correct visible state
6. Click scroll-to-top — smooth return to top
7. Open modal near top — modal behavior unchanged

## Desktop + mobile

Repeat sequence at desktop width and ~380px mobile viewport.

**Operator visual confirmation:** pending on http://127.0.0.1:8797/
