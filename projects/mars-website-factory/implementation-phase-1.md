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

## Phase 3 (documentation) — prompt standards layer v0

| # | Deliverable | Description |
|---|-------------|-------------|
| P3-1 | **Prompt standards overview** | **Done (doc):** [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md) — purpose, philosophy, non-claims (operational interfaces, not AGI). |
| P3-2 | **Prompt structure standard** | **Done (doc):** [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) — canonical sections, prompt variants (minimal / production / HITL / QA / frontend), examples. |
| P3-3 | **Agent prompt behavior** | **Done (doc):** [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md) — no fabrication, artifact-first, HITL escalation. |
| P3-4 | **Cursor execution standard** | **Done (doc):** [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md) — target folder / agent mode / git safety / REPORT loop. |
| P3-5 | **Reporting standard** | **Done (doc):** [reporting-standard-v0.md](reporting-standard-v0.md) — canonical REPORT and lane variants. |
| P3-6 | **HITL prompt boundary** | **Done (doc):** [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) — mandatory gates, no fake autonomous approval. |
| P3-7 | **SAFE UNKNOWN prompt rules** | **Done (doc):** [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md) — assumption discipline, fabrication forbidden, GOOD vs BAD. |
| P3-8 | **Artifact transfer prompt rules** | **Done (doc):** [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) — immutability, approval inheritance, revisions, QA inheritance. |
| P3-9 | **QA prompt rules** | **Done (doc):** [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) — evidence-based QA, no fake approvals, lane discipline. |
| P3-10 | **Frontend prompt discipline** | **Done (doc):** [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md) — Gulp-oriented source-first rules, SCSS modularity, data-* JS, no `dist/` edits. |

**Remaining (not claimed done):** deeper field binding to `task-contract-v0` wire examples, runbook artifacts beyond prompt-standard prose, automated prompt/QA checks — **SAFE UNKNOWN** until authored.

## Out of scope for phase 1

- Gulp project scaffolding in this repo.
- Figma plugins, n8n nodes, or Cursor extensions.
- Automated orchestration.

## Success criteria (documentation)

- Cross-links from `registry/project-registry.md` and `agents/registry.md` remain consistent.
- No **false** “production ready” language in phase 1 outputs.
