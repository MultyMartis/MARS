# PRODUCER-TASK-RECONFIRMATION — D6D3B

Token: **D6D3B_PRODUCER_TASK_RECONFIRMED_DISABLED**

| Field | Expected | Observed |
|-------|----------|----------|
| Task | `\MARS_SITE_002_Client_Ops_Producer` | present |
| State | Disabled / not Running | Disabled / not Running |
| Queued instance | none | none (missed runs=0) |
| Last result | 21 | 21 |
| MultipleInstancesPolicy | IgnoreNew | IgnoreNew |
| RestartCount | 0 | 0 |
| ExecutionTimeLimit | PT30M | PT30M |
| Trigger | daily 2026-07-31T13:00:00+07:00 | match |
| Wrapper | runtime-state `...\tmp\run-client-ops-site-002-producer-scheduled.ps1` | match |
| Working directory | producer runtime checkout | match |
| Creation XML hash (D6D3, Enabled) | `ACEBEC444CF5F3F75F8A040EA10C15DE8644F49E535F9EE0EAAA97E58085CEBB` | immutable creation contract |
| Current XML hash (Disabled post-proof) | `9A7D386CF01A05004D115EEB709534603AD4308332DC5065ECA1DA97E741C353` | matches D6D3R poststate |

Distinction: Enabled→Disabled is expected post-proof evolution, **not** material contract corruption.
Ongoing recurrence: **NOT AUTHORIZED**.
