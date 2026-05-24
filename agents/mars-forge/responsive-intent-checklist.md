# MARS Forge — Responsive Intent Checklist

**Status:** **overlay checklist** for human-supervised responsive intent QA.  
**Not:** automated responsive engine, screenshot diff, mobile redesign system, or substitute for foundation QA.

**Factory methodology:** [`../../projects/mars-website-factory/responsive-intent-governance.md`](../../projects/mars-website-factory/responsive-intent-governance.md).  
**Mobile composition:** [`../../projects/mars-website-factory/mobile-composition-preservation.md`](../../projects/mars-website-factory/mobile-composition-preservation.md).  
**Collapse taxonomy:** [`../../projects/mars-website-factory/responsive-collapse-taxonomy.md`](../../projects/mars-website-factory/responsive-collapse-taxonomy.md).

---

## 1. When to Run

Run this checklist:

- after responsive mechanics are implemented for the slice;
- after semantic QA, visual reconciliation, composition awareness, design intent, cadence, and rhythm reads when they are in scope;
- before section freeze or before declaring responsive closure.

This checklist extends Forge G1 / pre-freeze QA. It does not replace overflow, tap target, build, accessibility, or foundation checks.

---

## 2. Responsive Intent QA

- [ ] **Source anchored** — viewport behavior is anchored to mobile export, responsive rules, implementation pack, or documented HITL decision; otherwise **SAFE UNKNOWN**.
- [ ] **Hierarchy survival** — primary heading, support copy, proof, media, and CTA retain intended visual / semantic order.
- [ ] **Composition collapse checked** — dominant clusters remain perceptually grouped after stacking or reflow.
- [ ] **Stack integrity checked** — vertical stacks preserve grouping, emphasis, and breathing; they do not become equal-card lists.
- [ ] **Mobile cadence checked** — title/body gaps, item gaps, CTA isolation, dense-section resets, and section transitions remain readable.
- [ ] **CTA collapse checked** — primary / secondary / helper CTA hierarchy survives without mobile CTA screaming or burying.
- [ ] **Visual weight checked** — cards, surfaces, icons, badges, media, and CTAs do not flatten into equal emphasis.
- [ ] **Operational readability checked** — line length, tap zones, density, and scan path support real mobile use, not only compactness.
- [ ] **RU no word-splitting checked** — [ru-landing-qa-preset-v1.md](../../projects/mars-website-factory/ru-landing-qa-preset-v1.md) (mandatory for RU commercial); authority [russian-no-word-splitting-typography-v1.md](../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md). Generic responsive widths elsewhere are supplementary.
- [ ] **Responsive drift typed** — any failure uses [`responsive-collapse-taxonomy.md`](../../projects/mars-website-factory/responsive-collapse-taxonomy.md).

---

## 3. Mobile Hierarchy QA

- [ ] No responsive hierarchy inversion: secondary proof, image, rating, price, or helper CTA does not overpower the main claim.
- [ ] Dominant cluster appears early enough to orient the reader.
- [ ] Supporting details remain subordinate and grouped.
- [ ] Dense lists, specs, equipment cards, or trust blocks do not visually become the section’s accidental hero.
- [ ] Centering, full-width cards, and equal gaps do not erase the intended reading ladder.

---

## 4. Mobile Cadence QA

- [ ] Mobile spacing uses separate cadence logic rather than direct desktop compression.
- [ ] Dense sections receive breathing before/after.
- [ ] CTA moments have enough isolation without excessive pressure.
- [ ] Dark/light, sparse/dense, proof/CTA, and CTA/footer transitions remain paced.
- [ ] Long vertical sequences have readable resets to prevent mobile fatigue.

---

## 5. Collapse Taxonomy QA

Check for:

- [ ] Accordion collapse drift.
- [ ] Stack flattening.
- [ ] Hierarchy inversion.
- [ ] CTA overweight on mobile.
- [ ] Mobile dashboard effect.
- [ ] Endless-stack fatigue.
- [ ] Desktop-to-mobile contamination.
- [ ] Compressed trust drift.
- [ ] Over-centered mobile drift.
- [ ] Tap-zone suffocation.
- [ ] Mobile cadence collapse.

Record any match in **RESPONSIVE INTENT FINDINGS**.

---

## 6. Stack Integrity QA

- [ ] Related objects remain grouped more tightly than unrelated objects.
- [ ] Helper text stays near the CTA, price, form, or claim it qualifies.
- [ ] Proof stays connected to the claim it supports.
- [ ] Repeated card stacks have enough variation / grouping to avoid endless-feed behavior.
- [ ] The stack preserves section identity: hero, proof, explanation, dense specs, CTA, or footer.

---

## 7. Responsive Redesign Boundary

Stop and escalate when a responsive fix would:

- split or merge sections;
- remove semantic groups;
- invent a new mobile-only composition;
- replace dominant cluster relationships;
- change CTA semantics or pressure model;
- introduce a new mobile aesthetic not chartered by source;
- require DOM regrouping beyond approved scope.

Use **PARTIAL — responsive intent** or **SAFE UNKNOWN** rather than silent redesign.

---

## 8. REPORT Block

Use this block when responsive intent is in scope:

```text
RESPONSIVE INTENT FINDINGS — <section or block_id> — <viewport/source>

Observed vs source / rules:
- Hierarchy survival:
- Composition collapse:
- Mobile cadence:
- CTA hierarchy:
- Stack integrity:
- Visual weight:
- Operational readability:
- Drift taxonomy:

Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Action: tuned | deferred | structure escalation | HITL required | no action
Evidence: <paths, viewport widths, notes>
```

---

## 9. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- no mobile source or responsive rule exists;
- approved sources conflict across breakpoints;
- collapse behavior requires a structural decision;
- CTA mobile hierarchy is not chartered;
- dense-section compression threshold is unclear;
- the implementation can survive mobile but fidelity cannot be proven.

---

## 10. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Forge responsive intent checklist; adds `RESPONSIVE INTENT FINDINGS`. |
