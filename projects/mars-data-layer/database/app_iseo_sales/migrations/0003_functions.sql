-- app_iseo_sales SECURITY DEFINER functions (V1)
-- Prerequisites: 0001_base_tables, 0002_indexes
-- search_path locked to app_iseo_sales, mars_core, pg_temp
-- Function sources live in this migration; see ../functions/README.md

SET search_path = app_iseo_sales, mars_core, pg_temp;

-- ---------------------------------------------------------------------------
-- Status transition allow-list
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.fn_is_allowed_status_transition(
  p_from text,
  p_to text
) RETURNS boolean
LANGUAGE plpgsql
IMMUTABLE
AS $$
BEGIN
  IF p_from IS NULL OR p_to IS NULL THEN
    RETURN false;
  END IF;
  IF p_from = p_to THEN
    RETURN true; -- noop / idempotent same-status
  END IF;

  RETURN CASE p_from
    WHEN 'new' THEN p_to IN (
      'pending', 'processed', 'spam', 'error', 'reviewing',
      'contacted', 'waiting_client', 'qualified', 'not_target', 'closed'
    )
    WHEN 'pending' THEN p_to IN (
      'processed', 'spam', 'error', 'reviewing', 'contacted',
      'waiting_client', 'qualified', 'not_target', 'closed', 'reopened'
    )
    WHEN 'reviewing' THEN p_to IN (
      'pending', 'processed', 'spam', 'error', 'contacted',
      'waiting_client', 'qualified', 'not_target', 'closed'
    )
    WHEN 'contacted' THEN p_to IN (
      'waiting_client', 'qualified', 'not_target', 'processed',
      'closed', 'pending', 'reviewing'
    )
    WHEN 'waiting_client' THEN p_to IN (
      'contacted', 'qualified', 'not_target', 'processed', 'closed', 'pending'
    )
    WHEN 'qualified' THEN p_to IN ('processed', 'closed', 'waiting_client', 'contacted')
    WHEN 'not_target' THEN p_to IN ('closed', 'processed', 'spam', 'pending', 'reopened')
    WHEN 'processed' THEN p_to IN ('pending', 'reopened', 'closed', 'spam')
    WHEN 'spam' THEN p_to IN ('pending', 'reopened', 'processed')
    WHEN 'error' THEN p_to IN ('pending', 'reviewing', 'processed', 'spam', 'closed')
    WHEN 'closed' THEN p_to IN ('reopened', 'pending')
    WHEN 'reopened' THEN p_to IN (
      'pending', 'processed', 'spam', 'error', 'reviewing',
      'contacted', 'waiting_client', 'qualified', 'not_target', 'closed'
    )
    ELSE false
  END;
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.fn_is_allowed_status_transition(text, text) IS
  'Allow-list for manager_status transitions (ops + CRM lifecycle subset)';

