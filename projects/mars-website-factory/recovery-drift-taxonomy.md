# Recovery Drift Taxonomy - Website Factory

**Status:** **documented** - drift vocabulary for Website Factory failure recovery and operational resilience review.  
**Parent governance:** [failure-recovery-governance.md](failure-recovery-governance.md).  
**Model:** [operational-resilience-model.md](operational-resilience-model.md).

**Not:** automated drift detection, runtime incident classification, universal disaster-recovery taxonomy, or self-healing policy engine.

---

## 1. Purpose

This taxonomy names recovery drift patterns that can appear after frontend failure, partial rebuild collapse, corrupted continuity, rollback, freeze restoration, or emergency repair pressure.

The taxonomy is used for human-supervised reporting and Forge `FAILURE RECOVERY FINDINGS`.

---

## 2. Drift Patterns

| Pattern | Definition | Typical symptom | Governance response |
|---------|------------|-----------------|---------------------|
| **Corrupted continuity** | Active operational state contains missing, stale, contradictory, or contaminated history. | Work resumes from a fluent summary, but source, freeze, checkpoint, or decision state is unclear. | Stop broad continuation; reconstruct from artifacts and mark SAFE UNKNOWN. |
| **Rollback ambiguity** | Rollback target, scope, reason, or validation cannot be proven. | "Restore previous version" is requested without naming which state is trusted. | Identify rollback boundary and trusted state, or escalate. |
| **Broken freeze recovery** | Recovery cannot re-establish whether scope is frozen, reopened, superseded, blocked, or degraded. | A section is treated as frozen after emergency edits, but freeze evidence is missing. | Run freeze restoration review; do not claim freeze until proven. |
| **Contradictory checkpoints** | Checkpoints, reports, summaries, or source records disagree about current authority. | Two records claim different active versions, PASS states, or unresolved findings. | Escalate contradiction; choose authority through evidence or HITL. |
| **Panic-fix escalation** | Urgency pushes repairs beyond scoped recovery into hidden redesign or broad patching. | One fix triggers multiple unplanned edits to globals, breakpoints, copy, or layout. | Bound the patch, record risk, and route broader decisions to HITL. |
| **Unstable recovery loop** | Recovery repeatedly creates new failures, rollbacks, or patch layers without restoring trusted state. | Each repair requires another repair; no stable checkpoint emerges. | Stop loop, identify last trusted state, and checkpoint before continuing. |
| **Degraded-state normalization** | Partial or risky recovery is reported as healthy. | Report says PASS because UI loads, while missing states, source gaps, or unresolved validation remain. | Preserve degraded-state label and proof boundary. |
| **Recovery-without-validation** | Recovery is claimed without evidence that state, rollback, continuity, and degraded risk were checked. | Files are restored or build passes, but no recovery QA exists. | Run recovery validation or report SAFE UNKNOWN. |
| **Invalid trusted-state reuse** | An old, stale, archive, prior build, or summary state is treated as trusted without current authority. | Recovery resumes from prior success because it "worked before." | Re-verify authority, lineage, freeze posture, and validation evidence. |
| **Emergency-patch contamination** | Urgent repair introduces hidden coupling, source mutation, override pressure, or future rollback risk. | Hotfix touches shared selectors, tokens, or content without scope notes. | Record contamination risk and require implementation/workflow review. |
| **Reconstruction drift** | Reconstructed continuity mutates facts, authority, source order, or uncertainty. | Missing history is filled with plausible narrative rather than evidence. | Separate evidence, inference, assumption, and unknown. |
| **Resilience erosion** | Repeated recovery events weaken checkpoints, trust, readability, and escalation discipline. | The project becomes harder to recover each time, even when each fix appears local. | Add continuity checkpoint and temporal evolution review. |
| **Continuity-restoration collapse** | Recovery fixes visible output but fails to restore operational continuity. | UI appears stable but no one can explain current source, freeze, rollback, or unresolved findings. | Treat recovery as PARTIAL/FAIL until restoration is explainable. |

---

## 3. Severity Guidance

| Severity | Meaning | Typical action |
|----------|---------|----------------|
| **Low** | Drift is local, reversible, visible, and does not affect trusted state or freeze posture. | Continue with disclosure and checkpoint. |
| **Medium** | Drift affects recovery confidence, validation scope, degraded state, or future rollback clarity. | Require recovery findings and targeted validation. |
| **High** | Drift affects trusted state, rollback baseline, freeze restoration, source authority, or continuity reconstruction. | HITL recommended or required before PASS/freeze. |
| **Critical** | Drift makes recovery authority contradictory, untraceable, or unsafe to continue. | STOP or block by contradiction until human/project authority resolves it. |

Severity should follow evidence and impact, not urgency or visual polish.

---

## 4. Common False-Recovery Signals

These are not proof of recovery:

- build completes;
- page renders;
- previous file version is restored;
- visual output looks close again;
- one viewport passes;
- summary sounds coherent;
- no new error appears;
- agent confidence is high;
- emergency patch stops the immediate symptom.

Each may support a scoped finding, but none proves trusted-state recovery, rollback integrity, continuity restoration, or resilience.

---

## 5. Recovery Drift Combinations

Some patterns are especially risky together:

| Combination | Risk |
|-------------|------|
| **Rollback ambiguity + invalid trusted-state reuse** | Older state becomes false authority. |
| **Corrupted continuity + reconstruction drift** | Recovery narrative becomes more trusted than evidence. |
| **Broken freeze recovery + degraded-state normalization** | Frozen status hides partial or unsafe recovery. |
| **Panic-fix escalation + emergency-patch contamination** | Urgent repair becomes future implementation debt and rollback risk. |
| **Contradictory checkpoints + continuity-restoration collapse** | No record can safely govern continuation. |
| **Unstable recovery loop + resilience erosion** | Recovery process itself damages future recoverability. |

When combinations appear, record **FAILURE RECOVERY FINDINGS** and consider HITL even if visible output has recovered.

---

## 6. Reporting Vocabulary

Use concise labels:

```text
Recovery drift:
- Pattern: <taxonomy label>
- Severity: low | medium | high | critical
- Trusted-state impact:
- Rollback impact:
- Freeze / checkpoint impact:
- Degraded-state visibility:
- Continuity restoration impact:
- Disposition: safe with disclosure | checkpoint required | degraded | HITL required | STOP
```

Keep recovery drift separate from implementation drift, workflow drift, context drift, evolution drift, QA drift, and escalation drift, then summarize cross-layer impact.

---

## 7. SAFE UNKNOWN

Classify as **SAFE UNKNOWN** when:

- the pattern likely exists but evidence is incomplete;
- severity cannot be established;
- rollback or trusted-state impact is unknown;
- degraded-state risk may be hidden;
- continuity reconstruction cannot distinguish fact from assumption;
- checkpoint or freeze impact cannot be proven.

**Action:** state what evidence would resolve the classification and avoid claiming healthy recovery while taxonomy placement remains unknown.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial recovery drift taxonomy - corrupted continuity, rollback ambiguity, broken freeze recovery, contradictory checkpoints, panic-fix escalation, unstable recovery loop, degraded-state normalization, recovery-without-validation, invalid trusted-state reuse, emergency-patch contamination, reconstruction drift, resilience erosion, and continuity-restoration collapse; documentation only. |
