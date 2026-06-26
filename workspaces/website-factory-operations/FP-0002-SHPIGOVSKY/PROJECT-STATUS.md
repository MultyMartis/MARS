# FP-0002 — Project Status

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Last updated:** 2026-06-26 (Services V2 Block 1 — upper page complete pending operator review)

## Workspace versions (2026-06-24)

| Workspace | Path | Lifecycle | Tag / parent |
|-----------|------|-----------|--------------|
| **V6** | `workspaces/fp-0002-shpigovsky-v6/` | **FROZEN_FALLBACK** | `fp-0002-v6-final-before-v7-operator-stable-01` |
| **V7** | `workspaces/fp-0002-shpigovsky-v7/` | **ACTIVE_DEVELOPMENT** | `fp-0002-v7-pre-final-polish-operator-stable-01` |

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
services_v2_block_2a: COMPLETE_PENDING_OPERATOR_REVIEW
services_v2_category_reference_pattern: ADDICTIONS_IMPLEMENTED
services_v2_remaining_categories: NOT_STARTED
services_v2_program: NOT_STARTED
services_v2_manual_polish: OPERATOR_REQUIRED
services_v2_root_tokens_added: ZERO
services_v1: PRESERVED_FALLBACK
services_v2_page: workspaces/fp-0002-shpigovsky-v7/src/pages/uslugi-v2.html
services_v2_review_block_2a: workspaces/fp-0002-shpigovsky-v7/reviews/services-v2-block-2a/
home_source_universalization: NOT_STARTED
next_phase: SERVICES_V2_CATEGORY_RECONSTRUCTION_BLOCK_2
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
