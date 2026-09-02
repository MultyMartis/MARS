-- app_iseo_sales indexes (V1)
-- Prerequisites: 0001_base_tables.sql

CREATE INDEX idx_inbound_events_processing_received
  ON app_iseo_sales.inbound_events (processing_status, received_at);

CREATE INDEX idx_inbound_events_lead_id
  ON app_iseo_sales.inbound_events (lead_id);

CREATE INDEX idx_leads_manager_status_updated
  ON app_iseo_sales.leads (manager_status, updated_at);

CREATE INDEX idx_leads_created_at
  ON app_iseo_sales.leads (created_at);

CREATE INDEX idx_lead_events_lead_occurred
  ON app_iseo_sales.lead_events (lead_id, occurred_at);

CREATE INDEX idx_deliveries_status_available_pending_retry
  ON app_iseo_sales.deliveries (status, available_at)
  WHERE status IN ('pending', 'retry');

CREATE INDEX idx_deliveries_lead_id
  ON app_iseo_sales.deliveries (lead_id);

CREATE INDEX idx_jobs_status_available
  ON app_iseo_sales.jobs (status, available_at);

CREATE INDEX idx_jobs_job_type_status
  ON app_iseo_sales.jobs (job_type, status);

CREATE INDEX idx_errors_occurred_at
  ON app_iseo_sales.errors (occurred_at);

CREATE INDEX idx_access_rules_active_role
  ON app_iseo_sales.access_rules (is_active, role);

CREATE INDEX idx_audit_logs_entity_occurred
  ON app_iseo_sales.audit_logs (entity_type, entity_id, occurred_at);

INSERT INTO mars_core.schema_migrations (schema_name, version, checksum)
VALUES ('app_iseo_sales', '0002_indexes', NULL)
ON CONFLICT DO NOTHING;
