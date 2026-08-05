# `/help` root cause — Phase 3G.2.1

**Class:** runtime code exception (JavaScript syntax error in Help Code node)

## Defect

Phase 3G.2 text refresh left a corrupted splice in the shared Admin module inside the Help node: after the new `startReply(...)` body, an orphan fragment `}) {` + legacy `Sales Manager Admin запущен.` block remained before `function helpReply`.

Live error: `Unexpected token ')'` at Help; execution status=error; Safe Telegram Reply not reached.

## Not the cause

- Router mismatch (branch matched Help)
- Authorization failure
- Empty builder result
- Telegram parse_mode rejection
- Message-length overflow
- PROFILE_EVENTS side effect

## Repair

Removed orphan splice; wrapped Help footer in try/catch with safe fallback; `onError=continueRegularOutput`. Admin help length measured **2344** UTF-16 code units / characters under Telegram 4096 — **no split required**.

Post-patch Help hash: `2DD74ABFE6099814`.
