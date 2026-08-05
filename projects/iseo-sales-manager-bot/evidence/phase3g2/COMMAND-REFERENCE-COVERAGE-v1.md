# Command reference coverage

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Authority

`guides/TELEGRAM-COMMAND-REFERENCE-v1.md`

## Coverage map (live Admin.js matrix ∩ reference)

| Group | Commands | In reference | Present live |
|-------|----------|--------------|--------------|
| Public/personal | `/start` `/help` `/my_status` | yes | yes |
| Runtime/AI/health | `/status` `/health` `/ai_*` `/stats` `/last_error` `/config` | yes | yes |
| Leads/pending | `/leads` `/lead_history` `/pending_*` | yes | yes |
| Reminders | `/reminder_*` | yes | yes |
| Delivery | `/delivery_status` `/delivery_users` | yes | yes |
| Moderators | `/moderators` `/moderator_*` | yes | yes |
| Reply profiles | `/reply_profiles` `/reply_profile` `/reply_name_set|enable|disable` `/my_reply_profile` | yes (number-based) | yes |

## Deferred

- `/test_lead` — not advertised in help (sandbox).

## Result

- [x] Every current live command family mapped to TELEGRAM-COMMAND-REFERENCE-v1
