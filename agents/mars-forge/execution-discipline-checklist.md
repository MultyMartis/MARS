# Execution Discipline Checklist - MARS Forge

**Status:** **documented** - Forge overlay checklist for human-supervised operational workflow and execution discipline QA.  
**Not:** autonomous workflow AI, runtime orchestration, automatic checkpointing, universal SDLC enforcement, or perfect operational stability guarantee.

**Parent governance:** [`../../projects/mars-website-factory/operational-workflow-governance.md`](../../projects/mars-website-factory/operational-workflow-governance.md).  
**Execution model:** [`../../projects/mars-website-factory/execution-discipline-model.md`](../../projects/mars-website-factory/execution-discipline-model.md).  
**Drift taxonomy:** [`../../projects/mars-website-factory/workflow-drift-taxonomy.md`](../../projects/mars-website-factory/workflow-drift-taxonomy.md).

---

## 1. When To Run

Run this checklist before freeze, handoff, long-session continuation, multi-session continuation, or report closure when any of the following affect the section, page, or delivery scope:

- execution order or Forge phase sequencing;
- checkpoint state or missing checkpoint evidence;
- freeze validation, unfreeze reason, or reopen state;
- handoff quality or next-session survivability;
- uncontrolled iteration, repeated patching, or "just keep fixing" pressure;
- unsafe parallel modification or overlapping session scope;
- report consistency and future readability;
- context-loss continuation risk;
- task-boundary expansion or unclear scope;
- workflow escalation or HITL need.

Record results as **WORKFLOW DISCIPLINE FINDINGS**.

---

## 2. Intake QA

- [ ] Active task boundary is named: project, page, section, `block_id`, document, or scope.
- [ ] Active source/version and forbidden/stale sources are identified or marked **SAFE UNKNOWN**.
- [ ] Current workflow lane is clear: foundation, Forge overlay, QA, review, handoff, or documentation-only.
- [ ] Expected governance checklists are named when material.
- [ ] Files or sections likely to be touched are scoped or expansion is documented.
- [ ] Existing freeze/checkpoint state is known or marked **SAFE UNKNOWN**.

---

## 3. Execution-Order QA

- [ ] Work follows declared order: intake -> execution -> checkpoint -> validation -> freeze/review -> escalation -> handoff -> continuity.
- [ ] Forge phases are not mixed in ways that contaminate validation or freeze state.
- [ ] Structure/layout/styling/responsive/interaction/QA/freeze order is preserved or skip reason is documented.
- [ ] No validation or PASS claim is made before prerequisite evidence exists.
- [ ] No styling, interaction, or global fix silently resolves unresolved source, visual, responsive, or authority ambiguity.
- [ ] Execution-order contamination is recorded when later work depends on skipped or unstable earlier steps.

---

## 4. Task-Boundary QA

- [ ] Work remains inside the requested slice or scope expansion is explicit.
- [ ] Adjacent sections, shared tokens, includes, breakpoints, components, reports, or global files are not changed silently.
- [ ] One primary operational concern is active unless batching is explicitly authorized.
- [ ] "Small fix" changes do not cross into redesign, business authority, source priority, or architecture decisions.
- [ ] Boundary ambiguity is recorded as **WORKFLOW DISCIPLINE FINDINGS** or escalated.

---

## 5. Checkpoint QA

- [ ] Material progress has a checkpoint or report note with phase, scope, evidence, findings, and next action.
- [ ] Checkpoint names what changed since the last trusted state when relevant.
- [ ] Open findings, SAFE UNKNOWN items, deferrals, and blockers remain visible.
- [ ] Checkpoint state is not inferred from memory or a polished final summary.
- [ ] Missing checkpoint evidence is marked **SAFE UNKNOWN** instead of treated as continuity.
- [ ] Continuity checkpoint is created when long-running, multi-session, or repeated-iteration work accumulates risk.

---

## 6. Validation QA

- [ ] Relevant source, visual, responsive, implementation, QA confidence, escalation, multi-agent, strategic, temporal, and workflow checks are run or deferred with reason.
- [ ] PASS/PARTIAL/FAIL/SAFE UNKNOWN claims match evidence.
- [ ] Findings remain separated by layer instead of merged into one generic "QA passed."
- [ ] Workflow discipline is evaluated when execution order, checkpoint state, freeze readiness, handoff, or continuity affects trust.
- [ ] Validation gaps are disclosed before freeze or handoff.

---

## 7. Freeze-Validation QA

- [ ] Frozen scope, baseline, section, or `block_id` is named.
- [ ] Freeze evidence includes relevant governance findings or explicit deferrals.
- [ ] Unfreeze reason/path is documented when frozen scope is reopened or likely to change.
- [ ] Adjacent or shared-scope regression risk is reviewed or marked **SAFE UNKNOWN**.
- [ ] Freeze is not claimed when checkpoint state, validation evidence, or escalation ownership is missing.
- [ ] Silent freeze erosion is recorded when frozen scope changes without traceability.

