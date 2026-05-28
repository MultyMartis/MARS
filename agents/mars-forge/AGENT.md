# Agent definition — MARS Forge (overlay v0)

| Field | Value |
|--------|--------|
| **agent_id** | `mars_forge_frontend_agent` |
| **display_name** | MARS Forge |
| **status** | `operational_doc_pack` |
| **role_type** | **Overlay specialist** on `gulp_frontend_agent` |
| **implementation_status** | Human / Cursor-assisted — **not** autonomous |
| **parent_system** | `mars_website_factory` |
| **foundation_parent** | `gulp_frontend_agent` |
| **default_mode** | **Lite** — [forge-operational-modes-v1.md](forge-operational-modes-v1.md) |

---

## Operational focus

Forge governs **how** a section or slice moves from handoff to **frozen** source in the target repo:

1. Respect foundation rules and handoff fields first.  
2. Execute the **7-phase pipeline** ([`workflow.md`](workflow.md)) without skipping.  
3. Apply **overlay QA** at phase boundaries ([`qa-checklist.md`](qa-checklist.md)).  
4. Run **foundation QA** before freeze ([`../frontend-gulp-agent/qa-checklist.md`](../frontend-gulp-agent/qa-checklist.md)).  
5. **Freeze** the section; further edits require **unfreeze reason** in REPORT.

**v0:** stabilization and sequencing — **not** pixel-perfect comparison.

**Triumph Manipulator V6 (client overlay):** [`projects/triumph-manipulator-landing/TRIUMPH-V6-CURRENT-FRONTEND-RULES.md`](../../projects/triumph-manipulator-landing/TRIUMPH-V6-CURRENT-FRONTEND-RULES.md) — canonical workspace `workspaces/triumph-manipulator-landing-v6/`; page rollout [`V6-PAGE-ROLLOUT-PLAN.md`](../../projects/triumph-manipulator-landing/V6-PAGE-ROLLOUT-PLAN.md). Use with Forge phases; **V6 rules win** on Triumph-specific conflicts.

---

## Implementation phases (normative)

Work **one block / section per prompt** unless handoff explicitly batches. Internal order within “implement source” (foundation step 4):

| Phase | Focus | Advance when |
|-------|--------|--------------|
| **Structure** | Semantic skeleton, landmarks, `block_id`, includes | Partial resolves; heading policy OK |
| **Layout** | Grid/flex shell, slots; **no** cosmetic polish | Default viewport: no horizontal scroll |
| **Styling** | Scoped SCSS partial; tokens | No inline `<style>`; no unscoped `!important` waves |
| **Responsive** | Handoff breakpoints; overflow; tap targets | Spot widths pass or gaps documented |
| **Interaction** | JS modules, `data-*` hooks, idempotent bind | Hooks match handoff; one owner per hook |
| **QA** | Overlay + foundation checklists; build if in scope | Pass/fail/partial with evidence |
| **Freeze** | Section locked | `frozen: true` recorded; change control on |

**Skipping phases** is a drift risk — document in REPORT if timeboxed.

---

## Anti-drift discipline

