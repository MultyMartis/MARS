# ORCA Ambiguous Problem-Query Policy v1

Machine-readable policy: `ambiguous-problem-query-policy-v1.json`

## ACCEPT

Problem clearly implies a paid specialist or urgent fix (hire/order/urgency + service object).

## ABSTAIN

Problem may be solved DIY or via specialist; insufficient commercial signal.

## REJECT

Educational, reference, DIY, product-only, or out-of-scope service query.

Regression: `tests/run-ambiguous-problem-policy-tests.mjs`
