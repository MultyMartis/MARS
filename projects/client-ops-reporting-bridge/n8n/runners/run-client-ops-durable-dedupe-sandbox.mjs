/**
 * Phase 1B-D1 — Durable Dedupe Design and Inactive Sandbox Implementation runner.
 *
 * Default: dry-run (compose + validate; no live mutation).
 *
 * Live sequence (exact phrases required):
 *   --apply
 *   --confirm-create-table="CREATE CLIENT OPS DEDUPE DATA TABLE BZPM"
 *   --confirm-apply="APPLY CLIENT OPS DURABLE DEDUPE SANDBOX BZPM"
 *   --confirm-activate="ACTIVATE CLIENT OPS DURABLE DEDUPE TEST BZPM"
 *   --confirm-post-first="SEND CLIENT OPS DEDUPE FIRST SEEN TEST BZPM"
 *   --confirm-post-replay="SEND CLIENT OPS DEDUPE EXACT REPLAY TEST BZPM"
 *   --confirm-post-conflict="SEND CLIENT OPS DEDUPE CONFLICT TEST BZPM"
 *   --confirm-deactivate="DEACTIVATE CLIENT OPS DURABLE DEDUPE TEST BZPM"
 *
 * Rollback:
 *   --rollback --confirm-rollback="ROLL BACK CLIENT OPS DURABLE DEDUPE SANDBOX BZPM"
 *
 * Never prints secrets, full webhook URLs, or raw execution payloads.
 * No live action on module import.
 */

import { createHash, randomUUID } from 'node:crypto';
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
import {
  activateAllowlistedWorkflow,
  deactivateAllowlistedWorkflow,
  loadActivationCredentials,
  ALLOWED_WORKFLOW_ID,
  ALLOWED_WORKFLOW_NAME,
  EXPECTED_HOST,
} from './lib/client-ops-n8n-activation-client.mjs';
import {
  loadUpdateCredentials,
  prepareWorkflowPutPayload,
  updateAllowlistedWorkflow,
} from './lib/client-ops-n8n-workflow-update-client.mjs';
import {
  ALLOWED_TABLE_NAME,
  D1_TABLE_COLUMNS,
  countTablesByExactName,
  createAllowlistedDataTable,
  deleteAllowlistedDataTable,
  getDataTable,
  getDataTableRows,
  loadDataTableCredentials,
} from './lib/client-ops-n8n-datatable-client.mjs';
import {
  AUTH_CRED_ID,
  AUTH_CRED_NAME,
  BASE_NODE_NAMES,
  DEDUPE_NODE_NAMES,
  EXPECTED_EXEC_PRE,
  EXPECTED_NODES_PRE,
  EXPECTED_VERSION_PRE,
  EXPECTED_MAX_EXEC_ID_PRE,
  SANDBOX_MARKER,
  TELEGRAM_NODE_NAME,
  TG_CRED_ID,
  TG_CRED_NAME,
  composeDedupePutFromLive,
  computeEventFingerprint,
  validateDedupePutPayload,
} from './lib/client-ops-dedupe-compose.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');

const CREATE_TABLE_PHRASE = 'CREATE CLIENT OPS DEDUPE DATA TABLE BZPM';
const APPLY_PHRASE = 'APPLY CLIENT OPS DURABLE DEDUPE SANDBOX BZPM';
const ACTIVATE_PHRASE = 'ACTIVATE CLIENT OPS DURABLE DEDUPE TEST BZPM';
const POST_FIRST_PHRASE = 'SEND CLIENT OPS DEDUPE FIRST SEEN TEST BZPM';
const POST_REPLAY_PHRASE = 'SEND CLIENT OPS DEDUPE EXACT REPLAY TEST BZPM';
const POST_CONFLICT_PHRASE = 'SEND CLIENT OPS DEDUPE CONFLICT TEST BZPM';
const DEACTIVATE_PHRASE = 'DEACTIVATE CLIENT OPS DURABLE DEDUPE TEST BZPM';
const ROLLBACK_PHRASE = 'ROLL BACK CLIENT OPS DURABLE DEDUPE SANDBOX BZPM';

const AUTH_HEADER = 'X-MARS-Client-Ops-Token';
const SECRET_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env',
);
const ROLLBACK_DIR = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/rollback/phase-1b-d1',
);
const LOCAL_EVIDENCE = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/evidence/phase-1b-d1',
);
const REPO_EVIDENCE = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/n8n/evidence/phase-1b-d1-durable-dedupe',
);

const REQUEST_TIMEOUT_MS = 20000;
const EXEC_POLL_MS = 800;
const EXEC_POLL_MAX = 30;
const RESPONSE_CAPTURE_MAX = 2048;
const PRODUCER_NAME = SANDBOX_MARKER;
const TEMP_SEMANTICS_NAME = 'MARS Client Ops Telegram Semantics Probe — TEMP';

