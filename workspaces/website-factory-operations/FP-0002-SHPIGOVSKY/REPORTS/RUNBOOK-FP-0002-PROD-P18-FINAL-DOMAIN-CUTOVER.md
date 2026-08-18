# RUNBOOK — FP-0002 PROD-P18 FINAL DOMAIN CUTOVER (CURRENT EXECUTION STATE)

**Wave executed:** **P18A** — live-domain reality intake + legal demo state (2026-08-18)  
**P18 remainder:** SSL / public-origin bind / HTTPS smoke / redirects / SMTP / indexing — **not** this file’s remaining phases.

Historical trigger `NS SWITCHED` is **complete** (operator). Do **not** wait for NS or `home`/`siteurl` cutover anymore.

---

## Current facts (P18A intake)

| Surface | Value |
|---------|--------|
| WordPress `home` | `https://shpigovsky.ru` |
| WordPress `siteurl` | `https://shpigovsky.ru` |
| NS | Beget set observed (`ns1/ns2.beget.com` / `.pro` / `.ru`) |
| Public apex A (8.8.8.8) | `45.130.41.70` — **not** the Beget WP vhost `91.106.207.76` |
| Local resolver apex A | `92.255.111.71` (legacy REG.RU IP, cache/split) |
| Public `https://shpigovsky.ru/` | **Legacy site** (not WordPress) at intake |
| WordPress runtime | `http://shpigovsky.beget.tech` (inner routes 200; `/` 301 → public apex) |
| SSL on public apex | Let's Encrypt **valid** on the **legacy** origin |
| SSL on `shpigovsky.beget.tech:443` | timeout / not usable |
| `blog_public` | `0` |
| Mail suppression | ON |

**Do not revert** `home`/`siteurl` to `shpigovsky.beget.tech`.

---

## Remaining P18 (after P18A)

1. Bind public apex + www so they serve **this** WordPress docroot (Beget site/domain mapping / A as Beget instructs).  
2. Issue/attach SSL for **that** WordPress origin. Verify cert SAN, apex, www.  
3. HTTP and HTTPS on the **WordPress** host — no loop.  
4. Only then enable unconditional HTTP→HTTPS (if not already correct on the WP vhost).  
5. Host-conditional `shpigovsky.beget.tech` → `https://shpigovsky.ru` after WordPress HTTPS smoke.  
6. Bounded URL cleanup from P17-FU02 mutation plans (robots sitemap host, leftover absolute beget URLs). Serialization-safe. **No** blind search-replace.  
7. Cache purge. Smoke while indexing **CLOSED**.  
8. SMTP (PHASE B). Remove mail suppression only then.  
9. Form delivery QA.  
10. Indexing (PHASE C).  
11. Sitemap submissions.  
12. Final crawl.

Exact leftover objects still listed in `REPORTS/evidence/prod-p17-fu02-final-tail/CUTOVER-DB-MUTATION-PLAN.json` (skip `home`/`siteurl` — already done).

---

## Forbidden until WordPress HTTPS PASS

- Opening `blog_public` / robots Allow  
- SMTP as “done”  
- Temporary-host 301 if it would send users to the **legacy** origin  
- Re-running old P18 step “change home/siteurl”

*P18A executed. Remaining = SSL + origin bind + launch tails.*
