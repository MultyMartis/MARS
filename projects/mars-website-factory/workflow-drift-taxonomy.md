# MARS Website Factory - Workflow Drift Taxonomy

**Status:** **documented** - taxonomy for human-supervised Website Factory workflow drift classification.  
**Not:** automated workflow detector, runtime monitoring system, project-management engine, or universal process compliance framework.

**Parent governance:** [operational-workflow-governance.md](operational-workflow-governance.md).  
**Execution model:** [execution-discipline-model.md](execution-discipline-model.md).  
**Forge checklist:** [`../../agents/mars-forge/execution-discipline-checklist.md`](../../agents/mars-forge/execution-discipline-checklist.md).

---

## 1. Purpose

This taxonomy names operational workflow drift patterns that can appear during frontend execution even when the visible output looks acceptable.

Workflow drift is dangerous because it damages traceability, checkpoint continuity, freeze validity, and handoff survivability. A project can look productive while its workflow record becomes impossible to trust.

---

## 2. Taxonomy Summary

| Drift pattern | Primary risk |
|---------------|--------------|
| **Chaotic execution** | Work proceeds reactively without declared order, phase, or state. |
| **Workflow entropy** | Operational records accumulate confusion, gaps, and inconsistent findings. |
| **Uncontrolled iteration loops** | Repeated fixes continue without checkpoint, boundary, or stop condition. |
| **Unsafe parallel modification** | Multiple lanes affect the same scope without ownership or coordination. |
| **Checkpoint erosion** | Checkpoints become missing, stale, vague, or detached from evidence. |
| **Execution-order contamination** | Later phases inherit unvalidated or out-of-order decisions. |
| **Freeze omission** | Work claims done, PASS, or delivery-ready without freeze validation. |
| **Unstable handoff** | The next operator cannot continue without guessing. |
| **Report inconsistency** | Reporting stops preserving comparable findings, states, or risks. |
| **Continuity blindness** | Current work ignores prior trusted state, freeze, or open findings. |
| **Task-boundary collapse** | Scope expands silently into adjacent sections, files, or governance decisions. |
| **Escalation bypass** | Stop conditions or human-owned decisions are worked around. |
| **Context-loss execution** | Work continues after essential context has been lost. |

---

## 3. Chaotic Execution

**Definition:** Work proceeds by reacting to visible issues or new ideas without a declared workflow phase, execution order, or checkpoint target.

Signals:

- structure, styling, responsive, interaction, QA, and report edits happen in mixed order;
- "one more fix" repeatedly changes the active scope;
- no one can name the current phase;
- validation is performed before prerequisite work is stable.

Impact:

- increases regression risk;
- weakens freeze claims;
- hides why changes were made;
- makes handoff reconstruction difficult.

Mitigation:

- restate current phase and task boundary;
- create a checkpoint;
- resume from the earliest contaminated phase that matters.

---

## 4. Workflow Entropy

**Definition:** Workflow records accumulate enough gaps, inconsistent naming, stale assumptions, and scattered findings that operational state becomes hard to read.

Signals:

- reports use inconsistent sections or omit expected findings;
- unresolved risks appear in one session and disappear in the next;
- checkpoint language is vague or repetitive;
- future actions are not distinguishable from completed actions.

Impact:

- future operators cannot trust the record;
- SAFE UNKNOWN items are lost;
- governance becomes theater instead of continuity.

Mitigation:

- normalize the report structure;
- restore open findings;
- perform a continuity checkpoint.

---

## 5. Uncontrolled Iteration Loops

**Definition:** Iteration continues without bounded scope, checkpoint review, or stop condition.

Signals:

- repeated local patches keep changing the same area;
- no explicit "done," "deferred," or "blocked" state exists;
- improvements are justified by taste, polish, or momentum;
- freeze keeps moving without reason.

Impact:

- creates patch-history entropy;
- damages checkpoint integrity;
- can silently mutate design, strategy, accessibility, or implementation identity.

Mitigation:

- define iteration boundary;
- run freeze validation or escalation;
- record why further changes are needed or blocked.

---

## 6. Unsafe Parallel Modification

**Definition:** Multiple sessions, agents, or lanes modify overlapping frontend scope without clear ownership, ordering, or merge discipline.

Signals:

- same file, section, token, include, breakpoint, or report is touched by more than one lane;
- reviewer and executor responsibilities blur;
- handoff does not name parallel work;
- conflicting changes are resolved by convenience.

Impact:

- creates execution contamination;
- damages reviewer independence;
- can invalidate checkpoints and freeze state.

Mitigation:

- identify ownership;
- reconcile changes through a checkpoint;
- use [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md) when role boundaries matter.

---

## 7. Checkpoint Erosion

**Definition:** Checkpoints are missing, stale, too vague, or not tied to evidence.

Signals:

- report says "done" without phase, evidence, or findings;
- freeze state exists but no validation path is visible;
- open risks lack owner or next action;
- checkpoint does not say what changed since the last trusted state.

Impact:

- weakens continuity;
- makes future handoffs unsafe;
- turns PASS/freeze into unverifiable claims.

Mitigation:

- recreate checkpoint from available evidence;
- mark unrecoverable gaps as SAFE UNKNOWN;
- avoid freeze/delivery claims until checkpoint integrity is restored.

