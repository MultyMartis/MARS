# RUNBOOK — FP-0002 PROD-P18 FINAL DOMAIN CUTOVER (CURRENT EXECUTION STATE)

**Wave executed:** **P18C** — SMTP / forms Admin foundation (2026-08-19)  
**P18 remainder:** operator SMTP credentials → verification → real form QA · public apex → WordPress bind · Olya indexing · sitemaps · crawl.

Historical trigger `NS SWITCHED` and WordPress `home`/`siteurl` cutover are **complete** (operator). Do **not** wait for NS or URL cutover anymore. Do **not** open indexing automatically. Do **not** claim SMTP verified until the operator saves real settings and a later wave tests delivery.

---

## Current facts (P18C verification)

| Surface | Value |
|---------|--------|
| WordPress `home` | `https://shpigovsky.ru` |
| WordPress `siteurl` | `https://shpigovsky.ru` |
| Core | `0.3.12-p18c` |
| SMTP Admin | Настройки сайта → Почта и формы |
| SMTP state | **NOT CONFIGURED** (credentials not entered) |
| Sender | `noreply@shpigovsky.ru` |
| Mail suppression | **ON** (`delivery_active=0`) |
| Lead registry | table `fp02_form_leads` schema v1 **ACTIVE** |
| Metrika form goals | Admin-configurable; counter owner = SEO |
| Indexing | **CLOSED** (`blog_public=0`) |
| Public apex | still observed as **legacy Craftum** at P18C intake |
| Source ↔ production | **14/14 MATCH** |

**Do not revert** `home`/`siteurl` to `shpigovsky.beget.tech`.

---

## Operator next (this is the current handoff)

1. Open **Настройки сайта → Почта и формы**.  
2. Enter SMTP host, port, encryption, username, password, recipients.  
3. Save. (Save does **not** verify SMTP and does **not** enable sending.)  
4. Do **not** open indexing.  
5. Report that settings are saved — next wave verifies real SMTP.

---

## Remaining P18 (after operator SMTP save)

1. SMTP verification test (Admin «Отправить тестовое письмо»).  
2. Operator activates outbound delivery.  
3. Real form delivery QA.  
4. Bind public apex + www so they serve **this** WordPress docroot.  
5. Confirm visitors to `https://shpigovsky.ru/` get WordPress (not Craftum).  
6. Indexing **only** after Olya (Dashboard «Открыть индексацию») or explicit operator command.  
7. Sitemap submissions (manual).  
8. Final crawl.

Exact leftover URL objects still listed in `REPORTS/evidence/prod-p17-fu02-final-tail/CUTOVER-DB-MUTATION-PLAN.json` (skip `home`/`siteurl` — already done).

---

## Forbidden

- Opening indexing as a deploy side effect  
- Claiming SMTP VERIFIED because fields exist  
- Asking for / storing the mailbox password in Cursor, Git, reports, or Dashboard  
- Leaving two competing mail switches after VERIFIED/ACTIVE (retire the MU)  
- Temporary-host 301 if it would send users to the **legacy** origin  
- Treating Dashboard indexing button as launch authorization

P18A/P18B reports remain historical. Do not use P18A “NS pending” Dashboard copy. Do not use P18B “SMTP PENDING implementation” as if Admin SMTP owner were still missing.
