# REPORT — ISEO-SU SITE OPS FORM ANTISPAM AND VALIDATION 01

**Task ID:** ISEO-SU-SITE-OPS-FORMS-ANTISPAM-AND-VALIDATION-01  
**Date:** 2026-08-20  
**Site:** https://i-seo.su/

## 1. Execution Summary

Public lead forms on i-seo.su were hardened with shared server-side validation and layered anti-spam. Empty/malformed submissions no longer mail. Controlled testing used temporary routing to `im.work@nail.ru` only; test mode was then disabled; that address was permanently added to production recipients. MARS source mirrors production. CAPTCHA was not introduced.

**FINAL STATUS:** COMPLETE — ISEO-SU FORMS HARDENED / EMPTY SUBMISSIONS BLOCKED / ANTISPAM ACTIVE / MAIL ROUTING RESTORED

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Staged at start | empty |
| Foreign WIP | present (unrelated) — preserved / not staged |
| Prior origin tip noted in stabilization | `dd59de28` (verified as local `origin/mars/canonical-post-recovery` tip before this wave's push) |

## 3. Incident Symptoms

Spam / nonsense values; empty business fields on «Заявка обратной связи» and related forms; multiple form types affected (callback, audit, others).

## 4. Form Inventory

12 root handlers + service-tree delegates + `js/common.js`. Full matrix in `ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md` §2.

## 5. Root Cause

Server handlers mailed on POST existence without meaningful validation. Frontend `required` / JS checks were not authoritative. Direct bot POSTs and empty strings could still generate mail.

## 6. Existing Mail Architecture

Standalone PHP handlers using host `mail()`; shared client AJAX in `common.js`. Recipient authority centralized into `iseo-form-config.php` during this task. No WordPress form-plugin pipeline for these leads.

## 7. Server-Side Validation

Implemented in `iseo-form-security.php`: trim/normalize, required rules per form, contact checks, length caps, scalar enforcement, POST-only, HTML escape, safe reject (`false`).

## 8. Anti-Spam Design

Invisible layers only: honeypot, signed min-fill time, rate limit, light heuristics, duplicate suppression. No CAPTCHA.

## 9. Honeypot

`contact_company_url` — reject if missing or filled.

## 10. Minimum Fill Time

HMAC token via `iseo-form-token.php`; ≈3s threshold.

## 11. Rate Limiting

≈3/5min per form+IP; ≈10/hour per IP; file store under `.iseo-form-runtime/`.

## 12. Duplicate Protection

≈10 minutes same normalized payload suppress after successful send.

## 13. Temporary Test Routing

`test_mode=true` forced all test mail to `im.work@nail.ru` only. No normal recipients during test phase.

## 14. Single Mail Gate

`callback__FORM.php` → body `true` → PASS; intended ONLY `im.work@nail.ru`.

## 15. Negative Tests

empty / whitespace / honeypot / too_fast / bad_email / array / header injection / direct_no_token / GET — all `false`; mail count 0.

## 16. Full Form Test Matrix

Valid once per root handler (12) under test mode — all PASS. Spot empty/honeypot/duplicate — PASS. Summary: `all_form_pass=true`.

## 17. Final Recipient State

| Field | Value |
|-------|-------|
| test_mode | OFF (`false`) |
| im.work@nail.ru in production set | YES |
| Prior legitimate recipients | preserved |
| Fake production blast | NOT SENT (static config verify) |

## 18. Production Deployment

Exact form/security/JS files deployed over SFTP with scoped backups and checksums. Service copies converted to root `require` delegates. Resume deploy completed after initial `common.js` drop.

## 19. Production Validation

Handlers reject empty/honeypot/direct malformed POST. Valid path returns `true` under test mode. Config restored. Token endpoint and `common.js` marker `ISEO_FORM_SECURITY_V1` present. Bounded smoke: `/`, `/services.html`, `/blog/`, `/tariff-calc`, `/offers`, `/glossary/`, contacts/forms surfaces — no unrelated regression observed for this charter.

## 20. Site Regression

No glossary/SEO/layout/calculator-business-logic/WPilot/nav/sitemap/robots changes.

## 21. Files Created or Updated

**MARS:**

- `production-source/forms/*` (handlers + libs + README)
- `production-source/js/common.js`
- `ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md`
- `ISEO-SU-FORM-ANTISPAM-VALIDATION-EVIDENCE-v1.md`
- `reports/REPORT-ISEO-SU-SITE-OPS-FORM-ANTISPAM-AND-VALIDATION-01.md`
- updates: `ISEO-SU-CURRENT-STATE-v1.md`, `OPERATIONAL-INDEX.md`, `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`, `ISEO-SU-PROTECTED-ZONES-v1.md`, `ISEO-SU-FORMS-CALCULATORS-AND-WEB-KP-MAP-v1.md`

**Production (docroot):** matching PHP libs/handlers/token, `.iseo-form-runtime/`, `js/common.js`, service-tree delegates.

## 22. Production Mutations

Bounded to form/security/mail-config/JS surfaces named in charter. DB mutation: none.

## 23. Rollback

Restore files from `_form-antispam-01-tmp/backups/` (scoped per-file backups). Re-verify recipients and `test_mode`.

## 24. Git Persistence

Scoped commit on allowlisted paths only; foreign WIP excluded.

| Item | Value |
|------|-------|
| Local commit (dirty-main lineage) | `444d8a45` |
| Remote synced commit | `cee143df` |
| Method | clean worktree + cherry-pick onto remote tip `dd59de28` (histories had diverged; no force push) |
| Remote | `origin/mars/canonical-post-recovery` |
| Reachability | `git ls-remote` = `cee143df` |

## 25. Remaining Risks

Host `mail()` deliverability remains environment-dependent (SAFE UNKNOWN historically). Determined attackers may still try low-volume crafted posts; layers reduce empty/spam floods without CAPTCHA. HMAC secret lives in config — rotate under charter if leaked.

## 26. Final Decision

Accept form security baseline as current operating truth. Empty submission mail blocked. Anti-spam active. Mail routing restored with `im.work@nail.ru` included.

## 27. Stop Condition

STOP after inventory, root cause, validation, anti-spam, gated tests, restore, production validation, MARS docs/source, scoped Git + remote sync. No unrelated SEO/glossary work.

---

### FINAL HARD CHECK

```
PUBLIC FORMS DISCOVERED: 12 root handlers (+ service-tree delegates)
FORM HANDLERS DISCOVERED: 12 root (+ delegates)
EMPTY SUBMISSION MAIL POSSIBLE: NO
HONEYPOT ACTIVE: YES
SERVER VALIDATION ACTIVE: YES
RATE LIMIT ACTIVE: YES
DUPLICATE PROTECTION ACTIVE: YES
SINGLE TEST MAIL: PASS
SINGLE TEST RECIPIENT: im.work@nail.ru ONLY
NORMAL RECIPIENTS RECEIVED TEST MAIL: NO
NEGATIVE TEST MAIL COUNT: 0
FULL FORM TEST: PASS
FINAL TEST MODE: OFF
im.work@nail.ru IN FINAL RECIPIENT SET: YES
PRODUCTION/SOURCE ALIGNED: YES
OPEN BLOCKERS: 0
PRODUCTION MUTATIONS: YES (bounded form/security/JS)
REMOTE SYNC: COMPLETE (cee143df on origin/mars/canonical-post-recovery)
```
