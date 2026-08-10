# LIVE MIXED CARD EVIDENCE — Phase 3H.7.3.1

At: `2026-08-10T10:21:31.827Z`

## Operator observations
- One acceptance lead: full canonical production card
- One acceptance lead: Spam → Reopen → Spam with correct Russian acknowledgements
- One acceptance lead: reduced/status-only card (pending fields + returned-to-processing metadata)

## Code evidence
- Handle Callback Action still contains `buildFinalCard` reduced renderer: **true**
- Reduced renderer confirmed (status + client/site/service/request, no full production body): **true**

## Alias matrix (sanitized)
- **REAL_REOPEN_A** suffix=6e4c68e4 status=pending auth=4 post_parity_terminal=0 likely_reduced=false
- **REAL_REOPEN_B** suffix=259d186f status=pending auth=4 post_parity_terminal=0 likely_reduced=false
- **REAL_REOPEN_C** suffix=d0f1e764 status=spam auth=4 post_parity_terminal=0 likely_reduced=false
