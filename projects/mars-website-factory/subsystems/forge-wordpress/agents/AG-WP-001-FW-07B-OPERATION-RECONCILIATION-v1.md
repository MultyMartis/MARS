# AG-WP-001 — FW-07B Operation Reconciliation v1

**Document type:** Reconciliation audit  
**Version:** v1  
**Stage:** FW-07B  
**Date:** 2026-06-24  
**Source:** [FORGE-WORDPRESS-AG-WP-001-OPERATION-REGISTRY-v1.md](../registries/FORGE-WORDPRESS-AG-WP-001-OPERATION-REGISTRY-v1.md) (FW-07A)

**Machine-readable authority:** [operations/ag-wp-001/operations-v1.json](../operations/ag-wp-001/operations-v1.json)

---

## ID normalization

| FW-07A legacy `op_id` | Canonical `operation_id` | Alias rule |
|-----------------------|------------------------|------------|
| `inspect_wp_runtime` | `wp.inspect.runtime` | `legacy_op_id` field |
| `inspect_frontend_handoff` | `wp.inspect.frontend_handoff` | same |
| `inspect_theme` | `wp.inspect.theme` | same |
| `inspect_functionality_plugin` | `wp.inspect.functionality_plugin` | same |
| `inspect_content_model` | `wp.inspect.content_model` | same |
| `inspect_plugin_state` | `wp.inspect.plugin_state` | same |
| `inspect_routes` | `wp.inspect.routes` | same |
| `inspect_templates` | `wp.inspect.templates` | same |
| `inspect_assets` | `wp.inspect.assets` | same |
| `inspect_forms` | `wp.inspect.forms` | same |
| `inspect_editor_configuration` | `wp.inspect.editor_configuration` | same |
| `draft_implementation_plan` | `wp.plan.implementation` | same |
| `draft_theme_architecture` | `wp.plan.theme_architecture` | same |
| `draft_functionality_architecture` | `wp.plan.functionality_architecture` | same |
| `draft_content_model` | `wp.plan.content_model` | same |
| `draft_plugin_decision` | `wp.plan.plugin_decisions` | pluralized canonical |
| `draft_editor_governance` | `wp.plan.editor_governance` | same |
| `draft_migration_plan` | `wp.plan.migration` | same |
| `draft_validation_plan` | `wp.plan.validation` | same |
| `scaffold_theme` | `wp.scaffold.theme` | same |
| `scaffold_functionality_plugin` | `wp.scaffold.functionality_plugin` | same |
| `scaffold_tests` | `wp.scaffold.tests` | same |
| `generate_acf_json` | `wp.generate.acf_json` | same |
| `generate_template` | `wp.generate.template` | same |
| `generate_template_part` | `wp.generate.template_part` | same |
| `generate_custom_block` | `wp.generate.custom_block` | same |
| `apply_approved_source_change` | `wp.change.apply_approved_source` | same |
| `validate_php_syntax` | `wp.validate.php_syntax` | same |
| `validate_wpcs` | `wp.validate.wpcs` | same |
| `validate_wordpress_checksums` | `wp.validate.core_checksums` | renamed canonical |
| `validate_database` | `wp.validate.database` | same |
| `validate_routes` | `wp.validate.routes` | same |
| `validate_rendering` | `wp.validate.rendering` | same |
| `validate_visual_fidelity` | `wp.validate.visual_fidelity` | same |
| `validate_accessibility` | `wp.validate.accessibility` | same |
| `validate_security` | `wp.validate.security` | same |
| `validate_plugin_risk` | `wp.validate.plugin_risk` | same |
| `create_backup` | `wp.backup.create` | same |
| `create_checkpoint` | `wp.checkpoint.create` | same |
| `prepare_review_package` | `wp.review.prepare` | same |
| `prepare_rollback` | `wp.rollback.prepare` | same; `wp.plan.rollback` is planning-phase alias |

**FW-03 mapping:** `inspect_frontend_package` → `wp.inspect.frontend_handoff`; `inspect_wordpress_project` remains FW-03 only until chartered.

---

## Reconciliation table (summary)

| Operation | Category | FW-07A def | Duplicate | Schema | Tool candidate | Status |
|-----------|----------|------------|-----------|--------|----------------|--------|
| `wp.inspect.runtime` | inspection | yes | no | yes | WP-CLI, MLI manifest, HTTP | BOUND_NOT_IMPLEMENTED |
| `wp.inspect.frontend_handoff` | inspection | yes | no | yes | filesystem, Git | UNBOUND |
| `wp.inspect.theme` | inspection | yes | no | yes | WP-CLI, filesystem | BOUND_NOT_IMPLEMENTED |
| `wp.inspect.functionality_plugin` | inspection | yes | no | yes | filesystem | UNBOUND |
| `wp.inspect.content_model` | inspection | yes | no | yes | WP-CLI, docs | UNBOUND |
| `wp.inspect.plugin_state` | inspection | yes | no | yes | WP-CLI | BOUND_NOT_IMPLEMENTED |
| `wp.inspect.routes` | inspection | yes | no | yes | WP-CLI, HTTP/Playwright | BOUND_NOT_IMPLEMENTED |
| `wp.inspect.templates` | inspection | yes | no | yes | filesystem | UNBOUND |
| `wp.inspect.assets` | inspection | yes | no | yes | filesystem | UNBOUND |
| `wp.inspect.forms` | inspection | yes | no | yes | filesystem, HTTP | UNBOUND |
| `wp.inspect.editor_configuration` | inspection | yes | no | yes | filesystem | UNBOUND |
| `wp.plan.*` (9 ops) | planning | yes | no | yes | Cursor Agent (brain) | UNBOUND |
| `wp.scaffold.*` (3) | scaffold | yes | no | yes | guarded source | BOUND_NOT_IMPLEMENTED / UNBOUND |
| `wp.generate.*` (4) | generation | yes | no | yes | guarded source | UNBOUND |
| `wp.change.apply_approved_source` | change | yes | no | yes | guarded diff | UNBOUND |
| `wp.validate.*` (10) | validation | yes | no | yes | PHP, PHPCS, WP-CLI, Playwright | partial BOUND |
| `wp.backup.create` | backup | yes | no | yes | backup scripts | UNBOUND |
| `wp.checkpoint.create` | checkpoint | yes | no | yes | Git selective | BOUND_NOT_IMPLEMENTED |
| `wp.review.prepare` | review | yes | no | yes | report bundler | UNBOUND |
| `wp.rollback.prepare` | rollback | yes | no | yes | Git manifest | UNBOUND |

**Totals:** 42 operations; 0 duplicate canonical IDs; 42 machine-readable schemas; 10 contract bindings (none PROVEN/IMPLEMENTED).

---

*Reconciliation v1 — FW-07B.*
