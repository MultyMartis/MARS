# ORCA ABSTAIN Standard v1

**Standard ID:** `orca-abstain-standard`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

`ABSTAIN` is a **valid terminal decision** for automated semantic eligibility (invariant 20). It means: *evidence is insufficient or conflicting; do not admit to paid core without human adjudication.*

ABSTAIN is **success**, not pipeline failure. This standard defines mandatory ABSTAIN cases, required record fields, and reviewer workflow.

---

## Semantic meaning

| Aspect | ABSTAIN |
|--------|---------|
| PPC gate | Phrase **not approved** for automated core promotion |
| Automation | Processing **completes** normally |
| Human path | `review.workflow_status: ABSTAIN_PENDING_REVIEW` typical |
| vs REJECT | REJECT = confident exclusion; ABSTAIN = unresolved uncertainty |
| vs ACCEPT | ACCEPT = positive commercial evidence meets all requirements |

---

## Mandatory ABSTAIN cases

Automated `commercial_eligibility.decision` **must** be `ABSTAIN` when any condition below holds.

### A — Unresolved mandatory ambiguity types

Per [`ORCA-AMBIGUITY-TAXONOMY-v1.md`](../../taxonomy/ORCA-AMBIGUITY-TAXONOMY-v1.md):

| ambiguity type | reason_code family |
|----------------|-------------------|
| `PROVIDER_VS_DIY` | `PROVIDER_DIY_CONFLICT` |
| `PRODUCT_VS_SERVICE` | `PRODUCT_SERVICE_CONFLICT` |
| `CAREER_VS_PROVIDER` | `PROTECTED_SIGNAL_CONFLICT` |
| `SUPPORT_VS_INFORMATION` | `SUPPORT_INFORMATION_CONFLICT` |
| `SHORT_HEAD_TERM` (severity HIGH/CRITICAL) | `SHORT_AMBIGUOUS_PHRASE` |
| `MULTIPLE` | `COMPETING_INTENTS` |

### B — Protected signal conflict

Conflicting protected strata without adjudicated winner (invariant 3):

- career vs commercial hire in same phrase
- educational vs implementation language without dominance
- regulatory info vs implementation ask unclear

→ `PROTECTED_SIGNAL_CONFLICT`

### C — Insufficient commercial evidence

- Only WEAK/MEDIUM topical signals
- UNKNOWN-like intent with no STRONG/EXPLICIT commercial path
- Problem signal alone without provider path

→ `INSUFFICIENT_EVIDENCE`

### D — Competing intents without winner

Multiple `primary_intent` candidates with comparable support:

→ `COMPETING_INTENTS`

### E — Low confidence below threshold

Assessor confidence below `threshold_profile` (CONSERVATIVE/STANDARD):

→ `LOW_CONFIDENCE`

### F — Rule/model disagreement

Deterministic rules and model/LLM assessors disagree on eligibility:

→ `RULE_MODEL_DISAGREEMENT`

### G — Service ownership unresolved at eligibility boundary

Cannot responsibly assign service candidate at semantic gate:

→ `SERVICE_OWNERSHIP_UNRESOLVED_AT_ELIGIBILITY_BOUNDARY`

### H — Unresolved high ambiguity blocks ACCEPT

Invariant 4: severity HIGH/CRITICAL + competing interpretations → cannot ACCEPT.

---

## When ABSTAIN is preferred over weak ACCEPT

| Situation | Why ABSTAIN |
|-----------|-------------|
| «монтаж вентиляции» | DIY vs provider |
| «1с» | Short head |
| «купить и установить crm» | Product vs service |
| «1с не работает» | Problem without hire |
| «консультация 1с» | Support vs information |
| Mixed signals equal weight | Conservative gate |

**Principle:** False ACCEPT cost > ABSTAIN review cost for ORCA protected-strata FPR targets.

---

## Required fields (ABSTAIN record)

### Mandatory

| Field | Requirement |
|-------|-------------|
| `commercial_eligibility.decision` | `ABSTAIN` |
| `commercial_eligibility.reason_code` | One abstain family code (see taxonomy) |
| `commercial_eligibility.confidence` | 0.0–1.0 — typically moderate; not fake certainty |
| `commercial_eligibility.reviewer_required` | `true` when policy or risk demands |
| `ambiguity.unresolved_questions` | **minItems: 1** (invariant 6) — concrete question |
| `provenance_status` | Not `MISSING` (invariant 7) |

