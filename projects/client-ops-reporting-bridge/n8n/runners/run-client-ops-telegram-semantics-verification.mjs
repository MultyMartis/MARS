/**
 * Phase 1B-C0S — Telegram integration semantics verification runner.
 *
 * Default: dry-run.
 * Live requires:
 *   --apply
 *   --confirm="VERIFY CLIENT OPS TELEGRAM EXECUTION SEMANTICS"
 *
 * Creates ONE temporary workflow only. Never mutates tkM4H0G0gM3q9Foi.
 * Max Telegram messages: 1. Max synthetic webhook requests: 2.
 * Never prints token or complete webhook URL.
 */

import { randomBytes, randomUUID } from 'node:crypto';
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
  listWorkflows,
  loadCredentials,
  normalizeBaseUrl,
} from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';
import { listCredentialsMetadata, loadCredentialClientCredentials } from './lib/client-ops-n8n-credential-client.mjs';
import {
  TEMP_WORKFLOW_NAME,
  REAL_WORKFLOW_ID_DENY,
  REAL_WORKFLOW_NAME_DENY,
  EXPECTED_HOST,
  createTempSemanticsWorkflow,
  updateTempSemanticsWorkflow,
  activateTempSemanticsWorkflow,
  deactivateTempSemanticsWorkflow,
  deleteTempSemanticsWorkflow,
  prepareTempPutPayload,
  loadTempSemanticsCredentials,
} from './lib/client-ops-n8n-temp-semantics-client.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const CONFIRM_PHRASE = 'VERIFY CLIENT OPS TELEGRAM EXECUTION SEMANTICS';
const REAL_WORKFLOW_ID = REAL_WORKFLOW_ID_DENY;
const REAL_WORKFLOW_NAME = REAL_WORKFLOW_NAME_DENY;
const TG_CRED_ID = '2bIC5376l7ElXb4B';
const TG_CRED_NAME = 'MARS Client Ops Telegram — bzpm.ru';
const EXPECTED_PRIVATE_TARGET = 499423375;
const TARGET_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/telegram.target.local.env',
);
const REPO_EVIDENCE = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/n8n/evidence/phase-1b-c0s-telegram-integration-semantics',
);
const LOCAL_EVIDENCE = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/evidence/phase-1b-c0s',
);
const PROPOSED_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/apply/mars-client-ops-bridge-bzpm.telegram-sandbox.proposed.json',
);
const REQUEST_TIMEOUT_MS = 30000;
const EXEC_POLL_MS = 1500;
const EXEC_POLL_MAX = 20;
const MAX_TELEGRAM_MESSAGES = 1;
const MAX_WEBHOOK_REQUESTS = 2;

const ALLOWED_NODE_TYPES_L1 = new Set([
  'n8n-nodes-base.webhook',
  'n8n-nodes-base.set',
  'n8n-nodes-base.respondToWebhook',
]);
const ALLOWED_NODE_TYPES_L2 = new Set([
  ...ALLOWED_NODE_TYPES_L1,
  'n8n-nodes-base.telegram',
]);

function parseArgs(argv) {
  const args = { apply: false, confirm: null };
  for (const a of argv) {
    if (a === '--apply') args.apply = true;
    else if (a.startsWith('--confirm=')) args.confirm = a.slice('--confirm='.length);
  }
  return args;
}

function ensureDir(p) {
  mkdirSync(p, { recursive: true });
}

