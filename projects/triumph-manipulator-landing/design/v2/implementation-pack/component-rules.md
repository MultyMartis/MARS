# V2 — Component rules (implementation pack v0)

**Scope:** Buttons, cards, trust blocks, forms, CTAs for Triumph V2 — **structural/behavioral** rules agents can check. Visual detail: **`design/v2/`** + [triumph-manipulator-design-system.md](../../../design-system/triumph-manipulator-design-system.md).

## Source discipline

- Component **meaning** comes from **`design/v2/`** (which block type appears where).
- **`shared-assets/`** supplies **media**, not component taxonomy.

---

## Buttons / CTAs

- **Primary CTA:** brand accent (`--tm-accent` family); **no border-radius**.
- **Secondary / ghost:** bordered or inverted as in mock — **do not** add pill/rounded variants.
- **Label text:** **LOCKED** if visible on `NN.png` (see `semantics/content-authority.md`).
- **States:** hover/active/focus visible; focus ring must not rely on color alone.

---

## Cards

- **Rectilinear:** `border-radius: 0`; border `1px` using light/dark token as appropriate.
- **Padding:** baseline **24px** inner (adjust to mock).
- **Segment cards (`04`):** image + title + bullet lists as in PNG — not generic “service” blurbs.

---

## Trust / case blocks (`03`)

- **Three** peer cards + sidebar pattern — maintain **equal stature** (not one giant + two suppressed).
- **Chat / “correspondence”** cues: reproduce **layout role** from mock; **no fabricated** chat content in production unless operator supplies.

---

## Problem–solution matrix (`05`)

- Present as **paired rows** (problem / solution), **not** accordion-first, unless operator changes IA.
- Icon column alignment: stable vertical rhythm with **6** logical rows per side when implementing full mock.

---

## Forms (`01`, `06`)

- Field labels and required markers per mock; no extra fields “for SEO.”
- Submit control **matches** PNG CTA where shown.
- Legal / consent line: **LOCKED** or **PLACEHOLDER** only — no invented privacy claims.

---

## Iconography

- Use **approved** set (project policy / Font Awesome local pack). **No** ad-hoc emoji or generated SVG icons.

---

## Anti-drift

- Do not merge **consultation** and **hero** forms into one shared “smart” component if mock shows **distinct** compositions.
- Do not convert **matrix** into **FAQ** component for convenience.
