# MARS Website Factory — UI Weight Distribution Model

**Status:** **documented** — human-supervised visual governance model.  
**Not:** automated visual scoring, heatmap prediction, pixel measurement, runtime balancing engine, or universal aesthetics.

**Purpose:** Give Forge and Website Factory operators vocabulary for **where visual weight should concentrate**, where it leaks, and when emphasis becomes accidental.

**Parent layer:** [Design System Intent Governance](design-system-intent-governance.md).  
**Related:** [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [canonical-vertical-cadence-system.md](canonical-vertical-cadence-system.md), [cta-philosophy-governance.md](cta-philosophy-governance.md).

---

## 1. Core Definition

**UI weight distribution** is the perceived allocation of visual gravity across a section or page: size, contrast, surface mass, typography weight, CTA strength, icon density, shadow, borders, whitespace, and placement.

The QA question is:

```text
Does visual gravity support the intended story, or has emphasis drifted?
```

---

## 2. Core Concepts

| Concept | Meaning |
|---------|---------|
| **Visual gravity** | What the eye treats as most important before reading deeply. |
| **Weight concentration** | Deliberate clustering of attention on one section, card, CTA, claim, or proof unit. |
| **Hierarchy pressure** | The total emphasis load inside a viewport; too much pressure causes competition. |
| **Dominant surface** | The plane or container that owns the main attention in a section. |
| **Visual overload** | Too many heavy elements compete at once. |
| **Accidental emphasis** | An element becomes dominant through size, color, shadow, border, or position without source intent. |
| **Emphasis flattening** | All elements receive similar weight, making the hierarchy unreadable. |
| **Weight leakage** | A secondary element borrows primary treatment from another role or section. |
| **CTA overweight** | CTA styling or repetition dominates beyond the section's conversion role. |
| **Hero domination drift** | Hero styling is so strong that later proof, offer, and CTA sections cannot regain authority. |

---

## 3. Weight Sources

Visual weight usually comes from combined signals:

| Signal | Common drift |
|--------|--------------|
| **Size** | Oversized icons, cards, trust logos, or secondary headlines. |
| **Contrast** | Small objects become dominant because color contrast is too strong. |
| **Typography weight** | Headings, labels, and numbers compete with primary narrative. |
| **Surface mass** | Heavy panels/cards dominate sections that should read flat or explanatory. |
| **Shadow/elevation** | Fake foreground competes with source hierarchy. |
| **Border density** | Many outlined objects create dashboard or table pressure. |
| **Whitespace isolation** | A secondary object feels primary because it has too much isolation. |
| **CTA treatment** | Button color, scale, repetition, or placement overtakes story flow. |

---

## 4. Distribution Patterns

| Pattern | Healthy when | Drift when |
|---------|--------------|------------|
| **Single focal weight** | Hero claim or primary CTA needs first attention. | One object suffocates all surrounding proof or explanation. |
| **Stepped hierarchy** | Headline → support → proof → CTA read in intended order. | Steps are too close or too far apart. |
| **Distributed proof weight** | Multiple trust items need comparable authority. | Proof becomes an equal-card grid with no narrative lead. |
| **Dense technical weight** | Specs/prices need scannable authority. | Section becomes a dashboard or wall of panels. |
| **CTA concentration** | Conversion moment needs focus. | CTA screams, repeats, or visually overwhelms trust. |
| **Quiet support weight** | Secondary content stays readable but subordinate. | Support content becomes invisible or accidentally dominant. |

---

## 5. Weight Concentration Rules

- One viewport should not contain multiple unrelated dominant surfaces unless the source explicitly charters focal competition.
- A CTA can be visually strong, but it must not erase trust, offer clarity, or page pacing.
- Dense grids need a lead element or clear grouping, not identical card weight by default.
- Hero weight should introduce the page, not make every later section feel like an afterthought.
- Supporting proof should reinforce the claim, not compete as a second hero.
- Heavy surface, strong border, shadow, accent color, and large type should not all stack on a secondary element.

---

## 6. Weight Leakage

Weight leakage appears when an element inherits emphasis from the wrong source:

- hero button treatment reused in footer helper links;
- global card shadow applied to every proof item;
- trust logo row scaled like primary CTA support;
- dashboard table borders leaking into landing proof sections;
- previous dark-band typography reused in a light explanatory screen;
- icon treatment from navigation reused in conversion cards.

Leakage should be reported as a design-intent issue, not hidden as local CSS taste.

---

## 7. CTA Weight

CTA weight must be evaluated through [CTA Philosophy Governance](cta-philosophy-governance.md).

Check:

- Does the primary CTA dominate only where dominance is intended?
- Does secondary CTA remain restrained?
- Does repeated CTA weight create fatigue?
- Does outline treatment quietly support or accidentally rival the primary?
- Does mobile stacking overweight the CTA by repeating it too close to itself?

---

## 8. Hero Domination Drift

Hero domination drift occurs when the hero consumes so much visual authority that:

- later proof feels decorative;
- dense specs or price logic cannot be read;
- downstream CTA moments feel redundant;
- page cadence becomes “hero plus leftovers”;
- every supporting section tries to recover attention through heavier cards, shadows, or CTA repetition.

Mitigation is not automatically “make hero smaller.” The fix may be weight redistribution: proof clarity, section cadence, surface restraint, or CTA pacing.

---

## 9. Equal-Weight Collapse

Equal-weight collapse happens when all objects are styled as peers:

- same card surface everywhere;
- same radius and shadow for all content;
- same button treatment for primary and secondary;
- same heading weight for narrative beats;
- same spacing for different section roles.

This often feels clean at first but weakens commercial direction: the user cannot tell what to read first, trust second, and do next.

---

## 10. Forge QA Prompts

Use these during pre-freeze design intent review:

- What is the dominant surface in this section?
- Which object has first visual gravity?
- Is that object supposed to win?
- Which elements are accidentally heavy?
- Which intended primary elements are underweight?
- Did global or previous-section styling leak weight into this section?
- Does CTA weight match conversion pacing?
- Does mobile stacking preserve hierarchy or flatten it?

---

## 11. REPORT Block

Use inside **DESIGN INTENT FINDINGS** or standalone when weight is the main concern:

```text
UI WEIGHT FINDINGS — <section or block_id> — <source ref>

Visual gravity: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Intended dominant surface:
- Actual dominant surface:
- Accidental emphasis:

Weight distribution: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Weight concentration:
- Hierarchy pressure:
- Emphasis flattening / overload:
- Weight leakage:

CTA / hero weight: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- CTA overweight / underweight:
- Hero domination drift:

Disposition:
- Freeze impact:
- Deferrals / resolver:
```

---

## 12. Anti-Patterns

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **CTA overweight** | Conversion object dominates without pacing or trust support. |
| **Hero domination drift** | Rest of page loses commercial authority. |
| **Equal-weight collapse** | Hierarchy disappears. |
| **Weight leakage** | Wrong visual role inherits primary treatment. |
| **Visual overload** | Too many heavy elements compete. |
| **Accidental dashboard feel** | Dense panels and borders make marketing content read as app UI. |
| **Shadow weight inflation** | Elevation becomes the main hierarchy tool. |
| **Proof overweight** | Logos/reviews steal focal path from claim or CTA. |

---

## 13. SAFE UNKNOWN

Record **SAFE UNKNOWN** when source authority does not identify:

- intended dominant surface;
- primary vs secondary CTA weight;
- hero/proof/CTA section priority;
- mobile weight behavior;
- whether equal cards are intentional;
- whether heavy surface or shadow is brand-approved.

**Action:** request annotated source, implementation-pack note, or HITL decision.

---

## 14. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial UI weight distribution model for design intent governance. |
