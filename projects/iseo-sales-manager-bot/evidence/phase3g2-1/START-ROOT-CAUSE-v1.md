# `/start` root cause — Phase 3G.2.1

**Class:** runtime code exception (JavaScript syntax error in Start Code node)

## Defect

Same Phase 3G.2 splice corruption as Help: orphan `}) {` + legacy start body after the new INTLSEO `startReply`, so the Start node failed to parse/execute.

Live error: `Unexpected token ')'` at Start; Safe Telegram Reply not reached.

## Not the cause

- Router mismatch
- Missing connection (Start → IF Access Registry Write intact)
- Authorization failure
- Telegram HTML rejection
- Message length

## Repair

Removed orphan splice; extended moderator `/start` with `Имя в ответах:` from `Read ACCESS_CONTROL.reply_sender_name` (fallback `не задано`); try/catch + empty/length guards; `onError=continueRegularOutput`.

Post-patch Start hash: `2350550BB3EF82FC`.
