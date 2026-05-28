# Frontend Priority Model v0

**Method:** Triumph v5 index section order vs blueprint — `section-priority-observations-v1.md`.

## Priority tiers

| Tier | Meaning | Factory QA focus |
|------|---------|------------------|
| **P0** | Must work before launch — intent + conversion | Hero, footer contact |
| **P1** | Capability + fit proof | Specs, tasks allowed/denied |
| **P2** | Process + price framing | Order steps, pricing factors |
| **P3** | Trust + segment overlay | Trust/reviews, B2B |
| **P4** | Objections + reinforcement | Dark proof strip, FAQ |

## Triumph master hot stack (as-built)

| Tier | Section | Visual semantics link |
|------|---------|----------------------|
| P0 | Hero (`first-screen`) | All hero_* fields |
| P1 | Specs `#specs` | `semantic_focus: one_machine` |
| P1 | Tasks | `qualification_mode` when not in hero |
| P2 | Order steps | neutral |
| P2 | Pricing factors | `conversion_intent_weight: hot` |
| P3 | Trust + reviews | `trust_mode` social layer |
| P3 | B2B | `semantic_focus: b2b_payment` (partial) |
| P4 | Dark proof strip | `visual_noise_risk` if redundant |
| P4 | FAQ | — |
| P0 | Footer contact | `cta_priority` tel + messengers |

## Mismatch vs blueprint intent

Blueprint implied trust in **hero (P0–P1)**. As-built places social proof at **P3** while hero uses operational strip — document via `proof_priority` + `trust_mode`, not accidental.

## `frontend_priority` field

Ordered list for Factory build/QA. Example:

```yaml
frontend_priority:
  - hero_main
  - hero_aside
  - hero_lower
  - specs
  - tasks
  - order_steps
  - pricing_factors
  - trust_reviews
  - b2b
  - dark_proof_strip
  - faq
  - footer_contact
```

## Scaling rule

Use-case routes **elevate task-specific proof to P1** (scenario image) without changing global skeleton — see `next-evolution/scaling-rules-for-11-pages-v2.md`.

## SAFE UNKNOWN

Real user scan paths — no telemetry in repo.
