# Workflow — MARS Forge (deterministic overlay v0)

Forge **wraps** the foundation workflow — it does **not** replace [`../frontend-gulp-agent/workflow.md`](../frontend-gulp-agent/workflow.md).

**Operator flow:**

1. Run foundation steps **1–3** (handoff inspect, target repo inspect, plan slice).  
2. Run Forge **phases 1–7** below for the slice (inside foundation “implement source”).  
3. Run foundation steps **5–9** (build, foundation QA, report, HITL, checkpoint).

**Lane discipline:** production execution lane per [`../../governance/parallel-cursor-chat-work-mode-v0.md`](../../governance/parallel-cursor-chat-work-mode-v0.md).

**Semantic charter:** before phase 1, confirm the prompt includes the **active design version**, canonical/forbidden paths, and workspace per [`semantic-source-lock.md`](semantic-source-lock.md) §1. **Validation builds** should follow §5 there (screen-by-screen: source → visual reading → **source interpretation confidence** → semantic extraction → content lock → implementation → semantic QA → **visual reconciliation (G6)** → **compositional structure (G7)** → design intent QA → design token QA → implementation reliability QA → cadence QA → rhythm QA → responsive intent QA → content density QA → interaction intent QA → state consistency QA → accessibility intent QA → QA confidence QA → human escalation QA → multi-agent coordination QA → strategic intent QA → cross-project transfer QA when prior-project knowledge influences the scope → final responsive QA → freeze), not parallel guessing across versions. **Source interpretation QA** — [`source-interpretation-checklist.md`](source-interpretation-checklist.md) (`SOURCE INTERPRETATION FINDINGS`); **Visual reconciliation** — [`visual-reconciliation-checklist.md`](visual-reconciliation-checklist.md) (gate **G6**); **Font Awesome icon governance** — [`font-awesome-governance-checklist.md`](font-awesome-governance-checklist.md) (G6 add-on); **compositional structure** — [`composition-awareness-checklist.md`](composition-awareness-checklist.md) (gate **G7**); **design intent governance** — [`design-intent-checklist.md`](design-intent-checklist.md) (`DESIGN INTENT FINDINGS`); **design token intelligence governance** — [`design-token-checklist.md`](design-token-checklist.md) (`DESIGN TOKEN FINDINGS`); **implementation reliability governance** — [`implementation-reliability-checklist.md`](implementation-reliability-checklist.md) (`IMPLEMENTATION RELIABILITY FINDINGS`); **cadence governance** — [`cadence-governance-checklist.md`](cadence-governance-checklist.md) (inter-screen narrative pacing); **rhythm governance** — [`rhythm-governance-checklist.md`](rhythm-governance-checklist.md) (typography cadence + vertical rhythm); **responsive intent governance** — [`responsive-intent-checklist.md`](responsive-intent-checklist.md) (`RESPONSIVE INTENT FINDINGS`); **content density governance** — [`content-density-checklist.md`](content-density-checklist.md) (`CONTENT DENSITY FINDINGS`); **interaction intent governance** — [`interaction-intent-checklist.md`](interaction-intent-checklist.md) (`INTERACTION INTENT FINDINGS`); **state consistency governance** — [`state-consistency-checklist.md`](state-consistency-checklist.md) (`STATE CONSISTENCY FINDINGS`); **accessibility intent governance** — [`accessibility-intent-checklist.md`](accessibility-intent-checklist.md) (`ACCESSIBILITY FINDINGS`); **QA confidence governance** — [`qa-confidence-checklist.md`](qa-confidence-checklist.md) (`QA CONFIDENCE FINDINGS`); **human escalation governance** — [`human-escalation-checklist.md`](human-escalation-checklist.md) (`HUMAN ESCALATION FINDINGS`); **multi-agent coordination governance** — [`multi-agent-coordination-checklist.md`](multi-agent-coordination-checklist.md) (`MULTI-AGENT FINDINGS`); **strategic intent governance** — [`strategic-intent-checklist.md`](strategic-intent-checklist.md) (`STRATEGIC INTENT FINDINGS`); **cross-project transfer governance** — [`cross-project-transfer-checklist.md`](cross-project-transfer-checklist.md) (`CROSS-PROJECT TRANSFER FINDINGS`); methodology — [`../../projects/mars-website-factory/source-interpretation-governance.md`](../../projects/mars-website-factory/source-interpretation-governance.md), [`../../projects/mars-website-factory/source-confidence-model.md`](../../projects/mars-website-factory/source-confidence-model.md), [`../../projects/mars-website-factory/source-ambiguity-taxonomy.md`](../../projects/mars-website-factory/source-ambiguity-taxonomy.md), [`../../projects/mars-website-factory/visual-reconciliation-layer.md`](../../projects/mars-website-factory/visual-reconciliation-layer.md), [`../../projects/mars-website-factory/font-awesome-governance-layer.md`](../../projects/mars-website-factory/font-awesome-governance-layer.md), [`../../projects/mars-website-factory/compositional-structure-awareness.md`](../../projects/mars-website-factory/compositional-structure-awareness.md), [`../../projects/mars-website-factory/design-system-intent-governance.md`](../../projects/mars-website-factory/design-system-intent-governance.md), [`../../projects/mars-website-factory/design-token-intelligence-governance.md`](../../projects/mars-website-factory/design-token-intelligence-governance.md), [`../../projects/mars-website-factory/token-semantic-layer-model.md`](../../projects/mars-website-factory/token-semantic-layer-model.md), [`../../projects/mars-website-factory/token-drift-taxonomy.md`](../../projects/mars-website-factory/token-drift-taxonomy.md), [`../../projects/mars-website-factory/implementation-reliability-governance.md`](../../projects/mars-website-factory/implementation-reliability-governance.md), [`../../projects/mars-website-factory/frontend-stability-model.md`](../../projects/mars-website-factory/frontend-stability-model.md), [`../../projects/mars-website-factory/implementation-drift-taxonomy.md`](../../projects/mars-website-factory/implementation-drift-taxonomy.md), [`../../projects/mars-website-factory/ui-weight-distribution-model.md`](../../projects/mars-website-factory/ui-weight-distribution-model.md), [`../../projects/mars-website-factory/cta-philosophy-governance.md`](../../projects/mars-website-factory/cta-philosophy-governance.md), [`../../projects/mars-website-factory/canonical-vertical-cadence-system.md`](../../projects/mars-website-factory/canonical-vertical-cadence-system.md), [`../../projects/mars-website-factory/cadence-tier-model.md`](../../projects/mars-website-factory/cadence-tier-model.md), [`../../projects/mars-website-factory/typography-rhythm-governance.md`](../../projects/mars-website-factory/typography-rhythm-governance.md), [`../../projects/mars-website-factory/vertical-rhythm-governance.md`](../../projects/mars-website-factory/vertical-rhythm-governance.md), [`../../projects/mars-website-factory/responsive-intent-governance.md`](../../projects/mars-website-factory/responsive-intent-governance.md), [`../../projects/mars-website-factory/content-density-governance.md`](../../projects/mars-website-factory/content-density-governance.md), [`../../projects/mars-website-factory/interaction-intent-governance.md`](../../projects/mars-website-factory/interaction-intent-governance.md), [`../../projects/mars-website-factory/state-behavioral-consistency-governance.md`](../../projects/mars-website-factory/state-behavioral-consistency-governance.md), [`../../projects/mars-website-factory/accessibility-intent-governance.md`](../../projects/mars-website-factory/accessibility-intent-governance.md), [`../../projects/mars-website-factory/qa-confidence-governance.md`](../../projects/mars-website-factory/qa-confidence-governance.md), [`../../projects/mars-website-factory/human-escalation-governance.md`](../../projects/mars-website-factory/human-escalation-governance.md), [`../../projects/mars-website-factory/multi-agent-coordination-governance.md`](../../projects/mars-website-factory/multi-agent-coordination-governance.md), [`../../projects/mars-website-factory/strategic-intent-governance.md`](../../projects/mars-website-factory/strategic-intent-governance.md), [`../../projects/mars-website-factory/cross-project-transfer-governance.md`](../../projects/mars-website-factory/cross-project-transfer-governance.md).

