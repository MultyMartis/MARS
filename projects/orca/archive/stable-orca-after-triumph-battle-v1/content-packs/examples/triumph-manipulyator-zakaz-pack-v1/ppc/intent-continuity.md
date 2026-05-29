# PPC — Intent continuity (grp_fc12_zakaz)

**Instance:** `triumph-s-tier-draft-v1.json`  
**Group:** `grp_fc12_zakaz` — «12 — Заказать манипулятор»  
**semantic_intent:** заказать, вызвать, цена, аренда  
**landing_type:** `master_hot`

## Intent layers on landing

| Layer | Expression |
|-------|------------|
| Commercial hot | Form + tel + «Рассчитать» |
| Capability | 5 т / 3 т / 14 м — hero + specs + FAQ Q2 |
| Task breadth | Cargo + tasks allowed |
| Anti-broad-rental | Denied tasks + hero notice |
| B2B overlay | B2B section + hero «безнал» |
| Geo | H1 + lead + FAQ Q4 |

## Keyword → page mapping

| Keyword (instance) | Support | Strength |
|--------------------|---------|----------|
| аренда манипулятора краснодар | H1 «Аренда» | **strong** |
| заказать манипулятор | FAQ, final H2, meta — not H1 | **weak** |
| манипулятор цена краснодар | pricing + form | **strong** |
| вызвать манипулятор краснодар | proof «От 30 мин» | **partial** |
| услуги манипулятора краснодар | broad lead + tasks | **medium** |
| кран-манипулятор краснодар | specs only | **medium** |
| манипулятор краснодар | geo + general framing | **medium** |

## Continuity rule (instance)

`intent_continuity_rule`: «Hero - заказ, подача, квалификация задачи»  
`intent_continuity_ack`: **false** — honest process signal.

**Pack action:** set ack **true** only after operator signs H1 strategy + qualification placement.

## Survived correctly

- Hot commercial → CTA surfaces
- Capability numbers → hero + specs
- Price intent → no fake tariff
- Geo intent → H1 + lead

## At risk

- «Заказать» token absent in H1 (D2)
- «Кран-манипулятор» not echoed in H1/FAQ title
- Qualification below fold for fast bouncers (mitigated by hero notice)

## Fastlinks

8 fastlinks in instance — **not** mirrored as on-page UI (expected). User may arrive with extension context; landing qualifies general intent first — **low risk**.
