# PROD-P09 — Classification Matrix

| Group (RU) | Key | Objects | Inclusion | Exclusion / mutual exclusivity |
|------------|-----|---------|-----------|--------------------------------|
| Услуги | `services` | CPT `service` | published, no password | not in other groups |
| Статьи | `articles` | `post` | published, no password | not in other groups |
| Специалисты | `specialists` | `page` children under `/specyalisty/` hub | published; parent/ancestor = hub | hub itself is **Страницы**; not duplicated under Страницы |
| Страницы | `pages` | other published `page` | useful destinations | specialists; legal/system slugs via `shpigovsky_search_excluded_page_ids()` |

## Global exclusions

- drafts, trash, revisions  
- attachments as standalone hits  
- password-protected  
- legal/system: `user-agreement`, `consent-personal-data`, `cookie-files-policy`, `privacy-policy`

## Duplicate prevention

Each object assigned exactly one group key via `shpigovsky_smart_search_group_key()` before scoring; IDs de-duplicated within group.
