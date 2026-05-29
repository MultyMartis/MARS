# Trust Block Analysis v1

## ORCA expected trust (blueprint hero)

| Element | Blueprint |
|---------|-----------|
| Rating line | 4.9 ★ |
| Source | Отзывы клиентов на Яндекс и Авито |
| Placement | Hero trust strip |

## As-built trust layers

| Layer | Location | Content |
|-------|----------|---------|
| Hero proof strip | `screen-01-hero.html` | От 30 мин · Мин. заказ · Опытные водители · Безнал для юрлиц |
| Trust + reviews | `v5-page01/screen-03-trust-reviews.html` | Яндекс + Авито review framing (shared partial) |
| Dark proof strip | `dark-proof-strip.html` | Additional proof chips |
| B2B block | `screen-03b-b2b.html` | Legal / payment trust |

## Drift classification

| Change | Class | Reasoning |
|--------|-------|-----------|
| 4.9 ★ absent from hero | **ambiguous** | Social proof delayed; ops proof substituted |
| Ops proof in hero | **productive** | Supports «подача», B2B, speed — matches callouts partially |
| Reviews preserved below fold | **productive** | Lock on sources not violated if copy unchanged |
| v4 «Свой автопарк» removed | **productive** | Was destructive fleet signal |

## Continuity impact

| User expectation from ad | First screen experience |
|--------------------------|---------------------------|
| «Надёжный перевозчик» (implicit) | Ops facts, not stars |
| Price / calc intent | Form-forward — OK |
| Social proof seeker | Must scroll to trust section — **friction** |

## Comparison to 5-ton handoff

5-ton handoff explicitly locks trust strip in hero. Master hot blueprint matches. **5-ton pack** includes trust in hero contract — zakaz implementation **diverges from cousin pack**.

## Risks

1. **Hidden proof** — star rating not visible in first 5–10 sec.
2. **Weak trust for cold аренда queries** — competitors may show stars above fold.
3. **Over-trust on ops claims** — «От 30 минут» needs operational truth (SAFE UNKNOWN on SLA proof).

## Pack rule proposal

```yaml
trust_hero_mode: one_of [social_rating, operational_proof, hybrid]
trust_hero_social: "4.9 ★ — Яндекс и Авито"  # if social_rating
trust_hero_operational: [ ... ]               # if operational_proof
trust_reviews_section_required: true
```

## Block effectiveness (human)

| Block | Role | Observation |
|-------|------|-------------|
| Hero proof | Speed + B2B hint | Scannable; no links to reviews |
| Trust section | Credibility | Correct layer for detailed proof |
| Dark strip | Reinforcement | Risk of redundancy with hero proof — visual density |

**No analytics claim** — scroll depth UNKNOWN.
