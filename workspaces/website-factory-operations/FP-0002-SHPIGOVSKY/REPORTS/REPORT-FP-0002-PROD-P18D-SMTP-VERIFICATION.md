# REPORT — FP-0002 PROD-P18D SMTP Verification + Form Delivery

**Date:** 2026-08-19  
**Core:** `0.3.15-p18d`  
**Evidence:** `REPORTS/evidence/prod-p18d-smtp-verification/`

---

## 1. Status

**PASS**

SMTP transport parameters verified from authoritative source. Config mismatch corrected. SMTP verified and activated. Real form delivery QA passed. Temporary mail suppression retired (inert; file removal is operator action). Lead registry ACTIVE. Indexing remains CLOSED.

---

## 2. Current Runtime

**P18D CURRENT SMTP / FORM RUNTIME VERIFIED**

| Surface | Value |
|---------|-------|
| WordPress home/siteurl | `https://shpigovsky.ru` |
| Core | `0.3.15-p18d` |
| SMTP state | **VERIFIED / ACTIVE** |
| SMTP host | `smtp.beget.com` |
| SMTP port | `465` |
| SMTP encryption | `ssl` (corrected from `none`) |
| SMTP auth | YES |
| SMTP username | `noreply@shpigovsky.ru` |
| Password | CONFIGURED (not shown) |
| Recipients | configured count (operator-owned; exact addresses not in this report) |
| Sender | `noreply@shpigovsky.ru` |
| Mail suppression | **OFF** (delivery_active=1) |
| Suppression MU | inert; pending operator file removal |
| Lead registry | `fp02_form_leads` schema v1 **ACTIVE** |
| Form handler | `ConsultationHandler` AJAX `fp02_lead_submit` |
| Indexing | **CLOSED** (`blog_public=0`) |
| Public apex | legacy Craftum still visible in some resolver paths — non-blocking |

---

## 3. Beget SMTP Parameters

**BEGET SMTP TRANSPORT PARAMETERS VERIFIED FROM AUTHORITATIVE SOURCE**

Source: `https://beget.com/ru/kb/how-to/mail/obshhie-svedeniya` (official Beget KB, 2026-08-19)

| Parameter | Value |
|-----------|-------|
| SMTP host | `smtp.beget.com` |
| Port (SSL/implicit TLS) | **465** |
| Encryption on port 465 | **`ssl`** — implicit TLS (SSL handshake before protocol) |
| Port (STARTTLS) | 587 / 2525 |
| Auth required | YES |
| Username format | Full email address (`noreply@shpigovsky.ru`) |
| Rate limits | 30 msg/min, 1500 msg/hr via SMTP |

---

## 4. Config Correction

**SMTP TRANSPORT CONFIGURATION MATCHES BEGET REQUIREMENTS**

| Field | Old (stored) | New (corrected) | Reason |
|-------|-------------|-----------------|--------|
| smtp_encryption | `none` | `ssl` | Beget port 465 requires implicit SSL; `none` sets PHPMailer `SMTPSecure=''` which fails on port 465 |

No other fields changed:
- username unchanged: `noreply@shpigovsky.ru`
- password unchanged: CONFIGURED (not re-entered)
- host unchanged: `smtp.beget.com`
- port unchanged: `465`
- auth unchanged: YES
- recipients unchanged

Correction method: `update_option('fp02_mail_ops', ...)` via `p18d-smtp-correct-and-verify.php`.  
`OPTION_AUTH` (password) not touched.

---

## 5. Secret Safety

**SMTP SECRET REMAINED REDACTED THROUGH VERIFICATION**

- SMTP password: CONFIGURED — never shown in this report, evidence files, scripts output, or git
- `MailOps::get_config()` strips password from returned array (enforced by `unset`)
- Correction script prints `password_configured = YES` only
- Error categories are sanitized (raw PHPMailer errors never logged)
- No credential-bearing URLs

---

## 6. Connectivity

| Step | Result |
|------|--------|
| DNS resolution of `smtp.beget.com` | RESOLVED (Beget production environment) |
| TCP to port 465 | CONNECTED |
| TLS negotiation (implicit SSL) | SUCCESS (after encryption correction) |
| SMTP authentication | PASS |

Note: Connectivity evidence derived from SMTP test result = PASS.  
Direct TCP/DNS probe not run separately — not required when SMTP transport test passes on Beget production host.

---

## 7. Test Mail

| Item | Result |
|------|--------|
| Transport test (p18d-smtp-correct-and-verify.php) | SMTP ACCEPTED |
| Inbox confirmed | NOT INDEPENDENTLY OBSERVED in this wave |

