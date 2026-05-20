# QA checklist — MARS Forge (overlay v0)

**Overlay only.** Run **after** the relevant Forge phase, **before** advancing or freezing.

**Mandatory companion:** [`../frontend-gulp-agent/qa-checklist.md`](../frontend-gulp-agent/qa-checklist.md) — build, a11y, SEO, assets, and full production checks. **Do not** treat this file as a substitute.

**Foundation Lite (Wave 3 — compact):** [`foundation-lite-checklist.md`](foundation-lite-checklist.md) when touching `scss/foundations/`, `js/core/`, or `data-module` / section replacement — record **`FOUNDATION FINDINGS`**; skip for trivial copy-only Lite work.

**Semantic layer (normative when Forge is selected):** [`semantic-source-lock.md`](semantic-source-lock.md).

**Source interpretation layer (human-supervised, pre-freeze):** [`source-interpretation-checklist.md`](source-interpretation-checklist.md) — observed / inferred / assumed / unknown separation, confidence labels, ambiguity taxonomy, contradiction handling, and missing-source escalation; record `SOURCE INTERPRETATION FINDINGS`.

**Source lineage layer (human-supervised, pre-freeze):** [`source-lineage-checklist.md`](source-lineage-checklist.md) — provenance integrity, authority chain, derivation disclosure, stale-lineage risk, transformation boundaries, unknown-origin source handling, and lineage readability; record `SOURCE LINEAGE FINDINGS`.

**Reconstruction fidelity layer (human-supervised, pre-freeze):** [`reconstruction-fidelity-checklist.md`](reconstruction-fidelity-checklist.md) — source-to-build fidelity, design-intent transfer, approximation transparency, hierarchy fidelity, semantic transfer, responsive fidelity, and fidelity survivability; record `RECONSTRUCTION FIDELITY FINDINGS`.

**Initialization / reset / bootstrap layer (human-supervised, pre-implementation and pre-freeze):** clean-start, stale workspace residue, source-lock-before-build, reconstruction bootstrap, reset traceability, and reconstruction asset lifecycle per Website Factory governance; record `INITIALIZATION FINDINGS`, `WORKSPACE RESET FINDINGS`, `RECONSTRUCTION BOOTSTRAP FINDINGS`, and `RECONSTRUCTION ASSET FINDINGS`.

**Layout shell / first-screen / background layer (human-supervised, first viewport):** **HEADER != HERO**; layout shell, header, hero, atmosphere, background, overlay, mobile navigation, and conversion ownership per Website Factory governance; record `LAYOUT SHELL FINDINGS`, `FIRST-SCREEN DECOMPOSITION FINDINGS`, and `BACKGROUND OWNERSHIP FINDINGS`.

**Commercial pressure / atmosphere / section language / beautification layer (human-supervised, landing rhythm):** commercial density, landing momentum, atmosphere continuity, section language, anti-sterile UI, SaaSification pressure, and source-intent erosion through beautification; record `COMMERCIAL DENSITY FINDINGS`, `LANDING PRESSURE FINDINGS`, `ATMOSPHERE CONTINUITY FINDINGS`, `SECTION LANGUAGE FINDINGS`, and `BEAUTIFICATION DRIFT FINDINGS`.

**Terminal survivability / shell compatibility layer (human-supervised, validation command evidence):** PowerShell compatibility, shell-safe execution, command portability, UTF-8 continuity, output readability, console integrity, terminal readability continuity, validation-command survivability, and display-vs-file corruption distinction per Website Factory governance; record `TERMINAL SURVIVABILITY FINDINGS`, `SHELL COMPATIBILITY FINDINGS`, and `ENCODING READABILITY FINDINGS`.

**Visual intent layer (human-supervised, pre-freeze):** [`visual-reconciliation-checklist.md`](visual-reconciliation-checklist.md) — gate **G6** after semantic QA; [`composition-awareness-checklist.md`](composition-awareness-checklist.md) — gate **G7** (composition-vs-DOM) **with** or **immediately after** G6, before final responsive closure.

**Design intent layer (human-supervised, pre-freeze):** [`design-intent-checklist.md`](design-intent-checklist.md) — radius philosophy, surface hierarchy, CTA philosophy, UI weight, border/shadow restraint, SaaS contamination; record `DESIGN INTENT FINDINGS`.

**Design token layer (human-supervised, pre-freeze):** [`design-token-checklist.md`](design-token-checklist.md) — semantic token intent, token hierarchy, aliases, override governance, responsive/state token integrity, token drift taxonomy; record `DESIGN TOKEN FINDINGS`.

**Implementation reliability layer (human-supervised, pre-freeze):** [`implementation-reliability-checklist.md`](implementation-reliability-checklist.md) — frontend stability, deterministic rebuilds, scoped fixes, override/include/breakpoint integrity, regression survivability, implementation readability, and drift taxonomy; record `IMPLEMENTATION RELIABILITY FINDINGS`.

**Cadence layer (human-supervised, pre-freeze):** [`cadence-governance-checklist.md`](cadence-governance-checklist.md) — inter-screen spacing as narrative pacing; cadence continuity, transition pacing, density stacks, footer closure, mobile cadence survivability; record `CADENCE FINDINGS`.

**Rhythm layer (human-supervised, pre-freeze):** [`rhythm-governance-checklist.md`](rhythm-governance-checklist.md) — typography cadence, section spacing, density continuity, CTA/mobile/dark-light transition rhythm; record `RHYTHM FINDINGS`.

**Transition continuity / footer context / iconography / overlay focal layer (human-supervised, bootstrap and pre-freeze):** Website Factory governance for system-owned rhythm, same-background collapse, different-background reset rhythm, commercial continuity spacing, footer role classification, Font Awesome startup readiness, semantic iconography, operational icon selection, overlay balance, and focal-region survivability; record `TRANSITION CONTINUITY FINDINGS`, `FOOTER CONTEXT FINDINGS`, `ICONOGRAPHY FINDINGS`, `OVERLAY BALANCE FINDINGS`, and `FOCAL-POINT FINDINGS`.

**Responsive intent layer (human-supervised, pre-freeze):** [`responsive-intent-checklist.md`](responsive-intent-checklist.md) — hierarchy survival, mobile cadence, composition collapse, CTA collapse, stack integrity, collapse taxonomy; record `RESPONSIVE INTENT FINDINGS`.

**Content density layer (human-supervised, pre-freeze):** [`content-density-checklist.md`](content-density-checklist.md) — information pressure, scanning rhythm, proof pacing, trust density, overload taxonomy, CTA survival; record `CONTENT DENSITY FINDINGS`.

**Interaction intent layer (human-supervised, pre-freeze):** [`interaction-intent-checklist.md`](interaction-intent-checklist.md) — interaction semantics, hover authority, CTA behavior consistency, motion restraint, dead zones, overload taxonomy, and contamination; record `INTERACTION INTENT FINDINGS`.

