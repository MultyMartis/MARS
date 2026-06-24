# AG-WP-001 — Tool Binding Contract v1

**Document type:** Tool binding contract  
**Version:** v1  
**Stage:** FW-07B  
**Date:** 2026-06-24

**Schema:** [schemas/AG-WP-001-TOOL-BINDING-SCHEMA-v1.json](../schemas/AG-WP-001-TOOL-BINDING-SCHEMA-v1.json)  
**Machine-readable bindings:** [bindings/ag-wp-001/bindings-v1.json](../bindings/ag-wp-001/bindings-v1.json)

**Honesty:** A binding document entry is **not** implementation. `BOUND_NOT_IMPLEMENTED` until FW-07C harness proves execution.

---

## Required binding fields

Every binding must specify:

| Field | Requirement |
|-------|-------------|
| `operation_id` | Canonical `wp.*` ID |
| `tool_id` / `tool_ids` | Registered FW or MLI tool IDs |
| `binding_version` | Semver of binding contract |
| `invocation_class` | Command family (read-only CLI, phpcs, git selective, etc.) |
| `working_directory_policy` | Brain vs runtime root |
| `input_transformation` | Normalization rules |
| `output_normalization` | Report schema mapping |
| `allowed_files` | Allowlist paths |
| `forbidden_files` | wp-config, credentials, core |
| `allowed_environment` | From operation `environment_scope` |
| `forbidden_environment` | Production scopes always |
| `preflight` | Checks before invoke |
| `execution` | Approved command templates only |
| `post_validation` | Evidence checks |
| `rollback` | Method or N/A |
| `secret_handling` | Default `INDIRECT_CONSUMPTION` for runtime tools |
| `timeout` | Per operation policy |
| `retry` | Per operation policy |
| `audit_artifact` | Path pattern for evidence |

---

## Binding status semantics

| Status | Meaning |
|--------|---------|
| `UNBOUND` | No tool mapping |
| `BOUND` | Contract mapping exists |
| `BOUND_NOT_IMPLEMENTED` | Mapping exists; harness not proven |
| `PROVEN` | FW-07C+ executed with evidence |
| `HOLD` | Explicitly blocked (WPilot) |
| `NOT_APPROVED` | MCP/Abilities |

---

## Proven binding candidates (contract only)

| operation_id | tool_ids | invocation_class | binding_status |
|--------------|----------|------------------|----------------|
| `wp.inspect.runtime` | MLI-TOOL-007, MLI-TOOL-015, HTTP-PROBE | read_only_cli_and_http | BOUND_NOT_IMPLEMENTED |
| `wp.inspect.theme` | MLI-TOOL-007 | filesystem_and_wp_cli | BOUND_NOT_IMPLEMENTED |
| `wp.inspect.plugin_state` | MLI-TOOL-007 | wp_cli_read_only | BOUND_NOT_IMPLEMENTED |
| `wp.inspect.routes` | MLI-TOOL-007, MLI-TOOL-014 | wp_cli_and_http | BOUND_NOT_IMPLEMENTED |
| `wp.validate.php_syntax` | MLI-TOOL-004 | php_cli_lint | BOUND_NOT_IMPLEMENTED |
| `wp.validate.core_checksums` | MLI-TOOL-007 | wp_cli_read_only | BOUND_NOT_IMPLEMENTED |
| `wp.validate.database` | MLI-TOOL-007, MLI-TOOL-005 | wp_cli_and_db_check | BOUND_NOT_IMPLEMENTED |
| `wp.validate.routes` | MLI-TOOL-014 | http_or_playwright | BOUND_NOT_IMPLEMENTED |
| `wp.validate.wpcs` | MLI-TOOL-008, MLI-TOOL-009 | phpcs_scan | BOUND_NOT_IMPLEMENTED |
| `wp.checkpoint.create` | MLI-TOOL-011 | git_selective_commit | BOUND_NOT_IMPLEMENTED |

**No passwords or credentials in binding examples.**

---

## Forbidden binding patterns

- Unrestricted Cursor shell for source mutation
- Arbitrary user-provided SQL or shell text
- Production WP-CLI or SSH
- Fake MCP / Abilities / WPilot runtime adapters

---

*Tool binding contract v1.*
