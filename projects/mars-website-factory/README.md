# MARS Website Factory — project documentation pack

**project_id:** `mars-website-factory`  
**Status:** **planned** — **strategic, documentation-first** direction inside the MARS ecosystem.  
**Not claimed:** a single bot, a single runtime agent, autonomous studio, or production-ready automation.

## What this is

A **target architecture** for a **multi-agent, contract-driven** website production system: intake → strategy → IA → blueprints → wireframes → design → frontend production → QA → human approval → delivery. Execution in Phase 1 remains **human-supervised** and **prompt-driven** (see `../../governance/execution-model.md`).

## Pack index

| Document | Purpose |
|----------|---------|
| [system-overview.md](system-overview.md) | Vision, boundaries, relation to MARS core |
| [layer-map.md](layer-map.md) | Seven target layers, agents, artifacts, gates, risks |
| [agent-map.md](agent-map.md) | Planned agent roles (registry alignment) |
| [registries.md](registries.md) | Planned knowledge modules; **delivered v0:** [site-type-registry-v0.md](site-type-registry-v0.md), [block-registry-v0.md](block-registry-v0.md) |
| [site-type-registry-v0.md](site-type-registry-v0.md) | **Site Type Registry v0** — classification layer for strategy, SEO, UX, blocks, frontend, QA |
| [block-registry-v0.md](block-registry-v0.md) | **Block Registry v0** — section semantics, compatibility with site types, orchestration-facing fields (documentation only) |
| [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md) | **Page Blueprint Contract v0** — normalized page orchestration fields (strategy → SEO → UX → design → frontend → QA) |
| [design-handoff-contract-v0.md](design-handoff-contract-v0.md) | **Design Handoff Contract v0** — blueprint → visual production requirements (design layer); no automated Figma claim |
| [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md) | **Frontend Handoff Contract v0** — blueprint/design → static frontend production requirements (Gulp-oriented) |
| [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md) | **Page Blueprint QA Checklist v0** — blueprint-level validation categories and escalation |
| [workflow-map.md](workflow-map.md) | End-to-end flow, HITL, Cursor vs future runtime |
| [qa-validation-model.md](qa-validation-model.md) | QA lanes and Validator integration |
| [frontend-production-model.md](frontend-production-model.md) | Gulp-oriented production model (legacy-aligned) |
| [design-layer-model.md](design-layer-model.md) | Design artifacts and agent boundaries |
| [seo-marketing-layer.md](seo-marketing-layer.md) | SEO/marketing strategy and QA |
| [roadmap.md](roadmap.md) | Phased evolution (0–6) |
| [migration-strategy.md](migration-strategy.md) | How this pack relates to legacy Web-GPT ideas and other projects |
| [implementation-phase-1.md](implementation-phase-1.md) | First doc-only deliverables |
| [safe-unknown-boundary.md](safe-unknown-boundary.md) | Honesty boundary — no false implementation claims |

## Registry

Authoritative project row: [`../../registry/project-registry.md`](../../registry/project-registry.md).

## Related MARS artifacts (existing)

- Agent catalog: [`../../agents/registry.md`](../../agents/registry.md) — **Gulp Frontend Agent**, **Validator Agent** (documented as **legacy-bridge** / **planned**).
- Execution flow: [`../../workflows/execution-flow.md`](../../workflows/execution-flow.md).
- Legacy Gulp profile (imported): [`../../web-gpt-sources/04_agents.md`](../../web-gpt-sources/04_agents.md) (embedded gulp-frontend-agent section).
- Capability / web tasks (imported core draft): [`../../web-gpt-sources/03_core.md`](../../web-gpt-sources/03_core.md) — Page generation, frontend coding rows.

---

*Last updated: 2026-05-11 — design + frontend handoff contracts v0; page blueprint contract + QA checklist v0; documentation only.*
