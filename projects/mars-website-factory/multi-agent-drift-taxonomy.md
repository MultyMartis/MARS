# MARS Website Factory - Multi-Agent Drift Taxonomy

**Status:** **documented** - Website Factory vocabulary for multi-agent coordination drift.  
**Not:** automated drift detector, runtime consensus engine, policy enforcement system, or universal multi-agent law.

**Parent layer:** [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md).  
**Responsibility model:** [agent-responsibility-boundary-model.md](agent-responsibility-boundary-model.md).  
**Related taxonomies:** [qa-drift-taxonomy.md](qa-drift-taxonomy.md), [escalation-drift-taxonomy.md](escalation-drift-taxonomy.md), [implementation-drift-taxonomy.md](implementation-drift-taxonomy.md), [source-ambiguity-taxonomy.md](source-ambiguity-taxonomy.md).

---

## 1. Purpose

This taxonomy gives Website Factory operators named failure patterns for multi-agent frontend work.

It exists because agent chains can amplify:

- assumptions;
- ambiguity;
- hallucinations;
- fake confidence;
- fake consensus;
- unresolved responsibility gaps.

Multiple agreeing agents do **not** equal truth. Agreement is only useful when the roles are independent enough, the evidence is visible, and authority boundaries are intact.

---

## 2. Drift Summary

| Drift pattern | Short definition |
|---------------|------------------|
| **Reviewer/executor collapse** | The same narrative both builds and "reviews" without independent challenge. |
| **Validator contamination** | Validation inherits executor or reviewer assumptions as evidence. |
| **Authority overlap** | Several roles act as if they can decide the same authority-sensitive issue. |
| **Chain hallucination amplification** | A false claim gains confidence as it passes through summaries or agents. |
| **Assumption propagation** | A guess from one role becomes unstated premise for downstream work. |
| **Orchestration ambiguity** | The chain has steps but no clear authority, owner, stop condition, or handoff rule. |
| **Duplicate ownership** | Multiple roles appear to own the same decision, so none is accountable. |
| **Unresolved responsibility gap** | A material decision, defect, unknown, or escalation has no owner. |
| **Escalation orphaning** | An escalation is identified but no role carries it to resolution. |
| **Circular validation** | QA cites outputs from the same chain as proof of the chain. |
| **Feedback-loop contamination** | Later agents optimize for previous agent conclusions instead of source/evidence. |
| **Fake consensus** | Multiple agreeing outputs are treated as truth without evidence or independence. |
| **Responsibility diffusion** | Ownership dissolves into "the agents", "the workflow", or "the chain". |

---

## 3. Detailed Patterns

### 3.1 Reviewer/Executor Collapse

**Definition:** Implementation and review collapse into one self-confirming responsibility.

**Symptoms:**

- Review restates what the executor intended.
- No independent source or evidence challenge is visible.
- Self-review is reported as if it were independent QA.

**Risk:** defects and assumptions survive because review has no separate authority or evidence posture.

**Governance response:** disclose non-independent review, seek independent review when material, or downgrade confidence.

### 3.2 Validator Contamination

**Definition:** Validator output depends on executor/reviewer assumptions instead of independent evidence.

**Symptoms:**

- Validation cites "implemented as planned" as proof.
- Inferred assumptions become PASS language.
- Evidence boundaries are missing or copied from executor summary.

**Risk:** validation becomes narrative confirmation rather than QA confidence governance.

**Governance response:** re-run validation from source/evidence, mark PARTIAL, or record `MULTI-AGENT FINDINGS`.

### 3.3 Authority Overlap

**Definition:** Several roles act as if they can resolve source priority, approval, waiver, or escalation decisions.

**Symptoms:**

- Executor chooses between contradictory sources.
- Reviewer overrides project pack authority.
- Validator approves waiver because the chain agrees.

**Risk:** human-owned or source-owned decisions are replaced by coordination momentum.

**Governance response:** route through [decision-boundary-model.md](decision-boundary-model.md) and [human-escalation-governance.md](human-escalation-governance.md).

### 3.4 Chain Hallucination Amplification

**Definition:** A false or weakly supported claim becomes stronger as it is repeated by downstream agents.

**Symptoms:**

- "Assumed" becomes "inferred", then "verified".
- A missing source becomes "confirmed by prior pass".
- Later summaries omit uncertainty.

**Risk:** multi-agent workflow produces polished false confidence.

**Governance response:** restore original evidence level, name the propagation point, and block PASS/freeze claims that exceed evidence.

### 3.5 Assumption Propagation

**Definition:** A practical guess moves downstream without being labeled as an assumption.

**Symptoms:**

- Downstream role treats approximation as source authority.
- Missing mobile state becomes "responsive intent".
- Inferred CTA role becomes business meaning.

**Risk:** hidden assumptions accumulate into unapproved redesign or fake authority.

**Governance response:** return to observed/inferred/assumed/unknown classification and assign assumption owner.

### 3.6 Orchestration Ambiguity

**Definition:** The sequence of roles is known, but responsibility, authority, and stop conditions are unclear.

