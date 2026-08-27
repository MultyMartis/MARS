# NATURAL-DUPLICATE-ALL-EVIDENCE-v1

## Source execution

| Field | Value |
|-------|--------|
| Workflow | Admin.dev `wLrLp4WQHm1VJmxz` |
| Execution ID | `41719` |
| Business window | `pending-reminder:2026-08-27:10:00:Europe/Moscow` |
| Path | Natural **Send Reminder** (scheduled morning digest) |

## Telegram-visible keyboard (provider return)

From execution `41719` Telegram node result `reply_markup.inline_keyboard`:

| Row | Buttons |
|-----|---------|
| 1 | `🔍 Аудит · 14` → `sm:g:c:aa2771a403` |
| 2 | `📈 SEO · 1` → `sm:g:c:ade3cbdc59` · `📦 Другое · 8` → `sm:g:c:e130bfb8c3` |
| 3 | `🔴 Старше суток · 21` → `sm:g:o24` · `📋 Все · 23` → `sm:g:all` |
| 4 | `📋 Все` → `sm:g:all` · `📋 Все` → `sm:g:all` |
| 5 | `📋 Все` → `sm:g:all` |

## Counts

| Metric | Value |
|--------|-------|
| Logical main filters expected | 5 (Audit, SEO, Other, Older, All) |
| Legitimate All | 1 |
| Extra All from unused slots | 3 |
| Total All buttons on wire | **4** |
| `duplicate All buttons` | **3** |

## Renderer vs wire

- Digest / flatten reported `rm_kb_n = 5` (five real buttons including one All).
- Fixed-8 Send Reminder Telegram node still emitted slots 6–8 as All pads.
- Operator-visible regression matches rows 4–5 above.

## Sanitization

No chat IDs, tokens, or contact PII retained in this file. Raw private dump: worktree `private/forensic/send-41719-structure.json` (not committed).
