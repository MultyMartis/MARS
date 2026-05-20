# MARS Website Factory — Design System Intent Governance

**Status:** **documented** — Website Factory preferred commercial production philosophy for human-supervised frontend work.  
**Not:** raw token registry, color system, spacing system, universal aesthetics, runtime design engine, autonomous UI AI, or mandatory visual truth.

**Purpose:** Formalize **why** an interface visually behaves the way it does. Frontend production must preserve **visual intent** — not only tokens, DOM, screenshots, or semantic labels.

**Companion models:** [UI Weight Distribution Model](ui-weight-distribution-model.md), [CTA Philosophy Governance](cta-philosophy-governance.md).  
**Related layers:** [strategic-intent-governance.md](strategic-intent-governance.md), [design-token-intelligence-governance.md](design-token-intelligence-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [compositional-structure-awareness.md](compositional-structure-awareness.md), [canonical-vertical-cadence-system.md](canonical-vertical-cadence-system.md), [responsive-intent-governance.md](responsive-intent-governance.md), [content-density-governance.md](content-density-governance.md), [interaction-intent-governance.md](interaction-intent-governance.md), [state-behavioral-consistency-governance.md](state-behavioral-consistency-governance.md), [accessibility-intent-governance.md](accessibility-intent-governance.md), [cross-project-transfer-governance.md](cross-project-transfer-governance.md).  
**Forge checklist:** [`../../agents/mars-forge/design-intent-checklist.md`](../../agents/mars-forge/design-intent-checklist.md).

---

## 1. Positioning

Design system intent governance sits above token usage and below human creative direction:

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Visual philosophy and intent interpretation | Exact token values as a source of truth |
| Surface, radius, border, shadow, CTA, density, and emphasis behavior | Automatic style linting or runtime enforcement |
| Website Factory preferred commercial production language | Universal taste or mandatory aesthetics for every brand |
| Human-supervised QA vocabulary for Forge | Autonomous redesign or adaptive UI generation |

The governance question is not “which radius/color/shadow value did we use?”  
The governance question is: **does this choice support the interface's intended commercial, operational, and narrative behavior?**

---

## 2. Core Principle

Frontend implementation must understand:

```text
VISUAL INTENT > raw token translation
```

Tokens, spacing, screenshots, and DOM structure are evidence. They are not sufficient by themselves. A build can match surface values and still feel wrong through random radius behavior, CTA overweight, fake depth, SaaS inheritance, equal-weight collapse, or uncontrolled emphasis.

---

## 3. Radius Philosophy

Radius is a visual-language decision, not decorative rounding.

| Radius behavior | Governance read |
|-----------------|-----------------|
| **Sharp UI** | Acceptable and often intentional for operational seriousness, industrial clarity, engineering confidence, or restrained commercial tone. |
| **Rounded UI** | Acceptable when it supports approachable service, card grouping, form friendliness, or brand softness. |
| **Mixed radius** | Requires role logic: panels, chips, forms, media, and CTAs may differ only when hierarchy explains the difference. |
| **Radius escalation** | Drift where each new component becomes rounder because local choices copy SaaS defaults instead of the project language. |

**Rules:**

- Do not introduce random `border-radius` values because a component “looks modern.”
- Do not let imported SaaS card/button radius override a project that reads sharper, industrial, or operational.
- Keep radius families reviewable: section shells, cards, buttons, inputs, badges, and media should have clear relationship.
- A stronger radius may mark a softer interaction layer; it must not silently soften the entire page language.

---

## 4. Surface Hierarchy

Surface hierarchy defines how planes, cards, bands, and panels distribute visual authority.

| Surface type | Intent |
|--------------|--------|
| **Flat surface** | Direct, operational, content-first; no fake depth. |
| **Elevated surface** | Draws attention to a contained object or conversion unit; use sparingly. |
| **Outlined surface** | Groups content while preserving restraint and flatness. |
| **Heavy surface** | Dominant block, hero, CTA panel, or high-stakes proof area; must have narrative reason. |
| **Layered hierarchy** | Multiple planes with clear order; not equal-card spam. |

Contrast can be intentional. A light island in a dark flow, or a dark proof band after a light explanation, is valid when it supports section role and cadence.

---

## 5. CTA Philosophy

CTA behavior is governed by [CTA Philosophy Governance](cta-philosophy-governance.md).

Core expectations:

- Primary CTA dominates only where conversion focus is intended.
- Secondary CTA supports, explains, or defers; it must not become a peer by accident.
- Outline CTA is a restraint pattern, not a decorative alternate primary.
- Repeated CTA blocks require pacing discipline; repetition must not create CTA fatigue.
- Website Factory prefers operational, commercially serious CTA tone over aggressive conversion pressure.

---

## 6. Border Logic

Borders should explain grouping, containment, or hierarchy.

Acceptable uses:

- separating cards in dense information zones;
- clarifying form fields or comparison tables;
- marking restrained panels without adding fake elevation;
- preserving hierarchy where shadow would overstate importance.

Forbidden drift:

- decorative dividers everywhere;
- borders plus shadows plus glow for the same object;
- equal borders on all objects until hierarchy collapses;
- dashboard-style grid lines leaking into marketing narrative sections.

---

## 7. Shadow Governance

Shadow is an emphasis tool with contamination risk.

Acceptable:

- subtle elevation for one conversion card, modal-like focus, or clear foreground object;
- low-intensity depth that supports grouping without making the page float;
- project-approved premium treatment when the brand source explicitly demands it.

Reject:

- shadow spam;
- floating SaaS UI;
- fake premium glow;
- depth applied because the component library default had it;
- shadow escalation where every next panel needs stronger elevation to compete.

Operational restraint is the default. If a flat or outlined surface communicates the same hierarchy, prefer restraint.

---

## 8. UI Weight Distribution

UI weight is governed by [UI Weight Distribution Model](ui-weight-distribution-model.md).

Implementation must read:

- where visual gravity should concentrate;
- which surface is dominant;
- where hierarchy pressure is too high;
- whether CTAs are overweight or underweight;
- whether hero treatment dominates the rest of the page;
- whether accidental emphasis appears through icons, borders, shadows, or oversized cards.

---

## 9. Density Intention

Density is not simply “more compact” or “more airy.” It is a commercial reading of how much the user can process at a given moment; detailed information-pressure rules live in [Content Density Governance](content-density-governance.md).

- Dense sections require stronger grouping, rhythm, and breathing before/after.
- Sparse sections require enough content authority to avoid empty premium theater.
- Dense proof, price, specs, or form areas must not inherit app-dashboard compression.
- Mobile density must preserve tap safety, readable hierarchy, and CTA pacing.

---

## 10. Visual Restraint

Restraint means every visual device has a job.

Use fewer competing accents. Avoid stacking radius, shadow, borders, glow, badges, icons, gradients, uppercase, and CTA color on the same object unless the source explicitly charters that intensity.

Visual restraint is not minimalism as universal truth. It is a Website Factory preference for production interfaces that feel deliberate, serious, and commercially legible.

---

## 11. Operational vs SaaS Visual Language

Website Factory commercial production may borrow from SaaS UI when appropriate, but SaaS inheritance is not default authority.

| Operational / commercial seriousness | SaaS contamination risk |
|--------------------------------------|--------------------------|
| clear surfaces, restrained depth, purposeful CTAs | floating cards, glassy glow, badge clutter |
| sharp or moderately rounded controls by role | pill-shaped everything |
| section emphasis tied to story | dashboard cards replacing narrative flow |
| proof and CTA paced for trust | aggressive conversion widgets everywhere |

---

## 12. Commercial Seriousness

Commercial seriousness means the interface respects:

- the offer's stakes;
- the user's decision fatigue;
- trust and proof sequencing;
- clear conversion paths without coercion;
- brand and industry expectations.

It does not mean boring, austere, or low-conversion. It means the page avoids gimmickry unless the approved brand/source intentionally uses it.

---

## 13. Visual Contamination

Visual contamination happens when unchartered visual language leaks into the current section:

- SaaS dashboard defaults;
- previous-section tokens;
- copied card systems;
- unapproved glow/shadow;
- random radius families;
- hero treatment reused in support sections;
- framework component defaults;
- archived design version mood.

If local visual role is unclear, record **SAFE UNKNOWN** rather than letting defaults decide.

---

## 14. Section Emphasis Discipline

Every section should know its role:

| Section role | Emphasis discipline |
|--------------|---------------------|
| **Hero** | May carry strongest gravity, but must not suffocate all later proof and CTA moments. |
| **Proof** | Supports trust; should not steal primary conversion focus unless source says so. |
| **Explanation** | Clarity before spectacle; avoid accidental hero styling. |
| **Dense comparison/specs** | Needs grouping and breathing; avoid dashboard collapse. |
| **CTA / lead** | Isolated enough to convert; not repeated until fatigue. |
| **Footer** | Closure, not a second hero unless explicitly chartered. |

---

## 15. Anti-Patterns

Forbidden drift vocabulary:

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Random border-radius** | Breaks visual language and makes hierarchy arbitrary. |
| **Shadow spam** | Creates fake depth and focal competition. |
| **Floating SaaS UI** | Imports app-dashboard language into marketing narrative. |
| **Fake premium glow** | Simulates value through effects instead of proof and hierarchy. |
| **Over-cardization** | Turns every message into an equal card; kills story flow. |
| **CTA screaming** | Uses size/color/repetition to pressure instead of guide. |
| **Giant hero dominance** | Hero absorbs all visual authority; later sections feel secondary or irrelevant. |
| **Accidental dashboard feel** | Grids, tiny spacing, panels, and controls read like software UI, not landing communication. |
| **Excessive elevation** | Every object competes for foreground. |
| **Visual noise escalation** | More badges, icons, lines, and accents are added to solve unclear hierarchy. |
| **Equal-weight collapse** | Everything has similar weight, so nothing leads. |

---

## 16. Forge / QA Expectations

When Forge is selected, design intent is reviewed before freeze:

- Run [`design-intent-checklist.md`](../../agents/mars-forge/design-intent-checklist.md) alongside visual reconciliation, composition awareness, cadence, and rhythm QA.
- Run design token QA when radius, surface, shadow, color, spacing, typography, responsive values, state values, semantic aliases, or local overrides affect design-system trust; record `DESIGN TOKEN FINDINGS` per [`design-token-checklist.md`](../../agents/mars-forge/design-token-checklist.md).
- Run responsive intent QA when mobile / tablet behavior changes CTA weight, surface hierarchy, visual flattening, or operational readability; record `RESPONSIVE INTENT FINDINGS` per [`responsive-intent-checklist.md`](../../agents/mars-forge/responsive-intent-checklist.md).
- Run content density QA when visual intent depends on information pressure, proof density, card load, trust-wall drift, scanning fatigue, or CTA dilution; record `CONTENT DENSITY FINDINGS` per [`content-density-checklist.md`](../../agents/mars-forge/content-density-checklist.md).
- Run interaction intent QA when visual choices imply hover authority, CTA behavior, motion restraint, dead zones, or behavioral contamination; record `INTERACTION INTENT FINDINGS` per [`interaction-intent-checklist.md`](../../agents/mars-forge/interaction-intent-checklist.md).
- Run state consistency QA when visual choices imply hover/focus/disabled/loading/validation/success/error states, CTA state hierarchy, or accessibility-state risk; record `STATE CONSISTENCY FINDINGS` per [`state-consistency-checklist.md`](../../agents/mars-forge/state-consistency-checklist.md).
- Run accessibility intent QA when visual choices affect contrast trust, focus visibility, semantic affordance, form clarity, CTA accessibility, or assistive predictability; record `ACCESSIBILITY FINDINGS` per [`accessibility-intent-checklist.md`](../../agents/mars-forge/accessibility-intent-checklist.md).
- Run strategic intent QA when visual choices affect conversion hierarchy, proof hierarchy, operational seriousness, stakeholder intent, or business trust; record `STRATEGIC INTENT FINDINGS` per [`strategic-intent-checklist.md`](../../agents/mars-forge/strategic-intent-checklist.md).
- Run cross-project transfer QA when radius, surface, card, CTA, proof, SaaS/operational tone, or visual-language patterns are borrowed from another project; record `CROSS-PROJECT TRANSFER FINDINGS` per [`cross-project-transfer-checklist.md`](../../agents/mars-forge/cross-project-transfer-checklist.md).
- Record **DESIGN INTENT FINDINGS** when visual intent, UI weight, CTA philosophy, surface hierarchy, or SaaS contamination is in scope.
- Treat findings as human-supervised governance, not automated scoring.
- Escalate to **SAFE UNKNOWN** when source authority does not resolve visual language.

---

## 17. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory lessons:

- A section can be semantically correct while the surface mood is wrong due to foundation contamination.
- CTA dominance can improve while composition or weight distribution remains partially blocked.
- Dense/light adjacency affects perceived seriousness and conversion pacing.
- Random radius, shadow, and card treatment would have weakened the operational/industrial tone.
- Hero, proof, specs, and CTA sections need distinct visual authority; equalizing them flattens the page.

These are Website Factory lessons, not Triumph-only aesthetics.

---

## 18. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| No approved visual source | Cannot infer radius, surfaces, CTA tone, or weight model from taste. |
| Conflicting implementation pack notes | Cannot decide surface/CTA/shadow authority without HITL. |
| Brand language unclear | Operational vs SaaS tone is not chartered. |
| Mobile visual intent missing | Exact CTA weight, density, and surface hierarchy may change at breakpoint. |
| Existing code contradicts active source | Need authority decision before inheriting code defaults. |
| Project intentionally wants SaaS aesthetics | This layer cannot override explicit approved brand direction. |

**Action:** document the resolver: annotated export, implementation-pack note, design system rule, or HITL decision.

---

## 19. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Design System Intent Governance layer — philosophy and visual-governance methodology only. |
| v0.1 | 2026-05-17 | Linked Responsive Intent Governance for viewport-specific CTA weight, surface hierarchy, and visual flattening checks. |
| v0.2 | 2026-05-17 | Linked Content Density Governance for information pressure, proof density, scanning rhythm, and CTA dilution checks. |
| v0.3 | 2026-05-17 | Linked Interaction Intent Governance for hover authority, CTA behavior consistency, and motion restraint checks. |
| v0.4 | 2026-05-17 | Linked State & Behavioral Consistency Governance for state integrity, CTA states, feedback restraint, and accessibility-state drift checks. |
| v0.5 | 2026-05-17 | Linked Accessibility Intent Governance for contrast trust, focus visibility, semantic affordance, form clarity, CTA accessibility, and `ACCESSIBILITY FINDINGS`. |
| v0.6 | 2026-05-17 | Linked Design Token Intelligence Governance for semantic token intent, override governance, token drift, and `DESIGN TOKEN FINDINGS`. |
| v0.7 | 2026-05-17 | Linked Cross-Project Knowledge Transfer Governance for visual-language portability, aesthetic transfer risk, and project-identity preservation. |
