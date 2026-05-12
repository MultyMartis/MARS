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

## Phase 5 (documentation) — reference project layer v0

| # | Deliverable | Description |
|---|-------------|-------------|
| P5-1 | **Reference project model** | **Done (doc):** [reference-project-model-v0.md](reference-project-model-v0.md) — project kinds, conceptual fields (`project_id`, `project_type`, scopes, states, policies); **SAFE UNKNOWN** for storage, persistence, DB, engines. |
| P5-2 | **Reference artifact tree** | **Done (doc):** [reference-project-artifact-tree-v0.md](reference-project-artifact-tree-v0.md) — Intake→Delivery chain; lineage, inheritance, freeze, supersede vs revision; per-stage upstream/downstream/owner/QA/HITL. |
| P5-3 | **Reference project lifecycle** | **Done (doc):** [reference-project-lifecycle-v0.md](reference-project-lifecycle-v0.md) — lifecycle states, entry/exit, blocking, invalidation, QA, HITL; **not** a persisted state machine. |
| P5-4 | **Reference HITL governance** | **Done (doc):** [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md) — normalized authorities; irreversible/conditional approvals; inheritance/invalidation; forbids self-approval, autonomous approval, fake delivery acceptance. |
| P5-5 | **Reference QA matrix** | **Done (doc):** [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md) — stage × QA table; waivers, inheritance, invalidation resets, SAFE UNKNOWN handling. |
| P5-6 | **Reference delivery packages** | **Done (doc):** [reference-delivery-package-v0.md](reference-delivery-package-v0.md) — blueprint/design/frontend/QA/export/RC/delivery candidate package semantics. |
| P5-7 | **Multi-page orchestration** | **Done (doc):** [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md) — site graph semantics, clusters, linking, cannibalization, page vs site QA, cluster invalidation; **no** automation/orchestration-daemon claims. |

**Remaining (not claimed done):** deeper field binding to `task-contract-v0` wire examples, runbook artifacts beyond layer prose, automated prompt / QA / lifecycle checks — **SAFE UNKNOWN** until authored.

## Phase 6 (documentation) — semantic relationship layer v0

| # | Deliverable | Description |
|---|-------------|-------------|
| P6-1 | **Semantic relationship overview** | **Done (doc):** [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md) — definitions, non-claims, alignment with adjacent layers. |
| P6-2 | **Semantic object model** | **Done (doc):** [semantic-object-model-v0.md](semantic-object-model-v0.md) — canonical objects, ownership, lineage, supersede, drift. |
| P6-3 | **Cross-artifact semantics** | **Done (doc):** [cross-artifact-semantics-v0.md](cross-artifact-semantics-v0.md) — Blueprint→Delivery; mismatch, drift, downgrade, freeze break. |
| P6-4 | **Semantic dependency rules** | **Done (doc):** [semantic-dependency-rules-v0.md](semantic-dependency-rules-v0.md) — dependency kinds, severity, propagation scope, **SAFE UNKNOWN**. |
| P6-5 | **Semantic inheritance** | **Done (doc):** [semantic-inheritance-v0.md](semantic-inheritance-v0.md) — site→component chain; overrides; **inheritance ≠ runtime propagation**. |
| P6-6 | **Semantic consistency rules** | **Done (doc):** [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md) — C0–C3, escalation, freeze break, delivery blocking. |
| P6-7 | **Site semantic graph (conceptual)** | **Done (doc):** [site-semantic-graph-v0.md](site-semantic-graph-v0.md) — conceptual graph only; **not** a graph DB. |
| P6-8 | **Semantic freeze semantics** | **Done (doc):** [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md) — freeze, reopen, supersede, rollback, HITL. |
| P6-9 | **Semantic QA rules** | **Done (doc):** [semantic-qa-rules-v0.md](semantic-qa-rules-v0.md) — semantic QA scope, findings, evidence, waivers. |

## Phase 7 (documentation) — artifact bus layer v0

| # | Deliverable | Description |
|---|-------------|-------------|
| P7-1 | **Artifact bus overview** | **Done (doc):** [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md) — bus philosophy, definitions, non-claims (no queue/event/runtime bus). |
| P7-2 | **Envelope model** | **Done (doc):** [artifact-envelope-model-v0.md](artifact-envelope-model-v0.md) — minimum fields, immutable/mutable regions, supersede, stale/orphan. |
| P7-3 | **Routing rules** | **Done (doc):** [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md) — allowed/forbidden/partial/revision/rollback/invalidation/QA/delivery routes; authority; freeze. |
| P7-4 | **Transfer semantics** | **Done (doc):** [artifact-transfer-semantics-v0.md](artifact-transfer-semantics-v0.md) — inheritance, invalidation, downgrade, freeze break, partial transfer. |
| P7-5 | **Lineage semantics** | **Done (doc):** [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md) — parent/child/sibling/supersede/rollback/branch/frozen; drift; invalidation; orphaning. |
| P7-6 | **Publication semantics** | **Done (doc):** [artifact-publication-semantics-v0.md](artifact-publication-semantics-v0.md) — publication classes, authority, visibility, freeze, rollback. |
| P7-7 | **Consumption rules** | **Done (doc):** [artifact-consumption-rules-v0.md](artifact-consumption-rules-v0.md) — consume/reject/invalidate/reopen/partial; authority; stale/orphan/invalid. |
| P7-8 | **Artifact governance** | **Done (doc):** [artifact-governance-rules-v0.md](artifact-governance-rules-v0.md) — immutability, revision/rollback/freeze/delivery governance; explicit prohibitions. |
| P7-9 | **Delivery bus semantics** | **Done (doc):** [delivery-bus-semantics-v0.md](delivery-bus-semantics-v0.md) — release/delivery candidate, packages, authorities; pairs with [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md); **not** CI/CD automation. |
| P7-10 | **Transfer QA rules** | **Done (doc):** [artifact-transfer-qa-rules-v0.md](artifact-transfer-qa-rules-v0.md) — transfer-layer finding classes, severity, blocking, waivers, **SAFE UNKNOWN**. |

**Placement:** factory-wide bus semantics vs stage stacks — [layer-map.md](layer-map.md) §8.

## Out of scope for phase 1

- Gulp project scaffolding in this repo.
- Figma plugins, n8n nodes, or Cursor extensions.
- Automated orchestration.

## Success criteria (documentation)

- Cross-links from `registry/project-registry.md` and `agents/registry.md` remain consistent.
- No **false** “production ready” language in phase 1 outputs.
