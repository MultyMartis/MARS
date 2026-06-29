# Commander Transport — CT-1/CT-2 Design v1

**Scope:** Safe Commander transport tooling (validation + payload build boundary)  
**Pilot:** Corvonero Search PPC  
**Status:** Implemented — generation not authorized

## Architecture

```text
authority-manifest.json
        │
        ▼
┌───────────────────┐
│ authority-loader  │  SHA-256, role policy, path guard
└─────────┬─────────┘
          ▼
┌───────────────────┐     ┌────────────────────┐
│ template-validator│     │ transport-validator │  CT-3 technical rules
└─────────┬─────────┘     └─────────┬──────────┘
          │                         │
          └────────────┬────────────┘
                       ▼
              validate (default task mode)
                       │
                       ▼ PASS only
              ┌────────────────┐
              │ payload-builder │  CT-2 — per-campaign payloads
              └────────┬───────┘
                       ▼
              ┌─────────────────────────┐
              │ commander-patcher-adapter│  CT-1 — Triumph ZIP patch primitive
              └─────────────────────────┘
```

## Security boundary

| Rule | Enforcement |
|------|-------------|
| Drive `X:` + volume `AI WS` | `filesystem-guard.mjs` |
| Writes only under project root | Approved write root |
| No overwrite by default | `FAIL_IF_OUTPUT_EXISTS` |
| No semantic cache / run state | Forbidden authority roles + path segments |
| No generated XLSX as authority | Loader rejects `.xlsx` roles |
| No Git / network / delete | Adapter + CLI policy |

## Authority boundary

Explicit manifest with frozen file hashes. Allowed roles only. Operator approval state must be `OPERATOR_APPROVED` or `APPROVED`.

Supplemental refs resolved from `transport_config` (`bids_ref`, `display_paths_ref`, `group_negatives_ref`).

## Modes

| Mode | CT-1/CT-2 task |
|------|----------------|
| `validate` | **Allowed** |
| `build-payload` | **Allowed** (after PASS) |
| `generate` | Implemented but **not executed** on real authority |
| `verify-output` | Implemented but **not executed** |

Default CLI without mode: `STOP — EXPLICIT MODE REQUIRED`

## CT-3 validators (in transport-validator)

- 200-phrase group limit (hard stop)
- Region = `Новосибирская область`; organization blank
- Campaign / group / ad / bid / UTM / negatives integrity
- No strategy inference; no auto-split

## Retired prototypes (do not execute)

| Legacy script | Status |
|---------------|--------|
| `.tools/corvonero-commander-review-xlsx-w1-v1.py` | RETIRE_AND_REPLACE |
| `.tools/corvonero-commander-template-recovery-v1.py` | FORENSIC_ONLY / RETIRE_AND_REPLACE |
| `.tools/corvonero-commander-five-campaign-split-v1.py` | RETIRE_AND_REPLACE |
| `.tools/corvonero-commander-import-patch-v1.cjs` | Inspected only; logic reproduced in project-local adapter |

## Known Corvonero failures (current authority)

- `ca-01-specialist-search` — 384 phrases
- `ca-05-direct-service-order` — 201 phrases
- Region policy mismatch in campaign settings
- Missing group negatives authority
- Cross-campaign negatives not applied (warning)

## Example validation command

```powershell
cd "X:\AI MARS\projects\mars-search-ppc-production\tools\commander-transport"
node src/cli.mjs validate --corvonero-frozen `
  --out-json "..\..\pilots\corvonero\CORVONERO-COMMANDER-CURRENT-AUTHORITY-VALIDATION-v1.json" `
  --out-md "..\..\pilots\corvonero\CORVONERO-COMMANDER-CURRENT-AUTHORITY-VALIDATION-v1.md"
```
