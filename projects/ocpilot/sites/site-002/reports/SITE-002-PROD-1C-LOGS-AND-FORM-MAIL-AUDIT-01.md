# REPORT — SITE-002 1C Logs and Form Mail Audit 01

**Operation:** `SITE-002-PROD-1C-LOGS-AND-FORM-MAIL-AUDIT-01`  
**OCPilot run:** `4.264 — SITE-002 1C Logs and Form Mail Audit 01`  
**Date:** 2026-07-14  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\audits\SITE-002-PROD-1C-LOGS-AND-FORM-MAIL-AUDIT-01\`

---

## 1. Scope

Read-only health check of SITE-002 1C import logs / post-1C monitor / scheduler / sitemap, plus diagnosis of an empty website lead email (service fields only). Controlled test submissions allowed only while temporary recipient is `client.leads@polygon-ws.ru`. Production patch allowed only if exact root cause confirmed.

## 2. Operator context

1. Check 1C update logs and related monitor/scripts health.  
2. Empty lead arrived without name/phone/contacts — identify source form and why mail lacked user fields.  
3. Recipients temporarily limited to `client.leads@polygon-ws.ru` (test policy). Do **not** restore `info@bzpm.ru` in this task.

## 3. Screenshot facts

Recorded in Storage `mail-screenshot-facts/operator-email-empty-lead-2026-07-13.md`.

Key facts: From `noreply@bzpm.ru` → To `client.leads@polygon-ws.ru`; Subject `ЗПМ: новая заявка — Заявка с сайта`; Page/Referrer `https://bzpm.ru/about?utm_source=chatgpt.com`; mobile Safari iOS; user fields absent; service fields present.

Subject suffix **«Заявка с сайта»** = `zpmDialogLabel()` **default** → **`dialog = 0`**.

## 4. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` label | `AI WS` |
| Authority worktree | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Branch | `site-002-git-authority-realign-after-wave-e` |
| HEAD | `7fdd9d0c` (= `origin/mars/canonical-post-recovery` at fetch) |
| Staged / unpushed | none vs origin |
| Dirty main | foreign WIP present — **not mutated** |
| Authority safe for scoped audit/commit | **yes** (HEAD matches origin; untracked tools left unstaged) |

## 5. 1C import logs summary

Latest TXT reports downloaded from `/storage/mars-tools/cron/reports/`.

| Report | Status | Duration | Steps |
|--------|--------|----------|-------|
| `mars_1c_import_2026-07-13_080008.txt` | **SUCCESS** | 7.15s | Step1 PASS · Step2 PASS |
| `mars_1c_import_2026-07-12_080009.txt` | SUCCESS | 6.7s | PASS/PASS |
| `mars_1c_import_2026-07-11_080009.txt` | SUCCESS | 7.19s | PASS/PASS |

- Latest run ID: `mars-20260713-080001-f328bd6b`  
- Duration field populated (duration fix still working)  
- No import triggered by this audit  
- Details: Storage `onec-logs/` · `verification/onec-logs-summary.md`

## 6. Monitor / scheduler / sitemap summary

| Item | Result |
|------|--------|
| Task `MARS_SITE_002_Post_1C_Catalog_Monitor` | Ready · LastTaskResult **0** · Next ~2026-07-14 12:30 +07 |
| WorkingDirectory | `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` (not dirty main) |
| Latest monitor folder | `2026-07-13_13-00-39` (after pin folder `2026-07-13_00-05-00`) |
| Classification | **`NO_ACTION_REQUIRED`** |
| Baseline → current | **1530 → 1530** · added 0 · removed 0 · needs 0 · garbage 0 |
| Live sitemap | **1530** URLs · HTTP 200 |

## 7. Form inventory

Inspected: `/about?utm_source=chatgpt.com`, `/about`, `/custom-equipment`, `/payment-methods`, `/delivery`, `/dealers`, `/guarantee`, `/contact`.

- `/about` corp CTA: `.zpm-form`, `dialog=7`, fields `name|phone|email|message` with `required` on name/phone/email; **no** `data-fb-form` (corp-cta JS handler); **no** `source_page` hidden.  
- Shared footer dialogs 1/2/3 present (`data-fb-form`).  
- Other info pages: dialogs 8/9/10/11 as previously integrated.  
- JS authority: `/assets/js/main.js` (contains corp-cta + anketa); `main.min.js` lacks corp-cta block but page also loads full `main.js`.

## 8. Production source analysis

FTP-read:

- `catalog/controller/checkout/anketa.php` — no pre-patch user-content guard; recipients from `config_mail_alert_email`; dialog 0 → «Заявка с сайта».  
- `system/library/zpm/mail_renderer.php` — omits empty contact rows; always can show service_info.  
- `sections/corpcta-about.twig` / about embed — dialog **7** (dealers label — mislabel for price-list CTA).  
- Frontend corp-cta uses `FormData(form)` + CSRF + reCAPTCHA; HTML5 `checkValidity` before send.

## 9. Root cause candidates

