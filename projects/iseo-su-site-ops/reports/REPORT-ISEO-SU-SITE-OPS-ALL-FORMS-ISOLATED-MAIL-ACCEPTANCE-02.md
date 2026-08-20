# REPORT — ISEO-SU SITE OPS ALL-FORMS ISOLATED MAIL ACCEPTANCE 02

**Task ID:** ISEO-SU-SITE-OPS-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-02  
**Date:** 2026-08-21  
**Site:** https://i-seo.su/

## 1. Execution Summary

Corrected operator typo `im.work@nail.ru` → `im.work@mail.ru` in production and MARS source, re-ran isolated all-forms mail acceptance to the correct mailbox only, proved negatives generated zero mail, then restored normal routing with the correct operator address retained and the typo absent. Anti-spam was not redesigned.

**FINAL STATUS:** COMPLETE — ALL ISEO-SU FORMS RE-VERIFIED / CORRECT OPERATOR MAILBOX ACCEPTED / WRONG RECIPIENT REMOVED / NORMAL ROUTING RESTORED

## 2. Reason for Re-test

Acceptance 01 recipient evidence is invalid as operator mailbox-delivery acceptance because it used `im.work@nail.ru`. Anti-spam implementation remains valid unless contradicted; mail-delivery acceptance required a full re-run.

## 3. Address Correction

| Field | Value |
|-------|-------|
| Wrong | `im.work@nail.ru` |
| Correct | `im.work@mail.ru` |
| Exact-string discipline | enforced (no normalize/guess/substitute) |

## 4. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Local HEAD at start | `715f3f6f` |
| Origin tip at start | `80e208df` (verified; not assumed) |
| Staged | empty |
| Foreign WIP | present (unrelated) — preserved / not staged |
| Unpushed local lineage | parallel cherry-pick lineage vs origin — remote sync via clean worktree |

## 5. Existing Security State

Baseline unchanged: 12 root handlers, server validation, honeypot, HMAC timing, rate/duplicate protection, shared `mail()` helper without CC/BCC, CAPTCHA absent. Pre-correction production `test_mode=false`; typo address present; correct address absent.

## 6. Production Recipient Correction

Authority: `iseo-form-config.php` (production + `production-source/forms/`).

| Before | After (final) |
|--------|----------------|
| typo in `production_recipients` + `test_recipients` | typo **ABSENT** |
| correct operator absent | `im.work@mail.ru` **PRESENT ONCE** |
| other legitimate recipients | **preserved** |

Scoped backup + checksum before mutation. No recipient architecture redesign.

## 7. Test Mode Activation

Enabled `test_mode=true` with corrected source after backup; remote checksum verified.

### PRE-SEND HARD CHECK

```
TEST MODE: ON
EFFECTIVE RECIPIENT COUNT: 1
EFFECTIVE RECIPIENT: im.work@mail.ru
im.work@nail.ru ACTIVE: NO
NORMAL RECIPIENTS ACTIVE DURING TEST: NO
```

Ephemeral rate-limit files cleared once (code unchanged).

## 8. Single Controlled Mail

`callback__FORM.php` — Name `MARS TEST ACCEPTANCE 02` / controlled contact → HTTP 200 / `true` → **PASS**. Recipient intent: `im.work@mail.ru` ONLY.

**Proof level:** MAIL SEND ACCEPTED BY SERVER (PHP `mail()` path after accept). Inbox visual confirmation is operator-side and not claimed here.

## 9. Full Form Test Matrix

Valid once per root handler under test mode — **12/12 PASS**. Duplicate replay on partners: first `true`, second `false`.

## 10. Negative Test Matrix

Universal negatives + per-handler required omission / honeypot / empty direct POST — all reject; mail 0. Representative whitespace / too-fast / array / injection / GET retained.

## 11. Mail Accounting

| Metric | Value |
|-------:|
| SINGLE CONTROL VALID SENDS | 1 |
| MASS VALID SUBMISSIONS | 12 (+1 dup proof) |
| EXPECTED TOTAL VALID EMAILS | 13 |
| OBSERVED TOTAL VALID MAIL SENDS | 13 |
| NEGATIVE SUBMISSIONS | 46 |
| NEGATIVE MAIL SENDS | 0 |
| MAIL TO im.work@mail.ru | 13 |
| MAIL TO im.work@nail.ru | 0 |
| MAIL TO NORMAL RECIPIENTS | 0 |
| CC/BCC TEST MAIL | 0 |
| UNEXPECTED MAIL | 0 |

## 12. Correct Recipient Isolation

| Statement | Result |
|-----------|--------|
| ALL MASS TEST MAIL → im.work@mail.ru ONLY | **YES** |
| NORMAL RECIPIENTS RECEIVED MASS TEST MAIL | **NO** |
| NEGATIVE TESTS GENERATED MAIL | **NO** |

