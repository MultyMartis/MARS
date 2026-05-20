# V2 — Drift observations (seed)

**Purpose:** Running log of **known failure modes** for Triumph V2. Append new entries with date + link to task; keep entries short.

## Source discipline

- Root cause analysis references **`design/v2/`** vs implementation, not assumptions.

---

## Seeded lessons (from project audit / matrices)

| Topic | Observation | Mitigation (pack) |
|-------|-------------|-------------------|
| **equipment-prices drift** | Was: fleet block in homepage DOM without `design/v2` slice. **2026-05-16:** removed from `index.html`; isolated on `validation-equipment-prices.html`. | [equipment-prices-quarantine.md](./equipment-prices-quarantine.md); F-EP-HOME; [semantic-locks.md](../semantics/semantic-locks.md) |
| **PNG vs `<main>` index** | Historical: “third include” = prices. **Homepage fixed 2026-05-16:** third `<main>` = cases (`trust-cases-social-proof`). | [section-order.md](../semantics/section-order.md); F-PNG-INDEX |
| **Source blending** | Retired PDF, V1 maps, or `full.png` summaries treated as **verbatim** copy. | [content-authority.md](../semantics/content-authority.md); F-SOURCE-BLEND |
| **Semantic contamination** | V1 strip names (`landing-strip-*`) influence structure or order. | [V2-SECTION-SOURCE-MATRIX.md](../../../V2-SECTION-SOURCE-MATRIX.md); F-V1-BLEND |
| **Invented copy** | Stub sections filled with AI marketing, fake reviews, chats. | [content-authority.md](../semantics/content-authority.md); F-STUB-FILL, F-COPY-AI |
| **DOM drift** | Edits chained off **current** `index.html` instead of **`NN.png`** sequence. | NEXT IMPLEMENTATION RULE; F-DOM-ORDER |
| **Uncontrolled section insertion** | Extra blocks added for “conversion best practices.” | F-SECTION-INSERT |
| **Problem/solution vs FAQ** | Older docs mention `#faq`; current anchor is **`#problem-solution`** — FAQ accordion mindset vs **matrix** mock `05.png`. | [component-rules.md](../implementation-pack/component-rules.md); F-MATRIX-FAQ |
| **Structure under-spec** | **3+3** placeholders vs **6×2** mock for matrix. | [semantic-locks.md](../semantics/semantic-locks.md) entity counts; F-STRUCTURE-SHIMS |
| **Padding rhythm regression** | Global section spacing tweaked during single-screen work; frozen sections **shift**. | [spacing-system.md](../implementation-pack/spacing-system.md); F-PADDING-DRIVEBY |
| **Hero bullet vs trust strip** | Internal inconsistency risk between hero list and lower band (`01.png`). | Pixel + operator before rewriting bullets |
| **Screen 02 ≠ catalog** | Risk of multi-machine framing on **one-machine** section. | L-MACHINE-02; F-FLEET |

---

## Append template

```
## YYYY-MM-DD — short title
- **Seen:** …
- **Impact:** …
- **Fix / doc update:** …
```
