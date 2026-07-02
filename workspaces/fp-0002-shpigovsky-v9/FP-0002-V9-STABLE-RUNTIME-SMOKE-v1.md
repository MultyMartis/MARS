# FP-0002 V9 Stable Runtime Smoke v1

**Phase:** V9-03 stable baseline checkpoint  
**Date:** 2026-07-02  
**Server:** `node tools/v9-preview-server.mjs` @ `http://127.0.0.1:8898/`

## Result

**PASS** — 31/31 routes HTTP 200

## Global assets

| Asset | HTTP |
|-------|------|
| `/assets/css/style.css` | 200 |
| `/assets/js/main.js` | 200 |

## Per-route invariants (all 31 routes)

| Check | Result |
|-------|--------|
| HTTP 200 | PASS |
| Exactly 1 H1 | PASS |
| Exactly 1 `data-modal="consultation"` | PASS |
| Exactly 1 `data-scroll-to-top` | PASS |
| No preloader markup | PASS |
| No `data-inf-group="g6"` | PASS |

## Representative routes exercised

- `/` — home (modal triggers, scroll-to-top)
- `/o-centre/` — G6 absence confirmed
- `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` — full service leaf
- `/blog/nazvanie-stati/` — blog article
- `/kontakty/` — contacts

## Evidence

JSON results: `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v9\v9-03-stable-baseline-checkpoint\validation\runtime-smoke-results.json`

## Note

Interactive modal/gallery/mobile menu behavior validated in prior V9-03F/03G operator-approved phases; this smoke confirms static HTTP contract and invariant DOM counts on clean `dist`.
