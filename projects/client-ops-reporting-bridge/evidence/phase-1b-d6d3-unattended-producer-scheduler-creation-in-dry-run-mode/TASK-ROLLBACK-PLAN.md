# TASK-ROLLBACK-PLAN

Documented only; executed disable already performed after proof.

1. Disable-ScheduledTask `MARS_SITE_002_Client_Ops_Producer`
2. Confirm not Running
3. Delete only that task if full rollback required
4. Preserve producer runtime checkout
5. Preserve/archive sanitized runtime-state
6. Do not touch monitor task
7. Do not alter Client Ops production

Token: D6D3_TASK_ROLLBACK_PLAN_DEFINED

