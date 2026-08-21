# ISEO-SU FORM OPERATOR RECIPIENT REMOVAL EVIDENCE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-RECIPIENT-REMOVE-AND-TECH-SEO-AUDIT-01  
**Date:** 2026-08-21  
**Authority:** current production form recipient routing after intentional operator-mailbox removal  
**Does not rewrite:** historical Acceptance / Antispam / Recipient-Restore REPORTs (those remain historical evidence of earlier phases)

---

## 1. Intent

After acceptance testing, the temporary/operator mailbox `im.work@mail.ru` was intentionally removed from the **active production** recipient set. The original legitimate recipient remains the sole production To address. Anti-spam / validation / HMAC / rate limits / honeypot / duplicate protection / markup / JS were **not** changed.

## 2. State Before Mutation

Independent SFTP read of production `iseo-form-config.php` (stamp `20260821T055420Z`, SHA-256 `dea5b3482feb914f…`):

| Field | Value |
|-------|-------|
| `test_mode` | **false** (OFF) |
| `production_recipients` | `nikel007i33@yandex.ru`, `im.work@mail.ru` |
| `im.work@nail.ru` | **ABSENT** |
| Root handlers on shared send | **12/12** |
| Hardcoded To overrides in handlers | **NONE** |
| CC/BCC in send helper | **NONE** (no Cc/Bcc header literals) |

## 3. Mutation

| Step | Result |
|------|--------|
| Scoped backup | `local/sites/iseo-su-production/_recipient-remove-01/backups/remove-20260821T055420Z/` |
| Canonical source updated first | `production-source/forms/iseo-form-config.php` |
| Production upload | exact source file via SFTP |
| Post-upload SHA | **MATCH** source |
| Mail sent during task | **0** |

## 4. State After Mutation

| Field | Value |
|-------|-------|
| Production SHA-256 | `1aa4d09b091e1c3e…` |
| Source SHA-256 | `1aa4d09b091e1c3e…` |
| `test_mode` | **false** (OFF) |
| Effective production recipients | **`nikel007i33@yandex.ru` only** |
| `im.work@mail.ru` in `production_recipients` | **NO** |
| `im.work@nail.ru` | **ABSENT** |
| `test_recipients` | still lists operator mailbox for **future controlled tests only** (unused while `test_mode=false`) |
| PRODUCTION ↔ MARS SOURCE | **ALIGNED** |

## 5. Handler Coverage

All 12 root `__FORM.php` handlers continue to use shared `iseo_form_send_mail()` / `iseo-form-security.php`. No handler hardcodes `im.work@mail.ru` or `im.work@nail.ru`. Service-tree delegates remain thin `require` to roots.

## 6. Security Surface

**Unchanged:** server-side validation, honeypot, HMAC / min fill time, rate limiting, duplicate protection, malformed/empty POST rejection, mail templates, form markup, JS anti-spam.

## 7. Decision

**COMPLETE — OPERATOR MAILBOX REMOVED FROM PRODUCTION RECIPIENTS / ORIGINAL RECIPIENT RETAINED / TEST_MODE OFF / 0 MAIL SENT**

Historical note: Acceptance 02 correctly retained the operator mailbox for delivery proof. That phase remains historically valid. This evidence records the later, intentional removal after acceptance.
