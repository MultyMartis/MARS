# Visual reconciliation checklist — MARS Forge (overlay v0)

**Mandatory companion:** [visual-reconciliation-layer.md](../../projects/mars-website-factory/visual-reconciliation-layer.md) — concept, workflow, observation format.  
**Taxonomy reference:** [visual-drift-taxonomy.md](../../projects/mars-website-factory/visual-drift-taxonomy.md).  
**Icon governance add-on:** [font-awesome-governance-checklist.md](font-awesome-governance-checklist.md) — run when the slice contains Font Awesome / icon-bearing UI.  
**Next gate:** [composition-awareness-checklist.md](composition-awareness-checklist.md) — **G7** compositional structure (composition-vs-DOM); run **with** or **immediately after** this checklist, before final responsive closure.

**Nature:** **human-supervised** governance checklist — **not** screenshot diff tooling, **not** autonomous visual AI, **not** pixel enforcement.

**When:** After **semantic QA** (semantic source lock §6) for the same slice, **before** final **responsive QA** closure and **freeze** — see workflow in [`workflow.md`](workflow.md) and screen cadence in [`semantic-source-lock.md`](semantic-source-lock.md) §5.

Record pass / partial / fail in REPORT **Forge execution** subsection under `VISUAL FINDINGS`.

---

## Gate G6 — Visual reconciliation (pre-freeze)

- [ ] **Charter** — Active source path and screen anchor named (semantic source lock §1).  
- [ ] **Visual read recorded** — At least 3 bullets from hierarchy, dominance, density, focal path, trust placement, and **screen-local surface / band role** vs source.  
- [ ] **No silent flattening** — Primary vs supporting text steps are **intentional**, not accidental equal sizing/weight.  
- [ ] **CTA dominance** — Primary CTA **reads first** among actions in the section band; secondaries visibly subordinate.  
- [ ] **Trust / proof placement** — Does not **displace** hero or primary narrative path vs source (see drift: trust displacement).  
- [ ] **Icon semantics / rhythm** — Icon-bearing UI uses source-faithful glyph meanings, section-consistent FA family/style, and stable optical rhythm; if present, record `ICON FINDINGS` per [`font-awesome-governance-checklist.md`](font-awesome-governance-checklist.md).  
- [ ] **Density sanity** — Section does not feel **heavier or emptier** than source without documented rationale (drift: density collapse, spacing inflation).  
- [ ] **Grouping** — Clusters that should separate / merge per source are not **merged/split** by accident.  
- [ ] **Asymmetry / balance** — Deliberate **weighting** (left-heavy, offset media) preserved; watch over-centering / symmetry drift.  
- [ ] **Screen-local vs foundation defaults** — Chartered **surface / band role** (light vs dark, card framing, contrast vs neighbors) read **before** reusing global or prior-section tokens; if source contradicts globals → **screen intent overrides foundation defaults** (discipline only — [visual-reconciliation-layer §1.1](../../projects/mars-website-factory/visual-reconciliation-layer.md)).  
- [ ] **Foundation contamination signals checked** — Watch for inherited dark surfaces on light compositions; mechanical **rhythm** from siblings; **CTA / trust / typography mood** copied from neighbors when source implies a **reset** ([taxonomy §D](../../projects/mars-website-factory/visual-drift-taxonomy.md)).  
- [ ] **Foundation reconciliation prompts** — Section behaving **like its source**, not only semantically? Theme/chrome overpowering? Intentional **rhythm break** preserved? Neighboring leakage? ([visual-reconciliation-layer §7.1](../../projects/mars-website-factory/visual-reconciliation-layer.md)).  
- [ ] **Drift typed** — If issues found, label with [taxonomy](../../projects/mars-website-factory/visual-drift-taxonomy.md) terms + evidence line.  
- [ ] **SAFE UNKNOWN** — Any unclear emphasis in export → **stop PASS**, document gap (visual-reconciliation-layer §7).  
- [ ] **Disposition** — PASS | PARTIAL (deferrals explicit) | FAIL recorded before responsive closure.

---

## Final responsive QA note (ordering)

After **G6 and G7**, run **final** responsive spot checks (overlay responsive gate in [`qa-checklist.md`](qa-checklist.md)) to catch **hierarchy / dominance** and **composition-at-breakpoint** issues — e.g. focal collapse, accidental equalization in stack, cluster split on stack.

---

## Not claimed (v0)

- Pixel diff, perceptual hash, or CV automation.  
- Automatic pass/fail from tooling.  
- Mobile emphasis without chartered breakpoint exports.

---

## Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-16 | Initial G6 checklist for Visual Reconciliation Layer. |
| v0.1 | 2026-05-16 | Pointer to G7 compositional structure checklist + ordering note. |
| v0.2 | 2026-05-16 | **Foundation contamination bias:** screen-local vs globals, detection signals, §7.1 prompts; visual read includes surface/band role. |
| v0.3 | 2026-05-16 | Added Font Awesome icon governance add-on for icon-bearing slices. |
