# AG-WP-001 — Execution Envelope Contract v1

**Document type:** Execution envelope contract  
**Version:** v1  
**Stage:** FW-07B  
**Date:** 2026-06-24

**Schema:** [schemas/AG-WP-001-EXECUTION-ENVELOPE-SCHEMA-v1.json](../schemas/AG-WP-001-EXECUTION-ENVELOPE-SCHEMA-v1.json)  
**Example:** [fixtures/ag-wp-001/example-execution-envelope.json](../fixtures/ag-wp-001/example-execution-envelope.json)

**Honesty:** Envelopes are **not** emitted by AG-WP-001 runtime (runtime NOT ACTIVE). Schema and examples only.

---

## Mandatory envelope fields

`execution_id` · `operation_id` · `operation_version` · `agent_id` · `project_id` · `requested_by` · `approval_reference` · `environment` · `runtime_id` · `source_commit` · `started_at` · `completed_at` · `status` · `normalized_inputs` · `normalized_outputs` · `changed_files` · `runtime_mutations` · `database_mutations` · `validation_results` · `audit_artifacts` · `failure_codes` · `safe_unknown` · `rollback_reference` · `next_allowed_operations`

---

## Status values

`PLANNED` · `PREFLIGHT_FAILED` · `APPROVAL_REQUIRED` · `RUNNING` · `SUCCEEDED` · `SUCCEEDED_WITH_LIMITATIONS` · `FAILED` · `ROLLED_BACK` · `BLOCKED_SAFE_UNKNOWN`

---

## Rules

- No secrets in `normalized_inputs` / `normalized_outputs`
- `changed_files` must respect filesystem scope contract
- `failure_codes` must reference failure registry
- `safe_unknown` non-empty → status `BLOCKED_SAFE_UNKNOWN`

---

*Execution envelope contract v1.*
