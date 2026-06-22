# ORCA Ambiguity Taxonomy v1

**Taxonomy ID:** `orca-ambiguity-taxonomy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-ambiguity-taxonomy-v1.json`](orca-ambiguity-taxonomy-v1.json)

---

## Purpose

Typed ambiguity with **severity** drives conservative eligibility. Unresolved protected conflicts require **ABSTAIN**, not guess-ACCEPT.

---

## Severity scale

| Severity | Meaning |
|----------|---------|
| `LOW` | Minor; unlikely to change eligibility alone |
| `MEDIUM` | May change intent or goal assignment |
| `HIGH` | Blocks automated ACCEPT without resolution |
| `CRITICAL` | Automated ACCEPT forbidden; human/operator required |

---

## Ambiguity types

| type | typical severity | description | mandatory ABSTAIN if unresolved |
|------|------------------|-------------|--------------------------------|
| `NONE` | LOW | Нет конкурирующих интерпретаций. | no |
| `LEXICAL` | LOW–MEDIUM | Омонимия, морфология, опечатка допускает разные лексемы. | no |
| `INTENT` | MEDIUM–HIGH | Несколько primary intent с близкой вероятностью. | no |
| `SERVICE` | MEDIUM | Неясно, какая услуга из каталога соответствует фразе. | no |
| `PRODUCT_VS_SERVICE` | HIGH | Неясно: купить продукт или заказать услугу. | **yes** |
| `PROVIDER_VS_DIY` | HIGH | Неясно: нанять исполнителя или сделать самому. | **yes** |
| `SUPPORT_VS_INFORMATION` | MEDIUM–HIGH | Неясно: нужна поддержка или справочная информация. | **yes** |
| `CAREER_VS_PROVIDER` | HIGH | Путаница вакансия/подрядчик/работа. | **yes** |
| `REGULATORY_VS_IMPLEMENTATION` | MEDIUM | Нормативные требования vs заказ внедрения под нормы. | no |
| `GEOGRAPHIC` | LOW–MEDIUM | Гео неоднозначно или отсутствует при geo-dependent услуге. | no |
| `SHORT_HEAD_TERM` | HIGH–CRITICAL | Короткий head-term без контекста (1–2 токена). | **yes** |
| `MULTIPLE` | HIGH–CRITICAL | Несколько типов неоднозначности одновременно. | **yes** |
| `UNKNOWN` | MEDIUM | Не удалось классифицировать тип неоднозначности. | no |

---

## When ABSTAIN is mandatory

Automated `commercial_eligibility.decision` **must** be `ABSTAIN` when **any** of the following ambiguity types remain **unresolved** at eligibility boundary:

1. `PROVIDER_VS_DIY`
2. `PRODUCT_VS_SERVICE`
3. `CAREER_VS_PROVIDER`
4. `SUPPORT_VS_INFORMATION`
5. `SHORT_HEAD_TERM` (severity HIGH or CRITICAL)
6. `MULTIPLE`

Additionally (invariants 3–4):

- Conflicting **protected** signals without adjudication → ABSTAIN
- Severity `HIGH` or `CRITICAL` with competing interpretations → cannot ACCEPT

### ABSTAIN record requirements

- `commercial_eligibility.decision` = `ABSTAIN`
- `ambiguity.unresolved_questions` — **minItems: 1** (schema)
- `reason_code` from abstain family (e.g. `PROVIDER_DIY_CONFLICT`)
- `review.workflow_status` typically `ABSTAIN_PENDING_REVIEW`

### Examples

| Query | types | outcome |
|-------|-------|---------|
| «1с» | SHORT_HEAD_TERM | ABSTAIN |
| «монтаж вентиляции» | PROVIDER_VS_DIY | ABSTAIN |
| «1с вакансия» | CAREER_VS_PROVIDER | ABSTAIN |
| «купить и установить crm» | PRODUCT_VS_SERVICE | ABSTAIN |

---

## Related documents

- [`ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md`](ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md)
- [`../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md`](../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md)