**Symptoms:**

- "Agent A then B then C" exists without owner map.
- No role owns contradiction or escalation.
- Orchestrator coordinates output but not authority.

**Risk:** sequential execution is mistaken for governed coordination.

**Governance response:** add role map, authority boundary, handoff owner, escalation route, and stop condition.

### 3.7 Duplicate Ownership

**Definition:** Two or more roles are listed as owners of the same decision without priority.

**Symptoms:**

- Both reviewer and validator claim final QA truth.
- Several roles can "approve" a deferral.
- Escalation owner is duplicated but no one acts.

**Risk:** accountability disappears because ownership looks covered.

**Governance response:** assign one accountable owner and list supporting roles separately.

### 3.8 Unresolved Responsibility Gap

**Definition:** No role owns a material decision, defect, unknown, waiver, or contradiction.

**Symptoms:**

- Reports name the issue but not the next owner.
- SAFE UNKNOWN has no resolver.
- Freeze proceeds with "to be decided" but no authority.

**Risk:** the gap becomes hidden debt and future agents treat it as resolved.

**Governance response:** block or escalate until owner and resolver are named.

### 3.9 Escalation Orphaning

**Definition:** A role identifies a need for escalation, but the escalation is not carried forward.

**Symptoms:**

- Earlier note says HITL required; final report omits it.
- Contradiction appears in source read but disappears in QA.
- Escalation is assigned to "operator" without owner.

**Risk:** human-required decisions vanish during handoff.

**Governance response:** restore escalation state and route through human escalation governance.

### 3.10 Circular Validation

**Definition:** Validation proves the chain by citing chain outputs rather than independent evidence.

**Symptoms:**

- QA says "reviewer confirmed" while reviewer only read executor summary.
- Consensus is used as proof.
- Build/report text is treated as source evidence.

**Risk:** the workflow validates itself.

**Governance response:** require source-level, rendered, build-level, direct interaction, or explicit evidence boundary per QA confidence governance.

### 3.11 Feedback-Loop Contamination

**Definition:** A downstream role optimizes for agreement with previous roles rather than evidence.

**Symptoms:**

- Reviewer softens findings to align with implementation plan.
- Validator checks whether output matches report, not source.
- Orchestrator reframes blockers as deferrals to keep flow moving.

**Risk:** disagreement is suppressed and contradictions lose survivability.

**Governance response:** preserve disagreement and record independent finding scope.

### 3.12 Fake Consensus

**Definition:** Multiple outputs agree, but independence, evidence, or authority is insufficient.

**Symptoms:**

- "All agents agree" appears without evidence table.
- Same prompt/source bias affects every role.
- No role was allowed to contradict the chain.

**Risk:** agreement becomes confidence theater.

**Governance response:** state consensus is non-proof; require evidence and authority boundary review.

### 3.13 Responsibility Diffusion

**Definition:** Accountability dissolves into the collective chain.

**Symptoms:**

- Report says "we decided" without owner.
- Defects are attributed to workflow, not role boundary.
- No owner can reopen, fix, or escalate.

**Risk:** future operators cannot trace responsibility or safely continue.

**Governance response:** name role ownership for execution, review, validation, escalation, and HITL decisions.

---

## 4. Severity Guide

| Severity | Use when |
|----------|----------|
| **Low** | Drift is local, reversible, disclosed, and does not affect authority, freeze, or PASS confidence. |
| **Medium** | Drift affects review independence, evidence strength, handoff clarity, or assumption visibility but has a clear resolver. |
| **High** | Drift affects source authority, HITL boundary, contradiction resolution, freeze readiness, delivery confidence, or material business/design meaning. |
| **Blocking** | Drift hides approval, orphaned escalation, unresolved contradiction, fake validation, or responsibility gap required before continuation. |

---

## 5. Reporting Labels

Use these labels in `MULTI-AGENT FINDINGS`:

- `role-boundary-risk`
- `review-independence-risk`
- `validator-contamination-risk`
- `authority-overlap-risk`
- `assumption-propagation-risk`
- `chain-hallucination-risk`
- `orchestration-ambiguity-risk`
- `responsibility-gap-risk`
- `escalation-orphaning-risk`
- `circular-validation-risk`
- `fake-consensus-risk`
- `responsibility-diffusion-risk`

---

## 6. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Unknown | Why it matters |
|---------|----------------|
| Whether review was independent | Cannot use review as independent confidence support. |
| Whether validator saw source/evidence | Cannot claim validator integrity. |
| Which role owns escalation | Escalation may be orphaned. |
| Whether downstream role inherited assumptions | Chain confidence may be contaminated. |
| Whether contradiction was resolved or dropped | PASS/freeze may hide unresolved conflict. |
| Whether agreement was independent | Consensus may be fake. |

---

## 7. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial multi-agent drift taxonomy - reviewer/executor collapse, validator contamination, authority overlap, chain hallucination amplification, assumption propagation, orchestration ambiguity, duplicate ownership, responsibility gaps, escalation orphaning, circular validation, feedback-loop contamination, fake consensus, and responsibility diffusion. |
