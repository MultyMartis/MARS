# FP-0002 V9-06E27A Cleanup Dependency Audit v1

**Evidence:** `validation/v9-06e27a-obsolete-pages-cleanup-read-only-audit/cleanup-dependency-audit.json`

## Summary

| Candidate | Dependencies | Risk | Cleanup safety | Notes |
|---|---|---|---|---|
| #9 genotipirovanie | parent hub #5; not in menu | LOW | SAFE_AFTER_APPROVAL | Route already 404 |
| #10 specyalisty | none; not in menu | LOW | SAFE_AFTER_APPROVAL | Orphan page |
| #17 intervyu-i-smi | parent #11 o-centre | LOW | SAFE_AFTER_APPROVAL | Not in V9 manifest |
| #21 legal hub draft | none | LOW | SAFE_AFTER_APPROVAL | Already draft |
| #25 privacy duplicate | none; not in legal menu | MEDIUM | SAFE_AFTER_APPROVAL | Public duplicate URL |
| #6 zavisimosti page | **in Primary menu**; conflicts service #73 | HIGH | REQUIRES_DEPENDENCY_RESOLUTION | Trash only after menu retarget to service CPT |
| #7 psihicheskoe page | conflicts service #77 | HIGH | REQUIRES_DEPENDENCY_RESOLUTION | Same path ownership debt |
| #8 RPP page | conflicts service #84 | HIGH | REQUIRES_DEPENDENCY_RESOLUTION | Same path ownership debt |

## System dependencies (must not break)

- `wp_page_for_privacy_policy` → **#3** (not #25)
- `page_on_front` → **#4**
- `page_for_posts` → **#19**
- Legal menu objects → **#3, #22, #23, #24**