**Source lineage QA:** run [`source-lineage-checklist.md`](source-lineage-checklist.md) when provenance integrity, authority chain, derivation disclosure, stale-lineage risk, transformation boundaries, or unknown-origin source affects implementation; record `SOURCE LINEAGE FINDINGS` per [`../../projects/mars-website-factory/knowledge-provenance-governance.md`](../../projects/mars-website-factory/knowledge-provenance-governance.md).

**Font Awesome bootstrap readiness:** when iconography may be needed, decide FA readiness before Forge phase 1 section implementation. Inspect `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`; prepare the project-local FA delivery structure early; for CSS+webfont delivery use real `woff2` and `woff`, preserve `css/` to `webfonts/` `@font-face` paths, avoid SVG-font-only delivery, and start icon choice from semantic role/meaning rather than visual guesswork.

**Reconstruction fidelity QA:** run [`reconstruction-fidelity-checklist.md`](reconstruction-fidelity-checklist.md) when source-to-build fidelity, design-intent transfer, approximation transparency, hierarchy fidelity, semantic transfer, responsive fidelity, or fidelity survivability affects implementation; record `RECONSTRUCTION FIDELITY FINDINGS` per [`../../projects/mars-website-factory/design-intent-transfer-governance.md`](../../projects/mars-website-factory/design-intent-transfer-governance.md).

**Initialization / reset / bootstrap QA:** before reconstruction implementation, use [`qa-checklist.md`](qa-checklist.md) to review clean-start state, stale workspace residue, source-lock-before-build, reconstruction bootstrap, reset traceability, and asset lifecycle; record `INITIALIZATION FINDINGS`, `WORKSPACE RESET FINDINGS`, `RECONSTRUCTION BOOTSTRAP FINDINGS`, and `RECONSTRUCTION ASSET FINDINGS` per [`../../projects/mars-website-factory/initialization-governance.md`](../../projects/mars-website-factory/initialization-governance.md), [`../../projects/mars-website-factory/workspace-reset-governance.md`](../../projects/mars-website-factory/workspace-reset-governance.md), [`../../projects/mars-website-factory/reconstruction-bootstrap-governance.md`](../../projects/mars-website-factory/reconstruction-bootstrap-governance.md), and [`../../projects/mars-website-factory/reconstruction-asset-lifecycle-governance.md`](../../projects/mars-website-factory/reconstruction-asset-lifecycle-governance.md).

**Shell / first-screen / background QA:** when the opening viewport, header, hero, background, overlay, mobile navigation, or conversion environment is in scope, use [`qa-checklist.md`](qa-checklist.md) to enforce **HEADER != HERO** and first-screen layer ownership; record `LAYOUT SHELL FINDINGS`, `FIRST-SCREEN DECOMPOSITION FINDINGS`, and `BACKGROUND OWNERSHIP FINDINGS` per [`../../projects/mars-website-factory/layout-shell-governance.md`](../../projects/mars-website-factory/layout-shell-governance.md), [`../../projects/mars-website-factory/first-screen-decomposition-model.md`](../../projects/mars-website-factory/first-screen-decomposition-model.md), and [`../../projects/mars-website-factory/background-ownership-governance.md`](../../projects/mars-website-factory/background-ownership-governance.md).

