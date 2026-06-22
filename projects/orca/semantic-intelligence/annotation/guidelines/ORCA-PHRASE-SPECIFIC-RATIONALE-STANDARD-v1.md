# ORCA Phrase-Specific Rationale Standard v1

**Standard ID:** `orca-phrase-specific-rationale-standard`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Every semantic eligibility decision (ACCEPT, REJECT, ABSTAIN) must include a **phrase-specific rationale** — human-readable explanation tied to the **exact query**, not reusable boilerplate. This standard governs `commercial_eligibility.phrase_explanation`, adjudication notes, and human review narratives.

Aligns with:

- Invariant 14 — no raw numeric sentinels in narrative fields
- Commercial eligibility `phrase_explanation` field
- ORCA campaign production contract: phrase-specific hypothesis discipline (documentation layer only — not campaign export in semantic record)

---

## Core rule

> **If the rationale could apply unchanged to a different query in the same service vertical, it is invalid.**

Annotators must write for **this phrase only**, citing **this phrase's tokens** and **this decision path**.

---

## Required six elements

Every complete `phrase_explanation` (or linked adjudication narrative) must contain **all six elements**. Use labeled sentences or short bullets — order flexible.

### Element 1 — Literal reading

**What the phrase says** without rewriting or correcting the user.

| Requirement | Detail |
|-------------|--------|
| Anchor | Quote or paraphrase `raw_query` / `normalized_query` |
| No rewrite | Do not «fix» typos into a different commercial query |
| Language | Match query language (RU for RU queries) |

**Example:** «Фраза «заказать внедрение crm под ключ» буквально запрашивает оформление проекта внедрения CRM с полным циклом работ исполнителем.»

### Element 2 — Dominant user task

**Most likely next task** expressed as `primary_intent` (and `likely_user_goal` if assigned).

| Requirement | Detail |
|-------------|--------|
| Taxonomy ID | Name intent from 27-intent vocabulary |
| Task framing | User action, not SEO category |
| Separation | Intent ≠ eligibility decision (state both) |

**Example:** «Доминирующая задача: `REQUEST_IMPLEMENTATION` — пользователь ищет выполнение внедрения, а не покупку коробки или обучение.»

### Element 3 — Commercial evidence from phrase

**Positive and negative evidence spans** with signal strength.

| Requirement | Detail |
|-------------|--------|
| Cite tokens | «заказать», «под ключ», «внедрение» |
| Signal IDs | PROVIDER_HIRE EXPLICIT, IMPLEMENTATION STRONG, etc. |
| Honesty | State absent evidence — «нет маркеров DIY/курса» |

**Example:** «EXPLICIT `PROVIDER_HIRE` на «заказать»; STRONG `IMPLEMENTATION` на «внедрение crm под ключ»; отсутствуют `EDUCATIONAL`, `DIY`, `CAREER_SEEKER`.»

### Element 4 — Paid traffic justification (or exclusion)

**Why ACCEPT is justified** for PPC **or** why paid traffic is **not** justified (REJECT/ABSTAIN).

| Decision | Content |
|----------|---------|
| ACCEPT | User likely to convert on service landing; task matches catalog |
| REJECT | User seeks free/education/job/product — paid click misaligned |
| ABSTAIN | Insufficient basis to spend; human must resolve conflict |

**Example (ACCEPT):** «Платный трафик оправдан: пользователь на этапе выбора исполнителя внедрения — соответствует сервисному лендингу.»

**Example (REJECT):** «Платный трафик не оправдан: доминирует поиск курса, не заказ услуги.»

### Element 5 — Rejected competing interpretation

**At least one plausible alternative** and why it was rejected or deferred.

| Decision | Content |
|----------|---------|
| ACCEPT | Why DIY/info/product readings are subordinate |
| REJECT | Why commercial reading (if any) fails |
| ABSTAIN | Name tied interpretations — do not pick winner |

**Example:** «Отвергнута интерпретация INFORMATIONAL («узнать цену без заказа»): присутствует явный глагол заказа, не только «стоимость».»

**Example (ABSTAIN):** «Конкурируют PROVIDER vs DIY: «монтаж вентиляции» не содержит глагола найма или самостоятельной инструкции — победитель не определён.»

### Element 6 — Decision linkage

Explicit binding to machine fields.

| Requirement | Detail |
|-------------|--------|
| decision | ACCEPT / REJECT / ABSTAIN |
| reason_code | Exact family code |
| Optional | confidence note, reviewer_required, seed ID |

