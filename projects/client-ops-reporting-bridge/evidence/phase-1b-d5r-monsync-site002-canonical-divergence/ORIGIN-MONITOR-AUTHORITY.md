# ORIGIN-MONITOR-AUTHORITY

## Verdict

`ORIGIN_MONITOR_BASELINE_AUTHORITY_CONFIRMED`

## Authority commit

| Field | Value |
|-------|-------|
| Commit | `af5f3fcae588cdf0631ae7b3a4b7b7d48f404ef6` |
| Subject | ocpilot: refresh SITE-002 monitor baseline to 1737 |
| Parent | `62d82eb66341acfc3dd2e0ee5824a782fa9c13ed` |
| Date | 2026-07-20 22:35:28 +0700 |

## Runtime monitor blob

| Ref | Blob |
|-----|------|
| `af5f3fca:.../monitor-02.py` | `9c0272f6271a666cd50bad501779b8468c03e68c` |
| `origin/mars/canonical-post-recovery:.../monitor-02.py` | `9c0272f6271a666cd50bad501779b8468c03e68c` |

Identity: **EQUAL**. No post-`af5f3fca` origin commit modifies `monitor-02.py`.

## Sufficiency

For dedicated monitor runtime correctness, the required origin state is the single tools file:

`projects/ocpilot/sites/site-002/tools/site-002-prod-post-1c-catalog-onboarding-monitor-02.py`

Documentation/passport/index files also present in `af5f3fca` are **not** required for runtime target rebuild and were intentionally excluded from the MONSYNC commit to avoid unrelated origin import.
