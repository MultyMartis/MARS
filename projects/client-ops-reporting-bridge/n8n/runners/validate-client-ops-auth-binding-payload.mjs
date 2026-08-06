/**
 * Validate Client Ops auth-binding PUT payload (Phase 1B-B1).
 *
 * Usage:
 *   node validate-client-ops-auth-binding-payload.mjs [--payload=PATH]
 */

import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  AUTH_PLACEHOLDER,
  WORKFLOW_NAME,
} from '../harness/client-ops-validator.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const DEFAULT_PAYLOAD = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/apply/mars-client-ops-bridge-bzpm.auth-binding.put-payload.json',
);

const ALLOWED_TYPES = new Map([
  ['n8n-nodes-base.webhook', new Set([2.1])],
  ['n8n-nodes-base.code', new Set([2])],
  ['n8n-nodes-base.if', new Set([2.3])],
  ['n8n-nodes-base.respondToWebhook', new Set([1.1])],
]);

const FORBIDDEN_TYPES = new Set([
  'n8n-nodes-base.telegram',
  'n8n-nodes-base.telegramTrigger',
  'n8n-nodes-base.httpRequest',
  'n8n-nodes-base.googleSheets',
]);

const SECRET_PATTERNS = [
  { name: 'telegram_bot_token', re: /\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/ },
  { name: 'private_key', re: /BEGIN (RSA |OPENSSH )?PRIVATE KEY/i },
  {
    name: 'api_key_assignment',
    re: /\b(api[_-]?key|bot[_-]?token)\s*=\s*['"][^'"]+['"]/i,
  },
  {
    name: 'real_bearer',
    re: /Bearer\s+(?!SYNTHETIC_|REDACTED|<<<)[A-Za-z0-9._-]{20,}/i,
  },
];

function pass(gates, id, detail) {
  gates.push({ id, ok: true, detail });
}
function fail(gates, id, detail) {
  gates.push({ id, ok: false, detail });
}

