-- Extended local validation for iSEO Sales V1 (platform-neutral SQL)
-- Complements 02_constraints.sql / 03_permissions.sql
-- RAISE EXCEPTION on failure

-- ---------------------------------------------------------------------------
-- Functions: register / upsert / status / delivery / job
-- ---------------------------------------------------------------------------
DO $$
DECLARE
  inbound jsonb;
  lead jsonb;
  st1 jsonb;
  st2 jsonb;
  del1 jsonb;
  del2 jsonb;
  job jsonb;
  ver int;
  evt_cnt int;
  run_id text := replace(gen_random_uuid()::text, '-', '');
  v_lead_id text;
  src_id text;
  idem_status text;
  idem_del text;
  job_dedupe text;
BEGIN
  v_lead_id := 'LEAD_EXT_' || substr(run_id, 1, 12);
  src_id := 'msgid-ext-' || run_id;
  idem_status := 'idem-ext-status-' || run_id;
  idem_del := 'idem-ext-delivery-' || run_id;
  job_dedupe := 'dedupe-ext-job-' || run_id;

  inbound := app_iseo_sales.register_inbound_event(
    'gmail', src_id, '{"ok":true}'::jsonb, 'body text', 'corr-ext-1'
  );
  IF inbound->>'id' IS NULL THEN
    RAISE EXCEPTION 'ASSERT: register_inbound_event missing id';
  END IF;

  lead := app_iseo_sales.upsert_lead(
    v_lead_id,
    (inbound->>'id')::bigint,
    src_id,
    'Ext Client',
    'Contact',
    'email',
    NULL,
    'ext@example.com',
    NULL,
    'https://example.com',
    'seo',
    'summary',
    'test',
    'new'
  );
  IF lead->>'lead_id' <> v_lead_id THEN
    RAISE EXCEPTION 'ASSERT: upsert_lead lead_id';
  END IF;

  st1 := app_iseo_sales.change_lead_status(
    v_lead_id, NULL, 'new', 'pending',
    'moderator', 'MOD_B', idem_status, 'corr-ext-status'
  );
  IF (st1->>'version')::int < 2 THEN
    RAISE EXCEPTION 'ASSERT: status change should bump version';
  END IF;

  -- stale expected status rejected (actual is pending, expected from=new)
  BEGIN
    PERFORM app_iseo_sales.change_lead_status(
      v_lead_id, NULL, 'new', 'reviewing',
      'moderator', 'MOD_B', 'idem-ext-stale-' || run_id, 'corr-ext-stale'
    );
    RAISE EXCEPTION 'ASSERT: stale expected status should fail';
  EXCEPTION
    WHEN OTHERS THEN
      IF SQLERRM LIKE '%ASSERT:%' THEN RAISE; END IF;
  END;

  -- stale expected version rejected
  BEGIN
    PERFORM app_iseo_sales.change_lead_status(
      v_lead_id, 1, 'pending', 'reviewing',
      'moderator', 'MOD_B', 'idem-ext-stale-ver-' || run_id, 'corr-ext-stale-ver'
    );
    RAISE EXCEPTION 'ASSERT: stale expected version should fail';
  EXCEPTION
    WHEN OTHERS THEN
      IF SQLERRM LIKE '%ASSERT:%' THEN RAISE; END IF;
  END;

  -- duplicate same idempotency key does NOT duplicate side effect
  st2 := app_iseo_sales.change_lead_status(
    v_lead_id, NULL, 'new', 'pending',
    'moderator', 'MOD_B', idem_status, 'corr-ext-status'
  );
  IF COALESCE((st2->>'idempotent_replay')::boolean, false) IS NOT TRUE THEN
    RAISE EXCEPTION 'ASSERT: duplicate idempotency key must replay';
  END IF;

  SELECT l.version INTO ver FROM app_iseo_sales.leads l WHERE l.lead_id = v_lead_id;
  IF ver IS DISTINCT FROM (st1->>'version')::int THEN
    RAISE EXCEPTION 'ASSERT: version changed on idempotent replay (got %, expected %)',
      ver, (st1->>'version')::int;
  END IF;

  SELECT count(*) INTO evt_cnt FROM app_iseo_sales.lead_events e
  WHERE e.lead_id = v_lead_id AND e.event_type = 'status_changed';
  IF evt_cnt <> 1 THEN
    RAISE EXCEPTION 'ASSERT: expected exactly 1 status_changed event, got %', evt_cnt;
  END IF;

  IF NOT EXISTS (
    SELECT 1 FROM app_iseo_sales.audit_logs a
    WHERE a.entity_id = v_lead_id AND a.action = 'change_lead_status'
  ) THEN
    RAISE EXCEPTION 'ASSERT: audit_logs missing for status change';
  END IF;

  del1 := app_iseo_sales.enqueue_delivery(
    v_lead_id,
    'telegram',
    NULL,
    NULL,
    'lead_card',
    '{"fixture":true}'::jsonb,
    idem_del,
    'corr-ext-del'
  );
  IF del1->>'id' IS NULL THEN
    RAISE EXCEPTION 'ASSERT: enqueue_delivery missing id';
  END IF;

  del2 := app_iseo_sales.enqueue_delivery(
    v_lead_id,
    'telegram',
    NULL,
    NULL,
    'lead_card',
    '{"fixture":true}'::jsonb,
    idem_del,
    'corr-ext-del-2'
  );
  IF COALESCE((del2->>'idempotent_replay')::boolean, false) IS NOT TRUE THEN
    RAISE EXCEPTION 'ASSERT: duplicate delivery idempotency should replay';
  END IF;
  IF (del1->>'id') IS DISTINCT FROM (del2->>'id') THEN
    RAISE EXCEPTION 'ASSERT: delivery ids should match on replay';
  END IF;

  job := app_iseo_sales.enqueue_job(
    'reminder',
    jsonb_build_object('lead_id', v_lead_id),
    5,
    now() - interval '1 second',
    job_dedupe,
    'corr-ext-job',
    v_lead_id
  );
  IF job->>'id' IS NULL THEN
    RAISE EXCEPTION 'ASSERT: enqueue_job missing id';
  END IF;
