# FP-0002 — Project Status

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Last updated:** 2026-07-02 (V9-05A approved frontend intake + foundation adoption)

## Active frontend workspace (V9)

| Field | Value |
|-------|-------|
| Workspace | `workspaces/fp-0002-shpigovsky-v9/` |
| Static baseline | `FP0002_V9_OPERATOR_APPROVED_STATIC_FRONTEND_STABLE_BASELINE_COMPLETE` |
| Intake pack | `FP0002_V9_FORGE_WORDPRESS_INTAKE_PACK_COMPLETE` |
| Intake gate (V9-05A) | `FP0002_V9_APPROVED_FRONTEND_INTAKE_APPROVED` |
| WordPress foundation | **ADOPTED** — prepared MLI site, not legacy discard |
| Phase | V9-05A complete → **V9-05B pre-implementation checkpoint** |
| Dist output | Clean-route static site in `dist/` (root-relative `/assets/...`) |
| Route manifest | `workspaces/fp-0002-shpigovsky-v9/tools/v9-route-manifest.json` (31 routes) |
| Forge intake pack | `workspaces/fp-0002-shpigovsky-v9/forge-intake/` |
| Intake tag | `fp-0002-v9-forge-wordpress-intake-pack-01` |
| Stable tag | `fp-0002-v9-operator-approved-static-frontend-stable-01` @ `a51376872fbfefb7d5f68a58b440c726d6cf3de3` |
| WordPress implementation | **Not started** |

## Phase 07C-B static package — SUPERSEDED

