# ORCA REJECT Standard v1

**Standard ID:** `orca-reject-standard`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Defines when `commercial_eligibility.decision` must be **REJECT** — confident exclusion from paid acquisition semantic core. REJECT is appropriate when the **dominant user task** is incompatible with service PPC goals and ambiguity is **not** material.

Aligns with REJECT reason families in [`ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md`](../../taxonomy/ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md) and invariant 5.

---

## Core rule

> **REJECT requires confident dominant non-commercial or out-of-scope reading.**

When dominance is not confident → **ABSTAIN**, not REJECT. REJECT is not a shortcut to clear the queue.

---

## REJECT requirements

Every REJECT record must satisfy **all** of the following.

### RR1 — Dominant intent incompatible

The user's most likely next task is:

- Protected non-commercial stratum (career, education, DIY, regulatory info, navigational, free/download), **or**
- Product-only purchase outside service campaign scope, **or**
- Irrelevant/malformed query, **or**
- Unsupported service / landing mismatch

### RR2 — Valid REJECT reason_code (mandatory)

Invariant 5: REJECT **always** requires `reason_code` from REJECT family.

| reason_code | When to use |
|-------------|-------------|
| `CLEAR_EDUCATION` | Dominant `EDUCATIONAL` |
| `CLEAR_CAREER_SEEKER` | Dominant `CAREER_EMPLOYMENT` |
| `CLEAR_DIY_HOW_TO` | Dominant `DIY_HOW_TO` / self-service |
| `CLEAR_REGULATORY_INFORMATION` | Dominant `REGULATORY` without implementation |
| `CLEAR_NAVIGATION_LOGIN` | Dominant `NAVIGATIONAL` / `LOGIN_ACCOUNT_ACCESS` |
| `FREE_DOWNLOAD_INTENT` | Dominant `DOWNLOAD_RESOURCE` + free |
| `INCOMPATIBLE_PRODUCT_ONLY_INTENT` | Dominant `BUY_PRODUCT_OR_MODULE` |
| `IRRELEVANT` | Dominant `IRRELEVANT` |
| `MALFORMED` | Dominant `MALFORMED` |
| `UNSUPPORTED_SERVICE` | Commercial but not in catalog |
| `LANDING_MISMATCH` | Commercial intent incompatible with landing scope |

### RR3 — Documented supporting evidence

`commercial_eligibility.supporting_evidence` must cite phrase spans proving dominant protected or incompatible reading (e.g. «вакансия», «курс», «скачать бесплатно»).

### RR4 — Opposing commercial evidence assessed

If commercial tokens appear, `opposing_evidence` must explain why they are **subordinate** or **insufficient** — not ignored.

| Query | Why still REJECT |
|-------|------------------|
| «курс 1с программирование» | EDUCATIONAL EXPLICIT dominates |
| «вакансия 1с москва» | CAREER dominates — «1с» is domain not hire |
| «скачать 1с бесплатно» | DOWNLOAD+FREE dominates |

If commercial reading is equally strong → ABSTAIN, not REJECT.

### RR5 — Phrase-specific rationale

Meet six-element rationale standard; REJECT narratives must state **what task is excluded** and **why paid traffic is not justified**.

### RR6 — No query rewrite

Invariant 19: do not REJECT MALFORMED then invent a synthetic commercial query. MALFORMED stays MALFORMED.

### RR7 — Confidence appropriate to REJECT

`commercial_eligibility.confidence` should reflect confident exclusion. Low confidence + material ambiguity → ABSTAIN instead.

---

## Protected stratum REJECT quick reference

| Stratum | Example (RU) | reason_code |
|---------|--------------|-------------|
| Education | «курс 1с программирование» | `CLEAR_EDUCATION` |
| Career seeker | «вакансия 1с программист» | `CLEAR_CAREER_SEEKER` |
| Employer hiring | «требуется 1с в штат» | `CLEAR_CAREER_SEEKER` |
| DIY | «как настроить 1с самому» | `CLEAR_DIY_HOW_TO` |
| Regulatory info | «санпин вентиляция общепит» | `CLEAR_REGULATORY_INFORMATION` |
| Navigational | «1с официальный сайт» | `CLEAR_NAVIGATION_LOGIN` |
| Login | «войти в 1с онлайн» | `CLEAR_NAVIGATION_LOGIN` |
| Free download | «скачать конфигурацию 1с бесплатно» | `FREE_DOWNLOAD_INTENT` |