**Terminal survivability / shell compatibility QA:** when validation commands, terminal evidence, PowerShell execution, UTF-8 rendering, live-output readability, or command portability affects implementation or reporting, use [`qa-checklist.md`](qa-checklist.md); record `TERMINAL SURVIVABILITY FINDINGS`, `SHELL COMPATIBILITY FINDINGS`, and `ENCODING READABILITY FINDINGS` per [`../../projects/mars-website-factory/terminal-survivability-governance.md`](../../projects/mars-website-factory/terminal-survivability-governance.md), [`../../projects/mars-website-factory/shell-compatibility-model.md`](../../projects/mars-website-factory/shell-compatibility-model.md), and [`../../projects/mars-website-factory/encoding-drift-taxonomy.md`](../../projects/mars-website-factory/encoding-drift-taxonomy.md).

**Commercial pressure / atmosphere / beautification QA:** when landing rhythm, industrial pressure, atmosphere, section language, or clean-UI modernization affects the scope, use [`qa-checklist.md`](qa-checklist.md); record `COMMERCIAL DENSITY FINDINGS`, `LANDING PRESSURE FINDINGS`, `ATMOSPHERE CONTINUITY FINDINGS`, `SECTION LANGUAGE FINDINGS`, and `BEAUTIFICATION DRIFT FINDINGS` per [`../../projects/mars-website-factory/commercial-density-governance.md`](../../projects/mars-website-factory/commercial-density-governance.md), [`../../projects/mars-website-factory/commercial-landing-pressure-model.md`](../../projects/mars-website-factory/commercial-landing-pressure-model.md), [`../../projects/mars-website-factory/atmosphere-continuity-governance.md`](../../projects/mars-website-factory/atmosphere-continuity-governance.md), [`../../projects/mars-website-factory/section-language-governance.md`](../../projects/mars-website-factory/section-language-governance.md), and [`../../projects/mars-website-factory/beautification-drift-governance.md`](../../projects/mars-website-factory/beautification-drift-governance.md).

**Strategic intent QA:** run [`strategic-intent-checklist.md`](strategic-intent-checklist.md) when business priority, conversion hierarchy, proof hierarchy, operational trust, stakeholder intent, or local optimization boundaries affect implementation; record `STRATEGIC INTENT FINDINGS` per [`../../projects/mars-website-factory/strategic-intent-governance.md`](../../projects/mars-website-factory/strategic-intent-governance.md).

**Temporal evolution QA:** run [`temporal-evolution-checklist.md`](temporal-evolution-checklist.md) when freeze-state integrity, version lineage, cumulative edits, override history, modernization, or long-term continuity affect implementation; record `TEMPORAL EVOLUTION FINDINGS` per [`../../projects/mars-website-factory/temporal-evolution-governance.md`](../../projects/mars-website-factory/temporal-evolution-governance.md).

**Execution discipline QA:** run [`execution-discipline-checklist.md`](execution-discipline-checklist.md) when workflow discipline, checkpoint integrity, freeze-validation state, execution order, handoff stability, continuity checkpoints, unsafe parallel modification, or context-loss risk affects implementation; record `WORKFLOW DISCIPLINE FINDINGS` per [`../../projects/mars-website-factory/operational-workflow-governance.md`](../../projects/mars-website-factory/operational-workflow-governance.md).

**Production readiness QA:** run [`production-readiness-checklist.md`](production-readiness-checklist.md) when delivery survivability, handoff-survivability QA, onboarding-readability QA, maintainability QA, future-edit QA, deployment-survivability QA, frozen-build survivability, or lifecycle-survivability QA affects implementation or reporting; record `PRODUCTION READINESS FINDINGS` per [`../../projects/mars-website-factory/production-readiness-governance.md`](../../projects/mars-website-factory/production-readiness-governance.md).

**Context survivability QA:** run [`context-survivability-checklist.md`](context-survivability-checklist.md) when compressed context, summaries, checkpoint persistence, freeze-state memory, escalation memory, governance memory, or continuity reconstruction affects implementation; record `CONTEXT SURVIVABILITY FINDINGS` per [`../../projects/mars-website-factory/context-survivability-governance.md`](../../projects/mars-website-factory/context-survivability-governance.md).

**Failure recovery QA:** run [`failure-recovery-checklist.md`](failure-recovery-checklist.md) when trusted-state recovery, rollback integrity, freeze restoration, degraded-state handling, continuity restoration, panic-fix contamination, or recovery traceability affects implementation; record `FAILURE RECOVERY FINDINGS` per [`../../projects/mars-website-factory/failure-recovery-governance.md`](../../projects/mars-website-factory/failure-recovery-governance.md).

**Cross-project transfer QA:** run [`cross-project-transfer-checklist.md`](cross-project-transfer-checklist.md) when prior-project lessons, templates, governance rules, implementation patterns, visual treatments, or transfer assumptions affect implementation; record `CROSS-PROJECT TRANSFER FINDINGS` per [`../../projects/mars-website-factory/cross-project-transfer-governance.md`](../../projects/mars-website-factory/cross-project-transfer-governance.md).

**Governance minimalism QA:** run [`governance-minimalism-checklist.md`](governance-minimalism-checklist.md) when governance volume, checklist fatigue, process readability, finding sprawl, methodology weight, or governance-to-value risk affects implementation or reporting; record `GOVERNANCE MINIMALISM FINDINGS` per [`../../projects/mars-website-factory/governance-minimalism.md`](../../projects/mars-website-factory/governance-minimalism.md).

