# WP Forge Activity Log Module Spec v1

**Class:** B  
**Maturity:** PRODUCTION PROVEN WITH CAVEATS  
**Date:** 2026-08-18  
**Reference:** FP-0002 P12 / P13 V2 / P14

---

## Behavior

- Dedicated table (not `post_content`).
- Columns: user (or System), action, object type/id/title, timestamp.
- Suppress autosave/revision noise.
- Classify WP-CLI/cron/migrations as **System**.
- Admin: filters, pagination, retention job.
- **Do not** log full post content, tokens, passwords, PII payloads.

## Security

Cap `manage_options` or custom. No public REST dump.

## Extraction

`Admin/ActivityLog.php` — **B** after table prefix + text domain parameterization.

---

*Spec v1.*
