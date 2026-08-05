# MISSING NAME FAIL-CLOSED v1

## Behavior

1. If `reply_sender_name` missing/invalid or personalization not enabled → **no** customer copy block.  
2. Manager sees warning: нужно задать имя у администратора.  
3. Lead **delivery** to Telegram still proceeds (not a delivery failure).  
4. Never invent name from Telegram display/username.

Harness: P40 / P40b / P40c PASS.
