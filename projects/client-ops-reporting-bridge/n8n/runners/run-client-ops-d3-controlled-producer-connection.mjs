/**
 * Phase 1B-D3 — Controlled sequential producer connection orchestrator.
 *
 * Default: dry-run / preflight only (GET-only n8n + Python dry-run).
 * Live requires --apply and exact confirmation phrases.
 *
 * FORBIDDEN: workflow PUT/graph update, Telegram API, Data Table admin mutate,
 * fetch POST to webhook, secret/full-URL printing, scheduler, retries.
 *
 * Max 2 real producer HTTP requests via Python only.
 * Activation/deactivation only; deactivate in finally.
 *
 * No network on module import.
 */

import { spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import {
  getWorkflow,
  listWorkflows,
  loadCredentials,
  normalizeBaseUrl,
} from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';
import {
  activateAllowlistedWorkflow,
  deactivateAllowlistedWorkflow,
  loadActivationCredentials,
  ALLOWED_WORKFLOW_ID,
  ALLOWED_WORKFLOW_NAME,
  EXPECTED_HOST,
  D3_ACTIVATION_CONFIRM_PHRASE,
  D3_DEACTIVATION_CONFIRM_PHRASE,
  D3_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE,
} from './lib/client-ops-n8n-activation-client.mjs';
import {
  ALLOWED_TABLE_NAME,
  countTablesByExactName,
  getDataTable,
  getDataTableRows,
  loadDataTableCredentials,
} from './lib/client-ops-n8n-datatable-client.mjs';
import {
  AUTH_CRED_ID,
  AUTH_CRED_NAME,
  TELEGRAM_NODE_NAME,
  TG_CRED_ID,
  TG_CRED_NAME,
  DEDUPE_NODE_NAMES,
  BASE_NODE_NAMES,
} from './lib/client-ops-dedupe-compose.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const PROJECT = resolve(REPO_ROOT, 'projects/client-ops-reporting-bridge');

const WORKFLOW_ID = 'tkM4H0G0gM3q9Foi';
const EXPECTED_VERSION = '3d2fd6fc-bc17-4e0f-b9e5-086c959afd29';
const EXPECTED_NODES = 17;
const EXPECTED_EXEC_PRE = 29;
const TABLE_ID = 'H6VYhwz7RXZCBMmu';
const TABLE_ROWS_PRE = 1;
const CHAT_ID = '499423375';

const ENABLE_PHRASE = 'ENABLE CLIENT OPS CONTROLLED PRODUCER HTTP D3 BZPM';
const ACTIVATE_PHRASE = 'ACTIVATE CLIENT OPS CONTROLLED PRODUCER TEST D3 BZPM';
const SEND_FIRST = 'SEND ONE CLIENT OPS PRODUCER FIRST SEEN D3 BZPM';
const SEND_REPLAY = 'SEND ONE CLIENT OPS PRODUCER EXACT REPLAY D3 BZPM';
const DEACTIVATE_PHRASE = 'DEACTIVATE CLIENT OPS CONTROLLED PRODUCER TEST D3 BZPM';
const EMERGENCY = 'EMERGENCY DEACTIVATE CLIENT OPS PRODUCER D3 BZPM';

const PRODUCER_MARKER = 'mars-client-ops-producer-live-d3';
const FIXTURE_REL = 'projects/client-ops-reporting-bridge/fixtures/fixture-d3-synthetic-producer';
const FIXTURE = resolve(REPO_ROOT, FIXTURE_REL);
const REPO_EVIDENCE = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/evidence/phase-1b-d3-controlled-producer-connection',
);
const LOCAL_EVIDENCE = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/runs/d3-controlled-live',
);

const EXEC_POLL_MS = 1500;
const EXEC_POLL_MAX = 40;
const PYTHON_BIN = process.env.CLIENT_OPS_PYTHON || 'python';

const CLAIM_INSERT_NAME = 'Dedupe Claim Insert';
const RESPOND_ACCEPTED_NAME = 'Respond Accepted';

function ensureDir(p) {
  mkdirSync(p, { recursive: true });
}

