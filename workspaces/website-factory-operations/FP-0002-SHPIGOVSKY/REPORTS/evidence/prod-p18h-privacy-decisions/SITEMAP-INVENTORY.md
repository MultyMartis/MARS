# Sitemap Inventory — Read Only (P18H)

**Do not submit in P18H**

## Owner

WordPress core native sitemap (`wp-sitemap.xml`), extended per P10 SEO standard.

## Verified targets

| URL | HTTP | Notes |
|-----|------|-------|
| `https://shpigovsky.ru/wp-sitemap.xml` | 200 | Referenced in `robots.txt` |
| `https://shpigovsky.ru/sitemap.xml` | 200 | Alias/redirect observed |
| `https://shpigovsky.ru/sitemap_index.xml` | 404 | Not used |

## Submission targets (P18I)

1. **Google Search Console** — property `https://shpigovsky.ru/` — sitemap URL `https://shpigovsky.ru/wp-sitemap.xml`
2. **Yandex Webmaster** — host `shpigovsky.ru` — sitemap URL `https://shpigovsky.ru/wp-sitemap.xml`

## Validation

- Canonical domain in sitemap URLs: **shpigovsky.ru** (verify child sitemaps in P18I)
- No staging host URLs expected
- Legal pages disallowed in robots but may still appear in WP sitemap — acceptable; crawl charter should note

**SITEMAP SUBMISSION TARGETS VERIFIED BEFORE SUBMISSION**
