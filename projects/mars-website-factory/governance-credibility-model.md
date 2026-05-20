# MARS Website Factory - Governance Credibility Model

**Status:** **documented** - Website Factory governance credibility model and human-supervised trust-calibration methodology only.  
**Not:** runtime credibility scoring, autonomous reliability engine, universal trust model, mathematical certification, or perfect credibility guarantee.

**Purpose:** define the trust layers that keep governance credibility proportional, explainable, and survivable across QA, reasoning, escalation, handoff, failure, and future review.

**Parent governance:** [trust-calibration-governance.md](trust-calibration-governance.md).  
**Companion taxonomy:** [trust-drift-taxonomy.md](trust-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/trust-calibration-checklist.md`](../../agents/mars-forge/trust-calibration-checklist.md).

---

## 1. Model Overview

Governance credibility is not a single score. It is a layered relationship between evidence, confidence, uncertainty, escalation, continuity, institutional trust, and failure survivability.

| Layer | What it protects | Primary question |
|-------|------------------|------------------|
| **Evidence-backed trust layer** | Trust anchored to visible evidence, verification scope, and source authority | What evidence supports this trust? |
| **Rendered-confidence layer** | The confidence created by wording, format, report length, and presentation | Does the report appear more certain than it is? |
| **Escalation-confidence layer** | Trust created or limited by HITL, stop conditions, contradiction handling, and authority boundaries | Is continuation trust authorized or should it escalate? |
| **Calibrated-uncertainty layer** | Credibility preserved by visible unknowns, assumptions, and proof boundaries | Are uncertainty and limits readable? |
| **Institutional-trust layer** | Long-term trust placed in governance methods, checklists, and repeated patterns | Is institutional reliance still reviewable? |
| **Continuity-trust layer** | Trust that survives handoff, compression, memory, freeze, and recovery | Can future operators reconstruct why trust was granted? |
| **Credibility-survivability layer** | Trust that can survive failure because limits and recovery posture were honest | Would credibility collapse if this conclusion fails? |

These layers are descriptive methodology. They do not create automated trust measurement or runtime enforcement.

---

## 2. Evidence-Backed Trust Layer

**Definition:** trust that is grounded in named, reviewable evidence.

Evidence-backed trust requires:

- visible source or artifact basis;
- verification evidence from QA confidence governance;
- reasoning visibility for conclusions;
- source lineage when authority matters;
- proof boundary for PASS, PARTIAL, FAIL, STOP, HITL, or SAFE UNKNOWN;
- explicit distinction between observed, inferred, assumed, and unknown.

**Credibility rule:** trust cannot exceed evidence. A polished report with weak evidence remains weakly credible.

---

## 3. Rendered-Confidence Layer

**Definition:** the confidence perceived by operators from tone, structure, formatting, report length, assertiveness, and professional presentation.

Rendered confidence is useful when it improves readability. It becomes dangerous when it inflates perceived reliability.

Review signals:

- Does confident language match evidence?
- Does report length add credibility signal or create trust theater?
- Are partials and SAFE UNKNOWN visible, or visually buried?
- Does a polished summary make uncertainty feel resolved?
- Does "professional" wording imply a stronger reliability posture than the checks support?

**Credibility rule:** rendered confidence must be subordinate to evidence-backed trust.

---

## 4. Escalation-Confidence Layer

**Definition:** trust shaped by whether authority boundaries, stop conditions, contradiction handling, and human escalation are visible.

Escalation-confidence protects:

- bounded autonomy;
- HITL-required and HITL-recommended decisions;
- contradiction escalation;
- approval and waiver visibility;
- continuation-with-disclosure boundaries;
- stop conditions where trust would be unsafe.

**Credibility rule:** when authority is unclear, escalation honesty is more credible than confident continuation.

---

## 5. Calibrated-Uncertainty Layer

**Definition:** credibility preserved by showing uncertainty in proportion to its consequence.

Calibrated uncertainty includes:

- SAFE UNKNOWN for missing evidence;
- explicit assumptions when they affect conclusions;
- inferred validation labels;
- partial validation boundaries;
- unresolved source, device, interaction, state, accessibility, or recovery gaps;
- uncertainty impact on freeze, delivery, trust, and escalation.

**Credibility rule:** uncertainty visibility does not weaken governance credibility; hidden uncertainty does.

---

## 6. Institutional-Trust Layer

**Definition:** trust placed in Website Factory governance because it has reusable methods, checklists, taxonomies, and prior lessons.

Institutional trust is useful when it remains reviewable. It drifts when operators believe governance because it is established, long, dense, or mature-looking.

Review signals:

- Does the governance layer explain its limits?
- Are repeated patterns treated as evidence or as prompts for review?
- Is prior trust revalidated in the current context?
- Are checklists used for decision value, not institutional ritual?
- Can a human challenge the method without appearing to challenge "the system"?

**Credibility rule:** institutional trust must remain inspectable, bounded, and reversible.

---

## 7. Continuity-Trust Layer

**Definition:** trust that survives across sessions because rationale, evidence, uncertainty, and decisions remain reconstructable.

Continuity trust depends on:

- report readability;
- checkpoint and freeze-state clarity;
- context survivability;
- organizational memory with scope boundaries;
- recovery and rollback traceability;
- cross-layer links that remain navigable.

**Credibility rule:** if future operators cannot reconstruct why trust was granted, credibility continuity is weak.

---

## 8. Credibility-Survivability Layer

**Definition:** the ability of governance credibility to survive error, partial failure, contradiction, rollback, or later discovery of missing evidence.

Credibility survivability improves when reports:

- avoid absolute reliability claims;
- disclose proof boundaries before failure;
- name unknowns and deferred checks;
- keep escalation status visible;
- distinguish evidence-backed trust from institutional trust;
- explain recovery and revalidation needs.

Credibility collapses when a system sounded certain, hid uncertainty, claimed maturity, and then failed in an unacknowledged proof gap.

**Credibility rule:** overconfidence creates brittle trust; calibrated uncertainty creates survivable trust.

---

## 9. Trust Calibration Controls

Use these controls before PASS, freeze, delivery-readiness, or strong recommendation language:

| Control | Required review |
|---------|-----------------|
| **Trust calibration** | Does trust match evidence, uncertainty, and consequence? |
| **Reliability disclosure** | Is the reliability basis named and scoped? |
| **Confidence proportionality** | Does confidence language match verification strength? |
| **Explainable trust** | Can a future operator see why trust is being requested? |
| **Sustainable credibility** | Would repeated use of this trust posture remain believable? |
| **Trust-preserving escalation** | Does escalation protect credibility when authority or evidence is insufficient? |

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Evidence-backed trust cannot be established | Trust would depend on impression, not proof. |
| Rendered confidence may exceed evidence | Presentation may inflate perceived reliability. |
| Escalation confidence is unclear | Cannot tell whether continuation is authorized. |
| Uncertainty is not calibrated | Unknowns may be hidden or underweighted. |
| Institutional trust is unreviewed | Governance reputation may be substituting for current evidence. |
| Continuity trust is weak | Future operators cannot reconstruct the trust basis. |
| Credibility survivability is unproven | Failure could expose hidden overconfidence and collapse trust. |

**Action:** identify the weak layer, narrow the trust claim, disclose missing evidence, and route to `TRUST CALIBRATION FINDINGS`, HITL, or SAFE UNKNOWN.

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial governance credibility model - evidence-backed trust, rendered confidence, escalation confidence, calibrated uncertainty, institutional trust, continuity trust, credibility survivability, and trust calibration controls; documentation only. |
