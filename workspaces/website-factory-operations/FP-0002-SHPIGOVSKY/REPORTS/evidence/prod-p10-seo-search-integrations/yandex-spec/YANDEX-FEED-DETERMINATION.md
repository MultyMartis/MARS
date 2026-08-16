# Yandex Webmaster — official feed / sitemap determination (PROD-P10)

**Checked:** 2026-08-14  
**Official sources only**

## Sources

1. https://yandex.ru/support/webmaster/controlling-robot/sitemap.html — «Использование файла Sitemap»
2. https://yandex.ru/support/webmaster/indexing-options/sitemap.html — Sitemap files in Webmaster
3. https://yandex.ru/support/webmaster/feed/about.html — YML feeds overview (verticals)
4. https://yandex.ru/support/webmaster/search-appearance/services.html — services appearance via YML

## Finding

### For ordinary pages / sections / services (clinic IA)

Yandex expects a **standards-compliant XML Sitemap** (sitemaps.org), optionally TXT.  
Submission: robots.txt `Sitemap:` directive and/or Webmaster «Файлы Sitemap».

Official note: Yandex Search **does not** support sending RSS/Atom feeds via the Sitemap file.

### Separate “general page/service feed”

**NOT APPLICABLE** under current official specification for arbitrary pages/sections/services as a sitemap replacement.

### YML feeds

YML feeds exist for **specific verticals** of enriched search appearance (realty, vacancies, cars, education, doctors, household services, etc.). They describe **offers/sets** for appearance enhancement and are **not** a general-purpose content map for ordinary clinic pages/sections/services.

Implementing a fabricated proprietary “pages/services feed” would violate the charter (do not invent formats).

## Decision recorded for Admin + implementation

```
YANDEX GENERAL PAGE/SERVICE FEED = NOT APPLICABLE UNDER CURRENT OFFICIAL SPEC
```

P10 provides:

- Google/Yandex-compatible XML sitemap generation (WordPress-native)
- Admin explanation + clickable sitemap URL for Webmaster submission
- No fake alternate feed endpoint
