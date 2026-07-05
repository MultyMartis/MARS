# FP-0002 V9-06D9L Classic Editor Install Activation v1

**Date:** 2026-07-05  
**Task:** V9-06D9-L

## Actions

| Step | Result |
|---|---|
| Install official Classic Editor 1.7.0 from wordpress.org | PASS |
| Activate plugin | PASS |
| Set `classic-editor-replace` = `classic` | PASS |
| Set `classic-editor-allow-users` = `disallow` | PASS |
| Verify block editor off for Home #4 | PASS |
| Verify block editor off for pages | PASS |

## Notes

- Initial option write used incorrect value `classic-editor-replace=block`; corrected to `classic` before validation.
- Plugin installed to runtime only: `wp-content/plugins/classic-editor/` — not staged in Git.

Evidence: `validation/v9-06d9l-admin-editor-acf-visibility-repair/classic-editor-install-activation-result.json`
