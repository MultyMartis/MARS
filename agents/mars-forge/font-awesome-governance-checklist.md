# Font Awesome governance checklist — MARS Forge (overlay v0)

**Mandatory companion:** [`../../projects/mars-website-factory/font-awesome-governance-layer.md`](../../projects/mars-website-factory/font-awesome-governance-layer.md).  
**Nature:** human-supervised icon review discipline — **not** runtime icon tooling, **not** automated glyph selection, **not** SVG pipeline engineering.

**When:** first during project bootstrap / source inspection, then during Forge QA with gate **G6** visual reconciliation and before freeze. Use with **G7** when icon rows affect grouping or composition.

Record pass / partial / fail in REPORT **Forge execution** under `ICONOGRAPHY FINDINGS`.

---

## Gate G6 add-on — Font Awesome icon governance

- [ ] **Startup decision made** — before section implementation, decide whether FA may be needed for hero benefits, proof strips, spec rows, trust/review features, CTA/contact features, or other real UI/content icon slots.
- [ ] **Approved source inspected** — check `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/` before choosing classes or delivery.
- [ ] **Local delivery prepared early** — if CSS+webfont is used, create the project-local `css/` and `webfonts/` structure before section work depends on icons.
- [ ] **Webfont formats valid** — webfont delivery uses real `woff2` and `woff`; SVG-font-only delivery is not accepted as a final frontend fix.
- [ ] **Path relationship preserved** — local FA CSS `@font-face` paths resolve from `css/` to sibling `webfonts/`.
- [ ] **Referenced webfonts copied** — the built `dist` artifact contains every `woff2` / `woff` file referenced by local FA CSS.
- [ ] **Duotone source valid or blocked** — duotone is used only with verified matching `woff2` / `woff` webfonts or an approved inline SVG/sprite source; absent webfonts are recorded as BLOCKED, not guessed.
- [ ] **Solid fallback declared honestly** — CSS-softened solid icons are reported as solid fallback / verified solid delivery, never as active duotone output or duotone status.
- [ ] **Built glyph rendering verified** — the built `dist` page renders actual FA icons, not red/tofu squares, fallback boxes, or incorrect glyphs.
- [ ] **Class/codepoint/font mapping verified** — every used FA class exists in CSS, every mapped codepoint exists in the chosen font, and generated subsets are not accepted without this check.
- [ ] **Canonical version** — icon source is Font Awesome Pro **5.15.4** or a documented brand/custom exception.
- [ ] **Delivery mode respected** — implementation follows the target project’s existing webfont / sprite / extracted SVG mode; no casual second pipeline.
- [ ] **Role map named** — trust strip, specification rows, CTA/support, prohibition/transport lists, and social/contact roles identified where present.
- [ ] **Semantic fidelity** — each glyph matches local text meaning before visual resemblance.
- [ ] **No random FA** — glyphs were chosen from meaning and role, not because a nearby FA name looked acceptable.
- [ ] **No SaaS icon drift** — playful/generic SaaS icon language did not replace operational or commercial semantics.
- [ ] **Family consistency** — section uses a clear dominant style rule (`fal`, `far`, `fas`, `fab`) with role-based exceptions only.
- [ ] **Optical rhythm** — repeated icons align, share stable size/gap/baseline, and do not wobble text columns.
- [ ] **Hierarchy safety** — icons do not overpower CTA labels, specification values, trust copy, or primary narrative.
- [ ] **Brand handling** — `fab` used only for real brands; missing partner/marketplace/messenger marks remain documented assets.
- [ ] **Baked image discipline** — icons, labels, callouts, or annotations already baked into source pixels were not duplicated as separate overlays.
- [ ] **Drift typed** — if issues exist, use icon drift labels from the companion layer.
- [ ] **SAFE UNKNOWN** — unresolved glyph names, license path, or source meaning blocks PASS.
- [ ] **Disposition** — PASS | PARTIAL | FAIL recorded before section freeze.

---

## REPORT stub

```text
ICONOGRAPHY FINDINGS — <section or block_id> — <source ref>

Roles:
- <trust strip / spec rows / CTA-support / transport-prohibition / social-contact>

Policy:
- Canonical FA version: Font Awesome Pro 5.15.4
- Dominant section style: <fal / far / fas / fab / custom>

Checks:
- Semantic fidelity: PASS | PARTIAL | FAIL
- Family consistency: PASS | PARTIAL | FAIL
- Optical rhythm: PASS | PARTIAL | FAIL

Drift labels:
- <none / icon semantic mismatch / mixed-weight UI drift / optical rhythm drift / etc.>

Exceptions:
- <brand/custom/SAFE UNKNOWN>

Disposition: PASS | PARTIAL | FAIL
```

---

## Not claimed (v0)

- No automatic icon registry or policy engine.
- No automatic FA name validation.
- No screenshot or computer-vision icon scoring.
- No authority to replace official brand marks with generic FA glyphs.
- No approval of generated FA subsets until actual built glyph rendering and class/codepoint mapping are verified.

---

## Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-16 | Initial Forge icon governance checklist for FA Pro 5.15.4 discipline. |
| v0.1 | 2026-05-18 | Renamed reporting category to `ICONOGRAPHY FINDINGS`; added random-FA, SaaS icon drift, and baked annotation checks. |
| v0.2 | 2026-05-18 | Added bootstrap FA readiness, local delivery, `woff2`/`woff`, and path-resolution checks. |
| v0.3 | 2026-05-18 | Added built `dist` glyph rendering verification and generated-subset mapping checks. |
| v0.4 | 2026-05-18 | Added referenced-webfont copy check and duotone blocked-until-verified delivery rule. |
| v0.5 | 2026-05-18 | Added truth rule: CSS-softened solid fallback is not active duotone output and must be reported as verified solid delivery. |
