# Trust Mode System v0

## Modes

| Mode | Hero content | Best when | Triumph evidence |
|------|--------------|-----------|------------------|
| `social_proof` | 4.9 ★ + Яндекс/Авито | Cold commercial; user compares providers | Blueprint specifies; **not in v5 hero** |
| `operational_proof` | Speed, min order, drivers, B2B | Hot intent; user needs dispatch confidence | v5 strip: От 30 мин · Мин. заказ · Водители · Безнал |
| `hybrid_proof` | Compact rating + 1–2 ops facts | Balance credibility + speed | **Recommended** in hero-v2 (H2-3) — not built |

## Why operational proof worked above fold (Triumph)

Calibration observations (`trust-block-analysis-v1.md`):

1. **Aligns with ad callouts** — «Звонок и расчёт», «Борт 5 т» — form + ops facts match commercial hot intent.
2. **Supports speed keywords** — «вызвать», «подача» — «От 30 минут» answers dispatch anxiety without stars.
3. **B2B hint without section scroll** — «Для юрлиц — безнал» previews segment fit.
4. **Avoids fleet trap** — v4 «Свой автопарк» removed (destructive social signal).

## Cost of operational-only mode

| Risk | Severity |
|------|----------|
| Social proof seeker must scroll to trust section | medium |
| Weak vs competitors showing stars in hero | medium (hypothesis) |
| «От 30 минут» SLA truth | **SAFE UNKNOWN** — operational claim not verified in calibration |
| Divergence from 5-ton handoff (stars in hero contract) | process — cousin pack mismatch |

## Layering model (as-built)

| Layer | Mode | Location |
|-------|------|----------|
| Hero strip | `operational_proof` | `hero-proof--v5` |
| Trust section | `social_proof` | `screen-03-trust-reviews` |
| Dark strip | reinforcement | risk of redundancy |
| B2B | `operational_proof` | legal/payment |

**Rule:** `trust_reviews_section_required: true` even when hero is operational-only.

## Pack contract

```yaml
trust_mode: operational_proof  # or social_proof | hybrid_proof
proof_visibility: prominent
proof_priority: hero_strip
trust_reviews_section_required: true
trust_hero_social: "4.9 ★ — Отзывы на Яндекс и Авито"  # if social or hybrid
trust_hero_operational:
  - "От 30 минут"
  - "Мин. заказ 2 ч"
  - "Опытные водители"
  - "Для юрлиц — безнал"
```

## Drift classification (Triumph)

| Change | Class |
|--------|-------|
| 4.9 ★ absent from hero | ambiguous |
| Ops proof in hero | productive |
| Reviews below fold preserved | productive |
| «Свой автопарк» removed | productive |

## Factory expectations

- Do not invent star ratings.
- Link to review sources only in trust section unless pack provides exact strings.
- Max 4 hero ops items; hybrid max 3 total visible.

## SAFE UNKNOWN

Which `trust_mode` maximizes qualified leads for grp_fc12 — no analytics in repo.