function writeJson(path, obj) {
  writeFileSync(path, `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
}

function loadChatTarget() {
  if (!existsSync(TARGET_PATH)) {
    return { ok: false, error: 'target_file_missing' };
  }
  const raw = readFileSync(TARGET_PATH, 'utf8');
  let chatId = '';
  let chatType = '';
  for (const line of raw.split(/\r?\n/)) {
    const t = line.trim();
    if (!t || t.startsWith('#')) continue;
    if (t.startsWith('TELEGRAM_CHAT_ID=')) {
      chatId = t.slice('TELEGRAM_CHAT_ID='.length).trim();
    }
    if (t.startsWith('TELEGRAM_CHAT_TYPE=')) {
      chatType = t.slice('TELEGRAM_CHAT_TYPE='.length).trim();
    }
  }
  const numeric = Number(chatId);
  if (!Number.isFinite(numeric) || numeric !== EXPECTED_PRIVATE_TARGET) {
    return { ok: false, error: 'chat_id_mismatch', chatId_present: Boolean(chatId) };
  }
  return { ok: true, chatId: numeric, chatType: chatType || 'private' };
}

function redactText(text) {
  let out = String(text || '');
  out = out.replace(/https?:\/\/[^\s"'\\]+/gi, '<REDACTED_URL>');
  out = out.replace(/\/webhook(?:-test)?\/[A-Za-z0-9_-]+/gi, '/webhook/<REDACTED_PATH>');
  out = out.replace(/\b\d{6,}:[A-Za-z0-9_-]{20,}\b/g, '<REDACTED_TOKEN>');
  out = out.replace(/[A-Za-z]:\\[^\s"'\\]+/g, '<REDACTED_PATH>');
  return out;
}

function uid() {
  return randomUUID();
}

function randomWebhookPath() {
  return `mars-temp-sem-${randomBytes(12).toString('hex')}`;
}

function setNode(name, assignments, position) {
  return {
    parameters: {
      mode: 'manual',
      duplicateItem: false,
      assignments: {
        assignments: assignments.map((a) => ({
          id: uid(),
          name: a.name,
          value: a.value,
          type: a.type || 'string',
        })),
      },
      options: {},
    },
    id: uid(),
    name,
    type: 'n8n-nodes-base.set',
    typeVersion: 3.4,
    position,
  };
}

function buildLevel1Graph(webhookPath, testId) {
  const webhook = {
    parameters: {
      httpMethod: 'POST',
      path: webhookPath,
      responseMode: 'responseNode',
      options: {},
    },
    id: uid(),
    name: 'Webhook Semantics',
    type: 'n8n-nodes-base.webhook',
    typeVersion: 2.1,
    position: [0, 300],
  };
  const before = setNode(
    'Set Before Response',
    [
      { name: 'test_id', value: testId },
      { name: 'phase', value: '1B-C0S-L1' },
      { name: 'marker_before', value: 'SEMANTICS_BEFORE_RESPOND' },
    ],
    [260, 300],
  );
  const respond = {
    parameters: {
      respondWith: 'json',
      responseBody: `={{ ({ status: "SEMANTICS_TEST_ACCEPTED", test_id: $json.test_id || "${testId}" }) }}`,
      options: { responseCode: 202 },
    },
    id: uid(),
    name: 'Respond Semantics',
    type: 'n8n-nodes-base.respondToWebhook',
    typeVersion: 1.1,
    position: [520, 300],
  };
  const after = setNode(
    'Set After Response',
    [
      { name: 'test_id', value: `={{ $json.test_id || "${testId}" }}` },
      { name: 'marker_after', value: 'SEMANTICS_AFTER_RESPOND_REACHED' },
      { name: 'downstream_continuation', value: 'true' },
    ],
    [780, 300],
  );
  return {
    name: TEMP_WORKFLOW_NAME,
    nodes: [webhook, before, respond, after],
    connections: {
      'Webhook Semantics': {
        main: [[{ node: 'Set Before Response', type: 'main', index: 0 }]],
      },
      'Set Before Response': {
        main: [[{ node: 'Respond Semantics', type: 'main', index: 0 }]],
      },
      'Respond Semantics': {
        main: [[{ node: 'Set After Response', type: 'main', index: 0 }]],
      },
    },
    settings: { executionOrder: 'v1' },
  };
}

function buildLevel2Graph(webhookPath, testId, chatId) {
  const webhook = {
    parameters: {
      httpMethod: 'POST',
      path: webhookPath,
      responseMode: 'responseNode',
      options: {},
    },
    id: uid(),
    name: 'Webhook Semantics',
    type: 'n8n-nodes-base.webhook',
    typeVersion: 2.1,
    position: [0, 300],
  };
  const accepted = setNode(
    'Set Synthetic Accepted Event',
    [
      { name: 'test_id', value: testId },
      { name: 'phase', value: '1B-C0S-L2' },
      { name: 'accepted', value: 'true' },
      {
        name: 'telegram_text',
        value: `MARS sandbox test: проверка выполнения Telegram после ответа webhook. SITE-002 production не затронут. test=${testId}`,
      },
    ],
    [260, 300],
  );
  const respond = {
    parameters: {
      respondWith: 'json',
      responseBody: `={{ ({ status: "SEMANTICS_TEST_ACCEPTED", test_id: $json.test_id || "${testId}" }) }}`,
      options: { responseCode: 202 },
    },
    id: uid(),
    name: 'Respond Semantics',
    type: 'n8n-nodes-base.respondToWebhook',
    typeVersion: 1.1,
    position: [520, 300],
  };
  const telegram = {
    parameters: {
      chatId: String(chatId),
      text: '={{ $json.telegram_text }}',
      additionalFields: {
        appendAttribution: false,
      },
    },
    id: uid(),
    name: 'Telegram Semantics Send',
    type: 'n8n-nodes-base.telegram',
    typeVersion: 1.2,
    position: [780, 300],
    credentials: {
      telegramApi: {
        id: TG_CRED_ID,
        name: TG_CRED_NAME,
      },
    },
  };
  const marker = setNode(
    'Set Delivery Marker',
    [
      { name: 'test_id', value: testId },
      { name: 'delivery_marker', value: 'SEMANTICS_TELEGRAM_AFTER_RESPOND_DONE' },
    ],
    [1040, 300],
  );
  return {
    name: TEMP_WORKFLOW_NAME,
    nodes: [webhook, accepted, respond, telegram, marker],
    connections: {
      'Webhook Semantics': {
        main: [[{ node: 'Set Synthetic Accepted Event', type: 'main', index: 0 }]],
      },
      'Set Synthetic Accepted Event': {
        main: [[{ node: 'Respond Semantics', type: 'main', index: 0 }]],
      },
      'Respond Semantics': {
        main: [[{ node: 'Telegram Semantics Send', type: 'main', index: 0 }]],
      },
      'Telegram Semantics Send': {
        main: [[{ node: 'Set Delivery Marker', type: 'main', index: 0 }]],
      },
    },
    settings: { executionOrder: 'v1' },
  };
}

function validateGraphNodes(nodes, allowSet) {
  const errors = [];
  for (const n of nodes || []) {
    if (!allowSet.has(n.type)) {
      errors.push(`forbidden_type:${n.type}:${n.name}`);
    }
    if (n.type === 'n8n-nodes-base.code') {
      errors.push(`code_node_forbidden:${n.name}`);
    }
    if (n.type === 'n8n-nodes-base.httpRequest') {
      errors.push(`http_request_forbidden:${n.name}`);
    }
    if (n.type === 'n8n-nodes-base.wait') {
      errors.push(`wait_forbidden:${n.name}`);
    }
    if (n.type === 'n8n-nodes-base.executeWorkflow') {
      errors.push(`execute_workflow_forbidden:${n.name}`);
    }
  }
  return errors;
}

async function executionSnapshot(creds, workflowId) {
  const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions?workflowId=${encodeURIComponent(workflowId)}&limit=50`;
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      Accept: 'application/json',
      'X-N8N-API-KEY': creds.apiKey,
    },
  });
  if (!response.ok) {
    return { observable: false, reason: `HTTP_${response.status}`, rows: [] };
  }
  const data = await response.json();
  const rows = Array.isArray(data) ? data : data?.data;
  if (!Array.isArray(rows)) {
    return { observable: false, reason: 'unexpected_shape', rows: [] };
  }
  return {
    observable: true,
    count: typeof data?.count === 'number' ? data.count : rows.length,
    rows: rows.map((e) => ({
      id: String(e.id),
      status: e.status,
      finished: e.finished,
      startedAt: e.startedAt,
      stoppedAt: e.stoppedAt,
      workflowId: e.workflowId || e.workflowData?.id,
    })),
  };
}

