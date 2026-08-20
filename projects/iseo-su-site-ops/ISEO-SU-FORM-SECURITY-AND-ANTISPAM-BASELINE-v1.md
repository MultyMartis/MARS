# ISEO-SU FORM SECURITY AND ANTISPAM BASELINE v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-FORMS-ANTISPAM-AND-VALIDATION-01  
**Updated:** 2026-08-20  
**Authority:** current form/security operating baseline for public leads on `https://i-seo.su/`

## 1. Status

**COMPLETE — ISEO-SU FORMS HARDENED / EMPTY SUBMISSIONS BLOCKED / ANTISPAM ACTIVE / MAIL ROUTING RESTORED**

Server-side validation and layered anti-spam are authoritative. Client `required` attributes are convenience only. Temporary mail test mode is **OFF**. Operator address `im.work@nail.ru` is permanently included in the production recipient set.

## 2. Form Inventory

| FORM_ID | PUBLIC_ROUTE(S) | FORM_NAME | SOURCE_TEMPLATE | ACTION/HANDLER | METHOD | STATUS |
|---------|-----------------|-----------|-----------------|----------------|--------|--------|
| callback | `/`, `/contacts.html`, marketing chrome, many static pages | Заявка обратной связи | static HTML / theme chrome | `callback__FORM.php` (+ service-tree delegates) | POST AJAX | HARDENED |
| page | page-specific lead surfaces | Page lead | page HTML | `page__FORM.php` | POST AJAX | HARDENED |
| audit | audit CTAs / services | Заявка на бесплатный аудит | page HTML | `audit__FORM.php` | POST AJAX | HARDENED |
| calc | `/tariff-calc`, homepage calc | Calculator lead | calc UI | `calc__FORM.php` | POST AJAX | HARDENED |
| tariff_1..4 | tariff cards / slider | Tariff lead | tariff markup | `tariff_{1..4}__FORM.php` | POST AJAX | HARDENED |
| bonus | `/bonuses.html` | Bonus | page | `bonus__FORM.php` | POST AJAX | HARDENED |
| career | `/career.html` | Career | page | `career__FORM.php` | POST AJAX | HARDENED |
| partners | `/partners.html` | Partners | page | `partners__FORM.php` | POST AJAX | HARDENED |
| review | `/reviews.html` | Review | page | `review__FORM.php` | POST AJAX | HARDENED |

**Root handlers discovered:** 12.  
**Service-tree copies:** thin `require` delegates to root handlers under `services/**`.  
**Shared client:** `js/common.js` (ISEO_FORM_SECURITY_V1 block).  
**WordPress-native form plugins:** not used for these public leads (Akismet inactive historically).

## 3. Handler Architecture

```
Browser form
  -> js/common.js (AJAX POST + honeypot/token inject)
  -> *__FORM.php (thin wrapper)
  -> iseo-form-security.php (validate + anti-spam + mail)
  -> iseo-form-config.php (recipients / thresholds / test_mode)
  -> PHP mail()
```

Token endpoint: `iseo-form-token.php` returns signed `{t,s,id}` JSON.  
Runtime state dir: `.iseo-form-runtime/` (Deny via `.htaccess`) for rate/dup/event markers — **no full PII bodies**.

Canonical MARS mirror: `production-source/forms/` + `production-source/js/common.js`.

## 4. Required Field Rules

Per-form minimum viable submission (server authoritative; whitespace rejected):

| Form | Required (typical) | Notes |
|------|--------------------|-------|
| callback | name, method, contact | method/contact must be plausible pair; aliases accepted for known markup typos |
| page | name + contact (and form-specific fields as defined in helper) | |
| audit | name, contact, site (when audit semantics require URL) | comment optional |
| calc | calc lead identity fields as defined in helper | calculator business math unchanged |
| tariff_* | name + contact (+ tariff context fields) | |
| bonus / career / partners / review | name + contact (form-specific extras when present) | |

Reject: all-empty, punctuation-only, below min length, invalid email when method/type is email, array-where-scalar, oversized fields.

## 5. Server-Side Validation

Shared helper: `iseo-form-security.php`.

- trim + normalize line endings;
- scalar enforcement / length caps;
- POST-only;
- required field presence;
- contact heuristics (phone / email / Telegram — not over-strict for intl);
- HTML escape for mail body;
- generic client error body `false` (AJAX contract) / neutral messaging via JS;
- no internal PHP errors to client.

## 6. Anti-Spam Layers

A honeypot · B min fill time · C rate limit · D light content heuristics · E duplicate suppression.  
**No CAPTCHA** in this baseline. Do not add third-party CAPTCHA without a new charter after evidence.

## 7. Honeypot

Field name: `contact_company_url` (controlled convention).  
Injected by JS; CSS-hidden / aria-hidden.  
Server rejects when **missing** (direct bot POST) **or** **populated**.

## 8. Minimum Fill Time

Signed token (`t` timestamp + `s` HMAC + form `id`) issued by `iseo-form-token.php`.  
Threshold ≈ **3 seconds**. Too-fast submissions rejected. Plain client timestamps alone are not trusted.

## 9. Rate Limiting

Per IP + form identity, file-backed under `.iseo-form-runtime/`:

- ≈ **3 / 5 minutes** / form / IP  
- ≈ **10 / hour** / IP  

Conservative; not a permanent IP deny-list.

## 10. Duplicate Protection

After successful mail, same normalized payload fingerprint from same source suppressed ≈ **10 minutes** (no second mail). Long-period legitimate repeats allowed.

## 11. Mail Recipient Authority

Single config: `iseo-form-config.php`.

- `production_recipients` — normal routing (includes prior primary + `im.work@nail.ru`)  
- `test_recipients` — only used when `test_mode === true`  
- Do **not** hardcode recipients inside every handler.

Do not print full recipient lists in public REPORT/docs beyond operator-supplied test address when needed.

## 12. Test Mail Mode

Set `"test_mode" => true` only for controlled tests.  
While ON: mail **only** to `im.work@nail.ru` (no CC/BCC to production recipients).  
Must be reverted to `false` before declaring COMPLETE.  
Do not commit active test mode as final production state.

## 13. Production Mail State

| Field | Value |
|-------|-------|
| test_mode | **false** |
| im.work@nail.ru in production_recipients | **YES** |
| Prior legitimate recipients | **preserved** |
| CAPTCHA | **not installed** |

## 14. Security Boundaries

Handlers must continue to block: CRLF/header injection, arbitrary recipient injection, uncontrolled From, HTML injection into mail, GET submissions, direct POSTs without token/honeypot semantics.  
Do not expand into full pentest under ordinary edits.

## 15. Future Editing Rules

1. Prefer changing shared `iseo-form-security.php` / `iseo-form-config.php` over duplicating logic in wrappers.  
2. Keep service-tree copies as `require` delegates to root.  
3. After production mutation: promote to `production-source/forms/` (+ `js/common.js` if touched).  
4. Reconcile Protected Zones + this baseline before automation overwrite.  
5. No CAPTCHA / no broad IP hard-block as primary fix without charter.  
6. Never leave `test_mode` on.

## 16. Rollback

1. Restore scoped pre-change backups of each mutated production file from the task backup set.  
2. Or re-upload previous SHA-known versions from backup receipts.  
3. Confirm `test_mode` false and recipients restored.  
4. Promote rolled-back state into MARS source if rollback is lasting.

Local operational scratch (not Git authority): `X:\AI MARS\local\sites\iseo-su-production\_form-antispam-01-tmp\`.
