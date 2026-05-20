# Failure Recovery Checklist - MARS Forge

**Status:** **documented** - Forge overlay checklist for human-supervised failure recovery and operational resilience QA.  
**Not:** autonomous self-healing AI, runtime recovery automation, rollback service, incident platform, universal disaster recovery, or perfect resilience guarantee.

**Parent governance:** [`../../projects/mars-website-factory/failure-recovery-governance.md`](../../projects/mars-website-factory/failure-recovery-governance.md).  
**Operational resilience model:** [`../../projects/mars-website-factory/operational-resilience-model.md`](../../projects/mars-website-factory/operational-resilience-model.md).  
**Drift taxonomy:** [`../../projects/mars-website-factory/recovery-drift-taxonomy.md`](../../projects/mars-website-factory/recovery-drift-taxonomy.md).

---

## 1. When To Run

Run this checklist before recovery closure, rollback, freeze restoration, handoff, PASS/freeze claim, or report closure when any of the following affect the section, page, or delivery scope:

- corrupted continuity or missing trusted state;
- rollback, restore, revert, or "go back to previous version" request;
- failed rebuild, partial rebuild collapse, or failed reconstruction;
- broken freeze recovery, unclear reopen state, or contradictory freeze records;
- contradictory checkpoints, reports, summaries, matrices, or source authorities;
- emergency patching, panic fixes, or repeated recovery loops;
- degraded state that may be hidden behind visual recovery or build success;
- recovery requires HITL, checkpoint, context reconstruction, or validation boundary review.

Record results as **FAILURE RECOVERY FINDINGS**.

---

## 2. Trusted-State QA

- [ ] Last trusted state is named: source, checkpoint, freeze baseline, report, commit/reference, or artifact record.
- [ ] Trusted state has visible authority, validation evidence, scope, and remaining unknowns.
- [ ] Recovery does not rely on stale summaries, archive screenshots, prior success, or memory as authority.
- [ ] Invalid trusted-state reuse is recorded when an older or unproven state is used under pressure.
- [ ] Missing trusted state is marked **SAFE UNKNOWN**, checkpoint required, HITL required, or STOP.

---

## 3. Rollback Integrity QA

- [ ] Rollback target and rollback reason are explicit.
- [ ] Rollback scope is bounded: affected sections, files, artifacts, tokens, includes, breakpoints, and reports.
- [ ] Excluded scope is named when adjacent or shared areas could be affected.
- [ ] Rollback validation is planned or performed; build/file restoration alone is not treated as proof.
- [ ] Rollback impact on freeze state, checkpoints, source authority, and open findings is visible.
- [ ] Blind rollback, restore-to-unknown, or rollback-without-validation is recorded as drift.

---

## 4. Freeze Restoration QA

- [ ] Current freeze posture is classified: frozen-restored, reopened-for-recovery, superseded, degraded-freeze, blocked-by-freeze-ambiguity, or SAFE UNKNOWN.
- [ ] Unfreeze or recovery reason is documented when a frozen scope is touched.
- [ ] Recovery states what changed since the last trusted freeze or checkpoint.
- [ ] Adjacent or shared-scope regression risk is reviewed when recovery touches common files.
- [ ] Freeze is not reclaimed while validation evidence, checkpoint state, or escalation ownership is missing.

---

## 5. Degraded-State QA

- [ ] Recovery state is classified: healthy, partial, degraded, blocked, HITL-required, or SAFE UNKNOWN.
- [ ] Any degraded state remains visible in REPORT and handoff.
- [ ] Visual recovery, build success, or restored file presence is not treated as full recovery.
- [ ] Unverified states, breakpoints, interactions, accessibility, source authority, or rollback impact are disclosed.
- [ ] Degraded-state normalization is recorded when partial recovery is being framed as complete.

---

## 6. Continuity Restoration QA

- [ ] Recovery reconstructs continuity from named artifacts, reports, checkpoints, freeze records, and explicit unknowns.
- [ ] Evidence, inference, assumption, and unknown are separated.
- [ ] Checkpoint contradiction, summary contamination, source contradiction, or missing continuity is not resolved by guesswork.
- [ ] Recovery explains what can continue safely and what remains blocked, degraded, or HITL-required.
- [ ] Context survivability review is run when compressed context, summary integrity, or reconstruction affects recovery trust.

---

## 7. Recovery Traceability QA

