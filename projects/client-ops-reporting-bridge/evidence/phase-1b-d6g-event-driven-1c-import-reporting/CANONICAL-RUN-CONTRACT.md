# Canonical Run Contract

Schema: `1b-d6g.1`

Fields: schema_version, site_id, run_id, trigger_source (SCHEDULED|ADMIN_MANUAL), requested_at, started_at, completed_at, current_phase, final_status, inventories, phase results, sanitized_error_summary, log_reference, terminal_result_path, report_dispatch_status.

Final statuses: SUCCESS | ATTENTION_OFFERS_INPUT_MISSING | ATTENTION_COMPLETED_WITH_WARNINGS | FAILED

Source: `mars_1c_import_run_contract.php`
