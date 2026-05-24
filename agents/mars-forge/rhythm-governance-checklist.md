# Rhythm governance checklist — MARS Forge

**Status:** Forge overlay checklist for **human-supervised** rhythm QA.  
**Not:** automated typography linting, spacing engine, screenshot diff, runtime enforcement, or autonomous cadence analysis.

**Website Factory layers:**

- [Typography Rhythm Governance](../../projects/mars-website-factory/typography-rhythm-governance.md)
- [Russian No Word-Splitting Typography v1](../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md)
- [Vertical Rhythm Governance](../../projects/mars-website-factory/vertical-rhythm-governance.md)
- [Canonical Vertical Cadence System](../../projects/mars-website-factory/canonical-vertical-cadence-system.md)
- [Cadence Tier Model](../../projects/mars-website-factory/cadence-tier-model.md)

**Companion Forge checklist:** [`cadence-governance-checklist.md`](cadence-governance-checklist.md) records `CADENCE FINDINGS` for inter-screen narrative pacing. This file records `RHYTHM FINDINGS` for typography cadence and vertical rhythm detail.

Use this checklist during Forge QA / pre-freeze when a section or screen slice has visible typography, spacing, CTA, or density implications.

---

## 1. Typography Cadence Checks

- [ ] Project typography authority identified: implementation pack, design system, annotated export, or **SAFE UNKNOWN**.
- [ ] Preferred landing rhythm model applied where no approved exception exists: `line-height = font-size + 4px`.
- [ ] No arbitrary line-height values such as `53px`, `57px`, `61px` introduced without named approval.
- [ ] No random decimal line-height values such as `1.08` or `1.13` used as hidden cadence math.
- [ ] Body, list, lead, caption, and helper text use deterministic line-height or documented exception.
- [ ] Typography inheritance checked for accidental global or previous-section contamination.

---

## 2. Heading Rhythm Checks

- [ ] Heading scale descends predictably from hero to supporting sections.
- [ ] Section title → subtitle → body spacing is consistent with source / pack.
- [ ] Heading wraps at mobile widths preserve readability and hierarchy.
- [ ] **No mid-word splits (RU):** run [ru-landing-qa-preset-v1.md](../../projects/mars-website-factory/ru-landing-qa-preset-v1.md); authority [russian-no-word-splitting-typography-v1.md](../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md).
- [ ] Similar section roles do not use unrelated heading cadence unless source clearly requires it.
- [ ] Visual reconciliation confirms headings read with intended emphasis, not merely correct tags.

---

## 3. Paragraph Cadence Checks

- [ ] Paragraph stacks keep repeatable spacing inside sections, cards, forms, and proof blocks.
- [ ] Dense copy areas reduce content pressure through structure before compressing line-height.
- [ ] List item rhythm remains readable and does not collapse into a text wall.
- [ ] Captions, disclaimers, and metadata remain legible instead of being squeezed by layout fixes.

---

## 4. Section Spacing Checks

- [ ] Inter-screen cadence issues that affect narrative pacing are also checked via [`cadence-governance-checklist.md`](cadence-governance-checklist.md).
- [ ] Section `padding-block` follows project spacing scale or source-specific approved deviation.
- [ ] Adjacent sections do not collide or create double-gaps at shared boundaries.
- [ ] Global spacing changes did not shift previously frozen neighbors.
- [ ] Dark/light transitions include deliberate entry and exit breathing.
- [ ] Footer has terminal breathing; no footer suffocation.

---

## 5. Density Continuity Checks

- [ ] Sparse → dense transitions are readable and do not create a sudden wall of content.
- [ ] Dense → sparse transitions provide a reset without giant dead whitespace.
- [ ] Card grids, proof rows, forms, and technical lists do not create unplanned density spikes.
- [ ] Section pressure is identified when a section carries too many visual obligations for its cadence.
- [ ] Visual fatigue risk recorded if irregular rhythm accumulates across the landing.

---

## 6. CTA Spacing Checks

- [ ] Primary CTA has enough isolation to remain the conversion focal point.
- [ ] Secondary CTA/link does not crowd or visually equalize the primary CTA by accident.
- [ ] CTA helper text, proof, form fields, consent text, and submit buttons use deterministic gaps.
- [ ] CTA cluster remains readable at mobile widths with tap-safe spacing.
- [ ] CTA crowding is recorded as a rhythm finding, not hidden as a styling detail.

---

## 7. Mobile Cadence Checks

- [ ] Mobile heading wraps preserve title → body breathing.
- [ ] Card stacks use readable item gaps and do not collapse into one continuous band.
- [ ] Dense technical lists remain scannable.
- [ ] Forms and buttons preserve vertical rhythm and tap targets.
- [ ] Missing mobile source is recorded as **SAFE UNKNOWN** for exact cadence.

---

## 8. Dark / Light Transition Rhythm Checks

- [ ] Light islands inside dark flows have intentional top and bottom breathing.
- [ ] Dark bands after light sections do not collide or feel abruptly compressed.
- [ ] Screen-local surface intent overrides accidental foundation contamination when source is clear.
- [ ] Transition harshness is named when contrast and spacing shift too abruptly together.

---

## 9. REPORT Block

Use this block in Forge REPORT when rhythm QA is in scope:

```text
RHYTHM FINDINGS — <section or block_id> — <source ref>

Typography cadence: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Heading rhythm:
- Paragraph cadence:
- Line-height model:

Vertical rhythm: PASS | PARTIAL | FAIL | SAFE UNKNOWN
- Section cadence:
- Density continuity:
- CTA spacing:
- Mobile cadence:
- Dark/light transition rhythm:

Disposition:
- Freeze impact:
- Deferrals / resolver:
```

---

## 10. Word-splitting / RU typography checks

**Authority:** [russian-no-word-splitting-typography-v1.md](../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md) — full CSS/HTML rules; **do not** duplicate here.  
**QA preset:** [ru-landing-qa-preset-v1.md](../../projects/mars-website-factory/ru-landing-qa-preset-v1.md) — mandatory widths and checks for Russian commercial landings.

- [ ] Preset widths run; no mid-word splits; no horizontal overflow; headings/CTA/FAQ/forms per preset.
- [ ] No forbidden overflow CSS on UI (see authority — `anywhere`, `break-all`, global body `break-word`, UI `break-word`).
- [ ] Orphan/headline fixes: layout and selective ties only — no `nowrap` / `&nbsp;` chains / word fragmentation (typography-rhythm C-04/C-05).

Include: `RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial | FAIL | SAFE UNKNOWN`.

---

## 11. Not Claimed

- No automatic line-height linting.
- No automatic spacing token enforcement.
- No visual scoring or fatigue metric.
- No runtime typography or layout engine.
- No autonomous section redesign.

Defer to project implementation packs, Website Factory governance layers, visual reconciliation, composition awareness, and foundation QA where scoped.
