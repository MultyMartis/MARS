# RAW VS UNIQUE VS AUTHORITATIVE COUNT v1

Live proof 2026-08-14 13:12 MSK:

| Measure | Count |
|---|---|
| Raw CLEAN pending ∩ not-test rows | **30** |
| Unique lead IDs (old first-row set) | **10** |
| Authoritative current pending | **10** |
| Duplicate excess rows ignored | **20** |
| Terminal removed (among all resolved keys) | 6 |
| SAFE_UNKNOWN (among all resolved keys) | 2 |
| Test excluded (among all resolved keys) | 68 |
| Archive excluded | 0 |
| Test leaks in eligible | 0 |
| Archive leaks in eligible | 0 |

Authoritative count remained **10** — same as unique first-row set for this snapshot because the 10 candidates already had unanimous pending current-state. The defect class (first-row / historical pending overriding terminal) is still closed by the new contract.
