# Destructive Drift Findings v1

**Definition:** Changes that weaken PPC continuity, qualification, trust locks, or intent match.  
**Factory approval:** `drift_acceptance.destructive` must be **empty**.

## D1 — Qualification line dropped from hero

| | |
|---|---|
| **Blueprint** | «Не работаем с эвакуацией легковых…» in hero |
| **G1** | `hero__notice` present |
| **G2** | removed; filtering only in tasks section |
| **Risk** | junk leads; weak 5–10 sec filter |
| **Fields** | `qualification_mode: tasks_section_only` vs required `hero_notice` |
| **Fix** | Restore notice in `hero__lower` above cargo (H2-1) |

## D2 — Multi-ad H1 vs single landing H1

| Ad | H1 token |
|----|----------|
| A2 «Аренда манипулятора Краснодар» | **strong** match |
| A1 «Заказать манипулятор в Краснодаре» | **weak** — landing uses «Аренда» only |
| **Owner** | ORCA PPC + pack (`primary_ad_variant`) — not Factory-only |
| **Fields** | intent continuity failure for A1 variant |

## Historical destructive (G0 — do not restore)

- fake hero hourly rate
- fleet «5–10 т», «Свой автопарк»
- `hero_layout_mode: legacy_clutter`

## Ambiguous (not destructive without operator call)

| Item | Notes |
|------|-------|
| 4.9 ★ absent | ops substitute — may be acceptable |
| «Узнать» → «Рассчитать» | lexical |
| `intent_continuity_ack: false` in JSON | process honesty |

## Current pack status (calibration)

```yaml
drift_acceptance:
  destructive:
    - D1_qualification_hero_removed
    - D2_multi_ad_h1_unresolved
```

## Launch gate (calibration opinion)

Do not mark grp_fc12 fully continuity-verified until D1 fixed and H1 strategy covers **both** primary ads or ads split by URL.
