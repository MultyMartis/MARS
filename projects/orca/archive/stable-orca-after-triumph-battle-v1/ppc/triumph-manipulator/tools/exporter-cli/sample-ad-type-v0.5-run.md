# Sample run — Ad type literal fix v0.5

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm run export:sheet1-patch:v0.5
```

**Output:** `output/triumph-sheet1-patch-ad-type-v0.5.xlsx`

---

## Expected console signals

- `Rows patched (sheet1.xml): 15`
- `Row removal mode: true`
- `Last export row: 30`
- `Stale rows removed: 103` (template tail)
- `Integrity: INTEGRITY_OK`
- `ZIP preserve check: PASS`
- `sheet2.xml` / `sheet3.xml`: byte-identical

---

## Spot-check (sheet1.xml)

| Check | Expected |
|-------|----------|
| Col 2 rows 16–30 | `Текстово-графическое` |
| Col 64–66 rows 16–30 | empty (no `direct.yandex.ru/images`) |
| Col 12 / descriptions | no `×` (normalized to `x`) |
| Col 49 display URL | short paths (`manip-5-tonn`, …) |
| Rows 31+ | removed |

---

## Commander re-import checklist

- [ ] No «Тип объявления» missing-column warning
- [ ] No image/creative import popup
- [ ] Five groups, fastlinks, display paths unchanged from v0.2–v0.4
