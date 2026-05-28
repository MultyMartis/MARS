# Export Summary v1.1

**Exporter:** `tools/exporter-cli` — ORCA Commander Region Import Fix **v0.6** (unchanged)  
**Command:** `npm run export:sheet1-patch:full-cycle-v1.1`

## Output (local, not committed)

```
projects/orca/ppc/triumph-manipulator/tools/exporter-cli/output/triumph-sheet1-patch-full-cycle-v1.1.xlsx
```

## Transport stats

| Check | v1 | v1.1 |
|-------|-----|------|
| Rows patched | 82 | **108** |
| Last data row | 97 | **123** |
| Stale rows removed | 36 (98–133) | **10 (124–133)** |
| sharedStrings introduced | false | false |
| sheet2/sheet3 | byte-identical | byte-identical |
| Integrity reopen | INTEGRITY_OK | INTEGRITY_OK |
| Region (col 52) | Краснодарский край | Краснодарский край |
| Ad type (col 2) | Текстово-графическое | Текстово-графическое |
| Post-export script | `_validate-full-cycle-v1.1.js` | all checks passed |

## Validation report binding

Export used live `validation-report.output.json` after v1.1 validation pass.

## Limitations

- Prototype CLI — not production orchestration  
- Commander import behavior depends on Direct UI version  
- Human must confirm fastlink columns and bid fields after import
