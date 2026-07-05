# FP-0002 V9-06D9-0 Lightweight vs Broken Classification v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9-0-full-visual-port-charter/lightweight-vs-broken-classification.json`

## Interpretation

WordPress runtime reflects a **deliberately lightweight MVP skeleton/content seed phase** (D7-B scope + D8 seeds). Gaps are now **authorized full-port scope**, not evidence of accidental collapse.

## Classification table

| Mismatch | Class | Error or deferred | Required action |
|----------|-------|-------------------|-----------------|
| 12 home sections not ported | INTENTIONAL_LIGHTWEIGHT_DEFERRED | deferred | D9-D template transfer |
| D7-B 8-section wave scope | INTENTIONAL_LIGHTWEIGHT_DEFERRED | deferred | D9-D full orchestration |
| Gallery/articles hidden when empty | INTENTIONAL_LIGHTWEIGHT_DEFERRED | deferred | D9-E seed |
| social_links not seeded | INTENTIONAL_LIGHTWEIGHT_DEFERRED | deferred | D9-B V9 `#` fallback or operator URLs |
| Inter font `/assets/` 404 | **BROKEN_ASSET_PATH** | **broken** | D9-B CSS path rewrite |
| Hero image absent | ACF_NOT_SEEDED | deferred | D9-C media + seed |
| Swiper/Fancybox missing | VENDOR_ASSET_NOT_ENQUEUED | broken | D9-B/D9-F enqueue |
| WP menu ≠ V9 nav | WP_MENU_DATA_MISSING | deferred | D9-B menu alignment |
| Messenger icons absent | HEADER_STRUCTURE_NOT_PORTED | deferred | D9-B source fallback |
| Services hub sparse | INTENTIONAL_LIGHTWEIGHT_DEFERRED | deferred | D9-G |
| Service leaf missing blocks | MISSING_TEMPLATE_PORT | deferred | D9-G |
| Contacts map/messengers | OPERATOR_DATA_REQUIRED | deferred | Operator URLs or `#` fallback |
| FAQ / Service 74 copy | CONTENT_REVIEW_REQUIRED | deferred | Post-parity operator review |

## Broken vs deferred summary

| Category | Count | Waves |
|----------|------:|-------|
| Broken (must fix for any parity) | 2 | D9-B (fonts, vendor foundation) |
| Intentional deferred | 8 | D9-C through D9-G |
| Operator/review | 3 | After visual parity |

## Result

Classification complete. Full visual port authorized.
