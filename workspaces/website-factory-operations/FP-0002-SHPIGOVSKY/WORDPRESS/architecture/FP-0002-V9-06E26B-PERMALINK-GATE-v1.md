# FP-0002 V9-06E26B Permalink Gate v1

## Decision

**APPLY** — permalink changed to `/blog/%postname%/`

## Reasoning

| Check | Result |
|---|---|
| Published posts | 0 |
| Old article URLs at risk | None |
| `/blog/` archive route | Unchanged (page_for_posts=19) |
| Service CPT routes | HTTP 200 post-change |
| Page routes | HTTP 200 post-change |
| Redirects created | No |

## Actions

1. `permalink_structure` → `/blog/%postname%/`
2. `flush_rewrite_rules(true)` via WP bootstrap
3. Recorded in `permalink-gate-result.json`

## E26C note

Single post URLs will resolve at `/blog/{slug}/` once posts exist (E26D seed or editorial).

Evidence: `validation/v9-06e26b-blog-archive-wordpress-acf-port/permalink-gate-result.json`
