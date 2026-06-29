# MetaBOT — SEO Content Agent

**Classification:** **external multi-workflow AI system** (production-oriented SEO content pipeline).  
**Not:** a single webhook “tool”, a MARS runtime adapter, or an in-repo executable.

---

## Canonical project folder

This folder is the canonical MARS documentation folder for MetaBOT SEO Content Agent.

**Legacy folder:** [`projects/seo-content-agent/`](../seo-content-agent/) — remains only for older bridge/spec artifacts until migration is complete. **Do not** treat it as the documentation source of truth.

**Canonical contents:**

- external multi-workflow architecture
- Intake / Worker / Admin documentation
- roadmap and known issues
- sanitized exports (under [`exports/`](exports/))
- integration contracts (e.g. [`integration-contract-legacy.md`](integration-contract-legacy.md), [`integration-boundary.md`](integration-boundary.md))
- bridge mapping notes (under [`integrations/`](integrations/))
- migrated legacy doc snapshots (under [`legacy/`](legacy/))

---

## What this project is

**MetaBOT — SEO Content Agent** is an **external** system that orchestrates **multiple n8n workflows**, a **Telegram** control surface, **OpenRouter**-backed models, and **Google Sheets** for durable operational data. It generates and refines SEO-oriented content under locks, QA layers, and explicit task lifecycle semantics.

**Current stable worker reference (operations):** Worker **v13** stable — **SAFE UNKNOWN** whether other workflow variants exist in parallel; confirm in the live n8n instance.

---

## Relation to MARS

| Layer | Role |
|--------|------|
| **n8n** | **Execution runtime** — owns workflow graphs, triggers, credentials, and live orchestration. |
| **MetaBOT (external)** | **Product system** — Intake / Worker / Admin workflows, Telegram UX, Sheets-backed state. |
| **This repository (`X:\AI MARS`)** | **Architecture / contracts / knowledge** — documentation packs, integration boundaries, and governance alignment. **MARS does not execute MetaBOT workflows.** |

MARS stores **sanitized** descriptions, maps, and contracts only. **Secrets, tokens, and workflow JSON** live **outside** this repo (typically in n8n and chat provider configuration). See [integration-boundary.md](integration-boundary.md).

---

## Documentation pack (this folder)

| File | Purpose |
|------|---------|
| [mega-map.md](mega-map.md) | **Главный runtime mega-map** v13 (workflows, routes, locks, memory, quality, risks, SoT paths) |
| [system-overview.md](system-overview.md) | Capabilities, components, non-goals |
| [workflow-map.md](workflow-map.md) | Intake / Worker / Admin (+ future export), route types, single vs run |
| [intake-workflow.md](intake-workflow.md) | Intake responsibilities (**SAFE UNKNOWN** at node level) |
| [worker-workflow.md](worker-workflow.md) | Worker responsibilities (**SAFE UNKNOWN** at node level) |
| [admin-workflow.md](admin-workflow.md) | Admin / ops workflow |
| [telegram-commands.md](telegram-commands.md) | Bot command reference |
| [task-lifecycle.md](task-lifecycle.md) | Tasks, states, `from:`, cleanup |
| [lock-system.md](lock-system.md) | Concurrency and lock semantics |
| [storage-layer.md](storage-layer.md) | Google Sheets roles |
| [memory-and-task-reuse.md](memory-and-task-reuse.md) | Memory writes and reuse |
| [user-metadata.md](user-metadata.md) | Telegram user fields |
| [full-run-pipeline.md](full-run-pipeline.md) | End-to-end `/run` narrative |
| [seoqa-and-factcheck.md](seoqa-and-factcheck.md) | Strict QA vs factcheck |
| [cleanup-rewrite-layer.md](cleanup-rewrite-layer.md) | Post-generation cleanup |
| [admin-operations.md](admin-operations.md) | Operational tasks |
| [known-issues.md](known-issues.md) | Runtime / quality / infra / UX |
| [roadmap.md](roadmap.md) | Stabilization and future work |
| [seo-specialist-user-guide.md](seo-specialist-user-guide.md) | Guide for SEO operators |
| [lessons-learned.md](lessons-learned.md) | Design and operations lessons |
| [integration-boundary.md](integration-boundary.md) | MARS vs n8n vs credentials (**normative**) |
| [integration-contract-legacy.md](integration-contract-legacy.md) | Legacy MARS ↔ webhook payload contract (copied from early spec pack) |
| [exports/workflow-sanitized-legacy.json](exports/workflow-sanitized-legacy.json) | Sanitized n8n export snapshot (legacy single-workflow line; **not** full Intake/Worker/Admin set) |
| [integrations/n8n-mars-bridge-map-code.txt](integrations/n8n-mars-bridge-map-code.txt) | Bridge / mapping snippet for n8n (no secrets) |
| [legacy/data-schema-legacy.md](legacy/data-schema-legacy.md) | Legacy JSON shapes doc (snapshot) |

---

## Related in-repo material

- **Legacy documentation / bridge pack:** [`../seo-content-agent/`](../seo-content-agent/) — **do not add new docs there**; canonical narrative lives here. Reconcile execution truth with **live n8n**.
- **Raw workflow dumps (local, gitignored):** `projects/metabot-seo-content-agent/raw/` — optional local exports; **must not** be committed. Sanitized repo copies belong under [`exports/`](exports/). See [mega-map.md](mega-map.md) §10.

---

## Status honesty (per `AGENTS.md`)

This folder is **documentation only**. It does **not** prove that any particular n8n node graph, credential, or Telegram bot instance matches these words. Where execution detail is not evidenced here, the docs say **SAFE UNKNOWN**.

---

*Registry: `project_id` **metabot-seo-content-agent** — see [`../../registry/project-registry.md`](../../registry/project-registry.md).*
