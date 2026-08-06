/**
 * Client Ops auth-binding PUT runner for inactive workflow tkM4H0G0gM3q9Foi.
 *
 * Default: dry-run.
 * Live PUT requires:
 *   --apply
 *   --confirm="BIND AUTH TO INACTIVE CLIENT OPS BRIDGE BZPM"
 *
 * Never activates. Never calls webhook. Never executes workflow.
 */

import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
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
  ALLOWED_WORKFLOW_ID,
  ALLOWED_WORKFLOW_NAME,
  loadUpdateCredentials,
  updateAllowlistedWorkflow,
} from './lib/client-ops-n8n-workflow-update-client.mjs';
import { AUTH_PLACEHOLDER } from '../harness/client-ops-validator.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const EXPECTED_HOST = 'n8n.ai-metacode.com';
const CONFIRM_PHRASE = 'BIND AUTH TO INACTIVE CLIENT OPS BRIDGE BZPM';
const AUTH_MODE = 'AUTH_NATIVE_HEADER_CREDENTIAL_BOUND';
const CREDENTIAL_NAME = 'MARS Client Ops Webhook Auth — bzpm.ru';
const CREDENTIAL_TYPE = 'httpHeaderAuth';
const DEFAULT_PAYLOAD = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/apply/mars-client-ops-bridge-bzpm.auth-binding.put-payload.json',
);
const ROLLBACK_DIR = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/rollback/phase-1b-b1',
);
const LOCAL_EVIDENCE = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/evidence/phase-1b-b1',
);

function parseArgs(argv) {
  const args = { apply: false, confirm: null, payload: DEFAULT_PAYLOAD };
  for (const a of argv) {
    if (a === '--apply') args.apply = true;
    else if (a.startsWith('--confirm=')) args.confirm = a.slice('--confirm='.length);
    else if (a.startsWith('--payload=')) args.payload = resolve(a.slice('--payload='.length));
  }
  return args;
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
    if (!response.ok) return { observable: false, reason: `HTTP_${response.status}` };
    const data = await response.json();
    const rows = Array.isArray(data) ? data : data?.data;
    if (!Array.isArray(rows)) return { observable: false, reason: 'unexpected_shape' };
    const count = typeof data?.count === 'number' ? data.count : rows.length;
    return { observable: true, execution_count_observed: count };
  } catch {
    return { observable: false, reason: 'request_failed' };
  }
}