function writeJson(path, obj) {
  ensureDir(dirname(path));
  writeFileSync(path, `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

function parseArgs(argv) {
  const args = {
    apply: false,
    skipReplay: false,
    confirmEnable: null,
    confirmActivate: null,
    confirmSendFirst: null,
    confirmSendReplay: null,
    confirmDeactivate: null,
  };
  for (const a of argv) {
    if (a === '--apply') args.apply = true;
    else if (a === '--skip-replay') args.skipReplay = true;
    else if (a.startsWith('--confirm-enable=')) {
      args.confirmEnable = a.slice('--confirm-enable='.length);
    } else if (a.startsWith('--confirm-activate=')) {
      args.confirmActivate = a.slice('--confirm-activate='.length);
    } else if (a.startsWith('--confirm-send-first=')) {
      args.confirmSendFirst = a.slice('--confirm-send-first='.length);
    } else if (a.startsWith('--confirm-send-replay=')) {
      args.confirmSendReplay = a.slice('--confirm-send-replay='.length);
    } else if (a.startsWith('--confirm-deactivate=')) {
      args.confirmDeactivate = a.slice('--confirm-deactivate='.length);
    }
  }
  return args;
}

function hasScheduleNode(nodes) {
  return (nodes || []).some((n) => {
    const type = String(n?.type || '');
    const name = String(n?.name || '');
    return type.includes('n8n-nodes-base.schedule') || /schedule/i.test(name);
  });
}

function extractJsonPayload(stdout) {
  const text = String(stdout || '').trim();
  if (!text) return null;
  try {
    return JSON.parse(text);
  } catch {
    const lines = text.split(/\r?\n/).map((l) => l.trim()).filter(Boolean);
    for (let i = lines.length - 1; i >= 0; i -= 1) {
      try {
        return JSON.parse(lines[i]);
      } catch {
        /* continue */
      }
    }
  }
  return null;
}

function spawnPython(argvExtra) {
  const env = {
    ...process.env,
    PYTHONPATH: resolve(PROJECT, 'src'),
  };
  const result = spawnSync(PYTHON_BIN, ['-m', 'client_ops_reporting_bridge', ...argvExtra], {
    cwd: REPO_ROOT,
    env,
    encoding: 'utf8',
    windowsHide: true,
  });
  return {
    status: result.status,
    signal: result.signal,
    stdout: result.stdout || '',
    stderr: (result.stderr || '').slice(0, 800),
    error: result.error ? String(result.error.message).slice(0, 200) : null,
    json: extractJsonPayload(result.stdout),
  };
}

function spawnPythonEventId() {
  const code = [
    'from pathlib import Path',
    'from client_ops_reporting_bridge.producer_d3 import build_d3_synthetic_envelope',
    `env = build_d3_synthetic_envelope(Path(${JSON.stringify(FIXTURE)}))`,
    "print(env.get('event_id') or '')",
  ].join('; ');
  const env = {
    ...process.env,
    PYTHONPATH: resolve(PROJECT, 'src'),
  };
  const result = spawnSync(PYTHON_BIN, ['-c', code], {
    cwd: REPO_ROOT,
    env,
    encoding: 'utf8',
    windowsHide: true,
  });
  const eventId = String(result.stdout || '')
    .trim()
    .split(/\r?\n/)
    .filter(Boolean)
    .pop();
  return {
    ok: result.status === 0 && Boolean(eventId) && eventId.length >= 8,
    event_id: eventId || null,
    status: result.status,
    stderr: (result.stderr || '').slice(0, 400),
  };
}

async function executionSnapshot(creds, workflowId) {
  const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions?workflowId=${encodeURIComponent(workflowId)}&limit=100`;
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      Accept: 'application/json',
      'X-N8N-API-KEY': creds.apiKey,
    },
  });
  if (!response.ok) {
    return { observable: false, reason: `HTTP_${response.status}`, rows: [], count: null, running: null };
  }
  const data = await response.json();
  const rows = Array.isArray(data) ? data : data?.data;
  if (!Array.isArray(rows)) {
    return { observable: false, reason: 'unexpected_shape', rows: [], count: null, running: null };
  }
  const mapped = rows.map((e) => ({
    id: String(e.id),
    status: e.status,
    finished: e.finished,
    startedAt: e.startedAt,
    stoppedAt: e.stoppedAt,
    mode: e.mode,
    workflowId: e.workflowId || e.workflowData?.id,
  }));
  return {
    observable: true,
    count: typeof data?.count === 'number' ? data.count : mapped.length,
    nextCursor: data?.nextCursor || null,
    rows: mapped,
    running: mapped.filter((r) => r.status === 'running').length,
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
  let dedupeResult = null;
  let httpLikeResult = null;
  try {
    const accepted = runData[RESPOND_ACCEPTED_NAME]?.[0]?.data?.main?.[0]?.[0]?.json;
    if (accepted) {
      dedupeResult = accepted.dedupe_result || accepted.dedupe || accepted.dedupe_classification || null;
      httpLikeResult = accepted.result || accepted.code || null;
    }
  } catch {
    /* ignore */
  }
  return {
    ok: true,
    execution_id: String(detail.data?.id || ''),
    status: detail.data?.status,
    finished: detail.data?.finished,
    node_names_executed: nodeOrder,
    telegram_runs: telegramRuns,
    telegram_message_id: telegramMessageId,
    telegram_ok: telegramOk,
    dedupe_result: dedupeResult,
    response_result: httpLikeResult,
    has_claim_insert: nodeOrder.includes(CLAIM_INSERT_NAME),
    has_respond_accepted: nodeOrder.includes(RESPOND_ACCEPTED_NAME),
    has_telegram_notify: nodeOrder.includes(TELEGRAM_NODE_NAME),
    has_dedupe_lookup: nodeOrder.includes('Dedupe Lookup'),
    has_dedupe_classify: nodeOrder.includes('Dedupe Classify'),
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
      const terminal =
        newest.status === 'success' ||
        newest.status === 'error' ||
        newest.status === 'crashed' ||
        newest.status === 'canceled' ||
        newest.finished === true;
      if (!terminal || newest.status === 'running') {
        await sleep(EXEC_POLL_MS);
        continue;
      }
      return { found: true, execution: newest, snap };
    }
    await sleep(EXEC_POLL_MS);
  }
  return { found: false, execution: null, snap: await executionSnapshot(creds, workflowId) };
}