**State consistency layer (human-supervised, pre-freeze):** [`state-consistency-checklist.md`](state-consistency-checklist.md) — hover/focus/active/disabled/loading/validation/success/error integrity, CTA state consistency, mobile state continuity, accessibility-state drift; record `STATE CONSISTENCY FINDINGS`.

**Accessibility intent layer (human-supervised, pre-freeze):** [`accessibility-intent-checklist.md`](accessibility-intent-checklist.md) — semantic accessibility, focus survivability, keyboard continuity, assistive predictability, contrast trust, form seriousness, mobile accessibility continuity, accessibility drift taxonomy; record `ACCESSIBILITY FINDINGS`.

**QA confidence layer (human-supervised, pre-freeze):** [`qa-confidence-checklist.md`](qa-confidence-checklist.md) — evidence integrity, confidence honesty, scoped PASS discipline, verification traceability, SAFE UNKNOWN visibility, and anti-theater QA; record `QA CONFIDENCE FINDINGS`.

**Human escalation layer (human-supervised, pre-freeze):** [`human-escalation-checklist.md`](human-escalation-checklist.md) — escalation boundaries, stop conditions, contradiction escalation, HITL visibility, assumption thresholds, authority integrity, and escalation drift taxonomy; record `HUMAN ESCALATION FINDINGS`.

**Multi-agent coordination layer (human-supervised, pre-freeze):** [`multi-agent-coordination-checklist.md`](multi-agent-coordination-checklist.md) — responsibility boundaries, reviewer independence, validator integrity, escalation ownership, orchestration clarity, handoff survivability, and multi-agent drift taxonomy; record `MULTI-AGENT FINDINGS`.

**Strategic intent layer (human-supervised, pre-freeze):** [`strategic-intent-checklist.md`](strategic-intent-checklist.md) — business priority, conversion hierarchy, proof hierarchy, operational trust, stakeholder intent, local optimization boundaries, and strategic drift taxonomy; record `STRATEGIC INTENT FINDINGS`.

**Temporal evolution layer (human-supervised, continuity / drift survivability):** [`temporal-evolution-checklist.md`](temporal-evolution-checklist.md) — freeze-state integrity, governed evolution, controlled overrides, iterative-change accumulation, version lineage, continuity checkpoints, and project drift survivability; record `TEMPORAL EVOLUTION FINDINGS`.

**Operational workflow layer (human-supervised, workflow survivability):** [`execution-discipline-checklist.md`](execution-discipline-checklist.md) — execution discipline, checkpoint integrity, freeze-validation QA, execution-order QA, handoff stability, continuity checkpoints, and workflow drift taxonomy; record `WORKFLOW DISCIPLINE FINDINGS`.

**Production readiness layer (human-supervised, delivery survivability):** [`production-readiness-checklist.md`](production-readiness-checklist.md) — production readiness, handoff-survivability QA, onboarding-readability QA, maintainability QA, future-edit QA, deployment-survivability QA, frozen-build survivability, and lifecycle-survivability QA; record `PRODUCTION READINESS FINDINGS`.

**Context survivability layer (human-supervised, compression / reconstruction survivability):** [`context-survivability-checklist.md`](context-survivability-checklist.md) — compression integrity, checkpoint persistence, freeze-state memory, escalation memory, governance memory, continuity reconstruction, and context drift taxonomy; record `CONTEXT SURVIVABILITY FINDINGS`.

**Failure recovery layer (human-supervised, trusted-state / rollback / resilience):** [`failure-recovery-checklist.md`](failure-recovery-checklist.md) — trusted-state recovery, rollback integrity, freeze restoration, degraded-state handling, continuity restoration, recovery traceability, and recovery drift taxonomy; record `FAILURE RECOVERY FINDINGS`.

**Cross-project transfer layer (human-supervised, compatibility / portability):** [`cross-project-transfer-checklist.md`](cross-project-transfer-checklist.md) — transfer compatibility, semantic portability, strategic fit, operational fit, governance portability, incompatibility escalation, project identity, and transfer drift; record `CROSS-PROJECT TRANSFER FINDINGS`.

**Governance minimalism layer (human-supervised, complexity control):** [`governance-minimalism-checklist.md`](governance-minimalism-checklist.md) — proportional governance, cognitive load, operational readability, checklist fatigue, process survivability, governance-to-value review, and governance bloat taxonomy; record `GOVERNANCE MINIMALISM FINDINGS`.

**Risk weighting layer (human-supervised, prioritization control):** [`risk-weighting-checklist.md`](risk-weighting-checklist.md) — severity proportionality, operational focus, escalation relevance, signal-to-noise clarity, risk layers, and prioritization drift taxonomy; record `RISK WEIGHTING FINDINGS`.

**Adaptive governance layer (human-supervised, context-sensitive discipline):** [`adaptive-governance-checklist.md`](adaptive-governance-checklist.md) — proportional process depth, adaptive QA depth, governance fit, contextual escalation, process scaling, survivability balancing, and adaptive drift taxonomy; record `ADAPTIVE GOVERNANCE FINDINGS`.

**Governance economics layer (human-supervised, operational cost awareness):** [`governance-economics-checklist.md`](governance-economics-checklist.md) — governance efficiency, validation-cost QA, review allocation, sustainability balancing, governance ROI, and cost drift taxonomy; record `GOVERNANCE ECONOMICS FINDINGS`.

**Cognitive load layer (human-supervised, review ergonomics):** [`cognitive-load-checklist.md`](cognitive-load-checklist.md) — review readability, signal-to-noise clarity, reviewer sustainability, governance readability, cognitive survivability, and cognitive drift taxonomy; record `COGNITIVE LOAD FINDINGS`.

**Governance compression layer (human-supervised, operational modes):** [`governance-compression-checklist.md`](governance-compression-checklist.md) — operational modes, deployability, compression integrity, mode transitions, governance scalability, portability, and compression drift taxonomy; record `GOVERNANCE COMPRESSION FINDINGS`.

**Reasoning visibility layer (human-supervised, transparency / traceability):** [`reasoning-visibility-checklist.md`](reasoning-visibility-checklist.md) — reasoning visibility, decision traceability, escalation explainability, prioritization transparency, uncertainty visibility, assumption disclosure, and traceable conclusions; record `REASONING VISIBILITY FINDINGS`.

**Organizational memory layer (human-supervised, institutional knowledge):** [`organizational-memory-checklist.md`](organizational-memory-checklist.md) — institutional continuity, lesson survivability, operational wisdom, rediscovery avoidance, historical traceability, continuity inheritance, and memory drift taxonomy; record `ORGANIZATIONAL MEMORY FINDINGS`.

**Governance evolution layer (human-supervised, self-refinement discipline):** [`governance-evolution-checklist.md`](governance-evolution-checklist.md) — controlled governance evolution, refinement traceability, continuity-safe change, methodology review, adaptive survivability, historical-lineage QA, and evolutionary drift taxonomy; record `GOVERNANCE EVOLUTION FINDINGS`.

