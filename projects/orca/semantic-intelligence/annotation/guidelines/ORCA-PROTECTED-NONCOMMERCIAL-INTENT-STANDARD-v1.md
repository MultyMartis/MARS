# ORCA Protected Non-Commercial Intent Standard v1

**Standard ID:** `orca-protected-noncommercial-intent-standard`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Defines adjudication rules for **protected strata** — intent classes where automated ACCEPT is disallowed or requires extreme conservatism. Aligns with P0-B `protected_class` on primary intents and invariants 3–4.

Protected strata exist to reduce **false positives** in paid acquisition: career, education, DIY, regulatory information, navigational, and free/download intents must not be silently overridden by weak commercial tokens.

---

## Protected class map

| protected_class | Primary intent(s) | Default eligibility posture |
|-----------------|-------------------|----------------------------|
| `career` | `CAREER_EMPLOYMENT` | REJECT when dominant |
| `educational` | `EDUCATIONAL` | REJECT when dominant |
| `diy_how_to` | `DIY_HOW_TO` | REJECT when dominant |
| `regulatory` | `REGULATORY` | REJECT when dominant (info-only) |
| `navigational` | `NAVIGATIONAL`, often `LOGIN_ACCOUNT_ACCESS` | REJECT when dominant |
| *(download/free)* | `DOWNLOAD_RESOURCE` | REJECT when dominant — see § Free/download |

All other intents carry `protected_class: null` but may still conflict with protected signals in mixed phrases.

---

## Dominant-intent rule

> **Eligibility follows the user's dominant next task, not the presence of a commercial keyword elsewhere in the phrase.**

### Dominance test (apply in order)

1. **Explicit protected marker** — EXPLICIT signal for career, education, DIY, regulatory, navigational, download/free → protected intent is candidate dominant.
2. **Task shape** — Does the phrase describe *getting a job*, *learning*, *doing it yourself*, *reading a law*, *opening a site*, or *downloading a file*?
3. **Commercial override check** — Is there an EXPLICIT commercial hire/implementation verb **scoped to the same task** that clearly supersedes the protected reading?
4. **Conflict** — If steps 1–3 yield comparable weight → **ABSTAIN** (`PROTECTED_SIGNAL_CONFLICT` or type-specific conflict), not ACCEPT.

**Annotators must not** assign ACCEPT to a phrase whose dominant reading is protected merely because a service-domain noun appears (e.g. «1с» + «курс» → educational dominates).

---

## Section: Career (`career`)

**Signals:** `CAREER_SEEKER`, `EMPLOYEE_HIRING`  
**Intent:** `CAREER_EMPLOYMENT`  
**REJECT reason_code:** `CLEAR_CAREER_SEEKER`

### Inclusion (dominant → REJECT)

| Pattern | Example (RU) |
|---------|--------------|
| Job seeker | «вакансия 1с программист москва» |
| Employment | «работа инженер по вентиляции» |
| Resume / salary | «резюме системный администратор», «зарплата 1с программист» |
| Employer hiring staff | «требуется программист 1с в штат» |

### Exclusion (not career-dominant)

| Pattern | Routing |
|---------|---------|
| «найти подрядчика» | Commercial — `HIRE_SERVICE` |
| «заказать монтаж» | Commercial — not career |
| Brand job page navigation | May be `NAVIGATIONAL` |

### Career vs provider conflict

| Query | Issue | Outcome |
|-------|-------|---------|
| «1с вакансия» | `CAREER_VS_PROVIDER` | ABSTAIN if both readings live |
| «работа монтаж вентиляции» | Ambiguous: job vs service domain | ABSTAIN — `CAREER_VS_PROVIDER` |
| «найти специалиста 1с» | Provider hire | ACCEPT path if evidence strong |

---

## Section: Employee hiring (within career stratum)

Employer-side hiring (`EMPLOYEE_HIRING`) is **protected** the same as seeker-side:

- «ищем инженера вентиляции в команду» → REJECT `CLEAR_CAREER_SEEKER`
- Not the same as «ищем подрядчика на монтаж» (commercial)

**Disambiguation cue:** *штат*, *в команду*, *сотрудник*, *вакансия от работодателя* → career. *подрядчик*, *аутсорс*, *на объект* → commercial.

---

## Section: Education (`educational`)

**Signal:** `EDUCATIONAL`  
**Intent:** `EDUCATIONAL`  
**REJECT reason_code:** `CLEAR_EDUCATION`

### Dominant educational patterns

| Pattern | Example (RU) |
|---------|--------------|
| Course / training | «курс 1с программирование» |
| Certification study | «сертификация 1с специалист» |
| Training for staff | «обучение crm для отдела продаж» |
| Tuition / учебный центр | «учебный центр 1с москва» |

### Not educational-dominant

| Pattern | Routing |
|---------|---------|
| «как настроить отчёт в 1с» | `DIY_HOW_TO` |
| «документация 1с» | `DOCUMENTATION_LOOKUP` |
| «заказать обучение с внедрением» | Mixed — adjudicate; training-only → REJECT; bundled paid project → case-by-case ABSTAIN |

**Rule:** `may_support_accept: false` on `EDUCATIONAL` — protected stratum cannot be ACCEPT target.

---

## Section: DIY (`diy_how_to`)

**Signal:** `DIY`  
**Intent:** `DIY_HOW_TO`  
**REJECT reason_code:** `CLEAR_DIY_HOW_TO`

