# V2 — Semantic locks

**Purpose:** Hard **semantic** constraints for Forge / frontend agents validating against **`design/v2/`**. Not a styling spec.

## Source discipline

| Path | Role |
|------|------|
| `design/v2/` | Canonical implementation source (locks below derive from here + written matrix). |
| `design/v1/` | Archive — **forbidden** as authority for locks below. |
| `design/shared-assets/` | Media only — **no** lock on titles or counts from filenames alone. |

---

## Locked titles / meanings (structural)

| Lock ID | Statement |
|---------|-----------|
| L-HERO-01 | Screen **`01.png`** is **hero + conversion** (offer, pricing band, CTAs, form, supporting facts). It is not a generic “intro only” strip. |
| L-MACHINE-02 | Screen **`02.png`** is **one named machine** (Hino + UNIC path in mock), not a **fleet catalog** or “our park.” **Screen 02 is NOT a fleet catalog.** |
| L-CASES-03 | Screen **`03.png`** is **trust + case studies** (three parallel cases), not pricing tables. |
| L-SEG-04 | Screen **`04.png`** is **segments / tasks for one machine**, not multi-tonnage **equipment pickers**. |
| L-PS-05 | Screen **`05.png`** is **problem → solution matrix**, not a classic FAQ accordion by default. |
| L-CONSULT-06 | Screen **`06.png`** reinforces **one machine** + parameter checklist + lead form — not “we’ll source any crane from fleet” unless operator re-briefs. |
| L-FOOT-07 | Screen **`07.png`** footer brand column carries **one** spec line (5t / 3t / 14m) — not a multi-machine menu. |

---

## Entity-count locks

| Lock | Count | Forbid |
|------|-------|--------|
| Cases on `03.png` | **3** | Collapsing to 1 “generic testimonial” or inflating to >3 without operator approval |
| Segment cards on `04.png` | **8** | “About 8” placeholders; different grid without mock |
| Problem/solution rows on `05.png` | **6** pairs per column (mock) | Shipping **3+3** stub rows as “done” — structure under-spec vs V2 |
| Spec parameters called out on `02.png` | **5** in mock pattern | Renumbering or merging into unrelated KPI set without mock |

---

## Forbidden rewrites

1. **Fleet narrative** on sections locked to **single-machine** (`02`, `04`, `06`, `07` brand column).
2. **Marketing “improvement”** paraphrase of visible headlines / CTAs / legal lines on mocks.
3. **V1 / strip-era** copy or intent pulled from **`design/v1/`** or old section maps.
4. **Invented** case studies, segment titles, FAQ/problem lines, or footer legal text.

---

## Forbidden semantic mutations

| Do not… | Why |
|---------|-----|
| Treat **`equipment-prices`** as the **third V2 screen** on the **homepage** | Third **PNG** is `03.png` (cases). **`equipment-prices`** is **not** in homepage `index.html` — only on `validation-equipment-prices.html` ([V2-VISUAL-SOURCE-MATRIX.md](../../../V2-VISUAL-SOURCE-MATRIX.md)). |
| Turn **`02.png`** into multi-card tonnage SKUs | One-machine semantic lock. |
| Turn **`06.png`** into “select equipment class” wizard | Violates one-machine consultation lock. |
| Infer **structure** from **`shared-assets/`** alone | Visuals there are not IA. |

---

## Quarantine (validation / experimental)

**`equipment-prices`** — **removed from homepage** `index.html` (operator-approved 2026-05-16). Preserved on disk; rendered **only** on **`validation-equipment-prices.html`**. Do **not** re-expand onto the main page without a **new** written gate. Fleet semantics **must not** leak into canonical **`01.png`–`07.png`** sections during stub fill.
