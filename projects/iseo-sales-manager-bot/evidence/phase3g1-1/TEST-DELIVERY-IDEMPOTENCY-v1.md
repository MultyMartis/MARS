# TEST DELIVERY IDEMPOTENCY — Phase 3G.1.1

**Acceptance set:** T1 + T3 template fixtures (2 business fixtures)

## Delivery counters

| Counter | Value |
|---------|------:|
| test business fixtures | 2 (T1 + T3) |
| recipient drafts | 4 |
| Telegram successes | 4 |
| duplicate sends (acceptance set) | 0 |
| duplicate sends after 3 later polls | 0 |
| revoked-user sends | 0 |
| AI provider calls | 0 |
| workflows created | 0 |
| access-role changes | 0 |

## Storage mirrors

| Store | Rows appended |
|-------|--------------:|
| TEST_LEADS (sanitized mirror) | 2 |
| production LEADS (business acceptance) | 0 |

Production LEADS exclusion: `exclude_from_prod_stats` + synthetic acceptance markers — no production stats inflation claimed.

## Idempotency method

- Exactly-once claim → send → stamp path preserved from Phase 3E.2.3
- Three post-delivery polls observed zero additional sends on acceptance fixture keys
- Revoked labels (MOD_B_REVOKED, MOD_C_REVOKED) received zero delivery attempts

## Ops patch note

Narrow Operational.dev patch: `classifyProbableTest` early-return for marker `PHASE_3G11_TEMPLATE_ACCEPTANCE_HUMAN` so acceptance fixtures render drafts without probable_test suppression.

## Verdict

**PASS** — acceptance-set delivery idempotency proven; no duplicate or revoked sends.
