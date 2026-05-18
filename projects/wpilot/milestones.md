# WPilot Milestones

**Status:** sanitized operational milestone log.
**Chat type:** External Systems.

This file records confirmed WPilot milestones only when supported by real operator-supervised DEV/testing evidence. It does not store credentials, database dumps, production data, or claims of autonomous WordPress administration.

## WPilot Operational Prototype v0 Confirmed

**Milestone classification:** partially operational DEV/testing workflow milestone.
**Target:** `https://dev.gktriumph.ru`
**Environment:** DEV only.

WPilot is **PARTIALLY OPERATIONAL** as a human-supervised WordPress maintenance workflow system for DEV/testing scenarios.

### Confirmed Capabilities

1. Remote FTP operation
   - Connected to DEV WordPress hosting.
   - Detected a chrooted FTP root.
   - Listed the WordPress root.
   - Modified `/robots.txt`.
   - Verified the URL result.

2. Backup and rollback
   - Backed up `robots.txt` outside the repository.
   - Restored `robots.txt` from backup.
   - Verified byte-level equality after restore.

3. DEV indexing isolation workflow
   - Detected incomplete initial indexing isolation.
   - Changed `robots.txt` to a full block.
   - Verified WordPress search visibility state manually/operator-assisted.
   - Verified frontend meta robots before/after state.

4. WordPress/WPBakery structure inspection
   - Detected WPBakery shortcodes in page content.
   - Identified `vc_row`, `vc_column`, `vc_raw_html`, and `vc_column_text`.
   - Built a simplified structural map of the test page layout.

5. Scoped WPBakery DB-assisted edit
   - Found the target text occurrence exactly once.
   - Created a backup outside the repository.
   - Attempted full shortcode replacement and correctly observed `0 rows affected`.
   - Switched to a safer anchor-based replacement.
   - Confirmed `UPDATE` affected exactly `1` row.
   - Verified `new_text_present = 1` and `old_text_present = 0`.
   - Operator confirmed the frontend looked correct.

### Important Boundaries

- WPilot did not operate browser/admin UI directly.
- Browser UI control remains **NOT VERIFIED**.
- Database writes were operator-assisted through phpMyAdmin.
- FTP writes were script-assisted and human-supervised.
- No production changes were performed.
- No autonomous runtime was created or proven.
- No plugin, theme, or WordPress core updates were performed.

### Security Note

Credentials were exposed in chat during testing. Rotate FTP, WordPress, hosting, and database credentials after the test cycle.

### Current Classification

WPilot is a **partially operational, human-supervised WordPress maintenance workflow system** for DEV/testing scenarios.

This milestone does not prove:

- autonomous WordPress administration;
- browser/admin UI control;
- production readiness;
- a MARS runtime component;
- credential storage;
- plugin/theme/core update capability.

