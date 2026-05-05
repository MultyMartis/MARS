# SEO Content Agent — MVP Outline v1 — n8n build specification

**Workflow name:** `SEO Content Agent — MVP Outline v1`

**Document status:** **specification only** — implementation-ready build plan for n8n. **No** workflow import JSON, **no** credentials, **no** production secrets, **no** assertion that this graph exists in any environment.

**Purpose:** Telegram command **`/outline`** → **Parse Task** → **Build Outline** → **QA Outline** → Telegram result (human-readable outline + QA signals).

**Related docs:** [runtime-mvp-outline.md](runtime-mvp-outline.md), [data-schema.md](data-schema.md), [prompts.md](prompts.md), [workflows.md](workflows.md).

---

## 1. Environment variables (required)

| Variable | Role |
|----------|------|
| `OPENROUTER_API_KEY` | API key for OpenRouter (stored in n8n env or secret backend — **not** in this file). |
| `OPENROUTER_PARSE_MODEL` | Model id for Parse Task (e.g. provider slug from OpenRouter catalog — **exact value SAFE UNKNOWN** until chosen). |
| `OPENROUTER_OUTLINE_MODEL` | Model id for Build Outline. |
| `OPENROUTER_QA_MODEL` | Model id for QA Outline. |

**SAFE UNKNOWN:** Whether n8n reads these via `$env` in expressions, Credential fields, or external secrets injectors — depends on deployment.

---

## 2. n8n credentials (required)

| Credential | Use |
|------------|-----|
| **Telegram Bot API** | Telegram Trigger + Send Message nodes (bot token — **never** commit). |
| **OpenRouter** | Either **HTTP Header Auth** credential (header `Authorization`, value `Bearer …`) **or** env-based header assembly in HTTP Request nodes — **pattern SAFE UNKNOWN** per org policy. |

**Rule:** Do not embed raw API keys in node JSON exports; reference credentials or `$env.OPENROUTER_API_KEY` per runbook.

---

## 3. Workflow graph (execution order)

```text
Telegram Trigger
  → Set: Raw Input
  → HTTP Request: OpenRouter Parse Task
  → Code: Extract Parsed Task JSON
  → HTTP Request: OpenRouter Build Outline
  → Code: Extract Outline JSON
  → HTTP Request: OpenRouter QA Outline
  → Code: Format Telegram Message
  → Telegram: Send Message
```

---

## 4. Node definitions

Convention: **input** / **output** describe logical data passed along the chain. **Expressions** use n8n `{{ }}` style where illustrative; items marked **SAFE UNKNOWN** must be validated against the live Telegram Trigger output shape and OpenRouter response envelope on first run.

---

### 4.1 Telegram Trigger

| Field | Value |
|-------|--------|
| **Node name** | `Telegram Trigger` (or project prefix + `TG /outline`) |
| **Type** | `n8n-nodes-base.telegramTrigger` |
| **Input** | Incoming Telegram webhook / polling update (raw). |
| **Output** | Fields such as message text, `chat.id`, `from.id`, `message_id` — **exact property paths SAFE UNKNOWN** (depend on n8n node version and update type). |
| **Key settings** | Bot credential attached; updates: `message`; optional filter so only `/outline` starts the workflow (**filter mechanism SAFE UNKNOWN**: Trigger filter vs IF node). |
| **Expressions** | **SAFE UNKNOWN:** e.g. `{{ $json.message.text }}` vs nested `edited_message` — confirm in execution preview. |
| **Failure notes** | Webhook misconfiguration, invalid token, Telegram outage — workflow does not start; user sees nothing unless a separate health path exists. |

---

### 4.2 Set: Raw Input

| Field | Value |
|-------|--------|
| **Node name** | `Set: Raw Input` |
| **Type** | `n8n-nodes-base.set` |
| **Input** | Telegram Trigger output. |
| **Output** | Canonical fields for the run, e.g. `task_raw`, `chat_id`, `reply_to_message_id` (optional). |
| **Key settings** | Assign `task_raw` to full user message text; strip or keep `/outline` prefix per product rule (**SAFE UNKNOWN**). |
| **Expressions** | Example intent only: `task_raw` ← **SAFE UNKNOWN:** `{{ $json.message.text }}`; `chat_id` ← **SAFE UNKNOWN:** `{{ $json.message.chat.id }}`. |
| **Failure notes** | Empty message, non-text update — downstream may error; consider optional IF guard (**out of scope** unless added). |

---

### 4.3 HTTP Request: OpenRouter Parse Task

