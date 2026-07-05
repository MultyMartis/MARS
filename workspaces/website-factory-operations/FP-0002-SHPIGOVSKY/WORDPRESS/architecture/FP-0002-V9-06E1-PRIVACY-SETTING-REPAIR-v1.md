# FP-0002 V9-06E1 Privacy Setting Repair v1

**Phase:** V9-06E1  
**Date:** 2026-07-06

| Check | Before | After | Result |
|---|---|---|---|
| `wp_page_for_privacy_policy` | 25 | 3 | PASS |
| Selected page title | Политика конфиденциальности (системная) | Политика конфиденциальности | PASS |
| Selected route | /privacy-policy-page/ | /privacy-policy/ | PASS |
| Page #25 preserved | publish placeholder | unchanged | PASS |

Evidence: `validation/v9-06e1-legal-static-copy-seed/privacy-setting-repair-result.json`
