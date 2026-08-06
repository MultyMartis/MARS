/**
 * Phase 1B-D6F1B — Four-scenario Telegram acceptance gallery (SITE-002).
 *
 * Authorized live test. Uses namespaced test event IDs.
 * Does not mutate production Data Table rows.
 * Does not disable automation after gallery.
 *
 * Usage:
 *   node run-client-ops-d6f1b-acceptance-gallery.mjs
 *   node run-client-ops-d6f1b-acceptance-gallery.mjs --send \
 *     --confirm="SEND CLIENT OPS D6F1B FOUR SCENARIO ACCEPTANCE GALLERY BZPM"
 */

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  getWorkflow,
  loadCredentials,
  normalizeBaseUrl,
} from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';
import { ALLOWED_WORKFLOW_ID } from './lib/client-ops-n8n-activation-client.mjs';
import {
  getDataTableRows,
  loadDataTableCredentials,
} from './lib/client-ops-n8n-datatable-client.mjs';
import { TELEGRAM_NODE_NAME } from './lib/client-ops-dedupe-compose.mjs';
import { D6A_TABLE_ID } from './lib/client-ops-delivery-ledger-compose.mjs';
import {
  classifyImportReport,
  REPORT_CLASS,
} from './lib/client-ops-d6d-import-condition.mjs';
import { uuidV5, sha256Hex } from './lib/client-ops-d6d-artifact.mjs';
import { MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID } from './lib/client-ops-d6d-constants.mjs';
import {
  formatOperatorTelegramMessage,
  wrapAcceptanceTestMessage,
  SCENARIO_NAME_RU,
  formatSite002LocalTime,
} from './lib/client-ops-telegram-operator-message.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const MAIN_ROOT = 'X:\\AI MARS';
const EVIDENCE = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/evidence/phase-1b-d6f1b-telegram-operator-ux-polish',
);
const SECRET_PATH = existsSync(
  resolve(MAIN_ROOT, 'local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env'),
)
  ? resolve(MAIN_ROOT, 'local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env')
  : resolve(REPO_ROOT, 'local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env');
const N8N_ENV = existsSync(resolve(MAIN_ROOT, 'local/tokens/n8n-api.env'))
  ? resolve(MAIN_ROOT, 'local/tokens/n8n-api.env')
  : resolve(REPO_ROOT, 'local/tokens/n8n-api.env');
const CONFIRM = 'SEND CLIENT OPS D6F1B FOUR SCENARIO ACCEPTANCE GALLERY BZPM';
const GALLERY_TS = new Date().toISOString().replace(/[:.]/g, '-');

function writeJson(path, obj) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
}

function loadEnvKey(path, key) {
  if (!existsSync(path)) return { ok: false };
  const lines = readFileSync(path, 'utf8').split(/\r?\n/);
  for (const line of lines) {
    const t = line.trim();
    if (!t || t.startsWith('#')) continue;
    const i = t.indexOf('=');
    if (i < 0) continue;
    if (t.slice(0, i).trim() === key) {
      return { ok: true, value: t.slice(i + 1).trim() };
    }
  }
  return { ok: false };
}

function galleryEventId(scenarioId) {
  const name = `mars.client-ops.d6f1b-acceptance.site-002.${GALLERY_TS}.${scenarioId}`;
  return uuidV5(MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID, sha256Hex(name));
}

