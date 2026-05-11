# MARS Website Factory — Execution Semantics Overview v0

**Status:** **documentation only** — **operational methodology** and **runtime-preparation architecture** for how factory stages, artifacts, approvals, QA, and HITL **behave over time**. **Not** a runtime engine, **not** an orchestration implementation, **not** a scheduler, **not** a queue system, **not** a workflow daemon, **not** an autonomous execution platform.

**Version:** v0.

**Related:**

- Workflow: [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [workflow-map.md](workflow-map.md).
- Artifacts: [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md), [artifact-types-v0.md](artifact-types-v0.md).
- Prompt standards: [prompt-standards-overview-v0.md](prompt-standards-overview-v0.md), [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md), [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [reporting-standard-v0.md](reporting-standard-v0.md).
- Sibling execution-semantics docs: [stage-state-model-v0.md](stage-state-model-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [orchestration-signals-v0.md](orchestration-signals-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md).
- Honesty: [safe-unknown-boundary.md](safe-unknown-boundary.md), [`../../AGENTS.md`](../../AGENTS.md).
- Governance: [`../../governance/execution-model.md`](../../governance/execution-model.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md), [`../../control-plane/contract.md`](../../control-plane/contract.md), [`../../workflows/task-contract-v0.md`](../../workflows/task-contract-v0.md), [`../../workflows/execution-flow.md`](../../workflows/execution-flow.md).

---

## 1. Purpose

The factory already has:

- **stages** ([website-factory-workflow-v0.md](website-factory-workflow-v0.md) §S01–S15),
- **artifacts** ([artifact-types-v0.md](artifact-types-v0.md)),
- **contracts** ([page-blueprint-contract-v0.md](page-blueprint-contract-v0.md), [design-handoff-contract-v0.md](design-handoff-contract-v0.md), [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md)),
- **prompt standards** ([prompt-standards-overview-v0.md](prompt-standards-overview-v0.md) and siblings),
- **QA payloads** ([qa-result-payloads-v0.md](qa-result-payloads-v0.md)),
- **HITL gates** ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [workflow-map.md](workflow-map.md) §HITL).

The **Execution Semantics Layer v0** adds the **lifecycle behavior** that ties those pieces together: how **stages transition**, how **artifacts mutate or freeze**, how **approvals propagate and expire**, how **revisions invalidate downstream work**, how **QA gates pass or block**, how **regeneration is bounded**, how **signals travel**, and how **delivery is finalized**.

It answers **operational** questions about **time** and **state**:

- When does a stage become **ready** vs **blocked** vs **frozen**?
- When does an artifact become **immutable** and when does that immutability **break**?
- What happens to downstream artifacts when an upstream artifact changes?
- How is a **revision** different from a **regeneration** and from a **rollback**?
- When does a **QA gate** pass, fail, or pass **conditionally**?
- How does **delivery** authorize release without claiming deployment automation?

It does **not** answer **implementation** questions about queues, schedulers, daemons, or autonomous execution.

---

## 2. Why execution semantics are needed

### 2.1 Documentation defines shape; semantics define behavior

Workflow v0 names **what stages exist** and **what artifacts cross them**. Artifact architecture v0 names **what artifacts mean**. Prompt standards v0 names **how a prompt is shaped**. None of those documents fully define **how the system behaves over time** when:

- a previously approved artifact must be revised,
- a downstream stage discovers an upstream contradiction,
- a QA gate passes conditionally with bounded CRs,
- a delivery candidate is rolled back to a prior baseline,
- a stage is partially rerun for a single page rather than the whole site.

Without execution semantics, those situations devolve into **ad hoc human judgment**, which:

- breaks **artifact integrity** at handoff boundaries;
- weakens **QA traceability**;
- silently invalidates approvals;
- mixes **revision** with **regeneration** with **rollback**;
- prevents future **Control Plane** routing per [`../../control-plane/contract.md`](../../control-plane/contract.md) from binding the same lifecycle twice;
- forces fabrication when humans (or LLMs) cannot remember what was frozen.

### 2.2 Trust depends on bounded lifecycle behavior

A factory stage must behave **predictably and auditably** not only at first execution but across **revisions, regenerations, invalidations, and rollbacks**. That requires explicit semantics for:

- when a stage may **start**, **pause**, **freeze**, **reopen**, or **archive**;
- when an artifact may **mutate**, **supersede**, or be **invalidated**;
- when an approval **inherits**, **expires**, or is **revoked**;
- when a QA verdict becomes **stale**.

A factory that cannot answer those questions is a factory that **cannot honestly deliver**.

### 2.3 “Re-run everything” is forbidden

A naive lifecycle policy that says "any change re-runs the whole factory" is **not** acceptable in v0. It:

- destroys partial progress;
- defeats artifact reuse;
- masks dependency boundaries;
- inflates HITL cost;
- pretends that regeneration is free.

**v0 rule:** lifecycle behavior must be **dependency-aware** ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)), **scoped** ([regeneration-semantics-v0.md](regeneration-semantics-v0.md), [revision-semantics-v0.md](revision-semantics-v0.md)), and **HITL-anchored** ([approval-semantics-v0.md](approval-semantics-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)).

