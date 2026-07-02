# FP-0002 V9-03F Modal Migration Plan v1

## Principle

**TRIUMPH MODAL TECHNOLOGY + SHPIGOVSKY MODAL DESIGN**

## Triumph authority files (read-only)

- `triumph-manipulator-landing-v6/src/js/modal.js`
- `triumph-manipulator-landing-v6/src/scss/components/_modal.scss` (behavior reference only — **not copied visually**)

## Removed failed FP-0002 runtime

- `lockPageScroll` / `unlockPageScroll` page-shell `position: fixed` + negative `top`
- `pageShellEl`, `pageScrollLockY` shell freezing
- `focusWithoutScroll` scroll restoration loops
- `body[data-modal-state]` overflow duplication

## Adapted Triumph lifecycle in FP-0002

| Concern | Implementation |
|---------|----------------|
| Trigger | `[data-modal-open="consultation"]` + capture `bodyScrollLockY` at click |
| Open | `lockBodyScroll()` → show modal → `data-modal-state="open"` → focus with `preventScroll` |
| Scroll lock | `html/body.is-modal-scroll-locked { height:auto; min-height:100%; overflow:hidden; touch-action:none }` |
| Close | `data-modal-state="closing"` → unlock + `scrollTo` saved Y → transition → `[hidden]` |
| Focus | Triumph timing + `preventScroll` on open/close focus |
| DOM | Modal moved **outside** `.site-page-shell` via `global-consultation-modal.html` |

## Intentional FP-0002 adaptations (not Triumph visual)

1. **html+body lock** — FP-0002 scroll container uses `html` (`height:100%` baseline).
2. **`height:auto` during lock** — prevents overflow lock from zeroing scroll (Triumph does not need this).
3. **`bodyScrollLockY` + unlock `scrollTo`** — restores position when `height:100%` returns after unlock.
4. **Shpigovsky** `data-modal-state` animation instead of Triumph `site-modal--open` class names.
5. **Lead form** stack retained (`data-lead-form`).

## Preserved Shpigovsky design

- `modal-consultation.html` markup/content unchanged
- Overlay `rgba(17, 24, 39, 0.56)`
- All field layout, typography, button, close control, motion tokens

## Files modified

- `src/js/main.js` — modal runtime block
- `src/scss/style.scss` — scroll lock + dialog overscroll
- `src/partials/layout/global-consultation-modal.html` — **new**
- `src/pages/**/*.html` — modal include path (31 pages)
- `tools/v9-validate-all.mjs` — V9-03F contract checks

## Rollback

Use `FP-0002-V9-03E-PRE-TRIUMPH-MODAL-MIGRATION-BACKUP-MANIFEST.md`

## Explicit non-goals

- No Triumph branding/visual CSS
- No preloader restoration
- No route/content changes
- No git checkpoint in this phase
