# Intent Continuity v1 — grp_fc12

**Group:** `grp_fc12_zakaz` — Master hot  
**semantic_intent:** «заказать, вызвать, цена, аренда»  
**landing_type:** `master_hot`

## Intent layers

| Layer | Expression on landing |
|-------|----------------------|
| Commercial hot | Form + tel + «Рассчитать» |
| Capability | 5 т / 3 т / 14 м everywhere |
| Task breadth | Cargo chips + tasks section |
| Anti-broad-rental | Denied tasks; weak hero filter |
| B2B overlay | B2B section (shared partial) |
| Geo | Краснодар + край |

## Keyword → page mapping (sample)

| Keyword (instance) | Landing support |
|--------------------|-----------------|
| аренда манипулятора краснодар | H1 «Аренда» — **strong** |
| заказать манипулятор | H1 — **weak** |
| манипулятор цена краснодар | Pricing factors + form — **strong** |
| вызвать манипулятор краснодар | Proof «От 30 мин» — **partial** |
| услуги манипулятора краснодар | Broad lead + tasks — **medium** |
| кран-манипулятор краснодар | Specs — **medium** (no synonym in H1) |

## Continuity rule (instance)

`intent_continuity_rule`: «Hero - заказ, подача, квалификация задачи»  
`intent_continuity_ack`: **false** in JSON — honest signal that continuity not formally acknowledged.

**Calibration action:** set ack true only after operator signs H1 strategy + hero qualification.

## Survived correctly

- Hot commercial → CTA surfaces
- Capability numbers → hero + specs
- Price intent → no fake tariff
- Geo intent → H1 + lead

## At risk

- «Заказать» token absent in H1
- «Кран-манипулятор» not echoed (optional synonym line)
- `intent_continuity_ack: false` reflects real process gap
