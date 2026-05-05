# SEO Content Agent — Architecture

**Status:** **documented intent** — high-level design only. No claim that components exist as deployed services.

**MARS rule:** Where deployment details are unspecified, treat as **SAFE UNKNOWN**.

---

## 1. Request flow (plan)

High-level path for a single user request:

```text
Telegram Bot
    → n8n (webhook / bot integration)
        → Command parser (normalize message → `task` JSON)
            → Workflow router (select /outline | /text | /factcheck | /seoqa | /freshness)
                → AI steps (OpenRouter — see model-routing.md)
                    → Storage adapter (persist artefacts, run metadata)
                        → Telegram (reply with summary, links, or structured excerpts)
```

**Fact:** This repository does **not** contain n8n workflow JSON or executable parsers.

**Plan:** The **command parser** may be a dedicated n8n sub-workflow or a small code node; choice is **SAFE UNKNOWN** until implementation.

---

## 2. Component list

### Telegram Interface

- Receives commands and free-text briefs from internal users.
- Sends results, approval prompts, and error messages.
- **Plan:** Map Telegram `chat_id` / user to internal identity for audit (**SAFE UNKNOWN:** auth model).

### n8n Workflow Layer

- Orchestrates steps, retries, and branching (e.g. “outline approved?”).
- Holds **no** long-term secrets in workflow JSON (use n8n credentials store — **out of scope** for this doc).

### Task Normalizer

- Input: raw Telegram payload.
- Output: validated `task` object per [data-schema.md](data-schema.md).
- **Plan:** Reject or flag ambiguous tasks; never silently invent missing SEO parameters — use **SAFE UNKNOWN** fields in output.

### Source Analyzer

- Input: URLs, pasted text, or file references supplied by the user or admin.
- Output: `source_analysis` records (**Phase 2** may skip heavy analysis; **Phase 5** expands).
- **Plan:** Read-only fetch where allowed; respect robots/ToS (**governance TBD**).

### Outline Generator

- Input: `task`, optional `source` / `source_analysis`, company facts slice.
- Output: `outline` JSON + human-readable summary for Telegram.
- **Plan:** Single pass + optional short refinement step (**SAFE UNKNOWN**).

### Content Writer

- Input: **approved** `outline`, same fact boundary.
- Output: `generated_text` (body + metadata).
- **Plan:** No writing without approval record in storage (**implementation TBD**).

### Factchecker

- Input: `generated_text` (or excerpt), supporting `source`, `task`, company facts.
- Output: `factcheck_report` JSON.
- **Plan:** Flag unsupported claims; do not auto-delete client-facing copy without human confirmation.

### SEO QA Reviewer

- Input: `generated_text`, `outline`, optional SERP keywords from brief.
- Output: `seoqa_report` JSON.
- **Plan:** Structural checks (H1–H3), intent, FAQ relevance; keyword stuffing detection.

### Storage Adapter

- **Phase 1 (plan):** Google Sheets and/or filesystem under controlled paths.
- **Later (plan):** PostgreSQL (or compatible) for tasks, outlines, versions, reports.
- **Fact:** No adapter code in this folder.

### Model Router

- Selects provider/model per step (analytics vs draft vs polish).
- Applies temperature and token limits; handles fallback model on errors.
- See [model-routing.md](model-routing.md).

---

## 3. Data and boundaries

- All structured artefacts should conform to [data-schema.md](data-schema.md).
- **Fact boundary:** Models may use only what is in the task, attached sources, and approved company-facts corpus. Everything else must be labeled as missing or unsupported.

---

## 4. Non-goals (for architecture v0)

- Real-time collaborative editing inside Telegram.
- Fully automated publishing to CMS without human gate (**org policy** may forbid).
- Storing **client confidential** payloads in plain text without classification (**SAFE UNKNOWN:** DLP integration).

---

## 5. Relation to MARS platform docs

This project **reuses concepts** from MARS (registry, lifecycle, model routing vocabulary) but is **not** the MARS execution runtime. Integration with MARS orchestration, if any, is **SAFE UNKNOWN**.