| Field | Value |
|-------|--------|
| **Node name** | `HTTP Request: OpenRouter Parse Task` |
| **Type** | `n8n-nodes-base.httpRequest` |
| **Input** | `task_raw`, `chat_id`, passthrough from Set. |
| **Output** | OpenRouter HTTP response body (JSON). Typical path to completion: **SAFE UNKNOWN** — often `choices[0].message.content` (string, may be JSON string). |
| **Key settings** | Method `POST`; URL `https://openrouter.ai/api/v1/chat/completions` (**verify** against current OpenRouter docs); JSON body; auth header from credential or expression; timeout and retry (**values SAFE UNKNOWN**). |
| **Expressions** | Model: `{{ $env.OPENROUTER_PARSE_MODEL }}` (**or** static — **SAFE UNKNOWN**). Inject `task_raw` into user message per §7.1 / §8.1. |
| **Failure notes** | 401/403, 429, 5xx, empty `choices` — no `task_normalized`; implement Error Workflow or `onError` strategy (**SAFE UNKNOWN**). |

---

### 4.4 Code: Extract Parsed Task JSON

| Field | Value |
|-------|--------|
| **Node name** | `Code: Extract Parsed Task JSON` |
| **Type** | `n8n-nodes-base.code` |
| **Input** | HTTP response from Parse Task. |
| **Output** | `task_parsed` (raw model object), `task_normalized` (minimal MVP shape per [runtime-mvp-outline.md](runtime-mvp-outline.md) §5), plus passthrough `chat_id`. |
| **Key settings** | Mode: Run Once for All Items or per item — **SAFE UNKNOWN**; language JavaScript. |
| **Expressions** | N/A inside Code; access items via `items[0].json` — **exact path to OpenRouter body SAFE UNKNOWN**. |
| **Failure notes** | Model returns non-JSON or JSON wrapped in markdown fences — parser should strip fences or set error flag (**logic SAFE UNKNOWN**). Missing required fields → fill with `SAFE_UNKNOWN` / `[]` / `""` per schema policy. |

**Minimal `task_normalized` target shape (MVP-1):**

```json
{
  "task_type": "outline",
  "topic": "",
  "keywords": [],
  "page_type": "",
  "region": "",
  "tone": "",
  "brief": ""
}
```

---

### 4.5 HTTP Request: OpenRouter Build Outline

| Field | Value |
|-------|--------|
| **Node name** | `HTTP Request: OpenRouter Build Outline` |
| **Type** | `n8n-nodes-base.httpRequest` |
| **Input** | `task_normalized`, optional `task_raw`. |
| **Output** | OpenRouter response; outline JSON in assistant content — **envelope SAFE UNKNOWN**. |
| **Key settings** | Same host/path family as Parse; model from `OPENROUTER_OUTLINE_MODEL`. |
| **Expressions** | Serialize `task_normalized` into user prompt (stringify JSON) — **SAFE UNKNOWN:** `$json.task_normalized` vs `$node["Code: Extract Parsed Task JSON"].json`. |
| **Failure notes** | Same class as Parse; partial outline — QA may still run with explicit `MISSING_DATA` in prompt context. |

---

### 4.6 Code: Extract Outline JSON

| Field | Value |
|-------|--------|
| **Node name** | `Code: Extract Outline JSON` |
| **Type** | `n8n-nodes-base.code` |
| **Input** | Build Outline HTTP response. |
| **Output** | `outline` object aligned with `outline` in [data-schema.md](data-schema.md) (subset acceptable for MVP if documented), plus passthrough `task_normalized`, `chat_id`. |
| **Key settings** | Extract assistant content; parse JSON; optional key checks (`h1`, `sections`) — **strict validator SAFE UNKNOWN**. |
| **Expressions** | **SAFE UNKNOWN** — implement in Code only. |
| **Failure notes** | Invalid JSON → downstream QA fails; prefer user-facing error message path (**not specified** in MVP doc). |

---

### 4.7 HTTP Request: OpenRouter QA Outline

| Field | Value |
|-------|--------|
| **Node name** | `HTTP Request: OpenRouter QA Outline` |
| **Type** | `n8n-nodes-base.httpRequest` |
| **Input** | `outline`, `task_normalized`. |
| **Output** | OpenRouter response with QA result JSON in content — **schema §7.3 / §8.3**. |
| **Key settings** | Model `OPENROUTER_QA_MODEL`. |
| **Expressions** | Pass stringified `outline` + `task_normalized` into user content — **SAFE UNKNOWN** cross-node references. |
| **Failure notes** | QA timeout — operator may retry; no automatic partial send unless designed (**SAFE UNKNOWN**). |

---

