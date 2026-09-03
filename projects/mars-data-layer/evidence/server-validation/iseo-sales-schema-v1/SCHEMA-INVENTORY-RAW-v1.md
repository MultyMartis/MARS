# SCHEMA-INVENTORY-RAW-v1

```
     schema     |                    object                     | kind |     owner     
----------------+-----------------------------------------------+------+---------------
 app_iseo_sales | access_rules_id_seq                           | S    | mars_migrator
 app_iseo_sales | audit_logs_id_seq                             | S    | mars_migrator
 app_iseo_sales | config_id_seq                                 | S    | mars_migrator
 app_iseo_sales | deliveries_id_seq                             | S    | mars_migrator
 app_iseo_sales | errors_id_seq                                 | S    | mars_migrator
 app_iseo_sales | idempotency_keys_id_seq                       | S    | mars_migrator
 app_iseo_sales | inbound_events_id_seq                         | S    | mars_migrator
 app_iseo_sales | jobs_id_seq                                   | S    | mars_migrator
 app_iseo_sales | lead_dedup_keys_id_seq                        | S    | mars_migrator
 app_iseo_sales | lead_events_id_seq                            | S    | mars_migrator
 app_iseo_sales | leads_id_seq                                  | S    | mars_migrator
 app_iseo_sales | idx_access_rules_active_role                  | i    | mars_migrator
 app_iseo_sales | idx_audit_logs_entity_occurred                | i    | mars_migrator
 app_iseo_sales | idx_deliveries_lead_id                        | i    | mars_migrator
 app_iseo_sales | idx_deliveries_status_available_pending_retry | i    | mars_migrator
 app_iseo_sales | idx_errors_occurred_at                        | i    | mars_migrator
 app_iseo_sales | idx_inbound_events_lead_id                    | i    | mars_migrator
 app_iseo_sales | idx_inbound_events_processing_received        | i    | mars_migrator
 app_iseo_sales | idx_jobs_job_type_status                      | i    | mars_migrator
 app_iseo_sales | idx_jobs_status_available                     | i    | mars_migrator
 app_iseo_sales | idx_lead_events_lead_occurred                 | i    | mars_migrator
 app_iseo_sales | idx_leads_created_at                          | i    | mars_migrator
 app_iseo_sales | idx_leads_manager_status_updated              | i    | mars_migrator
 app_iseo_sales | pk_access_rules                               | i    | mars_migrator
 app_iseo_sales | pk_audit_logs                                 | i    | mars_migrator
 app_iseo_sales | pk_config                                     | i    | mars_migrator
 app_iseo_sales | pk_deliveries                                 | i    | mars_migrator
 app_iseo_sales | pk_errors                                     | i    | mars_migrator
 app_iseo_sales | pk_idempotency_keys                           | i    | mars_migrator
 app_iseo_sales | pk_inbound_events                             | i    | mars_migrator
 app_iseo_sales | pk_jobs                                       | i    | mars_migrator
 app_iseo_sales | pk_lead_dedup_keys                            | i    | mars_migrator
 app_iseo_sales | pk_lead_events                                | i    | mars_migrator
 app_iseo_sales | pk_leads                                      | i    | mars_migrator
 app_iseo_sales | uq_access_rules_principal_key                 | i    | mars_migrator
 app_iseo_sales | uq_config_key                                 | i    | mars_migrator
 app_iseo_sales | uq_deliveries_delivery_id                     | i    | mars_migrator
 app_iseo_sales | uq_deliveries_idempotency_key                 | i    | mars_migrator
 app_iseo_sales | uq_idempotency_keys_scope_key                 | i    | mars_migrator
 app_iseo_sales | uq_inbound_events_source                      | i    | mars_migrator
 app_iseo_sales | uq_jobs_dedupe_key                            | i    | mars_migrator
 app_iseo_sales | uq_lead_dedup_keys_dedup_key                  | i    | mars_migrator
 app_iseo_sales | uq_lead_events_event_id                       | i    | mars_migrator
 app_iseo_sales | uq_leads_lead_id                              | i    | mars_migrator
 app_iseo_sales | uq_leads_source_message_id                    | i    | mars_migrator
 app_iseo_sales | access_rules                                  | r    | mars_migrator
 app_iseo_sales | audit_logs                                    | r    | mars_migrator
 app_iseo_sales | config                                        | r    | mars_migrator
 app_iseo_sales | deliveries                                    | r    | mars_migrator
 app_iseo_sales | errors                                        | r    | mars_migrator
 app_iseo_sales | idempotency_keys                              | r    | mars_migrator
 app_iseo_sales | inbound_events                                | r    | mars_migrator
 app_iseo_sales | jobs                                          | r    | mars_migrator
 app_iseo_sales | lead_dedup_keys                               | r    | mars_migrator
 app_iseo_sales | lead_events                                   | r    | mars_migrator
 app_iseo_sales | leads                                         | r    | mars_migrator
 mars_core      | apps_id_seq                                   | S    | mars_migrator
 mars_core      | data_contract_versions_id_seq                 | S    | mars_migrator
 mars_core      | workflow_releases_id_seq                      | S    | mars_migrator
 mars_core      | idx_workflow_releases_app_status              | i    | mars_migrator
 mars_core      | pk_apps                                       | i    | mars_migrator
 mars_core      | pk_data_contract_versions                     | i    | mars_migrator
 mars_core      | pk_schema_migrations                          | i    | mars_migrator
 mars_core      | pk_workflow_releases                          | i    | mars_migrator
 mars_core      | uq_apps_app_key                               | i    | mars_migrator
 mars_core      | uq_apps_schema_name                           | i    | mars_migrator
 mars_core      | uq_data_contract_versions_app_key_ver         | i    | mars_migrator
 mars_core      | uq_workflow_releases_one_active_per_family    | i    | mars_migrator
 mars_core      | apps                                          | r    | mars_migrator
 mars_core      | data_contract_versions                        | r    | mars_migrator
 mars_core      | schema_migrations                             | r    | mars_migrator
 mars_core      | workflow_releases                             | r    | mars_migrator
(72 rows)

    nspname     |             proname             |     owner     
----------------+---------------------------------+---------------
 app_iseo_sales | change_lead_status              | mars_migrator
 app_iseo_sales | claim_jobs                      | mars_migrator
 app_iseo_sales | enqueue_delivery                | mars_migrator
 app_iseo_sales | enqueue_job                     | mars_migrator
 app_iseo_sales | fn_is_allowed_status_transition | mars_migrator
 app_iseo_sales | get_lead                        | mars_migrator
 app_iseo_sales | list_pending_leads              | mars_migrator
 app_iseo_sales | register_inbound_event          | mars_migrator
 app_iseo_sales | upsert_lead                     | mars_migrator
(9 rows)

            table_name            |                   conname                    | contype 
----------------------------------+----------------------------------------------+---------
 mars_core.schema_migrations      | pk_schema_migrations                         | p
 mars_core.schema_migrations      | schema_migrations_applied_at_not_null        | n
 mars_core.schema_migrations      | schema_migrations_schema_name_not_null       | n
 mars_core.schema_migrations      | schema_migrations_version_not_null           | n
 mars_core.apps                   | apps_app_key_not_null                        | n
 mars_core.apps                   | apps_created_at_not_null                     | n
 mars_core.apps                   | apps_display_name_not_null                   | n
 mars_core.apps                   | apps_id_not_null                             | n
 mars_core.apps                   | apps_metadata_not_null                       | n
 mars_core.apps                   | apps_schema_name_not_null                    | n
 mars_core.apps                   | apps_status_not_null                         | n
 mars_core.apps                   | apps_updated_at_not_null                     | n
 mars_core.apps                   | ck_apps_status                               | c
 mars_core.apps                   | pk_apps                                      | p
 mars_core.apps                   | uq_apps_app_key                              | u
 mars_core.apps                   | uq_apps_schema_name                          | u
 mars_core.data_contract_versions | ck_data_contract_versions_status             | c
 mars_core.data_contract_versions | data_contract_versions_app_id_not_null       | n
 mars_core.data_contract_versions | data_contract_versions_contract_key_not_null | n
 mars_core.data_contract_versions | data_contract_versions_id_not_null           | n
 mars_core.data_contract_versions | data_contract_versions_status_not_null       | n
 mars_core.data_contract_versions | data_contract_versions_version_not_null      | n
 mars_core.data_contract_versions | fk_data_contract_versions_app                | f
 mars_core.data_contract_versions | pk_data_contract_versions                    | p
 mars_core.data_contract_versions | uq_data_contract_versions_app_key_ver        | u
 mars_core.workflow_releases      | ck_workflow_releases_status                  | c
 mars_core.workflow_releases      | fk_workflow_releases_app                     | f
 mars_core.workflow_releases      | pk_workflow_releases                         | p
 mars_core.workflow_releases      | workflow_releases_app_id_not_null            | n
 mars_core.workflow_releases      | workflow_releases_created_at_not_null        | n
 mars_core.workflow_releases      | workflow_releases_id_not_null                | n
 mars_core.workflow_releases      | workflow_releases_metadata_not_null          | n
 mars_core.workflow_releases      | workflow_releases_release_version_not_null   | n
 mars_core.workflow_releases      | workflow_releases_status_not_null            | n
 mars_core.workflow_releases      | workflow_releases_updated_at_not_null        | n
 mars_core.workflow_releases      | workflow_releases_workflow_family_not_null   | n
 app_iseo_sales.inbound_events    | ck_inbound_events_processing_status          | c
 app_iseo_sales.inbound_events    | inbound_events_created_at_not_null           | n
 app_iseo_sales.inbound_events    | inbound_events_first_seen_at_not_null        | n
 app_iseo_sales.inbound_events    | inbound_events_id_not_null                   | n
 app_iseo_sales.inbound_events    | inbound_events_last_seen_at_not_null         | n
 app_iseo_sales.inbound_events    | inbound_events_processing_attempts_not_null  | n
 app_iseo_sales.inbound_events    | inbound_events_processing_status_not_null    | n
 app_iseo_sales.inbound_events    | inbound_events_raw_payload_not_null          | n
 app_iseo_sales.inbound_events    | inbound_events_source_id_not_null            | n
 app_iseo_sales.inbound_events    | inbound_events_source_system_not_null        | n
 app_iseo_sales.inbound_events    | inbound_events_updated_at_not_null           | n
 app_iseo_sales.inbound_events    | pk_inbound_events                            | p
 app_iseo_sales.inbound_events    | uq_inbound_events_source                     | u
 app_iseo_sales.leads             | ck_leads_contact_type                        | c
 app_iseo_sales.leads             | ck_leads_duplicate_status                    | c
 app_iseo_sales.leads             | ck_leads_manager_status                      | c
 app_iseo_sales.leads             | fk_leads_inbound_event                       | f
 app_iseo_sales.leads             | leads_created_at_not_null                    | n
 app_iseo_sales.leads             | leads_form_metadata_not_null                 | n
 app_iseo_sales.leads             | leads_id_not_null                            | n
 app_iseo_sales.leads             | leads_lead_id_not_null                       | n
 app_iseo_sales.leads             | leads_manager_status_not_null                | n
 app_iseo_sales.leads             | leads_updated_at_not_null                    | n
 app_iseo_sales.leads             | leads_version_not_null                       | n
 app_iseo_sales.leads             | pk_leads                                     | p
 app_iseo_sales.leads             | uq_leads_lead_id                             | u
 app_iseo_sales.lead_dedup_keys   | ck_lead_dedup_keys_key_type                  | c
 app_iseo_sales.lead_dedup_keys   | fk_lead_dedup_keys_lead                      | f
 app_iseo_sales.lead_dedup_keys   | lead_dedup_keys_created_at_not_null          | n
 app_iseo_sales.lead_dedup_keys   | lead_dedup_keys_dedup_key_not_null           | n
 app_iseo_sales.lead_dedup_keys   | lead_dedup_keys_id_not_null                  | n
 app_iseo_sales.lead_dedup_keys   | lead_dedup_keys_key_type_not_null            | n
 app_iseo_sales.lead_dedup_keys   | lead_dedup_keys_lead_id_not_null             | n
 app_iseo_sales.lead_dedup_keys   | pk_lead_dedup_keys                           | p
 app_iseo_sales.lead_dedup_keys   | uq_lead_dedup_keys_dedup_key                 | u
 app_iseo_sales.lead_events       | ck_lead_events_actor_type                    | c
 app_iseo_sales.lead_events       | fk_lead_events_lead                          | f
 app_iseo_sales.lead_events       | lead_events_created_at_not_null              | n
 app_iseo_sales.lead_events       | lead_events_event_type_not_null              | n
 app_iseo_sales.lead_events       | lead_events_id_not_null                      | n
 app_iseo_sales.lead_events       | lead_events_lead_id_not_null                 | n
 app_iseo_sales.lead_events       | lead_events_occurred_at_not_null             | n
 app_iseo_sales.lead_events       | lead_events_payload_not_null                 | n
 app_iseo_sales.lead_events       | pk_lead_events                               | p
 app_iseo_sales.lead_events       | uq_lead_events_event_id                      | u
 app_iseo_sales.access_rules      | access_rules_created_at_not_null             | n
 app_iseo_sales.access_rules      | access_rules_id_not_null                     | n
 app_iseo_sales.access_rules      | access_rules_is_active_not_null              | n
 app_iseo_sales.access_rules      | access_rules_principal_key_not_null          | n
 app_iseo_sales.access_rules      | access_rules_receives_cards_not_null         | n
 app_iseo_sales.access_rules      | access_rules_receives_reminders_not_null     | n
 app_iseo_sales.access_rules      | access_rules_role_not_null                   | n
 app_iseo_sales.access_rules      | access_rules_updated_at_not_null             | n
 app_iseo_sales.access_rules      | ck_access_rules_role                         | c
 app_iseo_sales.access_rules      | pk_access_rules                              | p
 app_iseo_sales.access_rules      | uq_access_rules_principal_key                | u
 app_iseo_sales.deliveries        | ck_deliveries_status                         | c
 app_iseo_sales.deliveries        | deliveries_attempts_not_null                 | n
 app_iseo_sales.deliveries        | deliveries_available_at_not_null             | n
 app_iseo_sales.deliveries        | deliveries_channel_not_null                  | n
 app_iseo_sales.deliveries        | deliveries_created_at_not_null               | n
 app_iseo_sales.deliveries        | deliveries_delivery_type_not_null            | n
 app_iseo_sales.deliveries        | deliveries_id_not_null                       | n
 app_iseo_sales.deliveries        | deliveries_max_attempts_not_null             | n
 app_iseo_sales.deliveries        | deliveries_payload_not_null                  | n
 app_iseo_sales.deliveries        | deliveries_status_not_null                   | n
 app_iseo_sales.deliveries        | deliveries_updated_at_not_null               | n
 app_iseo_sales.deliveries        | fk_deliveries_last_error                     | f
 app_iseo_sales.deliveries        | fk_deliveries_lead                           | f
 app_iseo_sales.deliveries        | pk_deliveries                                | p
 app_iseo_sales.deliveries        | uq_deliveries_delivery_id                    | u
 app_iseo_sales.deliveries        | uq_deliveries_idempotency_key                | u
 app_iseo_sales.jobs              | ck_jobs_status                               | c
 app_iseo_sales.jobs              | jobs_attempts_not_null                       | n
 app_iseo_sales.jobs              | jobs_available_at_not_null                   | n
 app_iseo_sales.jobs              | jobs_created_at_not_null                     | n
 app_iseo_sales.jobs              | jobs_id_not_null                             | n
 app_iseo_sales.jobs              | jobs_job_type_not_null                       | n
 app_iseo_sales.jobs              | jobs_max_attempts_not_null                   | n
 app_iseo_sales.jobs              | jobs_payload_not_null                        | n
 app_iseo_sales.jobs              | jobs_priority_not_null                       | n
 app_iseo_sales.jobs              | jobs_status_not_null                         | n
 app_iseo_sales.jobs              | jobs_updated_at_not_null                     | n
 app_iseo_sales.jobs              | pk_jobs                                      | p
 app_iseo_sales.idempotency_keys  | idempotency_keys_created_at_not_null         | n
 app_iseo_sales.idempotency_keys  | idempotency_keys_id_not_null                 | n
 app_iseo_sales.idempotency_keys  | idempotency_keys_idempotency_key_not_null    | n
 app_iseo_sales.idempotency_keys  | idempotency_keys_scope_not_null              | n
 app_iseo_sales.idempotency_keys  | pk_idempotency_keys                          | p
 app_iseo_sales.idempotency_keys  | uq_idempotency_keys_scope_key                | u
 app_iseo_sales.errors            | errors_context_not_null                      | n
 app_iseo_sales.errors            | errors_created_at_not_null                   | n
 app_iseo_sales.errors            | errors_id_not_null                           | n
 app_iseo_sales.errors            | errors_occurred_at_not_null                  | n
 app_iseo_sales.errors            | errors_resolved_not_null                     | n
 app_iseo_sales.errors            | errors_retryable_not_null                    | n
 app_iseo_sales.errors            | pk_errors                                    | p
 app_iseo_sales.audit_logs        | audit_logs_action_not_null                   | n
 app_iseo_sales.audit_logs        | audit_logs_created_at_not_null               | n
 app_iseo_sales.audit_logs        | audit_logs_detail_not_null                   | n
 app_iseo_sales.audit_logs        | audit_logs_id_not_null                       | n
 app_iseo_sales.audit_logs        | audit_logs_occurred_at_not_null              | n
 app_iseo_sales.audit_logs        | ck_audit_logs_result                         | c
 app_iseo_sales.audit_logs        | pk_audit_logs                                | p
 app_iseo_sales.config            | ck_config_value_type                         | c
 app_iseo_sales.config            | config_id_not_null                           | n
 app_iseo_sales.config            | config_is_secretish_not_null                 | n
 app_iseo_sales.config            | config_key_not_null                          | n
 app_iseo_sales.config            | config_updated_at_not_null                   | n
 app_iseo_sales.config            | config_value_type_not_null                   | n
 app_iseo_sales.config            | pk_config                                    | p
 app_iseo_sales.config            | uq_config_key                                | u
(148 rows)

  schema_name   |     version      
```
