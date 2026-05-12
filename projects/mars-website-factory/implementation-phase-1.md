# MARS Website Factory — implementation phase 1 (doc-first)

**Scope:** **Documentation and contracts only** — **no** code generation mandate, **no** new runtime.

**Numbering note:** Sections titled **Phase 5–8 (documentation)** below are **in-pack documentation milestone groups** (reference project layer, semantic relationship layer, artifact bus layer, validation runtime model). They **roll up to** [roadmap.md](roadmap.md) **Phase 4** (documentation maturity for execution semantics, reference/semantic/bus/validation docs). They **do not** mean [roadmap.md](roadmap.md) **Phase 5** (Cursor-assisted production) or **Phases 6–7** (runtime / automation) — those are **later** roadmap bands, not the section numbers used here. Sections **Phase 9–10 (documentation)** (**first operational runbook v0**, **operational templates layer v0**) **roll up to** [roadmap.md](roadmap.md) **Phase 5** — still **documentation only**, **not** runtime.

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

**Remaining (not claimed done):** deeper field binding to `task-contract-v0` wire examples, additional stage-sized prompt bundles beyond first operational v0, automated prompt / QA / lifecycle checks — **SAFE UNKNOWN** until authored.

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

## Phase 8 (documentation) — validation runtime model v0

| # | Deliverable | Description |
|---|-------------|-------------|
| P8-1 | **Validation runtime overview** | **Done (doc):** [validation-runtime-overview-v0.md](validation-runtime-overview-v0.md) — purpose, boundaries, layer connectivity, HITL/evidence philosophy, explicit prohibitions (no autonomous validator runtime, hidden engine, auto-repair/approval/waiver). |
| P8-2 | **Validation lifecycle** | **Done (doc):** [validation-lifecycle-v0.md](validation-lifecycle-v0.md) — stages, transitions, forbidden transitions, revalidation, invalidation, freeze, dependency invalidation, HITL ownership. |
| P8-3 | **Validator execution model** | **Done (doc):** [validator-execution-model-v0.md](validator-execution-model-v0.md) — conceptual inputs/outputs; no scheduler/queue/distributed runtime/workers; no deterministic LLM validation guarantee. |
| P8-4 | **Validation evidence model** | **Done (doc):** [validation-evidence-model-v0.md](validation-evidence-model-v0.md) — evidence classes, confidence, provenance, freshness/stale, GOOD vs BAD examples. |
| P8-5 | **Validation result semantics** | **Done (doc):** [validation-result-semantics-v0.md](validation-result-semantics-v0.md) — result fields, V0–V3 severity mapping, alignment with QA payloads. |
| P8-6 | **Validation failure semantics** | **Done (doc):** [validation-failure-semantics-v0.md](validation-failure-semantics-v0.md) — failure kinds, propagation, invalidation, downstream impact, re-open logic. |
| P8-7 | **Validation waiver semantics** | **Done (doc):** [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md) — waiver types/authority; forbids silent/auto/implicit inheritance waivers. |
| P8-8 | **Validation escalation model** | **Done (doc):** [validation-escalation-model-v0.md](validation-escalation-model-v0.md) — triggers, authority, routing (documentation sense), freeze, signal mapping. |
| P8-9 | **Validation consistency model** | **Done (doc):** [validation-consistency-model-v0.md](validation-consistency-model-v0.md) — cross-artifact/semantic/approval/QA/lineage/freeze/delivery consistency; contradictions; cascades. |
| P8-10 | **Validation runtime boundary** | **Done (doc):** [validation-runtime-boundary-v0.md](validation-runtime-boundary-v0.md) — honesty list of non-deliverables (no engine, CI, background validation, Lighthouse/crawl, graph DB, persistence). |

## Phase 9 (documentation) — first operational runbook v0

