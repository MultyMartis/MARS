# REPORT — ISEO-SU SITE OPS FORM RECIPIENT RESTORE 01

**Task:** ISEO-SU-SITE-OPS-FORM-RECIPIENT-RESTORE-01  
**Date:** 2026-08-21  
**Programme:** ISEO-SU-SITE-OPS  
**Production:** https://i-seo.su/

---

## 1. Execution Summary

Independently reconstructed the pre-antispam **active** recipient set from scoped production backups, compared it to live production and MARS canonical source, and verified that the desired final set was already in place: original legitimate recipient + operator mailbox `im.work@mail.ru`, typo `im.work@nail.ru` absent, `test_mode` OFF, all 12 handlers on shared routing. **No production recipient mutation** and **0 mail sends** were required. Documentation correction records the verification as current recipient-restore authority.

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` / **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| Local HEAD (dirty main) | `04d575a4…` (diverged; foreign WIP present) |
| Origin tip at start | `99593a9e…` |
| Staged | empty |
| Foreign WIP | preserved (not staged/cleaned) |
| Pull/reset/clean/stash | **not** performed on dirty main |
| Git sync path | clean worktree from `origin/mars/canonical-post-recovery` |

## 3. Current Production Recipient State

Authority: production `iseo-form-config.php` → `iseo_form_recipients()` in `iseo-form-security.php`.

| Field | Value |
|-------|-------|
| Verify stamp | `20260821T053743Z` |
| Config SHA-256 | `dea5b3482feb914f1ddf066137959c75f121362ba09bbecbdb462a8608c96e66` |
| `test_mode` | **false** |
| Production recipients | `nikel007i33@yandex.ru`, `im.work@mail.ru` |
| Count | **2** |
| Typo present | **NO** |
| CC/BCC | **NO** |
| Handler overrides | **NO** |

## 4. Original Recipient Recovery

From pre-antispam backups `local/sites/iseo-su-production/_form-antispam-01-tmp/backups/20260820T164529Z/` (all 12 root `__FORM.php`):

- Active `$sendto` on every root handler: **`nikel007i33@yandex.ru` only**
- `chrra@yandex.ru` appears only as **commented** alternate on 10/12 handlers — **not** active To
- No CC/BCC headers in original handlers
- Evidence order satisfied: scoped production backups before recipient centralization

## 5. Provenance

| Address | Provenance | Confidence |
|---------|------------|------------|
| `nikel007i33@yandex.ru` | Pre-antispam handler backups; active `$sendto` (e.g. `callback__FORM.php` SHA `50cfa2b4…`) | **PROVEN** |
| `chrra@yandex.ru` | Same backups; commented only | **PROVEN non-active** (excluded) |
| `im.work@mail.ru` | Operator retention requirement; live + source | **PROVEN** |

## 6. Set Comparison

| Set | Contents |
|-----|----------|
| ORIGINAL BEFORE ANTISPAM | `nikel007i33@yandex.ru` |
| CURRENT PRODUCTION | `nikel007i33@yandex.ru`, `im.work@mail.ru` |
| DESIRED FINAL | original + `im.work@mail.ru` |

| Class | Count / notes |
|-------|----------------|
| MISSING_LEGITIMATE | **0** |
| PRESENT_LEGITIMATE | 1 |
| OPERATOR_NEW | 1 (`im.work@mail.ru`) |
| UNEXPECTED | **0** |
| TYPO_WRONG | absent |

## 7. Production Correction

**None required.** Desired set already present. Verify-only SFTP download + checksum; no upload of recipient config.

## 8. Final Recipient State

| Field | Value |
|-------|-------|
| Final production recipients | `nikel007i33@yandex.ru` + `im.work@mail.ru` |
| Final legitimate + operator count | **2** |
| Duplicates | **0** |
| `im.work@nail.ru` | **ABSENT** |

## 9. Handler Coverage

| Item | Result |
|------|--------|
| Root handlers | **12/12** shared `iseo_form_send_mail` |
| Service delegates | `require` → root (sampled `services/callback__FORM.php`, `services/seo/…`, `services/adv/…`) |
| Hardcoded To / test override / typo / CC-BCC | **none** |

## 10. Test Mode Verification

**OFF** — `"test_mode" => false` in live production config.

## 11. Production / Source Alignment

Production `iseo-form-config.php` SHA ≡ `production-source/forms/iseo-form-config.php`. Security helper and sampled handlers SHA-matched. Recipient sets identical. **ALIGNED.**

## 12. Mail Sends

**0**

## 13. Documentation Correction

Created `ISEO-SU-FORM-RECIPIENT-RESTORATION-EVIDENCE-v1.md` as current recipient-restore authority. Historical Acceptance / Antispam REPORTs **not** rewritten. Current-state / baseline / index / artifact register / acceptance v2 updated to point at this verification. Previous “NORMAL RECIPIENTS RESTORED” claim for the **active** original set: **CONFIRMED** by independent evidence (not voided).

## 14. Files Created or Updated

**Created:**

- `projects/iseo-su-site-ops/ISEO-SU-FORM-RECIPIENT-RESTORATION-EVIDENCE-v1.md`
- `projects/iseo-su-site-ops/reports/REPORT-ISEO-SU-SITE-OPS-FORM-RECIPIENT-RESTORE-01.md`

**Updated:**

- `projects/iseo-su-site-ops/ISEO-SU-CURRENT-STATE-v1.md`
- `projects/iseo-su-site-ops/ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md`
- `projects/iseo-su-site-ops/OPERATIONAL-INDEX.md`
- `projects/iseo-su-site-ops/ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`
- `projects/iseo-su-site-ops/ISEO-SU-FORM-ALL-FORMS-ISOLATED-MAIL-ACCEPTANCE-EVIDENCE-v2.md`

**Local-only (not Git):** `_form-recipient-restore-01/` verify backups + script.

## 15. Production Mutations

**0** (recipient config / anti-spam / validation / handlers / JS / CSS untouched).

## 16. Rollback

N/A for mutations. Local verify backups available under Git-ignored `_form-recipient-restore-01/`.

## 17. Git Persistence

Scoped commit via clean worktree from `origin/mars/canonical-post-recovery` (dirty main unsafe). Foreign WIP preserved. No force push. Exact i-seo paths only.

## 18. Open Blockers

**0**

## 19. Final Decision

**COMPLETE — ORIGINAL ISEO-SU FORM RECIPIENTS RESTORED / OPERATOR MAILBOX RETAINED / ROUTING NORMALIZED**

## 20. Stop Condition

Stop after historical recovery, production comparison, confirmation that missing-recipient restoration was unnecessary, operator mailbox retention, typo absence, all-handler verification, production/source alignment, docs correction, and scoped Git remote sync. **No mass form retest.**

---

## FINAL HARD CHECK

```
ORIGINAL RECIPIENTS RECOVERED: YES (nikel007i33@yandex.ru)
ORIGINAL RECIPIENT PROVENANCE: PROVEN (pre-antispam backups 20260820T164529Z)
CURRENT RECIPIENTS BEFORE FIX: nikel007i33@yandex.ru + im.work@mail.ru
MISSING LEGITIMATE RECIPIENTS FOUND: 0
FINAL LEGITIMATE RECIPIENT COUNT: 2 (1 original + operator)
im.work@mail.ru IN FINAL SET: YES
im.work@nail.ru IN FINAL SET: NO
ALL ORIGINAL LEGITIMATE RECIPIENTS RESTORED: YES
DUPLICATE RECIPIENTS: 0
TEST MODE: OFF
HANDLERS VERIFIED: 12/12
MAIL SENT DURING THIS TASK: 0
ANTISPAM CHANGED: NO
VALIDATION CHANGED: NO
PRODUCTION/SOURCE ALIGNED: YES
PREVIOUS RECIPIENT-RESTORE CLAIM: CONFIRMED (active originals; now evidenced by restoration file)
OPEN BLOCKERS: 0
REMOTE SYNC: COMPLETE
```
