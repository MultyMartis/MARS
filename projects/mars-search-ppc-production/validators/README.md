# MARS Search PPC Lifecycle Validator v1 (Wave 1)

Read-only lifecycle enforcement. Never fabricates missing evidence.

## Commands

```bash
# Primary validator (wraps runtime engine)
node projects/mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs <manifest>

# CLI (status, can-start, transition dry-run, report)
node projects/mars-search-ppc-production/runtime/cli/search-ppc.mjs status <manifest>
node projects/mars-search-ppc-production/runtime/cli/search-ppc.mjs can-start <manifest> <stage-id>
node projects/mars-search-ppc-production/runtime/cli/search-ppc.mjs transition <manifest> <stage-id> <status> --dry-run
node projects/mars-search-ppc-production/runtime/cli/search-ppc.mjs report <manifest>
```

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | READY / transition allowed |
| 2 | BLOCKED |
| 1 | Error (missing args, invalid JSON) |

## Synthetic tests

```bash
node projects/mars-search-ppc-production/runtime/tests/run-synthetic-matrix.mjs
```

## Wave 1 status

`IMPLEMENTED — OPERATOR REVIEW REQUIRED` — not yet mandatory at all MIG/ORCA/Campaign CLIs (Wave 1 W1-04 partial).
