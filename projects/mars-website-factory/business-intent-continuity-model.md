# MARS Website Factory - Business Intent Continuity Model

**Status:** **documented** - Website Factory model for preserving business intent across human-supervised frontend production.  
**Not:** runtime business ontology, conversion optimizer, stakeholder replacement, automatic approval system, or universal marketing framework.

**Purpose:** define the continuity layers that protect strategic source intent from dilution as it moves through source interpretation, design, frontend implementation, QA, escalation, and reporting.

**Parent governance:** [strategic-intent-governance.md](strategic-intent-governance.md).  
**Drift taxonomy:** [strategic-drift-taxonomy.md](strategic-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/strategic-intent-checklist.md`](../../agents/mars-forge/strategic-intent-checklist.md).

---

## 1. Model Overview

Business intent continuity is the readable chain between:

```text
strategic source intent
-> business-priority layer
-> conversion hierarchy layer
-> proof / credibility layer
-> operational trust layer
-> implementation continuity layer
-> escalation / approval layer
```

The model exists because implementation can preserve local semantics while losing the strategic business path. A frontend that is polished, responsive, accessible, and QA-reviewed can still erode conversion, proof authority, operational seriousness, or stakeholder intent.

---

## 2. Continuity Layers

| Layer | Preserves | Failure signal |
|-------|-----------|----------------|
| **Strategic source intent** | The approved business objective, audience, offer, and desired decision path. | Strategy inferred from taste, template, prior output, or generic marketing assumptions. |
| **Business-priority layer** | Which claims, services, audiences, objections, and outcomes matter most. | Equal-weight message treatment or priority inversion. |
| **Conversion hierarchy layer** | Primary CTA, secondary CTA, deferral path, and CTA tone. | CTA spam, CTA dilution, secondary action overpowering primary action. |
| **Proof / credibility layer** | Authority order among proof types and where proof supports decision. | Proof flattening, proof saturation, fake authority, trust wallpaper. |
| **Operational trust layer** | Seriousness, restraint, confidence, and proportionate commercial tone. | Engagement-over-trust, fake premium styling, decorative seriousness. |
| **Implementation continuity layer** | Translation of business meaning into DOM, copy placement, visual hierarchy, interaction, responsive behavior, and QA scope. | Local UI optimization changes strategic meaning. |
| **Escalation / approval layer** | Stakeholder authority remains visible when intent is ambiguous, contradictory, or materially changed. | Agent or template silently overwrites stakeholder intent. |

---

## 3. Strategic Source Intent

Strategic source intent is the strongest available statement of why the page exists and what business outcome it supports.

Acceptable sources may include:

- approved brief;
- stakeholder notes;
- page objective model;
- conversion intent artifact;
- design implementation pack notes;
- approved copy deck;
- approved HITL decision;
- project-specific strategic constraints.

Source intent must not be invented from:

- visual taste;
- generic landing page convention;
- prior implementation artifacts without lineage;
- "more engagement" assumptions;
- component library defaults;
- agent preference.

If strategic source intent is missing, record **SAFE UNKNOWN** and avoid converting assumptions into implementation authority.

---

## 4. Business-Priority Layer

Business priority defines what must lead, what must support, and what must stay subordinate.

Review questions:

- Which audience or stakeholder priority is primary?
- Which offer or service is the main business object?
- Which objection or trust gap must be answered before action?
- Which detail is operationally necessary but strategically secondary?
- Which content must not be visually promoted above the main promise?

Business-priority continuity fails when local layout choices make all messages equal, promote secondary inventory above the primary offer, or hide the decisive business claim behind cards, proof, badges, or visual effects.

---

## 5. Conversion Hierarchy Layer

Conversion hierarchy is the ordered path from claim to action.

| Conversion element | Continuity rule |
|--------------------|-----------------|
| **Primary CTA** | Preserve role, weight, tone, position, and relationship to proof. |
| **Secondary CTA** | Support the primary path without visual or behavioral takeover. |
| **Repeated CTA** | Repeat only when it preserves pacing and does not create pressure fatigue. |
| **Sticky / persistent CTA** | Requires source authority or HITL because it changes conversion pressure. |
| **CTA microcopy** | Clarifies action and trust, not decorative urgency. |
| **Conversion proof** | Stays close enough to decision moments to earn action. |

Conversion continuity is not maximum CTA visibility. It is the preservation of the approved decision path.

---

## 6. Proof / Credibility Layer

Proof hierarchy identifies which evidence earns trust and how it should be weighted.

Proof may include:

- cases and project outcomes;
- reviews and testimonials;
- certificates, warranties, licenses, or guarantees;
- metrics and operational capacity;
- process transparency;
- equipment, team, location, or material evidence;
- before/after evidence;
- risk reducers and objections answered.

Proof continuity fails when evidence is over-cardized, over-decorated, saturated, visually equalized, moved away from decision moments, or replaced by fake premium styling.

**Rule:** proof should preserve authority. More proof is not automatically more trust.

---

## 7. Operational Trust Layer

Operational trust is the user's belief that the business is real, competent, serious, and appropriate for the stakes of the decision.

It is preserved through:

- restrained visual language;
- clear proof placement;
- credible CTA behavior;
- non-manipulative conversion pressure;
- accessible and predictable UI;
- evidence-based QA reporting;
- honest unknowns and escalation.

Operational seriousness can be harmed by both under-designed and over-designed UI. Fake premium styling, noisy animation, CTA spam, and proof wallpaper can damage trust even when they look expensive.

---

## 8. Implementation Continuity Layer

Implementation continuity asks whether business intent survived translation into frontend artifacts.

Review:

- DOM order and section order preserve strategic hierarchy.
- Copy placement preserves business priority.
- Visual hierarchy supports conversion hierarchy and proof hierarchy.
- Responsive collapse does not invert priority or bury proof/CTA.
- Interactions do not increase pressure or lower seriousness without authority.
- Accessibility and QA claims do not hide strategic unknowns.
- Local improvements do not rewrite stakeholder intent.

Implementation continuity is human-supervised. It is not a claim that code can understand strategy automatically.

---

## 9. Escalation / Approval Layer

Strategic escalation is required when:

- business priorities conflict across sources;
- CTA role is unclear or materially changed;
- proof authority is ambiguous;
- local optimization changes conversion pressure;
- operational seriousness is disputed;
- stakeholder intent is not visible;
- an implementation would promote, demote, remove, rewrite, or reframe a strategic element.

Approval should identify:

- what changed;
- who or what authority approved it;
- which source it supersedes or clarifies;
- whether QA and reporting need updated scope;
- whether future work should inherit the decision.

No missing approval should be filled by agent confidence.

---

## 10. Continuity Traceability

Strategic continuity should remain readable across sessions.

Minimal trace fields:

| Field | Purpose |
|-------|---------|
| **Strategic source** | Names the artifact or decision that defines intent. |
| **Stakeholder authority** | Names who or what has approval authority when known. |
| **Business priority** | States what leads and what supports. |
| **CTA role** | Identifies action type and priority. |
| **Proof role** | Identifies decisive vs supporting proof. |
| **Implementation translation** | Notes how the intent appears in structure, visual hierarchy, behavior, and responsive handling. |
| **Drift / unknowns** | Records strategic risks, SAFE UNKNOWN, HITL, or deferrals. |

Traceability does not require a runtime registry. It requires readable documentation and honest reporting.

---

## 11. Local Optimization Boundaries

Local optimization is allowed when it:

- clarifies the approved strategy;
- improves readability without changing priority;
- strengthens proof readability without saturating trust;
- improves CTA clarity without adding pressure;
- preserves operational seriousness;
- improves responsive behavior without priority inversion.

Local optimization is unsafe when it:

- makes a secondary action feel primary;
- makes proof louder but less credible;
- increases engagement at the cost of trust;
- overwrites stakeholder-specific messaging;
- changes strategic hierarchy to satisfy local visual symmetry;
- replaces real proof with decorative seriousness.

When uncertain, record **STRATEGIC INTENT FINDINGS** and escalate.

---

## 12. Strategic Drift Handling

Strategic drift should be handled by severity:

| Severity | Meaning | Response |
|----------|---------|----------|
| **Observation** | Possible strategic weakness but no confirmed damage. | Record finding and scope. |
| **Partial** | Strategy mostly preserved but one layer weakened or unverified. | Record partial, identify resolver, avoid broad PASS. |
| **Fail** | Business priority, CTA role, proof hierarchy, or trust is materially damaged. | Fix or request HITL before freeze. |
| **Blocked** | Source contradiction or missing authority prevents safe decision. | Stop or HITL required. |

Strategic drift should not be hidden inside visual, density, interaction, or QA findings. It may be related to those layers, but the business effect must be named.

---

## 13. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| No strategic source is available | Business intent cannot be established. |
| Stakeholder authority is absent | Cannot know whose priority governs. |
| CTA role is not explicit | Cannot safely tune action hierarchy. |
| Proof ranking is unclear | Cannot decide which evidence must lead. |
| Operational tone conflicts across sources | Cannot decide seriousness level by taste. |
| Local optimization changes priority | Requires authority decision before confidence. |
| Existing implementation is the only strategy evidence | Cannot prove it is intentional rather than drift. |

**Action:** state the missing layer, what artifact or decision would resolve it, and whether continuation is safe with disclosure, HITL recommended, HITL required, or stopped.

---

## 14. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Business Intent Continuity Model - strategic source intent, business priority, conversion hierarchy, proof/credibility, operational trust, implementation continuity, and escalation layers; documentation only. |
