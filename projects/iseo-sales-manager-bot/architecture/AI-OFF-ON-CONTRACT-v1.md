# AI OFF / AI ON CONTRACT v1

**Product:** i-SEO Sales Manager Bot  
**Status:** documented processing contract

---

## 1. Shared principles

1. Deterministic pipeline **always** produces a complete CLEAN-capable result.
2. AI is optional enrichment layered on top.
3. Default `ai_enabled=false`.
4. Prefer **one** structured AI call per lead when ON.
5. Any AI failure → `ai_status=fallback`, `fallback_used=true`, continue with AI OFF result.
6. First reply is **never** auto-sent to clients.
7. Do not publish unvalidated AI text to Telegram.

---

## 2. AI OFF — complete deterministic logic

### 2.1 Outputs (always)

| Field | Source |
|-------|--------|
| Normalized client fields | Parser + cleanup rules |
| `service` | Deterministic service rules |
| `summary` | Truncated/cleaned request + service hint |
| `priority` | Heuristic |
| `quality_status` + `quality_comment` | Strict missing-field rules |
| `missing_fields` | Explicit list |
| `clarification_questions` | Template questions from missing fields |
| `manager_recommendation` | Next-step template |
| `first_reply_text` | Reply templates |
| `processing_mode` | `ai_off` |
| `ai_status` | `skipped` |
| `first_reply_source` | `template` |

### 2.2 Service classification rules

Evaluate in order; first match wins.

| Service | Signals (any strong match) |
|---------|----------------------------|
| **Audit** | `request_page` / `form_name` / subject / text contains аудит, seo-аудит, audit, проверка сайта; calculator audit flags |
| **SEO** | SEO, продвижение, поисковое, позиции, трафик, семантическое ядро (without stronger Audit) |
| **Direct** | Директ, контекст, Яндекс Директ, реклама в поиске, PPC |
| **Site** | создание сайта, разработка сайта, лендинг, сайт под ключ, редизайн (site build intent) |
| **Other** | No strong match |

**Inputs used:** `request_page`, `form_name`, `email_subject`, `request_text`, `calc_detected`/`calc_data`, keyword lists versioned with `reply_template_version` / parser pack.

### 2.3 Quality rules (stricter than current optimistic ok)

| Condition | `quality_status` |
|-----------|------------------|
| No usable contact (no phone, email, messenger) | `unusable` |
| Contact present but name **and** site missing **and** request_text &lt; 40 chars | `poor` |
| Contact present; missing name or site or thin request | `needs_data` |
| Contact + (name or site) + meaningful request | `ok` |

**Never** mark `ok` when name and site both missing unless contact+rich request (still prefer `needs_data`).

### 2.4 Priority heuristic

| Signal | Priority |
|--------|----------|
| Audit + site present | `high` |
| Repeat client (`duplicate_status=repeat`) | `high` or `normal` (prefer high if prior qualified) |
| Unusable quality | `low` |
| Default | `normal` |

### 2.5 Missing fields & questions

Map missing → questions (Russian), e.g.:

- name → «Как к вам обращаться?»
- site → «Укажите, пожалуйста, адрес сайта.»
- phone/email → «Как удобнее связаться: телефон или email?»
- service unclear → «Какая задача актуальна: аудит, SEO, Директ или сайт?»

### 2.6 Manager recommendation templates

Examples:

- `needs_data`: «Уточнить контакты/сайт перед КП; использовать вопросы ниже.»
- `ok` + Audit: «Подтвердить получение; уточнить цели аудита и доступ к Метрике/Вебмастеру.»
- `unusable`: «Не писать вслепую; найти контакт в письме/логах или закрыть как spam.»

### 2.7 First-reply templates

**With name:**

```
Здравствуйте, {name}!

Спасибо, ваша заявка получена{service_clause}.
Специалист свяжется с вами, чтобы уточнить задачу.

С уважением,
команда i-SEO
```

**Without name:**

```
Здравствуйте!

Спасибо, ваша заявка получена{service_clause}.
Менеджер свяжется с вами, чтобы уточнить задачу.

С уважением,
команда i-SEO
```

`service_clause` examples (only when service confident):

- Audit: « (запрос по аудиту сайта)»
- SEO: « (запрос по SEO)»
- Direct: « (запрос по контекстной рекламе)»
- Site: « (запрос по сайту)»
- Other / low confidence: omit clause

**Forbidden in templates:** prices, deadlines, guarantees, «одобрено», fake personalization, internal notes.

---

## 3. AI ON — single call contract

### 3.1 When called

- `ai_enabled=true` from CONFIG
- Deterministic result already computed (passed as context)
- One HTTP OpenRouter (or equivalent) request per lead

### 3.2 Required JSON output fields

```json
{
  "summary": "string",
  "service": "Audit|SEO|Direct|Site|Other",
  "priority": "low|normal|high",
  "quality_status": "ok|needs_data|poor|unusable",
  "quality_comment": "string",
  "missing_fields": ["name", "site"],
  "clarification_questions": ["..."],
  "manager_recommendation": "string",
  "first_reply_text": "string",
  "risk_flags": ["..."],
  "confidence": 0.0
}
```

### 3.3 Deterministic validation after AI

Reject / fallback if any fail:

| Check | Rule |
|-------|------|
| JSON parse | Must parse |
| Enums | Allowlists only |
| Required fields | All present; non-empty summary + first_reply_text |
| Max lengths | summary ≤ 600; reply ≤ 1200; comment ≤ 400; recommendation ≤ 400 |
| Forbidden promises | price/deadline/guarantee patterns in reply |
| No internal notes in reply | no “менеджеру:”, “internal”, “DEBUG” |
| No markdown noise | strip `` ` ``, `**`, headings; prefer plain text |
| No fabricated facts | if site/phone absent in input, AI must not invent them |
| Service | must be allowlisted; optional: must not contradict strong deterministic Audit/Direct without `risk_flags` |

On failure: keep AI OFF fields; set `processing_mode=ai_fallback`, `ai_status=fallback`, `fallback_used=true`, log ERRORS/`LEAD_EVENTS`.

### 3.4 Merge policy on success

- Prefer AI `summary`, `clarification_questions`, `manager_recommendation`, `first_reply_text` if validated.
- `service`: accept AI if valid; if deterministic was strong Audit/Direct and AI says Other with low confidence → keep deterministic + flag.
- `quality_status`: take **stricter** of AI vs deterministic (never upgrade unusable→ok via AI alone without contacts).
- `missing_fields`: union of deterministic + AI lists.
- `first_reply_source=ai`, `processing_mode=ai_on`, `ai_status=ok`.

### 3.5 Token / cost rule

- AI OFF path: **zero** provider calls.
- AI ON path: **one** call; no second normalizer call.

---

## 4. Failure matrix

| Failure | Behavior |
|---------|----------|
| Timeout | fallback |
| HTTP 4xx/5xx | fallback |
| Invalid JSON | fallback |
| Enum violation | fallback |
| Forbidden promise in reply | fallback (or strip+reject — prefer full fallback for simplicity) |
| Provider credential missing | fallback + error_code `ai_cred` |
| AI OFF mode | skip call entirely |

---

## 5. Observability

Always stamp CLEAN: `ai_enabled`, `ai_status`, `ai_model`, `fallback_used`, `processing_mode`.  
Telegram shows human processing mode line (see UX contract) — not raw JSON.

---

*Related: LEAD-DATA-MODEL-v1 · TELEGRAM-UX-CONTRACT-v1 · CONFIGURATION-MODEL-v1.*
