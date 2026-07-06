# FP-0002 V9-06E7B — Project Plugin Scope Classification v1

**File:** `plugins/shpigovsky-core/src/Fields/FieldGroups.php`  
**Verdict:** ACCEPTED_PROJECT_PLUGIN_SOURCE_CHANGE

## Determination

| Check | Result |
|-------|--------|
| Project-owned plugin | YES — `shpigovsky-core` is FP-0002 project plugin |
| Third-party code touched | NO |
| Scope limited to hero admin | YES |
| Duplicate field groups | NO — fields added to existing groups |

## Hero fields added/updated

- **Home (`group_fp02_page_home`):** `hero_media` image field
- **Services Hub (`group_fp02_page_services_hub`):** `hero_eyebrow`, `hero_title_override`, `hero_media`, intro relabel
- **Institutional (`group_fp02_page_institutional`):** full hero text + `hero_media` + CTA label
- **Service (`group_fp02_service_layout_hero`):** `hero_media` instructions clarified
- **MODIFIED** timestamp bumped to `1783166400`

ACF JSON delta not required — local registration via project plugin source is canonical for FP-0002.

Authority: `validation/v9-06e7b-hero-system-finalization-scope-reconciliation/project-plugin-scope-classification.json`
