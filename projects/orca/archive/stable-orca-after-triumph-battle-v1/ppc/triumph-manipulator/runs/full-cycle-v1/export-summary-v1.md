# Export Summary v1

**Exporter:** `tools/exporter-cli` — ORCA Commander Region Import Fix v0.6 (sheet1 ZIP patch)  
**Command:** `npm run export:sheet1-patch:full-cycle-v1`

## Output (local, not committed)

```
projects/orca/ppc/triumph-manipulator/tools/exporter-cli/output/triumph-sheet1-patch-full-cycle-v1.xlsx
```

Listed in `tools/exporter-cli/.gitignore` (`output/*.xlsx`).

## Transport stats

| Check | Result |
|-------|--------|
| Rows patched | 82 |
| Last data row | 97 |
| Stale rows removed | 36 (rows 98–133) |
| sharedStrings introduced | false |
| sheet2.xml | byte-identical to template |
| sheet3.xml | byte-identical to template |
| Integrity reopen | INTEGRITY_OK |
| Region (col 52, rows 16–97) | Краснодарский край |
| Ad type (col 2) | Текстово-графическое |
| Display URL | short path only (no domain composite) |
| Image URLs in sheet1 | none detected |
| Post-export script | `_validate-full-cycle-v1.js` — all checks passed |

## Validation report binding

Export used live `validation-report.output.json` (document ID match). Fixture `export-allowed` was **not** used for this run.

## Limitations

- Prototype CLI — not production orchestration  
- Commander import behavior depends on Direct UI version  
- Human must confirm fastlink columns and bid fields after import
