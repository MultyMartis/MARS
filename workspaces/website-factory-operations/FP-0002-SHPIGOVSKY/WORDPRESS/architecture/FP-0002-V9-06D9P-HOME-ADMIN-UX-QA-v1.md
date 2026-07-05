# FP-0002 V9-06D9P Home Admin UX QA v1

**Date:** 2026-07-05  
**Task:** V9-06D9-P (read-only QA)  
**Page:** Home #4 (Главная)

## Scope

Read-only validation of Home page wp-admin editing experience after D9-L/M/N/O repairs. No DB writes, no live save mutation.

## Summary

| Check | Result | Method |
|---|---|---|
| Native editor hidden | PASS | D9-N allowlist policy (`shpigovsky_should_hide_native_editor(4)`) |
| Title / publish box | PASS (expected) | WP admin standard; not live-verified |
| ACF group `group_fp02_page_home` | PASS | DB meta present; runtime JSON exists |
| `home_reviews_teaser` optional | PASS | DB + canonical JSON `required=0`, `min=0` |
| Save without Reviews teaser | OPERATOR_CONFIRMATION_REQUIRED | Empty-repeater simulation PASS; live auth save not executed |
| Hero image attachment 89 | PASS | `home_hero_slides_0_image` = 89 |
| Gallery attachments 90–93 | PASS | 12 ACF sub-meta rows; frontend renders 4 `/uploads/` images |
| Recovery intro populated | PASS | `home_recovery_intro_heading` non-empty |
| FAQ heading + items | PASS | Heading + 10 sub-meta rows |
| Section headings (specialists/comfort/articles) | PASS | All present |
| Empty deferred fields block save | PASS | No required/min blockers in home group |
| ACF validation blocker | PASS | Simulation: `would_block_save=false` |

## ACF field inventory (read-only)

- **Populated:** recovery intro heading, hero slides (attachment 89), gallery media, FAQ, specialists/comfort/articles headings, reviews teaser meta (optional, may be empty rows).
- **Deferred / fallback:** intro band headings use theme fallbacks; do not block save.

## Evidence

`validation/v9-06d9p-admin-ux-qa/home-admin-ux-qa.json`

## Result

**PARTIAL** — all schema/policy checks PASS; live authenticated Update click requires operator confirmation.
