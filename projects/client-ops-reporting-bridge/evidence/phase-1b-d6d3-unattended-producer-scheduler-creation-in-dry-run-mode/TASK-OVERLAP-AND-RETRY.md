# TASK-OVERLAP-AND-RETRY

- Scheduler overlap: IgnoreNew (do not start new instance if running)
- Scheduler automatic retries: 0
- Producer singleton lock: second acquire rejected (PRODUCER_LOCK_HELD) via lock-probe
- Nonzero policy exit must not authorize retry (RestartCount=0)

Tokens: D6D3_TASK_OVERLAP_DISABLED; D6D3_SCHEDULER_AUTOMATIC_RETRIES_DISABLED; D6D3_SCHEDULER_AND_PRODUCER_OVERLAP_GUARDS_VERIFIED

