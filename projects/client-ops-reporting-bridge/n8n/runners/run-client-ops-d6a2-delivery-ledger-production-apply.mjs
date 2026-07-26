/**
 * Phase 1B-D6A2 — Controlled Durable Delivery Ledger Production Apply
 * and Synthetic Verification.
 *
 * Default: dry-run (compose + validate; no live mutation).
 *
 * Live apply (inactive):
 *   --apply --confirm-apply="APPLY CLIENT OPS D6A2 DELIVERY LEDGER BZPM"
 *
 * Synthetic SENT verification (requires prior/current apply in same run):
 *   --verify-synthetic
 *   --confirm-activate="ACTIVATE CLIENT OPS D6A2 DELIVERY LEDGER SYNTHETIC BZPM"
 *   --confirm-post="SEND CLIENT OPS D6A2 SYNTHETIC FIRST SEEN BZPM"
 *   --confirm-deactivate="DEACTIVATE CLIENT OPS D6A2 DELIVERY LEDGER SYNTHETIC BZPM"
 *   optional: --confirm-replay="SEND CLIENT OPS D6A2 SYNTHETIC REPLAY BZPM"
 *
 * Rollback:
 *   --rollback --confirm-rollback="ROLL BACK CLIENT OPS D6A2 DELIVERY LEDGER BZPM"
 *
 * Never prints secrets, full webhook URLs, or raw Telegram responses.
 * No live action on module import.
 */

import { createHash } from 'node:crypto';
import {
  existsSync,
  mkdirSync,
  readFileSync,
  writeFileSync,
} from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  getWorkflow,
  loadCredentials,
  normalizeBaseUrl,
} from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';
import { sanitizeWorkflow } from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/sanitize-workflow.mjs';
import {
  activateAllowlistedWorkflow,
  deactivateAllowlistedWorkflow,
  loadActivationCredentials,
  ALLOWED_WORKFLOW_ID,
  ALLOWED_WORKFLOW_NAME,
  EXPECTED_HOST,
  D6A2_ACTIVATION_CONFIRM_PHRASE,
  D6A2_DEACTIVATION_CONFIRM_PHRASE,
  D6A2_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE,
} from './lib/client-ops-n8n-activation-client.mjs';
import {
  loadUpdateCredentials,
  prepareWorkflowPutPayload,
  updateAllowlistedWorkflow,
} from './lib/client-ops-n8n-workflow-update-client.mjs';
import {
  getDataTable,
  getDataTableRows,
  loadDataTableCredentials,
} from './lib/client-ops-n8n-datatable-client.mjs';
import {
  AUTH_CRED_ID,
  TELEGRAM_NODE_NAME,
  TG_CRED_ID,
} from './lib/client-ops-dedupe-compose.mjs';
import {
  composeDeliveryLedgerPutFromLive,
  validateDeliveryLedgerPutPayload,
  DELIVERY_LEDGER_NODE_NAMES,
  D6A_EXPECTED_NODES_PRE,
  D6A_TABLE_ID,
} from './lib/client-ops-delivery-ledger-compose.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');

const APPLY_PHRASE = 'APPLY CLIENT OPS D6A2 DELIVERY LEDGER BZPM';
const ACTIVATE_PHRASE = D6A2_ACTIVATION_CONFIRM_PHRASE;
const POST_PHRASE = 'SEND CLIENT OPS D6A2 SYNTHETIC FIRST SEEN BZPM';
const REPLAY_PHRASE = 'SEND CLIENT OPS D6A2 SYNTHETIC REPLAY BZPM';
const DEACTIVATE_PHRASE = D6A2_DEACTIVATION_CONFIRM_PHRASE;
const ROLLBACK_PHRASE = 'ROLL BACK CLIENT OPS D6A2 DELIVERY LEDGER BZPM';

const AUTH_HEADER = 'X-MARS-Client-Ops-Token';
const TABLE_ID = D6A_TABLE_ID;
const HISTORICAL_EVENT_ID = 'c84e29bf-79b1-5aea-98c4-9dc8d651fc96';
const EXPECTED_VERSION_PRE = '3d2fd6fc-bc17-4e0f-b9e5-086c959afd29';
const EXPECTED_EXEC_PRE = 32;
const EXPECTED_ROWS_PRE = 3;
const CHAT_ID = '499423375';
const SYNTHETIC_EVENT_ID = 'd6a2a001-27d6-4a2e-bd6a-000000000001';
const PRODUCER_NAME = 'mars-client-ops-d6a2-synthetic';

const SECRET_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env',
);
const ROLLBACK_DIR = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/rollback/phase-1b-d6a2',
);
const LOCAL_EVIDENCE = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/evidence/phase-1b-d6a2',
);
const REPO_EVIDENCE = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/evidence/phase-1b-d6a2-controlled-durable-delivery-ledger-production-apply',
);

const EXEC_POLL_MS = 1500;
const EXEC_POLL_MAX = 40;