END
$$;

-- ---------------------------------------------------------------------------
-- Outbox: status change (moderator) creates delivery intent in same txn path
-- ---------------------------------------------------------------------------
DO $$
DECLARE
  before_del int;
  after_del int;
  before_ver int;
  after_ver int;
  run_id text := replace(gen_random_uuid()::text, '-', '');
  v_lead_id text := 'LEAD_OUT_' || substr(run_id, 1, 12);
BEGIN
  PERFORM app_iseo_sales.upsert_lead(
    v_lead_id, NULL, NULL, 'Outbox Client', NULL, NULL, NULL, NULL, NULL, NULL,
    NULL, NULL, NULL, 'new'
  );
  SELECT l.version INTO before_ver FROM app_iseo_sales.leads l WHERE l.lead_id = v_lead_id;
  SELECT count(*) INTO before_del FROM app_iseo_sales.deliveries d WHERE d.lead_id = v_lead_id;

  PERFORM app_iseo_sales.change_lead_status(
    v_lead_id, NULL, 'new', 'pending',
    'moderator', 'MOD_OUTBOX', 'idem-outbox-' || run_id, 'corr-outbox'
  );

  SELECT l.version INTO after_ver FROM app_iseo_sales.leads l WHERE l.lead_id = v_lead_id;
  SELECT count(*) INTO after_del FROM app_iseo_sales.deliveries d WHERE d.lead_id = v_lead_id;
  IF after_ver <= before_ver THEN
    RAISE EXCEPTION 'ASSERT: outbox path should update lead';
  END IF;
  IF after_del <= before_del THEN
    RAISE EXCEPTION 'ASSERT: moderator status change should enqueue lead_card_sync delivery';
  END IF;
  IF NOT EXISTS (
    SELECT 1 FROM app_iseo_sales.deliveries d
    WHERE d.lead_id = v_lead_id
      AND d.delivery_type = 'lead_card_sync'
      AND d.status = 'pending'
  ) THEN
    RAISE EXCEPTION 'ASSERT: pending lead_card_sync delivery missing';
  END IF;