-- ---------------------------------------------------------------------------
-- 1) register_inbound_event
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.register_inbound_event(
  p_source_system text DEFAULT 'gmail',
  p_source_id text DEFAULT NULL,
  p_payload jsonb DEFAULT '{}'::jsonb,
  p_raw_text text DEFAULT NULL,
  p_correlation_id text DEFAULT NULL,
  p_gmail_thread_id text DEFAULT NULL,
  p_received_at timestamptz DEFAULT NULL,
  p_subject text DEFAULT NULL,
  p_from_email text DEFAULT NULL,
  p_normalized_hash text DEFAULT NULL,
  p_parser_version text DEFAULT NULL,
  p_workflow_version text DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_id bigint;
  v_is_duplicate boolean := false;
  v_existing_id bigint;
BEGIN
  IF p_source_id IS NULL OR btrim(p_source_id) = '' THEN
    RAISE EXCEPTION 'register_inbound_event: p_source_id required';
  END IF;

  SELECT ie.id INTO v_existing_id
  FROM app_iseo_sales.inbound_events ie
  WHERE ie.source_system = COALESCE(p_source_system, 'gmail')
    AND ie.source_id = p_source_id;

  IF v_existing_id IS NOT NULL THEN
    UPDATE app_iseo_sales.inbound_events
    SET
      last_seen_at = now(),
      processing_attempts = processing_attempts + 1,
      updated_at = now(),
      raw_payload = CASE
        WHEN p_payload IS NOT NULL AND p_payload <> '{}'::jsonb THEN p_payload
        ELSE raw_payload
      END,
      raw_text = COALESCE(p_raw_text, raw_text),
      correlation_id = COALESCE(p_correlation_id, correlation_id)
    WHERE id = v_existing_id
    RETURNING id INTO v_id;
    v_is_duplicate := true;
  ELSE
    INSERT INTO app_iseo_sales.inbound_events (
      source_system, source_id, gmail_thread_id, received_at,
      raw_payload, raw_text, correlation_id, subject, from_email,
      normalized_hash, parser_version, workflow_version
    ) VALUES (
      COALESCE(p_source_system, 'gmail'),
      p_source_id,
      p_gmail_thread_id,
      COALESCE(p_received_at, now()),
      COALESCE(p_payload, '{}'::jsonb),
      p_raw_text,
      p_correlation_id,
      p_subject,
      p_from_email,
      p_normalized_hash,
      p_parser_version,
      p_workflow_version
    )
    ON CONFLICT (source_system, source_id) DO UPDATE
      SET
        last_seen_at = now(),
        processing_attempts = app_iseo_sales.inbound_events.processing_attempts + 1,
        updated_at = now()
    RETURNING id, (xmax <> 0) INTO v_id, v_is_duplicate;
    -- xmax<>0 means updated existing row in this INSERT…ON CONFLICT path
  END IF;

  RETURN jsonb_build_object(
    'id', v_id,
    'is_duplicate', COALESCE(v_is_duplicate, false),
    'source_system', COALESCE(p_source_system, 'gmail'),
    'source_id', p_source_id
  );
END;
$$;

-- ---------------------------------------------------------------------------
-- 2) upsert_lead
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.upsert_lead(
  p_lead_id text,
  p_inbound_event_id bigint DEFAULT NULL,
  p_source_message_id text DEFAULT NULL,
  p_client_name text DEFAULT NULL,
  p_primary_contact text DEFAULT NULL,
  p_contact_type text DEFAULT NULL,
  p_phone text DEFAULT NULL,
  p_email text DEFAULT NULL,
  p_messenger text DEFAULT NULL,
  p_site text DEFAULT NULL,
  p_service text DEFAULT NULL,
  p_summary text DEFAULT NULL,
  p_source text DEFAULT NULL,
  p_manager_status text DEFAULT NULL,
  p_form_metadata jsonb DEFAULT NULL,
  p_data_contract_version text DEFAULT NULL,
  p_workflow_version text DEFAULT NULL,
  p_parser_version text DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_id bigint;
  v_version int;
  v_inserted boolean := false;
BEGIN
  IF p_lead_id IS NULL OR btrim(p_lead_id) = '' THEN
    RAISE EXCEPTION 'upsert_lead: p_lead_id required';
  END IF;

  INSERT INTO app_iseo_sales.leads (
    lead_id, inbound_event_id, source_message_id, client_name, primary_contact,
    contact_type, phone, email, messenger, site, service, summary, source,
    manager_status, form_metadata, data_contract_version, workflow_version,
    parser_version, version, updated_at
  ) VALUES (
    p_lead_id, p_inbound_event_id, p_source_message_id, p_client_name, p_primary_contact,
    p_contact_type, p_phone, p_email, p_messenger, p_site, p_service, p_summary, p_source,
    COALESCE(p_manager_status, 'new'),
    COALESCE(p_form_metadata, '{}'::jsonb),
    p_data_contract_version, p_workflow_version, p_parser_version,
    1, now()
  )
  ON CONFLICT (lead_id) DO UPDATE SET
    inbound_event_id = COALESCE(EXCLUDED.inbound_event_id, app_iseo_sales.leads.inbound_event_id),
    source_message_id = COALESCE(EXCLUDED.source_message_id, app_iseo_sales.leads.source_message_id),
    client_name = COALESCE(EXCLUDED.client_name, app_iseo_sales.leads.client_name),
    primary_contact = COALESCE(EXCLUDED.primary_contact, app_iseo_sales.leads.primary_contact),
    contact_type = COALESCE(EXCLUDED.contact_type, app_iseo_sales.leads.contact_type),
    phone = COALESCE(EXCLUDED.phone, app_iseo_sales.leads.phone),
    email = COALESCE(EXCLUDED.email, app_iseo_sales.leads.email),
    messenger = COALESCE(EXCLUDED.messenger, app_iseo_sales.leads.messenger),
    site = COALESCE(EXCLUDED.site, app_iseo_sales.leads.site),
    service = COALESCE(EXCLUDED.service, app_iseo_sales.leads.service),
    summary = COALESCE(EXCLUDED.summary, app_iseo_sales.leads.summary),
    source = COALESCE(EXCLUDED.source, app_iseo_sales.leads.source),
    manager_status = COALESCE(p_manager_status, app_iseo_sales.leads.manager_status),
    form_metadata = CASE
      WHEN p_form_metadata IS NOT NULL THEN p_form_metadata
      ELSE app_iseo_sales.leads.form_metadata
    END,
    data_contract_version = COALESCE(EXCLUDED.data_contract_version, app_iseo_sales.leads.data_contract_version),
    workflow_version = COALESCE(EXCLUDED.workflow_version, app_iseo_sales.leads.workflow_version),
    parser_version = COALESCE(EXCLUDED.parser_version, app_iseo_sales.leads.parser_version),
    version = app_iseo_sales.leads.version + 1,
    updated_at = now()
  RETURNING id, version, (xmax = 0) INTO v_id, v_version, v_inserted;

  IF p_source_message_id IS NOT NULL AND btrim(p_source_message_id) <> '' THEN
    INSERT INTO app_iseo_sales.lead_dedup_keys (dedup_key, key_type, lead_id)
    VALUES (
      'gmail_message_id:' || p_source_message_id,
      'gmail_message_id',
      p_lead_id
    )
    ON CONFLICT (dedup_key) DO UPDATE
      SET lead_id = EXCLUDED.lead_id;
  END IF;

  RETURN jsonb_build_object(
    'id', v_id,
    'lead_id', p_lead_id,
    'version', v_version,
    'inserted', COALESCE(v_inserted, false)
  );
END;
$$;

-- ---------------------------------------------------------------------------
-- 3) change_lead_status
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.change_lead_status(
  p_lead_id text,
  p_expected_version int,
  p_from_status text,
  p_to_status text,
  p_actor_type text DEFAULT 'moderator',
  p_actor_id text DEFAULT NULL,
  p_idempotency_key text DEFAULT NULL,
  p_correlation_id text DEFAULT NULL,
  p_close_reason text DEFAULT NULL,
  p_notes text DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_prior jsonb;
  v_lead app_iseo_sales.leads%ROWTYPE;
  v_result jsonb;
  v_delivery_id text;
BEGIN
  IF p_lead_id IS NULL OR p_to_status IS NULL THEN
    RAISE EXCEPTION 'change_lead_status: lead_id and to_status required';
  END IF;

  IF p_idempotency_key IS NOT NULL THEN
    SELECT response_ref INTO v_prior
    FROM app_iseo_sales.idempotency_keys
    WHERE scope = 'change_lead_status'
      AND idempotency_key = p_idempotency_key;
    IF v_prior IS NOT NULL THEN
      RETURN v_prior || jsonb_build_object('idempotent_replay', true);
    END IF;
  END IF;

  SELECT * INTO v_lead
  FROM app_iseo_sales.leads
  WHERE lead_id = p_lead_id
  FOR UPDATE;

  IF NOT FOUND THEN
    RAISE EXCEPTION 'change_lead_status: lead % not found', p_lead_id;
  END IF;

  IF p_expected_version IS NOT NULL AND v_lead.version <> p_expected_version THEN
    RAISE EXCEPTION 'change_lead_status: version conflict (expected %, actual %)',
      p_expected_version, v_lead.version;
  END IF;

  IF p_from_status IS NOT NULL AND v_lead.manager_status <> p_from_status THEN
    RAISE EXCEPTION 'change_lead_status: status mismatch (expected %, actual %)',
      p_from_status, v_lead.manager_status;
  END IF;

  IF NOT app_iseo_sales.fn_is_allowed_status_transition(v_lead.manager_status, p_to_status) THEN
    RAISE EXCEPTION 'change_lead_status: transition % → % not allowed',
      v_lead.manager_status, p_to_status;
  END IF;

  UPDATE app_iseo_sales.leads
  SET
    manager_status = p_to_status,
    version = version + 1,
    updated_at = now(),
    close_reason = CASE WHEN p_to_status = 'closed' THEN COALESCE(p_close_reason, close_reason) ELSE close_reason END,
    closed_at = CASE WHEN p_to_status = 'closed' THEN COALESCE(closed_at, now()) ELSE closed_at END,
    manager_notes = COALESCE(p_notes, manager_notes),
    processed_at = CASE
      WHEN p_to_status IN ('processed', 'spam') THEN COALESCE(processed_at, now())
      ELSE processed_at
    END
  WHERE lead_id = p_lead_id
  RETURNING * INTO v_lead;

  INSERT INTO app_iseo_sales.lead_events (
    lead_id, event_type, actor_type, actor_id, correlation_id, payload
  ) VALUES (
    p_lead_id,
    'status_changed',
    COALESCE(p_actor_type, 'moderator'),
    p_actor_id,
    p_correlation_id,
    jsonb_build_object(
      'from_status', p_from_status,
      'to_status', p_to_status,
      'close_reason', p_close_reason
    )
  );

  INSERT INTO app_iseo_sales.audit_logs (
    actor_type, actor_id, action, entity_type, entity_id, correlation_id, result, detail
  ) VALUES (
    COALESCE(p_actor_type, 'moderator'),
    p_actor_id,
    'change_lead_status',
    'lead',
    p_lead_id,
    p_correlation_id,
    'success',
    jsonb_build_object('to_status', p_to_status, 'version', v_lead.version)
  );

  -- Moderator-driven status change: enqueue card refresh (simple outbox signal)
  IF COALESCE(p_actor_type, 'moderator') IN ('moderator', 'admin') THEN
    v_delivery_id := 'sync-' || p_lead_id || '-' || v_lead.version::text;
    INSERT INTO app_iseo_sales.deliveries (
      delivery_id, lead_id, delivery_type, status, payload, idempotency_key, correlation_id
    ) VALUES (
      v_delivery_id,
      p_lead_id,
      'lead_card_sync',
      'pending',
      jsonb_build_object('reason', 'status_changed', 'to_status', p_to_status),
      'lead_card_sync:' || p_lead_id || ':' || v_lead.version::text,
      p_correlation_id
    )
    ON CONFLICT (idempotency_key) DO NOTHING;
  END IF;

  v_result := jsonb_build_object(
    'lead_id', p_lead_id,
    'manager_status', v_lead.manager_status,
    'version', v_lead.version,
    'result', 'success'
  );

  IF p_idempotency_key IS NOT NULL THEN
    INSERT INTO app_iseo_sales.idempotency_keys (
      scope, idempotency_key, response_ref, lead_id
    ) VALUES (
      'change_lead_status', p_idempotency_key, v_result, p_lead_id
    )
    ON CONFLICT (scope, idempotency_key) DO NOTHING;
  END IF;

  RETURN v_result;
END;
$$;

-- ---------------------------------------------------------------------------
-- 4) enqueue_delivery
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.enqueue_delivery(
  p_lead_id text DEFAULT NULL,
  p_channel text DEFAULT 'telegram',
  p_recipient_principal_key text DEFAULT NULL,
  p_recipient_telegram_user_id text DEFAULT NULL,
  p_delivery_type text DEFAULT 'lead_card',
  p_payload jsonb DEFAULT '{}'::jsonb,
  p_idempotency_key text DEFAULT NULL,
  p_correlation_id text DEFAULT NULL,
  p_available_at timestamptz DEFAULT now(),
  p_delivery_id text DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_id bigint;
  v_delivery_id text;
BEGIN
  IF p_delivery_type IS NULL THEN
    RAISE EXCEPTION 'enqueue_delivery: delivery_type required';
  END IF;

  v_delivery_id := COALESCE(p_delivery_id, 'dlv-' || gen_random_uuid()::text);

  INSERT INTO app_iseo_sales.deliveries (
    delivery_id, lead_id, channel, recipient_principal_key,
    recipient_telegram_user_id, delivery_type, payload, status,
    available_at, idempotency_key, correlation_id
  ) VALUES (
    v_delivery_id, p_lead_id, COALESCE(p_channel, 'telegram'),
    p_recipient_principal_key, p_recipient_telegram_user_id,
    p_delivery_type, COALESCE(p_payload, '{}'::jsonb), 'pending',
    COALESCE(p_available_at, now()), p_idempotency_key, p_correlation_id
  )
  ON CONFLICT (idempotency_key) DO NOTHING
  RETURNING id INTO v_id;

  IF v_id IS NULL AND p_idempotency_key IS NOT NULL THEN
    SELECT id INTO v_id
    FROM app_iseo_sales.deliveries
    WHERE idempotency_key = p_idempotency_key;
    RETURN jsonb_build_object(
      'id', v_id,
      'idempotent_replay', true,
      'delivery_id', (SELECT delivery_id FROM app_iseo_sales.deliveries WHERE id = v_id)
    );
  END IF;

  RETURN jsonb_build_object(
    'id', v_id,
    'delivery_id', v_delivery_id,
    'idempotent_replay', false
  );
END;
$$;

-- ---------------------------------------------------------------------------
-- 5) enqueue_job (dedupe via unique index + unique_violation catch)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.enqueue_job(
  p_job_type text,
  p_payload jsonb DEFAULT '{}'::jsonb,
  p_priority int DEFAULT 100,
  p_available_at timestamptz DEFAULT now(),
  p_dedupe_key text DEFAULT NULL,
  p_correlation_id text DEFAULT NULL,
  p_lead_id text DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_id bigint;
  v_existing bigint;
BEGIN
  IF p_job_type IS NULL THEN
    RAISE EXCEPTION 'enqueue_job: job_type required';
  END IF;

  IF p_dedupe_key IS NOT NULL THEN
    SELECT id INTO v_existing FROM app_iseo_sales.jobs WHERE dedupe_key = p_dedupe_key;
    IF v_existing IS NOT NULL THEN
      RETURN jsonb_build_object('id', v_existing, 'idempotent_replay', true);
    END IF;
  END IF;

  BEGIN
    INSERT INTO app_iseo_sales.jobs (
      job_type, payload, priority, available_at, dedupe_key, correlation_id, lead_id, status
    ) VALUES (
      p_job_type, COALESCE(p_payload, '{}'::jsonb), COALESCE(p_priority, 100),
      COALESCE(p_available_at, now()), p_dedupe_key, p_correlation_id, p_lead_id, 'pending'
    )
    RETURNING id INTO v_id;
  EXCEPTION
    WHEN unique_violation THEN
      SELECT id INTO v_id FROM app_iseo_sales.jobs WHERE dedupe_key = p_dedupe_key;
      RETURN jsonb_build_object('id', v_id, 'idempotent_replay', true);
  END;

  RETURN jsonb_build_object('id', v_id, 'idempotent_replay', false);
END;
$$;

-- ---------------------------------------------------------------------------
-- 6) get_lead
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.get_lead(
  p_lead_id text
) RETURNS jsonb
LANGUAGE plpgsql
STABLE
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_row jsonb;
BEGIN
  SELECT to_jsonb(l) INTO v_row
  FROM app_iseo_sales.leads l
  WHERE l.lead_id = p_lead_id;

  IF v_row IS NULL THEN
    RETURN jsonb_build_object('found', false, 'lead_id', p_lead_id);
  END IF;

  RETURN jsonb_build_object('found', true, 'lead', v_row);
