# REPORT — FP-0002 Olya Robots Restore + Health Check Closeout

**Date:** 2026-08-24
**Status:** PASS
**Production:** https://shpigovsky.ru/
**Evidence:** `REPORTS/health-checks/2026-08-24/robots-closeout/`

## Canonical Olya Robots

- Runtime source: `WORDPRESS/plugins/shpigovsky-core/assets/robots-seo-policy.txt`
- Review copy: `WORDPRESS/seo/OLYA-ROBOTS-REVIEWED-CANDIDATE.txt`
- SHA-256: `2594093919d01f067bcd3776d50d973cfa20a1faf4a6d63fc23f21367d08529e`
- Both current Git blobs are byte-identical: LF, no BOM, 2826 bytes.
- Authority: current human-approved Olya SEO robots truth. It must not be optimized, normalized, simplified, or replaced without a new explicit Olya/operator SEO decision.

## Drift

- Detected physical/live SHA: `49e52465c97f697290c7d13ab62b1b5fa74a9a5343e5464af8fb11f50f4dfad7`
- Canonical SHA: `2594093919d01f067bcd3776d50d973cfa20a1faf4a6d63fc23f21367d08529e`
- Exact diff: four added `Disallow: /wp-json/` rules (Yandex, GoogleBot, Bingbot, `*`) plus reduced blank group separators.
- No global `Disallow: /` was present.

## Restore

- Backup: `/home/s/shpigovsky/shpigovsky.ru/public_html/robots.txt.fp0002-pre-restore-20260824T071539Z.bak`
- Backup SHA equals detected physical SHA; evidence mirror retained in the closeout pack.
- Physical `/robots.txt` restored from exact current canonical Git bytes.
- Live HTTP, physical file, runtime asset and `IndexingControl::robots_body(true)` now share canonical SHA.

**PHYSICAL PRODUCTION ROBOTS RESTORED FROM OLYA-APPROVED CANONICAL SOURCE**

## Ownership

- OPEN `IndexingControl::robots_body(true)` resolves to the canonical Olya asset.
- CLOSED is a separate temporary global safety overlay; reopen restores canonical policy.
- Watchdog is observation / Activity Log / alert only and has no robots file write.
- Active source contains no generic MARS OPEN template rewrite path.

**OPEN-STATE ROBOTS OWNER PRESERVES OLYA POLICY**

## Robots Validation

- `https://shpigovsky.ru/robots.txt`: HTTP 200, `text/plain`
- Live SHA = physical SHA = canonical SHA: `2594093919d01f067bcd3776d50d973cfa20a1faf4a6d63fc23f21367d08529e`
- Production sitemap directive present; no staging / `beget.tech` host.
- Yandex, GoogleBot, Bingbot, `*`, and Googlebot-Image groups present.
- Global `Disallow: /` absent; 2826 bytes / 151 lines; no truncation.

**OLYA-APPROVED ROBOTS POLICY INTACT**

## Indexing

- `blog_public=1`
- Effective state: `OPEN`
- Human decision: `OPEN` (`admin_ui`, recorded 2026-08-20)
- P18G guard: ACTIVE
- Watchdog: ACTIVE / hourly
- Homepage and representative service: no `noindex`; no `X-Robots-Tag` global block.

**INDEXING OPEN — HUMAN APPROVED**

No synthetic close QA was performed.

## Sitemap

`https://shpigovsky.ru/wp-sitemap.xml` returned HTTP 200, valid XML sitemap index, production host only, and is referenced by robots.

## Public Regression

- Homepage: HTTP 200
- Representative service: HTTP 200
- Contacts: HTTP 200

No form submission or SMTP test was performed.

## Health Check

- Previous: ATTENTION
- Current: PASS

**ATTENTION RESOLVED — PHYSICAL ROBOTS RESTORED TO OLYA-APPROVED POLICY**

Historical evidence remains explicit: detected → corrected → verified.

## Editorial Safety

**OLYA CURRENT EDITORIAL PRODUCTION TRUTH PRESERVED**

No editorial DB mutation was performed.

## Current Project State

**PRODUCTION / MAINTENANCE — STABLE**
