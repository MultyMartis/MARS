-- app_iseo_sales grants (V1)
-- Prerequisites: 0001–0003

-- Schema usage
GRANT USAGE ON SCHEMA app_iseo_sales TO iseo_runtime, iseo_agent, iseo_reader;

-- Runtime: DML on domain tables (mutable path)
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA app_iseo_sales TO iseo_runtime;

-- Immutable / append-only: runtime may INSERT+SELECT only (no UPDATE/DELETE)
REVOKE UPDATE, DELETE ON TABLE app_iseo_sales.lead_events FROM iseo_runtime;
REVOKE UPDATE, DELETE ON TABLE app_iseo_sales.audit_logs FROM iseo_runtime;
GRANT SELECT, INSERT ON TABLE app_iseo_sales.lead_events TO iseo_runtime;
GRANT SELECT, INSERT ON TABLE app_iseo_sales.audit_logs TO iseo_runtime;

-- Sequences for identity inserts
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA app_iseo_sales TO iseo_runtime;

-- Agent: SELECT on selected tables; mutating via functions is NOT granted
-- (EXECUTE limited in 0003 to get_lead / list_pending_leads only)
GRANT SELECT ON TABLE
  app_iseo_sales.leads,
  app_iseo_sales.lead_events,
  app_iseo_sales.access_rules,
  app_iseo_sales.config
TO iseo_agent;

-- Reader: SELECT only on main domain tables
GRANT SELECT ON ALL TABLES IN SCHEMA app_iseo_sales TO iseo_reader;

-- Ensure placeholder content schema remains inaccessible to iSEO roles
REVOKE ALL ON SCHEMA app_seo_content FROM iseo_runtime, iseo_agent, iseo_reader;

-- Default privileges for future tables created by migrator (best-effort)
ALTER DEFAULT PRIVILEGES IN SCHEMA app_iseo_sales
  GRANT SELECT, INSERT, UPDATE ON TABLES TO iseo_runtime;
ALTER DEFAULT PRIVILEGES IN SCHEMA app_iseo_sales
  GRANT SELECT ON TABLES TO iseo_reader;
ALTER DEFAULT PRIVILEGES IN SCHEMA app_iseo_sales
  GRANT USAGE, SELECT ON SEQUENCES TO iseo_runtime;

INSERT INTO mars_core.schema_migrations (schema_name, version, checksum)
VALUES ('app_iseo_sales', '0004_grants', NULL)
ON CONFLICT DO NOTHING;
