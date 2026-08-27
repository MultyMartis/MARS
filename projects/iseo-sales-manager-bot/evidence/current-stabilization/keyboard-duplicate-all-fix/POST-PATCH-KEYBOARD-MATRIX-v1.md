# POST-PATCH-KEYBOARD-MATRIX-v1

## ADMIN_A acceptance keyboard (post-deploy)

Telegram message_id `1142` (ADMIN_A-only; no claim / no `last_window` mutation).

At acceptance time pending mix had **no SEO** (`SEO=0`), so SEO button correctly omitted.

| Slot (logical order) | text | callback | Notes |
|----------------------|------|----------|-------|
| 1 | `🔍 Аудит · 12` | `sm:g:c:aa2771a403` | once |
| 2 | `📦 Другое · 4` | `sm:g:c:e130bfb8c3` | once |
| 3 | `🔴 Старше суток · 15` | `sm:g:o24` | once |
| 4 | `📋 Все · 16` | `sm:g:all` | **exactly once** |

| Metric | Value |
|--------|-------|
| `rm_kb_n` | 4 |
| All buttons actual | **1** |
| duplicate All | **0** |
| empty callback buttons | **0** |
| Send path | Switch → `Send Reminder Telegram KB4` (exact) |

## Live flatten proof

Deployed Code contains empty-slot emission (not All pad). `flatten_fix_live = true` in verify summary.
