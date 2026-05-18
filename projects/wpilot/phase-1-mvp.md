# WPilot Phase 1 MVP

**Status:** documented MVP baseline.
**Scope:** Beget-hosted test WordPress site only.

## Goal

Prepare a safe, human-supervised MVP for testing whether Cursor/operator can work with a Beget-hosted test WordPress site without storing credentials, touching production, or making broad changes.

## Required Conditions

- Operator confirms the site is a test site.
- Operator provides access through out-of-band secure channels, never through repository files.
- Backup existence is confirmed before any write-like test.
- Rollback plan is written before any change.
- Human approves every action that changes files, pages, settings, or content.

## MVP Workflow

1. Read-only site inspection
   - Identify WordPress version visibility, theme name, child theme presence, WPBakery/The7 signals, page builder structure, and obvious safety risks.
   - Do not infer admin access, deployment path, or database permission from public page inspection alone.

2. Access safety
   - Confirm access method, minimum required permission, and no-secret handling.
   - Do not save credentials, cookies, tokens, or panel screenshots with secrets.

3. Backup confirmation
   - Confirm a recent file backup and database backup exist outside this repo.
   - Record only sanitized backup facts: time, owner confirmation, storage class, and restore method.

4. Rollback planning
   - Prepare rollback steps for the exact test action.
   - Define stop conditions and escalation owner.

5. Safe file-level test
   - Prefer a harmless scoped test in a child theme or approved test file.
   - Do not edit core WordPress files, parent theme files, plugin files, or `wp-config.php`.

6. Safe WP admin page copy/create test
   - Copy or create a clearly labeled test page only after human approval.
   - Do not edit production pages in MVP unless the operator explicitly reclassifies the run outside this MVP.

7. WPBakery/The7 structure inspection
   - Inspect structure and theme-builder assumptions without bulk editing.
   - Record SAFE UNKNOWN when shortcode, template, or theme option ownership is unclear.

8. Child theme CSS patch test
   - Apply only a small reversible CSS patch in the child theme or approved custom CSS location.
   - Capture before/after evidence and rollback path.

9. Database read-only awareness
   - Treat the database as read-only in MVP.
   - No destructive SQL, no schema changes, no direct content updates by SQL.

10. QA and report
   - Run the Phase 1 QA checklist.
   - Produce a sanitized test report with actions, evidence, rollback readiness, SAFE UNKNOWN, and security risks.

## Explicit Exclusions

- Live production changes.
- Plugin/theme/core updates.
- Autonomous editing.
- Deploy automation.
- Credential storage.
- Secret scanning of external systems unless separately authorized.
- Destructive SQL or database writes.

## Exit Criteria

- Site passport completed with sanitized facts.
- Backup and rollback readiness recorded.
- One safe test action completed or explicitly deferred.
- QA checklist completed.
- Test report written with SAFE UNKNOWN and SECURITY RISK sections.
