# MARS Website Factory — Stage State Model v0

**Status:** **documentation only** — conceptual **state vocabulary** for workflow stage instances in the Website Factory. **Not** a runtime state machine, **not** a persisted state-store implementation, **not** a scheduler.

**Version:** v0.

**Related:** [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [workflow-map.md](workflow-map.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [`../../governance/state-model.md`](../../governance/state-model.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md), [`../../mars-runtime/run-lifecycle-v0.md`](../../mars-runtime/run-lifecycle-v0.md).

---

## 1. Purpose

[website-factory-workflow-v0.md](website-factory-workflow-v0.md) names stages **S01–S15**. This document gives each **stage instance** (a stage running for a defined project scope — a site, a batch, a single page) a **named state** and a **bounded set of allowed transitions** so that:

- humans (and any future runtime) can answer "what state is this stage in?" without paraphrase;
- prompts ([prompt-structure-standard-v0.md](prompt-structure-standard-v0.md)) can declare which state they intend to enter or exit;
- reports ([reporting-standard-v0.md](reporting-standard-v0.md)) can record which transition actually occurred;
- HITL gates ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)) have a stable anchor;
- dependency invalidation ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)) has a stable target.

This document **does not** introduce new stages, change stage ids, or define a runtime state machine.

---

## 2. State vocabulary

The factory recognizes the following **stage states** for a stage instance. **Spellings are canonical**; do not invent variants.

| State | Meaning |
|-------|---------|
| **not_started** | Stage instance has been **named** for a project scope but no work has begun. Upstream dependencies may or may not be satisfied. |
| **ready** | All upstream dependencies are satisfied (approved or in an explicitly allowed mutable state); the stage **may** begin execution. |
| **blocked** | An upstream artifact, registry row, contract gap, signal, or HITL prerequisite prevents the stage from starting or continuing. |
| **executing** | The stage is **actively producing or revising** its artifacts. Today this means a human is running prompts in Cursor per [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md). |
| **waiting_hitl** | The stage has produced or revised artifacts but **cannot exit** without a HITL decision ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)). |
| **qa_review** | The stage's output is under **QA assessment** in a defined lane ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)). |
| **approved** | The stage's output has **passed** its QA gate(s) **and** the appropriate HITL gate has granted approval ([approval-semantics-v0.md](approval-semantics-v0.md)). Downstream stages may now consume frozen artifacts produced here. |
| **rejected** | The stage's output has **failed** QA or HITL review; the stage instance must **revise** ([revision-semantics-v0.md](revision-semantics-v0.md)) or be **rolled back** ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) §rollback). |
| **frozen** | The stage's approved output is **immutable** for the active execution scope. Frozen state is **not** terminal — it can be **reopened** via revision under HITL. |
| **invalidated** | An upstream change ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)) has rendered this stage's output **stale** for the affected scope; the stage must be **rerun** in whole or in part. |
| **archived** | The stage instance is **closed** for this execution scope (project completed, delivery finalized, or scope abandoned). |

**Out of scope for v0:** any internal sub-state (e.g. "executing.draft", "qa_review.pending_evidence"). Projects may use prose annotations in reports but must not introduce new state tokens.

---

## 3. State transition rules

### 3.1 Allowed transitions

The arrows below describe the **only** transitions a stage instance may take. All other transitions are **forbidden** (§3.2).

```text
not_started ─► ready ─► executing ─► qa_review ─► approved ─► frozen
     │           │           │            │            │            │
     │           ▼           ▼            ▼            │            ▼
     │       blocked     waiting_hitl   rejected       │       invalidated
     │           │           │            │            │            │
     ▼           ▼           ▼            ▼            ▼            ▼
                          (resolve / revise / re-gate)             archived
```