function assertPutCandidate(bundle) {
  const errors = [];
  if (bundle.auth_mode !== AUTH_MODE) errors.push(`auth_mode must be ${AUTH_MODE}`);
  if (bundle.workflow_id !== ALLOWED_WORKFLOW_ID) errors.push('workflow_id mismatch');
  if (bundle.put_payload?.name !== ALLOWED_WORKFLOW_NAME) errors.push('name mismatch');
  if (bundle.active !== false) errors.push('bundle.active must be false');
  const blob = JSON.stringify(bundle.put_payload || {});
  if (blob.includes(AUTH_PLACEHOLDER) || blob.includes('HITL_REQUIRED:CLIENT_OPS_WEBHOOK_AUTH_SECRET')) {
    errors.push('auth placeholder still present');
  }
  if (/https?:\/\//i.test(blob)) errors.push('absolute URL in put payload');
  const webhook = (bundle.put_payload?.nodes || []).find(
    (n) => n.type === 'n8n-nodes-base.webhook',
  );
  if (!webhook) errors.push('webhook missing');
  if (webhook?.parameters?.authentication !== 'headerAuth') {
    errors.push('webhook authentication not headerAuth');
  }
  const href = webhook?.credentials?.[CREDENTIAL_TYPE];
  if (!href?.id || href.name !== CREDENTIAL_NAME) {
    errors.push('credential reference missing or mismatched');
  }
  for (const node of bundle.put_payload?.nodes || []) {
    if (node.webhookId) errors.push(`webhookId on put node ${node.name}`);
  }
  return errors;
}

function structuralAuthDiff(before, after, expectedCred) {
  const unexpected = [];
  if (after.name !== before.name) unexpected.push({ area: 'name' });
  if (after.active !== false) unexpected.push({ area: 'active', live: after.active });
  if ((after.nodes || []).length !== (before.nodes || []).length) {
    unexpected.push({ area: 'node_count' });
  }

  const beforeTypes = (before.nodes || []).map((n) => `${n.name}|${n.type}|${n.typeVersion}`);
  const afterTypes = (after.nodes || []).map((n) => `${n.name}|${n.type}|${n.typeVersion}`);
  if (JSON.stringify(beforeTypes) !== JSON.stringify(afterTypes)) {
    unexpected.push({ area: 'node_type_matrix' });
  }

  const beforeConn = JSON.stringify(before.connections || {});
  const afterConn = JSON.stringify(after.connections || {});
  if (beforeConn !== afterConn) unexpected.push({ area: 'connections' });

  const wh = (after.nodes || []).find((n) => n.type === 'n8n-nodes-base.webhook');
  if (wh?.parameters?.authentication !== 'headerAuth') {
    unexpected.push({ area: 'webhook_authentication' });
  }
  const href = wh?.credentials?.[CREDENTIAL_TYPE];
  if (!href || href.id !== expectedCred.id || href.name !== expectedCred.name) {
    unexpected.push({ area: 'credential_reference' });
  }

  const processNode = (after.nodes || []).find((n) => n.name === 'Process Client Ops Gates');
  const code = processNode?.parameters?.jsCode || '';
  if (code.includes(AUTH_PLACEHOLDER) || code.includes('HITL_REQUIRED:CLIENT_OPS_WEBHOOK_AUTH_SECRET')) {
    unexpected.push({ area: 'placeholder_still_present' });
  }
  if (!code.includes('NATIVE_HEADER_AUTH')) {
    unexpected.push({ area: 'native_marker_missing' });
  }

  const telegram = (after.nodes || []).some((n) => String(n.type).includes('telegram'));
  if (telegram) unexpected.push({ area: 'telegram_present' });

  return {
    unexpected_differences: unexpected,
    ok: unexpected.length === 0,
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const report = {
    runner: 'run-client-ops-auth-binding-put',
    mode: args.apply ? 'APPLY' : 'DRY_RUN',
    confirmation_phrase_required: CONFIRM_PHRASE,
    workflow_id: ALLOWED_WORKFLOW_ID,
    workflow_name: ALLOWED_WORKFLOW_NAME,
    auth_mode: AUTH_MODE,
    put_count: 0,
    activated: false,
    webhook_calls: 0,
    executed: false,
  };

  if (!existsSync(args.payload)) {
    report.aborted = 'missing_payload';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  const bundle = JSON.parse(readFileSync(args.payload, 'utf8'));
  const errors = assertPutCandidate(bundle);
  report.validation_errors = errors;
  if (errors.length) {
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
  const exact = listed.filter((w) => w.name === ALLOWED_WORKFLOW_NAME);
  report.exact_name_count = exact.length;
  if (exact.length !== 1 || exact[0].id !== ALLOWED_WORKFLOW_ID) {
    report.aborted = 'exact_name_drift';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  const liveBefore = await getWorkflow(ALLOWED_WORKFLOW_ID, readCreds);
  report.pre_put = {
    versionId: liveBefore.versionId || null,
    updatedAt: liveBefore.updatedAt || null,
    active: liveBefore.active,
    nodes: (liveBefore.nodes || []).length,
  };

  if (liveBefore.active !== false) {
    report.aborted = 'workflow_active';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  if (
    bundle.pre_put_versionId &&
    liveBefore.versionId &&
    bundle.pre_put_versionId !== liveBefore.versionId
  ) {
    report.aborted = 'versionId_drift';
    report.expected_versionId = bundle.pre_put_versionId;
    report.live_versionId = liveBefore.versionId;
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  // Save raw rollback snapshot (gitignored). Strip credential data values if any.
  mkdirSync(ROLLBACK_DIR, { recursive: true });
  const rollbackPath = resolve(ROLLBACK_DIR, 'pre-put-workflow.raw.json');
  const rollbackCopy = structuredClone(liveBefore);
  writeFileSync(rollbackPath, JSON.stringify(rollbackCopy, null, 2), 'utf8');
  report.rollback = {
    path: rollbackPath.replace(/\\/g, '/'),
    exists: true,
    workflow_id: ALLOWED_WORKFLOW_ID,
    versionId: liveBefore.versionId || null,
    updatedAt: liveBefore.updatedAt || null,
    active: liveBefore.active,
    secret_present: false,
    repository_inclusion: false,
  };

  if (!args.apply) {
    report.note = 'Dry-run only. Pass --apply and exact confirmation phrase to PUT.';
    console.log(JSON.stringify(report, null, 2));
    return;
  }

  if (args.confirm !== CONFIRM_PHRASE) {
    report.aborted = 'confirmation_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 3;
    return;
  }

  const writeCreds = loadUpdateCredentials();
  if (new URL(writeCreds.apiUrl).host !== EXPECTED_HOST) {
    throw new Error('Write client host mismatch');
  }

  let putResult;
  try {
    putResult = await updateAllowlistedWorkflow(bundle.put_payload, writeCreds);
    report.put_count = 1;
  } catch (err) {
    report.aborted = 'put_failed';
    report.error = err instanceof Error ? err.message.slice(0, 240) : 'put_failed';
    const liveAfterFail = await getWorkflow(ALLOWED_WORKFLOW_ID, readCreds);
    report.readback_after_fail = {
      active: liveAfterFail.active,
      versionId: liveAfterFail.versionId || null,
      updatedAt: liveAfterFail.updatedAt || null,
    };
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 4;
    return;
  }

  report.active_from_put_response = putResult?.active;
  if (putResult?.active === true) {
    report.aborted = 'BECAME_ACTIVE_UNEXPECTED';
    report.activation_count = 1;
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 5;
    return;
  }
  report.activation_count = 0;

  const liveAfter = await getWorkflow(ALLOWED_WORKFLOW_ID, readCreds);
  const { sanitized } = sanitizeWorkflow(liveAfter);
  const diff = structuralAuthDiff(liveBefore, liveAfter, bundle.credential_ref);
  const execInfo = await maybeExecutionCount(readCreds, ALLOWED_WORKFLOW_ID);

  const webhook = (liveAfter.nodes || []).find((n) => n.type === 'n8n-nodes-base.webhook');
  const processNode = (liveAfter.nodes || []).find((n) => n.name === 'Process Client Ops Gates');

  report.readback = {
    id: liveAfter.id,
    name: liveAfter.name,
    active: liveAfter.active,
    nodes: (liveAfter.nodes || []).length,
    versionId: liveAfter.versionId || null,
    updatedAt: liveAfter.updatedAt || null,
    webhook_authentication: webhook?.parameters?.authentication ?? null,
    credential_ref: webhook?.credentials?.[CREDENTIAL_TYPE]
      ? {
          id: webhook.credentials[CREDENTIAL_TYPE].id,
          name: webhook.credentials[CREDENTIAL_TYPE].name,
          type: CREDENTIAL_TYPE,
        }
      : null,
    credential_value_visible: false,
    placeholder_absent: !(processNode?.parameters?.jsCode || '').includes(AUTH_PLACEHOLDER),
    native_marker_present: String(processNode?.parameters?.jsCode || '').includes(
      'NATIVE_HEADER_AUTH',
    ),
    telegram_absent: !(liveAfter.nodes || []).some((n) => String(n.type).includes('telegram')),
    executions: execInfo,
  };
  report.structural_diff = diff;
  report.sanitized_workflow_available = Boolean(sanitized);

  mkdirSync(LOCAL_EVIDENCE, { recursive: true });
  writeFileSync(
    resolve(LOCAL_EVIDENCE, 'auth-binding-put-report.sanitized.json'),
    JSON.stringify(report, null, 2),
    'utf8',
  );
  writeFileSync(
    resolve(LOCAL_EVIDENCE, 'post-put-workflow.sanitized.json'),
    JSON.stringify(sanitized, null, 2),
    'utf8',
  );

  console.log(JSON.stringify(report, null, 2));
  if (!diff.ok || liveAfter.active !== false) {
    process.exitCode = 6;
  }
}

main().catch((err) => {
  console.error(
    JSON.stringify({
      runner: 'run-client-ops-auth-binding-put',
      aborted: 'uncaught',
      error: err instanceof Error ? err.message.slice(0, 240) : String(err).slice(0, 240),
    }),
  );
  process.exitCode = 1;
});
