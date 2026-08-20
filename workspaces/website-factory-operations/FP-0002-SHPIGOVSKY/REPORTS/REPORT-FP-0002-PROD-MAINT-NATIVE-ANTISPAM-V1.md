# REPORT — FP-0002 PROD-MAINT Native Form Anti-Spam v1

**Status:** PASS  
**Date:** 2026-08-20  
**Core:** `0.3.24-antispam`  
**Phase remains:** PRODUCTION / MAINTENANCE  

Evidence: `REPORTS/evidence/prod-maint-native-antispam-v1/`

---

## Summary

First-party layered anti-spam is live on **all** public FP-0002 lead forms (final + modal). No Google reCAPTCHA, no Yandex SmartCaptcha, no external CAPTCHA provider. Spam is rejected **before** lead persistence, mail, and analytics goals.

---

## Pipeline

See `evidence/.../PIPELINE-BEFORE-AFTER.md`.

**CURRENT FORM PIPELINE TRUTH VERIFIED**  
**SPAM FILTERING OCCURS BEFORE REAL LEAD PERSISTENCE**  
**ALL CURRENT PUBLIC FORM ENTRY POINTS COVERED**

---

## Layers

| Layer | Implementation | Proof |
|-------|----------------|-------|
| Honeypot | `company_url` server-checked | QA honeypot reject |
| Signed timing | `fp02_fs` HMAC (WP `AUTH_KEY` / salt) | too-fast / tamper / expiry QA |
| Replay | `request_token` transient claim | replay QA |
| Rate limit | 6/60s + 20/20m, salted fingerprint | rate QA |
| Heuristics | ≥4 URLs, script/iframe, giant body, etc. | heuristic matrix |

**HONEYPOT VERIFIED SERVER-SIDE**  
**TIME-TO-SUBMIT CHECK IS SERVER-SIGNED AND TAMPER-RESISTANT**  
**ACCEPTED FORM REQUEST IS IDEMPOTENT**  
**REPLAY CANNOT CREATE DUPLICATE REAL LEADS**  
**RATE LIMIT IS BOUNDED AND BUSINESS-SAFE**  
**DIRECT BACKEND POST CANNOT BYPASS ANTI-SPAM CONTROLS**  
**JS BYPASS DOES NOT REMOVE SERVER ANTI-SPAM**  
**NORMAL RUSSIAN USER INPUT IS NOT FALSE-POSITIVE BLOCKED**

---

## QA matrix

See `00-summary.json` — all gates PASS (valid human, honeypot, too-fast, tamper, expiry, replay, rate, heuristics, direct POST, parity, indexing open, no external captcha).

SMTP / recipients / Russian mail UX unchanged (`mail_state=verified_active`, recipients=2).  
Indexing: `blog_public=1`, effective OPEN, P18G/watchdog preserved.  
QA leads cleaned via `LeadRegistry::delete_qa_rows()`.

---

## Privacy

**NO EXTERNAL CAPTCHA PROVIDER**  
**NO NEW THIRD-PARTY ANTI-SPAM DATA FLOW**

---

## Source / production parity

Exact-file deploy; `02-deploy-manifest.json` + `07-parity-recheck.json` + AntiSpam redeploy match.

**NATIVE ANTISPAM SOURCE / PRODUCTION PARITY PASS**

---

## Acceptance

FP-0002 NATIVE FORM ANTI-SPAM V1 COMPLETE — ALL CURRENT PUBLIC FORMS ARE PROTECTED BY FIRST-PARTY LAYERED ANTI-SPAM WITHOUT GOOGLE RECAPTCHA, YANDEX SMARTCAPTCHA OR ANY OTHER EXTERNAL CAPTCHA PROVIDER — HONEYPOT, SERVER-SIGNED TIME-TO-SUBMIT, IDEMPOTENCY/REPLAY PROTECTION, BOUNDED RATE LIMITING AND CONSERVATIVE SERVER-SIDE PAYLOAD HEURISTICS ARE ACTIVE — SPAM IS REJECTED BEFORE REAL LEAD PERSISTENCE, MAIL AND ANALYTICS GOALS — DIRECT POST CANNOT BYPASS SERVER CONTROLS — NORMAL RUSSIAN USER INPUT REMAINS ACCEPTED — SMTP, RECIPIENT ROUTING, RUSSIAN MAIL UX, PRIVACY AND INDEXING SAFETY REMAIN INTACT — SOURCE/PRODUCTION PARITY PASSES — CANONICAL REMOTE IS UPDATED — FP-0002 REMAINS IN NORMAL PRODUCTION / MAINTENANCE.
