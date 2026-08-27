# KEYBOARD-SLOT-MATRIX-v1 — Pre-fix (exec 41719)

Architecture at defect time: single **Send Reminder Telegram** fixedCollection with 8 field-expression slots (`rm_b1_*` … `rm_b8_*`), filled by `flattenInlineKeyboardUi(..., 8, '📋 Все', 'sm:g:all')`.

| Slot | text field | callback field | Expected logical | Actual Telegram |
|------|------------|----------------|------------------|-----------------|
| 1 | `rm_b1_text` | `rm_b1_cb` | Audit | `🔍 Аудит · 14` / `sm:g:c:aa2771a403` |
| 2 | `rm_b2_text` | `rm_b2_cb` | SEO | `📈 SEO · 1` / `sm:g:c:ade3cbdc59` |
| 3 | `rm_b3_text` | `rm_b3_cb` | Other | `📦 Другое · 8` / `sm:g:c:e130bfb8c3` |
| 4 | `rm_b4_text` | `rm_b4_cb` | Older | `🔴 Старше суток · 21` / `sm:g:o24` |
| 5 | `rm_b5_text` | `rm_b5_cb` | All | `📋 Все · 23` / `sm:g:all` |
| 6 | `rm_b6_text` | `rm_b6_cb` | **unused / empty** | `📋 Все` / `sm:g:all` (**pad**) |
| 7 | `rm_b7_text` | `rm_b7_cb` | **unused / empty** | `📋 Все` / `sm:g:all` (**pad**) |
| 8 | `rm_b8_text` | `rm_b8_cb` | **unused / empty** | `📋 Все` / `sm:g:all` (**pad**) |

## Divergence

First wrong slot: **6** — unused slot defaulted to All pad instead of empty / omitted.
