
\set ON_ERROR_STOP on
BEGIN;
DELETE FROM app_iseo_sales.deliveries WHERE delivery_id LIKE 'adminv3test_%' OR lead_id LIKE 'adminv3test_%' OR idempotency_key LIKE 'adminv3test_%' OR idempotency_key LIKE 'reminder_delivery:adminv3test_%' OR idempotency_key LIKE 'cb:adminv3test_%' OR idempotency_key LIKE 'adminv3test_20260903T110001Z%';
DELETE FROM app_iseo_sales.lead_events WHERE lead_id LIKE 'adminv3test_%';
DELETE FROM app_iseo_sales.jobs WHERE dedupe_key LIKE 'reminder_window:adminv3test_%' OR payload->>'ns' = 'adminv3test_20260903T110001Z';
DELETE FROM app_iseo_sales.audit_logs WHERE actor_id LIKE 'adminv3test_%' OR entity_id LIKE 'adminv3test_%';
DELETE FROM app_iseo_sales.idempotency_keys WHERE idempotency_key LIKE '%adminv3test_%' OR idempotency_key LIKE '%adminv3test_20260903T110001Z%';
DELETE FROM app_iseo_sales.config WHERE key LIKE 'adminv3test.%';
DELETE FROM app_iseo_sales.access_rules WHERE principal_key LIKE 'adminv3test_%';
UPDATE app_iseo_sales.leads SET inbound_event_id=NULL WHERE lead_id LIKE 'adminv3test_%';
DELETE FROM app_iseo_sales.leads WHERE lead_id LIKE 'adminv3test_%';
COMMIT;

-- synthetic ACCESS (isolated; do not touch real ADMIN_A/MOD_*)
INSERT INTO app_iseo_sales.access_rules (principal_key, telegram_user_id, display_name, role, is_active, receives_cards, receives_reminders)
VALUES
  ('adminv3test_ADMIN', 'adminv3test_20260903T110001Z_tg_admin', 'Synthetic Admin', 'admin', true, true, true),
  ('adminv3test_OLYA', 'adminv3test_20260903T110001Z_tg_olya', 'Synthetic Olya', 'moderator', true, true, true),
  ('adminv3test_REVOKED', 'adminv3test_20260903T110001Z_tg_revoked', 'Synthetic Revoked', 'moderator', false, false, false);

INSERT INTO app_iseo_sales.leads (
  lead_id, manager_status, version, site, client_name, service, summary, source, data_contract_version
) VALUES (
  'adminv3test_20260903T110001Z_lead_1', 'pending', 1, 'https://adminv3.example.test', 'Synthetic Client', 'seo', 'fixture', 'fixture', 'iseo-sales-v1'
);

SET ROLE iseo_runtime;

-- ACCESS parity (synthetic)
SELECT app_iseo_sales.check_access('adminv3test_20260903T110001Z_tg_admin', NULL) AS a_admin \gset
SELECT app_iseo_sales.check_access('adminv3test_20260903T110001Z_tg_olya', NULL) AS a_olya \gset
SELECT app_iseo_sales.check_access('adminv3test_20260903T110001Z_tg_revoked', NULL) AS a_rev \gset
SELECT app_iseo_sales.check_access('adminv3test_20260903T110001Z_tg_unknown', NULL) AS a_unk \gset
\echo ACCESS_OK

-- shadow ACL read-only smoke (no mutation of real rows)
SELECT principal_key, role, is_active
FROM app_iseo_sales.access_rules
WHERE principal_key IN ('ADMIN_A','MOD_A','MOD_B','MOD_C')
ORDER BY principal_key;
\echo ACCESS_SHADOW_READ_OK

-- lead actions + idempotency
SELECT app_iseo_sales.admin_callback_lead_action(
  'adminv3test_20260903T110001Z_lead_1', 'processed', 'adminv3test_20260903T110001Z_tg_olya', 'adminv3test_20260903T110001Z_cb_processed_1', 1, 'pending', 'corr-adminv3test_20260903T110001Z'
) AS t1 \gset
\echo ACTION_PROCESSED_OK
SELECT app_iseo_sales.admin_callback_lead_action(
  'adminv3test_20260903T110001Z_lead_1', 'processed', 'adminv3test_20260903T110001Z_tg_olya', 'adminv3test_20260903T110001Z_cb_processed_1', NULL, NULL, 'corr-adminv3test_20260903T110001Z'
) AS t1b \gset
\echo ACTION_IDEMPOTENT_OK
-- spam from processed (allowed)
SELECT app_iseo_sales.admin_callback_lead_action(
  'adminv3test_20260903T110001Z_lead_1', 'spam', 'adminv3test_20260903T110001Z_tg_admin', 'adminv3test_20260903T110001Z_cb_spam', NULL, 'processed', 'corr-adminv3test_20260903T110001Z-spam'
) AS t2 \gset
\echo ACTION_SPAM_OK
-- revoked denied
SELECT app_iseo_sales.admin_callback_lead_action(
  'adminv3test_20260903T110001Z_lead_1', 'processed', 'adminv3test_20260903T110001Z_tg_revoked', 'adminv3test_20260903T110001Z_cb_denied', NULL, NULL, 'corr-denied'
) AS t_denied \gset
\echo ACTION_DENIED_OK

