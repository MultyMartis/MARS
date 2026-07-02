# FP-0002 V9 — Preloader Behavior v1

**Phase:** V9-03A

## First load (fresh session)

1. Head inline script adds `js-enabled`; if `sessionStorage.fp0002_preloader_session` absent → `is-preloader-active`.
2. Preloader overlay visible with logo + progress line.
3. Fake progress runs until `window.load` (unless reduced motion).
4. Minimum display ~300 ms, then fade ~450 ms.
5. `sessionStorage` set to `1`.

## Repeat navigation (same session)

- Head script does not add `is-preloader-active`.
- `initPreloader()` calls `hidePreloader()` immediately.
- No intrusive loader on internal static navigation.

## Hard fail-safe

- `3000 ms` timeout always clears overlay and marks session.

## BFCache

- `pageshow` with `persisted` → immediate hide.

## No-JS

- `<noscript>` style hides `.site-preloader` and restores overflow.

## Storage unavailable

- try/catch: preloader may show on each load; fail-safe still clears.

## Reduced motion

- Fake progress skipped; minimum wait 0; CSS transitions disabled.
