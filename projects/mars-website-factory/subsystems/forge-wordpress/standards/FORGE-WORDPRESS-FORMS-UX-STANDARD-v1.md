# Forge WordPress — Forms UX standard v1

**ID:** FW-S-40  
**Status:** ACTIVE — CANONICAL DEFAULT (UX)  
**Date:** 2026-08-18  
**Extends:** [FORMS-AND-SMTP](FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) (delivery / SMTP sequencing remain there)

---

## 1. Frontend UX checklist

| Item | Requirement |
|------|-------------|
| Labels | Visible; associated `for`/`id` |
| Required markers | Visible + `required` / `aria-required`; not color-only |
| Phone / email | `type="tel"` / `type="email"`; server re-validates |
| Inline errors | Next to the field; announced (aria-live or focus) |
| General errors | Banner if the failure is not field-specific |
| Pending / loading | Disable submit; visible pending state |
| Duplicate submit | Client guard **and** server duplicate token |
| Success | Honest copy ([FW-S-13](FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) pre-SMTP vs sent) |
| Retry | After error, submit re-enabled |
| Accessibility | [FW-S-37](FORGE-WORDPRESS-ACCESSIBILITY-BASELINE-v1.md) |
| Mobile keyboards | correct `inputmode` / types |

One JS owner per form family ([FW-S-36](FORGE-WORDPRESS-FRONTEND-INTERACTION-OWNERSHIP-STANDARD-v1.md)).

---

## 2. Abuse / rate control

Use **low friction** first:

| Control | Default |
|---------|---------|
| Nonce | required |
| Honeypot | recommended |
| Min-fill time / rate limit | recommended |
| Backend validation | required |
| CAPTCHA | **only when required** (abuse evidence or client policy) |

Do not add high-friction captcha by default.

---

## 3. Observability (UI success vs mail success)

After launch, operators must distinguish:

| Signal | Meaning |
|--------|---------|
| FORM UI SUCCESS | Handler accepted the payload; user saw success |
| MAIL ACTUAL DELIVERY SUCCESS | `wp_mail` / SMTP accepted **and** (where possible) no bounce in the evidence window |

Log: timestamp, form id, outcome (`accepted` / `mail_sent` / `mail_failed` / `rate_limited`), **not** full message bodies or secrets. Privacy: no PAN; truncate PII.

Dashboard or Activity Log may show counts; SMTP plugin logs stay Admin-only.

---

*FW-S-40 v1.*
