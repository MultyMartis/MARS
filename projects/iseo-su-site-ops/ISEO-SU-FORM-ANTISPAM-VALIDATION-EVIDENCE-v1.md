# ISEO-SU FORM ANTISPAM VALIDATION EVIDENCE v1

> **Recipient note (2026-08-21):** Historical test/production operator address recorded here is the typo `im.work@nail.ru`. Current authority: `im.work@mail.ru` (Acceptance 02). Anti-spam validation results remain accepted.

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-FORMS-ANTISPAM-AND-VALIDATION-01  
**Date:** 2026-08-20  
**Rule:** No secrets; no full production recipient lists; operator test address may appear.

## Forms discovered

12 root public mail handlers: `callback`, `page`, `audit`, `calc`, `bonus`, `career`, `partners`, `review`, `tariff_1..4`.  
Plus service-tree relative copies under `services/**` (delegates after harden).  
Client shared: `js/common.js`.

## Handlers

Thin wrappers → `iseo-form-security.php` → `iseo-form-config.php` → `mail()`.  
Token: `iseo-form-token.php`. Runtime: `.iseo-form-runtime/`.

## Old validation defect

Handlers accepted POST and mailed with **no meaningful server validation**. Empty/whitespace/direct bot POSTs could generate mail (e.g. «Заявка обратной связи» with empty business fields). Client `required` / JS checks were bypassable.

## Protection implemented

Server required-field rules; honeypot `contact_company_url`; HMAC min-fill token (~3s); rate limits (~3/5min form+IP, ~10/hour IP); duplicate suppress (~10min); light heuristics; HTML escape; POST-only; generic reject.

## One-message gate result

| Item | Result |
|------|--------|
| Endpoint | `callback__FORM.php` |
| HTTP | 200 |
| Body | `true` |
| Intended recipient | `im.work@nail.ru` ONLY (test_mode ON) |
| PASS | **YES** |

## Negative test matrix

| Case | Body | Mail expected | PASS |
|------|------|---------------|------|
| empty | false | 0 | YES |
| whitespace | false | 0 | YES |
| honeypot filled | false | 0 | YES |
| too_fast | false | 0 | YES |
| bad_email | false | 0 | YES |
| array injection | false | 0 | YES |
| header injection | false | 0 | YES |
| direct no token | false | 0 | YES |
| GET | false | 0 | YES |

**NEGATIVE TEST MAIL COUNT: 0**

## Mass form test matrix

One valid submission per root handler under test_mode (12 expected mails). Empty/honeypot/duplicate spot checks PASS. See local `test-results.json` summary: `all_form_pass=true`, `valid_expected_mails=12`.

## Mail counts

| Metric | Value |
|--------|------:|
| Valid test submissions (handler gate) | 12 |
| Expected test emails | 12 |
| Observed handler success bodies (`true`) | 12 |
| Rejected requests (negatives + mass negatives) | all `false` |
| Normal-recipient test emails | **0** (test_mode override) |

## Test routing proof

While `test_mode=true`, config routed exclusively to `im.work@nail.ru`. No production CC/BCC path in shared send helper under test mode.

## Final routing proof

`test_mode=false` restored. Production recipient set count = **2** (prior primary preserved + `im.work@nail.ru`). Verified via config read after disable script. No fake production lead blast performed (operator-safe static verify).

## Production/source checksums (SHA-256 prefix)

| File | Align |
|------|-------|
| iseo-form-config.php | C5C670829D87 (prod build ≡ MARS source) |
| iseo-form-security.php | 79CE65855E8A |
| iseo-form-token.php | FF4D9BBE008C |
| callback__FORM.php | 9DF4EC07E73A |
| page__FORM.php | 58FFA998D4EF |
| audit__FORM.php | 3A8A965BA9A1 |
| calc__FORM.php | 1D17017BD5A9 |
| bonus__FORM.php | 32C65F3C131E |
| career__FORM.php | 21C8F5BFA000 |
| partners__FORM.php | 5E15EEE1CE16 |
| review__FORM.php | A21EB896AEC7 |
| tariff_1__FORM.php | 08733DE2161F |
| tariff_2__FORM.php | 3D429B8F1939 |
| tariff_3__FORM.php | 932C0E8CABB9 |
| tariff_4__FORM.php | 93047418E54C |
| js/common.js | 4F572D9AFB8C |

## Rollback

Scoped file backups under `X:\AI MARS\local\sites\iseo-su-production\_form-antispam-01-tmp\backups\` (78 files recorded in session inventory). Restore exact paths from backups; re-verify `test_mode` and recipients.