| From → To | Trigger |
|-----------|---------|
| `not_started → ready` | Upstream dependencies satisfied (approved or allowed-mutable). |
| `not_started → blocked` | Upstream artifact missing, registry mismatch, or pending HITL prerequisite. |
| `ready → executing` | A production prompt ([prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) §3.2) begins. |
| `ready → blocked` | A previously satisfied dependency degrades before execution starts (e.g. upstream revision). |
| `executing → qa_review` | Production prompt closes with **artifacts out**; a QA prompt ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md)) starts. |
| `executing → blocked` | Mid-stage discovery of a missing binding → emit `UNKNOWN` ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)). |
| `executing → waiting_hitl` | Stage produces an output that **freezes scope** and requires HITL before QA can begin (e.g. design freeze proposal). |
| `qa_review → waiting_hitl` | QA emits `pass` / `conditional` / `fail`; HITL must rule on approval or waiver. |
| `qa_review → rejected` | QA emits `fail` with no waiver path. |
| `waiting_hitl → approved` | HITL approves per [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) §5 (decision + Approval artifact). |
| `waiting_hitl → rejected` | HITL rejects. |
| `waiting_hitl → executing` | HITL requests revision; stage re-enters execution under bounded scope ([revision-semantics-v0.md](revision-semantics-v0.md)). |
| `approved → frozen` | Approval at the stage's freeze gate (e.g. G3 blueprint batch, G5 design freeze, G6 frontend release tag intent) closes the scope. |
| `approved → invalidated` | An upstream stage entered `invalidated` / `rejected` and downstream impact applies ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)). |
| `frozen → invalidated` | Upstream revision invalidates the frozen baseline for the affected scope. |
| `frozen → executing` | HITL **reopens** the stage for a bounded revision ([revision-semantics-v0.md](revision-semantics-v0.md)) — new revision id recorded. |
| `rejected → executing` | Revision begins with a bounded CR list. |
| `invalidated → blocked` | Stage cannot resume until upstream stabilizes. |
| `invalidated → ready` | Upstream stabilized; stage may rerun in whole or in part ([regeneration-semantics-v0.md](regeneration-semantics-v0.md)). |
| any non-archived → `archived` | Execution scope closed (delivery finalized or scope abandoned with HITL). |

### 3.2 Forbidden transitions

| From → To | Why forbidden |
|-----------|---------------|
| `not_started → executing` | Skips dependency check. |
| `not_started → approved` | Fabrication. |
| `executing → approved` | Skips QA + HITL. |
| `qa_review → approved` | QA does not grant approval; HITL does ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §4). |
| `qa_review → frozen` | Freeze requires approval. |
| `approved → executing` (silent) | Reopen requires HITL-recorded revision. |
| `rejected → approved` (silent) | Severity / verdict tuning forbidden ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §5). |
| `frozen → executing` (silent) | Freeze breaking requires HITL reopen. |
| `invalidated → approved` (silent) | Stage must be rerun and re-gated. |
| `archived → anything` | Archival is closure; a new run requires a new stage instance. |

Any forbidden transition observed in practice → emit **STRUCTURE CHANGE** or **NEED HUMAN APPROVAL** per [orchestration-signals-v0.md](orchestration-signals-v0.md).

---

## 4. QA implications per state

| Stage state | QA behavior |
|-------------|-------------|
| `not_started` / `ready` / `blocked` | No QA. |
| `executing` | QA may be **scoped** (lane-specific spot checks) but not **gating**. |
| `waiting_hitl` (pre-QA) | No QA verdict yet. |
| `qa_review` | QA prompts run per [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md); findings attach to artifact id + revision ([artifact-state-model-v0.md](artifact-state-model-v0.md)). |
| `approved` | QA verdict for the active revision is **filed**; new revisions reset QA per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md) §gate reset. |
| `frozen` | Filed QA verdict remains **valid** for the frozen revision; revision triggers re-QA. |
| `rejected` | QA findings inform CR list; QA does not auto-resolve. |
| `invalidated` | All prior QA verdicts for the affected scope are **stale**; re-QA required after rerun. |
| `archived` | QA history preserved as audit; no new QA. |

QA never **promotes** a stage to `approved`; HITL does.

---

## 5. HITL implications per state

