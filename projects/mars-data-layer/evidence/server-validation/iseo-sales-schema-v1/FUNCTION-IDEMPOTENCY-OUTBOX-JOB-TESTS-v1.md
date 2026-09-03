# FUNCTION / IDEMPOTENCY / OUTBOX / JOB TESTS-v1

**Suite:** `tests/iseo_sales/04_extended_local_validation.sql`
**Status:** PASS

Covers: register_inbound_event, upsert_lead, change_lead_status, enqueue_delivery, enqueue_job/claim, status transition + audit/event append, idempotent replay, outbox atomicity (DB-only).

```
DO
DO
DO
DO
DO
DO
DO
DO
TEST_OK=tests/iseo_sales/04_extended_local_validation.sql

```
