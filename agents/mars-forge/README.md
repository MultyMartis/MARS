# MARS Forge — thin operational overlay (v0)

**Tier 2 entry (Forge lane)** — **modes (Lite default):** [forge-operational-modes-v1.md](forge-operational-modes-v1.md) → [AGENT.md](AGENT.md), [workflow.md](workflow.md). **Canonical Gulp↔Forge relationship (read once):** [frontend-legacy-and-foundation-map-v0.md](../../governance/frontend-legacy-and-foundation-map-v0.md) §5–6 — overlay **only**, **not** parallel SoT. **Tier model:** [survivability-canonical-entrypoint-model-v0.md](../../governance/survivability-canonical-entrypoint-model-v0.md).

**MARS Forge** is a **thin overlay specialist pack** on the **canonical** [Gulp Frontend Agent](../frontend-gulp-agent/README.md) foundation — **not** a second Gulp system, **not** runtime, **not** orchestration.

| Field | Value |
|--------|--------|
| **agent_id** | `mars_forge_frontend_agent` |
| **status** | `operational_doc_pack` |
| **parent_system** | `mars_website_factory` |
| **foundation_parent** | `gulp_frontend_agent` |

**Related card:** [`../cards/mars-forge-frontend-agent-v0.md`](../cards/mars-forge-frontend-agent-v0.md)

---

## What Forge is

An **overlay specialist** that **inherits → extends → stabilizes** frontend production execution:

- **Phased pipeline** (structure through freeze)
- **Anti-drift** and **no silent structural invention**
- **Freeze semantics** per section
- **Stronger QA sequencing** (overlay checks, not a duplicate QA system)
- **Design-to-code discipline** with honesty limits

**v0 posture:** **stabilization before precision** — not a pixel-perfect layer yet.

**Current stress-test preparation:** Triumph V3 battle test — [`../../projects/triumph-manipulator-landing/V3-BATTLE-TEST-CHARTER.md`](../../projects/triumph-manipulator-landing/V3-BATTLE-TEST-CHARTER.md). V3 is a doctrine validation exercise for a full rebuild from V1 source authority; it is not a V2 implementation continuation or production-readiness claim.

---

## What Forge inherits (mandatory — do not duplicate here)

| Surface | Canonical source |
|---------|------------------|
| Gulp / include workflow | [`../frontend-gulp-agent/workflow.md`](../frontend-gulp-agent/workflow.md), [`gulp-architecture.md`](../frontend-gulp-agent/gulp-architecture.md) |
| Implementation rules | [`../frontend-gulp-agent/frontend-rules.md`](../frontend-gulp-agent/frontend-rules.md), [`constraints.md`](../frontend-gulp-agent/constraints.md) |
| Handoff consumption | [`frontend-handoff-contract-v0.md`](../../projects/mars-website-factory/frontend-handoff-contract-v0.md), pack [`handoff-rules.md`](../frontend-gulp-agent/handoff-rules.md) |
| Prompt discipline | [`frontend-prompt-discipline-v0.md`](../../projects/mars-website-factory/frontend-prompt-discipline-v0.md), pack [`prompt-patterns.md`](../frontend-gulp-agent/prompt-patterns.md) |
| Reporting | pack [`reporting.md`](../frontend-gulp-agent/reporting.md), [`reporting-standard-v0.md`](../../projects/mars-website-factory/reporting-standard-v0.md) |
| Foundation QA | pack [`qa-checklist.md`](../frontend-gulp-agent/qa-checklist.md) |

**Rule:** If Forge is silent, **foundation wins**.

---

## What Forge adds (this pack only)

**Tier 3 catalog (on demand)** — do **not** read this table end-to-end for a normal session. Start: [AGENT.md](AGENT.md) → [qa-checklist.md](qa-checklist.md). Open one checklist only when a contract or phase gate requires it.

