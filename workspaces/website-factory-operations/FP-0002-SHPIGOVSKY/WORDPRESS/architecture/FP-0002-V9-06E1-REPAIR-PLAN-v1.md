# FP-0002 V9-06E1 Repair Plan v1

**Phase:** V9-06E1  
**Date:** 2026-07-06  
**Pre-write checkpoint:** `v9-06e1-legal-static-copy-seed-pre-20260706-035240`

## Planned actions

| Component | Planned action | Safety |
|---|---|---|
| Page #3 | Replace garbled `post_content` with static privacy body; publish | ALLOWED |
| Page #22 | Seed static user agreement body | ALLOWED |
| Page #23 | Seed static consent body | ALLOWED |
| Page #24 | Seed static cookie policy body | ALLOWED |
| `wp_page_for_privacy_policy` | Update 25 → 3 | ALLOWED |
| Page #25 | Preserve untouched | ALLOWED |
| Legal template | Minimal `document-page.php` + `legal.php` renderer for `the_content()` | ALLOWED (render blocker) |
| Admin editor | Remove #22–24 from native editor hide list | ALLOWED |

## Out of scope

- ACF writes, menu changes, rewrite flush, page deletes, unrelated pages (#6–10, #17, #19, #21).

Evidence: `validation/v9-06e1-legal-static-copy-seed/repair-plan.json`
