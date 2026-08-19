# RUNBOOK — FP-0002 PROD-P18 FINAL DOMAIN CUTOVER (CURRENT EXECUTION STATE)

**Wave executed:** **P18H** — privacy/retention decisions + launch-tail readiness (2026-08-20)  
**Prior:** **P18G** indexing safety · **P18E** cookie/consent · **P18D-FU01** SMTP closeout  
**P18 remainder:** sitemap submissions · final crawl · launch closeout (P18I).

Historical trigger `NS SWITCHED` and WordPress `home`/`siteurl` cutover are **complete** (operator). **Indexing is OPEN — human-approved (Olya/admin); do not close without explicit human command.**

---

## Current facts (P18D-FU01 closeout)

| Surface | Value |
|---------|--------|
| WordPress `home` | `https://shpigovsky.ru` |
| WordPress `siteurl` | `https://shpigovsky.ru` |
| Core target | `0.3.16-p18d-fu01` |
| SMTP Admin | **Настройки сайта → Почта и формы** |
| SMTP state | **VERIFIED / ACTIVE** |
| SMTP transport | `smtp.beget.com` port `465` encryption `ssl` |
| Sender | `noreply@shpigovsky.ru` |
| Mail suppression | **OFF** (delivery_active=1 → should_suppress()=false) |
| Suppression MU | **REMOVED** |
| Lead registry | table `fp02_form_leads` schema v1 **ACTIVE** |
| Form QA | PASS — MAIL_ACCEPTED status recorded |
| Leads Admin | **Заявки** top-level — reachable |
| Metrika form goals | Admin-configurable; counter owner = SEO |
| Indexing | **OPEN** (`blog_public=1`) — **HUMAN-APPROVED**; P18G guard active |
| Public apex | WordPress currently visible on `https://shpigovsky.ru/` |
| Source ↔ production | SMTP/forms closeout surfaces verified; dashboard/core sync handled in FU01 |

**Do not revert** `home`/`siteurl` to `shpigovsky.beget.tech`.

---

## Operator next (post-P18H)

1. **Do not close indexing** without explicit human command — current truth: **OPEN — HUMAN-APPROVED**; P18G guard active.
2. Optional: final legal sign-off on Cookie Policy (factually current).
3. Optional: set `lead_retention_days=730` in **Настройки сайта → Почта и формы** when operator accepts P18H recommendation (no auto-purge of historical leads).
4. **P18I:** submit sitemap to Search Console / Yandex Webmaster; run final crawl.

---

## Remaining P18 (post-P18H)

1. **P18I** — sitemap submissions + final production crawl + launch closeout.
2. Operator legal sign-off on Cookie Policy (non-blocking for P18I).
3. Privacy Policy retention wording alignment when lead retention is enabled.

**P18H RECOMMENDATION:** Form lead retention **730 days** — production config remains `0` until operator saves Admin.

**OPEN BUSINESS DECISION (narrow):** Apply recommended `lead_retention_days=730` + align Privacy Policy retention sentence.

Exact leftover URL objects still listed in `REPORTS/evidence/prod-p17-fu02-final-tail/CUTOVER-DB-MUTATION-PLAN.json` (skip `home`/`siteurl` — already done).

---

## Forbidden

- Opening indexing as a deploy side effect  
- Claiming SMTP VERIFIED because fields exist  
- Asking for / storing the mailbox password in Cursor, Git, reports, or Dashboard  
- Leaving two competing mail switches after VERIFIED/ACTIVE  
- Temporary-host 301 if it would send users to the **legacy** origin  
- Treating Dashboard indexing button as launch authorization

P18B reports remain historical for Dashboard/indexing. P18C remains historical for SMTP/forms internals. Do not treat P18C as proof that the left-menu item was discoverable — that gap is closed in FU01.
