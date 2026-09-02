# CONSTRAINT-TESTS-v1

**Harness:** `tests/iseo_sales/02_constraints.sql` + `04_extended_local_validation.sql`  
**Result:** PASS (pass2/pass3 after empty reset)

| Case | Expected | Result |
|------|----------|--------|
| Duplicate `(source_system, source_id)` inbound | Reject / no second row | PASS |
| Duplicate stable `lead_id` upsert | Upsert contract (no duplicate lead) | PASS |
| Invalid FK relationships | Rejected | PASS |
| NOT NULL / CHECK violations | Rejected | PASS |

Raw: `_constraints-pass2.log`, extended coverage in `_extended-pass2.log`.
