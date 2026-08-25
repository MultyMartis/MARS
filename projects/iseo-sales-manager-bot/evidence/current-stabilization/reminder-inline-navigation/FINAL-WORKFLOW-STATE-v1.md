# FINAL WORKFLOW STATE v1

Workflow: `wLrLp4WQHm1VJmxz` — i-SEO Sales Manager - Admin.dev  
Active: **true**  
Nodes after fix: **111** (was 106)  
POST sha16: `6CFE53A51F840A9E`

## Modified / added (keyboard attachment only)

| Area | Change |
|---|---|
| Reminder Build Claims | `flattenInlineKeyboardUi` → `rm_b*` fields |
| Send Reminder Telegram | static packed field-expression keyboard |
| Prepare Callback Answer | flatten + `rm_kb_band` |
| IF Telegram Has Buttons | true → Switch Reply Keyboard Band |
| Safe Telegram Reply KB4/8/12/14 | new field-expression send nodes |
| Safe Telegram Reply | unchanged path for no-buttons (`replyMarkup: none`) |

## Not modified

Schedule, business-window key, claims, last_window, delivery dedupe, pending selector, ACCESS, recipient resolution, AI.

## Acceptance message_ids (ADMIN_A)

1090 (digest), 1091 (group), 1092 (lead) — all with `reply_markup`.
