# MARS Website Factory — Compositional structure awareness

**Status:** **documented** — governance and production **methodology** only.  
**Not:** autonomous layout AI, DOM regeneration engines, runtime regrouping, automatic visual rewrite, or any MARS capability to redesign pages without human approval.

**Purpose:** Formalize that **visual composition** (how a design *groups* and *frames* meaning for the eye) is **not always equivalent** to the **current DOM tree**. Forge can tune hierarchy, CTAs, trust, and density *within* an existing structure — but **full composition parity** may remain blocked until **structural grouping** is reconsidered under human supervision.

**Companion taxonomy:** [composition-drift-taxonomy.md](composition-drift-taxonomy.md).  
**Forge checklist (gate G7):** [`../../agents/mars-forge/composition-awareness-checklist.md`](../../agents/mars-forge/composition-awareness-checklist.md).  
**Related visual layer:** [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [visual-drift-taxonomy.md](visual-drift-taxonomy.md) (emphasis and visual drift — complementary, not duplicate).  
**Related design intent layer:** [design-system-intent-governance.md](design-system-intent-governance.md), [ui-weight-distribution-model.md](ui-weight-distribution-model.md), [cta-philosophy-governance.md](cta-philosophy-governance.md) (radius, surfaces, CTA philosophy, UI weight, restraint — complementary, not structural regrouping).  
**Related cadence / rhythm layers:** [canonical-vertical-cadence-system.md](canonical-vertical-cadence-system.md), [cadence-tier-model.md](cadence-tier-model.md), [typography-rhythm-governance.md](typography-rhythm-governance.md), [vertical-rhythm-governance.md](vertical-rhythm-governance.md) (narrative pacing, cadence tiers, and breathing governance — complementary, not structural regrouping).
**Related responsive intent layer:** [responsive-intent-governance.md](responsive-intent-governance.md), [mobile-composition-preservation.md](mobile-composition-preservation.md), [responsive-collapse-taxonomy.md](responsive-collapse-taxonomy.md) (viewport collapse must preserve hierarchy, grouping, dominance, and cadence; not “just stack everything”).
**Related source interpretation layer:** [source-interpretation-governance.md](source-interpretation-governance.md), [source-confidence-model.md](source-confidence-model.md), [source-ambiguity-taxonomy.md](source-ambiguity-taxonomy.md) (inferred grouping and hallucinated structure must be confidence-labeled before composition decisions).
**Related implementation reliability layer:** [implementation-reliability-governance.md](implementation-reliability-governance.md), [frontend-stability-model.md](frontend-stability-model.md), [implementation-drift-taxonomy.md](implementation-drift-taxonomy.md) (composition fixes must not become hidden coupling, include-chain contamination, or unsafe patch layering).

---

## 1. Positioning (non‑negotiable)

| Compositional structure awareness **is** | It **is not** |
|-------------------------------------------|---------------|
| Human-supervised governance | Autonomous redesign |
| Implementation-aware (what the repo can absorb) | A “regenerate the page” system |
| Freeze-oriented (honest PARTIAL, honest deferral) | Layout generation or creativity runtime |
| Production methodology — detect, classify, report, escalate | Pixel diff or CV automation |

**Structural regrouping** (moving markup boundaries, wrappers, section splits) remains **human-approved** — documented **STRUCTURE CHANGE**, handoff update, or explicit HITL per factory workflow. The agent **must not** silently restructure pages to “fix” composition.

---

## 2. Core concepts

### 2.1 Composition cluster

A **composition cluster** is a set of UI elements that the **source design reads as one perceptual unit**: shared focal path, shared band, shared framing, or shared conversion story in one visual beat.  
It is defined by **visual grouping intent**, not by tag names.

### 2.2 DOM grouping

**DOM grouping** is how elements are **nested and segmented in markup**: sections, wrappers, grids, include boundaries, and component splits.  
It determines where **layout and spacing hooks** naturally apply and where **freeze boundaries** often sit.

### 2.3 Visual grouping

**Visual grouping** is how the **approved visual source** suggests elements **belong together**: proximity, common background, enclosure, alignment baseline, single CTA story, price + action + offer read as one card, etc.  
**Visual grouping may differ from DOM grouping:** the design may “paint” one cluster while the build places its parts in **separate DOM zones**.

### 2.4 Structural mismatch

**Structural mismatch** (composition-vs-DOM) exists when **visual grouping intent** requires a **different segmentation** than the **current DOM** provides — so that **local tuning** (margins, typography, flex order) **improves perception** but **cannot** achieve composition parity without **regrouping markup or boundaries**.

### 2.5 Composition-aware implementation

**Composition-aware implementation** means:

- Reading the source for **clusters** and **framing**, not only for **semantic slots**.  
- **Detecting** when the implementation’s DOM zones **fight** the design’s clusters.  
- **Reporting** mismatch with a typed label ([composition-drift-taxonomy.md](composition-drift-taxonomy.md)) and a **disposition** (see §5).  
- **Choosing** either bounded visual tuning, documented **PARTIAL** freeze, or a **human-approved** structural change — **not** silent rewrites.

---

## 3. Reference lesson — Triumph V2 Screen 01 (documentation observation)

During Screen 01 visual reconciliation, Forge could improve hierarchy, CTA dominance, trust positioning, density, and spacing rhythm **within** the existing structure. A recurring **limitation** (production observation): **price band**, **CTA cluster**, and **offer framing** may **behave as one composition cluster** in the source while the **DOM** places them in **separate regions**.  

**Effect:** spacing and type tweaks **help**, but **full** alignment to the design’s **single-cluster read** may require **shared framing or regrouped wrappers** — a **structural** decision, not a polish pass.

Use this as an **illustration** only; evidence for a given build must come from the **chartered** screen and implementation pack for that project.

### 3.1 Reference lesson — Triumph V2 Screen 02 (foundation contamination bias)

**Observation (documentation):** Screen 02’s chartered source reads as a **light surface**, **white cards**, and **light composition hierarchy**. A production misread applies the site’s **global dark foundation** instead: **semantic** structure can remain acceptable while **visual role** diverges — classified as **foundation contamination bias** ([visual drift taxonomy §D](visual-drift-taxonomy.md)).

**Boundary vs this doc’s core lens:** Composition-vs-DOM awareness (§2–§5) targets **cluster segmentation vs markup**. Foundation contamination targets **inherited globals vs screen-local band intent**. The two can co-occur; **neighbor-section visual leakage** may resemble grouping drift — **type** the dominant failure ([taxonomy](visual-drift-taxonomy.md)) and run **G6** alongside **G7**.

---

## 4. Detection rules — practical questions

Answer these **during** or **immediately after** the visual reconciliation read (gate G6), recorded in gate G7 ([`composition-awareness-checklist.md`](../../agents/mars-forge/composition-awareness-checklist.md)).

| # | Question | If “yes,” investigate |
|---|----------|------------------------|
| D1 | Do **visually related** elements (one cluster read) sit in **separate DOM zones** (distant wrappers, different sections/includes)? | Composition fragmentation / false separation |
| D2 | Are we using **spacing, negative margin, or absolute positioning** mainly to **pull apart or glue** what should be one cluster? | Accidental composition split; “faking” grouping |
| D3 | Does the source show **one framing** (band, card, panel) for the cluster, while the build **lacks a shared container/background**? | Framing mismatch |
| D4 | Does **heading / landmark hierarchy** follow the DOM, but **visual hierarchy** fights **container boundaries** (eye crosses “wrong” breaks)? | Hierarchy container mismatch |
| D5 | Is the **CTA cluster** (primary + supporting actions + urgency) **split** across markup zones that the design treats as **one beat**? | CTA cluster separation |
| D6 | After semantic QA **pass** and responsive QA **pass**, does **visual reconciliation** still show **parity gap** that **spacing alone** cannot close? | Likely structural ceiling; PARTIAL freeze honesty |
| D7 | Could **regrouping** (wrappers, section merge/split) resolve the gap **without** inventing new creative layout? | Candidate for human-approved STRUCTURE CHANGE |

**Honesty:** these are **human review prompts**, not automated detectors.

---

## 5. Decision model (escalation)

| Path | Label | Meaning | Typical action |
|------|--------|---------|----------------|
| **A** | Local tuning sufficient | Mismatch **not** confirmed, or cluster alignment achievable with **token-level** spacing, type, order within existing DOM | Finish visual tweaks; document PASS or minor PARTIAL |
| **B** | Local tuning insufficient | Gap confirmed, but **unclear** whether DOM or source ambiguity is the root cause | **SAFE UNKNOWN** or PARTIAL with evidence; request charter/input clarification |
| **C** | Structural regrouping recommended | Typed composition-vs-DOM drift; parity **unlikely** without **human-approved** wrapper/section/include change | **Stop silent edits**; REPORT with taxonomy + **proposal**; HITL approves STRUCTURE CHANGE |
| **D** | SAFE UNKNOWN | Ownership of framing, grouping intent, or breakpoint composition **cannot** be established from inputs | No PASS on composition closure; record resolver |

**Rule:** **C** never auto-executes. Implementation proceeds only after **explicit human approval** and contract updates as required by the factory handoff workflow.

---

## 6. Frontend agent implications

The **Forge / frontend agent** should:

- **Detect** composition-vs-DOM tension using §4 questions and log **COMPOSITION FINDINGS** in REPORT (see checklist).  
- **Distinguish** **visual tuning** (within existing structure) from **structural regrouping** (markup/boundary change).  
- **Report and classify** using [composition-drift-taxonomy.md](composition-drift-taxonomy.md).  
- **Avoid uncontrolled rewrites** — no new wrappers, section merges, or include graph edits “for composition” without **documented approval**.

The agent should **not**:

- Present **structural regrouping** as equivalent to **spacing fixes**.  
- **Freeze** with implied “full” visual parity when §5 points to **C** or **D**.  
- Claim **automatic** composition repair or layout synthesis.

---

## 7. Freeze implications

A section may correctly remain **PARTIAL** (or **unfrozen** with explicit deferral) **even when**:

- **Semantic QA** passes (correct meaning, copy, roles).  
- **Responsive QA** passes (no overflow, breakpoints survive).  
- **Visual reconciliation** **improved** (better CTA dominance, density, trust).

…if **composition-vs-DOM mismatch** still **blocks** parity with the chartered cluster read.  

**Freeze honesty:** record **PARTIAL — composition structure**, cite drift type, and whether **A/B/C/D** applies. Full **frozen** status for that slice may require **HITL** on structure or **scope change** (e.g. accept bounded fidelity).

---

## 8. SAFE UNKNOWN — compositional context

| Situation | Why it is UNKNOWN |
|-----------|-------------------|
| **Unclear intended grouping** | Source does not show whether two bands are one cluster or two |
| **No mobile composition reference** | Cannot charter cluster behavior at key breakpoints |
| **Composition differs between exports** | Same section, conflicting cluster reads |
| **Parity impossible without redesign** | Would require new creative layout — out of governance scope |
| **Unclear ownership of framing/background** | Which block owns the band; split responsibility across includes |

**Action:** Record **SAFE UNKNOWN** and what would resolve it (annotated export, implementation-pack note, HITL).

---

## 9. Relations to adjacent layers

| Neighbor | Relationship |
|----------|----------------|
| [visual-reconciliation-layer.md](visual-reconciliation-layer.md) | Visual **emphasis** and drift; composition awareness adds **structure-vs-cluster** literacy. |
| [design-system-intent-governance.md](design-system-intent-governance.md) / [ui-weight-distribution-model.md](ui-weight-distribution-model.md) / [cta-philosophy-governance.md](cta-philosophy-governance.md) | Philosophy-level checks for surface hierarchy, CTA restraint, UI weight, and SaaS contamination; composition awareness decides whether those fixes are blocked by DOM/grouping structure. |
| [visual-drift-taxonomy.md](visual-drift-taxonomy.md) | **Visual** drift names; composition taxonomy adds **structural** mismatch names; **foundation contamination bias** ([§D](visual-drift-taxonomy.md)) addresses inheritance-vs-charter band reads. |
| [semantic-source-lock.md](../../agents/mars-forge/semantic-source-lock.md) | Semantics lock **content**; composition awareness locks honest **cluster/DOM** reporting. |
| [design-governance-layer.md](design-governance-layer.md) | Pack notes may clarify **framing** ownership; gaps feed SAFE UNKNOWN. |
| [canonical-vertical-cadence-system.md](canonical-vertical-cadence-system.md) / [cadence-tier-model.md](cadence-tier-model.md) | Cadence canon names inter-screen spacing as narrative pacing and defines `XS`–`XL` tier intent; composition awareness decides whether cadence fixes are blocked by DOM/grouping structure. |
| [typography-rhythm-governance.md](typography-rhythm-governance.md) / [vertical-rhythm-governance.md](vertical-rhythm-governance.md) | Rhythm layers name typography cadence, section breathing, density spikes, and spacing contamination; composition awareness decides whether rhythm fixes are blocked by DOM/grouping structure. |
| [responsive-intent-governance.md](responsive-intent-governance.md) / [mobile-composition-preservation.md](mobile-composition-preservation.md) / [responsive-collapse-taxonomy.md](responsive-collapse-taxonomy.md) | Responsive intent applies the cluster/DOM read to viewport collapse: grouping, dominance, CTA hierarchy, stack integrity, and mobile cadence must survive responsive changes unless a human-approved redesign says otherwise. |
| [source-interpretation-governance.md](source-interpretation-governance.md) / [source-confidence-model.md](source-confidence-model.md) / [source-ambiguity-taxonomy.md](source-ambiguity-taxonomy.md) | Source interpretation decides whether grouping is observed, inferred, assumed, unknown, or contradictory before G7 treats it as a composition finding. |
| [implementation-reliability-governance.md](implementation-reliability-governance.md) / [frontend-stability-model.md](frontend-stability-model.md) / [implementation-drift-taxonomy.md](implementation-drift-taxonomy.md) | Reliability governance decides whether composition tuning remains maintainable or has become patch layering, include-chain contamination, hidden coupling, or structural escalation drift. |

---

## 10. Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-16 | Initial compositional structure awareness — methodology only; gate G7 checklist. |
| v0.1 | 2026-05-16 | §3.1 Triumph V2 Screen 02 — **foundation contamination bias** boundary vs composition-vs-DOM. |
| v0.2 | 2026-05-16 | Linked typography and vertical rhythm governance as adjacent cadence layers. |
| v0.3 | 2026-05-16 | Linked canonical vertical cadence system and cadence tier model as adjacent narrative pacing governance. |
| v0.4 | 2026-05-17 | Linked design system intent governance, UI weight, and CTA philosophy as adjacent visual-governance layers. |
| v0.5 | 2026-05-17 | Linked Responsive Intent Governance as adjacent viewport-collapse methodology. |
| v0.6 | 2026-05-17 | Linked Source Interpretation Governance for inferred grouping, false grouping, hallucinated structure, and confidence reporting. |
| v0.7 | 2026-05-17 | Linked Implementation Reliability Governance for patch layering, include-chain contamination, hidden coupling, and structural escalation drift. |