**Meta-governance layer (human-supervised, governance architecture integrity):** [`meta-governance-checklist.md`](meta-governance-checklist.md) — governance architecture integrity, cross-layer consistency, methodological coherence, layer-boundary clarity, contradiction survivability, governance topology, and meta-governance drift taxonomy; record `META-GOVERNANCE FINDINGS`.

**Trust calibration layer (human-supervised, governance credibility):** [`trust-calibration-checklist.md`](trust-calibration-checklist.md) — calibrated trust, confidence proportionality, uncertainty visibility, explainable reliability, credibility survivability, and trust traceability; record `TRUST CALIBRATION FINDINGS`.

Record pass / fail / partial in REPORT **Forge execution** subsection.

---

## Spacing consistency (overlay)

- [ ] Section vertical rhythm matches design intent / handoff spacing notes (heuristic).
- [ ] No ad-hoc margin/padding “nudging” without token or documented scale.
- [ ] Adjacent sections: no obvious collision or double-gap at shared boundary.
- [ ] Internal block padding consistent with sibling blocks of same type.
- [ ] Cadence governance checklist run when inter-screen pacing, dense/light adjacency, CTA isolation, footer closure, or mobile cadence is in scope.
- [ ] Rhythm governance checklist run when typography / section cadence is in scope.
- [ ] Transition continuity reviewed when same-background double-gaps, different-background reset rhythm, commercial continuity spacing, isolated-block feeling, section-stack feeling, or white-section energy collapse is in scope.
- [ ] Footer context reviewed when footer height, footer role, landing closure, portal/ecommerce expansion, legal/contact density, or final CTA-to-footer continuity is in scope.
- [ ] Iconography reviewed when Font Awesome, custom icons, social/review marks, operational symbols, icon semantics, SaaS icon drift, or baked image annotation duplication is in scope.
- [ ] Font Awesome readiness decided during bootstrap when icons may be needed: approved FA source inspected, local delivery structure prepared, `woff2`/`woff` available for webfont delivery, `css/` to `webfonts/` paths preserved, SVG-font-only delivery avoided, and semantic role map started before section implementation.
- [ ] Overlay balance and focal point reviewed when scrims, over-darkening, hero media readability, truck/product/person anchoring, text-safe zones, media-safe zones, or responsive focal survival is in scope.
- [ ] Responsive intent checklist run when viewport collapse affects hierarchy, grouping, CTA pacing, visual weight, mobile fatigue, or operational readability.
- [ ] Content density checklist run when information pressure, overloaded cards, noisy grids, proof density, trust-wall drift, verbose sections, or scanning fatigue is in scope.
- [ ] Source interpretation checklist run when source confidence, ambiguity, contradiction, screenshot authority, inferred grouping, missing state, or missing breakpoint authority affects implementation.
- [ ] Source lineage checklist run when source origin, authority chain, derivation disclosure, transformation boundary, stale lineage, summary contamination, or unknown-origin source affects implementation.
- [ ] Reconstruction fidelity checklist run when source-to-build fidelity, approximation transparency, hierarchy fidelity, semantic transfer, responsive fidelity, reconstruction confidence, or fidelity survivability affects implementation.
- [ ] Initialization / reset / bootstrap governance reviewed when clean-start state, stale workspace residue, source-lock-before-build, reconstruction bootstrap, or reset traceability affects implementation.
- [ ] Reconstruction asset lifecycle reviewed when approved, temporary, derived, transformed, deprecated, or unknown-origin assets affect source fidelity or background/media ownership.
- [ ] Layout shell and first-screen decomposition reviewed when header, hero, atmosphere, background, overlay, mobile navigation, or conversion layer cohabit the opening viewport.
- [ ] Background ownership reviewed when shell background, hero-local background, overlays, section bands, or media backgrounds affect readability, atmosphere, or section boundaries.
- [ ] Background focal-point governance reviewed when focal visual regions, hero focal anchoring, media-safe zones, text-safe zones, or responsive background scaling affect source fidelity.
- [ ] Commercial density / landing pressure reviewed when CTA rhythm, proof pacing, operational trust, urgency density, or anti-sterile UI affects conversion pressure.
- [ ] Atmosphere continuity / section language / beautification drift reviewed when environmental rhythm, dark/light cadence, density language, CTA language, SaaSification, or clean-UI drift affects the page.
- [ ] Terminal survivability / shell compatibility reviewed when validation commands, live-output readability, PowerShell execution, command portability, UTF-8 continuity, parser errors, console integrity, or display/file corruption distinction affects evidence.
- [ ] Interaction intent checklist run when hover behavior, CTA interaction, motion, dead zones, misleading affordance, mobile tap behavior, or JS hook behavior is in scope.
- [ ] State consistency checklist run when hover/focus/active/disabled/loading/validation/success/error states, CTA state behavior, keyboard state, or mobile state continuity is in scope.
- [ ] Accessibility intent checklist run when semantic HTML, ARIA, focus, keyboard, forms, CTAs, contrast, mobile accessibility, custom controls, or assistive predictability is in scope.
- [ ] Design token checklist run when tokens, variables, aliases, spacing/color/radius/shadow/type values, responsive values, state values, or local overrides affect design-system trust.
- [ ] Implementation reliability checklist run when CSS scope, includes, breakpoints, overrides, regression impact, rebuild behavior, JS ownership, or maintainability is in scope.
- [ ] QA confidence checklist run before PASS/PARTIAL/FAIL/freeze claims when evidence levels, proof boundaries, unverified states, build-only results, screenshot-only results, inferred validation, or SAFE UNKNOWN affect reporting.
- [ ] Human escalation checklist run when ambiguity, contradiction, approval boundary, assumption chain, source priority, stop condition, or HITL ownership affects continuation.
- [ ] Multi-agent coordination checklist run when multiple AI-assisted roles, sessions, reviewers, validators, handoffs, responsibility boundaries, reviewer independence, validator integrity, fake consensus, or escalation ownership affect the scope.
- [ ] Strategic intent checklist run when business priority, conversion hierarchy, proof hierarchy, CTA role, operational trust, stakeholder intent, or local optimization boundaries affect the scope.
- [ ] Temporal evolution checklist run when freeze-state integrity, version lineage, cumulative edits, override history, modernization, continuity checkpoints, or long-term governance survivability affect the scope.
- [ ] Execution discipline checklist run when workflow order, checkpoints, freeze validation, handoff state, report consistency, unsafe parallel modification, uncontrolled iteration, or context-loss risk affects the scope.
- [ ] Production readiness checklist run when delivery survivability, handoff state, onboarding readability, maintainability continuity, future edits, deployment assumptions, frozen-build survivability, or post-delivery stability affects the scope.
- [ ] Context survivability checklist run when compressed context, summaries, checkpoint persistence, freeze-state memory, escalation memory, governance memory, continuity reconstruction, or long-chain operational continuity affects the scope.
- [ ] Failure recovery checklist run when trusted-state recovery, rollback integrity, freeze restoration, degraded-state handling, continuity restoration, panic-fix contamination, recovery traceability, or resilience validation affects the scope.
- [ ] Cross-project transfer checklist run when prior-project lessons, templates, governance rules, implementation patterns, visual treatments, or inherited assumptions affect the scope.
- [ ] Governance minimalism checklist run when governance volume, checklist fatigue, finding sprawl, process readability, methodology weight, or governance-to-value risk affects the scope.
- [ ] Risk weighting checklist run when findings are numerous, severity is unclear, escalation relevance is disputed, cosmetic issues crowd critical issues, or signal-to-noise affects review focus.
- [ ] Adaptive governance checklist run when task criticality, QA depth, escalation level, governance weight, context mismatch, process scaling, or survivability balancing affects the scope.
- [ ] Governance economics checklist run when governance cost, review effort, QA depth, validation volume, process overhead, survivability cost, governance ROI, or operational sustainability affects the scope.
- [ ] Cognitive load checklist run when report length, finding volume, governance density, review fatigue, signal-to-noise clarity, reviewer sustainability, governance readability, or cognitive survivability affects the scope.
- [ ] Governance compression checklist run when operational mode, governance deployability, report density, compression integrity, mode transitions, governance portability, scalable governance depth, or deployment fatigue affects the scope.
- [ ] Reasoning visibility checklist run when conclusions, recommendations, prioritization, escalation, assumptions, tradeoffs, uncertainty, or freeze posture need reviewable rationale.
- [ ] Organizational memory checklist run when reusable lessons, repeated mistakes, historical decisions, institutional readability, rediscovery risk, or continuity inheritance affects the scope.
- [ ] Governance evolution checklist run when methodology age, governance stagnation, repeated rule friction, legacy assumptions, process redesign, governance renewal, or continuity-safe method change affects the scope.
- [ ] Meta-governance checklist run when governance-layer conflict, overlapping domains, contradictory methodology, duplicated concepts, governance graph instability, cross-layer ambiguity, or architecture readability affects the scope.
- [ ] Trust calibration checklist run when governance confidence, perceived reliability, uncertainty visibility, explainable reliability, institutional trust, or credibility survivability affects the scope.