See [`ORCA-PROTECTED-NONCOMMERCIAL-INTENT-STANDARD-v1.md`](ORCA-PROTECTED-NONCOMMERCIAL-INTENT-STANDARD-v1.md).

---

## Product and scope REJECT

| Situation | reason_code | Example (RU) |
|-----------|-------------|--------------|
| Product SKU only | `INCOMPATIBLE_PRODUCT_ONLY_INTENT` | «купить 1с бухгалтерию» |
| Wrong vertical | `IRRELEVANT` | «купить холодильник бытовой» (non-campaign) |
| Service not in catalog | `UNSUPPORTED_SERVICE` | Commercial but unmapped service |
| Landing scope violation | `LANDING_MISMATCH` | Service intent ≠ landing offer |

---

## REJECT vs ABSTAIN decision guide

| Condition | Outcome |
|-----------|---------|
| EXPLICIT protected marker, no rival interpretation | **REJECT** |
| Protected vs commercial genuinely tied | **ABSTAIN** |
| Head term without disambiguation | **ABSTAIN** — not REJECT |
| DIY vs provider tied | **ABSTAIN** |
| Product vs service tied | **ABSTAIN** |
| Informational quote only | **REJECT** or **ABSTAIN** — if quote could precede hire, prefer ABSTAIN |

---

## Anti-patterns

| Anti-pattern | Why wrong | Correct |
|--------------|-----------|---------|
| REJECT «1с» as irrelevant noise | Domain term — uncertain | ABSTAIN short head |
| REJECT ambiguous phrase to reduce queue | Overblocking risk | ABSTAIN |
| REJECT without reason_code | Invariant 5 violation | Add reason_code |
| «Не коммерческий» without stratum | Generic rationale | Use CLEAR_* code + spans |
| REJECT because campaign doesn't want education | Correct — but document EDUCATIONAL dominance | `CLEAR_EDUCATION` |
| Ignore embedded commercial verb | Under-explain | RR4 opposing evidence |
| Upgrade REJECT to ACCEPT on reviewer hunch | Needs evidence | ACCEPT standard |

---

## High-risk REJECT review

Set `reviewer_required: true` when:

- REJECT on borderline informational vs commercial
- REJECT `INCOMPATIBLE_PRODUCT_ONLY_INTENT` on 2-token product names
- Risk flag `NEGATIVE_OVERBLOCKING` elevated
- Any disagreement with prior AUTO_ACCEPT_CANDIDATE

Human override must preserve `audit.prior_decision` (invariant 12).

---

## Recording checklist

- [ ] `decision: REJECT`
- [ ] `reason_code` from REJECT family
- [ ] `primary_intent` matches dominant incompatible task
- [ ] `signals[]` with protected/incompatible EXPLICIT where present
- [ ] `supporting_evidence` with spans
- [ ] `opposing_evidence` if commercial tokens present
- [ ] `phrase_explanation` — six elements
- [ ] No campaign/cluster/export fields (invariants 10–11)

---

## Examples (RU)

| Query | decision | reason_code |
|-------|----------|-------------|
| «курс 1с программирование» | REJECT | `CLEAR_EDUCATION` |
| «вакансия 1с москва» | REJECT | `CLEAR_CAREER_SEEKER` |
| «как настроить отчёт 1с» | REJECT | `CLEAR_DIY_HOW_TO` |
| «скачать 1с бесплатно» | REJECT | `FREE_DOWNLOAD_INTENT` |
| «сайт 1с официальный» | REJECT | `CLEAR_NAVIGATION_LOGIN` |
| «купить лицензию 1с erp» | REJECT | `INCOMPATIBLE_PRODUCT_ONLY_INTENT` |
| «1с» | ABSTAIN | — (not REJECT) |
| «монтаж вентиляции» | ABSTAIN | — (not REJECT) |

---

## Related documents

- [`ORCA-PROTECTED-NONCOMMERCIAL-INTENT-STANDARD-v1.md`](ORCA-PROTECTED-NONCOMMERCIAL-INTENT-STANDARD-v1.md)
- [`ORCA-ABSTAIN-STANDARD-v1.md`](ORCA-ABSTAIN-STANDARD-v1.md)
- [`ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md`](ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md)