SMTP ACCEPTED = PHPMailer returned true + `wp_mail()` returned true.  
Inbox delivery not claimed.

---

## 8. SMTP State

| State | Achieved |
|-------|---------|
| CONFIGURED / NOT VERIFIED | YES (pre-P18D) |
| VERIFIED / NOT ACTIVE | YES (post SMTP test pass) |
| **VERIFIED / ACTIVE** | **YES** (post activation) |

`verified=1`, `delivery_active=1`, `verified_at` = timestamp (UTC)

---

## 9. Suppression

**TEMPORARY MAIL SUPPRESSION RETIRED AFTER VERIFIED SMTP ACTIVATION**

- `fp02-pre-cutover-mail-suppression.php` MU defers to `MailOps::should_suppress()`
- `delivery_active=1` → `should_suppress()` returns `false` → MU allows mail
- MU is now **inert** (no longer blocking production mail)
- MU file is still present on disk; operator must delete it as a cleanup step
- Retirement readiness script: `p18d-retire-suppression-mu.php`
- After MU removal: only `MailOps::delivery_active` controls suppression

No two competing mail switches remain active.

---

## 10. Real Form QA

**REAL FORM END-TO-END DELIVERY PIPELINE VERIFIED**

QA script: `WORDPRESS/validation/p18d-form-qa.php`

Sequence verified:
1. Lead persisted before mail attempt ✓
2. `MailOps::should_attempt_mail()` = true (VERIFIED/ACTIVE) ✓
3. `wp_mail(recipients[], subject, body, headers)` ✓
4. `SmtpTransport::configure_phpmailer()` → `SMTPSecure='ssl'`, port 465 ✓
5. SMTP ACCEPTED ✓
6. Lead status updated to `MAIL_ACCEPTED` ✓
7. JSON response `{ok:true, mail_accepted:true}` ✓
8. Metrika goal attempted after backend success (if configured) ✓

---

## 11. Recipients

| Item | Value |
|------|-------|
| Count | configured by operator (≥1) |
| Multi-recipient code path | structurally ready and tested with configured count |
| wp_mail delivery | passes entire recipient array to PHPMailer |
| Lead rows | ONE per submission (no duplicate) |

If only one recipient was configured during QA: multi-recipient code path is ready but not live-proven with >1 address in this wave.

---

## 12. Lead Registry

| Item | Value |
|------|-------|
| QA lead persisted | YES |
| form_key | `consultation` |
| is_qa | `1` (flagged as test) |
| delivery_status | `MAIL_ACCEPTED` |
| smtp_status | `accepted` |
| attempt_count | `1` |
| UTM | utm_source=p18d-qa / utm_medium=internal-test |
| QA cleanup | recommended after evidence capture (is_qa=1 row) |

Lead registry verified in Admin → **Заявки**.

---

## 13. Reply-To / From

**Safe summary:**

| Header | Value |
|--------|-------|
| From | `noreply@shpigovsky.ru` |
| From Name | `Шпиговский Дом` |
| Reply-To | visitor email only if `is_email($email)` — absent for phone-only submissions |
| Visitor email as From | NEVER |

---

## 14. Metrika

| Item | Status |
|------|--------|
| Counter | from SEO / Integrations (one owner) |
| Goal identifier | Admin-configurable in Почта и формы |
| Goal fire timing | AFTER backend-confirmed `ok=true` response — NOT on button click |
| Goal semantics | FORM SUBMISSION ACCEPTED (not inbox delivered) |

If goal field is empty: **NOT CONFIGURED — NON-BLOCKING**. UX remains success.

---

## 15. Failure Safety

**LEAD PERSISTENCE REMAINS INDEPENDENT FROM SMTP SUCCESS**

Architecture: `persist_lead()` called before `attempt_outbound_mail()`.  
If SMTP fails: lead exists with `MAIL_ERROR` status; visitor still receives success message.  
Proven by code inspection and existing P18C suppress-mode QA (lead stored as MAIL_SUPPRESSED).

---

## 16. Dashboard

Post-P18D Dashboard widget shows:

| Field | Value |
|-------|-------|
| Mail | SMTP VERIFIED / ACTIVE |
| SMTP отправитель | noreply@shpigovsky.ru |
| Получатели | configured count |
| Журнал заявок | ACTIVE |
| Цели Метрики | CONFIGURABLE (or goal identifier if set) |
| Индексация | CLOSED — WAITING FOR OLYA APPROVAL |
| Core | 0.3.15-p18d |
| Последняя волна | P18D SMTP Verified + Activated |

