# MARS Website Factory — workflow map

**Canonical orchestration chain (stages, contracts, escalation):** [website-factory-workflow-v0.md](website-factory-workflow-v0.md) — **Website Factory Workflow v0** (**documentation only**). This file remains the **diagram / HITL / execution-flow alignment** companion.

**First operational runbook (human execution layer v0):** [first-operational-runbook-v0.md](first-operational-runbook-v0.md) — reference sequence **R01–R15**, operator lanes, checkpoints **C01–C08**, artifact flow, failure/recovery prose, reporting alignment; **not** a workflow engine, **not** background orchestration, **not** autonomous routing.

**Reference execution case #1 (documentation-first):** [reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md](reference-cases/triumph-manipulator-landing/reference-case-overview-v0.md) — **Triumph / Manipulator Landing** end-to-end artifact chain (intake → strategy → IA → blueprint → handoffs → QA → validation → delivery readiness); **not** a production website build, **not** hidden automation.

**Client delivery execution case #2 (live workspace):** [reference-cases/isbd-care-landing/reference-case-overview-v1.md](reference-cases/isbd-care-landing/reference-case-overview-v1.md) — **ISBD Care Landing** (`isbd-care-landing`); Gulp workspace `workspaces/isbd-care-landing/`; registered in [execution-cases-registry-v1.md](execution-cases-registry-v1.md); **not** a MARS `project_id` program.

**Production project pack (initialized):** [../triumph-manipulator-landing/README.md](../triumph-manipulator-landing/README.md) — **Triumph / Manipulator Landing** governance folder, runbook, and Frontend Gulp Agent brief; local sources intended under [`../../workspaces/triumph-manipulator-landing/`](../../workspaces/triumph-manipulator-landing/) per project docs; **not** runtime, **not** deployed output by default.

**Operational templates layer (documentation v0):** [operational-template-overview-v0.md](operational-template-overview-v0.md) — reusable Markdown **shells** for project types (service / geo / catalog / multi-page / AI visibility posture), delivery/review gates (design, QA, HITL, revision, delivery readiness), bootstrap, and operator sessions; **distills** workflow + runbook + QA/HITL + prompt discipline into **copyable structure**; **not** runtime automation, **not** executable workflows, **not** orchestration daemons or generated Task/json pipelines.

**Artifact semantics (Phase 2 doc):** [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md) — normalized **artifact / payload** vocabulary layered on this flow; **not** executable schemas.

**Prompt standards (Phase 3 doc):** [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md) — operational discipline for prompts, execution, reporting, HITL, SAFE UNKNOWN, artifact transfer, QA, and frontend; **not** a prompt engine, **not** a runtime. Each factory stage below maps to a **prompt boundary** per [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), executed in Cursor per [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md), reported per [reporting-standard-v0.md](reporting-standard-v0.md).

**Execution semantics (Phase 4 doc):** [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md) — operational methodology for **lifecycle behavior** of stages, artifacts, approvals, QA gates, revisions, regenerations, invalidations, signals, and delivery. Each stage below has a **state** ([stage-state-model-v0.md](stage-state-model-v0.md)); its artifacts have **states** ([artifact-state-model-v0.md](artifact-state-model-v0.md)); HITL gates anchor approvals ([approval-semantics-v0.md](approval-semantics-v0.md)); changes propagate per [dependency-invalidation-v0.md](dependency-invalidation-v0.md); QA verdicts behave per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md); release flows through [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md). **Not** a runtime engine, **not** a scheduler, **not** a queue, **not** a workflow daemon, **not** an autonomous execution platform.

**Reference project layer (roadmap Phase 4 scope; [implementation-phase-1.md](implementation-phase-1.md) § Phase 5 (documentation)):** [reference-project-model-v0.md](reference-project-model-v0.md), [reference-project-artifact-tree-v0.md](reference-project-artifact-tree-v0.md), [reference-project-lifecycle-v0.md](reference-project-lifecycle-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md), [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md), [reference-delivery-package-v0.md](reference-delivery-package-v0.md), [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md) — **site-level** and **multi-artifact** operational reference (**project types**, packages, lifecycle tokens, HITL authority normalization, QA matrix, multi-page graph semantics). **Documentation only** — **no** project database, **no** orchestration engine, **no** hidden graph state in MARS.

