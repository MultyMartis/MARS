# MARS Website Factory — QA Confidence & Verification Governance

**Status:** **documented** — Website Factory QA confidence governance and human-supervised verification methodology only.  
**Not:** autonomous QA AI, runtime verification system, fake test engine, universal QA truth, real-device lab claim, or replacement for project-specific testing.

**Core principle:** frontend QA quality depends on **honest confidence reporting** and **verification transparency**, not only on running checks, visual inspection, build success, or responsive survivability.

**Companion documents:** [verification-evidence-model.md](verification-evidence-model.md), [qa-drift-taxonomy.md](qa-drift-taxonomy.md).  
**Related layers:** [adaptive-governance.md](adaptive-governance.md), [decision-transparency-governance.md](decision-transparency-governance.md), [trust-calibration-governance.md](trust-calibration-governance.md), [strategic-intent-governance.md](strategic-intent-governance.md), [knowledge-provenance-governance.md](knowledge-provenance-governance.md), [context-survivability-governance.md](context-survivability-governance.md), [failure-recovery-governance.md](failure-recovery-governance.md), [governance-minimalism.md](governance-minimalism.md), [governance-prioritization.md](governance-prioritization.md), [governance-economics.md](governance-economics.md), [source-interpretation-governance.md](source-interpretation-governance.md), [design-intent-transfer-governance.md](design-intent-transfer-governance.md), [implementation-reliability-governance.md](implementation-reliability-governance.md), [temporal-evolution-governance.md](temporal-evolution-governance.md), [operational-workflow-governance.md](operational-workflow-governance.md), [accessibility-intent-governance.md](accessibility-intent-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [responsive-intent-governance.md](responsive-intent-governance.md), [interaction-intent-governance.md](interaction-intent-governance.md), [state-behavioral-consistency-governance.md](state-behavioral-consistency-governance.md), [human-escalation-governance.md](human-escalation-governance.md), [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md).  
**Forge checklist:** [`../../agents/mars-forge/qa-confidence-checklist.md`](../../agents/mars-forge/qa-confidence-checklist.md).

---

## 1. Positioning

QA Confidence & Verification Governance formalizes the honesty layer that sits above individual QA checks.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Evidence integrity, scoped confidence, uncertainty visibility, and PASS qualification | A universal QA score or mathematical certainty model |
| Human-readable verification chains for frontend QA reports | Automated browser farms, device labs, screenshot diff systems, or CI engines |
| Anti-hallucination reporting discipline for build, source, rendered, visual, responsive, interaction, state, and accessibility checks | Claims that unrun tests, unseen devices, or unverified states passed |
| Drift vocabulary for fake PASS states, partial-check inflation, QA theater, and hidden uncertainty | Redesigning Triumph or any other project |

The governance question is not “can the report say PASS?”  
The governance question is: **what was verified, by what evidence, within what scope, and what remains unknown?**

---

## 2. Canonical Definition

**QA confidence** is the declared strength of a QA conclusion relative to the evidence actually available.

It preserves:

- **Evidence integrity** — claims are anchored to checks, source reads, rendered inspection, build output, or explicit unknowns.
- **Confidence honesty** — confidence never exceeds evidence.
- **Uncertainty visibility** — gaps, assumptions, and unverified states remain visible.
- **Verification traceability** — a future operator can tell why a PASS, PARTIAL, FAIL, or SAFE UNKNOWN was reported.
- **Scoped truthfulness** — validation applies only to the named slice, viewport, state, source, build, or check.
- **Anti-hallucination reporting** — inferred or assumed validation is labeled, not presented as verified fact.

QA confidence is not a mood, impression, or rhetorical seal. It is a reportable relationship between **claim**, **scope**, **evidence**, and **unknowns**.

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **QA confidence** | The stated trust level of a QA conclusion based on the evidence available. |
| **Verification evidence** | The concrete basis for a claim: direct interaction, rendered inspection, source review, build output, inference, assumption, or unknown. |
| **Scoped validation** | Validation limited to named files, sections, breakpoints, states, scripts, browsers, or source artifacts. |
| **Evidence hierarchy** | The ordered distinction between stronger and weaker verification modes; see [verification-evidence-model.md](verification-evidence-model.md). |
| **Confidence inflation** | Reporting stronger confidence than the evidence supports. |
| **Inferred verification** | A conclusion derived from related evidence but not directly checked; it must be labeled. |
| **Partial validation** | A valid but incomplete check set that cannot support universal PASS. |
| **Evidence transparency** | Report wording makes the evidence level and boundary readable. |
| **QA survivability** | QA findings remain useful across sessions because scope, evidence, gaps, and actions are understandable. |
| **Confidence contamination** | Build success, visual similarity, source review, or prior knowledge incorrectly raises confidence for unverified areas. |
| **Unverifiable claim** | A claim whose evidence cannot be named or reproduced from available artifacts. |
| **Hidden uncertainty** | Known or likely gaps omitted from the report. |
| **Proof boundary** | The limit beyond which evidence no longer supports the claim. |
| **Verification readability** | A future operator can read the QA record and understand what was checked, how, and what remains unresolved. |
| **Anti-theater QA** | QA reporting that avoids performative PASS language and exposes real evidence, gaps, and risk. |

---

## 4. Core Rules

- **Confidence must match evidence.**
- **Uncertainty should be visible.**
- **Evidence should be scoped.**
- **PASS claims require qualification** when the evidence is partial, inferred, source-only, build-only, or rendered-only.
- **Verification gaps must be disclosed** instead of hidden behind “looks good.”
- **QA should remain explainable** to a future operator.
- **SAFE UNKNOWN is preferable to false certainty.**
- **Inferred validation must be labeled** and cannot become direct verification by repetition.
- **Build success is not frontend correctness.**
- **Screenshot validation is not interaction validation.**
- **Source-level review is not rendered verification.**
- **Responsive survivability is not full responsive intent verification.**
- **Accessibility intent review is not a certified accessibility audit.**

---

## 5. PASS Qualification

A PASS is valid only inside its proof boundary.

Acceptable examples:

- `PASS — build-level: npm script completed; rendered behavior not checked.`
- `PASS — rendered verified at 1440px and 375px; tablet remains SAFE UNKNOWN.`
- `PARTIAL — visual hierarchy matches source; hover/focus states not verified.`
- `PASS — source-level: semantic structure reviewed; rendered CSS output not inspected.`

Forbidden examples:

- `PASS everywhere`
- `All good`
- `Fully verified` when only source or screenshot was reviewed
- `Responsive OK` when only desktop was seen
- `Interactions work` when hooks or user flows were not exercised
- `Accessible` when keyboard, focus, labels, contrast, or assistive behavior were not verified

---

## 6. Evidence Boundaries

Different checks answer different questions:

| Evidence | Supports | Does not support |
|----------|----------|------------------|
| **Build success** | Toolchain can complete under observed conditions. | Visual correctness, interaction correctness, accessibility correctness, responsive intent, device/browser coverage. |
| **Source-level review** | Code, semantics, ownership, selectors, includes, and declared behavior are readable. | Actual rendered layout, computed styles, browser behavior, interaction execution. |
| **Rendered visual inspection** | The UI appears correct for observed viewport/state. | Hidden states, keyboard flow, JS behavior, real device behavior, unobserved breakpoints. |
| **Screenshot comparison** | Qualitative visual similarity for visible source areas. | Interaction validation, responsive behavior, runtime state, exact pixels, hidden content. |
| **Direct interaction check** | Observed behavior for a named flow/state/environment. | Universal behavior across all devices, browsers, roles, or untested paths. |
| **Inference** | Reasonable expectation from related evidence. | Verified fact. |

---

## 7. Forge Integration

When Forge is selected, QA confidence is a pre-freeze reporting concern:

- Run [`qa-confidence-checklist.md`](../../agents/mars-forge/qa-confidence-checklist.md) before declaring section PASS, PARTIAL, FAIL, SAFE UNKNOWN, or freeze.
- Record **QA CONFIDENCE FINDINGS** when evidence level, proof boundary, uncertainty, inferred validation, partial validation, or PASS wording affects the report.
- Use [verification-evidence-model.md](verification-evidence-model.md) to label evidence levels.
- Use [qa-drift-taxonomy.md](qa-drift-taxonomy.md) to name fake PASS, QA theater, screenshot certainty drift, confidence escalation, and related patterns.
- Keep source interpretation, visual reconciliation, responsive intent, interaction/state/accessibility, implementation reliability, and foundation QA findings separate, then summarize the confidence boundary across them.
- Use [decision-boundary-model.md](decision-boundary-model.md) when missing evidence creates HITL-recommended, HITL-required, blocked-by-ambiguity, or blocked-by-contradiction conditions.
- Use [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md) when QA confidence depends on reviewer independence, validator integrity, role separation, or multi-agent consensus.
- Use [knowledge-provenance-governance.md](knowledge-provenance-governance.md) when QA confidence depends on source origin, authority chain, derivation disclosure, stale lineage, or unknown-origin evidence.
- Use [strategic-intent-governance.md](strategic-intent-governance.md) when QA confidence depends on business-priority preservation, conversion hierarchy, proof hierarchy, stakeholder intent, or operational trust; report `STRATEGIC INTENT FINDINGS` separately from evidence confidence.
- Use [temporal-evolution-governance.md](temporal-evolution-governance.md) when QA confidence depends on freeze-state integrity, version lineage, continuity checkpoints, cumulative change risk, or long-term governance survivability; report `TEMPORAL EVOLUTION FINDINGS` separately from evidence confidence.
- Use [operational-workflow-governance.md](operational-workflow-governance.md) when QA confidence depends on execution order, checkpoint integrity, freeze-validation evidence, report consistency, or handoff stability; report `WORKFLOW DISCIPLINE FINDINGS` separately from evidence confidence.
- Use [context-survivability-governance.md](context-survivability-governance.md) when QA confidence depends on compressed context, summary completeness, checkpoint persistence, freeze-state memory, escalation memory, or reconstruction integrity; report `CONTEXT SURVIVABILITY FINDINGS` separately from evidence confidence.
- Use [failure-recovery-governance.md](failure-recovery-governance.md) when QA confidence depends on recovery validation, trusted-state evidence, rollback proof, degraded-state visibility, freeze restoration, or continuity restoration; report `FAILURE RECOVERY FINDINGS` separately from evidence confidence.
- Use [governance-minimalism.md](governance-minimalism.md) when QA depth risks ritualized validation, checklist fatigue, or confidence theater through excessive process; report `GOVERNANCE MINIMALISM FINDINGS` separately from evidence confidence.
- Use [governance-prioritization.md](governance-prioritization.md) when QA confidence findings are numerous or severity-sensitive and need risk weighting, signal-to-noise protection, or critical-path prioritization; report `RISK WEIGHTING FINDINGS` separately from evidence confidence.
- Use [governance-economics.md](governance-economics.md) when QA depth creates validation-cost explosion, QA resource drain, weak governance ROI, or review-cost imbalance; report `GOVERNANCE ECONOMICS FINDINGS` separately from evidence confidence.
- Use [adaptive-governance.md](adaptive-governance.md) when QA depth itself needs context-sensitive selection, proportional rigor, or process-scaling justification; report `ADAPTIVE GOVERNANCE FINDINGS` separately from evidence confidence.
- Use [decision-transparency-governance.md](decision-transparency-governance.md) when PASS/PARTIAL/FAIL, confidence level, proof boundary, uncertainty, or recommendation requires visible rationale; report `REASONING VISIBILITY FINDINGS` separately from evidence confidence.
- Use [trust-calibration-governance.md](trust-calibration-governance.md) when QA confidence affects operator trust, credibility survivability, perceived reliability, or institutional overtrust; report `TRUST CALIBRATION FINDINGS` separately from evidence confidence.
- Use [design-intent-transfer-governance.md](design-intent-transfer-governance.md) when QA confidence depends on source-to-build fidelity, approximation transparency, hierarchy fidelity, semantic transfer, or reconstruction traceability; report `RECONSTRUCTION FIDELITY FINDINGS` separately from evidence confidence.
- Treat QA confidence findings as human-supervised governance, not automated scoring.

---

## 8. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory QA confidence lessons:

- A build can succeed while visual hierarchy, interaction behavior, state behavior, or accessibility intent remains unverified.
- Screenshot similarity can support a visual read, but it cannot prove hover, focus, form, mobile tap, or JS behavior.
- Source review can confirm code shape, but it cannot prove rendered spacing, computed styles, or viewport behavior without rendered evidence.
- Responsive survival at one or two widths does not prove full responsive intent or real device coverage.
- Dense frontend governance layers can create false confidence if the REPORT collapses many partial checks into one universal PASS.
- SAFE UNKNOWN should remain explicit when evidence is missing, especially for mobile source, interaction states, keyboard paths, build scripts, and device coverage.

These are Website Factory governance lessons, not Triumph-specific redesign instructions.

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Check was not run | Cannot claim verification without evidence. |
| Tool output is unavailable | Cannot prove build, lint, test, or preview result. |
| Rendered output was not inspected | Cannot claim visual or layout correctness. |
| Interaction was not exercised | Cannot claim click, hover, keyboard, form, carousel, modal, or JS behavior. |
| Breakpoint or device was not observed | Cannot claim that viewport or real device passed. |
| Source is ambiguous or missing | Cannot claim source-faithful implementation. |
| Evidence is inferred from adjacent checks | Cannot promote inference to direct verification. |
| Report scope is broader than evidence | Must narrow claim or disclose partial validation. |

**Action:** state what was verified, what was not verified, what would resolve the gap, and whether the outcome is PASS, PARTIAL, FAIL, SAFE UNKNOWN, HITL REQUIRED, or STOP.

---

## 10. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial QA Confidence & Verification Governance layer — evidence integrity, confidence honesty, verification transparency, anti-theater QA, Forge `QA CONFIDENCE FINDINGS`; documentation only. |
| v0.1 | 2026-05-17 | Linked Human Escalation & Decision Boundary Governance for QA confidence gaps that require HITL, stop conditions, or contradiction blocking. |
| v0.2 | 2026-05-17 | Linked Multi-Agent Coordination & Responsibility Governance for reviewer independence, validator integrity, fake consensus, and chain hallucination risks in QA confidence. |
| v0.3 | 2026-05-17 | Linked Knowledge Provenance & Source Lineage Governance for evidence lineage, source-authority visibility, stale-source risk, and unknown-origin QA evidence. |
| v0.4 | 2026-05-17 | Linked Temporal Evolution & Project Drift Governance for freeze-state integrity, version lineage, continuity checkpoints, cumulative change risk, and long-term governance survivability. |
| v0.5 | 2026-05-17 | Linked Operational Workflow & Execution Discipline Governance for execution order, checkpoint integrity, freeze-validation evidence, report consistency, and handoff stability. |
| v0.6 | 2026-05-17 | Linked Knowledge Compression & Context Survivability Governance for compressed-context evidence boundaries, checkpoint persistence, freeze-state memory, escalation memory, and reconstruction integrity. |
| v0.7 | 2026-05-17 | Linked Failure Recovery & Operational Resilience Governance for recovery validation, trusted-state evidence, rollback proof, degraded-state visibility, and continuity restoration. |
| v0.8 | 2026-05-17 | Linked Governance Minimalism & Complexity Control for ritualized QA, checklist fatigue, process proportionality, and governance-to-value review. |
| v0.9 | 2026-05-17 | Linked Governance Prioritization & Risk Weighting for severity proportionality, critical-path visibility, signal-to-noise QA, and prioritized QA confidence reporting. |
| v0.10 | 2026-05-17 | Linked Decision Transparency & Reasoning Visibility Governance for confidence rationale, traceable PASS/PARTIAL/FAIL conclusions, uncertainty readability, and reviewable QA recommendations. |
| v0.11 | 2026-05-17 | Linked Adaptive Governance & Context-Sensitive Discipline for adaptive QA depth, proportional rigor, and context-fit verification scope selection. |
| v0.12 | 2026-05-17 | Linked Design Intent Transfer & Reconstruction Fidelity Governance for QA evidence boundaries around reconstruction fidelity, approximation transparency, and source-to-build traceability. |
