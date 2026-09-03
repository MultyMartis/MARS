# PERMISSION-TESTS-v1

**Harness:** `03_permissions.sql` + extended role checks  
**Result:** PASS

| Role | Allowed | Denied (proven) |
|------|---------|-----------------|
| iseo_runtime | Intended DML/function path for runtime | DDL; unrelated schema write; not owner/admin |
| iseo_agent | Narrow allowed functions | Arbitrary UPDATE/DELETE business tables |
| iseo_reader | SELECT / read path | Writes |

## Event immutability

Runtime role cannot UPDATE or DELETE domain event rows (`lead_events`) — PASS.

## Cross-schema isolation

`app_seo_content` placeholder: `iseo_runtime` lacks USAGE/CREATE — PASS (structural). Full app schema still future work.
