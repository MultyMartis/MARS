# MARS Website Factory — Orchestration Signals v0

**Status:** **documentation only** — defines how **named signals** flow through factory workflow narrative, prompts, QA, HITL, and reports. **Not** a signal router, **not** an event bus, **not** an emission engine, **not** a queue.

**Version:** v0.

**Related:** [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [stage-state-model-v0.md](stage-state-model-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [workflow-map.md](workflow-map.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md), [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md), [reporting-standard-v0.md](reporting-standard-v0.md), [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md), [`../../workflows/task-contract-v0.md`](../../workflows/task-contract-v0.md), [`../../workflows/execution-flow.md`](../../workflows/execution-flow.md), [safe-unknown-boundary.md](safe-unknown-boundary.md).

---

## 1. Purpose

The factory uses **named signals** to express state-bearing conditions: "we cannot proceed without a binding", "we need a human decision", "the contract shape must change", "we suspect a policy violation". The MARS-wide canonical vocabulary lives in [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md).

This document defines, for the Website Factory:

- the **factory-specific** signals (extensions / specializations) on top of the MARS canonical set;
- the **source** of each signal (which prompts / stages / lanes may emit it);
- the **propagation** path through workflow / artifact / approval / QA / delivery layers;
- the **escalation** rules (when a signal forces a hard stop, a HITL gate, or a STRUCTURE CHANGE);
- the **resolution** path (how a signal closes);
- the **lifecycle** of a signal over time;
- the **relationship** to workflow stages, prompt sections, REPORT sections.

It does **not** ship a signal router. Signals are **prose discipline** in v0.

---

## 2. Canonical (MARS-wide) signals

Per [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md), the canonical signal set is:

| Signal | Canonical meaning (MARS) | Factory use (short summary) |
|--------|---------------------------|------------------------------|
| **UNKNOWN** | Required binding missing; cannot proceed. | Stage / artifact / approval has a missing prerequisite (no approver, no registry row, no upstream artifact). |
| **SAFE UNKNOWN** | Bounded uncertainty; proceed only with explicit limits and named approver. | Stage continues with bounded assumption recorded ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [safe-unknown-boundary.md](safe-unknown-boundary.md)). |
| **NEED HUMAN APPROVAL** | Human decision required before continuation. | HITL gate ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)) anchors transition. |
| **SECURITY RISK** | Policy violation / injection / scope escape suspected. | Stop line; HITL + security review required. |
| **STRUCTURE CHANGE** | Task / plan / artifact shape must change; not a small fix. | Revision class **structural** ([revision-semantics-v0.md](revision-semantics-v0.md)); often supersede. |
| **CONTEXT MIGRATION NEEDED** | Memory / RAG / knowledge pack lag. | Rarely emitted by factory prompts directly; may appear when factory references upstream knowledge artifacts that have shifted. |
| **GIT CHECKPOINT NEEDED** / **NO GIT CHECKPOINT** | Governance milestone hint. | Per `AGENTS.md`; factory work defaults to **NO GIT CHECKPOINT** unless a milestone is met. |

These are the **authoritative** spellings. Aliases (e.g. `STRUCTURE_CHANGE`) are **non-canonical** per [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md) §3.

---

## 3. Factory-layer signal extensions

The factory uses additional **stage- and lifecycle-specific** signals on top of the canonical set. These are **factory-scoped** narrative tokens; they do **not** introduce new MARS-wide signals. When used inside a factory REPORT or prompt, they pair with a canonical signal where appropriate.

| Factory signal | Meaning | Pairs with canonical signal |
|----------------|---------|-----------------------------|
| **BLOCKED** | A stage instance cannot proceed because an upstream artifact, approval, or HITL prerequisite is missing or invalid. | Often pairs with **UNKNOWN** (binding missing) or **NEED HUMAN APPROVAL** (HITL pending). |
| **INVALIDATED** | An upstream change has rendered a downstream artifact / approval / QA verdict stale ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)). | Often pairs with **STRUCTURE CHANGE** if upstream change is structural. |
| **QA FAILURE** | A QA gate emits `fail` ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)) without an applicable waiver path. | Often pairs with **NEED HUMAN APPROVAL** if waiver is requested. |
| **DELIVERY BLOCKED** | Delivery candidate cannot be released because prerequisites are missing or unresolved ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md)). | Pairs with **UNKNOWN** / **SECURITY RISK** / **NEED HUMAN APPROVAL** as applicable. |
| **REVISION REQUIRED** | A revision request is in scope for the affected artifact ([revision-semantics-v0.md](revision-semantics-v0.md)). | Pairs with **NEED HUMAN APPROVAL** at the HITL gate; with **STRUCTURE CHANGE** when structural. |

