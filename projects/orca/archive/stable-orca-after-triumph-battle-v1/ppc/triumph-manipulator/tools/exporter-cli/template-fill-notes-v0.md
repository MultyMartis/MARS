# Template-Fill Export Notes v0

**Phase:** ORCA Commander Template-Fill Export Prototype v0  
**Posture:** Local human-triggered clone-and-fill · **NOT** production-safe · **NOT** guaranteed Commander import

---

## Current fidelity level

| Capability | Status |
|------------|--------|
| Clone real `triumph-manipulator-commander-template-v0.xlsx` | **Yes** — source file never modified |
| Write into sheet **Тексты** from row 16 | **Yes** |
| Use verified columns from `commander-header-map-v0.json` | **Yes** — fail-closed if missing |
| Preserve template metadata rows 1–15 | **Yes** — exact mapped cells from row 16 only (no range clear) |
| Commander import success | **NOT claimed** — experimental draft only |

**Summary:** Higher structural fidelity than logical multi-sheet draft; still **transport-only** and **human-reviewed**.

---

## What is truly Commander-compatible

- Workbook shell: same 3 sheets as reference template (**Тексты**, **Регионы**, **Словарь значений полей**)
- Data table headers: row 14 literals unchanged
- Column positions: verified map columns (group name, phrase, headlines, text, link, display link, statuses, extensions)
- UTF-8 Cyrillic text written as string cell values

---

## What still requires manual editing

| Item | Reason |
|------|--------|
| Campaign metadata block (rows 7–12) | Not overwritten in v0 — still template examples |
| Campaign / group IDs | Commander IDs from template examples may remain in unmapped columns on untouched rows |
| Match type | No verified column — phrase copied verbatim only |
| Status literals (`Draft`/`Active` vs Russian) | **SAFE UNKNOWN** — may need operator adjustment before import |
| Fastlink / callout combined cells | Joined with `\|\|` delimiter — may not match Commander’s native encoding |
| Combinatorics, bids, regions, app promotion cols | Untouched |
| Row pairing flags («Доп. объявление группы» col 1) | Not set in v0 |

---

## Unsupported columns (intentionally untouched)

- `keywords.match_type` — unsupported in header map
- `campaigns.campaign_name` — no data-table column
- Geo tree (**Регионы** sheet)
- Combinatorics columns 16–47
- RSYA, retargeting, bidding, schedule, device modifiers
- Hidden / macro-driven logic

---

## Fastlink / callout encoding (v0)

Per ad, on each keyword×ad row:

| Column | Encoding |
|--------|----------|
| Заголовки быстрых ссылок | `title1\|\|title2\|\|…` |
| Описания быстрых ссылок | `desc1\|\|desc2\|\|…` |
| Адреса быстрых ссылок | `url1\|\|url2\|\|…` |
| Уточнения | `callout1\|\|callout2\|\|…` |

**SAFE UNKNOWN:** Whether Commander accepts `\|\|` on import — verify in test account.

---

## Why import is still experimental

- **NOT production-safe.**
- **NOT guaranteed Commander import success.**
- No human roundtrip test recorded in this phase.
- Template example rows may remain in unmapped columns below the written row span.
- Exporter does not validate symbol limits or Direct business rules at write time.

---

## Fail-closed protections

Export aborts (exit 1) when:

- Template or header map missing
- Sheet **Тексты** missing
- Required verified mapping unresolved
- Header row 14 mismatch vs map
- Zero template-fill rows from document
- Original template file mutated during run
- Post-save integrity reopen fails (`INTEGRITY_CHECK_FAILED`)
- Safe-write violation (merged cell, metadata row, formula cell)

See [xlsx-integrity-notes-v0.md](xlsx-integrity-notes-v0.md).

---

## Related

- [sample-template-fill-run.md](sample-template-fill-run.md)  
- [template-analysis-report.md](template-analysis-report.md)  
- [fidelity-notes-v0.md](fidelity-notes-v0.md)
