# Governance Compression Checklist - MARS Forge

**Status:** Forge overlay QA checklist for Website Factory governance compression and operational modes.  
**Methodology:** [governance-compression-governance.md](../../projects/mars-website-factory/governance-compression-governance.md), [operational-modes-model.md](../../projects/mars-website-factory/operational-modes-model.md), [compression-drift-taxonomy.md](../../projects/mars-website-factory/compression-drift-taxonomy.md).  
**Not:** autonomous governance scaling, runtime mode engine, automatic QA allocation, universal operational modes, or perfect deployability.

Use this checklist when governance deployability, operational mode, report density, mode transition, compression integrity, or governance scalability affects the scope.

Record findings under **GOVERNANCE COMPRESSION FINDINGS**.

---

## 1. Operational Mode QA

- [ ] Current work is classified as one primary mode: lite, operational-standard, elevated-review, critical, freeze-validation, audit/reconstruction, or recovery/emergency.
- [ ] Mode selection is justified by scope, risk, uncertainty, reversibility, source authority, freeze state, delivery consequence, and continuity pressure.
- [ ] Lite mode is used only for local, reversible, well-sourced, low-risk work with narrow blast radius.
- [ ] Operational-standard mode is used for ordinary frontend slices with stable source and normal production risk.
- [ ] Elevated-review mode is used when ambiguity, regression risk, specialist concern, or shared implementation risk is material.
- [ ] Critical mode is used when freeze, delivery, source authority, business meaning, accessibility trust, project identity, or release confidence may be affected.
- [ ] Freeze-validation mode is used before freeze/reopen/defer/delivery-position claims.
- [ ] Audit/reconstruction mode is used when state, source lineage, checkpoint, or governance memory must be rebuilt.
- [ ] Recovery/emergency mode is used when trusted state is broken, rollback is active, or degraded state must be stabilized.

---

## 2. Governance Compression QA

- [ ] Compression preserves source authority, proof boundaries, unresolved risks, escalation triggers, mode decision, and SAFE UNKNOWN.
- [ ] Compression reduces duplicated explanation or low-value density, not material evidence.
- [ ] Compressed reporting remains readable to a future operator.
- [ ] Specialist findings are grouped or referenced when they are not material to the current mode.
- [ ] Critical findings are not buried inside compressed summaries.
- [ ] Shorter report length is not treated as success unless deployability and survivability both improve.
- [ ] Full-density reporting is not retained when it harms routine deployability without adding evidence value.

---

## 3. Deployability QA

- [ ] Governance can be applied in the current production session without requiring impractical report/checklist density.
- [ ] The selected mode supports the next safe action.
- [ ] Routine work is not forced to inherit critical-mode ceremony without a current trigger.
- [ ] Critical, freeze, audit, or recovery work receives enough rigor even if compression pressure exists.
- [ ] Governance portability is preserved: another operator can understand mode, evidence, risks, and next action.
- [ ] Deployment fatigue is checked when repeated runs become too dense to sustain.

---

## 4. Mode-Transition QA

- [ ] Any mode escalation or de-escalation is explicit.
- [ ] Transition trigger is named: scope growth, ambiguity, criticality, freeze, audit, recovery, evidence resolution, or density fatigue.
- [ ] Scaling up does not become permanent critical-mode inheritance.
- [ ] Scaling down does not hide material risk, source ambiguity, or escalation need.
- [ ] Freeze-validation, audit/reconstruction, and recovery/emergency transitions preserve stronger evidence and unknown visibility.
- [ ] Mode-transition ambiguity is recorded as drift when rationale is missing.

---

## 5. Governance Scalability QA

- [ ] The governance path can scale across repeated sections, sessions, handoffs, and projects.
- [ ] Report density does not grow faster than operational value.
- [ ] Governance layers remain navigable through README, OPERATIONAL-INDEX, and Forge links.
- [ ] Governance compression does not create cross-layer ambiguity or duplicate reporting confusion.
- [ ] The selected mode preserves longevity, not just current-session closure.
- [ ] SAFE UNKNOWN is used when scalability, portability, or deployability cannot be proven.

---

## 6. Compression-Integrity QA

- [ ] SAFE UNKNOWN items survive compression.
- [ ] Human-owned decisions and HITL requirements survive compression.
- [ ] Freeze/reopen/defer/recovery state survives compression.
- [ ] Evidence type remains visible: source, rendered, build, inferred, assumed, unknown, reconstructed, or recovery evidence.
- [ ] Confidence is not inflated by report shortening.
- [ ] Survivability-critical context is preserved for future handoff or audit.

---

## 7. Drift Checks

- [ ] No governance deployment overload.
- [ ] No one-mode governance.
- [ ] No compression survivability failure.
- [ ] No review-mode mismatch.
- [ ] No governance scalability erosion.
- [ ] No excessive critical-mode inheritance.
- [ ] No operational density collapse.
- [ ] No deployment fatigue.
- [ ] No governance portability failure.
- [ ] No mode-transition ambiguity.
- [ ] No survivability compression loss.
- [ ] No governance deployment rigidity.
- [ ] No operational scaling collapse.

---

## 8. REPORT Format

Use this block when governance compression affects the scope:

```text
GOVERNANCE COMPRESSION FINDINGS

Operational mode: lite | operational-standard | elevated-review | critical | freeze-validation | audit/reconstruction | recovery/emergency
Mode rationale: <scope / risk / uncertainty / reversibility / source authority / freeze or delivery consequence / continuity>
Compression posture: keep density | compress | expand | scale up | scale down | freeze-validate | audit/reconstruct | recover | SAFE UNKNOWN
Deployability QA: <whether the governance path is usable in this session and repeatable later>
Compression integrity: <what must survive compression: evidence / risks / escalation / SAFE UNKNOWN / freeze state>
Mode transition: <none | escalation | de-escalation | transition trigger | unresolved ambiguity>
Scalability / portability: <how future operators can reuse or understand this mode>
Drift checked: <none | deployment overload | one-mode governance | critical-mode inheritance | density collapse | ...>
Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN | HITL REQUIRED | BLOCKED
```

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- operational mode cannot be justified;
- compression may hide material evidence, risk, escalation, freeze state, or unknowns;
- deployability cannot be proven;
- mode transition lacks rationale;
- governance portability is unclear;
- critical-mode inheritance may be excessive;
- lite/standard mode may under-protect material risk;
- audit/reconstruction or recovery confidence is unclear.

Required statement:

- what mode/compression evidence is missing;
- which modes are possible;
- what must survive compression;
- what evidence would justify scale up, scale down, freeze validation, audit, or recovery;
- whether continuation is deployable, elevated-review-needed, critical, freeze-validation-needed, reconstruction-needed, recovery-needed, HITL-needed, blocked, or deferred.

---

## 10. Not Claimed

- No autonomous governance scaling AI.
- No runtime governance orchestrator.
- No universal operational mode system.
- No automatic QA-depth allocation.
- No automatic report compression.
- No perfect deployability guarantee.
- No permission to disable material QA or hide risk.

---

*Documentation only - no runtime enforcement.*