These factory tokens are **narrative aids**; they **must** be readable alongside canonical signals and **must not** be introduced as standalone MARS-wide signals. Their authoritative shape stays here.

---

## 4. Signal source

| Signal | Typical source(s) |
|--------|--------------------|
| **UNKNOWN** | Production prompt that cannot resolve a binding; QA prompt that cannot find evidence; HITL prompt without a named approver. |
| **SAFE UNKNOWN** | Production prompt under bounded continuation; QA prompt without complete evidence; intake / strategy prompts with hypothesis-bearing assumptions. |
| **NEED HUMAN APPROVAL** | Any prompt approaching a HITL gate ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)); QA waiver request; revision opening; delivery release. |
| **SECURITY RISK** | QA prompt finding a policy / compliance issue; Frontend QA finding secrets / dangerous patterns; legal review escalation. |
| **STRUCTURE CHANGE** | Production prompt discovering a contract mismatch; QA prompt finding contract gap ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §5); registry / contract amendment request. |
| **BLOCKED** | Stage prompt awaiting upstream stabilization. |
| **INVALIDATED** | Revision / regeneration REPORT acknowledging downstream impact. |
| **QA FAILURE** | QA prompt emitting `fail` with no waiver path. |
| **DELIVERY BLOCKED** | Delivery prompt / Final Validation REPORT noting missing prerequisites. |
| **REVISION REQUIRED** | QA prompt / HITL prompt requesting revision. |

A signal is **never** emitted **silently**. It appears in the prompt body, the REPORT body, or both ([reporting-standard-v0.md](reporting-standard-v0.md) §3).

---

## 5. Signal propagation

Signals **propagate** through factory layers:

```text
prompt ──► REPORT ──► next stage prompt ──► REPORT ──► HITL gate ──► Approval artifact
                                  │
                                  ▼
                          QA prompt / REPORT
                                  │
                                  ▼
                      Validator REPORT (when routed)
                                  │
                                  ▼
                      Final Validation REPORT
                                  │
                                  ▼
                       Delivery REPORT / Approval artifact
```

Propagation rules:

| Rule | Detail |
|------|--------|
| **Forward only** | Signals propagate **forward** through workflow stages; a downstream stage may emit its own signals but does not retroactively rewrite upstream signals. |
| **Acknowledge in REPORTs** | A downstream stage that consumes an upstream artifact bearing an open signal **must** acknowledge the signal in its REPORT. |
| **Stack signals** | A single artifact / stage may carry **multiple** signals simultaneously (e.g. **SAFE UNKNOWN** + **NEED HUMAN APPROVAL**). Enumerate all. |
| **No silent collapse** | A downstream stage **may not** collapse multiple upstream signals into a single signal. |
| **No silent drop** | A downstream stage **may not** drop an upstream signal without recording its resolution. |

---

## 6. Signal escalation

Some signals **must escalate** when conditions worsen:

| From | To | Trigger |
|------|----|---------|
| **SAFE UNKNOWN** | **UNKNOWN** | Bounding assumption proven false ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)). |
| **SAFE UNKNOWN** | **NEED HUMAN APPROVAL** | Bounded continuation requires a HITL decision. |
| **UNKNOWN** | **STRUCTURE CHANGE** | Missing binding cannot be resolved without re-decomposing the work. |
| **NEED HUMAN APPROVAL** | **SECURITY RISK** | Approval request reveals a policy violation. |
| **QA FAILURE** | **STRUCTURE CHANGE** | Failure exposes a contract gap. |
| **REVISION REQUIRED** | **STRUCTURE CHANGE** | Revision scope is structural rather than bounded. |
| **BLOCKED** | **UNKNOWN** | Block reason resolves to a missing binding (not just a pending upstream). |
| **INVALIDATED** | **STRUCTURE CHANGE** | Invalidation pattern is structural / cross-cutting. |
| **DELIVERY BLOCKED** | **SECURITY RISK** | Delivery prerequisite is a policy concern. |

