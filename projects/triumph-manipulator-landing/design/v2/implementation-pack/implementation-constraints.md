# V2 — Implementation constraints (forbidden patterns)

**Purpose:** Stop recurring **semantic** and **structural** failures during Forge / frontend validation. Complements [V2-FRONTEND-SOURCE-OF-TRUTH.md](../../../V2-FRONTEND-SOURCE-OF-TRUTH.md).

## Source discipline

- **`design/v2/`** = canonical implementation source.
- **`design/v1/`** = archive only.
- **`design/shared-assets/`** = media only.

---

## Forbidden patterns

| ID | Forbidden | Rationale |
|----|-----------|-----------|
| F-DOM-ORDER | Implementing or QA’ing **only** from stale `index.html` assumptions | Canonical homepage `<main>` order now matches **`01`→`06`** flow (fleet block removed); still **verify each screen** against **`NN.png`**, not memory. |
| F-PNG-INDEX | Saying “third screen” = **third `<main>`** without naming **`03.png`** vs DOM | **Homepage:** third `<main>` = cases. Ambiguity remains if **re-reading old docs** or validation page. |
| F-FLEET | Expanding **one-machine** sections into **multi-machine** choice or pricing | Breaks L-MACHINE-02, L-CONSULT-06, L-FOOT-07. |
| F-EP-HOME | Re-adding **`equipment-prices`** to **`index.html`** without a **new** operator gate | **Forbidden** — block stays on **`validation-equipment-prices.html`** only until a new decision. |
| F-V1-BLEND | Copying **order, copy, or intent** from **`design/v1/`** or **landing-strip-*** partials | V1 contamination. |
| F-COPY-AI | Paraphrasing **LOCKED** headlines/CTAs with “better” marketing | Invented / unlock drift. |
| F-STUB-FILL | Filling stubs with **believable fake** cases, INN, chats, reviews | Legal/reputation risk; use PLACEHOLDER policy. |
| F-MATRIX-FAQ | Retheming **`problem-solution-matrix`** as accordion FAQ by habit | Semantic mutation vs `05.png` (matrix, not FAQ). |
| F-SECTION-INSERT | Adding **new** marketing sections not in **`design/v2/`** | Uncontrolled insertion. |
| F-SOURCE-BLEND | Mixing PDF (retired), old maps, or **full.png** paraphrase as **verbatim** copy | **full.png** = order check; lines per **`NN.png`**. |
| F-PADDING-DRIVEBY | Tweaking **global section padding** while working one screen | Causes **padding rhythm regression** on frozen sections. |
| F-STRUCTURE-SHIMS | Shipping **3+3** stub rows for a **6×2** mock as “complete” | Structural under-delivery on `05.png`. |

---

## Required when editing

1. Open **active** `design/v2/NN.png` for this task.  
2. Cross-check [section-order.md](../semantics/section-order.md) + [semantic-locks.md](../semantics/semantic-locks.md).  
3. If **any** conflict vs `src/` → **stop and report** before silent fixes.

---

## Lessons explicitly encoded

- **equipment-prices** drift vs **V2** narrative ([section matrix](../../../V2-SECTION-SOURCE-MATRIX.md)).  
- **PNG order ≠ `<main>` order** until re-wired.  
- **one-machine** vs **fleet** is a governance line, not stylistic preference.  
- **Stub completion** must not become **generative marketing**.