| Code | Verdict |
|------|---------|
| **`HANDLER_FALLBACK_TOO_PERMISSIVE`** | **PRIMARY — CONFIRMED** |
| `BOT_EMPTY_SUBMIT` | Likely contributor (dialog=0 + chatgpt UTM + empty fields) |
| `ABOUT_FORM_EMPTY_SUBMIT_ALLOWED` | Browser blocked by required; API not |
| `ABOUT_FORM_FIELDS_MISSING` | Rejected |
| `JS_SERIALIZATION_BUG` | Unlikely primary (empty lead was dialog 0, not 7) |
| `MAIL_RENDER_HIDES_FIELDS` | Rejected |
| `MOBILE_SAFARI_EDGE` | Possible secondary only |
| About dialog=7 mislabel | Separate deferred issue (not this empty-lead subject) |

**Empty lead source:** referrer/page = `/about?utm_source=chatgpt.com`, but subject proves **dialog=0** empty backend submission (not a normal dialog=7 about CTA with fields dropped).

## 10. Test submission plan

Marker: `MARS-TEST-SITE002-FORM-AUDIT-01`.  
Recipient gate: read-only DB confirmed `config_mail_alert_email` = **only** `client.leads@polygon-ws.ru` (`info@bzpm.ru` absent) → tests allowed.

## 11. Test submission results

**Before patch**

| Test | Status | ok |
|------|--------|----|
| empty dialog=0 | 200 | **true** (reproduces empty lead) |
| about dialog=7 valid | 200 | true |
| callback dialog=2 valid | 200 | true |

**After patch**

| Test | Status | ok |
|------|--------|----|
| empty dialog=0 | **400** | **false** |
| about dialog=7 valid | 200 | true |
| callback dialog=2 valid | 200 | true |

Mailbox visual confirmation of test letters: **SAFE UNKNOWN** (operator-side).

## 12. Decision matrix

See Storage `patch-plan/decision-matrix.md`.

- Empty lead → backend guard **applied**.  
- About dialog=7 mislabel → **deferred** (charter: dedicated about dialog / dialog label fix).

## 13. Patch applied or patch deferred

**Applied** — single-file Production FTP:

`/public_html/catalog/controller/checkout/anketa.php`

Guard: reject when none of `name|contact|phone|email|company|message|comment|text|project_description|subject` is non-empty → HTTP 400 JSON error; no admin mail.

Repo mirror updated: `projects/ocpilot/sites/site-002/tools/checkout_anketa_info_page_forms.php`.

Backup: Storage `backup/anketa.php.pre-patch.bak`.

## 14. Post-patch verification

- Empty lead success blocked.  
- Valid forms still succeed.  
- Sampled public pages: **БЗПМ = 0**.  
- Recipients unchanged.

## 15. Production mutation summary

| Kind | Count / note |
|------|----------------|
| FTP writes | **1** — `anketa.php` |
| DB writes | **0** (1 read-only SELECT for recipients) |
| Admin saves | **0** |
| Import runs triggered | **0** |
| Scheduler changes | **0** |
| Test form submissions | **6** (3 before + 3 after) |
| Mail sends (controlled tests) | **5** expected admin sends (empty before + 2 valid before + 2 valid after; empty after blocked) |
| Recipients changed | **0** |

## 16. Mail recipient status

- Temporary policy confirmed in DB: **only** `client.leads@polygon-ws.ru`  
- `info@bzpm.ru` **not** restored  
- `config_email` (From) remains noreply-style sender (masked in artifacts)

## 17. Git / worktree summary

- Dirty main untouched.  
- Commit/push from authority worktree of report + docs + anketa mirror (this wave).

## 18. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\audits\SITE-002-PROD-1C-LOGS-AND-FORM-MAIL-AUDIT-01\`

Includes: preflight, onec-logs, monitor, scheduler, sitemap, form-inventory, ftp-before, handler-analysis, test-submissions, patch-plan, backup, apply, verification, manifests.

## 19. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Operator mailbox visual of empty-lead original + tests | SAFE UNKNOWN |
| Exact human vs bot identity for IP `149.27.180.114` | SAFE UNKNOWN |
| Whether ChatGPT browsing agent submitted empty API POST | SAFE UNKNOWN (consistent with dialog=0 empty) |
| `main-pt2.js` FTP path | missing / 550 — corp-cta lives in `main.js` |
| About dialog label mislabel fix | deferred |

**Blockers:** none for closing this run.

## 20. Final verdict

**`SITE-002 1C AND FORM MAIL AUDIT COMPLETE — EMPTY LEAD ROOT CAUSE FIXED`**

## 21. Next recommendation

1. Operator optionally confirms test mails in `client.leads@polygon-ws.ru`.  
2. When ready for production leads: restore `info@bzpm.ru` into `config_mail_alert_email` via admin (**not** this task).  
3. Follow-up charter: fix `/about` CTA `dialog=7` mislabel (dedicated dialog + `source_page`).  
4. Optional: stricter contact rule (require phone **or** email specifically).