**Risk weighting QA:** run [`risk-weighting-checklist.md`](risk-weighting-checklist.md) when findings are numerous, severity is unclear, escalation volume is rising, cosmetic issues risk crowding out critical issues, or report focus affects freeze confidence; record `RISK WEIGHTING FINDINGS` per [`../../projects/mars-website-factory/governance-prioritization.md`](../../projects/mars-website-factory/governance-prioritization.md).

**Adaptive governance QA:** run [`adaptive-governance-checklist.md`](adaptive-governance-checklist.md) when task criticality, QA depth, escalation level, governance weight, context mismatch, or survivability balancing affects implementation or reporting; record `ADAPTIVE GOVERNANCE FINDINGS` per [`../../projects/mars-website-factory/adaptive-governance.md`](../../projects/mars-website-factory/adaptive-governance.md).

**Governance economics QA:** run [`governance-economics-checklist.md`](governance-economics-checklist.md) when governance cost, review effort, QA depth, validation volume, process overhead, survivability cost, governance ROI, or operational sustainability affects implementation or reporting; record `GOVERNANCE ECONOMICS FINDINGS` per [`../../projects/mars-website-factory/governance-economics.md`](../../projects/mars-website-factory/governance-economics.md).

**Cognitive load QA:** run [`cognitive-load-checklist.md`](cognitive-load-checklist.md) when report length, finding volume, governance density, review fatigue, signal-to-noise clarity, reviewer sustainability, or governance readability affects implementation or reporting; record `COGNITIVE LOAD FINDINGS` per [`../../projects/mars-website-factory/cognitive-load-governance.md`](../../projects/mars-website-factory/cognitive-load-governance.md).

**Governance compression QA:** run [`governance-compression-checklist.md`](governance-compression-checklist.md) when operational mode, governance deployability, report density, compression integrity, mode transitions, governance portability, or scalable governance depth affects implementation or reporting; record `GOVERNANCE COMPRESSION FINDINGS` per [`../../projects/mars-website-factory/governance-compression-governance.md`](../../projects/mars-website-factory/governance-compression-governance.md).

**Reasoning visibility QA:** run [`reasoning-visibility-checklist.md`](reasoning-visibility-checklist.md) when recommendations, escalation decisions, prioritization, QA confidence, SAFE UNKNOWN, freeze posture, or final conclusions need reviewable rationale; record `REASONING VISIBILITY FINDINGS` per [`../../projects/mars-website-factory/decision-transparency-governance.md`](../../projects/mars-website-factory/decision-transparency-governance.md).

**Organizational memory QA:** run [`organizational-memory-checklist.md`](organizational-memory-checklist.md) when reusable lessons, prior decisions, repeated mistakes, historical traceability, institutional readability, rediscovery risk, or continuity inheritance affect implementation or reporting; record `ORGANIZATIONAL MEMORY FINDINGS` per [`../../projects/mars-website-factory/organizational-memory-governance.md`](../../projects/mars-website-factory/organizational-memory-governance.md).

**Governance evolution QA:** run [`governance-evolution-checklist.md`](governance-evolution-checklist.md) when methodology age, governance stagnation, repeated rule friction, legacy assumptions, process redesign, or governance renewal affects implementation or reporting; record `GOVERNANCE EVOLUTION FINDINGS` per [`../../projects/mars-website-factory/governance-evolution-governance.md`](../../projects/mars-website-factory/governance-evolution-governance.md).

**Meta-governance QA:** run [`meta-governance-checklist.md`](meta-governance-checklist.md) when governance-layer conflicts, overlapping governance domains, contradictory methodology, duplicated concepts, governance graph instability, or architecture readability affects implementation or reporting; record `META-GOVERNANCE FINDINGS` per [`../../projects/mars-website-factory/meta-governance-integrity.md`](../../projects/mars-website-factory/meta-governance-integrity.md).

**Trust calibration QA:** run [`trust-calibration-checklist.md`](trust-calibration-checklist.md) when governance confidence, perceived reliability, uncertainty visibility, escalation confidence, institutional trust, or credibility survivability affects implementation or reporting; record `TRUST CALIBRATION FINDINGS` per [`../../projects/mars-website-factory/trust-calibration-governance.md`](../../projects/mars-website-factory/trust-calibration-governance.md).

---

## Forge phases (deterministic)

### 1. Structure

| | |
|--|--|
| **Purpose** | Correct semantic skeleton and include graph for `block_id` |
| **Validation** | Partial resolves; heading order; landmarks; matches `section_map` / `partials_mapping` |
| **Drift prevention** | Blocks styling wrong DOM or wrong hierarchy |

### 2. Layout

| | |
|--|--|
| **Purpose** | Section shell — grid/flex regions, content slots |
| **Validation** | Default viewport: no horizontal scroll; slots hold placeholder/real content |
| **Drift prevention** | Separates composition from cosmetic tuning |

### 3. Styling

| | |
|--|--|
| **Purpose** | Scoped SCSS partial per block; tokens from handoff/project |
| **Validation** | Partial exists; scoped selectors; no inline `<style>`; no global reset waves |
| **Drift prevention** | Avoids cascade fights and layout rework |

### 4. Responsive

| | |
|--|--|
| **Purpose** | Breakpoints per handoff `responsive_rules` |
| **Validation** | Spot widths (e.g. 375 / 768 / 1280) or documented defaults; overflow; tap targets; responsive intent preservation when source exists |
| **Drift prevention** | Catches desktop-only markup before interaction bind; prevents survivability-only collapse |

