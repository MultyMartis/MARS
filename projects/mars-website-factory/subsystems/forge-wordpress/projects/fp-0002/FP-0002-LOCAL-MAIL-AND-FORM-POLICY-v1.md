# FP-0002 — Local Mail and Form Policy v1

**Version:** v1 | **Date:** 2026-06-23

## Outgoing mail

| Control | Implementation |
|---------|----------------|
| MU-plugin `pre_wp_mail` | Returns `false` — all outbound blocked |
| SMTP plugin | **Not installed** |
| Production SMTP credentials | **Forbidden** |

## Forms (FW-06A)

| Item | Status |
|------|--------|
| WP form plugins | **Not installed** |
| Modal consultation form | Frontend only — backend **BLOCKED** in static |
| `home-final-form` | **NOT_CONNECTED** in static |
| Real recipient addresses | **Not configured** |

## Future architecture (FW-06B+)

Document at integration:

- Submission endpoint ownership (theme vs `shpigovsky-core`)
- reCAPTCHA / captcha keys — currently **BLOCKED** in project authority
- Local test inbox strategy (e.g. mailhog) — operator decision
- `false_success` — **PROHIBITED** per project charter

## Operator command

No mail leaves this runtime. If testing mail pipeline later, use dedicated local catcher — never production relays.

---

*FP-0002 local mail and form policy — FW-06A.*
