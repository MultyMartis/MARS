# FP-0002 V9-06D8B Home Seed Result v1

**Date:** 2026-07-05  
**Verdict:** PARTIAL PASS

## Apply result

| Metric | Value |
|---|---|
| Fields attempted | 3 |
| Fields updated | 2 (`home_advantages`, `home_faq_items`) |
| Fields unchanged | 0 |
| Fields skipped (allowlist) | 7 |
| Errors | 1 (`home_hero_slides` — update_field false; D4 value retained) |

## Post-seed visibility

- Feature grid section: **visible** (6 advantage cards)
- FAQ section: **visible** (5 accordion items)
- Gallery: **hidden** (no media — expected)
- Hero: **visible** (D4 seed + theme fallback)
- Route smoke: **ALL_200** (7/7)

## Scope

- DB writes: HOME_ACF_ONLY on page #4
- Runtime/source writes: 0
- Options writes: 0

Evidence: `validation/v9-06d8b-home-content-seed/final-verdict.json`
