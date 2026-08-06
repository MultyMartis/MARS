/**
 * Client Ops greenfield inactive sandbox create runner.
 *
 * Default: dry-run.
 * Live create requires:
 *   --apply
 *   --confirm="CREATE INACTIVE MARS CLIENT OPS BRIDGE BZPM"
 *
 * Creates exactly one inactive workflow. Never activates. Never calls webhook.
 * Uses separate write-capable client; re-GETs via GET-only exporter client.
 */

import { mkdirSync, readFileSync, writeFileSync, existsSync } from 'node:fs';
import { dirname, resolve, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  AUTH_PLACEHOLDER,
  WORKFLOW_NAME,
} from '../harness/client-ops-validator.mjs';
import {
  loadCredentials,
  listWorkflows,
  getWorkflow,
  normalizeBaseUrl,
} from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';
import { sanitizeWorkflow } from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/sanitize-workflow.mjs';
import {
  createWorkflow,
  loadWriteCredentials,
} from './lib/client-ops-n8n-write-client.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const DEFAULT_PAYLOAD = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/apply/mars-client-ops-bridge-bzpm.create-payload.json',
);
const LOCAL_EVIDENCE = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/evidence',
);
const EXPECTED_HOST = 'n8n.ai-metacode.com';
const CONFIRM_PHRASE = 'CREATE INACTIVE MARS CLIENT OPS BRIDGE BZPM';
const AUTH_MODE = 'AUTH_BLOCKED_INACTIVE_ONLY';

const FORBIDDEN_TYPES = new Set([
  'n8n-nodes-base.telegram',
  'n8n-nodes-base.telegramTrigger',
  'n8n-nodes-base.httpRequest',
  'n8n-nodes-base.googleSheets',
]);

const ALLOWED_TYPES = new Map([
  ['n8n-nodes-base.webhook', new Set([2.1])],
  ['n8n-nodes-base.code', new Set([2])],
  ['n8n-nodes-base.if', new Set([2.3])],
  ['n8n-nodes-base.respondToWebhook', new Set([1.1])],
]);

function parseArgs(argv) {
  const args = {
    apply: false,
    confirm: null,
    payload: DEFAULT_PAYLOAD,
  };
  for (const a of argv) {
    if (a === '--apply') args.apply = true;
    else if (a.startsWith('--confirm=')) args.confirm = a.slice('--confirm='.length);
    else if (a.startsWith('--payload=')) args.payload = resolve(a.slice('--payload='.length));
  }
  return args;
}

