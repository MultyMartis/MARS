# MARS Website Factory — Escalation Drift Taxonomy

**Status:** **documented** — Website Factory escalation drift vocabulary for human-supervised frontend governance only.  
**Not:** automated drift detector, runtime enforcement, universal escalation law, or autonomous approval system.

**Parent layer:** [human-escalation-governance.md](human-escalation-governance.md).  
**Decision model:** [decision-boundary-model.md](decision-boundary-model.md).  
**Forge checklist:** [`../../agents/mars-forge/human-escalation-checklist.md`](../../agents/mars-forge/human-escalation-checklist.md).

---

## 1. Purpose

This taxonomy names the drift patterns that appear when AI-assisted frontend work continues past the edge of its authority.

It helps operators distinguish:

- uncertainty from hidden assumption;
- SAFE UNKNOWN from required stop;
- inference from approval;
- implementation progress from decision authority;
- confidence from human ownership.

---

## 2. Taxonomy Summary

| Drift pattern | Symptom | Governance response |
|---------------|---------|---------------------|
| **Silent continuation** | Work proceeds through known ambiguity without report disclosure. | Classify boundary; record finding; stop if material. |
| **Fake certainty escalation** | The report uses strong confidence language to avoid escalation. | Downgrade confidence; apply QA confidence and decision boundary model. |
| **Assumption chain drift** | Several small guesses combine into a major unapproved choice. | Count assumptions as a risk chain; HITL-recommended or HITL-required. |
| **Unresolved contradiction continuation** | Conflicting sources are silently reconciled by taste. | Block by contradiction until priority or human decision exists. |
| **Hidden HITL dependency** | A human-owned decision is embedded in implementation as if already decided. | Surface decision owner; require HITL if authority-sensitive. |
| **Authority confusion** | Source, prompt, legacy note, prior session, and implementation default are treated as equal authority. | Re-establish source priority and decision owner. |
| **Escalation avoidance** | The agent chooses a workaround to avoid asking for human input. | Record stop condition; distinguish workaround from authorization. |
| **Unsafe autonomy** | AI makes a business, approval, release, structural, or source-priority decision. | HITL-required; revert to bounded autonomy scope. |
| **Implementation momentum bias** | Existing code progress pressures continuation despite unresolved risk. | Pause; reclassify decision boundary before proceeding. |
| **Contradiction minimization** | Conflict is described as minor without evidence that it is low-impact. | Name contradiction, scope, and required resolver. |
| **Ambiguity normalization** | Repeated unknowns become accepted as normal implementation input. | Keep unknowns visible; escalate if material or cumulative. |
| **Escalation fatigue** | The system stops reporting repeated risk because findings feel repetitive. | Preserve traceability; summarize repeated issues without hiding them. |
| **Invisible stop-condition drift** | Stop conditions exist but are not recognized until after implementation/freeze. | Add stop-condition QA before PASS/freeze. |

---

## 3. Pattern Details

### 3.1 Silent Continuation

**Definition:** implementation proceeds while a material ambiguity, unknown, or authority gap is known but unreported.

**Common cues:**

- "Proceeding with best guess" without boundary classification.
- Missing mobile source but broad responsive PASS.
- Ambiguous visual grouping implemented as definitive DOM.

**Required response:** record `HUMAN ESCALATION FINDINGS`; classify as autonomous-with-disclosure, HITL-recommended, HITL-required, or blocked.

### 3.2 Fake Certainty Escalation

**Definition:** confidence wording is inflated to avoid admitting that a human decision or stop condition exists.

**Common cues:**

- "Clearly intended" where evidence is weak.
- "Fully verified" after source-only or screenshot-only review.
- "Approved" without approval record.

**Required response:** downgrade claim; apply [qa-confidence-governance.md](qa-confidence-governance.md) and [decision-boundary-model.md](decision-boundary-model.md).

### 3.3 Assumption Chain Drift

**Definition:** individually small assumptions stack into a decision that changes source meaning, layout role, business claim, or QA confidence.

**Common cues:**

- Assumed grouping + assumed copy role + assumed mobile order.
- Missing source path + inferred hierarchy + unverified responsive behavior.
- Visual approximation plus unapproved CTA weight change.

**Required response:** treat the chain as one higher-risk decision. Escalate when assumptions affect authority, meaning, approval, freeze, or confidence.

### 3.4 Unresolved Contradiction Continuation

**Definition:** conflicting sources or instructions are collapsed into one implementation without a priority rule.

**Common cues:**

- Active design and legacy PDF disagree.
- Section matrix and screenshot disagree on entity count.
- Prompt requests a change that violates project pack constraints.

**Required response:** classify as **blocked-by-contradiction** unless current priority rules resolve it.

### 3.5 Hidden HITL Dependency

**Definition:** implementation depends on a decision only a human can own, but the dependency is not surfaced.

**Common cues:**

