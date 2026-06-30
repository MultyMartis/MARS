# Campaign Release Gate Spec v1

**Status:** IMPLEMENTED  
**Entry point:** `npm run campaign:release-gate -- --project <id> --package <path> --authority <path> --receipt <path>`  
**Module:** `tools/commander-transport/src/release-gate.mjs`

## Gate inputs (required)

1. `project_id`
2. Frozen semantic authority summary or path
3. Generated package path
4. Operator semantic approval receipt (`OPERATOR_SEMANTIC_APPROVED`)
5. Template contract (loaded automatically)

## Gate checks

- Operator approval receipt valid (no HOLD, timestamp, identity)
- Authority frozen
- Template contract valid
- Template contamination detected (informational if sanitization applied)
- **Actual XLSX** forensic validation per file
- Authority-to-artifact reconciliation
- Checksum manifest verification (when provided)
- Foreign-client contamination scan

## Gate outputs

| Result | Meaning |
|--------|---------|
| `RELEASE_GATE_PASS` | Artifact technically consistent with frozen authority |
| `RELEASE_GATE_FAIL` | Blocking violation — do not import |

## Explicit non-implications

`RELEASE_GATE_PASS` does **not** mean:
- Semantic quality approved by automation
- Commander import completed
- Direct launch approved
