# CORVONERO — РСЯ operator review checklist v0.2

**Pack:** Import Candidate v0.2  
**Campaign:** `CORVONERO-RSY`  
**Upload-ready:** NO  
**Launch approved:** NO

Passing a review row does not authorize Direct upload.

| ID | Check | Current mark | Area |
| --- | --- | --- | --- |
| OR-01 | Confirm one-campaign fallback: CORVONERO-RSY | OPERATOR_TO_CONFIRM | Structure |
| OR-02 | Confirm budget: 50 000 ₽ | OPERATOR_TO_CONFIRM | Budget |
| OR-03 | Confirm strategy: payment for leads / conversions | OPERATOR_TO_CONFIRM | Strategy |
| OR-04 | Confirm conversion goals: form + calls | OPERATOR_TO_CONFIRM | Goals |
| OR-05 | Confirm exact Direct goal names / IDs | CHECK_REQUIRED | Goals |
| OR-06 | Confirm exact campaign type | CHECK_REQUIRED | Campaign |
| OR-07 | Confirm whether Direct import format supports these settings | CHECK_REQUIRED | Import format |
| OR-08 | Confirm exact LOCAL geography | CHECK_REQUIRED | Geo |
| OR-09 | Confirm exact REMOTE geography and exclusions | CHECK_REQUIRED | Geo |
| OR-10 | Review all 10 groups | OPERATOR_TO_REVIEW | Groups |
| OR-11 | Review all ad candidates | OPERATOR_TO_REVIEW | Ads |
| OR-12 | Review UTM | OPERATOR_TO_REVIEW | UTM |
| OR-13 | Review exclusions | OPERATOR_TO_REVIEW | Exclusions |
| OR-14 | Create images separately | NOT_DONE / SEPARATE_CHARTER | Images |
| OR-15 | Upload images manually later | NOT_DONE / MANUAL_LATER | Images |
| OR-16 | Perform landing/legal live-check before launch | NOT_RESCANNED_IN_THIS_TASK | Landings/legal |
| OR-17 | Approve import package generation v1 | NOT_GRANTED | Next charter |
| OR-18 | Approve Direct import | NOT_GRANTED | Upload |
| OR-19 | Approve launch | NOT_GRANTED | Launch |
| OR-20 | Map budget 50 000 ₽ to exact Direct field (daily/weekly/monthly) | CHECK_REQUIRED | Budget |
| OR-21 | Confirm utm_campaign=corvonero_rsy without changing Search UTM policy | OPERATOR_TO_REVIEW | UTM |
| OR-22 | Confirm weak TEST groups remain included with lower exposure | OPERATOR_TO_CONFIRM | Priority |

## Open checks before true import-ready status

1. One-campaign fallback `CORVONERO-RSY` confirmed in cabinet workflow.
2. Budget 50 000 ₽ mapped to the actual Direct budget field/period.
3. Strategy intent (payment for leads / conversions) mapped to exact Direct settings.
4. Goals form + calls mapped to exact Direct/Metrica names and IDs.
5. Campaign type confirmed.
6. Direct import format confirmed to support campaign/group/ad/geo/strategy/goal fields.
7. Exact LOCAL geo approved.
8. Exact REMOTE geo and exclusions approved.
9. All 10 groups reviewed (including TEST/weak).
10. Ad candidates reviewed and turned into final ads in a later charter.
11. UTM approved without changing Search UTM policy.
12. Exclusions reviewed (RSY, not Search minus dump).
13. Images created separately and uploaded manually later.
14. Landing and legal live-check completed.
15. Import package generation v1 approved.
16. Direct import approved.
17. Launch approved.

Until these are closed: **NOT_UPLOAD_READY**.
