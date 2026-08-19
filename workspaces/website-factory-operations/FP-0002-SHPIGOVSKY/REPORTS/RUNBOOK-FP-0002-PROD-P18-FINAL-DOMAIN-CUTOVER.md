# RUNBOOK — FP-0002 PROD-P18 FINAL DOMAIN CUTOVER (CURRENT EXECUTION STATE)

**Wave executed:** **P18D-FU01** — fresh production intake, SMTP transport correction (none→ssl/465), verification, activation, physical suppression-MU retirement, bounded post-removal form QA, exact QA cleanup, indexing re-close, Olya/Admin truth preservation (2026-08-19)  
**P18 remainder:** public-domain finalization only if regression appears · Olya indexing approval · sitemaps · crawl.

Historical trigger `NS SWITCHED` and WordPress `home`/`siteurl` cutover are **complete** (operator). Do **not** wait for NS or URL cutover anymore. Do **not** open indexing automatically. Do **not** rollback current editor-owned DB content from an older backup to recover technical state.

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

## Operator next (P18D-FU01 complete — current handoff)

1. Do **not** open indexing without Olya approval or explicit operator command.
2. Observe public `https://shpigovsky.ru/`; if operator sees a routing regression, open a bounded public-domain finalization wave.
3. Keep current editor/Admin DB state as content truth; do not restore an old full DB backup over live editorial changes.

---

## Remaining P18 (post-P18D)

1. Public-domain finalization only if regression appears.
2. Indexing **only** after Olya (Dashboard «Открыть индексацию») or explicit operator command.
3. Sitemap submissions (manual).
4. Final crawl.

**OPEN BUSINESS DECISION:** Form lead retention period — `lead_retention_days=0` — operator sets when ready.

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
