# ORCA Semantic Minimal Pair Design v1

**Design ID:** `orca-semantic-minimal-pair-design`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Define **minimal pair** design pattern for semantic admission — pairs differing by minimal token change with **opposite or shifted** eligibility boundary.

**Illustrations below are design patterns only — not real benchmark phrases or gold labels.**

---

## Pattern types

| Pattern ID | Illustration (placeholder) | Expected shift |
|------------|---------------------------|----------------|
| MP_HIRE_VS_DIY | `[SERVICE] настройка` vs `[SERVICE] настройка своими руками` | ACCEPT/ABSTAIN → REJECT |
| MP_CONSULT_VS_INFO | `консультация по [TOPIC]` vs `что такое [TOPIC]` | Commercial → informational |
| MP_CAREER_TRAP | `[VENDOR] вакансии` vs `[VENDOR] внедрение` | REJECT vs ACCEPT |
| MP_PRODUCT_VS_SERVICE | `купить [MODULE]` vs `внедрить [MODULE]` | Product review vs service ACCEPT |
| MP_GEO_MODIFIER | `[SERVICE] [CITY]` vs `[SERVICE]` | Geo may shift risk not intent |

Placeholders in brackets — **do not** copy into production benchmark without full annotation path.

---

## Use

- Adversarial pack seeding (`DIFF_ADVERSARIAL`)
- Annotator training **outside** blind pack
- Regression anchor design

---

## Rules

1. Pairs must be annotated **independently** — no label inheritance across pair members
2. Both members may enter benchmark if sampled; link via `benchmark.minimal_pair_id` only
3. Synthetic pairs: `source_type` = synthetic design class
