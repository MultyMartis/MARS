# MARS Website Factory — QA Gating Semantics v0

**Status:** **documentation only** — defines the **lifecycle behavior** of QA gates: open, verdict, freeze, waiver, expiration, HITL override. **Not** an automated QA runner, **not** an enforcement engine, **not** a test orchestrator.

**Version:** v0.

**Related:** [execution-semantics-overview-v0.md](execution-semantics-overview-v0.md), [stage-state-model-v0.md](stage-state-model-v0.md), [artifact-state-model-v0.md](artifact-state-model-v0.md), [approval-semantics-v0.md](approval-semantics-v0.md), [revision-semantics-v0.md](revision-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [orchestration-signals-v0.md](orchestration-signals-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md), [qa-validation-model.md](qa-validation-model.md), [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [agent-map.md](agent-map.md), [`../../security/approval-gates.md`](../../security/approval-gates.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md).

---

## 1. Purpose

[qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) defines how QA prompts are **shaped** and what counts as **evidence**. [qa-result-payloads-v0.md](qa-result-payloads-v0.md) defines QA **field vocabulary**.

This document defines, for QA gates, **lifecycle behavior over time**:

- when a QA gate **opens**;
- what **verdicts** a gate may produce;
- how **conditional pass** behaves;
- how **waivers** behave;
- how **confidence** interacts with severity ([§7](#7-confidence-handling));
- what **evidence** must be attached at gate close;
- when QA **freezes** with the artifact and when QA **invalidates**;
- how QA **blocks** downstream consumption and **delivery**;
- when HITL **overrides** a QA recommendation.

It does **not** ship a QA runner. QA gates are **prose discipline** anchored to HITL approvals.

---

## 2. QA gate lifecycle

A QA gate is a **named checkpoint** on a workflow stage at which QA assesses an artifact revision. Stages with explicit QA gates per [website-factory-workflow-v0.md](website-factory-workflow-v0.md):

| Stage | QA gate(s) |
|-------|------------|
| S06 Blueprint QA | Page Blueprint QA Checklist v0 ([page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md)). |
| S09 Design QA | Design QA lane ([qa-validation-model.md](qa-validation-model.md)). |
| S12 Frontend QA | Frontend QA lane. |
| S13 Final Validation | Cross-lane validation; SEO QA, Conversion QA, Frontend QA, Validator overlap. |

Additional QA may occur **within** other stages (e.g. Blueprint QA per page during S05) but does not replace S06 / S09 / S12 / S13 as gating stages.

### 2.1 Gate states

| State | Meaning |
|-------|---------|
| **open** | The QA gate has been triggered for a specific artifact revision; QA prompt(s) are running. |
| **assessing** | QA findings are being collected; verdict not yet filed. |
| **verdict_filed** | QA verdict is recorded (`pass` / `pass_conditional` / `fail`) with evidence; HITL decision pending. |
| **closed_pass** | HITL approves; gate closes for this revision. |
| **closed_conditional** | HITL approves with the QA-listed CRs ([approval-semantics-v0.md](approval-semantics-v0.md) §5). |
| **closed_waived** | HITL waives one or more findings under named approver. |
| **closed_fail** | HITL rejects; revision required. |
| **stale** | An upstream change has invalidated the gate's verdict ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)); gate must re-open on the new revision. |

A gate **does not** close itself; HITL closes it ([§13](#13-hitl-override-and-authority)).

### 2.2 Gate transitions

```text
open ─► assessing ─► verdict_filed ─► closed_pass / closed_conditional / closed_waived / closed_fail
                                              │
                                              ▼
                                          (upstream change?) ─► stale ─► open (new revision)
```

| From → To | Trigger |
|-----------|---------|
| `(none) → open` | Stage moves to `qa_review` ([stage-state-model-v0.md](stage-state-model-v0.md) §3) for an artifact revision. |
| `open → assessing` | QA prompt begins. |
| `assessing → verdict_filed` | QA findings + verdict are recorded per [qa-result-payloads-v0.md](qa-result-payloads-v0.md). |
| `verdict_filed → closed_pass` | HITL approval. |
| `verdict_filed → closed_conditional` | HITL approval with bounded CRs ([approval-semantics-v0.md](approval-semantics-v0.md) §5). |
| `verdict_filed → closed_waived` | HITL waiver for specific findings ([§6](#6-waiver-flow)). |
| `verdict_filed → closed_fail` | HITL rejection. |
| `closed_*` → `stale` | Upstream invalidation per [dependency-invalidation-v0.md](dependency-invalidation-v0.md) §6. |
| `stale → open` | New revision triggers new gate cycle. |

Forbidden transitions:

- `assessing → closed_pass` (QA self-closes — QA does not approve, HITL does).
- `verdict_filed → (skipped HITL)` (no automatic transition to closed states).
- `closed_fail → closed_pass` without a new revision and new QA cycle.

---

## 3. Blocker semantics

Per [qa-result-payloads-v0.md](qa-result-payloads-v0.md) §`blocker` and [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §5:

A **blocker** is a QA finding whose severity is `blocker` — downstream consumption / delivery **must not proceed** without a fix or an explicit waiver.

| Blocker behavior | Detail |
|------------------|--------|
| **Without evidence** | Not a blocker — emit **SAFE UNKNOWN** instead. |
| **Inline fix in QA prompt** | Forbidden — QA does not produce production edits. |
| **Severity tuning** | Forbidden — severity changes require a new QA run or HITL. |
| **Contract gap exposed** | Surface **STRUCTURE CHANGE** ([orchestration-signals-v0.md](orchestration-signals-v0.md)). |
| **Multiple blockers** | Do not collapse into a single "overall blocker"; enumerate each. |
| **Blocker closure** | Only via revision + re-QA, or via HITL waiver ([§6](#6-waiver-flow)). |

A blocker forces the gate to `closed_fail` or `closed_waived`; a blocker **cannot** result in `closed_pass`.

---

## 4. Gate pass / fail

| Verdict | Meaning | Gate close state |
|---------|---------|------------------|
| **pass** | All blocker categories satisfied; warns / infos may exist but are not blocking. | `verdict_filed` → HITL → `closed_pass`. |
| **pass conditional** | All blocker categories satisfied **subject to bounded CRs**. | `verdict_filed` → HITL → `closed_conditional`. |
| **fail** | At least one blocker remains open; no waiver. | `verdict_filed` → HITL → `closed_fail` (revision required) or `closed_waived` (with HITL waiver per [§6](#6-waiver-flow)). |

Rules:

- A QA prompt may emit `pass conditional` **only** when CRs are bounded and listed with evidence ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §5).
- A QA prompt may emit `fail` **only** with blocker enumeration.
- A QA prompt **does not** emit `closed_*` — that is HITL's role.

---

## 5. Conditional pass

A **conditional pass** closes the gate at `closed_conditional` with explicit CRs that must be addressed before:

- the artifact moves to `frozen` ([artifact-state-model-v0.md](artifact-state-model-v0.md) §3); or
- a downstream stage consumes the artifact.

| Aspect | Detail |
|--------|--------|
| **Recording** | Approval artifact lists each CR with severity, evidence reference, resolution path ([approval-semantics-v0.md](approval-semantics-v0.md) §5). |
| **Downstream effect** | Downstream prompts must respect CRs as active obligations. |
| **Resolution** | CRs resolved within the **same revision id** when scope allows; new revision id required when scope expands. |
| **Forbidden** | Widening CRs silently; closing CRs without evidence; treating conditional pass as full freeze. |

A conditional pass is **not** a waiver; CRs **must** be resolved or explicitly waived under a separate named approver before freeze.

---

## 6. Waiver flow

A **waiver** ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §6) accepts a finding **temporarily or permanently** under a named approver. Lifecycle:

```text
finding open ─► waiver requested (NEED HUMAN APPROVAL) ─► HITL decision
                                                                  │
                                                                  ▼
                                                          waiver granted (scope + date + risk note)
                                                                  │
                                                                  ▼
                                                          finding remains attached as QA history;
                                                          gate moves to closed_waived
```

Waiver rules:

| Rule | Detail |
|------|--------|
| **HITL only** | Waivers require a named human approver. Agent-side waiver is **fabrication** ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md) §7). |
| **Bounded** | Scope (this revision / this run / permanent), date, risk note. |
| **Findings preserved** | Waiver does not delete findings ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §6). |
| **Risk note required** | Trade-off + downstream impact must be recorded. |
| **SECURITY RISK waivers** | Require additional approval per [`../../security/approval-gates.md`](../../security/approval-gates.md). |
| **Re-waiver on revision** | A new revision opens new findings; prior waivers may or may not carry forward — explicit decision required. |

A waiver **does not** make a finding "go away"; it permits proceeding **with the finding on record**.

---

## 7. Confidence handling

Per [qa-result-payloads-v0.md](qa-result-payloads-v0.md) §`confidence` and [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §7:

QA findings carry **confidence** (`low` / `medium` / `high`) **in addition to** severity.

| Confidence-aware lifecycle behavior |
|-------------------------------------|
| A `low` confidence finding may pair with **SAFE UNKNOWN** ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)) when evidence is partial. |
| A `low` confidence blocker **does not** automatically downgrade to warn; HITL discusses severity vs confidence explicitly. |
| A `high` confidence finding with direct evidence is least debatable. |
| Confidence **does not** replace severity in gate-close logic. A `low` confidence blocker still blocks unless waived. |
| Confidence appears in the QA REPORT for transparency, not as a tuning lever. |

Forbidden:

- using `low` confidence as a reason to silently drop a finding;
- using `high` confidence as evidence on its own — evidence is the artifact reference / repro step / screenshot reference, not the confidence value.

---

## 8. Evidence requirements

Per [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §3 and [qa-result-payloads-v0.md](qa-result-payloads-v0.md) §Core payload concepts:

At gate close, **every recorded finding** must have:

| Evidence | Examples |
|----------|----------|
| Artifact reference | URL, file path, selector, blueprint section, design frame name. |
| Reproduction step | How to observe the issue. |
| Viewport / breakpoint | For visual / responsive findings. |
| Screenshot reference | When available; required only where the lane mandates. |
| Contract / registry reference | Contract field name, registry row, policy rule for Validator-overlap findings. |

A finding without evidence is **not** a finding — at best it is a **SAFE UNKNOWN observation** ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §3).

The QA gate **cannot** close on findings without evidence; HITL **cannot** approve, reject, or waive what is not evidenced.

---

## 9. Freeze behavior

QA verdicts are tied to **artifact revisions** ([artifact-state-model-v0.md](artifact-state-model-v0.md)):

| Artifact transition | QA gate behavior |
|----------------------|------------------|
| `in_review → approved` | QA gate at `verdict_filed` → HITL → `closed_pass` / `closed_conditional` / `closed_waived`. |
| `approved → frozen` | QA verdict for the frozen revision **remains valid** for the frozen baseline. |
| `frozen → in_review` (revision opened) | Prior QA verdict becomes **stale** for the new revision; new gate cycle opens. |
| `approved → invalidated` / `frozen → invalidated` | Prior QA verdict becomes **stale**; new gate cycle opens on the new revision. |

A frozen artifact's QA verdict is **the verdict for that frozen revision only**. New revisions are assessed afresh.

---

## 10. Gate reset

A **gate reset** ([revision-semantics-v0.md](revision-semantics-v0.md) §9, [regeneration-semantics-v0.md](regeneration-semantics-v0.md) §9) occurs when:

- a revision opens on the artifact under review;
- a regeneration produces a new revision;
- an upstream invalidation propagates downstream;
- a registry / contract amendment requires re-assessment.

Reset behavior:

| Aspect | Detail |
|--------|--------|
| **Stale verdicts** | Preserved in QA history (append-only audit). |
| **Carry-forward findings** | Explicit enumeration in the new QA REPORT with rationale. |
| **New findings** | Open against the new revision id. |
| **Waivers** | Do **not** silently carry forward; explicit re-waiver decision required. |
| **Severity / confidence** | Re-evaluated against new revision; not copied from prior run. |

A gate that has reset must re-close via the standard verdict → HITL flow.

---

## 11. Delivery blocking

The Final Validation gate (S13) and the delivery gate (S15) ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md)) are **release-blocking**.

| Condition | Effect on delivery |
|-----------|---------------------|
| Open blockers without waiver | Delivery **blocked**; emit **DELIVERY BLOCKED** ([orchestration-signals-v0.md](orchestration-signals-v0.md) §3). |
| Unwaived SECURITY RISK | Delivery **blocked** until cleared per [`../../security/approval-gates.md`](../../security/approval-gates.md). |
| Open UNKNOWN bindings | Delivery **blocked**. |
| SAFE UNKNOWN without named approver | Delivery **blocked** until HITL acceptance. |
| Conditional approvals with unresolved CRs | Delivery **blocked** until CRs close. |
| Stale QA verdicts on the delivery candidate | Delivery **blocked** until re-QA. |

A delivery gate **never** closes on a non-empty blocker list without explicit HITL waiver + risk note.

---

## 12. Stale gate detection

A QA gate becomes **stale** when:

- the artifact moves to `invalidated` ([artifact-state-model-v0.md](artifact-state-model-v0.md));
- the underlying contract / registry has been amended under governance;
- the cross-lane neighboring artifact (e.g. blueprint changed → design QA stale) is updated;
- the prior gate's expiration window passes (rarely — most factory QA does not expire by time but by upstream change).

Stale detection is **prose discipline**: stages and downstream consumers must check their QA verdicts when consuming artifacts. A "QA was fine 3 weeks ago" claim **without** validating that the inputs are unchanged is forbidden.

---

## 13. HITL override and authority

Per [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §4 and [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md):

| Authority | What HITL may do | What HITL may NOT do |
|-----------|-------------------|-----------------------|
| HITL approver | Approve `pass`; approve `pass conditional` with bounded CRs; grant waivers; reject; request revision; park. | Modify findings; tune severity to make approval easier; close a fail without revision or waiver; bypass evidence requirements. |
| Stricter MARS approval policy ([`../../security/approval-gates.md`](../../security/approval-gates.md)) | Override factory waiver where stricter; require additional approver. | Be less strict than factory map. |

HITL **may** override a QA recommendation in three honest ways:

1. **Waiver** with named approver, scope, date, risk note ([§6](#6-waiver-flow)).
2. **Conditional approval** with bounded CRs ([§5](#5-conditional-pass)).
3. **Rejection** requiring revision.

HITL **may not** override by:

- ignoring evidence;
- rewriting findings;
- declaring a fail as a pass without recorded justification;
- approving against a SECURITY RISK without explicit security clearance.

---

## 14. Tie to QA payloads and prompt rules

This document **realizes** the lifecycle behavior implicit in [qa-result-payloads-v0.md](qa-result-payloads-v0.md) (field vocabulary) and [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) (prompt discipline).

| Source doc | Lifecycle anchor (this doc) |
|------------|------------------------------|
| qa-prompt-rules §2 (structure) | [§2.1](#21-gate-states) gate states + verdict filing. |
| qa-prompt-rules §3 (evidence) | [§8](#8-evidence-requirements). |
| qa-prompt-rules §4 (no fake approvals) | [§13](#13-hitl-override-and-authority). |
| qa-prompt-rules §5 (blockers) | [§3](#3-blocker-semantics). |
| qa-prompt-rules §6 (waivers) | [§6](#6-waiver-flow). |
| qa-prompt-rules §7 (confidence) | [§7](#7-confidence-handling). |
| qa-prompt-rules §8 (escalation) | [Orchestration signals](#orchestration-signals-v0). |
| qa-prompt-rules §9 (Validator) | Cross-cutting; Validator findings attach with same lifecycle. |
| qa-result-payloads §Core | [§8](#8-evidence-requirements). |
| qa-result-payloads §Lane relationships | Per-lane gate cycles ([§2](#2-qa-gate-lifecycle)). |

Conflicts must be resolved in favor of the **operational lifecycle** here for **gate behavior**, with [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) remaining the **prompt-discipline** anchor and [qa-result-payloads-v0.md](qa-result-payloads-v0.md) remaining the **field vocabulary** anchor.

---

## 15. Tie to Validator philosophy

Per [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §9 and [agent-map.md](agent-map.md):

- **Validator Agent** is **planned / legacy-bridge**. Validator-overlap findings attach to the same gate lifecycle as specialist QA.
- Validator findings carry their own evidence and severity per the same payload vocabulary.
- A gate **does not** close on the basis of "Validator probably approved" without a Validator REPORT.
- When Validator did not run, the gate's REPORT says so under **SAFE UNKNOWN**.

---

## 16. Tie to specialist QA lanes

Per [qa-validation-model.md](qa-validation-model.md) and [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §10:

Each specialist lane (Design QA / SEO QA / Conversion QA / Frontend QA / Validator overlap) has its **own gate cycle** at the relevant stage. Cross-lane interactions:

- Lanes **do not** speak on behalf of other lanes; cross-references are evidence, not authority.
- A lane that exposes a **STRUCTURE CHANGE** propagates upstream ([orchestration-signals-v0.md](orchestration-signals-v0.md)).
- A lane's gate may close while another lane's gate remains open; the **overall stage** moves to `approved` only when all relevant lane gates close ([stage-state-model-v0.md](stage-state-model-v0.md)).

---

## 17. Anti-patterns

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| "Gate auto-closed on pass." | Skips HITL. | HITL closes the gate. |
| "Severity downgraded after re-review." | Severity tuning. | Re-assess in scope; record honestly. |
| "Waiver self-approved by QA." | Bypasses HITL. | `NEED HUMAN APPROVAL` + wait. |
| "Conditional pass treated as freeze." | CRs ignored. | Resolve CRs or waive explicitly. |
| "Gate stale but artifact still consumed." | Silent staleness. | Re-open gate; re-QA on new revision. |
| "Blocker fixed inline by QA prompt." | QA does production edits. | Raise as finding; production fixes in separate prompt. |
| "Validator approved (Validator didn't run)." | Fabrication. | SAFE UNKNOWN on Validator. |
| "Delivery passed because QA was old and fine." | Stale gate at delivery. | Re-QA on the delivery candidate. |

---

## 18. Non-claims

- This document does **not** ship a QA runner.
- It does **not** assume an LLM enforces these states.
- It does **not** define wire formats for QA verdicts.
- It does **not** replace HITL judgment with predictable QA behavior.

What it **does** do is define **the lifecycle behavior of QA gates** — open, verdict, freeze, waiver, expiration, stale detection, HITL override — so QA outcomes stay traceable, comparable, and HITL-anchored across runs and lanes.

---

## 19. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial QA gating semantics (documentation only). |
