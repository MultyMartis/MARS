# FP-0002 V9-06E26B DB Checkpoint v1

**Wave:** V9-06E26B  
**Result:** PASS

## Checkpoint

| Item | Value |
|---|---|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e26b-blog-archive-wordpress-acf-port-pre-20260709-131602` |
| Dump | `mars_wp_fp0002.sql` |
| SHA256 | `EA7674E97C6B51A2D88B40BC177342565DF0CC07AB2300403024CD2EF3685625` |
| DB | `mars_wp_fp0002` / prefix `fp02_` |

## Pre-change WP options

| Option | Value |
|---|---|
| page_for_posts | 19 |
| page_on_front | 4 |
| show_on_front | page |
| permalink_structure | `/%postname%/` |
| blog_public | 0 |

## Snapshots

- `wp-options-snapshot.json`
- `blog-page-19-snapshot.json`
- `posts-snapshot.json` (0 posts)
- `categories-snapshot.json`
- `preservation-snapshot.json` (/o-centre/, reviews, service duplicate markers)

## Restore

```text
mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e26b-blog-archive-wordpress-acf-port-pre-20260709-131602\mars_wp_fp0002.sql"
```

Metadata only committed: `validation/v9-06e26b-blog-archive-wordpress-acf-port/db-checkpoint.json`