**Overlay QA gate G1** — see [`qa-checklist.md`](qa-checklist.md) § responsive/layout overlay.

### 5. Interaction

| | |
|--|--|
| **Purpose** | JS modules and `data-*` hooks per handoff |
| **Validation** | Hooks present; idempotent init; one owner per hook |
| **Drift prevention** | Prevents double-bind and resize races |

**Overlay QA gate G2** — see [`qa-checklist.md`](qa-checklist.md) § behavior overlay.

### 6. QA

| | |
|--|--|
| **Purpose** | Evidence before narrative — overlay then foundation; include gate G5, source interpretation, reconstruction fidelity, initialization/reset/bootstrap, shell/first-screen/background ownership, terminal survivability/shell compatibility/encoding readability, commercial pressure/atmosphere/beautification, visual reconciliation, composition, design intent, tokens, implementation reliability, cadence/rhythm, responsive intent, content density, interaction/state/accessibility, QA confidence, escalation, coordination, strategy, temporal/workflow/production/context/recovery/transfer/governance checks before declaring section pass / freeze when material |
| **Validation** | [`qa-checklist.md`](qa-checklist.md) + [`../frontend-gulp-agent/qa-checklist.md`](../frontend-gulp-agent/qa-checklist.md); build if in scope |
| **Drift prevention** | Stops “looks done” without checklist; lists **SAFE UNKNOWN** |

**Overlay QA gate G3** — pre-freeze.

**Overlay QA gate G6** — visual reconciliation (human-supervised visual intent read); **before** final responsive closure documented in [`semantic-source-lock.md`](semantic-source-lock.md) §5.

**G6 icon add-on** — Font Awesome governance (startup readiness evidence, semantic fidelity, family consistency, optical rhythm, delivery/path validity, exceptions) when a section contains icons; record under `ICONOGRAPHY FINDINGS`.

**Overlay QA gate G7** — compositional structure awareness (composition-vs-DOM cluster read); **with** or **immediately after** G6; **not** autonomous regroup per [`composition-awareness-checklist.md`](composition-awareness-checklist.md).

**Design intent QA** — radius philosophy, surface hierarchy, CTA philosophy, UI weight, border/shadow restraint, SaaS contamination, and section emphasis discipline; record `DESIGN INTENT FINDINGS` per [`design-intent-checklist.md`](design-intent-checklist.md).

**Design token QA** — semantic token intent, token hierarchy, aliases, override governance, responsive/state token integrity, token drift, and design-system trust read; record `DESIGN TOKEN FINDINGS` per [`design-token-checklist.md`](design-token-checklist.md). This is human-supervised methodology, not automatic token enforcement.

**Implementation reliability QA** — frontend stability, deterministic rebuilds, scoped fixes, override/include/breakpoint integrity, regression survivability, and implementation readability read; record `IMPLEMENTATION RELIABILITY FINDINGS` per [`implementation-reliability-checklist.md`](implementation-reliability-checklist.md). This is human-supervised methodology, not autonomous repair or runtime enforcement.

**Cadence QA** — inter-screen narrative pacing read; record `CADENCE FINDINGS` per [`cadence-governance-checklist.md`](cadence-governance-checklist.md). Check cadence continuity, transition pacing, density stacks, footer closure, and mobile cadence survivability.

**Rhythm QA** — typography cadence and vertical rhythm read; record `RHYTHM FINDINGS` per [`rhythm-governance-checklist.md`](rhythm-governance-checklist.md). This is human-supervised methodology, not automatic cadence analysis.

**Responsive intent QA** — hierarchy survival, composition collapse, mobile cadence, CTA collapse, stack integrity, visual weight, and operational readability read; record `RESPONSIVE INTENT FINDINGS` per [`responsive-intent-checklist.md`](responsive-intent-checklist.md). This is human-supervised methodology, not automatic responsive redesign.

**Content density QA** — information pressure, scanning rhythm, proof density, trust-wall drift, card overload, CTA dilution, and overload taxonomy read; record `CONTENT DENSITY FINDINGS` per [`content-density-checklist.md`](content-density-checklist.md). This is human-supervised methodology, not automatic readability scoring.

**Source interpretation QA** — observed / inferred / assumed / unknown separation, confidence labels, ambiguity taxonomy, source contradiction handling, and missing-source escalation; record `SOURCE INTERPRETATION FINDINGS` per [`source-interpretation-checklist.md`](source-interpretation-checklist.md). This is human-supervised methodology, not automatic source understanding.

**Source lineage QA** — provenance integrity, authority chain, derivation disclosure, stale-lineage risk, transformation boundaries, and unknown-origin source handling; record `SOURCE LINEAGE FINDINGS` per [`source-lineage-checklist.md`](source-lineage-checklist.md). This is human-supervised methodology, not runtime provenance enforcement.

**Reconstruction fidelity QA** — source-to-build fidelity, design-intent transfer, approximation transparency, hierarchy fidelity, semantic transfer, responsive fidelity, and fidelity survivability; record `RECONSTRUCTION FIDELITY FINDINGS` per [`reconstruction-fidelity-checklist.md`](reconstruction-fidelity-checklist.md). This is human-supervised methodology, not automatic fidelity scoring or perfect source reconstruction.

**Terminal survivability / shell compatibility QA** — shell type awareness, PowerShell-safe separators, avoidance of bash-only syntax in Windows shells, command portability, UTF-8 continuity, terminal readability continuity, validation-command survivability, and display-vs-file corruption distinction; record `TERMINAL SURVIVABILITY FINDINGS`, `SHELL COMPATIBILITY FINDINGS`, and `ENCODING READABILITY FINDINGS` per [`qa-checklist.md`](qa-checklist.md). This is human-supervised methodology, not autonomous shell adaptation or automatic encoding repair.

