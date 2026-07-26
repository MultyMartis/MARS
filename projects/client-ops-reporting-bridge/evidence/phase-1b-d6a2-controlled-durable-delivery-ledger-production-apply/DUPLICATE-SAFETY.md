# DUPLICATE-SAFETY

**Token:** `D6A2_DUPLICATE_SUPPRESSION_PRESERVED`

## Production synthetic replay (authorized)

| Item | Value |
|------|-------|
| Replay performed | yes (1) |
| Synthetic event_id | `d6a2a001-27d6-4a2e-bd6a-000000000001` |
| HTTP | 200 |
| Result | `DUPLICATE_SUPPRESSED` / dedupe=`DUPLICATE` |
| Telegram runs on replay | **0** |
| delivery_state after replay | still `SENT` |

## Static path

`Respond Non-First-Seen` does not connect to Telegram or ledger finalizer — duplicates never resend regardless of PENDING/SENT/FAILED.

## Historical

No replay of `c84e29bf-79b1-5aea-98c4-9dc8d651fc96`.