END
$$;

-- ---------------------------------------------------------------------------
-- Jobs: pending / available_at / claim exclusivity / complete
-- ---------------------------------------------------------------------------
DO $$
DECLARE
  enq jsonb;
  j1 app_iseo_sales.jobs%ROWTYPE;
  j2 app_iseo_sales.jobs%ROWTYPE;
  job_id bigint;
  claimed_target boolean := false;
  row_status text;
  row_attempts int;
  row_locked_by text;
BEGIN
  enq := app_iseo_sales.enqueue_job(
    'retry',
    '{"n":1}'::jsonb,
    1,
    now() - interval '5 seconds',
    'dedupe-claim-exclusive-' || replace(gen_random_uuid()::text, '-', ''),
    'corr-claim-ex',
    NULL
  );
  job_id := (enq->>'id')::bigint;
  IF job_id IS NULL THEN
    RAISE EXCEPTION 'ASSERT: enqueue_job did not return id';
  END IF;

  UPDATE app_iseo_sales.jobs
  SET status = 'pending', locked_by = NULL, lease_until = NULL, available_at = now() - interval '1 second'
  WHERE id = job_id;

  FOR j1 IN SELECT * FROM app_iseo_sales.claim_jobs('worker-A', 50, 60)
  LOOP
    IF j1.id = job_id THEN
      claimed_target := true;
    END IF;
  END LOOP;
  IF NOT claimed_target THEN
    RAISE EXCEPTION 'ASSERT: worker-A did not claim target job %', job_id;
  END IF;

  SELECT status, attempts, locked_by INTO row_status, row_attempts, row_locked_by
  FROM app_iseo_sales.jobs WHERE id = job_id;
  IF row_status <> 'running' OR row_attempts < 1 OR row_locked_by IS DISTINCT FROM 'worker-A' THEN
    RAISE EXCEPTION 'ASSERT: claim state unexpected status=% attempts=% locked_by=%',
      row_status, row_attempts, row_locked_by;
  END IF;

  FOR j2 IN SELECT * FROM app_iseo_sales.claim_jobs('worker-B', 50, 60)
  LOOP
    IF j2.id = job_id THEN
      RAISE EXCEPTION 'ASSERT: job % claimed by two workers', job_id;
    END IF;
  END LOOP;

  UPDATE app_iseo_sales.jobs
  SET status = 'completed', completed_at = now(), locked_by = NULL, lease_until = NULL, updated_at = now()
  WHERE id = job_id;

  IF NOT EXISTS (
    SELECT 1 FROM app_iseo_sales.jobs
    WHERE id = job_id AND status = 'completed' AND attempts >= 1
  ) THEN
    RAISE EXCEPTION 'ASSERT: job complete / attempts not recorded';
  END IF;
END
$$;

-- ---------------------------------------------------------------------------
-- Event immutability: runtime cannot UPDATE/DELETE lead_events
-- ---------------------------------------------------------------------------
DO $$
DECLARE
  eid bigint;
