# REPORT — FP-0002 PROD-P17-FU02 Final Pre-Cutover Tail

**Date:** 2026-08-18  
**Host:** http://shpigovsky.beget.tech/  
**Future canonical:** https://shpigovsky.ru/  
**Baseline:** `FP-0002-PROD-BASELINE-2026-08-17` (extended with P17-FU02)  
**Core:** `0.3.9-p17fu02`

Acceptance:

`PROD-P17-FU02 COMPLETE — ALL INTERNAL PRE-CUTOVER TAILS CLOSED — MARS-RUNTIME RESOLVED — WEBROOT CLEAN — USERS/ACTIVITY/SERVICE STATUS CURRENT — REDIRECTS VERIFIED — FINAL DOMAIN DB/FILE MUTATION SETS EXECUTABLE WITHOUT DISCOVERY — FORMS/SMTP/INDEXING SEQUENCED — FREEZE + MANUAL NS HANDOFF READY — FP-0002 READY FOR OPERATOR MANUAL NS SWITCH`

---

## 1. Status

| Item | Result |
|------|--------|
| Overall | **PASS** |
| Production writes | YES (scoped): dashboard/core/forms deploy; obsolete webroot removal; rollback of probe-created pages/menus; one publish URL host strip |
| DB/service writes | YES (scoped): `fp02_metacode_system_meta`; `wp_page_for_privacy_policy` restored to `3`; post 750 + 5 `generic_page_body` URL hosts; activity rows for probe junk purged |
| Cleanup | YES: `mars-runtime/`, `app/`, empty `debug.log`, two BROKEN-MPEGTS `.bak` |
| Git | clean-worktree checkpoint (see §23) |
| WPilot writes | **0** (`write_enabled=false`) |
| NS / SSL / siteurl / SMTP / robots open | **NOT DONE** (forbidden) |

`INTERNAL PRE-CUTOVER READINESS = GO`  
`MANUAL NS SWITCH = OPERATOR ACTION REQUIRED`

---

## 2. Current Reality

`P17-FU02 CURRENT PRODUCTION REALITY VERIFIED`

- Runtime Production / Beget; `WP_ENVIRONMENT_TYPE=production`; WP_DEBUG off  
- `home`/`siteurl` = `http://shpigovsky.beget.tech`  
- `blog_public=0`; robots `Disallow: /`; home meta `noindex, nofollow`  
- Mail: MU `pre_wp_mail` present  
- Focus source files MATCH origin; one dirty-worktree `content-page.php` extra-blank-line WIP **not** production drift (prod SHA = origin SHA `37aaac70…`)  
- FU02 deploy **3/3 MATCH**

---

## 3. `mars-runtime/`

See `REPORTS/evidence/prod-p17-fu02-final-tail/MARS-RUNTIME-RESOLUTION.md`.

| Field | Value |
|-------|--------|
| Path | `…/public_html/mars-runtime` |
| Owner | leftover local MLI scripts |
| Public | PHP executed on GET (security) |
| Action | snapshot + **removed** |

`MARS-RUNTIME STATUS RESOLVED`

Probe GET of `populate-fp-0002-pages.php` created 12 stub pages + 15 menu items; **rolled back**. Privacy option restored to `3`. Live smoke 200.

---

## 4. Webroot Hygiene

`PUBLIC WEBROOT PRE-CUTOVER HYGIENE = PASS`

Removed (after tar SHA `199fd6be…`): mars-runtime, app/, empty debug.log, two 27MB BROKEN-MPEGTS `.bak`. Working interview MP4 still 200. `acf-json/` at docroot kept (403 listing; not proven disposable). Post-removal mutating PHP URLs **404**.

---

## 5. Users/Admin

`PRODUCTION USER/ADMIN SET = CLEAN`

| Login | Role | Email |
|-------|------|--------|
| admin | Administrator | ola4seo@yandex.ru (Olya) |
| mars | Administrator | support@polygon-ws.ru |
| metacode | Administrator | metacode@polygon-ws.ru |

No `@localhost.test` users. No bootstrap `mli_admin_fp0002`. No duplicate QA admin. Passwords not rotated/exposed.

---

## 6. Activity Log

Table `fp02_user_activity_log` exists; schema version `1`; 55 rows before probe. Real Olya history preserved. No leftover P12/P13/FU01 QA strings. Probe-created user_id=0 rows for IDs 2038–2064 **purged** after rollback. Technical update of post 750 (new-site URL) may appear as a later system/update row — real FU02 history, not junk.

---

## 7. MetaCODE Dashboard

`METACODE DASHBOARD = READY FOR MANUAL NS SWITCH`

Widget now shows: site / current state (P17-FU02, READY FOR MANUAL NS SWITCH, MATCH, 7/7, WPilot write disabled, debug off, mail suppressed, indexing closed) / DNS (manual operator, REG.RU → Beget, no credentials) / next steps 1–7. No P06/P16 open tails.

---

## 8. Redirects

`7/7 LEGACY REDIRECTS = PASS`

