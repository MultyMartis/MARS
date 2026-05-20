# MARS Website Factory - Full-Page Cadence Continuity Governance

**Status:** **documented** - Website Factory full-page rhythm and transition methodology only.  
**Not:** spacing engine, automatic layout evaluator, pixel rulebook, screenshot diff, or autonomous redesign system.

**Core principle:** vertical rhythm is system-owned. Individual sections may express local structure, but the page-level cadence owns how sections hand attention to each other.

**Related layers:** [canonical-vertical-cadence-system.md](canonical-vertical-cadence-system.md), [vertical-rhythm-governance.md](vertical-rhythm-governance.md), [cadence-tier-model.md](cadence-tier-model.md), [commercial-landing-pressure-model.md](commercial-landing-pressure-model.md), [atmosphere-continuity-governance.md](atmosphere-continuity-governance.md), [section-language-governance.md](section-language-governance.md).  
**Forge findings categories:** `RHYTHM FINDINGS`, `CADENCE FINDINGS`, `TRANSITION CONTINUITY FINDINGS`.

---

## 1. Purpose

This layer captures V4 lessons where each section may look locally acceptable while the landing reads as a stack of isolated blocks.

It governs:

- vertical rhythm system ownership;
- section transition rhythm;
- background-transition spacing logic;
- same-background collapse logic;
- full-page cadence continuity;
- section pressure continuity;
- commercial pacing continuity;
- commercial continuity spacing;
- no-isolated-block governance.

---

## 2. System-Owned Rhythm Rules

| Rule | Governance meaning |
|------|--------------------|
| **Vertical rhythms are system-owned** | Section-local padding must serve the page cadence, not only the local component. |
| **Rhythm values stay globally consistent** | Similar boundary roles should use the same scale or named tier. |
| **Exceptions are intentional and documented** | A local deviation needs source evidence, role change, or HITL decision. |
| **Same-background transition usually uses only bottom rhythm** | When two adjacent sections share one surface/environment, avoid duplicated top + bottom spacing that creates a double-gap. |
| **Different-background transition may use upper + lower rhythm** | A contrast, density, or mood change can need entry and exit breathing on both sides. |
| **Commercial continuity spacing matters** | The gap should preserve conversion momentum, not merely prevent overlap. |

These are human-supervised rules. They do not define universal pixel values.

---

## 3. Transition Logic

### Same Background

When adjacent sections share the same background, surface, or environmental field:

- treat the boundary as a continuity seam inside one larger visual chapter;
- usually keep only the prior section's bottom rhythm or the next section's top rhythm, not both;
- avoid same-background spacing duplication;
- check whether the sections should collapse into one visual run without losing semantic separation.

### Different Background

When adjacent sections change background, contrast, density, or atmosphere:

- upper + lower rhythm is allowed;
- the boundary may need a reset beat;
- dark/light transitions should not collide;
- contrast change and density change should be reviewed together.

---

## 4. Commercial Continuity

Commercial landing rhythm is not only visual spacing. It controls the buyer's narrative pressure:

- proof should arrive near skepticism;
- CTA sections should not feel detached from the preceding proof;
- pricing grids should not be isolated catalog islands;
- white sections should not lose energy after a dark hero;
- repeated section starts should not reset the pitch from zero.

Use `LANDING PRESSURE FINDINGS` when conversion momentum is affected and `TRANSITION CONTINUITY FINDINGS` when the boundary itself causes the momentum loss.

---

## 5. Drift Lessons Captured

| Drift | Governance lesson |
|-------|-------------------|
| **Isolated-block feeling** | Sections can be individually coherent but page-level continuity can still fail. |
| **White-section energy collapse** | Light sections after dark industrial starts need commercial energy, density, and transition rhythm. |
| **Vertical rhythm inconsistency** | Random section paddings undermine authored cadence. |
| **Same-background spacing duplication** | Adjacent same-surface sections can acquire double-gaps from both section paddings. |
| **Section-stack feeling** | A landing should not read as screenshots pasted vertically. |
| **Loss of commercial narrative continuity** | CTA, proof, pricing, trust, FAQ, and footer must form one conversion arc. |

Required V4 lesson labels captured: `isolated-block feeling`, `white-section energy collapse`, `vertical rhythm inconsistency`, `same-background spacing duplication`, `section-stack feeling`, `loss of commercial narrative continuity`.

---

## 6. Forge Use

Record:

- `RHYTHM FINDINGS` for local vertical rhythm, heading/body/CTA spacing, and rhythm scale violations.
- `CADENCE FINDINGS` for page-level narrative pacing and density transitions.
- `TRANSITION CONTINUITY FINDINGS` for same-background double-gaps, dark/light boundary issues, commercial bridge failure, and isolated-block risk.

Do not create a separate checklist for every transition. Use the consolidated Forge QA layer and cadence/rhythm checklists.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Adjacent source screens are missing | Cannot prove transition rhythm. |
| Background ownership is unclear | Cannot tell whether same-background collapse applies. |
| Mobile source is absent | Exact mobile cadence cannot be asserted beyond survivability. |
| Existing implementation already contains spacing residue | Cannot tell active rhythm from stale patching. |
| Commercial sequence is incomplete | Cannot judge full momentum continuity. |

**Action:** document the boundary, source screens, chosen rhythm tier, exception reason, and unresolved authority before freeze.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-18 | Initial full-page cadence continuity governance from Triumph V4 lessons. |
