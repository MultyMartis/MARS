# Fidelity Notes v0 — Commander Template

**Phase:** ORCA Commander Template Fidelity v0  
**Scope:** Documentation of current fidelity level only.

---

## Current fidelity level

| Layer | Level | Description |
|-------|-------|-------------|
| Template introspection | **Done (v0)** | Sheets, header row, metadata block indexed locally |
| Logical → template header map | **Partial** | 22 verified, 1 probable, 2 unsupported (see JSON) |
| Prototype export layout | **Low** | Five logical sheets; English/lowercase logical keys |
| Commander workbook shape | **Not implemented** | No write into `Тексты` row 16+ cell positions |
| Import confidence | **None claimed** | Human must validate in Commander test account |

**Summary:** Fidelity v0 is **analysis + mapping foundation**, not production Commander compatibility.

---

## What blocks real Commander import confidence

1. **Sheet structure** — Commander expects `triumph-manipulator-commander-template-v0.xlsx` layout; prototype produces different workbook shape.
2. **Row generation model** — ORCA hierarchical entities vs flat combined rows in **Тексты**.
3. **Unsupported fields** — `keywords.match_type`, `campaigns.campaign_name` (as column), negatives export in prototype v0.
4. **Extension attachment** — Combined columns vs one-row-per-extension in prototype.
5. **No roundtrip test** — No human import diff recorded in this phase.
6. **Status enum literals** — «Статус объявления» / «Статус фразы» values not verified against live Commander.

---

## Unsupported features (explicit)

- Auto-import / Direct API upload
- Template cell-fill export (clone-and-fill mode)
- Multi-template adapters
- Match type column mapping
- Campaign name as data-table column
- Combinatorics / mobile ad / app promotion columns
- Geo ID resolution via **Регионы** tree automation

---

## Required future checks (human-operated)

| # | Check |
|---|-------|
| 1 | Export one fixture group from ORCA JSON → fill template positions (future phase) |
| 2 | Import in Commander **test** account; capture UI errors |
| 3 | Verify draft/active literals in «Статус объявления» |
| 4 | Confirm fastlink combined cell delimiter format |
| 5 | Confirm phrase-level match encoding when no match column |
| 6 | Diff re-export from Commander vs ORCA source JSON |

---

## Why human review is still mandatory

- Template is **transport reference**, not SoT ([commander-template-contract-v1.md](../../exporter/commander-template-contract-v1.md)).
- Hidden formatting, merges, and Commander version drift are **SAFE UNKNOWN**.
- Exporter prototype remains **transport-only** — no semantic rewriting, no launch approval.
- This phase produces **artifacts for operators**, not autonomous pipeline proof.

---

## Related

- [template-analysis-report.md](template-analysis-report.md)  
- [commander-header-map-v0.json](commander-header-map-v0.json)  
- [future-expansion-notes-v0.md](future-expansion-notes-v0.md)