All slash and no-slash variants: 301 → valid 200, 1 hop, no loops, query preserved, negative prefixes 404 (`/yoga-example/`, `/about-us/`, `/reviews-old/`). Not modified.

---

## 9. Temporary Host Dependencies

`FINAL DOMAIN MUTATION SET IS EXACT AND BOUNDED`

Manifest: `FINAL-TEMP-HOST-MUTATION-MANIFEST.md` + `.json`.  
Live HTML beget hrefs = class **B** (home_url). Class **A** = home/siteurl + two ACF option URLs + listed postmeta URL keys. GUIDs / `.test` notices = **D**. No UNKNOWN live-impacting class.

---

## 10. DB Cutover Plan

`CUTOVER DB PLAN = EXECUTABLE WITHOUT DISCOVERY`  
`CUTOVER-DB-MUTATION-PLAN.json` — exact keys/IDs, plain strings, WP APIs, rollback values. Not executed. No broad SQL.

---

## 11. File Cutover Plan

`CUTOVER FILE PLAN = EXECUTABLE WITHOUT DISCOVERY`  
`CUTOVER-FILE-MUTATION-PLAN.md` — PHASE A domain/SSL, PHASE B SMTP, PHASE C indexing. Legacy 301s already live.

---

## 12. Canonical Host

`FINAL CANONICAL HOST POLICY RECORDED`  
`https://shpigovsky.ru/` · www → apex 301. Not activated.

---

## 13. Temporary Beget Host

`TEMPORARY HOST POST-CUTOVER POLICY RECORDED`  
Host-conditional 301 `shpigovsky.beget.tech` → `https://shpigovsky.ru%{REQUEST_URI}` after smoke. Not activated.

---

## 14. SSL

`SSL CUTOVER STEPS READY` (DNS → cert → HTTP/HTTPS verify → then HTTPS redirects → then WP domain). Not executed.

---

## 15. Forms / SMTP

`FORMS READY FOR POST-DNS SMTP CONFIGURATION`  
One AJAX owner (`ConsultationHandler`). No PHP `mail()`. Recipient constant unused until SMTP.

---

## 16. Mail Suppression

Owner: `fp02-pre-cutover-mail-suppression.php`. Remove in **P18 PHASE B** only, after domain smoke, then SMTP, then form QA.

---

## 17. Indexing

`TEMPORARY HOST REMAINS NON-INDEXABLE UNTIL FINAL DOMAIN + SMTP SMOKE`  
`blog_public=0`, robots Disallow, meta noindex. Not opened.

---

## 18. Pre-Cutover Crawl

85 URLs; **2xx=85**, 3xx/4xx/5xx=0; broken=0. Intentional noindex on HTML. Live `new-site.space` on `/blog/nazvanie-stati/` **fixed**. `.test`/`localhost` not in live HTML. Hardcoded beget hrefs = dynamic class B.

---

## 19. Freeze

`PRE-CUTOVER FREEZE RUNBOOK READY`  
`REPORTS/RUNBOOK-FP-0002-PRE-CUTOVER-FREEZE.md`  
`FRESH FULL BACKUP TAKEN AFTER CONTENT FREEZE` remains a **launch gate** (not taken this wave). Proven process: P14 `_p14_full_backup.py` → `X:\AI MARS STORAGE\backups\fp-0002\`.

---

## 20. Manual NS Handoff

`MANUAL NS SWITCH HANDOFF READY`  
`REPORTS/RUNBOOK-FP-0002-MANUAL-NS-SWITCH-HANDOFF.md`

---

## 21. Go / No-Go

`INTERNAL PRE-CUTOVER READINESS = GO`  
`MANUAL NS SWITCH = OPERATOR ACTION REQUIRED`

---

## 22. Source / Production Parity

**3/3 FU02 deploy MATCH.**  
Theme/plugin/MU vs origin: MATCH (dirty local `content-page.php` extra newlines = foreign WIP, not prod). No unresolved operator/Olya file drift vs Beget.

---

## 23. Git

Clean worktree checkpoint `16706398f03825b054ce75c56e8af48ec4349329` (`FP-0002: close final pre-cutover tails`) plus follow-up `e9f623330deb58a5e928d4b457c37aff27c2132e` (`docs(fp-0002): record P17-FU02 git checkpoint`) on `origin/mars/canonical-post-recovery`. Dirty main / foreign WIP **untouched**. Secret scan on staged paths **PASS**. No registrar/DNS/SMTP credentials. Dashboard `git_sha` = `16706398f03825b054ce75c56e8af48ec4349329`.

---

## 24. Remaining Work

MANUAL NS SWITCH  
→ DNS verification  
→ SSL/domain cutover  
→ SMTP  
→ robots/indexing  
→ sitemap submissions  
→ final crawl  

P18 skeleton: `REPORTS/RUNBOOK-FP-0002-PROD-P18-FINAL-DOMAIN-CUTOVER.md` — **not executed**. Trigger: operator `NS SWITCHED`.

---

## 25. Acceptance

See header. Desired state: nothing inside WordPress/MARS remains to be figured out before launch. Next action is the operator's manual NS switch in REG.RU after freeze + full backup.
