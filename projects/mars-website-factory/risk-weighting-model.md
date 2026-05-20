# Risk Weighting Model - Website Factory

**Status:** **documented** - human-supervised frontend governance prioritization model only.  
**Not:** scoring engine, automated risk classifier, universal severity system, or perfect prioritization method.

**Parent layer:** [governance-prioritization.md](governance-prioritization.md).  
**Drift taxonomy:** [prioritization-drift-taxonomy.md](prioritization-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/risk-weighting-checklist.md`](../../agents/mars-forge/risk-weighting-checklist.md).

---

## 1. Purpose

The Risk Weighting Model gives Website Factory operators a shared vocabulary for deciding how much attention, escalation, and report prominence a finding deserves.

It preserves:

- risk visibility;
- severity weighting;
- proportional review logic;
- escalation relevance;
- governance signal clarity;
- operational focus preservation.

It does not replace evidence, specialist governance, or human project authority.

---

## 2. Weighting Inputs

Use these inputs before assigning a risk layer:

| Input | Question |
|-------|----------|
| **Consequence** | What can be damaged: freeze, source authority, business intent, trust, delivery, continuity, implementation stability, or visual fidelity? |
| **Reversibility** | Can the issue be corrected locally, or does it require structural change, HITL, or rollback? |
| **Evidence strength** | Is the finding direct, rendered, source-level, build-level, inferred, assumed, or unknown? |
| **Scope / blast radius** | Does it affect one small detail, one section, a shared system, a frozen area, or delivery confidence? |
| **Timing** | Must it be handled before freeze, before delivery, before adjacent work, or only as future cleanup? |
| **Authority boundary** | Is human approval, source priority, waiver, or contradiction resolution required? |
| **Operational cost of noise** | Would reporting this at high priority hide more important risks? |

---

## 3. Risk Layers

| Layer | Meaning | Typical action |
|-------|---------|----------------|
| **Critical-risk layer** | Can block safe freeze, delivery, source authority, human approval, major business meaning, or trusted recovery. | Stop, fix before freeze, or HITL required. |
| **Operational-risk layer** | Can damage execution reliability, rebuild predictability, regression survivability, workflow continuity, or report trust. | Fix before freeze or disclose with scoped mitigation. |
| **Continuity-risk layer** | Can damage future handoff, compressed context, freeze-state memory, version lineage, rollback trust, or long-term survivability. | Record clearly, checkpoint, fix if current scope depends on it. |
| **Strategic-risk layer** | Can weaken business priority, conversion hierarchy, proof authority, stakeholder intent, or operational seriousness. | Strategic review, HITL when authority or priority is unclear. |
| **Cosmetic/minor-risk layer** | Affects polish, small visual mismatch, reversible detail, or low-blast-radius inconsistency. | Fix opportunistically, group, defer, or report as minor. |
| **Escalation-only layer** | Not always a defect; becomes material only when ambiguity, contradiction, authority, or approval boundary appears. | Escalate only when threshold is crossed. |
| **Informational layer** | Useful context with no immediate operational consequence. | Record briefly or omit from main findings when it adds noise. |

**Rule:** a finding can mention multiple dimensions, but the report should identify the dominant risk layer for action.

---

## 4. Prioritization Thresholds

| Threshold | Raises priority when |
|-----------|----------------------|
| **Freeze blocker** | The issue makes PASS, freeze, or handoff unsafe. |
| **Delivery blocker** | The issue affects release readiness, approval, export package trust, or delivery claim honesty. |
| **Human authority boundary** | AI cannot decide safely because approval, waiver, contradiction, or business decision ownership is missing. |
| **Critical evidence gap** | Evidence is missing for a claim with high consequence. |
| **Regression blast radius** | A change can affect frozen sections, shared selectors, global tokens, include graphs, or JS hooks. |
| **Strategic damage** | A local improvement weakens CTA role, proof hierarchy, business priority, or stakeholder intent. |
| **Continuity loss** | Future operators cannot reconstruct source, decision, checkpoint, freeze state, or recovery boundary. |
| **Noise overload** | Findings are too numerous or equal-weighted for reviewers to see critical risks. |

Lower priority when:

- impact is local, reversible, and low consequence;
- evidence is weak and the finding is speculative;
- the issue is cosmetic and does not affect intent, trust, accessibility, source authority, or freeze;
- the finding duplicates another clearer finding;
- full escalation would add noise without improving safety.

---

## 5. Escalation Relevance

Escalation is relevant when at least one of these is true:

- human approval or waiver is required;
- approved-looking sources conflict;
- severity cannot be resolved from available evidence;
- strategic priority, proof authority, CTA role, project identity, legal/compliance language, or delivery readiness is affected;
- an implementation change crosses from scoped fix into structure, source priority, or design interpretation;
- unresolved uncertainty would make PASS, freeze, or delivery claims dishonest.

Escalation is usually not relevant when:

- the issue is minor, reversible, and source-authorized;
- a scoped fix is obvious and within the operator's authority;
- a finding is informational and does not affect freeze, trust, strategy, continuity, or safety;
- the report can disclose a bounded low-risk unknown without blocking work.

---

## 6. Proportional Review Logic

| Finding type | Review depth |
|--------------|--------------|
| Critical-risk | Lead the report; resolve or escalate before freeze. |
| Operational-risk | Review before freeze when it affects current source, build, regression, or handoff. |
| Continuity-risk | Preserve traceability and checkpoint clarity; fix when future recovery depends on it. |
| Strategic-risk | Review with business-intent evidence; escalate when priority or authority is unclear. |
| Cosmetic/minor-risk | Group, defer, or fix only when cheap and non-disruptive. |
| Escalation-only | Keep dormant until ambiguity, contradiction, approval, or threshold appears. |
| Informational | Keep short; avoid flooding the findings section. |

**Rule:** proportional review is not lower quality. It is attention discipline.

---

## 7. REPORT Shape

Use this summary when many governance findings exist:

```text
RISK WEIGHTING FINDINGS - <scope>

Highest-risk items:
- <critical / operational / continuity / strategic risk and required action>

Risk layers:
- Critical-risk:
- Operational-risk:
- Continuity-risk:
- Strategic-risk:
- Cosmetic/minor-risk:
- Escalation-only:
- Informational:

Escalation relevance:
- <HITL required / HITL recommended / disclosure enough / no escalation>

Signal-to-noise note:
- <what was grouped, deferred, or demoted to preserve focus>

Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN | HITL REQUIRED | STOP
```

---

## 8. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- the dominant risk layer cannot be determined;
- consequence, reversibility, scope, or authority boundary is unclear;
- a finding might be critical but evidence is too weak to justify severity;
- many findings are present and the critical path cannot be identified;
- escalation relevance cannot be decided safely.

**Action:** keep the finding visible, state the provisional layer, and name the evidence or human decision needed to resolve weighting.

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial risk weighting model - critical, operational, continuity, strategic, cosmetic/minor, escalation-only, and informational layers; documentation only. |
