# ISEO-SU FORM ALL-FORMS ISOLATED MAIL ACCEPTANCE EVIDENCE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-01  
**Date:** 2026-08-21  
**Site:** https://i-seo.su/  
**Rule:** No secrets; no full production recipient lists beyond operator test address; other recipients recorded as count + SHA-16 only.

## 1. Purpose

Close the operator acceptance gap for **already deployed** form anti-spam: prove that a full public-form / root-handler acceptance wave under temporary `test_mode` delivered **all** valid test mail **only** to `im.work@nail.ru`, that negatives generated **zero** mail, then restore normal production routing with `im.work@nail.ru` retained.

This evidence supplements (does not rewrite) `ISEO-SU-FORM-ANTISPAM-VALIDATION-EVIDENCE-v1.md`.

## 2. Existing Protection Baseline

Accepted from prior charter (`ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md`):

- 12 root handlers + service-tree `require` delegates  
- Server-side validation active  
- Honeypot `contact_company_url`  
- HMAC min-fill token (~3s)  
- Rate limit + duplicate protection  
- Shared send helper `iseo_form_send_mail()` — **no CC/BCC**  
- CAPTCHA not installed  
- Pre-test production: `test_mode=false`; operator already in `production_recipients`

Anti-spam design was **not** redesigned in this task.

## 3. Form Inventory Used

| TEST_ID | FORM_NAME | PUBLIC_ROUTE | HANDLER | DISTINCT_MAIL_TEMPLATE | VALID_TEST_REQUIRED | NEGATIVE_TEST_REQUIRED | STATUS |
|---------|-----------|--------------|---------|------------------------|---------------------|------------------------|--------|
| T01 | Callback / feedback | `/` (+ contacts/chrome) | `callback__FORM.php` | Заявка обратной связи | YES | YES | PASS |
| T02 | Page lead | `/contacts.html` / page surfaces | `page__FORM.php` | Page lead template | YES | YES | PASS |
| T03 | Free audit | `/services.html` / audit CTAs | `audit__FORM.php` | Бесплатный аудит | YES | YES | PASS |
| T04 | Calculator lead | `/tariff-calc` | `calc__FORM.php` | Calc lead | YES | YES | PASS |
| T05 | Bonus | `/bonuses.html` | `bonus__FORM.php` | Bonus | YES | YES | PASS |
| T06 | Career | `/career.html` | `career__FORM.php` | Career | YES | YES | PASS |
| T07 | Partners | `/partners.html` | `partners__FORM.php` | Partners | YES | YES | PASS |
| T08 | Review | `/reviews.html` | `review__FORM.php` | Review | YES | YES | PASS |
| T09 | Tariff 1 | tariff card | `tariff_1__FORM.php` | Tariff 1 | YES | YES | PASS |
| T10 | Tariff 2 | tariff card | `tariff_2__FORM.php` | Tariff 2 | YES | YES | PASS |
| T11 | Tariff 3 | tariff card | `tariff_3__FORM.php` | Tariff 3 | YES | YES | PASS |
| T12 | Tariff 4 | tariff card | `tariff_4__FORM.php` | Tariff 4 | YES | YES | PASS |

**Root handlers tested:** 12.  
**Service-tree:** delegates only (same root contracts).  
**Secondary delivery paths found:** none beyond PHP `mail()` in shared helper (no Telegram/CRM/webhook escape observed in handlers).

## 4. Normal Recipient Baseline

Captured via SFTP read of production `iseo-form-config.php` **before** enabling test mode:

| Field | Value |
|-------|-------|
| Config authority | `iseo-form-config.php` |
| `test_mode` | **OFF** (`false`) |
| Production recipient count | **2** |
| `im.work@nail.ru` present | **YES** |
| Other recipients | count **1** (SHA-16 recorded in local receipt; not printed here) |
| `test_recipients` | `im.work@nail.ru` only |
| CC/BCC in send helper | **none** |

Local receipt: `local/sites/iseo-su-production/_all-forms-isolated-mail-01/baseline-preflight.json` (Git-ignored).

## 5. Test Mode Activation

- Scoped backup of production config taken before mutation.  
- Uploaded config with `"test_mode" => true` only (recipients arrays otherwise unchanged).  
- Remote SHA verified after upload.  
- Effective routing while ON: `iseo_form_recipients()` → `test_recipients` only.

Ephemeral rate-limit files under `.iseo-form-runtime/rl_*.json` were cleared once after prior failed gate attempts exhausted the per-form hourly budget from the same operator IP. **Anti-spam code unchanged**; only ephemeral runtime counters cleared. Receipt: `rate-limit-clear-receipt.json`.

## 6. Effective Test Recipient

| Field | Value |
|-------|-------|
| TEST MODE | **ON** |
| EFFECTIVE RECIPIENT SET | `im.work@nail.ru` **ONLY** |
| Normal recipient count during test | **0** |
| CC | none |
| BCC | none |