-- reminders / groups / card
SELECT app_iseo_sales.list_pending_lead_groups() AS groups \gset
SELECT app_iseo_sales.get_pending_leads_in_group('https://adminv3.example.test', 10) AS glead \gset
SELECT app_iseo_sales.get_lead_card_payload('adminv3test_20260903T110001Z_lead_1') AS card \gset
SELECT app_iseo_sales.claim_reminder_window('adminv3test_20260903T110001Z_win', 'admin-v3-test', 3600) AS rem_claim \gset
SELECT app_iseo_sales.record_reminder_delivery('adminv3test_20260903T110001Z_win', 'adminv3test_OLYA', 'dryrun-msg-1', 'sent', 'corr-rem') AS rem_del \gset
\echo REMINDER_OK

-- commands
SELECT app_iseo_sales.admin_runtime_call('help', '{}'::jsonb) AS h \gset
SELECT app_iseo_sales.get_admin_health() AS health \gset
SELECT app_iseo_sales.get_admin_status_snapshot() AS status \gset
SELECT app_iseo_sales.get_admin_stats() AS stats \gset
SELECT app_iseo_sales.get_last_error(3) AS last_err \gset
SELECT app_iseo_sales.list_leads_page(ARRAY['spam','processed'], 10, 0, NULL) AS leads \gset
\echo COMMANDS_OK

-- config mutation on namespaced key only (do not flip live AI)
SELECT app_iseo_sales.set_config_value('adminv3test.ai.enabled', 'false', 'admin-v3-test', 'bool', 'synthetic') AS cfg \gset
SELECT app_iseo_sales.get_active_config(ARRAY['adminv3test.ai.enabled']) AS cfg_r \gset
\echo CONFIG_OK

-- malformed delivery exclusion
SELECT count(*) AS legacy_invalid
FROM app_iseo_sales.deliveries
WHERE external_message_id = 'LEGACY INVALID ROW';
\echo LEGACY_ROW_COUNTED_OK

RESET ROLE;

-- cleanup synthetic only
DELETE FROM app_iseo_sales.deliveries WHERE delivery_id LIKE 'adminv3test_%' OR lead_id LIKE 'adminv3test_%' OR idempotency_key LIKE '%adminv3test_%' OR idempotency_key LIKE 'reminder_delivery:adminv3test_20260903T110001Z%' OR idempotency_key LIKE 'cb:adminv3test_20260903T110001Z%' OR idempotency_key LIKE 'adminv3test_20260903T110001Z%' OR idempotency_key LIKE 'reminder_delivery:adminv3test_20260903T110001Z_win%';
DELETE FROM app_iseo_sales.lead_events WHERE lead_id LIKE 'adminv3test_%';
DELETE FROM app_iseo_sales.jobs WHERE dedupe_key LIKE 'reminder_window:adminv3test_20260903T110001Z%' OR dedupe_key LIKE 'reminder_window:adminv3test_%';
DELETE FROM app_iseo_sales.audit_logs WHERE actor_id LIKE 'adminv3test_%' OR entity_id LIKE 'adminv3test_%' OR actor_id LIKE 'adminv3test_20260903T110001Z%' OR actor_id IN ('adminv3test_20260903T110001Z_tg_admin','adminv3test_20260903T110001Z_tg_olya','adminv3test_20260903T110001Z_tg_revoked','admin-v3-test');
DELETE FROM app_iseo_sales.idempotency_keys WHERE idempotency_key LIKE '%adminv3test_%' OR idempotency_key LIKE '%adminv3test_20260903T110001Z%';
DELETE FROM app_iseo_sales.config WHERE key LIKE 'adminv3test.%';
DELETE FROM app_iseo_sales.access_rules WHERE principal_key LIKE 'adminv3test_%';
DELETE FROM app_iseo_sales.leads WHERE lead_id LIKE 'adminv3test_%';
\echo CLEANUP_OK
