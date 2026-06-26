# FP-0002 Static Demo — Excel Sheet Registry v1

| Sheet | Rows | Columns | Header row | Relevant columns | Hidden | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| Структура | 53 | 5 | 1 | 1 уровень, 2 уровень, 3 уровень, 4 уровень | visible | STRUCTURE |
| Спрос набросок | 53 | 8 | 1 | Запрос, Частотность МСК | visible | SUPPORTING |

## Workbook features

| Check | Result |
| ----- | ------ |
| Formulas | **None** in structure sheet |
| Merged cells | **0** |
| Hidden sheets | **0** (both visible) |
| Hidden rows/columns | **Not detected** |
| Formatting-based hierarchy | **No** — hierarchy via columns 2–5 |
| Hyperlinks | **Present** in column A (display URL); many hyperlink targets are stale/wrong — **registry uses cell display value, not hyperlink target** |
| Notes/comments | **None** |

## Sheet `Структура`

- Column A: canonical URL (with trailing-space typos normalized)
- Columns B–E: levels 1–4 page names
- 52 data rows + header
- Placeholder rows: `Название` (reserved slots), `Специалист 4–6` without URLs

## Sheet `Спрос набросок`

- Search demand only — **not** used for page registry in this pass
- 52 query rows + header