---

## Hierarchy consistency (overlay)

- [ ] Heading levels match handoff / blueprint for this `block_id`.
- [ ] Heading and paragraph cadence checked against rhythm governance or project typography pack.
- [ ] CTA prominence matches section role (hero vs supporting).
- [ ] CTA weight and repetition checked against design intent / CTA philosophy governance when in scope.
- [ ] CTA hierarchy checked at mobile/tablet widths when responsive collapse can change pressure or order.
- [ ] CTA visibility checked against density, proof saturation, trust-wall drift, and microcopy overload when in scope.
- [ ] CTA behavior checked for consistency, restrained feedback, no fake urgency, and no animation screaming when in scope.
- [ ] CTA states checked for hover/focus/active/loading/disabled consistency, mobile continuity, and no ambiguous state pressure when in scope.
- [ ] CTA accessibility checked for clear labels, focus survivability, keyboard continuity, trustworthy states, and no hover-only or icon-only ambiguity when in scope.
- [ ] CTA strategic role checked for conversion hierarchy, proof support, stakeholder intent, and no CTA dilution / spam when in scope.
- [ ] CTA rhythm checked against landing pressure, proof pacing, operational trust rhythm, and commercial density when first-screen or landing conversion is in scope.
- [ ] Header / hero ownership checked: header navigation, mobile menu, shell background, hero content, hero-local media, overlays, and conversion cues are not merged by accident.
- [ ] CTA changes checked against freeze-state integrity and long-term identity survivability when repeated edits or modernization affect conversion continuity.
- [ ] Surface hierarchy, radius family, shadow/border logic, and SaaS contamination checked when in scope.
- [ ] Semantic token intent, token hierarchy, aliases, overrides, responsive/state token integrity, and token drift checked when in scope.
- [ ] Implementation readability, coupling boundaries, override risk, include-chain integrity, and regression survivability checked when in scope.
- [ ] Landmark structure unchanged since structure phase (no drifted wrappers).
- [ ] List/card density readable at default viewport.

---

## Responsive stability (overlay — gate G1)

- [ ] Spot widths from handoff pass for **current section** (or gaps listed).
- [ ] No new horizontal scroll introduced in this slice.
- [ ] Sticky/fixed elements do not clip tap targets in section scope.
- [ ] Images/media respect max-width constraints in section.
- [ ] Responsive intent survives: hierarchy, cadence, grouping, CTA pacing, visual weight, and operational readability are preserved or findings recorded.
- [ ] Breakpoint integrity checked for patch layering, emergency hacks, hidden coupling, and width-regression risk when in scope.

---

## Section integrity (overlay)

- [ ] `block_id` alignment: one partial pair (+ scoped JS) per block registry intent.
- [ ] Include graph unchanged without documented reason.
- [ ] Include-chain integrity checked when partial/import order, shared components, or neighbor section dependencies affect the slice.
- [ ] `section_map` order preserved for implemented scope.
- [ ] Forbidden patterns from handoff not introduced.

---

## Implementation sequencing discipline (overlay)