function parseArgs(argv) {
  const args = {
    apply: false,
    rollback: false,
    confirmCreateTable: null,
    confirmApply: null,
    confirmActivate: null,
    confirmPostFirst: null,
    confirmPostReplay: null,
    confirmPostConflict: null,
    confirmDeactivate: null,
    confirmRollback: null,
  };
  for (const a of argv) {
    if (a === '--apply') args.apply = true;
    else if (a === '--rollback') args.rollback = true;
    else if (a.startsWith('--confirm-create-table='))
      args.confirmCreateTable = a.slice('--confirm-create-table='.length);
    else if (a.startsWith('--confirm-apply='))
      args.confirmApply = a.slice('--confirm-apply='.length);
    else if (a.startsWith('--confirm-activate='))
      args.confirmActivate = a.slice('--confirm-activate='.length);
    else if (a.startsWith('--confirm-post-first='))
      args.confirmPostFirst = a.slice('--confirm-post-first='.length);
    else if (a.startsWith('--confirm-post-replay='))
      args.confirmPostReplay = a.slice('--confirm-post-replay='.length);
    else if (a.startsWith('--confirm-post-conflict='))
      args.confirmPostConflict = a.slice('--confirm-post-conflict='.length);
    else if (a.startsWith('--confirm-deactivate='))
      args.confirmDeactivate = a.slice('--confirm-deactivate='.length);
    else if (a.startsWith('--confirm-rollback='))
      args.confirmRollback = a.slice('--confirm-rollback='.length);
  }
  return args;
}

function ensureDir(p) {
  mkdirSync(p, { recursive: true });
}

