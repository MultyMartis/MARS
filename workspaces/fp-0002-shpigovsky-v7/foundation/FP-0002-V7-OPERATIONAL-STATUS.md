# FP-0002 V7 Operational Status

**Updated:** 2026-06-26 (Services V2 Block 1 — upper page)

```text
workspace: V7
lifecycle: ACTIVE_DEVELOPMENT
parent_v6: FROZEN_FALLBACK
parent_tag: fp-0002-v6-final-before-v7-operator-stable-01
pre_final_polish_tag: fp-0002-v7-pre-final-polish-operator-stable-01
pre_final_polish_release: FP-0002-V7-PRE-FINAL-POLISH-OPERATOR-STABLE-01

source_parity_with_v6: PASS
visual_parity_with_v6: PASS (V7 supersedes for Package #001)
functional_parity_with_v6: PASS
v7_bootstrap: COMPLETE

design_authority: Spig_v1.2.fig
design_authority_status: ACTIVE
historical_design_source: Шпиговский.fig
historical_design_source_status: DO_NOT_USE_FOR_NEW_WORK
historical_design_sha256: D25A13617664040045A88AE9B804FEB737076007CB317D49699196F92232B64B
active_design_sha256: BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041

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

gallery_captions:
  CONTENT_VERIFIED
  POSITION_BELOW_IMAGE
  DESKTOP_COMPLETE
  MOBILE_COMPLETE_OR_RESPONSIVE_DERIVED

recovery_life:
  DESKTOP_COMPLETE
  MOBILE_RESPONSIVE_DERIVED_COMPLETE

spacing_cleanup: COMPLETE
global_visual_polish: COMPLETE_PENDING_OPERATOR_FINAL_REVIEW

head:
  TECHNICALLY_COMPLETE
  MARKETING_COPY_REVIEW_PENDING
  FAVICON_VISUAL_REVIEW_PENDING
  OG_VISUAL_REVIEW_PENDING

form_backend: BLOCKED
captcha: BLOCKED

visible_content_authority_rule: ACTIVE
hidden_layer_exclusion_rule: ACTIVE

operator_manual_checkpoint:
  date: 2026-06-26
  note: Operator manual polish checkpoint before Package #002. Current src is operator-canonical. Existing manual dimensions, spacing, typography and composition must be preserved.
  status: COMPLETE
  committed: true
  pushed: true
  commit: 95b97adf

package_002: COMPLETE_PENDING_OPERATOR_REVIEW
external_link_svg: COMPLETE
hero_architecture:
  HOME_COMPLETE: true
  INNER_PAGE_BASE_COMPLETE: true
  MOBILE_RESPONSIVE_COMPLETE: true
slider_pagination: COMPLETE
home_videos: COMPLETE
faq_filler: COMPLETE_TEMPORARY_CONTENT
home_recovery_intro_text: FIGMA_EXACT_COMPLETE

operator_checkpoint_before_package_003:
  date: 2026-06-26
  status: NOT_REQUIRED
  note: No src delta after dae060b0; source ZIP backup created pre-Package-003
  backup_zip: FP-0002-V7-BEFORE-PACKAGE-003-SOURCE.zip
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
services_general_final_polish_commit: pending
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
services_v2_missing_visible_text: ZERO_REAL_RUSSIAN_OMISSIONS
services_v2_true_visible_placeholders: 0
services_v2_extraction_failures: ZERO_UNRESOLVED_AFTER_PNG_ADJUDICATION
services_v2_premature_compaction: REMOVED_OR_CORRECTED
services_v2_category_geometry: CONTENT_DRIVEN
services_v2_operator_copy_required: []
services_v2_mockup_copy_review: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-exact-mockup-copy/
services_v2_text_recovery_review: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-category-text-recovery/
services_v2_category_family:
COMPLETE_PENDING_OPERATOR_POLISH

services_v2_mockup_text_policy:
ALL_VISIBLE_TEXT_INCLUDED

services_v2_hero_layout:
CORRECTED_PENDING_OPERATOR_REVIEW

services_v2_gallery_media_height:
NORMALIZED

services_v2_program_dom:
BODY_BEFORE_MEDIA

services_v2_program_card_pattern:
HOME_DIRECTION_STYLE_REUSED

services_v2_program:
COMPLETE_PENDING_OPERATOR_REVIEW

services_v2_program_mockup_text:
COMPLETE

services_v2_program_empty_content_slots:
ZERO

services_v2_program_component:
SERVICES_SPECIFIC_REUSABLE_PARTIAL

services_v2_program_review: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-program/
services_v2_lower_pass_review: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-founder-comfort-cta/

services_v2_founder:
HOME_FOUNDER_QUOTE_REUSED

services_v2_comfort:
HOME_COMFORT_REUSED

services_v2_mid_page_cta:
SECOND_PROGRAM_CTA_BAND_REUSED

services_v2_faq:
HOME_FAQ_REUSED

services_v2_final_form:
HOME_FINAL_FORM_REUSED

services_v2_program_item_descriptions:
REMOVED_BY_OPERATOR_DECISION

services_v2_lower_page_assembly:
COMPLETE_PENDING_OPERATOR_REVIEW

services_v2_operator_acceptance:
CONDITIONAL_ACCEPTED_REFERENCE

services_v2_reference_type:
SERVICES_HUB_INTERNAL_PAGE

services_v2_lifebuoy_decor:
REMOVED_BY_OPERATOR_DECISION

services_v2_detail_links:
HOME_REHABILITATION_PATTERN_REUSED

services_v2_reference_baseline:
READY_FOR_FREEZE

services_v2_canonical_switch:
NOT_STARTED

services_v1:
PRESERVED_FALLBACK

services_v2_reference_freeze_review: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-reference-freeze/
next_phase: SERVICE_SUBDIVISION_PAGE_PASS_3_OPERATOR_REVIEW

service_subdivision_page:
IN_IMPLEMENTATION

service_subdivision_pass_1_intro:
REMOVED_BY_OPERATOR_DECISION

service_subdivision_primary:
REMOVED_BY_OPERATOR_DECISION

service_subdivision_upper_structure:
RECONSTRUCTED_FROM_FIGMA

service_subdivision_subnav_border:
CANONICAL_EXISTING_TOKEN

service_subdivision_anchor_map:
VALID

service_subdivision_pass_1:
CORRECTED_AND_INTEGRATED

service_subdivision_intro_markup:
SUPERSEDED_NOT_IN_RUNTIME

service_subdivision_optional_regions:
CONDITIONAL_RENDERING_ENABLED

service_subdivision_primary_content:
REMOVED_BY_OPERATOR_DECISION

service_subdivision_pass_2:
COMPLETE

service_subdivision_nature:
PRESERVED

service_subdivision_info_cards:
PRESERVED

service_subdivision_first_cta:
PRESERVED

service_subdivision_program:
PRESERVED

service_subdivision_working_page:
src/pages/usluga-podrazdel-v1.html

service_subdivision_visible_mockup_text_policy:
ACTIVE

service_subdivision_lifebuoy_decor:
FORBIDDEN_ZERO

service_subdivision_root_tokens_added:
ZERO

service_subdivision_pass_3:
COMPLETE_PENDING_OPERATOR_REVIEW

service_subdivision_stages:
IMPLEMENTED

service_subdivision_second_cta:
IMPLEMENTED

service_subdivision_approach:
IMPLEMENTED

service_subdivision_center_visual:
IMPLEMENTED

service_subdivision_team_stats:
IMPLEMENTED

service_subdivision_pass_4:
NOT_STARTED

service_subdivision_pass_1_review:
workspaces/fp-0002-shpigovsky-v7/reviews/service-subdivision-pass-1/

service_subdivision_pass_2_review:
workspaces/fp-0002-shpigovsky-v7/reviews/service-subdivision-pass-2/

service_subdivision_pass_3_review:
workspaces/fp-0002-shpigovsky-v7/reviews/service-subdivision-pass-3/

services_v2_reference:
PRESERVED

home_operator_baseline_checkpoint:
  date: 2026-06-26
  status: FROZEN
  backup_id: FP-0002-V7-HOME-OPERATOR-STABLE-BEFORE-STYLE-AUDIT-01
  backup_path: C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\operator-checkpoints\FP-0002-V7-HOME-OPERATOR-STABLE-BEFORE-STYLE-AUDIT-01-SOURCE.zip
  backup_sha256: 61A7AC49E4A55EEDFF5389B91F91C3467D0134D1482E5F1FEDB598E3B0E6506B
  operator_edits_after_package_003:
    - src/partials/sections/home-recovery-intro.html
    - src/scss/style.scss

operator_checkpoint_before_services_planning:
  date: 2026-06-26
  status: COMPLETE
  backup_id: FP-0002-V7-OPERATOR-DELTA-BEFORE-SERVICES-PLANNING-01
  backup_path: C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\operator-checkpoints\FP-0002-V7-OPERATOR-DELTA-BEFORE-SERVICES-PLANNING-01-SOURCE.zip
  backup_sha256: 161003A850B88A63EC834ED7469DBBE800DD507D841DEB9E6E2F2022D24DD14F
  operator_deltas_committed: true
  planning_pack: workspaces/fp-0002-shpigovsky-v7/plans/services-general-01/
```

## Parent reference

| Field | Value |
|-------|-------|
| V6 workspace | `workspaces/fp-0002-shpigovsky-v6/` |
| V6 lifecycle | `FROZEN_FALLBACK` |
| V6 freeze commit | `85a6d654` |
| Pre-polish V7 release | `workspaces/fp-0002-shpigovsky-v7/releases/FP-0002-V7-PRE-FINAL-POLISH-OPERATOR-STABLE-01/` |
| External backup ZIP SHA-256 | `16e07ad168231ce4b9aa00eb60a35d1e1e4e0729ec140cc2dec9dbc426ff8d19` |

## Package #001 boundary

Phases 1–4A and gallery caption placement correction complete. Global polish audited with minimal proven corrections. Operator final visual review pending before WordPress integration.
