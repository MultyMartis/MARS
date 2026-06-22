# Lifecycle Validator v1

**Script:** `validate-search-ppc-lifecycle.mjs`  
**Status:** `IMPLEMENTED — NOT VALIDATED AT SCALE`

---

## Usage

```bash
node projects/mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs \
  --manifest <project-ppc-state-manifest.json> \
  [--contract contracts/mars-search-ppc-lifecycle-contract-v1.json] \
  [--out-json report.json] \
  [--out-md report.md]
```

**Exit codes:** `0` = READY, `2` = BLOCKED, `1` = usage error

---

## Behavior

1. Read lifecycle contract  
2. Read project state manifest  
3. Resolve required artifacts (filesystem check)  
4. Verify stage prerequisites  
5. Verify operator gates  
6. Detect forbidden downstream artifacts  
7. Detect bypassed stages  
8. Output readiness (JSON + Markdown)  
9. Never fabricate missing evidence  

---

## Synthetic fixtures

| Fixture | Expected |
|---------|----------|
| `state/fixtures/synthetic-blocked-v1.json` | BLOCKED, exit 2 |
| `state/fixtures/synthetic-pre-strategy-v1.json` | READY at SPPC-12, allows SPPC-13 only |

Results: [reports/synthetic-blocked-result-v1.json](../reports/synthetic-blocked-result-v1.json), [reports/synthetic-pre-strategy-result-v1.json](../reports/synthetic-pre-strategy-result-v1.json)
