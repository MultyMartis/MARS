# MISSED DAILY REMINDER REPAIR v1

**Phase:** 3H.8

## Defect
Reminder evaluator read obsolete `LEADS` sheet → false `zero_pending` while genuine pending leads existed in `lead_clean_v2`.

## Repair
Retarget Admin CLEAN reads to `lead_clean_v2`; add observability v1.1; preserve exactly-once (no last_window stamp on zero pending).

## Verification
- Failed-window forensic (exec 29969)
- Isolated TEST harness (4/4 deliveries; pass2=0)
- Operator-approved reopen of `REMINDER_PROD_LEAD_A` for next natural 10:00 window
