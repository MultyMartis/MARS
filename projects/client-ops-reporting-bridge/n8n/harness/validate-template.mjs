/**
 * Structural pre-create gate validator for Client Ops sandbox template.
 * Offline only — does not call n8n.
 *
 * Run: node validate-template.mjs
 */
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  AUTH_PLACEHOLDER,
  WORKFLOW_NAME,
} from './client-ops-validator.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const templatePath = resolve(
  __dirname,
  '../templates/mars-client-ops-bridge-bzpm-sandbox.template.json',
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
  { name: 'bearer_token', re: /\bBearer\s+[A-Za-z0-9._-]{16,}\b/i },
  { name: 'telegram_bot_token', re: /\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/ },
  { name: 'private_key', re: /BEGIN (RSA |OPENSSH )?PRIVATE KEY/i },
  { name: 'api_key_assignment', re: /\b(api[_-]?key|bot[_-]?token)\s*=\s*['"][^'"]+['"]/i },
];

function fail(gates, id, detail) {
  gates.push({ id, ok: false, detail });
}

function pass(gates, id, detail) {
  gates.push({ id, ok: true, detail });
}

function main() {
  const wf = JSON.parse(readFileSync(templatePath, 'utf8'));
  const gates = [];
  const names = new Set();
  const nodeByName = new Map();

  if (wf.name === WORKFLOW_NAME) {
    pass(gates, 'workflow_name', wf.name);
  } else {
    fail(gates, 'workflow_name', `got ${wf.name}`);
  }

  if (wf.active === false) {
    pass(gates, 'inactive', 'active=false');
  } else {
    fail(gates, 'inactive', `active=${wf.active}`);
  }

  if (!wf.id && !wf.versionId) {
    pass(gates, 'no_workflow_id', 'id/versionId omitted');
  } else {
    fail(gates, 'no_workflow_id', 'template must not contain real workflow ids');
  }

  const nodeCount = Array.isArray(wf.nodes) ? wf.nodes.length : 0;
  if (nodeCount >= 8 && nodeCount <= 12) {
    pass(gates, 'node_count', String(nodeCount));
  } else {
    fail(gates, 'node_count', String(nodeCount));
  }

  let hasTelegram = false;
  let hasHttp = false;
  let hasWebhookId = false;
  let hasCredentials = false;
  let webhookResponseModeOk = false;
  let placeholderPresent = false;

  for (const node of wf.nodes || []) {
    if (names.has(node.name)) {
      fail(gates, 'unique_node_names', `duplicate ${node.name}`);
    }
    names.add(node.name);
    nodeByName.set(node.name, node);

    const allowedVersions = ALLOWED_TYPES.get(node.type);
    if (!allowedVersions) {
      fail(gates, 'allowed_node_types', `${node.name}:${node.type}`);
    } else if (!allowedVersions.has(node.typeVersion)) {
      fail(
        gates,
        'typeVersions',
        `${node.name} ${node.type}@${node.typeVersion}`,
      );
    }

    if (FORBIDDEN_TYPES.has(node.type)) {
      if (node.type.includes('telegram')) hasTelegram = true;
      if (node.type === 'n8n-nodes-base.httpRequest') hasHttp = true;
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
  }

  if (!gates.some((g) => g.id === 'unique_node_names' && !g.ok)) {
    pass(gates, 'unique_node_names', `${names.size} unique`);
  }
  if (!gates.some((g) => g.id === 'allowed_node_types' && !g.ok)) {
    pass(gates, 'allowed_node_types', 'all allowed');
  }
  if (!gates.some((g) => g.id === 'typeVersions' && !g.ok)) {
    pass(gates, 'typeVersions', 'evidenced versions only');
  }

  if (!hasTelegram) pass(gates, 'no_telegram', 'ok');
  else fail(gates, 'no_telegram', 'telegram node present');

  if (!hasHttp) pass(gates, 'no_http_request', 'ok');
  else fail(gates, 'no_http_request', 'httpRequest present');

  if (!hasWebhookId) pass(gates, 'no_webhookId', 'ok');
  else fail(gates, 'no_webhookId', 'webhookId present');

  if (!hasCredentials) pass(gates, 'no_credentials', 'ok');
  else fail(gates, 'no_credentials', 'credentials present');

  if (webhookResponseModeOk) {
    pass(gates, 'responseMode_responseNode', 'ok');
  } else {
    fail(gates, 'responseMode_responseNode', 'missing');
  }

  if (placeholderPresent) {
    pass(gates, 'auth_placeholder_present', AUTH_PLACEHOLDER);
  } else {
    fail(gates, 'auth_placeholder_present', 'missing HITL placeholder');
  }

  // Connection integrity
  const connections = wf.connections || {};
  let dangling = false;
  for (const [src, outs] of Object.entries(connections)) {
    if (!names.has(src)) {
      dangling = true;
      fail(gates, 'connections_source', `missing source ${src}`);
    }
    for (const branch of outs.main || []) {
      for (const t of branch || []) {
        if (!names.has(t.node)) {
          dangling = true;
          fail(gates, 'connections_target', `missing target ${t.node}`);
        }
      }
    }
  }
  if (!dangling) pass(gates, 'no_dangling_connections', 'ok');

  // Terminal branches reach Respond
  const acceptPrep = connections['Prepare Accepted Response']?.main?.[0]?.[0]?.node;
  const rejectPrep = connections['Prepare Rejected Response']?.main?.[0]?.[0]?.node;
  if (acceptPrep === 'Respond Accepted' && rejectPrep === 'Respond Rejected') {
    pass(gates, 'terminals_reach_respond', 'ok');
  } else {
    fail(gates, 'terminals_reach_respond', `${acceptPrep}/${rejectPrep}`);
  }

  const ifBranches = connections['IF Accepted Branch']?.main || [];
  if (
    ifBranches.length === 2 &&
    ifBranches[0]?.[0]?.node === 'Prepare Accepted Response' &&
    ifBranches[1]?.[0]?.node === 'Prepare Rejected Response'
  ) {
    pass(gates, 'if_branches_complete', 'ok');
  } else {
    fail(gates, 'if_branches_complete', JSON.stringify(ifBranches));
  }

  // Secret scan (allow synthetic placeholder marker and SYNTHETIC harness label in comments)
  const full = JSON.stringify(wf);
  let secretHit = false;
  for (const pat of SECRET_PATTERNS) {
    if (pat.re.test(full)) {
      // Allow only if it's the documented placeholder context
      if (full.includes(AUTH_PLACEHOLDER) && pat.name === 'bearer_token') {
        // still check for real-looking bearer outside placeholder
        const stripped = full.split(AUTH_PLACEHOLDER).join('');
        if (pat.re.test(stripped)) {
          secretHit = true;
          fail(gates, 'secret_scan', pat.name);
        }
      } else if (pat.name !== 'bearer_token') {
        secretHit = true;
        fail(gates, 'secret_scan', pat.name);
      }
    }
  }
  if (!secretHit && !gates.some((g) => g.id === 'secret_scan' && !g.ok)) {
    pass(gates, 'secret_scan', 'no live secrets');
  }

  if (!/chat[_-]?id["']?\s*[:=]\s*["']?\d{5,}/i.test(full)) {
    pass(gates, 'no_chat_id', 'ok');
  } else {
    fail(gates, 'no_chat_id', 'chat id-like value');
  }

  const failed = gates.filter((g) => !g.ok);
  const report = {
    template: templatePath,
    gates_total: gates.length,
    gates_passed: gates.filter((g) => g.ok).length,
    gates_failed: failed.length,
    gates,
    verdict: failed.length === 0 ? 'PASS' : 'FAIL',
    apply_ready: false,
    reason:
      'Template retains HITL auth placeholder; create runner must reject until resolved.',
  };

  console.log(JSON.stringify(report, null, 2));
  if (failed.length > 0) process.exitCode = 1;
}

main();
