# MARS Website Factory — roadmap

**Status:** **strategic** — phases describe **documentation and future implementation** maturity, not committed dates.

| Phase | Name | Focus |
|-------|------|--------|
| **0** | Registration and architecture | This pack, registry row, cross-links to MARS contracts |
| **1** | Registries and contracts | Site Type / Block registries v0; handoff contracts |
| **2** | Artifact semantics and workflow depth | **Done (doc):** **Artifact Architecture Layer v0** ([artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md) and linked models); **v0 agent cards** + **Website Factory Workflow v0** — **done (doc)**. **Remaining:** optional `task-contract-v0` wire examples, prompt/runbook artifacts (**SAFE UNKNOWN** schedule). |
| **3** | Prompt standards and QA gates | Prompt templates, checklists, signal vocabulary |
| **4** | Cursor-based assisted production | Operational runbooks: human executes via Cursor per `execution-model.md` |
| **5** | Runtime-assisted execution | Execution Bridge consumers, durable state (**if** MARS runtime exists) |
| **6** | Production automation experiments | Higher automation **only** with governance, evals, and risk review |

## Dependency honesty

Phases **5–6** depend on MARS **planned-implementation** items (runtime, tools, observability) evidenced only when they exist per `AGENTS.md`.

## Changelog

| Date | Note |
|------|------|
| 2026-05-11 | Initial phase table for Website Factory registration |
| 2026-05-11 | Phase **2** row reframed: **Artifact Architecture Layer v0** documented (semantic models; **not** runtime/schemas). |