BEGIN
  SELECT id INTO eid FROM app_iseo_sales.lead_events ORDER BY id LIMIT 1;
  IF eid IS NULL THEN
    RAISE EXCEPTION 'ASSERT: need at least one lead_event';
  END IF;

  IF has_table_privilege('iseo_runtime', 'app_iseo_sales.lead_events', 'UPDATE') THEN
    RAISE EXCEPTION 'ASSERT: iseo_runtime must not UPDATE lead_events';
  END IF;
  IF has_table_privilege('iseo_runtime', 'app_iseo_sales.lead_events', 'DELETE') THEN
    RAISE EXCEPTION 'ASSERT: iseo_runtime must not DELETE lead_events';
  END IF;

  BEGIN
    EXECUTE 'SET ROLE iseo_runtime';
    BEGIN
      EXECUTE format('UPDATE app_iseo_sales.lead_events SET payload = ''{}''::jsonb WHERE id = %s', eid);
      RAISE EXCEPTION 'ASSERT: UPDATE lead_events as iseo_runtime should fail';
    EXCEPTION
      WHEN insufficient_privilege THEN NULL;
      WHEN OTHERS THEN
        IF SQLERRM LIKE '%ASSERT:%' THEN RAISE; END IF;
    END;
    BEGIN
      EXECUTE format('DELETE FROM app_iseo_sales.lead_events WHERE id = %s', eid);
      RAISE EXCEPTION 'ASSERT: DELETE lead_events as iseo_runtime should fail';
    EXCEPTION
      WHEN insufficient_privilege THEN NULL;
      WHEN OTHERS THEN
        IF SQLERRM LIKE '%ASSERT:%' THEN RAISE; END IF;
    END;
    EXECUTE 'RESET ROLE';
  EXCEPTION
    WHEN undefined_object THEN
      RAISE NOTICE 'SKIP SET ROLE iseo_runtime for immutability runtime check';
    WHEN OTHERS THEN
      EXECUTE 'RESET ROLE';
      RAISE;
  END;
END
$$;

-- ---------------------------------------------------------------------------
-- FK integrity: invalid inbound_event_id rejected
-- ---------------------------------------------------------------------------
DO $$
DECLARE
  ok boolean := false;
BEGIN
  BEGIN
    INSERT INTO app_iseo_sales.leads (lead_id, inbound_event_id, manager_status)
    VALUES ('LEAD_BAD_FK_' || substr(replace(gen_random_uuid()::text, '-', ''), 1, 8), 999999999, 'new');
  EXCEPTION
    WHEN foreign_key_violation THEN
      ok := true;
  END;
  IF NOT ok THEN
    RAISE EXCEPTION 'ASSERT: invalid FK should be rejected';
  END IF;
END
$$;

-- ---------------------------------------------------------------------------
-- NOT NULL / CHECK: invalid manager_status rejected
-- ---------------------------------------------------------------------------
DO $$
DECLARE
  ok boolean := false;
BEGIN
  BEGIN
    INSERT INTO app_iseo_sales.leads (lead_id, manager_status)
    VALUES ('LEAD_BAD_ST_' || substr(replace(gen_random_uuid()::text, '-', ''), 1, 8), 'not_a_real_status');
  EXCEPTION
    WHEN check_violation THEN
      ok := true;
  END;
  IF NOT ok THEN
    RAISE EXCEPTION 'ASSERT: invalid manager_status CHECK should reject';
  END IF;
END
$$;

-- ---------------------------------------------------------------------------
-- Cross-schema isolation structural: app_seo_content exists; runtime no write
-- ---------------------------------------------------------------------------
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = 'app_seo_content') THEN
    RAISE EXCEPTION 'ASSERT: placeholder schema app_seo_content must exist';
  END IF;
  IF has_schema_privilege('iseo_runtime', 'app_seo_content', 'USAGE') THEN
    RAISE EXCEPTION 'ASSERT: iseo_runtime must not have USAGE on app_seo_content';
  END IF;
  IF has_schema_privilege('iseo_runtime', 'app_seo_content', 'CREATE') THEN
    RAISE EXCEPTION 'ASSERT: iseo_runtime must not CREATE in app_seo_content';
  END IF;
END
$$;

DO $$
BEGIN
  RAISE NOTICE '04_extended_local_validation.sql: all assertions passed';
END
$$;