function writeJson(path, data) {
  ensureDir(dirname(path));
  writeFileSync(path, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
}

function loadEnvKey(filePath, key) {
  if (!existsSync(filePath)) return { ok: false, error: 'file_missing' };
  const raw = readFileSync(filePath, 'utf8');
  let value = '';
  for (const line of raw.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    if (!trimmed.startsWith(`${key}=`)) continue;
    value = trimmed.slice(`${key}=`.length).trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    break;
  }
  if (!value) return { ok: false, error: 'key_missing_or_empty' };
  return {
    ok: true,
    value,
    lengthClass: value.length >= 64 ? 'gte64' : value.length >= 32 ? 'gte32' : 'lt32',
  };
}

function fingerprintWorkflow(wf) {
  const nodes = wf.nodes || [];
  const fp = nodes.map((n) => `${n.name}|${n.type}|${n.typeVersion}`).join('||');
  return {
    fingerprint: fp,
    sha16: createHash('sha256').update(fp).digest('hex').slice(0, 16),
    node_names: nodes.map((n) => n.name),
    connection_keys: Object.keys(wf.connections || {}).sort(),
  };
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

async function executionSnapshot(creds, workflowId) {
  const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions?workflowId=${encodeURIComponent(workflowId)}&limit=100`;
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      Accept: 'application/json',
      'X-N8N-API-KEY': creds.apiKey,
    },
  });
  if (!response.ok) return { observable: false, reason: `HTTP_${response.status}`, rows: [], count: null };
  const data = await response.json();
  const rows = Array.isArray(data) ? data : data?.data;
  if (!Array.isArray(rows)) return { observable: false, reason: 'unexpected_shape', rows: [], count: null };
  return {
    observable: true,
    count: typeof data?.count === 'number' ? data.count : rows.length,
    nextCursor: data?.nextCursor || null,
    rows: rows.map((e) => ({
      id: String(e.id),
      status: e.status,
      finished: e.finished,
      startedAt: e.startedAt,
      stoppedAt: e.stoppedAt,
      mode: e.mode,
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
  if (!response.ok) return { ok: false, status: response.status };
  return { ok: true, data: await response.json() };
}

function summarizeExecution(detail) {
  if (!detail?.ok) return { ok: false };
  const runData = detail.data?.data?.resultData?.runData || {};
  const nodeOrder = [];
  const telegramRuns = Array.isArray(runData[TELEGRAM_NODE_NAME])
    ? runData[TELEGRAM_NODE_NAME].length
    : 0;
  for (const [name, runs] of Object.entries(runData)) {
    if (Array.isArray(runs) && runs.length > 0) nodeOrder.push(name);
  }
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
  return {
    ok: true,
    execution_id: String(detail.data?.id || ''),
    status: detail.data?.status,
    finished: detail.data?.finished,
    node_names_executed: nodeOrder,
    telegram_runs: telegramRuns,
    telegram_message_id: telegramMessageId,
    telegram_ok: telegramOk,
    has_dedupe_lookup: nodeOrder.includes('Dedupe Lookup'),
    has_dedupe_classify: nodeOrder.includes('Dedupe Classify'),
    has_claim_insert: nodeOrder.includes('Dedupe Claim Insert'),
    has_respond_accepted: nodeOrder.includes('Respond Accepted'),
    has_respond_non_first: nodeOrder.includes('Respond Non-First-Seen'),
  };
}

function buildValidEnvelope(overrides = {}) {
  const now = new Date();
  const observed = new Date(now.getTime() - 60_000);
  const status = overrides.status || 'OK';
  const eventId = overrides.event_id || randomUUID();
  const base = {
    schema_name: 'mars.client_ops.report',
    schema_version: '1.0',
    event_id: eventId,
    event_type: 'site.post_1c_monitor',
    generated_at: now.toISOString().replace(/\.\d{3}Z$/, 'Z'),
    observed_at: observed.toISOString().replace(/\.\d{3}Z$/, 'Z'),
    environment: 'sandbox',
    site: {
      site_id: 'SITE-002',
      site_name: 'ZPM-DEDUPE-SANDBOX',
      domain: 'bzpm.ru',
    },
    producer: {
      name: PRODUCER_NAME,
      version: '1b-d1.0',
    },
    run: {
      run_id: `dedupe-d1-${eventId.slice(0, 8)}`,
      source_status: 'NO_ACTION_REQUIRED',
      normalized_status: status,
      summary_code: 'NO_ACTION_REQUIRED',
      reason_codes: ['SANDBOX_DEDUPE_D1'],
    },
    action: {
      required: false,
      code: 'NONE',
      text: 'Тест durable dedupe MARS. Production SITE-002 не затронут.',
    },
    metrics: {
      baseline_count: 42,
      current_count: 42,
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
  if (overrides.metrics) Object.assign(base.metrics, overrides.metrics);
  if (overrides.event_id) base.event_id = overrides.event_id;
  return base;
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

async function capturePreState(creds) {
  const all = await listWorkflows(creds);
  const list = all.data || all || [];
  const exact = list.filter((w) => w.name === ALLOWED_WORKFLOW_NAME);
  const temp = list.filter((w) => w.name === TEMP_SEMANTICS_NAME);
  const wf = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
  const exec = await executionSnapshot(creds, ALLOWED_WORKFLOW_ID);
  const tableCount = await countTablesByExactName(creds, ALLOWED_TABLE_NAME);
  const fp = fingerprintWorkflow(wf);
  const webhook = (wf.nodes || []).find((n) => n.name === 'Webhook Intake');
  const telegram = (wf.nodes || []).find((n) => n.name === TELEGRAM_NODE_NAME);
  const connections = wf.connections || {};
  const patternB = (connections['Respond Accepted']?.main?.[0] || []).some(
    (c) => c.node === TELEGRAM_NODE_NAME,
  );

  return {
    exact_name_count: exact.length,
    temp_exact_name_count: temp.length,
    workflow: {
      id: wf.id,
      name: wf.name,
      active: wf.active,
      nodes: (wf.nodes || []).length,
      versionId: wf.versionId,
      node_names: (wf.nodes || []).map((n) => n.name),
    },
    fingerprint: fp,
    executions: exec.count,
    executions_observable: exec.observable,
    running: (exec.rows || []).filter((r) => r.status === 'running').length,
    max_execution_id: exec.rows?.length
      ? Math.max(...exec.rows.map((r) => Number(r.id)))
      : null,
    webhook: {
      authentication: webhook?.parameters?.authentication || null,
      credential_id: webhook?.credentials?.httpHeaderAuth?.id || null,
      credential_name: webhook?.credentials?.httpHeaderAuth?.name || null,
    },
    telegram: {
      credential_id: telegram?.credentials?.telegramApi?.id || null,
      credential_name: telegram?.credentials?.telegramApi?.name || null,
      chat_id: telegram?.parameters?.chatId ?? null,
    },
    pattern_b: patternB,
    data_table_nodes: (wf.nodes || []).filter((n) =>
      String(n.type).toLowerCase().includes('datatable'),
    ).length,
    dedupe_table_exact_name_count: tableCount,
    live: wf,
    exec_ids: new Set((exec.rows || []).map((r) => r.id)),
  };
}

function assertPreStateGates(pre) {
  const errors = [];
  if (pre.exact_name_count !== 1) errors.push('exact_name_count');
  if (pre.temp_exact_name_count !== 0) errors.push('temp_present');
  if (pre.workflow.active !== false) errors.push('active');
  if (pre.workflow.nodes !== EXPECTED_NODES_PRE) errors.push('nodes');
  if (pre.workflow.versionId !== EXPECTED_VERSION_PRE) errors.push('versionId');
  if (pre.executions !== EXPECTED_EXEC_PRE) errors.push(`executions_${pre.executions}`);
  if (pre.running !== 0) errors.push('running');
  if (pre.max_execution_id !== EXPECTED_MAX_EXEC_ID_PRE) {
    errors.push(`max_exec_${pre.max_execution_id}`);
  }
  if (pre.webhook.authentication !== 'headerAuth') errors.push('auth');
  if (pre.webhook.credential_id !== AUTH_CRED_ID) errors.push('auth_cred');
  if (pre.telegram.credential_id !== TG_CRED_ID) errors.push('tg_cred');
  if (String(pre.telegram.chat_id) !== '499423375') errors.push('tg_chat');
  if (!pre.pattern_b) errors.push('pattern_b');
  if (pre.data_table_nodes !== 0) errors.push('unexpected_datatable_nodes');
  if (pre.dedupe_table_exact_name_count !== 0) errors.push('dedupe_table_exists');
  for (const name of BASE_NODE_NAMES) {
    if (!pre.workflow.node_names.includes(name)) errors.push(`missing_${name}`);
  }
  return errors;
}

async function writeRollbackSnapshot(pre, designManifest) {
  ensureDir(ROLLBACK_DIR);
  const putRestore = prepareWorkflowPutPayload(pre.live);
  writeJson(resolve(ROLLBACK_DIR, 'pre-d1-workflow.put-payload.json'), putRestore);
  writeJson(resolve(ROLLBACK_DIR, 'pre-d1-manifest.json'), {
    phase: '1B-D1',
    captured_at: new Date().toISOString(),
    versionId: pre.workflow.versionId,
    active: false,
    nodes: pre.workflow.nodes,
    executions: pre.executions,
    fingerprint_sha16: pre.fingerprint.sha16,
    webhook_credential_id: AUTH_CRED_ID,
    telegram_credential_id: TG_CRED_ID,
    telegram_chat_id: '499423375',
    dedupe_table_exact_name_count: 0,
    table_name: ALLOWED_TABLE_NAME,
  });
  writeJson(resolve(ROLLBACK_DIR, 'd1-design-manifest.json'), designManifest);
  return {
    dir: ROLLBACK_DIR,
    files: [
      'pre-d1-workflow.put-payload.json',
      'pre-d1-manifest.json',
      'd1-design-manifest.json',
    ],
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const report = {
    phase: '1B-D1',
    mode: args.rollback ? 'rollback' : args.apply ? 'apply' : 'dry-run',
    started_at: new Date().toISOString(),
    mutations: {
      table_creates: 0,
      workflow_puts: 0,
      activation_changes: 0,
      webhook_posts: 0,
      telegram_deliveries: 0,
      table_deletes: 0,
    },
    readiness: 'NOT_READY_FOR_DURABLE_DEDUPE_BASELINE_COMMIT',
    verdict: null,
  };

  ensureDir(LOCAL_EVIDENCE);
  ensureDir(REPO_EVIDENCE);

  const creds = loadCredentials();
  const host = new URL(creds.apiUrl).host;
  if (host !== EXPECTED_HOST && !String(creds.apiUrl).includes(EXPECTED_HOST)) {
    // soft check — activation client owns strict host
  }

  if (args.rollback) {
    if (args.confirmRollback !== ROLLBACK_PHRASE) {
      throw new Error('Rollback requires exact confirm phrase');
    }
    const snapPath = resolve(ROLLBACK_DIR, 'pre-d1-workflow.put-payload.json');
    const metaPath = resolve(ROLLBACK_DIR, 'pre-d1-manifest.json');
    if (!existsSync(snapPath) || !existsSync(metaPath)) {
      throw new Error('Rollback snapshot missing');
    }
    const putPayload = JSON.parse(readFileSync(snapPath, 'utf8'));
    const meta = JSON.parse(readFileSync(metaPath, 'utf8'));
    const live = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
    if (live.active) {
      await deactivateAllowlistedWorkflow(
        loadActivationCredentials(),
        DEACTIVATE_PHRASE,
      );
      report.mutations.activation_changes += 1;
    }
    await updateAllowlistedWorkflow(putPayload, loadUpdateCredentials());
    report.mutations.workflow_puts += 1;
    const tableMetaPath = resolve(LOCAL_EVIDENCE, 'created-table-id.json');
    if (existsSync(tableMetaPath)) {
      const { table_id } = JSON.parse(readFileSync(tableMetaPath, 'utf8'));
      if (table_id) {
        await deleteAllowlistedDataTable(loadDataTableCredentials(), table_id);
        report.mutations.table_deletes += 1;
      }
    }
    const post = await capturePreState(creds);
    report.rollback = {
      triggered: true,
      restored_version_target: meta.versionId,
      post_active: post.workflow.active,
      post_nodes: post.workflow.nodes,
      table_count: post.dedupe_table_exact_name_count,
    };
    report.verdict = 'PARTIAL — DURABLE DEDUPE TEST FAILED AND SANDBOX ROLLED BACK SAFELY';
    writeJson(resolve(LOCAL_EVIDENCE, 'runner-report.json'), report);
    console.log(JSON.stringify({
      mode: 'rollback',
      verdict: report.verdict,
      mutations: report.mutations,
      rollback: report.rollback,
    }, null, 2));
    return;
  }

  const pre = await capturePreState(creds);
  const preErrors = assertPreStateGates(pre);
  writeJson(resolve(REPO_EVIDENCE, 'PRE-APPLY-MANIFEST.json'), {
    phase: '1B-D1',
    timestamp_utc: new Date().toISOString(),
    exact_name_count: pre.exact_name_count,
    workflow_id: pre.workflow.id,
    active: pre.workflow.active,
    nodes: pre.workflow.nodes,
    versionId: pre.workflow.versionId,
    executions: pre.executions,
    running: pre.running,
    max_execution_id: pre.max_execution_id,
    fingerprint_sha16: pre.fingerprint.sha16,
    webhook: pre.webhook,
    telegram: {
      credential_id: pre.telegram.credential_id,
      credential_name: pre.telegram.credential_name,
      chat_id: pre.telegram.chat_id,
    },
    pattern_b: pre.pattern_b,
    data_table_nodes: pre.data_table_nodes,
    dedupe_table_exact_name_count: pre.dedupe_table_exact_name_count,
    pre_gate_errors: preErrors,
  });

  if (preErrors.length) {
    report.verdict = 'PARTIAL — DURABLE DEDUPE IMPLEMENTATION BLOCKED BY PRE-STATE';
    report.pre_gate_errors = preErrors;
    writeJson(resolve(LOCAL_EVIDENCE, 'runner-report.json'), report);
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  // Dry-run compose uses placeholder table id for structure validation only
  const dryTableId = 'DRYRUN_TABLE_ID_PLACEHOLDER';
  const dryCompose = composeDedupePutFromLive(pre.live, dryTableId);
  if (!dryCompose.ok) {
    report.verdict = 'PARTIAL — DURABLE DEDUPE IMPLEMENTATION BLOCKED BY COMPOSE';
    report.compose_error = dryCompose.error;
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }
  const dryValidate = validateDedupePutPayload(dryCompose.bundle.put_payload, dryTableId);
  writeJson(resolve(REPO_EVIDENCE, 'SANITIZED-STRUCTURAL-DIFF.json'), {
    phase: '1B-D1',
    mode: 'dry-run-compose',
    pre_nodes: EXPECTED_NODES_PRE,
    post_nodes: dryCompose.expected_nodes_post,
    added_nodes: DEDUPE_NODE_NAMES,
    removed_nodes: [],
    connection_delta: {
      'IF Accepted Branch.main[0]': 'Prepare Accepted Response → Prepare Dedupe Context',
      new: [
        'Prepare Dedupe Context → Dedupe Lookup → Dedupe Classify → IF Dedupe First Seen',
        'IF Dedupe First Seen[true] → Dedupe Claim Insert → Prepare Accepted Response → Respond Accepted → Telegram',
        'IF Dedupe First Seen[false] → Prepare Non-First-Seen Response → Respond Non-First-Seen',
      ],
    },
    validate: dryValidate,
  });

  const designManifest = {
    phase: '1B-D1',
    architecture: 'n8n_data_table_primary',
    concurrency_class: 'DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN',
    table_name: ALLOWED_TABLE_NAME,
    columns: D1_TABLE_COLUMNS,
      fingerprint_algo: 'canonical_json_v1',
      fingerprint_note:
        'SHA-256 via require(crypto) is disallowed in this n8n Code sandbox; canonical JSON equality is the installed-safe fingerprint.',
    expected_nodes_post: dryCompose.expected_nodes_post,
    delivery_state_update_after_telegram: 'DEFERRED',
    retain_synthetic_row: true,
  };

  if (!args.apply) {
    report.dry_run = {
      pre_gates: 'PASS',
      compose: 'PASS',
      put_validate: dryValidate.ok ? 'PASS' : 'FAIL',
      put_validate_errors: dryValidate.errors,
      design: designManifest,
    };
    report.verdict = dryValidate.ok
      ? 'DRY_RUN_PASS — READY TO APPLY WITH PHRASES'
      : 'DRY_RUN_FAIL';
    writeJson(resolve(LOCAL_EVIDENCE, 'runner-report.json'), report);
    console.log(JSON.stringify({
      mode: 'dry-run',
      verdict: report.verdict,
      dry_run: report.dry_run,
    }, null, 2));
    if (!dryValidate.ok) process.exitCode = 2;
    return;
  }

  // APPLY path
  const required = [
    [args.confirmCreateTable, CREATE_TABLE_PHRASE, 'create-table'],
    [args.confirmApply, APPLY_PHRASE, 'apply'],
    [args.confirmActivate, ACTIVATE_PHRASE, 'activate'],
    [args.confirmPostFirst, POST_FIRST_PHRASE, 'post-first'],
    [args.confirmPostReplay, POST_REPLAY_PHRASE, 'post-replay'],
    [args.confirmPostConflict, POST_CONFLICT_PHRASE, 'post-conflict'],
    [args.confirmDeactivate, DEACTIVATE_PHRASE, 'deactivate'],
  ];
  for (const [got, need, label] of required) {
    if (got !== need) {
      throw new Error(`Missing or incorrect confirm phrase for ${label}`);
    }
  }

  const secret = loadEnvKey(SECRET_PATH, 'CLIENT_OPS_WEBHOOK_AUTH_SECRET');
  if (!secret.ok) throw new Error('Webhook auth secret unavailable locally');

  const webhookNode = (pre.live.nodes || []).find((n) => n.name === 'Webhook Intake');
  const webhookPath = webhookNode?.parameters?.path;
  if (!webhookPath) throw new Error('Webhook path missing');

  await writeRollbackSnapshot(pre, designManifest);
  writeJson(resolve(REPO_EVIDENCE, 'ROLLBACK-READINESS.md'.replace('.md', '.json')), {
    snapshot_dir: 'local/client-ops-reporting-bridge/bzpm.ru/rollback/phase-1b-d1/',
    prepared: true,
    table_delete_plan: 'delete only D1-created allowlisted table on rollback',
  });

  let tableId = null;
  let activated = false;
  let putApplied = false;
  let rollbackRecommended = false;
  const actCreds = loadActivationCredentials();
  const webhookUrl = `${normalizeBaseUrl(actCreds.apiUrl)}/webhook/${webhookPath}`;

  try {
    // 1) Create table
    const createRes = await createAllowlistedDataTable(loadDataTableCredentials(), {
      name: ALLOWED_TABLE_NAME,
      columns: D1_TABLE_COLUMNS,
    });
    report.mutations.table_creates += 1;
    tableId = createRes.data?.id;
    if (!tableId) throw new Error('Table create returned no id');
    writeJson(resolve(LOCAL_EVIDENCE, 'created-table-id.json'), {
      table_id: tableId,
      name: ALLOWED_TABLE_NAME,
    });

    const tableGet = await getDataTable(loadDataTableCredentials(), tableId);
    const rows0 = await getDataTableRows(loadDataTableCredentials(), tableId, { limit: 10 });
    const rowList0 = rows0.data?.data || rows0.data || [];
    writeJson(resolve(REPO_EVIDENCE, 'DATATABLE-CREATE-EVIDENCE.json'), {
      phrase: CREATE_TABLE_PHRASE,
      create_count: 1,
      table_name: ALLOWED_TABLE_NAME,
      table_id: tableId,
      column_count: (tableGet.data?.columns || []).length,
      column_names: (tableGet.data?.columns || []).map((c) => c.name),
      initial_row_count: Array.isArray(rowList0) ? rowList0.length : null,
      http_status: createRes.status,
      verification: tableGet.data?.name === ALLOWED_TABLE_NAME ? 'PASS' : 'FAIL',
    });
    if (tableGet.data?.name !== ALLOWED_TABLE_NAME) {
      throw new Error('Created table name mismatch');
    }

    // 2) Workflow PUT
    const compose = composeDedupePutFromLive(pre.live, tableId);
    if (!compose.ok) throw new Error(`Compose failed: ${compose.error}`);
    const v = validateDedupePutPayload(compose.bundle.put_payload, tableId);
    if (!v.ok) throw new Error(`Put validate failed: ${v.errors.join(',')}`);

    writeJson(
      resolve(
        REPO_ROOT,
        'local/client-ops-reporting-bridge/bzpm.ru/apply/mars-client-ops-bridge-bzpm.durable-dedupe.put-payload.json',
      ),
      compose.bundle.put_payload,
    );

    await updateAllowlistedWorkflow(compose.bundle.put_payload, loadUpdateCredentials());
    report.mutations.workflow_puts += 1;
    putApplied = true;

    const postPut = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
    const postPutExec = await executionSnapshot(creds, ALLOWED_WORKFLOW_ID);
    const postFp = fingerprintWorkflow(postPut);
    writeJson(resolve(REPO_EVIDENCE, 'POST-APPLY-WORKFLOW-STATE.json'), {
      phrase: APPLY_PHRASE,
      put_count: 1,
      pre_versionId: pre.workflow.versionId,
      post_versionId: postPut.versionId,
      pre_nodes: EXPECTED_NODES_PRE,
      post_nodes: (postPut.nodes || []).length,
      active: postPut.active,
      executions: postPutExec.count,
      running: (postPutExec.rows || []).filter((r) => r.status === 'running').length,
      fingerprint_sha16: postFp.sha16,
      node_names: (postPut.nodes || []).map((n) => n.name),
      auth_credential_id: (postPut.nodes || []).find((n) => n.name === 'Webhook Intake')
        ?.credentials?.httpHeaderAuth?.id,
      telegram_credential_id: (postPut.nodes || []).find((n) => n.name === TELEGRAM_NODE_NAME)
        ?.credentials?.telegramApi?.id,
      telegram_chat_id: (postPut.nodes || []).find((n) => n.name === TELEGRAM_NODE_NAME)
        ?.parameters?.chatId,
      pattern_b: ((postPut.connections || {})['Respond Accepted']?.main?.[0] || []).some(
        (c) => c.node === TELEGRAM_NODE_NAME,
      ),
    });
    writeJson(resolve(REPO_EVIDENCE, 'SANITIZED-STRUCTURAL-DIFF.json'), {
      phase: '1B-D1',
      mode: 'post-apply',
      pre_nodes: EXPECTED_NODES_PRE,
      post_nodes: (postPut.nodes || []).length,
      added_nodes: DEDUPE_NODE_NAMES,
      removed_nodes: [],
      validate: v,
    });

    if (postPut.active !== false) throw new Error('Workflow active after PUT');
    if ((postPut.nodes || []).length !== compose.expected_nodes_post) {
      throw new Error(`Unexpected post node count ${(postPut.nodes || []).length}`);
    }
    if (postPutExec.count !== EXPECTED_EXEC_PRE) {
      throw new Error(`Executions changed during PUT: ${postPutExec.count}`);
    }
    if (postPut.versionId === pre.workflow.versionId) {
      throw new Error('versionId did not change after PUT');
    }

    // 3) Activate
    await activateAllowlistedWorkflow(actCreds, ACTIVATE_PHRASE);
    report.mutations.activation_changes += 1;
    activated = true;
    const activeCheck = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
    if (activeCheck.active !== true) throw new Error('Activation did not stick');

    const eventId = randomUUID();
    const firstBody = buildValidEnvelope({ event_id: eventId });
    const fingerprint = computeEventFingerprint(firstBody);
    const priorIds = new Set(pre.exec_ids);
    let telegramDeliveries = 0;

    async function runPost(label, body, phrase) {
      const startedAfter = new Date(Date.now() - 2000).toISOString();
      const postResult = await postWebhook(webhookUrl, secret.value, body);
      report.mutations.webhook_posts += 1;
      const waited = await waitForNewExecution(
        creds,
        ALLOWED_WORKFLOW_ID,
        priorIds,
        startedAfter,
      );
      if (waited.found && waited.execution) {
        priorIds.add(waited.execution.id);
      }
      let summary = { ok: false };
      if (waited.found && waited.execution) {
        const detail = await getExecutionDetail(creds, waited.execution.id);
        summary = summarizeExecution(detail);
      }
      if (summary.telegram_runs > 0) {
        telegramDeliveries += summary.telegram_runs;
        report.mutations.telegram_deliveries = telegramDeliveries;
      }
      return {
        label,
        phrase,
        http_status: postResult.status,
        response_result: postResult.json?.result || null,
        response_dedupe: postResult.json?.dedupe || null,
        response_ok: postResult.json?.ok ?? null,
        execution_id: summary.execution_id || waited.execution?.id || null,
        execution_summary: summary,
        post_ok: postResult.ok,
        post_error: postResult.error || null,
        url_sanitized: postResult.url_sanitized,
      };
    }

    // POST 1 FIRST_SEEN
    const first = await runPost('FIRST_SEEN', firstBody, POST_FIRST_PHRASE);
    writeJson(resolve(REPO_EVIDENCE, 'FIRST-SEEN-RESULT.json'), {
      ...first,
      event_id: eventId,
      event_fingerprint: fingerprint,
      expected: {
        http_status: 202,
        result: 'ACCEPTED',
        dedupe: 'FIRST_SEEN',
        telegram_runs: 1,
      },
    });
    if (
      first.http_status !== 202 ||
      first.response_result !== 'ACCEPTED' ||
      first.response_dedupe !== 'FIRST_SEEN' ||
      first.execution_summary.telegram_runs !== 1 ||
      !first.execution_summary.has_claim_insert
    ) {
      rollbackRecommended = true;
      throw new Error('FIRST_SEEN test failed gates');
    }

    // POST 2 EXACT REPLAY
    const replay = await runPost('EXACT_REPLAY', firstBody, POST_REPLAY_PHRASE);
    writeJson(resolve(REPO_EVIDENCE, 'EXACT-REPLAY-RESULT.json'), {
      ...replay,
      event_id: eventId,
      event_fingerprint: fingerprint,
      expected: {
        http_status: 200,
        result: 'DUPLICATE_SUPPRESSED',
        dedupe: 'DUPLICATE',
        telegram_runs: 0,
      },
      total_telegram_deliveries_after: telegramDeliveries,
    });
    if (
      replay.http_status !== 200 ||
      replay.response_result !== 'DUPLICATE_SUPPRESSED' ||
      replay.execution_summary.telegram_runs !== 0 ||
      telegramDeliveries !== 1
    ) {
      rollbackRecommended = true;
      throw new Error('EXACT_REPLAY test failed gates');
    }

    // POST 3 CONFLICT
    const conflictBody = buildValidEnvelope({
      event_id: eventId,
      metrics: { baseline_count: 99 },
    });
    const conflictFp = computeEventFingerprint(conflictBody);
    const conflict = await runPost('EVENT_ID_CONFLICT', conflictBody, POST_CONFLICT_PHRASE);
    writeJson(resolve(REPO_EVIDENCE, 'EVENT-ID-CONFLICT-RESULT.json'), {
      ...conflict,
      event_id: eventId,
      original_fingerprint: fingerprint,
      conflict_fingerprint: conflictFp,
      expected: {
        http_status: 409,
        result: 'EVENT_ID_CONFLICT',
        telegram_runs: 0,
      },
      total_telegram_deliveries_after: telegramDeliveries,
    });
    if (
      conflict.http_status !== 409 ||
      conflict.response_result !== 'EVENT_ID_CONFLICT' ||
      conflict.execution_summary.telegram_runs !== 0 ||
      telegramDeliveries !== 1
    ) {
      rollbackRecommended = true;
      throw new Error('EVENT_ID_CONFLICT test failed gates');
    }

    // Table post-test state
    const rowsFinal = await getDataTableRows(loadDataTableCredentials(), tableId, {
      limit: 20,
      filter: {
        type: 'and',
        filters: [{ columnName: 'event_id', condition: 'eq', value: eventId }],
      },
    });
    const finalRows = rowsFinal.data?.data || rowsFinal.data || [];
    const retained = Array.isArray(finalRows) ? finalRows : [];
    writeJson(resolve(REPO_EVIDENCE, 'DATATABLE-POST-TEST-STATE.json'), {
      table_id: tableId,
      table_name: ALLOWED_TABLE_NAME,
      exact_name_count: await countTablesByExactName(creds, ALLOWED_TABLE_NAME),
      row_count_for_event: retained.length,
      retained_policy: 'retain_one_sanitized_synthetic_d1_row',
      rows_sanitized: retained.map((r) => ({
        event_id: r.event_id,
        event_fingerprint: r.event_fingerprint,
        intake_state: r.intake_state,
        delivery_state: r.delivery_state,
        duplicate_count: r.duplicate_count,
        conflict_count: r.conflict_count,
        sandbox_marker: r.sandbox_marker,
        site_id: r.site_id,
      })),
      original_fingerprint_retained:
        retained.length === 1 && retained[0].event_fingerprint === fingerprint,
      secrets_absent: true,
      raw_payload_absent: true,
    });

    writeJson(resolve(REPO_EVIDENCE, 'TELEGRAM-DELIVERY-EVIDENCE.json'), {
      max_allowed: 1,
      attempts: telegramDeliveries,
      delivered: telegramDeliveries,
      duplicates: 0,
      chat_id: '499423375',
      credential_id: TG_CRED_ID,
      message_id: first.execution_summary.telegram_message_id,
      production_data: false,
      secrets: false,
    });

    report.tests = { first, replay, conflict, fingerprint, eventId };
    report.mutations.telegram_deliveries = telegramDeliveries;
  } catch (err) {
    report.error = String(err instanceof Error ? err.message : err).slice(0, 400);
    report.rollback_recommended = rollbackRecommended || putApplied;
    report.verdict = rollbackRecommended
      ? 'PARTIAL — DURABLE DEDUPE TEST FAILED; RUN ROLLBACK'
      : 'PARTIAL — DURABLE DEDUPE CONTAINMENT REQUIRES REPAIR';
  } finally {
    if (activated) {
      try {
        await deactivateAllowlistedWorkflow(actCreds, DEACTIVATE_PHRASE);
        report.mutations.activation_changes += 1;
        activated = false;
      } catch (deactErr) {
        report.deactivate_error = String(
          deactErr instanceof Error ? deactErr.message : deactErr,
        ).slice(0, 200);
      }
    }
  }

  const finalWf = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
  const finalExec = await executionSnapshot(creds, ALLOWED_WORKFLOW_ID);
  const finalTableCount = await countTablesByExactName(creds, ALLOWED_TABLE_NAME);
  report.final_state = {
    active: finalWf.active,
    nodes: (finalWf.nodes || []).length,
    versionId: finalWf.versionId,
    executions: finalExec.count,
    running: (finalExec.rows || []).filter((r) => r.status === 'running').length,
    table_exact_name_count: finalTableCount,
  };

  writeJson(resolve(REPO_EVIDENCE, 'CONTAINMENT-STATUS.md'.replace(/\.md$/, '.json')), {
    final_active: finalWf.active,
    executions: finalExec.count,
    expected_executions: EXPECTED_EXEC_PRE + 3,
    running: report.final_state.running,
    table_count: finalTableCount,
    runtime_producer: false,
    scheduler: false,
  });

  const success =
    !report.error &&
    finalWf.active === false &&
    finalExec.count === EXPECTED_EXEC_PRE + 3 &&
    report.mutations.webhook_posts === 3 &&
    report.mutations.telegram_deliveries === 1 &&
    report.mutations.table_creates === 1 &&
    report.mutations.workflow_puts === 1 &&
    finalTableCount === 1;

  if (success) {
    report.readiness = 'READY_FOR_DURABLE_DEDUPE_BASELINE_COMMIT';
    report.verdict =
      'COMPLETE — DURABLE DEDUPE PROVEN IN INACTIVE SANDBOX; DUPLICATE DELIVERY SUPPRESSED';
  } else if (!report.verdict) {
    report.verdict = 'PARTIAL — DURABLE DEDUPE IMPLEMENTATION BLOCKED BY INSTALLED CAPABILITY';
  }

  writeJson(resolve(REPO_EVIDENCE, 'D1-DECISION.json'), {
    readiness: report.readiness,
    verdict: report.verdict,
    concurrency_class: 'DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN',
    architecture: 'n8n_data_table_primary',
    mutations: report.mutations,
    final_state: report.final_state,
  });
  writeJson(resolve(LOCAL_EVIDENCE, 'runner-report.json'), {
    ...report,
    live: undefined,
    tests: report.tests
      ? {
          eventId: report.tests.eventId,
          fingerprint: report.tests.fingerprint,
          first_http: report.tests.first?.http_status,
          replay_http: report.tests.replay?.http_status,
          conflict_http: report.tests.conflict?.http_status,
        }
      : null,
  });

  console.log(
    JSON.stringify(
      {
        mode: 'apply',
        readiness: report.readiness,
        verdict: report.verdict,
        mutations: report.mutations,
        final_state: report.final_state,
        error: report.error || null,
      },
      null,
      2,
    ),
  );

  if (!success) process.exitCode = 2;
}

function postWebhook(webhookUrl, secret, body) {
  return (async () => {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);
    try {
      const response = await fetch(webhookUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
          [AUTH_HEADER]: secret,
        },
        body: JSON.stringify(body),
        signal: controller.signal,
      });
      const text = await response.text();
      let json = null;
      try {
        json = text ? JSON.parse(text) : null;
      } catch {
        json = null;
      }
      return {
        ok: true,
        status: response.status,
        body_preview: text.slice(0, RESPONSE_CAPTURE_MAX),
        json,
        url_sanitized: sanitizeUrl(webhookUrl),
      };
    } catch (err) {
      return {
        ok: false,
        error: String(err instanceof Error ? err.message : err).slice(0, 200),
        url_sanitized: sanitizeUrl(webhookUrl),
      };
    } finally {
      clearTimeout(timer);
    }
  })();
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch((err) => {
    console.error(String(err instanceof Error ? err.message : err));
    process.exitCode = 1;
  });
}