**Interaction intent QA** — interaction semantics, hover authority, CTA behavior consistency, motion restraint, dead zones, behavioral overload, and contamination taxonomy read; record `INTERACTION INTENT FINDINGS` per [`interaction-intent-checklist.md`](interaction-intent-checklist.md). This is human-supervised methodology, not automatic UX behavior scoring.

**State consistency QA** — hover/focus/active/disabled/loading/validation/success/error integrity, CTA state consistency, mobile state continuity, and accessibility-state drift read; record `STATE CONSISTENCY FINDINGS` per [`state-consistency-checklist.md`](state-consistency-checklist.md). This is human-supervised methodology, not automatic state validation or accessibility AI.

**Accessibility intent QA** — trusted operational usability read: semantic accessibility, focus survivability, keyboard continuity, assistive predictability, contrast trust, form seriousness, mobile accessibility continuity, and accessibility drift taxonomy; record `ACCESSIBILITY FINDINGS` per [`accessibility-intent-checklist.md`](accessibility-intent-checklist.md). This is human-supervised methodology, not an automated WCAG engine or runtime accessibility AI.

**QA confidence QA** — evidence integrity, confidence honesty, scoped PASS/FAIL/PARTIAL discipline, SAFE UNKNOWN visibility, verification traceability, and anti-theater QA; record `QA CONFIDENCE FINDINGS` per [`qa-confidence-checklist.md`](qa-confidence-checklist.md). This is human-supervised methodology, not autonomous verification or universal QA truth.

**Human escalation QA** — escalation boundaries, stop conditions, contradiction escalation, HITL visibility, assumption thresholds, and authority integrity; record `HUMAN ESCALATION FINDINGS` per [`human-escalation-checklist.md`](human-escalation-checklist.md). This is human-supervised methodology, not a runtime approval engine or autonomous governance AI.

**Multi-agent coordination QA** — responsibility boundaries, reviewer independence, validator integrity, escalation ownership, orchestration clarity, handoff survivability, and fake-consensus risk; record `MULTI-AGENT FINDINGS` per [`multi-agent-coordination-checklist.md`](multi-agent-coordination-checklist.md). This is human-supervised methodology, not runtime orchestration or autonomous agent governance.

**Strategic intent QA** — business priority, conversion hierarchy, proof hierarchy, operational trust, stakeholder intent, local optimization boundaries, and strategic drift; record `STRATEGIC INTENT FINDINGS` per [`strategic-intent-checklist.md`](strategic-intent-checklist.md). This is human-supervised methodology, not autonomous business AI or conversion optimization.

**Temporal evolution QA** — freeze-state integrity, governed evolution, controlled overrides, iterative-change accumulation, version lineage, continuity checkpoints, and project drift survivability; record `TEMPORAL EVOLUTION FINDINGS` per [`temporal-evolution-checklist.md`](temporal-evolution-checklist.md). This is human-supervised methodology, not autonomous maintenance AI or runtime drift enforcement.

**Execution discipline QA** — workflow discipline, checkpoint integrity, freeze-validation QA, execution-order QA, handoff stability, continuity checkpoints, unsafe parallel modification, and context-loss risk; record `WORKFLOW DISCIPLINE FINDINGS` per [`execution-discipline-checklist.md`](execution-discipline-checklist.md). This is human-supervised methodology, not autonomous workflow AI or runtime orchestration.

**Production readiness QA** — delivery survivability, handoff survivability, onboarding readability, maintainability continuity, future-edit safety, deployment survivability, frozen-build survivability, and lifecycle survivability; record `PRODUCTION READINESS FINDINGS` per [`production-readiness-checklist.md`](production-readiness-checklist.md). This is human-supervised methodology, not autonomous maintenance AI, runtime deployment, or perfect maintainability.

**Context survivability QA** — compression integrity, checkpoint persistence, freeze-state memory, escalation memory, governance memory, continuity reconstruction, and context drift; record `CONTEXT SURVIVABILITY FINDINGS` per [`context-survivability-checklist.md`](context-survivability-checklist.md). This is human-supervised methodology, not autonomous memory AI or runtime persistence.

**Failure recovery QA** — trusted-state recovery, rollback integrity, freeze restoration, degraded-state handling, continuity restoration, recovery traceability, and resilience validation; record `FAILURE RECOVERY FINDINGS` per [`failure-recovery-checklist.md`](failure-recovery-checklist.md). This is human-supervised methodology, not autonomous self-healing or runtime recovery.

**Cross-project transfer QA** — transfer compatibility, semantic portability, strategic fit, operational fit, governance portability, incompatibility escalation, project identity, and transfer drift; record `CROSS-PROJECT TRANSFER FINDINGS` per [`cross-project-transfer-checklist.md`](cross-project-transfer-checklist.md). This is human-supervised methodology, not automatic compatibility detection or autonomous transfer AI.

**Governance minimalism QA** — proportional governance, cognitive load, operational readability, checklist fatigue, process survivability, and governance-to-value review; record `GOVERNANCE MINIMALISM FINDINGS` per [`governance-minimalism-checklist.md`](governance-minimalism-checklist.md). This is human-supervised methodology, not autonomous simplification, automatic pruning, or universal minimalism law.

**Risk weighting QA** — severity proportionality, operational focus, escalation relevance, signal-to-noise clarity, critical-path awareness, and prioritization drift review; record `RISK WEIGHTING FINDINGS` per [`risk-weighting-checklist.md`](risk-weighting-checklist.md). This is human-supervised methodology, not autonomous risk AI, scoring automation, or universal severity law.