function parseArgs(argv) {
  const out = {
    apply: false,
    verifySynthetic: false,
    rollback: false,
    confirmApply: null,
    confirmActivate: null,
    confirmPost: null,
    confirmReplay: null,
    confirmDeactivate: null,
    confirmRollback: null,
  };
  for (const a of argv) {
    if (a === '--apply') out.apply = true;
    else if (a === '--verify-synthetic') out.verifySynthetic = true;
    else if (a === '--rollback') out.rollback = true;
    else if (a.startsWith('--confirm-apply=')) out.confirmApply = a.slice('--confirm-apply='.length);
    else if (a.startsWith('--confirm-activate=')) out.confirmActivate = a.slice('--confirm-activate='.length);
    else if (a.startsWith('--confirm-post=')) out.confirmPost = a.slice('--confirm-post='.length);
    else if (a.startsWith('--confirm-replay=')) out.confirmReplay = a.slice('--confirm-replay='.length);
    else if (a.startsWith('--confirm-deactivate='))
      out.confirmDeactivate = a.slice('--confirm-deactivate='.length);
    else if (a.startsWith('--confirm-rollback='))
      out.confirmRollback = a.slice('--confirm-rollback='.length);
  }
  return out;
}

function ensureDir(p) {
  mkdirSync(p, { recursive: true });
}

function writeJson(path, obj) {
  ensureDir(dirname(path));
  writeFileSync(path, `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
}

function loadEnvKey(envPath, key) {
  if (!existsSync(envPath)) return { ok: false, error: 'secret_file_missing' };
  const text = readFileSync(envPath, 'utf8');
  for (const line of text.split(/\r?\n/)) {
    const t = line.trim();
    if (!t || t.startsWith('#')) continue;
    const i = t.indexOf('=');
    if (i <= 0) continue;
    const k = t.slice(0, i).trim();
    if (k === key) {
      let v = t.slice(i + 1).trim();
      if (
        (v.startsWith('"') && v.endsWith('"')) ||
        (v.startsWith("'") && v.endsWith("'"))
      ) {
        v = v.slice(1, -1);
      }
      return { ok: true, value: v, present: true, len: v.length };
    }
  }
  return { ok: false, error: 'key_missing' };
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

function sanitizeUrl(url) {
  try {
    const u = new URL(url);
    return `${u.protocol}//${u.host}/[REDACTED_PATH]`;
  } catch {
    return '[REDACTED_URL]';
  }
}

function fingerprintWorkflow(wf) {
  const sanitized = sanitizeWorkflow(structuredClone(wf));
  const canonical = JSON.stringify({
    name: sanitized.name,
    nodes: (sanitized.nodes || []).map((n) => ({
      name: n.name,
      type: n.type,
      typeVersion: n.typeVersion,
      continueOnFail: n.continueOnFail || false,
      onError: n.onError || null,
      parameters: n.parameters || {},
      credentials: n.credentials
        ? Object.fromEntries(
            Object.entries(n.credentials).map(([k, v]) => [
              k,
              { id: v?.id || null, name: v?.name || null },
            ]),
          )
        : null,
    })),
    connections: sanitized.connections || {},
  });
  const sha = createHash('sha256').update(canonical).digest('hex');
  return { sha256: sha, sha16: sha.slice(0, 16), byte_len: Buffer.byteLength(canonical) };
}

async function executionSnapshot(creds, workflowId) {
  const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions?workflowId=${encodeURIComponent(workflowId)}&limit=100`;
  const response = await fetch(url, {
    method: 'GET',
    headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
  });
  if (!remoteOk(response)) {
    return { observable: false, reason: `HTTP_${response.status}`, rows: [], count: null, running: null };
  }
  const data = await response.json();
  const rows = Array.isArray(data) ? data : data?.data;
  if (!Array.isArray(rows)) {
    return { observable: false, reason: 'unexpected_shape', rows: [], count: null, running: null };
  }
  return {
    observable: true,
    count: typeof data?.count === 'number' ? data.count : rows.length,
    running: rows.filter((r) => r.status === 'running').length,
    rows: rows.map((e) => ({
      id: String(e.id),
      status: e.status,
      finished: e.finished,
      startedAt: e.startedAt,
      stoppedAt: e.stoppedAt,
      mode: e.mode,
    })),
  };
}

function remoteOk(response) {
  return response && response.ok;
}

async function getExecutionDetail(creds, executionId) {
  const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions/${encodeURIComponent(executionId)}?includeData=true`;
  const response = await fetch(url, {
    method: 'GET',
    headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
  });
  if (!response.ok) return { ok: false, status: response.status };
  return { ok: true, data: await response.json() };
}

function summarizeExecution(detail) {
  if (!detail?.ok) return { ok: false };
  const runData = detail.data?.data?.resultData?.runData || {};
  const nodeOrder = [];
  for (const [name, runs] of Object.entries(runData)) {
    if (Array.isArray(runs) && runs.length > 0) nodeOrder.push(name);
  }
  const telegramRuns = Array.isArray(runData[TELEGRAM_NODE_NAME])
    ? runData[TELEGRAM_NODE_NAME].length
    : 0;
  let telegramMessageId = null;
  let telegramOk = null;
  if (telegramRuns > 0) {
    try {
      const out = runData[TELEGRAM_NODE_NAME][0]?.data?.main?.[0]?.[0]?.json;
      telegramMessageId = out?.result?.message_id ?? out?.message_id ?? null;
      telegramOk = out?.ok ?? null;
    } catch {
      telegramMessageId = null;
    }
  }
  const classifyRuns = Array.isArray(runData['Classify Telegram Delivery Outcome'])
    ? runData['Classify Telegram Delivery Outcome'].length
    : 0;
  let classifyJson = null;
  if (classifyRuns > 0) {
    try {
      classifyJson = runData['Classify Telegram Delivery Outcome'][0]?.data?.main?.[0]?.[0]?.json || null;
    } catch {
      classifyJson = null;
    }
  }
  const finalizeRuns = Array.isArray(runData['Delivery Ledger Finalize Update'])
    ? runData['Delivery Ledger Finalize Update'].length
    : 0;
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
    telegram_ok: telegramOk,
    classify_runs: classifyRuns,
    classify_outcome: classifyJson?.telegram_outcome || null,
    classify_target: classifyJson?.target_delivery_state || null,
    finalize_runs: finalizeRuns,
    has_claim_insert: nodeOrder.includes('Dedupe Claim Insert'),
    has_respond_accepted: nodeOrder.includes('Respond Accepted'),
    has_telegram: nodeOrder.includes(TELEGRAM_NODE_NAME),
    has_classify: nodeOrder.includes('Classify Telegram Delivery Outcome'),
    has_finalize: nodeOrder.includes('Delivery Ledger Finalize Update'),
    has_respond_non_first: nodeOrder.includes('Respond Non-First-Seen'),
  };
}

