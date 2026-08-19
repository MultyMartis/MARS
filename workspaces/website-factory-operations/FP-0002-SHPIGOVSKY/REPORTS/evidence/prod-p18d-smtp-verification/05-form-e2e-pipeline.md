# Form E2E Pipeline — P18D

**Wave:** PROD-P18D  
**Date:** 2026-08-19

---

## Real Form Delivery Sequence

```
Browser frontend form (data-lead-form)
  ↓ js: validate fields
  ↓ js: wp_ajax fp02_lead_submit POST
  ↓
ConsultationHandler::handle_ajax()
  ↓ POST method check
  ↓ nonce verify (fp02_lead_nonce)
  ↓ honeypot check
  ↓ fill timing check (MIN 3s)
  ↓ rate limit check
  ↓ duplicate request_token check
  ↓ sanitize_payload()
  ↓ validate_payload() → name ≥2 chars, phone ≥10 digits, message ≥3 chars, consent
  ↓
LeadRegistry::insert() → fp02_form_leads table → lead_id > 0
  ↓ STATUS: RECEIVED
  ↓
MailOps::should_attempt_mail() → true (VERIFIED/ACTIVE, is_complete)
  ↓
wp_mail(to[], subject, body, headers)
  ↓ SmtpTransport::configure_phpmailer() on phpmailer_init
    → isSMTP()
    → Host=smtp.beget.com, Port=465, SMTPSecure='ssl', SMTPAuth=true
    → Username=noreply@shpigovsky.ru, Password=[from MailOps::get_password_for_transport()]
  ↓
PHPMailer → SSL connect → AUTH → SMTP ACCEPT
  ↓
LeadRegistry::update_delivery() → STATUS: MAIL_ACCEPTED
  ↓
JSON response → {ok:true, accepted:true, mail_accepted:true, status:'MAIL_ACCEPTED'}
  ↓
Browser JS → show success message
  ↓
MailOps::metrika_goal() → if non-empty: ym(counter, 'reachGoal', goal) after success
```

---

## Failure Isolation

- Lead is persisted BEFORE mail attempt.
- If mail fails → status = MAIL_ERROR; JSON response still ok=true (lead stored).
- Visitor sees success message ("Заявка принята") regardless of mail transport.
- Lead registry is source of truth; email is delivery transport only.

---

## Multiple Recipients

- `MailOps::recipient_emails()` returns all valid unique recipients.
- `wp_mail($to_array, ...)` — WordPress passes array to PHPMailer.
- PHPMailer sends one SMTP transaction with all recipients in `To:`.
- One lead row, one logical mail operation, N recipients.

---

## Reply-To Safety

- `From:` = `noreply@shpigovsky.ru` (never visitor email)
- `Reply-To:` = visitor email only if `is_email($payload['email'])` — visitor email is optional
- Phone-only submissions (no email) → no Reply-To header

---

## REAL FORM END-TO-END DELIVERY PIPELINE VERIFIED (after SMTP activation)

QA script: `WORDPRESS/validation/p18d-form-qa.php`  
QA lead: `is_qa=1`, flagged for cleanup after evidence capture.