| # | Deliverable | Description |
|---|-------------|-------------|
| P9-1 | **First operational runbook v0** | **Done (doc):** [first-operational-runbook-v0.md](first-operational-runbook-v0.md) — purpose, scope, philosophy, “run” definition, relationships to workflow v0 / HITL / Cursor / artifacts / Validator+QA; explicit non-runtime prohibitions. |
| P9-2 | **Reference run sequence** | **Done (doc):** [reference-run-sequence-v0.md](reference-run-sequence-v0.md) — R01–R15 owner/inputs/outputs/artifacts/QA/HITL/freeze/invalidation/reporting per step. |
| P9-3 | **Operator lane model** | **Done (doc):** [operator-lane-model-v0.md](operator-lane-model-v0.md) — strategy/SEO/UX/design/frontend/QA/HITL/Validator observer lanes; authority; global prohibitions (no self-approval, silent overrides, hidden revisions). |
| P9-4 | **Human supervision model** | **Done (doc):** [human-supervision-model-v0.md](human-supervision-model-v0.md) — checkpoints cadence, approval/escalation/freeze/SAFE UNKNOWN supervision. |
| P9-5 | **Project execution checkpoints** | **Done (doc):** [project-execution-checkpoints-v0.md](project-execution-checkpoints-v0.md) — C01–C08 evidence, blockers, rollback rules, waivers, reports. |
| P9-6 | **Reference run artifact flow** | **Done (doc):** [reference-run-artifact-flow-v0.md](reference-run-artifact-flow-v0.md) — movement, lineage, freeze/revision/invalidation/QA propagation; diagram; SAFE UNKNOWN + blocked routes. |
| P9-7 | **Reference run failure & recovery** | **Done (doc):** [reference-run-failure-recovery-v0.md](reference-run-failure-recovery-v0.md) — partial failure, stage rollback, QA fail, stale artifacts, freeze break, delivery rollback, escalation; **no automatic rollback engine**. |
| P9-8 | **Reference run reporting** | **Done (doc):** [reference-run-reporting-v0.md](reference-run-reporting-v0.md) — stage/QA/escalation/invalidation/delivery/freeze/revision reports aligned to [reporting-standard-v0.md](reporting-standard-v0.md). |
| P9-9 | **Reference execution case #1 (Triumph Manipulator Landing)** | **Done (doc):** [reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md](reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md) + linked v0 artifacts — intake through delivery readiness as a **documented simulation**; **not** a built site, **not** runtime orchestration. |

## Phase 10 (documentation) — operational templates layer v0

| # | Deliverable | Description |
|---|-------------|-------------|
| P10-1 | **Operational templates overview** | **Done (doc):** [operational-template-overview-v0.md](operational-template-overview-v0.md) — definitions, relationships to workflow / artifact bus / execution semantics / reference runs / prompt standards / QA / HITL; **templates ≠ runtime automation**. |
| P10-2 | **Reference + site-type templates** | **Done (doc):** [reference-project-template-v0.md](reference-project-template-v0.md), [service-landing-template-v0.md](service-landing-template-v0.md), [geo-landing-template-v0.md](geo-landing-template-v0.md), [catalog-project-template-v0.md](catalog-project-template-v0.md), [ai-visibility-template-v0.md](ai-visibility-template-v0.md), [multi-page-site-template-v0.md](multi-page-site-template-v0.md) — reusable shells; **no** ranking / LLM outcome / deploy guarantees where prohibited. |
| P10-3 | **Delivery + review templates** | **Done (doc):** [frontend-delivery-template-v0.md](frontend-delivery-template-v0.md), [design-review-template-v0.md](design-review-template-v0.md), [qa-review-template-v0.md](qa-review-template-v0.md), [hitl-review-template-v0.md](hitl-review-template-v0.md), [revision-cycle-template-v0.md](revision-cycle-template-v0.md), [delivery-readiness-template-v0.md](delivery-readiness-template-v0.md) — Gulp-oriented frontend discipline, evidence-first QA, HITL without fake signatures, readiness without deployment claims. |
| P10-4 | **Bootstrap + session templates** | **Done (doc):** [project-bootstrap-template-v0.md](project-bootstrap-template-v0.md), [operator-session-template-v0.md](operator-session-template-v0.md) — project start + Cursor session REPORT/git/artifact hygiene. |

**Numbering note:** This **Phase 10** section is an **in-pack documentation milestone group** for operational templates; it **rolls up to** [roadmap.md](roadmap.md) **Phase 5** (Cursor-assisted production **documentation**) alongside the first operational runbook and reference execution case — **not** roadmap Phase 10 (Model layer in [master-build-map.md](../../governance/master-build-map.md)).

## Out of scope for phase 1

- Gulp project scaffolding in this repo.
- Figma plugins, n8n nodes, or Cursor extensions.
- Automated orchestration.

## Success criteria (documentation)

- Cross-links from `registry/project-registry.md` and `agents/registry.md` remain consistent.
- No **false** “production ready” language in phase 1 outputs.
