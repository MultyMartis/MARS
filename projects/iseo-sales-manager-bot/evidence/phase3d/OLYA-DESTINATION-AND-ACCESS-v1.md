# OLYA-DESTINATION-AND-ACCESS-v1

**Phase:** 3D  
**Manager persona:** PER-0010 Дягилева Ольга (Оля)

## Working model (accepted v1)

| Topic | Decision |
|-------|----------|
| Production lead cards destination | CONFIG `telegram_manager_chat_id` (manager destination) |
| Оля access to cards | Must be able to **read** that destination (shared chat/group or her account as destination) |
| Admin commands | Operator allowlist only (size=1) — **Оля not added** |
| n8n access | **Not required** for Оля |
| Gmail access | **Not required** for Оля |
| Credentials | **Not issued** to Оля |
| First reply | Оля **manually copies** prepared text |
| Lifecycle | Оля updates Sheets manager fields per LEAD-LIFECYCLE v1 |

## Current contour note

Operator-attested production Telegram destination is the configured manager chat used by Operational.dev Send node. Whether Оля already has membership in that exact destination is an **operator confirmation** item (do not invent access changes).

## Explicit non-actions

- Do **not** add Оля to Admin allowlist without separate operator approval.  
- Do **not** share n8n API keys, Gmail OAuth, Sheets credentials, or bot tokens.  
- Do **not** enable automatic client messaging for Оля or anyone.

## Handoff artifact

Russian guide: `guides/OLYA-LEAD-WORK-GUIDE-v1.md`.
