# RUNBOOK — FP-0002 PROD-P18 FINAL DOMAIN CUTOVER (SKELETON)

**Status:** PREPARED — **DO NOT EXECUTE** until the operator confirms:

`NS SWITCHED`

**Trigger:** operator confirmation in the launch chat, not inferred DNS.

This is a definition of the next wave, not an authorization to run it.

---

## Forbidden until trigger + DNS verification

- WordPress `home` / `siteurl` change
- HTTPS force / SSL attach (except after Beget DNS is authoritative)
- SMTP configuration
- robots / `blog_public` open
- sitemap submission
- registrar NS writes

---

## P18 sequence (after NS SWITCHED)

1. Verify actual public delegation (WHOIS + parent + 8.8.8.8 / 1.1.1.1 / 9.9.9.9).
2. Verify authoritative Beget DNS vs inventory.
3. Verify apex A = Beget website IP; www policy/record; MX/TXT preserved.
4. Request/attach SSL. Verify cert subject/SAN. HTTP must still answer until cert is live.
5. Verify HTTP and HTTPS on the final host.
6. **Only then** enable HTTPS redirects (file plan PHASE A).
7. **Only then** WordPress final-domain mutations (`CUTOVER-DB-MUTATION-PLAN.json` + `CUTOVER-FILE-MUTATION-PLAN.md`). Serialization-safe, no broad SQL search-replace.
8. Host-conditional temporary-host 301 (`shpigovsky.beget.tech` → `https://shpigovsky.ru`) after final-domain smoke.
9. Cache purge.
10. Smoke on https://shpigovsky.ru/ while indexing still CLOSED.
11. SMTP (PHASE B). Remove/disable `fp02-pre-cutover-mail-suppression.php` only in this phase. No PHP `mail()` fallback.
12. Form delivery QA.
13. Indexing open (PHASE C): `blog_public`, robots.txt, meta robots.
14. Sitemap submissions (Yandex Webmaster + Google Search Console) — `https://shpigovsky.ru/wp-sitemap.xml`.
15. Final crawl.

Exact objects: `REPORTS/evidence/prod-p17-fu02-final-tail/CUTOVER-DB-MUTATION-PLAN.json` and `CUTOVER-FILE-MUTATION-PLAN.md`.

*P17-FU02 preparation only. P18 not started.*
