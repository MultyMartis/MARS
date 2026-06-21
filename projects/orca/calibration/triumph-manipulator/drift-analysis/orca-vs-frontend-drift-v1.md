# ORCA vs Frontend Drift v1 — master hot

**Sources:** `01-master-hot-general.md` + `triumph-s-tier-draft-v1.json` (grp_fc12)  
**As-built (canonical v6):** `workspaces/triumph-manipulator-landing-v6/src/partials/sections/v5-ppc/zakaz/*`

## Summary table

| Domain | ORCA / blueprint | As-built v5 | Class |
|--------|------------------|-------------|-------|
| H1 | АРЕНДА МАНИПУЛЯТОРА В КРАСНОДАРЕ | Аренда манипулятора в Краснодаре | neutral (case/nbsp) |
| Subheadline | …манипулятором 5 т… | Same semantics | pass |
| Spec bullets (5) | Locked list | Same five values | pass |
| Hero trust | 4.9 ★ Яндекс + Авито | Operational proof strip | **ambiguous** |
| Qualification line | In hero (blueprint) | **Absent** in v5 hero; filtering in tasks | **destructive** (partial) |
| Primary CTA label | Узнать стоимость перевозки | Рассчитать стоимость | minor lexical |
| CTA placement | Qualification layer hero | Inline form + cargo CTAs | productive |
| Use-case chips | Static list | Interactive cargo cards | productive |
| Hero image | Not specified in blueprint text | Full-bleed bg + overlay | neutral/presentation |
| Fleet / fake price | Forbidden by doctrine | Removed vs v4 | productive (recovery) |

## Destructive drift (action required)

### D1 — Qualification line dropped from hero

- **Source:** `01-master-hot-general.md` — «Не работаем с эвакуацией легковых…»
- **Was in:** v4 `zakaz/screen-01-hero.html` → `hero__notice`
- **v5:** removed; denied tasks exist lower
- **Risk:** junk leads from evacuation intent; weaker 5–10 sec filter
- **Fix options:** restore notice in hero lower band OR mark pack «qualification_line_required_in_hero: true»

### D2 — Multi-ad H1 vs single landing H1

- **Ad A1:** «Заказать манипулятор в Краснодаре»
- **Ad A2:** «Аренда манипулятора Краснодар»
- **Landing H1:** «Аренда манипулятора в Краснодаре»
- **Risk:** A1 click sees «Заказать» ≠ «Аренда» — continuity gap for that variant
- **Owner:** ORCA PPC + pack (not Factory-only)

## Productive evolution (accept + encode in pack)

### P1 — Inline hero form

Aligns with «short form» + conversion goal; form visible with specs.

### P2 — Capability bullets in hero

Matches doctrine capability-first; continues ad callouts.

### P3 — v5 visual system

Bg layer + overlay improves readability vs busy composite hero.

### P4 — Cargo cards with micro-CTA

Extends use-case chips into qualification paths.

## Neutral presentation

- Title case H1 vs blueprint ALL CAPS
- `&nbsp;` typography ties in partials
- Section order matches capability handoff pattern (not blueprint’s older block names)

## Missing ORCA artifact (not drift — gap)

No master-hot **content pack** or **handoff** → Factory used blueprint + 5-ton patterns + operator sessions. Calibration should not blame Factory for all gaps.
