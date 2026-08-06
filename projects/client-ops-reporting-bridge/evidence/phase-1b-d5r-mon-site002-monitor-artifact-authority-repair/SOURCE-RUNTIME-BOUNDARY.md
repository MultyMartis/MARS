# SOURCE-RUNTIME-BOUNDARY

Three distinct layers (do not conflate):

| Layer | Path class | State after D5R-MON |
|-------|------------|---------------------|
| Canonical source | `X:\AI MARS\projects\ocpilot\sites\site-002\tools\site-002-post-1c-monitor-runner.ps1` | **REPAIRED** |
| Scheduled runtime checkout | `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo\...` | **NOT DEPLOYED / OLD** (still contains pre-merge default bug) |
| Historical production artifacts | Storage scheduled-monitors / D5 candidate packs | **UNCHANGED** |

## Proof hashes (post-repair)

| Object | SHA256 |
|--------|--------|
| Canonical repaired runner | `722CFF3CAC0E4F2EEABE8BB40807B5290EE35A83A1AB516E89E869511AB51FBE` |
| Runtime checkout runner (unchanged) | `8738D358C5DA6B5BCBDFD355EE6A91278F1B0AF8F370517E8FCFE640D934BF76` |

Hashes differ → runtime not deployed.

## Expected phase end state

`CANONICAL_SOURCE_REPAIRED_RUNTIME_NOT_DEPLOYED`
