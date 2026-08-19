# SMTP State Transitions — P18D

**Wave:** PROD-P18D  
**Date:** 2026-08-19

---

## State Machine

```
NOT_CONFIGURED
  → CONFIGURED_NOT_VERIFIED   (operator saves host/port/enc/user/pass/recipients)
  → VERIFIED_READY             (p18d-smtp-correct-and-verify.php: test PASS)
  → VERIFIED_ACTIVE            (p18d-activate-delivery.php or Admin button)
```

---

## P18D Sequence

| Step | Action | State Before | State After |
|------|--------|-------------|------------|
| Start of P18D | Operator has saved credentials | CONFIGURED/NOT VERIFIED | — |
| Config correction | smtp_encryption: none → ssl | CONFIGURED/NOT VERIFIED | CONFIGURED/NOT VERIFIED |
| SMTP test | p18d-smtp-correct-and-verify.php | CONFIGURED/NOT VERIFIED | VERIFIED/NOT ACTIVE |
| Delivery activation | p18d-activate-delivery.php or Admin | VERIFIED/NOT ACTIVE | VERIFIED/ACTIVE |
| MU retirement | fp02-pre-cutover-mail-suppression.php defers to MailOps | MU inert | MU removed |

---

## Activity Log Events (expected sequence)

| Event | Description |
|-------|-------------|
| `smtp_config_updated` | Config correction applied |
| `smtp_test_ok` | SMTP test accepted by server |
| `smtp_activated` | Delivery activated |

---

## Suppression State

| Phase | Suppression |
|-------|-------------|
| Pre-P18D | ON (delivery_active=0) |
| During test | Bounded bypass only (FP02_MAIL_ALLOW_ONCE) |
| After activation | OFF (delivery_active=1 → should_suppress()=false) |
| MU after activation | Inert (defers to MailOps) |
| After MU removal | MailOps-only owner |

---

## No Competing Mail Switches

After P18D:
- ONE owner: `MailOps::delivery_active` in `fp02_mail_ops` option
- ONE transport: `SmtpTransport` on `phpmailer_init`
- NO competing SMTP plugin
- MU defers to MailOps → removable cleanly