END;
$$;

-- ---------------------------------------------------------------------------
-- 7) list_pending_leads
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.list_pending_leads(
  p_limit int DEFAULT 50
) RETURNS SETOF jsonb
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
  SELECT to_jsonb(l)
  FROM app_iseo_sales.leads l
  WHERE l.manager_status IN ('new', 'pending', 'reopened', 'reviewing')
  ORDER BY l.updated_at ASC
  LIMIT GREATEST(COALESCE(p_limit, 50), 1);
$$;

-- ---------------------------------------------------------------------------
-- 8) claim_jobs — FOR UPDATE SKIP LOCKED
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.claim_jobs(
  p_worker text,
  p_limit int DEFAULT 10,
  p_lease_seconds int DEFAULT 60
) RETURNS SETOF app_iseo_sales.jobs
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
BEGIN
  IF p_worker IS NULL OR btrim(p_worker) = '' THEN
    RAISE EXCEPTION 'claim_jobs: p_worker required';
  END IF;

  RETURN QUERY
  WITH cte AS (
    SELECT j.id
    FROM app_iseo_sales.jobs j
    WHERE j.status IN ('pending', 'retry')
      AND j.available_at <= now()
      AND (j.lease_until IS NULL OR j.lease_until < now())
    ORDER BY j.priority ASC, j.available_at ASC
    FOR UPDATE SKIP LOCKED
    LIMIT GREATEST(COALESCE(p_limit, 10), 1)
  )
  UPDATE app_iseo_sales.jobs j
  SET
    status = 'running',
    locked_by = p_worker,
    locked_at = now(),
    lease_until = now() + make_interval(secs => GREATEST(COALESCE(p_lease_seconds, 60), 1)),
    attempts = j.attempts + 1,
    updated_at = now()
  FROM cte
  WHERE j.id = cte.id
  RETURNING j.*;
