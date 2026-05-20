# MARS Website Factory - Execution Discipline Model

**Status:** **documented** - Website Factory execution discipline model for human-supervised frontend workflow.  
**Not:** runtime workflow engine, autonomous task router, scheduling system, state machine implementation, or universal delivery methodology.

**Parent governance:** [operational-workflow-governance.md](operational-workflow-governance.md).  
**Drift taxonomy:** [workflow-drift-taxonomy.md](workflow-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/execution-discipline-checklist.md`](../../agents/mars-forge/execution-discipline-checklist.md).

---

## 1. Purpose

The Execution Discipline Model defines the layers that make Website Factory frontend work readable, resumable, and safe to hand off.

The model exists because frontend execution can appear productive while losing operational order. A workflow that keeps patching but cannot explain intake scope, checkpoint state, freeze readiness, validation evidence, escalation ownership, or handoff posture is not operationally stable.

---

## 2. Model Layers

| Layer | Purpose | Required output |
|-------|---------|-----------------|
| **Intake layer** | Establish source, scope, task boundary, authority, and active workflow lane. | Task scope, active source/version, files or sections, allowed changes, known unknowns. |
| **Execution layer** | Perform work in declared order without mixing concerns or expanding scope silently. | Ordered change record, phase state, changed areas, skipped-step rationale. |
| **Checkpoint layer** | Preserve state during or after material progress. | Checkpoint note with phase, evidence, findings, unknowns, next action. |
| **Validation layer** | Verify claims against evidence and governance checklists. | PASS/PARTIAL/FAIL/SAFE UNKNOWN by scope and evidence level. |
| **Freeze/review layer** | Decide whether scope can be frozen, reopened, deferred, blocked, or handed to review. | Freeze state, unfreeze path, blockers, deferred risks, review disposition. |
| **Escalation layer** | Route ambiguity, contradiction, authority gaps, unsafe continuation, or workflow breakdown. | Escalation reason, owner, decision boundary, stop/continue disposition. |
| **Handoff layer** | Transfer enough operational context for another operator or session to continue safely. | Summary, changed scope, evidence, findings, unresolved risks, next safe step. |
| **Continuity layer** | Preserve long-running workflow memory across sessions, freezes, and iterations. | Continuity checkpoint, trusted baseline, drift notes, unresolved SAFE UNKNOWN. |

These layers are conceptual governance layers. They do not imply a runtime state machine or automated workflow implementation.

---

## 3. Execution Ordering

Website Factory frontend execution should follow this order unless an explicit, reported reason changes it:

1. **Intake** - identify source, scope, authority, task boundary, and current state.
2. **Execution** - work inside the declared lane and phase order.
3. **Checkpoint** - record state after material progress, interruption, or scope risk.
4. **Validation** - run relevant source, visual, responsive, implementation, QA confidence, escalation, multi-agent, temporal, and workflow checks.
5. **Freeze/review** - classify frozen, partial, deferred, reopened, blocked, or review-required state.
6. **Escalation** - stop or route unresolved authority, evidence, workflow, or safety gaps.
7. **Handoff** - preserve enough context for continuation.
8. **Continuity** - ensure future sessions can reconstruct what changed and why.

Execution order may be adapted for small doc-only work, urgent defects, or operator-directed exceptions, but the exception should be recorded when it affects traceability, freeze, or handoff.

---

## 4. Intake Layer

The intake layer prevents task-boundary collapse before work begins.

Intake should establish:

- active project, page, section, block, or document scope;
- canonical source path, version, or authority;
- forbidden sources or stale references;
- expected workflow lane and checklist set;
- files likely to be touched;
- current freeze or checkpoint state;
- known SAFE UNKNOWN items;
- human/operator instruction boundaries.

Failure modes:

- starting from memory instead of source;
- treating prior output as authority without provenance;
- accepting a broad "continue" request without identifying the safe continuation point;
- mixing unrelated tasks because they are nearby.

---

## 5. Execution Layer

The execution layer protects deterministic sequencing.

Execution should:

- follow declared phase order;
- preserve one primary task boundary at a time;
- avoid parallel modification of the same scope without ownership;
- keep source edits and generated artifacts distinct;
- document skipped phases or scope expansions;
- avoid validating, freezing, or reporting before evidence exists.

Execution contamination occurs when later work inherits stale assumptions, half-finished changes, unresolved findings, or unrelated edits as if they were clean workflow state.

---

## 6. Checkpoint Layer

The checkpoint layer preserves state before memory decays.

Create or update a checkpoint when:

- a material section, phase, or governance check completes;
- work is interrupted;
- scope expands or changes;
- freeze is requested, deferred, or reopened;
- multiple sessions or agents may touch the same scope;
- unresolved findings or SAFE UNKNOWN items remain;
- a handoff is about to occur.

A checkpoint should record:

- scope and phase;
- files/sections affected;
- evidence gathered;
- findings opened/resolved/deferred;
- freeze state;
- SAFE UNKNOWN and resolver;
- next safe action.

---

## 7. Validation Layer

The validation layer keeps claims tied to evidence.

Validation should:

- name the checklist or governance layer used;
- keep findings separate by layer;
- qualify PASS, PARTIAL, FAIL, and SAFE UNKNOWN;
- avoid promoting build success, visual similarity, or agent agreement into universal proof;
- include workflow discipline QA when execution order, checkpoint state, freeze readiness, or handoff quality affects the outcome.

Validation without checkpoint traceability can still be operationally weak because future operators cannot reconstruct how the claim was reached.

---

## 8. Freeze / Review Layer

The freeze/review layer controls when a scope may be considered stable.

Freeze handling should name:

- frozen scope and baseline;
- validation evidence;
- unresolved findings or deferrals;
- unfreeze reason and path;
- adjacent or shared-scope regression risk;
- report section that preserves freeze state.

Freeze is unsafe when:

- checkpoint state is missing;
- validation evidence is partial but reported as complete;
- unresolved escalation is hidden;
- parallel changes may affect the same scope;
- future operators cannot tell what was frozen.

---

## 9. Escalation Layer

The escalation layer routes workflow problems before they become hidden drift.

Escalate or stop when:

- task boundary is unclear;
- checkpoint state is missing but freeze or PASS is requested;
- execution order was contaminated in a material way;
- conflicting parallel modifications are likely;
- report inconsistency hides risk;
- context-loss execution would be required to continue;
- human decision authority is needed for scope, freeze, waiver, or contradiction.

Escalation routing should align with [human-escalation-governance.md](human-escalation-governance.md) and [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md) when responsibility or role ownership is material.

---

## 10. Handoff Layer

The handoff layer makes work survivable after the current session.

A stable handoff includes:

- task summary and scope boundary;
- changed files or sections;
- execution phase state;
- validation performed and not performed;
- governance findings by layer;
- freeze state and unfreeze path;
- SAFE UNKNOWN items;
- next safe step;
- escalation or HITL status.

Unstable handoffs force the next operator to infer state from diffs, memory, or style of prior text. That is workflow drift even if the UI looks correct.

---

## 11. Continuity Layer

The continuity layer preserves long-running operational memory.

Continuity should answer:

- What is the last trusted state?
- What changed since then?
- Which findings remain unresolved?
- Which checkpoints matter for future work?
- Which frozen scopes must be protected?
- Which assumptions were disclosed but not resolved?
- What would make continuation unsafe?

Continuity connects this model to [temporal-evolution-governance.md](temporal-evolution-governance.md): temporal governance protects project identity over time; execution discipline protects workflow state across the work that creates that history.

---

## 12. Reporting Semantics

When execution discipline is in scope, reports should include **WORKFLOW DISCIPLINE FINDINGS**:

```text
WORKFLOW DISCIPLINE FINDINGS - <section or scope>

Task boundary integrity: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Execution order: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Checkpoint integrity: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Freeze validation: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Handoff stability: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Continuity checkpoint: not needed | done | required | deferred | SAFE UNKNOWN

Workflow drift pattern(s): <taxonomy names or none>
Disposition: safe to continue | checkpoint required | HITL required | blocked | monitored risk
Evidence / unknowns: <short scope>
```

Keep this separate from implementation, QA confidence, escalation, multi-agent, and temporal findings.

---

## 13. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- intake source or task boundary is missing;
- current workflow phase cannot be reconstructed;
- checkpoint state is absent;
- validation evidence is unavailable;
- freeze/review state is unclear;
- escalation owner is missing;
- handoff lacks enough context;
- continuity baseline cannot be identified.

**Action:** record what is unknown, what would resolve it, and whether continuation requires disclosure, checkpoint, HITL, or stop.

---

## 14. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Execution Discipline Model - intake, execution, checkpoint, validation, freeze/review, escalation, handoff, and continuity layers; documentation only. |
