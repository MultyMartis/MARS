# PROD-P09 — Smart Search Endpoint Contract

**Route:** `GET /wp-json/shpigovsky/v1/smart-search?q={query}`  
**Registration:** `shpigovsky_smart_search_register_rest_route()` in `inc/search-helpers.php`  
**Permission:** public (`__return_true`) — published content only  
**WPilot:** not used

## Request

| Arg | Rules |
|-----|--------|
| `q` | string; `sanitize_text_field` + trim; Cyrillic OK |
| Min length | 3 UTF-8 characters (server returns empty groups if shorter) |

## Response (JSON)

```json
{
  "q": "…",
  "min": 3,
  "empty": true|false,
  "groups": {
    "services": [{"id":1,"group":"services","title":"…","url":"…","snippet":"…"}],
    "articles": [],
    "specialists": [],
    "pages": []
  }
}
```

- Permalinks via `get_permalink()` (siteurl-relative; no hardcoded production host in source).
- No full bodies, no ACF dumps, no admin/private fields.
- Max ~5 items per group; candidate pool bounded (`posts_per_page` 40 per type).

## Ranking tiers

1. Title exact (100)  
2. Title starts with (80)  
3. Title contains (60)  
4. Excerpt / public short description / specialist public profile strings (40)  
5. Body contains (20)