**Adaptive governance QA** — context-sensitive rigor, proportional process depth, adaptive QA depth, governance fit, contextual escalation, process scaling, and survivability balancing review; record `ADAPTIVE GOVERNANCE FINDINGS` per [`adaptive-governance-checklist.md`](adaptive-governance-checklist.md). This is human-supervised methodology, not autonomous governance adaptation, runtime policy enforcement, or universal rigor law.

**Governance economics QA** — operational cost awareness, governance efficiency, validation-cost QA, review allocation, sustainability balancing, governance ROI, and cost drift review; record `GOVERNANCE ECONOMICS FINDINGS` per [`governance-economics-checklist.md`](governance-economics-checklist.md). This is human-supervised methodology, not autonomous governance optimization, runtime cost enforcement, or universal economics law.

**Cognitive load QA** — review readability, signal-to-noise clarity, reviewer sustainability, governance readability, cognitive survivability, and cognitive drift review; record `COGNITIVE LOAD FINDINGS` per [`cognitive-load-checklist.md`](cognitive-load-checklist.md). This is human-supervised methodology, not cognitive-monitoring AI, runtime attention systems, automatic readability scoring, or perfect readability.

**Governance compression QA** — operational mode, deployability, compression integrity, mode transition, governance scalability, portability, and density scaling review; record `GOVERNANCE COMPRESSION FINDINGS` per [`governance-compression-checklist.md`](governance-compression-checklist.md). This is human-supervised methodology, not autonomous governance scaling, runtime governance orchestration, universal operational modes, or perfect deployability.

**Reasoning visibility QA** — evidence-to-conclusion traceability, prioritization rationale, escalation explainability, uncertainty visibility, assumption disclosure, tradeoff disclosure, and conclusion readability; record `REASONING VISIBILITY FINDINGS` per [`reasoning-visibility-checklist.md`](reasoning-visibility-checklist.md). This is human-supervised methodology, not hidden chain-of-thought exposure, autonomous reasoning, or perfect explainability.

**Organizational memory QA** — lesson survivability, institutional continuity, operational wisdom, rediscovery avoidance, historical traceability, institutional readability, and continuity inheritance; record `ORGANIZATIONAL MEMORY FINDINGS` per [`organizational-memory-checklist.md`](organizational-memory-checklist.md). This is human-supervised methodology, not autonomous institutional AI, permanent memory, or perfect historical continuity.

**Governance evolution QA** — controlled governance evolution, refinement traceability, continuity-safe change, methodology review, adaptive survivability, historical-lineage QA, and evolutionary drift; record `GOVERNANCE EVOLUTION FINDINGS` per [`governance-evolution-checklist.md`](governance-evolution-checklist.md). This is human-supervised methodology, not autonomous self-improving AI, runtime governance mutation, or perfect adaptability.

**Meta-governance QA** — governance architecture integrity, cross-layer consistency, methodological coherence, layer-boundary clarity, contradiction survivability, governance topology, and architecture readability; record `META-GOVERNANCE FINDINGS` per [`meta-governance-checklist.md`](meta-governance-checklist.md). This is human-supervised methodology, not autonomous governance management AI, runtime governance engine, universal topology, or perfect coherence.

**Trust calibration QA** — calibrated trust, confidence proportionality, uncertainty visibility, explainable reliability, credibility survivability, and trust traceability; record `TRUST CALIBRATION FINDINGS` per [`trust-calibration-checklist.md`](trust-calibration-checklist.md). This is human-supervised methodology, not autonomous trust scoring, runtime credibility engines, universal trust laws, or perfect reliability.

### 7. Freeze

| | |
|--|--|
| **Purpose** | Lock section; engage change control |
| **Validation** | REPORT records `frozen: true` for scope; unfreeze path documented |
| **Drift prevention** | Stops endless micro-tweaks and cross-session spacing drift |

---

## Mapping to foundation workflow

| Foundation step | Forge |
|-----------------|-------|
| 1–3 Inspect / plan | Prerequisites for phase 1 |
| 4 Implement source | **Phases 1–5** (internal split) |
| 5–6 Build + QA | **Phase 6** (+ foundation checklist) |
| 7–9 Report / HITL / checkpoint | **Phase 7** + foundation reporting |

---

## Anti-patterns (drift)

