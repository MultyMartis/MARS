# Transport symbol normalization v0.4

**Phase:** ORCA Commander Import Refinement v0.4  
**Function:** `normalizeTransportText()` in [mapping.js](mapping.js)  
**Applied:** Before sheet1 export, inside `mapTemplateFillRows()` (and group names in `mapDocument()`)

---

## Commander symptom

Reject: *«Можно использовать только буквы … и знаки препинания»* when copy contains Unicode math/dash symbols (e.g. **6×6**).

---

## Rules (deterministic)

| Input | Output | Code point |
|-------|--------|------------|
| `×` | `x` | U+00D7 |
| `–` | `-` | U+2013 |
| `—` | `-` | U+2014 |
| non-breaking space | normal space | U+00A0 |
| repeated whitespace | single space | `collapseWhitespace()` tail |

**Preserved:** Cyrillic letters, ASCII letters/digits, standard punctuation already allowed by Commander.

**Not applied to:** `landing_url`, `fastlink_urls`, `display_url` path (ASCII pipeline separate).

---

## Example (fixture group 05 — вездеход)

| Field | Before | After |
|-------|--------|-------|
| description | `Манипулятор 6×6 для сложного рельефа` | `Манипулятор 6x6 для сложного рельефа` |

---

## Fields normalized on export rows

- `group_name` (after `normalizeGroupName`)
- `keywords.phrase` (after autotarget filter)
- `ads.headline_1`, `ads.headline_2`, `ads.description`
- `extensions.fastlink_titles`, `extensions.fastlink_descriptions`
- `extensions.callouts`

---

## Non-goals

- No AI rewrite / no semantic shortening
- No validation rule changes (SY-* still apply upstream)
- No mutation of source JSON on disk — transport-only in mapped rows

---

## Extension

Add symbols to the replacement table only with Commander import evidence — avoid broad Unicode stripping that could damage Russian copy.
