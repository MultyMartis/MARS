# BUTTON LABEL CONTRACT v1

## Scope

Visible captions on **pending** lead inline action buttons only.

## Approved labels (Phase 3D.8.3)

| Order | Action | Visible label | Callback (unchanged) |
|------:|--------|---------------|----------------------|
| 1 | processed | `✅ Обработано` | `sm:p:<opaque-token>` |
| 2 | spam | `🚫 Спам` | `sm:s:<opaque-token>` |

## Previous labels

| Order | Visible label |
|------:|---------------|
| 1 | `✅ Отметить обработанным` |
| 2 | `🚫 Отметить как спам` |

## Rules

- Cyrillic text exactly as approved
- No trailing period
- No extra words
- Processed button remains first; spam second
- Current row layout retained (both buttons on one row)
- Buttons only when lifecycle=`pending`
- Archive `/leads` cards remain non-actionable

## Sources patched (Operational.dev only)

1. `Format Telegram Lead Card` — `buildReplyMarkup()` button `text` values
2. `Send Telegram Lead Card With Buttons` — top-level `inlineKeyboard` button `text` values

Callback expressions and prefixes unchanged.