- Copy rewrite, trust claim, pricing, legal phrase, service entity, or CTA meaning is changed "for clarity."
- Source priority is chosen without approval.
- Waiver is implied but not recorded.

**Required response:** mark HITL-required and name the decision owner.

### 3.6 Authority Confusion

**Definition:** the system treats all inputs as equal authority or lets lower-authority artifacts override active source.

**Common cues:**

- Archive mockup overrides active `design/v2` charter.
- Prior implementation defaults override screen-local intent.
- Foundation style overrides a current implementation pack without note.

**Required response:** re-anchor source priority; escalate unresolved priority conflict.

### 3.7 Escalation Avoidance

**Definition:** the system chooses a technical workaround to avoid stopping or asking for human authority.

**Common cues:**

- CSS patch hides a structural contradiction.
- Generic component chosen to avoid asking which behavior is intended.
- "Temporary" text or asset inserted without escalation.

**Required response:** separate workaround from authority; record unresolved decision or stop.

### 3.8 Unsafe Autonomy

**Definition:** AI acts beyond bounded autonomy by making a human-owned decision.

**Common cues:**

- Approving its own work.
- Declaring delivery readiness without HITL where required.
- Resolving business claim, offer, pricing, or legal copy.
- Reprioritizing source hierarchy.

**Required response:** stop; require HITL approval, waiver, or source update.

### 3.9 Implementation Momentum Bias

**Definition:** the fact that implementation is already underway becomes a reason to continue.

**Common cues:**

- "Most of it is already done."
- "Changing now would cost time."
- "We can fix later" without owner or checkpoint.

**Required response:** pause and classify boundary. Momentum is not authority.

### 3.10 Contradiction Minimization

**Definition:** conflict is described as harmless before impact is evaluated.

**Common cues:**

- "Small mismatch" involving CTA, section order, entity count, or source version.
- "Probably same intent" where artifacts differ.

**Required response:** name impacted decision and resolver. If unresolved, block by contradiction.

### 3.11 Ambiguity Normalization

**Definition:** repeated unknowns become treated as acceptable default input.

**Common cues:**

- Desktop-only source repeatedly used for full responsive intent.
- Missing states repeatedly filled with generic behavior.
- Ambiguous grouping repeatedly implemented without findings.

**Required response:** escalate recurring unknowns as a systemic HITL or source-pack gap.

### 3.12 Escalation Fatigue

**Definition:** repeated escalation findings are suppressed because they feel obvious or repetitive.

**Common cues:**

- "Same as before" replaces explicit boundary.
- Known gaps disappear from later reports.
- Deferred HITL is never re-raised.

**Required response:** summarize recurring findings, preserve unresolved decision list, and avoid fake closure.

### 3.13 Invisible Stop-Condition Drift

**Definition:** stop conditions are only recognized after code, QA, freeze, or delivery claims have already occurred.

**Common cues:**

- Contradiction found during final report.
- Approval boundary discovered after freeze.
- QA evidence gap found after PASS language.

**Required response:** add stop-condition QA before freeze; reopen if necessary.

---

## 4. Severity Guidance

| Severity | Meaning | Typical action |
|----------|---------|----------------|
| **Low** | Local, reversible, disclosed, no authority-sensitive impact. | Continue with disclosure. |
| **Medium** | Material confidence or interpretation risk; human decision useful but not always blocking. | HITL-recommended; continue only with explicit boundary. |
| **High** | Meaning, source priority, approval, structural regrouping, or business claim affected. | HITL-required. |
| **Blocking** | Contradiction or ambiguity prevents safe implementation or PASS/freeze. | Stop until resolved. |

---

## 5. Anti-Patterns Introduced

The following terms are forbidden drift vocabulary for reports and reviews:

- continuing through ambiguity;
- silent redesign assumptions;
- hidden decision substitution;
- pretending approval exists;
- escalation suppression;
- "probably intended" continuation;
- fake autonomous authority;
- contradiction minimization;
- assumption stacking;
- implementation inertia.

Use these names to make drift visible, not to create blame. The goal is decision survivability.

---

## 6. Triumph V2 Lessons Captured

Triumph V2 illustrates why escalation drift taxonomy is needed:

- Cross-version artifacts can create authority confusion unless active source priority is explicit.
- Visual ambiguity can become silent continuation when implementation pressure is high.
- Repeated missing mobile/state evidence can normalize unknowns unless findings stay visible.
- Equipment, service, CTA, and trust semantics can cross into human business authority quickly.
- QA PASS language can hide unresolved HITL dependency if confidence and approval are not separated.

These lessons are reusable Website Factory governance, not Triumph redesign instructions.

---

## 7. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial escalation drift taxonomy — silent continuation, fake certainty, assumption chains, contradiction continuation, hidden HITL dependency, authority confusion, unsafe autonomy, and stop-condition drift. |