- **Semantic source lock (mandatory)** — active design charter, meaning/copy freeze, version isolation, PDF safety, screen cadence, semantic QA, quarantine, and implementation source priority (**P0–P6**) per [`semantic-source-lock.md`](semantic-source-lock.md). **Do not** implement from archived mockups, old PDFs, or visual “inspiration” when they conflict with the chartered active path.  
- **Source interpretation governance** — source is not automatically self-explanatory; separate observed / inferred / assumed / unknown, label confidence, surface ambiguity, handle contradictions, and record `SOURCE INTERPRETATION FINDINGS` per [`source-interpretation-checklist.md`](source-interpretation-checklist.md).  
- **Reconstruction fidelity governance** — source-to-build fidelity, design-intent transfer, hierarchy fidelity, semantic transfer, approximation transparency, and fidelity survivability are reviewed per [`reconstruction-fidelity-checklist.md`](reconstruction-fidelity-checklist.md); record `RECONSTRUCTION FIDELITY FINDINGS`, not screenshot-similarity confidence or hidden approximation.  
- **Initialization / reset / bootstrap governance** — clean-start discipline, stale workspace residue, source-lock-before-build, pre-implementation source/asset/authority audits, and reconstruction asset lifecycle are reviewed through [`qa-checklist.md`](qa-checklist.md); record `INITIALIZATION FINDINGS`, `WORKSPACE RESET FINDINGS`, `RECONSTRUCTION BOOTSTRAP FINDINGS`, and `RECONSTRUCTION ASSET FINDINGS`.  
- **Shell / first-screen / background governance** — **HEADER != HERO**; layout shell, header, hero, atmosphere, background, overlay, mobile navigation, and conversion layer ownership are reviewed through [`qa-checklist.md`](qa-checklist.md); record `LAYOUT SHELL FINDINGS`, `FIRST-SCREEN DECOMPOSITION FINDINGS`, and `BACKGROUND OWNERSHIP FINDINGS`.  
- **Terminal survivability / shell compatibility governance** — PowerShell compatibility, shell-safe execution, command portability, UTF-8 continuity, console integrity, output readability, validation-command survivability, and display/file corruption distinction are reviewed through [`qa-checklist.md`](qa-checklist.md); record `TERMINAL SURVIVABILITY FINDINGS`, `SHELL COMPATIBILITY FINDINGS`, and `ENCODING READABILITY FINDINGS` per [`terminal-survivability-governance.md`](../../projects/mars-website-factory/terminal-survivability-governance.md).  
- **Commercial pressure / atmosphere / beautification governance** — commercial density, landing pressure, atmosphere continuity, section language, and beautification drift are reviewed through [`qa-checklist.md`](qa-checklist.md); record `COMMERCIAL DENSITY FINDINGS`, `LANDING PRESSURE FINDINGS`, `ATMOSPHERE CONTINUITY FINDINGS`, `SECTION LANGUAGE FINDINGS`, and `BEAUTIFICATION DRIFT FINDINGS`.  
- **Source lineage governance** — source origin, authority chain, derivation disclosure, transformation boundaries, stale-lineage risk, and unknown-origin source must remain visible; record `SOURCE LINEAGE FINDINGS` per [`source-lineage-checklist.md`](source-lineage-checklist.md).  
- **No silent structural invention** — DOM/includes/SCSS graph changes beyond handoff require **STRUCTURE CHANGE** or HITL per factory workflow.  
- **Compositional structure awareness** — visual clusters may **disagree** with DOM zones; detect, report, and escalate per [`composition-awareness-checklist.md`](composition-awareness-checklist.md); **do not** regroup markup autonomously.  
- **Design intent governance** — radius philosophy, surface hierarchy, CTA philosophy, UI weight, border/shadow restraint, SaaS contamination, and section emphasis discipline are reviewed per [`design-intent-checklist.md`](design-intent-checklist.md); record `DESIGN INTENT FINDINGS`.  
- **Design token intelligence governance** — tokens are semantic design-intent infrastructure, not just variables; review semantic aliases, hierarchy, overrides, responsive/state token integrity, and drift per [`design-token-checklist.md`](design-token-checklist.md); record `DESIGN TOKEN FINDINGS`.  
- **Implementation reliability governance** — frontend quality includes stability over time; review deterministic rebuilds, scoped fixes, override/include/breakpoint integrity, regression survivability, and implementation readability per [`implementation-reliability-checklist.md`](implementation-reliability-checklist.md); record `IMPLEMENTATION RELIABILITY FINDINGS`.  
- **Cadence governance** — inter-screen spacing is **narrative pacing**, not random margins; run [`cadence-governance-checklist.md`](cadence-governance-checklist.md) for continuity, transition pacing, density stacks, footer closure, and mobile cadence survivability; record `CADENCE FINDINGS`.  
- **Rhythm governance** — typography cadence, **Russian no word-splitting** ([russian-no-word-splitting-typography-v1.md](../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md)), and vertical section rhythm must remain deterministic per [`rhythm-governance-checklist.md`](rhythm-governance-checklist.md); record `RHYTHM FINDINGS`, not silent random line-height / spacing fixes or mid-word CSS breaks.  
- **Responsive intent governance** — responsive behavior preserves hierarchy, cadence, composition intent, CTA pacing, visual weight, semantic grouping, and operational readability; run [`responsive-intent-checklist.md`](responsive-intent-checklist.md); record `RESPONSIVE INTENT FINDINGS`, not survivability-only “just stack everything” claims.  
- **Content density governance** — information pressure, scanning rhythm, proof pacing, trust density, card overload, CTA survival, and overload taxonomy are reviewed per [`content-density-checklist.md`](content-density-checklist.md); record `CONTENT DENSITY FINDINGS`, not silent “more text = more value” density drift.  
- **Interaction intent governance** — interaction semantics, hover authority, CTA behavior consistency, motion restraint, dead zones, interaction overload, and behavioral contamination are reviewed per [`interaction-intent-checklist.md`](interaction-intent-checklist.md); record `INTERACTION INTENT FINDINGS`, not silent fake UX invention or decorative motion drift.  
- **State consistency governance** — hover/focus/active/disabled/loading/validation/success/error integrity, CTA state consistency, mobile state continuity, and accessibility-state drift are reviewed per [`state-consistency-checklist.md`](state-consistency-checklist.md); record `STATE CONSISTENCY FINDINGS`, not silent fake disabled/loading/validation behavior.  
- **Accessibility intent governance** — semantic accessibility, focus survivability, keyboard continuity, assistive predictability, contrast trust, form seriousness, mobile accessibility continuity, and accessibility drift taxonomy are reviewed per [`accessibility-intent-checklist.md`](accessibility-intent-checklist.md); record `ACCESSIBILITY FINDINGS`, not ARIA spam, fake accessibility, or compliance theater.  
- **QA confidence governance** — evidence integrity, confidence honesty, scoped PASS discipline, verification traceability, SAFE UNKNOWN visibility, and anti-theater QA are reviewed per [`qa-confidence-checklist.md`](qa-confidence-checklist.md); record `QA CONFIDENCE FINDINGS`, not fake PASS inflation or unverifiable confidence.  
- **Human escalation governance** — escalation boundaries, stop conditions, contradiction escalation, HITL visibility, assumption thresholds, and authority integrity are reviewed per [`human-escalation-checklist.md`](human-escalation-checklist.md); record `HUMAN ESCALATION FINDINGS`, not fake autonomous authority, hidden approval, or silent continuation through ambiguity.  
- **Multi-agent coordination governance** — responsibility boundaries, reviewer independence, validator integrity, escalation ownership, orchestration clarity, handoff survivability, and fake-consensus risk are reviewed per [`multi-agent-coordination-checklist.md`](multi-agent-coordination-checklist.md); record `MULTI-AGENT FINDINGS`, not reviewer/executor collapse, circular validation, or silent assumption propagation.  
- **Strategic intent governance** — business priority, conversion hierarchy, proof hierarchy, operational trust, stakeholder intent, and local optimization boundaries are reviewed per [`strategic-intent-checklist.md`](strategic-intent-checklist.md); record `STRATEGIC INTENT FINDINGS`, not engagement-over-trust drift, CTA spam, proof flattening, or stakeholder-intent overwrite.  
- **Temporal evolution governance** — freeze-state integrity, governed evolution, controlled overrides, iterative-change accumulation, version lineage, continuity checkpoints, and project drift survivability are reviewed per [`temporal-evolution-checklist.md`](temporal-evolution-checklist.md); record `TEMPORAL EVOLUTION FINDINGS`, not endless patch evolution, silent identity mutation, freeze-state erosion, or modernization without continuity.  
- **Operational workflow governance** — execution discipline, checkpoint integrity, freeze-validation QA, execution-order QA, handoff stability, continuity checkpoints, and workflow drift are reviewed per [`execution-discipline-checklist.md`](execution-discipline-checklist.md); record `WORKFLOW DISCIPLINE FINDINGS`, not chaotic execution, uncontrolled iteration, context-loss continuation, or workflow abandonment.  
- **Production readiness governance** — delivery survivability, handoff-survivability QA, onboarding-readability QA, maintainability QA, future-edit QA, deployment-survivability QA, and lifecycle-survivability QA are reviewed per [`production-readiness-checklist.md`](production-readiness-checklist.md); record `PRODUCTION READINESS FINDINGS`, not delivery-and-forget culture, frozen-build worship, handoff opacity, or "it shipped therefore finished" drift.  
- **Context survivability governance** — compression integrity, checkpoint persistence, freeze-state memory, escalation memory, governance memory, and reconstruction survivability are reviewed per [`context-survivability-checklist.md`](context-survivability-checklist.md); record `CONTEXT SURVIVABILITY FINDINGS`, not blind continuation from summaries, compression without checkpoints, context laundering, or fake context completeness.  
- **Failure recovery governance** — trusted-state recovery, rollback integrity, freeze restoration, degraded-state handling, continuity restoration, recovery traceability, and resilience validation are reviewed per [`failure-recovery-checklist.md`](failure-recovery-checklist.md); record `FAILURE RECOVERY FINDINGS`, not blind rollback, panic patching, degraded-state denial, recovery opacity, or "it works again" false recovery.  
- **Cross-project transfer governance** — transfer compatibility, semantic portability, strategic fit, operational fit, governance portability, incompatibility escalation, and project identity are reviewed per [`cross-project-transfer-checklist.md`](cross-project-transfer-checklist.md); record `CROSS-PROJECT TRANSFER FINDINGS`, not blind pattern reuse, copied governance without validation, false analogy drift, or universal-solution thinking.  
- **Governance minimalism** — proportional governance, cognitive load, operational readability, checklist fatigue, process survivability, and governance-to-value review are checked per [`governance-minimalism-checklist.md`](governance-minimalism-checklist.md); record `GOVERNANCE MINIMALISM FINDINGS`, not governance inflation, ritualized QA, mandatory depth everywhere, or process-over-outcome thinking.  
- **Risk weighting governance** — severity proportionality, operational focus, escalation relevance, signal-to-noise clarity, risk layers, and prioritization drift are checked per [`risk-weighting-checklist.md`](risk-weighting-checklist.md); record `RISK WEIGHTING FINDINGS`, not equal-priority overload, false criticality, escalation spam, or "more warnings = safer system" thinking.  
- **Adaptive governance** — context-sensitive rigor, proportional process depth, adaptive QA depth, governance fit, contextual escalation, process scaling, and survivability balancing are checked per [`adaptive-governance-checklist.md`](adaptive-governance-checklist.md); record `ADAPTIVE GOVERNANCE FINDINGS`, not identical governance everywhere, maximum rigor by default, under-protection of critical work, or "more process always better" thinking.  
- **Governance economics** — operational cost awareness, governance efficiency, validation-cost QA, review allocation, sustainability balancing, governance ROI, and cost drift are checked per [`governance-economics-checklist.md`](governance-economics-checklist.md); record `GOVERNANCE ECONOMICS FINDINGS`, not governance cost blindness, validation-cost explosion, expensive low-value QA, or "more governance always safer" thinking.  
- **Cognitive load governance** — review readability, signal-to-noise clarity, reviewer sustainability, governance readability, cognitive survivability, and cognitive drift are checked per [`cognitive-load-checklist.md`](cognitive-load-checklist.md); record `COGNITIVE LOAD FINDINGS`, not endless reports, unreadable findings, review overload, signal burial, reviewer burnout, or "more detail always better" thinking.  
- **Governance compression** — operational modes, deployability, compression integrity, mode transitions, governance scalability, portability, and density scaling are checked per [`governance-compression-checklist.md`](governance-compression-checklist.md); record `GOVERNANCE COMPRESSION FINDINGS`, not one-mode governance, permanent critical-mode operation, deployment-hostile density, compression without integrity, or "maximum governance always safer" thinking.  
- **Reasoning visibility governance** — reasoning visibility, decision traceability, escalation explainability, prioritization transparency, uncertainty visibility, assumption disclosure, and traceable conclusions are checked per [`reasoning-visibility-checklist.md`](reasoning-visibility-checklist.md); record `REASONING VISIBILITY FINDINGS`, not black-box governance, recommendation without reasoning, hidden tradeoffs, or "trust the system" conclusions.  
- **Organizational memory governance** — institutional continuity, lesson survivability, operational wisdom, rediscovery avoidance, historical traceability, and continuity inheritance are checked per [`organizational-memory-checklist.md`](organizational-memory-checklist.md); record `ORGANIZATIONAL MEMORY FINDINGS`, not documentation-volume confidence, archive worship, tribal-memory dependence, or "start from scratch" culture.  
- **Governance evolution governance** — controlled evolution, refinement traceability, continuity-safe change, methodology review, adaptive survivability, and historical-lineage QA are checked per [`governance-evolution-checklist.md`](governance-evolution-checklist.md); record `GOVERNANCE EVOLUTION FINDINGS`, not governance fossilization, legacy-rule worship, uncontrolled methodology mutation, or "old process therefore correct" thinking.  
- **Meta-governance** — governance architecture integrity, cross-layer consistency, methodological coherence, layer-boundary clarity, contradiction survivability, governance topology, and architecture readability are checked per [`meta-governance-checklist.md`](meta-governance-checklist.md); record `META-GOVERNANCE FINDINGS`, not governance sprawl, duplicated methodology, cross-layer ambiguity, or "more layers = better governance" thinking.  
- **Trust calibration governance** — calibrated trust, confidence proportionality, uncertainty visibility, explainable reliability, credibility survivability, and trust traceability are checked per [`trust-calibration-checklist.md`](trust-calibration-checklist.md); record `TRUST CALIBRATION FINDINGS`, not confidence aesthetics, performative trust, hidden uncertainty, institutional overtrust, or "professional tone therefore trustworthy" thinking.  
- **One concern per phase** — do not style before structure is stable; do not bind JS before layout is stable.  
- **Scope anchors** — every prompt names `page_slug`, `block_id`, files touched ([`frontend-prompt-discipline-v0.md`](../../projects/mars-website-factory/frontend-prompt-discipline-v0.md)).  
- **Honest build claims** — run only documented scripts; else **SAFE UNKNOWN**. **Build fail → stale dist** — [frontend-production-invariants-v1.md](../../projects/mars-website-factory/frontend-production-invariants-v1.md) §7–§8.
- **No `dist/` edits** — inherit [`frontend-production-rules-v0.md`](../../projects/mars-website-factory/frontend-production-rules-v0.md) §2.
- **Production invariants** — breakpoints, container shell, FAQ/native `<details>`, typography ties: [frontend-production-invariants-v1.md](../../projects/mars-website-factory/frontend-production-invariants-v1.md).

