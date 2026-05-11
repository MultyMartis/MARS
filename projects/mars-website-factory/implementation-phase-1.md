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

## Phase 4 (documentation) — execution semantics layer v0

| # | Deliverable | Description |
|---|-------------|-------------|
| P4-1 | **Execution semantics overview** | **Done (doc):** [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md) — purpose, philosophy, non-claims; semantics ≠ implementation; no scheduler / queue / daemon. |
| P4-2 | **Stage state model** | **Done (doc):** [stage-state-model-v0.md](stage-state-model-v0.md) — conceptual stage states, allowed / forbidden transitions, ownership, freeze, reopen, invalidation. |
| P4-3 | **Artifact state model** | **Done (doc):** [artifact-state-model-v0.md](artifact-state-model-v0.md) — lifecycle, mutable / immutable regions, lineage, references, replacement philosophy, QA / SAFE UNKNOWN handling. |
| P4-4 | **Approval semantics** | **Done (doc):** [approval-semantics-v0.md](approval-semantics-v0.md) — meaning, scope, partial / conditional / inheritance / expiration / revocation; QA-linked / delivery approvals; HITL-only. |
| P4-5 | **Revision semantics** | **Done (doc):** [revision-semantics-v0.md](revision-semantics-v0.md) — requests, scope, lineage, ownership, impact, freeze breaking, escalation, QA reset, history. |
| P4-6 | **Regeneration semantics** | **Done (doc):** [regeneration-semantics-v0.md](regeneration-semantics-v0.md) — partial vs full, safe vs unsafe, boundaries, triggers, dependency-aware, QA invalidation; no autonomous regeneration. |
| P4-7 | **Dependency invalidation** | **Done (doc):** [dependency-invalidation-v0.md](dependency-invalidation-v0.md) — upstream/downstream propagation across artifact / approval / QA / lane; site type / CTA / trust / block / mobile UX examples. |
| P4-8 | **Orchestration signals** | **Done (doc):** [orchestration-signals-v0.md](orchestration-signals-v0.md) — canonical + factory tokens; source, propagation, escalation, resolution, lifecycle. |
| P4-9 | **QA gating semantics** | **Done (doc):** [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) — gate lifecycle, blocker / pass / fail / conditional / waiver / confidence / evidence / freeze / delivery blocking / HITL override. |
| P4-10 | **Delivery lifecycle** | **Done (doc):** [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) — candidate, pre-delivery validation, release approval, freeze, export package, deployment handoff, rollback, archive, post-delivery revision; no deployment automation claims. |

**Remaining (not claimed done):** deeper field binding to `task-contract-v0` wire examples, runbook artifacts beyond layer prose, automated prompt / QA / lifecycle checks — **SAFE UNKNOWN** until authored.

## Out of scope for phase 1

- Gulp project scaffolding in this repo.
- Figma plugins, n8n nodes, or Cursor extensions.
- Automated orchestration.

## Success criteria (documentation)

- Cross-links from `registry/project-registry.md` and `agents/registry.md` remain consistent.
- No **false** “production ready” language in phase 1 outputs.
