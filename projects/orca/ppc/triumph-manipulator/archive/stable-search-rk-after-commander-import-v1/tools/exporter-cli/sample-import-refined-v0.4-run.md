# Sample run — Commander import refinement v0.4

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm run export:sheet1-patch:v0.4
```

**Output:** `output/triumph-sheet1-patch-import-refined-v0.4.xlsx`

---

## Expected console signals

- `Rows patched (sheet1.xml): 15`
- `Row removal mode: true`
- `Stale rows removed: 103` (template tail)
- `Integrity: INTEGRITY_OK`
- `ZIP preserve check: PASS`
- `sheet2.xml` / `sheet3.xml`: byte-identical

---

## Spot-check (Excel)

| Row | Col 52 (Регион) | Col 64 (Изображение) | Col 2 (Тип) | Col 12 (Текст) |
|-----|-----------------|----------------------|-------------|----------------|
| 16 | Краснодарский край + Краснодар | empty | `-` | no `×` in 6x6 group row 30 |
| 25 | same geo lines | empty | `-` | was empty geo + image URL in template |
| 30 | same geo lines | empty | `-` | `6x6` not `6×6` in description |

---

## Commander re-import checklist

- [ ] No popup about images/creatives in import data
- [ ] No warning about regions replaced with **Все**
- [ ] No reject on invalid symbols for **6x6** copy
- [ ] Five groups, fastlinks, display paths still valid (v0.2–v0.3 preserved)
