# Sample Template Analysis — Operator Runbook

**Purpose:** Example commands and expected outputs for Commander Template Fidelity v0.  
**NOT:** Production procedure · NOT automated import.

---

## Example command

From repository root (or exporter-cli directory):

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm install
node template-reader.js
```

Optional: explicit template path

```bash
node template-reader.js ../../assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx
```

Stdout-only (no JSON write):

```bash
node template-reader.js --stdout-only
```

npm script:

```bash
npm run template:analyze
```

---

## Sample extracted headers (Тексты, row 14)

| Col | Header (Russian) |
|-----|------------------|
| 5 | Название группы |
| 8 | Фраза (с минус-словами) |
| 10 | Заголовок 1 |
| 11 | Заголовок 2 |
| 12 | Текст |
| 48 | Ссылка |
| 49 | Отображаемая ссылка |
| 56 | Статус объявления |
| 57 | Статус фразы |
| 58–60 | Заголовки / Описания / Адреса быстрых ссылок |
| 67 | Уточнения |
| 68 | Минус-фразы на группу |

Full list: [template-sheet-index-v0.json](template-sheet-index-v0.json) → `sheets[0].probableHeaderRows`.

---

## Sample mapping rows (commander-header-map-v0.json)

```json
{
  "ads.headline_1": {
    "sheet": "Тексты",
    "header": "Заголовок 1",
    "column": 10,
    "status": "verified"
  },
  "keywords.phrase": {
    "sheet": "Тексты",
    "header": "Фраза (с минус-словами)",
    "column": 8,
    "status": "verified"
  },
  "keywords.match_type": {
    "status": "unsupported",
    "safe_unknown": "No dedicated match-type column found"
  }
}
```

---

## Known ambiguities

| Item | Operator action |
|------|-----------------|
| Dual header rows 14–15 | Confirm row 14 is import header in your Commander version |
| Duplicate «Заголовок 1» (cols 10 vs 16+) | Use col 10 for ad text; ignore combinatorics unless needed |
| No `campaign_name` column | Track campaign via metadata block only |
| Fastlinks in cols 58–60 | Inspect live cell format before writing exporter fill logic |
| Prototype XLSX ≠ template XLSX | Do not import prototype output as Commander file without review |

---

## Expected next operator actions

1. Review [template-analysis-report.md](template-analysis-report.md) and [fidelity-notes-v0.md](fidelity-notes-v0.md).
2. Open reference template in Excel — visually confirm row 14 headers match JSON.
3. Mark any drift in pack notes (not governance).
4. Run validation-cli + export.js only when transport draft needed — separate from template analysis.
5. Schedule human Commander test import when template-fill exporter phase is chartered.

---

## Optional: prototype export with header map

When `commander-header-map-v0.json` exists, `workbook-writer.js` loads it automatically and may translate **sheet header row labels** (e.g. `headline_1` → `Заголовок 1` on `ads` sheet). Layout remains five logical sheets — **not** Commander fidelity.

```bash
node export.js ../../schema/instances/triumph-s-tier-draft-v1.json \
  ../../tools/validation-cli/output/validation-report.output.json
```

Check `_meta` sheet for `header_map_loaded: yes`.
