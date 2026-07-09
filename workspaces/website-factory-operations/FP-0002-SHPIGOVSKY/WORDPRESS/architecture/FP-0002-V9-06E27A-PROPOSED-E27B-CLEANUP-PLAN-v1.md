# FP-0002 V9-06E27A Proposed E27B Cleanup Plan v1

**Status:** PLAN ONLY — not executed in E27A  
**Evidence:** `validation/v9-06e27a-obsolete-pages-cleanup-read-only-audit/proposed-e27b-cleanup-plan.json`

| Batch | Operation | Objects | Risk | Needs approval | Notes |
|---|---|---|---|---|---|
| A | trash | #9, #10, #17, #21, #25 | LOW-MEDIUM | YES | No menu/front/privacy dependency |
| B | operator_decision | #6, #7, #8 | HIGH | YES | Resolve page vs service CPT + menu #6 |
| C | redirect_later | `/privacy-policy-page/` → `/privacy-policy/`; `/glavnaya/` → `/` | MEDIUM | YES | After Batch A trash or alongside |
| D | leave | 33 objects | — | — | Canonical, demo, placeholders, must-not-touch |

## E27B proposed commands (future, if approved)

```text
wp post delete 9 --force=0
wp post delete 10 --force=0
wp post delete 17 --force=0
wp post delete 21 --force=0
wp post delete 25 --force=0
```

Batch B requires explicit operator charter before any trash on pages #6–#8.
