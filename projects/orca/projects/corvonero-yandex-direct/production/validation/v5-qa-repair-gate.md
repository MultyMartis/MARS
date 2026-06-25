# V5 QA Repair Gate

**Result:** BLOCKED — QA REPAIR INCOMPLETE

**v6 production:** NOT AUTHORIZED

## Checks

| ID | Result | Detail |
|----|--------|--------|
| G-01-no-placeholder-in-repair-package | PASS | Repair package JSON must not introduce new placeholder values |
| G-02-root-cause-documented | PASS | 2464 shared-string index leak documented with reusable fix |
| G-03-career-education-leakage | FAIL | 4 active v5 phrases require EXCLUDE (education/career/employment) |
| G-04-controlled-test-hypothesis | FAIL | 149 controlled phrases lack commercial hypothesis |
| G-05-unique-negative-final-states | FAIL | UNRESOLVED=333 BLOCKING=0 |
| G-06-safe-evidence-specific | FAIL | 333 SAFE decisions still use generic template without phrase-specific proof |
| G-07-no-unresolved-semantic-risks | FAIL | unique_unresolved_after=333 |
| G-08-collision-exact-actions | FAIL | 20 blocking findings still have generic correction field in v5 source |
| G-09-summary-reconciliation | FAIL | v5 collision summary contradiction flagged (semantic_risks_after vs unresolved_count) |
| G-10-generator-regression | PASS | all passed |