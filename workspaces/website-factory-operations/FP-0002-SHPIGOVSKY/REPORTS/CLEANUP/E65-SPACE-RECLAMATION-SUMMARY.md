# E65 Space Reclamation Summary

| Metric | Value |
|--------|------:|
| Logged OK deletions | **15** |
| Bytes reclaimed (deletion log) | **1,422,479,674** |
| Approx GB | **~1.32 GB** |
| Historical packs created (extra disk) | ~15.6 MB manual-review + ~1.4 MB e29c pack |

## By class

| Class | Approx reclaimed | Notes |
|-------|-----------------:|-------|
| Git worktree e29c-e35 | ~452 MB | After validated bundle/patches |
| E59 + E59-FIX01 + E61 | ~842 MB | After compact DB/manifest pack |
| Persistence export | ~24 MB | Unique files compacted first |
| Source video `.bak` | ~26 MB | Covered by Stable/E63 freezes |
| Pre-E54 junk/empty | ~12 MB | 8 exact paths |
| Comfort JSON `.bak` | ~30 KB | Preserved in pack |

## Not reclaimed (intentional)

- ~116 pre-E54 backup directories (~6.9 GB class) — `MANUAL_REVIEW_REMAINS`
- Preview export (~255 MB) — `KEEP_UNTIL_PRODUCTION`
- Home-freeze export (~0.5 MB) — `KEEP_HISTORICAL`
- Protected freezes (Stable/E63/E58/E53/E64 packs) — untouched

## Net note

E65 prioritized correctness over GB KPI. Largest remaining reclaim opportunity is the deferred pre-E54 set, requiring deeper DB/asset uniqueness proofs in a later charter.
