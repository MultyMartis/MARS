# Sample Template-Fill Run — Operator Runbook

**NOT:** Automated import · NOT Direct API · NOT launch approval

---

## Command example

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm install

node export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  fixtures/validation-report.export-allowed.fixture.json \
  --template-fill
```

npm script:

```bash
npm run export:template-fill
```

Custom output path:

```bash
node export.js doc.json report.json --template-fill output/my-fill-draft.xlsx
```

---

## Expected output file

| File | Path |
|------|------|
| Default | `tools/exporter-cli/output/triumph-commander-template-fill-draft.xlsx` |

Console should report:

- `Mode: template-fill`
- `Sheet: Тексты (header row 14)`
- `Rows written: <N>`
- `Template source unmodified: true`

---

## Expected written rows

Row model: **one row per keyword × ad** per group (stable sort).

For `triumph-s-tier-draft-v1.json` (fixture path): row count = sum over groups of `max(1, keywords) × max(1, ads)`.

Written columns (verified only):

| Logical | Template header |
|---------|-----------------|
| `groups.group_name` | Название группы |
| `keywords.phrase` | Фраза (с минус-словами) |
| `ads.headline_1` | Заголовок 1 |
| `ads.headline_2` | Заголовок 2 |
| `ads.description` | Текст |
| `ads.landing_url` | Ссылка |
| `ads.display_url` | Отображаемая ссылка |
| `ads.ad_status` | Статус объявления |
| `keywords.status` | Статус фразы |
| Fastlinks | cols 58–60 (`\|\|` joined) |
| Callouts | Уточнения (`\|\|` joined) |

---

## Fail examples

| Condition | Block code |
|-----------|------------|
| Missing header map | `HEADER_MAP_NOT_FOUND` |
| Missing template asset | `TEMPLATE_NOT_FOUND` |
| Sheet **Тексты** absent | `SHEET_MISSING` |
| Map column missing | `UNRESOLVED_VERIFIED_MAPPING` |
| Header row drift | `HEADER_ROW_MISMATCH` |
| Empty document graph | `NO_TEMPLATE_FILL_ROWS` |
| Post-save workbook reopen fails | `INTEGRITY_CHECK_FAILED` |
| Write into merged slave cell | `MERGED_CELL_WRITE` |
| `export_allowed: false` | precheck `EXPORT_NOT_ALLOWED` |

Example — missing report:

```bash
node export.js doc.json missing-report.json --template-fill
# → [BLOCKED] ValidationReport not found
```

---

## Manual review checklist before import

1. Confirm **original** template at `assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx` was **not** modified (mtime/size).
2. Open output copy — sheet **Тексты**, row 14 headers unchanged.
3. Scan rows 16+ — Cyrillic intact, no obvious truncation.
4. Compare metadata block (rows 7–12) — still template defaults; edit manually if needed.
5. Verify status literals acceptable for your Commander version.
6. Inspect fastlink/callout cells — confirm `\|\|` encoding or fix manually.
7. Import in **test** Commander account only.
8. Log UI errors in pack notes — not governance.

---

## Logical draft mode (unchanged)

Without `--template-fill`:

```bash
node export.js doc.json report.json
# → output/triumph-export-draft.xlsx (five logical sheets)
```
