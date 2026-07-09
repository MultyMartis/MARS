# FP-0002 V9-06E26C DB Checkpoint v1

**Wave:** V9-06E26C Blog Single Template WordPress ACF Port  
**Result:** PASS

## Checkpoint

| Item | Value |
|---|---|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e26c-blog-single-template-wordpress-acf-port-pre-20260709-134131` |
| DB dump | `mars_wp_fp0002.sql` |
| SHA256 | `94CE0EA5E23EF17827F06133E36854E59109E67B360CD5D4011CBCE7D475CFB7` |
| Size | 2,023,144 bytes |

## WP options snapshot

- `page_for_posts`: 19
- `permalink_structure`: `/blog/%postname%/`
- `blog_public`: 0

## Restore

```text
mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e26c-blog-single-template-wordpress-acf-port-pre-20260709-134131\mars_wp_fp0002.sql"
```

Evidence: `validation/v9-06e26c-blog-single-template-wordpress-acf-port/db-checkpoint.json`
