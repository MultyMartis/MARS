# ISEO-SU FORM ALL-FORMS ISOLATED MAIL ACCEPTANCE EVIDENCE v2

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-02  
**Date:** 2026-08-21  
**Site:** https://i-seo.su/  
**Recipient-restore cross-check:** `ISEO-SU-FORM-RECIPIENT-RESTORATION-EVIDENCE-v1.md` (2026-08-21) is current authority for original-recipient reconstruction; independently **confirms** active original retained + `im.work@mail.ru`.  
**Rule:** No secrets; no full production recipient lists beyond the operator address; other recipients recorded as count + SHA-16 only.

## 1. Reason for Re-test

Acceptance 01 used operator typo address `im.work@nail.ru`. Anti-spam implementation remains accepted unless contradicted. **Operator mailbox-delivery acceptance must be repeated** with the correct mailbox `im.work@mail.ru`.

## 2. Address Correction

| Field | Value |
|-------|-------|
| Wrong address previously used | `im.work@nail.ru` |
| Correct operator address | `im.work@mail.ru` |
| Normalization / substitution | **none** — exact string used |

## 3. Previous Acceptance Supersession

| Artifact | Status |
|----------|--------|
| `ISEO-SU-FORM-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-EVIDENCE-v1.md` | HISTORICAL (factual typo address retained) |
| `reports/REPORT-ISEO-SU-SITE-OPS-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-01.md` | HISTORICAL — **recipient evidence SUPERSEDED BY ACCEPTANCE 02** |
| This file (v2) + REPORT 02 | **CURRENT** mail-delivery / recipient authority |

Historical REPORT/evidence 01 contents were **not** rewritten to pretend the typo never happened.

## 4. Production Recipient Baseline

Captured via SFTP before correction (local receipt `baseline-preflight.json`):

| Field | Value |
|-------|-------|
| Config authority | `iseo-form-config.php` |
| `test_mode` | **OFF** |
| Production recipient count | **2** |
| `im.work@mail.ru` present | **NO** |
| `im.work@nail.ru` present | **YES** (typo) |
| Other recipients | count **1** (SHA-16 in local receipt; not printed) |
| `test_recipients` | `im.work@nail.ru` only |
| CC/BCC in send helper | **none** |
| Root handlers | **12** |

## 5. Test Mode Activation

- Canonical MARS source corrected first (`production-source/forms/iseo-form-config.php`).  
- Scoped backup taken; production config uploaded with corrected recipients + `"test_mode" => true`.  
- Remote checksum verified.  
- Ephemeral `.iseo-form-runtime/rl_*.json` cleared once before the wave (anti-spam code unchanged).

## 6. Effective Correct Test Recipient

### MANDATORY PRE-SEND HARD CHECK

| Check | Result |
|-------|--------|
| TEST MODE | **ON** |
| EFFECTIVE RECIPIENT COUNT | **1** |
| EFFECTIVE RECIPIENT | `im.work@mail.ru` |
| `im.work@nail.ru` ACTIVE | **NO** |
| NORMAL RECIPIENTS ACTIVE DURING TEST | **NO** |
| CC / BCC | none |

## 7. Single Mail Gate

| Field | Value |
|-------|-------|
| Handler | `callback__FORM.php` |
| Name | `MARS TEST ACCEPTANCE 02` |
| Semantics | ISEO-SU correct-mailbox isolated acceptance |
| HTTP / body | 200 / `true` |
| Effective recipient | `im.work@mail.ru` ONLY |
| Proof level | **MAIL SEND ACCEPTED BY SERVER** (not operator-inbox observation) |
| SINGLE CONTROL MAIL | **PASS** |

## 8. Full 12-Form Matrix