function scenarios() {
  const now = new Date();
  const observed = new Date(now.getTime() - 120_000).toISOString().replace(/\.\d{3}Z$/, 'Z');
  const generated = now.toISOString().replace(/\.\d{3}Z$/, 'Z');

  const defs = [
    {
      id: 'T1',
      nameRu: SCENARIO_NAME_RU.T1,
      severity: 'OK',
      classification: classifyImportReport({
        fresh_import_confirmed: true,
        catalog_input_files: ['import0_1.xml'],
        offers_input_files: ['offers0_1.xml'],
        catalog_phase_ok: true,
        offers_phase_ok: true,
        offers_processed_count: 1,
      }),
      formatInput: {
        report_class: REPORT_CLASS.FULL_SUCCESS,
        summary_code: 'FULL_IMPORT_SUCCESS',
        normalized_status: 'OK',
        observed_at: observed,
        domain: 'bzpm.ru',
      },
      metrics: {
        baseline_count: 1879,
        current_count: 1879,
        added_urls: 0,
        removed_urls: 0,
        onboarding_needed_count: 0,
      },
      source_status: 'NO_ACTION_REQUIRED',
    },
    {
      id: 'T2',
      nameRu: SCENARIO_NAME_RU.T2,
      severity: 'ATTENTION',
      classification: classifyImportReport({
        fresh_import_confirmed: true,
        catalog_input_files: ['import0_1.xml'],
        offers_input_files: [],
        catalog_phase_ok: true,
        offers_phase_ok: true,
        offers_processed_count: 0,
      }),
      formatInput: {
        report_class: REPORT_CLASS.CATALOG_SUCCESS_OFFERS_INPUT_MISSING,
        summary_code: 'OFFERS_INPUT_MISSING',
        normalized_status: 'ATTENTION',
        reason_codes: ['OFFERS0_XML_ABSENT'],
        observed_at: observed,
        domain: 'bzpm.ru',
      },
      metrics: {
        baseline_count: 1879,
        current_count: 1879,
        added_urls: 0,
        removed_urls: 0,
        onboarding_needed_count: 0,
      },
      source_status: 'HYGIENE_REVIEW_REQUIRED',
    },
    {
      id: 'T3',
      nameRu: SCENARIO_NAME_RU.T3,
      severity: 'ATTENTION',
      classification: classifyImportReport({
        fresh_import_confirmed: false,
        monitor_completion_confirmed: true,
      }),
      formatInput: {
        report_class: REPORT_CLASS.NO_FRESH_IMPORT,
        summary_code: 'NO_FRESH_1C_IMPORT',
        normalized_status: 'ATTENTION',
        reason_codes: ['NO_FRESH_IMPORT_IN_EXPECTED_WINDOW'],
        observed_at: observed,
        domain: 'bzpm.ru',
      },
      metrics: {
        baseline_count: 1879,
        current_count: 1879,
        added_urls: 0,
        removed_urls: 0,
        onboarding_needed_count: 0,
      },
      source_status: 'HYGIENE_REVIEW_REQUIRED',
    },
    {
      id: 'T4',
      nameRu: SCENARIO_NAME_RU.T4,
      severity: 'FAILED',
      classification: classifyImportReport({
        fresh_import_confirmed: true,
        catalog_input_files: ['import0_1.xml'],
        offers_input_files: ['offers0_1.xml'],
        catalog_phase_ok: false,
        offers_phase_ok: false,
        import_error: true,
      }),
      formatInput: {
        report_class: REPORT_CLASS.IMPORT_ERROR,
        summary_code: 'IMPORT_ERROR',
        normalized_status: 'FAILED',
        observed_at: observed,
        domain: 'bzpm.ru',
        error_summary: 'Ошибка фазы импорта каталога',
      },
      metrics: {
        baseline_count: 1879,
        current_count: 1879,
        added_urls: 0,
        removed_urls: 0,
        onboarding_needed_count: 0,
      },
      source_status: 'FAILURE_REVIEW_REQUIRED',
    },
  ];

  return defs.map((d) => {
    const event_id = galleryEventId(d.id);
    const body = formatOperatorTelegramMessage(d.formatInput);
    const text = wrapAcceptanceTestMessage(body, d.nameRu);
    const envelope = {
      schema_name: 'mars.client_ops.report',
      schema_version: '1.0',
      event_id,
      event_type: 'site.post_1c_monitor',
      generated_at: generated,
      observed_at: observed,
      environment: `d6f1b-acceptance.${d.id}`,
      site: {
        site_id: 'SITE-002',
        site_name: `ZPM-D6F1B-${d.id}`,
        domain: 'bzpm.ru',
      },
      producer: {
        name: 'mars.client-ops.d6f1b-acceptance.site-002',
        version: '1b-d6f1b.1',
      },
      run: {
        run_id: `d6f1b-acceptance-${GALLERY_TS}-${d.id}`,
        source_status: d.source_status,
        normalized_status: d.severity === 'FAILED' ? 'FAILED' : d.severity,
        summary_code: d.classification.summary_code,
        reason_codes: [
          'D6F1B_ACCEPTANCE',
          'SYNTHETIC_NON_CUSTOMER',
          ...(d.classification.reason_codes || []),
        ],
      },
      action: {
        required: d.severity !== 'OK',
        code: d.classification.action_code || 'NONE',
        text,
      },
      metrics: d.metrics,
      freshness: { age_seconds: 120, stale: false },
      security: {
        classification: 'internal',
        contains_secrets: false,
        redacted: true,
      },
    };
    return {
      scenario_id: d.id,
      scenario_name_ru: d.nameRu,
      severity: envelope.run.normalized_status,
      report_class: d.classification.report_class,
      event_id,
      event_namespace: `mars.client-ops.d6f1b-acceptance.site-002.${GALLERY_TS}.${d.id}`,
      message_text: text,
      local_time: formatSite002LocalTime(observed),
      envelope,
    };
  });
}

