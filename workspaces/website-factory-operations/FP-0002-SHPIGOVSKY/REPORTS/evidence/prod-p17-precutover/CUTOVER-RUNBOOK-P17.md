# FP-0002 — P17 Cutover Runbook (PRE-CUTOVER + CONT1)

**Status:** PRE-CUTOVER readiness pack + legacy redirects **live**.  
**NS / SSL / siteurl / SMTP / indexing:** **NOT authorized** until a later explicit charter.

---

## Distinguish redirect classes

| Class | What | State |
|-------|------|--------|
| **A. Legacy path redirects** | 7 SEO mappings in `.htaccess` | **IMPLEMENTED PRE-CUTOVER** — do not redo |
| **B. Temporary host → final domain** | `shpigovsky.beget.tech` → `https://shpigovsky.ru` | CUTOVER, after smoke |
| **C. HTTP → HTTPS** | after certificate | CUTOVER after SSL |
| **D. www ↔ apex** | planned www → apex 301 | CUTOVER after SSL |

Do **not** activate B now (duplicate public copies stay until cutover by policy).

---

## Final launch sequence

1. **Legacy redirects — DONE** (CONT1)
2. **P17 PRE-CUTOVER** (this pack)
3. Operator/Olya **content freeze**
4. Fresh **full site + DB backup**
5. Prepare/verify **Beget DNS zone** (copy mail records; replace website A)
6. **Switch NS** at REG.RU (only with explicit charter) to published Beget NS set
7. Verify **authoritative Beget DNS** (parent + Beget NS + 8.8.8.8 / 1.1.1.1 / 9.9.9.9)
8. Verify website resolves to Beget `91.106.207.76` (re-check panel IP)
9. **Issue/attach SSL** (HTTP must still answer for LE; do not force HTTPS first)
10. Verify HTTPS
11. Switch WordPress `home` / `siteurl` to `https://shpigovsky.ru` if that remains the safest proven order
12. Exact DB URL migration
13. Cache purge
14. Final-domain smoke while **indexing CLOSED**
15. **SMTP** (no PHP mail fallback)
16. Form delivery QA
17. robots / indexing open
18. Sitemap submissions
19. Final crawl

Beget evidence: SSL install can auto-change A if the domain is on Beget DNS ([SSL article](https://beget.com/ru/kb/how-to/sites/podklyuchenie-ssl-k-sajtu)). Re-check MX/SPF after SSL.

---

## NS GO / NO-GO gates

Token: `NS CUTOVER GO/NO-GO GATES READY`

| ID | Gate | CONT1 state |
|----|------|-------------|
| NS01 | Current zone inventoried | **PASS** |
| NS02 | Target Beget zone prepared | **NO-GO** — manual panel work remaining |
| NS03 | MX preserved in target zone | **PLAN READY** / not in Beget zone yet |
| NS04 | SPF preserved | **PLAN READY** / not in Beget zone yet |
| NS05 | DKIM preserved | **PUBLIC ABSENT** — confirm REG.RU panel |
| NS06 | DMARC preserved | **PUBLIC ABSENT** — nothing to copy |
| NS07 | Active subdomains preserved | **PLAN READY** (mail/ftp/smtp/pop) |
| NS08 | Verification TXT | **NONE public** — copy if later found |
| NS09 | Apex website target prepared | **IP KNOWN** (`91.106.207.76`) — panel not written |
| NS10 | www policy prepared | **DOCUMENTED** (www → apex after SSL) |
| NS11 | Stale website AAAA ruled out | **PASS** (apex/www none; mail AAAA copy) |
| NS12 | Target nameservers verified | **PUBLISHED SET RECORDED** — panel confirm still required |
| NS13 | Registrar access available | **OPERATOR** (REGRU-RU) — not proven this wave |
| NS14 | Rollback nameservers recorded | **PASS** (`ns1/ns2.hosting.reg.ru`) |
| NS15 | Operator/Olya freeze | **NOT ACTIVE** (CONT1 redirects only) |
| NS16 | Fresh full backup | **NOT THIS WAVE** (P14 backup exists; take a new one before NS) |
| NS17 | Beget FS + DB + WP Admin | **HISTORICAL PASS** + CONT1 SSH/HTTP proven for `.htaccess` |

**NS cutover decision: NO-GO** until NS02, NS13, NS15, NS16 are green and a dedicated NS charter exists.

---

## Robots / indexing

Changing NS does **not** open indexing. Keep `blog_public` closed, robots Disallow, noindex as applicable until final-domain smoke + HTTPS + SMTP/form QA + canonical/sitemap PASS.

---

## SMTP sequencing

NS/domain/SSL → WordPress final-domain switch → final-domain smoke → **SMTP** → form QA → robots/indexing.

Do not enable PHP `mail()` fallback. Pre-cutover mail suppression remains until SMTP is explicitly ready.

---

## Temporary host

Do not redirect `shpigovsky.beget.tech` to the final domain until after successful final-domain smoke. Desired later rule: path-preserving 301 to `https://shpigovsky.ru/<path>`.

---

*Runbook · P17 CONT1 · NS not switched.*
