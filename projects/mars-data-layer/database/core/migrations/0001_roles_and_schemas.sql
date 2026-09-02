-- mars_core / app schemas — foundation
-- Prerequisites: database/roles/001_create_roles.sql (mars_migrator, iseo_*, …)
-- Apply order: roles/001 → core/0001 → core/0002 → app_iseo_sales/0001–0004

-- Schemas
CREATE SCHEMA IF NOT EXISTS mars_core;
CREATE SCHEMA IF NOT EXISTS app_iseo_sales;
CREATE SCHEMA IF NOT EXISTS app_seo_content; -- placeholder: no business tables in V1

COMMENT ON SCHEMA mars_core IS 'Platform registry: apps, migrations ledger, workflow releases';
COMMENT ON SCHEMA app_iseo_sales IS 'i-SEO Sales Manager domain data';
COMMENT ON SCHEMA app_seo_content IS 'Placeholder for MetaBOT SEO Content Agent — empty in V1';

-- Lock down PUBLIC
REVOKE ALL ON SCHEMA mars_core FROM PUBLIC;
REVOKE ALL ON SCHEMA app_iseo_sales FROM PUBLIC;
REVOKE ALL ON SCHEMA app_seo_content FROM PUBLIC;

-- Migrator: full DDL path on owned schemas (object ownership follows applying role)
GRANT USAGE, CREATE ON SCHEMA mars_core TO mars_migrator;
GRANT USAGE, CREATE ON SCHEMA app_iseo_sales TO mars_migrator;
GRANT USAGE, CREATE ON SCHEMA app_seo_content TO mars_migrator;

-- Runtime / agent / reader: USAGE only where needed (table grants in app migrations)
GRANT USAGE ON SCHEMA mars_core TO iseo_runtime, iseo_agent, iseo_reader;
GRANT USAGE ON SCHEMA app_iseo_sales TO iseo_runtime, iseo_agent, iseo_reader;

-- Explicit: no iSEO access to content placeholder schema
REVOKE ALL ON SCHEMA app_seo_content FROM iseo_runtime, iseo_agent, iseo_reader;
