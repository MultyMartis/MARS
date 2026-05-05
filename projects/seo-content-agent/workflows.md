# SEO Content Agent — Workflows

**Status:** **specification** — describes intended behavior. **No** n8n workflow graphs exist in this repository.

Convention: **Input / Steps / AI calls / Output / Human review** per workflow.

---

## Shared prerequisites (plan)

- User is authenticated for internal use (**SAFE UNKNOWN:** mechanism).
- OpenRouter credentials configured in n8n (**not** documented here).
- Optional: company facts document or sheet ID configured as environment-level reference (**SAFE UNKNOWN**).

---

## `/outline`

**Purpose:** Produce an **SEO outline / copywriter brief** from a user brief. The workflow exists at **two levels** (documentation + runtime); see [runtime-mvp-outline.md](runtime-mvp-outline.md) for MVP-1 orchestration.

### Levels (plan)

| Level | Scope | Flow summary |
|-------|--------|--------------|
| **MVP-1** | Telegram brief **only**; **no** competitor parsing, **no** URL/source fetching, **no** Storage Adapter persistence. | **Telegram** → **Parse Task** → **Normalize** → **Build Outline** → **QA Outline** → **Telegram** result. |
| **Later** | Optional structured **source** analysis, brief deep-dive, durable storage. | Normalize → **Analyze Brief** → *(optional)* **Analyze Sources** → **Build Outline** → *(optional)* QA step per policy → **Persist** → **Format** delivery. |

**Fact:** Neither level is implemented in this repository; MVP-1 is specified for n8n build-out (**plan**).

**Sources in MVP-1:** “Optional sources” means **plain text pasted into the Telegram message** (same chat as `/outline`). **Not** automated URL ingestion or `source_analysis` pipeline — that is **later** only.

---

### MVP-1 — Steps (plan)

Aligned with [runtime-mvp-outline.md](runtime-mvp-outline.md):

1. **Parse Task** — AI: interpret free text into structured fields (prompt family: Parse Task / parse brief).
2. **Normalize** — Code (or equivalent): map model output to minimal `task` shape ([data-schema.md](data-schema.md) MVP-1 compatibility).
3. **Build Outline** — AI: emit `outline` JSON (sections, H1–H3, meta direction, per-section notes).
4. **QA Outline** — AI: consistency and gap pass on the outline.
5. **Telegram result** — human-readable summary (and **no** requirement to persist artefacts in storage).

### Later version — Steps (plan)

1. **Normalize** message → full `task` JSON ([data-schema.md](data-schema.md)).
2. **Analyze brief** — AI: extract goals, intent, gaps; mark **SAFE UNKNOWN** for missing inputs.
3. *(Optional)* **Analyze sources** — if user provided **fetchable** sources and policy allows: AI produces `source_analysis`; if none, skip with explicit empty list.
4. **Build outline** — AI: emit `outline` JSON (sections, H1–H3, intent per section, FAQ plan, internal note on missing data).
5. **Persist** outline + task via Storage Adapter.
6. **Format** short Telegram summary + attach or link full JSON (**SAFE UNKNOWN:** delivery format).

### AI calls (plan)

**MVP-1:**

| Step | Prompt family | Typical output |
|------|---------------|----------------|
| Parse Task | Parse Telegram Task | `task` / parsed fields → normalized minimal task |
| Build Outline | Build Outline | `outline` |
| QA Outline | QA Outline | `qa_outline` (or annotated outline) |

**Later:**

| Step | Prompt family | Typical output |
|------|---------------|----------------|
| Normalize | Parse Telegram Task | `task` |
| Brief | Analyze Brief | JSON summary + gaps |
| Sources | Analyze Sources | `source_analysis[]` |
| Outline | Build Outline | `outline` |

### Input

- Telegram command + free text or structured fields: topic, audience, intent, keywords, tone, page type (landing / blog / category), constraints.
- **MVP-1:** paste any reference material as **plain text** in the message; **no** URL parsing.
- **Later:** links or pasted source text may feed **Analyze Sources** where implemented (**SAFE UNKNOWN:** fetch policy).
- Optional: locale (e.g. `ru-RU`).

### Output

