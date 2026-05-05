# SEO Content Agent — MVP runtime plan: `/outline` (n8n + Telegram)

**Status:** **specification** — executable orchestration design for the first MVP. **No** n8n workflow JSON, bot code, or OpenRouter request bodies are included in this repository.

**Fact vs plan:** This file describes **planned** node order, data contracts, and human gates. Whether a given n8n instance implements it exactly as written is **not** asserted here.

**SAFE UNKNOWN (global):** OpenRouter request/response field names, exact n8n expression syntax, message chunking limits, retry/backoff configuration, and observability hooks are **unknown** until implementation — treat as **SAFE UNKNOWN** rather than guessing.

---

## 1. Purpose

This file describes the **first executable MVP**: user invokes **`/outline`** in Telegram; **n8n** orchestrates **AI** steps via **OpenRouter**; the user receives a **structured SEO brief** (outline + meta plan + section-level guidance). **No** article body generation, **no** publishing, **no** durable storage in this MVP — see [Known limitations](#8-known-limitations).

**MVP-1 and sources:** MVP-1 **does not** parse URLs, fetch external pages, or run a **source_analysis** pipeline. Any reference material must be **pasted as plain text** into the user brief (Telegram message body / `brief` field). Automated ingestion is **later** (see [workflows.md](workflows.md) “Later version”).

---

## 2. Minimal architecture

Exact **plan** flow:

```text
Telegram Bot
    → n8n Telegram Trigger
        → AI: Parse Task
        → Code: Normalize
        → AI: Build Outline
        → AI: QA Outline
        → Telegram Send Message
```

**Fact vs plan:** “Code: Normalize” is a **logical** step. In the [n8n node structure](#3-n8n-node-structure-very-important), normalization is **folded into** the first **Code (extract JSON)** node after **Parse Task** (see that node’s purpose). A separate Code node is **not** required for MVP-1 unless implementers choose to split concerns (**SAFE UNKNOWN**).

**Boundaries:** No secrets, tokens, or credentials appear in this document. Integration details belong in n8n credential stores and runbooks (**out of scope** here).

---

## 3. n8n node structure (very important)

Nodes in **execution order**. For each: **input**, **output**, **purpose**.

### 1. Telegram Trigger

| | |
|--|--|
| **Input** | Incoming Telegram update (message text, chat context, ids — **exact shape SAFE UNKNOWN**). |
| **Output** | Raw webhook payload fields exposed to n8n (e.g. message body, `chat_id`). |
| **Purpose** | Start the workflow when the user sends a message that qualifies as `/outline` (**routing rule SAFE UNKNOWN**: command-only vs prefix match). |

### 2. Set (raw input)

| | |
|--|--|
| **Input** | Telegram Trigger output. |
| **Output** | `task_raw` (and any passthrough ids needed for the reply), e.g. normalized string of user text + metadata snapshot. |
| **Purpose** | Freeze a single **canonical raw brief** for the run and simplify downstream expressions. |

### 3. HTTP Request (OpenRouter: Parse Task)

| | |
|--|--|
| **Input** | `task_raw` (user text + optional context from Set). |
| **Output** | OpenRouter HTTP response (body includes model completion — **exact JSON envelope SAFE UNKNOWN**). |
| **Purpose** | **AI: Parse Task** — interpret free text into structured fields; infer `task_type: "outline"` when appropriate; surface gaps without inventing facts. |

### 4. Code (extract JSON)

| | |
|--|--|
| **Input** | HTTP response from Parse Task. |
| **Output** | `task_parsed` (parsed model payload) and **`task_normalized`** conforming to [Minimal task schema](#5-minimal-task-schema) (defaults, empty arrays, explicit unknowns). |
| **Purpose** | Extract assistant JSON from the provider response **and** perform **Code: Normalize** — map into the minimal schema; attach **signals** (e.g. `MISSING_DATA`, `LOW_INPUT_QUALITY`) when applicable; do **not** call external APIs. |

### 5. HTTP Request (OpenRouter: Build Outline)

| | |
|--|--|
| **Input** | `task_normalized` (and optionally `task_raw` for traceability — **plan**). |
| **Output** | OpenRouter HTTP response for outline generation. |
| **Purpose** | **AI: Build Outline** — produce structured outline: H1, sections (H2/H3), meta direction, per-section keywords and notes, word-count targets. |

### 6. Code (extract JSON)

| | |
|--|--|
| **Input** | HTTP response from Build Outline. |
| **Output** | `outline` (structured object ready for QA). |
| **Purpose** | Extract JSON outline from the model response; validate minimal keys expected by the QA step (**strict schema file SAFE UNKNOWN**). |

### 7. HTTP Request (OpenRouter: QA Outline)

| | |
|--|--|
| **Input** | `outline` + `task_normalized` (**plan**: both in prompt context). |
| **Output** | OpenRouter HTTP response (QA result). |
| **Purpose** | **AI: QA Outline** — consistency check, gap flagging, SEO-structure sanity; output revised or annotated outline per prompt policy (**exact policy in [prompts.md](prompts.md) — alignment TBD**). |

### 8. Code (extract JSON)

| | |
|--|--|
| **Input** | HTTP response from QA Outline. |
| **Output** | `qa_outline` (final structured brief for formatting). |
| **Purpose** | Extract JSON; merge QA annotations into a single object if the model returns wrapper fields (**shape SAFE UNKNOWN**). |

### 9. Telegram Send Message

| | |
|--|--|
| **Input** | `final_output` derived from `qa_outline` (see [Data flow](#4-data-flow) and [Output format](#6-output-format)); reply target from Trigger/Set (`chat_id` / thread — **SAFE UNKNOWN**). |
| **Output** | Telegram API result (message id — **optional persistence SAFE UNKNOWN**). |
| **Purpose** | Deliver the human-readable MVP artefact to the user; split long messages if over limits (**chunking strategy SAFE UNKNOWN**). |

---

## 4. Data flow

JSON (or JSON-compatible objects) passed between steps — **plan**:

| Stage | Name | Role |
|-------|------|------|
| After Set | `task_raw` | Raw captured user message / brief. |
| After Parse + first Code | `task_parsed` | Structured extraction as returned by the model (before or during normalization). |
| After normalization | `task_normalized` | Minimal task schema instance for downstream AI. |
| After Build + second Code | `outline` | Outline draft. |
| After QA + third Code | `qa_outline` | Outline after QA pass (may equal `outline` plus `qa_notes` — **field names SAFE UNKNOWN**). |
| Before Telegram | `final_output` | Rendered content for the bot message (from `qa_outline` via formatting Code or expression — **implementation choice SAFE UNKNOWN**). |

**Chain (mnemonic):** `task_raw` → `task_parsed` → `task_normalized` → `outline` → `qa_outline` → `final_output`.

---

## 5. Minimal task schema

MVP **`task_normalized`** shape (subset of full `task` in [data-schema.md](data-schema.md); extend later):

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

**Alignment note:** Full `task` uses `primary_keywords` / `secondary_keywords`; MVP-1 uses `keywords[]`. Mapping to the full schema: see **MVP-1 schema compatibility** in [data-schema.md](data-schema.md).

---

## 6. Output format

The **final Telegram message** (**plan**) must include:

- **H1**
- **Meta Title**
- **Meta Description**
- **Structured outline (H2 / H3)**
- **Word count per section**
- **Keywords per section**
- **Copywriter notes** (constraints, gaps, “do not invent” reminders)

Formatting (Markdown vs plain text, locale) is **SAFE UNKNOWN** until product preference is fixed.

---

## 7. Human-in-the-loop

- **SEO specialist** reviews the outline **manually** (outside or after the bot message — **process SAFE UNKNOWN**).
- **No** automated full article (`/text`) in this MVP.
- **No** publishing to CMS or public channels from this workflow.

---

## 8. Known limitations

- No competitor parsing.
- No entity scoring.
- No SERP integration.
- **No storage** of tasks/outlines in this MVP (conversation-only artefact).
- **No versioning** of outlines.
- **No history** / audit DB beyond Telegram chat history (**retention SAFE UNKNOWN**).

These align with Phase 2 non-goals in [roadmap.md](roadmap.md) for scope; **persistence** appears in later phases there — MVP-1 is intentionally narrower.

---

## 9. Next step hook

**Next step after MVP-1** (**plan**):

- Add **`/text`** workflow (draft generation from **approved** outline).
- Add **storage** (task/outline ids, approval flags — mechanism **SAFE UNKNOWN**).
- Add **source parsing** (URLs / pasted corpus analysis per [workflows.md](workflows.md) and [architecture.md](architecture.md)).

---

## 10. Signals

Possible **machine- or prompt-emitted** signals for gating and messaging (**plan**; not an exhaustive enum):

| Signal | Meaning (plan) |
|--------|----------------|
| `UNKNOWN` | Required runtime detail or external fact not available — do not invent; label for human. |
| `MISSING_DATA` | Brief lacks fields needed for a confident outline; outline may include explicit gaps. |
| `LOW_INPUT_QUALITY` | Brief is vague, contradictory, or too short; QA or Parse should flag for specialist follow-up. |

**Convention:** Use **`MISSING_DATA`** as a **system signal**; persist gaps in artefacts under the JSON field **`missing_data`** (array). See [data-schema.md](data-schema.md) — *System signals vs JSON fields*.

---

## Traceability

| Doc | Relation |
|-----|----------|
| [roadmap.md](roadmap.md) | Phase 2.1 — MVP `/outline` runtime. |
| [workflows.md](workflows.md) | Full `/outline` vision (extra steps, persistence); MVP is a **deliberate subset**. |
| [architecture.md](architecture.md) | Target architecture includes Storage Adapter; **MVP-1 defers** storage. |
| [prompts.md](prompts.md) | Source for Parse / Build / QA prompt text — **to be wired in n8n**. |
