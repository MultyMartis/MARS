# FP-0002 V9-06D9-X — Baseline Binding Audit

**Phase:** V9-06D9-X  
**Date:** 2026-07-06

## Root cause

Operator edit **Андрей, Москва** persisted to legacy `options_*` namespace (`options_reviews_items_0_review_author`) while frontend helper read `fp02-reviews_*` first (`fp02-reviews_reviews_items_0_review_author` = **Александр, Москва** stale D9-W copy).

| Context | First author | Rows |
|---|---|---|
| `option` (legacy) | Андрей, Москва | 10 |
| `fp02-reviews` (canonical) | Александр, Москва (stale) | 10 |
| Helper output | Александр, Москва | 10 |
| Home frontend | Александр, Москва | 10 slides |
| `/otzyvy/` frontend | Александр, Москва | 10 cards |

Helper reported `OPTIONS` because stale canonical context had usable rows — not static fallback.

Evidence: `validation/v9-06d9x-reviews-admin-to-frontend-binding-repair/baseline-binding-audit.json`