function rowListFromResponse(res) {
  const rows = res?.data?.data || res?.data || [];
  return Array.isArray(rows) ? rows : [];
}

async function countTableRows(creds, tableId, filter) {
  const query = { limit: 50 };
  if (filter) query.filter = filter;
  const res = await getDataTableRows(creds, tableId, query);
  const rows = rowListFromResponse(res);
  const count =
    typeof res?.data?.count === 'number' ? res.data.count : rows.length;
  return { count, rows, status: res.status };
}

function credentialChecks(wf) {
  const webhook = (wf.nodes || []).find((n) => n.name === 'Webhook Intake');
  const telegram = (wf.nodes || []).find((n) => n.name === TELEGRAM_NODE_NAME);
  const authId = webhook?.credentials?.httpHeaderAuth?.id || null;
  const authName = webhook?.credentials?.httpHeaderAuth?.name || null;
  const tgId = telegram?.credentials?.telegramApi?.id || null;
  const tgName = telegram?.credentials?.telegramApi?.name || null;
  const chatId = telegram?.parameters?.chatId != null ? String(telegram.parameters.chatId) : null;
  return {
    webhook_auth: {
      id: authId,
      name: authName,
      id_ok: authId === AUTH_CRED_ID,
      name_ok: !authName || authName === AUTH_CRED_NAME,
    },
    telegram: {
      id: tgId,
      name: tgName,
      chat_id: chatId,
      id_ok: tgId === TG_CRED_ID,
      name_ok: !tgName || tgName === TG_CRED_NAME,
      chat_ok: chatId === CHAT_ID,
    },
    ok:
      authId === AUTH_CRED_ID &&
      tgId === TG_CRED_ID &&
      chatId === CHAT_ID,
  };
}

function nodeInventory(wf) {
  const names = (wf.nodes || []).map((n) => n.name);
  const expected = new Set([...BASE_NODE_NAMES, ...DEDUPE_NODE_NAMES]);
  const missing = [...expected].filter((n) => !names.includes(n));
  const extra = names.filter((n) => !expected.has(n));
  return {
    count: names.length,
    missing,
    extra,
    has_all_base: missing.filter((n) => BASE_NODE_NAMES.includes(n)).length === 0,
    has_all_dedupe: missing.filter((n) => DEDUPE_NODE_NAMES.includes(n)).length === 0,
  };
}

