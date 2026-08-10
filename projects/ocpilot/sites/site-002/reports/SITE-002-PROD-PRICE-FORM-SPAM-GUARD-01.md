# REPORT — SITE-002 Price Form Spam Guard 01

**Operation:** `SITE-002-PROD-PRICE-FORM-SPAM-GUARD-01`  
**OCPilot run:** **4.321**  
**Date:** 2026-08-10  
**Production:** https://bzpm.ru/  
**Verdict:** `SITE-002 PRICE FORM SPAM GUARD COMPLETE — READY FOR OBSERVATION`

## 1. Scope

Diagnose and apply layered anti-spam for SITE-002 form handler, focused on dialog 7 / dealer-price-list spam, without breaking legitimate forms, without import/1C/category/Client Ops changes.

## 2. Operator request

While waiting for 1C specialists, new spam arrives through SITE-002 forms:

- Subject: `ЗПМ: новая заявка — Форма дилерам и оптовикам`
- Dialog ID: `7`
- Random Latin name/message pairs; suspicious emails; proxy/Tor-like IPs
- Form delivery works after Run 4.320; issue is non-empty bot payloads

## 3. Client Ops boundary

Client Ops / n8n / Telegram / MetaBOT **not** touched.

## 4. Preflight

- Volume `X:` label **AI WS**
- Dirty main (`X:\AI MARS`) read-only only; foreign WIP out of scope
- Prior authority worktree on `site-002-git-authority-realign-after-wave-e` @ `812d1515` (behind origin) — left untouched
- Clean commit worktree: `X:\AI MARS STORAGE\git-sync-e01\repo-site002-spam-guard-01`
- Branch: `site-002-price-form-spam-guard-01` from `origin/mars/canonical-post-recovery`
- Prior fix commit `d76a68f7` is ancestor of origin

## 5. Reports read / current state

- Run 4.320 fixed FormData-before-disable in `main.js` (dealer / fancybox / corp CTA)
- Empty-lead guard (4.264+) still rejects service-only/whitespace
- Stack: CSRF + reCAPTCHA success + empty guard + mail renderer
- Recipients admin-managed; not changed in this run

## 6. Spam evidence

Sanitized operator samples (dialog 7):

| Approx TS | Name pattern | Message pattern | Email domain | IP |
|-----------|--------------|-----------------|--------------|-----|
| 2026-08-09 10:15:53 | `oUMTrjxivfGTftQr` | `DtDRggHFutZPgxdOZamEw` | comcast.net | 185.220.100.246 |
| 2026-08-09 14:28:02 | `AluEItLmywcRDjNcoqQ` | `anQMgYLZZPlftCSf` | sbcglobal.net | 204.8.96.140 |
| 2026-08-10 07:02:39 | `TgGwxYYWAWaBYXHCqfieNFm` | `IaOmKwLEVTTYyRSCxI` | gmail.com (dotted local) | 23.129.64.188 |

Pattern: non-empty Latin gibberish name+message; passes empty guard; no Russian business text.  
Application mail logs for exact timestamps: **SAFE UNKNOWN** (not available as structured form audit on FTP).

## 7. Form source map

1. Home/about dealers & price-list UI → `form.zpm-form` hidden `dialog=7`
2. JS `assets/js/main.js` builds FormData **before** loading disable (4.320 intact)
3. POST `index.php?route=checkout/anketa`
4. Backend: CSRF → reCAPTCHA → field map → empty guard → **new spam guard** → mail

## 8. Anti-spam design

Layered scoring (threshold 8), plus honeypot fake-OK:

1. Honeypot `zpm_hp` filled → reject with fake `ok:true` (no mail)
2. Fill timestamp `zpm_ft` too fast / odd / missing → soft score
3. Gibberish Latin name/message heuristics → strong score
4. Suspicious email patterns (dotted localpart, weak domains) → soft score
5. reCAPTCHA score soft signals if present
6. File rate-limit IP+dialog (soft ≥6 / hard ≥12 in 120s) via `DIR_CACHE/zpm_form_rl`
7. Dialog 7 double-gibberish bonus
8. Sanitized reject log `zpm_form_spam.log` when writable

Empty-lead guard and recipients unchanged. No country/IP range bans. No third-party service.

## 9. Before tests

Before patch (9/9 for documented expectations):

- Valid human dialog7 / callback / product / about → **200**
- Empty guard → **400**
- Screenshot-like spam → **200** (mail path open) — confirms need for guard

## 10. Implementation

Production files:

- `public_html/catalog/controller/checkout/anketa.php`
- `public_html/assets/js/main.js`

