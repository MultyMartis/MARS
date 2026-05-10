# MetaBOT — SEO Content Agent

**Classification:** **external multi-workflow AI system** (production-oriented SEO content pipeline).  
**Not:** a single webhook “tool”, a MARS runtime adapter, or an in-repo executable.

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
| **This repository (`D:\AI MARS`)** | **Architecture / contracts / knowledge** — documentation packs, integration boundaries, and governance alignment. **MARS does not execute MetaBOT workflows.** |

MARS stores **sanitized** descriptions, maps, and contracts only. **Secrets, tokens, and workflow JSON** live **outside** this repo (typically in n8n and chat provider configuration). See [integration-boundary.md](integration-boundary.md).

---

## Documentation pack (this folder)

| File | Purpose |
|------|---------|
| [system-overview.md](system-overview.md) | Capabilities, components, non-goals |
| [workflow-map.md](workflow-map.md) | Intake / Worker / Admin (+ future export) |
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

---

## Related in-repo material

- Earlier **spec-oriented** pack: [`../seo-content-agent/`](../seo-content-agent/) — may overlap in naming; **MetaBOT** docs here describe the **external multi-workflow** system as operated today. Reconcile discrepancies against **live n8n**, not against this repo alone.

---

## Status honesty (per `AGENTS.md`)

This folder is **documentation only**. It does **not** prove that any particular n8n node graph, credential, or Telegram bot instance matches these words. Where execution detail is not evidenced here, the docs say **SAFE UNKNOWN**.

---

*Registry: `project_id` **metabot-seo-content-agent** — see [`../../registry/project-registry.md`](../../registry/project-registry.md).*
