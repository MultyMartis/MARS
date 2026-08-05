# TARGETED LIVE ACCEPTANCE v1

Five unique markers only. Operator visual judgment still **required**.

## Fixture 1 — cart/conversion

| Field | Value |
|-------|-------|
| Marker | `PHASE_3E2_1_B_CART_CONVERSION_HUMAN` |
| Comment | падает конверсия на корзине, нужна проверка |
| Service | Audit |
| Theme | conversion_cart |
| Missing | (empty) |
| Reply | cart-ack draft ready (see CART-CONVERSION-REPLY-v1) |
| Forbidden | PASS |
| Telegram sendOk | **0** (claim Sheets quota — fail-closed) |
| Expand observed | 2 (retry wave) |
| Duplicates | 0 |

## Fixture 2 — website development

| Field | Value |
|-------|-------|
| Marker | `PHASE_3E2_1_C_WEBDEV_HUMAN` |
| Service | WebsiteDevelopment |
| Theme | need_new_website |
| Missing | функциональность |
| Reply | natural webdev questions; no internal no-site wording |
| Forbidden | PASS |
| sendOk | **0** (quota fail-closed) |

## Fixture 3 — website + SEO

| Field | Value |
|-------|-------|
| Marker | `PHASE_3E2_1_D_WEBDEV_SEO_HUMAN` |
| Service | WebsiteDevelopmentSEO |
| Theme | website_plus_seo |
| Missing | тип бизнеса, функциональность, регион продвижения |
| Reply | acknowledges both tasks; natural questions |
| Forbidden | PASS |
| sendOk | **0** (quota fail-closed) |

## Fixture 4 — damaged contact

| Field | Value |
|-------|-------|
| Marker | `PHASE_3E2_1_G_DAMAGED_CONTACT_UX` |
| ready | false |
| Missing | контакт, фокус аудита |
| warnCount | 1 |
| copy block | absent |
| sendOk | **0** (quota fail-closed) |

## Fixture 5 — probable test / no duplicate

| Field | Value |
|-------|-------|
| Marker | `PHASE_3E2_1_H_TEST_NO_DUPLICATE` |
| Suppression | yes (test badge path) |
| Poll observe (5) | extraSends=0 each |
| duplicateResends | **0** |
| Dual-card success | **not proven** under Sheets quota (sendOk=0 on claim failure) |

## Operator packet questions

For each draft above, judge as Оля:

1. Immediately understandable?
2. Sounds like a real manager?
3. Minimal editing to send?
4. Acknowledges the actual problem?
5. Useful questions?
6. Anything robotic/unnecessary?
7. Any known info re-asked?

**Do not claim Phase 3E.2 COMPLETE until operator accepts human copy and dual-card delivery is proven after Sheets recovery.**
