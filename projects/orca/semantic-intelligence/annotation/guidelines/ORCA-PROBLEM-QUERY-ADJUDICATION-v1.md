# ORCA Problem Query Adjudication v1

**Adjudication ID:** `orca-problem-query-adjudication`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Problem-shaped queries (`PROBLEM` signal, `PROBLEM_UNRESOLVED` intent) are a major source of **over-ACCEPT** in PPC semantic review. This standard defines how annotators interpret failure/symptom language without treating **problem signal alone** as commercial evidence.

Aligns with:

- Signal `PROBLEM` ([`ORCA-SEMANTIC-SIGNAL-TAXONOMY-v1.md`](../../taxonomy/ORCA-SEMANTIC-SIGNAL-TAXONOMY-v1.md))
- Intent `PROBLEM_UNRESOLVED` ([`ORCA-PRIMARY-INTENT-TAXONOMY-v1.md`](../../taxonomy/ORCA-PRIMARY-INTENT-TAXONOMY-v1.md))
- ACCEPT reason `STRONG_PAID_SERVICE_PROBLEM_INTENT` ([`ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md`](../../taxonomy/ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md))

---

## Core rule

> **Problem signal alone ≠ ACCEPT.**

A symptom («не работает», «ошибка», «зависает», «не проводит») establishes that something is wrong. It does **not** establish that the user intends to **hire a paid provider** rather than self-troubleshoot, read documentation, or seek free community help.

---

## Mandatory three-interpretation protocol

For every problem-shaped phrase, document **exactly three** competing interpretations before eligibility assignment. Store in `ambiguity.competing_interpretations` or adjudication notes.

| Slot | Interpretation class | Typical intent / goal |
|------|---------------------|------------------------|
| **I1 — Self-service** | User will fix alone | `TROUBLESHOOT_SELF`, `DIY_HOW_TO`, `DOCUMENTATION_LOOKUP` |
| **I2 — Informational** | User wants explanation, not engagement | `INFORMATIONAL`, `REGULATORY` |
| **I3 — Paid provider** | User seeks external paid fix | `REQUEST_SUPPORT`, `REQUEST_RECOVERY`, `HIRE_SERVICE` |

### Example: «1с не проводит документ»

| Slot | Reading | Signals |
|------|---------|---------|
| I1 | Self-troubleshoot posting error | `PROBLEM` STRONG, `DIY` latent |
| I2 | Search for known causes / forum | `PROBLEM` + informational pattern |
| I3 | Call specialist / support contract | `PROBLEM` + `SUPPORT`/`PROVIDER_HIRE` if present |

**Without I3 evidence** → not ACCEPT. Default **ABSTAIN** (`PROVIDER_DIY_CONFLICT` or `INSUFFICIENT_EVIDENCE`), not optimistic ACCEPT.

### Example: «ошибка 1с при закрытии месяца»

| Slot | Reading |
|------|---------|
| I1 | DIY fix via instruction |
| I2 | Understand what the error means |
| I3 | Paid recovery / support visit |

Eligibility: ABSTAIN unless explicit support/recovery/hire markers appear.

---

## Problem signal strength vs eligibility

| PROBLEM strength | Other signals | Typical eligibility |
|------------------|---------------|---------------------|
| EXPLICIT symptom only | None commercial | ABSTAIN |
| STRONG symptom | DIY EXPLICIT | REJECT `CLEAR_DIY_HOW_TO` |
| STRONG symptom | DOCUMENTATION dominant | REJECT or ABSTAIN |
| STRONG symptom | SUPPORT/RECOVERY EXPLICIT | ACCEPT path `STRONG_PAID_SERVICE_PROBLEM_INTENT` |
| STRONG symptom | PROVIDER_HIRE STRONG + urgency | ACCEPT path |
| WEAK symptom | Strong commercial cluster | Case-by-case; document rationale |

---

## ACCEPT paths for problem queries

ACCEPT is permitted only when **paid provider path (I3)** is dominant **and** evidenced:

