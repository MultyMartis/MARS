# Campaign Differential Validation Spec v1

**Status:** IMPLEMENTED  
**Module:** `tools/commander-transport/src/differential-validator.mjs`

## Purpose

Compare frozen authority / previous package / new package and classify differences.

## Change types

- `EXPECTED_GENERATION_CHANGE`
- `EXPECTED_VERSION_CHANGE`
- `EXPECTED_METADATA_CLEAR`
- `SEMANTIC_CHANGE`
- `STRUCTURAL_CHANGE`
- `UNEXPECTED_CHANGE`

## Hotfix mode (V2.6 → V2.6.1)

Allowed: file version, timestamps, checksums, manifest refs, E9 clear.  
Forbidden: phrase, ad, bid, URL, region changes.

## Usage

```javascript
import { differentialValidate } from './differential-validator.mjs';
await differentialValidate(previousXlsx, currentXlsx, { mode: 'hotfix' });
```
