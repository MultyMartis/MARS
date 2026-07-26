# REGRESSION-TEST-DESIGN

## Harness

`projects/ocpilot/sites/site-002/tools/site-002-post-1c-monitor-runner-finish-summary-authority-regression.ps1`

## Why side-effect safe

Production runner top-level creates Storage run directories and may probe network on `-DryRun`. Therefore:

- **Do not** dot-source / `-File` execute the production runner for tests.
- Extract pure helpers via PowerShell **AST** (`ParseFile` + `FunctionDefinitionAst`).
- Simulate merge/defaults only.
- Use `%TEMP%` synthetic JSON only.
- No monitor process, no Storage scheduled root writes, no network.

## Static proofs

- Runner parses with 0 errors.
- Helpers present.
- Old pre-merge `$summary.classification = NO_ACTION_REQUIRED` pattern absent.

## Behavioral proofs

Cases A–F / enrichment / next_action / syntax / temp-not-Storage.
