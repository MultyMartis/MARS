# FP-0002 V9-06E25A — Correction Result

**Wave:** V9-06E25A  
**Generated:** 2026-07-09

## Changes

| Component | Before | After | Result |
|---|---|---|---|
| `page_row_actions` | not hooked | hooked | PASS |
| `post_row_actions` | hooked | kept | PASS |
| Edit meta box | absent | `Дублирование` side box | PASS |
| Capability | literal `create_posts` | CPT-mapped `cap->create_posts` | PASS |
| `duplicate_service()` | E25 logic | unchanged | PASS |
| Plugin version | `0.3.2-v9-06e25-source` | `0.3.3-v9-06e25a-source` | PASS |

## Files modified

- `plugins/shpigovsky-core/src/Admin/ServiceDuplicate.php`
- `plugins/shpigovsky-core/shpigovsky-core.php`

## Evidence

`validation/v9-06e25a-service-duplicate-action-visibility-repair/correction-result.json`

**Result:** PASS