- [ ] Phases 1–5 completed in order (or skip reason documented).
- [ ] No cosmetic styling recorded during structure/layout-only work.
- [ ] No interaction bind before layout phase exit criteria met.
- [ ] Interaction behavior does not invent hover, motion, disclosure, carousel, sticky CTA, or gesture systems without source authority.
- [ ] State behavior does not invent disabled, loading, validation, success, error, focus, or keyboard behavior without source authority or disclosed SAFE UNKNOWN.
- [ ] Accessibility behavior does not add ARIA spam, fake semantic wrappers, custom-control semantics, or assistive announcements without source authority, implementation evidence, or disclosed SAFE UNKNOWN.
- [ ] Implementation reliability does not depend on patch-on-patch fixes, random utility overrides, selector escalation, hidden dependencies, or “works now” engineering.
- [ ] Implementation does not inherit summaries, prior outputs, existing code, assets, or screenshots as authority without visible source lineage.
- [ ] Implementation does not start from stale workspace state, old hero rebuilds, orphaned imports, deprecated partials, or frozen-state resets without reset traceability.
- [ ] Implementation does not treat “first screen” as one owner when shell, header, hero, atmosphere, background, overlay, mobile navigation, and conversion layers require decomposition.
- [ ] Implementation does not mutate approved assets, promote temporary assets, reuse deprecated assets, or hide derived asset transformations without reconstruction asset lifecycle disclosure.
- [ ] Implementation does not beautify, SaaSify, sterilize, or modernize source intent at the cost of commercial pressure, atmosphere continuity, or section language.
- [ ] Implementation does not treat vertical rhythm as section-local improvisation; same-background boundaries avoid accidental double-gaps, different-background boundaries use documented reset rhythm, and exceptions are intentional.
- [ ] Implementation does not use random Font Awesome glyphs, playful SaaS icons, semantically mismatched icons, broken FA webfont delivery, SVG-font-only FA delivery, or duplicate baked image annotations as separate HTML/CSS overlays.
- [ ] Implementation does not over-darken hero media, suffocate atmosphere, misplace focal vehicles/products/people, or hide focal-point uncertainty behind overlay pressure.
- [ ] Implementation does not apply footer-height absolutism; footer size follows landing, portal, ecommerce, corporate, or operational-contact role.
- [ ] Validation commands do not use bash-only syntax in a PowerShell shell; PowerShell commands use PowerShell-safe separators and shell-compatible quoting.
- [ ] Shell type, command portability, path quoting, parser errors, and terminal readability are considered before validation output is treated as PASS/PARTIAL/FAIL evidence.
- [ ] Broken terminal rendering, mojibake, unreadable output, or terminal-noise collapse is not ignored; display corruption is not treated as guaranteed file corruption without file-content verification.
- [ ] Implementation does not continue through HITL-required ambiguity, unresolved contradiction, fake approval, or hidden human decision substitution.
- [ ] Multi-agent handoffs do not collapse executor, reviewer, validator, orchestrator, escalation authority, or HITL authority into one untraceable responsibility.
- [ ] Implementation does not optimize local UI polish, engagement, CTA pressure, proof volume, or aesthetic symmetry at the expense of business intent.
- [ ] Implementation does not treat repeated local patches, modernization, or prior drift as project identity without freeze-state and version-lineage review.
- [ ] Implementation does not continue through missing checkpoints, unsafe parallel modifications, unstable handoff state, report inconsistency, or context-loss execution.
- [ ] Implementation and reporting do not treat successful delivery, build completion, visual correctness, freeze-state existence, or QA pass as production readiness without handoff survivability, onboarding readability, maintainability continuity, future-edit safety, and lifecycle-survivability review.
- [ ] Implementation does not continue blindly from summaries, compressed context, reconstructed state, stale memory, or implicit assumptions without checkpoint persistence and context survivability review.
- [ ] Implementation does not recover by blind rollback, invalid trusted-state reuse, panic patching, degraded-state denial, recovery opacity, or "it works again" claims without recovery governance review.
- [ ] Implementation does not transfer patterns, templates, governance rules, visual language, strategic assumptions, or frontend structures from another project without compatibility review.
- [ ] Implementation does not convert every valid governance concern into mandatory depth when lightweight, escalation-only, optional-depth, or deferred treatment would be proportional.
- [ ] Implementation and reporting do not treat all findings as equal, inflate false criticality, escalate low-value issues, or let minor drift hide critical operational risk.
- [ ] Implementation and reporting do not apply identical governance everywhere, default to maximum rigor, under-protect critical work, or hide governance-depth selection when context-sensitive discipline is required.
- [ ] Implementation and reporting do not treat governance cost as free, expand validation endlessly, drain QA resources, overload review, or pursue survivability without efficiency.
- [ ] Implementation and reporting do not treat longer reports, more findings, denser evidence, or more governance terminology as better review when readability, signal-to-noise clarity, reviewer sustainability, or cognitive survivability is declining.
- [ ] Implementation and reporting do not force one-mode governance, permanent critical-mode operation, deployment-hostile density, compression without integrity, or unclear mode transitions when operational mode selection is required.
- [ ] Implementation and reporting do not collapse reasoning into opaque verdicts, hidden assumptions, unexplained escalation, invisible prioritization logic, unverifiable recommendations, or "trust the system" governance.
- [ ] Implementation and reporting do not treat archives, old reports, remembered project history, or documentation volume as institutional memory without lesson survivability, historical traceability, and reuse boundaries.
- [ ] Implementation and reporting do not treat old methodology as automatically correct, new methodology as automatically better, or rule accumulation as governance maturity without refinement traceability and continuity-safe change.
- [ ] Prompt scope matched one primary `block_id` per session slice.

---

## Anti-regression (overlay — gate G4)

- [ ] Previously **frozen** sections: spot check still passes after adjacent edits.
- [ ] No accidental selector bleed into frozen section partials.
- [ ] Global SCSS/JS changes flagged if they touch frozen blocks.
- [ ] Regression survivability reviewed when scoped fixes touch shared selectors, tokens, includes, components, breakpoints, or JS hooks.

---

## Freeze validation (overlay — gate G3)

- [ ] Overlay sections above pass or partial with explicit deferrals.
- [ ] Foundation QA checklist run (or **SAFE UNKNOWN** with reason).
- [ ] `frozen: true` recorded for `block_id` / scope in REPORT.
- [ ] Unfreeze policy stated if hotfix required.

---

## Semantic source lock — pre-freeze (**gate G5**)

Normative checklist; full rules in [`semantic-source-lock.md`](semantic-source-lock.md).

