# V2 — Canonical section order (visual only)

**Purpose:** Single **canonical homepage narrative order** for Triumph Manipulator Landing **V2**, as read from **`design/v2/`** top to bottom.  
**Out of scope:** DOM node order, `@@include` order, legacy `index.html`, experimental blocks, V1 strip order.

## Source discipline

- **`design/v2/`** = canonical implementation source for **order and meaning**.
- **`design/v1/`** = archive only.
- **`design/shared-assets/`** = reusable media only (no IA / order).

---

## Canonical V2 order (01 → 07)

1. **`01.png`** — Hero + primary conversion (with header in same visual screen)
2. **`02.png`** — Single machine: specs + transport lists + CTA column
3. **`03.png`** — Reviews / trust / **three** cases
4. **`04.png`** — Segments & applications — **eight** cards
5. **`05.png`** — Problem → solution matrix (**six** row pairs per column in mock)
6. **`06.png`** — Consultation & estimate (dark closing lead)
7. **`07.png`** — Footer (messengers, columns, legal bar)

**`full.png`** — composite; must reflect the same sequence.

---

## Not in canon

- **`equipment-prices`** (fleet / multi-card pricing) — **no** corresponding `design/v2` slice between `02` and `03`. **Not on homepage** (removed from `index.html` 2026-05-16). Isolated on **`workspaces/triumph-manipulator-landing-v2/src/pages/validation-equipment-prices.html`** — **EXPERIMENTAL / VALIDATION** only; see [equipment-prices-quarantine.md](../validation/equipment-prices-quarantine.md) and [V2-CLEANUP-DECISION-LOG.md](../../../V2-CLEANUP-DECISION-LOG.md).
- **`design/v1/`** strip sequence and any **landing-strip-*** legacy maps — **not** V2 order truth.

---

## Rule for agents

**Homepage (post–2026-05-16):** third **visual** screen **`03.png`** (cases) ↔ third **`<main>`** block `trust-cases-social-proof` — **aligned**. The former **`equipment-prices`** / «третий PNG vs третий include» collision applies only to **historical DOM** or if someone re-inserts the block; do **not** re-equate terms without checking which snapshot you mean.

When validating “section 3” or “third screen”: default = **`03.png` / cases**; if discussing **`equipment-prices`**, say **validation page** explicitly.