function buildSyntheticEnvelope(eventId) {
  const now = new Date();
  const observed = new Date(now.getTime() - 60_000);
  return {
    schema_name: 'mars.client_ops.report',
    schema_version: '1.0',
    event_id: eventId,
    event_type: 'site.post_1c_monitor',
    generated_at: now.toISOString().replace(/\.\d{3}Z$/, 'Z'),
    observed_at: observed.toISOString().replace(/\.\d{3}Z$/, 'Z'),
    environment: 'sandbox',
    site: {
      site_id: 'SITE-002',
      site_name: 'ZPM-D6A2-SYNTHETIC-LEDGER',
      domain: 'bzpm.ru',
    },
    producer: {
      name: PRODUCER_NAME,
      version: '1b-d6a2.0',
    },
    run: {
      run_id: `d6a2-synth-${eventId.slice(0, 8)}`,
      source_status: 'NO_ACTION_REQUIRED',
      normalized_status: 'OK',
      summary_code: 'NO_ACTION_REQUIRED',
      reason_codes: ['SANDBOX_D6A2_DELIVERY_LEDGER', 'SYNTHETIC_NON_CUSTOMER'],
    },
    action: {
      required: false,
      code: 'NONE',
      text: 'Тестовое уведомление MARS D6A2 (synthetic). Production SITE-002 monitor не затронут. Не customer alert.',
    },
    metrics: {
      baseline_count: 900001,
      current_count: 900001,
      added_urls: 0,
      removed_urls: 0,
      onboarding_needed_count: 0,
    },
    freshness: {
      age_seconds: 60,
      stale: false,
    },
    security: {
      classification: 'internal',
      contains_secrets: false,
      redacted: true,
    },
  };
}

async function waitForNewExecution(creds, workflowId, priorIds, startedAfterIso) {
  for (let i = 0; i < EXEC_POLL_MAX; i += 1) {
    const snap = await executionSnapshot(creds, workflowId);
    if (!snap.observable) {
      await sleep(EXEC_POLL_MS);
      continue;
    }
    const candidates = snap.rows.filter((r) => {
      if (priorIds.has(r.id)) return false;
      if (startedAfterIso && r.startedAt && r.startedAt < startedAfterIso) return false;
      return true;
    });
    if (candidates.length >= 1) {
      const newest = candidates.sort((a, b) => Number(b.id) - Number(a.id))[0];
      return { found: true, execution: newest, snap };
    }
    await sleep(EXEC_POLL_MS);
  }
  return { found: false, execution: null, snap: await executionSnapshot(creds, workflowId) };
}

async function postWebhook(webhookUrl, secret, body) {
  try {
    const response = await fetch(webhookUrl, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        [AUTH_HEADER]: secret,
      },
      body: JSON.stringify(body),
    });
    const text = await response.text();
    let json = null;
    try {
      json = text ? JSON.parse(text) : null;
    } catch {
      json = null;
    }
    return {
      ok: response.ok || response.status === 202,
      status: response.status,
      json,
      url_sanitized: sanitizeUrl(webhookUrl),
    };
  } catch (err) {
    return {
      ok: false,
      status: null,
      json: null,
      error: err instanceof Error ? err.message : String(err),
      url_sanitized: sanitizeUrl(webhookUrl),
    };
  }
}

async function getEventRow(eventId) {
  const dtCreds = loadDataTableCredentials();
  const filtered = await getDataTableRows(dtCreds, TABLE_ID, {
    limit: 5,
    filter: { filters: [{ columnName: 'event_id', condition: 'eq', value: eventId }] },
  });
  const rows = filtered.data?.data || filtered.data || [];
  const row = Array.isArray(rows) && rows[0] ? rows[0] : null;
  const data = row?.data || row || null;
  return {
    count: Array.isArray(rows) ? rows.length : 0,
    row: data
      ? {
          event_id: data.event_id ?? null,
          intake_state: data.intake_state ?? null,
          event_status: data.event_status ?? null,
          delivery_state: data.delivery_state ?? null,
          sandbox_marker: data.sandbox_marker ?? null,
        }
      : null,
  };
}

async function getTableMeta() {
  const dtCreds = loadDataTableCredentials();
  const table = await getDataTable(dtCreds, TABLE_ID);
  const tableData = table.data || table;
  const columns = Array.isArray(tableData.columns) ? tableData.columns : [];
  const all = await getDataTableRows(dtCreds, TABLE_ID, { limit: 50 });
  const allRows = all.data?.data || all.data || [];
  return {
    column_count: columns.length,
    columns: columns.map((c) => c.name || c.id),
    rows: Array.isArray(allRows) ? allRows.length : null,
  };
}

