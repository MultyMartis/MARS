# Campaign Artifact Validation Spec v1

**Status:** IMPLEMENTED  
**Module:** `tools/commander-transport/src/artifact-xlsx-validator.mjs`

## Source of truth

**Actual final XLSX on disk** — never generator intent, in-memory workbook, or JSON payload alone.

## Required checks

- File opens; sheets `Тексты` + `Регионы` exist
- MUST_CLEAR metadata cells blank (E9, E12 when policy blank)
- Expected counts (groups, phrases, ads) when authority provided
- No duplicate phrases
- Callout serialization (`||` delimiter)
- Clean URL policy (no UTM, query, fragment)
- Stale template contamination (ремонт/запчасти/эвакуатор in E9)
- Foreign client string scan

## Evidence format

```json
{
  "filename": "...",
  "sheet": "Тексты",
  "cell": "E9",
  "raw_value": "...",
  "normalized_value": "...",
  "expected": "MUST_CLEAR"
}
```

## Output status

`ARTIFACT_VALIDATED` or `ARTIFACT_VALIDATION_FAIL` with `SCRIPT_PASS`/`SCRIPT_FAIL`.
