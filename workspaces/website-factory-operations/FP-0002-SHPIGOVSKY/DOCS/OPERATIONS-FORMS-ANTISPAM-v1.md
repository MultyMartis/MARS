# DOCS — Forms anti-spam operations (FP-0002)

**Audience:** operator / maintenance  
**Status:** ACTIVE with core `0.3.24-antispam`

## What is active

Native layered anti-spam on final + modal lead forms:

1. Invisible honeypot (`company_url`)
2. Server-signed time-to-submit (`fp02_fs`)
3. Request token idempotency
4. Bounded rate limits
5. Conservative payload heuristics

No Google / Yandex / external CAPTCHA.

## Admin

**Настройки сайта → Почта и формы** shows «Антиспам: Активен» + layer list + reject counters (24h/7d, no PII).

## Visitor UX

Neutral Russian errors only. No reason codes exposed.

## Ops notes

- Spam never creates leads, mail, or Metrika goals.
- Accepted leads still persist-before-mail.
- Do not lower rate limits blindly (shared NAT / mobile).
- Do not add third-party CAPTCHA without a new charter.

## Evidence

`REPORTS/evidence/prod-maint-native-antispam-v1/`  
`REPORTS/REPORT-FP-0002-PROD-MAINT-NATIVE-ANTISPAM-V1.md`
