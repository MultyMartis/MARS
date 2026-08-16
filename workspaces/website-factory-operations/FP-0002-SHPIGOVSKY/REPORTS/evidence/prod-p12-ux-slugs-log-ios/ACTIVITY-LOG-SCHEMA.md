# Activity log schema — PROD-P12

## Architecture

- FP-0002-owned module: `Shpigovsky\Core\Admin\ActivityLog`
- Storage: table `{wpdb_prefix}user_activity_log` → production `fp02_user_activity_log`
- Install: `dbDelta` on Admin `admin_init` when option `fp02_activity_log_db_version` != `1`
- Admin UI: top-level **Журнал действий** (`manage_options` / Administrator)
- Retention: newest **8000** rows; prune on write when over limit
- Starts from deployment onward (no retroactive Olya history import)

## Columns

| Column | Purpose |
|--------|---------|
| id | PK |
| user_id | actor |
| action | created/updated/trashed/restored |
| object_id | post ID |
| object_type | page/post/service/specialist |
| object_title | title snapshot |
| object_status | status snapshot |
| created_at | site-local MySQL datetime |

## Noise control

- Skip autosave / revisions / auto-draft
- In-request de-dupe key `action:object_id:user_id`
- Trash/restore via `transition_post_status` only
- Create/update via `save_post`
- No content bodies / passwords / PII forms

BASIC WORDPRESS USER ACTIVITY LOG LIVE
