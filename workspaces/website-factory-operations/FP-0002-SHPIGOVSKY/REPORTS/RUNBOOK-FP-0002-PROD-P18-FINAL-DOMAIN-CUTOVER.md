# RUNBOOK — FP-0002 PROD-P18 FINAL DOMAIN CUTOVER (CURRENT EXECUTION STATE)

**Wave executed:** **P18E-A/B** — fresh production/privacy/legal/tracker re-intake, consent foundation deploy, exact-file parity, Dashboard truth update, Admin discoverability and persistence proof, frontend no-change proof (2026-08-19)  
**Latest planning wave:** **P18E-C/D** — public cookie notice/settings UX + real conditional Yandex Metrika loading  
**P18 remainder:** P18E-C/D frontend gating · P18E-E/F form-goal consent + withdrawal/policy integration · public-domain finalization only if regression appears · Olya indexing approval · sitemaps · crawl.

Historical trigger `NS SWITCHED` and WordPress `home`/`siteurl` cutover are **complete** (operator). Do **not** wait for NS or URL cutover anymore. Do **not** open indexing automatically. Do **not** rollback current editor-owned DB content from an older backup to recover technical state.

---

## Current facts (P18E-A/B closeout)

| Surface | Value |
|---------|--------|
| WordPress `home` | `https://shpigovsky.ru` |
| WordPress `siteurl` | `https://shpigovsky.ru` |
| Core target | `0.3.17-p18e-ab` |
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
| Cookie/privacy controls | **FOUNDATION READY / FRONTEND PENDING** |
| Indexing | **CLOSED** (`blog_public=0`) |
| Public apex | WordPress currently visible on `https://shpigovsky.ru/` |
| Source ↔ production | SMTP/forms closeout surfaces verified; dashboard/core sync handled in FU01 |

**Do not revert** `home`/`siteurl` to `shpigovsky.beget.tech`.

---

## Operator next (P18D-FU01 complete — current handoff)

1. Do **not** open indexing without Olya approval or explicit operator command.
2. Next privacy wave starts from the deployed `PrivacyConsent` foundation; do **not** bypass it with ad-hoc banner/theme patches.
3. Observe public `https://shpigovsky.ru/`; if operator sees a routing regression, open a bounded public-domain finalization wave.
4. Keep current editor/Admin DB state as content truth; do not restore an old full DB backup over live editorial changes.

---

## Remaining P18 (post-P18D)

1. P18E-C/D: public cookie notice/settings + actual Yandex Metrika consent-gating.
2. P18E-E/F: form-goal consent gating + withdrawal/policy integration.
3. Public-domain finalization only if regression appears.
4. Indexing **only** after Olya (Dashboard «Открыть индексацию») or explicit operator command.
5. Sitemap submissions (manual).
6. Final crawl.

**OPEN BUSINESS DECISION:** Form lead retention period — `lead_retention_days=0` — operator sets when ready.

Exact leftover URL objects still listed in `REPORTS/evidence/prod-p17-fu02-final-tail/CUTOVER-DB-MUTATION-PLAN.json` (skip `home`/`siteurl` — already done).

---

## Forbidden

- Opening indexing as a deploy side effect  
- Treating P18E design as if the cookie/privacy control is already live  
- Claiming SMTP VERIFIED because fields exist  
- Asking for / storing the mailbox password in Cursor, Git, reports, or Dashboard  
- Leaving two competing mail switches after VERIFIED/ACTIVE  
- Temporary-host 301 if it would send users to the **legacy** origin  
- Treating Dashboard indexing button as launch authorization

P18B reports remain historical for Dashboard/indexing. P18C remains historical for SMTP/forms internals. Do not treat P18C as proof that the left-menu item was discoverable — that gap is closed in FU01.
