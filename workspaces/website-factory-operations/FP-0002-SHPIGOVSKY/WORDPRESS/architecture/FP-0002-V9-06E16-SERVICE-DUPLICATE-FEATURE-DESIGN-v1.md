# FP-0002 V9-06E16 — Service Duplicate Feature Design

**Evidence:** `validation/v9-06e16-operator-qa-closure-reusable-blocks-clone-cleanup-audit/service-duplicate-feature-design.json`

## Scope

Service CPT only (`service`, hierarchical, `/uslugi/` rewrite).

## UI

Row action **Дублировать** on service list → creates draft → redirect to edit screen.

## Copy policy

| Copy | Reset |
|------|-------|
| post_parent, menu_order | slug (unique) |
| service_layout_variant, hero_*, structured sections, FAQ, relationships | status → draft |
| service_short_description | timestamps, guid |
| Featured/hero media attachment IDs (reuse, no file duplication) | — |

## Implementation (future)

New module `Admin/ServiceDuplicate.php` in shpigovsky-core: nonce-protected `admin_action`, `wp_insert_post`, allowlisted `copy_post_meta`.

## Risks

- **HIGH:** accidental publish of duplicate — mitigated by draft-only creation.
- **HIGH:** slug collision — mitigated by `-copy` suffix loop.

**No implementation in E16.**
