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
| [website-factory-workflow-v0.md](website-factory-workflow-v0.md) | **Website Factory Workflow v0** — canonical orchestration stages, artifact flow, QA/HITL escalation (**documentation only**) |
| [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md) | **Artifact Architecture Layer v0** — workflow vs artifact vs payload vs contract; orchestration/HITL/Validator alignment (**conceptual only**) |
| [artifact-types-v0.md](artifact-types-v0.md) | **Artifact types v0** — lifecycle, mutability, HITL, QA ties per artifact class |
| [page-objective-model-v0.md](page-objective-model-v0.md), [cta-semantics-v0.md](cta-semantics-v0.md), [trust-semantics-v0.md](trust-semantics-v0.md) | **Page objective, CTA, trust** — normalized semantics (no performance guarantees) |
| [section-payload-model-v0.md](section-payload-model-v0.md) | **Section payload model v0** — per-section semantic fields (not implementation JSON) |
| [seo-intent-model-v0.md](seo-intent-model-v0.md), [conversion-intent-model-v0.md](conversion-intent-model-v0.md) | **SEO / conversion intent** — intent dimensions and escalation triggers |
| [frontend-artifact-model-v0.md](frontend-artifact-model-v0.md) | **Frontend artifact model v0** — static build artifacts vs handoff/production docs |
| [qa-result-payloads-v0.md](qa-result-payloads-v0.md) | **QA result payloads v0** — conceptual QA output fields and Validator relationship |
| [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md) | **Prompt Standards Layer v0 — overview** (operational discipline; **not** a prompt engine) |
| [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) | **Prompt structure standard v0** — normalized sections, prompt variants (minimal / production / HITL / QA / frontend) |
| [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md) | **Agent prompt behavior v0** — behavioral rules (no fabrication, escalation, artifact-first) |
| [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md) | **Cursor execution standard v0** — prompt → execute → report loop, git safety, target folder / agent mode |
| [reporting-standard-v0.md](reporting-standard-v0.md) | **Reporting standard v0** — REPORT format and lane variants (doc / frontend / QA / migration / validation) |
| [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) | **HITL prompt boundary v0** — mandatory gates, escalation triggers, “no fake autonomous approval” |
| [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md) | **SAFE UNKNOWN prompt rules v0** — assumption discipline, fabrication forbidden, GOOD vs BAD examples |
| [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) | **Artifact transfer prompt rules v0** — immutability, approval inheritance, revisions, QA inheritance |
| [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) | **QA prompt rules v0** — evidence-based QA, no fake approvals, blocker / waiver, Validator relationship |
| [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md) | **Frontend prompt discipline v0** — Gulp-oriented source-first rules, SCSS modularity, data-* JS, no `dist/` edits |
| [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md) | **Execution Semantics Layer v0 — overview** — operational methodology for stage / artifact / approval / QA / delivery lifecycle; **not** a scheduler / queue / runtime |
| [stage-state-model-v0.md](stage-state-model-v0.md) | **Stage state model v0** — conceptual states, transitions, ownership, freeze / reopen / invalidation |
| [artifact-state-model-v0.md](artifact-state-model-v0.md) | **Artifact state model v0** — lifecycle, mutable/immutable regions, lineage, replacement philosophy, approval inheritance |
| [approval-semantics-v0.md](approval-semantics-v0.md) | **Approval semantics v0** — scope, partial / conditional / inheritance / expiration / revocation; HITL-anchored |
| [revision-semantics-v0.md](revision-semantics-v0.md) | **Revision semantics v0** — scope, lineage, ownership, impact, freeze breaking, QA reset, history |
| [regeneration-semantics-v0.md](regeneration-semantics-v0.md) | **Regeneration semantics v0** — partial / full / safe / unsafe; boundaries; triggers; dependency-aware; HITL-anchored |
| [dependency-invalidation-v0.md](dependency-invalidation-v0.md) | **Dependency invalidation v0** — upstream/downstream propagation across blueprint / design / SEO / frontend; partial rerun |
| [orchestration-signals-v0.md](orchestration-signals-v0.md) | **Orchestration signals v0** — signal source, propagation, escalation, resolution, lifecycle; tied to system signals dictionary |
| [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) | **QA gating semantics v0** — gate lifecycle, blocker / pass / fail / conditional / waiver, freeze, delivery blocking, HITL override |
| [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) | **Delivery lifecycle v0** — candidate, pre-delivery validation, release approval, export package, handoff, rollback, archive, post-delivery revision |
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

**Agent identities:** stable planned **`agent_id`** rows in [`../../agents/registry.md`](../../agents/registry.md) §4.1; **v0 agent cards** for all listed factory roles in [`../../agents/cards/`](../../agents/cards/) (documentation-only, **not** runtime). **SoT** for extended per-role prose remains **[`agent-map.md`](agent-map.md)**. Factory **`entity_id`** rows: [`../../governance/dependency-map.md`](../../governance/dependency-map.md) §4 (`mars_website_factory`, `website_factory_*`, `website_factory_workflow_v0`).

## Related MARS artifacts (existing)

- Agent catalog: [`../../agents/registry.md`](../../agents/registry.md) — **Gulp Frontend Agent**, **Validator Agent** (documented as **legacy-bridge** / **planned**).
- Execution flow: [`../../workflows/execution-flow.md`](../../workflows/execution-flow.md).
- Legacy Gulp profile (imported): [`../../web-gpt-sources/04_agents.md`](../../web-gpt-sources/04_agents.md) (embedded gulp-frontend-agent section).
- Capability / web tasks (imported core draft): [`../../web-gpt-sources/03_core.md`](../../web-gpt-sources/03_core.md) — Page generation, frontend coding rows.

---

*Last updated: 2026-05-11 — **Execution Semantics Layer v0** (overview, stage state, artifact state, approval, revision, regeneration, dependency invalidation, orchestration signals, QA gating, delivery lifecycle; **documentation only — not a runtime engine, not a scheduler, not a queue, not a workflow daemon, not an autonomous execution platform**); previously: Prompt Standards Layer v0 (overview, structure, agent behavior, Cursor execution, reporting, HITL boundary, SAFE UNKNOWN, artifact transfer, QA prompt rules, frontend prompt discipline; **documentation only — not a prompt engine, not a runtime**); Artifact Architecture Layer v0 (overview, types, objective/CTA/trust/section/SEO/conversion semantics, frontend artifacts, QA payloads); Website Factory Workflow v0; agent cards v0; registries + handoff contracts + blueprint QA; documentation only.*
