-- app_iseo_sales Admin.v3.dev runtime functions
-- Prerequisites: 0001–0005
-- Role grants: iseo_runtime (least privilege). No execute_sql / generic_update.

SET search_path = app_iseo_sales, mars_core, pg_temp;

-- ---------------------------------------------------------------------------
-- check_access — ACCESS parity (read-only authority from access_rules)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.check_access(
  p_telegram_user_id text DEFAULT NULL,
  p_principal_key text DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_row app_iseo_sales.access_rules%ROWTYPE;
BEGIN
  IF (p_telegram_user_id IS NULL OR btrim(p_telegram_user_id) = '')
     AND (p_principal_key IS NULL OR btrim(p_principal_key) = '') THEN
    RETURN jsonb_build_object(
      'authorized', false,
      'reason', 'missing_actor'
    );
  END IF;

  IF p_principal_key IS NOT NULL AND btrim(p_principal_key) <> '' THEN
    SELECT * INTO v_row
    FROM app_iseo_sales.access_rules
    WHERE principal_key = p_principal_key;
  ELSE
    SELECT * INTO v_row
    FROM app_iseo_sales.access_rules
    WHERE telegram_user_id = p_telegram_user_id
    ORDER BY is_active DESC, updated_at DESC
    LIMIT 1;
  END IF;

  IF NOT FOUND THEN
    RETURN jsonb_build_object(
      'authorized', false,
      'reason', 'unknown_actor',
      'telegram_user_id', p_telegram_user_id,
      'principal_key', p_principal_key
    );
  END IF;

  RETURN jsonb_build_object(
    'authorized', COALESCE(v_row.is_active, false),
    'reason', CASE WHEN v_row.is_active THEN 'ok' ELSE 'revoked' END,
    'principal_key', v_row.principal_key,
    'role', v_row.role,
    'display_name', v_row.display_name,
    'is_active', v_row.is_active,
    'receives_cards', v_row.receives_cards,
    'receives_reminders', v_row.receives_reminders,
    'revoked_at', v_row.revoked_at
  );
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.check_access IS
  'Admin.v3 ACCESS check against access_rules; does not mutate ACL';

-- ---------------------------------------------------------------------------
-- set_config_value — non-secret app flags only (AI on/off etc.)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.set_config_value(
  p_key text,
  p_value text,
  p_updated_by text DEFAULT 'admin',
  p_value_type text DEFAULT 'string',
  p_description text DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_row app_iseo_sales.config%ROWTYPE;
  v_forbidden text[] := ARRAY[
    'bot_token', 'telegram_token', 'oauth', 'password', 'api_key',
    'n8n_api_key', 'encryption_key', 'client_secret'
  ];
  k text;
BEGIN
  IF p_key IS NULL OR btrim(p_key) = '' THEN
    RAISE EXCEPTION 'set_config_value: key required';
  END IF;

  FOREACH k IN ARRAY v_forbidden LOOP
    IF lower(p_key) LIKE '%' || k || '%' THEN
      RAISE EXCEPTION 'set_config_value: key % rejected (secret contour)', p_key;
    END IF;
  END LOOP;

  INSERT INTO app_iseo_sales.config AS c (
    key, value, value_type, description, updated_at, updated_by, is_secretish
  ) VALUES (
    p_key, p_value, COALESCE(p_value_type, 'string'), p_description,
    now(), COALESCE(p_updated_by, 'admin'), false
  )
  ON CONFLICT (key) DO UPDATE
  SET
    value = EXCLUDED.value,
    value_type = EXCLUDED.value_type,
    description = COALESCE(EXCLUDED.description, c.description),
    updated_at = now(),
    updated_by = EXCLUDED.updated_by,
    is_secretish = false
  WHERE COALESCE(c.is_secretish, false) = false
  RETURNING * INTO v_row;

  IF NOT FOUND THEN
    RAISE EXCEPTION 'set_config_value: refused secretish key %', p_key;
  END IF;

  INSERT INTO app_iseo_sales.audit_logs (
    actor_type, actor_id, action, entity_type, entity_id, result, detail
  ) VALUES (
    'admin', p_updated_by, 'set_config_value', 'config', p_key, 'success',
    jsonb_build_object('value_type', v_row.value_type)
  );

  RETURN jsonb_build_object(
    'ok', true,
    'key', v_row.key,
    'value', v_row.value,
    'updated_at', v_row.updated_at,
    'updated_by', v_row.updated_by
  );
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.set_config_value IS
  'Upsert non-secret config; rejects secret-like keys; secrets stay outside PG';

-- ---------------------------------------------------------------------------
-- get_admin_health — component status; never abort whole payload
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.get_admin_health()
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_pg text := 'ok';
  v_leads bigint := 0;
  v_access bigint := 0;
  v_err bigint := 0;
  v_ai text := 'unknown';
  v_overall text := 'ok';
BEGIN
  BEGIN
    SELECT count(*) INTO v_leads FROM app_iseo_sales.leads;
    SELECT count(*) INTO v_access FROM app_iseo_sales.access_rules WHERE is_active;
    SELECT count(*) INTO v_err FROM app_iseo_sales.errors WHERE resolved = false;
  EXCEPTION WHEN OTHERS THEN
    v_pg := 'error';
    v_overall := 'degraded';
  END;

  BEGIN
    SELECT COALESCE(c.value, 'off') INTO v_ai
    FROM app_iseo_sales.config c
    WHERE c.key IN ('ai.enabled', 'AI_ENABLED', 'ai_status')
    ORDER BY CASE c.key WHEN 'ai.enabled' THEN 0 WHEN 'AI_ENABLED' THEN 1 ELSE 2 END
    LIMIT 1;
  EXCEPTION WHEN OTHERS THEN
    v_ai := 'unavailable';
  END;

  IF v_pg <> 'ok' THEN
    v_overall := 'error';
  ELSIF v_err > 50 THEN
    v_overall := 'degraded';
  END IF;

  RETURN jsonb_build_object(
    'overall', v_overall,
    'components', jsonb_build_object(
      'postgresql', jsonb_build_object('status', v_pg, 'leads', v_leads, 'active_access', v_access),
      'telegram', jsonb_build_object('status', 'not_probed_in_candidate', 'note', 'live probe deferred to cutover'),
      'gmail_operational', jsonb_build_object('status', 'external', 'note', 'inspect Operational.v3 / Operational.dev separately'),
      'ai', jsonb_build_object('status', COALESCE(v_ai, 'off')),
      'unresolved_errors', jsonb_build_object('count', v_err)
    ),
    'sheets_critical_dependency', false
  );
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.get_admin_health IS
  'Component health for /health; returns degraded/error without aborting response';

-- ---------------------------------------------------------------------------
-- get_admin_status_snapshot / get_admin_stats
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.get_admin_status_snapshot()
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_by_status jsonb;
  v_ai text;
BEGIN
  SELECT COALESCE(jsonb_object_agg(manager_status, cnt), '{}'::jsonb)
  INTO v_by_status
  FROM (
    SELECT manager_status, count(*)::int AS cnt
    FROM app_iseo_sales.leads
    GROUP BY manager_status
  ) s;

  SELECT value INTO v_ai
  FROM app_iseo_sales.config
  WHERE key IN ('ai.enabled', 'AI_ENABLED')
  ORDER BY CASE key WHEN 'ai.enabled' THEN 0 ELSE 1 END
  LIMIT 1;

  RETURN jsonb_build_object(
    'authority', 'postgresql',
    'lead_counts_by_status', COALESCE(v_by_status, '{}'::jsonb),
    'ai_enabled', COALESCE(v_ai, 'off'),
    'active_access_count', (SELECT count(*) FROM app_iseo_sales.access_rules WHERE is_active),
    'pending_deliveries', (
      SELECT count(*) FROM app_iseo_sales.deliveries WHERE status IN ('pending', 'processing', 'retry')
    )
  );
END;
$$;

CREATE OR REPLACE FUNCTION app_iseo_sales.get_admin_stats()
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_snap jsonb;
BEGIN
  v_snap := app_iseo_sales.get_admin_status_snapshot();
  RETURN jsonb_build_object(
    'available_from_pg', v_snap,
    'legacy_history_only', jsonb_build_object(
      'note', 'Pre-migration Sheets historical metrics not reconstructed',
      'classification', 'LEGACY HISTORY ONLY'
    ),
    'deferred', jsonb_build_object(
      'classification', 'DEFERRED',
      'items', jsonb_build_array('long_window_sheets_quota_charts', 'pre_pg_error_rate_series')
    )
  );
END;
$$;

-- ---------------------------------------------------------------------------
-- get_last_error
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.get_last_error(
  p_limit int DEFAULT 5
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_rows jsonb;
BEGIN
  SELECT COALESCE(jsonb_agg(row_to_json(x)::jsonb ORDER BY x.created_at DESC), '[]'::jsonb)
  INTO v_rows
  FROM (
    SELECT id, created_at, app_component, error_class, provider, stage,
           retryable, resolved, message_sanitized
    FROM app_iseo_sales.errors
    ORDER BY created_at DESC
    LIMIT GREATEST(1, LEAST(COALESCE(p_limit, 5), 50))
  ) x;

  RETURN jsonb_build_object('errors', COALESCE(v_rows, '[]'::jsonb), 'authority', 'postgresql');
END;
$$;

-- ---------------------------------------------------------------------------
-- list_leads_page
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.list_leads_page(
  p_statuses text[] DEFAULT NULL,
  p_limit int DEFAULT 20,
  p_offset int DEFAULT 0,
  p_site text DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_rows jsonb;
  v_total bigint;
  v_lim int := GREATEST(1, LEAST(COALESCE(p_limit, 20), 100));
  v_off int := GREATEST(0, COALESCE(p_offset, 0));
BEGIN
  SELECT count(*) INTO v_total
  FROM app_iseo_sales.leads l
  WHERE (p_statuses IS NULL OR l.manager_status = ANY (p_statuses))
    AND (p_site IS NULL OR l.site = p_site);

  SELECT COALESCE(jsonb_agg(jsonb_build_object(
    'lead_id', q.lead_id,
    'manager_status', q.manager_status,
    'version', q.version,
    'site', q.site,
    'client_name', q.client_name,
    'updated_at', q.updated_at
  ) ORDER BY q.updated_at DESC), '[]'::jsonb)
  INTO v_rows
  FROM (
    SELECT lead_id, manager_status, version, site, client_name, updated_at
    FROM app_iseo_sales.leads l
    WHERE (p_statuses IS NULL OR l.manager_status = ANY (p_statuses))
      AND (p_site IS NULL OR l.site = p_site)
    ORDER BY updated_at DESC
    LIMIT v_lim OFFSET v_off
  ) q;

  RETURN jsonb_build_object(
    'total', v_total,
    'limit', v_lim,
    'offset', v_off,
    'leads', COALESCE(v_rows, '[]'::jsonb),
    'authority', 'postgresql'
  );
END;
$$;

-- ---------------------------------------------------------------------------
-- Reminder groups (pending actionable leads)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.list_pending_lead_groups()
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_rows jsonb;
BEGIN
  SELECT COALESCE(jsonb_agg(jsonb_build_object(
    'group_key', g.group_key,
    'site', g.site,
    'count', g.cnt
  ) ORDER BY g.cnt DESC, g.group_key), '[]'::jsonb)
  INTO v_rows
  FROM (
    SELECT
      COALESCE(NULLIF(btrim(site), ''), '_unknown') AS group_key,
      COALESCE(NULLIF(btrim(site), ''), '_unknown') AS site,
      count(*)::int AS cnt
    FROM app_iseo_sales.leads
    WHERE manager_status IN ('new', 'pending', 'reopened', 'reviewing')
    GROUP BY 1, 2
  ) g;

  RETURN jsonb_build_object(
    'groups', COALESCE(v_rows, '[]'::jsonb),
    'authority', 'postgresql',
    'sheets_dependency', false
  );
END;
$$;

CREATE OR REPLACE FUNCTION app_iseo_sales.get_pending_leads_in_group(
  p_group_key text,
  p_limit int DEFAULT 50
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_rows jsonb;
  v_gk text := COALESCE(NULLIF(btrim(p_group_key), ''), '_unknown');
BEGIN
  SELECT COALESCE(jsonb_agg(jsonb_build_object(
    'lead_id', q.lead_id,
    'manager_status', q.manager_status,
    'version', q.version,
    'site', q.site,
    'client_name', q.client_name,
    'updated_at', q.updated_at
  ) ORDER BY q.updated_at ASC), '[]'::jsonb)
  INTO v_rows
  FROM (
    SELECT lead_id, manager_status, version, site, client_name, updated_at
    FROM app_iseo_sales.leads
    WHERE manager_status IN ('new', 'pending', 'reopened', 'reviewing')
      AND COALESCE(NULLIF(btrim(site), ''), '_unknown') = v_gk
    ORDER BY updated_at ASC
    LIMIT GREATEST(1, LEAST(COALESCE(p_limit, 50), 200))
  ) q;

  RETURN jsonb_build_object(
    'group_key', v_gk,
    'leads', COALESCE(v_rows, '[]'::jsonb),
    'authority', 'postgresql'
  );
END;
$$;

-- ---------------------------------------------------------------------------
-- Canonical lead card payload (no Telegram send)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.get_lead_card_payload(
  p_lead_id text
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_lead app_iseo_sales.leads%ROWTYPE;
  v_pending boolean;
  v_actions jsonb;
  v_delivery jsonb;
BEGIN
  SELECT * INTO v_lead FROM app_iseo_sales.leads WHERE lead_id = p_lead_id;
  IF NOT FOUND THEN
    RETURN jsonb_build_object('ok', false, 'reason', 'lead_not_found');
  END IF;

  v_pending := v_lead.manager_status IN ('new', 'pending', 'reopened', 'reviewing');

  IF v_pending THEN
    v_actions := jsonb_build_array(
      jsonb_build_object('id', 'processed', 'label', E'\u2705 \u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043e'),
      jsonb_build_object('id', 'spam', 'label', E'\ud83d\udeab \u0421\u043f\u0430\u043c'),
      jsonb_build_object('id', 'source', 'label', E'\ud83d\udcc4 \u0418\u0441\u0445\u043e\u0434\u043d\u0430\u044f \u0437\u0430\u044f\u0432\u043a\u0430')
    );
  ELSE
    v_actions := jsonb_build_array(
      jsonb_build_object('id', 'source', 'label', E'\ud83d\udcc4 \u0418\u0441\u0445\u043e\u0434\u043d\u0430\u044f \u0437\u0430\u044f\u0432\u043a\u0430')
    );
  END IF;

  SELECT jsonb_build_object(
    'delivery_id', d.delivery_id,
    'external_message_id', d.external_message_id,
    'status', d.status,
    'delivery_type', d.delivery_type,
    'recipient_principal_key', d.recipient_principal_key
  )
  INTO v_delivery
  FROM app_iseo_sales.deliveries d
  WHERE d.lead_id = p_lead_id
    AND d.delivery_type IN ('lead_card', 'lead_card_sync')
    AND COALESCE(d.external_message_id, '') <> 'LEGACY INVALID ROW'
  ORDER BY d.updated_at DESC NULLS LAST, d.id DESC
  LIMIT 1;

  RETURN jsonb_build_object(
    'ok', true,
    'lead_id', v_lead.lead_id,
    'manager_status', v_lead.manager_status,
    'version', v_lead.version,
    'lifecycle', CASE WHEN v_pending THEN 'pending_actionable' ELSE 'terminal' END,
    'card_kind', CASE WHEN v_pending THEN 'actionable' ELSE 'terminal' END,
    'forbid_stray_kartochka', true,
    'actions', v_actions,
    'summary', jsonb_build_object(
      'client_name', v_lead.client_name,
      'site', v_lead.site,
      'service', v_lead.service,
      'phone', v_lead.phone,
      'email', v_lead.email
    ),
    'latest_delivery', v_delivery,
    'authority', 'postgresql'
  );
END;
$$;

-- ---------------------------------------------------------------------------
-- admin_callback_lead_action — atomic status + card intent (idempotent)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.admin_callback_lead_action(
  p_lead_id text,
  p_action text,
  p_telegram_user_id text,
  p_callback_id text DEFAULT NULL,
  p_expected_version int DEFAULT NULL,
  p_from_status text DEFAULT NULL,
  p_correlation_id text DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_access jsonb;
  v_to text;
  v_idem text;
  v_status jsonb;
  v_card jsonb;
BEGIN
  v_access := app_iseo_sales.check_access(p_telegram_user_id, NULL);
  IF NOT COALESCE((v_access->>'authorized')::boolean, false) THEN
    INSERT INTO app_iseo_sales.audit_logs (
      actor_type, actor_id, action, entity_type, entity_id, correlation_id, result, detail
    ) VALUES (
      'moderator', p_telegram_user_id, 'admin_callback_lead_action', 'lead', p_lead_id,
      p_correlation_id, 'rejected', jsonb_build_object('access', v_access, 'action', p_action)
    );
    RETURN jsonb_build_object('ok', false, 'reason', 'access_denied', 'access', v_access);
  END IF;

  v_to := CASE lower(COALESCE(p_action, ''))
    WHEN 'processed' THEN 'processed'
    WHEN 'spam' THEN 'spam'
    ELSE NULL
  END;

  IF v_to IS NULL THEN
    IF lower(COALESCE(p_action, '')) = 'source' THEN
      v_card := app_iseo_sales.get_lead_card_payload(p_lead_id);
      RETURN jsonb_build_object(
        'ok', true,
        'action', 'source',
        'transition', false,
        'card', v_card,
        'note', 'source request — no status mutation'
      );
    END IF;
    RETURN jsonb_build_object('ok', false, 'reason', 'unknown_action', 'action', p_action);
  END IF;

  v_idem := COALESCE(
    NULLIF(btrim(p_callback_id), ''),
    'cb:' || p_lead_id || ':' || v_to || ':' || COALESCE(p_telegram_user_id, 'anon')
  );

  v_status := app_iseo_sales.change_lead_status(
    p_lead_id,
    p_expected_version,
    p_from_status,
    v_to,
    COALESCE(v_access->>'role', 'moderator'),
    COALESCE(v_access->>'principal_key', p_telegram_user_id),
    v_idem,
    p_correlation_id,
    NULL,
    'admin_callback:' || v_to
  );

  v_card := app_iseo_sales.get_lead_card_payload(p_lead_id);

  RETURN jsonb_build_object(
    'ok', true,
    'action', v_to,
    'transition', v_status,
    'card', v_card,
    'idempotency_key', v_idem
  );
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.admin_callback_lead_action IS
  'Validate ACCESS → change_lead_status (idempotent) → return canonical card payload';

-- ---------------------------------------------------------------------------
-- Reminder window claim/mark via jobs + deliveries (no Sheets)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.claim_reminder_window(
  p_window_key text,
  p_actor_id text DEFAULT 'admin-v3',
  p_ttl_seconds int DEFAULT 86400
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_job jsonb;
  v_dedupe text;
BEGIN
  IF p_window_key IS NULL OR btrim(p_window_key) = '' THEN
    RAISE EXCEPTION 'claim_reminder_window: window_key required';
  END IF;
  v_dedupe := 'reminder_window:' || p_window_key;
  v_job := app_iseo_sales.enqueue_job(
    'pending_reminder',
    jsonb_build_object('window_key', p_window_key, 'claimed_by', p_actor_id),
    40,
    now(),
    v_dedupe,
    'reminder-' || p_window_key,
    NULL
  );
  RETURN jsonb_build_object(
    'ok', true,
    'window_key', p_window_key,
    'job', v_job,
    'ttl_seconds', COALESCE(p_ttl_seconds, 86400)
  );
END;
$$;

CREATE OR REPLACE FUNCTION app_iseo_sales.record_reminder_delivery(
  p_window_key text,
  p_recipient_principal_key text,
  p_external_message_id text DEFAULT NULL,
  p_status text DEFAULT 'sent',
  p_correlation_id text DEFAULT NULL
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  v_delivery_id text;
  v_idem text;
BEGIN
  v_delivery_id := 'rem-' || p_window_key || '-' || COALESCE(p_recipient_principal_key, 'na');
  v_idem := 'reminder_delivery:' || p_window_key || ':' || COALESCE(p_recipient_principal_key, 'na');
  INSERT INTO app_iseo_sales.deliveries (
    delivery_id, lead_id, delivery_type, status, payload, idempotency_key,
    correlation_id, recipient_principal_key, external_message_id, sent_at
  ) VALUES (
    v_delivery_id,
    NULL,
    'reminder',
    CASE WHEN p_status IN ('pending','processing','sent','retry','dead','cancelled')
         THEN p_status ELSE 'sent' END,
    jsonb_build_object('window_key', p_window_key),
    v_idem,
    p_correlation_id,
    p_recipient_principal_key,
    CASE WHEN p_external_message_id = 'LEGACY INVALID ROW' THEN NULL ELSE p_external_message_id END,
    CASE WHEN p_status = 'sent' THEN now() ELSE NULL END
  )
  ON CONFLICT (idempotency_key) DO UPDATE
  SET
    status = EXCLUDED.status,
    external_message_id = COALESCE(EXCLUDED.external_message_id, app_iseo_sales.deliveries.external_message_id),
    updated_at = now()
  RETURNING delivery_id INTO v_delivery_id;

  RETURN jsonb_build_object('ok', true, 'delivery_id', v_delivery_id, 'idempotency_key', v_idem);
END;
$$;

-- ---------------------------------------------------------------------------
-- update_delivery_message_binding — card/message instance state
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.update_delivery_message_binding(
  p_delivery_id text,
  p_external_message_id text,
  p_telegram_chat_id text DEFAULT NULL,
  p_status text DEFAULT 'sent'
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
BEGIN
  IF p_external_message_id = 'LEGACY INVALID ROW' THEN
    RAISE EXCEPTION 'update_delivery_message_binding: LEGACY INVALID ROW forbidden';
  END IF;
  RETURN app_iseo_sales.mark_delivery_result(
    p_delivery_id, COALESCE(p_status, 'sent'), p_external_message_id, p_telegram_chat_id, NULL, NULL
  );
END;
$$;

-- ---------------------------------------------------------------------------
-- Closed-op dispatcher for Admin.v3 n8n node (allowlist only)
-- ---------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION app_iseo_sales.admin_runtime_call(
  p_op text,
  p_payload jsonb DEFAULT '{}'::jsonb
) RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = app_iseo_sales, mars_core, pg_temp
AS $$
DECLARE
  p jsonb := COALESCE(p_payload, '{}'::jsonb);
BEGIN
  CASE lower(COALESCE(p_op, ''))
    WHEN 'check_access' THEN
      RETURN app_iseo_sales.check_access(p->>'telegram_user_id', p->>'principal_key');
    WHEN 'get_admin_health' THEN
      RETURN app_iseo_sales.get_admin_health();
    WHEN 'get_admin_status' THEN
      RETURN app_iseo_sales.get_admin_status_snapshot();
    WHEN 'get_admin_stats' THEN
      RETURN app_iseo_sales.get_admin_stats();
    WHEN 'get_last_error' THEN
      RETURN app_iseo_sales.get_last_error(COALESCE((p->>'limit')::int, 5));
    WHEN 'get_active_config' THEN
      RETURN app_iseo_sales.get_active_config(
        CASE WHEN p ? 'keys' THEN ARRAY(SELECT jsonb_array_elements_text(p->'keys')) ELSE NULL END
      );
    WHEN 'set_config_value' THEN
      RETURN app_iseo_sales.set_config_value(
        p->>'key', p->>'value', COALESCE(p->>'updated_by', 'admin'),
        COALESCE(p->>'value_type', 'string'), p->>'description'
      );
    WHEN 'list_leads_page' THEN
      RETURN app_iseo_sales.list_leads_page(
        CASE WHEN p ? 'statuses' THEN ARRAY(SELECT jsonb_array_elements_text(p->'statuses')) ELSE NULL END,
        COALESCE((p->>'limit')::int, 20),
        COALESCE((p->>'offset')::int, 0),
        p->>'site'
      );
    WHEN 'list_pending_lead_groups' THEN
      RETURN app_iseo_sales.list_pending_lead_groups();
    WHEN 'get_pending_leads_in_group' THEN
      RETURN app_iseo_sales.get_pending_leads_in_group(
        p->>'group_key', COALESCE((p->>'limit')::int, 50)
      );
    WHEN 'get_lead_card_payload' THEN
      RETURN app_iseo_sales.get_lead_card_payload(p->>'lead_id');
    WHEN 'get_lead' THEN
      RETURN app_iseo_sales.get_lead(p->>'lead_id');
    WHEN 'admin_callback_lead_action' THEN
      RETURN app_iseo_sales.admin_callback_lead_action(
        p->>'lead_id', p->>'action', p->>'telegram_user_id',
        p->>'callback_id',
        CASE WHEN p ? 'expected_version' THEN (p->>'expected_version')::int ELSE NULL END,
        p->>'from_status', p->>'correlation_id'
      );
    WHEN 'claim_reminder_window' THEN
      RETURN app_iseo_sales.claim_reminder_window(
        p->>'window_key', COALESCE(p->>'actor_id', 'admin-v3'),
        COALESCE((p->>'ttl_seconds')::int, 86400)
      );
    WHEN 'record_reminder_delivery' THEN
      RETURN app_iseo_sales.record_reminder_delivery(
        p->>'window_key', p->>'recipient_principal_key',
        p->>'external_message_id', COALESCE(p->>'status', 'sent'), p->>'correlation_id'
      );
    WHEN 'update_delivery_message_binding' THEN
      RETURN app_iseo_sales.update_delivery_message_binding(
        p->>'delivery_id', p->>'external_message_id', p->>'telegram_chat_id',
        COALESCE(p->>'status', 'sent')
      );
    WHEN 'help' THEN
      RETURN jsonb_build_object(
        'commands', jsonb_build_array(
          '/help','/status','/ai_status','/health','/stats','/last_error',
          '/config','/ai_on','/ai_off','/leads'
        ),
        'note', 'Admin.v3.dev PostgreSQL candidate — inactive fixtures only'
      );
    ELSE
      RETURN jsonb_build_object('ok', false, 'reason', 'unknown_op', 'op', p_op);
  END CASE;
END;
$$;

COMMENT ON FUNCTION app_iseo_sales.admin_runtime_call IS
  'Closed allowlist dispatcher for Admin.v3.dev; no free-form SQL';

-- Grants
REVOKE ALL ON FUNCTION app_iseo_sales.check_access(text, text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.set_config_value(text, text, text, text, text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.get_admin_health() FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.get_admin_status_snapshot() FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.get_admin_stats() FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.get_last_error(int) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.list_leads_page(text[], int, int, text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.list_pending_lead_groups() FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.get_pending_leads_in_group(text, int) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.get_lead_card_payload(text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.admin_callback_lead_action(text, text, text, text, int, text, text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.claim_reminder_window(text, text, int) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.record_reminder_delivery(text, text, text, text, text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.update_delivery_message_binding(text, text, text, text) FROM PUBLIC;
REVOKE ALL ON FUNCTION app_iseo_sales.admin_runtime_call(text, jsonb) FROM PUBLIC;

GRANT EXECUTE ON FUNCTION app_iseo_sales.check_access(text, text) TO iseo_runtime, iseo_agent, iseo_reader;
GRANT EXECUTE ON FUNCTION app_iseo_sales.set_config_value(text, text, text, text, text) TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.get_admin_health() TO iseo_runtime, iseo_agent, iseo_reader;
GRANT EXECUTE ON FUNCTION app_iseo_sales.get_admin_status_snapshot() TO iseo_runtime, iseo_agent, iseo_reader;
GRANT EXECUTE ON FUNCTION app_iseo_sales.get_admin_stats() TO iseo_runtime, iseo_agent, iseo_reader;
GRANT EXECUTE ON FUNCTION app_iseo_sales.get_last_error(int) TO iseo_runtime, iseo_agent, iseo_reader;
GRANT EXECUTE ON FUNCTION app_iseo_sales.list_leads_page(text[], int, int, text) TO iseo_runtime, iseo_agent, iseo_reader;
GRANT EXECUTE ON FUNCTION app_iseo_sales.list_pending_lead_groups() TO iseo_runtime, iseo_agent, iseo_reader;
GRANT EXECUTE ON FUNCTION app_iseo_sales.get_pending_leads_in_group(text, int) TO iseo_runtime, iseo_agent, iseo_reader;
GRANT EXECUTE ON FUNCTION app_iseo_sales.get_lead_card_payload(text) TO iseo_runtime, iseo_agent, iseo_reader;
GRANT EXECUTE ON FUNCTION app_iseo_sales.admin_callback_lead_action(text, text, text, text, int, text, text) TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.claim_reminder_window(text, text, int) TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.record_reminder_delivery(text, text, text, text, text) TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.update_delivery_message_binding(text, text, text, text) TO iseo_runtime;
GRANT EXECUTE ON FUNCTION app_iseo_sales.admin_runtime_call(text, jsonb) TO iseo_runtime;

INSERT INTO mars_core.schema_migrations (schema_name, version, checksum)
VALUES ('app_iseo_sales', '0006_admin_v3_runtime_functions', NULL)
ON CONFLICT DO NOTHING;
