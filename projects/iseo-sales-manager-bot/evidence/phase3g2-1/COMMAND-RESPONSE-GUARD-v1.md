# Command response guard — Phase 3G.2.1

**Invariant:** no recognized command may silently terminate.

## Implementation

1. **Builder try/catch** on Help / Start / Config Summary footers.
2. **Empty / overflow guards** return safe Russian fallback.
3. **Capture Admin Reply** fills fallback when `command` is set and `reply_text` empty; records `command_response_guard_applied` + error timestamps (no stack traces).
4. **onError=continueRegularOutput** on Help / Start / Config Summary so post-parse runtime faults still reach Capture.

## Fallback text

`Не удалось сформировать ответ команды. Ошибка зафиксирована, повторите позже.`

## Capture hash

`52D277079D2DC1C3`
