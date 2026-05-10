# MARS Website Factory — system overview

## Vision

**MARS Website Factory** is a **planned** **multi-agent website production system** expressed primarily through **documentation, contracts, registries, and workflows** — not through a shipped orchestration runtime in this repository.

It extends MARS’s existing ideas (task contracts, execution-flow stages, Validator role, **Gulp Frontend Agent** as a documented specialist profile) into a **coherent factory story** for marketing sites and similar deliverables.

## What it is not

- A **single** chat bot or monolithic agent.
- **Runtime-ready** automation inside MARS core (no evidenced dispatcher for this factory in-repo).
- An **autonomous AI design or dev studio** without human gates.
- A replacement for **project-specific** packs such as **MetaBOT — SEO Content Agent** (`projects/metabot-seo-content-agent/`), which documents an **external** n8n system.

## What it is

- A **strategic ecosystem direction** for MARS: architecture-first, registry-first, workflow-first.
- A **composition** of **planned** specialist agents, **knowledge registries**, **QA gates**, **HITL checkpoints**, and **orchestration semantics** aligned with `workflows/execution-flow.md`.
- A **production story** where **frontend build** is centered on the documented **Gulp / static** profile (see `web-gpt-sources/04_agents.md` and [frontend-production-model.md](frontend-production-model.md)).

## Operating reality (Phase 1)

Per `governance/execution-model.md`, **today’s** execution path for file changes is **human-in-the-loop** tooling (e.g. **Cursor**), not an autonomous MARS process. Factory workflows are **targets**; **prompt → execute → report** remains an **operational pattern** (see `web-gpt-sources/05_workflows.md`, `workflows/README.md`).

## SAFE UNKNOWN

- Whether a dedicated **gulp-starter** repository or template will be versioned **inside** MARS vs **outside** — **not** specified here.
- **Wire formats** for any future Execution Bridge handoff specific to Website Factory — **unknown** until specified in integration contracts.
- **Figma**, **n8n**, and **Cursor** are **not** assumed to be connected automatically; any integration is **future** and **optional**.
