# REPORT — FP-0002 PROD-P17 PRE-CUTOVER (CONT1)

**Date:** 2026-08-18  
**Host:** http://shpigovsky.beget.tech/  
**Future canonical:** https://shpigovsky.ru/  
**Baseline:** `FP-0002-PROD-BASELINE-2026-08-17` (extended with P17 CONT1 redirects + DNS inventory)  
**Status:** **PASS / PRE-CUTOVER READY** with NS cutover **NO-GO** until gates below

At CONT1 start the git tree had **no** committed `REPORT-FP-0002-PROD-P17-*`. This file **is** the P17 readiness report/runbook, extended with the two operator-approved CONT1 requirements (legacy 301s now; NS/DNS plan without switching NS).

## 1. Status

| Item | Result |
|------|--------|
| Overall | **PASS** for CONT1 scope |
| Legacy redirects | **7/7 LIVE** |
| DNS/NS switch | **NOT DONE** (forbidden) |
| SSL / siteurl / SMTP / robots | **NOT DONE** (forbidden) |
| Beget DNS panel writes | **NOT DONE** (credentials empty → manual instructions) |
| Git | clean worktree checkpoint (see closeout) |

Acceptance:

`FP-0002 P17 PRE-CUTOVER NOW INCLUDES A VERIFIED LEGACY REDIRECT LAYER AND A COMPLETE NAMESERVER-MIGRATION PLAN.`

Runbook: `REPORTS/evidence/prod-p17-precutover/CUTOVER-RUNBOOK-P17.md`

---

## Legacy Redirects

**7/7 LEGACY REDIRECTS LIVE** · **7/7 FINAL TARGETS = 200** · **NO REDIRECT LOOPS**

| Source | Destination | Status | Destination HTTP | Hops |
|--------|-------------|--------|------------------|------|
| `/yoga` `/yoga/` | `/o-centre/programma-lecheniya/kinezioterapiya/` | 301 | 200 | 1 |
| `/about` `/about/` | `/o-centre/` | 301 | 200 | 1 |
| `/psy` `/psy/` | `/o-centre/programma-lecheniya/psihokorrektsiya/` | 301 | 200 | 1 |
| `/home` `/home/` | `/o-centre/programma-lecheniya/` | 301 | 200 | 1 |
| `/policy` `/policy/` | `/privacy-policy/` | 301 | 200 | 1 |
| `/neuro` `/neuro/` | `/o-centre/programma-lecheniya/prostranstvo-vosstanovleniya/` | 301 | 200 | 1 |
| `/reviews` `/reviews/` | `/otzyvy/` | 301 | 200 | 1 |

- Path-relative rules (Apache expands Location on the current host; no hardcoded `https://shpigovsky.ru/...`).
- Query string preserved (`/about?utm_source=test` → `/o-centre/?utm_source=test`).
- Exact-path only; `/yoga-example/` `/about-us/` `/reviews-old/` not captured.
- WordPress smoke PASS: `/` `/uslugi/` `/o-centre/` `/privacy-policy/` `/otzyvy/` `/specyalisty/` article `/blog/nazvanie-stati/` REST `/wp-json/` Smart Search `/wp-json/shpigovsky/v1/smart-search` wp-login sitemap — all final 200.
- Pre `.htaccess` SHA `eb8dff1…8bf6` (vanilla WordPress only). Post `ec8f0602…8d9f38`. WordPress block unchanged.
- Token: `CURRENT PRODUCTION .HTACCESS PRESERVED BEFORE REDIRECT IMPLEMENTATION`
- Token: `7/7 REDIRECT TARGETS VALID` before deploy
- Token: `LEGACY REDIRECT CONFIG HAS A CANONICAL OWNER`

These seven mappings are **IMPLEMENTED PRE-CUTOVER** and must **not** be reimplemented at domain cutover.

Manifest: `REPORTS/evidence/prod-p17-precutover/REDIRECT-MANIFEST.md`

---

## DNS / NS Current State

| Item | Value |
|------|--------|
| Current NS | `ns1.hosting.reg.ru` `ns2.hosting.reg.ru` (WHOIS + recursive) |
| Registrar | REGRU-RU |
| Target NS | Published Beget: `ns1.beget.com` `ns2.beget.com` `ns1.beget.pro` `ns2.beget.pro` — **panel confirm still required** |
| Apex A | `92.255.111.71` (old hosting) |
| Beget website A | `91.106.207.76` (`shpigovsky.beget.tech`) |
| Target zone in Beget panel | **NOT WRITTEN** this wave |

Inventory: `REPORTS/evidence/prod-p17-precutover/DNS-CURRENT-ZONE-INVENTORY.md`  
Plan: `DNS-BEGET-ZONE-MIGRATION-PLAN.md`

Token: `CURRENT DNS ZONE MUST BE INVENTORIED BEFORE NAMESERVER CUTOVER`

---

## Mail DNS Preservation

| Item | State |
|------|--------|
| Mail provider | **REG.RU hosting mail** (`mx1/mx2.hosting.reg.ru`) — not Beget |
| MX | `10 mx1.hosting.reg.ru.` `20 mx2.hosting.reg.ru.` — COPY |
| SPF | `v=spf1 ip4:31.31.196.206 a mx include:_spf.hosting.reg.ru ~all` — COPY |
| DKIM | **Not in public DNS** (selector probe) — confirm REG.RU panel |
| DMARC | **Not published** |
| mail/ftp/smtp/pop | A `31.31.196.206` + AAAA `2a00:f940:2:2:1:1:0:168` — COPY |

Token: `MAIL DNS PRESERVATION PLAN = READY BEFORE NS CUTOVER`

SMTP not configured. Mail suppression MU remains.

---

## NS GO / NO-GO

Token: `NS CUTOVER GO/NO-GO GATES READY`

**Decision: NO-GO for NS switch** (as required). Gates documented in the runbook. PASS now: NS01, NS11, NS14. Published NS set recorded (NS12). Manual remaining: NS02 zone in panel, NS13 registrar access, NS15 freeze, NS16 fresh backup.

---

## NS Rollback

| Item | Value |
|------|--------|
| Current delegation | `ns1.hosting.reg.ru` `ns2.hosting.reg.ru` |
| Rollback target | Restore those two NS at REG.RU |
| Old zone retention | Keep REG.RU DNS zone during stabilization; do not delete |

Token: `NS ROLLBACK TARGET RECORDED`

---

## Final Launch Sequence

legacy redirects — **DONE**  
→ P17 PRE-CUTOVER  
→ fresh backup/freeze  
→ prepare/verify Beget DNS zone  
→ switch NS  
→ verify authoritative DNS  
→ SSL  
→ `home/siteurl` + exact URL migration  
→ cache purge  
→ final-domain smoke while indexing CLOSED  
→ SMTP  
→ form delivery QA  
→ robots/indexing  
→ sitemap submissions  
→ final crawl

---

## Source / production parity

`.htaccess` is production-owned with a canonical **fragment** in `DOCS/PRODUCTION/`. Dashboard remaining-tails updated if deployed this closeout.

---

## Git / secrets

No registrar/Beget/SMTP passwords in committed files. Secret scan required on checkpoint.

## Execution safety

- cwd: `X:\AI MARS`
- scope lock honored: yes (`FP-0002-SHPIGOVSKY` + STORAGE layer-b + production `.htaccess` only)
- destructive ops: none
- protected zone touch: `.htaccess` custom block **chartered**; DNS NS **not** mutated