**Semantic relationship layer (Phase 4 doc):** [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md) — **cross-artifact meaning**: semantic objects, relationships, inheritance, propagation, invalidation, authority, freeze, drift, consistency; linked [semantic-object-model-v0.md](semantic-object-model-v0.md), [cross-artifact-semantics-v0.md](cross-artifact-semantics-v0.md), [semantic-dependency-rules-v0.md](semantic-dependency-rules-v0.md), [semantic-inheritance-v0.md](semantic-inheritance-v0.md), [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md), [site-semantic-graph-v0.md](site-semantic-graph-v0.md), [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md), [semantic-qa-rules-v0.md](semantic-qa-rules-v0.md). **Documentation only** — **not** a graph database, **not** a vector engine, **not** a semantic automation/runtime layer, **not** autonomous reasoning.

**Artifact bus layer (Phase 4 doc):** [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md) — **document-first transfer movement**: envelope, routing, transfer/lineage/publication/consumption, governance, delivery-bus slice, transfer QA; linked [artifact-envelope-model-v0.md](artifact-envelope-model-v0.md), [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md), [artifact-transfer-semantics-v0.md](artifact-transfer-semantics-v0.md), [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md), [artifact-publication-semantics-v0.md](artifact-publication-semantics-v0.md), [artifact-consumption-rules-v0.md](artifact-consumption-rules-v0.md), [artifact-governance-rules-v0.md](artifact-governance-rules-v0.md), [delivery-bus-semantics-v0.md](delivery-bus-semantics-v0.md), [artifact-transfer-qa-rules-v0.md](artifact-transfer-qa-rules-v0.md). **Cross-layer placement:** [layer-map.md](layer-map.md) §8. **Documentation only** — **not** a queue, **not** an event engine, **not** a runtime message bus (Kafka/Rabbit/etc.), **not** async execution infrastructure, **not** hidden transport.

**Validation runtime model (Phase 4 doc):** [validation-runtime-overview-v0.md](validation-runtime-overview-v0.md) — **documentation-only** validation semantics, lifecycle tokens, evidence/result/failure/waiver/escalation/consistency vocabulary, honesty boundary; linked [validation-lifecycle-v0.md](validation-lifecycle-v0.md), [validator-execution-model-v0.md](validator-execution-model-v0.md), [validation-evidence-model-v0.md](validation-evidence-model-v0.md), [validation-result-semantics-v0.md](validation-result-semantics-v0.md), [validation-failure-semantics-v0.md](validation-failure-semantics-v0.md), [validation-waiver-semantics-v0.md](validation-waiver-semantics-v0.md), [validation-escalation-model-v0.md](validation-escalation-model-v0.md), [validation-consistency-model-v0.md](validation-consistency-model-v0.md), [validation-runtime-boundary-v0.md](validation-runtime-boundary-v0.md). **Not** a validator engine, **not** CI, **not** background workers, **not** Lighthouse/crawl automation, **not** autonomous enforcement.

## Target high-level flow

```text
Intake
  → Strategy
  → Information Architecture
  → Page Blueprint (see page-blueprint-contract-v0.md, page-blueprint-qa-checklist-v0.md)
  → Wireframe
  → Design (handoff: design-handoff-contract-v0.md)
  → Frontend Production (handoff: frontend-handoff-contract-v0.md)
  → QA
  → Human approval
  → Delivery
```

This is a **target** pipeline for **documentation and future orchestration** — not evidence of an automated engine in this repo.

## Frontend page QA sub-chain (greenfield / page closure)

After **Frontend Production** produces a page or slice (post–Foundation QA and Home work), **Production PASS** requires the documented gate chain — **not** compact operational QA alone:

```text
Page / block production
        ↓
Design Completeness Audit
        ↓
Frontend Design QA Matrix (full)
        ↓
Pixel Fidelity Audit
        ↓
Production PASS
```

**Foundation path (pre–Home):** Production Standards Draft → Mapping QA → Approval → **Canonical Clean Shell v1** → **Group Decomposition (APPROVED)** → **Layout Spec (APPROVED)** → Shell → Visual Foundation → Design Calibration → Foundation QA — [canonical-clean-shell-v1.md](canonical-clean-shell-v1.md) · [group-decomposition-law-v1.md](group-decomposition-law-v1.md) · [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md) · [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) · [layout-spec-law-v1.md](layout-spec-law-v1.md).