---

## 8. Handoff QA

- [ ] Handoff names changed files/sections and current phase state.
- [ ] Handoff preserves validation performed and not performed.
- [ ] Handoff lists open findings, deferred risks, blockers, SAFE UNKNOWN items, and escalation state.
- [ ] Handoff states next safe action.
- [ ] Future operator can continue without private memory, transcript archaeology, or guessing.
- [ ] Unstable handoff is recorded as PARTIAL, SAFE UNKNOWN, HITL required, or STOP.

---

## 9. Continuity-Checkpoint QA

- [ ] Last trusted state, freeze baseline, or continuity reference is identified.
- [ ] Current work states what changed since that baseline when material.
- [ ] Prior unresolved findings are preserved or explicitly resolved.
- [ ] Repeated patches or long-running edits trigger continuity review.
- [ ] Current state does not depend on context-loss continuation.
- [ ] Continuity posture is PASS, PARTIAL, FAIL, SAFE UNKNOWN, checkpoint required, or HITL required.

---

## 10. Parallel / Multi-Session QA

- [ ] Overlapping file, section, token, include, breakpoint, component, or report edits are identified.
- [ ] Owner and order are clear when multiple sessions or agents touch the same scope.
- [ ] Reviewer/executor/validator/handoff responsibilities remain visible.
- [ ] Conflicting modifications are reconciled through evidence and checkpoint, not convenience.
- [ ] Unsafe parallel modification is routed through multi-agent coordination governance when role boundaries matter.

---

## 11. Drift Classification

Classify any issue using [`workflow-drift-taxonomy.md`](../../projects/mars-website-factory/workflow-drift-taxonomy.md):

- [ ] Chaotic execution
- [ ] Workflow entropy
- [ ] Uncontrolled iteration loops
- [ ] Unsafe parallel modification
- [ ] Checkpoint erosion
- [ ] Execution-order contamination
- [ ] Freeze omission
- [ ] Unstable handoff
- [ ] Report inconsistency
- [ ] Continuity blindness
- [ ] Task-boundary collapse
- [ ] Escalation bypass
- [ ] Context-loss execution

---

## 12. Workflow Escalation

Stop or escalate when:

- checkpoint state is missing but PASS, freeze, delivery readiness, or handoff is requested;
- execution order is too contaminated to validate honestly;
- task boundary collapsed into broader work without authority;
- parallel modifications conflict or ownership is unclear;
- handoff cannot be made stable from available evidence;
- context-loss execution would require guessing;
- human authority is needed for freeze, waiver, scope expansion, or contradiction.

Use **SAFE UNKNOWN**, **checkpoint required**, **HITL required**, or **STOP** rather than workflow abandonment.

---

## 13. Reporting Block

Use this block in Forge reports when execution discipline is in scope:

```text
WORKFLOW DISCIPLINE FINDINGS - <section or scope>

Intake / task boundary: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Execution order: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Checkpoint integrity: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Validation sequencing: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Freeze validation: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Handoff stability: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Continuity checkpoint: not needed | done | required | deferred | SAFE UNKNOWN
Parallel / multi-session risk: PASS | PARTIAL | FAIL | SAFE UNKNOWN

Workflow drift taxonomy:
- Patterns:
- Severity:
- Freeze / handoff impact:

Disposition:
- Action: safe to continue | checkpoint required | deferred | monitored risk | HITL required | STOP
- Evidence / unknowns:
```

Keep this separate from `IMPLEMENTATION RELIABILITY FINDINGS`, `QA CONFIDENCE FINDINGS`, `HUMAN ESCALATION FINDINGS`, `MULTI-AGENT FINDINGS`, and `TEMPORAL EVOLUTION FINDINGS`.

---

## 14. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- active task boundary is unclear;
- source/version authority is missing;
- current workflow phase cannot be reconstructed;
- checkpoint record is absent or stale;
- validation evidence is unavailable;
- freeze state is unproven;
- parallel modification ownership is unclear;
- handoff lacks enough context;
- continuity baseline cannot be identified;
- report consistency cannot be trusted.

**Action:** state what is unknown, what would resolve it, and whether continuation is safe with disclosure, checkpoint required, HITL required, blocked, or monitored risk.

---

## 15. Non-Goals

- Do not redesign Triumph or any other project.
- Do not invent autonomous workflow AI.
- Do not create runtime orchestration systems.
- Do not define universal SDLC law.
- Do not claim perfect operational stability.
- Do not use workflow discipline as a reason to keep patching without boundaries.

---

*Documentation only - no runtime enforcement.*
