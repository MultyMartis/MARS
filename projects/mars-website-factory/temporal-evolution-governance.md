# MARS Website Factory - Temporal Evolution & Project Drift Governance

**Status:** **documented** - Website Factory long-term governance methodology for human-supervised frontend evolution.  
**Not:** autonomous maintenance AI, runtime drift engine, universal frontend lifecycle law, permanent architectural stability claim, or automatic freeze enforcement.

**Core principle:** frontend systems must preserve **continuity over time, governance durability, architectural readability, freeze-state traceability, controlled evolution, and identity survivability**.

**Companion documents:** [project-drift-survivability-model.md](project-drift-survivability-model.md), [evolution-drift-taxonomy.md](evolution-drift-taxonomy.md).  
**Related layers:** [implementation-reliability-governance.md](implementation-reliability-governance.md), [strategic-intent-governance.md](strategic-intent-governance.md), [knowledge-provenance-governance.md](knowledge-provenance-governance.md), [context-survivability-governance.md](context-survivability-governance.md), [failure-recovery-governance.md](failure-recovery-governance.md), [governance-minimalism.md](governance-minimalism.md), [qa-confidence-governance.md](qa-confidence-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [human-escalation-governance.md](human-escalation-governance.md), [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md), [operational-workflow-governance.md](operational-workflow-governance.md), [production-readiness-governance.md](production-readiness-governance.md), [organizational-memory-governance.md](organizational-memory-governance.md), [governance-evolution-governance.md](governance-evolution-governance.md).  
**Forge checklist:** [`../../agents/mars-forge/temporal-evolution-checklist.md`](../../agents/mars-forge/temporal-evolution-checklist.md).

---

## 1. Positioning

Temporal Evolution & Project Drift Governance sits above current correctness, presentational quality, one-time QA success, and local implementation reliability.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Long-term continuity, freeze-state integrity, architectural survivability, version lineage, drift explainability, and governance durability | Universal lifecycle law, permanent stability guarantees, or autonomous maintenance systems |
| Human-supervised checks for controlled evolution across future edits, patches, freezes, reviews, and handoffs | Background drift detection, runtime monitoring, telemetry, or automatic remediation |
| Drift vocabulary for gradual erosion, patch-history entropy, cumulative override pressure, governance fatigue, and identity drift | Redesigning Triumph or any other project |
| Forge reporting discipline for `TEMPORAL EVOLUTION FINDINGS` | A claim that Website Factory can keep projects stable forever |

The governance question is not "does this change pass now?"  
The governance question is: **can the project remain explainable, governable, and identity-preserving after many justified local changes over time?**

---

## 2. Canonical Definition

**Temporal evolution governance** is the discipline of preserving frontend system identity while allowing controlled change over time.

It protects:

- **Temporal continuity** - future operators can understand how the current state relates to earlier frozen states.
- **Project drift visibility** - slow, local, incremental erosion remains nameable and reviewable.
- **Freeze-state integrity** - frozen states stay traceable even when later changes are approved.
- **Governance survivability** - governance rules remain usable after long iteration, turnover, urgency, and fatigue.
- **Architectural readability** - structure remains understandable as an evolving system, not only as a current snapshot.
- **Version lineage** - current artifacts disclose what they supersede, inherit, diverge from, or invalidate.
- **Identity survivability** - local fixes, redesign pressure, modernization, and overrides do not silently mutate the system's approved identity.

A frontend can degrade **slowly, invisibly, and incrementally** while every local change still appears **justified, QA-passed, and visually acceptable**. This layer exists to make that risk visible before a project becomes historically ambiguous or architecturally unreadable.

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Temporal continuity** | The readable relationship between past frozen states, current state, and proposed future changes. |
| **Project drift** | Slow divergence from approved identity, architecture, source intent, or governance discipline through accumulated changes. |
| **Freeze-state integrity** | A frozen state remains traceable, respected, and explainable after later edits, exceptions, or reopenings. |
| **Governance survivability** | Governance remains practical and followed over time rather than abandoned under patch pressure, turnover, or fatigue. |
| **Architectural erosion** | Structure, ownership, dependencies, and rationale become less readable after repeated local edits. |
| **Iterative contamination** | New work inherits stale assumptions, overrides, local hacks, or previous drift as if they were active truth. |
| **Version lineage** | The visible chain between versions, freezes, supersedes, branches, rollbacks, and approved divergence. |
| **Cumulative override pressure** | Local exceptions stack over time until the normal system path is no longer trusted or readable. |
| **Continuity readability** | A future operator can explain why the project is in its current state without relying on memory. |
| **Patch-history entropy** | The history of fixes becomes a confusing source of behavior, authority, and risk. |
| **Identity drift** | The system still functions but no longer expresses the approved design, business, architectural, or governance identity. |
| **Long-term consistency** | Consistency across time, not only within the current screen or release. |
| **Drift survivability** | The project's ability to absorb change while keeping drift visible, bounded, and reversible where possible. |
| **Evolution traceability** | Material changes disclose what changed, why, what authority allowed it, and what earlier state it affects. |
| **Governance fatigue** | Operators gradually stop applying governance because exceptions, urgency, or checklist volume feel normal. |

---

## 4. Core Rules

- **Freeze states matter.** A frozen state is not a decorative label; it is a reference point for future traceability.
- **Continuity requires visibility.** If a change cannot explain what it inherits, supersedes, or diverges from, it weakens continuity.
- **Iterative changes accumulate risk.** Small justified edits can create large drift when their cumulative effect is unreviewed.
- **Local improvements may damage identity.** Better local polish, modernization, or patching can still mutate system identity.
- **Governance must survive time.** A rule that only works during the first build is not enough for long-lived frontend systems.
- **Drift should remain explainable.** If drift is accepted, its source, scope, rationale, and future risk should be visible.
- **Architectural readability matters.** A project that works but cannot be understood is not stable over time.
- **Long-term consistency requires checkpoints.** Continuity checkpoints should review accumulation, not only latest diffs.
- **Patch history is evidence, not authority.** Past patches do not become canonical merely because they survived.
- **Modernization requires lineage.** Updating patterns, libraries, design language, or code style must preserve identity and traceability.

---

## 5. Temporal Review Questions

Before accepting an evolution step, ask:

- What frozen state, version, or approved baseline does this change relate to?
- Does the change preserve, supersede, branch from, or intentionally diverge from that baseline?
- Is the divergence documented enough for a future operator to understand it?
- Does the change add override pressure, patch-history entropy, or hidden dependency?
- Does local polish preserve the approved design, business, source, and architectural identity?
- Does QA evidence cover only current correctness, or also freeze impact and continuity risk?
- Are previous temporary exceptions still temporary, normalized, accepted risk, or forgotten drift?
- Does this change make future governance easier or harder to apply?

---

## 6. Continuity Checkpoints

Continuity checkpoints are human-supervised review moments. They do not require automation.

Use them when:

- a frozen section is reopened;
- an adjacent edit touches frozen neighbors;
- a local override becomes repeated;
- modernization affects tokens, layout, typography, components, dependencies, or conventions;
- a project changes hands between operators or sessions;
- QA keeps passing while architectural readability declines;
- a project accumulates many small fixes after initial freeze;
- a source, strategy, design, or implementation pack is superseded.

Checkpoint output should name:

- baseline or freeze reference;
- divergence summary;
- lineage impact;
- drift patterns;
- affected governance layers;
- required HITL, follow-up, or acceptance with monitored risk.

---

## 7. Anti-Patterns

Forbidden drift vocabulary:

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Endless patch evolution** | The project changes only by local fixes until no one can explain the whole. |
| **Modernization without continuity** | New patterns are introduced without preserving source identity or version lineage. |
| **Silent redesign accumulation** | Many small visual improvements gradually become an unapproved redesign. |
| **Historical lineage loss** | Current state cannot be traced to approved source, freeze, or decision history. |
| **Override stacking over years** | Exceptions become the normal operating path. |
| **Uncontrolled local evolution** | Section-level changes mutate global identity without review. |
| **Governance abandonment** | Checklists, freeze semantics, provenance, QA confidence, and escalation disappear under urgency. |
| **Iterative fragmentation** | Repeated changes create divergent patterns between sections, breakpoints, or components. |
| **Small-change accumulation blindness** | Each edit is accepted alone, but the accumulated result is never reviewed. |
| **Freeze-state erosion** | Frozen scope is repeatedly reopened, bypassed, or reinterpreted without traceability. |

Use [evolution-drift-taxonomy.md](evolution-drift-taxonomy.md) for full drift classification.

---

## 8. Forge Integration

When Forge is selected, temporal evolution becomes a pre-freeze and post-change governance concern:

- Run [`temporal-evolution-checklist.md`](../../agents/mars-forge/temporal-evolution-checklist.md) when freeze state, version lineage, cumulative edits, override history, modernization, regression risk, or long-term maintainability affects the scope.
- Record **TEMPORAL EVOLUTION FINDINGS** for temporal continuity QA, freeze-state QA, drift survivability QA, continuity checkpoint QA, evolution traceability QA, and long-term governance QA.
- Use [project-drift-survivability-model.md](project-drift-survivability-model.md) to classify freeze-state layer, governed evolution layer, controlled override layer, iterative-change layer, long-term continuity layer, escalation/review layer, and architectural survivability layer.
- Use [evolution-drift-taxonomy.md](evolution-drift-taxonomy.md) to name gradual erosion, freeze divergence, cumulative override decay, patch-history contamination, governance fatigue, identity mutation, and related patterns.
- Use [operational-workflow-governance.md](operational-workflow-governance.md) when long-term continuity depends on checkpoint integrity, freeze-validation records, handoff stability, or context-loss prevention; report `WORKFLOW DISCIPLINE FINDINGS` separately.
- Use [production-readiness-governance.md](production-readiness-governance.md) when long-term continuity depends on delivery survivability, onboarding readability, maintainability continuity, future-edit safety, or post-delivery stability; report `PRODUCTION READINESS FINDINGS` separately.
- Use [context-survivability-governance.md](context-survivability-governance.md) when long-term continuity depends on compressed context, checkpoint memory, freeze-state memory, escalation memory, or reconstruction survivability; report `CONTEXT SURVIVABILITY FINDINGS` separately.
- Use [failure-recovery-governance.md](failure-recovery-governance.md) when long-term continuity depends on trusted-state recovery, rollback integrity, freeze restoration, degraded-state handling, or recovery traceability; report `FAILURE RECOVERY FINDINGS` separately.
- Use [governance-minimalism.md](governance-minimalism.md) when long-term governance survivability is threatened by governance fatigue, over-layering, or methodological weight; report `GOVERNANCE MINIMALISM FINDINGS` separately.
- Use [organizational-memory-governance.md](organizational-memory-governance.md) when long-term evolution creates reusable lessons, historical decision memory, rediscovery risks, or continuity inheritance needs; report `ORGANIZATIONAL MEMORY FINDINGS` separately.
- Use [governance-evolution-governance.md](governance-evolution-governance.md) when project evolution exposes stale methodology, frozen-process decay, legacy-rule accumulation, or continuity-preserving governance refinement needs; report `GOVERNANCE EVOLUTION FINDINGS` separately.
- Keep **TEMPORAL EVOLUTION FINDINGS** separate from `IMPLEMENTATION RELIABILITY FINDINGS`, `SOURCE LINEAGE FINDINGS`, `QA CONFIDENCE FINDINGS`, and `STRATEGIC INTENT FINDINGS`, then summarize whether the current change preserves future continuity.
- Escalate **SAFE UNKNOWN** when freeze source, baseline, version lineage, approval path, divergence rationale, cumulative override impact, or architectural survivability cannot be established.

This is human-supervised evolution methodology. It does not claim automatic drift detection, autonomous maintenance, runtime validation, or permanent architectural stability.

---

## 9. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory temporal evolution lessons:

- A V2 rebuild can preserve current visual intent while still needing explicit continuity against V1/archive contamination.
- Freeze states are valuable only when later edits disclose whether they preserve, reopen, supersede, or diverge from the frozen baseline.
- Local fixes for hierarchy, proof, CTA, spacing, icons, or responsiveness can slowly mutate project identity if cumulative impact is not reviewed.
- A visually acceptable patch may still increase override pressure, patch-history entropy, or architectural ambiguity.
- Provenance, strategic intent, QA confidence, and implementation reliability need time-aware review when sessions accumulate.
- Long-lived frontend work needs checkpoint language for "what changed since the last trusted state," not only "what passes now."

These are Website Factory governance lessons, not Triumph redesign instructions.

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Freeze baseline is unclear | Cannot prove what state future work must preserve or compare against. |
| Version lineage is missing | Cannot know whether current state supersedes, branches, or diverges from earlier artifacts. |
| Divergence rationale is absent | Cannot tell if a change is approved evolution, emergency patch, or drift. |
| Patch history is ambiguous | Cannot identify whether repeated fixes are intentional pattern or entropy. |
| Override accumulation is unreviewed | Cannot assess cumulative pressure or future regression risk. |
| Modernization authority is missing | Cannot know whether new style, code, or architecture may replace older identity. |
| Governance checkpoint was skipped | Cannot claim long-term continuity when only local correctness was checked. |
| Architectural survivability is unproven | Cannot claim the project remains readable for future operators. |

**Action:** state the unknown, identify the resolver, and classify continuation as continue with disclosure, checkpoint required, HITL required, blocked, or monitored risk.

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Temporal Evolution & Project Drift Governance layer - continuity over time, freeze-state integrity, project drift, governance survivability, evolution traceability, drift survivability model, taxonomy, and Forge `TEMPORAL EVOLUTION FINDINGS`; documentation only. |
| v0.1 | 2026-05-17 | Linked Operational Workflow & Execution Discipline Governance for checkpoint integrity, freeze-validation records, handoff stability, context-loss prevention, and continuity checkpoint discipline. |
| v0.2 | 2026-05-17 | Linked Knowledge Compression & Context Survivability Governance for compression integrity, checkpoint memory, freeze-state memory, escalation memory, and reconstruction survivability. |
| v0.3 | 2026-05-17 | Linked Failure Recovery & Operational Resilience Governance for trusted-state recovery, rollback integrity, freeze restoration, degraded-state handling, and recovery traceability. |
| v0.4 | 2026-05-17 | Linked Governance Minimalism & Complexity Control for governance fatigue, methodological weight, and long-term governance survivability. |
| v0.5 | 2026-05-17 | Linked Organizational Memory & Institutional Knowledge Governance for lesson survivability, historical continuity, rediscovery avoidance, and continuity inheritance across long-term evolution. |
| v0.6 | 2026-05-17 | Linked Governance Evolution & Self-Refinement Discipline for stale-methodology review, frozen-process decay, legacy-rule accumulation, and continuity-preserving governance refinement. |
| v0.7 | 2026-05-17 | Linked Production Readiness & Delivery Survivability Governance for delivery traceability, post-delivery stability, onboarding survivability, and lifecycle continuity after freeze. |
