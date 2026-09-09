# REPORT — ISEO-SU-SITE-OPS-WEBINAR-FORM-FIX-01

**Task ID:** `ISEO-SU-SITE-OPS-WEBINAR-FORM-FIX-01`  
**Lane:** ISEO-SU-SITE-OPS — WEBINAR FORM FAILURE DIAGNOSIS + FIX 01  
**Date:** 2026-09-09  
**FINAL STATUS:**  
**COMPLETE — WEBINAR REGISTRATION FORM FIXED / ROOT CAUSE PROVEN / SECURITY PRESERVED**

---

## 1. Summary

Live webinar registration at `https://i-seo.su/webinar-seo-podryadchik.html` submitted to `/page__FORM.php` and received HTTP 200 body `false`. Shared JS then showed the generic failure message.

Root cause: rebuild-01 cloned restaurant `free_audit` markup, so the visible tel used `name="pf_contact"` and **omitted `pf_phone`**. The handler requires `pf_contact` as contact **method** and `pf_phone` as the actual contact.

Fix: hidden `pf_contact=WhatsApp` + visible tel `name="pf_phone"`. Handler and shared JS unchanged. Security baseline preserved.

Isolated `test_mode` accept to `im.work@mail.ru` proven. Production mail to `nikel007i33@yandex.ru` was not sent.

## 2. Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume X: | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Origin tip | `187591a8859dda2e2d3ceeaa18de8392e7e7ad85` |
| Charter SHA `131882bd…` | stale; used actual origin tip |
| Main vs origin | dirty / unpushed / foreign WIP preserved |
| Sync strategy | STORAGE worktree `git-sync-iseo-su-webinar-form-fix-01` from origin |

## 3. Failure reproduction

| Field | Value |
|-------|--------|
| FAILURE REPRODUCED | YES |
| FAILURE STAGE | E. HANDLER BUSINESS REJECTION |
| HTTP STATUS BEFORE | 200 |
| SERVER RESPONSE BEFORE | `false` |
| UI | generic «Не удалось отправить заявку…» |

## 4. Root cause

Webinar markup uses `pf_contact` as the visible phone field and omits `pf_phone`, while `/page__FORM.php` + homepage `#page__FORM` require `pf_contact` = method and `pf_phone` as contact, causing handler `required` reject (`false`) and generic JS failure UI.

## 5. Backup / deploy

