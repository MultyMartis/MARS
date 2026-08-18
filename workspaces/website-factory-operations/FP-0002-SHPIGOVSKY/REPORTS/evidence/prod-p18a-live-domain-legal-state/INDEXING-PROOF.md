# INDEXING PROOF — P18A

**Required:** LIVE DOMAIN ACTIVE (WP options), INDEXING STILL INTENTIONALLY CLOSED

| Check | Value |
|-------|--------|
| `blog_public` | `0` |
| robots.txt (WP / beget host) | `User-agent: *` / `Disallow: /` / Sitemap still `http://shpigovsky.beget.tech/wp-sitemap.xml` |
| REST | 200 on beget; `X-Robots-Tag: noindex` on `/wp-json/` |
| Public apex robots | **legacy** file (`Disallow: /*?` + `sitemap.xml`) — not WP; not opened by this wave |

SMTP still suppressed (`pre_wp_mail` filter present). Mail MU not removed.

Sources: `ROBOTS-BEGET.txt`, `DB-LEGAL-INTAKE.txt`, `DEPLOY-QA.json`.
