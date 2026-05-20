# MARS Forge — Content Density Checklist

**Status:** **overlay checklist** for human-supervised content density QA.  
**Not:** automatic readability engine, density scorer, SEO optimizer, copywriting system, or substitute for foundation QA.

**Factory methodology:** [`../../projects/mars-website-factory/content-density-governance.md`](../../projects/mars-website-factory/content-density-governance.md).  
**Information pressure model:** [`../../projects/mars-website-factory/information-pressure-model.md`](../../projects/mars-website-factory/information-pressure-model.md).  
**Overload taxonomy:** [`../../projects/mars-website-factory/content-overload-taxonomy.md`](../../projects/mars-website-factory/content-overload-taxonomy.md).

---

## 1. When to Run

Run this checklist:

- when a section contains dense copy, cards, grids, proof, trust, specs, pricing, FAQ, tables, reviews, badges, or multiple CTAs;
- after semantic QA confirms the content meaning and source authority;
- alongside visual reconciliation, composition awareness, design intent, cadence, rhythm, and responsive intent when density affects their reads;
- before section freeze or before declaring dense content acceptable.

This checklist does not authorize copy trimming, hiding, rewriting, section splitting, or responsive redesign without source authority or HITL.

---

## 2. Information Pressure QA

- [ ] **Source anchored** — density is anchored to approved copy, design source, SEO brief, implementation pack, proof inventory, or HITL decision; otherwise **SAFE UNKNOWN**.
- [ ] **Pressure level named** — section is classified as low / medium / high pressure or **SAFE UNKNOWN**.
- [ ] **Pressure role clear** — the density supports orientation, explanation, proof, comparison, decision, CTA, or closure.
- [ ] **Pressure sequence checked** — current section and neighbors create a readable pressure arc, not accidental dense-stack fatigue.
- [ ] **High-density intent justified** — high pressure is deliberate and controlled, not content stuffing.
- [ ] **Information breathing present** — dense sections include approach, grouping, recovery, or transition breathing.

---

## 3. Scanning Rhythm QA

- [ ] Primary claim, supporting copy, details, proof, and CTA are visibly distinct.
- [ ] Headings and subheads create a scan path before dense detail.
- [ ] Cards / rows / bullets do not all compete at equal weight.
- [ ] Paragraphs, microcopy, and caveats do not bury the main meaning.
- [ ] Dense grids have grouping, priority, or readable item rhythm.
- [ ] Mobile stack preserves scan rhythm and recovery beats.

---

## 4. Proof / Trust Density QA

- [ ] Proof appears near the claim it validates.
- [ ] Proof types are paced; reviews, logos, numbers, certificates, and badges are not spammed.
- [ ] Trust elements support credibility instead of becoming wallpaper.
- [ ] Proof volume does not overpower the section's primary role.
- [ ] Trust density does not degrade operational seriousness.
- [ ] Missing proof authority or conflicting proof inventory is recorded as **SAFE UNKNOWN**.

---

## 5. CTA Density QA

- [ ] Primary CTA remains visible and semantically clear.
- [ ] Supporting proof, price notes, helper text, and badges do not bury CTA.
- [ ] CTA is not amplified into pressure because surrounding density is unresolved.
- [ ] Secondary actions remain subordinate and do not multiply into CTA noise.
- [ ] Mobile CTA placement survives dense stacks without CTA dilution or CTA screaming.

---

## 6. Overload Taxonomy QA

Check for:

- [ ] Wall-of-text drift.
- [ ] Endless-card drift.
- [ ] SEO stuffing feel.
- [ ] Trust saturation.
- [ ] Proof spam.
- [ ] Feature-grid overload.
- [ ] Dense-table collapse.
- [ ] Visual scanning exhaustion.
- [ ] Card-noise escalation.
- [ ] Hierarchy flattening.
- [ ] Microcopy overload.
- [ ] CTA burial.
- [ ] Operational seriousness collapse.

Record any match in **CONTENT DENSITY FINDINGS** using the taxonomy name.

---

## 7. Responsive Density QA

- [ ] Desktop density was not copied directly into mobile without re-reading mobile pressure.
- [ ] Long card stacks include grouping or recovery where source allows.
- [ ] Dense proof/trust blocks do not become narrow-viewport wallpaper.
- [ ] Tables, specs, prices, and FAQ remain readable without collapse into noise.
- [ ] Missing mobile density authority is recorded as **SAFE UNKNOWN**.

---

## 8. Escalation Boundary

Stop and escalate when a density fix would:

- remove required copy, proof, trust, price, FAQ, or legal detail;
- rewrite SEO strategy or commercial claims;
- split or merge sections;
- hide content behind disclosure patterns not chartered by source;
- reduce proof inventory without authority;
- change CTA meaning, order, or pressure model;
- invent a different commercial style.

Use **PARTIAL — content density** or **SAFE UNKNOWN** rather than silent content redesign.

---

## 9. REPORT Block

Use this block when content density is in scope:

```text
CONTENT DENSITY FINDINGS — <section or block_id> — <source ref>

Pressure authority: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Source / copy authority:
- Pressure level: low | medium | high | SAFE UNKNOWN
- Density role:
- SAFE UNKNOWN resolver:

Scanning rhythm: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Hierarchy / scan path:
- Card / grid readability:
- Microcopy load:

Proof and trust density: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Proof pacing:
- Trust-wall drift:
- Proof saturation:

CTA survival: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- CTA visibility:
- CTA dilution by density:
- Mobile CTA density:

Overload taxonomy:
- Patterns:
- Operational seriousness risk:

Disposition:
- Freeze impact:
- Action: no action | tuned | deferred | HITL required | structure/content escalation
- Evidence:
```

---

## 10. Not Claimed

- No automatic content density scoring.
- No automatic readability engine.
- No universal copy length limits.
- No autonomous copy trimming or SEO rewriting.
- No mandatory sparse/minimal commercial style.

Defer to Website Factory content density governance, source authority, project implementation packs, HITL decisions, and foundation QA where scoped.

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Forge content density checklist; adds `CONTENT DENSITY FINDINGS`. |