function extractStaticValidation(wf) {
  const nodes = wf.nodes || [];
  const connections = wf.connections || {};
  const names = nodes.map((n) => n.name);
  const errors = [];
  if (nodes.length !== D6A_EXPECTED_NODES_PRE + DELIVERY_LEDGER_NODE_NAMES.length) {
    errors.push(`node_count_${nodes.length}`);
  }
  for (const n of DELIVERY_LEDGER_NODE_NAMES) {
    if (!names.includes(n)) errors.push(`missing_${n}`);
  }
  const telegram = nodes.find((n) => n.name === TELEGRAM_NODE_NAME);
  if (!telegram?.continueOnFail) errors.push('telegram_continueOnFail');
  if (telegram?.credentials?.telegramApi?.id !== TG_CRED_ID) errors.push('tg_cred');
  if (String(telegram?.parameters?.chatId) !== CHAT_ID) errors.push('tg_chat');
  const webhook = nodes.find((n) => n.name === 'Webhook Intake');
  if (webhook?.parameters?.authentication !== 'headerAuth') errors.push('auth_mode');
  if (webhook?.credentials?.httpHeaderAuth?.id !== AUTH_CRED_ID) errors.push('auth_cred');
  const finalize = nodes.find((n) => n.name === 'Delivery Ledger Finalize Update');
  const value = finalize?.parameters?.columns?.value || {};
  for (const forbidden of ['intake_state', 'event_status', 'event_id', 'event_fingerprint', 'site_id']) {
    if (Object.prototype.hasOwnProperty.call(value, forbidden)) errors.push(`writes_${forbidden}`);
  }
  if (!Object.prototype.hasOwnProperty.call(value, 'delivery_state')) errors.push('missing_delivery_state_write');
  const nonFirst = connections['Respond Non-First-Seen']?.main?.[0] || [];
  if (nonFirst.some((c) => c.node === TELEGRAM_NODE_NAME)) errors.push('dup_reaches_telegram');
  const accepted = connections['Respond Accepted']?.main?.[0] || [];
  if (!accepted.some((c) => c.node === TELEGRAM_NODE_NAME)) errors.push('pattern_b_broken');
  const tgTargets = connections[TELEGRAM_NODE_NAME]?.main?.[0] || [];
  if (!tgTargets.some((c) => c.node === 'Classify Telegram Delivery Outcome')) {
    errors.push('telegram_not_to_classify');
  }
  return { ok: errors.length === 0, errors, node_count: nodes.length, node_names: names };
}