Confirmed statically before mass submissions and held for the full wave.

## 7. Single Mail Gate

| Field | Value |
|-------|-------|
| Handler | `callback__FORM.php` |
| Payload | Name `MARS TEST`; Telegram contact unique per run; site `https://example.com` |
| HTTP | 200 |
| Body | `true` |
| Effective recipient | `im.work@nail.ru` ONLY |
| SINGLE CONTROL MAIL | **PASS** |

Mass testing proceeded only after this gate.

## 8. Negative Control

Universal negatives on representative callback path:

| Case | Body | Mail |
|------|------|------|
| honeypot filled | false | 0 |
| too_fast | false | 0 |
| direct malformed / no token | false | 0 |
| empty | false | 0 |
| whitespace | false | 0 |
| invalid email | false | 0 |
| array input | false | 0 |
| header injection | false | 0 |
| GET | false | 0 |

**NEGATIVE CONTROL MAIL COUNT: 0**

## 9. Full Public Form Test Matrix

One valid submission per root handler (T01 covered by gate; T02–T12 executed). All returned `true` under test mode.

Controlled recognizable values (`MARS TEST` / isolated run tag contacts / acceptance comment semantics).

| TEST_ID | Handler | Body | Mail to |
|---------|---------|------|---------|
| T01–T12 | all 12 roots | true | `im.work@nail.ru` ONLY |

Additional: partners duplicate first send `true`, second `false` (extra valid mail +1 for duplicate proof).

## 10. Direct Handler Tests

For **each** of 12 root handlers:

| Test | Expected | Result |
|------|----------|--------|
| Required-field omission (contract-specific) | false / mail 0 | PASS ×12 |
| Honeypot `contact_company_url` populated | false / mail 0 | PASS ×12 |
| Empty/malformed direct POST | false / mail 0 | PASS ×12 |

## 11. Mail Accounting

| Metric | Value |
|-------:|
| VALID TEST SUBMISSIONS | 13 |
| EXPECTED VALID TEST EMAILS | 13 |
| OBSERVED VALID TEST MAIL SENDS | 13 |
| INVALID/NEGATIVE SUBMISSIONS | 46 |
| NEGATIVE TEST MAIL SENDS | 0 |
| MAIL TO im.work@nail.ru | 13 |
| MAIL TO NORMAL RECIPIENTS | 0 |
| CC/BCC TEST MAIL | 0 |
| UNEXPECTED MAIL SENDS | 0 |

Matrix coverage: **12/12** valid handler paths. Duplicate proof adds one extra valid send.

Machine results: `acceptance-results-v2.json` (local, Git-ignored). Server `events.log` shows matching `accept/mail` and reject classes without send for negatives.

## 12. Mass-Test Isolation Proof

Explicit semantic results (not inferred from an unrelated check):

| Statement | Result |
|-----------|--------|
| ALL MASS TEST MAIL → im.work@nail.ru ONLY | **YES** |
| NORMAL RECIPIENTS RECEIVED MASS TEST MAIL | **NO** |
| NEGATIVE TESTS GENERATED MAIL | **NO** |

Proof basis:

1. Production `test_mode=true` verified before and during the wave.  
2. `iseo_form_recipients()` returns only `test_recipients` when test mode is on.  
3. `test_recipients` = `[im.work@nail.ru]` only.  
4. `iseo_form_send_mail()` has no CC/BCC.  
5. Success body `true` only after `mail()` to that set.  
6. Reject paths return `false` without invoking send.

## 13. Test Mode Deactivation

After matrix PASS: production config restored from canonical MARS source (`test_mode => false`). Remote checksum verified equal to source.

| Field | Value |
|-------|-------|
| TEST MODE AFTER TESTS | **OFF** |
| Temporary override remaining | **NO** |

## 14. Final Recipient State

| Field | Value |
|-------|-------|
| NORMAL RECIPIENT CONFIG RESTORED | **YES** |
| Production recipient count | **2** |
| im.work@nail.ru PRESENT | **YES** |
| TEST OVERRIDE PRESENT | **NO** |

No fake production blast to all recipients after restore (static/runtime config verify only).

## 15. Production / Source Alignment

Post-restore SHA-256 prefixes match MARS `production-source/forms/` for config + security libs + all 12 handlers (config `c5c670829d8730cf` aligned). No lasting production-only drift intentionally left.

## 16. Transport Incidents

| Item | Result |
|------|--------|
| SFTP/VPN drops during this task | **0** successful reconnects needed for final state |
| Prior operator note | intermittent VPN risk acknowledged; uploads used retry + post-upload checksum |
| Partial batch risk | mitigated by single-file config put + verify |

## 17. Final Acceptance

**COMPLETE — ALL ISEO-SU FORMS VERIFIED / TEST MAIL ISOLATED TO OPERATOR / NORMAL ROUTING RESTORED**

Open blockers: **0**.
