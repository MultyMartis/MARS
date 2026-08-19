# Forge WordPress — Forms and SMTP Standard v1

**ID:** FW-S-13  
**Status:** ACTIVE — PRODUCTION PROVEN  
**Date:** 2026-08-19  
**Evidence:** FP-0002 ConsultationHandler; P15 mail suppress; P17-FU02 sequencing; P18D SMTP verification + activation

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
5. Only then indexing gate (explicit human action — [SEARCH-INDEXING-CONTROL](FORGE-WORDPRESS-SEARCH-INDEXING-CONTROL-STANDARD-v1.md)).

---

## 5. Technical sender mailbox naming

Default dedicated technical website sender:

```text
noreply@<site-domain>
```

unless the project explicitly requires another sender identity.

Do **not** store mailbox passwords or SMTP credentials in Git or project docs.

Example (FP-0002): mailbox `noreply@shpigovsky.ru` may exist at the host while WordPress SMTP configuration is still PENDING.

---

## 6. One Admin owner

SMTP host/port/encryption/auth/username/password, sender, recipients, form Metrika goal, and lead retention live in **one** Admin section (Site Settings → Почта и формы). Do not scatter fields across `wp-config`, theme, handlers, and plugin files.

Saving fields ≠ verified. Verified ≠ active outbound delivery.

---

## 7. SMTP secrets

Operator-entered Admin storage (dedicated `wp_options`, autoload off) may be accepted for a typical site. It is **not** a cryptographic secret manager.

Never:

- commit the password
- render it in HTML
- show it in Dashboard / Activity Log / REST / reports
- log PHPMailer dumps that include credentials

Write-only UX: show CONFIGURED / NOT CONFIGURED; blank field keeps the existing secret.

---

## 8. Transport owner

One PHPMailer / `phpmailer_init` owner in the functionality plugin. No competing SMTP plugin unless the project charter requires it. Forms use `wp_mail` only — never PHP `mail()`.

---

## 9. Lead persistence (source of truth)

```text
validate → normalize → persist lead → attempt mail → update delivery status → JSON
```

**FORM LEAD PERSISTENCE DOES NOT DEPEND ON EMAIL SUCCESS.** Email is transport. Frontend success may mean “заявка принята” after persist even if mail is suppressed or failed. Do not call SMTP acceptance “delivered to inbox”.

Preferred statuses: `RECEIVED`, `MAIL_SUPPRESSED`, `SMTP_PENDING`, `MAIL_ACCEPTED`, `MAIL_ERROR`.

QA data rule:

- QA rows must be explicitly identifiable by a field such as `is_qa`, a known task marker, or an exact evidence-backed ID list;
- never delete production rows merely because they were created near a test window or "look like a test".

**Lead retention (P18H / FORM-RETENTION-001–002):**

- `lead_retention_days=0` means auto-deletion is **off** — not a neutral default;
- recommend an explicit purpose-bound period (FP-0002: **730 days** for consultation leads) documented in project DECISIONS;
- introducing a retention setting must **not** silently purge historical real leads in the same wave;
- align Privacy Policy retention wording when the Admin value is applied.

---

## 10. Analytics

Yandex Metrika **counter** lives in SEO / Integrations. Form settings store only the **goal identifier**. Fire `reachGoal` only after a backend-confirmed accepted response. Never on button click. Analytics must not break submit UX if the counter is missing or blocked.

Goal semantics: **FORM SUBMISSION ACCEPTED**, not **EMAIL DELIVERED**, unless the product explicitly proves mailbox delivery.

---

## 11. Mail suppression lifecycle

Temporary MU `pre_wp_mail` is allowed until SMTP is **verified** and the operator **explicitly activates** sending. Do not auto-enable on Save. Retire the MU after the SMTP module owns production delivery (AP-027 / FORM-006).

States: NOT CONFIGURED → CONFIGURED / NOT VERIFIED → VERIFIED → VERIFIED / ACTIVE. Do not confuse configured with verified (AP-028 / FORM-007).

The SMTP/forms Admin screen is not done until it is **visible** under the intended Site Settings parent (AP-029). A working callback or direct URL is not operator discoverability.

---

## 12. Reply-To / From

From = `noreply@<domain>` (or the project sender). Reply-To = visitor email **only** if valid. Never put the visitor address in From.

---

---

## 13. SMTP Provider Parameter Verification (P18D lesson)

**Always verify SMTP transport parameters from the provider's authoritative documentation before marking any configuration "correct".**

Do **not** assume:
- Port 465 = any encryption is acceptable
- Default encryption (none) passes just because the host and port fields are filled

Port semantics:
- `465` = **implicit SSL** (SSL handshake BEFORE any protocol exchange) — use `smtp_encryption=ssl`
- `587` = **STARTTLS** — use `smtp_encryption=tls`
- `25` / `2525` = plaintext or opportunistic STARTTLS — provider-specific

PHPMailer behavior:
- `SMTPSecure=''` + `SMTPAutoTLS=true` on port 465 will attempt STARTTLS upgrade, **not** implicit SSL.
- Beget port 465 requires `SMTPSecure='ssl'` (implicit TLS).
- Result of wrong setting: connection failure or TLS negotiation failure, no mail, no useful Admin error.

**Anti-patterns (SMTP):**

| Code | Description |
|------|-------------|
| SMTP-001 | Guessing provider port/encryption without verifying from authoritative source |
| SMTP-002 | Marking configured settings as verified without running an actual SMTP test |
| SMTP-003 | Leaving pre-cutover suppression MU active after SMTP activation |
| SMTP-004 | Calling SMTP acceptance "delivery" — use MAIL_ACCEPTED not MAIL_DELIVERED |
| SMTP-005 | Enabling production mail before controlled verification |

**CONFIGURED ≠ VERIFIED ≠ ACTIVE** — these are three distinct states in the lifecycle.

---

*FW-S-13 v1.4 — P18D: provider parameter verification, SMTP state machine, anti-patterns SMTP-001–005.*
