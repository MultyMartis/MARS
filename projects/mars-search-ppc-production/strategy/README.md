# MARS Search PPC — Strategy Layer (Wave 4)

**Status:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED`  
**Stages:** SPPC-12 (Dated Analytical Pack), SPPC-13 (AI PPC Strategist)

Wave 4 consumes published ORCA semantic packs and MIG evidence. It does **not** duplicate ORCA semantic execution, import campaigns, or generate Commander files.

## Layout

| Path | Role |
|------|------|
| `contracts/` | Human-readable contracts |
| `schemas/` | JSON Schema for pack, strategy, authority matrix |
| `runtime/lib/` | Builder, strategist, validators, frameworks |
| `runtime/cli/` | Gated CLI (`strategy-ppc.mjs`) |
| `fixtures/` | Test fixtures (complete, blocked, provisional) |
| `tests/` | Fixture tests, bypass audit, E2E, live model |
| `reports/` | Run outputs (uncommitted live results excluded) |

## Entry points

```bash
node projects/mars-search-ppc-production/strategy/runtime/cli/strategy-ppc.mjs pack --manifest <path> --evidence-dir <dir>
node projects/mars-search-ppc-production/strategy/runtime/cli/strategy-ppc.mjs strategy --pack <pack.json> --manifest <path>
node projects/mars-search-ppc-production/strategy/tests/run-strategy-fixture-tests.mjs
node projects/mars-search-ppc-production/strategy/tests/run-wave4-bypass-audit.mjs
node projects/mars-search-ppc-production/strategy/tests/run-synthetic-e2e.mjs
```

## Authority

Only manifest-registered artifacts with `PRODUCTION AUTHORITY` or `APPROVED EVIDENCE` may drive production strategy. Missing Paid SERP blocks full pack (`W4-D5`).
