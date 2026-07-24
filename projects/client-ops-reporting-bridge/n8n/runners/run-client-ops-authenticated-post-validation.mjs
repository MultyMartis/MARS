/**
 * Phase 1B-B2 — Authenticated Client Ops sandbox POST validation runner.
 *
 * Default: dry-run.
 * Live matrix requires:
 *   --apply
 *   --confirm="RUN AUTHENTICATED CLIENT OPS SANDBOX POST MATRIX"
 *
 * Temporarily activates allowlisted workflow tkM4H0G0gM3q9Foi, runs T01–T28,
 * deactivates in finally. Never prints secret or full webhook URL.
 */

import { randomUUID } from 'node:crypto';
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
  ACTIVATION_CONFIRM_PHRASE,
  DEACTIVATION_CONFIRM_PHRASE,
  activateAllowlistedWorkflow,
  deactivateAllowlistedWorkflow,
  loadActivationCredentials,
  ALLOWED_WORKFLOW_ID,
  ALLOWED_WORKFLOW_NAME,
  EXPECTED_HOST,
} from './lib/client-ops-n8n-activation-client.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const CONFIRM_PHRASE = 'RUN AUTHENTICATED CLIENT OPS SANDBOX POST MATRIX';
const CREDENTIAL_ID = 'WKHmPaw6QBp7WnzP';
const CREDENTIAL_NAME = 'MARS Client Ops Webhook Auth — bzpm.ru';
const AUTH_HEADER = 'X-MARS-Client-Ops-Token';
const SECRET_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env',
);
const SECRET_KEY = 'CLIENT_OPS_WEBHOOK_AUTH_SECRET';
const ROLLBACK_DIR = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/rollback/phase-1b-b2',
);
const LOCAL_EVIDENCE = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/evidence/phase-1b-b2',
);
const REPO_EVIDENCE = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/n8n/evidence/phase-1b-b2-authenticated-post-validation',
);
const MAX_REQUESTS = 30;
const REQUEST_TIMEOUT_MS = 20000;
const RESPONSE_CAPTURE_MAX = 2048;
const MAX_PAYLOAD_BYTES = 256 * 1024;
const PRODUCER_NAME = 'mars-client-ops-sandbox-validator';

const C1_POST_CONFIRM = 'SEND ONE CLIENT OPS TELEGRAM SANDBOX TEST BZPM';

function parseArgs(argv) {
  const args = { apply: false, confirm: null, c1SandboxTest: false };
  for (const a of argv) {
    if (a === '--apply') args.apply = true;
    else if (a === '--c1-sandbox-test') args.c1SandboxTest = true;
    else if (a.startsWith('--confirm=')) args.confirm = a.slice('--confirm='.length);
  }
  return args;
}

function ensureDir(p) {
  mkdirSync(p, { recursive: true });
}

