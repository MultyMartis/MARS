# FINAL WORKFLOW STATE v1 — Phase 3D.8.3

| Workflow | ID | Active | Nodes | Notes |
|----------|----|--------|------:|-------|
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | 19 | rollback; unchanged |
| i-SEO Sales Manager - Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | sole Gmail intake; button labels polished |
| i-SEO Sales Manager - Admin.dev | `wLrLp4WQHm1VJmxz` | true | 59 | callbacks/attribution unchanged this phase |

## Operational.dev patch summary

- Same workflow ID (no copy)
- Format `buildReplyMarkup` button texts → `✅ Обработано` / `🚫 Спам`
- Send With Buttons `inlineKeyboard` texts → same
- Callback expressions unchanged
- OpenRouter remains disabled
- Exactly one active Schedule Trigger
- Gmail Fetch remains sole intake path

## Admin.dev

No callback-processing logic change. No patch required for label polish.