| TEST_ID | Handler | Body | Mail to |
|---------|---------|------|---------|
| T01 | `callback__FORM.php` | true (gate) | `im.work@mail.ru` ONLY |
| T02 | `page__FORM.php` | true | `im.work@mail.ru` ONLY |
| T03 | `audit__FORM.php` | true | `im.work@mail.ru` ONLY |
| T04 | `calc__FORM.php` | true | `im.work@mail.ru` ONLY |
| T05 | `bonus__FORM.php` | true | `im.work@mail.ru` ONLY |
| T06 | `career__FORM.php` | true | `im.work@mail.ru` ONLY |
| T07 | `partners__FORM.php` | true | `im.work@mail.ru` ONLY |
| T08 | `review__FORM.php` | true | `im.work@mail.ru` ONLY |
| T09–T12 | `tariff_{1..4}__FORM.php` | true | `im.work@mail.ru` ONLY |

Partners duplicate proof: first `true`, second `false` (+1 valid mail).

**Matrix:** 12/12 PASS.

## 9. Negative Tests

Universal (callback): honeypot, too-fast, direct malformed, empty, whitespace, invalid email, array, header injection, GET — all `false`, mail 0.

Per root handler (×12): required-field omission, honeypot populated, empty/direct POST — all reject, mail 0.

**NEGATIVE MAIL SENDS = 0**

## 10. Mail Accounting

| Metric | Value |
|-------:|
| SINGLE CONTROL VALID SENDS | 1 |
| MASS VALID SUBMISSIONS | 12 matrix (+1 duplicate proof) |
| EXPECTED TOTAL VALID EMAILS | 13 |
| OBSERVED TOTAL VALID MAIL SENDS | 13 |
| NEGATIVE SUBMISSIONS | 46 |
| NEGATIVE MAIL SENDS | 0 |
| MAIL TO `im.work@mail.ru` | 13 |
| MAIL TO `im.work@nail.ru` | 0 |
| MAIL TO NORMAL RECIPIENTS | 0 |
| CC/BCC TEST MAIL | 0 |
| UNEXPECTED MAIL | 0 |

Machine results: `local/sites/iseo-su-production/_all-forms-isolated-mail-02/acceptance-results-v2.json` (Git-ignored).

## 11. Wrong-Address Zero-Mail Proof

| Statement | Result |
|-----------|--------|
| MAIL TO `im.work@nail.ru` | **0** |
| Wrong address in effective test set | **NO** |
| Wrong address in final production set | **NO** |

## 12. Normal-Recipient Isolation

| Statement | Result |
|-----------|--------|
| ALL MASS TEST MAIL → `im.work@mail.ru` ONLY | **YES** |
| NORMAL RECIPIENTS RECEIVED MASS TEST MAIL | **NO** |
| NEGATIVE TESTS GENERATED MAIL | **NO** |

Proof basis: `test_mode=true` → `iseo_form_recipients()` returns only `test_recipients` = [`im.work@mail.ru`]; send helper has no CC/BCC; success body `true` only after `mail()` to that set.

## 13. Test Mode Deactivation

Production config restored from corrected MARS source (`test_mode => false`). Remote SHA matched source.

| Field | Value |
|-------|-------|
| TEST MODE AFTER TESTS | **OFF** |
| Temporary override remaining | **NO** |

## 14. Final Production Recipient Set

| Field | Value |
|-------|-------|
| Production recipient count | **2** |
| `im.work@mail.ru` IN FINAL SET | **YES** (once) |
| `im.work@nail.ru` IN FINAL SET | **NO** |
| Other legitimate recipients | **preserved** (count 1) |
| Fake post-restore blast | **not performed** (static verify only) |

## 15. Production / Source Alignment

Config SHA-256 prefix `dea5b3482feb914f` — production ≡ `production-source/forms/iseo-form-config.php`. Handlers/security libs unchanged and remain aligned. No lasting production-only drift.

## 16. SFTP / VPN Incidents

**0** blocking transport incidents for baseline / enable / clear-RL / disable-restore / post-check. Resilient put/get with retry + checksum used.

## 17. Final Acceptance

**COMPLETE — ALL ISEO-SU FORMS RE-VERIFIED / CORRECT OPERATOR MAILBOX ACCEPTED / WRONG RECIPIENT REMOVED / NORMAL ROUTING RESTORED**

Anti-spam design was **not** redesigned. CAPTCHA was **not** introduced.
