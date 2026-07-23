# ISEO-SU NON-SECRET EVIDENCE REQUEST v1

**Audience:** Operator (Andrey)  
**Programme:** ISEO-SU-SITE-OPS  
**Phase:** 2 — Non-secret site evidence intake  
**Status:** WAVE A ACTIVE — Waves B–E deferred until Wave A is reviewed  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  

Related:

- Intake ledger: [ISEO-SU-SITE-EVIDENCE-INTAKE-v1.md](ISEO-SU-SITE-EVIDENCE-INTAKE-v1.md)
- Redaction guide: [ISEO-SU-EVIDENCE-REDACTION-GUIDE-v1.md](ISEO-SU-EVIDENCE-REDACTION-GUIDE-v1.md)
- Questionnaire: [ISEO-SU-HYBRID-DISCOVERY-QUESTIONNAIRE-v1.md](ISEO-SU-HYBRID-DISCOVERY-QUESTIONNAIRE-v1.md)
- Route register: [ISEO-SU-PUBLIC-ROUTE-REGISTER-v1.md](ISEO-SU-PUBLIC-ROUTE-REGISTER-v1.md)

---

## Hard rules (all waves)

**Do not send:**

- passwords  
- tokens  
- cookies  
- session IDs  
- `wp-config.php`  
- database dumps  
- full hosting archives  
- private keys / API keys / SMTP passwords  
- secret-bearing URLs (login links with tokens, etc.)  

**Do redact** account names, emails, IPs, and filesystem home segments where not operationally needed.  
See the redaction guide before attaching screenshots or exports.

Cursor / agents will **not** log in, crawl, FTP, or open WordPress admin in this phase.

---

## WAVE A — Basic architecture (REQUESTED NOW)

Answer in plain language. No credentials.

| # | Request | Example answer shape |
|---|---------|----------------------|
| A1 | Hosting provider name | e.g. “Beget”, “Timeweb”, “other: …” |
| A2 | Control panel name | e.g. “ISPmanager”, “cPanel”, “hosting personal account”, “unknown” |
| A3 | Whether FTP/SFTP access exists | yes / no / unknown (no host/user/password) |
| A4 | Whether WordPress admin exists | yes / no / unknown (do not send login URL with secrets) |
| A5 | Whether staging/dev exists | yes / no / unknown; if yes, public hostname only if safe |
| A6 | Public list of key URLs | home, blog, tariffs, calculator, web-KP, contacts, etc. |
| A7 | Plain-language split: static vs WordPress sections | which areas feel static HTML vs WP |
| A8 | Whether current source code exists locally or in Git | local path class (no secrets) / Git remote name / none / unknown |
| A9 | Who currently maintains the site / who else has changed it | names or roles |
| A10 | Known business-critical pages/tools that must not be touched | short list |

**How to deliver Wave A:** reply in chat or paste answers into a note under this locus only after review — no secrets.

**After Wave A:** operator + agent run **PHASE 2A WAVE A EVIDENCE REVIEW**. Waves B–E are **not** requested until that review.

---

## WAVE B — Sanitized hosting / filesystem evidence (DEFERRED)

Request later, only after Wave A review:

- sanitized screenshot of domain / docroot settings  
- sanitized directory tree of top-level site folders  
- sanitized indication of WordPress directory location  
- sanitized rewrite / config **filename** list only  
- **no** file contents that may contain secrets  

---

## WAVE C — Sanitized WordPress evidence (DEFERRED)

Request later, only after Wave A review:

- WordPress version  
- PHP version  
- active theme and child theme names  
- plugin list (names + versions if available)  
- ACF status (active / inactive / unknown)  
- CPT / taxonomy list if known  
- screenshots **without** usernames, emails, tokens, license keys, or sensitive notices  

---

## WAVE D — Custom tools (DEFERRED)

Request later, only after Wave A review:

- URLs or route names for calculator and web-KP  
- plain-language purpose of each tool  
- known source folders/files (names only)  
- external integrations (names only; no keys)  
- business-critical restrictions (“do not change X”)  

---

## WAVE E — Backup and ownership (DEFERRED)

Request later, only after Wave A review:

- current backup method (plain language)  
- retention (if known)  
- restore owner  
- source-of-truth location (hosting / Git / mixed / unknown)  
- known manual production changes  
- files or areas that must **never** be overwritten  

---

## Current operator action

1. Complete **Wave A** only.  
2. Apply redaction if attaching any screenshot.  
3. Do **not** send Waves B–E yet.  
4. Do **not** authorize production connection.

---

*Non-secret evidence request v1 · 2026-07-22 · Wave A active.*