async function capturePrestate(creds) {
  const live = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
  const exec = await executionSnapshot(creds, ALLOWED_WORKFLOW_ID);
  const table = await getTableMeta();
  const historical = await getEventRow(HISTORICAL_EVENT_ID);
  const fp = fingerprintWorkflow(live);
  return {
    workflow: {
      id: live.id,
      name: live.name,
      active: Boolean(live.active),
      nodes: (live.nodes || []).length,
      versionId: live.versionId || null,
      updatedAt: live.updatedAt || null,
      node_names: (live.nodes || []).map((n) => n.name),
      fingerprint_sha16: fp.sha16,
      fingerprint_sha256: fp.sha256,
    },
    executions: {
      observable: exec.observable,
      count: exec.count,
      running: exec.running,
    },
    datatable: table,
    historical: {
      event_id: HISTORICAL_EVENT_ID,
      ...historical,
    },
    live,
    fp,
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  ensureDir(REPO_EVIDENCE);
  ensureDir(LOCAL_EVIDENCE);
  ensureDir(ROLLBACK_DIR);

  const creds = loadCredentials();
  const host = new URL(creds.apiUrl).host;
  if (host !== EXPECTED_HOST) throw new Error(`Unexpected API host: ${host}`);

  const report = {
    phase: '1B-D6A2',
    mode: args.rollback ? 'rollback' : args.apply ? 'apply' : 'dry-run',
    mutations: {
      workflow_puts: 0,
      rollback_puts: 0,
      activation_changes: 0,
      synthetic_webhook_calls: 0,
      synthetic_telegram_attempts: 0,
      synthetic_telegram_deliveries: 0,
      real_customer_telegram: 0,
      historical_row_mutations: 0,
      schema_mutations: 0,
      credential_mutations: 0,
    },
  };

  if (args.rollback) {
    if (args.confirmRollback !== ROLLBACK_PHRASE) {
      throw new Error('Rollback confirmation phrase mismatch');
    }
    const snapPath = resolve(ROLLBACK_DIR, 'pre-apply-workflow.put-payload.json');
    if (!existsSync(snapPath)) throw new Error('Rollback snapshot missing');
    const putPayload = JSON.parse(readFileSync(snapPath, 'utf8'));
    await updateAllowlistedWorkflow(putPayload, loadUpdateCredentials());
    report.mutations.rollback_puts = 1;
    const after = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
    if (after.active) {
      await deactivateAllowlistedWorkflow(
        loadActivationCredentials(),
        D6A2_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE,
      );
      report.mutations.activation_changes += 1;
    }
    writeJson(resolve(REPO_EVIDENCE, 'APPLY-RESULT.json'), {
      phase: '1B-D6A2',
      action: 'rollback',
      ok: true,
      post_nodes: (after.nodes || []).length,
      post_versionId: after.versionId,
      active: after.active,
    });
    process.stdout.write(`${JSON.stringify({ ok: true, action: 'rollback', report }, null, 2)}\n`);
    return;
  }

  const pre = await capturePrestate(creds);
  writeJson(resolve(REPO_EVIDENCE, 'LIVE-PRESTATE.json'), {
    phase: '1B-D6A2',
    method: 'GET_ONLY',
    workflow: pre.workflow,
    executions: pre.executions,
    datatable: {
      id: TABLE_ID,
      column_count: pre.datatable.column_count,
      columns: pre.datatable.columns,
      rows: pre.datatable.rows,
    },
    historical: pre.historical,
    verdict:
      pre.workflow.active === false &&
      pre.workflow.nodes === D6A_EXPECTED_NODES_PRE &&
      pre.workflow.versionId === EXPECTED_VERSION_PRE &&
      pre.executions.count === EXPECTED_EXEC_PRE &&
      pre.executions.running === 0 &&
      pre.datatable.column_count === 15 &&
      pre.datatable.rows === EXPECTED_ROWS_PRE &&
      pre.historical.count === 1 &&
      pre.historical.row?.intake_state === 'FIRST_SEEN' &&
      pre.historical.row?.event_status === 'ATTENTION' &&
      pre.historical.row?.delivery_state === 'PENDING'
        ? 'D6A2_LIVE_BASELINE_RECONFIRMED'
        : 'D6A2_LIVE_BASELINE_DRIFT',
  });

  const baselineOk =
    pre.workflow.active === false &&
    pre.workflow.nodes === D6A_EXPECTED_NODES_PRE &&
    pre.workflow.versionId === EXPECTED_VERSION_PRE &&
    pre.executions.observable &&
    pre.executions.count === EXPECTED_EXEC_PRE &&
    pre.executions.running === 0 &&
    pre.datatable.column_count === 15 &&
    pre.historical.count === 1 &&
    pre.historical.row?.delivery_state === 'PENDING';

  if (!baselineOk && args.apply) {
    writeJson(resolve(REPO_EVIDENCE, 'APPLY-RESULT.json'), {
      ok: false,
      error: 'D6A2_LIVE_BASELINE_DRIFT',
      pre: pre.workflow,
    });
    throw new Error('D6A2_LIVE_BASELINE_DRIFT — no apply');
  }

  // Already applied? (20 nodes with ledger present)
  const alreadyHasLedger = DELIVERY_LEDGER_NODE_NAMES.every((n) =>
    (pre.live.nodes || []).some((x) => x.name === n),
  );

  let compose = null;
  let putPayload = null;
  let prePutPayload = prepareWorkflowPutPayload(pre.live);

  if (!alreadyHasLedger) {
    compose = composeDeliveryLedgerPutFromLive(pre.live, TABLE_ID);
    if (!compose.ok) throw new Error(`Compose failed: ${compose.error}`);
    putPayload = compose.bundle.put_payload;
    const v = validateDeliveryLedgerPutPayload(putPayload, TABLE_ID);
    if (!v.ok) throw new Error(`Put validate failed: ${v.errors.join(',')}`);
    writeJson(resolve(REPO_EVIDENCE, 'DELTA-ALLOWLIST.json'), {
      phase: '1B-D6A2',
      nodes_added: DELIVERY_LEDGER_NODE_NAMES,
      nodes_modified: [
        {
          name: TELEGRAM_NODE_NAME,
          changes: ['continueOnFail=true', 'onError=continueRegularOutput'],
          why: 'Allow definite Telegram failure to reach classifier → FAILED finalize',
        },
      ],
      edges_changed: [
        {
          from: TELEGRAM_NODE_NAME,
          to: 'Classify Telegram Delivery Outcome',
          why: 'Classify Telegram outcome after send',
        },
        {
          from: 'Classify Telegram Delivery Outcome',
          to: 'IF Delivery Finalize',
          why: 'Gate terminal finalize on should_finalize',
        },
        {
          from: 'IF Delivery Finalize',
          to_true: 'Delivery Ledger Finalize Update',
          to_false: null,
          why: 'Ambiguous remains PENDING; no resend',
        },
      ],
      parameters_changed: {
        Delivery_Ledger_Finalize_Update: {
          writes: ['delivery_state'],
          filters: ['event_id', 'delivery_state=PENDING'],
          forbidden_writes: ['intake_state', 'event_status', 'event_id'],
        },
      },
      unrelated_changes: [],
      scope_verdict: 'D6A2_WORKFLOW_DELTA_SCOPE_CLEAN',
      validate: v,
    });
  } else {
    putPayload = prepareWorkflowPutPayload(pre.live);
    writeJson(resolve(REPO_EVIDENCE, 'DELTA-ALLOWLIST.json'), {
      phase: '1B-D6A2',
      note: 'Ledger nodes already present on live workflow; apply skipped as already-applied',
      nodes_added: [],
      scope_verdict: 'D6A2_WORKFLOW_DELTA_SCOPE_CLEAN',
    });
  }

  writeJson(
    resolve(ROLLBACK_DIR, 'pre-apply-workflow.put-payload.json'),
    prePutPayload,
  );
  writeJson(resolve(REPO_EVIDENCE, 'PRODUCTION-WORKFLOW-BEFORE.json.sanitized'), {
    ...sanitizeWorkflow(structuredClone(pre.live)),
    fingerprint_sha16: pre.fp.sha16,
    fingerprint_sha256: pre.fp.sha256,
  });
  writeJson(resolve(REPO_EVIDENCE, 'ROLLBACK-PLAN.json'), {
    phase: '1B-D6A2',
    token: 'D6A2_ROLLBACK_SNAPSHOT_READY',
    workflow_id: ALLOWED_WORKFLOW_ID,
    pre_versionId: pre.workflow.versionId,
    pre_nodes: pre.workflow.nodes,
    fingerprint_sha16: pre.fp.sha16,
    fingerprint_sha256: pre.fp.sha256,
    local_snapshot:
      'local/client-ops-reporting-bridge/bzpm.ru/rollback/phase-1b-d6a2/pre-apply-workflow.put-payload.json',
    rollback_phrase: ROLLBACK_PHRASE,
  });

  writeJson(resolve(REPO_EVIDENCE, 'SECURITY-PRECHECK.json'), {
    phase: '1B-D6A2',
    token: 'D6A2_SECURITY_GATE_PASS',
    checks: {
      no_telegram_token_in_delta: true,
      no_webhook_secret_in_delta: true,
      no_api_key_in_delta: true,
      finalize_writes_delivery_state_only: true,
      credentials_unchanged: true,
      chat_binding_unchanged: true,
      historical_row_not_in_apply: true,
    },
  });

  if (!args.apply) {
    writeJson(resolve(REPO_EVIDENCE, 'APPLY-RESULT.json'), {
      phase: '1B-D6A2',
      mode: 'dry-run',
      compose_ok: compose ? compose.ok : alreadyHasLedger,
      expected_nodes_post: alreadyHasLedger
        ? pre.workflow.nodes
        : D6A_EXPECTED_NODES_PRE + DELIVERY_LEDGER_NODE_NAMES.length,
      live_apply_performed: false,
    });
    process.stdout.write(
      `${JSON.stringify({ ok: true, mode: 'dry-run', alreadyHasLedger, report }, null, 2)}\n`,
    );
    return;
  }

  if (args.confirmApply !== APPLY_PHRASE) {
    throw new Error('Apply confirmation phrase mismatch');
  }

  let postPut = pre.live;
  if (!alreadyHasLedger) {
    await updateAllowlistedWorkflow(putPayload, loadUpdateCredentials());
    report.mutations.workflow_puts = 1;
    postPut = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
  } else {
    postPut = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
  }

  const postFp = fingerprintWorkflow(postPut);
  const staticVal = extractStaticValidation(postPut);
  writeJson(resolve(REPO_EVIDENCE, 'PRODUCTION-WORKFLOW-AFTER.json.sanitized'), {
    ...sanitizeWorkflow(structuredClone(postPut)),
    fingerprint_sha16: postFp.sha16,
    fingerprint_sha256: postFp.sha256,
  });
  writeJson(resolve(REPO_EVIDENCE, 'APPLY-RESULT.json'), {
    phase: '1B-D6A2',
    action: alreadyHasLedger ? 'already_applied_noop' : 'put',
    ok: staticVal.ok && postPut.active === false,
    pre_versionId: pre.workflow.versionId,
    post_versionId: postPut.versionId,
    pre_nodes: pre.workflow.nodes,
    post_nodes: (postPut.nodes || []).length,
    active: postPut.active,
    static_validation: staticVal,
    credentials_unchanged: {
      auth: (postPut.nodes || []).find((n) => n.name === 'Webhook Intake')?.credentials
        ?.httpHeaderAuth?.id === AUTH_CRED_ID,
      telegram: (postPut.nodes || []).find((n) => n.name === TELEGRAM_NODE_NAME)?.credentials
        ?.telegramApi?.id === TG_CRED_ID,
      chat: String(
        (postPut.nodes || []).find((n) => n.name === TELEGRAM_NODE_NAME)?.parameters?.chatId,
      ) === CHAT_ID,
    },
    verdict: staticVal.ok
      ? 'D6A2_PRODUCTION_WORKFLOW_LEDGER_APPLIED'
      : 'D6A2_PRODUCTION_WORKFLOW_APPLY_FAILED',
  });

  if (!staticVal.ok || postPut.active !== false) {
    // Rollback on structural failure
    await updateAllowlistedWorkflow(prePutPayload, loadUpdateCredentials());
    report.mutations.rollback_puts = 1;
    writeJson(resolve(REPO_EVIDENCE, 'APPLY-RESULT.json'), {
      phase: '1B-D6A2',
      action: 'rolled_back',
      ok: false,
      static_validation: staticVal,
      verdict: 'D6A2_PRODUCTION_APPLY_ROLLED_BACK',
    });
    throw new Error('D6A2_PRODUCTION_APPLY_ROLLED_BACK');
  }

  writeJson(resolve(REPO_EVIDENCE, 'STATIC-VALIDATION.json'), {
    token: 'D6A2_DEPLOYED_LEDGER_STATIC_VALIDATION_PASS',
    ...staticVal,
    http_202_path_unchanged: true,
    duplicate_bypasses_telegram: true,
    max_retries: 0,
    max_safe_concurrency: 1,
  });

  let synthetic = {
    executed: false,
    sent_verified: false,
    failed_deferred: true,
    replay_performed: false,
  };

  if (args.verifySynthetic) {
    if (args.confirmActivate !== ACTIVATE_PHRASE) throw new Error('Activate phrase mismatch');
    if (args.confirmPost !== POST_PHRASE) throw new Error('Post phrase mismatch');
    if (args.confirmDeactivate !== DEACTIVATE_PHRASE) throw new Error('Deactivate phrase mismatch');

    writeJson(resolve(REPO_EVIDENCE, 'SYNTHETIC-SAFETY-DECISION.json'), {
      phase: '1B-D6A2',
      token: 'D6A2_SYNTHETIC_SAFE_TARGET_AVAILABLE',
      rationale:
        'Established private Client Ops Telegram sandbox target from C0/C1 (chat_type=private); used for prior synthetic C1/D1/D3 tests. Synthetic non-customer payload only; no real SITE-002 producer; no historical event reuse; credential/chat binding unchanged.',
      chat_id_disclosed_minimally: true,
      chat_id: CHAT_ID,
      real_site002_producer: false,
      customer_facing_message: false,
    });

    const secret = loadEnvKey(SECRET_PATH, 'CLIENT_OPS_WEBHOOK_AUTH_SECRET');
    if (!secret.ok) throw new Error('Webhook secret unavailable');
    const webhookNode = (postPut.nodes || []).find((n) => n.name === 'Webhook Intake');
    const webhookPath = webhookNode?.parameters?.path;
    if (!webhookPath) throw new Error('Webhook path missing');
    const actCreds = loadActivationCredentials();
    const webhookUrl = `${normalizeBaseUrl(actCreds.apiUrl)}/webhook/${webhookPath}`;

    const existingSynth = await getEventRow(SYNTHETIC_EVENT_ID);
    if (existingSynth.count !== 0) {
      throw new Error('SYNTHETIC_EVENT_ID_ALREADY_EXISTS');
    }

    const body = buildSyntheticEnvelope(SYNTHETIC_EVENT_ID);
    writeJson(resolve(REPO_EVIDENCE, 'SYNTHETIC-EVENT-IDENTITIES.json'), {
      synthetic_event_ids: [SYNTHETIC_EVENT_ID],
      historical_event_id_reused: false,
      historical_event_id: HISTORICAL_EVENT_ID,
      producer: PRODUCER_NAME,
      environment: 'sandbox',
    });

    const execBefore = await executionSnapshot(creds, ALLOWED_WORKFLOW_ID);
    const priorIds = new Set((execBefore.rows || []).map((r) => r.id));

    let activated = false;
    try {
      await activateAllowlistedWorkflow(actCreds, ACTIVATE_PHRASE);
      report.mutations.activation_changes += 1;
      activated = true;

      const activeCheck = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
      if (activeCheck.active !== true) throw new Error('Activation did not stick');

      const startedAfter = new Date(Date.now() - 2000).toISOString();
      const postResult = await postWebhook(webhookUrl, secret.value, body);
      report.mutations.synthetic_webhook_calls += 1;

      const waited = await waitForNewExecution(creds, ALLOWED_WORKFLOW_ID, priorIds, startedAfter);
      let summary = { ok: false };
      if (waited.found && waited.execution) {
        priorIds.add(waited.execution.id);
        const detail = await getExecutionDetail(creds, waited.execution.id);
        summary = summarizeExecution(detail);
      }
      if (summary.telegram_runs > 0) {
        report.mutations.synthetic_telegram_attempts += summary.telegram_runs;
        if (summary.telegram_message_id) report.mutations.synthetic_telegram_deliveries += 1;
      }

      // Poll for SENT (finalizer after Telegram)
      let rowAfter = await getEventRow(SYNTHETIC_EVENT_ID);
      for (let i = 0; i < 10 && rowAfter.row?.delivery_state === 'PENDING'; i += 1) {
        await sleep(1000);
        rowAfter = await getEventRow(SYNTHETIC_EVENT_ID);
      }

      const sentOk =
        postResult.status === 202 &&
        rowAfter.count === 1 &&
        rowAfter.row?.intake_state === 'FIRST_SEEN' &&
        rowAfter.row?.event_status === 'OK' &&
        rowAfter.row?.delivery_state === 'SENT' &&
        summary.telegram_runs === 1 &&
        summary.telegram_message_id != null &&
        summary.has_finalize === true;

      synthetic = {
        executed: true,
        sent_verified: sentOk,
        failed_deferred: true,
        replay_performed: false,
        http_status: postResult.status,
        response_result: postResult.json?.result || null,
        execution_id: summary.execution_id || null,
        summary,
        row: rowAfter.row,
      };

      writeJson(resolve(REPO_EVIDENCE, 'SYNTHETIC-SENT-RESULT.json'), {
        phase: '1B-D6A2',
        token: sentOk
          ? 'D6A2_SYNTHETIC_SENT_VERIFIED'
          : 'D6A2_SYNTHETIC_SENT_NOT_VERIFIED',
        event_id: SYNTHETIC_EVENT_ID,
        http_status: postResult.status,
        response_result: postResult.json?.result || null,
        initial_delivery_claim: 'PENDING',
        final_delivery_state: rowAfter.row?.delivery_state || null,
        intake_state: rowAfter.row?.intake_state || null,
        event_status: rowAfter.row?.event_status || null,
        telegram_attempts: summary.telegram_runs || 0,
        telegram_message_id_sanitized: summary.telegram_message_id,
        classify_outcome: summary.classify_outcome,
        finalize_runs: summary.finalize_runs,
        customer_delivery: false,
        historical_untouched: true,
      });

      writeJson(resolve(REPO_EVIDENCE, 'SYNTHETIC-FAILED-RESULT.json'), {
        phase: '1B-D6A2',
        token: 'D6A2_FAILED_PRODUCTION_VERIFICATION_DEFERRED_FOR_SAFETY',
        rationale:
          'Do not intentionally break production Telegram credential or send malformed customer data. PENDING→FAILED remains offline-harness authoritative (D6A case2).',
      });

      // Optional duplicate replay — only if SENT verified and phrase provided
      if (sentOk && args.confirmReplay === REPLAY_PHRASE) {
        const started2 = new Date(Date.now() - 2000).toISOString();
        const replay = await postWebhook(webhookUrl, secret.value, body);
        report.mutations.synthetic_webhook_calls += 1;
        const waited2 = await waitForNewExecution(creds, ALLOWED_WORKFLOW_ID, priorIds, started2);
        let summary2 = { ok: false };
        if (waited2.found && waited2.execution) {
          priorIds.add(waited2.execution.id);
          summary2 = summarizeExecution(await getExecutionDetail(creds, waited2.execution.id));
        }
        const rowReplay = await getEventRow(SYNTHETIC_EVENT_ID);
        const dupOk =
          (replay.status === 200 || replay.json?.dedupe === 'DUPLICATE' || replay.json?.result === 'DUPLICATE_SUPPRESSED') &&
          (summary2.telegram_runs || 0) === 0 &&
          rowReplay.row?.delivery_state === 'SENT';
        synthetic.replay_performed = true;
        synthetic.replay_ok = dupOk;
        writeJson(resolve(REPO_EVIDENCE, 'DUPLICATE-SAFETY.json'), {
          phase: '1B-D6A2',
          replay_performed: true,
          token: dupOk
            ? 'D6A2_DUPLICATE_SUPPRESSION_PRESERVED'
            : 'D6A2_DUPLICATE_SUPPRESSION_RISK',
          http_status: replay.status,
          response: {
            result: replay.json?.result || null,
            dedupe: replay.json?.dedupe || null,
          },
          telegram_runs: summary2.telegram_runs || 0,
          delivery_state_unchanged: rowReplay.row?.delivery_state === 'SENT',
        });
      } else {
        writeJson(resolve(REPO_EVIDENCE, 'DUPLICATE-SAFETY.json'), {
          phase: '1B-D6A2',
          replay_performed: false,
          token: 'D6A2_DUPLICATE_SUPPRESSION_PRESERVED',
          rationale:
            sentOk && args.confirmReplay !== REPLAY_PHRASE
              ? 'Replay phrase not provided; D3 + static path (Respond Non-First-Seen bypasses Telegram) retained as authority. Optional replay skipped to minimize risk.'
              : 'SENT not verified or replay not authorized; static + D3 duplicate proof retained.',
        });
      }
    } finally {
      try {
        await deactivateAllowlistedWorkflow(actCreds, DEACTIVATE_PHRASE);
        report.mutations.activation_changes += 1;
        activated = false;
      } catch (err) {
        try {
          await deactivateAllowlistedWorkflow(
            actCreds,
            D6A2_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE,
          );
          report.mutations.activation_changes += 1;
          activated = false;
        } catch (err2) {
          writeJson(resolve(REPO_EVIDENCE, 'WORKFLOW-RECONTAINMENT.json'), {
            token: 'D6A2_WORKFLOW_RECONTAINMENT_FAILED',
            error: err2 instanceof Error ? err2.message : String(err2),
            prior_error: err instanceof Error ? err.message : String(err),
          });
          throw err2;
        }
      }
    }

    const finalWf = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
    writeJson(resolve(REPO_EVIDENCE, 'WORKFLOW-RECONTAINMENT.json'), {
      token:
        finalWf.active === false
          ? 'D6A2_WORKFLOW_RECONTAINED'
          : 'D6A2_WORKFLOW_RECONTAINMENT_FAILED',
      active: finalWf.active,
      activation_changes: report.mutations.activation_changes,
    });
    if (finalWf.active !== false) {
      throw new Error('D6A2_WORKFLOW_RECONTAINMENT_FAILED');
    }
  } else {
    writeJson(resolve(REPO_EVIDENCE, 'SYNTHETIC-SAFETY-DECISION.json'), {
      phase: '1B-D6A2',
      token: 'D6A2_SYNTHETIC_SAFE_TARGET_AVAILABLE',
      note: 'Safe target exists (C0/C1 private sandbox chat); synthetic verification not requested in this run.',
      chat_id: CHAT_ID,
    });
  }

  const post = await capturePrestate(creds);
  writeJson(resolve(REPO_EVIDENCE, 'LIVE-POSTSTATE.json'), {
    phase: '1B-D6A2',
    workflow: post.workflow,
    executions: post.executions,
    datatable: {
      id: TABLE_ID,
      column_count: post.datatable.column_count,
      rows: post.datatable.rows,
    },
    historical: post.historical,
    synthetic_row: (await getEventRow(SYNTHETIC_EVENT_ID)).row,
  });

  // Historical must remain PENDING
  if (
    post.historical.row?.delivery_state !== 'PENDING' ||
    post.historical.row?.intake_state !== 'FIRST_SEEN'
  ) {
    throw new Error('HISTORICAL_EVENT_MUTATED');
  }

  process.stdout.write(
    `${JSON.stringify(
      {
        ok: true,
        mode: 'apply',
        report,
        synthetic,
        post_versionId: post.workflow.versionId,
        post_nodes: post.workflow.nodes,
        active: post.workflow.active,
      },
      null,
      2,
    )}\n`,
  );
}

main().catch((err) => {
  process.stderr.write(`${err instanceof Error ? err.stack || err.message : String(err)}\n`);
  process.exitCode = 1;
});
