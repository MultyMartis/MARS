# STRAY-LEAD-MESSAGE-FORENSIC-v1

## Source (proven)

Standalone Telegram message text **`Лид`** came from `answer_text: 'Лид'` on **queue_open** callback handling — not from card body text.

## Post-patch

- Static: `queue_open_no_literal_lid: true` (patch-deploy.json)
- Live acceptance: `standalone_lid_after_fix: 0`, queue_open `answer_text: Карточка`

## Expected after fix

`standalone literal Лид messages = 0` for normal reminder / `/leads` navigation.
