# FP-0002 — Future Task: Site Settings Admin Information Architecture Audit and Russian UX Rebuild

**Status:** REGISTERED — not started  
**Registered in:** V9-06E59-FIX01  
**Task name:** `FP-0002 — Site Settings Admin Information Architecture Audit and Russian UX Rebuild`

## Trigger

Operator screenshot of the current «Настройки сайта» admin submenu demonstrates confusing information architecture for a non-technical administrator. That screenshot demonstrates the **need** for this future audit; it is **not** sufficient evidence for field deletion in the present wave.

## Do not do in FIX01

This future task must **not** be implemented as part of V9-06E59-FIX01. FIX01 only registers the backlog item.

## Scope (when chartered)

1. Inventory every «Настройки сайта» submenu item.
2. Inventory every ACF field group and field attached to Site Settings / reusable blocks / options screens.
3. Map each field to frontend route/component ownership.
4. Identify unused, orphaned, or duplicated fields.
5. Identify groups not attached to active UI.
6. Validate actual data ownership and `post_id` / options context.
7. Produce a removal plan for confirmed obsolete fields (operator confirmation required before any deletion).
8. Full Russian labels and instructions suitable for administrator Оля.
9. Logical regrouping for non-technical administrators.
10. Simpler submenu names.
11. Clearer section hierarchy.
12. Consistent admin styling (build on E53/E55 patterns; do not invent a new product surface).
13. Possible consolidation or splitting of options pages.
14. Screenshots and an operator decision pack **before** implementation.
15. No deletion before explicit operator confirmation.

## Out of scope reminders

- Not a redesign of Contacts page locations (`contacts_locations`) already cleaned in FIX01.
- Not automatic DB postmeta purge.
- Not production SMTP / hosting changes.
- Not a claim that Site Settings is broken — only that IA needs a dedicated audit wave.

## Suggested next charter token

`CREATE_FP0002_SITE_SETTINGS_ADMIN_IA_AUDIT_AND_RU_UX_REBUILD_TASK`
