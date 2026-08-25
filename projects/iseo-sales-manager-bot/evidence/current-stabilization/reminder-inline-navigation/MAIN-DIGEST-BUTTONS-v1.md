# MAIN DIGEST BUTTONS v1

## Contract

Main digest shows compact **group/filter** buttons only (not one button per lead).

Namespace: `sm:g:`

Generic categories (count > 0 only):

- Аудит / SEO / Реклама / Разработка сайта / Другое / Требует уточнения
- Старше суток (`sm:g:o24`)
- Все (`sm:g:all`)

## Layout

Packed 1–2 buttons per row (mobile-readable). Field slots `rm_b1`…`rm_b8` feed the Telegram node.

## Live acceptance

ADMIN_A digest message_id **1090**:

- `digest_has_reply_markup: true`
- `digest_group_callbacks: 8` (includes pad slots to fixed keyboard size)
- Generated filter buttons from current pending categories (`digest_button_n: 6` before pad)

No PII in callbacks.