- [ ] **Charter OK** — task states active design version, canonical visual path, forbidden paths, allowed `shared-assets` path (if any), workspace path; otherwise **stopped** with **SAFE UNKNOWN** (§1).
- [ ] **Meaning/copy lock** — section meaning, order, titles, key copy, entity count, CTA meaning, screen roles match source or documented approved rewrite — no marketing rewrite “by feel” (§2).
- [ ] **Version isolation** — only active version defines structure/semantics; archive/`v1` not driving layout; `shared-assets` = media only (§3).
- [ ] **Legacy doc safety** — no PDF/old rules relied on unless named canonical in task; conflicts resolved toward current SoT (§4).
- [ ] **Screen cadence** — this slice anchored to identified source screen; no later sections built from stale DOM guesses (§5).
- [ ] **Semantic QA** — §6 items satisfied (titles, entities, CTAs, no V1/V2 blend, no archive contamination, no invented fleet/pricing).
- [ ] **Visual reconciliation (G6)** — [`visual-reconciliation-checklist.md`](visual-reconciliation-checklist.md) satisfied or PARTIAL with explicit deferrals (**before** final responsive closure and freeze).
- [ ] **Source interpretation QA** — [`source-interpretation-checklist.md`](source-interpretation-checklist.md) satisfied or PARTIAL with explicit `SOURCE INTERPRETATION FINDINGS` for confidence, ambiguity, missing source, contradiction, and approximation disclosure.
- [ ] **Source lineage QA** — [`source-lineage-checklist.md`](source-lineage-checklist.md) satisfied or PARTIAL with explicit `SOURCE LINEAGE FINDINGS` for provenance integrity, authority chain, derivation disclosure, stale lineage, transformation boundaries, unknown-origin source, and lineage readability.
- [ ] **Reconstruction fidelity QA** — [`reconstruction-fidelity-checklist.md`](reconstruction-fidelity-checklist.md) satisfied or PARTIAL with explicit `RECONSTRUCTION FIDELITY FINDINGS` for source-to-build fidelity, approximation transparency, hierarchy fidelity, semantic transfer, responsive fidelity, reconstruction confidence, and fidelity survivability.
- [ ] **Initialization / reset / bootstrap QA** — clean-start, workspace reset, reconstruction bootstrap, and reconstruction asset lifecycle governance satisfied or PARTIAL with explicit `INITIALIZATION FINDINGS`, `WORKSPACE RESET FINDINGS`, `RECONSTRUCTION BOOTSTRAP FINDINGS`, and `RECONSTRUCTION ASSET FINDINGS`.
- [ ] **Shell / first-screen / background QA** — **HEADER != HERO**, first-screen decomposition, shell continuity, mobile navigation ownership, background authority, overlay ownership, and media traceability satisfied or PARTIAL with explicit `LAYOUT SHELL FINDINGS`, `FIRST-SCREEN DECOMPOSITION FINDINGS`, and `BACKGROUND OWNERSHIP FINDINGS`.
- [ ] **Commercial pressure / atmosphere / beautification QA** — commercial density, landing pressure, atmosphere continuity, section language, anti-sterile UI, anti-SaaSification, and beautification drift satisfied or PARTIAL with explicit `COMMERCIAL DENSITY FINDINGS`, `LANDING PRESSURE FINDINGS`, `ATMOSPHERE CONTINUITY FINDINGS`, `SECTION LANGUAGE FINDINGS`, and `BEAUTIFICATION DRIFT FINDINGS`.
- [ ] **Terminal survivability / shell compatibility QA** — PowerShell-safe separators, avoidance of bash-only syntax in Windows shell, shell type awareness, command portability, UTF-8 readability, console integrity, validation-command survivability, parser-error handling, and display-vs-file corruption distinction satisfied or PARTIAL with explicit `TERMINAL SURVIVABILITY FINDINGS`, `SHELL COMPATIBILITY FINDINGS`, and `ENCODING READABILITY FINDINGS`.
- [ ] **Compositional structure (G7)** — [`composition-awareness-checklist.md`](composition-awareness-checklist.md) satisfied or PARTIAL with explicit deferrals and **A/B/C/D** decision recorded (**before** final responsive closure and freeze).
- [ ] **Design intent QA** — [`design-intent-checklist.md`](design-intent-checklist.md) satisfied or PARTIAL with explicit `DESIGN INTENT FINDINGS` for radius, surfaces, CTA philosophy, UI weight, shadow/border restraint, and SaaS contamination.
- [ ] **Design token QA** — [`design-token-checklist.md`](design-token-checklist.md) satisfied or PARTIAL with explicit `DESIGN TOKEN FINDINGS` for semantic token intent, hierarchy, aliases, override governance, responsive/state token integrity, token drift, and design-system trust.
- [ ] **Implementation reliability QA** — [`implementation-reliability-checklist.md`](implementation-reliability-checklist.md) satisfied or PARTIAL with explicit `IMPLEMENTATION RELIABILITY FINDINGS` for stability, deterministic rebuilds, scoped fixes, override/include/breakpoint integrity, regression survivability, and implementation readability.
- [ ] **Cadence governance** — [`cadence-governance-checklist.md`](cadence-governance-checklist.md) satisfied or PARTIAL with explicit `CADENCE FINDINGS` for inter-screen narrative pacing.
- [ ] **Responsive intent governance** — [`responsive-intent-checklist.md`](responsive-intent-checklist.md) satisfied or PARTIAL with explicit `RESPONSIVE INTENT FINDINGS` for hierarchy survival, mobile cadence, composition collapse, CTA collapse, and stack integrity.
- [ ] **Content density governance** — [`content-density-checklist.md`](content-density-checklist.md) satisfied or PARTIAL with explicit `CONTENT DENSITY FINDINGS` for information pressure, scanning rhythm, proof pacing, trust density, overload taxonomy, and CTA survival.
- [ ] **Interaction intent governance** — [`interaction-intent-checklist.md`](interaction-intent-checklist.md) satisfied or PARTIAL with explicit `INTERACTION INTENT FINDINGS` for interaction semantics, hover authority, CTA behavior consistency, motion restraint, dead zones, overload, and contamination.
- [ ] **State consistency governance** — [`state-consistency-checklist.md`](state-consistency-checklist.md) satisfied or PARTIAL with explicit `STATE CONSISTENCY FINDINGS` for hover/focus/active/disabled/loading/validation/success/error integrity, CTA state consistency, mobile state continuity, and accessibility-state drift.
- [ ] **Accessibility intent governance** — [`accessibility-intent-checklist.md`](accessibility-intent-checklist.md) satisfied or PARTIAL with explicit `ACCESSIBILITY FINDINGS` for semantic accessibility, focus survivability, keyboard continuity, assistive predictability, contrast trust, form seriousness, mobile accessibility continuity, and accessibility drift.
- [ ] **QA confidence governance** — [`qa-confidence-checklist.md`](qa-confidence-checklist.md) satisfied or PARTIAL with explicit `QA CONFIDENCE FINDINGS` for evidence levels, scoped PASS/PARTIAL/FAIL boundaries, inferred/assumed/unknown validation, verification traceability, and QA drift taxonomy.
- [ ] **Human escalation governance** — [`human-escalation-checklist.md`](human-escalation-checklist.md) satisfied or PARTIAL with explicit `HUMAN ESCALATION FINDINGS` for decision boundary level, stop conditions, contradiction escalation, HITL visibility, assumption thresholds, authority integrity, and escalation drift taxonomy.
- [ ] **Multi-agent coordination governance** — [`multi-agent-coordination-checklist.md`](multi-agent-coordination-checklist.md) satisfied or PARTIAL with explicit `MULTI-AGENT FINDINGS` for responsibility boundaries, reviewer independence, validator integrity, escalation ownership, orchestration clarity, handoff survivability, and multi-agent drift taxonomy.
- [ ] **Strategic intent governance** — [`strategic-intent-checklist.md`](strategic-intent-checklist.md) satisfied or PARTIAL with explicit `STRATEGIC INTENT FINDINGS` for business priority, conversion hierarchy, proof hierarchy, operational trust, stakeholder intent, local optimization boundaries, and strategic drift taxonomy.
- [ ] **Temporal evolution governance** — [`temporal-evolution-checklist.md`](temporal-evolution-checklist.md) satisfied or PARTIAL with explicit `TEMPORAL EVOLUTION FINDINGS` for freeze-state integrity, version lineage, governed evolution, controlled override pressure, iterative-change accumulation, continuity checkpoints, and project drift survivability.
- [ ] **Operational workflow governance** — [`execution-discipline-checklist.md`](execution-discipline-checklist.md) satisfied or PARTIAL with explicit `WORKFLOW DISCIPLINE FINDINGS` for task-boundary integrity, execution order, checkpoint integrity, freeze validation, handoff stability, continuity checkpoint, unsafe parallel modification, and workflow drift taxonomy.
- [ ] **Production readiness governance** — [`production-readiness-checklist.md`](production-readiness-checklist.md) satisfied or PARTIAL with explicit `PRODUCTION READINESS FINDINGS` for delivery survivability, handoff survivability, onboarding readability, maintainability continuity, future-edit safety, deployment survivability, frozen-build survivability, and lifecycle survivability.
- [ ] **Context survivability governance** — [`context-survivability-checklist.md`](context-survivability-checklist.md) satisfied or PARTIAL with explicit `CONTEXT SURVIVABILITY FINDINGS` for compression integrity, checkpoint persistence, freeze-state memory, escalation memory, governance memory, continuity reconstruction, and context drift taxonomy.
- [ ] **Failure recovery governance** — [`failure-recovery-checklist.md`](failure-recovery-checklist.md) satisfied or PARTIAL with explicit `FAILURE RECOVERY FINDINGS` for trusted-state recovery, rollback integrity, freeze restoration, degraded-state handling, continuity restoration, recovery traceability, and recovery drift taxonomy.
- [ ] **Cross-project transfer governance** — [`cross-project-transfer-checklist.md`](cross-project-transfer-checklist.md) satisfied or PARTIAL with explicit `CROSS-PROJECT TRANSFER FINDINGS` when prior-project knowledge influences the scope.
- [ ] **Governance minimalism** — [`governance-minimalism-checklist.md`](governance-minimalism-checklist.md) satisfied or PARTIAL with explicit `GOVERNANCE MINIMALISM FINDINGS` when governance proportionality, cognitive load, checklist fatigue, process survivability, or governance-to-value risk affects the scope.
- [ ] **Risk weighting governance** — [`risk-weighting-checklist.md`](risk-weighting-checklist.md) satisfied or PARTIAL with explicit `RISK WEIGHTING FINDINGS` when severity proportionality, escalation relevance, signal-to-noise ratio, critical-path visibility, or prioritization drift affects the scope.
- [ ] **Adaptive governance** — [`adaptive-governance-checklist.md`](adaptive-governance-checklist.md) satisfied or PARTIAL with explicit `ADAPTIVE GOVERNANCE FINDINGS` when discipline layer, adaptive QA depth, contextual escalation, process scaling, governance fit, or survivability balance affects the scope.
- [ ] **Governance economics** — [`governance-economics-checklist.md`](governance-economics-checklist.md) satisfied or PARTIAL with explicit `GOVERNANCE ECONOMICS FINDINGS` when operational cost awareness, governance efficiency, validation-cost QA, review allocation, sustainability balancing, or governance ROI affects the scope.
- [ ] **Cognitive load governance** — [`cognitive-load-checklist.md`](cognitive-load-checklist.md) satisfied or PARTIAL with explicit `COGNITIVE LOAD FINDINGS` when review readability, signal-to-noise clarity, reviewer sustainability, governance readability, cognitive survivability, or cognitive drift affects the scope.
- [ ] **Governance compression governance** — [`governance-compression-checklist.md`](governance-compression-checklist.md) satisfied or PARTIAL with explicit `GOVERNANCE COMPRESSION FINDINGS` when operational mode, deployability, compression integrity, mode transition, governance scalability, portability, or density scaling affects the scope.
- [ ] **Reasoning visibility governance** — [`reasoning-visibility-checklist.md`](reasoning-visibility-checklist.md) satisfied or PARTIAL with explicit `REASONING VISIBILITY FINDINGS` when reasoning visibility, decision traceability, escalation explainability, prioritization transparency, uncertainty visibility, assumption disclosure, or traceable conclusions affect the scope.
- [ ] **Organizational memory governance** — [`organizational-memory-checklist.md`](organizational-memory-checklist.md) satisfied or PARTIAL with explicit `ORGANIZATIONAL MEMORY FINDINGS` when lesson survivability, operational wisdom, rediscovery avoidance, historical traceability, institutional readability, or continuity inheritance affects the scope.
- [ ] **Governance evolution governance** — [`governance-evolution-checklist.md`](governance-evolution-checklist.md) satisfied or PARTIAL with explicit `GOVERNANCE EVOLUTION FINDINGS` when controlled evolution, refinement traceability, continuity-safe change, methodology review, adaptive survivability, or historical-lineage QA affects the scope.
- [ ] **Trust calibration governance** — [`trust-calibration-checklist.md`](trust-calibration-checklist.md) satisfied or PARTIAL with explicit `TRUST CALIBRATION FINDINGS` when calibrated trust, confidence proportionality, uncertainty visibility, explainable reliability, credibility survivability, or trust traceability affects the scope.
- [ ] **Quarantine** — any un-matrixed section flagged for human decision, not silently shipped (§7).
- [ ] **Source priority** — P0–P6 applied; archive never overrides active version (§8).