### Dominant DIY patterns

| Pattern | Example (RU) |
|---------|--------------|
| How-to | «как настроить права в 1с» |
| Self-service | «настроить crm самому» |
| Instruction-seeking | «инструкция по настройке отчёта 1с» |

### Provider vs DIY conflict

| Query | Outcome |
|-------|---------|
| «монтаж вентиляции» | ABSTAIN — `PROVIDER_DIY_CONFLICT` |
| «заказать монтаж вентиляции» | ACCEPT — provider explicit |
| «монтаж вентиляции своими руками» | REJECT — DIY explicit |

---

## Section: Regulatory (`regulatory`)

**Signal:** `REGULATORY`  
**Intent:** `REGULATORY`  
**REJECT reason_code:** `CLEAR_REGULATORY_INFORMATION`

### Dominant regulatory (information-only)

| Pattern | Example (RU) |
|---------|--------------|
| Norm reference | «требования санпин к холодильному оборудованию» |
| Standard lookup | «гост на вентиляцию общепита» |
| Compliance question | «нужна ли лицензия на монтаж» |

### Regulatory vs implementation

| Query | Dominant read | Outcome |
|-------|---------------|---------|
| «заказать монтаж по санпин» | Commercial implementation | ACCEPT path — not regulatory-dominant |
| «санпин требования к вытяжке» | Regulatory info | REJECT |
| «аудит соответствия санпин» | `REQUEST_AUDIT_OR_DIAGNOSTIC` | Commercial path possible |

Use ambiguity type `REGULATORY_VS_IMPLEMENTATION` when unclear; default ABSTAIN if implementation verb absent.

---

## Section: Navigational (`navigational`)

**Signals:** `NAVIGATIONAL`, `LOGIN`  
**Intents:** `NAVIGATIONAL`, `LOGIN_ACCOUNT_ACCESS`  
**REJECT reason_code:** `CLEAR_NAVIGATION_LOGIN`

### Dominant navigational patterns

| Pattern | Example (RU) |
|---------|--------------|
| Official site | «сайт 1с официальный» |
| Brand lookup | «битрикс24 личный кабинет» |
| Company name only | «компания триумф манипулятор» |
| Login | «войти в 1с онлайн» |

### Brand + service ambiguity

| Query | Outcome |
|-------|---------|
| «1с» | ABSTAIN — head term |
| «заказать 1с внедрение» | ACCEPT — commercial dominates |
| «1с официальный сайт» | REJECT — navigational |

---

## Section: Free / download

**Signals:** `DOWNLOAD`, `FREE`  
**Intent:** `DOWNLOAD_RESOURCE`  
**REJECT reason_code:** `FREE_DOWNLOAD_INTENT`

### Dominant free/download patterns

| Pattern | Example (RU) |
|---------|--------------|
| Download | «скачать конфигурацию 1с» |
| Free resource | «1с бесплатно скачать» |
| Trial / demo file | «демо версия crm скачать» |
| Documentation PDF | «скачать руководство пользователя 1с» |

### Exceptions (not free-dominant)

| Pattern | Routing |
|---------|---------|
| «купить и скачать лицензию» | `BUY_PRODUCT_OR_MODULE` — product adjudication |
| «заказать поставку и установку» | Commercial — not download |

**Rule:** `FREE` + `DOWNLOAD` without commercial path → REJECT. Paid delivery of install media alone does not convert to service ACCEPT without hire evidence.

---

## Protected conflict → ABSTAIN matrix

| Condition | reason_code |
|-----------|-------------|
| Unresolved `CAREER_VS_PROVIDER` | `PROTECTED_SIGNAL_CONFLICT` |
| Unresolved `PROVIDER_VS_DIY` | `PROVIDER_DIY_CONFLICT` |
| Unresolved `PRODUCT_VS_SERVICE` | `PRODUCT_SERVICE_CONFLICT` |
| Unresolved `SUPPORT_VS_INFORMATION` | `SUPPORT_INFORMATION_CONFLICT` |
| Mixed protected + commercial, no winner | `PROTECTED_SIGNAL_CONFLICT` |
| `SHORT_HEAD_TERM` | `SHORT_AMBIGUOUS_PHRASE` |

Automated processing **must ABSTAIN** when mandatory ambiguity types remain unresolved ([`ORCA-AMBIGUITY-TAXONOMY-v1.md`](../../taxonomy/ORCA-AMBIGUITY-TAXONOMY-v1.md)).

---

## Human review norms

| protected_class | human_review_normally_required |
|-----------------|--------------------------------|
| career | true |
| educational | true |
| diy_how_to | false (clear DIY → REJECT) |
| regulatory | true |
| navigational | true |

High-risk protected false-positive → escalate per adjudication policy.

---

## Related documents

- [`ORCA-REJECT-STANDARD-v1.md`](ORCA-REJECT-STANDARD-v1.md)
- [`ORCA-ABSTAIN-STANDARD-v1.md`](ORCA-ABSTAIN-STANDARD-v1.md)
- [`../../taxonomy/ORCA-PRIMARY-INTENT-TAXONOMY-v1.md`](../../taxonomy/ORCA-PRIMARY-INTENT-TAXONOMY-v1.md)
- [`../../taxonomy/ORCA-AMBIGUITY-TAXONOMY-v1.md`](../../taxonomy/ORCA-AMBIGUITY-TAXONOMY-v1.md)