### Strongly recommended

| Field | Requirement |
|-------|-------------|
| `ambiguity.types[]` | Typed ambiguity |
| `ambiguity.severity` | HIGH/CRITICAL when applicable |
| `ambiguity.competing_interpretations` | ≥ 2–3 for conflict cases |
| `commercial_eligibility.opposing_evidence` | Why ACCEPT was not chosen |
| `commercial_eligibility.phrase_explanation` | Phrase-specific rationale |
| `review.workflow_status` | `ABSTAIN_PENDING_REVIEW` |

### Schema conditional

ABSTAIN records **must** populate `ambiguity.unresolved_questions` with at least one human-actionable question, e.g.:

- «Пользователь ищет подрядчика или инструкцию для самостоятельного монтажа?»
- «Покупка лицензии или заказ проекта внедрения?»
- «Какая доминирующая задача по фразе «1с» без контекста?»

---

## unresolved_questions quality rules

| Rule | Description |
|------|-------------|
| Actionable | Question must be answerable by human review |
| Phrase-anchored | References actual tokens, not generic «unclear intent» |
| Non-rhetorical | Not «что хотел пользователь?» alone |
| Single-focus | One conflict per question when possible |
| No sentinels | Invariant 14 — no raw numeric sentinel codes in text |

---

## ABSTAIN reason_code catalog (reference)

| reason_code | Use when |
|-------------|----------|
| `INSUFFICIENT_EVIDENCE` | Weak signals only |
| `COMPETING_INTENTS` | Multiple intents tied |
| `SHORT_AMBIGUOUS_PHRASE` | Head term |
| `PROVIDER_DIY_CONFLICT` | Hire vs self-service |
| `PRODUCT_SERVICE_CONFLICT` | Buy vs order work |
| `SUPPORT_INFORMATION_CONFLICT` | Support vs info |
| `RULE_MODEL_DISAGREEMENT` | Assessor conflict |
| `LOW_CONFIDENCE` | Below threshold |
| `PROTECTED_SIGNAL_CONFLICT` | Protected strata clash |
| `SERVICE_OWNERSHIP_UNRESOLVED_AT_ELIGIBILITY_BOUNDARY` | Service mapping premature |

---

## Examples (RU)

| Query | reason_code | unresolved_question (example) |
|-------|-------------|-------------------------------|
| «1с» | `SHORT_AMBIGUOUS_PHRASE` | «Доминирует покупка, внедрение или навигация на официальный ресурс?» |
| «монтаж вентиляции» | `PROVIDER_DIY_CONFLICT` | «Нужен подрядчик или справочная информация для самостоятельных работ?» |
| «купить и установить 1с» | `PRODUCT_SERVICE_CONFLICT` | «Запрос на покупку коробки или проект внедрения под ключ?» |
| «crm» | `SHORT_AMBIGUOUS_PHRASE` | «Какая CRM-задача: выбор продукта, внедрение или вход в сервис?» |
| «консультация по 1с» | `SUPPORT_INFORMATION_CONFLICT` | «Платная консультация специалиста или бесплатный информационный ответ?» |

---

## Human adjudication outcomes

After review, workflow may transition:

`ABSTAIN_PENDING_REVIEW` → `HUMAN_REVIEWED` / `ADJUDICATED` → `APPROVED_FOR_CORE` or `REJECTED_FROM_CORE`

Human may set `commercial_eligibility.decision` to ACCEPT or REJECT with `OPERATOR_OVERRIDE` audit (invariant 12).

---

## Anti-patterns

| Anti-pattern | Correct action |
|--------------|----------------|
| Treat ABSTAIN as error | Valid terminal |
| ACCEPT to avoid review queue | Violates invariants |
| Empty unresolved_questions | Schema/invariant violation |
| Generic reason without code | Must use reason_code |
| Copy-paste same question for all phrases | Fails phrase-specific standard |

---

## Related documents

- [`ORCA-ACCEPT-STANDARD-v1.md`](ORCA-ACCEPT-STANDARD-v1.md)
- [`ORCA-REJECT-STANDARD-v1.md`](ORCA-REJECT-STANDARD-v1.md)
- [`../../taxonomy/ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md`](../../taxonomy/ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md)
- [`../../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md`](../../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md)
