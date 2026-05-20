# Context-Sensitive Discipline Model

**Status:** **documented** - Website Factory model for human-supervised governance-depth selection.  
**Not:** automated process selection, runtime policy routing, universal rigor law, autonomous governance adaptation, or perfect scaling guarantee.

**Parent layer:** [adaptive-governance.md](adaptive-governance.md).  
**Companion taxonomy:** [adaptive-drift-taxonomy.md](adaptive-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/adaptive-governance-checklist.md`](../../agents/mars-forge/adaptive-governance-checklist.md).

---

## 1. Purpose

This model gives Website Factory operators a shared vocabulary for choosing governance depth.

It exists because a frontend task may be:

- low-risk and reversible;
- ordinary but production-facing;
- source-ambiguous or evidence-limited;
- high-criticality for freeze, delivery, accessibility, business meaning, or project identity;
- escalation-heavy because authority is unclear;
- continuity-sensitive because handoff, recovery, compression, or long-term drift is at stake.

The model does not decide automatically. It makes the human selection explainable.

---

## 2. Discipline Layers

| Layer | When it fits | Governance depth |
|-------|--------------|------------------|
| **Lightweight-governance layer** | Local, reversible, well-sourced, low-risk edits with narrow blast radius. | Short source check, scoped change, minimal QA evidence, concise report note, no full checklist unless risk appears. |
| **Operational-standard layer** | Normal frontend section or component work with known source, stable scope, and ordinary production risk. | Forge phase discipline, relevant overlay QA, foundation QA when in scope, scoped PASS/PARTIAL/FAIL boundaries. |
| **Elevated-risk layer** | Source ambiguity, responsive uncertainty, interaction/state complexity, accessibility implications, shared selectors, or nontrivial regression risk. | Focused specialist checklists, stronger evidence, explicit unknowns, risk weighting, possible HITL recommendation. |
| **High-criticality layer** | Freeze, delivery, business meaning, CTA/proof hierarchy, source authority, project identity, accessibility trust, or release confidence may be damaged. | Full relevant governance depth, high evidence discipline, explicit blockers/deferrals, strong survivability review, HITL where authority requires it. |
| **Escalation-heavy layer** | Contradictory sources, missing approvals, authority ambiguity, assumption chains, or human-owned decisions. | Human escalation governance, decision-boundary classification, stop conditions, HITL-required or blocked states when needed. |
| **Continuity-sensitive layer** | Long session, handoff, compressed context, recovery, freeze-state restoration, cross-session edits, or multi-agent coordination affects trust. | Workflow, context, temporal, recovery, provenance, and coordination checks focused on state survivability. |
| **Adaptive-review layer** | Context changes during work or findings reveal that original depth is too light or too heavy. | Reassess governance depth, document why scaling changed, prune unnecessary depth or add missing safeguards. |

---

## 3. Governance Scaling

Governance scaling is the human-supervised act of increasing or decreasing process depth as the operational context changes.

Scale up when:

- source authority is missing, ambiguous, stale, or contradictory;
- the work affects freeze, delivery, release confidence, or rollback trust;
- user-facing meaning, CTA priority, proof hierarchy, accessibility trust, or interaction/state behavior is affected;
- the change touches shared CSS, tokens, includes, breakpoints, or JS ownership;
- multiple governance findings interact and need prioritization;
- handoff, compressed context, or recovery state makes continuity fragile;
- the operator cannot explain why lightweight process is enough.

Scale down when:

- the work is local, reversible, and low-impact;
- source authority is clear;
- evidence needed for confidence is narrow;
- full checklist depth would repeat existing evidence without improving decisions;
- escalation-only or optional-depth treatment is sufficient;
- the report would become less readable from unnecessary process volume.

---

## 4. Proportional QA

QA should be proportional to the risk and evidence need.

| QA depth | Appropriate when | Example outcome |
|----------|------------------|-----------------|
| **Targeted QA** | A small local change needs one or two directly relevant checks. | `PASS - source-level selector scope checked; rendered state not in scope.` |
| **Standard QA** | A normal section slice needs Forge overlay plus foundation checks in scope. | `PARTIAL - responsive checked at named widths; tablet remains SAFE UNKNOWN.` |
| **Focused elevated QA** | A specific risk needs specialist review. | `RESPONSIVE INTENT FINDINGS` or `QA CONFIDENCE FINDINGS` added without running every unrelated layer. |
| **Full relevant QA** | Critical path, freeze, delivery, or high uncertainty requires broad evidence. | Multiple findings reported with risk weighting and confidence boundaries. |
| **Escalation QA** | QA cannot resolve authority, contradiction, approval, or meaning. | `HUMAN ESCALATION FINDINGS` and HITL classification. |

**Rule:** proportional QA is not "less QA." It is QA whose depth, evidence, and report weight match the work.

---

## 5. Adaptive Escalation

Escalation depth should follow authority and consequence.

| Escalation level | Use when |
|------------------|----------|
| **No escalation** | Source is clear, risk is low, decision is reversible, and evidence supports the claim. |
| **Disclosure only** | A minor unknown exists but does not affect material meaning, freeze, delivery, or trust. |
| **HITL recommended** | Human input would reduce risk but continuation with disclosure remains safe. |
| **HITL required** | Human-owned decision, approval, source priority, business meaning, accessibility trust, or freeze/release decision is involved. |
| **Blocked** | Contradiction, missing authority, or evidence gap makes continuation unsafe. |

Escalation is not a punishment for uncertainty. It is a proportional response to authority boundaries.

---

## 6. Process-Depth Allocation

When allocating process depth, consider:

- **Scope:** one selector, one component, one section, page-wide, cross-page, release/freeze.
- **Blast radius:** local, adjacent section, shared token, global SCSS/JS, project identity.
- **Reversibility:** easy revert, contained correction, structural rewrite, human decision, delivery blocker.
- **Evidence:** direct, rendered, build-level, source-level, inferred, assumed, unknown.
- **Authority:** source-owned, governance-owned, operator-owned, human-owned, contradictory.
- **Criticality:** cosmetic, operational, strategic, accessibility, continuity, delivery.
- **Continuity:** current-session only, handoff-sensitive, compressed-context-sensitive, recovery-sensitive.

---

## 7. Contextual Rigor

Contextual rigor means:

- low-risk work can use lightweight governance without being undisciplined;
- standard work should follow ordinary Forge phase and QA discipline;
- elevated-risk work should use focused specialist depth;
- high-criticality work should not hide behind minimal process;
- escalation-heavy work should stop or route authority to humans;
- continuity-sensitive work should preserve checkpoint, freeze, and handoff survivability;
- adaptive-review should adjust the process when evidence changes.

The rigor is contextual, but the honesty boundary is constant.

---

## 8. Survivability Balancing

Adaptive governance balances two survivability risks:

| Risk | Failure mode |
|------|--------------|
| **Too little governance** | Critical ambiguity, source drift, freeze erosion, accessibility trust loss, or delivery risk goes under-protected. |
| **Too much governance** | Operators drown in process, reports lose signal, simple work slows, and future continuation becomes harder. |

The goal is not maximum discipline. The goal is enough discipline to preserve quality, honesty, authority boundaries, and future operability for the current context.

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when the appropriate discipline layer cannot be chosen from available context.

**Action:** name the competing layers, state what evidence would resolve the choice, and select the safest provisional route: lightweight-safe, standard-safe, elevated-review-needed, HITL-needed, blocked, or deferred.

---

## 10. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial context-sensitive discipline model - lightweight, standard, elevated-risk, high-criticality, escalation-heavy, continuity-sensitive, and adaptive-review layers; documentation only. |