Backup root: `X:\AI MARS\local\sites\iseo-su-production\_webinar-form-fix-01\`

| File | SHA-256 BEFORE | Timestamp |
|------|----------------|-----------|
| webinar HTML | `2434e990b08b6765fd0e475d203671f34acf77222447d03c48a43b49758c4382` | `2026-09-09T09:47:48Z` |
| `iseo-form-config.php` | `d4e394f3a8dd725f526e6c195d290b6cb2ad46a8f27e1b8021d5769567d5ecb7` | `2026-09-09T09:47:48Z` |

Production HTML SHA-256 after: `f5e7d6029faeda9cabae7502a34ad716c6700f1eb309c188372205ab64b14331`. Date 10 сентября 2026 preserved.

## 6. Changed files (project)

| Path | Action |
|------|--------|
| `production-source/static-html/webinar-seo-podryadchik.html` | form fields only |
| `tools/_webinar-form-fix-01-backup-deploy-validate.py` | backup/deploy/validate helper |
| `evidence/webinar-form-fix-01/*` | machine JSON + screenshots |
| `ISEO-SU-WEBINAR-FORM-FIX-01-EVIDENCE-v1.md` | evidence |
| `reports/REPORT-ISEO-SU-SITE-OPS-WEBINAR-FORM-FIX-01.md` | this report |
| `reports/ISEO-SU-WEBINAR-FORM-FIX-01-RU.md` | operator RU |
| `ISEO-SU-CURRENT-STATE-v1.md` | WEBINAR FORM FIX 01 COMPLETE |

**Not changed:** `page__FORM.php`, `common.js`, `iseo-form-security.php`, restaurant/`content-form-seo.php`, webinar CSS, menu, sitemap.

## 7. Validation

| Check | Result |
|-------|--------|
| Valid POST after | 200 `true` / `accept` |
| Desktop UI | «Успешно! Сообщение отправлено» |
| Missing consent | REJECT `consent` |
| consent=0 | REJECT `consent` |
| malformed consent | REJECT `consent` |
| honeypot filled | REJECT `honeypot` |
| Homepage smoke | 200; working `pf_phone` family |
| Restaurant smoke | 200; form present (clone not submitted) |
| test_mode final | OFF |
| Normal recipient | `nikel007i33@yandex.ru` |

## 8. FINAL HARD CHECK

```
WEBINAR URL: https://i-seo.su/webinar-seo-podryadchik.html
FAILURE REPRODUCED: YES
FAILURE STAGE: E. HANDLER BUSINESS REJECTION
HTTP STATUS BEFORE: 200
SERVER RESPONSE BEFORE: false
ROOT CAUSE: webinar tel used name=pf_contact and omitted pf_phone; handler requires pf_contact=method and pf_phone=contact

WORKING FORM REFERENCE: homepage #page__FORM / original webinar landing contract
HANDLER: /page__FORM.php
HANDLER CHANGED: NO
WEBINAR SOURCE CHANGED: YES (form fields only)
SHARED JS CHANGED: NO

VALID FORM REQUEST AFTER: PASS
VALID FORM SERVER RESULT AFTER: PASS (accept / true)
VALID FORM UI RESULT AFTER: PASS (Успешно! Сообщение отправлено)

MISSING CONSENT: REJECT
CONSENT=0: REJECT
MALFORMED CONSENT: REJECT
HONEYPOT TEST: REJECT (honeypot)

REAL/ISOLATED MAIL DELIVERY VERIFIED: ISOLATED YES (accept to im.work@mail.ru); production nikel NOT sent
TEST MAIL RECIPIENT IF USED: im.work@mail.ru

NORMAL RECIPIENT: nikel007i33@yandex.ru
TEST MODE FINAL: OFF
HMAC: ACTIVE
HONEYPOT: ACTIVE
MIN-FILL: ACTIVE
RATE LIMIT: ACTIVE
DUPLICATE PROTECTION: ACTIVE
CONSENT SERVER GUARD: ACTIVE

DESIGN CHANGED: NO
TITLE CHANGED: NO
DESCRIPTION CHANGED: NO
H1 CHANGED: NO
CANONICAL CHANGED: NO
DATE/TIME CHANGED: NO
MENU CHANGED: NO
SITEMAP CHANGED: NO

RELATED FORM REGRESSION: NONE
PRODUCTION/SOURCE ALIGNED: YES
PROJECT-OWNED UNCOMMITTED: NO (scoped worktree commits)
FOREIGN WIP PRESERVED: YES
REMOTE SYNC: pending push of worktree `iseo-su-webinar-form-fix-01` from origin `187591a8`

FINAL STATUS:
COMPLETE — WEBINAR REGISTRATION FORM FIXED / ROOT CAUSE PROVEN / SECURITY PRESERVED
```

FUNCTIONAL FIX VERIFIED THROUGH SERVER ACCEPTANCE / MAIL DELIVERY PROOF REQUIRES OPERATOR-APPROVED TEST SEND

## 9. Git

Worktree: `X:\AI MARS STORAGE\git-sync-iseo-su-webinar-form-fix-01\repo`  
Base: `origin/mars/canonical-post-recovery` @ `187591a8859dda2e2d3ceeaa18de8392e7e7ad85`  
Implementation: `e7050fcb88ab77709276e3c9eb638a416570b3a1` — `fix(iseo-su): repair webinar registration form`  
Docs: this commit (same branch).  
Main workspace foreign WIP: not staged.
