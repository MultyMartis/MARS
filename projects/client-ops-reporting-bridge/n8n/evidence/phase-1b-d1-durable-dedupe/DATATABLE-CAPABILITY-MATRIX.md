# Data Table Capability Matrix — D1

| Capability | Installed evidence | Result | Load-bearing |
|---|---|---|---|
| Data Table API | OpenAPI + GET /api/v1/data-tables 200 | PROVEN | Yes |
| Create table | POST 201 dedicated table | PROVEN | Yes |
| Get/list rows | GET rows filter by event_id | PROVEN | Yes |
| Insert row | Workflow node + API | PROVEN | Yes |
| Upsert documented | OpenAPI upsertRowRequest | PROVEN (API) | Partial |
| Unique constraint on event_id | OpenAPI column schema has no unique | ABSENT | Yes — sequential only |
| Native atomic CAS | Not proven under concurrency | SAFE UNKNOWN | Yes |
| Workflow node | n8n-nodes-base.dataTable typeVersion 1.1 executed | PROVEN | Yes |
| Persistence across workflow PUT | Table retained across rollback+reapply | PROVEN | Yes |
| Delete table | DELETE 204 during rollback of first attempt | PROVEN | Yes |
| Backup/export | Not proven | SAFE UNKNOWN | No for MVP |
| Extra credentials | Same n8n API key | PROVEN | Yes |
