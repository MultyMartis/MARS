/**
 * Phase 1B-C1 — Telegram Sandbox Integration Controlled Apply.
 *
 * Default: dry-run (compose + validate; no live mutation).
 *
 * Live apply + one sandbox delivery:
 *   node run-client-ops-telegram-sandbox-controlled-apply.mjs --apply \
 *     --confirm-apply="APPLY CLIENT OPS TELEGRAM SANDBOX INTEGRATION BZPM" \
 *     --confirm-activate="ACTIVATE CLIENT OPS TELEGRAM SANDBOX TEST BZPM" \
 *     --confirm-post="SEND ONE CLIENT OPS TELEGRAM SANDBOX TEST BZPM" \
 *     --confirm-deactivate="DEACTIVATE CLIENT OPS TELEGRAM SANDBOX TEST BZPM"
 *
 * Rollback only:
 *   node run-client-ops-telegram-sandbox-controlled-apply.mjs --rollback \
 *     --confirm-rollback="ROLL BACK CLIENT OPS TELEGRAM SANDBOX INTEGRATION BZPM"
 *
 * Never prints secrets, full webhook URLs, or raw Telegram/execution payloads.
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
import { sanitizeWorkflow } from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/sanitize-workflow.mjs';
import {
  C1_ACTIVATION_CONFIRM_PHRASE,
  C1_DEACTIVATION_CONFIRM_PHRASE,
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

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');

const APPLY_CONFIRM = 'APPLY CLIENT OPS TELEGRAM SANDBOX INTEGRATION BZPM';
const POST_CONFIRM = 'SEND ONE CLIENT OPS TELEGRAM SANDBOX TEST BZPM';
const ROLLBACK_CONFIRM = 'ROLL BACK CLIENT OPS TELEGRAM SANDBOX INTEGRATION BZPM';

const TG_CRED_ID = '2bIC5376l7ElXb4B';
const TG_CRED_NAME = 'MARS Client Ops Telegram — bzpm.ru';
const AUTH_CRED_ID = 'WKHmPaw6QBp7WnzP';
const AUTH_CRED_NAME = 'MARS Client Ops Webhook Auth — bzpm.ru';
const EXPECTED_VERSION_PRE = '6c6d1282-0105-47e1-a3f5-b070cec0664b';
const EXPECTED_EXEC_PRE = 24;
const EXPECTED_NODES_PRE = 9;
const TELEGRAM_NODE_NAME = 'Telegram Notify Accepted';
const AUTH_HEADER = 'X-MARS-Client-Ops-Token';
const PRODUCER_NAME = 'mars-client-ops-telegram-sandbox-c1';
const TEMP_SEMANTICS_NAME = 'MARS Client Ops Telegram Semantics Probe — TEMP';

const SECRET_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env',
);
const TG_SECRET_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/telegram.secrets.local.env',
);
const TG_TARGET_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/telegram.target.local.env',
);
const COMMITTED_PROPOSAL = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/n8n/evidence/phase-1b-c-telegram-bot-intake/PROPOSED-INTEGRATION.json',
);
const IGNORED_PROPOSAL = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/apply/mars-client-ops-bridge-bzpm.telegram-sandbox.proposed.json',
);
const LOCAL_PUT_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/apply/mars-client-ops-bridge-bzpm.telegram-sandbox.put-payload.json',
);
const ROLLBACK_DIR = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/rollback/phase-1b-c1',
);
const LOCAL_EVIDENCE = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/evidence/phase-1b-c1',
);
const REPO_EVIDENCE = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/n8n/evidence/phase-1b-c1-telegram-sandbox-controlled-apply',
);

const REQUEST_TIMEOUT_MS = 20000;
const EXEC_POLL_MS = 800;
const EXEC_POLL_MAX = 25;
const RESPONSE_CAPTURE_MAX = 2048;

const BASE_NODE_NAMES = [
  'Webhook Intake',
  'Capture Request Metadata',
  'Process Client Ops Gates',
  'IF Accepted Branch',
  'Prepare Accepted Response',
  'Prepare Rejected Response',
  'Respond Accepted',
  'Respond Rejected',
  'Sanitized Internal Evidence',
];

function parseArgs(argv) {
  const args = {
    apply: false,
    rollback: false,
    confirmApply: null,
    confirmActivate: null,
    confirmPost: null,
    confirmDeactivate: null,
    confirmRollback: null,
  };
  for (const a of argv) {
    if (a === '--apply') args.apply = true;
    else if (a === '--rollback') args.rollback = true;
    else if (a.startsWith('--confirm-apply=')) args.confirmApply = a.slice('--confirm-apply='.length);
    else if (a.startsWith('--confirm-activate='))
      args.confirmActivate = a.slice('--confirm-activate='.length);
    else if (a.startsWith('--confirm-post=')) args.confirmPost = a.slice('--confirm-post='.length);
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
  return { ok: true, value, lengthClass: value.length >= 64 ? 'gte64' : value.length >= 32 ? 'gte32' : 'lt32' };
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

function buildTelegramTextExpression() {
  // Cross-node reference keeps accepted-path gating; no helper Code/Set node.
  return `={{ (() => {
  const body = $('Capture Request Metadata').item.json.body || {};
  const status = String((body.run && body.run.normalized_status) || 'OK');
  const statusRu =
    status === 'OK' ? 'Всё работает штатно'
    : status === 'ATTENTION' ? 'Требуется внимание'
    : status === 'FAILED' ? 'Есть сбой'
    : status === 'BLOCKED' ? 'Доставка заблокирована'
    : status;
  const observedRaw = String(body.observed_at || body.generated_at || '');
  const observed = observedRaw.replace('T', ' ').replace(/\\.\\d{3}Z$/, '').replace(/Z$/, '').slice(0, 16);
  const eventShort = String(body.event_id || '').slice(0, 8);
  const problems =
    Number((body.metrics && body.metrics.onboarding_needed_count) || 0) +
    Number((body.metrics && body.metrics.removed_urls) || 0);
  const importResult = String((body.action && body.action.text) || 'Тестовая проверка канала уведомлений');
  const rec = status === 'OK' ? 'Действия не требуются' : String((body.action && body.action.text) || 'Требуется проверка');
  return '[' + status + '] bzpm.ru — контроль после обмена с 1С\\n\\n'
    + 'Статус: ' + statusRu + '\\n'
    + 'Время проверки: ' + observed + '\\n'
    + 'Результат импорта: ' + importResult + '\\n'
    + 'Найдено проблем: ' + problems + '\\n'
    + 'Рекомендация: ' + rec + '\\n'
    + 'Event: ' + eventShort + '\\n\\n'
    + 'Тестовое уведомление MARS. Production SITE-002 не затронут.';
})() }}`;
}

function buildTelegramNode(chatId) {
  // Parameter shape matches Phase 1B-C0S proven sendMessage node (typeVersion 1.2).
  return {
    parameters: {
      chatId: String(chatId),
      text: buildTelegramTextExpression(),
      additionalFields: {
        appendAttribution: false,
      },
    },
    id: randomUUID(),
    name: TELEGRAM_NODE_NAME,
    type: 'n8n-nodes-base.telegram',
    typeVersion: 1.2,
    position: [1440, 180],
    credentials: {
      telegramApi: {
        id: TG_CRED_ID,
        name: TG_CRED_NAME,
      },
    },
  };
}

function composePutFromLive(live, chatId) {
  const nodes = structuredClone(live.nodes || []);
  const connections = structuredClone(live.connections || {});
  if (nodes.some((n) => String(n.type).includes('telegram'))) {
    return { ok: false, error: 'telegram_already_present' };
  }
  if (nodes.length !== EXPECTED_NODES_PRE) {
    return { ok: false, error: `unexpected_pre_node_count_${nodes.length}` };
  }
  for (const name of BASE_NODE_NAMES) {
    if (!nodes.some((n) => n.name === name)) {
      return { ok: false, error: `missing_base_node_${name}` };
    }
  }
  if (connections['Respond Accepted']) {
    return { ok: false, error: 'respond_accepted_already_has_outgoing' };
  }
  const telegram = buildTelegramNode(chatId);
  nodes.push(telegram);
  connections['Respond Accepted'] = {
    main: [[{ node: TELEGRAM_NODE_NAME, type: 'main', index: 0 }]],
  };
  const put_payload = prepareWorkflowPutPayload({
    name: live.name,
    nodes,
    connections,
    settings: live.settings,
  });
  return {
    ok: true,
    bundle: {
      phase: '1B-C1',
      applied: false,
      workflow_id: ALLOWED_WORKFLOW_ID,
      workflow_name: ALLOWED_WORKFLOW_NAME,
      active: false,
      pattern: 'B_RESPONSE_FIRST_THEN_TELEGRAM',
      pre_put_versionId: live.versionId,
      telegram_node_name: TELEGRAM_NODE_NAME,
      telegram_credential: { id: TG_CRED_ID, name: TG_CRED_NAME, type: 'telegramApi' },
      chat_id: chatId,
      put_payload,
    },
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
  if (!response.ok) return { observable: false, reason: `HTTP_${response.status}`, rows: [], count: null };
  const data = await response.json();
  const rows = Array.isArray(data) ? data : data?.data;
  if (!Array.isArray(rows)) return { observable: false, reason: 'unexpected_shape', rows: [], count: null };
  return {
    observable: true,
    count: typeof data?.count === 'number' ? data.count : rows.length,
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

async function listCredentialsMeta(creds) {
  const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/credentials`;
  const response = await fetch(url, {
    method: 'GET',
    headers: {
      Accept: 'application/json',
      'X-N8N-API-KEY': creds.apiKey,
    },
  });
  if (!response.ok) return [];
  const data = await response.json();
  const rows = Array.isArray(data) ? data : data?.data;
  return Array.isArray(rows) ? rows : [];
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
        (!startedAtMs || !r.startedAt || new Date(r.startedAt).getTime() >= startedAtMs - 5000),
    );
    const finished = fresh.find((r) => r.finished || r.status === 'success' || r.status === 'error');
    if (finished) return { snap, execution: finished };
    await sleep(EXEC_POLL_MS);
  }
  const snap = await executionSnapshot(creds, workflowId);
  return { snap, execution: null };
}

function redactText(text, secret) {
  let out = String(text || '');
  if (secret && secret.length >= 8) out = out.split(secret).join('<REDACTED_SECRET>');
  out = out.replace(/https?:\/\/[^\s"'\\]+/gi, '<REDACTED_URL>');
  out = out.replace(/\/webhook(?:-test)?\/[A-Za-z0-9_-]+/gi, '/webhook/<REDACTED_PATH>');
  out = out.replace(/[A-Za-z]:\\[^\s"'\\]+/g, '<REDACTED_PATH>');
  out = out.replace(/\b\d{6,}:[A-Za-z0-9_-]{20,}\b/g, '<REDACTED_TOKEN>');
  if (out.length > RESPONSE_CAPTURE_MAX) out = `${out.slice(0, RESPONSE_CAPTURE_MAX - 3)}...`;
  return out;
}

function inspectExecutionSanitized(exec) {
  const runData = exec?.data?.resultData?.runData || {};
  const entries = [];
  let telegramMessageId = null;
  let telegramChatId = null;
  for (const [nodeName, runs] of Object.entries(runData)) {
    const arr = Array.isArray(runs) ? runs : [];
    for (let i = 0; i < arr.length; i += 1) {
      const run = arr[i] || {};
      const err = run.error ? String(run.error?.message || 'error') : null;
      let telegramOk = false;
      let telegramHasMessageId = false;
      try {
        const main = run.data?.main;
        const first = Array.isArray(main) && Array.isArray(main[0]) ? main[0][0] : null;
        const json = first?.json || {};
        if (nodeName.includes('Telegram')) {
          const mid = json.message_id || json.messageId || json.result?.message_id;
          const cid = json.chat?.id || json.chat_id || json.result?.chat?.id;
          telegramHasMessageId = mid != null;
          telegramOk = !err && (telegramHasMessageId || json.ok === true || Boolean(json.chat));
          if (mid != null && telegramMessageId == null) telegramMessageId = Number(mid);
          if (cid != null && telegramChatId == null) telegramChatId = Number(cid);
        }
      } catch {
        // ignore
      }
      entries.push({
        node: nodeName,
        run_index: i,
        startTime: typeof run.startTime === 'number' ? run.startTime : null,
        executionTime: typeof run.executionTime === 'number' ? run.executionTime : null,
        has_error: Boolean(err),
        error_class: err ? redactText(err).slice(0, 120) : null,
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
  const respondIdx = nodeOrder.findIndex((n) => n === 'Respond Accepted');
  const tgIdx = nodeOrder.findIndex((n) => n === TELEGRAM_NODE_NAME);
  return {
    execution_status: exec.status || null,
    finished: Boolean(exec.finished),
    node_order: nodeOrder,
    node_run_count: entries.length,
    respond_before_telegram: respondIdx >= 0 && tgIdx > respondIdx,
    telegram_node_runs: entries.filter((e) => e.node === TELEGRAM_NODE_NAME).length,
    telegram_ok_signal: entries.some((e) => e.telegram_ok_signal),
    telegram_message_id_present: entries.some((e) => e.telegram_message_id_present),
    telegram_message_id: Number.isFinite(telegramMessageId) ? telegramMessageId : null,
    telegram_chat_id: Number.isFinite(telegramChatId) ? telegramChatId : null,
    runs: entries,
  };
}

function structuralState(wf, execSnap) {
  const nodes = wf.nodes || [];
  const webhook = nodes.find((n) => n.type === 'n8n-nodes-base.webhook');
  const tg = nodes.filter((n) => String(n.type).includes('telegram'));
  const fp = fingerprintWorkflow(wf);
  const running = (execSnap.rows || []).filter(
    (r) => r.status === 'running' || (r.finished === false && r.status !== 'success' && r.status !== 'error'),
  ).length;
  return {
    id: wf.id,
    name: wf.name,
    active: wf.active,
    nodes: nodes.length,
    versionId: wf.versionId,
    executions: execSnap.count,
    running,
    webhook_authentication: webhook?.parameters?.authentication || null,
    auth_credential: webhook?.credentials?.httpHeaderAuth || null,
    telegram_nodes: tg.length,
    telegram_node_names: tg.map((n) => n.name),
    telegram_credential: tg[0]?.credentials?.telegramApi || null,
    telegram_chat_id: tg[0]?.parameters?.chatId != null ? String(tg[0].parameters.chatId) : null,
    pattern_b_connection:
      (wf.connections || {})['Respond Accepted']?.main?.[0]?.[0]?.node || null,
    rejected_reaches_telegram:
      (wf.connections || {})['Respond Rejected']?.main?.[0]?.[0]?.node === TELEGRAM_NODE_NAME,
    http_request_nodes: nodes.filter((n) => String(n.type).includes('httpRequest')).length,
    fingerprint_sha16: fp.sha16,
    fingerprint: fp.fingerprint,
  };
}

function compareProposals(expectedChatId) {
  const committed = JSON.parse(readFileSync(COMMITTED_PROPOSAL, 'utf8'));
  const ignored = JSON.parse(readFileSync(IGNORED_PROPOSAL, 'utf8'));
  const equal = JSON.stringify(committed) === JSON.stringify(ignored);
  const cpi = committed.proposed_integration || {};
  const ipi = ignored.proposed_integration || {};
  return {
    equal_json: equal,
    committed_applied: committed.applied,
    ignored_applied: ignored.applied,
    pattern_match: cpi.pattern === ipi.pattern && cpi.pattern === 'B_RESPONSE_FIRST_THEN_TELEGRAM',
    credential_match: cpi.credential?.id === ipi.credential?.id && cpi.credential?.id === TG_CRED_ID,
    chat_match:
      Number(cpi.chat_target?.chat_id) === expectedChatId &&
      Number(ipi.chat_target?.chat_id) === expectedChatId,
    type_match:
      cpi.telegram_node?.type === 'n8n-nodes-base.telegram' &&
      ipi.telegram_node?.type === 'n8n-nodes-base.telegram',
    typeVersion_match:
      Number(cpi.telegram_node?.typeVersion_proposed) === 1.2 &&
      Number(ipi.telegram_node?.typeVersion_proposed) === 1.2,
    semantics_match:
      cpi.integration_semantics?.pattern_b_continuation_after_respond === 'PATTERN_B_CONFIRMED' &&
      ipi.integration_semantics?.pattern_b_continuation_after_respond === 'PATTERN_B_CONFIRMED',
    no_token_committed: !/\b\d{6,}:[A-Za-z0-9_-]{20,}\b/.test(JSON.stringify(committed)),
    no_token_ignored: !/\b\d{6,}:[A-Za-z0-9_-]{20,}\b/.test(JSON.stringify(ignored)),
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
      site_name: 'ZPM-SANDBOX-C1',
      domain: 'bzpm.ru',
    },
    producer: {
      name: PRODUCER_NAME,
      version: '1b-c1.1',
    },
    run: {
      run_id: `c1-sandbox-${eventId.slice(0, 8)}`,
      source_status: 'NO_ACTION_REQUIRED',
      normalized_status: 'OK',
      summary_code: 'NO_ACTION_REQUIRED',
      reason_codes: ['SANDBOX_TELEGRAM_C1'],
    },
    action: {
      required: false,
      code: 'NONE',
      text: 'Тестовая проверка канала уведомлений',
    },
    metrics: {
      baseline_count: 0,
      current_count: 0,
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

async function postOnce(webhookUrl, secret, body) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);
  const started = Date.now();
  try {
    const response = await fetch(webhookUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        [AUTH_HEADER]: secret,
      },
      body: JSON.stringify(body),
      redirect: 'error',
      signal: controller.signal,
    });
    const text = await response.text();
    let fields = null;
    try {
      const parsed = JSON.parse(text);
      fields = {
        ok: parsed.ok,
        result: parsed.result,
        event_id: parsed.event_id,
        dedupe: parsed.dedupe,
        code: parsed.code,
      };
    } catch {
      fields = null;
    }
    return {
      http_status: response.status,
      elapsed_ms: Date.now() - started,
      fields,
      body_redacted: redactText(text, secret),
    };
  } catch (err) {
    return {
      http_status: 0,
      elapsed_ms: Date.now() - started,
      fields: null,
      body_redacted: redactText(err instanceof Error ? err.message : String(err), secret),
      transport_error: true,
    };
  } finally {
    clearTimeout(timer);
  }
}

function writeRepoEvidenceFiles(files) {
  ensureDir(REPO_EVIDENCE);
  for (const [name, content] of Object.entries(files)) {
    const path = resolve(REPO_EVIDENCE, name);
    if (typeof content === 'string') writeFileSync(path, content.endsWith('\n') ? content : `${content}\n`, 'utf8');
    else writeJson(path, content);
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const report = {
    runner: 'run-client-ops-telegram-sandbox-controlled-apply',
    mode: args.rollback ? 'ROLLBACK' : args.apply ? 'APPLY' : 'DRY_RUN',
    workflow_id: ALLOWED_WORKFLOW_ID,
    workflow_name: ALLOWED_WORKFLOW_NAME,
    put_count: 0,
    rollback_put_count: 0,
    activation_changes: 0,
    webhook_calls: 0,
    telegram_messages_attempted: 0,
    telegram_messages_delivered: 0,
    telegram_direct_api_calls: 0,
    executions_added: 0,
    secret_printed: false,
    full_url_exposed: false,
    rollback_triggered: false,
  };

  ensureDir(ROLLBACK_DIR);
  ensureDir(LOCAL_EVIDENCE);
  ensureDir(dirname(LOCAL_PUT_PATH));
  ensureDir(REPO_EVIDENCE);

  const target = loadEnvKey(TG_TARGET_PATH, 'TELEGRAM_CHAT_ID');
  const targetType = loadEnvKey(TG_TARGET_PATH, 'TELEGRAM_CHAT_TYPE');
  const tgSecret = loadEnvKey(TG_SECRET_PATH, 'TELEGRAM_BOT_TOKEN');
  const whSecret = loadEnvKey(SECRET_PATH, 'CLIENT_OPS_WEBHOOK_AUTH_SECRET');
  const expectedChatId = target.ok ? Number(target.value) : NaN;
  report.local_boundaries = {
    header_auth_secret: { exists: whSecret.ok || whSecret.error !== 'file_missing', length_class: whSecret.lengthClass || whSecret.error, printed: false },
    telegram_secret: { exists: tgSecret.ok || tgSecret.error !== 'file_missing', length_class: tgSecret.lengthClass || tgSecret.error, printed: false },
    telegram_target: {
      exists: target.ok,
      chat_id_present: target.ok && Number.isFinite(expectedChatId),
      chat_type: targetType.ok ? targetType.value : null,
      printed: false,
    },
  };
  if (!target.ok || !Number.isFinite(expectedChatId) || (targetType.ok && targetType.value !== 'private')) {
    report.aborted = 'telegram_target_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }
  // Cross-check committed proposal target without hardcoding the numeric literal in source.
  const committedChat = Number(
    JSON.parse(readFileSync(COMMITTED_PROPOSAL, 'utf8')).proposed_integration?.chat_target?.chat_id,
  );
  if (expectedChatId !== committedChat) {
    report.aborted = 'telegram_target_diverges_from_committed_proposal';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  const proposalCompare = compareProposals(expectedChatId);
  report.proposal_compare = proposalCompare;
  if (!proposalCompare.equal_json || !proposalCompare.pattern_match || !proposalCompare.credential_match || !proposalCompare.chat_match) {
    report.aborted = 'proposal_conflict';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }
  if (!tgSecret.ok) {
    report.aborted = `telegram_secret_${tgSecret.error}`;
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }
  if (!whSecret.ok || whSecret.value.length < 32) {
    report.aborted = `webhook_secret_${whSecret.error || 'too_short'}`;
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
  const listRows = Array.isArray(listed) ? listed : listed?.data || [];
  const exact = listRows.filter((w) => w.name === ALLOWED_WORKFLOW_NAME);
  const tempSem = listRows.filter((w) => w.name === TEMP_SEMANTICS_NAME);
  const live = await getWorkflow(ALLOWED_WORKFLOW_ID, readCreds);
  const execPre = await executionSnapshot(readCreds, ALLOWED_WORKFLOW_ID);
  const credsMeta = await listCredentialsMeta(readCreds);
  const whCreds = credsMeta.filter((c) => c.name === AUTH_CRED_NAME);
  const tgCreds = credsMeta.filter((c) => c.name === TG_CRED_NAME);
  const pre = structuralState(live, execPre);
  pre.exact_name_count = exact.length;
  pre.temp_semantics_count = tempSem.length;
  pre.webhook_cred_exact_count = whCreds.length;
  pre.telegram_cred_exact_count = tgCreds.length;
  pre.webhook_cred_id = whCreds[0]?.id || null;
  pre.telegram_cred_id = tgCreds[0]?.id || null;
  pre.webhook_cred_type = whCreds[0]?.type || null;
  pre.telegram_cred_type = tgCreds[0]?.type || null;
  pre.webhook_cred_data_visible = Boolean(whCreds[0]?.data && Object.keys(whCreds[0].data).length);
  pre.telegram_cred_data_visible = Boolean(tgCreds[0]?.data && Object.keys(tgCreds[0].data).length);
  report.pre_state = pre;

  // Post-C1 dry-run / reapply guard: Telegram already present → block before strict pre-C1 gates.
  const telegramAlready = (live.nodes || []).some((n) => String(n.type).includes('telegram'));
  if (telegramAlready && !args.apply && !args.rollback) {
    report.pre_state_ok = false;
    report.dry_run_gates = {
      pre_state_ok: false,
      proposals_equal: proposalCompare.equal_json,
      put_composed: false,
      remains_inactive: live.active === false,
      telegram_delta_one: false,
      pattern_b: (live.connections || {})['Respond Accepted']?.main?.[0]?.[0]?.node === TELEGRAM_NODE_NAME,
      rollback_snapshot_written: existsSync(resolve(ROLLBACK_DIR, 'SANITIZED-MANIFEST.json')),
      reapply_blocked: true,
      final_inactive: live.active === false,
      telegram_nodes: pre.telegram_nodes,
      executions: pre.executions,
    };
    report.dry_run_verdict = 'BLOCKED_REAPPLY';
    report.replay_guard =
      'Telegram node already present on real Client Ops workflow; reapply blocked.';
    report.final_state = pre;
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  const preOk =
    exact.length === 1 &&
    live.id === ALLOWED_WORKFLOW_ID &&
    live.active === false &&
    pre.nodes === EXPECTED_NODES_PRE &&
    pre.executions === EXPECTED_EXEC_PRE &&
    pre.running === 0 &&
    pre.versionId === EXPECTED_VERSION_PRE &&
    pre.webhook_authentication === 'headerAuth' &&
    pre.auth_credential?.id === AUTH_CRED_ID &&
    pre.telegram_nodes === 0 &&
    pre.http_request_nodes === 0 &&
    tempSem.length === 0 &&
    whCreds.length === 1 &&
    whCreds[0].id === AUTH_CRED_ID &&
    whCreds[0].type === 'httpHeaderAuth' &&
    tgCreds.length === 1 &&
    tgCreds[0].id === TG_CRED_ID &&
    tgCreds[0].type === 'telegramApi' &&
    !pre.webhook_cred_data_visible &&
    !pre.telegram_cred_data_visible;

  report.pre_state_ok = preOk;
  if (!preOk && !args.rollback) {
    report.aborted = 'pre_state_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  // Rollback path
  if (args.rollback) {
    if (args.confirmRollback !== ROLLBACK_CONFIRM) {
      report.aborted = 'rollback_confirmation_mismatch';
      console.log(JSON.stringify(report, null, 2));
      process.exitCode = 2;
      return;
    }
    const rollbackRawPath = resolve(ROLLBACK_DIR, 'workflow-rollback.raw.json');
    if (!existsSync(rollbackRawPath)) {
      report.aborted = 'rollback_snapshot_missing';
      console.log(JSON.stringify(report, null, 2));
      process.exitCode = 2;
      return;
    }
    const snap = JSON.parse(readFileSync(rollbackRawPath, 'utf8'));
    const put = prepareWorkflowPutPayload(snap);
    const updateCreds = loadUpdateCredentials();
    await updateAllowlistedWorkflow(put, updateCreds);
    report.rollback_put_count = 1;
    report.rollback_triggered = true;
    const after = await getWorkflow(ALLOWED_WORKFLOW_ID, readCreds);
    const execAfter = await executionSnapshot(readCreds, ALLOWED_WORKFLOW_ID);
    report.post_rollback_state = structuralState(after, execAfter);
    if (after.active) {
      const actCreds = loadActivationCredentials();
      await deactivateAllowlistedWorkflow(actCreds, C1_DEACTIVATION_CONFIRM_PHRASE);
      report.activation_changes += 1;
    }
    console.log(JSON.stringify(report, null, 2));
    return;
  }

  // Save rollback snapshot (sanitized manifest + raw put-ready clone without secrets)
  const rollbackPayload = prepareWorkflowPutPayload(live);
  writeJson(resolve(ROLLBACK_DIR, 'workflow-rollback.raw.json'), {
    name: live.name,
    nodes: live.nodes,
    connections: live.connections,
    settings: live.settings,
    id: live.id,
    versionId: live.versionId,
    active: live.active,
  });
  writeJson(resolve(ROLLBACK_DIR, 'SANITIZED-MANIFEST.json'), {
    workflow_id: ALLOWED_WORKFLOW_ID,
    workflow_name: ALLOWED_WORKFLOW_NAME,
    versionId: live.versionId,
    active: live.active,
    nodes: EXPECTED_NODES_PRE,
    executions: EXPECTED_EXEC_PRE,
    fingerprint_sha16: pre.fingerprint_sha16,
    auth_credential_id: AUTH_CRED_ID,
    telegram_nodes: 0,
    created_at: new Date().toISOString(),
  });
  writeJson(resolve(ROLLBACK_DIR, 'pre-state-fingerprint.json'), {
    versionId: live.versionId,
    fingerprint_sha16: pre.fingerprint_sha16,
    fingerprint: pre.fingerprint,
    connection_keys: Object.keys(live.connections || {}),
  });

  const composed = composePutFromLive(live, expectedChatId);
  if (!composed.ok) {
    // After successful C1 apply, dry-run must block reapply.
    if (composed.error === 'telegram_already_present') {
      report.dry_run_gates = {
        pre_state_ok: false,
        proposals_equal: proposalCompare.equal_json,
        put_composed: false,
        remains_inactive: live.active === false,
        telegram_delta_one: false,
        pattern_b: (live.connections || {})['Respond Accepted']?.main?.[0]?.[0]?.node === TELEGRAM_NODE_NAME,
        rollback_snapshot_written: existsSync(resolve(ROLLBACK_DIR, 'SANITIZED-MANIFEST.json')),
        reapply_blocked: true,
      };
      report.dry_run_verdict = 'BLOCKED_REAPPLY';
      report.replay_guard = 'Telegram node already present on real Client Ops workflow; reapply blocked.';
      report.final_state = pre;
      console.log(JSON.stringify(report, null, 2));
      process.exitCode = 2;
      return;
    }
    report.aborted = composed.error;
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }
  writeJson(LOCAL_PUT_PATH, composed.bundle);
  report.composed_put_path = 'local/client-ops-reporting-bridge/bzpm.ru/apply/mars-client-ops-bridge-bzpm.telegram-sandbox.put-payload.json';
  report.composed_node_count = composed.bundle.put_payload.nodes.length;
  report.dry_run_gates = {
    pre_state_ok: preOk,
    proposals_equal: proposalCompare.equal_json,
    put_composed: true,
    remains_inactive: true,
    telegram_delta_one: composed.bundle.put_payload.nodes.length === 10,
    pattern_b: true,
    rollback_snapshot_written: true,
    reapply_blocked: false,
  };

  if (!args.apply) {
    // Reapply guard preview: if telegram already present, block
    report.dry_run_verdict = 'READY';
    report.confirmation_phrases = {
      apply: APPLY_CONFIRM,
      activate: C1_ACTIVATION_CONFIRM_PHRASE,
      post: POST_CONFIRM,
      deactivate: C1_DEACTIVATION_CONFIRM_PHRASE,
      rollback: ROLLBACK_CONFIRM,
    };
    console.log(JSON.stringify(report, null, 2));
    return;
  }

  if (args.confirmApply !== APPLY_CONFIRM) {
    report.aborted = 'apply_confirmation_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }
  if (args.confirmActivate !== C1_ACTIVATION_CONFIRM_PHRASE) {
    report.aborted = 'activate_confirmation_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }
  if (args.confirmPost !== POST_CONFIRM) {
    report.aborted = 'post_confirmation_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }
  if (args.confirmDeactivate !== C1_DEACTIVATION_CONFIRM_PHRASE) {
    report.aborted = 'deactivate_confirmation_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  const updateCreds = loadUpdateCredentials();
  const putResult = await updateAllowlistedWorkflow(composed.bundle.put_payload, updateCreds);
  report.put_count = 1;
  report.put_versionId = putResult?.versionId || null;

  const postPut = await getWorkflow(ALLOWED_WORKFLOW_ID, readCreds);
  const execPostPut = await executionSnapshot(readCreds, ALLOWED_WORKFLOW_ID);
  const postPutState = structuralState(postPut, execPostPut);
  report.post_put_state = postPutState;

  const structuralOk =
    postPutState.active === false &&
    postPutState.nodes === 10 &&
    postPutState.telegram_nodes === 1 &&
    postPutState.telegram_credential?.id === TG_CRED_ID &&
    postPutState.telegram_chat_id === String(expectedChatId) &&
    postPutState.pattern_b_connection === TELEGRAM_NODE_NAME &&
    postPutState.rejected_reaches_telegram === false &&
    postPutState.webhook_authentication === 'headerAuth' &&
    postPutState.auth_credential?.id === AUTH_CRED_ID &&
    postPutState.executions === EXPECTED_EXEC_PRE &&
    postPutState.running === 0 &&
    postPutState.versionId &&
    postPutState.versionId !== EXPECTED_VERSION_PRE &&
    postPutState.http_request_nodes === 0;

  report.structural_ok = structuralOk;

  if (!structuralOk) {
    report.rollback_triggered = true;
    const snap = JSON.parse(readFileSync(resolve(ROLLBACK_DIR, 'workflow-rollback.raw.json'), 'utf8'));
    await updateAllowlistedWorkflow(prepareWorkflowPutPayload(snap), updateCreds);
    report.rollback_put_count = 1;
    const afterRb = await getWorkflow(ALLOWED_WORKFLOW_ID, readCreds);
    report.post_rollback_state = structuralState(
      afterRb,
      await executionSnapshot(readCreds, ALLOWED_WORKFLOW_ID),
    );
    report.aborted = 'structural_verification_failed_rolled_back';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  const actCreds = loadActivationCredentials();
  let activated = false;
  let emergencyDeactivate = false;
  const eventId = randomUUID();
  report.synthetic_event_id = eventId;

  try {
    await activateAllowlistedWorkflow(actCreds, C1_ACTIVATION_CONFIRM_PHRASE);
    report.activation_changes += 1;
    activated = true;
    const mid = await getWorkflow(ALLOWED_WORKFLOW_ID, readCreds);
    report.active_confirmed = mid.active === true;
    if (mid.active !== true) throw new Error('activation_not_confirmed');

    const knownIds = new Set((execPostPut.rows || []).map((r) => r.id));
    const webhookPath = (mid.nodes || []).find((n) => n.type === 'n8n-nodes-base.webhook')?.parameters?.path;
    if (!webhookPath) throw new Error('webhook_path_missing');
    const webhookUrl = `${normalizeBaseUrl(actCreds.apiUrl)}/webhook/${webhookPath}`;

    const envelope = buildSyntheticEnvelope(eventId);
    const startedAtMs = Date.now();
    const postResult = await postOnce(webhookUrl, whSecret.value, envelope);
    report.webhook_calls = 1;
    report.telegram_messages_attempted = 1;
    report.post_result = {
      http_status: postResult.http_status,
      elapsed_ms: postResult.elapsed_ms,
      fields: postResult.fields,
      body_redacted: postResult.body_redacted,
      production_data_used: false,
      secret_exposed: false,
      url_exposed: false,
    };

    const waited = await waitForNewExecution(readCreds, ALLOWED_WORKFLOW_ID, knownIds, startedAtMs);
    report.correlated_execution_id = waited.execution?.id || null;
    if (!waited.execution) throw new Error('execution_not_correlated');

    const detail = await getExecutionDetail(readCreds, waited.execution.id);
    if (!detail.ok) throw new Error(`execution_detail_http_${detail.status}`);
    const inspected = inspectExecutionSanitized(detail.data);
    report.execution_inspect = {
      execution_id: waited.execution.id,
      status: inspected.execution_status,
      finished: inspected.finished,
      node_order: inspected.node_order,
      respond_before_telegram: inspected.respond_before_telegram,
      telegram_node_runs: inspected.telegram_node_runs,
      telegram_ok_signal: inspected.telegram_ok_signal,
      telegram_message_id_present: inspected.telegram_message_id_present,
      telegram_message_id: inspected.telegram_message_id,
      telegram_chat_id: inspected.telegram_chat_id,
    };
    report.executions_added = 1;
    if (
      inspected.telegram_node_runs === 1 &&
      inspected.telegram_ok_signal &&
      inspected.respond_before_telegram &&
      inspected.telegram_chat_id === expectedChatId
    ) {
      report.telegram_messages_delivered = 1;
    } else if (inspected.telegram_node_runs > 1) {
      report.delivery_ambiguous_or_duplicate = true;
    } else {
      report.delivery_failed_or_ambiguous = true;
    }
  } catch (err) {
    report.live_error = redactText(err instanceof Error ? err.message : String(err), whSecret.value);
  } finally {
    try {
      await deactivateAllowlistedWorkflow(actCreds, C1_DEACTIVATION_CONFIRM_PHRASE);
      report.activation_changes += 1;
      activated = false;
    } catch (deactErr) {
      report.deactivation_error = redactText(
        deactErr instanceof Error ? deactErr.message : String(deactErr),
        whSecret.value,
      );
    }
    let finalWf = await getWorkflow(ALLOWED_WORKFLOW_ID, readCreds);
    if (finalWf.active === true) {
      try {
        await deactivateAllowlistedWorkflow(actCreds, C1_DEACTIVATION_CONFIRM_PHRASE);
        report.activation_changes += 1;
        emergencyDeactivate = true;
        finalWf = await getWorkflow(ALLOWED_WORKFLOW_ID, readCreds);
      } catch (e2) {
        report.emergency_deactivation_error = redactText(
          e2 instanceof Error ? e2.message : String(e2),
          whSecret.value,
        );
      }
    }
    const execFinal = await executionSnapshot(readCreds, ALLOWED_WORKFLOW_ID);
    report.emergency_deactivate = emergencyDeactivate;
    report.final_state = structuralState(finalWf, execFinal);
    report.containment = {
      final_active: finalWf.active === false,
      running: report.final_state.running === 0,
      executions: report.final_state.executions,
      expected_executions: EXPECTED_EXEC_PRE + (report.executions_added || 0),
    };
  }

  // Mark local put bundle applied flag for operators (ignored path)
  try {
    const localBundle = JSON.parse(readFileSync(LOCAL_PUT_PATH, 'utf8'));
    localBundle.applied = report.put_count === 1 && !report.rollback_triggered;
    localBundle.applied_at = new Date().toISOString();
    localBundle.post_put_versionId = report.post_put_state?.versionId || null;
    writeJson(LOCAL_PUT_PATH, localBundle);
  } catch {
    // ignore
  }

  report.verdict =
    report.final_state?.active === false &&
    report.structural_ok &&
    report.webhook_calls === 1 &&
    report.executions_added === 1 &&
    report.telegram_messages_delivered === 1 &&
    report.telegram_messages_attempted === 1 &&
    report.post_result?.http_status === 202 &&
    report.post_result?.fields?.result === 'ACCEPTED' &&
    !report.rollback_triggered &&
    report.containment?.final_active
      ? 'COMPLETE'
      : 'PARTIAL';

  writeJson(resolve(LOCAL_EVIDENCE, 'RUNNER-REPORT.sanitized.json'), report);
  console.log(JSON.stringify(report, null, 2));
  if (report.verdict !== 'COMPLETE') process.exitCode = 2;
}

main().catch((err) => {
  console.log(
    JSON.stringify(
      {
        runner: 'run-client-ops-telegram-sandbox-controlled-apply',
        aborted: 'unhandled',
        error: String(err instanceof Error ? err.message : err).slice(0, 300),
      },
      null,
      2,
    ),
  );
  process.exitCode = 2;
});
