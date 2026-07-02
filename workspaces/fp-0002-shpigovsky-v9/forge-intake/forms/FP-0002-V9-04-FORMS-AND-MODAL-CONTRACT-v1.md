# FP-0002 V9-04 Forms and Modal Contract v1

**Date:** 2026-07-02

## Markup authority

`src/partials/layout/global-consultation-modal.html` + V9 `dist/` rendered output.

## Placement

- **One global modal** per page via footer/layout include — outside `.site-page-shell`
- Triggers: `data-modal-open="consultation"` with optional title/subtitle/submit/source attributes

## Runtime authority

Triumph Manipulator lifecycle adapted in `src/js/main.js` (V9-03F):
- `is-modal-scroll-locked` on html/body with `bodyScrollLockY` restore
- No `position:fixed` on body shell
- Overlay `rgba(17, 24, 39, 0.56)`
- States: open → closing → hidden
- Focus: `preventScroll` on field focus

## Visual authority

**Shpigovsky design only** — do not import Triumph branding.

## Form fields

Name, phone, consent checkbox with links to `/privacy-policy/` and `/consent-personal-data/`.

## Backend (NOT this phase)

| Strategy | Notes |
|----------|-------|
| Custom REST handler | Recommended for theme ownership |
| Form plugin | Alternative — must not override modal markup |
| WPilot-assisted | Future operations lane |

Current: `FORM_MODE=STATIC_DEMO_NO_BACKEND`
