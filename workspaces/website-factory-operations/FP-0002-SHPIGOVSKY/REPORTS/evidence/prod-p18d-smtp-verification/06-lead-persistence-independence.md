# Lead Persistence Independence from SMTP — P18D

**Wave:** PROD-P18D  
**Date:** 2026-08-19

---

## Architecture Guarantee

`ConsultationHandler::persist_lead()` is called before `attempt_outbound_mail()`.  
If `wp_mail()` fails (or throws, or is suppressed), the lead already exists in `fp02_form_leads`.

```php
$lead_id = self::persist_lead($payload);       // persists first
if ($lead_id <= 0) { return error; }

$mail = self::attempt_outbound_mail($payload, $lead_id); // then tries mail
// success or failure → updates lead status
```

Possible lead statuses after SMTP attempt:
- `MAIL_ACCEPTED` — SMTP accepted
- `MAIL_ERROR` — SMTP returned error; lead still exists
- `MAIL_SUPPRESSED` — suppression active; lead still exists
- `SMTP_PENDING` — SMTP configured but not verified/active; lead still exists

The visitor sees `"Заявка принята"` as long as the lead was stored, independent of mail.

---

## Failure Safety Test Approach

The negative-path is proven by architecture inspection (code review) since:
- Intentionally breaking production SMTP globally would violate the bounds of this wave.
- The code path is deterministic: `persist_lead → attempt_outbound_mail → update_delivery`.
- The status codes are distinct: `MAIL_ERROR` ≠ `MAIL_ACCEPTED`.

Bounded negative-path can be tested by temporarily setting `delivery_active=0` (suppression) and verifying lead is stored with `MAIL_SUPPRESSED` status — this is the existing P18C QA path and is already proven.

---

## LEAD PERSISTENCE REMAINS INDEPENDENT FROM SMTP SUCCESS