async function capturePreState(creds) {
  if (WORKFLOW_ID !== ALLOWED_WORKFLOW_ID) {
    throw new Error('WORKFLOW_ID / ALLOWED_WORKFLOW_ID mismatch');
  }
  const host = new URL(creds.apiUrl).host;
  if (host !== EXPECTED_HOST) {
    throw new Error(`Unexpected API host: ${host}`);
  }

  const all = await listWorkflows(creds);
  const list = all.data || all || [];
  const exact = list.filter((w) => w.name === ALLOWED_WORKFLOW_NAME);
  const wf = await getWorkflow(WORKFLOW_ID, creds);
  const exec = await executionSnapshot(creds, WORKFLOW_ID);
  const tableCount = await countTablesByExactName(creds, ALLOWED_TABLE_NAME);
  const tableMeta = await getDataTable(creds, TABLE_ID);
  const tableRows = await countTableRows(creds, TABLE_ID);
  const credsMeta = credentialChecks(wf);
  const nodes = nodeInventory(wf);
  const schedule = hasScheduleNode(wf.nodes);

  const gates = {
    exact_name_count_1: exact.length === 1,
    active_false: wf.active === false,
    nodes_17: (wf.nodes || []).length === EXPECTED_NODES,
    version_exact: wf.versionId === EXPECTED_VERSION,
    no_schedule: !schedule,
    exec_count_29: exec.observable && exec.count === EXPECTED_EXEC_PRE,
    running_0: exec.observable && exec.running === 0,
    table_name_count_1: tableCount === 1,
    table_id_exact: tableMeta?.data?.id
      ? tableMeta.data.id === TABLE_ID
      : false,
    table_name_exact: tableMeta?.data?.name === ALLOWED_TABLE_NAME,
    table_rows_1: tableRows.count === TABLE_ROWS_PRE,
    credentials_ok: credsMeta.ok,
    nodes_inventory_ok: nodes.missing.length === 0 && nodes.count === EXPECTED_NODES,
  };

  const blockers = Object.entries(gates)
    .filter(([, v]) => !v)
    .map(([k]) => k);

  return {
    exact_name_count: exact.length,
    workflow: {
      id: wf.id,
      name: wf.name,
      active: wf.active,
      versionId: wf.versionId,
      node_count: (wf.nodes || []).length,
      has_schedule: schedule,
    },
    nodes,
    executions: {
      observable: exec.observable,
      count: exec.count,
      running: exec.running,
      max_id: exec.rows?.length
        ? Math.max(...exec.rows.map((r) => Number(r.id) || 0))
        : null,
      known_ids: (exec.rows || []).map((r) => r.id),
    },
    table: {
      exact_name_count: tableCount,
      id: tableMeta?.data?.id || null,
      name: tableMeta?.data?.name || null,
      row_count: tableRows.count,
    },
    credentials: credsMeta,
    gates,
    blockers,
    ready_n8n: blockers.length === 0,
  };
}

function writeContainmentMd(path, payload) {
  ensureDir(dirname(path));
  const body = [
    '# Containment Status — D3 Controlled Producer',
    '',
    '```json',
    JSON.stringify(payload, null, 2),
    '```',
    '',
  ].join('\n');
  writeFileSync(path, body, 'utf8');
}

async function runDry(creds) {
  ensureDir(REPO_EVIDENCE);
  ensureDir(LOCAL_EVIDENCE);

  const pre = await capturePreState(creds);
  const py = spawnPython([
    'producer-d3-controlled-live',
    '--dry-run',
    '--mode',
    'first_seen',
  ]);
  const pyReady =
    py.status === 0 &&
    py.json &&
    (py.json.ok === true || py.json.final_state === 'D3_DRY_RUN_READY') &&
    (py.json.network_calls === 0 || py.json.real_network === false);

  const ready = pre.ready_n8n && pyReady;
  const readiness = ready
    ? 'READY_FOR_ONE_CONTROLLED_SYNTHETIC_PRODUCER_POST'
    : 'NOT_READY_FOR_CONTROLLED_SYNTHETIC_PRODUCER_POST';

  const manifest = {
    phase: '1B-D3',
    mode: 'dry-run',
    generated_at: new Date().toISOString(),
    workflow_id: WORKFLOW_ID,
    expected_version: EXPECTED_VERSION,
    expected_nodes: EXPECTED_NODES,
    expected_exec_pre: EXPECTED_EXEC_PRE,
    table_id: TABLE_ID,
    table_rows_pre: TABLE_ROWS_PRE,
    producer_marker: PRODUCER_MARKER,
    fixture_rel: FIXTURE_REL,
    fixture_exists: existsSync(FIXTURE),
    preflight: {
      exact_name_count: pre.exact_name_count,
      active: pre.workflow.active,
      versionId: pre.workflow.versionId,
      node_count: pre.workflow.node_count,
      has_schedule: pre.workflow.has_schedule,
      executions: pre.executions.count,
      running: pre.executions.running,
      table_exact_name_count: pre.table.exact_name_count,
      table_id: pre.table.id,
      table_rows: pre.table.row_count,
      credentials_ok: pre.credentials.ok,
      credential_ids_only: {
        auth: pre.credentials.webhook_auth.id,
        telegram: pre.credentials.telegram.id,
        chat_id: pre.credentials.telegram.chat_id,
      },
      blockers: pre.blockers,
    },
    python_dry_run: {
      status: py.status,
      ok: pyReady,
      final_state: py.json?.final_state || null,
      network_calls: py.json?.network_calls ?? null,
      profile_present: py.json?.profile_present ?? null,
      secret_present: py.json?.secret_present ?? null,
      error: py.error,
    },
    readiness,
    secrets_printed: false,
    webhook_url_printed: false,
    graph_put: false,
    telegram_api_called: false,
    datatable_admin_mutate: false,
  };

  writeJson(resolve(REPO_EVIDENCE, 'PRE-LIVE-MANIFEST.json'), manifest);
  writeJson(resolve(LOCAL_EVIDENCE, 'pre-live-manifest.json'), {
    readiness,
    blockers: pre.blockers,
    python_status: py.status,
  });

  console.log(readiness);
  console.log(
    JSON.stringify(
      {
        mode: 'dry-run',
        readiness,
        blockers: pre.blockers,
        python_dry_run_ok: pyReady,
        network_calls: 0,
      },
      null,
      2,
    ),
  );
  return ready ? 0 : 2;
}

