# ROOT CAUSES v1 — Phase 3D.5.2 Admin silence

| # | Root cause | Symptom | Repair |
|---|---|---|---|
| 1 | `require('crypto')` disallowed in n8n task-runner | Check User Authorization error; total silence | Pure JS SHA-256 (bit-compatible) |
| 2 | Malformed JS headers with literal `\n` breaking `/**` comments | SyntaxError `Unexpected token '*'`; silence after first patch | Clean rebuild of Code sources |
| 3 | CONFIG Sheets fan-out (N rows) × ACCESS_CONTROL reads | Rate-limit errors; silence on subsequent commands | Collapse Authorization Context → one item |
| 4 | `/start` registry upsert path: Restore read Sheets `$json` | Empty `reply_text`/`chat_id`; silent send failure | Restore from Prepare Access Upsert / Start |
| 5 | Telegram/n8n Markdown default ate `_` in help | `/lasterror` visually instead of `/last_error` | HTML `parse_mode` + `<code>/…</code>` |

Not root causes: missing webhook; wrong bot Trigger owner; empty ACCESS_CONTROL after 3D.5.1 population.