### Path A — Explicit support/recovery request

| Requirement | Example (RU) |
|-------------|--------------|
| `SUPPORT` or `RECOVERY` EXPLICIT | «вызвать специалиста 1с срочно» |
| Engagement verb + problem | «заказать восстановление базы после сбоя» |
| reason_code | `EXPLICIT_SUPPORT_RECOVERY_REQUEST` |

### Path B — Strong paid-service problem intent

| Requirement | Example (RU) |
|-------------|--------------|
| `PROBLEM` STRONG + `PROVIDER_HIRE` STRONG | «1с не работает вызвать мастера» |
| `URGENCY` + provider path | «срочно не проводит накладную нужен специалист» |
| DIY absent or clearly subordinate | No «самому», «как исправить» |
| reason_code | `STRONG_PAID_SERVICE_PROBLEM_INTENT` |

### Path C — Implementation/support scoped task

Problem embedded in broader commercial task:

- «после обновления 1с перестал работать обмен — нужна настройка подрядчиком» → `REQUEST_CONFIGURATION` / support cluster → ACCEPT with appropriate reason_code.

---

## REJECT paths for problem queries

| Dominant reading | reason_code | Example (RU) |
|------------------|-------------|--------------|
| DIY troubleshooting | `CLEAR_DIY_HOW_TO` | «1с ошибка 131 как исправить» |
| Documentation | `CLEAR_DIY_HOW_TO` or informational | «ошибка 1с расшифровка» |
| Educational | `CLEAR_EDUCATION` | «курс устранение ошибок 1с» |
| Free download fix | `FREE_DOWNLOAD_INTENT` | «скачать патч 1с бесплатно» |

---

## ABSTAIN paths (preferred over weak ACCEPT)

| Situation | reason_code |
|-----------|-------------|
| I1 and I3 equally plausible | `PROVIDER_DIY_CONFLICT` |
| Problem + head term | `SHORT_AMBIGUOUS_PHRASE` |
| Problem + product/service blur | `PRODUCT_SERVICE_CONFLICT` |
| Support vs information unclear | `SUPPORT_INFORMATION_CONFLICT` |
| All three interpretations viable, no winner | `COMPETING_INTENTS` |

---

## Anti-patterns

| Anti-pattern | Why wrong |
|--------------|-----------|
| «Есть проблема → пользователь купит услугу» | Assumes conversion without hire evidence |
| ACCEPT on «не работает 1с» alone | Problem-only; invariant violation risk |
| Ignoring DIY interpretation | Overblocks or underblocks asymmetrically |
| Rewriting query into commercial form | Invariant 19 — MALFORMED / no rewrite |
| Single interpretation documented | Fails three-interpretation protocol |

---

## Recording requirements

| Field | Content |
|-------|---------|
| `primary_intent` | Best task intent — may be `PROBLEM_UNRESOLVED` |
| `signals[]` | `PROBLEM` + any SUPPORT/RECOVERY/DIY with spans |
| `ambiguity.competing_interpretations` | Min three entries for problem-shaped phrases |
| `ambiguity.unresolved_questions` | Required for ABSTAIN — e.g. «DIY или вызов специалиста?» |
| `commercial_eligibility.opposing_evidence` | DIY / informational readings |

---

## Decision flow (summary)

```
PROBLEM signal detected?
  → Document I1, I2, I3
  → Is I3 dominant with STRONG/EXPLICIT commercial evidence?
       YES → ACCEPT (appropriate reason_code)
       NO → Is protected stratum dominant?
              YES → REJECT
              NO → ABSTAIN (default for unresolved problem phrases)
```

---

## Related documents

- [`ORCA-COMMERCIAL-EVIDENCE-STANDARD-v1.md`](ORCA-COMMERCIAL-EVIDENCE-STANDARD-v1.md)
- [`ORCA-ABSTAIN-STANDARD-v1.md`](ORCA-ABSTAIN-STANDARD-v1.md)
- [`ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md`](ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md)
