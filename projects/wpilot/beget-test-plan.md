# WPilot Beget Test Plan

**Status:** documented Phase 1 test plan.
**Target:** Beget-hosted test WordPress site.

## Preconditions

- Operator confirms the target is not production.
- Operator confirms authorized access.
- Secrets are provided only through secure out-of-band handling.
- Backup and rollback documents are prepared before any write-like test.

## Test Sequence

1. Identify target context
   - Domain or test URL.
   - Hosting account owner confirmation.
   - WordPress admin role if admin access is used.
   - File access method if file inspection is used.

2. Read-only public inspection
   - Home page and selected test page.
   - Theme and page-builder signals visible from markup.
   - Obvious cache, CDN, maintenance, or access restrictions.

3. Read-only admin/file inspection
   - Confirm child theme presence.
   - Inspect The7/WPBakery structure indicators.
   - Identify approved custom CSS or child theme stylesheet location.
   - Avoid copying secret-bearing files.

4. Backup confirmation
   - Confirm database backup exists.
   - Confirm files backup exists.
   - Confirm restore owner and rollback contact.

5. Safe file-level test
   - Select a reversible, low-impact test file or child theme CSS target.
   - Record exact before state.
   - Make only the approved change.
   - Verify site remains accessible.
   - Roll back immediately if stop condition is reached.

6. Safe WP admin page copy/create test
   - Create or copy a clearly named test page.
   - Do not edit production pages.
   - Do not publish publicly unless the operator explicitly approves visibility.

7. QA and report
   - Run [qa-checklist.md](qa-checklist.md).
   - Fill [reports/test-report-template.md](reports/test-report-template.md).

## Stop Conditions

- Site is production or cannot be confirmed as test.
- Backup cannot be confirmed.
- Rollback owner or method is unclear.
- Required access would expose secrets in repo.
- The change target is core, parent theme, plugin code, or `wp-config.php`.
- The site shows errors, broken layout, failed login, or unexpected caching behavior after a test.

## Evidence To Record

- Sanitized target identity.
- Access type used, without secrets.
- Backup confirmation summary.
- Files or pages touched.
- Before/after observations.
- Rollback status.
- SAFE UNKNOWN and SECURITY RISK.
