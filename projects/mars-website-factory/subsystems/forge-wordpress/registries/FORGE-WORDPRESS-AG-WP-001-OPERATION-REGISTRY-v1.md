# Forge WordPress — AG-WP-001 Operation Registry v1

**Document type:** Typed operation registry (contract level)  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24  
**Agent:** AG-WP-001

**Extends:** [FORGE-WORDPRESS-COMMAND-AND-OPERATION-MODEL-v1.md](../FORGE-WORDPRESS-COMMAND-AND-OPERATION-MODEL-v1.md)  
**Risk classes:** [AG-WP-001-RISK-AND-APPROVAL-MATRIX-v1.md](../agents/AG-WP-001-RISK-AND-APPROVAL-MATRIX-v1.md)

**Honesty:** Operation **specifications** only — **not** implemented runtime, MCP, or Abilities API (FW-07B).

---

## Registry legend

| Column | Meaning |
|--------|---------|
| **op_id** | Stable operation identifier |
| **risk** | R0–R5 per AG-WP-001 matrix |
| **scope** | `local` · `staging` · `production` |
| **approval** | `auto` · `plan+checkpoint` · `operator` · `denied` |
| **rollback** | Method summary |
| **failure** | `stop` · `report` · `escalate` |

---

## Inspection operations (R0)

| op_id | description | input schema | output schema | risk | scope | approval | rollback | audit | failure |
|-------|-------------|--------------|---------------|------|-------|----------|----------|-------|---------|
| `inspect_wp_runtime` | Validate MLI runtime profile vs manifest | `runtime_id`, `expected_url` | `runtime_validation_report` | R0 | local | auto | N/A | manifest hash | stop |
| `inspect_frontend_handoff` | Verify input contract completeness | `handoff_manifest`, `commit_sha` | `gate_a_report` | R0 | local | auto | N/A | commit sha | stop |
| `inspect_theme` | Theme structure, hierarchy, enqueue | `theme_path` | `theme_inspection_report` | R0 | local | auto | N/A | file list hash | report |
| `inspect_functionality_plugin` | Plugin bootstrap, CPT registration | `plugin_path` | `plugin_inspection_report` | R0 | local | auto | N/A | file list hash | report |
| `inspect_content_model` | Model doc vs runtime fields | `model_doc`, `runtime_id` | `content_model_diff` | R0 | local | auto | N/A | diff summary | report |
| `inspect_plugin_state` | Installed vs register | `plugin_register`, `runtime_id` | `plugin_state_report` | R0 | local | auto | N/A | plugin list | stop |
| `inspect_routes` | URL resolution smoke | `route_list`, `base_url` | `route_report` | R0 | local | auto | N/A | HTTP status log | report |
| `inspect_templates` | Template map coverage | `template_map`, `theme_path` | `template_coverage_report` | R0 | local | auto | N/A | coverage % | report |
| `inspect_assets` | Asset manifest vs theme | `assets_manifest`, `theme_path` | `asset_audit_report` | R0 | local | auto | N/A | missing asset list | report |
| `inspect_forms` | Forms map vs implementation | `forms_map` | `forms_inspection_report` | R0 | local | auto | N/A | endpoint list | stop |
| `inspect_editor_configuration` | ACF/editor boundaries | `editor_governance_doc` | `editor_audit_report` | R0 | local | auto | N/A | field list | report |

---

## Draft operations (R1)

| op_id | description | input schema | output schema | risk | scope | approval | rollback | audit | failure |
|-------|-------------|--------------|---------------|------|-------|----------|----------|-------|---------|
| `draft_implementation_plan` | Master implementation plan | `handoff_manifest` | `implementation_plan` | R1 | local | human review | discard draft | plan version | report |
| `draft_theme_architecture` | Theme architecture doc | `handoff_manifest`, `mode_decision` | `theme_architecture` | R1 | local | human review | discard | doc id | report |
| `draft_functionality_architecture` | Functionality plugin architecture | `content_model_draft` | `functionality_architecture` | R1 | local | human review | discard | doc id | report |
| `draft_content_model` | Content model proposal | `block_inventory`, `editable_regions` | `content_model` | R1 | local | human review | discard | model version | stop |
| `draft_plugin_decision` | Plugin register proposal | `project_constraints` | `plugin_register_draft` | R1 | local | human review | discard | register id | report |
| `draft_editor_governance` | Editor boundaries doc | `content_model` | `editor_governance` | R1 | local | human review | discard | doc id | report |
| `draft_migration_plan` | Content migration plan | `content_model` | `migration_plan` | R1 | local | human review | discard | plan id | stop |
| `draft_validation_plan` | Project validation plan | `project_scope` | `validation_plan` | R1 | local | human review | discard | plan id | report |

---

## Scaffold / generate operations (R2)

