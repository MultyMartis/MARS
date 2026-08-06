# Adapter Result Contract

Fields: adapter_run_id, source_contract_version, source_run_id, source_observed_at, source_status, client_ops_status, event_id, source_contract_fingerprint, validation_result, redaction_result, producer_build_result, transport_mode, network_calls, final_state, safe_unknowns (+ sanitized metrics / message_preview).

Never includes raw source object.