async function runApply(args, creds) {
  const phraseOk =
    args.confirmEnable === ENABLE_PHRASE &&
    args.confirmActivate === ACTIVATE_PHRASE &&
    args.confirmSendFirst === SEND_FIRST &&
    args.confirmDeactivate === DEACTIVATE_PHRASE &&
    args.confirmActivate === D3_ACTIVATION_CONFIRM_PHRASE &&
    args.confirmDeactivate === D3_DEACTIVATION_CONFIRM_PHRASE;

  if (!phraseOk) {
    console.error(
      JSON.stringify({
        ok: false,
        error: 'APPLY_CONFIRMATION_PHRASE_MISMATCH',
        hint: 'require exact enable/activate/send-first/deactivate phrases',
      }),
    );
    return 2;
  }

  ensureDir(REPO_EVIDENCE);
  ensureDir(LOCAL_EVIDENCE);

  const report = {
    phase: '1B-D3',
    mode: 'apply',
    started_at: new Date().toISOString(),
    mutations: {
      activation_changes: 0,
      producer_http_requests: 0,
      webhook_calls: 0,
      executions_added: 0,
      table_rows_created_through_workflow: 0,
      telegram_attempted: 0,
      telegram_delivered: 0,
    },
    first_seen: null,
    replay: null,
    replay_skipped: null,
    containment: null,
    error: null,
    readiness: null,
    verdict: null,
  };

  const actCreds = loadActivationCredentials();
  let activated = false;
  let eventId = null;

  try {
    const pre = await capturePreState(creds);
    writeJson(resolve(REPO_EVIDENCE, 'PRE-LIVE-MANIFEST.json'), {
      phase: '1B-D3',
      mode: 'apply-reconfirm',
      generated_at: new Date().toISOString(),
      preflight: pre,
      readiness: pre.ready_n8n
        ? 'READY_FOR_ONE_CONTROLLED_SYNTHETIC_PRODUCER_POST'
        : 'NOT_READY_FOR_CONTROLLED_SYNTHETIC_PRODUCER_POST',
    });
    if (!pre.ready_n8n) {
      throw new Error(`PRE_STATE_MISMATCH: ${pre.blockers.join(',')}`);
    }

    const built = spawnPythonEventId();
    if (!built.ok) {
      throw new Error(`EVENT_ID_BUILD_FAILED: status=${built.status}`);
    }
    eventId = built.event_id;
    writeJson(resolve(LOCAL_EVIDENCE, 'synthetic-event-id.json'), {
      event_id: eventId,
      producer_marker: PRODUCER_MARKER,
    });

    const beforeRows = await countTableRows(creds, TABLE_ID, {
      type: 'and',
      filters: [{ columnName: 'event_id', condition: 'eq', value: eventId }],
    });
    if (beforeRows.count !== 0) {
      throw new Error('EVENT_ID_ALREADY_IN_DATATABLE');
    }

    const priorIds = new Set(pre.executions.known_ids || []);
    const windowStart = new Date().toISOString();

    await activateAllowlistedWorkflow(actCreds, ACTIVATE_PHRASE);
    report.mutations.activation_changes += 1;
    activated = true;

    const wfActive = await getWorkflow(WORKFLOW_ID, creds);
    if (wfActive.active !== true) {
      throw new Error('ACTIVATION_GET_CONFIRM_FAILED');
    }

    const execAfterAct = await executionSnapshot(creds, WORKFLOW_ID);
    if (
      !execAfterAct.observable ||
      execAfterAct.count !== EXPECTED_EXEC_PRE ||
      execAfterAct.running !== 0
    ) {
      throw new Error('UNEXPECTED_EXECUTIONS_AFTER_ACTIVATE');
    }

    const pyFirst = spawnPython([
      'producer-d3-controlled-live',
      '--apply',
      '--mode',
      'first_seen',
      '--fixture',
      FIXTURE_REL,
      `--confirm-enable=${ENABLE_PHRASE}`,
      `--confirm-send=${SEND_FIRST}`,
      '--concurrency',
      '1',
      '--max-retries',
      '0',
    ]);
    report.mutations.producer_http_requests += 1;
    report.mutations.webhook_calls += 1;

    const producerFirst = pyFirst.json || {
      ok: false,
      final_state: 'PRODUCER_NO_JSON',
      status: pyFirst.status,
      stderr_len: pyFirst.stderr.length,
    };
    writeJson(resolve(REPO_EVIDENCE, 'FIRST-SEEN-PRODUCER-RESULT.json'), {
      label: 'FIRST_SEEN',
      event_id: eventId,
      producer_status: pyFirst.status,
      result: producerFirst,
      secrets_absent: true,
      full_webhook_url_absent: true,
    });
    writeJson(resolve(LOCAL_EVIDENCE, 'first-seen-producer.json'), {
      status: pyFirst.status,
      final_state: producerFirst.final_state || producerFirst.status || null,
      event_id: eventId,
    });

    const waited = await waitForNewExecution(creds, WORKFLOW_ID, priorIds, windowStart);
    if (!waited.found) {
      throw new Error('FIRST_SEEN_EXECUTION_NOT_OBSERVED');
    }
    const detail = await getExecutionDetail(creds, waited.execution.id);
    const summary = summarizeExecution(detail);
    report.mutations.executions_added += 1;

    const execPost = await executionSnapshot(creds, WORKFLOW_ID);
    const firstSeenUnambiguous =
      execPost.count === EXPECTED_EXEC_PRE + 1 &&
      summary.ok &&
      summary.has_claim_insert &&
      summary.has_respond_accepted &&
      summary.has_telegram_notify &&
      summary.telegram_runs === 1 &&
      (summary.dedupe_result === 'FIRST_SEEN' ||
        summary.response_result === 'ACCEPTED' ||
        producerFirst.dedupe_result === 'FIRST_SEEN' ||
        producerFirst.business_result === 'INTAKE_ACCEPTED' ||
        producerFirst.final_state === 'INTAKE_ACCEPTED' ||
        producerFirst.http_status === 202);

    if (summary.telegram_runs > 0) {
      report.mutations.telegram_attempted += 1;
      if (summary.telegram_ok === true || summary.telegram_message_id != null) {
        report.mutations.telegram_delivered += 1;
      }
    }

    writeJson(resolve(REPO_EVIDENCE, 'FIRST-SEEN-N8N-RESULT.json'), {
      label: 'FIRST_SEEN',
      execution_id: waited.execution.id,
      executions_before: EXPECTED_EXEC_PRE,
      executions_after: execPost.count,
      summary,
      unambiguous: firstSeenUnambiguous,
    });

    const tableAfter = await countTableRows(creds, TABLE_ID);
    const eventRows = await countTableRows(creds, TABLE_ID, {
      type: 'and',
      filters: [{ columnName: 'event_id', condition: 'eq', value: eventId }],
    });
    if (eventRows.count === 1 && tableAfter.count === TABLE_ROWS_PRE + 1) {
      report.mutations.table_rows_created_through_workflow += 1;
    }

    writeJson(resolve(REPO_EVIDENCE, 'FIRST-SEEN-DATATABLE-RESULT.json'), {
      table_id: TABLE_ID,
      total_rows: tableAfter.count,
      event_id: eventId,
      event_row_count: eventRows.count,
      expected_total: TABLE_ROWS_PRE + 1,
      ok: eventRows.count === 1 && tableAfter.count === TABLE_ROWS_PRE + 1,
    });

    writeJson(resolve(REPO_EVIDENCE, 'FIRST-SEEN-TELEGRAM-RESULT.json'), {
      node: TELEGRAM_NODE_NAME,
      telegram_runs: summary.telegram_runs,
      telegram_message_id: summary.telegram_message_id,
      telegram_ok: summary.telegram_ok,
      chat_id_expected: CHAT_ID,
      secrets_absent: true,
    });

    report.first_seen = {
      unambiguous: firstSeenUnambiguous,
      execution_id: waited.execution.id,
      producer_final_state: producerFirst.final_state || null,
      table_ok: eventRows.count === 1,
    };

    if (!firstSeenUnambiguous) {
      report.replay_skipped = 'REPLAY_SKIPPED_SAFETY_GATE';
      writeJson(resolve(REPO_EVIDENCE, 'EXACT-REPLAY-PRODUCER-RESULT.json'), {
        skipped: true,
        reason: 'REPLAY_SKIPPED_SAFETY_GATE',
        detail: 'FIRST_SEEN unambiguous gate failed',
      });
    } else if (args.skipReplay) {
      report.replay_skipped = 'REPLAY_SKIPPED_SAFETY_GATE';
      writeJson(resolve(REPO_EVIDENCE, 'EXACT-REPLAY-PRODUCER-RESULT.json'), {
        skipped: true,
        reason: 'REPLAY_SKIPPED_SAFETY_GATE',
        detail: '--skip-replay',
      });
    } else if (args.confirmSendReplay !== SEND_REPLAY) {
      report.replay_skipped = 'REPLAY_SKIPPED_SAFETY_GATE';
      writeJson(resolve(REPO_EVIDENCE, 'EXACT-REPLAY-PRODUCER-RESULT.json'), {
        skipped: true,
        reason: 'REPLAY_SKIPPED_SAFETY_GATE',
        detail: 'confirm-send-replay missing or mismatch',
      });
    } else {
      const prior2 = new Set((execPost.rows || []).map((r) => r.id));
      const window2 = new Date().toISOString();
      const pyReplay = spawnPython([
        'producer-d3-controlled-live',
        '--apply',
        '--mode',
        'exact_replay',
        `--confirm-enable=${ENABLE_PHRASE}`,
        `--confirm-send=${SEND_REPLAY}`,
        '--concurrency',
        '1',
        '--max-retries',
        '0',
      ]);
      report.mutations.producer_http_requests += 1;
      report.mutations.webhook_calls += 1;
      const producerReplay = pyReplay.json || {
        ok: false,
        final_state: 'PRODUCER_NO_JSON',
        status: pyReplay.status,
      };
      writeJson(resolve(REPO_EVIDENCE, 'EXACT-REPLAY-PRODUCER-RESULT.json'), {
        label: 'EXACT_REPLAY',
        event_id: eventId,
        producer_status: pyReplay.status,
        result: producerReplay,
        secrets_absent: true,
      });

      const waited2 = await waitForNewExecution(creds, WORKFLOW_ID, prior2, window2);
      let summary2 = { ok: false };
      if (waited2.found) {
        const detail2 = await getExecutionDetail(creds, waited2.execution.id);
        summary2 = summarizeExecution(detail2);
        report.mutations.executions_added += 1;
      }
      const execFinal = await executionSnapshot(creds, WORKFLOW_ID);
      const tableReplay = await countTableRows(creds, TABLE_ID, {
        type: 'and',
        filters: [{ columnName: 'event_id', condition: 'eq', value: eventId }],
      });
      writeJson(resolve(REPO_EVIDENCE, 'EXACT-REPLAY-N8N-RESULT.json'), {
        label: 'EXACT_REPLAY',
        found: waited2.found,
        execution_id: waited2.execution?.id || null,
        executions_after: execFinal.count,
        summary: summary2,
        telegram_runs_expected_0: summary2.telegram_runs === 0,
      });
      writeJson(resolve(REPO_EVIDENCE, 'EXACT-REPLAY-DATATABLE-RESULT.json'), {
        event_id: eventId,
        event_row_count: tableReplay.count,
        expected_still_1: tableReplay.count === 1,
      });
      report.replay = {
        executed: true,
        execution_id: waited2.execution?.id || null,
        producer_final_state: producerReplay.final_state || null,
      };
    }
  } catch (err) {
    report.error = String(err instanceof Error ? err.message : err).slice(0, 500);
    report.verdict = 'PARTIAL — CONTROLLED PRODUCER LIVE TEST REQUIRES REPAIR';
  } finally {
    const containment = {
      deactivate_attempted: false,
      emergency_attempted: false,
      final_active: null,
      final_running: null,
      final_executions: null,
      ok: false,
    };
    try {
      if (activated) {
        await deactivateAllowlistedWorkflow(actCreds, DEACTIVATE_PHRASE);
        report.mutations.activation_changes += 1;
        containment.deactivate_attempted = true;
        activated = false;
      } else {
        // Still attempt normal deactivate for safety if apply path started
        try {
          await deactivateAllowlistedWorkflow(actCreds, DEACTIVATE_PHRASE);
          report.mutations.activation_changes += 1;
          containment.deactivate_attempted = true;
        } catch {
          /* may already be inactive */
        }
      }
      let wf = await getWorkflow(WORKFLOW_ID, creds);
      if (wf.active === true) {
        await deactivateAllowlistedWorkflow(
          actCreds,
          EMERGENCY === D3_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE
            ? EMERGENCY
            : D3_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE,
        );
        report.mutations.activation_changes += 1;
        containment.emergency_attempted = true;
        wf = await getWorkflow(WORKFLOW_ID, creds);
      }
      const exec = await executionSnapshot(creds, WORKFLOW_ID);
      containment.final_active = wf.active;
      containment.final_running = exec.running;
      containment.final_executions = exec.count;
      containment.ok = wf.active === false && exec.running === 0;
    } catch (deactErr) {
      containment.error = String(
        deactErr instanceof Error ? deactErr.message : deactErr,
      ).slice(0, 300);
      report.verdict =
        'PARTIAL — CONTROLLED PRODUCER LIVE TEST CONTAINMENT REQUIRES REPAIR';
    }
    report.containment = containment;
    writeContainmentMd(resolve(REPO_EVIDENCE, 'CONTAINMENT-STATUS.md'), containment);
    writeJson(resolve(LOCAL_EVIDENCE, 'containment.json'), containment);
  }

  if (!report.verdict) {
    const success =
      !report.error &&
      report.containment?.ok &&
      report.first_seen?.unambiguous &&
      report.mutations.producer_http_requests >= 1 &&
      report.mutations.producer_http_requests <= 2 &&
      report.mutations.telegram_delivered === 1;
    if (success) {
      report.readiness = 'READY_FOR_CONTROLLED_PRODUCER_CONNECTION_BASELINE_COMMIT';
      report.verdict = report.replay?.executed
        ? 'COMPLETE — CONTROLLED PRODUCER LIVE CONNECTION PROVEN; FIRST_SEEN DELIVERED ONCE AND REPLAY SUPPRESSED'
        : 'COMPLETE — CONTROLLED PRODUCER LIVE CONNECTION PROVEN; FIRST_SEEN DELIVERED ONCE, REPLAY SAFELY DEFERRED';
    } else if (report.containment && !report.containment.ok) {
      report.verdict =
        'PARTIAL — CONTROLLED PRODUCER LIVE TEST CONTAINMENT REQUIRES REPAIR';
    } else {
      report.verdict =
        report.verdict ||
        'PARTIAL — CONTROLLED PRODUCER LIVE TEST CONTAINED; BASELINE REQUIRES REVIEW';
    }
  }

  writeJson(resolve(REPO_EVIDENCE, 'D3-RUNNER-SUMMARY.json'), {
    readiness: report.readiness,
    verdict: report.verdict,
    mutations: report.mutations,
    first_seen: report.first_seen,
    replay: report.replay,
    replay_skipped: report.replay_skipped,
    containment: report.containment,
    error: report.error,
    event_id: eventId,
  });
  writeJson(resolve(LOCAL_EVIDENCE, 'runner-report.json'), {
    mutations: report.mutations,
    verdict: report.verdict,
    error: report.error,
    event_id: eventId,
  });

  console.log(
    JSON.stringify(
      {
        mode: 'apply',
        readiness: report.readiness,
        verdict: report.verdict,
        mutations: report.mutations,
        replay_skipped: report.replay_skipped,
        containment: report.containment,
        error: report.error || null,
      },
      null,
      2,
    ),
  );

  return report.containment?.ok && !report.error ? 0 : 2;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const creds = loadCredentials();

  if (!args.apply) {
    process.exitCode = await runDry(creds);
    return;
  }
  process.exitCode = await runApply(args, creds);
}

if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  main().catch((err) => {
    console.error(
      JSON.stringify({
        ok: false,
        error: String(err instanceof Error ? err.message : err).slice(0, 400),
      }),
    );
    process.exitCode = 2;
  });
}
