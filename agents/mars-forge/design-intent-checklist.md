# Design intent checklist — MARS Forge

**Status:** Forge overlay checklist for **human-supervised** design intent QA.  
**Not:** automated visual scoring, style linting, runtime enforcement, autonomous redesign, or universal aesthetics.

**Website Factory layers:**

- [Design System Intent Governance](../../projects/mars-website-factory/design-system-intent-governance.md)
- [UI Weight Distribution Model](../../projects/mars-website-factory/ui-weight-distribution-model.md)
- [CTA Philosophy Governance](../../projects/mars-website-factory/cta-philosophy-governance.md)

Use this checklist during Forge QA / pre-freeze when radius, surface hierarchy, CTA weight, shadow, visual density, SaaS contamination, or emphasis discipline are in scope.

---

## 1. Authority and Scope

- [ ] Active design version and source screen are identified.
- [ ] Project design system / implementation pack is identified or marked **SAFE UNKNOWN**.
- [ ] Local screen visual intent is read before global defaults are applied.
- [ ] No archived mockup, previous section, framework default, or SaaS component library overrides the active source.
- [ ] Any intentional deviation from source is HITL-approved or recorded as **SAFE UNKNOWN**.

---

## 2. Radius Philosophy

- [ ] Radius family is consistent by role: section shells, cards, buttons, inputs, badges, media.
- [ ] Sharp UI is preserved when operational seriousness or source intent requires it.
- [ ] Rounded UI is used only where it supports source/brand role.
- [ ] No random border-radius values introduced.
- [ ] No radius escalation from copied SaaS defaults.

---

## 3. Surface Hierarchy

- [ ] Dominant surface is identified and matches source intent.
- [ ] Flat, outlined, elevated, and heavy surfaces have clear roles.
- [ ] Contrast shifts are intentional, not accidental foundation contamination.
- [ ] Cards/panels do not equalize the section unless equal weight is chartered.
- [ ] Surface hierarchy survives mobile stacking.

---

## 4. CTA Philosophy

- [ ] Primary CTA dominance matches section role.
- [ ] Secondary CTA remains restrained.
- [ ] Outline CTA behavior is intentional and not a disguised primary.
- [ ] CTA repetition follows conversion pacing, not pressure.
- [ ] CTA fatigue risk checked across current section and neighbors.
- [ ] Operational CTA tone used; no fake urgency or aggressive conversion drift.

---

## 5. Border and Shadow Governance

- [ ] Borders clarify grouping, containment, form fields, or comparison structure.
- [ ] Borders are not decorative noise.
- [ ] Shadows are used only where elevation has a visual-intent role.
- [ ] No shadow spam, fake premium glow, or floating SaaS UI.
- [ ] Border + shadow + glow are not stacked on secondary objects without source authority.

---

## 6. UI Weight Distribution

- [ ] First visual gravity matches intended dominant object.
- [ ] Hierarchy pressure is readable; not too many heavy elements in one viewport.
- [ ] Accidental emphasis from icons, badges, borders, shadows, or oversized cards is flagged.
- [ ] No equal-weight collapse unless source explicitly wants equal peers.
- [ ] No weight leakage from hero, previous sections, global CTA treatment, or dashboard components.
- [ ] Hero domination drift checked against downstream proof/CTA authority.

---

## 7. Density and Visual Restraint

- [ ] Dense areas are grouped and paced; not compressed into app-dashboard density.
- [ ] Sparse areas have narrative reason; not empty premium theater.
- [ ] Visual devices are not stacked to compensate for unclear hierarchy.
- [ ] Icons, badges, borders, shadows, uppercase, and CTA color do not escalate visual noise.
- [ ] Mobile density preserves hierarchy, tap safety, and CTA pacing.

---

## 8. Operational vs SaaS Contamination

- [ ] No unapproved floating cards, glassy glow, dashboard grids, or pill-everything language.
- [ ] Operational/commercial seriousness is preserved where project source implies it.
- [ ] SaaS visual language is used only when the active source or brand direction charters it.
- [ ] Previous-section visual language does not leak into current screen-local role.
- [ ] Foundation contamination bias is considered when global theme conflicts with local source.

---

## 9. Section Emphasis Discipline

- [ ] Hero, proof, explanation, dense comparison/specs, CTA, and footer roles are visually distinct.
- [ ] Supporting sections do not accidentally become heroes.
- [ ] Proof does not steal focal path unless source says so.
- [ ] CTA panels are isolated enough to convert but not so heavy they pressure.
- [ ] Footer reads as closure unless explicitly chartered as a final conversion hero.

---

## 10. REPORT Block

Use this block in Forge REPORT when design intent QA is in scope:

```text
DESIGN INTENT FINDINGS — <section or block_id> — <source ref>

Design intent authority: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Active source:
- Project design system / pack:
- SAFE UNKNOWN resolver:

Radius / surfaces: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Radius philosophy:
- Dominant surface:
- Surface hierarchy:
- Border / shadow logic:

CTA philosophy: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Primary dominance:
- Secondary restraint:
- Repetition / fatigue:
- Operational tone:

UI weight: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Visual gravity:
- Weight concentration:
- Accidental emphasis:
- Equal-weight / overload risk:

Contamination / restraint: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- SaaS contamination:
- Shadow/glow drift:
- Visual noise escalation:
- Section emphasis discipline:

Disposition:
- Freeze impact:
- Deferrals / resolver:
```

---

## 11. Not Claimed

- No automatic design-intent detection.
- No pixel-perfect or visual scoring claim.
- No mandatory aesthetic outside approved project direction.
- No autonomous UI redesign.
- No runtime engine or enforcement system.

Defer to Website Factory governance layers, project implementation packs, visual reconciliation, composition awareness, cadence/rhythm checklists, and foundation QA where scoped.
