# FP-0002 V6 → V7 Source Parity

**Date:** 2026-06-24  
**V6 tag:** `fp-0002-v6-final-before-v7-operator-stable-01`  
**V6 commit:** `85a6d654`

## Summary

| Metric | V6 | V7 | Verdict |
|--------|----|----|---------|
| `src/` file count | 77 | 77 | PASS |
| `src/` SHA-256 mismatches | — | 0 | PASS |
| `src/` paths only in V6 | 0 | — | PASS |
| `src/` paths only in V7 | — | 0 | PASS |
| `gulpfile.js` | present | identical copy | PASS |
| `package.json` | v6 metadata | v7 name/version only | EXPECTED |
| `package-lock.json` | v6 name | v7 name only | EXPECTED |

## Excluded from parity comparison (version metadata)

- `README.md` (V7 only)
- `foundation/FP-0002-V7-OPERATIONAL-STATUS.md` (V7 only)
- `foundation/FP-0002-V6-*` copies in V7 (reference docs, not src)
- `reviews/v7-bootstrap/` (parity artefacts)

## Root file note

Automated compare includes `package.json`, `package-lock.json`, and `gulpfile.js` in V7 inventory. `gulpfile.js` is byte-identical. Package files differ only by workspace name/version metadata (`fp-0002-shpigovsky-v7` / `7.0.0`).

## Verdict

```text
Unexpected source differences = 0
SOURCE PARITY = PASS
```