---

## Freeze semantics

| State | Meaning |
|-------|---------|
| **Unfrozen** | Phase work in progress |
| **Frozen** | Section passed QA; only bugfix or approved change |
| **Unfreeze** | Requires explicit reason in REPORT (handoff update, defect, HITL) |

After freeze, adjacent-section work must include **anti-regression** spot check on frozen neighbors ([`qa-checklist.md`](qa-checklist.md)).

---

## Section sequencing

- Follow handoff **`section_map`** order unless operator re-scopes with documented reason.  
- Prefer completing **structure → freeze** for one section before starting the next section’s styling-heavy work.  
- Parallel sections only when handoff allows and freeze boundaries are clear per section.

---

## QA gates (Forge)

| Gate | When |
|------|------|
| **G1 — post-responsive** | Overlay: layout rhythm, overflow (current section) |
| **G2 — post-interaction** | Overlay: hooks, behavior smoke |
| **G3 — pre-freeze** | Full foundation QA checklist + handoff `QA_requirements` |
| **G5 — pre-freeze semantic** | [`semantic-source-lock.md`](semantic-source-lock.md) §6 — titles, meaning, entities, CTAs, no cross-version contamination; run **before** declaring section PASS/freeze |
| **Source interpretation QA — pre-freeze confidence** | [`source-interpretation-checklist.md`](source-interpretation-checklist.md) — observed / inferred / assumed / unknown separation, source confidence, ambiguity taxonomy, source contradiction handling; report as `SOURCE INTERPRETATION FINDINGS` |
| **Reconstruction fidelity QA — pre-freeze source-to-build fidelity** | [`reconstruction-fidelity-checklist.md`](reconstruction-fidelity-checklist.md) — source transfer, approximation transparency, hierarchy fidelity, semantic transfer, responsive fidelity, and fidelity survivability; report as `RECONSTRUCTION FIDELITY FINDINGS` |
| **Initialization / reset / bootstrap QA — pre-implementation and pre-freeze** | [`qa-checklist.md`](qa-checklist.md) — clean-start, stale residue, source-lock-before-build, reconstruction bootstrap, asset lifecycle, and reset traceability; report as `INITIALIZATION FINDINGS`, `WORKSPACE RESET FINDINGS`, `RECONSTRUCTION BOOTSTRAP FINDINGS`, `RECONSTRUCTION ASSET FINDINGS` |
| **Shell / first-screen / background QA — first viewport decomposition** | [`qa-checklist.md`](qa-checklist.md) — **HEADER != HERO**, shell continuity, header/hero/mobile-nav separation, background/overlay ownership, first-screen layer map; report as `LAYOUT SHELL FINDINGS`, `FIRST-SCREEN DECOMPOSITION FINDINGS`, `BACKGROUND OWNERSHIP FINDINGS` |
| **Terminal survivability / shell compatibility QA — validation command evidence** | [`qa-checklist.md`](qa-checklist.md) — PowerShell-safe separators, no bash-only syntax in Windows shell, shell type awareness, UTF-8 readability, console integrity, command portability, validation-command survivability; report as `TERMINAL SURVIVABILITY FINDINGS`, `SHELL COMPATIBILITY FINDINGS`, `ENCODING READABILITY FINDINGS` |
| **Commercial pressure / atmosphere / beautification QA — landing rhythm** | [`qa-checklist.md`](qa-checklist.md) — commercial density, landing momentum, atmosphere continuity, section language, anti-sterile UI, anti-SaaSification, source-intent protection; report as `COMMERCIAL DENSITY FINDINGS`, `LANDING PRESSURE FINDINGS`, `ATMOSPHERE CONTINUITY FINDINGS`, `SECTION LANGUAGE FINDINGS`, `BEAUTIFICATION DRIFT FINDINGS` |
| **Source lineage QA — pre-freeze provenance** | [`source-lineage-checklist.md`](source-lineage-checklist.md) — provenance integrity, authority chain, derivation disclosure, stale-lineage risk, transformation boundaries, and unknown-origin source handling; report as `SOURCE LINEAGE FINDINGS` |
| **G6 — pre-freeze visual reconciliation** | [`visual-reconciliation-checklist.md`](visual-reconciliation-checklist.md) — human-supervised **visual intent** read vs source; **after** G5, **before** final responsive closure + freeze |
| **G6 icon add-on — Font Awesome governance** | [`font-awesome-governance-checklist.md`](font-awesome-governance-checklist.md) — semantic icon matching, FA family/style consistency, optical rhythm, brand/custom exceptions; run when icons are present |
| **G7 — pre-freeze compositional structure** | [`composition-awareness-checklist.md`](composition-awareness-checklist.md) — **composition-vs-DOM** cluster read; **with** or **immediately after** G6; **not** silent regroup; structural change **human-approved** only |
| **Design intent QA — pre-freeze visual philosophy** | [`design-intent-checklist.md`](design-intent-checklist.md) — radius philosophy, surface hierarchy, CTA philosophy, UI weight, shadow/border restraint, SaaS contamination; report as `DESIGN INTENT FINDINGS` |
| **Design token QA — pre-freeze token intent** | [`design-token-checklist.md`](design-token-checklist.md) — semantic token intent, token hierarchy, aliases, override governance, responsive/state token integrity, token drift taxonomy; report as `DESIGN TOKEN FINDINGS` |
| **Implementation reliability QA — pre-freeze stability** | [`implementation-reliability-checklist.md`](implementation-reliability-checklist.md) — frontend stability, deterministic rebuilds, scoped fixes, override/include/breakpoint integrity, regression survivability, implementation drift taxonomy; report as `IMPLEMENTATION RELIABILITY FINDINGS` |
| **Cadence QA — pre-freeze narrative pacing** | [`cadence-governance-checklist.md`](cadence-governance-checklist.md) — cadence continuity, transition pacing, density-stack checks, footer closure, mobile cadence survivability; report as `CADENCE FINDINGS` |
| **Rhythm QA — pre-freeze cadence** | [`rhythm-governance-checklist.md`](rhythm-governance-checklist.md) — typography cadence, section spacing, density continuity, CTA/mobile/dark-light transition rhythm; report as `RHYTHM FINDINGS` |
| **Responsive intent QA — pre-freeze viewport fidelity** | [`responsive-intent-checklist.md`](responsive-intent-checklist.md) — hierarchy survival, mobile cadence, composition collapse, CTA collapse, stack integrity, collapse taxonomy; report as `RESPONSIVE INTENT FINDINGS` |
| **Content density QA — pre-freeze information pressure** | [`content-density-checklist.md`](content-density-checklist.md) — information pressure, scanning rhythm, proof density, trust-wall drift, overload taxonomy, CTA survival; report as `CONTENT DENSITY FINDINGS` |
| **Interaction intent QA — pre-freeze behavior fidelity** | [`interaction-intent-checklist.md`](interaction-intent-checklist.md) — interaction semantics, hover authority, CTA behavior consistency, motion restraint, dead zones, overload, contamination; report as `INTERACTION INTENT FINDINGS` |
| **State consistency QA — pre-freeze state fidelity** | [`state-consistency-checklist.md`](state-consistency-checklist.md) — hover/focus/active/disabled/loading/validation/success/error integrity, CTA state consistency, mobile state continuity, accessibility-state drift; report as `STATE CONSISTENCY FINDINGS` |
| **Accessibility intent QA — pre-freeze operational usability** | [`accessibility-intent-checklist.md`](accessibility-intent-checklist.md) — semantic accessibility, focus survivability, keyboard continuity, assistive predictability, contrast trust, mobile accessibility continuity, accessibility drift taxonomy; report as `ACCESSIBILITY FINDINGS` |
| **QA confidence QA — pre-freeze verification honesty** | [`qa-confidence-checklist.md`](qa-confidence-checklist.md) — evidence levels, scoped PASS/PARTIAL/FAIL discipline, proof boundaries, SAFE UNKNOWN visibility, and QA drift taxonomy; report as `QA CONFIDENCE FINDINGS` |
| **Human escalation QA — pre-freeze authority boundary** | [`human-escalation-checklist.md`](human-escalation-checklist.md) — escalation boundaries, stop conditions, contradiction escalation, HITL visibility, assumption thresholds, authority integrity, and escalation drift taxonomy; report as `HUMAN ESCALATION FINDINGS` |
| **Multi-agent coordination QA — pre-freeze responsibility boundary** | [`multi-agent-coordination-checklist.md`](multi-agent-coordination-checklist.md) — role separation, responsibility clarity, reviewer independence, validator integrity, escalation ownership, orchestration clarity, and multi-agent drift taxonomy; report as `MULTI-AGENT FINDINGS` |
| **Strategic intent QA — pre-freeze business continuity** | [`strategic-intent-checklist.md`](strategic-intent-checklist.md) — business priority, conversion hierarchy, proof hierarchy, operational trust, stakeholder intent, local optimization boundaries, and strategic drift taxonomy; report as `STRATEGIC INTENT FINDINGS` |
| **Temporal evolution QA — continuity / drift survivability** | [`temporal-evolution-checklist.md`](temporal-evolution-checklist.md) — freeze-state integrity, governed evolution, controlled overrides, iterative-change accumulation, version lineage, continuity checkpoints, and evolution drift taxonomy; report as `TEMPORAL EVOLUTION FINDINGS` |
| **Execution discipline QA — workflow survivability** | [`execution-discipline-checklist.md`](execution-discipline-checklist.md) — workflow discipline, checkpoint integrity, freeze-validation QA, execution-order QA, handoff stability, continuity checkpoints, and workflow drift taxonomy; report as `WORKFLOW DISCIPLINE FINDINGS` |
| **Production readiness QA — delivery survivability** | [`production-readiness-checklist.md`](production-readiness-checklist.md) — production readiness, handoff survivability, onboarding readability, maintainability continuity, future-edit safety, deployment survivability, and lifecycle survivability; report as `PRODUCTION READINESS FINDINGS` |
| **Context survivability QA — compression / reconstruction survivability** | [`context-survivability-checklist.md`](context-survivability-checklist.md) — compression integrity, checkpoint persistence, freeze-state memory, escalation memory, governance memory, continuity reconstruction, and context drift taxonomy; report as `CONTEXT SURVIVABILITY FINDINGS` |
| **Failure recovery QA — trusted-state / rollback / resilience** | [`failure-recovery-checklist.md`](failure-recovery-checklist.md) — trusted-state recovery, rollback integrity, freeze restoration, degraded-state handling, continuity restoration, recovery traceability, and recovery drift taxonomy; report as `FAILURE RECOVERY FINDINGS` |
| **Cross-project transfer QA — compatibility / portability** | [`cross-project-transfer-checklist.md`](cross-project-transfer-checklist.md) — transfer compatibility, semantic portability, strategic fit, operational fit, governance portability, incompatibility escalation, project identity, and transfer drift taxonomy; report as `CROSS-PROJECT TRANSFER FINDINGS` |
| **Governance minimalism QA — proportionality / readability** | [`governance-minimalism-checklist.md`](governance-minimalism-checklist.md) — proportional governance, cognitive load, operational readability, checklist fatigue, process survivability, governance-to-value review, and governance bloat taxonomy; report as `GOVERNANCE MINIMALISM FINDINGS` |
| **Risk weighting QA — prioritization / severity** | [`risk-weighting-checklist.md`](risk-weighting-checklist.md) — severity proportionality, operational focus, escalation relevance, signal-to-noise clarity, risk layers, and prioritization drift taxonomy; report as `RISK WEIGHTING FINDINGS` |
| **Adaptive governance QA — context-sensitive rigor / process scaling** | [`adaptive-governance-checklist.md`](adaptive-governance-checklist.md) — proportional process depth, adaptive QA depth, governance fit, contextual escalation, process scaling, survivability balancing, and adaptive drift taxonomy; report as `ADAPTIVE GOVERNANCE FINDINGS` |
| **Governance economics QA — operational cost awareness** | [`governance-economics-checklist.md`](governance-economics-checklist.md) — governance efficiency, validation-cost QA, review allocation, sustainability balancing, governance ROI, and cost drift taxonomy; report as `GOVERNANCE ECONOMICS FINDINGS` |
| **Cognitive load QA — review ergonomics / readability** | [`cognitive-load-checklist.md`](cognitive-load-checklist.md) — review readability, signal-to-noise clarity, reviewer sustainability, governance readability, cognitive survivability, and cognitive drift taxonomy; report as `COGNITIVE LOAD FINDINGS` |
| **Governance compression QA — operational modes / deployability** | [`governance-compression-checklist.md`](governance-compression-checklist.md) — operational mode, compression integrity, deployability, mode transitions, governance scalability, portability, and compression drift taxonomy; report as `GOVERNANCE COMPRESSION FINDINGS` |
| **Reasoning visibility QA — transparency / traceability** | [`reasoning-visibility-checklist.md`](reasoning-visibility-checklist.md) — reasoning visibility, decision traceability, escalation explainability, prioritization transparency, uncertainty visibility, assumption disclosure, and reasoning drift taxonomy; report as `REASONING VISIBILITY FINDINGS` |
| **Organizational memory QA — institutional knowledge / lesson survivability** | [`organizational-memory-checklist.md`](organizational-memory-checklist.md) — institutional continuity, lesson survivability, operational wisdom, rediscovery avoidance, historical traceability, continuity inheritance, and memory drift taxonomy; report as `ORGANIZATIONAL MEMORY FINDINGS` |
| **Governance evolution QA — controlled refinement / methodology survivability** | [`governance-evolution-checklist.md`](governance-evolution-checklist.md) — governance evolution, refinement traceability, continuity-safe change, methodology review, adaptive survivability, historical-lineage QA, and evolutionary drift taxonomy; report as `GOVERNANCE EVOLUTION FINDINGS` |
| **Meta-governance QA — architecture integrity / topology survivability** | [`meta-governance-checklist.md`](meta-governance-checklist.md) — governance architecture integrity, cross-layer consistency, methodological coherence, layer-boundary clarity, contradiction survivability, governance topology, and meta-governance drift taxonomy; report as `META-GOVERNANCE FINDINGS` |
| **Trust calibration QA — governance credibility / sustainable trust** | [`trust-calibration-checklist.md`](trust-calibration-checklist.md) — calibrated trust, confidence proportionality, uncertainty visibility, explainable reliability, credibility survivability, and trust drift taxonomy; report as `TRUST CALIBRATION FINDINGS` |
| **G4 — post-adjacent-edit** | Frozen-section regression spot check |