| op_id | description | input schema | output schema | risk | scope | approval | rollback | audit | failure |
|-------|-------------|--------------|---------------|------|-------|----------|----------|-------|---------|
| `scaffold_theme` | Create theme skeleton | `approved_plan`, `slug` | `theme_source_tree` | R2 | local | plan+checkpoint | git revert | commit sha | stop |
| `scaffold_functionality_plugin` | Create plugin skeleton | `approved_plan`, `slug` | `plugin_source_tree` | R2 | local | plan+checkpoint | git revert | commit sha | stop |
| `scaffold_tests` | Test harness skeleton | `project_path` | `test_tree` | R2 | local | plan+checkpoint | git revert | commit sha | report |
| `generate_acf_json` | Version-controlled field JSON | `content_model` | `acf_json_files` | R2 | local | plan+checkpoint | git revert | field group ids | stop |
| `generate_template` | PHP template from map | `template_spec` | `template_file` | R2 | local | plan+checkpoint | git revert | file path | report |
| `generate_template_part` | Template part from partial map | `partial_spec` | `template_part_file` | R2 | local | plan+checkpoint | git revert | file path | report |
| `generate_custom_block` | Block scaffold (hybrid/block mode) | `block_spec` | `block_source` | R2 | local | plan+checkpoint | git revert | block name | report |
| `apply_approved_source_change` | Apply scoped code edit | `change_set`, `approval_ref` | `diff`, `build_log` | R2 | local | plan+checkpoint | git revert | diff hash | stop |

---

## Validation operations (R0–R1)

| op_id | description | input schema | output schema | risk | scope | approval | rollback | audit | failure |
|-------|-------------|--------------|---------------|------|-------|----------|----------|-------|---------|
| `validate_php_syntax` | PHP lint all project PHP | `paths[]` | `php_syntax_report` | R0 | local | auto | N/A | error count | stop |
| `validate_wpcs` | PHPCS/WPCS scan | `paths[]`, `ruleset` | `wpcs_report` | R0 | local | auto/waiver | fix code | report id | report |
| `validate_wordpress_checksums` | Core integrity | `runtime_id` | `checksum_report` | R0 | local | auto | N/A | core version | stop |
| `validate_database` | DB integrity check | `runtime_id` | `db_check_report` | R0 | local | auto | N/A | table status | stop |
| `validate_routes` | HTTP route tests | `route_list` | `route_test_report` | R0 | local | auto | N/A | status codes | report |
| `validate_rendering` | Render smoke (no fatal) | `urls[]` | `render_report` | R0 | local | auto | N/A | response log | stop |
| `validate_visual_fidelity` | Screenshot diff vs baseline | `baselines[]`, `urls[]` | `visual_diff_report` | R0 | local | auto/waiver | re-baseline | diff % | report |
| `validate_accessibility` | a11y scan | `urls[]` | `a11y_report` | R0 | local | auto/waiver | fix | violation count | report |
| `validate_security` | Secret scan, capability review | `source_paths[]` | `security_report` | R0 | local | auto | N/A | finding list | stop |
| `validate_plugin_risk` | Plugin provenance check | `plugin_register` | `plugin_risk_report` | R0 | local | auto | N/A | vuln refs | report |

---

## Checkpoint / package operations (R2–R3)

| op_id | description | input schema | output schema | risk | scope | approval | rollback | audit | failure |
|-------|-------------|--------------|---------------|------|-------|----------|----------|-------|---------|
| `create_backup` | DB + files backup | `runtime_id`, `paths[]` | `backup_manifest` | R3 | local | operator | restore backup | backup id | stop |
| `create_checkpoint` | Git checkpoint + manifest | `message`, `artifacts[]` | `commit_sha`, `checkpoint_manifest` | R2 | local | plan+checkpoint | git revert | sha | stop |
| `prepare_review_package` | Operator review bundle | `reports[]` | `review_package` | R1 | local | human review | N/A | package id | report |
| `prepare_rollback` | Rollback package assembly | `checkpoint_ref` | `rollback_package` | R2 | local | plan+checkpoint | execute rollback | package id | stop |

---

## Forbidden / denied at foundation

| op_id | risk | scope | approval |
|-------|------|-------|----------|
| Any production write | R5 | production | **denied** |
| Unrestricted SQL | R5 | any | **denied** |
| Arbitrary plugin install | R4+ | staging/prod | **denied** |
| MCP bridge auto-expose | — | any | **not approved** |

---

## FW-03 operation mapping

Operations above **superset** FW-03 names (`inspect_frontend_package` → `inspect_frontend_handoff`, etc.). FW-03 remains valid; this registry is **AG-WP-001 authoritative** for agent-bound ops.

---

## Next phase

**FW-07B** — Typed Operations and Tool Contract: machine-readable stubs, runner bindings, optional MCP mapping — **not started**.

---

*Operation registry v1 — contract only.*
