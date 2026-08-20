# REPORT — ISEO-SU SITE OPS ALL-FORMS ISOLATED MAIL ACCEPTANCE 01

**Task ID:** ISEO-SU-SITE-OPS-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-01  
**Date:** 2026-08-21  
**Site:** https://i-seo.su/

## 1. Execution Summary

Executed the missing operator acceptance wave for already-deployed i-seo.su form anti-spam: temporarily routed all form mail to `im.work@nail.ru` only, passed a single controlled mail gate, ran negatives and full 12-handler public-form coverage, proved mass-test isolation, then disabled test mode and restored production recipients with `im.work@nail.ru` retained. Anti-spam design was not redesigned.

**FINAL STATUS:** COMPLETE — ALL ISEO-SU FORMS VERIFIED / TEST MAIL ISOLATED TO OPERATOR / NORMAL ROUTING RESTORED

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Local HEAD at start | `b44d8dc2` |
| Origin tip noted in charter | `1b29e932` (verified) |
| Staged | empty |
| Foreign WIP | present (unrelated) — preserved / not staged |
| Unpushed local lineage | present vs origin — remote sync via clean worktree |

## 3. Existing Form Security State

Baseline unchanged: 12 root handlers, server validation, honeypot, HMAC timing, rate/duplicate protection, shared `mail()` helper without CC/BCC, CAPTCHA absent. Pre-test production `test_mode=false`; operator already in production recipient set.

## 4. Form Inventory

Executable matrix T01–T12 covering all 12 root handlers and associated public routes (callback, page, audit, calc, bonus, career, partners, review, tariff_1–4). Service-tree copies remain root delegates. Full table in evidence §3.

## 5. Normal Recipient Baseline

| Field | Value |
|-------|-------|
| Authority | `iseo-form-config.php` |
| test_mode | OFF |
| Recipient count | 2 |
| im.work@nail.ru | YES |
| Other | 1 (masked SHA-16 in local receipt) |

## 6. Test Mode Activation

Enabled `test_mode=true` on production after scoped backup; remote checksum verified. Effective recipients during test: `im.work@nail.ru` only; normal count 0; no CC/BCC. Cleared ephemeral `.iseo-form-runtime/rl_*.json` once after earlier gate attempts exhausted hourly rate budget from the operator IP (code unchanged).

## 7. Single Controlled Mail

`callback__FORM.php` with `MARS TEST` / controlled contact → HTTP 200 / body `true` → **PASS**. Recipient intent: `im.work@nail.ru` ONLY.

## 8. Negative Control

Empty, whitespace, honeypot, too-fast, invalid email, array, header injection, direct malformed, GET — all `false`; mail 0.

## 9. Full Form Test Matrix

Valid once per root handler under test mode — **12/12 PASS**. Duplicate replay on partners: first `true`, second `false`.

## 10. Direct Handler Tests

Per root handler: required-field omission, honeypot filled, empty direct POST — all reject with mail 0 (12× each class).

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

(12 matrix valids + 1 duplicate-proof valid.)

## 12. Mass-Test Recipient Isolation

| Statement | Result |
|-----------|--------|
| ALL MASS TEST MAIL → im.work@nail.ru ONLY | **YES** |
| NORMAL RECIPIENTS RECEIVED MASS TEST MAIL | **NO** |
| NEGATIVE TESTS GENERATED MAIL | **NO** |

## 13. Test Mode Deactivation

`test_mode` set **false**; remote checksum matches canonical source. No temporary override left.

## 14. Final Recipient Restoration

| Field | Value |
|-------|-------|
| NORMAL RECIPIENTS RESTORED | YES |
| im.work@nail.ru IN FINAL SET | YES |
| TEST OVERRIDE PRESENT | NO |
| Production recipient count | 2 |

## 15. Production Validation

12 handlers present; anti-spam + server validation still active; token endpoint live; config OFF; no fake post-restore blast to all recipients.

## 16. Production / Source Alignment

YES — restored config SHA matches `production-source/forms/iseo-form-config.php`; security libs/handlers remain aligned.

## 17. SFTP / VPN Incidents

0 blocking drops for final state. Resilient put/get with retry + checksum used for config enable/disable. Prior operator VPN instability noted; no incomplete final remote state.

## 18. Files Created or Updated

**MARS (Git):**

- `ISEO-SU-FORM-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-EVIDENCE-v1.md` (new)
- `reports/REPORT-ISEO-SU-SITE-OPS-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-01.md` (this file)
- updates: `ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md`, `ISEO-SU-CURRENT-STATE-v1.md`, `OPERATIONAL-INDEX.md`, `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`

**Local (Git-ignored):** `_all-forms-isolated-mail-01/` receipts, backups, `acceptance-results-v2.json`, events extracts.

## 19. Production Mutations

Bounded to temporary `iseo-form-config.php` test_mode toggle + ephemeral rate-limit file clear under `.iseo-form-runtime/`. Final production config restored to source-equivalent OFF state. No handler/security redesign. No DB mutation.

## 20. Git Persistence

Scoped commit on allowlisted i-seo paths only; foreign WIP excluded.

| Item | Value |
|------|-------|
| Local commit (dirty-main lineage) | `adac09ee` |
| Remote synced commit | `1ed12d5f` |
| Method | clean worktree + cherry-pick onto origin tip `1b29e932` (no force push) |
| Remote | `origin/mars/canonical-post-recovery` |
| Reachability | `git ls-remote` = `1ed12d5f` |

## 21. Open Blockers

**0**

## 22. Final Decision

Accept all-forms isolated mail acceptance as complete. Mass-test mail isolation to operator proven; normal routing restored with operator retained.

## 23. Stop Condition

STOP after isolated all-forms test, restore, docs/Git sync. No CAPTCHA, no anti-spam redesign, no unrelated SEO/glossary/menu work.

---

### FINAL HARD CHECK

```
PUBLIC FORMS TESTED: 12
ROOT HANDLERS TESTED: 12
SINGLE CONTROL MAIL: PASS
SINGLE CONTROL RECIPIENT: im.work@nail.ru ONLY
ALL MASS TEST MAIL → im.work@nail.ru ONLY: YES
NORMAL RECIPIENTS RECEIVED MASS TEST MAIL: NO
VALID TEST EMAILS EXPECTED: 13
VALID TEST EMAILS OBSERVED: 13
NEGATIVE TEST SUBMISSIONS: 46
NEGATIVE TEST MAIL COUNT: 0
EMPTY DIRECT POST MAIL COUNT: 0
HONEYPOT TEST MAIL COUNT: 0
TEST MODE AFTER TESTS: OFF
NORMAL RECIPIENTS RESTORED: YES
im.work@nail.ru IN FINAL RECIPIENT SET: YES
ANTISPAM ACTIVE: YES
SERVER VALIDATION ACTIVE: YES
PRODUCTION/SOURCE ALIGNED: YES
SFTP/VPN INCIDENTS: 0 (final state)
OPEN BLOCKERS: 0
REMOTE SYNC: COMPLETE (1ed12d5f on origin/mars/canonical-post-recovery)
```
