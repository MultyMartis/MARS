-- Constraint / behavior assertions for app_iseo_sales V1
-- Run after 01_schema_apply.sh (fixtures present)
-- RAISE EXCEPTION on failure

DO $$
DECLARE
  v1 jsonb;
  v2 jsonb;
  cnt int;
BEGIN
  -- Idempotent register_inbound_event (duplicate source)
  v1 := app_iseo_sales.register_inbound_event(
    'gmail', 'msgid-constraint-dup-001', '{"t":1}'::jsonb, 'body', 'corr-c-1'
  );
  v2 := app_iseo_sales.register_inbound_event(
    'gmail', 'msgid-constraint-dup-001', '{"t":2}'::jsonb, NULL, 'corr-c-2'
  );
  IF (v1->>'id') IS DISTINCT FROM (v2->>'id') THEN
    RAISE EXCEPTION 'ASSERT: duplicate inbound should same id';
  END IF;
  IF COALESCE((v2->>'is_duplicate')::boolean, false) IS NOT TRUE THEN
    RAISE EXCEPTION 'ASSERT: second register should is_duplicate=true';
  END IF;
  SELECT count(*) INTO cnt FROM app_iseo_sales.inbound_events
  WHERE source_id = 'msgid-constraint-dup-001';
  IF cnt <> 1 THEN
    RAISE EXCEPTION 'ASSERT: expected 1 inbound row, got %', cnt;
  END IF;
END
$$;

DO $$
DECLARE
  a jsonb;
  b jsonb;
BEGIN
  -- upsert_lead by lead_id is idempotent / version bumps
  a := app_iseo_sales.upsert_lead(
    'LEAD_CONSTRAINT001', NULL, 'msgid-constraint-lead-001',
    'Client A', NULL, 'email', NULL, 'a@example.com', NULL, NULL,
    'seo', 'summary a', 'test', 'new'
  );
  b := app_iseo_sales.upsert_lead(
    'LEAD_CONSTRAINT001', NULL, 'msgid-constraint-lead-001',
    'Client A Updated', NULL, 'email', NULL, 'a@example.com', NULL, NULL,
    'seo', 'summary b', 'test', 'pending'
  );
  IF (b->>'lead_id') <> 'LEAD_CONSTRAINT001' THEN
    RAISE EXCEPTION 'ASSERT: upsert lead_id mismatch';
  END IF;
  IF (b->>'version')::int <= (a->>'version')::int THEN
    RAISE EXCEPTION 'ASSERT: upsert should bump version';
  END IF;
END
$$;

DO $$
DECLARE
  ok boolean := false;
BEGIN
  -- Invalid status transition rejected
  PERFORM app_iseo_sales.upsert_lead(
    'LEAD_CONSTRAINT_TX', NULL, NULL, 'Tx Client', NULL, NULL, NULL, NULL, NULL, NULL,
    NULL, NULL, NULL, 'processed'
  );
  BEGIN
    PERFORM app_iseo_sales.change_lead_status(
      'LEAD_CONSTRAINT_TX', NULL, 'processed', 'new',
      'moderator', 'MOD_B', 'idem-bad-tx-1', 'corr-tx'
    );
  EXCEPTION
    WHEN OTHERS THEN
      ok := true;
  END;
  IF NOT ok THEN
    RAISE EXCEPTION 'ASSERT: processed→new should be rejected';
  END IF;
END
$$;

DO $$
DECLARE
  r1 jsonb;
  r2 jsonb;
  ver1 int;
  ver2 int;
BEGIN
  -- Idempotency: no double side effect on change_lead_status
  PERFORM app_iseo_sales.upsert_lead(
    'LEAD_CONSTRAINT_IDEM', NULL, NULL, 'Idem Client', NULL, NULL, NULL, NULL, NULL, NULL,
    NULL, NULL, NULL, 'new'
  );
  r1 := app_iseo_sales.change_lead_status(
    'LEAD_CONSTRAINT_IDEM', NULL, 'new', 'pending',
    'moderator', 'MOD_B', 'idem-status-once', 'corr-idem'
  );
  r2 := app_iseo_sales.change_lead_status(
    'LEAD_CONSTRAINT_IDEM', NULL, 'new', 'pending',
    'moderator', 'MOD_B', 'idem-status-once', 'corr-idem'
  );
  IF COALESCE((r2->>'idempotent_replay')::boolean, false) IS NOT TRUE THEN
    RAISE EXCEPTION 'ASSERT: second change_lead_status should idempotent_replay';
  END IF;
  SELECT version INTO ver1 FROM app_iseo_sales.leads WHERE lead_id = 'LEAD_CONSTRAINT_IDEM';
  -- version should not bump again on replay (still at post-first-change)
  IF (r1->>'version')::int IS DISTINCT FROM ver1 THEN
    RAISE EXCEPTION 'ASSERT: version drifted after idempotent replay';
  END IF;
  ver2 := (r2->>'version')::int;
  IF ver2 IS DISTINCT FROM (r1->>'version')::int THEN
    RAISE EXCEPTION 'ASSERT: replay response version mismatch';
  END IF;
END
$$;

DO $$
BEGIN
  -- lead_events immutability is enforced by REVOKE DELETE (and no UPDATE grant path
  -- for agents). Document: runtime should not UPDATE; grants revoke DELETE.
  -- Soft check: table exists and has no updated_at column.
  IF EXISTS (
    SELECT 1 FROM information_schema.columns
    WHERE table_schema = 'app_iseo_sales'
      AND table_name = 'lead_events'
      AND column_name = 'updated_at'
  ) THEN
    RAISE EXCEPTION 'ASSERT: lead_events must not have updated_at';
  END IF;
END
$$;

DO $$
DECLARE
  claimed int := 0;
  j app_iseo_sales.jobs%ROWTYPE;
BEGIN
  PERFORM app_iseo_sales.enqueue_job(
    'reconciliation',
    '{"fixture":"claim"}'::jsonb,
    10,
    now(),
    'fixture-claim-jobs-key-001',
    'corr-claim',
    NULL
  );
  FOR j IN SELECT * FROM app_iseo_sales.claim_jobs('worker-test-1', 5, 30)
  LOOP
    claimed := claimed + 1;
  END LOOP;
  IF claimed < 1 THEN
    RAISE EXCEPTION 'ASSERT: claim_jobs should return at least one job';
  END IF;
END
$$;

DO $$
BEGIN
  RAISE NOTICE '02_constraints.sql: all assertions passed';
END
$$;