| Field | Value |
|-------|-------|
| Package | `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\FP-0002-V8-STATIC-CLIENT-DEMO-1-OPERATOR-REVIEW\` |
| Status | `SUPERSEDED_FAILED_STATIC_PACKAGING_NOT_FOR_FORGE_NOT_FOR_CLIENT` |
| Defect | Nested routes resolved `assets/...` relative to page depth — CSS/JS/fonts failed on nested URLs |
| Replacement | V9 workspace native `dist/` clean routes |
| Note | Package retained as historical evidence only — not Forge authority, not for client |

## Historical stable baseline (V8)

| Field | Value |
|-------|-------|
| Baseline | [FP-0002-V8-OPERATOR-APPROVED-FRONTEND-BASELINE-01.md](FP-0002-V8-OPERATOR-APPROVED-FRONTEND-BASELINE-01.md) |
| Tag | `fp-0002-v8-operator-approved-frontend-stable-01` |
| Parent | `eeab3d68` · `fp-0002-v8-blog-full-stable-01` |
| Recovery pack | `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\FP-0002-V8-OPERATOR-APPROVED-FRONTEND-STABLE-01\` |
| Next | Phase 07C-B static demo assembly (blocked on operator gate) · deferred operator polish · Forge WP |
| Phase 07B | [REPORT-FP-0002-V8-PHASE-07B-DOCUMENTATION-AND-LESSONS-LEARNED-v1.md](REPORT-FP-0002-V8-PHASE-07B-DOCUMENTATION-AND-LESSONS-LEARNED-v1.md) · [FP-0002-V8-IMPLEMENTATION-GUIDE-v1.md](FP-0002-V8-IMPLEMENTATION-GUIDE-v1.md) |
| Phase 07C-A | [REPORT-FP-0002-V8-PHASE-07C-A-EXCEL-DEMO-RECONCILIATION-v1.md](REPORT-FP-0002-V8-PHASE-07C-A-EXCEL-DEMO-RECONCILIATION-v1.md) · evidence `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\phase-07c-a-excel-demo-reconciliation\` · **operator gate pending** |

## ACTIVE TEMPORARY PRIORITY RULE

Before any FP-0002 frontend implementation, read:

[`FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md`](FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md)

- **Visual PASS:** OPERATOR ONLY
- **Commit before operator visual approval:** PROHIBITED
- **Mandatory report header:** REQUIRED
- **Web-GPT recovery source:** THIS PROTOCOL

## V8 workspace (2026-06-29)

| Field | Value |
|-------|-------|
| Workspace | `workspaces/fp-0002-shpigovsky-v8/` |
| Branch | `mars/canonical-post-recovery` |
| CF-011 dark CTA | COMPLETE — commit `4d98d6fb` |
| CF-012 program modifiers | COMPLETE — commit `9e8fa083` |
| Operator manual polish | OPERATOR_MANUAL_POLISH_CANONICAL |
| Visual authority | V8 working source post manual polish |
| CF-003–CF-012 | APPROVED |
| Next wave | CF-010 clinic landscape — **NOT STARTED** |
| Page-wide DOM gate | PASS |
| O-Centre | **STABLE_PREVIOUSLY_APPROVED** in operator baseline — historical audit [FP-0002-OCENTRE-VISUAL-AUDIT-STATUS-v1.md](FP-0002-OCENTRE-VISUAL-AUDIT-STATUS-v1.md) superseded by baseline |
| Priority visual protocol | **ACTIVE** — [FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md](FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md) |

## Workspace versions (2026-06-24)

| Workspace | Path | Lifecycle | Tag / parent |
|-----------|------|-----------|--------------|
| **V6** | `workspaces/fp-0002-shpigovsky-v6/` | **FROZEN_FALLBACK** | `fp-0002-v6-final-before-v7-operator-stable-01` |
| **V7** | `workspaces/fp-0002-shpigovsky-v7/` | **IMMUTABLE_STABLE_FALLBACK** | `fp-0002-v7-pre-final-polish-operator-stable-01` |
| **V8** | `workspaces/fp-0002-shpigovsky-v8/` | **OPERATOR_APPROVED_BASELINE** | `fp-0002-v8-operator-approved-frontend-stable-01` @ `eb47ebb` |

```text
V7 design authority: workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig
V7 design authority SHA-256: BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041
Historical Figma (Шпиговский.fig): DO NOT USE FOR NEW WORK
Factory Figma rules: projects/mars-website-factory/figma-inspection-authority-rules-v1.md
package_001: COMPLETE_PENDING_OPERATOR_FINAL_REVIEW
package_001_phase_1_figma_rules: COMPLETE
package_001_phase_2_head: TECHNICALLY_COMPLETE
package_001_phase_3a_intro_content: COMPLETE
package_001_phase_3b_founder_quote_svg: COMPLETE
package_001_phase_3b_gallery_captions: COMPLETE
package_001_phase_3c_recovery_life: DESKTOP_COMPLETE
package_001_phase_3c_mobile: MOBILE_RESPONSIVE_DERIVED_COMPLETE
package_001_phase_4a_spacing_cleanup: COMPLETE
package_001_phase_9_global_polish: COMPLETE_PENDING_OPERATOR_FINAL_REVIEW
gallery_captions: POSITION_BELOW_IMAGE — COMPLETE
recovery_life: DESKTOP_COMPLETE / MOBILE_RESPONSIVE_DERIVED_COMPLETE
section_spacing_cleanup: COMPLETE
global_visual_polish: COMPLETE_PENDING_OPERATOR_FINAL_REVIEW

operator_manual_checkpoint:
  date: 2026-06-26
  status: COMPLETE
  committed: true
  pushed: true
  commit: 95b97adf

package_002: COMPLETE_PENDING_OPERATOR_REVIEW
external_link_svg: COMPLETE
hero_architecture: HOME_COMPLETE / INNER_PAGE_BASE_COMPLETE / MOBILE_RESPONSIVE_COMPLETE
slider_pagination: COMPLETE
home_videos: COMPLETE
faq_filler: COMPLETE_TEMPORARY_CONTENT
home_recovery_intro_text: FIGMA_EXACT_COMPLETE

operator_checkpoint_before_package_003:
  date: 2026-06-26
  status: NOT_REQUIRED
  backup_sha256: 3BE9ADAA1B35FD27DC5E4F0CAA3CFB34667A18B818511F4EC5A51247B37C0E75

package_003: TECHNICALLY_ACCEPTED
package_003_commit: c74bb04d
video_posters: REAL_VIDEO_FRAMES_COMPLETE
hero_container_gutters: COMPLETE
founder_quote_current_variant: variant-b
founder_quote_variant_a: PRESERVED_FALLBACK
founder_quote_variant_b: ACTIVE_ON_HOME
treatment_service_icons: COMPLETE

