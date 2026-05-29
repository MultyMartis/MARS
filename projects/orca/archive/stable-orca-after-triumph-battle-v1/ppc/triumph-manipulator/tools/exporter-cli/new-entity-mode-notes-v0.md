# New entity mode — Commander import notes v0

**Phase:** ORCA Commander Template Cleanup + New Entity Mode v0  
**Default:** `new_campaign_mode = true` (CLI: default on; disable with `--preserve-commander-ids`)

---

## Why old IDs are dangerous

Commander import treats populated **ID** columns as references to **existing** entities:

| Column (row 14) | Logical key | Col | Status |
|-----------------|-------------|-----|--------|
| ID группы | `groups.group_id` | 4 | **Verified** |
| ID фразы | `keywords.phrase_id` | 7 | **Verified** |
| ID объявления | `ads.ad_id` | 9 | **Verified** |

If the template still carries IDs from a prior Triumph export (e.g. `5741811865`, `205741811865`), importing new ORCA copy may:

- **Update** old ads/phrases instead of creating new ones  
- **Merge** into wrong groups  
- Fail silently with partial updates  

**Evidence:** [template-sheet-index-v0.json](template-sheet-index-v0.json) row 16 preview shows non-empty ID cells from transport template.

---

## New import semantics (v0)

When **new-campaign mode** is on:

1. **Do not** write `ads.ad_id` from ORCA JSON (even if present in document).  
2. **Clear** verified ID columns on every **exported** row (16 … 16+N−1).  
3. **Clear** ID + PPC writable columns on **stale** rows (16+N … last data row).  
4. Commander should treat rows as **new entity candidates** on import (operator-confirmed).

This expresses **fresh import intent** — not a guarantee Commander will create new entities (**SAFE UNKNOWN** until test-account import).

---

## Commander collision risks

| Risk | Mitigation (v0) |
|------|-----------------|
| Stale row IDs survive | Stale-row neutralization clears ID cells |
| Stale row text survives | Writable PPC columns blanked |
| Exported row keeps template ID | ID cleared after content patch |
| Duplicate group names with old IDs | Names from ORCA JSON; IDs empty — **human** must verify group strategy |
| Campaign-level ID in metadata | No verified `campaigns.campaign_id` column — **SAFE UNKNOWN** |

---

## Probable / SAFE UNKNOWN entity columns

| Header (row 14) | Assessment |
|-----------------|------------|
| Номер группы (col 6) | **Probable** transport sequence — not cleared in v0 (no verified header-map entry) |
| Доп. объявление группы (col 1) | **Probable** row-shape marker — not cleared |
| Мобильное объявление (col 3) | **Probable** — not cleared |
| Campaign ID in metadata block | **SAFE UNKNOWN** — metadata rows 7–12 not modified in v0 |
| Internal Commander row keys | **SAFE UNKNOWN** — hidden cells not inspected |

---

## CLI overrides (debug / exceptional)

| Flag | Effect |
|------|--------|
| `--preserve-commander-ids` | Legacy behavior: may write `ad_id` from JSON; no ID clear on export rows |
| `--no-new-campaign-mode` | Skip ID clear on exported rows only |
| `--no-cleanup` | Skip stale-row neutralization |

**Default production path for new Triumph campaigns:** no flags (cleanup + new-entity on).

---

## Human operator checklist

- [ ] Confirm ID columns empty on sample rows before Commander import  
- [ ] Confirm stale rows (below export block) have no old phrases/URLs  
- [ ] Confirm metadata block (rows 7–12) still matches intended campaign settings  
- [ ] Import on **test** account first if available  
- [ ] Reconcile Commander result back to ORCA JSON manually  

**NOT:** Direct API sync, auto-import, orchestration, runtime platform.