## 13. Wrong Address Verification

| Check | Result |
|-------|--------|
| MAIL TO im.work@nail.ru | **0** |
| Wrong address removed from production | **YES** |
| Wrong address in final set | **NO** |

## 14. Test Mode Deactivation

`test_mode` set **false**; remote checksum matches corrected canonical source. No temporary override left.

## 15. Final Recipient Restoration

| Field | Value |
|-------|-------|
| NORMAL RECIPIENTS RESTORED | YES |
| im.work@mail.ru IN FINAL SET | YES |
| im.work@nail.ru IN FINAL SET | NO |
| TEST OVERRIDE PRESENT | NO |
| Production recipient count | 2 |

No fake production lead blast after restore.

## 16. Production Validation

12 handlers present; anti-spam + server validation still active; token endpoint live; config OFF; correct operator present; typo absent; no temporary config left.

## 17. Production / Source Alignment

YES — restored config SHA `dea5b3482feb914f` matches `production-source/forms/iseo-form-config.php`; security libs/handlers remain aligned.

## 18. Documentation Supersession

Current authorities updated to `im.work@mail.ru`. Historical Acceptance 01 / Form Antispam 01 REPORTs left intact as factual records of the typo address used then; recipient evidence marked **SUPERSEDED BY ACCEPTANCE 02**.

## 19. SFTP / VPN Incidents

0 blocking drops for final state. Resilient put/get with retry + checksum used.

## 20. Files Created or Updated

**MARS (Git):**

- `ISEO-SU-FORM-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-EVIDENCE-v2.md` (new)
- `reports/REPORT-ISEO-SU-SITE-OPS-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-02.md` (this file)
- `production-source/forms/iseo-form-config.php` (recipient correction)
- updates: `ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md`, `ISEO-SU-CURRENT-STATE-v1.md`, `OPERATIONAL-INDEX.md`, `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`

**Local (Git-ignored):** `_all-forms-isolated-mail-02/` receipts, backups, `acceptance-results-v2.json`, events extracts.

## 21. Production Mutations

Bounded to `iseo-form-config.php` recipient correction + temporary `test_mode` toggle + ephemeral rate-limit clear. Final production config = corrected source OFF state. No handler/security redesign. No DB mutation.

## 22. Git Persistence

Scoped commit on allowlisted i-seo paths only; foreign WIP excluded. Remote sync via clean worktree onto `origin/mars/canonical-post-recovery` (no force push). Tip recorded after push.

## 23. Open Blockers

**0**

## 24. Final Decision

Accept corrected-operator all-forms isolated mail acceptance as complete. Typo removed; correct mailbox accepted for isolated delivery; normal routing restored.

## 25. Stop Condition

STOP after wrong-recipient removal, correct recipient configuration, isolated single test, complete 12-form + negative retest, routing restoration, documentation supersession, source alignment, and Git remote sync. No CAPTCHA, no anti-spam redesign, no unrelated work.

---

### FINAL HARD CHECK

```
PUBLIC FORMS TESTED: 12
ROOT HANDLERS TESTED: 12
CORRECT OPERATOR ADDRESS: im.work@mail.ru
WRONG ADDRESS: im.work@nail.ru
WRONG ADDRESS REMOVED FROM PRODUCTION: YES
SINGLE CONTROL MAIL: PASS
SINGLE CONTROL RECIPIENT: im.work@mail.ru ONLY
ALL MASS TEST MAIL → im.work@mail.ru ONLY: YES
MAIL TO im.work@nail.ru: 0
NORMAL RECIPIENTS RECEIVED MASS TEST MAIL: NO
VALID TEST EMAILS EXPECTED: 13
VALID TEST EMAILS OBSERVED: 13
NEGATIVE TEST SUBMISSIONS: 46
NEGATIVE TEST MAIL COUNT: 0
EMPTY DIRECT POST MAIL COUNT: 0
HONEYPOT TEST MAIL COUNT: 0
TEST MODE AFTER TESTS: OFF
NORMAL RECIPIENTS RESTORED: YES
im.work@mail.ru IN FINAL RECIPIENT SET: YES
im.work@nail.ru IN FINAL RECIPIENT SET: NO
ANTISPAM ACTIVE: YES
SERVER VALIDATION ACTIVE: YES
PRODUCTION/SOURCE ALIGNED: YES
ACCEPTANCE 01 RECIPIENT EVIDENCE: SUPERSEDED BY ACCEPTANCE 02
SFTP/VPN INCIDENTS: 0 (final state)
OPEN BLOCKERS: 0
REMOTE SYNC: (filled after push)
```
