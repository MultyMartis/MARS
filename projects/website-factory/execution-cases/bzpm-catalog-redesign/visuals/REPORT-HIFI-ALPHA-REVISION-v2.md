# REPORT — BZPM HIFI ALPHA SVG REVISION v2

**Execution case:** `bzpm-catalog-redesign`  
**Phase:** W8A.1 — Hi-Fi Alpha SVG Revision  
**Lane:** A (Website Factory)  
**Mode:** Visual Revision — no implementation  
**Date:** 2026-06-09  
**Reference SKU:** ВМЦ-П3-2/500 (серия ПРЕМИУМ-3)

**Source:** `BZPM-PDP-HIFI-ALPHA-v1.md` · v1 SVG artifacts  
**Approved direction (unchanged):** 70% Mockup B · 30% Mockup A

---

## Created files

| File | Role |
|------|------|
| `visuals/BZPM-PDP-HIFI-ALPHA-DESKTOP-v2.svg` | Desktop Hi-Fi concept — revised |
| `visuals/BZPM-PDP-HIFI-ALPHA-MOBILE-v2.svg` | Mobile Hi-Fi concept — revised |
| `visuals/REPORT-HIFI-ALPHA-REVISION-v2.md` | This report |

**Generator updated:** `visuals/_generate_hifi_alpha.py` — adds v2 output paths; v1 artifacts preserved.

---

## What changed

### Revision 1 — Product Context Block (desktop + mobile)

| v1 | v2 |
|----|-----|
| Hard-coded **Series Context Band** | Universal **Product Context Block** |
| Label `СЕРИЯ` + `ПРЕМИУМ-3` | `Серия ПРЕМИУМ-3` (Mode 1 example) |
| `Цельнотянутые ванны премиум-класса` | `Цельнотянутые моечные ванны` |
| Button `Все модели серии (10) →` | Text link `10 моделей в серии` |
| Cross-links `См. также: ПРЕМИУМ · СТАНДАРТ` | **Removed** — not universal across catalog sections |

**Design annotations (not live UI copy):**

- Internal label above block: `Product Context · Mode 1 (Series)` / `Product Context · Mode 1`
- Legend note (desktop panel + mobile footer area):  
  *«Блок условный: серия / линейка / группа. Если контекста нет — скрывается.»*

**Three supported modes (concept logic, not all rendered):**

| Mode | When | Example copy |
|------|------|--------------|
| **1 — Series** | Clear OEM series | Серия ПРЕМИУМ-3 · Цельнотянутые моечные ванны · 10 моделей в серии |
| **2 — Product line / group** | Broader group, no strict series | Группа оборудования · Производственные столы ASSUM · Модели разных размеров и исполнений |
| **3 — Hidden** | No meaningful group context | Block not shown |

Current SVG shows **Mode 1** for reference SKU only.

### Revision 2 — Mobile gallery position

Gallery moved from **P4** to **P1**, compact size (140px hero + thumb strip, not full-width 200px block).

**New P1 order:** Product Context → article / H1 → compact gallery → price / stock / CTA → B2B one-liners.

Priority zones P2–P5 reorganized to match operator feedback (buyer sees product image early without pushing commercial core too far down).

---

## What stayed unchanged

- Overall 70/30 B/A visual direction — no redesign, no new concept
- Desktop hero layout: ~30% media column, fit grid, buy box, integrated commercial row
- Desktop scroll zones: min spec table, description, full specs accordion, documents, in-series alternatives, related equipment, trust strip, footer
- Reference content (ВМЦ-П3-2/500, prices, dimensions, sibling cards)
- Palette, typography weights, card geometry, industrial OEM tone
- No OpenCart · no Twig · no CSS · no JS · no implementation

---

## Mobile order — before / after

### v1 (before)

| Zone | Content order |
|------|----------------|
| **P1** | Commercial (price/CTA) → Series band → article/H1 → fit grid → B2B links |
| **P2** | Compare / Избранное → Ключевые параметры (5 rows) |
| **P3** | In-series alternatives → consult links → description teaser |
| **P4** | Full specs accordion → documents → **Фото / gallery** ← too low |
| **P5** | Back to series → related equipment → footer |

### v2 (after)

| Zone | Content order |
|------|----------------|
| **P1** | **Product Context** → article/H1 → **compact gallery** → price/stock/CTA → B2B links |
| **P2** | Fit verification grid → Compare / Избранное → Ключевые параметры |
| **P3** | Min spec summary (description prose + «Показать полностью») |
| **P4** | Full specs accordion → documents *(gallery removed)* |
| **P5** | In-series alternatives → back to series → consult → related equipment → legend note → footer |

**Operator intent addressed:** product image visible in first screenful (~y 256px on 390px viewport) before deep scroll; commercial core remains in P1 after identity confirmation.

---

## Product Context block logic

```text
IF product has OEM series (taxonomy)
  → Mode 1: «Серия {NAME}» + category descriptor + model count
ELSE IF product belongs to product line / equipment group
  → Mode 2: «Группа оборудования» + line name + size/variant note
ELSE
  → Mode 3: block hidden (no empty band, no breadcrumb-only substitute)
```

**Implementation feasibility (future, not in scope):** block content can be driven from existing OpenCart category/series metadata where present; Mode 3 is the default fallback for orphan SKUs. Cross-family links (`См. также`) deliberately removed from universal block — belong in alternatives / navigation, not context band.

---

## Known limitations

1. **Modes 2 and 3 not illustrated** — only Mode 1 rendered for ПРЕМИУМ-3 SKU; stakeholder must infer other modes from legend + this report.
2. **Design annotations visible** — `Product Context · Mode 1` labels are reviewer aids; strip before live implementation experiment.
3. **Mobile P3 naming** — zone labeled «Min Spec Summary» shows prose description; desktop min spec remains the key-parameters table (P2 mobile carries table for scan continuity). Intentional mobile compression — not a layout divergence for implementation.
4. **Sticky CTA** — not shown; remains TBD from v1 concept.
5. **Illustrative values** — prices, stock counts, sibling SKUs unchanged from v1; content ops owns final data.
6. **Generator regen** — v2 SVGs are build outputs from `_generate_hifi_alpha.py`; hand-edit SVG discouraged.

---

## Next step (out of scope for this task)

After operator approval of v2 SVGs → **manual implementation experiment** on live test PDP using current site styles (no new design system).

---

## Git status note

New/untracked deliverables under `projects/website-factory/execution-cases/bzpm-catalog-redesign/visuals/`. No commit performed.
