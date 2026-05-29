# Commander import observations v0

**Source:** First successful ORCA → Commander import loop (human-operated, 2026-05)  
**Evidence type:** Operator session + template forensics + patched XLSX probes  
**NOT:** automated import telemetry · NOT runtime proof

---

## What imported successfully

| Entity | Observation |
|--------|-------------|
| Workbook open | Excel opens patched XLSX without repair dialog (integrity gate PASS) |
| ZIP fidelity | `sheet2.xml`, `sheet3.xml`, rels, styles byte-identical to template |
| Commander import | Campaign structure created — groups, ads, keyword phrases present |
| Cyrillic copy | Headlines, descriptions, landing URLs from ORCA JSON visible post-import |
| Workbook transport | Sheet1-only patch preserves reference sheets (**Регионы**, dictionary) |

---

## What looked broken (pre–v0.1)

| Symptom | Evidence | Probable cause |
|---------|----------|----------------|
| Group names truncated / inconsistent | Commander UI showed short names (e.g. «Ман 1») | **All rows `Номер группы` = 1** in export — Commander merged groups |
| `---autotargeting` rows | Template row 16 col 8 (`template-sheet-index-v0.json` preview) | Autotarget marker inherited when phrase not fully replaced |
| Stale «грузотакси» phrases | Rows 31+ in template | Cleanup cleared cells but **empty** rows still listed in Commander |
| Wrong campaign metadata | Rows 7–12 still had old «грузотакси» URLs and minus lists | Metadata block not overwritten in sheet1 patch v0 |
| Status noise | Cells showed `Draft`, `active` (English) | Unverified literals — dictionary sheet has no status enums |
| Extension readability | Fastlinks joined with `||` | v0 combined-cell encoding — acceptable transport, manual polish in Commander |

---

## UI observations (operator)

- Commander lists **all template data rows** even when cells are empty — structural rows remain until human delete in UI (**SAFE UNKNOWN** for row deletion via XLSX).
- Group tree readability improves when **distinct group numbers** and **full `Название группы`** align.
- Autotarget rows appear when phrase column contains `---autotargeting` or empty phrase inherits autotarget behavior (**probable** — needs re-import confirmation after v0.1).

---

## Commander behavior notes

| Topic | Marking |
|-------|---------|
| New entity mode (empty IDs) | **Verified** intent — IDs cleared on export rows |
| Match type column | **Unsupported** — no dedicated column |
| Campaign name in data table | **Unsupported** — metadata block only |
| Row deletion via XLSX | **SAFE UNKNOWN** — v0.1 clears/masks only |
| Russian status literals | **SAFE UNKNOWN** — v0.1 exports empty status |

---

## Row removal phase (v0 — 2026-05)

**Why added:** Neutralization (v0.1) was **not enough** — Commander still imported leftover structural rows as objects.

**Change:** Default export now **removes** `<row>` nodes 31–133 from `sheet1.xml`; dimension `A6:BZ133` → `A6:BZ30`. See [safe-row-removal-notes-v0.md](safe-row-removal-notes-v0.md).

**Next human import should verify:**

- No tail garbage rows from old «грузотакси» template  
- Five groups still present with full names  
- Excel opens row-clean workbook without repair  

---

## Remaining garbage (post–row-removal expectations)

| Item | Status |
|------|--------|
| Empty structural rows 31–133 | **Removed** in row-clean export — re-verify in Commander UI |
| `ads.ad_type` col 2 | v0.4 wrote `-` → Commander warned; **v0.5** writes «Текстово-графическое» explicitly — see [ad-type-literal-fix-v0.5.md](ad-type-literal-fix-v0.5.md) |
| Combinatorics cols 16–47 | Template defaults — **not mapped** |
| Order number / currency metadata | Template values — not patched |

---

## v0.1 fix verification checklist (human)

- [ ] Re-import `triumph-sheet1-patch-feedback-v0.1.xlsx`
- [ ] Five distinct groups with full names (`01 — …` through `05 — …`)
- [ ] No `---autotargeting` phrases in imported keywords
- [ ] Campaign minus list matches JSON (row 9)
- [ ] Promotion URL = Triumph landing (row 11)
- [ ] Stale rows show `-` or empty — not old «грузотакси» copy

---

## Display URL field (v0.3 — operator-confirmed)

| Topic | Observation |
|-------|-------------|
| Field semantics | «Отображаемая ссылка» = **short path only**, not `domain/slug` composite |
| Max length | ≈ **20** characters |
| Charset | Letters, digits, hyphen — kebab-case ASCII in transport |
| Pre-v0.3 bug | `manipulator-triumph.ru/manipulyator-5-tonn` exported — invalid for Commander |
| v0.3 fix | Exporter writes `manip-5-tonn`, `perevozka-byt`, etc. |

**Human re-import should verify:** col 49 shows short paths; col 48 still has full landing URLs.

---

## Ad type column (v0.5)

| Topic | Observation |
|-------|-------------|
| Commander warning | «Тип объявления» not set on rows 16, 19, 23, 25–30 when col 2 = `-` (v0.4) |
| Dictionary literal | Sheet3 has **Текстово-графическое** / **Графическое** only |
| v0.5 fix | Export rows 16–30 col 2 = **Текстово-графическое**; image cols 64–66 stay empty |
| Popup risk | v0.4 cleared image URLs — literal ad type without image cells should **not** re-trigger creative popup (**human verify**) |

**Human re-import should verify:** no missing ad-type warning; no image/creative popup.

---

## Region column (v0.6)

| Topic | Observation |
|-------|-------------|
| Commander warning | «Неуказанные и некорректные регионы заменены значением "Все"» after v0.4 multi-line export |
| Operator `direct.xlsx` | Col **AZ** / «Регион» = **Краснодарский край** only for group 01 — not city, not two lines |
| v0.4 bug | `Краснодарский край\nКраснодар` and blank tail rows treated as invalid |
| v0.6 fix | All export rows col 52 = **Краснодарский край**; tail rows removed (not left with **Все**) |

See [commander-region-fix-v0.6.md](commander-region-fix-v0.6.md).

**Human re-import should verify:** no region-replaced-with-**Все** warning; col 52 single krai label on rows 16–30.

---

## SAFE UNKNOWN

- Whether Commander accepts empty status cells as «новое» / draft semantics  
- Whether transport mask `-` reduces UI noise vs empty cells  
- Whether autotarget still appears with empty phrase + `Текстово-графическое` ad type  
- Optimal campaign type literal for `search_only` Triumph pack beyond dictionary guess  