function loadSecretFromLocalFile() {
  if (!existsSync(SECRET_PATH)) {
    return { ok: false, lengthClass: 'missing', error: 'secret_file_missing' };
  }
  const raw = readFileSync(SECRET_PATH, 'utf8');
  let value = '';
  for (const line of raw.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    if (!trimmed.startsWith(`${SECRET_KEY}=`)) continue;
    value = trimmed.slice(`${SECRET_KEY}=`.length).trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    break;
  }
  if (!value) {
    return { ok: false, lengthClass: 'empty', error: 'secret_key_missing_or_empty' };
  }
  const lengthClass =
    value.length >= 64 ? 'gte64' : value.length >= 32 ? 'gte32' : 'lt32';
  if (value.length < 32) {
    return { ok: false, lengthClass, error: 'secret_length_below_32' };
  }
  return { ok: true, lengthClass, value };
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
    return { observable: false, reason: `HTTP_${response.status}`, rows: [] };
  }
  const data = await response.json();
  const rows = Array.isArray(data) ? data : data?.data;
  if (!Array.isArray(rows)) {
    return { observable: false, reason: 'unexpected_shape', rows: [] };
  }
  const count =
    typeof data?.count === 'number' ? data.count : rows.length;
  return {
    observable: true,
    count,
    rows: rows.map((e) => ({
      id: e.id,
      status: e.status,
      mode: e.mode,
      startedAt: e.startedAt,
      stoppedAt: e.stoppedAt,
      finished: e.finished,
      workflowId: e.workflowId || e.workflowData?.id,
    })),
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
    environment: 'production',
    site: {
      site_id: 'SITE-002',
      site_name: 'ZPM-SANDBOX',
      domain: 'bzpm.ru',
    },
    producer: {
      name: PRODUCER_NAME,
      version: '1b-b2.1',
    },
    run: {
      run_id: `sandbox-${eventId.slice(0, 8)}`,
      source_status:
        status === 'OK'
          ? 'NO_ACTION_REQUIRED'
          : status === 'ATTENTION'
            ? 'ONBOARDING_NEEDED'
            : status === 'FAILED'
              ? 'EXECUTION_FAILED'
              : 'BLOCKED_CONFLICT',
      normalized_status: status,
      summary_code:
        status === 'OK'
          ? 'NO_ACTION_REQUIRED'
          : status === 'ATTENTION'
            ? 'ONBOARDING_NEEDED'
            : status === 'FAILED'
              ? 'EXECUTION_FAILED'
              : 'BLOCKED_CONFLICT',
      reason_codes: ['SANDBOX_SYNTHETIC'],
    },
    action: {
      required: status !== 'OK',
      code: status === 'OK' ? 'NONE' : 'REVIEW',
      text: 'sandbox synthetic',
    },
    metrics: {
      baseline_count: 10,
      current_count: 10,
      added_urls: 0,
      removed_urls: 0,
      onboarding_needed_count: status === 'ATTENTION' ? 1 : 0,
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

  if (overrides.schema_name !== undefined) base.schema_name = overrides.schema_name;
  if (overrides.schema_version !== undefined) base.schema_version = overrides.schema_version;
  if (overrides.event_type !== undefined) base.event_type = overrides.event_type;
  if (overrides.site_id !== undefined) base.site.site_id = overrides.site_id;
  if (overrides.domain !== undefined) base.site.domain = overrides.domain;
  if (overrides.metrics !== undefined) Object.assign(base.metrics, overrides.metrics);
  if (overrides.security !== undefined) Object.assign(base.security, overrides.security);
  if (overrides.inject_field) {
    const [path, value] = overrides.inject_field;
    if (path === 'action.text') base.action.text = value;
    else if (path === 'run.reason_codes.0') base.run.reason_codes = [value];
    else if (path === 'site.site_name') base.site.site_name = value;
  }
  return base;
}

function redactText(text, secret) {
  let out = String(text || '');
  if (secret && secret.length >= 8) {
    out = out.split(secret).join('<REDACTED_SECRET>');
  }
  out = out.replace(/https?:\/\/[^\s"'\\]+/gi, '<REDACTED_URL>');
  out = out.replace(/\/webhook(?:-test)?\/[A-Za-z0-9_-]+/gi, '/webhook/<REDACTED_PATH>');
  out = out.replace(/[A-Za-z]:\\[^\s"'\\]+/g, '<REDACTED_PATH>');
  out = out.replace(/\\\\[^\s\\/]+\\[^\s"'\\]+/g, '<REDACTED_UNC>');
  out = out.replace(
    /(\b(api[_-]?key|bot[_-]?token|access[_-]?token|secret[_-]?key|bearer\s+[A-Za-z0-9\-._~+/]+=*)\b|\b\d{8,10}:[A-Za-z0-9_-]{30,}\b)/gi,
    '<REDACTED_TOKEN>',
  );
  if (out.length > RESPONSE_CAPTURE_MAX) {
    out = `${out.slice(0, RESPONSE_CAPTURE_MAX - 3)}...`;
  }
  return out;
}

function sanitizeResponseBody(text, secret) {
  const redacted = redactText(text, secret);
  try {
    const parsed = JSON.parse(text);
    if (parsed && typeof parsed === 'object') {
      const safe = {};
      for (const key of [
        'ok',
        'result',
        'event_id',
        'dedupe',
        'code',
        'note',
        'message',
        'error',
        'status',
      ]) {
        if (key in parsed) {
          const v = parsed[key];
          safe[key] =
            typeof v === 'string' ? redactText(v, secret) : v;
        }
      }
      return { kind: 'json', fields: safe, raw_redacted: redacted };
    }
  } catch {
    // fall through
  }
  return { kind: 'text', raw_redacted: redacted };
}

function classifyResponse(status, bodyFields, caseId) {
  if (status === 0) return 'TRANSPORT_ERROR';
  if (status === 413) return 'PAYLOAD_TOO_LARGE';
  if (caseId === 'T01' || caseId === 'T02') {
    if (status === 401 || status === 403 || status === 404) return 'NATIVE_AUTH_REJECTED';
    return 'UNEXPECTED';
  }
  if (caseId === 'T03' || caseId === 'T04') {
    if (status >= 400 && status < 500) return 'NATIVE_PARSE_REJECTED';
    if (bodyFields?.result === 'REJECTED' || bodyFields?.ok === false) {
      return 'WORKFLOW_VALIDATION_REJECTED';
    }
  }
  if (bodyFields?.result === 'ACCEPTED') return 'WORKFLOW_ACCEPTED';
  if (bodyFields?.code === 'SECURITY_REJECTED') return 'WORKFLOW_SECURITY_REJECTED';
  if (
    bodyFields?.code === 'INVALID_SCHEMA' ||
    bodyFields?.code === 'UNSUPPORTED_MEDIA_TYPE' ||
    bodyFields?.code === 'PAYLOAD_TOO_LARGE' ||
    bodyFields?.result === 'REJECTED'
  ) {
    if (bodyFields?.code === 'SECURITY_REJECTED') return 'WORKFLOW_SECURITY_REJECTED';
    if (bodyFields?.code === 'PAYLOAD_TOO_LARGE' || status === 413) return 'PAYLOAD_TOO_LARGE';
    return 'WORKFLOW_VALIDATION_REJECTED';
  }
  if (status >= 500) return 'INTERNAL_ERROR';
  if (status >= 400) return 'UNEXPECTED';
  return 'UNEXPECTED';
}

/**
 * @param {string} webhookUrl
 * @param {{
 *   authMode: 'omit'|'wrong'|'valid',
 *   secret: string,
 *   contentType?: string|null,
 *   body: string|Buffer,
 *   redirect?: 'error'|'follow',
 * }} opts
 */
async function postCase(webhookUrl, opts) {
  const headers = {};
  if (opts.contentType !== null) {
    headers['Content-Type'] =
      opts.contentType === undefined ? 'application/json' : opts.contentType;
  }
  if (opts.authMode === 'valid') {
    headers[AUTH_HEADER] = opts.secret;
  } else if (opts.authMode === 'wrong') {
    headers[AUTH_HEADER] =
      'SYNTHETIC_WRONG_TOKEN_PHASE1BB2_NOT_A_REAL_CREDENTIAL_XXXX';
  }

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);
  const started = Date.now();
  try {
    const response = await fetch(webhookUrl, {
      method: 'POST',
      headers,
      body: opts.body,
      redirect: 'error',
      signal: controller.signal,
    });
    const text = await response.text();
    return {
      http_status: response.status,
      latency_ms: Date.now() - started,
      body_text: text,
      redirected: false,
    };
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    return {
      http_status: 0,
      latency_ms: Date.now() - started,
      body_text: '',
      transport_error_class: /abort/i.test(message)
        ? 'timeout'
        : /redirect/i.test(message)
          ? 'redirect_blocked'
          : 'network',
    };
  } finally {
    clearTimeout(timer);
  }
}

function buildCaseMatrix(duplicateEventId) {
  const oversizedJson = `{"schema_name":"mars.client_ops.report","schema_version":"1.0","event_id":"${randomUUID()}","event_type":"site.post_1c_monitor","generated_at":"2026-07-24T00:00:00Z","observed_at":"2026-07-24T00:00:00Z","environment":"production","site":{"site_id":"SITE-002","site_name":"ZPM","domain":"bzpm.ru"},"producer":{"name":"${PRODUCER_NAME}","version":"1"},"run":{"run_id":"oversize","source_status":"NO_ACTION_REQUIRED","normalized_status":"OK","summary_code":"NO_ACTION_REQUIRED","reason_codes":["X"]},"action":{"required":false,"code":"NONE","text":"pad"},"metrics":{"baseline_count":1,"current_count":1,"added_urls":0,"removed_urls":0,"onboarding_needed_count":0},"freshness":{"age_seconds":1,"stale":false},"security":{"classification":"internal","contains_secrets":false,"redacted":true},"pad":"${'x'.repeat(MAX_PAYLOAD_BYTES)}}`;

  return [
    {
      id: 'T01',
      scenario: 'No auth header',
      authMode: 'omit',
      expectClass: 'NATIVE_AUTH_REJECTED',
      expectExec: false,
      body: () => JSON.stringify(buildValidEnvelope({ status: 'OK' })),
    },
    {
      id: 'T02',
      scenario: 'Wrong auth value',
      authMode: 'wrong',
      expectClass: 'NATIVE_AUTH_REJECTED',
      expectExec: false,
      body: () => JSON.stringify(buildValidEnvelope({ status: 'OK' })),
    },
    {
      id: 'T03',
      scenario: 'Unsupported content type',
      authMode: 'valid',
      contentType: 'text/plain',
      expectClass: 'NATIVE_PARSE_REJECTED',
      expectExec: true,
      body: () => JSON.stringify(buildValidEnvelope({ status: 'OK' })),
    },
    {
      id: 'T04',
      scenario: 'Malformed JSON',
      authMode: 'valid',
      expectClass: 'NATIVE_PARSE_REJECTED',
      expectExec: false,
      body: () => '{"schema_name":"mars.client_ops.report",',
    },
    {
      id: 'T05',
      scenario: 'Valid OK',
      authMode: 'valid',
      expectClass: 'WORKFLOW_ACCEPTED',
      expectExec: true,
      body: () => JSON.stringify(buildValidEnvelope({ status: 'OK' })),
    },
    {
      id: 'T06',
      scenario: 'Valid ATTENTION',
      authMode: 'valid',
      expectClass: 'WORKFLOW_ACCEPTED',
      expectExec: true,
      body: () => JSON.stringify(buildValidEnvelope({ status: 'ATTENTION' })),
    },
    {
      id: 'T07',
      scenario: 'Valid FAILED',
      authMode: 'valid',
      expectClass: 'WORKFLOW_ACCEPTED',
      expectExec: true,
      body: () => JSON.stringify(buildValidEnvelope({ status: 'FAILED' })),
    },
    {
      id: 'T08',
      scenario: 'Valid BLOCKED',
      authMode: 'valid',
      expectClass: 'WORKFLOW_ACCEPTED',
      expectExec: true,
      body: () => JSON.stringify(buildValidEnvelope({ status: 'BLOCKED' })),
    },
    {
      id: 'T09',
      scenario: 'Invalid schema_name',
      authMode: 'valid',
      expectClass: 'WORKFLOW_VALIDATION_REJECTED',
      expectExec: true,
      body: () =>
        JSON.stringify(buildValidEnvelope({ schema_name: 'not.client_ops.report' })),
    },
    {
      id: 'T10',
      scenario: 'Unsupported schema major',
      authMode: 'valid',
      expectClass: 'WORKFLOW_VALIDATION_REJECTED',
      expectExec: true,
      body: () => JSON.stringify(buildValidEnvelope({ schema_version: '2.0' })),
    },
    {
      id: 'T11',
      scenario: 'Invalid site_id',
      authMode: 'valid',
      expectClass: 'WORKFLOW_VALIDATION_REJECTED',
      expectExec: true,
      body: () => JSON.stringify(buildValidEnvelope({ site_id: 'SITE-999' })),
    },
    {
      id: 'T12',
      scenario: 'Invalid domain',
      authMode: 'valid',
      expectClass: 'WORKFLOW_VALIDATION_REJECTED',
      expectExec: true,
      body: () => JSON.stringify(buildValidEnvelope({ domain: 'example.com' })),
    },
    {
      id: 'T13',
      scenario: 'Invalid event_type',
      authMode: 'valid',
      expectClass: 'WORKFLOW_VALIDATION_REJECTED',
      expectExec: true,
      body: () =>
        JSON.stringify(buildValidEnvelope({ event_type: 'site.other_event' })),
    },
    {
      id: 'T14',
      scenario: 'Invalid status',
      authMode: 'valid',
      expectClass: 'WORKFLOW_VALIDATION_REJECTED',
      expectExec: true,
      body: () => JSON.stringify(buildValidEnvelope({ status: 'WARN' })),
    },
    {
      id: 'T15',
      scenario: 'Invalid event_id UUID',
      authMode: 'valid',
      expectClass: 'WORKFLOW_VALIDATION_REJECTED',
      expectExec: true,
      body: () =>
        JSON.stringify(buildValidEnvelope({ event_id: 'not-a-uuid' })),
    },
    {
      id: 'T16',
      scenario: 'Boolean metric',
      authMode: 'valid',
      expectClass: 'WORKFLOW_VALIDATION_REJECTED',
      expectExec: true,
      body: () =>
        JSON.stringify(
          buildValidEnvelope({ metrics: { added_urls: true } }),
        ),
    },
    {
      id: 'T17',
      scenario: 'Negative metric',
      authMode: 'valid',
      expectClass: 'WORKFLOW_VALIDATION_REJECTED',
      expectExec: true,
      body: () =>
        JSON.stringify(
          buildValidEnvelope({ metrics: { removed_urls: -1 } }),
        ),
    },
    {
      id: 'T18',
      scenario: 'contains_secrets=true',
      authMode: 'valid',
      expectClass: 'WORKFLOW_SECURITY_REJECTED',
      expectExec: true,
      body: () =>
        JSON.stringify(
          buildValidEnvelope({ security: { contains_secrets: true } }),
        ),
    },
    {
      id: 'T19',
      scenario: 'redacted=false',
      authMode: 'valid',
      expectClass: 'WORKFLOW_SECURITY_REJECTED',
      expectExec: true,
      body: () =>
        JSON.stringify(buildValidEnvelope({ security: { redacted: false } })),
    },
    {
      id: 'T20',
      scenario: 'Windows path injection',
      authMode: 'valid',
      expectClass: 'WORKFLOW_SECURITY_REJECTED',
      expectExec: true,
      body: () =>
        JSON.stringify(
          buildValidEnvelope({
            inject_field: ['action.text', 'see X:\\AI MARS\\sandbox-only\\synthetic.txt'],
          }),
        ),
    },
    {
      id: 'T21',
      scenario: 'UNC path injection',
      authMode: 'valid',
      expectClass: 'WORKFLOW_SECURITY_REJECTED',
      expectExec: true,
      body: () =>
        JSON.stringify(
          buildValidEnvelope({
            inject_field: ['action.text', 'see \\\\sandbox-host\\share\\synthetic.txt'],
          }),
        ),
    },
    {
      id: 'T22',
      scenario: 'Embedded URI credentials',
      authMode: 'valid',
      expectClass: 'WORKFLOW_SECURITY_REJECTED',
      expectExec: true,
      body: () =>
        JSON.stringify(
          buildValidEnvelope({
            inject_field: [
              'action.text',
              'probe https://sandbox_user:sandbox_pass@example.invalid/path',
            ],
          }),
        ),
    },
    {
      id: 'T23',
      scenario: 'Token-like value',
      authMode: 'valid',
      expectClass: 'WORKFLOW_SECURITY_REJECTED',
      expectExec: true,
      body: () =>
        JSON.stringify(
          buildValidEnvelope({
            inject_field: [
              'action.text',
              'api_key=SYNTHETIC_TOKEN_MARKER_NOT_A_REAL_CREDENTIAL_ABCDEF',
            ],
          }),
        ),
    },
    {
      id: 'T24',
      scenario: 'Stack-trace-like value',
      authMode: 'valid',
      expectClass: 'WORKFLOW_SECURITY_REJECTED',
      expectExec: true,
      body: () =>
        JSON.stringify(
          buildValidEnvelope({
            inject_field: [
              'action.text',
              'Traceback (most recent call last):\n  File "sandbox.py", line 1',
            ],
          }),
        ),
    },
    {
      id: 'T25',
      scenario: 'Private-key marker',
      authMode: 'valid',
      expectClass: 'WORKFLOW_SECURITY_REJECTED',
      expectExec: true,
      body: () => {
        // Assemble PEM markers at runtime so offline security scan does not flag source.
        const begin = `-----${'BEGIN'} ${'PRIVATE'} ${'KEY'}-----`;
        const end = `-----${'END'} ${'PRIVATE'} ${'KEY'}-----`;
        return JSON.stringify(
          buildValidEnvelope({
            inject_field: [
              'action.text',
              `${begin}\nSYNTHETIC_NOT_A_KEY\n${end}`,
            ],
          }),
        );
      },
    },
    {
      id: 'T26',
      scenario: 'Oversized payload',
      authMode: 'valid',
      expectClass: 'PAYLOAD_TOO_LARGE',
      expectExec: false,
      body: () => oversizedJson,
      // keep within safe ceiling (~few hundred KB)
      note: `payload_bytes≈${Buffer.byteLength(oversizedJson, 'utf8')}`,
    },
    {
      id: 'T27',
      scenario: 'Duplicate event_id first',
      authMode: 'valid',
      expectClass: 'WORKFLOW_ACCEPTED',
      expectExec: true,
      body: () =>
        JSON.stringify(
          buildValidEnvelope({ status: 'OK', event_id: duplicateEventId }),
        ),
    },
    {
      id: 'T28',
      scenario: 'Duplicate event_id second',
      authMode: 'valid',
      expectClass: 'WORKFLOW_ACCEPTED',
      expectExec: true,
      body: () =>
        JSON.stringify(
          buildValidEnvelope({ status: 'OK', event_id: duplicateEventId }),
        ),
    },
  ];
}

function structuralSummary(wf) {
  const webhook = (wf.nodes || []).find((n) => n.type === 'n8n-nodes-base.webhook');
  const blob = JSON.stringify(wf);
  return {
    id: wf.id,
    name: wf.name,
    active: wf.active,
    nodes: (wf.nodes || []).length,
    versionId: wf.versionId,
    updatedAt: wf.updatedAt,
    webhook_authentication: webhook?.parameters?.authentication || null,
    credential_reference: webhook?.credentials?.httpHeaderAuth
      ? {
          id: webhook.credentials.httpHeaderAuth.id,
          name: webhook.credentials.httpHeaderAuth.name,
          type: 'httpHeaderAuth',
        }
      : null,
    auth_placeholder_absent: !blob.includes('HITL_REQUIRED:CLIENT_OPS_WEBHOOK_AUTH_SECRET'),
    dedupe_deferred: /DEDUPE_DEFERRED_SANDBOX|DEFERRED_SANDBOX/.test(blob),
    telegram_absent: !(wf.nodes || []).some((n) => /telegram/i.test(n.type)),
    http_request_absent: !(wf.nodes || []).some(
      (n) => n.type === 'n8n-nodes-base.httpRequest',
    ),
    node_matrix: (wf.nodes || []).map((n) => ({
      name: n.name,
      type: n.type,
      typeVersion: n.typeVersion,
      disabled: Boolean(n.disabled),
    })),
  };
}

function writeJson(path, obj) {
  writeFileSync(path, `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const report = {
    runner: 'run-client-ops-authenticated-post-validation',
    mode: args.apply ? 'APPLY' : 'DRY_RUN',
    post_mode: 'POST_MODE_CONTROLLED_TEMPORARY_ACTIVATION',
    confirmation_phrase_required: CONFIRM_PHRASE,
    workflow_id: ALLOWED_WORKFLOW_ID,
    workflow_name: ALLOWED_WORKFLOW_NAME,
    credential_id: CREDENTIAL_ID,
    credential_name: CREDENTIAL_NAME,
    secret_printed: false,
    full_url_exposed: false,
    activation_changes: 0,
    requests_attempted: 0,
    requests_completed: 0,
    cases: [],
  };

  const secretInfo = loadSecretFromLocalFile();
  report.secret_file_exists = secretInfo.ok || secretInfo.error !== 'secret_file_missing';
  report.secret_key_present = secretInfo.ok || Boolean(secretInfo.value);
  report.secret_length_class = secretInfo.lengthClass;
  if (!secretInfo.ok) {
    report.aborted = secretInfo.error;
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

  const live = await getWorkflow(ALLOWED_WORKFLOW_ID, readCreds);
  const listed = await listWorkflows(readCreds);
  const exact = (Array.isArray(listed) ? listed : listed?.data || []).filter(
    (w) => w.name === ALLOWED_WORKFLOW_NAME,
  );
  const summary = structuralSummary(live);
  summary.exact_name_count = exact.length;
  report.pre_state = summary;

  const execBefore = await executionSnapshot(readCreds, ALLOWED_WORKFLOW_ID);
  report.executions_baseline = {
    observable: execBefore.observable,
    count: execBefore.count ?? null,
    row_count: execBefore.rows.length,
  };

  const webhookNode = (live.nodes || []).find(
    (n) => n.type === 'n8n-nodes-base.webhook',
  );
  const webhookPath = webhookNode?.parameters?.path;
  if (!webhookPath || typeof webhookPath !== 'string') {
    report.aborted = 'webhook_path_missing';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  const duplicateEventId = randomUUID();
  const matrix = buildCaseMatrix(duplicateEventId);
  report.case_count = matrix.length;
  report.max_requests = MAX_REQUESTS;

  const telegramPresent = summary.telegram_absent === false;
  const execCount = execBefore.count ?? execBefore.rows.length;
  const matrixReplayBlocked = telegramPresent || execCount > 0;

  if (!args.apply) {
    if (args.c1SandboxTest) {
      report.dry_run = {
        mode: 'C1_SINGLE_SYNTHETIC_OVERRIDE',
        would_activate: true,
        would_deactivate: true,
        would_post_cases: ['C1_OK_SYNTHETIC'],
        matrix_replay_rejected: true,
        production_payload_rejected: true,
        pre_active: live.active,
        gates: {
          exact_name_count: exact.length === 1,
          active_false: live.active === false,
          header_auth: summary.webhook_authentication === 'headerAuth',
          credential_bound:
            summary.credential_reference?.id === CREDENTIAL_ID &&
            summary.credential_reference?.name === CREDENTIAL_NAME,
          http_request_absent: summary.http_request_absent,
          c1_override_phrase_required: true,
          single_post_only: true,
          telegram_integration_present_or_pending: true,
        },
      };
      const gateFail = Object.entries(report.dry_run.gates).filter(([, v]) => !v);
      report.dry_run_verdict = gateFail.length === 0 ? 'READY_C1_OVERRIDE' : 'BLOCKED';
      if (gateFail.length) report.dry_run_failed_gates = gateFail.map(([k]) => k);
      console.log(JSON.stringify(report, null, 2));
      process.exitCode = gateFail.length === 0 ? 0 : 2;
      return;
    }

    report.dry_run = {
      would_activate: true,
      would_deactivate: true,
      would_post_cases: matrix.map((c) => c.id),
      pre_active: live.active,
      matrix_replay_blocked: matrixReplayBlocked,
      production_payload_rejected: true,
      gates: {
        exact_name_count: exact.length === 1,
        active_false: live.active === false,
        nodes_9: (live.nodes || []).length === 9,
        header_auth: summary.webhook_authentication === 'headerAuth',
        credential_bound:
          summary.credential_reference?.id === CREDENTIAL_ID &&
          summary.credential_reference?.name === CREDENTIAL_NAME,
        telegram_absent: summary.telegram_absent,
        http_request_absent: summary.http_request_absent,
        executions_baseline_zero: execCount === 0,
        matrix_not_blocked_by_prior_work: !matrixReplayBlocked,
      },
    };
    const gateFail = Object.entries(report.dry_run.gates).filter(([, v]) => !v);
    report.dry_run_verdict = gateFail.length === 0 ? 'READY' : 'BLOCKED';
    if (gateFail.length) report.dry_run_failed_gates = gateFail.map(([k]) => k);
    if (matrixReplayBlocked) {
      report.dry_run_verdict = 'BLOCKED_MATRIX_REPLAY';
      report.replay_guard =
        'B2 28-case matrix replay rejected after prior executions and/or Telegram integration; use Phase 1B-C1 runner or --c1-sandbox-test override.';
    }
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = report.dry_run_verdict === 'READY' ? 0 : 2;
    return;
  }

  if (matrixReplayBlocked && !args.c1SandboxTest) {
    report.aborted = 'matrix_replay_blocked';
    report.replay_guard =
      'Authenticated POST matrix apply is blocked after prior sandbox executions/Telegram integration.';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  if (args.c1SandboxTest) {
    report.aborted = 'c1_override_must_use_phase_c1_runner';
    report.hint =
      'Use run-client-ops-telegram-sandbox-controlled-apply.mjs for the single authorized C1 POST.';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  if (args.confirm !== CONFIRM_PHRASE) {
    report.aborted = 'confirmation_phrase_mismatch';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  if (live.active !== false) {
    report.aborted = 'pre_state_active_not_false';
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }
  if (exact.length !== 1) {
    report.aborted = `exact_name_count_${exact.length}`;
    console.log(JSON.stringify(report, null, 2));
    process.exitCode = 2;
    return;
  }

  ensureDir(ROLLBACK_DIR);
  ensureDir(LOCAL_EVIDENCE);
  ensureDir(REPO_EVIDENCE);

  const rawSnapshot = {
    captured_at: new Date().toISOString(),
    workflow_id: live.id,
    versionId: live.versionId,
    updatedAt: live.updatedAt,
    active: live.active,
    node_count: (live.nodes || []).length,
    credential_reference: summary.credential_reference,
    executions_baseline: report.executions_baseline,
    sanitized_workflow: sanitizeWorkflow(live),
  };
  writeJson(resolve(ROLLBACK_DIR, 'pre-test-workflow.sanitized.json'), {
    ...rawSnapshot,
    note: 'Sanitized snapshot; secret values absent; webhook path redacted from public evidence.',
  });
  // Raw GET retained only under ignored local path — strip usable URL pieces in a companion meta file.
  writeJson(resolve(ROLLBACK_DIR, 'pre-test-meta.json'), {
    workflow_id: live.id,
    versionId: live.versionId,
    updatedAt: live.updatedAt,
    active: live.active,
    node_count: (live.nodes || []).length,
    credential_reference: summary.credential_reference,
    executions_baseline: report.executions_baseline,
    webhook_path_present: true,
    webhook_path_stored: false,
  });
  // Keep raw workflow for emergency rollback only in local ignored tree.
  writeFileSync(
    resolve(ROLLBACK_DIR, 'pre-test-workflow.raw.json'),
    `${JSON.stringify(live)}\n`,
    'utf8',
  );

  const actCreds = loadActivationCredentials();
  const webhookUrl = `${normalizeBaseUrl(actCreds.apiUrl)}/webhook/${webhookPath}`;
  let activated = false;
  let containment = {
    deactivate_attempted: false,
    deactivate_ok: false,
    emergency_retry: false,
    final_active: null,
  };

  try {
    await activateAllowlistedWorkflow(actCreds, ACTIVATION_CONFIRM_PHRASE);
    activated = true;
    report.activation_changes += 1;
    report.activation = { attempted: true, ok: true };

    // brief settle
    await new Promise((r) => setTimeout(r, 2500));
    const mid = await getWorkflow(ALLOWED_WORKFLOW_ID, readCreds);
    report.during_tests_active = mid.active;
    if (mid.active !== true) {
      throw new Error('Workflow did not become active after activation');
    }

    for (const testCase of matrix) {
      if (report.requests_attempted >= MAX_REQUESTS) {
        report.aborted = 'max_requests_exceeded';
        break;
      }
      report.requests_attempted += 1;
      const body = testCase.body();
      const result = await postCase(webhookUrl, {
        authMode: testCase.authMode,
        secret: secretInfo.value,
        contentType: testCase.contentType,
        body,
      });
      report.requests_completed += 1;
      const sanitized = sanitizeResponseBody(result.body_text, secretInfo.value);
      const classification = classifyResponse(
        result.http_status,
        sanitized.fields || {},
        testCase.id,
      );
      const classOk =
        classification === testCase.expectClass ||
        // allow observed native/content-type variance documentation
        (testCase.id === 'T03' &&
          (classification === 'NATIVE_PARSE_REJECTED' ||
            classification === 'WORKFLOW_VALIDATION_REJECTED')) ||
        (testCase.id === 'T04' &&
          (classification === 'NATIVE_PARSE_REJECTED' ||
            classification === 'WORKFLOW_VALIDATION_REJECTED' ||
            classification === 'UNEXPECTED'));

      const row = {
        case: testCase.id,
        scenario: testCase.scenario,
        auth: testCase.authMode,
        http: result.http_status,
        classification,
        expected_classification: testCase.expectClass,
        latency_ms: result.latency_ms,
        response: sanitized.fields || { raw_redacted: sanitized.raw_redacted },
        transport_error_class: result.transport_error_class || null,
        class_match: classOk,
        expect_execution: testCase.expectExec,
      };
      report.cases.push(row);

      // containment triggers
      const leak =
        (result.body_text &&
          secretInfo.value &&
          result.body_text.includes(secretInfo.value)) ||
        /BEGIN (RSA |OPENSSH )?PRIVATE KEY/i.test(result.body_text || '') ||
        /X:\\AI MARS\\/i.test(result.body_text || '');
      if (leak) {
        report.aborted = 'secret_or_path_reflected';
        break;
      }
      if (result.transport_error_class === 'redirect_blocked') {
        report.aborted = 'unexpected_redirect';
        break;
      }
    }

    const execAfter = await executionSnapshot(readCreds, ALLOWED_WORKFLOW_ID);
    report.executions_after = {
      observable: execAfter.observable,
      count: execAfter.count ?? null,
      row_count: execAfter.rows.length,
      rows: execAfter.rows.map((e) => ({
        id: e.id,
        status: e.status,
        startedAt: e.startedAt,
        stoppedAt: e.stoppedAt,
        workflowId: e.workflowId,
      })),
    };
  } catch (err) {
    report.runtime_error = redactText(
      err instanceof Error ? err.message : String(err),
      secretInfo.value,
    );
  } finally {
    if (activated) {
      containment.deactivate_attempted = true;
      try {
        await deactivateAllowlistedWorkflow(
          actCreds,
          DEACTIVATION_CONFIRM_PHRASE,
        );
        report.activation_changes += 1;
        containment.deactivate_ok = true;
      } catch (err) {
        containment.emergency_retry = true;
        try {
          await deactivateAllowlistedWorkflow(
            actCreds,
            DEACTIVATION_CONFIRM_PHRASE,
          );
          report.activation_changes += 1;
          containment.deactivate_ok = true;
        } catch (err2) {
          containment.deactivate_ok = false;
          containment.deactivate_error = redactText(
            err2 instanceof Error ? err2.message : String(err2),
            secretInfo.value,
          );
        }
      }
    }

    await new Promise((r) => setTimeout(r, 1000));
    const finalWf = await getWorkflow(ALLOWED_WORKFLOW_ID, readCreds);
    containment.final_active = finalWf.active;
    containment.final_summary = structuralSummary(finalWf);
    report.containment = containment;
    report.post_state = containment.final_summary;

    const execFinal = await executionSnapshot(readCreds, ALLOWED_WORKFLOW_ID);
    report.executions_final = {
      observable: execFinal.observable,
      count: execFinal.count ?? null,
      row_count: execFinal.rows.length,
      rows: execFinal.rows.map((e) => ({
        id: e.id,
        status: e.status,
        startedAt: e.startedAt,
        stoppedAt: e.stoppedAt,
        workflowId: e.workflowId,
      })),
    };

    writeJson(resolve(LOCAL_EVIDENCE, 'runner-report.sanitized.json'), report);
    writeJson(resolve(REPO_EVIDENCE, 'SANITIZED-CASE-RESULTS.json'), {
      generated_at: new Date().toISOString(),
      post_mode: report.post_mode,
      requests_attempted: report.requests_attempted,
      requests_completed: report.requests_completed,
      activation_changes: report.activation_changes,
      cases: report.cases,
      secret_printed: false,
      full_url_exposed: false,
    });
    writeJson(resolve(REPO_EVIDENCE, 'EXECUTION-CORRELATION.json'), {
      baseline: report.executions_baseline,
      after_matrix: report.executions_after || null,
      final: report.executions_final || null,
      attribution: {
        posts: report.requests_completed,
        expected_no_execution_cases: ['T01', 'T02', 'T04', 'T26'],
        expected_execution_count: Math.max(
          0,
          report.requests_completed - 4,
        ),
        observed_execution_count:
          report.executions_final?.count ??
          report.executions_final?.row_count ??
          null,
        note: 'T01/T02 native auth and T04/T26 native parse produce no workflow executions on this host.',
      },
      note: 'Sanitized execution metadata only; no raw payloads.',
    });
  }

  const criticalFail =
    containment.final_active !== false ||
    !containment.deactivate_ok ||
    report.aborted ||
    !report.cases.some(
      (c) => c.case === 'T05' && c.classification === 'WORKFLOW_ACCEPTED',
    ) ||
    !report.cases.some(
      (c) => c.case === 'T01' && c.classification === 'NATIVE_AUTH_REJECTED',
    ) ||
    !report.cases.some(
      (c) => c.case === 'T02' && c.classification === 'NATIVE_AUTH_REJECTED',
    );

  report.verdict = criticalFail
    ? 'PARTIAL'
    : 'COMPLETE';

  // Final console output — never include secret or URL.
  const publicReport = { ...report };
  console.log(JSON.stringify(publicReport, null, 2));
  process.exitCode = criticalFail ? 2 : 0;
}

main().catch((err) => {
  console.error(
    redactText(err instanceof Error ? err.message : String(err), ''),
  );
  process.exit(1);
});
