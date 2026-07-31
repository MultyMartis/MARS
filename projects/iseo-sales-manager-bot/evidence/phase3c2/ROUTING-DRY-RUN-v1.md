# ROUTING-DRY-RUN-v1

**Phase:** 3C.2

## Evaluation against known website-form metadata

| Expectation | Result |
|-------------|--------|
| Filter #1 matches website-form `from` | **yes** (exact hash parity) |
| Filter adds OPS incoming | **configured yes** |
| Filter moves to Trash | **no** |
| Eligible for production `labelIds` query when incoming present | **yes** |
| Historical Trash message restored/reprocessed | **no** (forbidden) |

## Post-repair observation

A later same-sender website-form message (2026-07-31T11:11:41Z) remained out of Trash long enough for Operational.dev to process and finalize labels after OPS field-loss repairs.
