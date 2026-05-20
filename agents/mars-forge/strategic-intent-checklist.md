# Strategic Intent Checklist - MARS Forge

**Status:** **documented** - Forge overlay checklist for human-supervised strategic intent QA.  
**Not:** autonomous business AI, conversion optimizer, marketing engine, automatic strategy reader, or runtime enforcement.

**Parent governance:** [`../../projects/mars-website-factory/strategic-intent-governance.md`](../../projects/mars-website-factory/strategic-intent-governance.md).  
**Continuity model:** [`../../projects/mars-website-factory/business-intent-continuity-model.md`](../../projects/mars-website-factory/business-intent-continuity-model.md).  
**Drift taxonomy:** [`../../projects/mars-website-factory/strategic-drift-taxonomy.md`](../../projects/mars-website-factory/strategic-drift-taxonomy.md).

---

## 1. When To Run

Run this checklist before freeze when any of the following affect the section, page, or delivery scope:

- business priority;
- strategic messaging;
- conversion hierarchy;
- CTA role, placement, repetition, behavior, or tone;
- proof hierarchy or credibility placement;
- operational trust / seriousness;
- stakeholder intent or approval authority;
- local UI optimization that may change global intent;
- source ambiguity around business meaning;
- QA report claims about business continuity.

Record results as **STRATEGIC INTENT FINDINGS**.

---

## 2. Strategic Source

- [ ] Strategic source intent is named, or **SAFE UNKNOWN** is recorded.
- [ ] Stakeholder authority is visible where known.
- [ ] Business objective is not inferred from generic landing-page convention.
- [ ] Existing implementation is not treated as strategy authority without lineage.
- [ ] Prior agent outputs, summaries, screenshots, and old versions do not overwrite active source intent.
- [ ] Any contradiction between source, design, copy, implementation, and HITL is escalated.

---

## 3. Business Priority

- [ ] Primary business promise remains visible and dominant enough for the section/page role.
- [ ] Secondary details support rather than overtake the main promise.
- [ ] Stakeholder-specific language is not rewritten into generic marketing language.
- [ ] Section order and visual hierarchy preserve approved priority.
- [ ] Responsive collapse does not invert business priority.
- [ ] Local layout symmetry does not flatten strategic hierarchy.

---

## 4. Conversion Hierarchy

- [ ] Primary CTA role is clear: commit, request, qualify, learn, compare, contact, or defer.
- [ ] Primary CTA remains visibly and behaviorally primary where conversion focus is intended.
- [ ] Secondary CTA supports the primary path without competing as a peer.
- [ ] CTA repetition is paced and does not become CTA spam.
- [ ] CTA motion, hover, sticky behavior, and emphasis do not create engagement-over-trust pressure.
- [ ] Dense content, proof, badges, or microcopy do not bury CTA intent.
- [ ] Mobile CTA order and emphasis preserve conversion continuity.

---

## 5. Proof Hierarchy

- [ ] Strongest proof remains identifiable and appropriately placed.
- [ ] Supporting proof does not flatten decisive proof into equal-card noise.
- [ ] Proof near conversion moments reduces uncertainty instead of becoming wallpaper.
- [ ] Badges, certificates, reviews, metrics, and operational details preserve authority order.
- [ ] Proof volume does not create saturation, fake authority, or trust fatigue.
- [ ] Decorative trust cues do not replace real proof.
- [ ] Missing proof authority is recorded as **SAFE UNKNOWN**.

---

## 6. Operational Trust

- [ ] Visual language preserves appropriate operational seriousness.
- [ ] Styling does not simulate seriousness through fake premium effects.
- [ ] Interaction and motion remain credible, restrained, and source-authorized.
- [ ] Accessibility, state behavior, and QA evidence support trust instead of theater.
- [ ] Responsive behavior keeps the interface calm and decision-readable.
- [ ] Engagement devices do not lower credibility.

---

## 7. Local Optimization Boundary

- [ ] Any local "polish" is checked against global business intent.
- [ ] Card, spacing, animation, proof, CTA, or copy changes do not alter business priority.
- [ ] Aesthetic-first redesign is not introduced under implementation scope.
- [ ] Local improvements that change strategy are escalated to HITL.
- [ ] Agent preference, template default, or component-library behavior does not replace stakeholder intent.

---

## 8. Strategic Drift Classification

Classify any issue using [`strategic-drift-taxonomy.md`](../../projects/mars-website-factory/strategic-drift-taxonomy.md):

- [ ] Conversion-goal erosion
- [ ] CTA dilution
- [ ] Proof flattening
- [ ] Aesthetic-first contamination
- [ ] Operational seriousness collapse
- [ ] Stakeholder-intent overwrite
- [ ] Engagement-maximization drift
- [ ] Local optimization destruction
- [ ] Strategic hierarchy inversion
- [ ] Business-message fragmentation
- [ ] Trust erosion through styling
- [ ] Proof saturation
- [ ] Decorative conversion inflation

---

## 9. Reporting Block

Use this block in Forge reports when strategic intent is in scope:

```text
STRATEGIC INTENT FINDINGS - <section or scope>

Strategic source: <artifact / HITL / SAFE UNKNOWN>
Business priority: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Conversion hierarchy: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Proof hierarchy: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Operational trust: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Stakeholder intent: PASS | PARTIAL | FAIL | SAFE UNKNOWN

Drift pattern(s): <taxonomy names or none>
Disposition: PASS | PARTIAL | FAIL | HITL REQUIRED | STOP
Evidence / unknowns: <short scope>
```

Keep this separate from `DESIGN INTENT FINDINGS`, `CONTENT DENSITY FINDINGS`, `INTERACTION INTENT FINDINGS`, `QA CONFIDENCE FINDINGS`, and `SOURCE LINEAGE FINDINGS`.

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- strategic source intent is missing;
- stakeholder authority is unclear;
- CTA role is ambiguous;
- proof authority cannot be ranked;
- operational seriousness is not chartered;
- business-semantic signals conflict;
- local optimization would decide strategy;
- source lineage for business intent is weak or unknown.

**Action:** state what is unknown, what would resolve it, and whether continuation is safe with disclosure, HITL recommended, HITL required, or stopped.

---

## 11. Non-Goals

- Do not redesign Triumph or any other project.
- Do not invent autonomous business AI.
- Do not create conversion-optimization engines.
- Do not define universal marketing truth.
- Do not claim automatic strategic understanding.
- Do not use "looks premium," "feels modern," or "more engagement" as strategic proof.

---

*Documentation only - no runtime enforcement.*
