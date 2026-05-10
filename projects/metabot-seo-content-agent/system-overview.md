# System overview — MetaBOT SEO Content Agent

## Purpose

Deliver **production-grade SEO content** through a **multi-workflow** pipeline: user input via **Telegram**, model calls via **OpenRouter**, coordination and business logic in **n8n**, and durable operational state in **Google Sheets**.

---

## Architectural stance

| Principle | Meaning |
|-----------|---------|
| **Multi-workflow** | **Intake**, **Worker**, and **Admin** workflows divide responsibilities; the system is **not** a single monolithic webhook. |
| **External to MARS** | Live execution is **outside** the MARS repository; this pack documents behavior and boundaries. |
| **Quality via layers** | Prefer **universal senior SEO editor** behavior, **cleanup rewrite**, and **QA enforcement** over niche validators and large schema refactors. |
| **Sheets as operational store** | **Memory** and **`seo_active_jobs`** (and related task state) use Google Sheets — subject to quota and consistency constraints. |

---

## Components (logical)

| Component | Role |
|-----------|------|
| **Telegram bot** | Command surface: `/outline`, `/text`, `/run`, `/seoqa`, `/factcheck`, etc. |
| **Intake workflow** | Accepts and normalizes incoming requests; routes toward worker-facing queues or triggers — **SAFE UNKNOWN** for exact routing mechanism between workflows. |
| **Worker workflow** | Core generation, chunking, locks, QA hooks, writes to Sheets — **Worker v13 stable**. |
| **Admin workflow** | Operational commands, health-style checks, housekeeping — **SAFE UNKNOWN** which commands are wired only to Admin vs Worker. |
| **OpenRouter** | LLM / model routing (specific models per step — **SAFE UNKNOWN** in this repo). |
| **Google Sheets** | Memory, `seo_active_jobs`, metadata persistence. |

---

## Features (documented as working in operations)

- `/start`, `/help`, `/outline`, `/text`, `/run`
- `/seoqa --strict from:task_id`, `/factcheck --strict from:task_id` (canonical strict usage)
- `/locks`, chunking, lock cleanup, metadata, memory write
- `seo_active_jobs` lifecycle, cleanup rewrite for `/text`, strict QA runtime enforcement, factcheck separation

---

## Non-goals (explicit)

- **Massive refactors** of schema or workflow topology without operational need.
- **Unnecessary new tables** (in Sheets or elsewhere) when layers can improve quality.
- **Niche-only validators** instead of universal editorial / QA layers.
- **MARS in-repo runtime** replacing n8n for this product — **not** claimed.

---

## SAFE UNKNOWN

- Exact **n8n** node graphs, expressions, and credential bindings.
- **Intake → Worker → Admin** internal transport (queue name, webhook URL shape, execute-workflow node vs external trigger).
- **Model IDs** and per-step prompts as deployed.
- Whether **File Export Workflow** exists yet (treated as **future** in [workflow-map.md](workflow-map.md)).

---

*See [workflow-map.md](workflow-map.md), [full-run-pipeline.md](full-run-pipeline.md), [integration-boundary.md](integration-boundary.md).*
