# Group Fidelity QA v1

**Date:** 2026-05-29  
**Export:** `triumph-sheet1-patch-launch-ready-v1.4.xlsx`  
**Template SoT:** `triumph-manipulator-commander-template-v1.xlsx`

---

## Automated QA result

| Check | Result |
|-------|--------|
| Groups | **12/12** |
| Distinct group_number (col 6) | **1–12** |
| Region col 52 | **Краснодарский край** on all rows |
| Ad type col 2 (ad rows) | **Текстово-графическое** |
| Group negatives col 68 (first ad / group) | **12/12 present** |
| Autostavka col 53 | `-` (inherited from template row positions) |

**Verdict:** **PASS**

---

## Group settings columns

| Col | Header | Template behavior | v1.4 export |
|-----|--------|-------------------|-------------|
| 5 | Название группы | `NN - Title` | Same (from JSON, normalized) |
| 6 | Номер группы | 1–12 distinct | Same |
| 52 | Регион | Краснодарский край | Patched all rows |
| 53 | Автоставка | `-` (manual) | Inherited from template base per row slot |
| 54 | Ставка | On phrase rows in template sample | On **keyword rows only** (transport split) |
| 68 | Минус-фразы на группу | Minimal in template (2 groups) | Full doctrine + cross-route (syntax-fixed) |

---

## Expected diffs vs template (by design)

| Col | Reason |
|-----|--------|
| 1 | Transport split: empty / `+` vs template `-` mask |
| 54 | Bids on keyword rows, not ad rows (v1.2+ model) |
| 68 | Expanded cross-negative matrix vs template calibration sample |

These diffs do **not** change ads, phrases, URLs, or bid values — only transport row layout and negative syntax.

---

## Per-group negative sample (v1.4 — no wildcards)

| Group | Sample tokens (truncated) |
|-------|---------------------------|
| 01 — 5 тонн | `-3 тонны -10 тонн … -бытовка -бытовки -перевозка контейнеров …` |
| 02 — бытовки | `-купить бытовку -аренда бытовки -перевозка контейнеров …` |
| 03 — стройматериалы | `-оптом кирпич -перевозка бытовок …` |
| 12 — заказать | `-купить манипулятор -вакансии … -бытовка -бытовки …` |

Full cells verified: `commander_negative_syntax_pass`, `no_wildcard_negatives`.

---

## Human spot-check (required)

- [ ] 12 groups with full names visible in Commander  
- [ ] No `---autotargeting` garbage phrases  
- [ ] Group negatives accepted without syntax error  
- [ ] Region not replaced with «Все»  