home_operator_manual_polish: ACCEPTED_AS_CURRENT_BASELINE
home_source_authority: OPERATOR_CANONICAL
home_visual_style_audit: COMPLETE
home_visual_baseline: DOCUMENTED
component_reuse_map: COMPLETE
source_universalization: NOT_STARTED
services_general_source_reconciliation: COMPLETE
services_general_design_mapping: COMPLETE
services_general_build_plan: COMPLETE
services_general_implementation_pass_1: COMPLETE_PENDING_OPERATOR_REVIEW
services_general_implementation_pass_2: COMPLETE_PENDING_OPERATOR_REVIEW
services_general_inner_hero: FINAL_ASSET_COMPLETE
services_general_reuse_section_order: COMPLETE
services_general_category_hubs: FOUR_IMPLEMENTED
services_general_unique_assets: FIGMA_EXPORT_COMPLETE
services_general_page: PASS_2_CATEGORY_HUBS_COMPLETE
services_general_clean_build: PASS
services_general_assets: FIGMA_EXPORT_COMPLETE
services_general_home_regression: NONE_DETECTED
services_general_content_safe_unknowns:
  - Genotyping hub lead paragraphs (Figma lorem only)
  - Mental health per-service descriptions (Figma lorem excluded)
  - Eating disorders per-service descriptions (Figma lorem excluded)
