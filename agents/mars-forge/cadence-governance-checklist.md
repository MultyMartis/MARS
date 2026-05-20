# Cadence governance checklist — MARS Forge

**Status:** Forge overlay checklist for **human-supervised** vertical cadence QA.  
**Not:** automated spacing linting, runtime cadence engine, screenshot diff, autonomous visual balancing, or universal spacing truth.

**Website Factory canon:**

- [Canonical Vertical Cadence System](../../projects/mars-website-factory/canonical-vertical-cadence-system.md)
- [Cadence Tier Model](../../projects/mars-website-factory/cadence-tier-model.md)
- [Vertical Rhythm Governance](../../projects/mars-website-factory/vertical-rhythm-governance.md)

Use this checklist during Forge QA / pre-freeze when inter-screen spacing, section adjacency, dense stacks, CTA isolation, dark/light transitions, mobile cadence, or footer closure are in scope.

---

## 1. Cadence Authority

- [ ] Active design version and source screens are identified.
- [ ] Current section and immediate neighbors are known in section order.
- [ ] Project cadence tier mapping exists or exact tier assignment is recorded as **SAFE UNKNOWN**.
- [ ] Cadence is read from approved source / implementation pack / HITL decision, not from inherited DOM spacing.
- [ ] No archived mockup, old PDF, or prior implementation overrides the active cadence source.

---

## 2. Cadence Continuity Checks

- [ ] Inter-screen spacing reads as **narrative pacing**, not random margin/padding.
- [ ] Section boundaries preserve a clear page-level pacing arc.
- [ ] Similar section roles use comparable cadence unless the source intentionally changes role.
- [ ] Different section roles are not flattened into identical cadence everywhere.
- [ ] Previously frozen neighbors did not shift through global spacing changes.
- [ ] Same-background transitions avoid accidental double-gaps; usually only one side owns boundary rhythm.
- [ ] Different-background transitions use documented reset rhythm when upper + lower breathing is needed.
- [ ] Page does not read as isolated blocks or a section stack.

---

## 3. Transition Pacing Checks

- [ ] Dark → light and light → dark transitions include a deliberate cadence reset when contrast change requires it.
- [ ] Sparse → dense transitions provide a readable approach before content pressure increases.
- [ ] Dense → sparse transitions provide breathing without becoming giant whitespace deserts.
- [ ] Proof → CTA transitions preserve CTA isolation and dominance.
- [ ] CTA → footer transition provides closure cadence.
- [ ] Transition compression is named when the boundary feels too tight for the mood, density, or CTA shift.

---

## 4. Density Stack Checks

- [ ] Dense grid sections have breathing before and after.
- [ ] Multiple adjacent dense/light sections are reviewed as a sequence, not only as isolated sections.
- [ ] Zero-breathing dense stacks are flagged.
- [ ] Visual exhaustion risk is recorded when density accumulates across the page.
- [ ] Density bridge is present when the page moves between dense and light content.

**Canonical reference sequence:** Triumph V2 `03 → 04 → 05` is the named Website Factory lesson for middle-page cadence collapse risk: semantically correct sections can still create compressed middle cadence, section collision, or density-stack fatigue.

---

## 5. Tier Model Checks

- [ ] Boundary tier is identified as `XS`, `S`, `M`, `L`, `XL`, or **SAFE UNKNOWN**.
- [ ] Tier assignment explains cadence intention, pacing role, breathing role, density impact, and transition role.
- [ ] `XS` / `S` are not used to compress major section boundaries by accident.
- [ ] `L` / `XL` are not used as decorative whitespace without narrative purpose.
- [ ] Cadence escalation is intentional when CTA stakes, density, contrast, or closure increase.
- [ ] Cadence flattening is flagged when global spacing makes every section feel the same.

---

## 6. Mobile Cadence Survivability

- [ ] Mobile cadence is reviewed separately from desktop cadence.
- [ ] Heading wraps preserve title → body breathing.
- [ ] Card stacks and dense lists remain scannable.
- [ ] CTA clusters preserve tap-safe vertical isolation.
- [ ] Footer groups retain closure rhythm on mobile.
- [ ] Missing mobile source is recorded as **SAFE UNKNOWN** for exact cadence.

---

## 7. Transition Continuity Checks

- [ ] Same-background collapse logic reviewed where adjacent sections share one surface/environment.
- [ ] Background-transition spacing logic reviewed where contrast, atmosphere, or density changes.
- [ ] Commercial continuity spacing preserves offer -> proof -> price -> trust -> FAQ -> CTA -> footer momentum.
- [ ] White-section energy collapse is flagged when light sections lose industrial/commercial pressure.
- [ ] No-isolated-block governance reviewed for full-page flow.

---

## 8. Cadence Contamination Checks

- [ ] No SaaS dashboard spacing contamination in marketing landing flow.
- [ ] No Figma slice compression drift from cropped exports.
- [ ] No accidental inheritance from previous section wrappers, global utilities, or copied SCSS.
- [ ] No random spacing values introduced outside the approved project scale.
- [ ] No giant whitespace desert introduced to compensate for an earlier compression issue.

---

## 9. REPORT Block

Use this block in Forge REPORT when cadence QA is in scope:

```text
CADENCE FINDINGS — <section or boundary scope> — <source ref>

Cadence authority: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Source screens / neighbors:
- Tier mapping:
- SAFE UNKNOWN resolver:

Continuity: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Boundary read:
- Cadence continuity:
- Cadence flattening / escalation:

Transition pacing: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Dark/light cadence:
- Dense/light bridge:
- CTA isolation:
- Footer closure:

Density stack: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Dense sections:
- Visual breathing:
- Visual exhaustion risk:
- Triumph-style 03→04→05 risk present? yes/no:

Mobile cadence: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Mobile survivability:
- Exact mobile tier authority:

Transition continuity: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Same-background boundary:
- Different-background reset:
- Commercial continuity spacing:
- Isolated-block / section-stack risk:

Disposition:
- Freeze impact:
- Deferrals / resolver:
```

---

## 10. Not Claimed

- No automatic cadence detection.
- No universal pixel ranges.
- No runtime pacing AI.
- No autonomous visual balancing.
- No automatic section redesign.

Defer to Website Factory cadence canon, rhythm governance, visual reconciliation, composition awareness, project implementation packs, and foundation QA where scoped.