| Doc | Role |
|-----|------|
| [`AGENT.md`](AGENT.md) | Operational behavior, phases, gates, freeze |
| [`workflow.md`](workflow.md) | Deterministic 7-phase pipeline + drift prevention |
| [`qa-checklist.md`](qa-checklist.md) | **Overlay** QA — spacing, hierarchy, sequencing, freeze (not full duplicate) |
| [`visual-reconciliation-checklist.md`](visual-reconciliation-checklist.md) | **Visual reconciliation (G6)** — human-supervised visual intent check pre-freeze ([factory methodology](../../projects/mars-website-factory/visual-reconciliation-layer.md)) |
| [`composition-awareness-checklist.md`](composition-awareness-checklist.md) | **Compositional structure (G7)** — composition-vs-DOM cluster read pre-freeze ([methodology](../../projects/mars-website-factory/compositional-structure-awareness.md)) |
| [`design-intent-checklist.md`](design-intent-checklist.md) | **Design intent QA** — radius philosophy, surface hierarchy, CTA philosophy, UI weight, shadow/border restraint, SaaS contamination; records `DESIGN INTENT FINDINGS` ([governance](../../projects/mars-website-factory/design-system-intent-governance.md)) |
| [`design-token-checklist.md`](design-token-checklist.md) | **Design token intelligence QA** — semantic token intent, token hierarchy, aliases, override governance, responsive/state token integrity, drift taxonomy; records `DESIGN TOKEN FINDINGS` ([governance](../../projects/mars-website-factory/design-token-intelligence-governance.md), [layers](../../projects/mars-website-factory/token-semantic-layer-model.md), [taxonomy](../../projects/mars-website-factory/token-drift-taxonomy.md)) |
| [`implementation-reliability-checklist.md`](implementation-reliability-checklist.md) | **Implementation reliability QA** — frontend stability, deterministic rebuilds, scoped fixes, override/include/breakpoint integrity, regression survivability, drift taxonomy; records `IMPLEMENTATION RELIABILITY FINDINGS` ([governance](../../projects/mars-website-factory/implementation-reliability-governance.md), [model](../../projects/mars-website-factory/frontend-stability-model.md), [taxonomy](../../projects/mars-website-factory/implementation-drift-taxonomy.md)) |
| [`cadence-governance-checklist.md`](cadence-governance-checklist.md) | **Cadence governance** — inter-screen spacing as narrative pacing; continuity, transition pacing, density stacks, footer closure, mobile survivability; records `CADENCE FINDINGS` ([canon](../../projects/mars-website-factory/canonical-vertical-cadence-system.md), [tiers](../../projects/mars-website-factory/cadence-tier-model.md)) |
| [`rhythm-governance-checklist.md`](rhythm-governance-checklist.md) | **Rhythm governance** — typography cadence, section spacing, density continuity, CTA/mobile rhythm; records `RHYTHM FINDINGS` ([typography](../../projects/mars-website-factory/typography-rhythm-governance.md), [vertical](../../projects/mars-website-factory/vertical-rhythm-governance.md)) |
| [`responsive-intent-checklist.md`](responsive-intent-checklist.md) | **Responsive intent QA** — hierarchy survival, mobile cadence, composition collapse, CTA collapse, stack integrity, collapse taxonomy; records `RESPONSIVE INTENT FINDINGS` ([governance](../../projects/mars-website-factory/responsive-intent-governance.md)) |
| [`content-density-checklist.md`](content-density-checklist.md) | **Content density QA** — information pressure, scanning rhythm, proof pacing, trust density, overload taxonomy, CTA survival; records `CONTENT DENSITY FINDINGS` ([governance](../../projects/mars-website-factory/content-density-governance.md), [pressure model](../../projects/mars-website-factory/information-pressure-model.md), [taxonomy](../../projects/mars-website-factory/content-overload-taxonomy.md)) |
| [`source-interpretation-checklist.md`](source-interpretation-checklist.md) | **Source interpretation QA** — interpretation confidence, ambiguity, screenshot authority boundaries, source contradiction handling, SAFE UNKNOWN escalation; records `SOURCE INTERPRETATION FINDINGS` ([governance](../../projects/mars-website-factory/source-interpretation-governance.md), [confidence](../../projects/mars-website-factory/source-confidence-model.md), [taxonomy](../../projects/mars-website-factory/source-ambiguity-taxonomy.md)) |
| [`reconstruction-fidelity-checklist.md`](reconstruction-fidelity-checklist.md) | **Reconstruction fidelity QA** — source-to-build fidelity, design-intent transfer, approximation transparency, hierarchy fidelity, semantic transfer, and fidelity survivability; records `RECONSTRUCTION FIDELITY FINDINGS` ([governance](../../projects/mars-website-factory/design-intent-transfer-governance.md), [model](../../projects/mars-website-factory/reconstruction-fidelity-model.md), [taxonomy](../../projects/mars-website-factory/reconstruction-drift-taxonomy.md)) |
| [`qa-checklist.md`](qa-checklist.md) § initialization / shell expansion | **Forge initialization and first-screen governance QA** — clean-start, workspace reset, reconstruction bootstrap, shell/header separation, first-screen decomposition, background ownership, commercial density, atmosphere continuity, section language, beautification drift, asset lifecycle, and landing pressure; records `INITIALIZATION FINDINGS`, `WORKSPACE RESET FINDINGS`, `RECONSTRUCTION BOOTSTRAP FINDINGS`, `LAYOUT SHELL FINDINGS`, `FIRST-SCREEN DECOMPOSITION FINDINGS`, `BACKGROUND OWNERSHIP FINDINGS`, `COMMERCIAL DENSITY FINDINGS`, `ATMOSPHERE CONTINUITY FINDINGS`, `SECTION LANGUAGE FINDINGS`, `BEAUTIFICATION DRIFT FINDINGS`, `RECONSTRUCTION ASSET FINDINGS`, `LANDING PRESSURE FINDINGS` ([operational index](../../projects/mars-website-factory/OPERATIONAL-INDEX.md)) |
| [`qa-checklist.md`](qa-checklist.md) § terminal survivability / shell compatibility | **Forge terminal survivability QA** — PowerShell compatibility, shell-safe execution, command portability, UTF-8 continuity, console integrity, terminal readability continuity, validation-command survivability, and display/file corruption distinction; records `TERMINAL SURVIVABILITY FINDINGS`, `SHELL COMPATIBILITY FINDINGS`, `ENCODING READABILITY FINDINGS` ([governance](../../projects/mars-website-factory/terminal-survivability-governance.md), [model](../../projects/mars-website-factory/shell-compatibility-model.md), [taxonomy](../../projects/mars-website-factory/encoding-drift-taxonomy.md)) |
| [`source-lineage-checklist.md`](source-lineage-checklist.md) | **Source lineage QA** — provenance integrity, authority chain, derivation disclosure, transformation boundaries, stale-lineage risk, and unknown-origin source handling; records `SOURCE LINEAGE FINDINGS` ([governance](../../projects/mars-website-factory/knowledge-provenance-governance.md), [model](../../projects/mars-website-factory/source-lineage-model.md), [taxonomy](../../projects/mars-website-factory/provenance-drift-taxonomy.md)) |
| [`interaction-intent-checklist.md`](interaction-intent-checklist.md) | **Interaction intent QA** — interaction semantics, hover authority, CTA behavior consistency, motion restraint, dead zones, overload, and contamination; records `INTERACTION INTENT FINDINGS` ([governance](../../projects/mars-website-factory/interaction-intent-governance.md), [taxonomy](../../projects/mars-website-factory/interaction-behavior-taxonomy.md), [motion](../../projects/mars-website-factory/motion-restraint-model.md)) |
| [`state-consistency-checklist.md`](state-consistency-checklist.md) | **State consistency QA** — hover/focus/active/disabled/loading/validation/success/error integrity, CTA state consistency, mobile state continuity, accessibility-state drift; records `STATE CONSISTENCY FINDINGS` ([governance](../../projects/mars-website-factory/state-behavioral-consistency-governance.md), [taxonomy](../../projects/mars-website-factory/ui-state-taxonomy.md), [integrity model](../../projects/mars-website-factory/interaction-state-integrity-model.md)) |
| [`accessibility-intent-checklist.md`](accessibility-intent-checklist.md) | **Accessibility intent QA** — trusted operational usability, semantic accessibility, focus survivability, keyboard continuity, assistive predictability, contrast trust, accessibility restraint, and drift taxonomy; records `ACCESSIBILITY FINDINGS` ([governance](../../projects/mars-website-factory/accessibility-intent-governance.md), [model](../../projects/mars-website-factory/operational-accessibility-model.md), [taxonomy](../../projects/mars-website-factory/accessibility-drift-taxonomy.md)) |
| [`qa-confidence-checklist.md`](qa-confidence-checklist.md) | **QA confidence QA** — evidence integrity, confidence honesty, scoped PASS discipline, verification traceability, SAFE UNKNOWN visibility, and anti-theater QA; records `QA CONFIDENCE FINDINGS` ([governance](../../projects/mars-website-factory/qa-confidence-governance.md), [evidence model](../../projects/mars-website-factory/verification-evidence-model.md), [taxonomy](../../projects/mars-website-factory/qa-drift-taxonomy.md)) |
| [`human-escalation-checklist.md`](human-escalation-checklist.md) | **Human escalation QA** — escalation boundaries, stop conditions, contradiction escalation, HITL visibility, assumption thresholds, and authority integrity; records `HUMAN ESCALATION FINDINGS` ([governance](../../projects/mars-website-factory/human-escalation-governance.md), [decision model](../../projects/mars-website-factory/decision-boundary-model.md), [taxonomy](../../projects/mars-website-factory/escalation-drift-taxonomy.md)) |
| [`multi-agent-coordination-checklist.md`](multi-agent-coordination-checklist.md) | **Multi-agent coordination QA** — responsibility boundaries, reviewer independence, validator integrity, escalation ownership, orchestration clarity, handoff survivability, and fake-consensus risk; records `MULTI-AGENT FINDINGS` ([governance](../../projects/mars-website-factory/multi-agent-coordination-governance.md), [boundary model](../../projects/mars-website-factory/agent-responsibility-boundary-model.md), [taxonomy](../../projects/mars-website-factory/multi-agent-drift-taxonomy.md)) |
| [`strategic-intent-checklist.md`](strategic-intent-checklist.md) | **Strategic intent QA** — business priority, conversion hierarchy, proof hierarchy, operational trust, stakeholder intent, local optimization boundaries, and strategic drift; records `STRATEGIC INTENT FINDINGS` ([governance](../../projects/mars-website-factory/strategic-intent-governance.md), [continuity model](../../projects/mars-website-factory/business-intent-continuity-model.md), [taxonomy](../../projects/mars-website-factory/strategic-drift-taxonomy.md)) |
| [`temporal-evolution-checklist.md`](temporal-evolution-checklist.md) | **Temporal evolution QA** — freeze-state integrity, governed evolution, controlled overrides, iterative-change accumulation, version lineage, continuity checkpoints, and project drift survivability; records `TEMPORAL EVOLUTION FINDINGS` ([governance](../../projects/mars-website-factory/temporal-evolution-governance.md), [model](../../projects/mars-website-factory/project-drift-survivability-model.md), [taxonomy](../../projects/mars-website-factory/evolution-drift-taxonomy.md)) |
| [`execution-discipline-checklist.md`](execution-discipline-checklist.md) | **Execution discipline QA** — workflow discipline, checkpoint integrity, freeze-validation QA, execution-order QA, handoff stability, continuity checkpoints, and workflow drift; records `WORKFLOW DISCIPLINE FINDINGS` ([governance](../../projects/mars-website-factory/operational-workflow-governance.md), [model](../../projects/mars-website-factory/execution-discipline-model.md), [taxonomy](../../projects/mars-website-factory/workflow-drift-taxonomy.md)) |
| [`production-readiness-checklist.md`](production-readiness-checklist.md) | **Production readiness QA** — delivery survivability, handoff-survivability QA, onboarding-readability QA, maintainability QA, future-edit QA, deployment-survivability QA, and lifecycle-survivability QA; records `PRODUCTION READINESS FINDINGS` ([governance](../../projects/mars-website-factory/production-readiness-governance.md), [model](../../projects/mars-website-factory/delivery-survivability-model.md), [taxonomy](../../projects/mars-website-factory/production-drift-taxonomy.md)) |
| [`context-survivability-checklist.md`](context-survivability-checklist.md) | **Context survivability QA** — compression integrity, checkpoint persistence, freeze-state memory, escalation memory, governance memory, reconstruction handling, and context drift; records `CONTEXT SURVIVABILITY FINDINGS` ([governance](../../projects/mars-website-factory/context-survivability-governance.md), [model](../../projects/mars-website-factory/context-compression-integrity-model.md), [taxonomy](../../projects/mars-website-factory/context-drift-taxonomy.md)) |
| [`failure-recovery-checklist.md`](failure-recovery-checklist.md) | **Failure recovery QA** — trusted-state recovery, rollback integrity, freeze restoration, degraded-state handling, continuity restoration, recovery traceability, and resilience validation; records `FAILURE RECOVERY FINDINGS` ([governance](../../projects/mars-website-factory/failure-recovery-governance.md), [model](../../projects/mars-website-factory/operational-resilience-model.md), [taxonomy](../../projects/mars-website-factory/recovery-drift-taxonomy.md)) |
| [`cross-project-transfer-checklist.md`](cross-project-transfer-checklist.md) | **Cross-project transfer QA** — transfer compatibility, semantic portability, strategic fit, operational fit, governance portability, incompatibility escalation, project identity, and transfer drift; records `CROSS-PROJECT TRANSFER FINDINGS` ([governance](../../projects/mars-website-factory/cross-project-transfer-governance.md), [model](../../projects/mars-website-factory/knowledge-transfer-compatibility-model.md), [taxonomy](../../projects/mars-website-factory/transfer-drift-taxonomy.md)) |
| [`governance-minimalism-checklist.md`](governance-minimalism-checklist.md) | **Governance minimalism QA** — proportional governance, cognitive load, operational readability, checklist fatigue, process survivability, governance-to-value review, and governance bloat taxonomy; records `GOVERNANCE MINIMALISM FINDINGS` ([governance](../../projects/mars-website-factory/governance-minimalism.md), [model](../../projects/mars-website-factory/complexity-control-model.md), [taxonomy](../../projects/mars-website-factory/governance-bloat-taxonomy.md)) |
| [`risk-weighting-checklist.md`](risk-weighting-checklist.md) | **Risk weighting QA** — severity proportionality, operational focus, escalation relevance, signal-to-noise clarity, risk layers, and prioritization drift; records `RISK WEIGHTING FINDINGS` ([governance](../../projects/mars-website-factory/governance-prioritization.md), [model](../../projects/mars-website-factory/risk-weighting-model.md), [taxonomy](../../projects/mars-website-factory/prioritization-drift-taxonomy.md)) |
| [`adaptive-governance-checklist.md`](adaptive-governance-checklist.md) | **Adaptive governance QA** — context-sensitive rigor, proportional process depth, adaptive QA depth, governance fit, contextual escalation, process scaling, survivability balancing, and adaptive drift; records `ADAPTIVE GOVERNANCE FINDINGS` ([governance](../../projects/mars-website-factory/adaptive-governance.md), [model](../../projects/mars-website-factory/context-sensitive-discipline-model.md), [taxonomy](../../projects/mars-website-factory/adaptive-drift-taxonomy.md)) |
| [`governance-economics-checklist.md`](governance-economics-checklist.md) | **Governance economics QA** — operational cost awareness, governance efficiency, validation-cost QA, review allocation, sustainability balancing, governance ROI, and cost drift; records `GOVERNANCE ECONOMICS FINDINGS` ([governance](../../projects/mars-website-factory/governance-economics.md), [model](../../projects/mars-website-factory/operational-cost-awareness-model.md), [taxonomy](../../projects/mars-website-factory/governance-cost-drift-taxonomy.md)) |
| [`cognitive-load-checklist.md`](cognitive-load-checklist.md) | **Cognitive load QA** — review readability, signal-to-noise clarity, reviewer sustainability, governance readability, cognitive survivability, and cognitive drift; records `COGNITIVE LOAD FINDINGS` ([governance](../../projects/mars-website-factory/cognitive-load-governance.md), [model](../../projects/mars-website-factory/review-ergonomics-model.md), [taxonomy](../../projects/mars-website-factory/cognitive-drift-taxonomy.md)) |
| [`governance-compression-checklist.md`](governance-compression-checklist.md) | **Governance compression QA** — operational modes, deployability, compression integrity, mode transitions, governance scalability, portability, and compression drift; records `GOVERNANCE COMPRESSION FINDINGS` ([governance](../../projects/mars-website-factory/governance-compression-governance.md), [model](../../projects/mars-website-factory/operational-modes-model.md), [taxonomy](../../projects/mars-website-factory/compression-drift-taxonomy.md)) |
| [`reasoning-visibility-checklist.md`](reasoning-visibility-checklist.md) | **Reasoning visibility QA** — reasoning visibility, decision traceability, escalation explainability, prioritization transparency, uncertainty visibility, assumption disclosure, and traceable conclusions; records `REASONING VISIBILITY FINDINGS` ([governance](../../projects/mars-website-factory/decision-transparency-governance.md), [model](../../projects/mars-website-factory/reasoning-visibility-model.md), [taxonomy](../../projects/mars-website-factory/reasoning-drift-taxonomy.md)) |
| [`organizational-memory-checklist.md`](organizational-memory-checklist.md) | **Organizational memory QA** — institutional continuity, lesson survivability, operational wisdom, rediscovery avoidance, historical traceability, continuity inheritance, and memory drift; records `ORGANIZATIONAL MEMORY FINDINGS` ([governance](../../projects/mars-website-factory/organizational-memory-governance.md), [model](../../projects/mars-website-factory/institutional-knowledge-model.md), [taxonomy](../../projects/mars-website-factory/knowledge-memory-drift-taxonomy.md)) |
| [`governance-evolution-checklist.md`](governance-evolution-checklist.md) | **Governance evolution QA** — controlled governance evolution, refinement traceability, continuity-safe change, methodology review, adaptive survivability, historical-lineage QA, and evolutionary drift; records `GOVERNANCE EVOLUTION FINDINGS` ([governance](../../projects/mars-website-factory/governance-evolution-governance.md), [model](../../projects/mars-website-factory/self-refinement-model.md), [taxonomy](../../projects/mars-website-factory/evolutionary-drift-taxonomy.md)) |
| [`meta-governance-checklist.md`](meta-governance-checklist.md) | **Meta-governance QA** — governance architecture integrity, cross-layer consistency, methodological coherence, layer-boundary clarity, contradiction survivability, governance topology, and architecture readability; records `META-GOVERNANCE FINDINGS` ([governance](../../projects/mars-website-factory/meta-governance-integrity.md), [model](../../projects/mars-website-factory/governance-architecture-model.md), [taxonomy](../../projects/mars-website-factory/meta-governance-drift-taxonomy.md)) |
| [`trust-calibration-checklist.md`](trust-calibration-checklist.md) | **Trust calibration QA** — calibrated trust, confidence proportionality, uncertainty visibility, explainable reliability, credibility survivability, and trust traceability; records `TRUST CALIBRATION FINDINGS` ([governance](../../projects/mars-website-factory/trust-calibration-governance.md), [model](../../projects/mars-website-factory/governance-credibility-model.md), [taxonomy](../../projects/mars-website-factory/trust-drift-taxonomy.md)) |
| [`semantic-source-lock.md`](semantic-source-lock.md) | **Semantic source lock** — active version charter, meaning/copy lock, version isolation, P0–P6 priority, quarantine |

