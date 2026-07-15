# REPORT — SITE-002 Form Empty Lead Guard Follow-up 01

**Operation:** `SITE-002-PROD-FORM-EMPTY-LEAD-GUARD-FOLLOWUP-01`  
**OCPilot run:** `4.265 — SITE-002 Form Empty Lead Guard Follow-up 01`  
**Date:** 2026-07-14  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\audits\SITE-002-PROD-FORM-EMPTY-LEAD-GUARD-FOLLOWUP-01\`

---

## 1. Scope

Verify whether the empty admin lead mail seen after Run 4.264 was pre-patch test traffic or a live guard gap; harden production `anketa.php` only if a gap is confirmed. No recipient / DB / scheduler / frontend changes.

## 2. Operator finding

Empty mail:

| Field | Value |
|-------|--------|
| Subject | ЗПМ: новая заявка — Заявка с сайта |
| Type | Заявка с сайта (= dialog **0**) |
| Date | **2026-07-13 20:21:09** |
| Page | `https://bzpm.ru/about?utm_source=mars_test&utm_medium=form_audit` |
| User-Agent | `HeadlessChrome/148.0.7778.96` |
| UTM | `utm_source=mars_test` |
| Body | service fields only; no name/phone/email/comment |

Most other test mails from the same window were valid (full user fields).

## 3. Chronology

| UTC | Event | Result |
|-----|-------|--------|
| **20:21:11.515** | before-patch empty dialog=0 POST | **HTTP 200** (sends admin mail) |
| 20:21:15 / 20:21:18 | before-patch valid dialog 7 / 2 | 200 |
| **20:21:50.395** | `anketa.php` patch uploaded | sha `d86c812b…` |
| 20:22:06 | after-patch empty dialog=0 | **HTTP 400** |
| 20:22:10 / 20:22:13 | after-patch valid dialog 7 / 2 | 200 |

**Classification: `EMPTY_EMAIL_PRE_PATCH`**

Operator Date **20:21:09** sits in the before-patch window; page + `mars_test` + HeadlessChrome match the controlled Playwright empty probe (`before-empty-dialog0`). ≈2s skew vs POST time is negligible.

| Hypothesis | Verdict |
|------------|---------|
| A before patch | **CONFIRMED** |
| B uncovered after patch | REJECTED for this email |
| C service fields as content | REJECTED for this email; live retest OK |
| D dialog=0 bypass | REJECTED for this email; live retest OK |
| E renderer hid fields | REJECTED |

Artifacts: Storage `chronology/chronology.md` · `chronology.json`

## 4. Current guard analysis

FTP download of production `/public_html/catalog/controller/checkout/anketa.php`:

- SHA256 = `d86c812b3925720d561007fc304413375b544777810f20307fda6842082c716e` (**unchanged** vs Run 4.264 upload)
- Allowlist user fields: `name|contact|phone|email|company|message|comment|text|project_description|subject`
- Values must be non-empty after `trim`
- Service/technical POST keys (page, referrer, utm*, dialog, CSRF, captcha) **not** in allowlist
- dialog=0 does **not** bypass the guard (guard runs before mail / label)

## 5. Controlled tests before

Marker: `MARS-TEST-SITE002-EMPTY-GUARD-FOLLOWUP-01`

| Test | Expected | Actual | Pass |
|------|----------|--------|------|
| service-only (page/referrer/utm/dialog=0) | 400 | **400** | yes |
| whitespace-only name/phone/email/message | 400 | **400** | yes |
| valid about dialog=7 | 200 | **200** | yes |
| valid callback dialog=2 | 200 | **200** | yes |

**all_pass: true** — Storage `controlled-tests-before/`

## 6. Patch decision

**NO PATCH** — empty operator mail explained by chronology; live guard already blocks service-only and whitespace-only; valid forms still succeed.

## 7. Patch applied or not needed

**Not needed / not applied.** Production mutation count for this follow-up: **0**.

## 8. Controlled tests after

**Skipped** (identical production state). Before-phase results are the final verification. See Storage `controlled-tests-after/results.md`.

## 9. Production mutation summary

| Kind | Count |
|------|-------|
| FTP writes | **0** |
| DB writes | **0** |
| Admin saves | **0** |
| Import / scheduler | **0** |
| Controlled POST tests | **4** (2 blocked + 2 valid admin mails expected) |
| Recipients changed | **0** |

## 10. Mail recipient status

- Remains **only** `client.leads@polygon-ws.ru` (temp test policy from Run 4.264)
- `info@bzpm.ru` **not** restored

## 11. Git / worktree summary

| Check | Result |
|-------|--------|
| Authority worktree | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Branch | `site-002-git-authority-realign-after-wave-e` |
| Preflight HEAD | `2bec4794` = `origin/mars/canonical-post-recovery` |
| Dirty main | untouched |
| Commit message | `ocpilot: verify SITE-002 empty lead guard` |

## 12. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\audits\SITE-002-PROD-FORM-EMPTY-LEAD-GUARD-FOLLOWUP-01\`

Includes: preflight, chronology, previous-test-evidence, ftp-before, handler-analysis, controlled-tests-before/after, patch plan, apply (no-upload), verification, reports, logs.

## 13. Final verdict

**`SITE-002 FORM EMPTY LEAD GUARD FOLLOWUP COMPLETE — EMPTY EMAIL WAS PRE-PATCH, CURRENT GUARD OK`**

## 14. Next recommendation

1. Treat the empty `20:21:09` mail as intentional before-patch controlled probe; ignore as organic empty lead.
2. When ready for production leads: restore `info@bzpm.ru` into `config_mail_alert_email` via OpenCart admin (**separate charter**).
3. Optional later: about dialog=7 mislabel (deferred from 4.264) remains open if operator wants a dedicated dialog label fix.
