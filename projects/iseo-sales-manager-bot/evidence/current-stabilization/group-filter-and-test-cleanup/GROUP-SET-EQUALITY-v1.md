# GROUP-SET-EQUALITY-v1

## Method

Compute expected ID sets for Audit / SEO / Other / older24 / All using the same AUTHORITATIVE_GROUP_PENDING rules as patched `group_open` and reminder `isTest` exclusion. Compare expected == actual by shared selector (internal set equality).

## Result (`2026-08-26T09-56` / acceptance `10-00`)

| Group | Expected | Actual | Mismatch |
|-------|---------:|-------:|---------:|
| Audit | 14 | 14 | 0 |
| SEO | 1 | 1 | 0 |
| Other | 7 | 7 | 0 |
| older24 | 19 | 19 | 0 |
| All | 22 | 22 | 0 |

`group_set_mismatches = 0`

SEO expected ID set = `{ lead_19fb7df740e51e2… }` only — no Audit/Other/synthetic bleed.

Note: an earlier seteq draft flagged broad name-heuristic “isTest” rows still pending in CLEAN; those are SAFE_UNKNOWN (not archived). Strict **isProven** pending = 0. Production queue excludes broad isTest.
