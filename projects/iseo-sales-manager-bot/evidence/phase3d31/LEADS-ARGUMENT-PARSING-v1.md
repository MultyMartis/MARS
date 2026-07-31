# LEADS-ARGUMENT-PARSING-v1

Exact supported forms:

- `/leads` → default **5**
- `/leads 3` | `/leads 5` | `/leads 10`
- Optional `@bot_username` on the command token only (Normalize strips `@…` before route)

Rules:

- Trim repeated whitespace via `split(/\s+/)`
- Argument must be exact token `3`|`5`|`10` (`/^(3|5|10)$/`)
- Reject: `1`, `7`, `03`, `10 extra`, non-integers
- `10` is never truncated to `1`
- Route Command uses Switch **equals** on `$json.command` (`/leads`) — no substring match

Invalid reply (exact):

```
⚠️ Укажите количество: 3, 5 или 10.
Например: /leads 5
```
