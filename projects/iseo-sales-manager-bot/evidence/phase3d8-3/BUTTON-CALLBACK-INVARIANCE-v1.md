# BUTTON CALLBACK INVARIANCE v1

## Contract

Visible button text and callback action are separate contracts.

## Invariants verified

| Item | Before | After |
|------|--------|-------|
| Processed callback prefix | `sm:p:` | `sm:p:` |
| Spam callback prefix | `sm:s:` | `sm:s:` |
| Token algorithm | FNV dual-hash 12 hex | unchanged |
| Send processed expression | `={{$json.telegram_callback_processed}}` | unchanged |
| Send spam expression | `={{$json.telegram_callback_spam}}` | unchanged |
| Normalize Command parse | `sm:p:` → processed / `sm:s:` → spam | unchanged |
| Handle Callback Action | no label-based branching | unchanged |

## Live API proof (synth `PHASE_3D8_3_BUTTON_LABEL_ACCEPTANCE`)

- Both recipient sends returned `reply_markup` with two buttons
- Labels: `✅ Обработано` / `🚫 Спам`
- Callback prefixes on live messages: `sm:p:` / `sm:s:`
- Token length: 12

## Non-changes

- Lifecycle values (`pending` / `processed` / `spam`)
- CLEAN / LEAD_EVENTS schema
- Actor attribution logic
- ACCESS_CONTROL
- Authorization rules
