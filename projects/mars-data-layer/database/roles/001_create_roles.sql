-- MARS Bot Data Platform — role stubs (no passwords)
-- Apply before core/app migrations when roles do not yet exist.
-- Passwords / LOGIN are set out-of-band by Server Ops. Do NOT store secrets here.

-- Idempotent CREATE ROLE pattern (PostgreSQL has no CREATE ROLE IF NOT EXISTS).
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'mars_migrator') THEN
    CREATE ROLE mars_migrator NOLOGIN;
    COMMENT ON ROLE mars_migrator IS
      'Applies schema migrations. LOGIN/password set out-of-band by Server Ops.';
  END IF;
END
$$;

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'iseo_runtime') THEN
    CREATE ROLE iseo_runtime NOLOGIN;
    COMMENT ON ROLE iseo_runtime IS
      'iSEO Sales mutating runtime (n8n/Toolkit). LOGIN/password set out-of-band.';
  END IF;
END
$$;

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'iseo_agent') THEN
    CREATE ROLE iseo_agent NOLOGIN;
    COMMENT ON ROLE iseo_agent IS
      'iSEO Sales agent: read + limited EXECUTE. LOGIN/password set out-of-band.';
  END IF;
END
$$;

DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'iseo_reader') THEN
    CREATE ROLE iseo_reader NOLOGIN;
    COMMENT ON ROLE iseo_reader IS
      'iSEO Sales read-only. LOGIN/password set out-of-band.';
  END IF;
END
$$;

-- Note: mars_owner is typically the database owner / bootstrap role and is
-- not created here. content_* roles are deferred until app_seo_content ships tables.
