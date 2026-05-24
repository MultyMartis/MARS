# MARS Website Factory — Responsive Intent Governance

**Status:** **documented** — Website Factory preferred responsive methodology for human-supervised frontend production.  
**Not:** automatic responsive AI, runtime layout engine, universal mobile aesthetic, breakpoint generator, screenshot diff, or autonomous redesign.

**Core principle:** responsive implementation must preserve **visual / semantic / compositional intent** across viewports.  
It is not merely “make it fit,” “stack blocks,” “remove overflow,” or “survive mobile.”

**Companion documents:** [mobile-composition-preservation.md](mobile-composition-preservation.md), [responsive-collapse-taxonomy.md](responsive-collapse-taxonomy.md).  
**Related layers:** [source-interpretation-governance.md](source-interpretation-governance.md), [source-confidence-model.md](source-confidence-model.md), [source-ambiguity-taxonomy.md](source-ambiguity-taxonomy.md), [design-intent-transfer-governance.md](design-intent-transfer-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [compositional-structure-awareness.md](compositional-structure-awareness.md), [canonical-vertical-cadence-system.md](canonical-vertical-cadence-system.md), [design-system-intent-governance.md](design-system-intent-governance.md), [design-token-intelligence-governance.md](design-token-intelligence-governance.md), [implementation-reliability-governance.md](implementation-reliability-governance.md), [content-density-governance.md](content-density-governance.md), [interaction-intent-governance.md](interaction-intent-governance.md), [state-behavioral-consistency-governance.md](state-behavioral-consistency-governance.md), [accessibility-intent-governance.md](accessibility-intent-governance.md).  
**Forge checklist:** [`../../agents/mars-forge/responsive-intent-checklist.md`](../../agents/mars-forge/responsive-intent-checklist.md).  
**RU commercial landings:** canonical QA widths — [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md); typography/overflow authority — [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md). Generic breakpoint lists elsewhere are **supplementary**.

---

## 1. Positioning

Responsive Intent Governance sits between visual reconciliation, composition awareness, cadence governance, and frontend responsive QA.

| Responsive behavior **is** | Responsive behavior **is not** |
|----------------------------|--------------------------------|
| Intent preservation across viewport states | Survival-only fitting |
| Human-supervised breakpoint interpretation | Automatic mobile redesign |
| Hierarchy, cadence, CTA, grouping, and visual-weight governance | “Just stack everything” |
| A reporting vocabulary for responsive drift | A mandatory one-size mobile style |

The governance question is not “does it fit?”  
The governance question is: **does the viewport version still read like the same authored section with the same hierarchy, pacing, emphasis, grouping, and operational readability?**

---

## 2. Canonical Definition

**Responsive intent preservation** means the mobile, tablet, and desktop states preserve:

- **Hierarchy** — primary, secondary, supporting, and proof elements remain correctly ordered and weighted.
- **Cadence** — section and intra-section rhythm changes deliberately, not by accidental compression.
- **Emphasis** — CTA, proof, trust, media, and headings keep their intended dominance relationships.
- **Composition intent** — clusters, framing, and reading paths remain legible after collapse.
- **CTA pacing** — conversion moments remain guided and breathable, not screaming or buried.
- **Visual weight** — surfaces, cards, icons, and media do not equalize into flat noise.
- **Semantic grouping** — related content remains perceptually grouped even when grid mechanics change.
- **Operational readability** — mobile is readable and usable under real attention constraints, not merely compact.

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Responsive intent preservation** | Maintaining visual, semantic, and compositional purpose across viewport changes. |
| **Composition collapse** | A desktop cluster loses its authored grouping or dominance when collapsed. |
| **Hierarchy survival** | The main reading ladder remains intact after stacking, wrapping, or reordering. |
| **Mobile cadence** | Separate pacing logic for narrow screens; not a simple scale-down of desktop spacing. |
| **Stack integrity** | A vertical stack preserves grouping, order, emphasis, and breath rather than becoming a list of equal blocks. |
| **Responsive drift** | Any viewport-specific departure from approved intent that is not an approved redesign. |
| **Compression threshold** | The point where reducing width/spacing starts harming hierarchy, tap safety, readability, or cluster identity. |
| **Mobile fatigue** | Reader exhaustion caused by endless dense stacks, repeated cards, CTA pressure, or insufficient resets. |
| **Desktop-thinking contamination** | Desktop grid assumptions copied into mobile without re-reading mobile attention and cadence. |
| **CTA collapse** | Primary, secondary, and supporting conversion elements lose proper order or weight at smaller widths. |
| **Visual flattening** | Dominant and supporting elements become equal-weight after collapse. |
| **Responsive hierarchy inversion** | A secondary object becomes visually or sequentially stronger than the primary object on mobile. |
| **Stack contamination** | One stack inherits spacing, card weight, CTA treatment, or rhythm from another without source authority. |
| **Mobile overload** | Too many dense controls, cards, badges, icons, or proof items in one narrow viewport beat. |
| **Survivability vs fidelity** | Survival asks whether it fits; fidelity asks whether the intent still reads. |

---

## 4. Canonical Rules

- **Not every desktop grid should fully flatten.** Some grids need grouping, priority splitting, carousel/summary treatment, or staged disclosure only when source or HITL allows it.
- **Mobile spacing requires separate cadence logic.** Desktop rhythm may compress, but title/body breathing, cluster gaps, CTA isolation, and transition pacing must remain authored.
- **CTA hierarchy may need rebalance on mobile.** Primary actions should not become giant pressure blocks; secondary actions should not overtake or vanish without intent.
- **Dense sections require breathing on small viewports.** Specs, proof, equipment lists, reviews, forms, and price blocks need resets to avoid mobile fatigue.
- **Mobile requires operational readability, not merely compactness.** Tap zones, line length, paragraph rhythm, and visible grouping are part of intent preservation.
- **Desktop composition intent must survive collapse.** Dominance relationships and visual clusters cannot be destroyed simply because the layout stacks.
- **Responsive redesign is not automatically acceptable.** Some structures must preserve hierarchy, grouping, and dominance relationships; if preservation seems impossible, escalate instead of inventing a new mobile concept.

---

## 5. Survivability vs Fidelity

| Survivability-only responsive QA | Intent-preserving responsive QA |
|----------------------------------|---------------------------------|
| No overflow | No overflow **and** hierarchy preserved |
| Blocks stack | Stack preserves cluster identity and pacing |
| Text wraps | Text remains readable with correct cadence |
| Buttons fit | CTA hierarchy and pressure remain appropriate |
| Cards resize | Visual weight and grouping remain source-faithful |
| Section fits viewport | Section still has a readable role in the page story |

Survivability is necessary but insufficient. A page can pass mechanical responsive checks while failing responsive intent through hierarchy inversion, visual flattening, CTA collapse, or endless-stack fatigue.

---

## 6. Responsive Redesign Boundary

Viewport-specific redesign is a governance decision, not a default responsive tactic.

Acceptable responsive adaptation:

- Reordering within an approved reading flow.
- Changing grid columns while preserving grouping and dominance.
- Adjusting spacing tiers for mobile cadence.
- Rebalancing CTA presentation while preserving CTA semantics.
- Reducing decorative weight to protect readability.

Requires HITL / documented decision:

- Splitting or merging sections.
- Replacing a dominant cluster with a different mobile pattern.
- Removing proof, CTA, price, trust, or semantic groups.
- Turning desktop hierarchy into a new mobile narrative.
- Inventing a mobile-specific aesthetic not present in the approved source.

---

## 7. Forge / QA Expectations

When Forge is selected, responsive intent is reviewed before freeze:

- Run [`responsive-intent-checklist.md`](../../agents/mars-forge/responsive-intent-checklist.md) alongside visual reconciliation, compositional structure, design intent, cadence, and rhythm QA.
- Record **RESPONSIVE INTENT FINDINGS** when breakpoint behavior affects hierarchy, cadence, CTA pacing, composition collapse, stack integrity, or mobile operational readability.
- Run design token QA when breakpoint-specific tokens, responsive aliases, mobile spacing/type/radius/shadow values, or local responsive overrides affect continuity; record `DESIGN TOKEN FINDINGS` per [`design-token-checklist.md`](../../agents/mars-forge/design-token-checklist.md).
- Run implementation reliability QA when breakpoint fixes risk patch layering, hidden coupling, emergency overrides, width regressions, or rebuild unpredictability; record `IMPLEMENTATION RELIABILITY FINDINGS` per [`implementation-reliability-checklist.md`](../../agents/mars-forge/implementation-reliability-checklist.md).
- Run content density QA when breakpoint behavior amplifies information pressure, dense-stack fatigue, trust-wall drift, proof saturation, or CTA burial; record `CONTENT DENSITY FINDINGS` per [`content-density-checklist.md`](../../agents/mars-forge/content-density-checklist.md).
- Run source interpretation QA when viewport behavior depends on inferred, missing, ambiguous, unknown, or contradictory source authority; record `SOURCE INTERPRETATION FINDINGS` per [`source-interpretation-checklist.md`](../../agents/mars-forge/source-interpretation-checklist.md).
- Run reconstruction fidelity QA when breakpoint behavior creates source-to-build fidelity, approximation, hierarchy fidelity, semantic transfer, or fidelity survivability risk; record `RECONSTRUCTION FIDELITY FINDINGS` per [`reconstruction-fidelity-checklist.md`](../../agents/mars-forge/reconstruction-fidelity-checklist.md).
- Run interaction intent QA when breakpoint behavior affects hover-to-tap translation, mobile CTA behavior, motion restraint, tap ambiguity, or scroll-motion fatigue; record `INTERACTION INTENT FINDINGS` per [`interaction-intent-checklist.md`](../../agents/mars-forge/interaction-intent-checklist.md).
- Run state consistency QA when breakpoint behavior affects focus visibility, tap/active feedback, disabled/loading/validation states, CTA state hierarchy, or mobile state continuity; record `STATE CONSISTENCY FINDINGS` per [`state-consistency-checklist.md`](../../agents/mars-forge/state-consistency-checklist.md).
- Run accessibility intent QA when breakpoint behavior affects labels, reading order, keyboard/focus continuity, tap clarity, form messages, sticky obstruction, or mobile accessibility collapse; record `ACCESSIBILITY FINDINGS` per [`accessibility-intent-checklist.md`](../../agents/mars-forge/accessibility-intent-checklist.md).
- Classify failures using [responsive-collapse-taxonomy.md](responsive-collapse-taxonomy.md).
- Treat findings as human-supervised governance, not automated scoring.
- Escalate **SAFE UNKNOWN** when no mobile source, responsive rules, or HITL decision establishes breakpoint intent.

---

## 8. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory responsive lessons:

- A semantically correct mobile stack can still flatten the hero, trust, price, and CTA hierarchy.
- Dense equipment, proof, and service sections need separate mobile cadence instead of pure compression.
- CTA blocks can become visually louder on mobile than the source intended, creating pressure rather than guidance.
- Composition clusters such as price + offer + CTA may require preserved grouping even when columns collapse.
- Mobile survivability is not enough for an operational landing page; the narrow viewport must remain readable, serious, and paced.

These are Website Factory lessons, not Triumph-only layout prescriptions.

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Missing mobile source | Breakpoint hierarchy and composition cannot be chartered beyond survivability. |
| Conflicting responsive rules | Implementation pack, desktop export, and existing code imply different collapse behavior. |
| Unclear cluster dominance | Cannot tell which object must remain dominant after collapse. |
| Dense section overload unresolved | No authority for whether to split, summarize, disclose, or preserve full stack. |
| CTA mobile pressure unclear | No approved guidance for mobile CTA size, repetition, or order. |
| Current structure blocks fidelity | Existing DOM cannot preserve grouping without structural change. |

**Action:** document the resolver: mobile export, annotated implementation-pack note, responsive rule, section-source matrix update, or HITL decision.

---

## 10. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Responsive Intent Governance layer — intent-preserving responsive methodology only. |
| v0.1 | 2026-05-17 | Linked Content Density Governance for mobile information pressure, dense-stack fatigue, and CTA burial interactions. |
| v0.2 | 2026-05-17 | Linked Source Interpretation Governance for missing mobile source, inferred breakpoint behavior, and source confidence reporting. |
| v0.3 | 2026-05-17 | Linked Interaction Intent Governance for mobile interaction restraint, tap ambiguity, hover translation, and motion fatigue reporting. |
| v0.4 | 2026-05-17 | Linked State & Behavioral Consistency Governance for mobile state continuity, focus/active/validation/loading consistency, and `STATE CONSISTENCY FINDINGS`. |
| v0.5 | 2026-05-17 | Linked Accessibility Intent Governance for mobile accessibility continuity, labels, reading order, tap clarity, focus, and `ACCESSIBILITY FINDINGS`. |
| v0.6 | 2026-05-17 | Linked Design Token Intelligence Governance for responsive token integrity, breakpoint-token divergence, and `DESIGN TOKEN FINDINGS`. |
| v0.7 | 2026-05-17 | Linked Implementation Reliability Governance for breakpoint integrity, emergency override risk, regression survivability, and `IMPLEMENTATION RELIABILITY FINDINGS`. |
| v0.8 | 2026-05-17 | Linked Design Intent Transfer & Reconstruction Fidelity Governance for responsive source-to-build fidelity, approximation transparency, and fidelity survivability. |
