/**
 * Validate composed Client Ops Telegram sandbox PUT payload (Phase 1B-C1).
 *
 * Usage:
 *   node validate-client-ops-telegram-sandbox-put-payload.mjs [--payload=PATH]
 */

import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const DEFAULT_PAYLOAD = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/apply/mars-client-ops-bridge-bzpm.telegram-sandbox.put-payload.json',
);

const WORKFLOW_NAME = 'MARS Client Ops Bridge — bzpm.ru';
const WORKFLOW_ID = 'tkM4H0G0gM3q9Foi';
const TG_CRED_ID = '2bIC5376l7ElXb4B';
const TG_CRED_NAME = 'MARS Client Ops Telegram — bzpm.ru';
const AUTH_CRED_ID = 'WKHmPaw6QBp7WnzP';
const AUTH_CRED_NAME = 'MARS Client Ops Webhook Auth — bzpm.ru';
const TELEGRAM_NODE_NAME = 'Telegram Notify Accepted';
const EXPECTED_BASE_NODES = 9;

const SECRET_PATTERNS = [
  { name: 'telegram_bot_token', re: /\b\d{6,}:[A-Za-z0-9_-]{20,}\b/ },
  { name: 'private_key', re: /BEGIN (RSA |OPENSSH )?PRIVATE KEY/i },
  {
    name: 'api_key_assignment',
    re: /\b(api[_-]?key|bot[_-]?token|accessToken)\s*[:=]\s*['"][^'"]{8,}['"]/i,
  },
  { name: 'telegram_api_url_with_token', re: /api\.telegram\.org\/bot\d+/i },
  {
    name: 'client_ops_webhook_secret_assignment',
    re: /CLIENT_OPS_WEBHOOK_AUTH_SECRET\s*=\s*\S+/i,
  },
  { name: 'absolute_url', re: /https?:\/\/[^\s"'\\]+/i },
];

const FORBIDDEN_NEW_TYPES = new Set([
  'n8n-nodes-base.code',
  'n8n-nodes-base.httpRequest',
  'n8n-nodes-base.googleSheets',
  'n8n-nodes-base.dataStore',
  'n8n-nodes-base.wait',
  'n8n-nodes-base.executeWorkflow',
]);

function pass(gates, id, detail) {
  gates.push({ id, ok: true, detail });
}
function fail(gates, id, detail) {
  gates.push({ id, ok: false, detail });
}

function main() {
  const arg = process.argv.find((a) => a.startsWith('--payload='));
  const payloadPath = arg ? resolve(arg.slice('--payload='.length)) : DEFAULT_PAYLOAD;
  const gates = [];

  if (!existsSync(payloadPath)) {
    console.log(
      JSON.stringify(
        {
          validator: 'validate-client-ops-telegram-sandbox-put-payload',
          payload_path: payloadPath.replace(/\\/g, '/'),
          verdict: 'BLOCKED_PAYLOAD_MISSING',
          gates: [{ id: 'payload_exists', ok: false, detail: 'missing' }],
        },
        null,
        2,
      ),
    );
    process.exitCode = 2;
    return;
  }

  const raw = readFileSync(payloadPath, 'utf8');
  const bundle = JSON.parse(raw);
  const put = bundle.put_payload || bundle;
  const nodes = put.nodes || [];
  const connections = put.connections || {};

  if (bundle.workflow_id === WORKFLOW_ID || put.id === WORKFLOW_ID) {
    pass(gates, 'workflow_id', WORKFLOW_ID);
  } else if (!bundle.workflow_id && !put.id) {
    pass(gates, 'workflow_id', 'omitted_in_put_body_ok');
  } else {
    fail(gates, 'workflow_id', String(bundle.workflow_id || put.id));
  }

  if (put.name === WORKFLOW_NAME) pass(gates, 'workflow_name', WORKFLOW_NAME);
  else fail(gates, 'workflow_name', String(put.name));

  if (bundle.active === false || put.active === false || put.active === undefined) {
    pass(gates, 'inactive', 'false_or_omitted');
  } else {
    fail(gates, 'inactive', String(put.active));
  }

  if (nodes.length === EXPECTED_BASE_NODES + 1) {
    pass(gates, 'node_count', String(nodes.length));
  } else {
    fail(gates, 'node_count', String(nodes.length));
  }

  const telegramNodes = nodes.filter((n) => String(n.type).includes('telegram'));
  if (telegramNodes.length === 1) pass(gates, 'telegram_node_count', '1');
  else fail(gates, 'telegram_node_count', String(telegramNodes.length));

  const tg = telegramNodes[0];
  if (tg?.name === TELEGRAM_NODE_NAME) pass(gates, 'telegram_node_name', TELEGRAM_NODE_NAME);
  else fail(gates, 'telegram_node_name', String(tg?.name));

  if (tg?.type === 'n8n-nodes-base.telegram') pass(gates, 'telegram_type', tg.type);
  else fail(gates, 'telegram_type', String(tg?.type));

  if (Number(tg?.typeVersion) === 1.2 || tg?.typeVersion === '1.2') {
    pass(gates, 'telegram_typeVersion', String(tg?.typeVersion));
  } else {
    fail(gates, 'telegram_typeVersion', String(tg?.typeVersion));
  }

  if (tg?.parameters?.operation === 'sendMessage' || tg?.parameters?.operation === undefined) {
    // n8n telegram 1.2 often defaults operation via resource/operation fields
    const op = tg?.parameters?.operation || tg?.parameters?.resource;
    if (tg?.parameters?.text && (tg?.parameters?.chatId != null || tg?.parameters?.chatId === 0)) {
      pass(gates, 'sendMessage_shape', 'chatId+text');
    } else {
      fail(gates, 'sendMessage_shape', `op=${op}`);
    }
  } else {
    fail(gates, 'sendMessage_shape', String(tg?.parameters?.operation));
  }

  const chat = String(tg?.parameters?.chatId ?? '');
  const proposalChat = (() => {
    try {
      const committed = JSON.parse(
        readFileSync(
          resolve(
            REPO_ROOT,
            'projects/client-ops-reporting-bridge/n8n/evidence/phase-1b-c-telegram-bot-intake/PROPOSED-INTEGRATION.json',
          ),
          'utf8',
        ),
      );
      return String(committed.proposed_integration?.chat_target?.chat_id ?? '');
    } catch {
      return '';
    }
  })();
  if (chat && proposalChat && chat === proposalChat) pass(gates, 'chat_id', 'matches_committed_proposal');
  else fail(gates, 'chat_id', chat ? 'mismatch_or_unresolved' : 'missing');

  const cred = tg?.credentials?.telegramApi;
  if (cred?.id === TG_CRED_ID && cred?.name === TG_CRED_NAME) {
    pass(gates, 'telegram_credential', TG_CRED_ID);
  } else {
    fail(gates, 'telegram_credential', JSON.stringify(cred || null));
  }

  const webhook = nodes.find((n) => n.type === 'n8n-nodes-base.webhook');
  if (webhook?.parameters?.authentication === 'headerAuth') {
    pass(gates, 'headerAuth', 'headerAuth');
  } else {
    fail(gates, 'headerAuth', String(webhook?.parameters?.authentication));
  }
  const whCred = webhook?.credentials?.httpHeaderAuth;
  if (whCred?.id === AUTH_CRED_ID && whCred?.name === AUTH_CRED_NAME) {
    pass(gates, 'auth_credential', AUTH_CRED_ID);
  } else {
    fail(gates, 'auth_credential', JSON.stringify(whCred || null));
  }

  const acceptOut = connections['Respond Accepted']?.main?.[0]?.[0]?.node;
  if (acceptOut === TELEGRAM_NODE_NAME) pass(gates, 'pattern_b_connection', acceptOut);
  else fail(gates, 'pattern_b_connection', String(acceptOut));

  const rejectOut = connections['Respond Rejected']?.main?.[0]?.[0]?.node;
  if (!rejectOut || rejectOut !== TELEGRAM_NODE_NAME) {
    pass(gates, 'rejected_path_excluded', String(rejectOut || 'none'));
  } else {
    fail(gates, 'rejected_path_excluded', rejectOut);
  }

  const baseNames = [
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
  const missing = baseNames.filter((n) => !nodes.some((x) => x.name === n));
  if (missing.length === 0) pass(gates, 'base_nodes_preserved', '9');
  else fail(gates, 'base_nodes_preserved', missing.join(','));

  const addedNonTelegram = nodes.filter(
    (n) => !baseNames.includes(n.name) && n.name !== TELEGRAM_NODE_NAME,
  );
  if (addedNonTelegram.length === 0) pass(gates, 'no_extra_nodes', '0');
  else fail(gates, 'no_extra_nodes', addedNonTelegram.map((n) => n.name).join(','));

  for (const n of addedNonTelegram) {
    if (FORBIDDEN_NEW_TYPES.has(n.type)) fail(gates, 'forbidden_new_type', `${n.name}:${n.type}`);
  }
  if (!gates.some((g) => g.id === 'forbidden_new_type' && !g.ok)) {
    pass(gates, 'forbidden_new_type', 'none');
  }

  if (!nodes.some((n) => n.webhookId)) pass(gates, 'no_webhookId', 'clean');
  else fail(gates, 'no_webhookId', 'present');

  for (const p of SECRET_PATTERNS) {
    if (p.re.test(raw)) fail(gates, `secret_scan_${p.name}`, 'match');
    else pass(gates, `secret_scan_${p.name}`, 'clean');
  }

  const text = String(tg?.parameters?.text || '');
  if (/Тестовое уведомление MARS|Production SITE-002 не затронут|bzpm\.ru/.test(text)) {
    pass(gates, 'message_contract_markers', 'present_in_expression');
  } else {
    fail(gates, 'message_contract_markers', 'missing');
  }

  if (/parse_mode|MarkdownV2|inline_keyboard|callback/i.test(JSON.stringify(tg?.parameters || {}))) {
    fail(gates, 'no_rich_telegram_features', 'present');
  } else {
    pass(gates, 'no_rich_telegram_features', 'clean');
  }

  const failed = gates.filter((g) => !g.ok);
  console.log(
    JSON.stringify(
      {
        validator: 'validate-client-ops-telegram-sandbox-put-payload',
        payload_path: payloadPath.replace(/\\/g, '/'),
        pass_count: gates.filter((g) => g.ok).length,
        fail_count: failed.length,
        gates,
        verdict: failed.length === 0 ? 'PASS' : 'FAIL',
      },
      null,
      2,
    ),
  );
  if (failed.length) process.exitCode = 2;
}

main();
