# Repeated Daily Attention Event Identity

| Date | run_id | event_id |
|---|---|---|
| 2026-08-08 | mars-20260808-080002-9257427a | e07640ed-2573-57b2-b69c-39aff6885e0e |
| 2026-08-09 | mars-20260809-080002-4eaac9f2 | bc6dbc9f-3df0-570c-872f-f832fb47bb6c |
| 2026-08-10 | mars-20260810-080002-6b8c0191 | e2a44eaf-2bab-5f7d-bfdc-40bda425fb73 |
| 2026-08-11 | mars-20260811-080003-64c62107 | c043a8c1-4005-5a74-a346-6f1c15713894 |
| 2026-08-12 | mars-20260812-080002-ac019969 | 05b0357f-bbad-5f5a-bdc9-56598154ca65 |

Proof:

- 2026-08-08 ≠ 2026-08-09 ≠ 2026-08-10 (run_id and event_id distinct)
- Data Table rows distinct; delivery_state SENT each day
- Same condition (`OFFERS_INPUT_MISSING`) still produces new daily report events
- Replay/idempotency of same run remains covered by dispatch delivered markers + offline regression R15

Gate: `D6G1B_REPEATED_DAILY_ATTENTION_REPORTING_PASS`
