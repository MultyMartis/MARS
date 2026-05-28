# Hero Zoning Findings v1

**Source:** `current-hero-analysis-v1.md`

## Zone map (G2)

```text
.first-screen
  └── .hero.hero--v5
        ├── .hero__main
        │     ├── .hero__content    ← capability scan path
        │     └── .hero__aside      ← conversion path
        └── .hero__lower
              ├── .hero-proof--v5   ← trust ops path
              └── .hero__cargo-block ← qualification path
```

## Zone → visual semantic role

| Zone | Primary fields |
|------|----------------|
| `hero__content` | `hero_priority`, `semantic_focus`, `compactness_level` |
| `hero__aside` | `cta_priority`, `cta_weight` |
| `hero__lower` proof | `trust_mode`, `proof_visibility` |
| `hero__lower` cargo | `use_case_fit`, `visual_noise_risk` |

## Zoning vs G0

G0 had **no lower band** — proof, features, rate, CTA competed in one cognitive layer.

G2 separation is **productive drift** — enables `visual_density: high` without `critical`.

## Copy locks in zones (zakaz)

| Zone | Locked content |
|------|----------------|
| H1 | Аренда манипулятора **в Краснодаре** |
| Lead | 5 т, край, без посредников |
| Specs | 5 т / 3 т / 14 м / 6.2×2.2 / 2 ч |
| Form | Рассчитать стоимость |
| Proof | 30 мин · мин заказ · водители · безнал |

## Missing zone content

- Qualification notice (was G1 `hero__notice`) — **empty in G2** → D1