async function listExecutions(creds, workflowId, limit = 50) {
  const base = normalizeBaseUrl(creds.apiUrl);
  const url = `${base}/api/v1/executions?workflowId=${encodeURIComponent(workflowId)}&limit=${limit}`;
  const response = await fetch(url, {
    headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
  });
  if (!response.ok) return { ok: false, status: response.status, rows: [] };
  const data = await response.json();
  return { ok: true, rows: data.data || data || [] };
}

async function getExecutionDetail(creds, id) {
  const base = normalizeBaseUrl(creds.apiUrl);
  const response = await fetch(`${base}/api/v1/executions/${id}?includeData=true`, {
    headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
  });
  if (!response.ok) return { ok: false, status: response.status };
  return { ok: true, data: await response.json() };
}

function summarizeExecution(detail) {
  if (!detail?.ok) return { ok: false };
  const runData = detail.data?.data?.resultData?.runData || {};
  const nodeOrder = Object.keys(runData).filter((k) => Array.isArray(runData[k]) && runData[k].length);
  const telegramRuns = Array.isArray(runData[TELEGRAM_NODE_NAME])
    ? runData[TELEGRAM_NODE_NAME].length
    : 0;
  let telegramMessageId = null;
  let telegramText = null;
  if (telegramRuns > 0) {
    const out = runData[TELEGRAM_NODE_NAME][0]?.data?.main?.[0]?.[0]?.json;
    telegramMessageId = out?.result?.message_id ?? out?.message_id ?? null;
    telegramText = out?.result?.text ?? out?.text ?? null;
  }
  return {
    ok: true,
    execution_id: String(detail.data?.id || ''),
    status: detail.data?.status,
    finished: detail.data?.finished,
    node_names_executed: nodeOrder,
    telegram_runs: telegramRuns,
    telegram_message_id:
      telegramMessageId != null && /^\d+$/.test(String(telegramMessageId))
        ? String(telegramMessageId)
        : null,
    telegram_text_preview:
      typeof telegramText === 'string' ? telegramText.slice(0, 240) : null,
    has_telegram: nodeOrder.includes(TELEGRAM_NODE_NAME),
  };
}

async function postWebhook(webhookUrl, secret, body) {
  const response = await fetch(webhookUrl, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      'x-mars-client-ops-token': secret,
    },
    body: JSON.stringify(body),
  });
  const text = await response.text();
  let json = null;
  try {
    json = text ? JSON.parse(text) : null;
  } catch {
    json = { parse_error: true, body_len: text.length };
  }
  return { status: response.status, json };
}

async function waitForNewExecution(creds, workflowId, priorIds, startedAfterIso) {
  for (let i = 0; i < 40; i += 1) {
    await new Promise((r) => setTimeout(r, 1000));
    const snap = await listExecutions(creds, workflowId, 30);
    const fresh = (snap.rows || []).find((row) => {
      if (priorIds.has(String(row.id))) return false;
      if (startedAfterIso && row.startedAt && row.startedAt < startedAfterIso) return false;
      return true;
    });
    if (fresh) {
      const detail = await getExecutionDetail(creds, fresh.id);
      return { found: true, execution: fresh, summary: summarizeExecution(detail) };
    }
  }
  return { found: false };
}