**JPG / clean-room foundation path (2026-06-22):** When visual source is raster audit only (e.g. FP-0002 V6), use **[frontend-implementation-pipeline-v1.md](frontend-implementation-pipeline-v1.md)** — SOURCE → VISUAL AUDIT → GROUNDING → **DESIGN FOUNDATION EXTRACTION** → **PRACTICAL VALUE NORMALIZATION** → **SITE-WIDE STYLE FOUNDATION** (operator approval) → PAGE/BLOCK IMPLEMENTATION SPECIFICATION → HTML → SCSS → VISUAL QA. **Do not** skip to HTML after structure lock. Contracts: [practical-value-normalization-contract-v1.md](practical-value-normalization-contract-v1.md) · [site-wide-style-foundation-contract-v1.md](site-wide-style-foundation-contract-v1.md) · [block-implementation-specification-contract-v1.md](block-implementation-specification-contract-v1.md).

**Reporting rollup:** [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §5–§6 · **Production PASS authority:** [operational-qa-entry-v1.md](operational-qa-entry-v1.md) § Production PASS authority.

## Prompt → execute → report

MARS **Workflow layer** documents a richer chain: `prompt` → `task` → `plan` → `route` → `execute` → `validate` → `report` → `log` (`workflows/execution-flow.md`). The **Website Factory** aligns each factory stage with that model:

| Factory stage | Typical mapping to execution-flow |
|---------------|-----------------------------------|
| Intake / classifier | **prompt** → **task** (draft) |
| Strategy / IA / blueprint | **plan**, **route** |
| Wireframe / design / frontend | **execute** (specialist agents) |
| QA | **validate** |
| Delivery pack | **report** |
| Audit / lifecycle | **log** (future observability) |

The **legacy operational shorthand** “prompt → execute → report” remains valid for **human-driven** steps (`web-gpt-sources/05_workflows.md`, `web-gpt-sources/02_architecture.md` — as **requirements**, not v1 implementation).

## Cursor execution model (Phase 1)

Per `governance/execution-model.md` and [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md):

- **Today**, filesystem work is performed in a **user-controlled** environment (e.g. **Cursor**), not by a MARS daemon.
- Factory stages translate to **Cursor prompt bundles**: context window, **AGENT** vs **ASK** mode per project rules, explicit paths, git safety, REPORT discipline.
- **Execution Bridge** (`mars-runtime/execution-bridge-v0.md`) may **eventually** package handoffs; **no** Website Factory–specific wire format is defined yet (**SAFE UNKNOWN**).

## Future runtime integration

| Aspect | Intent |
|--------|--------|
| **MARS runtime** | Could bind **Tasks**, persist state, dispatch agents per `control-plane/contract.md` — **planned-implementation**. |
| **n8n / external** | Optional; same boundary discipline as **MetaBOT** docs — external runtime **not** owned by MARS core. |
| **Factory** | Becomes a **workflow template** + registry IDs, not a hard-coded single agent. |

## HITL checkpoints

Suggested **human approval** gates (refine per `security/approval-gates.md` and **Task** `hitl_gates`):

1. After **Strategy** — brand/compliance sensitivity.
2. After **Page Blueprint** — scope/size/cost; validate against [Page Blueprint QA Checklist v0](page-blueprint-qa-checklist-v0.md) before approving handoff.
3. After **Design** — before **Frontend Production**.
4. After **QA** — before **Delivery** / public deploy.

## Artifact approval gates

| Gate | Artifact | Typical approver |
|------|----------|------------------|
| G1 | Intake + classification | PM / lead |
| G2 | Strategy + SEO hypotheses | Marketing lead |
| G3 | Sitemap + blueprints | PM + tech lead |
| G4 | Wireframes | UX / client |
| G5 | Full design | Design lead / client |
| G6 | Frontend PR / file set | Tech + design |
| G7 | Release | Ops / client |

## Signals

Use governance signals consistently: **UNKNOWN**, **SAFE UNKNOWN**, **NEED HUMAN APPROVAL**, **SECURITY RISK**, **STRUCTURE CHANGE** (`governance/system-signals-dictionary.md`, `workflows/task-contract-v0.md`).
