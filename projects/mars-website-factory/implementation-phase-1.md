# MARS Website Factory — implementation phase 1 (doc-first)

**Scope:** **Documentation and contracts only** — **no** code generation mandate, **no** new runtime.

## Proposed concrete deliverables

| # | Deliverable | Description |
|---|-------------|-------------|
| 1 | **Site Type Registry v0** | **Done (doc):** [site-type-registry-v0.md](site-type-registry-v0.md) — initial `site_type_id` rows and field glossary (Markdown in this pack). |
| 2 | **Block Registry v0** | **Done (doc):** [block-registry-v0.md](block-registry-v0.md) — initial `block_id` set, compatibility matrix, field glossary (Markdown); aligned with static HTML feasibility. |
| 3 | **Website Factory workflow v0** | **Done (doc):** [website-factory-workflow-v0.md](website-factory-workflow-v0.md) — orchestration stages, artifact flow, QA/HITL escalation; aligns with `workflows/task-contract-v0.md` fields as **narrative** (**no** runtime) |
| 4 | **Factory agent cards (§4.1 roster, incl. Gulp Frontend)** | **Done (doc):** v0 cards under [`../../agents/cards/`](../../agents/cards/) per [`../../agents/registry.md`](../../agents/registry.md) §4.1, including [`../../agents/cards/gulp-frontend-agent-v0.md`](../../agents/cards/gulp-frontend-agent-v0.md). |
| 5 | **Page Blueprint contract** | **Done (doc):** [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md) — normalized page orchestration fields; human-readable (**no** strict JSON Schema in v0). |
| 6 | **Design handoff contract** | **Done (doc):** [design-handoff-contract-v0.md](design-handoff-contract-v0.md) — blueprint → visual production requirements (tokens, sections, QA); **not** automated Figma |
| 7 | **Frontend handoff contract** | **Done (doc):** [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md) — blueprint/design → **Gulp**-oriented static production requirements |
| 8 | **QA checklist v0** | **Done (doc, blueprint slice):** [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md); broader lanes remain in [qa-validation-model.md](qa-validation-model.md). |

## Phase 2 (documentation) — artifact architecture layer v0

| # | Deliverable | Description |
|---|-------------|-------------|
| P2-1 | **Artifact architecture overview + types** | **Done (doc):** [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md), [artifact-types-v0.md](artifact-types-v0.md). |
| P2-2 | **Objective / CTA / trust / section semantics** | **Done (doc):** [page-objective-model-v0.md](page-objective-model-v0.md), [cta-semantics-v0.md](cta-semantics-v0.md), [trust-semantics-v0.md](trust-semantics-v0.md), [section-payload-model-v0.md](section-payload-model-v0.md). |
| P2-3 | **SEO / conversion intent models** | **Done (doc):** [seo-intent-model-v0.md](seo-intent-model-v0.md), [conversion-intent-model-v0.md](conversion-intent-model-v0.md). |
| P2-4 | **Frontend + QA payload concepts** | **Done (doc):** [frontend-artifact-model-v0.md](frontend-artifact-model-v0.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md). |

**Remaining (not claimed done):** deeper field binding to `task-contract-v0` wire examples, prompt/runbook artifacts — **SAFE UNKNOWN** until authored.

## Out of scope for phase 1

- Gulp project scaffolding in this repo.
- Figma plugins, n8n nodes, or Cursor extensions.
- Automated orchestration.

## Success criteria (documentation)

- Cross-links from `registry/project-registry.md` and `agents/registry.md` remain consistent.
- No **false** “production ready” language in phase 1 outputs.
