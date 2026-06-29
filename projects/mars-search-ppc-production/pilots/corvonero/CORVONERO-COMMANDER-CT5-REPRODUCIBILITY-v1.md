# CORVONERO COMMANDER CT-5 REPRODUCIBILITY v1

**Verified:** 2026-06-30

## Run directories

| Role | Path |
|------|------|
| Original | `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-COMMANDER-CT5-FINAL-2026-06-30` |
| Repro | `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-COMMANDER-CT5-REPRO-CHECK-2026-06-30` |

## Count comparison

| Metric | Original (5 files) | Repro (5 files) |
|--------|-------------------|-----------------|
| Campaigns | 5 | 5 |
| Groups | 21 | 21 |
| Keyword rows | 833 | 833 |
| Primary ads | 21 | 21 |
| Groups over 200 | 0 | 0 |

## Hash comparison

Binary SHA-256 differs for all five workbook pairs (ZIP package metadata timestamps on rebuild).

**NORMALIZED WORKBOOK CONTENT: IDENTICAL**

All populated cells, metadata values, region (`Новосибирская область`), organization blank, negatives, URLs and UTM parameters match pairwise across original and repro sets.

## Ten-file forensic re-verification

All ten XLSX files pass: header row 14, 78 columns, bids, callouts, sitelinks omitted, no utm_term, no `{keyword}`, forbidden organization ID count 0.

## Verdict

**PASS** — semantic reproducibility confirmed; binary drift is harmless ZIP metadata only.
