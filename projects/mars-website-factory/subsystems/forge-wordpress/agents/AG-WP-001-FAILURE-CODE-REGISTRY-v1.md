# AG-WP-001 — Failure Code Registry v1

**Document type:** Failure code registry  
**Version:** v1  
**Stage:** FW-07B  
**Date:** 2026-06-24  
**Machine-readable:** [schemas/AG-WP-001-FAILURE-CODE-REGISTRY-v1.json](../schemas/AG-WP-001-FAILURE-CODE-REGISTRY-v1.json)

---

## Families

`WP_INPUT_*` · `WP_SOURCE_*` · `WP_RUNTIME_*` · `WP_DATABASE_*` · `WP_PLUGIN_*` · `WP_THEME_*` · `WP_CONTENT_MODEL_*` · `WP_VALIDATION_*` · `WP_SECURITY_*` · `WP_APPROVAL_*` · `WP_ROLLBACK_*` · `WP_ENVIRONMENT_*` · `WP_TOOL_*` · `WP_SAFE_UNKNOWN_*`

---

## Registry

| Code | Severity | Retryable | Stop rule | Operator action | Expected evidence |
|------|----------|-----------|-----------|-----------------|-------------------|
| `WP_INPUT_FRONTEND_NOT_APPROVED` | BLOCKER | no | STOP | Obtain frontend production pass and FW-06B intake | `gate_a_report` |
| `WP_INPUT_COMMIT_MISSING` | BLOCKER | no | STOP | Record `source_commit` in handoff manifest | `handoff_manifest` |
| `WP_INPUT_HANDOFF_INCOMPLETE` | BLOCKER | no | STOP | Complete approved frontend input contract fields | `gate_a_report` |
| `WP_SOURCE_AUTHORITY_AMBIGUOUS` | BLOCKER | no | STOP | Resolve single source-of-truth path | `filesystem_scope_audit` |
| `WP_SOURCE_OUT_OF_SCOPE` | BLOCKER | no | STOP | Restrict writes to approved allowlist | `changed_files_log` |
| `WP_RUNTIME_NOT_LOCAL` | BLOCKER | no | STOP | Use MLI local runtime profile only | `runtime_validation_report` |
| `WP_RUNTIME_PRODUCTION_DETECTED` | BLOCKER | no | STOP | Abort — production mutation prohibited | `environment_probe` |
| `WP_RUNTIME_MANIFEST_MISMATCH` | ERROR | yes | STOP | Reconcile `runtime_id` with MLI manifest | `manifest_hash` |
| `WP_DATABASE_CONNECTION_FAILED` | ERROR | yes | STOP | Verify MLI MySQL; indirect wp-config only | `db_check_report` |
| `WP_DATABASE_INTEGRITY_UNCERTAIN` | BLOCKER | no | STOP | Run `wp db check`; escalate if uncertain | `db_check_report` |
| `WP_PLUGIN_UNAPPROVED` | BLOCKER | no | STOP | Add plugin to approved register or remove | `plugin_state_report` |
| `WP_PLUGIN_NOT_INSTALLED` | ERROR | yes | REPORT | Install per approved plan with operator approval | `plugin_state_report` |
| `WP_THEME_MODE_NOT_APPROVED` | BLOCKER | no | STOP | Obtain architecture approval for implementation mode | `mode_decision_doc` |
| `WP_THEME_STRUCTURE_INVALID` | ERROR | no | STOP | Fix theme hierarchy per FW-S-03 | `theme_inspection_report` |
| `WP_CONTENT_MODEL_MISMATCH` | ERROR | no | STOP | Reconcile model doc with runtime fields | `content_model_diff` |
| `WP_CONTENT_MODEL_NOT_APPROVED` | BLOCKER | no | STOP | Obtain content model approval before apply | `content_model_doc` |
| `WP_VALIDATION_PHP_SYNTAX_FAIL` | ERROR | yes | STOP | Fix PHP syntax errors | `php_syntax_report` |
| `WP_VALIDATION_WPCS_FAIL` | WARNING | yes | REPORT | Fix or document waiver per FW-S-07 | `wpcs_report` |
| `WP_VALIDATION_ROUTE_FAIL` | ERROR | yes | REPORT | Fix routing or permalink config | `route_test_report` |
| `WP_VALIDATION_RENDER_FATAL` | BLOCKER | no | STOP | Fix fatal render error | `render_report` |
| `WP_VALIDATION_VISUAL_REGRESSION` | WARNING | yes | REPORT | Review visual diff; re-baseline if approved | `visual_diff_report` |
| `WP_VALIDATION_SECURITY_FINDING` | BLOCKER | no | STOP | Remediate security finding | `security_report` |
| `WP_SECURITY_SECRET_DETECTED` | BLOCKER | no | STOP | Remove secret from source; rotate if exposed | `secret_scan_report` |
| `WP_APPROVAL_REQUIRED` | BLOCKER | no | STOP | Issue approval token per risk class | `approval_reference` |
| `WP_APPROVAL_EXPIRED` | BLOCKER | no | STOP | Re-issue approval token with current scope | `approval_reference` |
| `WP_APPROVAL_SCOPE_MISMATCH` | BLOCKER | no | STOP | Match operation to `approved_scope` | `approval_reference` |
| `WP_ROLLBACK_UNAVAILABLE` | BLOCKER | no | STOP | Create checkpoint or backup before mutation | `rollback_reference` |
| `WP_ROLLBACK_PARTIAL` | ERROR | no | ESCALATE | Manual operator recovery required | `rollback_package` |
| `WP_ENVIRONMENT_SCOPE_VIOLATION` | BLOCKER | no | STOP | Restrict to operation `environment_scope` | `environment_probe` |
| `WP_ENVIRONMENT_STAGING_NOT_AUTHORIZED` | BLOCKER | no | STOP | Staging requires future charter | `environment_probe` |
| `WP_TOOL_BINDING_UNAVAILABLE` | BLOCKER | no | STOP | Complete FW-07C harness or bind tool | `tool_capability_matrix` |
| `WP_TOOL_NOT_PROVEN` | ERROR | no | STOP | Validate tool in MLI before execution | `tool_verification_report` |
| `WP_TOOL_VERSION_MISMATCH` | WARNING | yes | REPORT | Align with MLI toolchain standard | `tool_version_audit` |
| `WP_SAFE_UNKNOWN_BLOCKING` | BLOCKER | no | STOP | Resolve unknown; do not assume | `safe_unknown_log` |
| `WP_SAFE_UNKNOWN_RUNTIME_STATE` | BLOCKER | no | STOP | Inspect runtime; do not mutate | `runtime_validation_report` |
| `WP_SAFE_UNKNOWN_HANDOFF_STATE` | BLOCKER | no | STOP | Complete intake validation | `gate_a_report` |

**Count:** 36 codes across 14 families.

---

*Failure code registry v1 — contract only.*
