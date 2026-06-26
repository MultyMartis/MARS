# PASS 2.1 Overflow Diagnostic — AFTER

## Summary

- Total probes: 110
- Overflow detected: **0**
- REAL_LAYOUT_OVERFLOW: **0**
- Page-level horizontal scroll: **0**
- Functional smoke: `PASS-2-1-FUNCTIONAL-SMOKE.json` — pass
- Visual smoke (`capture-meta.json`): all representative pages `overflow: false` @ 1437 and 380

## Fix applied

`path-utils.js` — rewrite quoted `assets/` paths to `/assets/` for nested outputs; collapse double prefixes.

No `style.scss` changes. No global `html/body` clipping added.
