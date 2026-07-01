# Search PPC campaign architecture standard v1

**Implementation:** `campaign-architecture-validator.mjs`

## Rules

| Check | Severity |
|-------|----------|
| Duplicate group ID | HARD_FAIL |
| Group above max size (default 30) | WARNING |
| Empty group | HARD_FAIL |
| Single phrase without justification | OPERATOR_REVIEW |
| Mixed intent in one group | HARD_FAIL |
| Overlapping duplicate phrases | HARD_FAIL |
| Service-family inconsistency | WARNING |
| Forbidden generic ad text | HARD_FAIL |
| Generic ad reuse >3 | WARNING |

## Landing alignment

- All groups must map to exactly one landing page unless explicit exception documented
- One group → two landing pages without exception: HARD_FAIL

## Corvonero fixture

71 groups, 10 campaigns — `CORVONERO-CAMPAIGN-GROUP-TO-LANDING-MAP-v1.json`
