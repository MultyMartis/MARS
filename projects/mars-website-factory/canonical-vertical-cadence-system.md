# MARS Website Factory — Canonical Vertical Cadence System

**Status:** **documented** — Website Factory core canon for human-supervised production governance.  
**Not:** universal spacing truth, automatic cadence engine, runtime pacing AI, autonomous visual balancing, screenshot diff, or layout generation.

**Core principle:** **inter-screen spacing = narrative pacing.**  
It is not random margin/padding, cosmetic whitespace, or a local implementation afterthought.

**Companion model:** [cadence-tier-model.md](cadence-tier-model.md).  
**Related rhythm layer:** [vertical-rhythm-governance.md](vertical-rhythm-governance.md), [typography-rhythm-governance.md](typography-rhythm-governance.md).  
**Related full-page continuity layer:** [full-page-cadence-continuity-governance.md](full-page-cadence-continuity-governance.md).  
**Related visual layers:** [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [compositional-structure-awareness.md](compositional-structure-awareness.md).  
**Related design intent layer:** [design-system-intent-governance.md](design-system-intent-governance.md), [ui-weight-distribution-model.md](ui-weight-distribution-model.md), [cta-philosophy-governance.md](cta-philosophy-governance.md).  
**Related token intelligence layer:** [design-token-intelligence-governance.md](design-token-intelligence-governance.md), [token-semantic-layer-model.md](token-semantic-layer-model.md) (spacing tokens preserve cadence intent; not every repeated gap deserves global token scope).  
**Related responsive intent layer:** [responsive-intent-governance.md](responsive-intent-governance.md), [mobile-composition-preservation.md](mobile-composition-preservation.md) (mobile cadence preserves hierarchy, CTA pacing, stack integrity, and transition breathing; not survivability-only compression).  
**Related content density layer:** [content-density-governance.md](content-density-governance.md), [information-pressure-model.md](information-pressure-model.md) (cadence must pace information pressure, proof density, and readability recovery; not only visual spacing).  
**Forge checklist:** [`../../agents/mars-forge/cadence-governance-checklist.md`](../../agents/mars-forge/cadence-governance-checklist.md).

---

## 1. Positioning

Vertical cadence is the Website Factory governance layer that controls how one screen hands attention to the next. It treats page flow as a sequence of authored narrative beats:

- entry
- proof
- explanation
- dense comparison
- CTA
- closure

Spacing between these beats must be deliberate enough to prevent section collision, density collapse, visual exhaustion, and accidental spacing inheritance.

This system does **not** make every landing page mathematically identical. A project may define its own spacing scale, but the relationship between adjacent sections must be explicit, consistent, and reviewable.

---

## 2. Canonical Definition

**Inter-screen spacing** is the authored transition between two page sections or screen bands. It carries:

| Function | Meaning |
|----------|---------|
| **Pacing role** | How quickly the reader moves from one narrative obligation to the next. |
| **Breathing role** | How much perceptual reset the eye receives before the next density or mood. |
| **Density role** | Whether a sparse, medium, or dense section needs support before/after. |
| **Transition role** | Whether the boundary changes mood, contrast, CTA intensity, or content type. |
| **Continuity role** | Whether the landing reads as one authored story instead of stitched slices. |

Therefore the QA question is not “what margin is this?”  
The QA question is: **does this boundary pace the story correctly?**

---

## 3. Canonical Vocabulary

| Concept | Meaning |
|---------|---------|
| **Cadence tier** | A named spacing intention used for a section boundary or intra-section transition; see [cadence-tier-model.md](cadence-tier-model.md). |
| **Pacing reset** | A deliberate pause before a new mood, density, CTA moment, or narrative chapter. |
| **Visual breathing** | Perceived air that lets the reader recover from density or contrast pressure. |
| **Transition compression** | A boundary is too tight for the change it carries. |
| **Section collision** | Adjacent sections visually crash together; the boundary has no readable transition. |
| **Density bridge** | A controlled step between dense and light sections so the page does not jump from wall-of-content to void. |
| **Dark/light cadence** | Cadence decisions around surface contrast changes; often needs reset space. |
| **Cadence continuity** | Adjacent sections maintain a purposeful pacing arc without identical spacing everywhere. |
| **Rhythm reset** | A cadence break that reorients the reader before a new role or visual mood. |
| **Visual exhaustion** | The accumulated fatigue from compressed dense sections, irregular gaps, or overlong unbroken stacks. |
| **Cadence escalation** | The page intentionally increases breathing or isolation as narrative stakes rise, often before CTA or footer closure. |
| **Cadence flattening** | Every section uses the same spacing despite different density, mood, and story role. |
| **Cadence contamination** | A prior section, global utility, framework default, or imported style imposes spacing not chartered by the current source. |

---

## 4. Canonical Rules

- **Dark → light and light → dark transitions may require a cadence reset.** Contrast shifts amplify spacing errors; a valid reset is not “extra margin,” it is transition authorship.
- **Dense grid sections require breathing before and after.** Card grids, proof matrices, icon rows, price tables, technical lists, and review stacks increase section pressure.
- **Multiple adjacent dense/light sections require cadence breathing adjustments.** Do not let a dense middle run inherit one repeated gap until the landing feels compressed.
- **CTA-heavy sections require isolation space.** Primary conversion moments need enough vertical separation from proof, pricing, helper text, and next-section noise.
- **Footer requires closure cadence.** Footer spacing should feel terminal and intentional, not leftover padding or a sudden drop after the last CTA.
- **Mobile cadence differs from desktop cadence.** Mobile should compress intelligently while preserving title/body breathing, item gaps, CTA isolation, and tap-safe rhythm.
- **Cadence should feel authored, not mathematical spam.** Deterministic tiers guide decisions; they do not excuse identical spacing everywhere.
- **Cadence changes must be source-anchored.** Use active design exports, implementation pack notes, section maps, and human-approved decisions. If authority is missing, record **SAFE UNKNOWN**.
- **Same-background boundaries should avoid duplicated rhythm.** If adjacent sections share one surface/environment, usually one side owns the boundary spacing.
- **Different-background boundaries may use two-sided rhythm.** Contrast, density, or mood transitions can justify both exit and entry breathing.
- **Focal commercial continuity matters.** Spacing should not make sections feel like isolated blocks or reset the sales narrative without reason.

---

## 5. Dense / Light Adjacency Rule

When three or more adjacent sections alternate density or surface mood, run a page-level cadence read rather than reviewing each boundary alone.

Review:

- Does the middle of the page become compressed because every screen inherited the previous gap?
- Does a dense grid receive a pacing reset before the next dense, CTA, or dark/light transition?
- Does a light section after density provide breathing without becoming a giant whitespace desert?
- Does the sequence preserve narrative momentum rather than presenting unrelated screenshots?

**Canonical example:** Triumph V2 `03 → 04 → 05` exposed the production risk: a middle run can remain semantically correct while the page-level cadence collapses through section collision, compressed transitions, and insufficient breathing between dense/light narrative beats.

This is a **Website Factory lesson**, not a Triumph-only rule.

---

## 6. Anti-Patterns

| Anti-pattern | Why it is forbidden drift |
|--------------|---------------------------|
| **Random spacing values** | Makes cadence subjective and unreviewable. |
| **Accidental inheritance** | Current section spacing comes from globals, framework defaults, or previous screens. |
| **Section collision** | Boundary fails to separate narrative beats. |
| **Giant whitespace deserts** | Pacing stalls without narrative reason. |
| **Compressed CTA transitions** | Conversion moments compete with adjacent content. |
| **Identical cadence everywhere** | Different section roles are flattened into one mechanical rhythm. |
| **Zero-breathing dense stacks** | Dense grids or lists run together until the reader fatigues. |
| **SaaS dashboard spacing contamination** | Compact app UI spacing leaks into marketing narrative flow. |
| **Figma slice compression drift** | Cropped exports or screenshot framing cause implementation to under-space inter-screen transitions. |
| **Cadence contamination** | A section inherits spacing from a source that is not authoritative for its role. |
| **Same-background double-gap** | Shared-surface sections use both top and bottom spacing by accident. |
| **Section-stack feeling** | The page reads as unrelated blocks instead of one authored landing. |

---

## 7. Forge / QA Expectations

When Forge is selected, cadence is reviewed before freeze:

- Run `CADENCE FINDINGS` alongside visual reconciliation, composition awareness, and rhythm governance.
- Run `DESIGN TOKEN FINDINGS` when spacing tokens, cadence aliases, breakpoint spacing values, or local margin/padding overrides affect narrative pacing; use [`design-token-checklist.md`](../../agents/mars-forge/design-token-checklist.md).
- Run `DESIGN INTENT FINDINGS` when cadence decisions interact with CTA weight, surface hierarchy, visual restraint, or SaaS contamination.
- Check cadence continuity across the current section and its immediate neighbors.
- Check transition pacing for dark/light, sparse/dense, proof/CTA, and CTA/footer boundaries.
- Check density stacks for breathing and visual exhaustion risk.
- Run content density QA when dense stacks create information pressure, proof saturation, scanning fatigue, trust-wall drift, or CTA dilution; record `CONTENT DENSITY FINDINGS` per [`content-density-checklist.md`](../../agents/mars-forge/content-density-checklist.md).
- Check footer closure cadence.
- Check mobile cadence survivability when mobile source or responsive rules exist.
- Run responsive intent QA when mobile cadence affects hierarchy, CTA pacing, stack integrity, or operational readability; record `RESPONSIVE INTENT FINDINGS` per [`responsive-intent-checklist.md`](../../agents/mars-forge/responsive-intent-checklist.md).

Cadence QA is **human-supervised methodology**. It does not claim automated scoring, adaptive spacing, or autonomous balancing.

---

## 8. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Missing cadence scale | No approved tier model or project spacing pack exists. |
| Conflicting adjacent exports | Neighbor screens imply incompatible transition breathing. |
| Missing mobile cadence source | Mobile pacing cannot be chartered beyond survivability. |
| Cropped Figma slices | Inter-screen boundary may be hidden by export framing. |
| DOM order differs from source order | Implemented adjacency may not match approved narrative sequence. |
| Global spacing source unclear | Cannot tell whether inherited gap is intentional or contamination. |
| Dense stack intent unclear | No authority for whether the section should compress, reset, or split. |

**Action:** document the resolver: cadence tier table, annotated export, implementation-pack note, section-source matrix update, or HITL decision.

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-16 | Initial Website Factory core canon for vertical cadence as narrative pacing; introduces cadence tier relationship, anti-patterns, Triumph V2 03→04→05 lesson, and Forge `CADENCE FINDINGS` hook. |
| v0.1 | 2026-05-17 | Linked design system intent governance for CTA weight, surface hierarchy, visual restraint, and SaaS contamination interactions. |
| v0.2 | 2026-05-17 | Linked Responsive Intent Governance for mobile cadence, stack integrity, and viewport transition pacing. |
| v0.3 | 2026-05-17 | Linked Content Density Governance for information pressure, proof density, readability recovery, and cadence-density interaction. |
| v0.4 | 2026-05-17 | Linked Design Token Intelligence Governance for spacing-token continuity, cadence aliases, responsive token integrity, and `DESIGN TOKEN FINDINGS`. |
| v0.5 | 2026-05-18 | Added V4 transition continuity rules for same-background collapse, different-background reset rhythm, and no-isolated-block governance. |