function main() {
  const arg = process.argv.find((a) => a.startsWith('--payload='));
  const payloadPath = arg ? resolve(arg.slice('--payload='.length)) : DEFAULT_PAYLOAD;
  const bundle = JSON.parse(readFileSync(payloadPath, 'utf8'));
  const gates = [];
  const wf = bundle.full_workflow_for_validation;
  const put = bundle.put_payload;
  const cred = bundle.credential_ref || {};

  if (bundle.auth_mode === 'AUTH_NATIVE_HEADER_CREDENTIAL_BOUND') {
    pass(gates, 'auth_mode', bundle.auth_mode);
  } else {
    fail(gates, 'auth_mode', String(bundle.auth_mode));
  }

  if (bundle.workflow_id === 'tkM4H0G0gM3q9Foi') {
    pass(gates, 'workflow_id', bundle.workflow_id);
  } else {
    fail(gates, 'workflow_id', String(bundle.workflow_id));
  }

  if (wf.name === WORKFLOW_NAME && put.name === WORKFLOW_NAME) {
    pass(gates, 'exact_name', WORKFLOW_NAME);
  } else {
    fail(gates, 'exact_name', `${wf.name}/${put.name}`);
  }

  if (wf.active === false && put.active === undefined) {
    pass(gates, 'inactive', 'active=false / put omits read-only active');
  } else {
    fail(gates, 'inactive', `wf.active=${wf.active} put.active=${put.active}`);
  }

  if (put.id || put.versionId || put.createdAt || put.updatedAt) {
    fail(gates, 'no_server_managed_fields', 'server fields present on put payload');
  } else {
    pass(gates, 'no_server_managed_fields', 'ok');
  }

  const names = new Set();
  let hasTelegram = false;
  let hasExternal = false;
  let webhookAuthOk = false;
  let webhookCredOk = false;
  let placeholderPresent = false;
  let nativeMarker = false;
  let durableDedupeClaim = false;
  let nodeCount = 0;

  for (const node of put.nodes || []) {
    nodeCount += 1;
    if (names.has(node.name)) fail(gates, 'unique_node_names', `duplicate ${node.name}`);
    names.add(node.name);

    const allowed = ALLOWED_TYPES.get(node.type);
    if (!allowed) {
      fail(gates, 'allowed_node_types', `${node.name}:${node.type}`);
      if (FORBIDDEN_TYPES.has(node.type)) {
        if (String(node.type).includes('telegram')) hasTelegram = true;
        hasExternal = true;
      }
    } else if (!allowed.has(node.typeVersion)) {
      fail(gates, 'typeVersions', `${node.name} ${node.type}@${node.typeVersion}`);
    }

    if (node.webhookId) fail(gates, 'no_webhookId_on_put', node.name);

    if (node.type === 'n8n-nodes-base.webhook') {
      if (node.parameters?.authentication === 'headerAuth') webhookAuthOk = true;
      const href = node.credentials?.httpHeaderAuth;
      if (
        href &&
        href.id === cred.id &&
        href.name === cred.name &&
        cred.type === 'httpHeaderAuth'
      ) {
        webhookCredOk = true;
      }
      // Ensure credential object has only id/name
      if (href && Object.keys(href).some((k) => !['id', 'name'].includes(k))) {
        fail(gates, 'credential_ref_shape', Object.keys(href).join(','));
      }
    }

    if (node.name !== 'Webhook Intake' && node.credentials) {
      fail(gates, 'credentials_only_on_webhook', node.name);
    }

    const blob = JSON.stringify(node);
    if (blob.includes(AUTH_PLACEHOLDER) || blob.includes('HITL_REQUIRED:CLIENT_OPS_WEBHOOK_AUTH_SECRET')) {
      placeholderPresent = true;
    }
    if (blob.includes('NATIVE_HEADER_AUTH') || blob.includes('auth_mode=NATIVE_HEADER_AUTH')) {
      nativeMarker = true;
    }
    if (/durable.?dedupe|DEDUPE_ENABLED|unique.?store/i.test(blob)) {
      durableDedupeClaim = true;
    }
  }

  if (!gates.some((g) => g.id === 'unique_node_names' && !g.ok)) {
    pass(gates, 'unique_node_names', `${names.size} unique`);
  }
  if (!gates.some((g) => g.id === 'allowed_node_types' && !g.ok)) {
    pass(gates, 'allowed_node_types', 'ok');
  }
  if (!gates.some((g) => g.id === 'typeVersions' && !g.ok)) {
    pass(gates, 'typeVersions', 'ok');
  }
  if (!gates.some((g) => g.id === 'no_webhookId_on_put' && !g.ok)) {
    pass(gates, 'no_webhookId_on_put', 'ok');
  }
  if (!gates.some((g) => g.id === 'credentials_only_on_webhook' && !g.ok)) {
    pass(gates, 'credentials_only_on_webhook', 'ok');
  }
  if (!gates.some((g) => g.id === 'credential_ref_shape' && !g.ok)) {
    pass(gates, 'credential_ref_shape', 'id+name only');
  }

  if (nodeCount === 9) pass(gates, 'node_count', '9');
  else fail(gates, 'node_count', String(nodeCount));

  if (!hasTelegram) pass(gates, 'no_telegram', 'ok');
  else fail(gates, 'no_telegram', 'present');

  if (!hasExternal) pass(gates, 'no_external_nodes', 'ok');
  else fail(gates, 'no_external_nodes', 'present');

  if (webhookAuthOk) pass(gates, 'webhook_header_auth', 'headerAuth');
  else fail(gates, 'webhook_header_auth', 'missing');

  if (webhookCredOk) pass(gates, 'webhook_credential_ref', `${cred.type}:${cred.name}`);
  else fail(gates, 'webhook_credential_ref', 'mismatch');

  if (cred.header_name === 'X-MARS-Client-Ops-Token') {
    pass(gates, 'header_name', cred.header_name);
  } else {
    fail(gates, 'header_name', String(cred.header_name));
  }

  if (!placeholderPresent) pass(gates, 'placeholder_absent', 'ok');
  else fail(gates, 'placeholder_absent', 'still present');

  if (nativeMarker) pass(gates, 'native_auth_marker', 'NATIVE_HEADER_AUTH');
  else fail(gates, 'native_auth_marker', 'missing');

  if (!durableDedupeClaim) pass(gates, 'dedupe_deferred', 'no durable claim');
  else fail(gates, 'dedupe_deferred', 'durable claim found');

  const blob = JSON.stringify(put);
  if (/https?:\/\//i.test(blob)) fail(gates, 'no_absolute_url', 'url present');
  else pass(gates, 'no_absolute_url', 'ok');

  let secretHit = false;
  for (const p of SECRET_PATTERNS) {
    if (p.re.test(blob)) {
      secretHit = true;
      fail(gates, 'secret_patterns', p.name);
    }
  }
  if (!secretHit) pass(gates, 'secret_patterns', 'clean');

  // Credential data must not appear
  if (/"value"\s*:\s*"[^"]{16,}"/.test(blob) && !blob.includes('SYNTHETIC_')) {
    fail(gates, 'no_credential_values', 'suspicious value field');
  } else {
    pass(gates, 'no_credential_values', 'ok');
  }

  const failed = gates.filter((g) => !g.ok);
  const result = {
    payload: payloadPath.replace(/\\/g, '/'),
    gates,
    pass_count: gates.filter((g) => g.ok).length,
    fail_count: failed.length,
    verdict: failed.length === 0 ? 'PASS' : 'FAIL',
  };
  console.log(JSON.stringify(result, null, 2));
  process.exitCode = failed.length === 0 ? 0 : 1;
}

main();
