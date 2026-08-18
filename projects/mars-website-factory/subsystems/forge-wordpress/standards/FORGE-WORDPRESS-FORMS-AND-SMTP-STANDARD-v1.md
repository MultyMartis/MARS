# Forge WordPress — Forms and SMTP Standard v1

**ID:** FW-S-13  
**Status:** ACTIVE — PRODUCTION PROVEN WITH CAVEATS  
**Date:** 2026-08-18  
**Evidence:** FP-0002 ConsultationHandler; P15 mail suppress; P17-FU02 sequencing

---

## 1. Form checklist (every public form)

| Item | Requirement |
|------|-------------|
| Handler | One named AJAX/REST owner in functionality plugin |
| Validation | Server-side required; client UX is extra |
| CSRF | WordPress nonce; fail closed |
| Anti-spam | Honeypot and/or min-fill time, rate limit, duplicate token |
| Success/error UX | Visible without SMTP being live (accept vs send) |
| Recipient | Options or named constant — **never** in public HTML |
| From | Domain-aligned after SMTP; not a random `@localhost` |
| Reply-To | Submitter email when valid |
| AJAX | Same origin; logged-in and guest as designed |
| Logging | Optional private receipt; no full PAN/PII dump |
| SMTP | WordPress `wp_mail` after plugin/SMTP config |
| Suppression | MU `pre_wp_mail` allowed **until** SMTP phase |
| Forbidden | Direct PHP `mail()` bypass |

---

## 2. Launch sequencing

```text
domain / DNS / SSL
  → SMTP on the real sending domain
  → real form delivery proof
  → then indexing
```

Do not open indexing before forms are proven (AP-015).  
Do not remove mail suppression until domain smoke PASS.

Recipient constants may exist in code for future use; they must not send during pre-SMTP.

---

## 3. Pre-SMTP mode (allowed)

Validate + accept + optional Admin log. Return success to the user only if product policy says “we received it” **or** show a honest “saved, mail pending” — **do not claim email sent**.

---

## 4. SMTP phase

1. Remove or disable suppress MU.  
2. Configure SMTP (plugin or host) with final domain.  
3. Send test + one real form.  
4. Record evidence.  
5. Only then indexing gate.

---

*FW-S-13 v1.*
