# CALLBACK EXECUTION FORENSIC v1

## Harness / demo executions (not real user)

| Exec | Time UTC | Trigger | Outcome | Notes |
|------|----------|---------|---------|-------|
| 21531 | 20:32 | P3D8 Callback Harness WH | unknown_lead | Token mismatch era / pre-sync |
| 21540 | 20:36 | Harness WH | unknown_lead | |
| 21542 | 20:36 | Harness WH | unknown_lead | |
| 21551 | 20:40 | Harness WH | **applied** processed | CLEAN+EVENTS updated; 1 card edit; AnswerCallback **Bad request** (fake query id) |

## Real user executions

| Exec | Time UTC | Trigger | Actor hash | Outcome |
|------|----------|---------|------------|---------|
| 21584 | 20:56:32 | Telegram Trigger | h:518CC34C4C0F | idempotent processed |
| 21585 | 20:56:50 | Telegram Trigger | h:518CC34C4C0F | idempotent processed |

## Node path (real 21585)

Normalize → Auth → Route `/__callback` → Read CLEAN → Handle (idempotent) → IF Mutate false → Append LEAD_EVENTS → Read LEAD_DELIVERIES (**error item**) → Expand (initiator fallback, no msg) → Aggregate → Prepare → Answer Callback Query OK → Capture → Safe Telegram Reply

## Counts

- CLEAN matched rows: full sheet read (~63)
- Matched business lead: 1 (already processed)
- LEAD_DELIVERIES usable copies: **0** (sheet missing)
- Card edits attempted: 0 on real clicks
