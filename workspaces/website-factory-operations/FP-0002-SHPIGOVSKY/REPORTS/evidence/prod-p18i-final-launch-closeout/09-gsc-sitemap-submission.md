# Google Search Console — sitemap submission (P18I)

**Captured:** 2026-08-20 UTC (P18I closeout wave)

## Property

- **Canonical site:** `https://shpigovsky.ru/`
- **Sitemap URL:** `https://shpigovsky.ru/wp-sitemap.xml`

## Result

**AUTH BLOCKER — SERVICE SUBMISSION BLOCKED BY AUTH**

MARS agent runtime in this session has no authenticated Google Search Console browser profile or API credentials. Automated Playwright runs use ephemeral contexts without operator Google login.

## Operator follow-up (non-blocking for technical launch closeout)

1. Open [Google Search Console](https://search.google.com/search-console) with the verified property for `https://shpigovsky.ru/`.
2. Navigate to **Sitemaps**.
3. Submit or re-submit: `https://shpigovsky.ru/wp-sitemap.xml`
4. Confirm status shows **Success** or **Couldn't fetch** resolved after recrawl.

## Technical readiness (verified without GSC UI)

- Sitemap returns HTTP **200**
- Referenced in `robots.txt`
- Indexing **OPEN — HUMAN-APPROVED**
- Final crawl found **no staging hostnames** in public HTML after P18I URL normalization fix