---

## 3. Distinct concepts (terminology)

The execution-semantics layer **does not** redefine workflow, artifact, prompt, QA, or HITL terms. It refines **behavior over time** for those existing concepts and uses the following normalized distinctions.

| Term | Meaning in v0 |
|------|----------------|
| **Workflow** | The **ordered process** of stages ([website-factory-workflow-v0.md](website-factory-workflow-v0.md)). Describes **shape**, not behavior. |
| **Execution** | A **single pass** through a workflow slice — one or more stages run in sequence for a defined scope (e.g. a page, a batch, a full site). Today: **human-driven** in Cursor per [`../../governance/execution-model.md`](../../governance/execution-model.md). |
| **Artifact lifecycle** | The **state progression** of a logical deliverable: `draft → in_review → approved → frozen → superseded / invalidated / archived` ([artifact-state-model-v0.md](artifact-state-model-v0.md)). Anchored to [artifact-types-v0.md](artifact-types-v0.md). |
| **Stage state** | The **state progression** of a workflow stage instance: `not_started → ready → blocked → executing → waiting_hitl → qa_review → approved → rejected → frozen → invalidated → archived` ([stage-state-model-v0.md](stage-state-model-v0.md)). |
| **Orchestration** | The **conceptual routing and coordination** of stages, artifacts, and signals. In v0 it is **prose discipline** + future Control Plane intent; **no** scheduler or daemon. |
| **Approval lifecycle** | The **lifecycle of HITL approvals**: granted, scoped, conditional, inherited, expired, revoked ([approval-semantics-v0.md](approval-semantics-v0.md)). |
| **QA lifecycle** | The **lifecycle of QA gates** and verdicts: open, pass, fail, conditional, waived, stale ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)). |
| **Revision** | A **deliberate scope-bounded change** to an already-approved or frozen artifact ([revision-semantics-v0.md](revision-semantics-v0.md)). |
| **Regeneration** | The **re-production** of artifact content, full or partial, with explicit boundaries ([regeneration-semantics-v0.md](regeneration-semantics-v0.md)). |
| **Invalidation** | The **propagation** of upstream changes into downstream artifacts, approvals, QA states ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)). |
| **Signal** | A **named state hint** flowing through workflow narrative: `UNKNOWN`, `SAFE UNKNOWN`, `NEED HUMAN APPROVAL`, `STRUCTURE CHANGE`, `SECURITY RISK`, plus factory-layer extensions documented in [orchestration-signals-v0.md](orchestration-signals-v0.md). |
| **Delivery lifecycle** | The **release-side state progression**: delivery candidate → pre-delivery validation → release approval → frozen release → handoff → post-delivery revision ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md)). |

A **workflow stage** is not the same as **its instance running for a project**; a **contract** is not the same as **an artifact filed under that contract**; an **approval** is not the same as **an approval artifact** that records a HITL decision.

---

## 4. Relationship map