async function getEventRow(eventId) {
  const creds = loadDataTableCredentials(N8N_ENV);
  const filtered = await getDataTableRows(creds, D6A_TABLE_ID, {
    limit: 5,
    filter: { filters: [{ columnName: 'event_id', condition: 'eq', value: eventId }] },
  });
  const rows = filtered.data?.data || filtered.data || [];
  const list = Array.isArray(rows) ? rows : [];
  const matches = list.filter((r) => String(r.event_id) === String(eventId));
  return { count: matches.length, row: matches[0] || null };
}

async function listAllRows() {
  const creds = loadDataTableCredentials(N8N_ENV);
  const all = await getDataTableRows(creds, D6A_TABLE_ID, { limit: 200 });
  const rows = all.data?.data || all.data || [];
  return Array.isArray(rows) ? rows : [];
}

function isTestRow(r) {
  const producer = String(r.producer || r.producer_name || '');
  const env = String(r.environment || '');
  return (
    producer.includes('test-gallery') ||
    producer.includes('d6f1b-acceptance') ||
    env.includes('test-gallery') ||
    env.includes('d6f1b-acceptance')
  );
}

function parseArgs(argv) {
  const out = { send: false, confirm: null, retry: null };
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    if (a === '--send') out.send = true;
    if (a.startsWith('--confirm=')) out.confirm = a.slice('--confirm='.length);
    if (a === '--confirm') out.confirm = argv[++i];
    if (a.startsWith('--retry=')) out.retry = a.slice('--retry='.length);
  }
  return out;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  mkdirSync(EVIDENCE, { recursive: true });
  let items = scenarios();
  if (args.retry) {
    items = items.filter((s) => s.scenario_id === args.retry);
    if (!items.length) throw new Error(`unknown retry scenario ${args.retry}`);
  }

  writeJson(join(EVIDENCE, 'ACCEPTANCE-GALLERY-PAYLOADS.json'), {
    phase: '1B-D6F1B',
    gallery_timestamp: GALLERY_TS,
    count: items.length,
    scenarios: items.map((s) => ({
      scenario_id: s.scenario_id,
      scenario_name_ru: s.scenario_name_ru,
      severity: s.severity,
      report_class: s.report_class,
      event_id_redacted: `${String(s.event_id).slice(0, 8)}…`,
      event_namespace: s.event_namespace,
      local_time: s.local_time,
      message_text: s.message_text,
    })),
  });
  writeFileSync(
    join(EVIDENCE, 'ACCEPTANCE-GALLERY-VISIBLE-TEXT.md'),
    items
      .map((s) => `## ${s.scenario_id} — ${s.scenario_name_ru}\n\n\`\`\`\n${s.message_text}\n\`\`\`\n`)
      .join('\n'),
    'utf8',
  );

  if (!args.send) {
    console.log(
      JSON.stringify(
        {
          mode: 'dry-run',
          scenarios: items.length,
          evidence: EVIDENCE,
          token: 'D6F1B_FOUR_SCENARIO_ACCEPTANCE_GALLERY_PREPARED',
        },
        null,
        2,
      ),
    );
    return;
  }
  if (args.confirm !== CONFIRM) {
    throw new Error('CONFIRM_PHRASE_MISMATCH');
  }

  const secret = loadEnvKey(SECRET_PATH, 'CLIENT_OPS_WEBHOOK_AUTH_SECRET');
  if (!secret.ok) throw new Error('WEBHOOK_SECRET_MISSING');
  const creds = loadCredentials(N8N_ENV);
  const live = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
  if (!live.active) throw new Error('WORKFLOW_NOT_ACTIVE');
  const webhookNode = (live.nodes || []).find((n) => n.name === 'Webhook Intake');
  const path = webhookNode?.parameters?.path;
  if (!path) throw new Error('WEBHOOK_PATH_MISSING');
  const webhookUrl = `${normalizeBaseUrl(creds.apiUrl)}/webhook/${path}`;

  const beforeList = await listAllRows();
  const productionBefore = beforeList.filter((r) => !isTestRow(r));
  const testBefore = beforeList.filter((r) => isTestRow(r));
  writeJson(join(EVIDENCE, 'DATA-TABLE-PRESTATE.json'), {
    total: beforeList.length,
    production_count: productionBefore.length,
    test_count: testBefore.length,
    production_event_ids_redacted: productionBefore.map((r) => `${String(r.event_id).slice(0, 8)}…`),
  });

  const results = [];
  const priorIds = new Set(
    ((await listExecutions(creds, ALLOWED_WORKFLOW_ID, 50)).rows || []).map((r) => String(r.id)),
  );

  for (const item of items) {
    const existing = await getEventRow(item.event_id);
    if (existing.count !== 0) {
      results.push({
        scenario_id: item.scenario_id,
        skipped: true,
        reason: 'EVENT_ID_ALREADY_EXISTS',
        event_id_redacted: `${String(item.event_id).slice(0, 8)}…`,
      });
      continue;
    }
    const startedAfter = new Date(Date.now() - 2000).toISOString();
    const post = await postWebhook(webhookUrl, secret.value, item.envelope);
    const waited = await waitForNewExecution(creds, ALLOWED_WORKFLOW_ID, priorIds, startedAfter);
    if (waited.found) priorIds.add(String(waited.execution.id));
    let row = await getEventRow(item.event_id);
    for (let i = 0; i < 15 && row.row && row.row.delivery_state === 'PENDING'; i += 1) {
      await new Promise((r) => setTimeout(r, 1000));
      row = await getEventRow(item.event_id);
    }
    // Same-event retry dedupe proof for T1 only (once).
    let duplicateCount = 0;
    if (item.scenario_id === 'T1' && (post.status === 200 || post.status === 202)) {
      const retry = await postWebhook(webhookUrl, secret.value, item.envelope);
      duplicateCount = retry.status === 200 || retry.status === 202 ? 1 : 0;
      // Wait briefly; expect no second telegram for same event.
      await new Promise((r) => setTimeout(r, 2000));
    }
    const summary = waited.summary || { ok: false };
    const delivered =
      (post.status === 200 || post.status === 202) &&
      summary.telegram_runs === 1 &&
      summary.telegram_message_id != null;
    results.push({
      scenario_id: item.scenario_id,
      scenario_name_ru: item.scenario_name_ru,
      severity: item.severity,
      event_id_redacted: `${String(item.event_id).slice(0, 8)}…`,
      http_status: post.status,
      intake_state: row.row?.intake_state || null,
      delivery_state: row.row?.delivery_state || null,
      n8n_execution_id: summary.execution_id || null,
      telegram_delivery_success: delivered,
      telegram_message_id_present: Boolean(summary.telegram_message_id),
      telegram_message_id_redacted: summary.telegram_message_id
        ? `msg:${String(summary.telegram_message_id).slice(0, 2)}***`
        : null,
      duplicate_retry_posts: duplicateCount,
      report_class: item.report_class,
      message_text: item.message_text,
      workflow_status: summary.status || null,
    });
  }

  const afterList = await listAllRows();
  const productionAfter = afterList.filter((r) => !isTestRow(r));
  const testAfter = afterList.filter((r) => isTestRow(r));
  writeJson(join(EVIDENCE, 'DATA-TABLE-POSTSTATE.json'), {
    total: afterList.length,
    production_count: productionAfter.length,
    test_count: testAfter.length,
    production_count_delta: productionAfter.length - productionBefore.length,
    test_count_delta: testAfter.length - testBefore.length,
  });

  const deliveredCount = results.filter((r) => r.telegram_delivery_success).length;
  writeJson(join(EVIDENCE, 'ACCEPTANCE-GALLERY-DELIVERY-RESULTS.json'), {
    phase: '1B-D6F1B',
    gallery_timestamp: GALLERY_TS,
    delivered: deliveredCount,
    required: 4,
    results,
    workflow_active_after: (await getWorkflow(ALLOWED_WORKFLOW_ID, creds)).active === true,
  });

  console.log(
    JSON.stringify(
      {
        ok: deliveredCount === items.length,
        delivered: deliveredCount,
        required: items.length,
        results: results.map((r) => ({
          scenario_id: r.scenario_id,
          telegram_delivery_success: r.telegram_delivery_success,
          n8n_execution_id: r.n8n_execution_id,
          telegram_message_id_redacted: r.telegram_message_id_redacted,
        })),
      },
      null,
      2,
    ),
  );
  if (deliveredCount !== items.length) process.exitCode = 2;
}

main().catch((err) => {
  console.error(String(err?.stack || err));
  process.exit(1);
});
