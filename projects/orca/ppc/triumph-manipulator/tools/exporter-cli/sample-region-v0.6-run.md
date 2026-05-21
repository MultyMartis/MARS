# Sample run — Region import fix v0.6

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm run export:sheet1-patch:v0.6
node _validate-v06.js
```

**Output:** `output/triumph-sheet1-patch-region-v0.6.xlsx`

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
| Col 52 rows 16–30 | `Краснодарский край` (single line) |
| Col 52 | no `Все`, no empty, no `\n` |
| Col 2 rows 16–30 | `Текстово-графическое` |
| Col 64–66 | empty |
| Col 49 | short paths |
| Rows 31+ | removed |

---

## Commander re-import checklist

- [ ] No «регионы заменены на Все» warning
- [ ] Col 52 = **Краснодарский край** on all imported data rows
- [ ] Ad type, display paths, fastlinks unchanged from v0.5