---

## 8. Execution-Order Contamination

**Definition:** Later work relies on earlier steps that were skipped, unstable, or unvalidated.

Signals:

- styling begins before structure is confirmed;
- interaction binds before layout/responsive behavior is stable;
- freeze is requested before QA confidence and escalation boundaries are reviewed;
- report summarizes a clean sequence that did not happen.

Impact:

- hides root causes;
- creates fragile fixes;
- may require returning to an earlier phase.

Mitigation:

- identify the earliest contaminated step;
- rerun or qualify the affected validation;
- disclose partial state.

---

## 9. Freeze Omission

**Definition:** Work is treated as complete without an explicit freeze/review decision.

Signals:

- "looks good" or "PASS" replaces frozen/deferred/blocked state;
- no unfreeze path is recorded;
- adjacent edits affect a supposedly stable section;
- frozen baseline is not named.

Impact:

- weakens regression survivability;
- confuses future continuation;
- breaks temporal evolution and checkpoint integrity.

Mitigation:

- run freeze validation;
- record frozen scope or blocker;
- connect to [temporal-evolution-governance.md](temporal-evolution-governance.md) when baseline continuity matters.

---

## 10. Unstable Handoff

**Definition:** Handoff lacks enough context for another operator to continue safely.

Signals:

- changed files or sections are not named;
- findings are collapsed into a vague summary;
- unknowns, blockers, or deferrals are absent;
- next action is unclear.

Impact:

- causes context-loss execution;
- increases duplicated work and unsafe assumptions;
- can contaminate later validation.

Mitigation:

- provide a handoff block with scope, evidence, findings, freeze state, SAFE UNKNOWN, and next safe action;
- stop if critical context cannot be reconstructed.

---

## 11. Report Inconsistency

**Definition:** Reports stop preserving stable headings, evidence boundaries, findings, or status semantics.

Signals:

- expected Forge findings are missing when in scope;
- PASS/PARTIAL/FAIL/SAFE UNKNOWN terms are used inconsistently;
- freeze, checkpoint, and handoff state move between unrelated sections;
- prior finding categories are renamed or merged without reason.

Impact:

- damages operational readability;
- makes longitudinal comparison hard;
- hides unresolved risks.

Mitigation:

- restore expected report blocks;
- keep layer findings separate;
- state deviations explicitly.

---

## 12. Continuity Blindness

**Definition:** Current work ignores prior freeze state, trusted baselines, open findings, or continuity checkpoints.

Signals:

- current session starts from latest visible files without reading continuity docs;
- prior SAFE UNKNOWN or HITL items are not preserved;
- repeated patches are treated as current truth;
- no one asks what changed since the last trusted state.

Impact:

- weakens project memory;
- creates temporal drift;
- can turn accidental current state into canonical identity.

Mitigation:

- perform continuity checkpoint;
- restore baseline and open findings;
- route long-term identity questions to temporal evolution governance.

---

## 13. Task-Boundary Collapse

**Definition:** Work expands beyond the declared task without explicit scope change or authority.

Signals:

- adjacent sections are edited because they are nearby;
- global tokens, includes, or components are modified for local needs;
- report claims the original task while changes cover broader scope;
- governance decisions are made while described as implementation.

Impact:

- creates hidden regression surface;
- bypasses human authority;
- weakens handoff stability.

Mitigation:

- stop and restate scope;
- split work or request authority;
- record boundary expansion as a finding.

---

## 14. Escalation Bypass

**Definition:** Stop conditions, contradictions, missing authority, or human-owned decisions are avoided to keep work moving.

Signals:

- "probably intended" replaces source authority;
- ambiguity is resolved by taste;
- approval is implied from silence;
- workflow instability is not reported because output looks acceptable.

Impact:

- creates fake autonomy;
- can invalidate freeze and QA claims;
- hides human decision needs.

Mitigation:

- use [human-escalation-governance.md](human-escalation-governance.md);
- classify decision boundary;
- stop or continue only with disclosure.

---

## 15. Context-Loss Execution

**Definition:** Work continues after essential source, checkpoint, decision, or handoff context has been lost.

Signals:

- operator cannot identify active source or current checkpoint;
- previous session decisions are assumed from memory;
- missing report sections are filled by inference;
- continuation requires guessing what prior work meant.

Impact:

- causes false continuity;
- weakens traceability;
- can propagate stale or incorrect assumptions.

Mitigation:

- stop and reconstruct from source;
- record unrecoverable gaps as SAFE UNKNOWN;
- create a fresh continuity checkpoint before further changes.

---

## 16. Reporting Use

When a workflow drift pattern is detected, record:

- pattern name;
- affected scope;
- evidence;
- workflow layer affected;
- checkpoint/freeze/handoff impact;
- disposition: safe to continue, checkpoint required, HITL required, blocked, or monitored risk.

---

## 17. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Workflow Drift Taxonomy - chaotic execution, workflow entropy, uncontrolled iteration loops, unsafe parallel modification, checkpoint erosion, execution-order contamination, freeze omission, unstable handoff, report inconsistency, continuity blindness, task-boundary collapse, escalation bypass, and context-loss execution; documentation only. |
