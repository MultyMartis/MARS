# SEO Content Agent

**Status (fact):** This folder contains **documentation and roadmap only**. No runnable agent, n8n workflows, or production integrations are implemented here yet.

---

## Purpose (plan)

The **SEO Content Agent** is an internal assistant for **SEO specialists**. It is designed to run on **n8n**, expose a **Telegram** chat interface, and call models through **OpenRouter** to support the content lifecycle: briefs and outlines, article drafting from approved outlines, fact checking, SEO quality review, and (later) freshness analysis.

**Fact:** The integration stack (Telegram bot, n8n instance, OpenRouter account, storage) is **not** defined in this repository beyond high-level intent. **SAFE UNKNOWN:** hosting, instance IDs, and operational runbooks.

---

## Target users

- **Internal SEO specialists** (in-house team members using the bot for daily work).

---

## Main components (planned)

| Layer | Role |
|-------|------|
| **Telegram** | Primary user interface (commands and message payloads). |
| **n8n** | Automation engine; workflow orchestration (**not** authored in this repo yet). |
| **OpenRouter** | Model gateway; routing policy in [model-routing.md](model-routing.md). |
| **Storage** | **Phase 1 (plan):** Google Sheets and/or local files. **Later (plan):** PostgreSQL. **SAFE UNKNOWN:** final choice until MVP is built. |

---

## Documentation index

| File | Contents |
|------|----------|
| [roadmap.md](roadmap.md) | Phased delivery plan. |
| [architecture.md](architecture.md) | High-level system and modules. |
| [workflows.md](workflows.md) | `/outline`, `/text`, `/factcheck`, `/seoqa`, `/freshness`. |
| [runtime-mvp-outline.md](runtime-mvp-outline.md) | MVP-1 `/outline` execution spec (n8n + Telegram; **plan**). |
| [prompts.md](prompts.md) | Draft system prompts for AI steps. |
| [data-schema.md](data-schema.md) | JSON shapes for tasks and artefacts. |
| [telegram-commands.md](telegram-commands.md) | Command reference and Russian examples. |
| [model-routing.md](model-routing.md) | Model roles, temperatures, fallbacks. |
| [qa-checklist.md](qa-checklist.md) | Human and automated QA gates. |

---

## Warnings

1. **No runtime implementation** — Do not assume any workflow, credential, or deployment exists because of this documentation.
2. **No secrets in-repo** — API keys, tokens, and client private data must never be committed here.
3. **Honesty boundary** — Outlines and articles must not invent facts; see prompts and QA checklist for explicit rules.

---

*Project registry: `project_id` **seo-content-agent** in `registry/project-registry.md`. Last documentation pass: 2026-05-04.*