```text
              workflow stage (shape)
                       │
                       ▼
              stage state (over time)
                       │
                       ▼
                  artifact(s)
                       │
                       ▼
             artifact state (over time)
                       │
                       ▼
                  QA gate(s)
                       │
                       ▼
                 QA lifecycle
                       │
                       ▼
                HITL gate(s)
                       │
                       ▼
              approval lifecycle
                       │
              (revision / regeneration /
               invalidation / rollback)
                       │
                       ▼
              delivery lifecycle
                       │
                       ▼
                  release / archive
```

The same prompt that drives a stage ([prompt-structure-standard-v0.md](prompt-structure-standard-v0.md)) also **announces** which lifecycle transitions it intends to cause, and the report ([reporting-standard-v0.md](reporting-standard-v0.md)) records which transitions actually occurred. Lifecycle correctness is **observable in prose**, not enforced by a runtime.

---

## 5. Relationship to future runtime

When (and **if**) a Control Plane, Execution Bridge, or runtime exists per [`../../governance/execution-model.md`](../../governance/execution-model.md), [`../../mars-runtime/execution-bridge-v0.md`](../../mars-runtime/execution-bridge-v0.md), [`../../mars-runtime/execution-orchestrator-v0.md`](../../mars-runtime/execution-orchestrator-v0.md), [`../../mars-runtime/run-lifecycle-v0.md`](../../mars-runtime/run-lifecycle-v0.md), and [`../../storage/runtime-state-store-v0.md`](../../storage/runtime-state-store-v0.md):

- **stage states** become persisted **state-store rows**;
- **artifact states** become **records** referenced by stage rows;
- **signals** become enumerated values per [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md);
- **approval lifecycle** maps onto **`hitl_gates`** on Task Contract;
- **revisions / regenerations / invalidations** map onto **lifecycle events** ([`../../mars-runtime/run-lifecycle-v0.md`](../../mars-runtime/run-lifecycle-v0.md)) and **checkpoint / resume** boundaries ([`../../storage/checkpoint-resume-protocol-v0.md`](../../storage/checkpoint-resume-protocol-v0.md));
- **QA gate verdicts** map onto **`validate` stage outputs** ([`../../workflows/execution-flow.md`](../../workflows/execution-flow.md));
- **delivery lifecycle** maps onto **release-gated tasks** with **HITL** approval.

**Until then**, execution semantics are **human-facing operational discipline**. Nothing here implies that a runtime parses these documents or enforces these transitions automatically.

---

## 6. Relationship to HITL

HITL ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)) remains **authoritative** for any state transition that:

- **freezes** an artifact baseline;
- **approves** a stage exit;
- **waives** a QA blocker;
- **revokes** an earlier approval;
- **authorizes** delivery or release.

No execution-semantics document allows an agent or automation to perform those transitions **on its own**. Every approval-bearing transition is described **as a HITL-issued event** with an Approval artifact ([artifact-types-v0.md](artifact-types-v0.md) §Approval artifact).

---

## 7. Relationship to prompt standards

Prompt standards ([prompt-standards-overview-v0.md](prompt-standards-overview-v0.md) and siblings) **shape instructions**. Execution semantics **shape state**. A well-formed prompt:

- declares which **stage state** it intends to advance to ([stage-state-model-v0.md](stage-state-model-v0.md));
- declares which **artifact state** it intends to change ([artifact-state-model-v0.md](artifact-state-model-v0.md));
- declares any **revision** or **regeneration** scope ([revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md));
- declares any **invalidation** it may cause ([dependency-invalidation-v0.md](dependency-invalidation-v0.md));
- declares any **signal** it expects to emit ([orchestration-signals-v0.md](orchestration-signals-v0.md));
- declares its **HITL boundary** ([approval-semantics-v0.md](approval-semantics-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)).

A prompt that omits its lifecycle effects is **not** a factory prompt — it is a request to mutate state silently, which the factory forbids.

---

## 8. Relationship to artifacts and contracts

The execution-semantics layer is **purely behavioral**. It **does not**:

- redefine contract fields;
- introduce new artifact classes;
- change registry semantics;
- alter handoff boundaries.

It **does**:

- give every artifact class ([artifact-types-v0.md](artifact-types-v0.md)) a **named state model** ([artifact-state-model-v0.md](artifact-state-model-v0.md));
- give every handoff a **lifecycle dependency** ([dependency-invalidation-v0.md](dependency-invalidation-v0.md));
- give every approval inheritance rule ([artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) §5) a **time dimension** ([approval-semantics-v0.md](approval-semantics-v0.md));
- give every QA payload field ([qa-result-payloads-v0.md](qa-result-payloads-v0.md)) a **lifecycle anchor** ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)).

---

## 9. Honesty boundary (explicit non-claims)

This layer **does not**:

- ship a scheduler, queue, or workflow daemon;
- guarantee any automated state transition;
- expose hidden orchestration that operates behind the user's back;
- imply that planned factory agents ([agent-map.md](agent-map.md)) maintain runtime state machines;
- imply that Cursor enforces these lifecycle rules beyond what the user/operator does;
- imply that future Control Plane code already exists in this repository.

This layer **does**:

- define **lifecycle vocabulary** for stages, artifacts, approvals, QA, revisions, regenerations, invalidations, signals, and delivery;
- define **allowed and forbidden transitions** as **prose discipline**;
- align with **SAFE UNKNOWN** per [safe-unknown-boundary.md](safe-unknown-boundary.md) and `AGENTS.md`;
- align with **HITL** per [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md);
- align with **system signals** per [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md).

> **Semantics ≠ implementation.** No scheduler exists. No orchestration daemon exists. No queue engine exists. Lifecycle correctness is **a human responsibility** in Phase 1.

---

## 10. Scope of this overview

| In scope | Out of scope |
|----------|--------------|
| Stage state vocabulary and allowed transitions | A runtime state machine implementation |
| Artifact lifecycle (mutable / frozen / superseded / invalidated) | Wire formats for artifacts |
| Approval semantics (scope, expiration, revocation) | Cryptographic signing or notification systems |
| Revision and regeneration discipline | Automated artifact rewriting |
| Dependency-aware invalidation rules | A dependency graph engine |
| Orchestration signal lifecycle (factory-side) | Runtime signal routing |
| QA gating lifecycle | An automated QA runner |
| Delivery lifecycle (candidate → release → rollback) | Deployment automation |
| HITL anchoring of all gated transitions | Approval signing infrastructure |

---

## 11. Document set

| Document | Role |
|----------|------|
| [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md) | **This file** — purpose, philosophy, non-claims. |
| [stage-state-model-v0.md](stage-state-model-v0.md) | Conceptual stage states, transitions, ownership, freeze/reopen/invalidation. |
| [artifact-state-model-v0.md](artifact-state-model-v0.md) | Artifact lifecycle, mutable/immutable regions, lineage, approval inheritance. |
| [approval-semantics-v0.md](approval-semantics-v0.md) | Approval meaning, scope, partial / conditional / expiration / revocation. |
| [revision-semantics-v0.md](revision-semantics-v0.md) | Revision triggers, scope, lineage, freeze breaking, QA reset. |
| [regeneration-semantics-v0.md](regeneration-semantics-v0.md) | Partial vs full regeneration, safe vs unsafe, boundaries, QA invalidation. |
| [dependency-invalidation-v0.md](dependency-invalidation-v0.md) | Upstream/downstream propagation across blueprint / design / SEO / frontend. |
| [orchestration-signals-v0.md](orchestration-signals-v0.md) | Signal source, propagation, escalation, resolution; tie to signals dictionary. |
| [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) | Gate lifecycle, blocker, pass / fail / conditional, waiver, freeze, HITL override. |
| [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) | Delivery candidate, validation, release, freeze, rollback, archive. |

---

## 12. Operating principles (one-line summary)

1. **Semantics ≠ implementation.**
2. **Every stage has a state. Every artifact has a state.**
3. **Approvals are scoped, finite, and HITL-anchored.**
4. **Revisions and regenerations are bounded and dependency-aware.**
5. **Invalidation propagates honestly — no silent staleness.**
6. **A QA verdict has a lifecycle, not just a value.**
7. **Delivery is a state, not a deployment.**
8. **No transition without a prompt + report pair.**
9. **No autonomous freeze, approval, or release.**
10. **Documentation-first stays documentation-first until evidence says otherwise.**

---

## 13. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial execution-semantics overview (documentation only). |
