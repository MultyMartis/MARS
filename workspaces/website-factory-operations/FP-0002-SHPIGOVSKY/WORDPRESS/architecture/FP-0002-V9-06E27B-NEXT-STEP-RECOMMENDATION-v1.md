# FP-0002 V9-06E27B Next Step Recommendation v1

**Wave:** V9-06E27B  
**Date:** 2026-07-09

## Recommended next phase

**CREATE_V9_06E27C_PAGE_SERVICE_OWNERSHIP_DECISION_TASK**

## Rationale

E27B completed Batch A low-risk obsolete cleanup (5 pages trashed). Ownership debt remains unresolved for pages **#6**, **#7**, **#8** — each conflicts with a service CPT at the same public path (`/uslugi/zavisimosti/`, `/uslugi/psihicheskoe-zdorovie/`, `/uslugi/rasstroystva-pischevogo-povedeniya/`). Page #6 is also linked from the Primary menu.

E27C should produce an operator decision on page vs service CPT ownership before any further trash or redirect work on those routes.

## Deferred (not next)

- **CREATE_V9_06E28_FINAL_WORDPRESS_READINESS_QA_TASK** — after E27C ownership resolution
- Batch C redirect candidates (`/privacy-policy-page/`, `/glavnaya/`) — not needed post-trash for privacy-page; glavnaya alias remains informational only
