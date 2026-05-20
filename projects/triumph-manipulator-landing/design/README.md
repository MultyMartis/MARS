# Triumph Manipulator Landing — design folder map

This directory holds **versioned design exports** and **shared raster/SVG materials** for the Triumph Manipulator Landing initiative inside MARS. It is **documentation-facing source architecture** — not the Gulp implementation tree (`workspaces/`).

**Normative isolation rules:** [V2-FRONTEND-SOURCE-OF-TRUTH.md](../V2-FRONTEND-SOURCE-OF-TRUTH.md) §4 (Design version isolation).

---

## Layout

```
projects/triumph-manipulator-landing/design/
├── v1/
├── v2/
├── shared-assets/
└── README.md   ← this file
```

---

## A. `design/v2/` — CANONICAL IMPLEMENTATION SOURCE (V2)

**Status:** **CANONICAL IMPLEMENTATION SOURCE** for **Triumph Landing V2**.

**Allowed uses:**

- Frontend implementation (pixel fidelity, layout, spacing, hierarchy).
- Forge validation and phased QA against approved visuals.
- Section semantics **as visible in these exports** (reading order, intent of blocks shown).
- DOM structure and landmarks **when derived from** these mocks plus the written rule stack.
- Visual flow and responsive interpretation consistent with the mocks.

**Notes:**

- Filenames `01.png` … `07.png` and `full.png` are the trusted V2 raster set unless superseded by explicit operator decision recorded in project docs.
- **Visual references ≠ semantic references in isolation** — meaning must still align with [V2-FRONTEND-SOURCE-OF-TRUTH.md](../V2-FRONTEND-SOURCE-OF-TRUTH.md) and matrices; do not infer copy or IA from unrelated folders.

---

## B. `design/v1/` — ARCHIVE / HISTORICAL REFERENCE ONLY

**Status:** **ARCHIVE / HISTORICAL REFERENCE ONLY** (prior strip-era landing composition).

**Allowed uses:**

- Historical comparison against older iterations.
- Research and audit trails.
- Legacy continuity maps (e.g. `frontend-section-map.md` ↔ `landing-strip-*` scaffolding).

**Forbidden for V2:**

- V2 implementation targets.
- Semantic interpretation of the **current** homepage or sections for V2.
- DOM generation or section ordering truth for V2.
- Section meaning, IA, or marketing narrative authority for V2.
- Content or headline generation for V2.

**Path note:** Older documentation may mention `design/mockups/`. That name is **deprecated**; **canonical archive path for those PNGs is `design/v1/`**. If a stray `design/mockups/` directory appears in a working copy, treat it as **stale** — do not use it as V2 truth.

---

## C. `design/shared-assets/` — REUSABLE VISUAL MATERIALS

**Status:** **REUSABLE VISUAL MATERIALS** (cross-version graphics).

**Allowed uses:**

- Logos and brand marks.
- Icons and small SVG/raster UI graphics.
- Reusable backgrounds and decorative images.
- Other shared visual materials **explicitly approved** for embedding in implementation.

**Important:**

- **`shared-assets/` does not define section semantics or landing structure.**  
  It does not set homepage order, headline intent, or block roles for any generation unless paired with that generation’s canonical mocks (`design/v2/` for V2).

---

## Companion indexes

| Document | Role |
|----------|------|
| [mockups-index.md](./mockups-index.md) | Index of **V1** slice filenames under `design/v1/` |
| [frontend-section-map.md](./frontend-section-map.md) | Legacy strip ↔ partial continuity (**V1** foundation; not V2 homepage truth) |
| [../V2-CANONICAL-STATE.md](../V2-CANONICAL-STATE.md) | Where to edit live V2 implementation |
| [../V2-FRONTEND-SOURCE-OF-TRUTH.md](../V2-FRONTEND-SOURCE-OF-TRUTH.md) | Classification of sources + **Design version isolation** |

---

## Document control

- **Purpose:** Prevent semantic contamination between design generations (V1 vs V2) and between reusable assets vs versioned mocks.
- **Does not replace:** Implementation under `workspaces/` or operator approvals outside this repo structure.