| Pattern | Risk |
|---------|------|
| **No semantic charter** (`semantic-source-lock.md` §1) | Wrong design version, archive-driven structure, entity-count drift |
| Font Awesome readiness deferred until visual QA | Missing glyphs, square icons, broken webfont paths, late icon rewrites |
| Styling before structure | Selector/DOM rework |
| Interaction before responsive stable | Double-bind on resize |
| QA only at page end | Bad section poisons neighbors |
| Icon choice by visual approximation | Semantic mismatch, mixed-weight UI drift, icon contamination |
| Ignoring design intent governance | Random radius feel, CTA weight drift, shadow spam, surface hierarchy inconsistency, SaaS contamination |
| Ignoring design token intelligence governance | Semantic alias confusion, override chaos, breakpoint-token divergence, token spaghetti, fake design-system consistency |
| Ignoring implementation reliability governance | CSS spaghetti, include-chain contamination, unsafe overrides, breakpoint hacks, regression cascades, rebuild unpredictability |
| Ignoring cadence as narrative pacing | Section collision, compressed middle cadence, CTA/footer pacing drift |
| Random typography / spacing rhythm | Arbitrary line-height, section padding, density spikes, CTA crowding |
| Survivability-only responsive work | “Just stack everything,” hierarchy inversion, CTA collapse, mobile fatigue |
| Ignoring information pressure | Wall-of-text drift, endless-card drift, proof spam, trust-wall wallpaper, CTA burial |
| Ignoring source interpretation confidence | Screenshot hallucination, false certainty, missing-source guessing, inferred certainty inflation |
| Ignoring source lineage governance | Lineage loss, stale-source reuse, summary contamination, fake authority inheritance, unknown-origin implementation |
| Ignoring reconstruction fidelity governance | Fidelity illusion, hidden approximation, hierarchy collapse, semantic reconstruction mismatch, source-to-build divergence |
| Ignoring initialization governance | Bad initialization, source-lock failure, stale workspace contamination, reconstruction bootstrap chaos |
| Ignoring layout shell governance | Header/hero confusion, shell opacity, mobile navigation ownership drift, shell continuity collapse |
| Ignoring first-screen decomposition | Over-merged first-screen logic, background/overlay/CTA/mobile-nav ownership ambiguity |
| Ignoring background ownership governance | Wrong background owner, overlay laundering, approved asset mutation, media traceability loss |
| Ignoring commercial pressure / atmosphere / beautification governance | Clean UI drift, SaaSification pressure, atmospheric fragmentation, commercial density collapse, section language drift |
| Ignoring terminal survivability / shell compatibility governance | Bash-on-PowerShell drift, shell-assumption drift, parser-error survivability failure, unreadable terminal output, validation-command incompatibility, console readability erosion |
| Ignoring interaction intent governance | Hover hallucination, fake premium motion, dead-click zones, CTA animation screaming, interaction overload |
| Ignoring state consistency governance | Focus invisibility, fake disabled states, loading ambiguity, validation chaos, CTA state mismatch |
| Ignoring accessibility intent governance | ARIA spam, keyboard traps, focus invisibility, fake semantic wrappers, screen-reader contamination, mobile accessibility collapse |
| Ignoring QA confidence governance | Fake PASS inflation, screenshot certainty drift, build-success illusion, hidden QA gaps, confidence escalation |
| Ignoring human escalation governance | Silent continuation, fake autonomous authority, hidden HITL dependency, contradiction minimization, assumption stacking |
| Ignoring multi-agent coordination governance | Reviewer/executor collapse, validator contamination, fake consensus, responsibility diffusion, escalation orphaning |
| Ignoring strategic intent governance | Conversion-goal erosion, CTA dilution, proof flattening, stakeholder-intent overwrite, engagement-over-trust drift |
| Ignoring temporal evolution governance | Freeze-state divergence, silent identity mutation, cumulative override decay, patch-history contamination, governance fatigue |
| Ignoring operational workflow governance | Chaotic execution, checkpoint erosion, uncontrolled iteration loops, freeze omission, unstable handoff, context-loss execution |
| Ignoring production readiness governance | Delivery-and-forget culture, handoff collapse, onboarding fragility, future-edit instability, frozen-build fragility, maintainability collapse |
| Ignoring context survivability governance | Summary hallucination, checkpoint amnesia, freeze-memory loss, escalation-memory loss, context laundering, compression-induced drift |
| Ignoring failure recovery governance | Blind rollback, invalid trusted-state reuse, panic patching, degraded-state denial, recovery opacity, "it works again" false recovery |
| Ignoring cross-project transfer governance | Unsafe pattern reuse, false analogy drift, template contamination, copied-governance overreach, project-identity erosion |
| Ignoring governance minimalism | Governance inflation, checklist fatigue, ritualized QA, process paralysis, governance-over-execution, collapse through weight |
| Ignoring risk weighting governance | Equal-priority overload, minor-drift obsession, critical-risk dilution, false criticality, escalation spam, signal-to-noise collapse |
| Ignoring adaptive governance | Governance-context mismatch, maximum rigor by default, under-protection of critical work, context-blind QA, operational rigidity, adaptive survivability erosion |
| Ignoring governance economics | Governance cost blindness, process cost inflation, QA resource drain, validation-cost explosion, expensive low-value governance, survivability-to-cost mismatch |
| Ignoring cognitive load governance | Reviewer fatigue, cognitive overload, unreadable reports, signal burial, review paralysis, operator burnout, endless-report drift |
| Ignoring governance compression | Governance deployment overload, one-mode governance, compression survivability failure, critical-mode inheritance, mode-transition ambiguity, operational scaling collapse |
| Ignoring reasoning visibility governance | Opaque reasoning, hidden assumptions, unexplained escalation, invisible prioritization logic, unverifiable recommendations, governance black-boxing |
| Ignoring organizational memory governance | Institutional memory loss, rediscovery loops, tribal-knowledge dependence, lesson burial, governance-memory erosion, historical amnesia |
| Ignoring governance evolution governance | Governance stagnation, methodology fossilization, legacy-rule accumulation, uncontrolled methodology mutation, continuity-breaking evolution, governance ossification |
| Ignoring meta-governance | Governance-layer conflict, duplicated methodology, contradictory rules, cross-layer ambiguity, topology erosion, governance architecture collapse |
| Ignoring trust calibration governance | False trust escalation, governance overconfidence, confidence inflation, perceived reliability drift, institutional overtrust, credibility collapse after failure |
| No freeze | Hierarchy/spacing drift across sessions |
| Forge rules without opening foundation docs | Forked semantics |

---

## SAFE UNKNOWN

CI job names, exact stage IDs, hosting URLs, active shell behavior, terminal encoding state, and command portability remain **factory- and project-specific** — record in REPORT.