END;
$$;

-- ---------------------------------------------------------------------------
-- Grants: EXECUTE
-- ---------------------------------------------------------------------------
REVOKE ALL ON FUNCTION app_iseo_sales.fn_is_allowed_status_transition(text, text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.register_inbound_event(text, text, jsonb, text, text, text, timestamptz, text, text, text, text, text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.upsert_lead(text, bigint, text, text, text, text, text, text, text, text, text, text, text, text, jsonb, text, text, text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.change_lead_status(text, int, text, text, text, text, text, text, text, text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.enqueue_delivery(text, text, text, text, text, jsonb, text, text, timestamptz, text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.enqueue_job(text, jsonb, int, timestamptz, text, text, text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.get_lead(text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.list_pending_leads(int) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.claim_jobs(text, int, int) FROM PUBLIC;

GRANT EXECUTE ON FUNCTION app_iseo_sales.register_inbound_event(text, text, jsonb, text, text, text, timestamptz, text, text, text, text, text) TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.upsert_lead(text, bigint, text, text, text, text, text, text, text, text, text, text, text, text, jsonb, text, text, text) TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.change_lead_status(text, int, text, text, text, text, text, text, text, text) TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.enqueue_delivery(text, text, text, text, text, jsonb, text, text, timestamptz, text) TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.enqueue_job(text, jsonb, int, timestamptz, text, text, text) TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.claim_jobs(text, int, int) TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.fn_is_allowed_status_transition(text, text) TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.get_lead(text) TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.list_pending_leads(int) TO iseo_runtime;

-- Agent / reader: read functions only
GRANT EXECUTE ON FUNCTION app_iseo_sales.get_lead(text) TO iseo_agent, iseo_reader;
GRANT EXECUTE ON FUNCTION app_iseo_sales.list_pending_leads(int) TO iseo_agent, iseo_reader;

INSERT INTO mars_core.schema_migrations (schema_name, version, checksum)
VALUES ('app_iseo_sales', '0003_functions', NULL)
ON CONFLICT DO NOTHING;
