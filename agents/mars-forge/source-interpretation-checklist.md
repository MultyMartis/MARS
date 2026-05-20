# Source interpretation checklist — MARS Forge (overlay v0)

**Status:** **overlay checklist** for human-supervised source interpretation QA.  
**Not:** automated source understanding, screenshot diff, computer vision, runtime interpretation AI, or substitute for foundation QA.

**Factory methodology:** [`../../projects/mars-website-factory/source-interpretation-governance.md`](../../projects/mars-website-factory/source-interpretation-governance.md).  
**Confidence model:** [`../../projects/mars-website-factory/source-confidence-model.md`](../../projects/mars-website-factory/source-confidence-model.md).  
**Ambiguity taxonomy:** [`../../projects/mars-website-factory/source-ambiguity-taxonomy.md`](../../projects/mars-website-factory/source-ambiguity-taxonomy.md).

---

## 1. When to Run

Run this checklist:

- before implementation choices depend on screenshot / pack / matrix interpretation;
- after semantic source lock charter confirms active source path and version;
- alongside visual reconciliation, composition awareness, responsive intent, and content density QA when source interpretation affects those reads;
- before declaring source reading complete, section PASS, or freeze.

This checklist does not authorize guessing, redesign, hidden responsive decisions, or invented UX.

---

## 2. Source Interpretation QA

- [ ] **Source anchor named** — active version, source path, source artifact, and slice / `block_id` are named.
- [ ] **Observed facts listed** — copy, visible hierarchy, CTA role, entities, assets, grouping, and states that are explicit.
- [ ] **Inferred intent separated** — strongly implied and weakly implied reads are not mixed with observed facts.
- [ ] **Assumptions disclosed** — any practical assumption is named, bounded, and reversible.
- [ ] **Unknowns surfaced** — missing source, unreadable source, absent states, or missing breakpoint authority recorded as **SAFE UNKNOWN**.
- [ ] **Contradictions checked** — active source, matrix, implementation pack, old docs, shared assets, and existing code do not silently conflict.
- [ ] **Visual extraction uncertainty checked** — raster artifacts, compression noise, export artifacts, accidental alignment, crop, or low resolution not treated as design law.
- [ ] **No hallucinated structure** — no invented wrappers, section splits, cards, catalogs, sliders, tabs, forms, or hidden states.
- [ ] **No screenshot overfitting** — visible detail is interpreted by confidence, not copied blindly.
- [ ] **Source confidence recorded** — explicit / strongly implied / weakly implied / ambiguous / unknown / contradictory.

---

## 3. Confidence Gate

Use [`source-confidence-model.md`](../../projects/mars-website-factory/source-confidence-model.md):

- [ ] **Explicit** decisions are implemented normally.
- [ ] **Strongly implied** decisions are implemented with confidence label when material.
- [ ] **Weakly implied** decisions are not reported as fact.
- [ ] **Ambiguous** decisions are escalated or marked PARTIAL / SAFE UNKNOWN.
- [ ] **Unknown** decisions stop implementation when material.
- [ ] **Contradictory** decisions stop material implementation unless charter priority resolves them.

Material fields include meaning, hierarchy, CTA, grouping, responsive behavior, interaction logic, asset authority, structural change, and freeze.

---

## 4. Ambiguity Taxonomy Gate

Check for and record patterns from [`source-ambiguity-taxonomy.md`](../../projects/mars-website-factory/source-ambiguity-taxonomy.md):

- [ ] Screenshot hallucination.
- [ ] Inferred semantics drift.
- [ ] Accidental redesign.
- [ ] Fake hierarchy extraction.
- [ ] Missing mobile assumptions.
- [ ] False grouping.
- [ ] Invisible-source guessing.
- [ ] Overconfident interpretation.
- [ ] Visual ambiguity collapse.
- [ ] Screenshot literalism.
- [ ] Asset hallucination.
- [ ] Invented interaction logic.
- [ ] Source contradiction masking.
- [ ] Undocumented intent inflation.
- [ ] Interpretation contamination.
- [ ] Hallucinated structure.

Any material match requires SOURCE INTERPRETATION FINDINGS.

---

## 5. Escalation Boundary

Stop and escalate when a source interpretation would:

- invent UX behavior, interaction state, or responsive pattern;
- create or remove semantic groups, sections, entities, CTAs, offers, pricing, or trust claims;
- infer mobile behavior from desktop-only screenshots without authority;
- resolve contradictory sources by taste;
- rely on unreadable or cropped source for material hierarchy;
- treat raster artifacts, compression noise, export artifacts, or accidental alignment as design law;
- claim full parity while source confidence is weak, ambiguous, unknown, or contradictory.

Use **SAFE UNKNOWN**, **PARTIAL — source interpretation**, or **HITL required** rather than silent guessing.

---

## 6. REPORT Block

Use this block when source interpretation affects implementation:

```text
SOURCE INTERPRETATION FINDINGS — <section or block_id> — <source ref>

Observed:
- <explicit source facts>

Inferred:
- <strongly implied / weakly implied reads + confidence>

Assumed:
- <assumptions, if any, with disclosure>

Unknown / contradictory:
- <SAFE UNKNOWN / HITL items>

Ambiguity taxonomy:
- <patterns found, if any>

Visual extraction uncertainty:
- <raster / compression / crop / hidden-state / missing-breakpoint concerns>

Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN | HITL REQUIRED | STOP
Action: proceed | approximate with disclosure | defer | request source | structure escalation
Evidence: <paths, source artifacts, notes>
```

---

## 7. Not Claimed

- No automated source reading.
- No CV or screenshot interpretation model.
- No universal design truth.
- No authority to redesign Triumph or any project.
- No runtime interpretation layer.
- No freeze when material ambiguity is hidden.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Forge source interpretation checklist; adds `SOURCE INTERPRETATION FINDINGS`. |