---

## Relationships

| Neighbor | Relationship |
|----------|--------------|
| **`agents/frontend-gulp-agent/`** | **Canonical foundation.** Forge is an overlay; never fork or replace this pack. |
| **Website Factory** | Upstream contracts (handoff, workflow S10–S12, block registry, artifact model). Forge **consumes**. |
| **`frontend-production-rules-v0.md`** | **Normative operator cheat sheet.** Forge operationalizes rules through phased pipeline + anti-drift; does **not** supersede the file. |
| **`gulp_frontend_agent`** | Same production lane; Forge is the **named stabilization overlay** for that lane when operator selects Forge discipline. |
| **Frontend QA Agent (planned)** | Downstream Stage 12 reviewer — Forge **prepares** evidence. |

**Execution target:** real HTML/SCSS/JS edits happen in an **external or local gulp-starter project** — same as foundation. This directory is **documentation only**.

**Governance map:** [frontend-legacy-and-foundation-map-v0.md](../../governance/frontend-legacy-and-foundation-map-v0.md) · design precedent: [mars-forge-operational-design-v0.md](../../governance/mars-forge-operational-design-v0.md)

---

## Pack index

1. [`AGENT.md`](AGENT.md) — behavior and gates  
2. [`workflow.md`](workflow.md) — phased pipeline  
3. [`qa-checklist.md`](qa-checklist.md) — overlay QA  
4. [`semantic-source-lock.md`](semantic-source-lock.md) — semantic SoT charter, drift prevention  
5. [`design-intent-checklist.md`](design-intent-checklist.md) — design system intent / UI weight / CTA philosophy QA overlay  
6. [`design-token-checklist.md`](design-token-checklist.md) — semantic token intent / override governance / token drift QA overlay  
7. [`implementation-reliability-checklist.md`](implementation-reliability-checklist.md) — frontend stability / deterministic rebuild / regression survivability QA overlay  
8. [`cadence-governance-checklist.md`](cadence-governance-checklist.md) — inter-screen cadence / narrative pacing QA overlay  
9. [`rhythm-governance-checklist.md`](rhythm-governance-checklist.md) — typography + vertical rhythm QA overlay  
10. [`responsive-intent-checklist.md`](responsive-intent-checklist.md) — responsive intent preservation / mobile composition QA overlay  
11. [`content-density-checklist.md`](content-density-checklist.md) — information pressure / proof pacing / overload taxonomy QA overlay  
12. [`source-interpretation-checklist.md`](source-interpretation-checklist.md) — source confidence / ambiguity / SAFE UNKNOWN QA overlay  
13. [`reconstruction-fidelity-checklist.md`](reconstruction-fidelity-checklist.md) — source-to-build fidelity / approximation transparency / reconstruction survivability QA overlay
14. [`qa-checklist.md`](qa-checklist.md) § initialization / shell expansion — clean-start / reset / bootstrap / first-screen decomposition / commercial pressure / terminal survivability / shell compatibility QA overlay
15. [`source-lineage-checklist.md`](source-lineage-checklist.md) — provenance integrity / authority chain / derivation traceability QA overlay  
16. [`interaction-intent-checklist.md`](interaction-intent-checklist.md) — interaction semantics / hover authority / motion restraint QA overlay  
17. [`state-consistency-checklist.md`](state-consistency-checklist.md) — UI state integrity / behavioral consistency QA overlay  
18. [`accessibility-intent-checklist.md`](accessibility-intent-checklist.md) — operational accessibility / focus / keyboard / assistive predictability QA overlay  
19. [`qa-confidence-checklist.md`](qa-confidence-checklist.md) — evidence integrity / verification transparency / scoped PASS QA overlay  
20. [`human-escalation-checklist.md`](human-escalation-checklist.md) — decision-boundary / HITL visibility / stop-condition QA overlay  
21. [`multi-agent-coordination-checklist.md`](multi-agent-coordination-checklist.md) — responsibility boundary / reviewer independence / validator integrity QA overlay
22. [`strategic-intent-checklist.md`](strategic-intent-checklist.md) — business continuity / conversion hierarchy / proof hierarchy QA overlay
23. [`temporal-evolution-checklist.md`](temporal-evolution-checklist.md) — temporal continuity / freeze-state integrity / drift survivability QA overlay
24. [`execution-discipline-checklist.md`](execution-discipline-checklist.md) — workflow discipline / checkpoint integrity / handoff survivability QA overlay
25. [`production-readiness-checklist.md`](production-readiness-checklist.md) — production readiness / delivery survivability / maintainability continuity QA overlay
26. [`context-survivability-checklist.md`](context-survivability-checklist.md) — compression integrity / checkpoint persistence / context reconstruction QA overlay
27. [`failure-recovery-checklist.md`](failure-recovery-checklist.md) — trusted-state recovery / rollback integrity / degraded-state handling / resilience validation QA overlay
28. [`cross-project-transfer-checklist.md`](cross-project-transfer-checklist.md) — transfer compatibility / semantic portability / governance portability QA overlay
29. [`governance-minimalism-checklist.md`](governance-minimalism-checklist.md) — proportional governance / cognitive load / checklist fatigue QA overlay
30. [`risk-weighting-checklist.md`](risk-weighting-checklist.md) — severity proportionality / risk weighting / signal-to-noise QA overlay
31. [`adaptive-governance-checklist.md`](adaptive-governance-checklist.md) — context-sensitive rigor / adaptive QA depth / process scaling QA overlay
32. [`reasoning-visibility-checklist.md`](reasoning-visibility-checklist.md) — reasoning visibility / decision traceability / traceable conclusions QA overlay
33. [`organizational-memory-checklist.md`](organizational-memory-checklist.md) — institutional continuity / lesson survivability / rediscovery avoidance QA overlay
34. [`governance-evolution-checklist.md`](governance-evolution-checklist.md) — controlled evolution / refinement traceability / continuity-safe methodology change QA overlay
35. [`meta-governance-checklist.md`](meta-governance-checklist.md) — governance architecture integrity / cross-layer consistency / contradiction survivability QA overlay
36. [`governance-economics-checklist.md`](governance-economics-checklist.md) — operational cost awareness / governance efficiency / validation-cost / governance ROI QA overlay
37. [`cognitive-load-checklist.md`](cognitive-load-checklist.md) — review readability / signal-to-noise / reviewer sustainability / cognitive survivability QA overlay
38. [`governance-compression-checklist.md`](governance-compression-checklist.md) — operational modes / deployability / compression integrity / governance scalability QA overlay
39. [`trust-calibration-checklist.md`](trust-calibration-checklist.md) — trust calibration / governance credibility / confidence proportionality QA overlay

