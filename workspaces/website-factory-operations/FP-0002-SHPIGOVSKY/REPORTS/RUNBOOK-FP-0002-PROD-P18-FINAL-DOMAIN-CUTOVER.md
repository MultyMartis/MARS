# RUNBOOK — FP-0002 PROD-P18 FINAL DOMAIN CUTOVER (CURRENT EXECUTION STATE)

**Wave executed:** **P18B** — Dashboard reality + safe indexing control (2026-08-19)  
**P18 remainder:** public apex → WordPress bind · SMTP · forms/Metrika/lead stats · Olya indexing · sitemaps · crawl.

Historical trigger `NS SWITCHED` and WordPress `home`/`siteurl` cutover are **complete** (operator). Do **not** wait for NS or URL cutover anymore. Do **not** open indexing automatically.

---

## Current facts (P18B verification)

| Surface | Value |
|---------|--------|
| WordPress `home` | `https://shpigovsky.ru` |
| WordPress `siteurl` | `https://shpigovsky.ru` |
| NS | Operator: **DONE**. Dashboard must not show NS as pending. Public resolver NS answers may still split. |
| Public apex A (8.8.8.8) | `45.130.41.70` |
| Public `https://shpigovsky.ru/` (latest P18B reprobe) | **Legacy Craftum CMS** (not WordPress) |
| WordPress runtime | Beget docroot; inner `http://shpigovsky.beget.tech` routes; `/` 301 → public apex |
| SSL | Let's Encrypt **valid** on the public hostname; visitor origin at latest check is **legacy** |
| `blog_public` | `0` (Admin control can change it; leave CLOSED until Olya) |
| Mail suppression | ON |
| SMTP mailbox | `noreply@shpigovsky.ru` exists; WP SMTP **PENDING** |
| Core | `0.3.11-p18b` |

**Do not revert** `home`/`siteurl` to `shpigovsky.beget.tech`.

---

## Remaining P18 (after P18B)

1. Bind public apex + www so they serve **this** WordPress docroot.  
2. Confirm visitors to `https://shpigovsky.ru/` get WordPress (not Craftum).  
3. Host-conditional `shpigovsky.beget.tech` → `https://shpigovsky.ru` only after that smoke.  
4. Bounded leftover URL cleanup from P17-FU02 plans (skip `home`/`siteurl`). Serialization-safe.  
5. SMTP using `noreply@shpigovsky.ru`. Remove mail suppression only then.  
6. Form delivery QA.  
7. Metrika form goals (backend-confirmed success → JS fire) + internal lead statistics — separate forms wave.  
8. Indexing **only** after Olya (Dashboard «Открыть индексацию») or explicit operator command.  
9. Sitemap submissions (manual; control does not submit).  
10. Final crawl.

Exact leftover objects still listed in `REPORTS/evidence/prod-p17-fu02-final-tail/CUTOVER-DB-MUTATION-PLAN.json` (skip `home`/`siteurl` — already done).

---

## Forbidden until WordPress is the public origin AND Olya approves indexing

- Opening `blog_public` / robots Allow as a deploy side effect  
- SMTP as “done”  
- Temporary-host 301 if it would send users to the **legacy** origin  
- Re-running old P18 step “change home/siteurl”  
- Treating Dashboard indexing button as launch authorization

*P18B executed. Remaining = public origin bind + SMTP + forms/indexing tails.*

P18A intake remains historical in `REPORTS/REPORT-FP-0002-PROD-P18A-LIVE-DOMAIN-LEGAL-STATE.md`. Do not use the P18A “NS pending” Dashboard copy.

