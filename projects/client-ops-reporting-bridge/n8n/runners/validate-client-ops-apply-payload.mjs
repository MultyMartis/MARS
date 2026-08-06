/**
 * Validate Client Ops proposed final apply payload (blocked-inactive mode allowed).
 *
 * Usage:
 *   node validate-client-ops-apply-payload.mjs [--payload=PATH]
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
  'local/client-ops-reporting-bridge/bzpm.ru/apply/mars-client-ops-bridge-bzpm.create-payload.json',
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
  const authMode = bundle.auth_mode;
  const wf = bundle.full_workflow_for_validation;
  const createPayload = bundle.create_payload;
  const gates = [];

  if (authMode === 'AUTH_BLOCKED_INACTIVE_ONLY') {
    pass(gates, 'auth_mode', authMode);
  } else {
    fail(gates, 'auth_mode', String(authMode));
  }

  if (wf.name === WORKFLOW_NAME && createPayload.name === WORKFLOW_NAME) {
    pass(gates, 'exact_name', WORKFLOW_NAME);
  } else {
    fail(gates, 'exact_name', `${wf.name}/${createPayload.name}`);
  }

  if (wf.active === false && createPayload.active === undefined) {
    pass(gates, 'inactive', 'active=false / create omits active');
  } else {
    fail(gates, 'inactive', `wf.active=${wf.active}`);
  }

  if (!createPayload.id && !wf.id && !wf.versionId) {
    pass(gates, 'no_workflow_id', 'ok');
  } else {
    fail(gates, 'no_workflow_id', 'id present');
  }

  const names = new Set();
  let hasTelegram = false;
  let hasExternal = false;
  let hasWebhookId = false;
  let hasCredentials = false;
  let webhookResponseModeOk = false;
  let placeholderPresent = false;
  let durableDedupeClaim = false;

  for (const node of createPayload.nodes || []) {
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

    if (node.webhookId) hasWebhookId = true;
    if (node.credentials) hasCredentials = true;
    if (
      node.type === 'n8n-nodes-base.webhook' &&
      node.parameters?.responseMode === 'responseNode'
    ) {
      webhookResponseModeOk = true;
    }
    const blob = JSON.stringify(node);
    if (blob.includes(AUTH_PLACEHOLDER)) placeholderPresent = true;
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

  if (!hasTelegram) pass(gates, 'no_telegram', 'ok');
  else fail(gates, 'no_telegram', 'present');

  if (!hasExternal) pass(gates, 'no_external_nodes', 'ok');
  else fail(gates, 'no_external_nodes', 'present');

  if (!hasWebhookId) pass(gates, 'no_webhookId', 'ok');
  else fail(gates, 'no_webhookId', 'present');

  if (!hasCredentials) {
    pass(gates, 'no_credential_values_or_refs', 'blocked mode: no credential refs');
  } else {
    fail(gates, 'no_credential_values_or_refs', 'credentials present in blocked mode');
  }

  if (webhookResponseModeOk) pass(gates, 'responseMode_responseNode', 'ok');
  else fail(gates, 'responseMode_responseNode', 'missing');

  if (placeholderPresent) {
    pass(gates, 'blocked_placeholder_present', AUTH_PLACEHOLDER);
  } else {
    fail(gates, 'blocked_placeholder_present', 'missing in blocked mode');
  }

  if (!durableDedupeClaim) pass(gates, 'dedupe_deferred', 'DEDUPE_DEFERRED_SANDBOX');
  else fail(gates, 'dedupe_deferred', 'durable claim found');

  const connections = createPayload.connections || {};
  let dangling = false;
  for (const [src, outs] of Object.entries(connections)) {
    if (!names.has(src)) {
      dangling = true;
      fail(gates, 'connections_source', src);
    }
    for (const branch of outs.main || []) {
      for (const t of branch || []) {
        if (!names.has(t.node)) {
          dangling = true;
          fail(gates, 'connections_target', t.node);
        }
      }
    }
  }
  if (!dangling) pass(gates, 'valid_connections', 'ok');

  const acceptPrep = connections['Prepare Accepted Response']?.main?.[0]?.[0]?.node;
  const rejectPrep = connections['Prepare Rejected Response']?.main?.[0]?.[0]?.node;
  if (acceptPrep === 'Respond Accepted' && rejectPrep === 'Respond Rejected') {
    pass(gates, 'terminals_reach_respond', 'ok');
  } else {
    fail(gates, 'terminals_reach_respond', `${acceptPrep}/${rejectPrep}`);
  }

  const full = JSON.stringify(createPayload);
  let secretHit = false;
  for (const pat of SECRET_PATTERNS) {
    const stripped = full.split(AUTH_PLACEHOLDER).join('');
    if (pat.re.test(stripped)) {
      secretHit = true;
      fail(gates, 'secret_scan', pat.name);
    }
  }
  if (!secretHit && !gates.some((g) => g.id === 'secret_scan' && !g.ok)) {
    pass(gates, 'secret_scan', 'no live secrets');
  }

  if (!/https?:\/\//i.test(full)) pass(gates, 'no_production_urls', 'ok');
  else fail(gates, 'no_production_urls', 'url-like value');

  // Reject real absolute path literals only (not regex character-class examples in Code).
  const rawPathLiteral =
    /["'`][A-Za-z]:\\(?:Users|AI MARS|Windows|Program Files)[^"'`]*["'`]/i.test(full) ||
    /["'`]\\\\[^\\s\\/"'`]{2,}\\[^"'`]*["'`]/i.test(full);
  if (!rawPathLiteral) pass(gates, 'no_raw_paths', 'ok');
  else fail(gates, 'no_raw_paths', 'path-like');

  if (!/"active"\s*:\s*true/.test(full)) pass(gates, 'no_auto_activation', 'ok');
  else fail(gates, 'no_auto_activation', 'active true');

  // create payload schema
  const schemaOk =
    typeof createPayload.name === 'string' &&
    Array.isArray(createPayload.nodes) &&
    createPayload.connections &&
    typeof createPayload.connections === 'object' &&
    createPayload.settings &&
    typeof createPayload.settings === 'object' &&
    !('id' in createPayload) &&
    !('active' in createPayload);
  if (schemaOk) pass(gates, 'create_payload_schema', 'ok');
  else fail(gates, 'create_payload_schema', 'invalid');

  const failed = gates.filter((g) => !g.ok);
  const report = {
    payload: payloadPath,
    auth_mode: authMode,
    gates_total: gates.length,
    gates_passed: gates.filter((g) => g.ok).length,
    gates_failed: failed.length,
    gates,
    verdict: failed.length === 0 ? 'PASS' : 'FAIL',
    apply_ready_blocked_inactive: failed.length === 0,
  };
  console.log(JSON.stringify(report, null, 2));
  if (failed.length > 0) process.exitCode = 1;
}

main();
