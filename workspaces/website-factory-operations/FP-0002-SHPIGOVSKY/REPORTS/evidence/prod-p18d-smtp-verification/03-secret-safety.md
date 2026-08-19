# Secret Safety — P18D Wave

**Wave:** PROD-P18D  
**Date:** 2026-08-19

---

## Secret Handling Summary

| Surface | SMTP Password Exposure |
|---------|----------------------|
| This report | NO — not present |
| Git commit | NO — only source PHP committed; `OPTION_AUTH` is DB-only |
| `MailOps::get_config()` | NO — `unset($cfg['smtp_password'], ...)` before return |
| `SystemDashboard` | NO — renders `noreply@shpigovsky.ru` only |
| Correction script output | NO — prints `password_configured = YES` only |
| Activity log | NO — `log_system_event` does not receive password |
| Verification evidence files | NO — this file and all evidence files |
| REPORT | NO — Section 5 states CONFIGURED only |

---

## DB Storage Note

WordPress option `fp02_mailbox_auth` stores `{configured: 1, secret: "..."}`.  
WordPress DB is not a dedicated secret manager (documented honestly in P18C).  
The secret is only accessed in `MailOps::get_password_for_transport()` and passed to PHPMailer `$phpmailer->Password`.  
It is never returned to Admin HTML, REST, Dashboard, logs, or Git.

---

## SMTP SECRET REMAINED REDACTED THROUGH VERIFICATION