---

## Design-to-code honesty (overlay)

- [ ] Ambiguous mockup areas flagged **SAFE UNKNOWN** — not guessed in markup.
- [ ] Observed, inferred, assumed, and unknown source reads are separated before implementation confidence is claimed.
- [ ] Primary, derived, interpreted, transformed, summarized, inferred, and unknown-origin sources are classified before source authority is claimed.
- [ ] Source-to-build fidelity is not inferred from screenshot similarity, visual polish, or "looks close" language without traceable source transfer, approximation disclosure, and calibrated reconstruction confidence.
- [ ] Clean-start integrity is not inferred from current workspace appearance; active source, stale residue, reset posture, and reconstruction bootstrap readiness are visible.
- [ ] First-screen fidelity is not inferred from one viewport screenshot; header, hero, atmosphere, background, overlay, mobile navigation, and conversion layers have separate ownership or disclosed SAFE UNKNOWN.
- [ ] Background and asset fidelity are not inferred from visual similarity; background ownership, overlay rationale, media source, asset state, and transformation traceability are visible.
- [ ] Commercial landing quality is not inferred from polished UI; commercial density, proof pacing, CTA pressure rhythm, atmosphere continuity, and anti-SaaS / beautification drift are checked when material.
- [ ] Terminal validation quality is not inferred from a command that failed to parse, used the wrong shell syntax, produced unreadable output, or relied on assumed portability.
- [ ] File corruption is not inferred from broken live terminal rendering; display-level encoding corruption and file-level content corruption are separated before claims are made.
- [ ] A polished downstream artifact is not treated as stronger source authority than the original source without explicit human/project promotion.
- [ ] Missing or ambiguous interaction states are reported as **SAFE UNKNOWN**, not filled with fake UX invention.
- [ ] Missing or ambiguous UI states are reported as **SAFE UNKNOWN**, not filled with fake disabled, loading, validation, success, or error behavior.
- [ ] Missing or ambiguous accessibility evidence is reported as **SAFE UNKNOWN**, not filled with ARIA spam, fake semantics, or compliance theater.
- [ ] No pixel-perfect claim in v0.
- [ ] Token/color gaps documented vs handoff.
- [ ] Token authority, alias ambiguity, local overrides, responsive token gaps, and state token gaps documented as `DESIGN TOKEN FINDINGS` or **SAFE UNKNOWN** when material.
- [ ] Implementation ownership, rebuild path, include dependencies, override rationale, breakpoint authority, and regression impact documented as `IMPLEMENTATION RELIABILITY FINDINGS` or **SAFE UNKNOWN** when material.
- [ ] QA confidence does not exceed evidence: build-only, source-only, rendered-only, screenshot-only, inferred, assumed, and unknown validation are labeled before PASS/freeze claims.
- [ ] SAFE UNKNOWN is paired with decision-boundary action: continue with disclosure, HITL requested/required, stopped, or blocked.
- [ ] Multiple agreeing agents are not treated as truth unless evidence, reviewer independence, validator integrity, and authority boundaries are visible.
- [ ] Strategic intent is not inferred from "looks polished," "feels modern," "more engagement," or local UI quality without source authority.
- [ ] Long-term continuity is not inferred from current PASS, local polish, build success, or repeated patch survival without freeze-state and version-lineage evidence.
- [ ] Workflow stability is not inferred from productivity, isolated QA, or visible output without execution order, checkpoint integrity, freeze validation, handoff stability, and continuity evidence.
- [ ] Production readiness is not inferred from successful delivery, build completion, visual correctness, freeze-state existence, or QA pass without delivery survivability, onboarding readability, maintainability continuity, future-edit safety, deployment-survivability evidence, and post-delivery stability.
- [ ] Context survivability is not inferred from a coherent summary, compressed report, prior chat memory, or reconstructed narrative without checkpoint persistence, freeze-state memory, escalation memory, and traceable unknowns.
- [ ] Failure recovery is not inferred from visual repair, restored files, build success, rollback completion, or symptom disappearance without trusted-state recovery, rollback integrity, degraded-state visibility, and continuity restoration evidence.
- [ ] Cross-project transfer safety is not inferred from prior-project success, visual familiarity, template consistency, copied governance, or implementation speed without compatibility evidence.
- [ ] Governance quality is not inferred from more layers, longer reports, fuller checklists, or process density without proportional operational value.
- [ ] Risk weighting is not inferred from more findings, more warnings, larger QA output, or more escalation without severity proportionality and critical-path visibility.
- [ ] Adaptive governance quality is not inferred from identical workflow, maximum process everywhere, full QA by default, or lightweight continuation without context-sensitive rigor justification.
- [ ] Governance economics quality is not inferred from more validation, stronger-looking survivability, longer reports, broader coverage, or more review unless operational cost, value density, validation efficiency, review allocation, and governance ROI are visible.
- [ ] Cognitive-load quality is not inferred from more detail, longer reports, more findings, more terminology, or broader visibility unless operational readability, signal-to-noise clarity, reviewer sustainability, and cognitive survivability remain visible.
- [ ] Governance compression quality is not inferred from shorter reports, fewer checks, full critical-mode inheritance, or dense governance stacks unless operational mode, deployability, compression integrity, mode transition, portability, and scalable governance depth remain visible.
- [ ] Decision quality is not inferred from confident conclusions, polished recommendations, or concise summaries without visible evidence, assumptions, tradeoffs, prioritization rationale, escalation rationale, uncertainty, and traceability.
- [ ] Organizational memory quality is not inferred from stored documentation, archived reports, old projects, or remembered lessons without operational lineage, lesson scope, historical traceability, and continuity inheritance.
- [ ] Governance evolution quality is not inferred from more rules, older rules, newer process, or mature-looking documentation without refinement source, historical rationale, proportionality, continuity impact, and mutation-risk review.
- [ ] Governance architecture quality is not inferred from more layers, more taxonomies, more rules, longer reports, or dense cross-links without cross-layer consistency, boundary clarity, contradiction survivability, and topology readability.
- [ ] Governance trust is not inferred from confident tone, polished reasoning, extensive QA, long reports, or professional presentation without calibrated trust, confidence proportionality, uncertainty visibility, explainable reliability, and trust traceability.