function assertCreateCandidate(createPayload, authMode) {
  const errors = [];
  if (authMode !== AUTH_MODE) {
    errors.push(`auth_mode must be ${AUTH_MODE}`);
  }
  if (createPayload.name !== WORKFLOW_NAME) {
    errors.push(`workflow name must be exactly ${WORKFLOW_NAME}`);
  }
  if ('active' in createPayload && createPayload.active !== false) {
    errors.push('create payload must not request active workflow');
  }
  if (createPayload.id) errors.push('create payload must not include workflow id');
  if ('active' in createPayload && createPayload.active === true) {
    errors.push('active=true rejected');
  }

  const blob = JSON.stringify(createPayload);
  if (blob.includes(AUTH_PLACEHOLDER) === false) {
    errors.push('blocked mode requires unresolved auth placeholder');
  }
  if (/HITL_REQUIRED/.test(blob) === false) {
    errors.push('blocked marker missing');
  }

  // Reject real-looking secrets outside placeholder
  const stripped = blob.split(AUTH_PLACEHOLDER).join('');
  if (/\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/.test(stripped)) {
    errors.push('telegram-like token in payload');
  }
  if (/Bearer\s+(?!SYNTHETIC_|REDACTED|<<<)[A-Za-z0-9._-]{20,}/i.test(stripped)) {
    errors.push('bearer-like secret in payload');
  }
  if (/https?:\/\//i.test(blob)) errors.push('absolute URL in create payload');

  for (const node of createPayload.nodes || []) {
    if (node.webhookId) errors.push(`webhookId on ${node.name}`);
    if (node.credentials) errors.push(`credentials on ${node.name}`);
    if (FORBIDDEN_TYPES.has(node.type)) {
      errors.push(`forbidden type ${node.type} on ${node.name}`);
    }
    const allowed = ALLOWED_TYPES.get(node.type);
    if (!allowed || !allowed.has(node.typeVersion)) {
      errors.push(`unauthorized type/version ${node.type}@${node.typeVersion}`);
    }
  }

  return errors;
}

function nodeMatrix(wf) {
  return (wf.nodes || []).map((n) => ({
    name: n.name,
    type: n.type,
    typeVersion: n.typeVersion,
    disabled: Boolean(n.disabled),
    has_credentials: Boolean(n.credentials),
    has_webhookId: Boolean(n.webhookId),
  }));
}

function structuralDiff(expectedCreate, liveWf) {
  const expectedNodes = (expectedCreate.nodes || []).map((n) => ({
    name: n.name,
    type: n.type,
    typeVersion: n.typeVersion,
    disabled: Boolean(n.disabled),
  }));
  const liveNodes = (liveWf.nodes || []).map((n) => ({
    name: n.name,
    type: n.type,
    typeVersion: n.typeVersion,
    disabled: Boolean(n.disabled),
  }));

  const unexpected = [];
  if (liveWf.name !== expectedCreate.name) {
    unexpected.push({ area: 'name', expected: expectedCreate.name, live: liveWf.name });
  }
  if (liveWf.active !== false) {
    unexpected.push({ area: 'active', expected: false, live: liveWf.active });
  }
  if (JSON.stringify(expectedNodes) !== JSON.stringify(liveNodes)) {
    unexpected.push({
      area: 'node_matrix',
      expected: expectedNodes,
      live: liveNodes,
    });
  }
  const expConn = JSON.stringify(expectedCreate.connections || {});
  const liveConn = JSON.stringify(liveWf.connections || {});
  if (expConn !== liveConn) {
    unexpected.push({ area: 'connections', state: 'DIFF' });
  }

  const serverManaged = {
    id: liveWf.id ?? null,
    versionId: liveWf.versionId ?? null,
    createdAt: liveWf.createdAt ?? null,
    updatedAt: liveWf.updatedAt ?? null,
    webhookIds_present: (liveWf.nodes || []).some((n) => Boolean(n.webhookId)),
    meta_present: Boolean(liveWf.meta),
  };

  return {
    client_managed_match: unexpected.length === 0,
    unexpected_differences: unexpected,
    server_managed_fields: serverManaged,
  };
}

async function maybeExecutionCount(creds, workflowId) {
  try {
    const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions?workflowId=${encodeURIComponent(workflowId)}&limit=1`;
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        Accept: 'application/json',
        'X-N8N-API-KEY': creds.apiKey,
      },
    });
    if (!response.ok) {
      return { observable: false, reason: `HTTP_${response.status}` };
    }
    const data = await response.json();
    const rows = Array.isArray(data) ? data : data?.data;
    if (!Array.isArray(rows)) {
      return { observable: false, reason: 'unexpected_shape' };
    }
    // If API returns only a page, treat count==0 as strong signal; otherwise report page length.
    const count = typeof data?.count === 'number' ? data.count : rows.length;
    return { observable: true, execution_count_observed: count };
  } catch {
    return { observable: false, reason: 'request_failed' };
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!existsSync(args.payload)) {
    throw new Error(`Missing apply payload: ${args.payload}`);
  }
  const bundle = JSON.parse(readFileSync(args.payload, 'utf8'));
  const createPayload = bundle.create_payload;
  const authMode = bundle.auth_mode;
  const errors = assertCreateCandidate(createPayload, authMode);

  const report = {
    runner: 'run-client-ops-greenfield-create',
    mode: args.apply ? 'APPLY' : 'DRY_RUN',
    workflow_name: WORKFLOW_NAME,
    auth_mode: authMode,
    confirmation_phrase_required: CONFIRM_PHRASE,
    validation_errors: errors,
    network: false,
    executed_create: false,
    activated: false,
    webhook_calls: 0,
    created_count: 0,
  };

  if (errors.length) {
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  const readCreds = loadCredentials();
  const host = new URL(readCreds.apiUrl).host;
  if (host !== EXPECTED_HOST) {
    report.validation_errors = [`unexpected API host ${host}; expected ${EXPECTED_HOST}`];
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }
  report.api_host = host;

  // Pre-create collision check
  const listed = await listWorkflows(readCreds);
  const exact = listed.filter((w) => w.name === WORKFLOW_NAME);
  report.pre_create_exact_name_count = exact.length;
  if (exact.length > 0) {
    report.aborted = 'NAME_COLLISION';
    report.exact_hits_sanitized = exact.map((w) => ({
      id: w.id,
      active: w.active,
      name: w.name,
    }));
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  if (!args.apply) {
    report.create_payload_prepared = true;
    report.node_count = createPayload.nodes.length;
    report.note = 'Dry-run only. Pass --apply and exact confirmation phrase to create.';
    console.log(JSON.stringify(report, null, 2));
    return;
  }

  if (args.confirm !== CONFIRM_PHRASE) {
    report.aborted = 'confirmation_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  // Live create
  report.network = true;
  const writeCreds = loadWriteCredentials();
  const writeHost = new URL(writeCreds.apiUrl).host;
  if (writeHost !== EXPECTED_HOST) {
    throw new Error(`Write client host mismatch: ${writeHost}`);
  }

  const created = await createWorkflow(createPayload, writeCreds);
  if (!created || typeof created !== 'object' || !created.id) {
    report.aborted = 'malformed_create_response';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 4;
    return;
  }

  report.executed_create = true;
  report.created_count = 1;
  report.workflow_id = created.id;
  report.active_from_create = created.active;

  if (created.active === true) {
    report.aborted = 'CREATED_ACTIVE_UNEXPECTED';
    report.activation_count = 1;
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 5;
    return;
  }
  report.activation_count = 0;

  // Immediate re-GET via GET-only client
  const live = await getWorkflow(String(created.id), readCreds);
  const { sanitized: sanitizedLive } = sanitizeWorkflow(live);
  const diff = structuralDiff(createPayload, live);
  const execInfo = await maybeExecutionCount(readCreds, String(created.id));

  report.readback = {
    name: live.name,
    active: live.active,
    node_count: Array.isArray(live.nodes) ? live.nodes.length : 0,
    node_matrix: nodeMatrix(live),
    settings: live.settings || null,
    credential_reference: (live.nodes || []).some((n) => Boolean(n.credentials)),
    placeholder_still_present: JSON.stringify(live).includes(AUTH_PLACEHOLDER),
    telegram_present: (live.nodes || []).some((n) =>
      String(n.type || '').includes('telegram'),
    ),
    external_nodes_present: (live.nodes || []).some((n) => FORBIDDEN_TYPES.has(n.type)),
  };
  report.structural_diff = diff;
  report.executions = execInfo;
  report.webhook_calls = 0;

  mkdirSync(LOCAL_EVIDENCE, { recursive: true });
  const createSanitized = {
    id: created.id,
    name: created.name,
    active: created.active,
    node_count: Array.isArray(created.nodes) ? created.nodes.length : null,
    auth_mode: AUTH_MODE,
  };
  // Structural sanitized summary only (avoid committing raw webhookId UUID keys).
  const sanitizedReadbackSummary = {
    id: live.id,
    name: live.name,
    active: live.active,
    isArchived: Boolean(live.isArchived),
    node_count: Array.isArray(live.nodes) ? live.nodes.length : 0,
    node_matrix: nodeMatrix(live).map((n) => ({
      ...n,
      webhookId_sanitized: n.has_webhookId ? 'REDACTED_WEBHOOK_ID' : null,
    })),
    connection_keys: Object.keys(live.connections || {}).sort(),
    settings: live.settings || null,
    auth_mode: AUTH_MODE,
    placeholder_marker_present: JSON.stringify(live).includes(AUTH_PLACEHOLDER),
    telegram_absent: !(live.nodes || []).some((n) =>
      String(n.type || '').includes('telegram'),
    ),
    credential_values_absent: !(live.nodes || []).some((n) => Boolean(n.credentials)),
    server_assigned_webhookId_on_inactive_create: (live.nodes || []).some((n) =>
      Boolean(n.webhookId),
    ),
    versionId: live.versionId || null,
    createdAt: live.createdAt || null,
    updatedAt: live.updatedAt || null,
    note: 'Structural sanitized read-back only. Server-assigned webhookId stored as REDACTED_WEBHOOK_ID marker; not a usable public URL.',
  };
  writeFileSync(
    join(LOCAL_EVIDENCE, 'SANITIZED-CREATE-RESULT.json'),
    JSON.stringify(createSanitized, null, 2),
    'utf8',
  );
  writeFileSync(
    join(LOCAL_EVIDENCE, 'SANITIZED-READBACK.json'),
    JSON.stringify(sanitizedReadbackSummary, null, 2),
    'utf8',
  );
  // Keep full sanitized workflow locally for operator review (gitignored local/).
  writeFileSync(
    join(LOCAL_EVIDENCE, 'SANITIZED-READBACK-FULL.local.json'),
    JSON.stringify(sanitizedLive, null, 2),
    'utf8',
  );
  writeFileSync(
    join(LOCAL_EVIDENCE, 'STRUCTURAL-DIFF.json'),
    JSON.stringify(diff, null, 2),
    'utf8',
  );
  writeFileSync(
    join(LOCAL_EVIDENCE, 'RUNNER-REPORT.json'),
    JSON.stringify(report, null, 2),
    'utf8',
  );

  const materialUnexpected = diff.unexpected_differences.filter(
    (d) => d.area !== 'connections' || true,
  );
  // connections may include server-normalized ordering; treat node matrix/name/active as material
  const hardUnexpected = diff.unexpected_differences.filter((d) =>
    ['name', 'active', 'node_matrix'].includes(d.area),
  );
  report.verification_ok = hardUnexpected.length === 0 && live.active === false;
  report.local_evidence_dir = LOCAL_EVIDENCE;

  console.log(JSON.stringify(report, null, 2));
  if (!report.verification_ok) process.exitCode = 6;
}

main().catch((err) => {
  console.error(err instanceof Error ? err.message : String(err));
  process.exitCode = 1;
});
