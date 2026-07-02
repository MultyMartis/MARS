# FP-0002 V9-03E — Modal Root Cause Decision v1

**Phase:** V9-03E  
**Date:** 2026-07-02

## Symptom
Opening consultation modal from deep scroll depth caused visible page movement; V9-03D body-fixed lock also made overlay appear to cover wrong content (non-semitransparent / top-of-page bleed).

## Primary root cause
Applying scroll lock via `overflow: hidden` on `body` resets document `scrollY` to `0` while page content remains visually offset — perceived jump to top. V9-03D body `position: fixed; top: -scrollY` preserved coordinates but caused visible restore jump and overlay regression per operator.

## Contributing causes
- Focus on modal open without `{ preventScroll: true }` (V9-03C baseline)
- Preloader/page-shell opacity fade created extra stacking context (removed in V9-03E)
- Automated harness sometimes measured before close animation finished (documented separately)

## Rejected hypotheses
- Modal overlay CSS alpha wrong (approved `rgba(17, 24, 39, 0.56)` unchanged)
- `#` href on modal triggers (all triggers are `type="button"`)
- Global body-fixed lock (operator rejected V9-03D)

## Selected fix (V9-03E)
1. **Shell-scoped fixed lock:** freeze `.site-page-shell` at `top: -scrollY` while modal open; modal remains outside shell.
2. **Body overflow lock:** `body.is-modal-scroll-locked { overflow: hidden }` only — no body `position: fixed`.
3. **Restore:** unfix shell → `scrollTo(savedY)` → remove overflow class (double rAF).
4. **Focus:** `focusWithoutScroll()` with `{ preventScroll: true }` on open/close.
5. **Triggers:** synchronous `preventDefault` + `stopPropagation`.

## Rollback point
V9-03C authority ZIP + V9-03D failed-state backup in Storage.
