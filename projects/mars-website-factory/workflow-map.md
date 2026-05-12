# MARS Website Factory — workflow map

**Canonical orchestration chain (stages, contracts, escalation):** [website-factory-workflow-v0.md](website-factory-workflow-v0.md) — **Website Factory Workflow v0** (**documentation only**). This file remains the **diagram / HITL / execution-flow alignment** companion.

**Artifact semantics (Phase 2 doc):** [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md) — normalized **artifact / payload** vocabulary layered on this flow; **not** executable schemas.

**Prompt standards (Phase 3 doc):** [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md) — operational discipline for prompts, execution, reporting, HITL, SAFE UNKNOWN, artifact transfer, QA, and frontend; **not** a prompt engine, **not** a runtime. Each factory stage below maps to a **prompt boundary** per [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), executed in Cursor per [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md), reported per [reporting-standard-v0.md](reporting-standard-v0.md).

**Execution semantics (Phase 4 doc):** [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md) — operational methodology for **lifecycle behavior** of stages, artifacts, approvals, QA gates, revisions, regenerations, invalidations, signals, and delivery. Each stage below has a **state** ([stage-state-model-v0.md](stage-state-model-v0.md)); its artifacts have **states** ([artifact-state-model-v0.md](artifact-state-model-v0.md)); HITL gates anchor approvals ([approval-semantics-v0.md](approval-semantics-v0.md)); changes propagate per [dependency-invalidation-v0.md](dependency-invalidation-v0.md); QA verdicts behave per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md); release flows through [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md). **Not** a runtime engine, **not** a scheduler, **not** a queue, **not** a workflow daemon, **not** an autonomous execution platform.

**Reference project layer (Phase 4 / 5 doc boundary):** [reference-project-model-v0.md](reference-project-model-v0.md), [reference-project-artifact-tree-v0.md](reference-project-artifact-tree-v0.md), [reference-project-lifecycle-v0.md](reference-project-lifecycle-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md), [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md), [reference-delivery-package-v0.md](reference-delivery-package-v0.md), [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md) — **site-level** and **multi-artifact** operational reference (**project types**, packages, lifecycle tokens, HITL authority normalization, QA matrix, multi-page graph semantics). **Documentation only** — **no** project database, **no** orchestration engine, **no** hidden graph state in MARS.

**Semantic relationship layer (Phase 4 doc):** [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md) — **cross-artifact meaning**: semantic objects, relationships, inheritance, propagation, invalidation, authority, freeze, drift, consistency; linked [semantic-object-model-v0.md](semantic-object-model-v0.md), [cross-artifact-semantics-v0.md](cross-artifact-semantics-v0.md), [semantic-dependency-rules-v0.md](semantic-dependency-rules-v0.md), [semantic-inheritance-v0.md](semantic-inheritance-v0.md), [semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md), [site-semantic-graph-v0.md](site-semantic-graph-v0.md), [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md), [semantic-qa-rules-v0.md](semantic-qa-rules-v0.md). **Documentation only** — **not** a graph database, **not** a vector engine, **not** a semantic automation/runtime layer, **not** autonomous reasoning.

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
