# CORVONERO Commander Transport — CT-1/CT-2 Synthetic Validation v1

**Date:** 2026-06-29  
**Runner:** `npm test` in `tools/commander-transport/`

## Result

**Synthetic validation: PASS** (21/21 tests)

## Fixture coverage

| Fixture | Expected |
|---------|----------|
| `valid-synthetic` | PASS |
| `invalid-over-200` | GROUP_PHRASE_LIMIT (201) |
| `invalid-region` | INVALID_REGION_AUTHORITY |
| `invalid-organization` | NONBLANK_ORGANIZATION_POLICY |
| `invalid-negatives` | DUPLICATE, EMPTY, CA05 leak, unknown group ref |
| `invalid-unapproved-ad` | UNAPPROVED_AD |

## Test categories exercised

- Filesystem boundary, volume identity, deprecated drives, UNC, traversal
- Template SHA-256, sheet/header/column, region dictionary
- Authority SHA mismatch, forbidden role
- Phrase limits, duplicates, ads, bids, URL/UTM, region, organization
- Negatives integrity, cross-campaign absent policy
- FAIL_IF_OUTPUT_EXISTS, payload determinism
- Patcher adapter synthetic XLSX (isolated `.tools-test-output/`)

## Not tested

- Network, Yandex Direct, OpenRouter
- Real Corvonero XLSX generation