**Example:** «Итог: `commercial_eligibility.decision: ACCEPT`, `reason_code: EXPLICIT_PROVIDER_REQUEST`, confidence 0.91.»

---

## Prohibited generic rationales

The following patterns are **invalid** as standalone or primary explanations:

| Prohibited pattern | Why invalid |
|--------------------|-------------|
| «Релевантно услуге» | No phrase anchor |
| «Коммерческий запрос» | No evidence |
| «Не коммерческий» | No stratum/code |
| «Подходит для кампании» | Campaign field leakage |
| «Высокочастотный ключ» | Volume ≠ intent |
| «По опыту пользователи хотят внедрение» | SERP/population prior |
| «Тематика 1С» | Topic match — invariant 1 |
| «ACCEPT по умолчанию» | Policy violation |
| «REJECT — мусор» | Use MALFORMED/IRRELEVANT with basis |
| «ABSTAIN — неясно» | Fails unresolved_questions discipline |
| «См. аналогичный кейс» | Not phrase-specific |
| Raw sentinels `1234`, `970`, etc. | Invariant 14 |

---

## Quality rubric

| Grade | Criteria |
|-------|----------|
| **Pass** | All 6 elements; phrase tokens cited; reason_code stated; no prohibited generics |
| **Revise** | Missing element or generic boilerplate section |
| **Fail** | Could swap query text without changing rationale; or contains sentinels |

---

## Examples by decision

### ACCEPT — «заказать внедрение crm под ключ»

1. **Literal:** Запрос на заказ полного цикла внедрения CRM.
2. **Task:** `REQUEST_IMPLEMENTATION` / hire-provider goal.
3. **Evidence:** `PROVIDER_HIRE` EXPLICIT «заказать»; `IMPLEMENTATION` STRONG «внедрение crm под ключ»; нет protected signals.
4. **Paid traffic:** Пользователь на стадии привлечения исполнителя — соответствует PPC сервиса.
5. **Rejected:** INFORMATIONAL отвергнут — нет запроса «сколько стоит» без заказа.
6. **Linkage:** ACCEPT, `EXPLICIT_PROVIDER_REQUEST`.

### REJECT — «курс 1с программирование»

1. **Literal:** Поиск обучающей программы по программированию 1С.
2. **Task:** `EDUCATIONAL`.
3. **Evidence:** `EDUCATIONAL` EXPLICIT «курс»; commercial hire отсутствует.
4. **Paid traffic:** Не оправдан для сервисного лендинга — intent обучение.
5. **Rejected:** Коммерческое внедрение отвергнуто — нет глаголов заказа/внедрения.
6. **Linkage:** REJECT, `CLEAR_EDUCATION`.

### ABSTAIN — «1с»

1. **Literal:** Однотокенный head-term домена 1С без задачи.
2. **Task:** Не назначается уверенно — кандидаты BUY / HIRE / NAVIGATIONAL.
3. **Evidence:** Только WEAK topical; нет STRONG/EXPLICIT commercial path.
4. **Paid traffic:** Нельзя обосновать расход без угадывания задачи.
5. **Rejected/deferred:** Все конкурирующие интерпретации остаются открытыми.
6. **Linkage:** ABSTAIN, `SHORT_AMBIGUOUS_PHRASE`; вопрос: «Покупка, внедрение или навигация?»

---

## Field mapping

| Narrative use | Schema field |
|---------------|--------------|
| Primary rationale | `commercial_eligibility.phrase_explanation` |
| Competing reads | `ambiguity.competing_interpretations[]` |
| Open questions | `ambiguity.unresolved_questions[]` |
| Evidence lists | `supporting_evidence`, `opposing_evidence` |
| Human review | `review.review_notes` (supplement, not substitute) |

---

## Automation note

LLM-generated rationales must be **validated** against this rubric by human reviewers or QA gates. Template-filled rationales fail P0-C quality gates.

---

## Related documents

- [`ORCA-ACCEPT-STANDARD-v1.md`](ORCA-ACCEPT-STANDARD-v1.md) — R7
- [`ORCA-REJECT-STANDARD-v1.md`](ORCA-REJECT-STANDARD-v1.md) — RR5
- [`ORCA-ABSTAIN-STANDARD-v1.md`](ORCA-ABSTAIN-STANDARD-v1.md)
- [`../../schemas/ORCA-SEMANTIC-NULL-UNKNOWN-POLICY-v1.md`](../../schemas/ORCA-SEMANTIC-NULL-UNKNOWN-POLICY-v1.md)
