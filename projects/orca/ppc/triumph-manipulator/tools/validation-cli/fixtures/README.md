# Validation CLI fixtures (v0.1)

## Golden report

**File:** [validation-report.triumph-s-tier.expected.json](validation-report.triumph-s-tier.expected.json)

**Source input:** [triumph-s-tier-draft-v1.json](../../schema/instances/triumph-s-tier-draft-v1.json)

**Why it exists:** Regression reference for deterministic validator output. When rules or the draft fixture change intentionally, regenerate this file and review the diff.

## How to regenerate

From `tools/validation-cli/`:

```bash
set ORCA_VALIDATOR_FIXED_TIMESTAMP=2026-05-20T12:00:00.000Z
node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json
copy output\validation-report.output.json fixtures\validation-report.triumph-s-tier.expected.json
```

(PowerShell: `$env:ORCA_VALIDATOR_FIXED_TIMESTAMP="2026-05-20T12:00:00.000Z"`)

Fixed timestamp keeps `validation_timestamp` stable across machines.

## How to compare (manual v0.1)

1. Run validator with the same `ORCA_VALIDATOR_FIXED_TIMESTAMP` as the fixture.  
2. Diff `output/validation-report.output.json` vs `fixtures/validation-report.triumph-s-tier.expected.json`.  
3. Or strip volatile fields and diff JSON (timestamp only if you used the env var).

**Expected diff on current draft:** none, if validator version and input unchanged.

## Why deterministic output matters

- Operators can trust `git diff` on reports during rule changes  
- Future CI can compare golden vs output without flaky timestamps  
- Failures isolate **logic** changes, not sort order or clock drift  

## Not included

- Automated diff runner (future)  
- CI workflow (future)  
- `launch_allowed` in reports — **never** emitted by validator; human-only launch