- `outline` / `qa_outline` artefact (MVP-1: in-chat only unless operator adds storage); human-readable summary in Telegram.
- Explicit list of **`missing_data`** (JSON field) and **assumptions** (should be empty or labeled — no silent invention). System-level gap signaling: see signal convention in [data-schema.md](data-schema.md).

### Human review points

- Confirm keywords and intent match client/stakeholder expectations.
- Approve or edit outline before any `/text` run.
- Reject if **unsupported facts** appear — send back with corrected brief only.

---

## `/text`

**Purpose:** Generate a full **SEO article draft** from an **approved** outline only.

### Input

- Reference to approved outline (ID or last message thread context — **SAFE UNKNOWN:** how thread state is stored).
- Same `task` correlation as outline.
- Optional: length targets, banned phrases, compliance notes.

### Steps (plan)

1. Verify **approval** flag on outline record; if not approved, abort with instruction to run `/outline` and approve.
2. **Write SEO text** — AI: produce `generated_text` following outline and fact boundary.
3. Persist draft with version number.
4. Return excerpt + metadata (word count, reading level **if** available) to Telegram.

### AI calls (plan)

| Step | Prompt family | Typical output |
|------|---------------|----------------|
| Draft | Write SEO Text | `generated_text` |

### Output

- `generated_text` (title, meta description, body with heading markers, FAQ block if in outline).

### Human review points

- Copy review for brand voice and legal/compliance.
- Run `/factcheck` and `/seoqa` before external use.

---

## `/factcheck`

**Purpose:** Structured report on factual support for claims in a draft.

### Input

- `generated_text` (by reference or pasted).
- Supporting materials: original `task`, `source`, company facts (**SAFE UNKNOWN:** attachment limits).

### Steps (plan)

1. Load draft and evidence set.
2. **Fact check** — AI: map claims to evidence or mark unsupported; **JSON-only** `factcheck_report`.
3. Persist report linked to draft version.
4. Send summary + severity counts to Telegram.

### AI calls (plan)

| Step | Prompt family | Typical output |
|------|---------------|----------------|
| Verify | Fact Check | `factcheck_report` |

### Output

- `factcheck_report` with per-claim status: `supported`, `unsupported`, `needs_source`, `contradicts_source`.

### Human review points

- Resolve **unsupported** / **contradicts_source** before publication.
- Decide whether to run **Rewrite With Fixes** (future prompt) or manual edit.

---

## `/seoqa`

**Purpose:** SEO-focused quality review (structure, intent, spam risk) — **not** a substitute for human editorial.

### Input

- `generated_text`, `outline`, keyword list from `task`.

### Steps (plan)

1. **SEO QA** — AI: emit `seoqa_report` (JSON).
2. Optionally cross-check outline ↔ draft headings (**plan:** deterministic script in n8n **SAFE UNKNOWN**).
3. Post summary to Telegram.

### AI calls (plan)

| Step | Prompt family | Typical output |
|------|---------------|----------------|
| Review | SEO QA | `seoqa_report` |

### Output

- `seoqa_report`: heading structure, intent coverage, FAQ quality, keyword use assessment, issues list.

### Human review points

- Accept or schedule edits for **fail** / **warn** items (see [qa-checklist.md](qa-checklist.md)).

---

## `/freshness`

**Purpose:** **Phase 6** — flag potentially stale facts, dates, stats, product claims.

### Input

- `generated_text` or URL of published page (**plan**).
- Freshness corpus: dated internal facts sheet or allowed URLs (**SAFE UNKNOWN**).

### Steps (plan)

1. Extract dated claims and numeric/statistical statements.
2. Compare against freshness sources; AI + rules (**SAFE UNKNOWN** split).
3. Produce report artifact (extend schema later — **SAFE UNKNOWN:** final field names).

### AI calls (plan)

| Step | Prompt family | Typical output |
|------|---------------|----------------|
| Analyze | *(TBD prompt)* | Structured freshness findings |

### Output

- List of stale or unverifiable items with **recommended action** (verify / update / remove).

### Human review points

- All freshness findings are **advisory** until a human validates against live product/legal truth.

---

## Failure and escalation (plan)

- Model timeout / rate limit → retry with **fallback model** ([model-routing.md](model-routing.md)); if still failing, message user with **SAFE UNKNOWN** on ETA.
- Invalid JSON from model → bounded repair pass or abort; log for tuning (**SAFE UNKNOWN:** observability stack).
