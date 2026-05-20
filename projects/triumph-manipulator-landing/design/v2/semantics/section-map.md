# V2 — Section map (semantics ↔ screens)

**Pack:** first canonical implementation pack (`design/v2/implementation-pack/`, `design/v2/validation/`).  
**Purpose:** Map each **V2 raster screen** to semantic role, intent, and the **expected** implementation target (when known). This is **not** a DOM contract.

## Source discipline

| Source | Role |
|--------|------|
| **`design/v2/`** (`01.png` … `07.png`, `full.png`) | **Canonical implementation source** — visual order, block intent, copy visible on mocks. |
| **`design/v1/`** | **Archive only** — must not define V2 section meaning or order. |
| **`design/shared-assets/`** | **Reusable media only** — not semantics, not structure. |

**Companions:** [V2-VISUAL-SOURCE-MATRIX.md](../../../V2-VISUAL-SOURCE-MATRIX.md), [V2-SECTION-SOURCE-MATRIX.md](../../../V2-SECTION-SOURCE-MATRIX.md).

---

## Screen matrix

| Screen file | Semantic role | Section purpose | Matching implementation (if known) | Notes |
|-------------|---------------|-----------------|-----------------------------------|--------|
| `01.png` | **Hero + primary conversion** | First viewport: offer (5 t / 3 t / 14 m narrative), price band, primary + secondary CTAs, estimate form column, supporting parameter grid / trust strip | `hero-conversion` (+ global `header` before `<main>`) | Header/nav is part of screen 01 composition. Bullet list in hero vs lower strip may diverge — verify **pixel + operator** before “improving” copy. |
| `02.png` | **Single-machine showcase** | One concrete rig (Hino + UNIC): **5** spec parameters, “what we haul / what we don’t”, dedicated CTA column | `machine-specs-transport-lists` | **Not** a fleet catalog. Long lists: word-level lock from PNG or operator. |
| `03.png` | **Trust + case studies** | Heading about working with clients; **three** case columns (photo, tag, body, “correspondence” cue); trust sidebar + legal snippet; lower CTA | `trust-cases-social-proof` | Entity count: **3** cases. Do not invent client stories. |
| `04.png` | **Segments / use cases** | Subhead + H2 “for which tasks…”; **8** numbered scenario cards (01–08) with imagery and lists | `segments-applications-grid` | **8** cards. **Single-machine** scenarios — not “pick from fleet.” |
| `05.png` | **Problem → solution matrix** | Two columns × **6** row pairs, icons, closing CTA | `problem-solution-matrix` | Visual is **6×2**, not FAQ accordion. Anchor **`problem-solution`** in current `src` — do not re-theme as generic FAQ without operator decision. |
| `06.png` | **Consultation / lead (dark band)** | Bullets to clarify task; **“one machine”** highlight box; checklist of parameters (5 t / 3 t / 14 m etc.); form + phone | `consultation-lead-form` | “One machine” framing is **mandatory** — not “we’ll pick from pool.” |
| `07.png` | **Footer** | Messenger row; 3 columns (brand + **one** spec line 5t/3t/14m, legal links, contacts); bottom bar (INN / © / credit) | `site-footer-v2` | Brand column must stay **one configuration** story unless operator changes brief. |
| `full.png` | **Composite reference** | Vertical stack confirming **01→07** order | *n/a* (sanity check only) | Use to verify sequence; fine copy still per `NN.png`. |

---

## Explicit non-members (homepage canon)

| Artifact | Status |
|----------|--------|
| **Multi-machine / fleet price cards** between `02` and `03` | **Absent** from `design/v2` homepage flow. **`equipment-prices`** preserved on **`validation-equipment-prices.html`** only ([equipment-prices-quarantine.md](../validation/equipment-prices-quarantine.md)). |

---

## SAFE UNKNOWN

- Until pixel proof: **verbatim** match of every string in `01.png` hero vs current `src`.
- Final legal/footer strings for `07.png` vs future `site-footer-v2` content (operator / counsel).
- Full nested `partials/components/*` map for each row (see section matrix).
