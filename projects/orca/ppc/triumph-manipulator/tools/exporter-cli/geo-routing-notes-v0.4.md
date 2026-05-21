# Geo routing notes v0.4 → superseded by v0.6

**Phase:** ORCA Commander Import Refinement v0.4 (historical) · **current:** [commander-region-fix-v0.6.md](commander-region-fix-v0.6.md)  
**Scope:** Column **52** «Регион» on sheet **Тексты** · template forensic labels only · **no** region ID API

---

## Commander symptom

*«Неуказанные и некорректные регионы заменены значением "Все"»*.

---

## Forensics (v0.4 era)

| Source | Finding |
|--------|---------|
| Header map | `geo.region` → col **52**, header «Регион» |
| Template rows 16–24 | Value `Краснодар` |
| Template rows **25–30** | **Empty** region cell |
| Sheet **Регионы** tree | `Краснодарский край` (row 9755, col 4); `Краснодар` (row 9989, col 5) |
| Triumph JSON | `geo.primary_region`: `Краснодар` (project + campaign) |

**Root cause (v0.4):** Six tail rows had blank col 52 → Commander **Все**. v0.4 also wrote **two-line** parent+city label → still rejected post-import.

---

## v0.4 transport rule (superseded)

| Input `primary_region` | Exported col 52 (v0.4) |
|------------------------|-------------------------|
| `Краснодар` | `Краснодарский край` + newline + `Краснодар` |

**Superseded by v0.6:** single line `Краснодарский край` only — see [commander-region-fix-v0.6.md](commander-region-fix-v0.6.md).

---

## v0.6 transport rule (current)

| All Triumph export rows 16–30 | Col 52 value |
|-------------------------------|--------------|
| Constant | `Краснодарский край` |

Operator `direct.xlsx` evidence: Commander accepts parent krai label without city line.

---

## Limitations (SAFE UNKNOWN)

| Topic | Status |
|-------|--------|
| Region ID columns | **Not implemented** |
| Per-group / multi-campaign geo | Single constant for fixture |
| Excluded regions / bid modifiers | **Skipped** |
| Sheet **Регионы** mutation | **Forbidden** — ZIP byte-preserve |

---

## Human re-import checklist (v0.6)

- [ ] Col 52 rows 16–30 = **Краснодарский край** (one line, no `\n`)
- [ ] No import warning about regions replaced with **Все**
- [ ] Sheet **Регионы** unchanged vs template (ZIP forensics)