---

## SAFE UNKNOWN (normative)

- Target project path, gulp version, npm scripts — **project-specific** (inherit foundation).
- Whether sessions must cite Forge vs Gulp pack in REPORT headers — **operator choice** until factory runbook standardizes.
- Full governance transition (alias vs merge-by-reference for `gulp_frontend_agent`) — **SAFE UNKNOWN**.
- Human approval records, waivers, and override owners are project-specific; do not infer approval from missing context.
- Checkpoint records, handoff state, and continuity baselines are project/session-specific; do not infer workflow stability from visible output alone.
- Production-readiness evidence is project- and delivery-specific; do not infer delivery survivability, onboarding readability, maintainability continuity, deployment survivability, or post-delivery stability from QA pass, visual polish, freeze state, or successful shipment alone.
- Compressed context, summaries, and reconstructed state are project/session-specific; do not infer checkpoint persistence, freeze-state memory, or escalation memory from coherent summary language alone.
- Trusted recovery state, rollback baseline, freeze restoration, and degraded-state health are project/session-specific; do not infer operational recovery from visual repair, restored files, or build success alone.
- Cross-project transfer compatibility is project-specific; do not infer strategic fit, semantic portability, governance portability, or project-identity safety from prior-project success alone.
- Governance depth is project- and scope-specific; do not infer that more layers, longer reports, or fuller checklists create better execution quality without proportional governance value.
- Risk weighting is project- and scope-specific; do not infer that many findings, many warnings, or broad QA coverage equal better prioritization, higher safety, or correct severity.
- Adaptive governance depth is project- and scope-specific; do not infer that identical process, maximum rigor, full QA, or lightweight continuation is correct without context-sensitive proportionality.
- Governance economics is project- and scope-specific; do not infer that more validation, stronger survivability, longer reports, or broader governance coverage are worth their operational cost without value density, review allocation, validation efficiency, and survivability-to-cost review.
- Cognitive-load governance is project- and scope-specific; do not infer that longer reports, more findings, denser evidence, or broader visibility improve review quality without operational readability, reviewer sustainability, signal-to-noise clarity, and cognitive survivability.
- Governance compression is project- and scope-specific; do not infer that shorter reports, fewer checks, critical-mode defaults, or dense governance stacks improve deployability without operational mode, compression integrity, mode-transition clarity, governance portability, and scalable density review.
- Reasoning visibility is project- and scope-specific; do not infer that a confident conclusion, polished report, or strong recommendation is reviewable unless evidence, assumptions, uncertainty, prioritization, escalation rationale, and traceability remain visible.
- Organizational memory is project- and scope-specific; do not infer lesson survivability, institutional continuity, rediscovery avoidance, or continuity inheritance from archive volume, old reports, or remembered project history alone.
- Governance evolution is project- and scope-specific; do not infer that old methodology remains correct, new methodology is better, or more rules improve maturity without refinement traceability, continuity-safe change, historical lineage, and proportional governance renewal.
- Meta-governance is project- and scope-specific; do not infer governance architecture integrity, cross-layer consistency, methodological coherence, or contradiction survivability from having many governance layers, indexes, checklists, or cross-links.
- Trust calibration is project- and scope-specific; do not infer credibility, reliability, or sustainable trust from confident tone, long reports, polished reasoning, institutional familiarity, or extensive QA without evidence-backed trust, uncertainty visibility, and trust traceability.
- Reconstruction fidelity is project- and source-specific; do not infer source-to-build fidelity, design-intent transfer, hierarchy fidelity, semantic transfer, or approximation transparency from screenshot similarity, polished layout, visual QA, or "looks close" language alone.
- First-screen, shell, background, atmosphere, commercial pressure, and asset lifecycle ownership are project-specific; do not infer clean-start state, **HEADER != HERO** boundaries, background authority, approved asset inheritance, landing momentum, or anti-SaaS fidelity from visual polish or existing workspace code alone.
- Terminal output, shell syntax, and encoding readability are environment-specific; do not infer terminal survivability, command portability, UTF-8 continuity, file integrity, or validation success from a parser-failed command, unreadable live output, or shell assumptions alone.

---

*Documentation only — no runtime enforcement.*
