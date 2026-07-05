# FP-0002 V9-06D9P Next Step Recommendation v1

**Date:** 2026-07-05  
**Task:** V9-06D9-P Admin UX QA  
**Verdict:** PARTIAL PASS

## QA outcome

Admin UX after D9-L/M/N/O is **operationally ready** with one open confirmation:

- **OPERATOR_CONFIRMATION_REQUIRED:** Live wp-admin Update on Home #4 with empty Reviews teaser (schema simulation already PASS).

No blockers identified. Frontend regression PASS. Managed pages and operator-review preservation PASS.

## Recommended next phase

**CREATE_V9_06D9Q_REVIEWS_INCLUDE_PLANNING_TASK**

Rationale:

1. `home_reviews_teaser` is optional and unblocks save — next UX gap is the **frontend reviews block** still static/deferred (not ACF-driven include).
2. Reviews include planning is the highest-value follow-up before legal content review or media polish.
3. Legal/native content review (IDs 3, 6–10, 17, 19, 21, 25) remains a **separate** human editorial task — not an admin UX blocker.

## Deferred (not blocking D9-Q)

| Task | When |
|---|---|
| CREATE_V9_06D9Q_LEGAL_NATIVE_CONTENT_REVIEW_TASK | After or parallel to reviews include planning |
| CREATE_V9_06D9Q_OPERATOR_MEDIA_REVIEW_TASK | Optional polish; hero/gallery already seeded D9-K |
| Operator in-browser save confirm | Any time before production handoff |

## Operator action (optional, immediate)

1. Log into `http://shpigovsky.test/wp-admin/`
2. Edit page **Главная** (#4)
3. Confirm: no native editor box; ACF fields visible; Reviews teaser not marked required
4. Click **Update** without filling Reviews teaser — expect success