### 4.8 Code: Format Telegram Message

| Field | Value |
|-------|--------|
| **Node name** | `Code: Format Telegram Message` |
| **Type** | `n8n-nodes-base.code` |
| **Input** | QA Outline HTTP response **and** passthrough `outline` / `task_normalized` / `chat_id` if needed for context (**which branches to read SAFE UNKNOWN** — may require Merge node or carry-forward fields in prior nodes). |
| **Output** | `telegram_text` (final string), `chat_id`, optional `parse_mode`. |
| **Key settings** | Parse QA JSON from response; merge QA verdict/issues with outline headings for display; enforce Telegram length limit with truncation or split (**strategy SAFE UNKNOWN** — may need second Send node). |
| **Expressions** | **SAFE UNKNOWN** — implement in Code. |
| **Failure notes** | If QA returns invalid JSON, fall back to “outline only + error stub” (**policy SAFE UNKNOWN**). |

---

### 4.9 Telegram: Send Message

| Field | Value |
|-------|--------|
| **Node name** | `Telegram: Send Message` |
| **Type** | `n8n-nodes-base.telegram` |
| **Input** | `telegram_text`, `chat_id`. |
| **Output** | Telegram API acknowledgment (`message_id`, etc.). |
| **Key settings** | Operation: send message; `chatId` from expression; `text` from `telegram_text`; `parse_mode` if using Markdown/HTML — **SAFE UNKNOWN** (see §9). |
| **Expressions** | **SAFE UNKNOWN:** `{{ $json.chat_id }}`, `{{ $json.telegram_text }}`. |
| **Failure notes** | Message too long, Markdown parse errors, bot blocked by user — handle errors and logging (**SAFE UNKNOWN**). |

---

## 5. OpenRouter request body examples

**Shared notes:**

- Replace `MODEL_ID_*` with `$env.OPENROUTER_*_MODEL` at runtime.
- **SAFE UNKNOWN:** optional headers `HTTP-Referer`, `X-Title` per OpenRouter policy.
- Messages array uses `role` `system` | `user` with content strings (or multi-part — **if supported SAFE UNKNOWN**).

### 5.1 Parse Task (example body)

```json
{
  "model": "MODEL_ID_PARSE",
  "messages": [
    {
      "role": "system",
      "content": "FULL_PROMPT_TEXT_PARSE_TASK"
    },
    {
      "role": "user",
      "content": "USER_BRIEF_TEXT_FROM_task_raw"
    }
  ],
  "temperature": 0.2,
  "response_format": { "type": "json_object" }
}
```

**SAFE UNKNOWN:** Whether `response_format` is supported for the chosen model on OpenRouter — verify before production.

### 5.2 Build Outline (example body)

```json
{
  "model": "MODEL_ID_OUTLINE",
  "messages": [
    {
      "role": "system",
      "content": "FULL_PROMPT_TEXT_BUILD_OUTLINE"
    },
    {
      "role": "user",
      "content": "TASK_NORMALIZED_JSON_STRING"
    }
  ],
  "temperature": 0.4,
  "response_format": { "type": "json_object" }
}
```

### 5.3 QA Outline (example body)

```json
{
  "model": "MODEL_ID_QA",
  "messages": [
    {
      "role": "system",
      "content": "FULL_PROMPT_TEXT_QA_OUTLINE"
    },
    {
      "role": "user",
      "content": "OUTLINE_PLUS_TASK_CONTEXT_STRING"
    }
  ],
  "temperature": 0.2,
  "response_format": { "type": "json_object" }
}
```

---

## 6. Full prompt texts

### 6.1 Parse Task — system + user template

**System (full text):**

```text
You are a task normalizer for an internal SEO content pipeline. The user invoked /outline from Telegram. Extract structured fields from the user message only. Do not add SEO strategy the user did not imply. Do not invent facts, prices, deadlines, certifications, or client names.

Output rules:
- Output a single JSON object only (no markdown fences, no commentary).
- Use keys exactly as specified below.
- For any required scalar you cannot derive from the message, use the string "SAFE_UNKNOWN" or empty array [] as appropriate.
- List "assumptions" only when you must interpret ambiguous text; keep them minimal. If an assumption is risky, set "needs_confirmation": true.
- If the brief is too vague or contradictory, add a system-level note in "parse_notes" (string) and optionally include "LOW_INPUT_QUALITY" in "signals" (array of strings).

Required JSON shape:
{
  "task_type": "outline",
  "topic": "string",
  "keywords": ["string"],
  "page_type": "landing | blog | category | comparison | service | article | SAFE_UNKNOWN",
  "region": "string or SAFE_UNKNOWN",
  "tone": "string or SAFE_UNKNOWN",
  "brief": "string — full normalized brief text for downstream steps",
  "locale": "e.g. ru-RU or SAFE_UNKNOWN",
  "assumptions": [ { "text": "string", "needs_confirmation": true } ],
  "missing_data": ["string — gaps that limit outline quality"],
  "signals": ["optional: MISSING_DATA, LOW_INPUT_QUALITY, ..."]
}

Do not fetch URLs, do not read external links beyond treating them as opaque text if pasted.
```

