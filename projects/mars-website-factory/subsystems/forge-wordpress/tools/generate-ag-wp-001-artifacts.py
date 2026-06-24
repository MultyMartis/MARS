#!/usr/bin/env python3
"""Generate AG-WP-001 operation definitions, bindings, and failure codes (FW-07B)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = ROOT / "operations" / "ag-wp-001"
BIND_DIR = ROOT / "bindings" / "ag-wp-001"
SCHEMA_DIR = ROOT / "schemas"

PROVEN_BINDINGS = {
    "wp.inspect.runtime": {
        "binding_id": "BIND-WP-INSPECT-RUNTIME-v1",
        "tool_ids": ["MLI-TOOL-007", "MLI-TOOL-015", "FW-TOL-010"],
        "invocation_class": "read_only_cli_and_http",
        "status": "BOUND_NOT_IMPLEMENTED",
        "commands": ["wp option get siteurl", "wp core version", "HTTP GET /"],
        "environment": ["LOCAL_RUNTIME_READ_ONLY"],
    },
    "wp.inspect.theme": {
        "binding_id": "BIND-WP-INSPECT-THEME-v1",
        "tool_ids": ["FW-TOL-010", "MLI-TOOL-007"],
        "invocation_class": "filesystem_and_wp_cli",
        "status": "BOUND_NOT_IMPLEMENTED",
        "commands": ["wp theme list", "filesystem read theme_path"],
        "environment": ["LOCAL_SOURCE", "LOCAL_RUNTIME_READ_ONLY"],
    },
    "wp.inspect.plugin_state": {
        "binding_id": "BIND-WP-INSPECT-PLUGIN-v1",
        "tool_ids": ["FW-TOL-010", "MLI-TOOL-007"],
        "invocation_class": "wp_cli_read_only",
        "status": "BOUND_NOT_IMPLEMENTED",
        "commands": ["wp plugin list --format=json"],
        "environment": ["LOCAL_RUNTIME_READ_ONLY"],
    },
    "wp.inspect.routes": {
        "binding_id": "BIND-WP-INSPECT-ROUTES-v1",
        "tool_ids": ["FW-TOL-010", "MLI-TOOL-014", "FW-TOL-015"],
        "invocation_class": "wp_cli_and_http",
        "status": "BOUND_NOT_IMPLEMENTED",
        "commands": ["wp rewrite list", "HTTP GET routes"],
        "environment": ["LOCAL_RUNTIME_READ_ONLY"],
    },
    "wp.validate.php_syntax": {
        "binding_id": "BIND-WP-VALIDATE-PHP-v1",
        "tool_ids": ["MLI-TOOL-004", "FW-TOL-005"],
        "invocation_class": "php_cli_lint",
        "status": "BOUND_NOT_IMPLEMENTED",
        "commands": ["php -l <file>"],
        "environment": ["LOCAL_SOURCE"],
    },
    "wp.validate.core_checksums": {
        "binding_id": "BIND-WP-VALIDATE-CHECKSUMS-v1",
        "tool_ids": ["MLI-TOOL-007", "FW-TOL-010"],
        "invocation_class": "wp_cli_read_only",
        "status": "BOUND_NOT_IMPLEMENTED",
        "commands": ["wp core verify-checksums"],
        "environment": ["LOCAL_RUNTIME_READ_ONLY"],
    },
    "wp.validate.database": {
        "binding_id": "BIND-WP-VALIDATE-DB-v1",
        "tool_ids": ["MLI-TOOL-007", "MLI-TOOL-005", "FW-TOL-007"],
        "invocation_class": "wp_cli_and_db_check",
        "status": "BOUND_NOT_IMPLEMENTED",
        "commands": ["wp db check"],
        "environment": ["LOCAL_RUNTIME_READ_ONLY"],
    },
    "wp.validate.routes": {
        "binding_id": "BIND-WP-VALIDATE-ROUTES-v1",
        "tool_ids": ["MLI-TOOL-014", "FW-TOL-015"],
        "invocation_class": "http_or_playwright",
        "status": "BOUND_NOT_IMPLEMENTED",
        "commands": ["HTTP GET route_list", "playwright smoke"],
        "environment": ["LOCAL_RUNTIME_READ_ONLY"],
    },
    "wp.validate.wpcs": {
        "binding_id": "BIND-WP-VALIDATE-WPCS-v1",
        "tool_ids": ["MLI-TOOL-008", "MLI-TOOL-009", "FW-TOL-011", "FW-TOL-012"],
        "invocation_class": "phpcs_scan",
        "status": "BOUND_NOT_IMPLEMENTED",
        "commands": ["phpcs --standard=WordPress <paths>"],
        "environment": ["LOCAL_SOURCE"],
    },
    "wp.checkpoint.create": {
        "binding_id": "BIND-WP-CHECKPOINT-v1",
        "tool_ids": ["MLI-TOOL-011", "FW-TOL-001"],
        "invocation_class": "git_selective_commit",
        "status": "BOUND_NOT_IMPLEMENTED",
        "commands": ["git status", "git diff", "git commit (selective, approved scope)"],
        "environment": ["LOCAL_SOURCE"],
    },
}

OPERATIONS_SPEC = [
    # Inspection R0
    ("wp.inspect.runtime", "inspect_wp_runtime", "inspection", "R0", ["LOCAL_RUNTIME_READ_ONLY"], "Validate MLI runtime profile vs manifest", "runtime_validation_report", "IDEMPOTENT", "NONE", False),
    ("wp.inspect.frontend_handoff", "inspect_frontend_handoff", "inspection", "R0", ["BRAIN_ONLY", "LOCAL_SOURCE"], "Verify approved frontend input contract completeness", "gate_a_report", "IDEMPOTENT", "NONE", False),
    ("wp.inspect.theme", "inspect_theme", "inspection", "R0", ["LOCAL_SOURCE", "LOCAL_RUNTIME_READ_ONLY"], "Theme structure, hierarchy, enqueue audit", "theme_inspection_report", "IDEMPOTENT", "NONE", False),
    ("wp.inspect.functionality_plugin", "inspect_functionality_plugin", "inspection", "R0", ["LOCAL_SOURCE"], "Functionality plugin bootstrap and CPT registration audit", "plugin_inspection_report", "IDEMPOTENT", "NONE", False),
    ("wp.inspect.content_model", "inspect_content_model", "inspection", "R0", ["BRAIN_ONLY", "LOCAL_RUNTIME_READ_ONLY"], "Content model doc vs runtime fields diff", "content_model_diff", "IDEMPOTENT", "NONE", False),
    ("wp.inspect.plugin_state", "inspect_plugin_state", "inspection", "R0", ["LOCAL_RUNTIME_READ_ONLY"], "Installed plugins vs register", "plugin_state_report", "IDEMPOTENT", "NONE", False),
    ("wp.inspect.routes", "inspect_routes", "inspection", "R0", ["LOCAL_RUNTIME_READ_ONLY"], "URL resolution smoke inspection", "route_report", "IDEMPOTENT", "NONE", False),
    ("wp.inspect.templates", "inspect_templates", "inspection", "R0", ["LOCAL_SOURCE"], "Template map coverage audit", "template_coverage_report", "IDEMPOTENT", "NONE", False),
    ("wp.inspect.assets", "inspect_assets", "inspection", "R0", ["LOCAL_SOURCE"], "Asset manifest vs theme files", "asset_audit_report", "IDEMPOTENT", "NONE", False),
    ("wp.inspect.forms", "inspect_forms", "inspection", "R0", ["LOCAL_SOURCE", "LOCAL_RUNTIME_READ_ONLY"], "Forms map vs implementation", "forms_inspection_report", "IDEMPOTENT", "NONE", False),
    ("wp.inspect.editor_configuration", "inspect_editor_configuration", "inspection", "R0", ["BRAIN_ONLY", "LOCAL_SOURCE"], "ACF/editor governance boundaries audit", "editor_audit_report", "IDEMPOTENT", "NONE", False),
    # Planning R1
    ("wp.plan.implementation", "draft_implementation_plan", "planning", "R1", ["BRAIN_ONLY"], "Master implementation plan draft", "implementation_plan", "NON_IDEMPOTENT", "READ_ONLY_ARTIFACTS", True),
    ("wp.plan.theme_architecture", "draft_theme_architecture", "planning", "R1", ["BRAIN_ONLY"], "Theme architecture proposal", "theme_architecture", "NON_IDEMPOTENT", "READ_ONLY_ARTIFACTS", True),
    ("wp.plan.functionality_architecture", "draft_functionality_architecture", "planning", "R1", ["BRAIN_ONLY"], "Functionality plugin architecture proposal", "functionality_architecture", "NON_IDEMPOTENT", "READ_ONLY_ARTIFACTS", True),
    ("wp.plan.content_model", "draft_content_model", "planning", "R1", ["BRAIN_ONLY"], "Content model proposal", "content_model", "NON_IDEMPOTENT", "READ_ONLY_ARTIFACTS", True),
    ("wp.plan.plugin_decisions", "draft_plugin_decision", "planning", "R1", ["BRAIN_ONLY"], "Plugin register proposal", "plugin_register_draft", "NON_IDEMPOTENT", "READ_ONLY_ARTIFACTS", True),
    ("wp.plan.editor_governance", "draft_editor_governance", "planning", "R1", ["BRAIN_ONLY"], "Editor boundaries document draft", "editor_governance", "NON_IDEMPOTENT", "READ_ONLY_ARTIFACTS", True),
    ("wp.plan.migration", "draft_migration_plan", "planning", "R1", ["BRAIN_ONLY"], "Content migration plan draft", "migration_plan", "NON_IDEMPOTENT", "READ_ONLY_ARTIFACTS", True),
    ("wp.plan.validation", "draft_validation_plan", "planning", "R1", ["BRAIN_ONLY"], "Project validation plan draft", "validation_plan", "NON_IDEMPOTENT", "READ_ONLY_ARTIFACTS", True),
    ("wp.plan.rollback", "prepare_rollback", "planning", "R1", ["BRAIN_ONLY"], "Rollback strategy draft (plan phase)", "rollback_plan_draft", "NON_IDEMPOTENT", "READ_ONLY_ARTIFACTS", True),
    # Scaffold R2
    ("wp.scaffold.theme", "scaffold_theme", "scaffold", "R2", ["LOCAL_SOURCE"], "Create theme skeleton from approved plan", "theme_source_tree", "CONDITIONALLY_IDEMPOTENT", "SOURCE_MUTATION", True),
    ("wp.scaffold.functionality_plugin", "scaffold_functionality_plugin", "scaffold", "R2", ["LOCAL_SOURCE"], "Create functionality plugin skeleton", "plugin_source_tree", "CONDITIONALLY_IDEMPOTENT", "SOURCE_MUTATION", True),
    ("wp.scaffold.tests", "scaffold_tests", "scaffold", "R2", ["LOCAL_SOURCE"], "Test harness skeleton", "test_tree", "CONDITIONALLY_IDEMPOTENT", "SOURCE_MUTATION", True),
    # Generation R2
    ("wp.generate.acf_json", "generate_acf_json", "generation", "R2", ["LOCAL_SOURCE"], "Version-controlled ACF field JSON", "acf_json_files", "CONDITIONALLY_IDEMPOTENT", "SOURCE_MUTATION", True),
    ("wp.generate.template", "generate_template", "generation", "R2", ["LOCAL_SOURCE"], "PHP template from template map", "template_file", "CONDITIONALLY_IDEMPOTENT", "SOURCE_MUTATION", True),
    ("wp.generate.template_part", "generate_template_part", "generation", "R2", ["LOCAL_SOURCE"], "Template part from partial map", "template_part_file", "CONDITIONALLY_IDEMPOTENT", "SOURCE_MUTATION", True),
    ("wp.generate.custom_block", "generate_custom_block", "generation", "R2", ["LOCAL_SOURCE"], "Custom block scaffold", "block_source", "CONDITIONALLY_IDEMPOTENT", "SOURCE_MUTATION", True),
    # Change R2
    ("wp.change.apply_approved_source", "apply_approved_source_change", "change", "R2", ["LOCAL_SOURCE"], "Apply scoped approved source edit", "diff_and_build_log", "NON_IDEMPOTENT", "SOURCE_MUTATION", True),
    # Validation R0
    ("wp.validate.php_syntax", "validate_php_syntax", "validation", "R0", ["LOCAL_SOURCE"], "PHP lint all project PHP paths", "php_syntax_report", "IDEMPOTENT", "NONE", False),
    ("wp.validate.wpcs", "validate_wpcs", "validation", "R0", ["LOCAL_SOURCE"], "PHPCS/WPCS scan", "wpcs_report", "IDEMPOTENT", "READ_ONLY_ARTIFACTS", False),
    ("wp.validate.core_checksums", "validate_wordpress_checksums", "validation", "R0", ["LOCAL_RUNTIME_READ_ONLY"], "WordPress core integrity checksums", "checksum_report", "IDEMPOTENT", "NONE", False),
    ("wp.validate.database", "validate_database", "validation", "R0", ["LOCAL_RUNTIME_READ_ONLY"], "Database integrity check", "db_check_report", "IDEMPOTENT", "NONE", False),
    ("wp.validate.routes", "validate_routes", "validation", "R0", ["LOCAL_RUNTIME_READ_ONLY"], "HTTP route validation tests", "route_test_report", "IDEMPOTENT", "READ_ONLY_ARTIFACTS", False),
    ("wp.validate.rendering", "validate_rendering", "validation", "R0", ["LOCAL_RUNTIME_READ_ONLY"], "Render smoke — no fatal errors", "render_report", "IDEMPOTENT", "READ_ONLY_ARTIFACTS", False),
    ("wp.validate.visual_fidelity", "validate_visual_fidelity", "validation", "R0", ["LOCAL_RUNTIME_READ_ONLY"], "Screenshot diff vs approved baseline", "visual_diff_report", "IDEMPOTENT", "READ_ONLY_ARTIFACTS", False),
    ("wp.validate.accessibility", "validate_accessibility", "validation", "R0", ["LOCAL_RUNTIME_READ_ONLY"], "Accessibility scan", "a11y_report", "IDEMPOTENT", "READ_ONLY_ARTIFACTS", False),
    ("wp.validate.security", "validate_security", "validation", "R0", ["LOCAL_SOURCE", "LOCAL_RUNTIME_READ_ONLY"], "Secret scan and capability review", "security_report", "IDEMPOTENT", "READ_ONLY_ARTIFACTS", False),
    ("wp.validate.plugin_risk", "validate_plugin_risk", "validation", "R0", ["BRAIN_ONLY", "LOCAL_RUNTIME_READ_ONLY"], "Plugin provenance and risk check", "plugin_risk_report", "IDEMPOTENT", "READ_ONLY_ARTIFACTS", False),
    # Checkpoint / backup / review R2-R3
    ("wp.backup.create", "create_backup", "backup", "R3", ["LOCAL_RUNTIME_MUTATION"], "DB and files backup before mutation", "backup_manifest", "NON_IDEMPOTENT", "RUNTIME_MUTATION", True),
    ("wp.checkpoint.create", "create_checkpoint", "checkpoint", "R2", ["LOCAL_SOURCE"], "Git checkpoint with manifest", "commit_sha_and_checkpoint_manifest", "NON_IDEMPOTENT", "SOURCE_MUTATION", True),
    ("wp.review.prepare", "prepare_review_package", "review", "R1", ["BRAIN_ONLY"], "Operator review bundle assembly", "review_package", "NON_IDEMPOTENT", "READ_ONLY_ARTIFACTS", True),
    ("wp.rollback.prepare", "prepare_rollback", "rollback", "R2", ["BRAIN_ONLY", "LOCAL_SOURCE"], "Rollback package assembly", "rollback_package", "NON_IDEMPOTENT", "READ_ONLY_ARTIFACTS", True),
]

FAILURE_CODES = [
    ("WP_INPUT_FRONTEND_NOT_APPROVED", "WP_INPUT", "BLOCKER", False, "STOP", "Obtain frontend production pass and FW-06B intake", "gate_a_report"),
    ("WP_INPUT_COMMIT_MISSING", "WP_INPUT", "BLOCKER", False, "STOP", "Record source_commit in handoff manifest", "handoff_manifest"),
    ("WP_INPUT_HANDOFF_INCOMPLETE", "WP_INPUT", "BLOCKER", False, "STOP", "Complete approved frontend input contract fields", "gate_a_report"),
    ("WP_SOURCE_AUTHORITY_AMBIGUOUS", "WP_SOURCE", "BLOCKER", False, "STOP", "Resolve single source-of-truth path", "filesystem_scope_audit"),
    ("WP_SOURCE_OUT_OF_SCOPE", "WP_SOURCE", "BLOCKER", False, "STOP", "Restrict writes to approved allowlist", "changed_files_log"),
    ("WP_RUNTIME_NOT_LOCAL", "WP_RUNTIME", "BLOCKER", False, "STOP", "Use MLI local runtime profile only", "runtime_validation_report"),
    ("WP_RUNTIME_PRODUCTION_DETECTED", "WP_RUNTIME", "BLOCKER", False, "STOP", "Abort — production mutation prohibited", "environment_probe"),
    ("WP_RUNTIME_MANIFEST_MISMATCH", "WP_RUNTIME", "ERROR", True, "STOP", "Reconcile runtime_id with MLI manifest", "manifest_hash"),
    ("WP_DATABASE_CONNECTION_FAILED", "WP_DATABASE", "ERROR", True, "STOP", "Verify MLI MySQL and wp-config indirect access", "db_check_report"),
    ("WP_DATABASE_INTEGRITY_UNCERTAIN", "WP_DATABASE", "BLOCKER", False, "STOP", "Run wp db check; escalate if uncertain", "db_check_report"),
    ("WP_PLUGIN_UNAPPROVED", "WP_PLUGIN", "BLOCKER", False, "STOP", "Add plugin to approved register or remove", "plugin_state_report"),
    ("WP_PLUGIN_NOT_INSTALLED", "WP_PLUGIN", "ERROR", True, "REPORT", "Install per approved plan with operator approval", "plugin_state_report"),
    ("WP_THEME_MODE_NOT_APPROVED", "WP_THEME", "BLOCKER", False, "STOP", "Obtain architecture approval for implementation mode", "mode_decision_doc"),
    ("WP_THEME_STRUCTURE_INVALID", "WP_THEME", "ERROR", False, "STOP", "Fix theme hierarchy per FW-S-03", "theme_inspection_report"),
    ("WP_CONTENT_MODEL_MISMATCH", "WP_CONTENT_MODEL", "ERROR", False, "STOP", "Reconcile model doc with runtime fields", "content_model_diff"),
    ("WP_CONTENT_MODEL_NOT_APPROVED", "WP_CONTENT_MODEL", "BLOCKER", False, "STOP", "Obtain content model approval before apply", "content_model_doc"),
    ("WP_VALIDATION_PHP_SYNTAX_FAIL", "WP_VALIDATION", "ERROR", True, "STOP", "Fix PHP syntax errors", "php_syntax_report"),
    ("WP_VALIDATION_WPCS_FAIL", "WP_VALIDATION", "WARNING", True, "REPORT", "Fix or document waiver per FW-S-07", "wpcs_report"),
    ("WP_VALIDATION_ROUTE_FAIL", "WP_VALIDATION", "ERROR", True, "REPORT", "Fix routing or permalink config", "route_test_report"),
    ("WP_VALIDATION_RENDER_FATAL", "WP_VALIDATION", "BLOCKER", False, "STOP", "Fix fatal render error", "render_report"),
    ("WP_VALIDATION_VISUAL_REGRESSION", "WP_VALIDATION", "WARNING", True, "REPORT", "Review visual diff; re-baseline if approved", "visual_diff_report"),
    ("WP_VALIDATION_SECURITY_FINDING", "WP_SECURITY", "BLOCKER", False, "STOP", "Remediate security finding before continue", "security_report"),
    ("WP_SECURITY_SECRET_DETECTED", "WP_SECURITY", "BLOCKER", False, "STOP", "Remove secret from source; rotate if exposed", "secret_scan_report"),
    ("WP_APPROVAL_REQUIRED", "WP_APPROVAL", "BLOCKER", False, "STOP", "Issue approval token per risk class", "approval_reference"),
    ("WP_APPROVAL_EXPIRED", "WP_APPROVAL", "BLOCKER", False, "STOP", "Re-issue approval token with current scope", "approval_reference"),
    ("WP_APPROVAL_SCOPE_MISMATCH", "WP_APPROVAL", "BLOCKER", False, "STOP", "Match operation to approved_scope", "approval_reference"),
    ("WP_ROLLBACK_UNAVAILABLE", "WP_ROLLBACK", "BLOCKER", False, "STOP", "Create checkpoint or backup before mutation", "rollback_reference"),
    ("WP_ROLLBACK_PARTIAL", "WP_ROLLBACK", "ERROR", False, "ESCALATE", "Manual operator recovery required", "rollback_package"),
    ("WP_ENVIRONMENT_SCOPE_VIOLATION", "WP_ENVIRONMENT", "BLOCKER", False, "STOP", "Restrict to operation environment_scope", "environment_probe"),
    ("WP_ENVIRONMENT_STAGING_NOT_AUTHORIZED", "WP_ENVIRONMENT", "BLOCKER", False, "STOP", "Staging requires future charter", "environment_probe"),
    ("WP_TOOL_BINDING_UNAVAILABLE", "WP_TOOL", "BLOCKER", False, "STOP", "Complete FW-07C harness or bind tool", "tool_capability_matrix"),
    ("WP_TOOL_NOT_PROVEN", "WP_TOOL", "ERROR", False, "STOP", "Validate tool in MLI before execution", "tool_verification_report"),
    ("WP_TOOL_VERSION_MISMATCH", "WP_TOOL", "WARNING", True, "REPORT", "Align with MLI toolchain standard", "tool_version_audit"),
    ("WP_SAFE_UNKNOWN_BLOCKING", "WP_SAFE_UNKNOWN", "BLOCKER", False, "STOP", "Resolve unknown; do not assume", "safe_unknown_log"),
    ("WP_SAFE_UNKNOWN_RUNTIME_STATE", "WP_SAFE_UNKNOWN", "BLOCKER", False, "STOP", "Inspect runtime; do not mutate", "runtime_validation_report"),
    ("WP_SAFE_UNKNOWN_HANDOFF_STATE", "WP_SAFE_UNKNOWN", "BLOCKER", False, "STOP", "Complete intake validation", "gate_a_report"),
]


def build_operation(op_id, legacy, category, risk, env_scope, desc, output_key, idempotency, side_effects, approval_required):
    is_r0 = risk == "R0"
    is_mutation = side_effects in ("SOURCE_MUTATION", "RUNTIME_MUTATION", "DATABASE_MUTATION")
    binding = PROVEN_BINDINGS.get(op_id, {})
    tool_status = "UNBOUND"
    impl_status = "UNBOUND"
    if binding:
        tool_status = "BOUND"
        impl_status = "BOUND_NOT_IMPLEMENTED"
    elif category in ("planning", "review") or risk == "R1":
        impl_status = "DEFINED" if False else "UNBOUND"
    if risk == "R5":
        impl_status = "PRODUCTION_PROHIBITED"

    rollback_required = is_mutation
    rollback_method = "git_revert" if side_effects == "SOURCE_MUTATION" else (
        "restore_backup" if side_effects in ("RUNTIME_MUTATION", "DATABASE_MUTATION") else "not_applicable"
    )

    base_failures = ["WP_SAFE_UNKNOWN_BLOCKING", "WP_ENVIRONMENT_SCOPE_VIOLATION"]
    if is_r0:
        base_failures.extend(["WP_RUNTIME_NOT_LOCAL", "WP_TOOL_BINDING_UNAVAILABLE"])
    if approval_required:
        base_failures.extend(["WP_APPROVAL_REQUIRED", "WP_APPROVAL_SCOPE_MISMATCH"])
    if rollback_required:
        base_failures.append("WP_ROLLBACK_UNAVAILABLE")

    return {
        "operation_id": op_id,
        "legacy_op_id": legacy,
        "version": "1.0.0",
        "title": op_id.replace("wp.", "").replace(".", " ").title(),
        "description": desc,
        "category": category,
        "lifecycle_status": "DEFINED",
        "implementation_status": impl_status if risk != "R5" else "PRODUCTION_PROHIBITED",
        "risk_class": risk,
        "environment_scope": env_scope,
        "production_allowed": False,
        "input_schema": {
            "type": "object",
            "properties": {
                "project_id": {"type": "string"},
                "runtime_id": {"type": "string"},
                "source_commit": {"type": "string"},
                "approval_reference": {"type": "string"},
            },
            "additionalProperties": True,
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "report_type": {"const": output_key},
                "status": {"enum": ["SUCCEEDED", "FAILED", "BLOCKED_SAFE_UNKNOWN"]},
                "evidence_paths": {"type": "array", "items": {"type": "string"}},
            },
        },
        "preconditions": [
            "AG-WP-001 agent registered; runtime NOT required for BRAIN_ONLY ops",
            "environment_scope matches operation allowlist",
            "production_allowed is false",
        ],
        "postconditions": [
            "execution envelope schema-compatible artifact emitted (when harness exists)",
            "audit_evidence paths recorded without secrets",
        ],
        "invariants": [
            "No production mutation",
            "No credential emission in logs",
            "Risk class not escalated without approval",
        ],
        "approval": {
            "required": approval_required,
            "risk_gate": risk,
            "token_required": approval_required and risk in ("R2", "R3", "R4"),
            "pre_authorized_local": is_r0 and not approval_required,
        },
        "approval_evidence": ["approval_id", "approved_scope", "source_commit"] if approval_required else [],
        "tool_binding": {
            "binding_id": binding.get("binding_id", "UNBOUND"),
            "tool_ids": binding.get("tool_ids", []),
            "invocation_class": binding.get("invocation_class", "unbound"),
        },
        "tool_status": tool_status,
        "idempotency": idempotency,
        "side_effects": side_effects,
        "rollback": {
            "required": rollback_required,
            "method": rollback_method,
            "automatic": False,
        },
        "audit_evidence": ["execution_id", "operation_id", "started_at", "status"],
        "success_criteria": [f"Emit {output_key} without BLOCKER failure codes"],
        "failure_codes": base_failures,
        "safe_unknown_behavior": "BLOCK",
        "timeout_policy": {"default_seconds": 120, "max_seconds": 600},
        "retry_policy": {"retryable": is_r0, "max_attempts": 2 if is_r0 else 0},
        "secret_policy": "INDIRECT_CONSUMPTION" if "LOCAL_RUNTIME" in str(env_scope) else "NO_ACCESS",
        "logging_policy": {"sanitize_secrets": True, "redact_paths": ["wp-config.php", "runtime.env", ".env"]},
        "dependencies": [],
        "conflicts": [],
        "allowed_next_operations": [],
    }


def main():
    OPS_DIR.mkdir(parents=True, exist_ok=True)
    BIND_DIR.mkdir(parents=True, exist_ok=True)

    operations = [build_operation(*spec) for spec in OPERATIONS_SPEC]

    registry = {
        "registry_id": "AG-WP-001-OPERATION-REGISTRY-v1",
        "version": "1.0.0",
        "stage": "FW-07B",
        "agent_id": "AG-WP-001",
        "operation_count": len(operations),
        "id_convention": "wp.<category_verb>.<object>",
        "legacy_alias_note": "FW-07A snake_case legacy_op_id preserved per operation",
        "operations": operations,
    }

    with open(OPS_DIR / "operations-v1.json", "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
        f.write("\n")

    for op in operations:
        op_path = OPS_DIR / f"{op['operation_id'].replace('.', '-')}.json"
        with open(op_path, "w", encoding="utf-8") as f:
            json.dump(op, f, indent=2, ensure_ascii=False)
            f.write("\n")

    bindings = {
        "binding_registry_id": "AG-WP-001-TOOL-BINDINGS-v1",
        "version": "1.0.0",
        "stage": "FW-07B",
        "honesty": "Bindings are contract-level; BOUND_NOT_IMPLEMENTED until FW-07C harness",
        "wpilot_status": "NOT_BOUND_HOLD",
        "mcp_status": "NOT_APPROVED",
        "abilities_api_status": "EXPERIMENTAL_NOT_APPROVED",
        "bindings": [
            {
                "operation_id": op_id,
                **{k: v for k, v in data.items() if k != "status"},
                "binding_status": data["status"],
                "implementation_status": "BOUND_NOT_IMPLEMENTED",
                "secret_handling": "INDIRECT_CONSUMPTION",
                "timeout_seconds": 120,
                "retry": {"max_attempts": 2, "retryable": True},
                "audit_artifact": f"reports/ag-wp-001/{op_id.replace('.', '-')}-audit.json",
                "forbidden_environment": ["PRODUCTION_MUTATION", "PRODUCTION_READ_ONLY"],
            }
            for op_id, data in PROVEN_BINDINGS.items()
        ],
    }

    with open(BIND_DIR / "bindings-v1.json", "w", encoding="utf-8") as f:
        json.dump(bindings, f, indent=2, ensure_ascii=False)
        f.write("\n")

    failure_registry = {
        "registry_id": "AG-WP-001-FAILURE-CODE-REGISTRY-v1",
        "version": "1.0.0",
        "stage": "FW-07B",
        "families": [
            "WP_INPUT", "WP_SOURCE", "WP_RUNTIME", "WP_DATABASE", "WP_PLUGIN",
            "WP_THEME", "WP_CONTENT_MODEL", "WP_VALIDATION", "WP_SECURITY",
            "WP_APPROVAL", "WP_ROLLBACK", "WP_ENVIRONMENT", "WP_TOOL", "WP_SAFE_UNKNOWN",
        ],
        "codes": [
            {
                "code": code,
                "family": family,
                "severity": severity,
                "retryable": retryable,
                "stop_rule": stop_rule,
                "operator_action": action,
                "expected_evidence": evidence,
            }
            for code, family, severity, retryable, stop_rule, action, evidence in FAILURE_CODES
        ],
    }

    with open(SCHEMA_DIR / "AG-WP-001-FAILURE-CODE-REGISTRY-v1.json", "w", encoding="utf-8") as f:
        json.dump(failure_registry, f, indent=2, ensure_ascii=False)
        f.write("\n")

    manifest = {
        "manifest_id": "AG-WP-001-OPERATIONS-MANIFEST-v1",
        "operations_file": "operations-v1.json",
        "per_operation_dir": "operations/ag-wp-001/",
        "operation_ids": [o["operation_id"] for o in operations],
        "pilot_safe_core": [
            "wp.inspect.runtime", "wp.inspect.frontend_handoff", "wp.inspect.theme",
            "wp.inspect.functionality_plugin", "wp.inspect.plugin_state", "wp.inspect.routes",
            "wp.inspect.assets", "wp.validate.php_syntax", "wp.validate.core_checksums",
            "wp.validate.database", "wp.validate.routes",
        ],
    }
    with open(OPS_DIR / "manifest-v1.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Generated {len(operations)} operations, {len(PROVEN_BINDINGS)} bindings, {len(FAILURE_CODES)} failure codes")


if __name__ == "__main__":
    main()