| Stage state | HITL behavior |
|-------------|---------------|
| `not_started` | HITL may approve scope (G1 intake) before `ready`. |
| `ready` / `executing` | Mid-stage HITL only on explicit `NEED HUMAN APPROVAL` ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)). |
| `waiting_hitl` | HITL is the **only** way out (approve / reject / request revision / park). |
| `qa_review` | HITL is informed by QA verdict; HITL still owns the gate. |
| `approved` | Approval artifact ([artifact-types-v0.md](artifact-types-v0.md) §Approval artifact) is recorded. |
| `frozen` | Reopening freeze is **HITL-only** ([approval-semantics-v0.md](approval-semantics-v0.md) §revocation, [revision-semantics-v0.md](revision-semantics-v0.md)). |
| `rejected` | HITL records rejection and may approve revision scope. |
| `invalidated` | HITL may approve **partial rerun** scope per [regeneration-semantics-v0.md](regeneration-semantics-v0.md). |
| `archived` | HITL records closure / archival. |

No state transition that bears HITL semantics may occur without a HITL-issued decision; agent-side simulation is fabrication.

---

## 6. Downstream effects per state

The state of a stage instance directly affects **downstream stage states** ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)).

| Upstream state | Downstream stages |
|----------------|--------------------|
| `not_started` / `ready` / `executing` | Downstream **must not** start (unless an explicitly allowed mutable read is documented). |
| `qa_review` | Downstream **must not** rely on un-verdicted output. |
| `waiting_hitl` | Downstream remains **blocked** until approval. |
| `approved` | Downstream may move from `blocked` / `not_started` → `ready`. |
| `frozen` | Downstream may treat the frozen baseline as **immutable** ([artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) §5). |
| `rejected` | Downstream that already consumed an earlier draft must mark its own state `invalidated` if intersecting the change. |
| `invalidated` | Downstream that depends on the affected scope must move to `invalidated` per [dependency-invalidation-v0.md](dependency-invalidation-v0.md). |
| `archived` | Downstream cannot re-run against an archived upstream without HITL reopening. |

---

## 7. Stage ownership

Each stage instance has **one** **primary owner role** per [website-factory-workflow-v0.md](website-factory-workflow-v0.md) §S01–S15 (e.g. Page Blueprint Agent — planned — for S05, with PM + tech lead at G3). Ownership rules:

- **Production prompts** for the stage are issued by or on behalf of the owner role.
- **QA prompts** are **not** owned by the production role; QA is a separate lane ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §10).
- **HITL** is owned by the approver role(s) at the relevant gate; the production owner cannot self-approve.
- **Ownership does not equal automation:** "owned by Page Blueprint Agent (planned)" means **planned**; human authoring of the same artifact is equally valid ([agent-map.md](agent-map.md)).

An ownership change mid-execution requires a HITL-recorded handoff (e.g. PM transfers stage ownership). The previous owner's report ([reporting-standard-v0.md](reporting-standard-v0.md)) remains in the audit trail.

---

## 8. Stage freeze

A stage instance **freezes** when its output reaches an approval that anchors a downstream scope:

| Stage | Freeze anchor |
|-------|----------------|
| S01 Intake | G1 approval of `scope_in` / `scope_out`. |
| S03 Strategy | G2 approval of strategy / SEO narrative. |
| S04 IA | G3 partial: approved sitemap / templates. |
| S05 Blueprint | G3 approval of blueprint batch (per scope). |
| S08 Design Production | G5 design freeze. |
| S10 Frontend Handoff | Tech lead approval before S11. |
| S11 Frontend Production | G6 release-tag intent. |
| S14 Human Approval | Final release authorization (G7). |
| S15 Delivery | Release package frozen as delivered ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md)). |

When a stage is `frozen`:

- its artifact baseline is **immutable** for the active scope ([artifact-state-model-v0.md](artifact-state-model-v0.md));
- downstream stages may consume the baseline directly;
- new revisions require **reopening** ([§9](#9-stage-reopening)).

Freeze is **never automatic**; freeze follows the approval artifact ([approval-semantics-v0.md](approval-semantics-v0.md) §approval freeze).

---

## 9. Stage reopening

A frozen stage may be **reopened** only when:

1. a **revision request** is recorded ([revision-semantics-v0.md](revision-semantics-v0.md));
2. a **named HITL approver** authorizes the reopen ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md));
3. the **scope** of the revision is bounded (which artifacts / pages / fields are in scope);
4. downstream invalidation impact is **acknowledged** ([dependency-invalidation-v0.md](dependency-invalidation-v0.md));
5. the revision is recorded with a **new revision id** on the affected artifact(s) ([artifact-types-v0.md](artifact-types-v0.md) §`artifact_id` philosophy).

Forbidden:

- silent reopen ("we'll just tweak the design");
- expanding revision scope mid-flight without HITL re-approval;
- treating a partial reopen as a full rerun;
- treating a full rerun as a partial reopen.

---

## 10. Stage invalidation

A stage may be moved to `invalidated` when:

- an upstream stage's frozen baseline changes ([dependency-invalidation-v0.md](dependency-invalidation-v0.md));
- a registry row that the stage depended on is amended under governance;
- a contract gap exposed by downstream QA forces a `STRUCTURE CHANGE` upstream ([orchestration-signals-v0.md](orchestration-signals-v0.md));
- a security-sensitive issue requires re-running with a different scope (`SECURITY RISK`).

Invalidation **must be acknowledged** in the responsible REPORT ([reporting-standard-v0.md](reporting-standard-v0.md)) with:

- which stage instances are invalidated,
- which artifacts and revisions are affected,
- which downstream stages move to `blocked` / `invalidated`,
- the HITL approval required for partial rerun ([regeneration-semantics-v0.md](regeneration-semantics-v0.md)).

Invalidation is **not** silent staleness. An artifact that **could** be stale but has not been invalidated still represents the last-approved truth until an explicit transition occurs.

---

## 11. Tie to MARS run lifecycle

The factory stage state model is **scoped** to Website Factory stage instances. It **does not** replace the MARS-wide run lifecycle in [`../../mars-runtime/run-lifecycle-v0.md`](../../mars-runtime/run-lifecycle-v0.md). When a future runtime exists:

- factory stage instances may map onto **runtime run records** with their own lifecycle;
- factory state names may map onto the runtime's enumerated run states;
- HITL gates map onto run pauses / approvals;
- archival maps onto run closure.

**Until then**, the factory state model is **prose discipline**; the runtime mapping is **conceptual alignment**.

---

## 12. Tie to MARS state model

The MARS-wide [`../../governance/state-model.md`](../../governance/state-model.md) defines **entity** state vocabulary. Factory stage states are **operational**, not governance entity lifecycle; do not conflate them. A factory stage instance that is `approved` is **not** the same as a governance entity that is `production`.

---

## 13. Anti-patterns

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| "Stage approved by the agent." | No agent owns approval. | HITL approval at the named gate. |
| "Auto-frozen after QA pass." | Freeze requires approval. | Approval artifact + recorded freeze. |
| "Reopened a frozen stage with a small tweak." | Silent freeze breaking. | Revision request + new revision id + HITL. |
| "QA pass implies approval." | Categories collapsed. | QA recommendation + HITL approval. |
| "Stage marked done." | "Done" is not a state. | Use `approved`, `frozen`, or `archived`. |
| "Partial rerun without HITL." | Scope drift risk. | Bounded scope + HITL-approved revision. |
| "Skipped invalidation because downstream looked fine." | Silent staleness. | Explicit invalidation REPORT entry. |

---

## 14. Non-claims

- This document does **not** ship a state machine.
- It does **not** define a persistence layer.
- It does **not** assert any automated transition.
- It does **not** replace HITL judgment with predictable agent behavior.

What it **does** do is define **a stable vocabulary** for stage states and **bounded transitions** so prompts, reports, and HITL decisions speak the same language.

---

## 15. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial stage state model (documentation only). |