Forbidden:

- **de-escalating** a signal silently (e.g. **STRUCTURE CHANGE** → **SAFE UNKNOWN** without HITL);
- emitting **NEED HUMAN APPROVAL** to bypass a stricter signal (e.g. **SECURITY RISK**);
- using **SAFE UNKNOWN** as a way to skip an avoidable check ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)).

---

## 7. Signal resolution

Each signal has a **resolution path**:

| Signal | Resolution path |
|--------|------------------|
| **UNKNOWN** | Resolve the missing binding (named approver, registry row, upstream artifact) and record in REPORT; signal closes when binding exists. |
| **SAFE UNKNOWN** | Either gather evidence and close, or escalate to **NEED HUMAN APPROVAL** for bounded continuation, or escalate to **UNKNOWN** if assumption fails. |
| **NEED HUMAN APPROVAL** | HITL decision recorded as Approval artifact; signal closes with the decision. |
| **SECURITY RISK** | Block stage; security review per [`../../security/approval-gates.md`](../../security/approval-gates.md) and risk-register ([`../../governance/risk-register.md`](../../governance/risk-register.md)); signal closes after explicit clearance. |
| **STRUCTURE CHANGE** | New artifact_id (or major version bump), upstream stage re-plan, registry / contract amendment under governance; signal closes after the new structure is approved. |
| **BLOCKED** | Upstream stabilizes; downstream moves to `ready`. |
| **INVALIDATED** | Revise or regenerate per scope ([revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md)); re-QA + re-gate; signal closes after new revision is approved. |
| **QA FAILURE** | Revise or waive (HITL); signal closes after re-QA passes or waiver is recorded. |
| **DELIVERY BLOCKED** | Resolve prerequisites; re-run Final Validation; HITL release approval. |
| **REVISION REQUIRED** | Revision opened, executed, re-gated; signal closes after approval. |

Resolution is **recorded** in the closing REPORT; resolution **without** a recorded path is incomplete.

---

## 8. Signal lifecycle

A signal has its own state progression within the affected artifact / stage's lifetime:

```text
open ─► acknowledged ─► (escalated?) ─► resolved / waived
```