Repo mirrors:

- `projects/ocpilot/sites/site-002/tools/checkout_anketa_price_form_spam_guard.php`
- `projects/ocpilot/sites/site-002/tools/main_js_price_form_spam_guard.js`

JS injects `zpm_hp` + `zpm_ft` into `.zpm-form` on DOM ready.  
Run 4.320 FormData-before-disable markers preserved (3 sites).

Retune after first after-battery: softened rate-limit (soft/hard levels) and recaptcha low-score weight so legitimate rapid regression tests are not false-positive blocked.

## 11. Deploy plan / backups

- Backups: `backups/anketa.php.ftp-before`, `backups/main.js.ftp-before`
- Deploy: STOR exact two files; SHA verified via RETR
- Final live SHA:
  - anketa `c63981b43d9b7592c1a812af3c2a7781899fa47b34aa0064ccf6e1c8e737382d`
  - main.js `656601534c37809d5787e1e184a00a758a3ed8c23b4b85bcfdbd236c802f45dd`

## 12. FTP deploy / cache

- FTP writes: **2** files
- Global `storage/modification/` clear: **not** performed
- Test cache-bust query only; rate-limit cache clear attempted (dir may be created on first hit)

## 13. After tests

Authoritative retune battery **9/9 PASS**:

| Test | Result |
|------|--------|
| valid human dialog7 | 200 |
| spam screenshot ×3 | 400 (no mail path) |
| honeypot | 200 fake-ok |
| callback dialog2 | 200 |
| product dialog1 | 200 |
| empty guard | 400 |
| about dialog7 | 200 |

## 14. Public smoke

Home /katalog /about /dealers + discovered category/product + `main.js` asset: **6/6 PASS**  
No PHP fatal; no public `БЗПМ`; FormData fix + spam helper present in JS.

## 15. Regression / mutation summary

| Item | Count |
|------|------:|
| production DB writes | 0 |
| production FTP writes | 2 (+ anketa retune STOR) |
| PHP changes | 1 |
| JS changes | 1 |
| template changes | 0 |
| cache clear global | 0 |
| import runs | 0 |
| scheduler / baseline / category/product | 0 |
| redirects / `.htaccess` | 0 |
| Client Ops / n8n / Telegram | 0 |
| dirty main | 0 |

## 16. Docs update

OPERATIONAL-INDEX run **4.321**, OCPILOT-STATE, production-profile, site-passport, knowledge map, tools README.

Durable rule: SITE-002 form anti-spam is layered (empty guard + honeypot/timestamp/risk/rate-limit); dialog 7 gibberish pattern; Run 4.320 FormData fix must not regress.

## 17. Decision

- Classification: `PRICE_FORM_SPAM_GUARD_COMPLETE`
- Next: `READY_FOR_OBSERVATION`
- Final: **`SITE-002 PRICE FORM SPAM GUARD COMPLETE — READY FOR OBSERVATION`**

## 18. Production mutation summary

Exact FTP only for anketa.php + main.js. No DB writes. Recipients unchanged.

## 19. Git/worktree summary

- Commit worktree: `X:\AI MARS STORAGE\git-sync-e01\repo-site002-spam-guard-01`
- Branch: `site-002-price-form-spam-guard-01` → push `origin/mars/canonical-post-recovery`
- Dirty main / prior authority WIP: out of scope

## 20. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-PRICE-FORM-SPAM-GUARD-01\`

## 21. SAFE UNKNOWN / blockers

- Exact count of organic spam since 2026-08-09 beyond operator screenshots: **SAFE UNKNOWN**
- Whether reCAPTCHA scores for real bots are stored historically: **SAFE UNKNOWN** (verify API score used only as soft live signal)
- Whether `DIR_CACHE/zpm_form_rl` persists across host cache wipes: **SAFE UNKNOWN** (fail-open if unwritable)
- Stronger CAPTCHA/WAF: not required now; observe mailbox for residual spam

## 22. Final verdict

**`SITE-002 PRICE FORM SPAM GUARD COMPLETE — READY FOR OBSERVATION`**

## 23. Next recommendation

1. Observe `client.leads@polygon-ws.ru` / `info@bzpm.ru` for residual dialog-7 spam for 48–72h.
2. If spam continues with Cyrillic/human-like text, consider stronger CAPTCHA score hard floor or WAF charter.
3. Optional: inspect `system/storage/logs/zpm_form_spam.log` after traffic accumulates.
4. 1C offers attention from Run 4.320 remains open and out of this charter.
