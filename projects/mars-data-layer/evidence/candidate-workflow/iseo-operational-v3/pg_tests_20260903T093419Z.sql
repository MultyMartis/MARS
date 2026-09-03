
\set ON_ERROR_STOP on
BEGIN;
-- pre-clean leftover synthetic namespace rows from prior runs
DELETE FROM app_iseo_sales.deliveries WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.lead_events WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.lead_dedup_keys WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.jobs WHERE dedupe_key LIKE 'dedupe-v3test_%' OR lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.errors WHERE message_sanitized='sanitized test' AND context->>'ns' LIKE 'v3test_%';
DELETE FROM app_iseo_sales.idempotency_keys WHERE idempotency_key LIKE '%v3test_%';
UPDATE app_iseo_sales.leads SET inbound_event_id=NULL WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.inbound_events WHERE source_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.leads WHERE lead_id LIKE 'v3test_%';
COMMIT;
SET ROLE iseo_runtime;
-- 1) new lead commit
SELECT app_iseo_sales.process_gmail_inbound_commit(
  'v3test_20260903T093419Z_gmail_src_1', 'v3test_20260903T093419Z_lead_1', '{"ns":"v3test_20260903T093419Z"}'::jsonb, 'fixture body', 'corr-v3test_20260903T093419Z_gmail_src_1',
  NULL, now(), 'subj1', 'noreply@example.com', NULL, 'v3-pg', 'Operational.v3.dev',
  'Test Client', NULL, NULL, NULL, 'test@example.com', NULL, 'https://example.test',
  'seo', 'summary', 'gmail', 'new', '{}'::jsonb, 'iseo-sales-v1', true,
  '{"dry_run":true}'::jsonb, NULL
) AS r1 \gset
\echo R1_OK
-- 2) same source repeated
SELECT app_iseo_sales.process_gmail_inbound_commit(
  'v3test_20260903T093419Z_gmail_src_1', 'v3test_20260903T093419Z_lead_1', '{"ns":"v3test_20260903T093419Z"}'::jsonb, 'fixture body', 'corr-v3test_20260903T093419Z_gmail_src_1',
  NULL, now(), 'subj1', 'noreply@example.com', NULL, 'v3-pg', 'Operational.v3.dev',
  'Test Client', NULL, NULL, NULL, 'test@example.com', NULL, 'https://example.test',
  'seo', 'summary', 'gmail', 'new', '{}'::jsonb, 'iseo-sales-v1', true,
  '{"dry_run":true}'::jsonb, NULL
) AS r2 \gset
\echo R2_OK
-- counts
SELECT count(*) AS inbound_c FROM app_iseo_sales.inbound_events WHERE source_id='v3test_20260903T093419Z_gmail_src_1';
SELECT count(*) AS lead_c FROM app_iseo_sales.leads WHERE lead_id='v3test_20260903T093419Z_lead_1';
SELECT count(*) AS del_c FROM app_iseo_sales.deliveries WHERE lead_id='v3test_20260903T093419Z_lead_1' AND idempotency_key LIKE 'lead_card:v3test_20260903T093419Z_lead_1:%:v3test_20260903T093419Z_gmail_src_1';
SELECT count(*) AS evt_c FROM app_iseo_sales.lead_events WHERE lead_id='v3test_20260903T093419Z_lead_1' AND event_id LIKE 'evt-v3test_20260903T093419Z_gmail_src_1-%';
-- 3) status spam + processed
SELECT app_iseo_sales.change_lead_status(
  'v3test_20260903T093419Z_lead_1',
  (SELECT version FROM app_iseo_sales.leads WHERE lead_id='v3test_20260903T093419Z_lead_1'),
  'new', 'spam', 'workflow', 'v3-test', 'idem-spam-v3test_20260903T093419Z_gmail_src_1', 'corr-v3test_20260903T093419Z_gmail_src_1', NULL, 'test'
);
SELECT app_iseo_sales.change_lead_status(
  'v3test_20260903T093419Z_lead_1',
  (SELECT version FROM app_iseo_sales.leads WHERE lead_id='v3test_20260903T093419Z_lead_1'),
  'spam', 'processed', 'workflow', 'v3-test', 'idem-proc-v3test_20260903T093419Z_gmail_src_1', 'corr-v3test_20260903T093419Z_gmail_src_1', NULL, 'test'
);
\echo STATUS_OK
-- 4) second source / upsert path
SELECT app_iseo_sales.process_gmail_inbound_commit(
  'v3test_20260903T093419Z_gmail_src_2', 'v3test_20260903T093419Z_lead_2', '{"ns":"v3test_20260903T093419Z"}'::jsonb, 'body2', 'corr-v3test_20260903T093419Z_gmail_src_2',
  NULL, now(), 'subj2', 'a@example.com', NULL, 'v3-pg', 'Operational.v3.dev',
  'Client2', NULL, NULL, NULL, NULL, NULL, NULL, 'seo', 's2', 'gmail', 'new',
  '{}'::jsonb, 'iseo-sales-v1', false, '{}'::jsonb, NULL
);
\echo R3_OK
-- 5) error record
SELECT app_iseo_sales.record_error('operational','Operational.v3.dev','exec-test','corr-err',
  'lead','v3test_20260903T093419Z_lead_1','transient_db','postgres',NULL,NULL,'commit',true,'sanitized test',
  '{"ns":"v3test_20260903T093419Z"}'::jsonb);
-- 6) job enqueue with backoff
SELECT app_iseo_sales.enqueue_job('delivery_retry','{"ns":"v3test_20260903T093419Z"}'::jsonb,50, now()+interval '60 seconds',
  'dedupe-v3test_20260903T093419Z-job', 'corr-job', 'v3test_20260903T093419Z_lead_1');
\echo JOB_OK
-- 7) claim deliveries (may be empty if no recipients)
SELECT app_iseo_sales.claim_pending_deliveries('v3-test-worker', 50, 30) AS claimed;
\echo CLAIM_OK
-- dry-run finalize claimed deliveries for this NS only (via contract)
SELECT app_iseo_sales.mark_delivery_result(d.delivery_id, 'sent', 'dry-run-msg', 'dry-run-chat', NULL, NULL)
FROM app_iseo_sales.deliveries d
WHERE d.lead_id LIKE 'v3test_20260903T093419Z%' AND d.status = 'processing';
\echo DELIVERY_DRYRUN_OK
RESET ROLE;
-- cleanup synthetic (admin) — FK order: children before leads
DELETE FROM app_iseo_sales.deliveries WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.lead_events WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.lead_dedup_keys WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.jobs WHERE dedupe_key LIKE 'dedupe-v3test_%' OR lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.errors WHERE message_sanitized='sanitized test' AND (context->>'ns' LIKE 'v3test_%' OR context->>'ns' = 'v3test_20260903T093419Z');
DELETE FROM app_iseo_sales.idempotency_keys WHERE idempotency_key LIKE 'idem-%v3test_%' OR idempotency_key LIKE '%v3test_%';
UPDATE app_iseo_sales.leads SET inbound_event_id=NULL WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.inbound_events WHERE source_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.leads WHERE lead_id LIKE 'v3test_%';
\echo CLEANUP_OK
-- shadow read smoke (no mutation of business meaning)
SELECT count(*) AS shadow_leads FROM app_iseo_sales.leads;
SELECT count(*) AS shadow_inbound FROM app_iseo_sales.inbound_events;
SELECT count(*) AS shadow_deliveries FROM app_iseo_sales.deliveries;
SELECT count(*) AS access_active FROM app_iseo_sales.access_rules WHERE is_active;