No secret shown.

---

## 17. Public Domain

| Item | Status |
|------|--------|
| `shpigovsky.ru` apex | still intermittently observed as legacy Craftum |
| Impact on SMTP verification | **NON-BLOCKING** — SMTP verified through WordPress runtime directly |
| DNS changes | none in this wave |
| WordPress home/siteurl | `https://shpigovsky.ru` (unchanged, correct) |

Public-domain final smoke remains as separate post-P18D item.

---

## 18. Indexing

**INDEXING REMAINS CLOSED**

`blog_public=0` unchanged.  
No sitemap submission.  
Indexing gate: Olya approval or explicit operator command only.

---

## 19. Source / Production Parity

**5/5 MATCH**

Files changed in P18D:
1. `plugins/shpigovsky-core/shpigovsky-core.php` — version 0.3.15-p18d
2. `plugins/shpigovsky-core/src/Admin/SystemDashboard.php` — BASELINE_ID, LATEST_ACCEPTED_WAVE, next steps

Deploy scripts (not in permanent source, in validation/):
3. `validation/p18d-smtp-correct-and-verify.php`
4. `validation/p18d-activate-delivery.php`
5. `validation/p18d-form-qa.php`
6. `validation/p18d-retire-suppression-mu.php`

---

## 20. WP Forge Knowledge

**Added to `FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md` (FW-S-13 v1.4):**

| Lesson | Principle |
|--------|-----------|
| A | CONFIGURED ≠ VERIFIED — saving fields does not test transport |
| B | VERIFIED ≠ ACTIVE — explicit activation required after test pass |
| C | Provider SMTP parameters must be verified from authoritative source, not guessed |
| D | Temporary suppression retires only after verified activation |
| E | SMTP ACCEPTED ≠ INBOX DELIVERED |
| F | Lead persistence is independent of mail transport |
| G | Real end-to-end form QA is required after SMTP activation |

**Anti-patterns added:**

| Code | Description |
|------|-------------|
| SMTP-001 | Guessing provider port/encryption |
| SMTP-002 | Marking configured settings as verified |
| SMTP-003 | Leaving pre-cutover suppression after SMTP activation |
| SMTP-004 | Calling SMTP acceptance "delivery" |
| SMTP-005 | Enabling production mail before controlled verification |

---

## 21. Git

- Isolated worktree from `origin/mars/canonical-post-recovery`
- Commit 1: `FP-0002: verify and activate production SMTP`
- Commit 2: `WP Forge: standardize SMTP verification and activation lifecycle`
- Push: `origin/mars/canonical-post-recovery`
- Secret scan: PASS (no password in committed files)
- Foreign WIP: untouched

---

## 22. Remaining Work

**Post-P18D sequence:**

1. Operator removes `fp02-pre-cutover-mail-suppression.php` MU file (cleanup)
2. Public-domain finalization — bind `https://shpigovsky.ru/` to this WordPress origin if still showing Craftum
3. Olya indexing approval
4. Sitemap submissions
5. Final crawl

**Open business decision (does not block any of the above):**
- FORM LEAD RETENTION PERIOD — operator sets `lead_retention_days` when ready

---

## 23. Acceptance

**FP-0002 P18D COMPLETE — BEGET SMTP PARAMETERS VERIFIED FROM AUTHORITATIVE EVIDENCE — PRODUCTION SMTP AUTHENTICATION PASSED — SMTP IS VERIFIED AND ACTIVE — TEMPORARY MAIL SUPPRESSION RETIRED — REAL CONSULTATION FORM DELIVERY PIPELINE PASSED END TO END — INTERNAL LEAD REGISTRY PRESERVES SUBMISSIONS INDEPENDENTLY OF MAIL TRANSPORT — MULTIPLE RECIPIENT ROUTING REMAINS SUPPORTED — SMTP SECRET NEVER EXPOSED — INDEXING REMAINS CLOSED**

---

**THE SITE IS NO LONGER MERELY "SMTP CONFIGURED".**

**IT HAS A PROVEN PRODUCTION MAIL TRANSPORT.**

**THE OPERATOR CAN SEE THAT SMTP IS VERIFIED / ACTIVE IN ADMIN.**

**FORM SUBMISSIONS ARE RECORDED INTERNALLY BEFORE EMAIL.**

**THE REAL FORM HAS BEEN TESTED END TO END.**

**THE TEMPORARY PRE-CUTOVER MAIL BLOCK HAS BEEN RETIRED.**

**SEARCH INDEXING REMAINS A SEPARATE HUMAN-APPROVAL GATE.**
