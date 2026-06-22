# ORCA Short Head Term Adjudication v1

**Adjudication ID:** `orca-short-head-term-adjudication`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Short head terms — typically **1–2 tokens** with high SERP entropy — are CRITICAL ambiguity carriers. This standard governs adjudication for head queries in ORCA Semantic Intelligence, with **1С (1C)** as the canonical reference domain.

Aligns with:

- Ambiguity type `SHORT_HEAD_TERM` (severity HIGH–CRITICAL, mandatory ABSTAIN if unresolved)
- Intent `AMBIGUOUS`, `UNKNOWN`
- reason_code `SHORT_AMBIGUOUS_PHRASE`

---

## Definition: short head term

| Criterion | Rule |
|-----------|------|
| Token count | ≤ 2 meaningful tokens after normalization |
| Context | Lacks task verb, object scope, geo, or disambiguating modifier |
| Entropy | Multiple plausible intents with comparable prior |
| Risk | Automated ACCEPT **forbidden** (invariant 4) |

**Examples:** «1с», «crm», «вентиляция», «битрикс», «erp», «1с бухгалтерия» (borderline — may still ABSTAIN).

---

## Core rule

> **Short head term alone → ABSTAIN (`SHORT_AMBIGUOUS_PHRASE`).**

No amount of domain familiarity («we know 1С users often want implementation») substitutes for **phrase-local evidence**. Operator priors belong in review policy, not automated ACCEPT.

---

## 1С reference interpretations

For head query **«1с»** (and close variants «1c», «1 с»), document **at minimum** these competing readings:

| # | Interpretation | Intent / goal | Typical user action |
|---|----------------|---------------|---------------------|
| 1 | Buy product/license | `BUY_PRODUCT_OR_MODULE` | Purchase SKU |
| 2 | Hire implementation/service | `HIRE_SERVICE` / `REQUEST_IMPLEMENTATION` | Order project |
| 3 | Navigational | `NAVIGATIONAL` | Open official site |
| 4 | Career | `CAREER_EMPLOYMENT` | Job search context (weak alone) |
| 5 | Education | `EDUCATIONAL` | Training browse |
| 6 | Download/trial | `DOWNLOAD_RESOURCE` | Get demo |
| 7 | Login | `LOGIN_ACCOUNT_ACCESS` | Enter cloud account |
| 8 | Problem (latent) | `PROBLEM_UNRESOLVED` | Unstated failure |

**Eligibility:** ABSTAIN — insufficient evidence to select dominant task.

### 1С examples table

| Query | Tokens | Dominant resolvable? | Decision | Notes |
|-------|--------|----------------------|----------|-------|
| «1с» | 1 | No | **ABSTAIN** | Canonical head |
| «1c» | 1 | No | **ABSTAIN** | Latin homoglyph |
| «1с erp» | 2 | Partial product/edition | **ABSTAIN** | Edition ≠ task |
| «1с бухгалтерия» | 2 | Product SKU likely | **REJECT** | Product module name — still document rationale |
| «1с внедрение» | 2 | Service task present | **ACCEPT path** | Implementation object |
| «1с официальный сайт» | 3 | Navigational | **REJECT** | Protected navigational |
| «заказать 1с» | 2 | Hire verb present | **ACCEPT path** | PROVIDER_HIRE explicit |
| «курс 1с» | 2 | Educational | **REJECT** | Protected |
| «вакансия 1с» | 2 | Career | **REJECT** | Protected |
| «1с не работает» | 3 | Problem — not head-only | See problem adjudication | **ABSTAIN** default |
| «скачать 1с» | 2 | Download | **REJECT** | Free/download |

---

## When 2-token phrases exit short-head treatment

A 2-token phrase may be adjudicated (not automatic ABSTAIN) **only when**:

1. **Explicit protected marker** → REJECT (e.g. «курс 1с»).
2. **Explicit commercial task** → ACCEPT path (e.g. «заказать 1с», «1с внедрение»).
3. **Explicit product SKU pattern** → REJECT product (e.g. «1с бухгалтерия» as product name).

If none apply → remain ABSTAIN.

---

## Borderline: brand + category

| Query | Issue | Outcome |
|-------|-------|---------|
| «crm» | Pure head | ABSTAIN |
| «crm внедрение» | Service object | ACCEPT path |
| «битрикс24» | Brand head | ABSTAIN |
| «битрикс24 цена» | Quote — informational risk | ABSTAIN or REJECT |
| «вентиляция» | Trade head — DIY vs provider | ABSTAIN `PROVIDER_DIY_CONFLICT` |

---

## Severity assignment

| Condition | ambiguity severity |
|-----------|-------------------|
| 1 token, high-volume domain | CRITICAL |
| 2 tokens, no verb | HIGH |
| 2 tokens, ambiguous verb | HIGH |
| 3+ tokens | Usually not `SHORT_HEAD_TERM` — use other types |

---

## Recording requirements

| Field | Requirement |
|-------|-------------|
| `ambiguity.types[]` | Include `SHORT_HEAD_TERM` |
| `ambiguity.severity` | HIGH or CRITICAL |
| `ambiguity.competing_interpretations` | ≥ 3 for true head terms |
| `ambiguity.unresolved_questions` | Min 1 — e.g. «Какая следующая задача: покупка, внедрение или вход в сервис?» |
| `commercial_eligibility.decision` | ABSTAIN |
| `commercial_eligibility.reason_code` | `SHORT_AMBIGUOUS_PHRASE` |

---

## Operator seed exception

`VALIDATED_OPERATOR_SEED` may support ACCEPT for specific head terms **only** when:

- Operator pre-approval record exists with phrase-exact match
- Audit trail links seed to campaign scope
- Annotator cites seed ID in `phrase_explanation`

**Default:** head terms are not seed-candidates without explicit operator charter.

---

## Anti-patterns

| Anti-pattern | Why forbidden |
|--------------|---------------|
| ACCEPT «1с» because business sells 1С services | Prior ≠ evidence |
| REJECT «1с» as irrelevant | Domain term — ABSTAIN not IRRELEVANT |
| Pick navigational because official SERP shows site | SERP prior not in phrase |
| Merge head into longest historical query | Invariant 19 — no rewrite |

---

## Related documents

- [`ORCA-PRODUCT-VS-SERVICE-ADJUDICATION-v1.md`](ORCA-PRODUCT-VS-SERVICE-ADJUDICATION-v1.md)
- [`ORCA-ABSTAIN-STANDARD-v1.md`](ORCA-ABSTAIN-STANDARD-v1.md)
- [`ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md`](ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md)