- [ ] Failure event or unsafe state is described.
- [ ] Last trusted state and recovery path are traceable.
- [ ] Rollback, reconstruction, degraded operation, escalation, and validation decisions are recorded.
- [ ] The next safe action is stated.
- [ ] A future operator can explain why recovery is safe, partial, degraded, blocked, or escalated.
- [ ] Recovery opacity is recorded when the path cannot be reconstructed from the report.

---

## 8. Resilience Validation QA

- [ ] Recovery preserved checkpoint visibility rather than hiding behind "fixed" output.
- [ ] Recovery did not introduce emergency-patch contamination, broad overrides, hidden coupling, or source mutation.
- [ ] Repeated recovery attempts are checked for unstable recovery loops and resilience erosion.
- [ ] QA confidence matches recovery evidence and does not overclaim.
- [ ] Implementation reliability review is run when recovery affects CSS scope, includes, breakpoints, JS hooks, tokens, or shared files.
- [ ] Operational workflow review is run when checkpoint, handoff, execution order, or freeze-validation state affects recovery.

---

## 9. Recovery Escalation

Stop or escalate when:

- trusted state cannot be identified;
- rollback target or scope is ambiguous;
- checkpoints or freeze records contradict;
- recovery requires guessing missing continuity;
- degraded state would be hidden by PASS/freeze/delivery language;
- emergency patches affect source authority, business meaning, shared implementation, or delivery readiness;
- recovery cannot be validated inside the requested scope.

Use **SAFE UNKNOWN**, **checkpoint required**, **HITL required**, **blocked by contradiction**, or **STOP** rather than panic repair.

---

## 10. Drift Classification

Classify any issue using [`recovery-drift-taxonomy.md`](../../projects/mars-website-factory/recovery-drift-taxonomy.md):

- [ ] Corrupted continuity
- [ ] Rollback ambiguity
- [ ] Broken freeze recovery
- [ ] Contradictory checkpoints
- [ ] Panic-fix escalation
- [ ] Unstable recovery loop
- [ ] Degraded-state normalization
- [ ] Recovery-without-validation
- [ ] Invalid trusted-state reuse
- [ ] Emergency-patch contamination
- [ ] Reconstruction drift
- [ ] Resilience erosion
- [ ] Continuity-restoration collapse

---

## 11. Reporting Block

Use this block in Forge reports when failure recovery is in scope:

```text
FAILURE RECOVERY FINDINGS - <section or scope>

Failure / unsafe state:
Last trusted state: <named / partial / SAFE UNKNOWN>
Trusted-state QA: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Rollback integrity: PASS | PARTIAL | FAIL | SAFE UNKNOWN | not applicable
Freeze restoration: PASS | PARTIAL | FAIL | SAFE UNKNOWN | not applicable
Degraded-state handling: healthy | partial | degraded | blocked | HITL required | SAFE UNKNOWN
Continuity restoration: evidence-based | partial | assumption-based | contradicted | blocked | not needed
Recovery traceability: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Resilience validation: PASS | PARTIAL | FAIL | SAFE UNKNOWN

Recovery drift taxonomy:
- Patterns:
- Severity:
- Freeze / rollback / handoff impact:

Disposition:
- Action: safe to continue | checkpoint required | degraded-state visible | monitored risk | HITL required | STOP
- Evidence / unknowns:
```

Keep this separate from `WORKFLOW DISCIPLINE FINDINGS`, `CONTEXT SURVIVABILITY FINDINGS`, `TEMPORAL EVOLUTION FINDINGS`, `IMPLEMENTATION RELIABILITY FINDINGS`, `QA CONFIDENCE FINDINGS`, and `HUMAN ESCALATION FINDINGS`.

---

## 12. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- last trusted state is missing;
- rollback baseline is unclear;
- checkpoint records contradict;
- freeze posture cannot be restored;
- recovery validation is absent;
- continuity reconstruction requires guessing;
- emergency patch scope is unbounded;
- degraded state may be hidden.

**Action:** state what is unknown, what would resolve it, and whether recovery is safe with disclosure, checkpoint required, degraded, HITL required, blocked, or monitored risk.

---

## 13. Non-Goals

- Do not redesign Triumph or any other project.
- Do not invent autonomous self-healing AI.
- Do not create runtime recovery systems.
- Do not define universal disaster-recovery law.
- Do not claim perfect resilience.
- Do not treat "it works again" as recovery without trusted-state, rollback, continuity, and validation evidence.

---

*Documentation only - no runtime enforcement.*
