# RENDERER KEYBOARD OUTPUT v1

Source: natural execution **40019** + live `Reminder Build Claims` digest renderer.

## Renderer produced

- `telegram_has_buttons: true`
- `digest_button_count: 5`
- `telegram_inline_keyboard_ui.rows` with group/filter buttons (`sm:g:`)

## Example button set (counts from that window; not hardcoded forever)

| Label pattern | callback namespace |
|---|---|
| 🔍 Аудит · N | `sm:g:c:<hash>` |
| 📈 SEO · N | `sm:g:c:<hash>` |
| 📦 Другое · N | `sm:g:c:<hash>` |
| 🔴 Старше суток · N | `sm:g:o24` |
| 📋 Все · N | `sm:g:all` |

Only categories with count > 0 are rendered. Layout packs 1–2 buttons per row.

## Conclusion (pre-fix)

Renderer **did** produce a valid inline keyboard object for the natural reminder path.

## Post-fix addition

`Reminder Build Claims` now also emits flat field slots `rm_bN_text` / `rm_bN_cb` (via `flattenInlineKeyboardUi`) for Telegram node field-expression binding.