---

## Non-goals (inherit foundation + overlay)

- No autonomous deploy, orchestration, or runtime in `mars-runtime/**`.  
- No duplicate SoT for handoff, production rules, or gulp architecture.  
- No pixel-perfect / Figma diff automation in v0.  
- No framework/CMS migration without documented **STRUCTURE CHANGE**.
- No automatic UI AI, runtime design engine, or universal visual truth claims.
- No automatic clean-start engine, workspace reset automation, first-screen decomposer, background ownership detector, asset lifecycle manager, landing-pressure scorer, or beautification drift detector.
- No runtime terminal framework, shell abstraction runtime, CLI orchestration platform, autonomous shell adaptation, automatic encoding repair, universal shell compatibility, or guaranteed terminal integrity.
- No automatic responsive AI, runtime layout engine, or mandatory mobile aesthetic.
- No automatic readability engine, density scoring, SEO text maximizer, or universal content-density truth.
- No automated source understanding, CV interpretation, runtime interpretation AI, or universal design-reading truth.
- No runtime provenance engine, autonomous source-trust AI, immutable lineage guarantee, or universal provenance law.
- No runtime UX engine, autonomous interaction AI, universal motion truth, or mandatory animation style.
- No runtime UI state engine, automated accessibility AI, universal UI-state truth, or mandatory interaction-state aesthetics.
- No automated WCAG engine, runtime accessibility AI, universal accessibility truth, compliance certification, or mandatory accessibility aesthetics.
- No runtime token engine, autonomous design-system AI, universal token architecture, or automatic token enforcement.
- No runtime frontend reliability engine, autonomous repair AI, universal frontend architecture, or stack enforcement.
- No autonomous QA AI, runtime verification system, fake test engine, real-device lab claim, or universal QA truth.
- No autonomous governance AI, runtime approval engine, universal escalation law, fake self-approval, or self-governing autonomy.
- No runtime multi-agent orchestration, autonomous agent governance AI, universal multi-agent law, consensus truth engine, or self-governing agent swarm.
- No autonomous business AI, conversion-optimization engine, universal marketing truth, automatic strategic understanding, or self-optimizing CTA/proof system.
- No autonomous maintenance AI, runtime drift engine, universal frontend lifecycle law, or permanent architectural stability guarantee.
- No autonomous workflow AI, runtime orchestration, universal SDLC law, automatic checkpoint engine, or perfect operational stability claim.
- No autonomous maintenance AI, runtime deployment system, universal production law, or perfect maintainability claim.
- No autonomous memory AI, runtime persistence, universal memory law, automatic compression validator, or perfect continuity reconstruction claim.
- No autonomous self-healing AI, runtime recovery system, automatic rollback, universal disaster-recovery law, or perfect resilience claim.
- No autonomous transfer AI, automatic compatibility detection, universal reusable systems, universal frontend standards, or automatic governance portability claim.
- No autonomous simplification AI, automatic governance pruning, universal minimalism law, or perfect governance balance claim.
- No autonomous risk AI, scoring engine, universal severity law, automatic prioritization, or perfect risk weighting claim.
- No autonomous governance adaptation AI, runtime policy engine, universal rigor law, automatic QA-depth selection, identical workflow law, or perfect contextual scaling claim.
- No autonomous governance optimization AI, runtime cost engine, universal governance economics law, automatic cost scoring, automatic QA allocation, or perfect efficiency balancing claim.
- No cognitive-monitoring AI, runtime attention system, automatic readability scoring, universal cognition law, report-optimization engine, or perfect readability claim.
- No autonomous governance scaling AI, runtime governance orchestrator, universal operational mode system, automatic report compression, automatic QA-depth allocation, or perfect deployability claim.
- No hidden chain-of-thought exposure, autonomous reasoning engine, universal transparency law, automatic explainability scoring, or perfect explainability claim.
- No autonomous institutional AI, permanent memory system, universal organizational law, automatic lesson extraction, or perfect historical continuity claim.
- No autonomous self-improving AI, runtime governance mutation, automatic methodology rewriting, universal evolution law, or perfect adaptability claim.
- No autonomous governance management AI, runtime governance engine, universal governance topology, automatic contradiction resolver, or perfect architectural coherence claim.
- No autonomous trust engine, runtime credibility scoring, universal trust law, automatic reliability certification, or perfect reliability claim.
- No autonomous design-reading AI, runtime fidelity scoring, automatic reconstruction validator, universal reconstruction law, or perfect source-fidelity claim.

