# PPC-to-Hero Alignment Findings v1

**Source:** `ppc-continuity-analysis-v1.md`, `intent-continuity-v1.md`, `headline-alignment-v1.md`

## Continuity matrix

| Dimension | Survived? |
|-----------|-----------|
| Geo Краснодар | **yes** |
| Capability 5 т / 3 т / 14 м | **yes** |
| Intent «аренда» (A2) | **yes** |
| Intent «заказать» (A1) | **no** |
| Price framing по задаче | **yes** |
| Form + tel CTA | **yes** |
| Trust in ad | N/A — delayed on LP |
| Qualification | **partial** — below fold only |

## Instance signals

- `semantic_intent`: заказать, вызвать, цена, аренда
- `intent_continuity_rule`: Hero - заказ, подача, квалификация задачи
- `intent_continuity_ack: false` — honest; set true only after D1 + H1 strategy

## Callouts vs hero

| Callout | Hero |
|---------|------|
| Звонок и расчёт | form + tel — aligned |
| Борт 5 т | spec bullet — aligned |

## Fastlinks

8 fastlinks in instance — **not** mirrored in hero UI (expected). Low risk if `/` qualifies general intent first.

## Visual semantics actions

1. Pack `primary_ad_variant` per deployed H1 strategy
2. Set `mobile_critical` for call-first
3. Do not treat semantic copy completeness as PPC continuity pass

## Launch recommendation (calibration)

Spec numbers pass; H1 token pass for **аренда only**. Resolve D2 before full group sign-off.