---

## Not claimed (v0)

- Full WCAG audit, Lighthouse CI, automated visual diff, cross-browser matrix.
- Autonomous regression or self-heal.
- Runtime multi-agent orchestration, consensus truth engine, or self-governing agent swarm.
- Autonomous business AI, conversion-optimization engine, universal marketing truth, or automatic strategic understanding.
- Autonomous maintenance AI, runtime drift engine, universal frontend lifecycle law, or permanent architectural stability guarantee.
- Autonomous workflow AI, runtime orchestration, automatic checkpoint engine, universal SDLC law, or perfect operational stability guarantee.
- Autonomous maintenance AI, runtime deployment systems, universal production laws, automatic delivery certification, or perfect maintainability.
- Autonomous memory AI, runtime persistence, automatic summarization validation, universal memory law, or perfect continuity reconstruction.
- Autonomous self-healing AI, runtime recovery system, automatic rollback, universal disaster-recovery law, or perfect resilience.
- Autonomous transfer AI, automatic compatibility detection, universal reusable systems, universal frontend standards, or automatic governance portability.
- Autonomous simplification AI, automatic governance pruning, universal minimalism law, or perfect governance balance.
- Autonomous risk AI, automatic prioritization, scoring engines, universal severity law, or perfect risk weighting.
- Autonomous governance adaptation AI, runtime policy engines, automatic QA-depth selection, universal rigor laws, or perfect contextual scaling.
- Autonomous governance optimization AI, runtime cost engines, automatic cost scoring, automatic QA allocation, universal governance economics laws, or perfect efficiency balancing.
- Cognitive-monitoring AI, runtime attention systems, automatic readability scoring, universal cognition laws, report-optimization engines, or perfect readability guarantees.
- Autonomous governance scaling AI, runtime governance orchestrators, universal operational modes, automatic report compression, automatic QA-depth allocation, or perfect deployability.
- Hidden chain-of-thought exposure, autonomous reasoning engines, automatic explainability scoring, universal transparency law, or perfect explainability.
- Autonomous institutional AI, permanent memory systems, automatic lesson extraction, universal organizational law, or perfect historical continuity.
- Autonomous governance management AI, runtime governance engines, universal governance topology, automatic contradiction resolution, or perfect architectural coherence.
- Autonomous trust engines, runtime credibility scoring, universal trust laws, automatic reliability certification, or perfect reliability.
- Autonomous design-reading AI, runtime fidelity scoring, automatic reconstruction validation, universal reconstruction laws, or perfect source fidelity.
- Automatic clean-start enforcement, workspace reset automation, first-screen decomposition engines, background ownership detection, asset lifecycle management, landing-pressure scoring, or beautification drift detection.
- Runtime terminal frameworks, shell abstraction runtimes, CLI orchestration platforms, autonomous shell adaptation, automatic encoding repair, universal shell compatibility, or guaranteed terminal integrity.

Defer to foundation checklist and factory QA lanes when scoped.