services_general_final_polish: COMPLETE_PENDING_OPERATOR_REVIEW
services_general_visual_parity: COMPLETE_WITH_DOCUMENTED_SAFE_UNKNOWNS
services_general_clean_build: PASS_WITH_CLEAN_DIST_ENVIRONMENT_CAVEAT
services_general_home_regression: NONE_DETECTED
services_general_untracked_asset_cleanup: PROBE_CLEANUP_COMPLETE_17_FILES_REMOVED
services_general_stable_freeze: NOT_STARTED
services_general_pass_2: COMPLETE_PENDING_OPERATOR_REVIEW
services_figma_mcp_connection: VERIFIED
services_figma_mcp_live_file_read: BLOCKED_NO_FILEKEY
services_figma_target_frames: VERIFIED_OFFLINE
services_page_anatomy: COMPLETE
services_breadcrumbs: IDENTIFIED
services_page_subnav: IDENTIFIED
services_v1_differential: COMPLETE
services_v2_decision: HYBRID_RECONSTRUCTION
services_v1: PRESERVED_FALLBACK
services_v2_strategy: HYBRID_RECONSTRUCTION
services_v2_block_1: ACCEPTED_WORKING_BASE
services_v2_block_2a: CORRECTED_AND_INTEGRATED
services_v2_block_2b: COMPLETE_PENDING_OPERATOR_REVIEW
services_v2_category_structure: COMPLETE
services_v2_category_content_fidelity: SUPERSEDED_BY_MOCKUP_COPY_PASS
services_v2_category_text_recovery: SUPERSEDED_BY_MOCKUP_COPY_PASS
services_v2_category_mockup_copy_population: COMPLETE
services_v2_runtime_content_population: COMPLETE
services_v2_empty_content_slots: ZERO
services_v2_visible_mockup_text_omissions: ZERO
services_v2_temporary_mockup_copy: PRESENT_AND_DOCUMENTED
services_v2_production_copy_replacement: FUTURE_SEPARATE_PASS
services_v2_true_visible_placeholders: 0
services_v2_premature_compaction: REMOVED_OR_CORRECTED
services_v2_category_geometry: CONTENT_DRIVEN
services_v2_mockup_copy_review: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-exact-mockup-copy/
services_v2_text_recovery_review: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-category-text-recovery/
services_v2_category_family: COMPLETE_PENDING_OPERATOR_POLISH
services_v2_mockup_copy_policy: ALL_VISIBLE_TEXT_INCLUDED
services_v2_hero_layout: CORRECTED_PENDING_OPERATOR_REVIEW
services_v2_gallery_media_height: NORMALIZED
services_v2_program_dom: BODY_BEFORE_MEDIA
services_v2_program_card_pattern: HOME_DIRECTION_STYLE_REUSED
services_v2_program: COMPLETE_PENDING_OPERATOR_REVIEW
services_v2_program_mockup_text: COMPLETE
services_v2_program_empty_content_slots: ZERO
services_v2_program_component: SERVICES_SPECIFIC_REUSABLE_PARTIAL
services_v2_root_tokens_added: ZERO
services_v2_program_item_descriptions: REMOVED_BY_OPERATOR_DECISION
services_v2_founder: HOME_FOUNDER_QUOTE_REUSED
services_v2_comfort: HOME_COMFORT_REUSED
services_v2_mid_page_cta: SECOND_PROGRAM_CTA_BAND_REUSED
services_v2_faq: HOME_FAQ_REUSED
services_v2_final_form: HOME_FINAL_FORM_REUSED
services_v2_lower_page_assembly: COMPLETE_PENDING_OPERATOR_REVIEW
services_v2_visible_mockup_text_policy: ACTIVE
services_v2_root_tokens_added: ZERO
services_v2_v1: PRESERVED_FALLBACK
services_v2_navigation_switch: NOT_STARTED
services_v2_founder_comfort_cta_superseded: SUPERSEDED_NOT_IN_RUNTIME
services_v2_final_assembly_review: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-final-lower-assembly/
services_v2_operator_acceptance: CONDITIONAL_ACCEPTED_REFERENCE
services_v2_reference_type: SERVICES_HUB_INTERNAL_PAGE
services_v2_lifebuoy_decor: REMOVED_BY_OPERATOR_DECISION
services_v2_detail_links: HOME_REHABILITATION_PATTERN_REUSED
services_v2_reference_baseline: READY_FOR_FREEZE
services_v2_canonical_switch: NOT_STARTED
services_v2_reference_freeze_review: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-reference-freeze/
service_subdivision_planning: workspaces/fp-0002-shpigovsky-v7/plans/service-subdivision-page/
service_subdivision_page: IN_IMPLEMENTATION
service_subdivision_pass_1_intro: REMOVED_BY_OPERATOR_DECISION
service_subdivision_primary: REMOVED_BY_OPERATOR_DECISION
service_subdivision_upper_structure: RECONSTRUCTED_FROM_FIGMA
service_subdivision_subnav_border: CANONICAL_EXISTING_TOKEN
service_subdivision_anchor_map: VALID
service_subdivision_pass_1: CORRECTED_AND_INTEGRATED
service_subdivision_intro_markup: SUPERSEDED_NOT_IN_RUNTIME
service_subdivision_optional_regions: CONDITIONAL_RENDERING_ENABLED
service_subdivision_primary_content: REMOVED_BY_OPERATOR_DECISION
service_subdivision_pass_2: COMPLETE
service_subdivision_nature: PRESERVED
service_subdivision_info_cards: PRESERVED
service_subdivision_first_cta: PRESERVED
service_subdivision_program: PRESERVED
service_subdivision_visible_mockup_text_policy: ACTIVE
service_subdivision_lifebuoy_decor: FORBIDDEN_ZERO
service_subdivision_root_tokens_added: ZERO
service_subdivision_pass_3: COMPLETE
service_subdivision_hero_inner_alignment: CANONICAL_CONTAINER_ALIGNED
service_subdivision_dependencies: IMPLEMENTED_FROM_FIGMA
service_subdivision_nature_lead: CANONICAL_EXISTING_PATTERN_REUSED
service_subdivision_team_stats: HOME_FEATURE_GRID_PATTERN_REUSED
service_subdivision_specialists: COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_founder: COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_comfort: COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_reviews: COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_faq: COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_final_form: COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_full_page: STRUCTURALLY_COMPLETE_PENDING_OPERATOR_REVIEW
service_subdivision_temporary_boundaries: ZERO
service_subdivision_pass_4: INTEGRATED_INTO_FINAL_LOWER_PASS
service_subdivision_final_lower_pass_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-subdivision-final-lower-pass/
service_subdivision_pass_3_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-subdivision-pass-3/
service_subdivision_stages: IMPLEMENTED
service_subdivision_second_cta: IMPLEMENTED
service_subdivision_approach: IMPLEMENTED
service_subdivision_center_visual: IMPLEMENTED
service_subdivision_pass_1_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-subdivision-pass-1/
service_subdivision_pass_2_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-subdivision-pass-2/
service_subdivision_png_group_1: COMPLETE
service_subdivision_png_group_2: COMPLETE
service_subdivision_cta_01: PNG_MATCH_COMPLETE
service_subdivision_program: PNG_MATCH_COMPLETE
service_subdivision_cta_02: PNG_MATCH_COMPLETE
service_subdivision_group_2_desktop: PASS
service_subdivision_group_2_mobile: PASS
service_subdivision_png_group_3: COMPLETE
service_subdivision_rehabilitation_stages: PNG_MATCH_COMPLETE
service_subdivision_rehabilitation_support: PNG_MATCH_COMPLETE
service_subdivision_group_3_desktop: PASS
service_subdivision_group_3_mobile: PASS
service_subdivision_png_group_4: COMPLETE
service_subdivision_team_center: PNG_MATCH_COMPLETE
service_subdivision_team_stats: PNG_MATCH_COMPLETE
service_subdivision_corridor_interior: PNG_MATCH_COMPLETE
service_subdivision_group_4_empty_media: ZERO
service_subdivision_group_4_artificial_blank_zones: ZERO
service_subdivision_group_4_desktop: PASS
service_subdivision_group_4_mobile: PASS
service_subdivision_remaining_groups: ZERO
service_subdivision_full_page: COMPLETE
service_subdivision_canonical_switch: NOT_STARTED
service_subdivision_second_cta: REMOVED_FROM_RUNTIME_PNG_AUTHORITY
service_subdivision_approach_v1: SUPERSEDED_NOT_IN_RUNTIME
service_subdivision_clinic_landscape: HOME_SHARED_COMPONENT_REUSED
service_subdivision_program_template_garbage: ZERO
service_subdivision_dependencies_row_borders: REMOVED_BY_OPERATOR_DECISION
service_subdivision_final_corrections: COMPLETE
service_subdivision_build: PASS
service_subdivision_functional_qa: PASS
service_subdivision_regression_qa: PASS
service_subdivision_stable_source_backup: COMPLETE
service_subdivision_stable_tag: fp-0002-v7-service-subdivision-internal-page-reference-01
service_subdivision_reference_type: SERVICE_SUBDIVISION_INTERNAL_PAGE
service_subdivision_operator_status: CONDITIONALLY_ACCEPTED_REFERENCE
service_subdivision_navigation_switch: NOT_STARTED
service_subdivision_deploy: NOT_STARTED
fp0002_png_grouped_page_implementation_protocol: ACTIVE_REFERENCE_WORKFLOW
service_subdivision_final_reference_freeze_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-subdivision-final-reference-freeze/
next_page: FP-0002-PG-004-SERVICE-LEAF-INTERNAL-PAGE
next_phase: FP-0002-PG-004-SERVICE-LEAF-FULL-PAGE-OPERATOR-REVIEW
services_v2_reference: PRESERVED
service_leaf_page_id: FP-0002-PG-004
service_leaf_page_name: Услуга конечная
service_leaf_page_type: SERVICE_LEAF_INTERNAL_PAGE
service_leaf_source: src/pages/usluga-konechnaya-v1.html
service_leaf_group_1: COMPLETE
service_leaf_group_1_hero: PNG_MATCH_COMPLETE
service_leaf_group_1_navigation: PNG_MATCH_COMPLETE
service_leaf_group_1_intro: PNG_MATCH_COMPLETE
service_leaf_group_1_bordered_info: PNG_MATCH_COMPLETE_WITH_OPERATOR_DECOR_OVERRIDE
service_leaf_group_1_cta: PNG_MATCH_COMPLETE
service_leaf_lifebuoy_runtime: ZERO_BY_OPERATOR_OVERRIDE
service_leaf_group_1_desktop: PASS
service_leaf_group_1_mobile: PASS
service_leaf_group_2: COMPLETE
service_leaf_group_2_name: SIGNS_OF_ALCOHOL_DEPENDENCE_EDITORIAL
service_leaf_group_2_text_transcript: COMPLETE
service_leaf_group_2_content_fidelity: EXACT_VISIBLE_DESIGN_COPY
service_leaf_group_2_desktop: PASS
service_leaf_group_2_mobile: PASS
service_leaf_group_2_missing_text: ZERO
service_leaf_group_2_invented_copy: ZERO
service_leaf_group_2_template_garbage: ZERO
service_leaf_group_3: COMPLETE
service_leaf_group_3_name: TREATMENT_APPROACH_TEAM_AND_LANDSCAPE
service_leaf_group_3_desktop: PASS
service_leaf_group_3_mobile: PASS
service_leaf_group_4: COMPLETE
service_leaf_group_4_name: FOUR_DIRECTION_PROGRAM
service_leaf_group_4_desktop: PASS
service_leaf_group_4_mobile: PASS
service_leaf_group_5: COMPLETE
service_leaf_group_5_name: REHABILITATION_REQUIREMENTS_STAGES_AND_INTERIOR
service_leaf_group_5_desktop: PASS
service_leaf_group_5_mobile: PASS
service_leaf_group_6: COMPLETE
service_leaf_group_6_name: SHARED_LOWER_BLOCKS
service_leaf_group_6_desktop: PASS
service_leaf_group_6_mobile: PASS
service_leaf_remaining_groups: COMPLETE
service_leaf_full_page: COMPLETE_PENDING_OPERATOR_REVIEW
service_leaf_operator_wip_backup: COMPLETE
service_leaf_auto_polish: ACCEPTED_AS_PART_OF_CURRENT_CANONICAL_SOURCE
service_leaf_polish_reference: HOME_PLUS_SERVICE_SUBDIVISION_PLUS_SERVICES_V2
service_leaf_content_changed: NO
service_leaf_block_order_changed: NO
service_leaf_assets_changed: NO
service_leaf_operator_edits_preserved: YES
service_leaf_root_tokens_added: ZERO
service_leaf_stable_freeze: COMPLETE
service_leaf_desktop: PASS
service_leaf_mobile: PASS
service_leaf_functional_qa: PASS
service_leaf_regression_qa: PASS
service_leaf_noindex: ACTIVE
fp0002_operator_manual_edits: CANONICAL
fp0002_auto_polish: ACCEPTED_AS_PART_OF_CURRENT_CANONICAL_SOURCE
fp0002_four_template_baseline: CANONICAL_STABLE
fp0002_home_template: CANONICAL_STABLE
fp0002_services_hub_template: CANONICAL_STABLE
fp0002_service_subdivision_template: CANONICAL_STABLE
fp0002_service_leaf_template: CANONICAL_STABLE
fp0002_static_demo_site: PASS_4_FINAL_QA_COMPLETE
fp0002_static_demo_client_readiness: READY_FOR_DEPLOYMENT
fp0002_static_demo_overflow: ZERO_CONFIRMED
fp0002_static_demo_visual_readiness: READY_FOR_CLIENT_QA
fp0002_static_demo_excel_authority: CONFIRMED
fp0002_static_demo_page_registry: FINAL_58_PAGES
fp0002_static_demo_url_registry: FINAL_58_PAGES
fp0002_static_demo_title_h1_registry: FINAL_58_PAGES
fp0002_static_demo_navigation_registry: COMPLETE
fp0002_static_demo_placeholder_registry: FINAL_58_PAGES
fp0002_static_demo_generation: IMPLEMENTED
fp0002_static_demo_generated_pages: 58
fp0002_static_demo_template_pages: 12
fp0002_static_demo_placeholder_pages: 46
fp0002_static_demo_breadcrumbs: IMPLEMENTED
fp0002_static_demo_navigation: COMPLETE
fp0002_static_demo_full_navigation: COMPLETE
fp0002_static_demo_link_graph: COMPLETE
fp0002_static_demo_internal_404: ZERO
fp0002_static_demo_broken_anchors: ZERO
fp0002_static_demo_unexpected_orphans: ZERO
fp0002_static_demo_active_states: IMPLEMENTED
fp0002_static_demo_http_200: 58
fp0002_static_demo_asset_failures: ZERO
fp0002_static_demo_console_errors: ZERO
fp0002_static_demo_functional_qa: PASS
fp0002_static_demo_deploy_pack: V2_READY
fp0002_static_demo_deployment: NOT_PERFORMED_BY_TASK
fp0002_static_demo_composition: URGENT_V2_COMPLETE
fp0002_static_demo_primary_pages: 58
fp0002_static_demo_legacy_aliases: 1
fp0002_static_demo_dependencies_page: RENAMED_TO_ZAVISIMOSTI
fp0002_static_demo_genotipirovanie_route: LEGACY_ALIAS_ONLY
fp0002_static_demo_task_001_placeholders: 11_TARGETS_COMPLETE
fp0002_static_demo_task_002_placeholders: 4_UNIQUE_URLS_COMPLETE
fp0002_about_page: REUSE_FIRST_REBUILD_V3_IMPLEMENTED
fp0002_about_page_source: src/pages/o-centre-v1.html
fp0002_about_page_visual_donor_map: COMPLETE
fp0002_about_page_architecture: EXACT_COMPONENT_REUSE
fp0002_about_page_new_namespaces: ZERO
fp0002_about_page_preview: READY_FOR_OPERATOR_VISUAL_REVIEW
fp0002_about_page_registry_switch: NOT_STARTED
fp0002_about_page_route_switch: NOT_STARTED
fp0002_static_demo_v2: UNCHANGED
fp0002_deployment: UNCHANGED
fp0002_static_demo_client_url: NOT_ASSIGNED
fp0002_static_demo_deploy: NOT_STARTED
fp0002_static_demo_structure_source: CONFIRMED
fp0002_static_demo_planning_pack: workspaces/fp-0002-shpigovsky-v7/plans/static-client-demo/
fp0002_static_demo_generator: IMPLEMENTED
fp0002_canonical_templates: UNCHANGED
fp0002_placeholder_page_contract: READY
fp0002_wordpress: NOT_STARTED
fp0002_canonical_switch: NOT_STARTED
fp0002_navigation_switch: NOT_STARTED
fp0002_deploy: NOT_STARTED
fp0002_four_template_freeze_tag: fp-0002-v7-four-template-canonical-demo-baseline-01
service_leaf_group_1_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-leaf-group-1/
service_leaf_group_2_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-leaf-group-2/
service_leaf_group_3_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-leaf-group-3/
service_leaf_group_4_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-leaf-group-4/
service_leaf_full_page_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-leaf-remaining-page/
service_leaf_implementation: FULL_PAGE_ASSEMBLY_COMPLETE
service_leaf_canonical_switch: NOT_STARTED
service_leaf_navigation_switch: NOT_STARTED
service_leaf_deploy: NOT_STARTED
service_leaf_pass_opening_review: workspaces/fp-0002-shpigovsky-v7/reviews/service-leaf-pass-opening/
service_leaf_planning_pack: workspaces/fp-0002-shpigovsky-v7/plans/service-leaf-page/
```

## Milestone (2026-06-23)

**FP-0002 WORDPRESS FOUNDATION CLOSURE (FW-06A.1)** — local runtime `shpigovsky.test` validated: direct domain PASS, `wp db check` PASS, Playwright foundation smoke PASS. Theme integration **LOCKED** until Frontend Production Pass and FW-06B.

## MLI-03R.1 post-reboot (2026-06-24)

After full Windows reboot, MySQL datadir/config drift broke DB connectivity. Remediation restored authoritative `my.ini`, loopback binding, and X Protocol disable. **No reinstall, no DB recreate, no password rotation.**

```text
FP-0002 WordPress foundation:
READY — POST-REBOOT VALIDATED

