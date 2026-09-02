-- Permission smoke tests for app_iseo_sales V1
-- Prefer connecting as superuser/owner that can SET ROLE to iseo_* roles.
-- Roles are NOLOGIN by default; SET ROLE still works for membership/superuser.

DO $$
BEGIN
  -- iseo_runtime must not CREATE TABLE in app_iseo_sales
  BEGIN
    EXECUTE 'SET ROLE iseo_runtime';
    BEGIN
      EXECUTE 'CREATE TABLE app_iseo_sales._perm_should_fail (id int)';
      RAISE EXCEPTION 'ASSERT: iseo_runtime CREATE TABLE should fail';
    EXCEPTION
      WHEN insufficient_privilege THEN
        NULL; -- expected
      WHEN OTHERS THEN
        IF SQLERRM LIKE '%ASSERT:%' THEN
          RAISE;
        END IF;
        -- some PG versions may raise different privilege errors
        NULL;
    END;
    EXECUTE 'RESET ROLE';
  EXCEPTION
    WHEN undefined_object THEN
      RAISE NOTICE 'SKIP: cannot SET ROLE iseo_runtime — grant membership or use superuser';
    WHEN OTHERS THEN
      EXECUTE 'RESET ROLE';
      RAISE;
  END;
END
$$;

DO $$
BEGIN
  -- iSEO roles must not see app_seo_content
  BEGIN
    EXECUTE 'SET ROLE iseo_runtime';
    BEGIN
      EXECUTE 'SELECT 1 FROM app_seo_content.no_such_table';
      RAISE EXCEPTION 'ASSERT: unexpected success selecting app_seo_content';
    EXCEPTION
      WHEN insufficient_privilege THEN
        NULL;
      WHEN undefined_table THEN
        -- schema USAGE denied often surfaces as undefined_table OR privilege;
        -- if we got here with USAGE, table absence is ok only if schema accessible —
        -- verify USAGE denied via has_schema_privilege
        IF has_schema_privilege('iseo_runtime', 'app_seo_content', 'USAGE') THEN
          RAISE EXCEPTION 'ASSERT: iseo_runtime must not have USAGE on app_seo_content';
        END IF;
      WHEN OTHERS THEN
        IF SQLERRM LIKE '%ASSERT:%' THEN
          RAISE;
        END IF;
        IF has_schema_privilege('iseo_runtime', 'app_seo_content', 'USAGE') THEN
          RAISE EXCEPTION 'ASSERT: iseo_runtime must not have USAGE on app_seo_content';
        END IF;
    END;
    EXECUTE 'RESET ROLE';
  EXCEPTION
    WHEN undefined_object THEN
      RAISE NOTICE 'SKIP: cannot SET ROLE iseo_runtime';
    WHEN OTHERS THEN
      EXECUTE 'RESET ROLE';
      RAISE;
  END;
END
$$;

DO $$
BEGIN
  IF has_schema_privilege('iseo_agent', 'app_seo_content', 'USAGE')
     OR has_schema_privilege('iseo_reader', 'app_seo_content', 'USAGE') THEN
    RAISE EXCEPTION 'ASSERT: iseo_agent/reader must not have USAGE on app_seo_content';
  END IF;
END
$$;

DO $$
BEGIN
  -- iseo_agent must not UPDATE leads
  BEGIN
    EXECUTE 'SET ROLE iseo_agent';
    BEGIN
      EXECUTE $q$UPDATE app_iseo_sales.leads SET manager_notes = 'hack' WHERE lead_id = 'LEAD_SYNTH000001'$q$;
      IF FOUND THEN
        -- UPDATE with 0 rows still succeeds privilege-wise; check privilege explicitly
        NULL;
      END IF;
      IF has_table_privilege('iseo_agent', 'app_iseo_sales.leads', 'UPDATE') THEN
        RAISE EXCEPTION 'ASSERT: iseo_agent must not have UPDATE on leads';
      END IF;
    EXCEPTION
      WHEN insufficient_privilege THEN
        NULL; -- expected
      WHEN OTHERS THEN
        IF SQLERRM LIKE '%ASSERT:%' THEN
          RAISE;
        END IF;
        IF has_table_privilege('iseo_agent', 'app_iseo_sales.leads', 'UPDATE') THEN
          RAISE EXCEPTION 'ASSERT: iseo_agent must not have UPDATE on leads';
        END IF;
    END;
    EXECUTE 'RESET ROLE';
  EXCEPTION
    WHEN undefined_object THEN
      RAISE NOTICE 'SKIP: cannot SET ROLE iseo_agent';
    WHEN OTHERS THEN
      EXECUTE 'RESET ROLE';
      RAISE;
  END;

  IF has_table_privilege('iseo_agent', 'app_iseo_sales.leads', 'UPDATE') THEN
    RAISE EXCEPTION 'ASSERT: iseo_agent must not have UPDATE on leads';
  END IF;
END
$$;

DO $$
BEGIN
  -- iseo_reader SELECT ok on leads; no INSERT
  IF NOT has_table_privilege('iseo_reader', 'app_iseo_sales.leads', 'SELECT') THEN
    RAISE EXCEPTION 'ASSERT: iseo_reader should SELECT leads';
  END IF;
  IF has_table_privilege('iseo_reader', 'app_iseo_sales.leads', 'INSERT') THEN
    RAISE EXCEPTION 'ASSERT: iseo_reader must not INSERT leads';
  END IF;
END
$$;

DO $$
BEGIN
  -- runtime may INSERT lead_events but not DELETE
  IF NOT has_table_privilege('iseo_runtime', 'app_iseo_sales.lead_events', 'INSERT') THEN
    RAISE EXCEPTION 'ASSERT: iseo_runtime should INSERT lead_events';
  END IF;
  IF has_table_privilege('iseo_runtime', 'app_iseo_sales.lead_events', 'DELETE') THEN
    RAISE EXCEPTION 'ASSERT: iseo_runtime must not DELETE lead_events';
  END IF;
END
$$;

DO $$
BEGIN
  RAISE NOTICE '03_permissions.sql: assertions passed (or skips noted)';
END
$$;
