-- app_iseo_sales 0005 — Operational.v3.dev runtime helper functions
-- Closed catalog for n8n / MARS DB Toolkit. No arbitrary SQL API.
-- Prerequisites: 0001–0004 applied.

-- ---------------------------------------------------------------------------
-- append_lead_event (immutable INSERT)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.append_lead_event(
  p_lead_id text,
  p_event_type text,
  p_payload jsonb DEFAULT '{}'::jsonb,
  p_actor_type text DEFAULT 'workflow',
  p_actor_id text DEFAULT NULL,
  p_correlation_id text DEFAULT NULL,
  p_causation_id text DEFAULT NULL,
  p_workflow_version text DEFAULT NULL,
  p_event_id text DEFAULT NULL,
  p_occurred_at timestamptz DEFAULT now()
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_id bigint;
  v_event_id text;
BEGIN
  IF p_lead_id IS NULL OR btrim(p_lead_id) = '' THEN
    RAISE EXCEPTION 'append_lead_event: p_lead_id required';
  END IF;
  IF p_event_type IS NULL OR btrim(p_event_type) = '' THEN
    RAISE EXCEPTION 'append_lead_event: p_event_type required';
  END IF;

  v_event_id := COALESCE(NULLIF(btrim(p_event_id), ''), 'evt-' || gen_random_uuid()::text);

  INSERT INTO app_iseo_sales.lead_events (
    event_id, lead_id, event_type, occurred_at, actor_type, actor_id,
    correlation_id, causation_id, workflow_version, payload
  ) VALUES (
    v_event_id, p_lead_id, p_event_type, COALESCE(p_occurred_at, now()),
    COALESCE(p_actor_type, 'workflow'), p_actor_id,
    p_correlation_id, p_causation_id, p_workflow_version,
    COALESCE(p_payload, '{}'::jsonb)
  )
  ON CONFLICT (event_id) DO NOTHING
  RETURNING id INTO v_id;

  IF v_id IS NULL THEN
    SELECT id INTO v_id FROM app_iseo_sales.lead_events WHERE event_id = v_event_id;
    RETURN jsonb_build_object(
      'id', v_id,
      'event_id', v_event_id,
      'idempotent_replay', true
    );
  END IF;

  RETURN jsonb_build_object(
    'id', v_id,
    'event_id', v_event_id,
    'idempotent_replay', false
  );
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.append_lead_event IS
  'Immutable lead_events insert; event_id unique for idempotent replay';

-- ---------------------------------------------------------------------------
-- mark_inbound_processed
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.mark_inbound_processed(
  p_source_system text,
  p_source_id text,
  p_status text DEFAULT 'processed',
  p_lead_id text DEFAULT NULL,
  p_error_message text DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_id bigint;
  v_status text;
BEGIN
  IF p_source_id IS NULL OR btrim(p_source_id) = '' THEN
    RAISE EXCEPTION 'mark_inbound_processed: p_source_id required';
  END IF;

  v_status := COALESCE(NULLIF(btrim(p_status), ''), 'processed');
  -- Map aliases onto ck_inbound_events_processing_status
  IF v_status IN ('error') THEN
    v_status := 'failed';
  ELSIF v_status IN ('ignored') THEN
    v_status := 'skipped';
  END IF;
  IF v_status NOT IN ('received', 'processing', 'processed', 'failed', 'deferred', 'skipped') THEN
    v_status := 'processed';
  END IF;

  UPDATE app_iseo_sales.inbound_events
  SET
    processing_status = v_status,
    lead_id = COALESCE(p_lead_id, lead_id),
    parse_status = CASE
      WHEN v_status = 'failed' THEN COALESCE(NULLIF(btrim(p_error_message), ''), parse_status)
      ELSE parse_status
    END,
    updated_at = now()
  WHERE source_system = COALESCE(p_source_system, 'gmail')
    AND source_id = p_source_id
  RETURNING id INTO v_id;

  IF v_id IS NULL THEN
    RAISE EXCEPTION 'mark_inbound_processed: inbound not found for % / %',
      COALESCE(p_source_system, 'gmail'), p_source_id;
  END IF;

  RETURN jsonb_build_object(
    'id', v_id,
    'source_system', COALESCE(p_source_system, 'gmail'),
    'source_id', p_source_id,
    'processing_status', v_status
  );
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.mark_inbound_processed IS
  'Commit inbound processing_status after durable lead/event/delivery state';

-- ---------------------------------------------------------------------------
-- record_error (sanitized application errors)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.record_error(
  p_app_component text DEFAULT 'operational',
  p_workflow_version text DEFAULT NULL,
  p_n8n_execution_id text DEFAULT NULL,
  p_correlation_id text DEFAULT NULL,
  p_entity_type text DEFAULT NULL,
  p_entity_id text DEFAULT NULL,
  p_error_class text DEFAULT NULL,
  p_provider text DEFAULT NULL,
  p_code text DEFAULT NULL,
  p_http_status int DEFAULT NULL,
  p_stage text DEFAULT NULL,
  p_retryable boolean DEFAULT false,
  p_message_sanitized text DEFAULT NULL,
  p_context_sanitized jsonb DEFAULT '{}'::jsonb
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_id bigint;
BEGIN
  INSERT INTO app_iseo_sales.errors (
    app_component, workflow_version, n8n_execution_id, correlation_id,
    entity_type, entity_id, error_class, provider, code, http_status,
    stage, retryable, message_sanitized, context
  ) VALUES (
    COALESCE(p_app_component, 'operational'),
    p_workflow_version, p_n8n_execution_id, p_correlation_id,
    p_entity_type, p_entity_id, p_error_class, p_provider, p_code, p_http_status,
    p_stage, COALESCE(p_retryable, false), p_message_sanitized,
    COALESCE(p_context_sanitized, '{}'::jsonb)
  )
  RETURNING id INTO v_id;

  RETURN jsonb_build_object('id', v_id);
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.record_error IS
  'Append sanitized error row; never store secrets/PII in message/context';

-- ---------------------------------------------------------------------------
-- get_active_config (non-secret config values)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.get_active_config(
  p_keys text[] DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_out jsonb := '{}'::jsonb;
BEGIN
  SELECT COALESCE(jsonb_object_agg(c.key, c.value), '{}'::jsonb)
  INTO v_out
  FROM app_iseo_sales.config c
  WHERE COALESCE(c.is_secretish, false) = false
    AND (p_keys IS NULL OR c.key = ANY (p_keys));

  RETURN jsonb_build_object('config', COALESCE(v_out, '{}'::jsonb));
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.get_active_config IS
  'Read active non-secret config keys from app_iseo_sales.config';

-- ---------------------------------------------------------------------------
-- list_delivery_recipients (from access_rules; no ACCESS redesign)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.list_delivery_recipients(
  p_delivery_type text DEFAULT 'lead_card'
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_rows jsonb;
BEGIN
  SELECT COALESCE(jsonb_agg(jsonb_build_object(
    'principal_key', a.principal_key,
    'telegram_user_id', a.telegram_user_id,
    'role', a.role,
    'receives_cards', a.receives_cards,
    'receives_reminders', a.receives_reminders
  ) ORDER BY a.principal_key), '[]'::jsonb)
  INTO v_rows
  FROM app_iseo_sales.access_rules a
  WHERE a.is_active = true
    AND a.revoked_at IS NULL
    AND (
      (COALESCE(p_delivery_type, 'lead_card') = 'lead_card' AND a.receives_cards = true)
      OR (p_delivery_type = 'reminder' AND a.receives_reminders = true)
      OR (p_delivery_type NOT IN ('lead_card', 'reminder'))
    );

  RETURN jsonb_build_object('recipients', COALESCE(v_rows, '[]'::jsonb));
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.list_delivery_recipients IS
  'Active access_rules recipients for delivery enqueue (read-only ACL)';

-- ---------------------------------------------------------------------------
-- claim_pending_deliveries
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.claim_pending_deliveries(
  p_worker_id text,
  p_limit int DEFAULT 10,
  p_lease_seconds int DEFAULT 120
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_rows jsonb;
BEGIN
  IF p_worker_id IS NULL OR btrim(p_worker_id) = '' THEN
    RAISE EXCEPTION 'claim_pending_deliveries: p_worker_id required';
  END IF;

  WITH cte AS (
    SELECT d.id
    FROM app_iseo_sales.deliveries d
    WHERE d.status IN ('pending', 'retry')
      AND d.available_at <= now()
      AND (d.lease_until IS NULL OR d.lease_until < now())
      AND d.attempts < d.max_attempts
    ORDER BY d.available_at ASC, d.id ASC
    FOR UPDATE SKIP LOCKED
    LIMIT GREATEST(COALESCE(p_limit, 10), 1)
  ),
  upd AS (
    UPDATE app_iseo_sales.deliveries d
    SET
      status = 'processing',
      locked_by = p_worker_id,
      locked_at = now(),
      lease_until = now() + make_interval(secs => GREATEST(COALESCE(p_lease_seconds, 120), 30)),
      attempts = d.attempts + 1,
      updated_at = now()
    FROM cte
    WHERE d.id = cte.id
    RETURNING d.id, d.delivery_id, d.lead_id, d.channel, d.recipient_principal_key,
      d.recipient_telegram_user_id, d.delivery_type, d.payload, d.status,
      d.attempts, d.idempotency_key, d.correlation_id
  )
  SELECT COALESCE(jsonb_agg(to_jsonb(upd) ORDER BY upd.id), '[]'::jsonb)
  INTO v_rows
  FROM upd;

  RETURN jsonb_build_object(
    'claimed', COALESCE(v_rows, '[]'::jsonb),
    'worker_id', p_worker_id,
    'count', COALESCE(jsonb_array_length(COALESCE(v_rows, '[]'::jsonb)), 0)
  );
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.claim_pending_deliveries IS
  'Lease pending/retry deliveries for outbox worker';

-- ---------------------------------------------------------------------------
-- mark_delivery_result
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.mark_delivery_result(
  p_delivery_id text,
  p_status text,
  p_external_message_id text DEFAULT NULL,
  p_telegram_chat_id text DEFAULT NULL,
  p_error_id bigint DEFAULT NULL,
  p_retry_after_seconds int DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_id bigint;
  v_status text;
BEGIN
  v_status := COALESCE(NULLIF(btrim(p_status), ''), 'sent');
  IF v_status NOT IN ('pending', 'processing', 'sent', 'retry', 'dead', 'cancelled') THEN
    RAISE EXCEPTION 'mark_delivery_result: invalid status %', v_status;
  END IF;

  UPDATE app_iseo_sales.deliveries
  SET
    status = v_status,
    sent_at = CASE WHEN v_status = 'sent' THEN now() ELSE sent_at END,
    external_message_id = COALESCE(p_external_message_id, external_message_id),
    telegram_chat_id = COALESCE(p_telegram_chat_id, telegram_chat_id),
    last_error_id = COALESCE(p_error_id, last_error_id),
    available_at = CASE
      WHEN v_status = 'retry' THEN now() + make_interval(secs => GREATEST(COALESCE(p_retry_after_seconds, 60), 5))
      ELSE available_at
    END,
    locked_by = NULL,
    locked_at = NULL,
    lease_until = NULL,
    updated_at = now()
  WHERE delivery_id = p_delivery_id
  RETURNING id INTO v_id;

  IF v_id IS NULL THEN
    RAISE EXCEPTION 'mark_delivery_result: delivery_id not found %', p_delivery_id;
  END IF;

  RETURN jsonb_build_object('id', v_id, 'delivery_id', p_delivery_id, 'status', v_status);
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.mark_delivery_result IS
  'Finalize delivery outbox row after send/retry/dead';

-- ---------------------------------------------------------------------------
-- process_gmail_inbound_commit — atomic business commit point for v3
-- Persists inbound (idempotent) + lead upsert + event + delivery intents.
-- Does NOT touch Gmail labels; caller finalizes Gmail only after success.
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.process_gmail_inbound_commit(
  p_source_id text,
  p_lead_id text,
  p_payload jsonb DEFAULT '{}'::jsonb,
  p_raw_text text DEFAULT NULL,
  p_correlation_id text DEFAULT NULL,
  p_gmail_thread_id text DEFAULT NULL,
  p_received_at timestamptz DEFAULT NULL,
  p_subject text DEFAULT NULL,
  p_from_email text DEFAULT NULL,
  p_normalized_hash text DEFAULT NULL,
  p_parser_version text DEFAULT 'v3-pg',
  p_workflow_version text DEFAULT 'Operational.v3.dev',
  p_client_name text DEFAULT NULL,
  p_primary_contact text DEFAULT NULL,
  p_contact_type text DEFAULT NULL,
  p_phone text DEFAULT NULL,
  p_email text DEFAULT NULL,
  p_messenger text DEFAULT NULL,
  p_site text DEFAULT NULL,
  p_service text DEFAULT NULL,
  p_summary text DEFAULT NULL,
  p_source text DEFAULT 'gmail',
  p_manager_status text DEFAULT 'new',
  p_form_metadata jsonb DEFAULT '{}'::jsonb,
  p_data_contract_version text DEFAULT 'iseo-sales-v1',
  p_enqueue_telegram boolean DEFAULT true,
  p_card_payload jsonb DEFAULT '{}'::jsonb,
  p_event_type text DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_inbound jsonb;
  v_lead jsonb;
  v_event jsonb;
  v_recipients jsonb;
  v_rec jsonb;
  v_deliveries jsonb := '[]'::jsonb;
  v_delivery jsonb;
  v_inbound_id bigint;
  v_is_dup boolean;
  v_event_type text;
  v_idem text;
  v_evt_id text;
BEGIN
  IF p_source_id IS NULL OR btrim(p_source_id) = '' THEN
    RAISE EXCEPTION 'process_gmail_inbound_commit: p_source_id required';
  END IF;
  IF p_lead_id IS NULL OR btrim(p_lead_id) = '' THEN
    RAISE EXCEPTION 'process_gmail_inbound_commit: p_lead_id required';
  END IF;

  v_inbound := app_iseo_sales.register_inbound_event(
    'gmail', p_source_id, COALESCE(p_payload, '{}'::jsonb), p_raw_text,
    p_correlation_id, p_gmail_thread_id, p_received_at, p_subject, p_from_email,
    p_normalized_hash, p_parser_version, p_workflow_version
  );
  v_inbound_id := (v_inbound->>'id')::bigint;
  v_is_dup := COALESCE((v_inbound->>'is_duplicate')::boolean, false);

  -- Enrich inbound snapshot for recovery short-circuit
  SELECT jsonb_build_object(
    'id', ie.id,
    'is_duplicate', v_is_dup,
    'source_system', ie.source_system,
    'source_id', ie.source_id,
    'processing_status', ie.processing_status,
    'lead_id', ie.lead_id
  )
  INTO v_inbound
  FROM app_iseo_sales.inbound_events ie
  WHERE ie.id = v_inbound_id;

  -- Gmail finalize recovery: if already fully committed, do not mutate business state
  IF v_is_dup
     AND COALESCE(v_inbound->>'processing_status', '') = 'processed' THEN
    RETURN jsonb_build_object(
      'ok', true,
      'inbound', v_inbound,
      'lead', jsonb_build_object('lead_id', COALESCE(v_inbound->>'lead_id', p_lead_id)),
      'event', jsonb_build_object('idempotent_replay', true),
      'deliveries', '[]'::jsonb,
      'gmail_finalize_allowed', true,
      'inbound_was_duplicate', true,
      'already_committed', true,
      'commit_point', 'inbound+lead+event+delivery_intents'
    );
  END IF;

  -- Mark processing while committing
  UPDATE app_iseo_sales.inbound_events
  SET processing_status = 'processing', updated_at = now()
  WHERE id = v_inbound_id
    AND processing_status IS DISTINCT FROM 'processed';

  v_lead := app_iseo_sales.upsert_lead(
    p_lead_id, v_inbound_id, p_source_id, p_client_name, p_primary_contact,
    p_contact_type, p_phone, p_email, p_messenger, p_site, p_service, p_summary,
    p_source, COALESCE(p_manager_status, 'new'), p_form_metadata,
    p_data_contract_version, p_workflow_version, p_parser_version
  );

  v_event_type := COALESCE(
    NULLIF(btrim(p_event_type), ''),
    CASE WHEN COALESCE((v_lead->>'inserted')::boolean, false) THEN 'lead_created' ELSE 'lead_updated' END
  );
  v_evt_id := 'evt-' || p_source_id || '-' || v_event_type;
  v_event := app_iseo_sales.append_lead_event(
    p_lead_id, v_event_type, jsonb_build_object(
      'source_id', p_source_id,
      'inbound_event_id', v_inbound_id,
      'lead', v_lead
    ),
    'workflow', 'Operational.v3.dev', p_correlation_id, NULL,
    p_workflow_version, v_evt_id, now()
  );

  IF COALESCE(p_enqueue_telegram, true) THEN
    v_recipients := app_iseo_sales.list_delivery_recipients('lead_card');
    FOR v_rec IN
      SELECT * FROM jsonb_array_elements(COALESCE(v_recipients->'recipients', '[]'::jsonb))
    LOOP
      v_idem := 'lead_card:' || p_lead_id || ':' || COALESCE(v_rec->>'principal_key', 'unknown') || ':' || p_source_id;
      v_delivery := app_iseo_sales.enqueue_delivery(
        p_lead_id,
        'telegram',
        v_rec->>'principal_key',
        v_rec->>'telegram_user_id',
        'lead_card',
        COALESCE(p_card_payload, '{}'::jsonb) || jsonb_build_object(
          'principal_key', v_rec->>'principal_key',
          'dry_run_default', true
        ),
        v_idem,
        p_correlation_id,
        now(),
        NULL
      );
      v_deliveries := v_deliveries || jsonb_build_array(v_delivery);
    END LOOP;
  END IF;

  -- Durable commit marker on inbound (Gmail finalize is separate, after this returns)
  PERFORM app_iseo_sales.mark_inbound_processed(
    'gmail', p_source_id, 'processed', p_lead_id, NULL
  );

  RETURN jsonb_build_object(
    'ok', true,
    'inbound', v_inbound,
    'lead', v_lead,
    'event', v_event,
    'deliveries', v_deliveries,
    'gmail_finalize_allowed', true,
    'inbound_was_duplicate', v_is_dup,
    'commit_point', 'inbound+lead+event+delivery_intents'
  );
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.process_gmail_inbound_commit IS
  'Atomic PG commit for Gmail inbound; Gmail labels only after this succeeds';

-- Grants
GRANT EXECUTE ON FUNCTION app_iseo_sales.append_lead_event TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.mark_inbound_processed TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.record_error TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.get_active_config TO iseo_runtime, iseo_agent, iseo_reader;
GRANT EXECUTE ON FUNCTION app_iseo_sales.list_delivery_recipients TO iseo_runtime, iseo_agent;
GRANT EXECUTE ON FUNCTION app_iseo_sales.claim_pending_deliveries TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.mark_delivery_result TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.process_gmail_inbound_commit TO iseo_runtime;

INSERT INTO mars_core.schema_migrations (schema_name, version, checksum)
VALUES ('app_iseo_sales', '0005_v3_runtime_functions', NULL)
ON CONFLICT DO NOTHING;