| State | Meaning |
|-------|---------|
| **open** | Signal emitted but not yet acknowledged downstream or by HITL. |
| **acknowledged** | Downstream stage / HITL has recorded the signal in their REPORT. |
| **escalated** | Signal has been upgraded (per [§6](#6-signal-escalation)). |
| **resolved** | Signal closed per [§7](#7-signal-resolution). |
| **waived** | HITL has accepted the signal under bounded continuation with named approver and risk note. |

Signals **do not** expire silently. An `open` signal that has been unacknowledged for a long time still blocks downstream consumption per the relevant lifecycle rules.

---

## 9. Tie to workflow stages

[website-factory-workflow-v0.md](website-factory-workflow-v0.md) §S01–S15 names typical signals per stage. The execution-semantics layer adds the **lifecycle behavior** of those signals:

| Stage | Typical emissions (per workflow v0) | Lifecycle hook (this doc) |
|-------|--------------------------------------|-----------------------------|
| S01 Intake | **UNKNOWN** (compliance, market), **SAFE UNKNOWN** (assumptions) | Resolution at G1; SAFE UNKNOWN bounded by HITL. |
| S02 Site Type | **SAFE UNKNOWN** / **STRUCTURE CHANGE** (no registry fit) | STRUCTURE CHANGE may trigger registry amendment. |
| S03 Strategy | **NEED HUMAN APPROVAL** / **STRUCTURE CHANGE** (SEO vs commercial conflict) | Resolution at G2. |
| S04 IA | **STRUCTURE CHANGE** (impossible CTA flow); **SAFE UNKNOWN** (stack/CMS) | Resolution at G3; SAFE UNKNOWN documented. |
| S05 Blueprint | **STRUCTURE CHANGE** (registry mismatch) | Resolution at G3 batch. |
| S06 Blueprint QA | **NEED HUMAN APPROVAL** (waivers); **SAFE UNKNOWN** (ambiguous checklist) | Closed at QA verdict + HITL. |
| S07 Design Handoff | **SAFE UNKNOWN** (tooling) | Closed at design lead sign-off. |
| S08 Design Production | **STRUCTURE CHANGE** (template drift); **SECURITY RISK** (asset / compliance breach) | Closed at G4 / G5. |
| S09 Design QA | **NEED HUMAN APPROVAL** (freeze ambiguity) | Closed at G5. |
| S10 Frontend Handoff | **UNKNOWN** / **STRUCTURE CHANGE** (unsupported requirement) | Closed at tech lead approval. |
| S11 Frontend Production | **SAFE UNKNOWN** (CI / stack) | Closed at G6. |
| S12 Frontend QA | **NEED HUMAN APPROVAL** (blocker waivers); **SECURITY RISK** | Closed at HITL waiver / re-pass. |
| S13 Final Validation | **STRUCTURE CHANGE** (late registry mismatch) | Closed at G7 prep. |
| S14 Human Approval | **UNKNOWN** (missing approver) | Closed at G7 decision. |
| S15 Delivery | **SAFE UNKNOWN** (hosting); **DELIVERY BLOCKED** | Closed at release authorization or held. |

These mappings are **illustrative**; specific projects may emit different combinations.

---

## 10. Signals in prompts

Per [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) §3 and [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md):

A well-formed prompt:

- declares which signals its **upstream artifacts** carry (and how to interpret them);
- declares which signals it may **emit** during execution and under what conditions;
- declares the **escalation rules** ([§6](#6-signal-escalation));
- declares the **resolution paths** ([§7](#7-signal-resolution)).

A prompt that omits signal expectations is **not** a factory prompt — it cannot bind correctly to lifecycle behavior.

---

## 11. Signals in REPORTs

Per [reporting-standard-v0.md](reporting-standard-v0.md) §3 "HITL flags" and the general REPORT structure:

A well-formed REPORT:

- enumerates **emitted signals** with their lifecycle state ([§8](#8-signal-lifecycle));
- enumerates **inherited signals** (from upstream artifacts) and how this stage acknowledged / resolved them;
- enumerates **escalations** taken during the stage;
- enumerates **resolutions** recorded;
- enumerates **open signals** at stage exit (handed off to downstream).

A REPORT that omits signal narrative is **incomplete**.

---

## 12. Signals in HITL prompts and Approval artifacts

Per [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) §5 + §6:

A HITL prompt:

- carries the **signal set** the agent emitted that triggered the HITL request;
- carries the **proposed resolution path**;
- carries the **escalation triggers** that would force escalation if HITL refuses to grant approval.

An Approval artifact ([artifact-types-v0.md](artifact-types-v0.md) §Approval artifact):

- records which signals the HITL decision **closed**;
- records which signals the HITL decision **deferred** (and to whom);
- records which signals the HITL decision **escalated**.

---

## 13. Non-claims

- This document does **not** ship a signal router, event bus, or queue.
- It does **not** assume signals are emitted, transmitted, or stored by code.
- It does **not** override [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md) for canonical signal names.
- It does **not** introduce new MARS-wide signals; factory-layer tokens in [§3](#3-factory-layer-signal-extensions) remain factory-scoped narrative.
- It does **not** replace HITL judgment with predictable signal handling.

What it **does** do is define **how signals behave over time** within the factory: their source, propagation, escalation, resolution, lifecycle, and relationship to prompts, REPORTs, and HITL decisions.

---

## 14. Anti-patterns

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| "Signal handled by the agent." | No signal router. | HITL handles gated signals; REPORT acknowledges all signals. |
| "STRUCTURE_CHANGE applied silently." | Non-canonical alias + silent escalation. | **STRUCTURE CHANGE** + HITL pass. |
| "SAFE UNKNOWN used to skip an avoidable check." | Bypasses discipline. | Gather evidence or escalate per [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md). |
| "Multiple signals collapsed into one." | Severity / category hidden. | Enumerate all. |
| "Upstream signal dropped on downstream." | Silent loss. | Acknowledge in REPORT; resolve or carry forward. |
| "SECURITY RISK downgraded to SAFE UNKNOWN." | Severity tuning. | Maintain severity; resolve per security policy. |
| "NEED HUMAN APPROVAL emitted to bypass STRUCTURE CHANGE." | Severity tuning. | Recognize structural shape change; emit STRUCTURE CHANGE first. |

---

## 15. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial orchestration signal semantics (documentation only). |
