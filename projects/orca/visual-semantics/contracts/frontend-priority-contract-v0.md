# Frontend Priority Contract v0

Factory agrees to implement and QA sections in `frontend_priority` order.

## Default skeleton (Triumph 12-route family)

1. `hero_main` / `hero_aside` / `hero_lower` (P0)
2. `specs` (P1)
3. `tasks` (P1)
4. `order_steps` (P2)
5. `pricing_factors` (P2)
6. `trust_reviews` (P3)
7. `b2b` (P3)
8. `dark_proof_strip` (P4)
9. `faq` (P4)
10. `footer_contact` (P0)

## Route overrides

| Route type | Override |
|------------|----------|
| use_case | elevate scenario image in specs to P1 |
| b2b yurlica | elevate `b2b` toward P2 |
| intercity | geo copy in hero — no skeleton change |

## Partial completeness

Factory may ship hero+specs first for pilot **only** if pack marks `pilot_scope` — **not** defined in v0; operator decision.

## QA contract

QA verifies P0 blocks before P4 polish. Visual semantics fields with `visual_noise_risk: high` get extra hero lower-band review.

## Reference

[frontend-priority-model-v0.md](../frontend-priority-model-v0.md)