Evidence:
wp db check PASS; HTTP 200; Playwright 5/5; controlled MySQL restart PASS
Report: projects/mars-localhost-infrastructure/reports/MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md
```

---

## Phase

| Field | Value |
|-------|-------|
| **Phase** | **Foundation** |

---

## Website Factory status

| Field | Value |
|-------|-------|
| **Website Factory Status** | **Pre-Onboarding** |

Manifest enrollment (Playbook 01), registry enrollment (Playbook 02), and RT-G04 substrate (POC-01…POC-10) are **not started** for FP-0002.

---

## Production lanes

| Lane | Status |
|------|--------|
| **Frontend** | **V7 ACTIVE_DEVELOPMENT** — Package #001 complete pending operator final review (gallery captions below image, controlled polish) |
| **WordPress** | **Foundation READY — POST-REBOOT VALIDATED (MLI-03R.1)** — local runtime `shpigovsky.test`; theme integration **LOCKED** until Production Pass + FW-06B |
| **QA** | Not Started |
| **Delivery** | Not Started |

---

## Design and inventory

| Field | Value |
|-------|-------|
| **Design Materials** | Awaiting Intake |
| **Page Inventory** | **Updated** — `foundation/FP-0002-V6-PAGE-INVENTORY.md` in V6 workspace |
| **Block Inventory** | **Updated** — `reviews/services-page/reuse-only/FP-0002-HOME-BLOCK-INVENTORY-v1.md` |

---

## Services page status

| Field | Value |
|-------|-------|
| `services_foundation` | COMPLETE |
| `services_rejected_unique_implementation` | REVERTED (`25bfbce`) |
| `services_reuse_matrix` | COMPLETE |
| `services_page_mode` | REUSE_ONLY |
| `services_exact_reused_blocks` | header, program, founder, comfort, FAQ, final form, footer, modal |
| `services_new_unique_blocks` | 0 |
| `services_unimplemented_blocks` | hero, addictions, mental-health, eating-disorders |
| `services_unique_blocks` | REJECTED_AND_REVERTED |

---

## ATLAS linkage

| Check | Status |
|-------|--------|
| PRJ-0012 attested | **Yes** — AT-W3-SHPIG-01 |
| WEB-SHPIG-01 attested | **Yes** — AT-W4-SHPIG-01 |
| DOM-SHPIG-01 attested | **Yes** — AT-W5-SHPIG-01 |
| ORG-0008 attested | **Yes** — AT-W1D-SHPIG-01 |
| Factory manifest bind | **No** — pending onboarding |

---

## Intake

| Intake area | Status |
|-------------|--------|
| Structure | **Ready** — INCOMING/ scaffold created |
| Design materials | **Empty** — awaiting client/operator intake |
| Content | **Empty** |
| Access / hosting | **Empty** |

---

## Next gate

**Package #001** — implementation complete pending operator final visual review. WordPress theme integration **LOCKED** until operator sign-off + FW-06B.

---

*Status register only. Not a runtime state store.*


## 2026-07-04 — V9-06D.1 rerun runtime delivery

PASS: local WordPress runtime received canonical theme, Shpigovsky Core, and ACF JSON. Content model activation verified; service CPT registered; ACF groups and Options Page discoverable. WordPress object skeleton and V9 integration remain not started.


## 2026-07-04 — V9-06D.2 WordPress object skeleton

PASS: local WordPress runtime object skeleton created under checkpoint control. Services total: 15; Pages created: 0; Page templates reconciled: 13; Posts created: 0; Menus/options/redirects/rewrite flush unchanged. Content migration and V9 integration remain not started.


## 2026-07-04 — V9-06D.3 content migration planning

PASS: planning/audit only. 31 routes mapped; minimal visual content seed plan READY. Runtime content writes: 0.


## 2026-07-04 — V9-06D.4 RERUN minimal content seed for visual route QA

PARTIAL PASS: minimal ACF/meta seed applied to Pages 4/5/20 and Services 73/74/77/84 under DB checkpoint. Unauthorized writes: 0. Menus/options/redirects unchanged. Rewrite flush not performed. Service 74 HTTP 404 with matching generated permalink → REWRITE_FLUSH_MICRO_GATE_REQUIRED. Full content migration and V9 integration not performed.


## 2026-07-04 — REWRITE-FLUSH-MICRO-GATE

PARTIAL PASS: soft rewrite flush performed under DB checkpoint; `rewrite_rules` updated; `.htaccess` unchanged; content/ACF/menus/redirects/objects unchanged. Service 74 still HTTP 404 with matching generated permalink → FLUSH_NOT_SUFFICIENT. Next: route ownership / path conflict investigation.