---

## SoT and boundaries

- **Agent input contracts (governance):** explicit required/forbidden inputs and quarantine posture — [../../governance/agent-input-contracts.md](../../governance/agent-input-contracts.md); template [../../templates/agent-input-contract-template.md](../../templates/agent-input-contract-template.md).  
- **Foundation SoT:** [`../frontend-gulp-agent/`](../frontend-gulp-agent/) + Website Factory contracts.  
- **Forge SoT:** this pack’s pipeline, overlay QA, freeze semantics, and **semantic source lock** ([`semantic-source-lock.md`](semantic-source-lock.md)) — methodology only, not a second handoff contract.  
- **Registry:** [`../registry.md`](../registry.md) §4.1 — `mars_forge_frontend_agent`.  
- **Not** implemented in `mars-runtime`.

---

## REPORT expectations (extends foundation)

Include subsection **Forge execution**:

- Phases completed (1–7) for scope  
- Freeze state per `block_id`  
- Drift risks found / deferred  
- Overlay QA pass/fail/partial  
- **Semantic gate G5** outcome (semantic-source-lock checklist)  
- **SOURCE INTERPRETATION FINDINGS** — confidence, ambiguity, missing source, source contradiction, and approximation disclosure outcome ([`source-interpretation-checklist.md`](source-interpretation-checklist.md))  
- **RECONSTRUCTION FIDELITY FINDINGS** — source-to-build fidelity, hierarchy fidelity, semantic transfer, approximation transparency, reconstruction confidence, and fidelity survivability outcome ([`reconstruction-fidelity-checklist.md`](reconstruction-fidelity-checklist.md))  
- **INITIALIZATION FINDINGS / WORKSPACE RESET FINDINGS / RECONSTRUCTION BOOTSTRAP FINDINGS / RECONSTRUCTION ASSET FINDINGS** — clean-start state, stale residue, source-lock-before-build, pre-implementation audit, and asset lifecycle outcome ([`qa-checklist.md`](qa-checklist.md))  
- **LAYOUT SHELL FINDINGS / FIRST-SCREEN DECOMPOSITION FINDINGS / BACKGROUND OWNERSHIP FINDINGS** — **HEADER != HERO**, shell continuity, first-screen layer ownership, background/overlay/media ownership outcome ([`qa-checklist.md`](qa-checklist.md))  
- **TERMINAL SURVIVABILITY FINDINGS / SHELL COMPATIBILITY FINDINGS / ENCODING READABILITY FINDINGS** — shell type, PowerShell-safe command discipline, command portability, parser-error handling, terminal readability, UTF-8 continuity, console integrity, and display-vs-file corruption outcome ([`qa-checklist.md`](qa-checklist.md))  
- **COMMERCIAL DENSITY FINDINGS / LANDING PRESSURE FINDINGS / ATMOSPHERE CONTINUITY FINDINGS / SECTION LANGUAGE FINDINGS / BEAUTIFICATION DRIFT FINDINGS** — operational pressure, landing momentum, environment continuity, section language, anti-SaaSification, and source-intent protection outcome ([`qa-checklist.md`](qa-checklist.md))  
- **SOURCE LINEAGE FINDINGS** — provenance integrity, authority chain, derivation disclosure, stale lineage, transformation boundaries, unknown-origin source, and lineage readability outcome ([`source-lineage-checklist.md`](source-lineage-checklist.md))  
- **Visual reconciliation gate G6** outcome ([`visual-reconciliation-checklist.md`](visual-reconciliation-checklist.md))  
- **Icon governance findings** when icons are present ([`font-awesome-governance-checklist.md`](font-awesome-governance-checklist.md))  
- **Compositional structure gate G7** outcome ([`composition-awareness-checklist.md`](composition-awareness-checklist.md))  
- **DESIGN INTENT FINDINGS** — radius/surface/CTA/UI-weight/shadow/SaaS-contamination outcome ([`design-intent-checklist.md`](design-intent-checklist.md))  
- **DESIGN TOKEN FINDINGS** — semantic token intent, hierarchy, aliases, overrides, responsive/state token integrity, token drift, and design-system trust outcome ([`design-token-checklist.md`](design-token-checklist.md))  
- **IMPLEMENTATION RELIABILITY FINDINGS** — frontend stability, deterministic rebuild, scoped-fix, override/include/breakpoint integrity, regression survivability, and implementation readability outcome ([`implementation-reliability-checklist.md`](implementation-reliability-checklist.md))  
- **CADENCE FINDINGS** — inter-screen narrative pacing outcome ([`cadence-governance-checklist.md`](cadence-governance-checklist.md))  
- **RHYTHM FINDINGS** — typography cadence + vertical rhythm outcome ([`rhythm-governance-checklist.md`](rhythm-governance-checklist.md))  
- **RESPONSIVE INTENT FINDINGS** — viewport hierarchy, composition collapse, mobile cadence, CTA collapse, stack integrity, and collapse taxonomy outcome ([`responsive-intent-checklist.md`](responsive-intent-checklist.md))  
- **CONTENT DENSITY FINDINGS** — information pressure, scanning rhythm, proof pacing, trust density, overload taxonomy, CTA survival outcome ([`content-density-checklist.md`](content-density-checklist.md))  
- **INTERACTION INTENT FINDINGS** — interaction semantics, hover authority, CTA behavior consistency, motion restraint, dead zones, overload, and contamination outcome ([`interaction-intent-checklist.md`](interaction-intent-checklist.md))  
- **STATE CONSISTENCY FINDINGS** — hover/focus/active/disabled/loading/validation/success/error integrity, CTA state consistency, mobile state continuity, and accessibility-state drift outcome ([`state-consistency-checklist.md`](state-consistency-checklist.md))  
- **ACCESSIBILITY FINDINGS** — semantic accessibility, focus survivability, keyboard continuity, assistive predictability, contrast trust, form seriousness, mobile accessibility continuity, and accessibility drift outcome ([`accessibility-intent-checklist.md`](accessibility-intent-checklist.md))  
- **QA CONFIDENCE FINDINGS** — evidence levels, scoped PASS/PARTIAL/FAIL boundaries, inferred/assumed/unknown validation, verification traceability, and QA drift taxonomy outcome ([`qa-confidence-checklist.md`](qa-confidence-checklist.md))  
- **HUMAN ESCALATION FINDINGS** — decision boundary level, stop conditions, contradiction escalation, HITL visibility, assumption thresholds, authority integrity, and escalation drift outcome ([`human-escalation-checklist.md`](human-escalation-checklist.md))  
- **MULTI-AGENT FINDINGS** — responsibility boundaries, reviewer independence, validator integrity, escalation ownership, orchestration clarity, handoff survivability, and fake-consensus risk outcome ([`multi-agent-coordination-checklist.md`](multi-agent-coordination-checklist.md))  
- **STRATEGIC INTENT FINDINGS** — business priority, conversion hierarchy, proof hierarchy, operational trust, stakeholder intent, local optimization boundary, and strategic drift outcome ([`strategic-intent-checklist.md`](strategic-intent-checklist.md))  
- **TEMPORAL EVOLUTION FINDINGS** — freeze-state integrity, version lineage, governed evolution, controlled override pressure, iterative-change accumulation, continuity checkpoint, and project drift survivability outcome ([`temporal-evolution-checklist.md`](temporal-evolution-checklist.md))  
- **WORKFLOW DISCIPLINE FINDINGS** — task-boundary integrity, execution order, checkpoint integrity, freeze validation, handoff stability, continuity checkpoint, parallel/multi-session risk, and workflow drift outcome ([`execution-discipline-checklist.md`](execution-discipline-checklist.md))  
- **PRODUCTION READINESS FINDINGS** — delivery survivability, handoff survivability, onboarding readability, maintainability continuity, future-edit safety, deployment survivability, frozen-build survivability, and lifecycle survivability outcome ([`production-readiness-checklist.md`](production-readiness-checklist.md))  
- **CONTEXT SURVIVABILITY FINDINGS** — compression integrity, checkpoint persistence, freeze-state memory, escalation memory, governance memory, continuity reconstruction, context drift, and long-chain operational continuity outcome ([`context-survivability-checklist.md`](context-survivability-checklist.md))  
- **FAILURE RECOVERY FINDINGS** — trusted-state recovery, rollback integrity, freeze restoration, degraded-state handling, continuity restoration, recovery traceability, and resilience validation outcome ([`failure-recovery-checklist.md`](failure-recovery-checklist.md))  
- **CROSS-PROJECT TRANSFER FINDINGS** — transfer compatibility, semantic portability, strategic fit, operational fit, governance portability, incompatibility escalation, project identity, rejected assumptions, and transfer drift outcome ([`cross-project-transfer-checklist.md`](cross-project-transfer-checklist.md))  
- **GOVERNANCE MINIMALISM FINDINGS** — governance proportionality, cognitive load, operational readability, checklist fatigue, process survivability, governance-to-value ratio, and governance bloat outcome ([`governance-minimalism-checklist.md`](governance-minimalism-checklist.md))  
- **RISK WEIGHTING FINDINGS** — severity proportionality, operational focus, escalation relevance, signal-to-noise ratio, risk layer distribution, prioritization drift, and critical-path visibility outcome ([`risk-weighting-checklist.md`](risk-weighting-checklist.md))  
- **ADAPTIVE GOVERNANCE FINDINGS** — discipline layer, scaling decision, adaptive QA depth, contextual escalation depth, governance-context fit, process-scaling drift, and survivability balance outcome ([`adaptive-governance-checklist.md`](adaptive-governance-checklist.md))  
- **GOVERNANCE ECONOMICS FINDINGS** — cost layer, cost driver, governance efficiency, validation-cost QA, review allocation, survivability-to-cost balance, governance ROI, and cost drift outcome ([`governance-economics-checklist.md`](governance-economics-checklist.md))  
- **COGNITIVE LOAD FINDINGS** — review layer, load driver, critical signal preservation, review-readability QA, signal-to-noise QA, reviewer sustainability, governance readability, and cognitive drift outcome ([`cognitive-load-checklist.md`](cognitive-load-checklist.md))  
- **GOVERNANCE COMPRESSION FINDINGS** — operational mode, mode rationale, compression posture, deployability QA, compression integrity, mode transition, scalability/portability, and compression drift outcome ([`governance-compression-checklist.md`](governance-compression-checklist.md))  
- **REASONING VISIBILITY FINDINGS** — reasoning visibility, decision traceability, escalation explainability, prioritization transparency, uncertainty visibility, assumption disclosure, tradeoff disclosure, and traceable-conclusion outcome ([`reasoning-visibility-checklist.md`](reasoning-visibility-checklist.md))  
- **ORGANIZATIONAL MEMORY FINDINGS** — lesson survivability, operational wisdom, rediscovery avoidance, historical traceability, institutional readability, continuity inheritance, and memory drift outcome ([`organizational-memory-checklist.md`](organizational-memory-checklist.md))  
- **GOVERNANCE EVOLUTION FINDINGS** — governance evolution, refinement traceability, continuity-safe change, methodology review, adaptive survivability, historical-lineage QA, and evolutionary drift outcome ([`governance-evolution-checklist.md`](governance-evolution-checklist.md))  
- **META-GOVERNANCE FINDINGS** — governance architecture integrity, cross-layer consistency, layer-boundary clarity, contradiction survivability, governance topology, architecture readability, and meta-governance drift outcome ([`meta-governance-checklist.md`](meta-governance-checklist.md))  
- **TRUST CALIBRATION FINDINGS** — trust claim, evidence basis, confidence adjustment, uncertainty visibility, explainable reliability, credibility survivability, and trust drift outcome ([`trust-calibration-checklist.md`](trust-calibration-checklist.md))  
- Pointer to foundation QA outcome  

Use foundation [`reporting.md`](../frontend-gulp-agent/reporting.md) for full REPORT shape.
