# Commander Template Contract v1

**Status:** IMPLEMENTED  
**Machine-readable:** `tools/commander-transport/contracts/commander-template-contract-v1.json`

## Template identity

- Path: `projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx`
- SHA-256: `1112793a888ac2e0762317fa0bf728a116e36a143fc72fa0f5fe729c56c3f1fa`
- **Structurally reusable; semantically contaminated until sanitization**

## Key metadata cells (Тексты sheet)

| Cell | Field | Classification |
|------|-------|----------------|
| E7 | campaign_type | MAY_PRESERVE |
| E9 | campaign_negatives | MUST_CLEAR (default) |
| E10 | optimize_text | MUST_SET |
| E11 | promotion_url | MUST_CLEAR |
| E12 | organization | MUST_CLEAR |

## Contamination signatures

Stale Triumph values: `ремонт`, `запчасти`, `эвакуатор` (E9); `manipulator-triumph.ru`; org ID `29500847237`.

## Consumers

- `template-sanitizer.mjs`
- `artifact-xlsx-validator.mjs`
- `release-gate.mjs`
- `template-validator.mjs` (SHA + structure)
