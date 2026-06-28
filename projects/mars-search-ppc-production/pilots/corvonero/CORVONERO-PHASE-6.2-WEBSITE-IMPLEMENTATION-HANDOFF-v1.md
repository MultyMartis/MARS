# CORVONERO Phase 6.2 — Website Implementation Handoff v1

## Purpose

Transfer package for website development: six dedicated service landing pages on `lk.corvonero.ru`. **Do not build in Phase 6.2** — requirements only.

## Required page inventory

| LP | Campaign | Slug (recommended) | Priority |
|----|----------|-------------------|----------|
| LP-01 | CA-01 | programmist-1s | P1 |
| LP-02 | CA-02 | soprovozhdenie-1s | P1 |
| LP-03 | CA-03 | dorabotka-razrabotka-1s | P1 |
| LP-04 | CA-04 | integracii-1s | P1 |
| LP-05 | CA-05 | markirovka-chestny-znak | P1 |
| LP-06 | CA-06 | otchety-obrabotki-1s | P2 |

## Dependencies

1. Operator Decision Packet v3 — blocking confirmations.
2. Client evidence inventory — blocking fields cleared.
3. Production sequence — LP-01 → LP-02 → LP-05 → LP-03 → LP-04 → LP-06.

## Acceptance criteria

- Unique URL + H1 per campaign family.
- Message match for all mapped ad groups.
- Geography: Новосибирск + Новосибирская область.
- CTA + phone + form with privacy notice.
- No unsupported commercial claims.

## Prohibited

- `corvonero.ru` as LP.
- `/products` for service campaign traffic.
- Invented prices, SLA, or certifications.
