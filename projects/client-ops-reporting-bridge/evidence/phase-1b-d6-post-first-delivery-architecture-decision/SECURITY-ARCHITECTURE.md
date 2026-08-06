# SECURITY ARCHITECTURE — Phase 1B-D6

`D6_SECURITY_ARCHITECTURE_REVIEWED`

## Scope

Review of **future** architecture against current containment. No secrets exposed in this pack.

## Surfaces

| Surface | Current control | Future risk if unattended early |
|---------|-----------------|----------------------------------|
| Webhook secret / header auth | Header auth credential on webhook; local ignored secrets | Continuous exposure under C2; windowed under C3 |
| n8n API key | Local credentials loader; activation allowlist | Activation automation must not broaden API scope |
| Telegram credentials | n8n Telegram credential; chat allowlisted in compose validation | Duplicate sends = customer spam / info disclosure |
| Event payload | Firewall + allowlists; raw monitor logs stripped | Must keep raw paths/logs out of Telegram + DT |
| Data Table content | No tokens; sandbox marker; no message_id yet | Do not store tokens; message_id OK if sanitized |
| Personal Telegram identity | Chat id in workflow; evidence uses sanitized message_id only | Evidence packs must not store personal profile dumps |
| Source filesystem paths | D5 sanitizes labels; forbidden in message preview | Unattended must never place absolute Storage paths in customer text |
| Runtime / MAIN | Dedicated runtime pin; MAIN may be dirty | Producer must not execute from dirty MAIN |

## Least privilege rules (design)

1. Activation client remains allowlisted to one workflow activate/deactivate only.
2. Producer HTTP only to approved host/route with auth header.
3. Data Table stores delivery metadata, never credentials.
4. Unattended jobs use dedicated runtime + Storage artifact roots already approved.
5. No broadening of Telegram chat targets without new charter.

## D6 evidence hygiene

- No raw webhook URL, API keys, tokens, or raw execution bodies in this pack.
- Allowed identifiers: workflow id, table id, event_id, run_id, execution 3416, sanitized message_id 7, commits.

## Conclusion

Security posture is acceptable for **continued contained C1 manual charters**.
It is **not** acceptable to authorize unattended production until A/B/C/E minimum model is implemented and re-reviewed.
