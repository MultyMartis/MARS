# Prioritization Drift Taxonomy - Website Factory

**Status:** **documented** - taxonomy for human-supervised governance prioritization review only.  
**Not:** automated drift detector, scoring system, universal severity standard, or runtime enforcement.

**Parent layer:** [governance-prioritization.md](governance-prioritization.md).  
**Risk model:** [risk-weighting-model.md](risk-weighting-model.md).  
**Forge checklist:** [`../../agents/mars-forge/risk-weighting-checklist.md`](../../agents/mars-forge/risk-weighting-checklist.md).

---

## 1. Purpose

This taxonomy names the ways frontend governance can lose priority clarity even when individual findings are valid.

A governance report can be long, thorough, careful, and category-rich while still failing if the reviewer cannot tell which risks are critical, which are operational, which are minor, and which should only be escalated under specific thresholds.

---

## 2. Drift Patterns

| Drift pattern | Description | Risk |
|---------------|-------------|------|
| **Equal-priority overload** | Every finding is presented with similar weight. | Critical issues become hard to distinguish from minor observations. |
| **Minor-drift obsession** | Review attention fixates on small visual, copy, spacing, icon, or polish mismatches. | Operational, strategic, source, or freeze risks are delayed or hidden. |
| **Critical-risk dilution** | Critical findings are buried inside long lists of ordinary findings. | Reviewers miss blockers or underestimate required action. |
| **Severity inflation** | Low-risk or speculative issues are labeled as high severity. | Severity language loses trust and escalation becomes noisy. |
| **Governance noise escalation** | Report volume grows through duplicated, low-value, or non-actionable warnings. | Signal-to-noise collapses and review fatigue rises. |
| **Low-value escalation** | HITL is requested for issues that do not require human authority. | Human attention is spent on decisions the operator could safely handle. |
| **Review imbalance** | Some categories receive deep attention while higher-risk categories receive shallow treatment. | QA coverage appears broad but operational risk remains unresolved. |
| **Cosmetic-over-critical focus** | Polish defects lead the report while critical path risks appear later or without emphasis. | Freeze or delivery decisions may be made from the wrong priority frame. |
| **Signal-to-noise collapse** | Useful findings are overwhelmed by volume, repetition, or vague warnings. | The report becomes harder to act on than the underlying issue. |
| **False criticality** | A finding is framed as urgent without impact, evidence, or authority consequence. | Operators become desensitized to real critical risk. |
| **Disproportionate QA allocation** | QA effort is spent where risk is low while high-consequence areas remain thinly checked. | QA looks complete but does not protect the project. |
| **Escalation fatigue** | Frequent low-value escalations reduce attention to true HITL conditions. | Human review becomes slower, weaker, or ignored. |
| **Operational focus erosion** | The operator loses the next safe action because governance produces too many competing priorities. | Execution survivability declines despite more documentation. |

---

## 3. Anti-Patterns

Forbidden prioritization drift:

| Anti-pattern | Why it is forbidden |
|--------------|---------------------|
| **Treating all findings equally** | Removes the distinction between blocker, risk, note, and cosmetic observation. |
| **Cosmetic obsession** | Lets polish consume attention before operational, strategic, or authority risks are handled. |
| **False criticality inflation** | Makes every warning sound severe until severity becomes meaningless. |
| **Escalation spam** | Sends low-value issues to HITL and weakens real escalation paths. |
| **Governance-noise generation** | Adds warnings because more reporting looks safer, not because action value increases. |
| **Report flooding** | Produces so much output that priority, evidence, and next action become unclear. |
| **Review exhaustion** | Overloads reviewers until meaningful judgment declines. |
| **Severity blindness** | The report no longer shows which issues are critical, operational, minor, or informational. |
| **Checklist quantity over operational meaning** | Completion volume replaces risk-aware review. |
| **"More warnings = safer system"** | Mistakes warning count for protection. |

---

## 4. Diagnostic Questions

Use these questions when prioritization drift is suspected:

- Can a reviewer name the top three risks in under one minute?
- Are critical risks visually or structurally distinct from minor findings?
- Do severity labels explain consequence, not just category?
- Are HITL requests tied to authority, contradiction, or material uncertainty?
- Are minor findings grouped or deferred when they do not affect safe progress?
- Does the report preserve signal-to-noise ratio?
- Are cosmetic findings prevented from displacing operational, strategic, or continuity risks?
- Does the report explain what must happen before freeze?
- Does QA depth match actual risk instead of checklist availability?
- Is focus being spent where consequence is highest?

---

## 5. Drift Outcomes

| Outcome | What happens |
|---------|--------------|
| **Critical risk hidden** | The most dangerous issue exists but is not prominent enough to drive action. |
| **Escalation weakened** | Human review gets too many low-value requests and misses real authority boundaries. |
| **QA confidence distorted** | A large report creates confidence even when priority weighting is poor. |
| **Governance minimalism undermined** | Complexity may be reduced, but the remaining findings still lack priority. |
| **Operational attention depleted** | Reviewers spend limited attention on low-consequence material. |
| **Freeze decision degraded** | PASS, PARTIAL, FAIL, SAFE UNKNOWN, HITL, or STOP cannot be chosen reliably. |

---

## 6. Mitigation

When drift is present:

- lead with critical-risk, operational-risk, continuity-risk, and strategic-risk items;
- group cosmetic/minor and informational findings;
- demote speculative issues unless consequence justifies escalation;
- separate "must fix before freeze" from "defer," "monitor," and "informational";
- state why escalation is relevant or not relevant;
- preserve a short critical-path summary before detailed evidence;
- record **RISK WEIGHTING FINDINGS** when prioritization affects review quality.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- the report contains many findings but priority cannot be read;
- a finding might be critical but evidence or consequence is unclear;
- escalation threshold cannot be established;
- review allocation appears imbalanced but impact is not proven;
- cosmetic and operational risks compete without a clear decision rule.

**Action:** use [risk-weighting-model.md](risk-weighting-model.md) to assign provisional layers and name the evidence, source, or HITL decision needed to resolve priority.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial prioritization drift taxonomy - equal-priority overload, minor-drift obsession, critical-risk dilution, severity inflation, governance noise, review imbalance, escalation fatigue, and operational focus erosion. |
