# Compression Drift Taxonomy - Website Factory

**Status:** **documented** - Website Factory drift vocabulary for governance compression and operational modes.  
**Not:** automated drift detection, runtime governance enforcement, universal drift law, or proof that drift is present without evidence.

**Parent governance:** [governance-compression-governance.md](governance-compression-governance.md).  
**Operational model:** [operational-modes-model.md](operational-modes-model.md).  
**Forge checklist:** [`../../agents/mars-forge/governance-compression-checklist.md`](../../agents/mars-forge/governance-compression-checklist.md).

---

## 1. Purpose

This taxonomy names failure patterns where governance becomes too heavy, too rigid, too compressed, or too mode-blind to remain deployable.

It protects against the false assumption that strong methodology automatically means usable operational governance.

---

## 2. Drift Patterns

| Drift pattern | Definition | Typical symptom | Governance response |
|---------------|------------|-----------------|---------------------|
| **Governance deployment overload** | Governance is too dense to apply in real production sessions. | Operators avoid checks, reports balloon, next action becomes unclear. | Compress around mode, risk, evidence, and next action. |
| **One-mode governance** | Every task receives the same governance intensity. | Routine edits and critical freeze decisions use identical process. | Select explicit operational mode. |
| **Compression survivability failure** | Compression removes information required for future trust. | Short report hides source ambiguity, unresolved risk, or escalation. | Restore proof boundary, SAFE UNKNOWN, and mode rationale. |
| **Review-mode mismatch** | Review depth does not match current task risk. | Lite review covers critical risk, or critical review overwhelms local fix. | Reclassify mode and justify transition. |
| **Governance scalability erosion** | Governance cost/density grows faster than operational value. | Each new layer makes future use less repeatable. | Apply deployability and governance-scalability QA. |
| **Excessive critical-mode inheritance** | Critical rigor remains after critical trigger is gone. | Later low-risk tasks inherit freeze/delivery-level reporting. | De-escalate with survivability record. |
| **Operational density collapse** | Report/checklist density makes governance unreadable. | Findings are technically present but cannot be acted on. | Compress, group, prioritize, and preserve critical signal. |
| **Deployment fatigue** | Repeated high-density governance exhausts routine usage. | Operators skip checks or avoid governance because every run feels critical. | Move routine work to lite/standard mode. |
| **Governance portability failure** | Governance depends on private context or maximal local detail. | Future operators cannot reuse the compressed path. | Add portable mode/evidence/unknowns summary. |
| **Mode-transition ambiguity** | Operators cannot tell why intensity changed. | Report says "full QA" or "light pass" without trigger/rationale. | Record transition trigger and current mode. |
| **Survivability compression loss** | Continuity, freeze, escalation, or reconstruction evidence is compressed away. | Handoff looks clean but cannot support later audit/recovery. | Restore survivability-critical details. |
| **Governance deployment rigidity** | Governance refuses to scale despite context changes. | Same checklist depth persists through low-risk, critical, audit, and recovery work. | Use operational-mode transitions. |
| **Operational scaling collapse** | The governance system cannot handle many sections/sessions without cost and density failure. | The method works once but becomes unusable at project scale. | Review scalability, economics, cognitive load, and compression integrity. |

---

## 3. Severity Hints

| Severity | Use when |
|----------|----------|
| **Informational** | Compression or mode choice is suboptimal but does not affect evidence, escalation, freeze, or delivery confidence. |
| **Low** | Governance density or mode mismatch creates friction but remains recoverable through short report correction. |
| **Medium** | Mode mismatch, compression loss, or density overload may affect handoff, review confidence, or repeated deployability. |
| **High** | Critical evidence, source authority, freeze state, escalation, recovery, or delivery confidence may be hidden or under-protected. |
| **Blocking** | The current mode cannot safely continue because governance is too light, too dense, too ambiguous, or too rigid for the known risk. |

---

## 4. Drift Differentiation

Compression drift is adjacent to, but distinct from:

- **Governance minimalism drift** - rule/checklist bloat and complexity control.
- **Adaptive governance drift** - task-context rigor mismatch.
- **Governance economics drift** - cost/value imbalance.
- **Cognitive-load drift** - review readability and attention collapse.
- **Workflow drift** - execution order, checkpoints, freeze, and handoff instability.
- **Meta-governance drift** - layer topology, ownership, and contradiction issues.

Compression drift specifically asks whether governance can be **deployed at the right mode and density while preserving survivability**.

---

## 5. Anti-Pattern Phrases

Treat these as warning cues:

- "Run the full governance stack for every change."
- "Shorter report means lower quality."
- "Critical mode is safer as the default."
- "Lite mode means no QA."
- "Compression means remove unknowns."
- "Every governance layer must report separately every time."
- "If a rule exists, it must be mandatory."
- "A dense report proves rigor."
- "Routine work should inherit the last critical review."
- "Maximum governance always safer."

---

## 6. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Drift pattern is suspected but unproven | Cannot classify deployment overload, mode mismatch, or compression loss from available evidence. |
| Severity is unclear | Cannot determine whether mode drift affects handoff, freeze, escalation, recovery, or delivery. |
| Compression effect is unclear | Cannot prove whether shortened governance preserved material risk and proof boundaries. |
| Mode trigger is missing | Cannot know whether current intensity is justified. |
| Portability is untested | Cannot claim future operators can reuse the governance path. |

**Action:** name the suspected drift, state missing evidence, classify provisional severity, and decide whether to compress, expand, re-mode, escalate, defer, or block.

---

## 7. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial compression drift taxonomy - deployment overload, one-mode governance, compression survivability failure, review-mode mismatch, scalability erosion, critical-mode inheritance, density collapse, deployment fatigue, portability failure, transition ambiguity, survivability compression loss, deployment rigidity, and operational scaling collapse. |
