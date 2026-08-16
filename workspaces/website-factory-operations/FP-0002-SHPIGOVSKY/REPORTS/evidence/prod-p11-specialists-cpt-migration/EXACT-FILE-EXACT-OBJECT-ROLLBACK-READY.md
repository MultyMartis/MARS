# EXACT-FILE / EXACT-OBJECT ROLLBACK READY — PROD-P11

## File snapshots

`X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p11-layer-b-pre\`

Pre-deploy production bytes for every uploaded path (see `LAYER-B-MANIFEST.json`).

## DB snapshots

`X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p11-db-snapshots\`

- `post-{1031,1032,1033,1097}-wp_posts.sql` + `.sha256`
- `post-{ID}-wp_postmeta.sql` + `.sha256`
- `hub-1030-*.sql`
- `pre-migrate-post-{ID}-wp_posts.sql`
- `pre-clear-wp-page-template-meta.sql`
- `inventory-raw.json`

## Rollback method (exact)

1. Restore changed theme/plugin/acf files from Layer B snapshots via SFTP put of exact bytes.
2. Restore `fp02_posts` rows for IDs 1031/1032/1033/1097 from SQL dumps (`post_type=page`, `post_parent=1030`).
3. Restore `_wp_page_template` rows from `pre-clear-wp-page-template-meta.sql` if needed.
4. Delete option `fp02_specialist_cpt_rewrite_flushed_p11` and flush rewrites once if CPT code is removed.

No full Beget backup required for this wave (operator-authorized exact-file/object mode).
