# Operational Modes Model - Website Factory

**Status:** **documented** - Website Factory operational-mode vocabulary for human-supervised governance deployment.  
**Not:** runtime mode engine, autonomous process selector, universal operating model, automatic QA-depth allocation, or perfect deployability guarantee.

**Parent governance:** [governance-compression-governance.md](governance-compression-governance.md).  
**Drift taxonomy:** [compression-drift-taxonomy.md](compression-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/governance-compression-checklist.md`](../../agents/mars-forge/governance-compression-checklist.md).

---

## 1. Purpose

The Operational Modes Model gives Website Factory operators a shared vocabulary for scaling governance intensity without treating every frontend task as critical-mode work.

The model protects:

- scalable operational deployment;
- proportional governance intensity;
- compression survivability;
- adaptive operational modes;
- sustainable deployability;
- clear mode transitions.

Modes are **methodology states**, not automated runtime states.

---

## 2. Mode Stack

| Mode | Use when | Governance density | Required survivability |
|------|----------|--------------------|------------------------|
| **Lite mode** | Work is local, reversible, well-sourced, low-risk, and narrow in blast radius. | Short checklist, focused evidence, compact report. | Scope, source, change, validation boundary, SAFE UNKNOWN if any. |
| **Operational-standard mode** | Normal frontend slice with stable source and ordinary production risk. | Standard Forge/foundation flow with relevant specialist checks. | Phase state, evidence, findings, freeze/deferral posture, handoff note. |
| **Elevated-review mode** | Ambiguity, regression risk, responsive/interaction/state/accessibility complexity, or shared implementation risk is material. | More evidence and specialist checks, but still targeted. | Risk rationale, elevated checks, proof boundaries, escalation decision. |
| **Critical mode** | Freeze, delivery, business meaning, source authority, accessibility trust, project identity, or release confidence may be affected. | High rigor, explicit findings, stronger escalation and evidence. | Full relevant evidence, risk weighting, HITL boundary, freeze/delivery impact. |
| **Freeze-validation mode** | A scope is being frozen, reopened, deferred, or declared delivery-relevant. | Freeze-focused validation and anti-regression review. | Frozen scope, evidence, unresolved findings, unfreeze path, continuity note. |
| **Audit/reconstruction mode** | State, source lineage, checkpoint, report, or governance history must be reconstructed. | Investigative depth, provenance, unknowns, contradiction handling. | Reconstructed baseline, evidence gaps, confidence limits, SAFE UNKNOWN. |
| **Recovery/emergency mode** | Trusted state is broken, rollback/recovery is active, or degraded state must be handled. | Fast but explicit recovery governance; critical unknowns stay visible. | Trusted-state claim, rollback boundary, recovery evidence, degraded-state risks. |

---

## 3. Mode Selection Questions

Before choosing a mode, ask:

- What is the task scope and blast radius?
- Is the work reversible without harming freeze, delivery, source authority, or project identity?
- What source authority and evidence are available?
- What can break: visual intent, semantics, responsiveness, accessibility, state, workflow, freeze, trust, or delivery?
- Does the task need routine deployability, elevated review, critical rigor, freeze validation, reconstruction, or recovery?
- What is the smallest sufficient mode that preserves evidence, escalation, and continuity?
- What would be unsafe to compress?

**Rule:** mode selection should be explicit when it affects QA depth, escalation, report density, freeze state, or handoff.

---

## 4. Mode Transitions

Mode transitions are allowed, but hidden transitions are drift.

| Transition | Valid trigger | Required record |
|------------|---------------|-----------------|
| **Lite -> operational-standard** | Scope grows, evidence need increases, or standard Forge/foundation checks become material. | New scope and QA depth. |
| **Standard -> elevated-review** | Ambiguity, regression risk, specialist concern, or uncertainty becomes material. | Elevated risk and added evidence/checks. |
| **Elevated -> critical** | Freeze, delivery, source authority, accessibility trust, business meaning, or project identity becomes at risk. | Criticality rationale and escalation boundary. |
| **Any mode -> freeze-validation** | Scope is being frozen, reopened, deferred, or delivery-positioned. | Freeze state, evidence, unresolved findings, unfreeze path. |
| **Any mode -> audit/reconstruction** | Checkpoint, source lineage, state, report, or governance memory is untrusted. | Reconstruction scope, known evidence, unknowns, confidence. |
| **Any mode -> recovery/emergency** | Trusted state breaks, rollback is needed, or degraded state must be stabilized. | Recovery baseline, action boundary, evidence, remaining risk. |
| **Critical/elevated -> standard/lite** | Risk is resolved, scope narrows, evidence becomes stable, or continued depth would create deployment fatigue. | De-escalation reason and what survivability remains. |

---

## 5. Escalation Thresholds

Escalate mode when:

- source authority is ambiguous or contradictory;
- freeze/delivery confidence is affected;
- accessibility trust, business meaning, or project identity may be harmed;
- compressed context or checkpoint loss affects continuation;
- recovery requires trusted-state judgment;
- multiple governance layers conflict;
- report compression may hide material risk.

De-escalate mode when:

- risk becomes local, reversible, well-sourced, and low blast-radius;
- critical evidence is resolved or deferred with explicit owner;
- full-depth review adds little decision value;
- report density is harming deployability;
- further rigor would create review fatigue without added safety.

---

## 6. Deployability Scaling

Each mode should preserve a different level of operational detail:

| Mode | Report compression posture |
|------|----------------------------|
| **Lite** | One short scope/evidence/disposition note is usually enough. |
| **Operational-standard** | Standard findings with only relevant specialist sections. |
| **Elevated-review** | Expanded findings for material risks; low-risk context stays compressed. |
| **Critical** | Full relevant evidence, explicit escalation, proof boundaries, and confidence. |
| **Freeze-validation** | Freeze state and unresolved findings are never compressed away. |
| **Audit/reconstruction** | Unknowns, lineage gaps, and confidence limits stay visible. |
| **Recovery/emergency** | Recovery speed is allowed, but trusted-state uncertainty stays explicit. |

Compression should reduce density, not responsibility.

---

## 7. Survivability Balancing

Operational modes balance five survivability needs:

- **Evidence survivability** - enough evidence remains to trust or challenge the result.
- **Escalation survivability** - human-owned or blocked decisions remain visible.
- **Context survivability** - compressed reports preserve what future operators need.
- **Deployability survivability** - governance can be repeated without operational fatigue.
- **Transition survivability** - mode changes remain traceable and justified.

The correct mode is not always the strongest mode. The correct mode is the one that protects material risk while preserving operational deployment.

---

## 8. Anti-Patterns

- **One-mode governance** - every task receives the same intensity.
- **Permanent critical mode** - critical rigor becomes routine operating density.
- **Lite-mode risk hiding** - compression hides material evidence or unknowns.
- **Standard-mode complacency** - ordinary mode continues after risk escalates.
- **Elevated-review stickiness** - elevated depth remains after the trigger is gone.
- **Freeze-validation shortcutting** - freeze is claimed without evidence and unresolved-finding visibility.
- **Audit without reconstruction honesty** - reconstructed state is treated as original source authority.
- **Recovery panic mode** - emergency speed hides trusted-state uncertainty.
- **Mode-transition ambiguity** - operators cannot tell why intensity changed.

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Mode cannot be selected | Risk, source, reversibility, or consequence is unclear. |
| Mode transition is unjustified | Cannot prove why governance scaled up or down. |
| Compression may erase evidence | Cannot safely reduce density without losing proof boundary or escalation. |
| Critical mode may be over-inherited | Cannot tell whether high rigor is still required. |
| Lite/standard mode may under-protect risk | Cannot prove low operational intensity is safe. |
| Freeze/recovery/audit state is unclear | Cannot claim freeze, recovery, or reconstruction confidence. |

**Action:** state possible modes, name missing evidence, choose provisional intensity, and disclose whether continuation is deployable, elevated-review-needed, critical, freeze-validation-needed, reconstruction-needed, recovery-needed, HITL required, or blocked.

---

## 10. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial operational modes model - lite, operational-standard, elevated-review, critical, freeze-validation, audit/reconstruction, recovery/emergency; documentation only. |