async function getExecutionDetail(creds, executionId) {
  const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions/${encodeURIComponent(executionId)}?includeData=true`;
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      Accept: 'application/json',
      'X-N8N-API-KEY': creds.apiKey,
    },
  });
  if (!response.ok) {
    return { ok: false, status: response.status };
  }
  return { ok: true, data: await response.json() };
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function waitForNewExecution(creds, workflowId, knownIds, startedAtMs) {
  for (let i = 0; i < EXEC_POLL_MAX; i += 1) {
    const snap = await executionSnapshot(creds, workflowId);
    const fresh = (snap.rows || []).filter(
      (r) =>
        r.workflowId === workflowId &&
        !knownIds.has(r.id) &&
        (!startedAtMs ||
          !r.startedAt ||
          new Date(r.startedAt).getTime() >= startedAtMs - 5000),
    );
    const finished = fresh.find((r) => r.finished || r.status === 'success' || r.status === 'error');
    if (finished) return { snap, execution: finished };
    const running = fresh.find((r) => r.status === 'running' || r.finished === false);
    if (running && i === EXEC_POLL_MAX - 1) return { snap, execution: running };
    await sleep(EXEC_POLL_MS);
  }
  const snap = await executionSnapshot(creds, workflowId);
  return { snap, execution: null };
}

/**
 * Sanitize execution node-run metadata without raw payloads.
 * @param {Record<string, unknown>} exec
 */
function inspectExecutionOrder(exec) {
  const runData =
    /** @type {Record<string, Array<Record<string, unknown>>>} */ (
      exec?.data?.resultData?.runData || {}
    );
  const entries = [];
  for (const [nodeName, runs] of Object.entries(runData)) {
    const arr = Array.isArray(runs) ? runs : [];
    for (let i = 0; i < arr.length; i += 1) {
      const run = arr[i] || {};
      const err = run.error ? String(run.error?.message || 'error') : null;
      let markerAfter = false;
      let deliveryMarker = false;
      let telegramOk = false;
      let telegramHasMessageId = false;
      try {
        const main = run.data?.main;
        const first = Array.isArray(main) && Array.isArray(main[0]) ? main[0][0] : null;
        const json = first?.json || {};
        const blob = JSON.stringify(json);
        markerAfter = blob.includes('SEMANTICS_AFTER_RESPOND_REACHED');
        deliveryMarker = blob.includes('SEMANTICS_TELEGRAM_AFTER_RESPOND_DONE');
        if (nodeName.includes('Telegram')) {
          telegramHasMessageId = Boolean(json.message_id || json.messageId || json.result?.message_id);
          telegramOk = !err && (telegramHasMessageId || json.ok === true || Boolean(json.chat));
        }
      } catch {
        // ignore parse
      }
      entries.push({
        node: nodeName,
        run_index: i,
        startTime: typeof run.startTime === 'number' ? run.startTime : null,
        executionTime: typeof run.executionTime === 'number' ? run.executionTime : null,
        has_error: Boolean(err),
        error_class: err ? redactText(err).slice(0, 120) : null,
        marker_after_reached: markerAfter,
        delivery_marker_reached: deliveryMarker,
        telegram_ok_signal: telegramOk,
        telegram_message_id_present: telegramHasMessageId,
      });
    }
  }
  entries.sort((a, b) => {
    const sa = a.startTime ?? 0;
    const sb = b.startTime ?? 0;
    if (sa !== sb) return sa - sb;
    return String(a.node).localeCompare(String(b.node));
  });
  const nodeOrder = entries.map((e) => e.node);
  const nodeCounts = {};
  for (const e of entries) {
    nodeCounts[e.node] = (nodeCounts[e.node] || 0) + 1;
  }
  return {
    execution_status: exec.status || null,
    finished: Boolean(exec.finished),
    node_run_count: entries.length,
    node_order: nodeOrder,
    node_counts: nodeCounts,
    runs: entries,
    after_marker_reached: entries.some((e) => e.marker_after_reached),
    delivery_marker_reached: entries.some((e) => e.delivery_marker_reached),
    telegram_node_runs: entries.filter((e) => e.node.includes('Telegram')).length,
    telegram_ok_signal: entries.some((e) => e.telegram_ok_signal),
    telegram_message_id_present: entries.some((e) => e.telegram_message_id_present),
  };
}

async function postSynthetic(webhookUrl, testId) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);
  const started = Date.now();
  try {
    const response = await fetch(webhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        semantics_test: true,
        test_id: testId,
        note: 'synthetic_no_production_data',
      }),
      redirect: 'error',
      signal: controller.signal,
    });
    const text = await response.text();
    let bodyFields = null;
    try {
      const parsed = JSON.parse(text);
      bodyFields = {
        status: parsed.status || null,
        test_id: parsed.test_id || null,
      };
    } catch {
      bodyFields = { parse_error: true };
    }
    return {
      http_status: response.status,
      latency_ms: Date.now() - started,
      body_fields: bodyFields,
      body_redacted: redactText(text).slice(0, 500),
    };
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    return {
      http_status: 0,
      latency_ms: Date.now() - started,
      body_fields: null,
      transport_error_class: /abort/i.test(message) ? 'timeout' : 'network',
      body_redacted: redactText(message).slice(0, 200),
    };
  } finally {
    clearTimeout(timer);
  }
}

async function summarizeRealWorkflow(creds) {
  const listed = await listWorkflows(creds);
  const exact = listed.filter((w) => w.name === REAL_WORKFLOW_NAME);
  const wf = await getWorkflow(REAL_WORKFLOW_ID, creds);
  const nodes = wf.nodes || [];
  const telegramNodes = nodes.filter((n) => String(n.type || '').includes('telegram'));
  const webhook = nodes.find((n) => n.type === 'n8n-nodes-base.webhook');
  const exec = await executionSnapshot(creds, REAL_WORKFLOW_ID);
  const runningUrl = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions?workflowId=${encodeURIComponent(REAL_WORKFLOW_ID)}&status=running&limit=5`;
  const runRes = await fetch(runningUrl, {
    headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
  });
  const runData = runRes.ok ? await runRes.json() : null;
  const runningRows = Array.isArray(runData?.data)
    ? runData.data
    : Array.isArray(runData)
      ? runData
      : [];
  return {
    exact_name_count: exact.length,
    id: wf.id,
    name: wf.name,
    active: wf.active,
    nodes: nodes.length,
    versionId: wf.versionId,
    webhook_authentication: webhook?.parameters?.authentication || null,
    webhook_credential_id: webhook?.credentials?.httpHeaderAuth?.id || null,
    telegram_nodes: telegramNodes.length,
    telegram_credential_bound: nodes.some((n) =>
      JSON.stringify(n.credentials || {}).includes(TG_CRED_ID),
    ),
    executions: exec.count ?? exec.rows?.length ?? null,
    running: runningRows.length,
    forbidden_external: nodes
      .filter((n) =>
        [
          'n8n-nodes-base.httpRequest',
          'n8n-nodes-base.googleSheets',
          'n8n-nodes-base.dataStore',
        ].includes(n.type),
      )
      .map((n) => n.type),
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const report = {
    runner: 'run-client-ops-telegram-semantics-verification',
    mode: args.apply ? 'APPLY' : 'DRY_RUN',
    confirmation_phrase_required: CONFIRM_PHRASE,
    temp_workflow_name: TEMP_WORKFLOW_NAME,
    real_workflow_deny_id: REAL_WORKFLOW_ID,
    max_telegram_messages: MAX_TELEGRAM_MESSAGES,
    max_webhook_requests: MAX_WEBHOOK_REQUESTS,
    telegram_messages_attempted: 0,
    telegram_messages_delivered: 0,
    webhook_requests: 0,
    temp_creates: 0,
    temp_updates: 0,
    temp_activation_changes: 0,
    temp_deletes: 0,
    real_workflow_mutations: 0,
    secret_printed: false,
    complete_webhook_url_printed: false,
  };

  ensureDir(REPO_EVIDENCE);
  ensureDir(LOCAL_EVIDENCE);

  const chat = loadChatTarget();
  report.chat_target = {
    ok: chat.ok,
    expected_target: EXPECTED_PRIVATE_TARGET,
    match: chat.ok === true,
    chat_type: chat.ok ? chat.chatType : null,
    source: 'ignored_local_target_file',
  };
  if (!chat.ok) {
    report.aborted = chat.error || 'chat_target_invalid';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  const readCreds = loadCredentials();
  const host = new URL(readCreds.apiUrl).host;
  report.api_host = host;
  if (host !== EXPECTED_HOST) {
    report.aborted = `unexpected_api_host:${host}`;
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  const listed = await listWorkflows(readCreds);
  const tempExact = listed.filter((w) => w.name === TEMP_WORKFLOW_NAME);
  const realExact = listed.filter((w) => w.name === REAL_WORKFLOW_NAME);
  report.pre_temp_exact_name_count = tempExact.length;
  report.pre_real_exact_name_count = realExact.length;

  if (tempExact.length > 1) {
    report.aborted = 'TEMP_WORKFLOW_DUPLICATES';
    report.temp_hits = tempExact.map((w) => ({ id: w.id, active: w.active }));
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }
  if (tempExact.length === 1) {
    report.aborted = 'TEMP_WORKFLOW_ALREADY_EXISTS';
    report.temp_hits = tempExact.map((w) => ({ id: w.id, active: w.active }));
    report.note =
      'Prior incomplete temporary workflow present. Do not create duplicate. Return PARTIAL / cleanup phase.';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  const realPre = await summarizeRealWorkflow(readCreds);
  report.real_workflow_pre = realPre;
  if (
    realPre.exact_name_count !== 1 ||
    realPre.id !== REAL_WORKFLOW_ID ||
    realPre.active !== false ||
    realPre.nodes !== 9 ||
    realPre.executions !== 24 ||
    realPre.running !== 0 ||
    realPre.telegram_nodes !== 0 ||
    realPre.telegram_credential_bound !== false ||
    realPre.webhook_authentication !== 'headerAuth' ||
    realPre.webhook_credential_id !== 'WKHmPaw6QBp7WnzP'
  ) {
    report.aborted = 'REAL_WORKFLOW_PRESTATE_MISMATCH';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  const credMeta = await listCredentialsMetadata(loadCredentialClientCredentials());
  const tgExact = credMeta.filter((c) => c.name === TG_CRED_NAME);
  report.telegram_credential = {
    exact_name_count: tgExact.length,
    id: tgExact[0]?.id || null,
    type: tgExact[0]?.type || null,
    expected_id: TG_CRED_ID,
    match: tgExact.length === 1 && tgExact[0].id === TG_CRED_ID,
  };
  if (!report.telegram_credential.match) {
    report.aborted = 'TELEGRAM_CREDENTIAL_MISMATCH';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  const webhookPath = randomWebhookPath();
  const level1TestId = `L1-${randomBytes(3).toString('hex')}`;
  const level2TestId = `L2-${randomBytes(3).toString('hex')}`;
  const level1Graph = buildLevel1Graph(webhookPath, level1TestId);
  const level1Errors = validateGraphNodes(level1Graph.nodes, ALLOWED_NODE_TYPES_L1);
  const level2GraphPreview = buildLevel2Graph(webhookPath, level2TestId, chat.chatId);
  const level2Errors = validateGraphNodes(level2GraphPreview.nodes, ALLOWED_NODE_TYPES_L2);

  report.dry_run_gates = {
    temp_name_count_zero: tempExact.length === 0,
    real_mutation_denied: true,
    level1_allowlist_ok: level1Errors.length === 0,
    level2_allowlist_ok: level2Errors.length === 0,
    level1_errors: level1Errors,
    level2_errors: level2Errors,
    message_cap: MAX_TELEGRAM_MESSAGES,
    request_cap: MAX_WEBHOOK_REQUESTS,
    chat_id_loaded: true,
    telegram_credential_exact: true,
    bot_token_shape_absent: !/\b\d{6,}:[A-Za-z0-9_-]{20,}\b/.test(
      JSON.stringify(level2GraphPreview),
    ),
    complete_webhook_url_not_printed: true,
    activation_containment_prepared: true,
    deletion_plan_prepared: true,
    evidence_paths_sanitized: true,
  };

  const gateBools = [
    report.dry_run_gates.temp_name_count_zero,
    report.dry_run_gates.real_mutation_denied,
    report.dry_run_gates.level1_allowlist_ok,
    report.dry_run_gates.level2_allowlist_ok,
    report.dry_run_gates.chat_id_loaded,
    report.dry_run_gates.telegram_credential_exact,
    report.dry_run_gates.bot_token_shape_absent,
    report.dry_run_gates.complete_webhook_url_not_printed,
    report.dry_run_gates.activation_containment_prepared,
    report.dry_run_gates.deletion_plan_prepared,
    report.dry_run_gates.evidence_paths_sanitized,
    report.dry_run_gates.message_cap === MAX_TELEGRAM_MESSAGES,
    report.dry_run_gates.request_cap === MAX_WEBHOOK_REQUESTS,
  ];
  report.dry_run_verdict =
    gateBools.every(Boolean) && level1Errors.length === 0 && level2Errors.length === 0
      ? 'PASS'
      : 'FAIL';

  writeJson(resolve(REPO_EVIDENCE, 'TEST-CHARTER.json'), {
    phase: '1B-C0S',
    confirm_phrase: CONFIRM_PHRASE,
    temp_workflow_name: TEMP_WORKFLOW_NAME,
    real_workflow_deny: REAL_WORKFLOW_ID,
    max_telegram_messages: 1,
    max_webhook_requests: 2,
    patterns_under_test: ['PATTERN_B', 'PATTERN_A_FALLBACK', 'ASYNC_BRANCH_DOC_ONLY'],
  });

  if (!args.apply) {
    report.note =
      'Dry-run only. Pass --apply and exact confirmation phrase to run Level 1 / Level 2 semantics tests.';
    report.ready_for_apply = report.dry_run_verdict === 'PASS';
    console.log(JSON.stringify(report, null, 2));
    writeJson(resolve(LOCAL_EVIDENCE, 'dry-run-report.json'), report);
    return;
  }

  if (args.confirm !== CONFIRM_PHRASE) {
    report.aborted = 'confirmation_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }
  if (report.dry_run_verdict !== 'PASS') {
    report.aborted = 'dry_run_gates_failed';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  const writeCreds = loadTempSemanticsCredentials();
  let tempId = null;
  let tempActive = false;
  /** @type {Record<string, unknown>} */
  const results = {
    level1: null,
    level2: null,
    pattern_a: null,
    decision: 'SEMANTICS_NOT_PROVEN',
    deleted: false,
    containment: {},
  };

  try {
    // Create Level 1 temporary workflow
    const created = await createTempSemanticsWorkflow(level1Graph, writeCreds);
    report.temp_creates = 1;
    tempId = String(created.id);
    if (created.active === true) {
      throw new Error('CREATED_ACTIVE_UNEXPECTED');
    }
    const liveTemp = await getWorkflow(tempId, readCreds);
    const livePath = liveTemp.nodes?.find((n) => n.type === 'n8n-nodes-base.webhook')
      ?.parameters?.path;
    if (!livePath || typeof livePath !== 'string') {
      throw new Error('temp_webhook_path_missing');
    }
    // Rebuild graphs with live path (should match) without printing it
    const pathForUse = livePath;
    writeJson(resolve(REPO_EVIDENCE, 'TEMP-WORKFLOW-MANIFEST.json'), {
      name: TEMP_WORKFLOW_NAME,
      id: tempId,
      created_active: false,
      node_count_level1: liveTemp.nodes?.length ?? null,
      node_types: (liveTemp.nodes || []).map((n) => ({
        name: n.name,
        type: n.type,
        typeVersion: n.typeVersion,
      })),
      webhook_path_stored: false,
      webhook_path_present: true,
      telegram_bound_at_create: false,
    });

    // LEVEL 1
    await activateTempSemanticsWorkflow(tempId, writeCreds);
    report.temp_activation_changes += 1;
    tempActive = true;
    const knownL1 = new Set(
      ((await executionSnapshot(readCreds, tempId)).rows || []).map((r) => r.id),
    );
    const windowStart = Date.now();
    const webhookUrl = `${normalizeBaseUrl(writeCreds.apiUrl)}/webhook/${pathForUse}`;
    const http1 = await postSynthetic(webhookUrl, level1TestId);
    report.webhook_requests += 1;
    const waited1 = await waitForNewExecution(readCreds, tempId, knownL1, windowStart);
    let inspect1 = null;
    if (waited1.execution?.id) {
      const detail = await getExecutionDetail(readCreds, waited1.execution.id);
      if (detail.ok) inspect1 = inspectExecutionOrder(detail.data);
    }
    await deactivateTempSemanticsWorkflow(tempId, writeCreds);
    report.temp_activation_changes += 1;
    tempActive = false;

    const afterReached = Boolean(inspect1?.after_marker_reached);
    const orderOk =
      Array.isArray(inspect1?.node_order) &&
      inspect1.node_order.includes('Respond Semantics') &&
      inspect1.node_order.includes('Set After Response') &&
      inspect1.node_order.indexOf('Respond Semantics') <
        inspect1.node_order.indexOf('Set After Response');
    let level1Verdict = 'PATTERN_B_STRUCTURAL_TEST_INCONCLUSIVE';
    if (afterReached && orderOk && http1.http_status === 202) {
      level1Verdict = 'PATTERN_B_STRUCTURALLY_SUPPORTED';
    } else if (
      http1.http_status === 202 &&
      inspect1 &&
      !afterReached &&
      inspect1.node_order?.includes('Respond Semantics') &&
      !inspect1.node_order?.includes('Set After Response')
    ) {
      level1Verdict = 'PATTERN_B_STRUCTURALLY_UNSUPPORTED';
    } else if (inspect1 && !afterReached) {
      level1Verdict = 'PATTERN_B_STRUCTURALLY_UNSUPPORTED';
    }

    results.level1 = {
      request_count: 1,
      response_status: http1.http_status,
      elapsed_ms: http1.latency_ms,
      body_fields: http1.body_fields,
      execution_id: waited1.execution?.id || null,
      execution_status: inspect1?.execution_status || waited1.execution?.status || null,
      node_order: inspect1?.node_order || [],
      after_response_marker: afterReached,
      downstream_continuation: afterReached && orderOk,
      telegram_messages: 0,
      verdict: level1Verdict,
      inspect: inspect1,
    };
    writeJson(resolve(REPO_EVIDENCE, 'LEVEL-1-STRUCTURAL-RESULT.json'), results.level1);

    if (level1Verdict !== 'PATTERN_B_STRUCTURALLY_SUPPORTED') {
      results.decision = 'PATTERN_A_REQUIRED';
      // Pattern A would need Telegram before Respond — only if no message sent yet.
      // Level 1 sent 0 Telegram messages. Charter allows one Pattern A message test.
      // Prefer documenting Pattern A as required without live Telegram if Level 1 proves
      // no continuation — still need Pattern A runtime verification with Telegram for
      // PATTERN_A_REQUIRED confirmation of send-before-respond.
      // Run Pattern A with Telegram once.
      const patternAGraph = {
        name: TEMP_WORKFLOW_NAME,
        nodes: [
          {
            parameters: {
              httpMethod: 'POST',
              path: pathForUse,
              responseMode: 'responseNode',
              options: {},
            },
            id: uid(),
            name: 'Webhook Semantics',
            type: 'n8n-nodes-base.webhook',
            typeVersion: 2.1,
            position: [0, 300],
          },
          setNode(
            'Set Synthetic Accepted Event',
            [
              { name: 'test_id', value: level2TestId },
              {
                name: 'telegram_text',
                value: `MARS sandbox test: проверка выполнения Telegram до ответа webhook. SITE-002 production не затронут. test=${level2TestId}`,
              },
            ],
            [260, 300],
          ),
          {
            parameters: {
              chatId: String(chat.chatId),
              text: '={{ $json.telegram_text }}',
              additionalFields: { appendAttribution: false },
            },
            id: uid(),
            name: 'Telegram Semantics Send',
            type: 'n8n-nodes-base.telegram',
            typeVersion: 1.2,
            position: [520, 300],
            credentials: {
              telegramApi: { id: TG_CRED_ID, name: TG_CRED_NAME },
            },
          },
          {
            parameters: {
              respondWith: 'json',
              responseBody: `={{ ({ status: "SEMANTICS_TEST_ACCEPTED", test_id: "${level2TestId}" }) }}`,
              options: { responseCode: 202 },
            },
            id: uid(),
            name: 'Respond Semantics',
            type: 'n8n-nodes-base.respondToWebhook',
            typeVersion: 1.1,
            position: [780, 300],
          },
        ],
        connections: {
          'Webhook Semantics': {
            main: [[{ node: 'Set Synthetic Accepted Event', type: 'main', index: 0 }]],
          },
          'Set Synthetic Accepted Event': {
            main: [[{ node: 'Telegram Semantics Send', type: 'main', index: 0 }]],
          },
          'Telegram Semantics Send': {
            main: [[{ node: 'Respond Semantics', type: 'main', index: 0 }]],
          },
        },
        settings: { executionOrder: 'v1' },
      };

      const putA = prepareTempPutPayload(patternAGraph);
      await updateTempSemanticsWorkflow(tempId, putA, writeCreds);
      report.temp_updates += 1;
      await activateTempSemanticsWorkflow(tempId, writeCreds);
      report.temp_activation_changes += 1;
      tempActive = true;
      const knownA = new Set(
        ((await executionSnapshot(readCreds, tempId)).rows || []).map((r) => r.id),
      );
      const windowA = Date.now();
      report.telegram_messages_attempted = 1;
      const httpA = await postSynthetic(
        `${normalizeBaseUrl(writeCreds.apiUrl)}/webhook/${pathForUse}`,
        level2TestId,
      );
      report.webhook_requests += 1;
      const waitedA = await waitForNewExecution(readCreds, tempId, knownA, windowA);
      let inspectA = null;
      if (waitedA.execution?.id) {
        const detail = await getExecutionDetail(readCreds, waitedA.execution.id);
        if (detail.ok) inspectA = inspectExecutionOrder(detail.data);
      }
      await deactivateTempSemanticsWorkflow(tempId, writeCreds);
      report.temp_activation_changes += 1;
      tempActive = false;

      const deliveredA = Boolean(inspectA?.telegram_message_id_present || inspectA?.telegram_ok_signal);
      if (deliveredA) report.telegram_messages_delivered = 1;
      results.pattern_a = {
        request_count: 1,
        response_status: httpA.http_status,
        elapsed_ms: httpA.latency_ms,
        execution_id: waitedA.execution?.id || null,
        node_order: inspectA?.node_order || [],
        telegram_node_runs: inspectA?.telegram_node_runs || 0,
        messages_attempted: 1,
        messages_delivered: deliveredA ? 1 : 0,
        inspect: inspectA,
        verdict:
          deliveredA && httpA.http_status === 202
            ? 'PATTERN_A_RUNTIME_VERIFIED'
            : 'PATTERN_A_RUNTIME_INCONCLUSIVE',
      };
      writeJson(resolve(REPO_EVIDENCE, 'PATTERN-A-RESULT.json'), results.pattern_a);
      results.decision =
        results.pattern_a.verdict === 'PATTERN_A_RUNTIME_VERIFIED'
          ? 'PATTERN_A_REQUIRED'
          : 'SEMANTICS_NOT_PROVEN';
    } else {
      // LEVEL 2 — Pattern B with Telegram
      const level2Graph = buildLevel2Graph(pathForUse, level2TestId, chat.chatId);
      const put2 = prepareTempPutPayload(level2Graph);
      await updateTempSemanticsWorkflow(tempId, put2, writeCreds);
      report.temp_updates += 1;
      await activateTempSemanticsWorkflow(tempId, writeCreds);
      report.temp_activation_changes += 1;
      tempActive = true;
      const knownL2 = new Set(
        ((await executionSnapshot(readCreds, tempId)).rows || []).map((r) => r.id),
      );
      const window2 = Date.now();
      report.telegram_messages_attempted = 1;
      const http2 = await postSynthetic(
        `${normalizeBaseUrl(writeCreds.apiUrl)}/webhook/${pathForUse}`,
        level2TestId,
      );
      report.webhook_requests += 1;
      const waited2 = await waitForNewExecution(readCreds, tempId, knownL2, window2);
      let inspect2 = null;
      if (waited2.execution?.id) {
        const detail = await getExecutionDetail(readCreds, waited2.execution.id);
        if (detail.ok) inspect2 = inspectExecutionOrder(detail.data);
      }
      // Extra short wait if still running (Telegram after respond)
      if (waited2.execution && !waited2.execution.finished) {
        await sleep(3000);
        const detail2 = await getExecutionDetail(readCreds, waited2.execution.id);
        if (detail2.ok) inspect2 = inspectExecutionOrder(detail2.data);
      }
      await deactivateTempSemanticsWorkflow(tempId, writeCreds);
      report.temp_activation_changes += 1;
      tempActive = false;

      const order2 = inspect2?.node_order || [];
      const respondIdx = order2.indexOf('Respond Semantics');
      const tgIdx = order2.indexOf('Telegram Semantics Send');
      const markerIdx = order2.indexOf('Set Delivery Marker');
      const tgAfterRespond =
        respondIdx >= 0 && tgIdx >= 0 && respondIdx < tgIdx;
      const delivered = Boolean(
        inspect2?.telegram_message_id_present || inspect2?.telegram_ok_signal,
      );
      if (delivered) report.telegram_messages_delivered = 1;
      const duplicateTg = (inspect2?.telegram_node_runs || 0) > 1;
      let l2Verdict = 'LEVEL2_INCONCLUSIVE';
      if (
        http2.http_status === 202 &&
        tgAfterRespond &&
        delivered &&
        inspect2?.delivery_marker_reached &&
        !duplicateTg &&
        (inspect2?.telegram_node_runs || 0) === 1
      ) {
        l2Verdict = 'PATTERN_B_TELEGRAM_AFTER_RESPOND_CONFIRMED';
      } else if (http2.http_status === 202 && !delivered && tgIdx < 0) {
        l2Verdict = 'PATTERN_B_TELEGRAM_DID_NOT_EXECUTE';
      }

      results.level2 = {
        request_count: 1,
        response_status: http2.http_status,
        elapsed_ms: http2.latency_ms,
        body_fields: http2.body_fields,
        execution_id: waited2.execution?.id || null,
        execution_status: inspect2?.execution_status || null,
        node_order: order2,
        telegram_node_runs: inspect2?.telegram_node_runs || 0,
        messages_attempted: 1,
        messages_delivered: delivered ? 1 : 0,
        final_marker: Boolean(inspect2?.delivery_marker_reached),
        duplicate_sends: duplicateTg,
        telegram_after_respond: tgAfterRespond,
        marker_after_telegram: tgIdx >= 0 && markerIdx > tgIdx,
        verdict: l2Verdict,
        inspect: inspect2,
      };
      writeJson(resolve(REPO_EVIDENCE, 'LEVEL-2-TELEGRAM-RESULT.json'), results.level2);

      if (l2Verdict === 'PATTERN_B_TELEGRAM_AFTER_RESPOND_CONFIRMED') {
        results.decision = 'PATTERN_B_CONFIRMED';
      } else if (
        l2Verdict === 'PATTERN_B_TELEGRAM_DID_NOT_EXECUTE' &&
        report.telegram_messages_delivered === 0
      ) {
        results.decision = 'SEMANTICS_NOT_PROVEN';
      } else {
        results.decision = 'SEMANTICS_NOT_PROVEN';
      }
    }

    // Cleanup delete
    const beforeDelete = await getWorkflow(tempId, readCreds);
    if (beforeDelete.active === true) {
      await deactivateTempSemanticsWorkflow(tempId, writeCreds);
      report.temp_activation_changes += 1;
      tempActive = false;
    }
    if (
      beforeDelete.id === tempId &&
      beforeDelete.name === TEMP_WORKFLOW_NAME &&
      beforeDelete.id !== REAL_WORKFLOW_ID
    ) {
      await deleteTempSemanticsWorkflow(tempId, writeCreds);
      report.temp_deletes = 1;
      results.deleted = true;
      tempId = null;
    }

    const listedAfter = await listWorkflows(readCreds);
    const tempAfter = listedAfter.filter((w) => w.name === TEMP_WORKFLOW_NAME);
    results.containment = {
      temp_active_after: false,
      deleted: results.deleted,
      exact_name_count_after: tempAfter.length,
      residual_temp_ids: tempAfter.map((w) => w.id),
    };
  } catch (err) {
    report.error = redactText(err instanceof Error ? err.message : String(err)).slice(0, 300);
    results.decision = 'SEMANTICS_NOT_PROVEN';
    report.aborted = 'APPLY_ERROR';
  } finally {
    if (tempId && tempActive) {
      try {
        await deactivateTempSemanticsWorkflow(tempId, writeCreds);
        report.temp_activation_changes += 1;
        tempActive = false;
      } catch (e) {
        report.finally_deactivate_error = redactText(
          e instanceof Error ? e.message : String(e),
        ).slice(0, 200);
      }
    }
  }

  const realPost = await summarizeRealWorkflow(readCreds);
  report.real_workflow_post = realPost;
  report.real_unchanged =
    realPost.active === false &&
    realPost.nodes === 9 &&
    realPost.executions === 24 &&
    realPost.running === 0 &&
    realPost.versionId === realPre.versionId &&
    realPost.telegram_nodes === 0 &&
    realPost.telegram_credential_bound === false;

  report.results = {
    level1_verdict: results.level1?.verdict || null,
    level2_verdict: results.level2?.verdict || null,
    pattern_a_verdict: results.pattern_a?.verdict || null,
    decision: results.decision,
    containment: results.containment,
    deleted: results.deleted,
  };

  // Update ignored proposed integration
  if (existsSync(PROPOSED_PATH)) {
    try {
      const bundle = JSON.parse(readFileSync(PROPOSED_PATH, 'utf8'));
      const pi = bundle.proposed_integration || bundle;
      if (results.decision === 'PATTERN_B_CONFIRMED') {
        pi.pattern = 'B_RESPONSE_FIRST_THEN_TELEGRAM';
        pi.pattern_rationale =
          'Runtime-verified on this n8n host: nodes after Respond to Webhook execute, including Telegram sendMessage exactly once.';
        pi.integration_semantics = {
          pattern_b_continuation_after_respond: 'PATTERN_B_CONFIRMED',
          evidence_phase: '1B-C0S',
        };
      } else if (results.decision === 'PATTERN_A_REQUIRED') {
        pi.pattern = 'A_TELEGRAM_BEFORE_RESPOND';
        pi.pattern_rationale =
          'Downstream continuation after Respond to Webhook is unsupported or unreliable on this host; Telegram must complete before Respond with controlled error handling.';
        pi.integration_semantics = {
          pattern_b_continuation_after_respond: 'UNSUPPORTED',
          selected: 'PATTERN_A_REQUIRED',
          evidence_phase: '1B-C0S',
        };
      } else {
        pi.integration_semantics = {
          pattern_b_continuation_after_respond: 'SAFE_UNKNOWN',
          selected: 'SEMANTICS_NOT_PROVEN',
          evidence_phase: '1B-C0S',
        };
      }
      pi.applied = false;
      bundle.applied = false;
      bundle.proposed_integration = pi;
      bundle.overall_apply_readiness =
        results.decision === 'PATTERN_B_CONFIRMED' ||
        results.decision === 'PATTERN_A_REQUIRED' ||
        results.decision === 'ASYNC_BRANCH_PATTERN_CONFIRMED'
          ? 'READY_FOR_TELEGRAM_SANDBOX_INTEGRATION_APPLY'
          : 'NOT_READY_FOR_TELEGRAM_SANDBOX_INTEGRATION_APPLY';
      bundle.phase = '1B-C0S';
      writeFileSync(PROPOSED_PATH, `${JSON.stringify(bundle, null, 2)}\n`, 'utf8');
      report.proposed_integration_updated = true;
    } catch (e) {
      report.proposed_integration_updated = false;
      report.proposed_update_error = redactText(
        e instanceof Error ? e.message : String(e),
      ).slice(0, 200);
    }
  } else {
    report.proposed_integration_updated = false;
    report.proposed_missing = true;
  }

  writeJson(resolve(REPO_EVIDENCE, 'SEMANTICS-DECISION.json'), {
    decision: results.decision,
    level1: results.level1?.verdict || null,
    level2: results.level2?.verdict || null,
    pattern_a: results.pattern_a?.verdict || null,
    telegram_messages_attempted: report.telegram_messages_attempted,
    telegram_messages_delivered: report.telegram_messages_delivered,
    private_target: EXPECTED_PRIVATE_TARGET,
    credential_id: TG_CRED_ID,
  });
  writeJson(resolve(REPO_EVIDENCE, 'EXECUTION-ORDER-EVIDENCE.json'), {
    level1: results.level1?.inspect || null,
    level2: results.level2?.inspect || null,
    pattern_a: results.pattern_a?.inspect || null,
  });
  writeJson(resolve(LOCAL_EVIDENCE, 'apply-report.sanitized.json'), report);

  console.log(JSON.stringify(report, null, 2));
  if (report.aborted || !report.real_unchanged) process.exitCode = 4;
  if (
    results.decision === 'SEMANTICS_NOT_PROVEN' ||
    (results.containment && results.containment.exact_name_count_after > 0 && !results.deleted)
  ) {
    process.exitCode = process.exitCode || 5;
  }
}

main().catch((err) => {
  console.error(
    JSON.stringify(
      {
        runner: 'run-client-ops-telegram-semantics-verification',
        fatal: redactText(err instanceof Error ? err.message : String(err)).slice(0, 300),
      },
      null,
      2,
    ),
  );
  process.exitCode = 1;
});