**User (template):** raw Telegram text from `task_raw` (single message body).

---

### 6.2 Build Outline — system + user template

**System (full text):**

```text
You build SEO outlines for experienced copywriters. You receive a JSON object "task_normalized" describing topic, keywords, page type, tone, locale, and brief text.

Rules:
- Use only information present in task_normalized (including its "brief"). If data is missing, reflect gaps in outline.missing_data and in section content_notes (e.g. "REQUIRES_DATA: ..."). Never invent product specs, statistics, legal claims, or testimonials.
- Output a single JSON object only (no markdown fences, no commentary).
- Commercial SEO structure: one H1, logical H2/H3, intent-aligned sections, CTA plan, FAQ block when appropriate for the page type.
- No keyword stuffing in headings; primary keyword in H1 or first H2 only if natural.
- Match language to locale when set; if locale is SAFE_UNKNOWN, match the language of the brief text.

Required JSON shape (align fields to your pipeline; omit nulls):
{
  "outline_id": "generate a short id string or use OUTLINE_LOCAL",
  "task_id": "SAFE_UNKNOWN",
  "status": "draft",
  "title_options": ["string"],
  "h1": "string",
  "meta_description_plan": "string — intent and constraints, not necessarily final 160 chars",
  "sections": [
    {
      "level": 2,
      "heading": "string",
      "intent": "string",
      "key_points": ["string"],
      "target_keywords": ["string"],
      "content_notes": ["string"],
      "word_count_target": 0
    }
  ],
  "faq": [ { "question": "string", "answer_brief": "string" } ],
  "cta": { "placement": "string", "copy_direction": "string" },
  "missing_data": ["string"],
  "internal_risks": ["string"]
}

If sections need nested H3, use "level": 3 for those entries.
```

**User (template):**

```text
task_normalized (JSON):\nTASK_NORMALIZED_JSON_STRING
```

---

### 6.3 QA Outline — system + user template

**System (full text):**

```text
You are a conservative SEO editor reviewing an outline before writing. You receive the outline JSON and the original task_normalized JSON.

Tasks:
- Check heading hierarchy (single H1, sensible H2/H3), intent coverage for stated page type, keyword naturalness, CTA realism, FAQ relevance.
- Flag unsupported claims implied by headings or key_points that are not in the brief.
- Do not rewrite the entire outline unless small fixes clearly improve consistency; prefer a structured report.

Output a single JSON object only (no markdown fences, no commentary), shape:
{
  "verdict": "pass | pass_with_warnings | fail",
  "summary": "short RU or match brief language",
  "issues": [
    {
      "issue_id": "string",
      "severity": "info | warn | fail",
      "category": "structure | intent | keywords | compliance | other",
      "detail": "string",
      "suggested_fix": "string or SAFE_UNKNOWN"
    }
  ],
  "outline": { ... },
  "missing_data": ["string"],
  "keyword_spam_risk": "low | medium | high",
  "signals": ["optional: MISSING_DATA, LOW_INPUT_QUALITY"]
}

The "outline" object must be the full revised outline after your edits. If you make no structural edits, copy the input outline and only adjust content_notes / missing_data if needed.
```

**User (template):**

```text
task_normalized (JSON):\nTASK_NORMALIZED_JSON_STRING\n\noutline (JSON):\nOUTLINE_JSON_STRING
```

---

## 7. Final Telegram Markdown format

**Parse mode:** **SAFE UNKNOWN** — Telegram supports `Markdown`, `MarkdownV2`, `HTML`; escaping rules differ. Validate with a real bot before locking.

**Recommended human-readable layout (example):**

```markdown
*SEO Outline — MVP*

*H1:* …

*Title options*
• …
• …

*Meta description plan*
…

*Structure*
*1.* … — ~… слов; ключи: …
*1.1.* …

*FAQ*
• …

*CTA*
…

*QA:* pass_with_warnings
*Резюме QA:* …

*Замечания*
• [warn] …

*Пробелы данных*
• …

_Факты только из брифа. Публикация после проверки человеком._
```

**SAFE UNKNOWN:**

