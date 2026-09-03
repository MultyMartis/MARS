# OPEN-QUESTIONS-STATUS-v1

**Source:** `architecture/ISEO-SALES-DATA-OPEN-QUESTIONS-v1.md`  
**After local schema validation (2026-09-03)**

| ID | Topic (short) | Classification | Notes |
|----|---------------|----------------|-------|
| Q1 | Business semantics / lead identity rules | OPERATOR_DECISION_REQUIRED | Schema supports upsert; product rules not decided here |
| Q2 | Production source forensic / Sheets truth | NEEDS PRODUCTION DATA FORENSIC | No production data touched |
| Q3 | Channel / delivery product rules | OPERATOR_DECISION_REQUIRED / NON-BLOCKING | Outbox mechanism validated; channel policy open |
| Q4 | Ops / release process beyond schema | OPERATOR_DECISION_REQUIRED | Server foundation still separate gate |
| Q5 | Local PostgreSQL runtime for validation | RESOLVED_BY_SCHEMA_TEST | Portable PG 17.11 under MARS-Localhost; empty→migrate→test PASS ×3 |

Do not treat unresolved business questions as schema failures.
