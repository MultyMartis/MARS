-- Synthetic fixtures for app_iseo_sales V1
-- NO real PII — example.com / fake phone only
-- Apply after migrations 0001–0004

BEGIN;

-- Access rules
INSERT INTO app_iseo_sales.access_rules (
  principal_key, telegram_user_id, display_name, username, role,
  is_active, receives_cards, receives_reminders, notes
) VALUES
  (
    'ADMIN_A',
    '100001',
    'Synthetic Admin A',
    'synth_admin_a',
    'admin',
    true,
    true,
    true,
    'fixture admin'
  ),
  (
    'MOD_B',
    '100002',
    'Synthetic Moderator B',
    'synth_mod_b',
    'moderator',
    true,
    true,
    true,
    'fixture moderator'
  )
ON CONFLICT (principal_key) DO NOTHING;

-- Inbound event (gmail)
SELECT app_iseo_sales.register_inbound_event(
  'gmail',
  'msgid-synthetic-001',
  '{"fixture":true,"form":"contact"}'::jsonb,
  'Synthetic inquiry body for LEAD_SYNTH000001. Contact: lead@example.com',
  'corr-synth-001',
  'thread-synthetic-001',
  '2026-09-01T10:00:00+00'::timestamptz,
  'Synthetic SEO inquiry',
  'lead@example.com',
  NULL,
  'parser-synth-1',
  'operational.v0.fixture'
);

-- Duplicate attempt (idempotent re-sight) — should bump last_seen_at / attempts
-- Comment: second register with same source_system+source_id must not create a second row.
SELECT app_iseo_sales.register_inbound_event(
  'gmail',
  'msgid-synthetic-001',
  '{"fixture":true,"resight":true}'::jsonb,
  NULL,
  'corr-synth-001-resight'
);

-- Lead
SELECT app_iseo_sales.upsert_lead(
  'LEAD_SYNTH000001',
  (SELECT id FROM app_iseo_sales.inbound_events WHERE source_id = 'msgid-synthetic-001'),
  'msgid-synthetic-001',
  'Example Client LLC',
  'lead@example.com',
  'email',
  '79001234567',
  'lead@example.com',
  NULL,
  'https://example.com',
  'seo_audit',
  'Synthetic lead for local schema tests',
  'gmail_form',
  'new',
  '{"fixture":true}'::jsonb,
  'iseo.sales.contract.v0',
  'operational.v0.fixture',
  'parser-synth-1'
);

UPDATE app_iseo_sales.inbound_events
SET lead_id = 'LEAD_SYNTH000001',
    processing_status = 'processed',
    updated_at = now()
WHERE source_id = 'msgid-synthetic-001';

-- Lead event
INSERT INTO app_iseo_sales.lead_events (
  event_id, lead_id, event_type, actor_type, actor_id, correlation_id, payload
) VALUES (
  'evt-synth-001',
  'LEAD_SYNTH000001',
  'lead_created',
  'system',
  'fixture_loader',
  'corr-synth-001',
  '{"fixture":true}'::jsonb
)
ON CONFLICT (event_id) DO NOTHING;

-- Delivery pending
SELECT app_iseo_sales.enqueue_delivery(
  'LEAD_SYNTH000001',
  'telegram',
  'MOD_B',
  '100002',
  'lead_card',
  '{"text":"Synthetic lead card"}'::jsonb,
  'fixture-delivery-LEAD_SYNTH000001',
  'corr-synth-001',
  now(),
  'dlv-synth-001'
);

-- Job pending reminder
SELECT app_iseo_sales.enqueue_job(
  'pending_reminder',
  '{"window":"weekday_am"}'::jsonb,
  50,
  now(),
  'fixture-job-pending-reminder-20260901',
  'corr-synth-001',
  'LEAD_SYNTH000001'
);

-- Config
INSERT INTO app_iseo_sales.config (key, value, value_type, description, updated_by, is_secretish)
VALUES (
  'ai_enabled',
  'false',
  'bool',
  'Fixture: AI replies disabled',
  'fixture_loader',
  false
)
ON CONFLICT (key) DO UPDATE
  SET value = EXCLUDED.value,
      updated_at = now(),
      updated_by = EXCLUDED.updated_by;

-- Error sample
INSERT INTO app_iseo_sales.errors (
  app_component, workflow_version, correlation_id, entity_type, entity_id,
  error_class, provider, code, retryable, message_sanitized, context, resolved
) VALUES (
  'operational',
  'operational.v0.fixture',
  'corr-synth-quota-001',
  'lead',
  'LEAD_SYNTH000001',
  'sheets_quota_exceeded',
  'google_sheets',
  '429',
  true,
  'Synthetic Sheets quota exceeded (fixture)',
  '{"fixture":true}'::jsonb,
  false
);

COMMIT;