- Whether to use bold/italic with `*` vs `**` depends on `parse_mode`.
- Bullet and numbering may need adjustment for MarkdownV2 escaping.
- Truncation if message exceeds Telegram limit (~4096 characters — **confirm** in current API docs).

---

## 8. Limitations (MVP-1 explicit)

- **No URL parsing** — URLs in user text are not fetched or interpreted as machine-readable sources.
- **No external source fetching** — no HTTP crawler, no SERP, no competitor pages.
- **No storage** — no database or file persistence of tasks/outlines in this workflow.
- **No version history** — no outline versioning or diff across runs.
- **No competitor analysis** — no comparative SERP or competitor structure.

---

## 9. Test input examples (Russian)

### 9.1 Service page (услуга)

```text
/outline
Тип: страница услуги
Услуга: аудит безопасности облачной инфраструктуры для финтеха
Регион: РФ
Интент: коммерческий, B2B
Ключи: аудит облачной безопасности, соответствие 152-ФЗ, финтех
Аудитория: CTO, CISO среднего банка
Тон: деловой, без обещаний «100% защита»
Ограничения: не указывать цены и сроки — в брифе нет цифр
Дополнительно: упомянуть этапы работ на высоком уровне, без детальных методик
```

### 9.2 Category page (категория)

```text
/outline
Тип: категория интернет-магазина
Категория: промышленные насосы для водоснабжения
Интент: коммерческий обзор + подбор моделей
Ключи: насосы для водоснабжения, промышленные насосы, подбор насосного оборудования
Аудитория: инженеры снабжения и эксплуатации на предприятиях
Тон: технический, но понятный
Ограничения: не перечислять конкретные бренды и артикулы — данных нет
Нужны блоки: критерии выбора, типовые ошибки, FAQ для закупки
```

### 9.3 Article (статья / экспертный материал)

```text
/outline
Тип: статья / блог
Тема: как снизить риски ошибок при миграции в облако для госсектора
Интент: информационный с элементами экспертизы
Ключи: миграция в облако, госсектор, управление рисками, compliance
Аудитория: руководители ИТ в госкомпаниях
Тон: нейтрально-деловой, без политических оценок
Ограничения: не ссылаться на реальные проекты и заказчиков; статистику не выдумывать
Объём планируемого текста: средний (ориентир 6000–9000 знаков)
```

---

## 10. Manual QA checklist (after first n8n run)

Use this once the graph is wired and test messages are sent (no automation implied).

1. **Trigger:** Sending `/outline` with brief text starts exactly one run; non-command messages do not start it (**unless policy says otherwise** — **SAFE UNKNOWN**).
2. **Parse:** Response JSON validates; `task_normalized` fields populate; `missing_data` appears when brief is intentionally thin.
3. **Outline:** `h1` and `sections` exist; `word_count_target` is numeric; `missing_data` lists gaps for missing facts test case.
4. **QA:** `verdict` and `issues` make sense; `outline` in QA output is present and consistent with input outline.
5. **Telegram:** Message delivers; Markdown/HTML does not break (no raw parse errors); Cyrillic renders correctly.
6. **Failure injection:** Invalid API key or model returns non-JSON — operator sees controlled error or log (**behavior SAFE UNKNOWN** until Error Workflow exists).
7. **Limits:** Very long brief — either full delivery or intentional split/truncation documented.
8. **Secrets:** No API keys in execution data exports stored in insecure logs (**org policy SAFE UNKNOWN**).

---

## 11. SAFE UNKNOWN summary (expressions & runtime)

| Area | Marker |
|------|--------|
| Telegram Trigger JSON paths for text / chat id | **SAFE UNKNOWN** |
| OpenRouter response path to assistant `content` | **SAFE UNKNOWN** |
| Cross-node references in HTTP Request body expressions | **SAFE UNKNOWN** |
| `response_format: json_object` support per model | **SAFE UNKNOWN** |
| Telegram `parse_mode` and escaping | **SAFE UNKNOWN** |
| Long message chunking / second Send | **SAFE UNKNOWN** |
| Error Workflow / retry / backoff | **SAFE UNKNOWN** |
| `/outline` routing (strict command vs substring) | **SAFE UNKNOWN** |

---

## Traceability

| Artifact | Role |
|----------|------|
| [roadmap.md](roadmap.md) Phase 2.1 | Points to this file as implementation-ready build spec. |
| [runtime-mvp-outline.md](runtime-mvp-outline.md) | Logical architecture and minimal task shape. |
| [data-schema.md](data-schema.md) | Canonical `task` / `outline` fields for later strict validation. |
