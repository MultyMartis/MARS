# FP-0002 V9-06E29A Named Placeholder Pages Inventory v1

**Evidence:** `validation/v9-06e29a-placeholder-pages-and-ocentre-admin-parity-decision-audit/named-placeholder-pages-inventory.json`

## Summary

Five institutional child pages exist under hub `#11` (`/o-centre/`). All match static V9 manifest routes marked `PLACEHOLDER` / `PLACEHOLDER_PENDING_CONTENT`. Static V9 has stub `plain-page-content` layouts; WordPress child template currently renders **hero + breadcrumbs only** (no body copy wired).

| Page title | ID | URL | Status | V9 layout | Classification |
|---|---:|---|---|---|---|
| О нас | 12 | `/o-centre/o-nas/` | publish | PLACEHOLDER stub | KEEP_PLACEHOLDER_FOR_LATER_PORT |
| Программа лечения | 13 | `/o-centre/programma-lecheniya/` | publish | PLACEHOLDER stub | KEEP_PLACEHOLDER_FOR_LATER_PORT |
| Галерея о доме | 14 | `/o-centre/galereya-o-dome/` | publish | PLACEHOLDER stub | KEEP_PLACEHOLDER_FOR_LATER_PORT |
| Специалистам | 15 | `/o-centre/specialistam/` | publish | PLACEHOLDER stub | KEEP_PLACEHOLDER_FOR_LATER_PORT |
| Родственникам | 16 | `/o-centre/rodstvennikam/` | publish | PLACEHOLDER stub | KEEP_PLACEHOLDER_FOR_LATER_PORT |

## Key findings

- **Template:** all use `page-templates/institutional.php`, parent `#11`.
- **HTTP:** all routes return **200**.
- **WP menu DB:** none assigned to nav menu items; **footer fallback** in `inc/navigation.php` links all five.
- **Inbound links:** `Программа лечения` linked from multiple theme partials (home, services, `/o-centre/` approach/program sections).
- **ACF on child pages:** 0 fields populated; child branch of institutional template does not render `institutional_content_sections`.
- **Design authority:** partial — V9 stub only, not approved full layout.

## Recommended action (decision only)

**Keep published** as structural placeholders until operator approves E29C (draft vs port vs trash). Do **not** trash — routes are in V9 manifest and footer IA.
