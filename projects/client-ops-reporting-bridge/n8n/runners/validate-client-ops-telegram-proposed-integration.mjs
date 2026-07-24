/**
 * Validate proposed (inactive, not applied) Client Ops Telegram integration payload.
 *
 * Usage:
 *   node validate-client-ops-telegram-proposed-integration.mjs [--payload=PATH]
 */

import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const DEFAULT_PAYLOAD = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/apply/mars-client-ops-bridge-bzpm.telegram-sandbox.proposed.json',
);

const CREDENTIAL_NAME = 'MARS Client Ops Telegram — bzpm.ru';
const WORKFLOW_NAME = 'MARS Client Ops Bridge — bzpm.ru';
const AUTH_CRED_ID = 'WKHmPaw6QBp7WnzP';

const SECRET_PATTERNS = [
  { name: 'telegram_bot_token', re: /\b\d{6,}:[A-Za-z0-9_-]{20,}\b/ },
  { name: 'private_key', re: /BEGIN (RSA |OPENSSH )?PRIVATE KEY/i },
  {
    name: 'api_key_assignment',
    re: /\b(api[_-]?key|bot[_-]?token|accessToken)\s*[:=]\s*['"][^'"]{8,}['"]/i,
  },
  {
    name: 'telegram_api_url_with_token',
    re: /api\.telegram\.org\/bot\d+/i,
  },
  {
    name: 'client_ops_webhook_secret_assignment',
    re: /CLIENT_OPS_WEBHOOK_AUTH_SECRET\s*=\s*\S+/i,
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
  const gates = [];

  if (!existsSync(payloadPath)) {
    console.log(
      JSON.stringify(
        {
          validator: 'validate-client-ops-telegram-proposed-integration',
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
  const proposal = bundle.proposed_integration || bundle;
  const chatTarget = proposal.chat_target || {};
  const telegramNode = proposal.telegram_node || null;
  const credential = proposal.credential || {};

  if (bundle.applied === false || proposal.applied === false) {
    pass(gates, 'not_applied', 'applied=false');
  } else {
    fail(gates, 'not_applied', String(bundle.applied ?? proposal.applied));
  }

  if (bundle.workflow_name === WORKFLOW_NAME || proposal.workflow_name === WORKFLOW_NAME) {
    pass(gates, 'workflow_name', WORKFLOW_NAME);
  } else {
    fail(gates, 'workflow_name', String(bundle.workflow_name || proposal.workflow_name));
  }

  if (proposal.preserves_headerAuth === true) {
    pass(gates, 'preserves_headerAuth', 'true');
  } else {
    fail(gates, 'preserves_headerAuth', String(proposal.preserves_headerAuth));
  }

  if (proposal.preserves_auth_credential_id === AUTH_CRED_ID) {
    pass(gates, 'preserves_auth_credential', AUTH_CRED_ID);
  } else {
    fail(gates, 'preserves_auth_credential', String(proposal.preserves_auth_credential_id));
  }

  if (proposal.preserves_dedupe === 'DEDUPE_DEFERRED_SANDBOX') {
    pass(gates, 'preserves_dedupe', 'DEDUPE_DEFERRED_SANDBOX');
  } else {
    fail(gates, 'preserves_dedupe', String(proposal.preserves_dedupe));
  }

  if (proposal.remains_inactive === true) {
    pass(gates, 'remains_inactive', 'true');
  } else {
    fail(gates, 'remains_inactive', String(proposal.remains_inactive));
  }

  if (proposal.no_production_activation === true) {
    pass(gates, 'no_production_activation', 'true');
  } else {
    fail(gates, 'no_production_activation', 'false');
  }

  if (proposal.no_durable_dedupe_false_claim === true) {
    pass(gates, 'no_durable_dedupe_false_claim', 'true');
  } else {
    fail(gates, 'no_durable_dedupe_false_claim', 'false');
  }

  if (credential.name === CREDENTIAL_NAME && credential.type === 'telegramApi') {
    pass(gates, 'dedicated_credential_ref', CREDENTIAL_NAME);
  } else {
    fail(gates, 'dedicated_credential_ref', JSON.stringify(credential));
  }

  if (credential.id && credential.id !== 'UNRESOLVED' && !String(credential.id).includes('TOKEN')) {
    pass(gates, 'credential_id_present', String(credential.id));
  } else {
    fail(gates, 'credential_id_present', String(credential.id));
  }

  const chatVerdict = chatTarget.verdict || proposal.chat_target_verdict;
  if (chatVerdict === 'TELEGRAM_CHAT_TARGET_CONFIRMED' && chatTarget.chat_id != null) {
    pass(gates, 'known_chat_id', String(chatTarget.chat_id));
  } else if (chatVerdict === 'TELEGRAM_CHAT_TARGET_NOT_YET_AVAILABLE') {
    fail(gates, 'known_chat_id', 'BLOCKED_CHAT_TARGET');
  } else {
    fail(gates, 'known_chat_id', String(chatVerdict));
  }

  if (telegramNode?.type === 'n8n-nodes-base.telegram') {
    pass(gates, 'telegram_node_type', telegramNode.type);
  } else {
    fail(gates, 'telegram_node_type', String(telegramNode?.type));
  }

  if (telegramNode?.operation === 'sendMessage') {
    pass(gates, 'send_operation', 'sendMessage');
  } else {
    fail(gates, 'send_operation', String(telegramNode?.operation));
  }

  if (telegramNode?.send_count === 1) {
    pass(gates, 'one_send_only', '1');
  } else {
    fail(gates, 'one_send_only', String(telegramNode?.send_count));
  }

  if (proposal.rejects_do_not_send === true) {
    pass(gates, 'no_send_on_reject', 'true');
  } else {
    fail(gates, 'no_send_on_reject', 'false');
  }

  if (proposal.preserves_response_contract === true) {
    pass(gates, 'preserves_response_contract', 'true');
  } else {
    fail(gates, 'preserves_response_contract', 'false');
  }

  if (proposal.external_http_nodes === 0) {
    pass(gates, 'no_unknown_http', '0');
  } else {
    fail(gates, 'no_unknown_http', String(proposal.external_http_nodes));
  }

  if (proposal.contains_bot_token !== true && !SECRET_PATTERNS[0].re.test(raw)) {
    pass(gates, 'no_token_in_payload', 'clean');
  } else {
    fail(gates, 'no_token_in_payload', 'token_pattern_or_flag');
  }

  for (const p of SECRET_PATTERNS) {
    if (p.re.test(raw)) fail(gates, `secret_scan_${p.name}`, 'match');
    else pass(gates, `secret_scan_${p.name}`, 'clean');
  }

  if (proposal.integration_semantics?.pattern_b_continuation_after_respond === 'PATTERN_B_CONFIRMED') {
    pass(gates, 'semantics_pattern_b', 'PATTERN_B_CONFIRMED');
  } else if (proposal.integration_semantics?.pattern_b_continuation_after_respond === 'SAFE_UNKNOWN') {
    fail(gates, 'semantics_pattern_b', 'SAFE_UNKNOWN');
  } else if (proposal.integration_semantics?.selected === 'PATTERN_A_REQUIRED') {
    pass(gates, 'semantics_pattern_a', 'PATTERN_A_REQUIRED');
  } else {
    fail(
      gates,
      'semantics_pattern_b',
      String(proposal.integration_semantics?.pattern_b_continuation_after_respond),
    );
  }

  const failed = gates.filter((g) => !g.ok);
  const chatBlocked = failed.some((g) => g.id === 'known_chat_id' && g.detail === 'BLOCKED_CHAT_TARGET');
  const verdict =
    failed.length === 0
      ? 'PASS'
      : chatBlocked && failed.every((g) => g.id === 'known_chat_id' || g.ok)
        ? 'BLOCKED_CHAT_TARGET'
        : failed.length === 1 && chatBlocked
          ? 'BLOCKED_CHAT_TARGET'
          : 'FAIL';

  // Recalculate BLOCKED_CHAT_TARGET carefully: only chat gate failed among critical gates
  const criticalFails = failed.filter((g) => !g.id.startsWith('secret_scan_'));
  let finalVerdict = verdict;
  if (
    criticalFails.length === 1 &&
    criticalFails[0].id === 'known_chat_id' &&
    criticalFails[0].detail === 'BLOCKED_CHAT_TARGET'
  ) {
    finalVerdict = 'BLOCKED_CHAT_TARGET';
  } else if (failed.length === 0) {
    finalVerdict = 'PASS';
  } else {
    finalVerdict = 'FAIL';
  }

  console.log(
    JSON.stringify(
      {
        validator: 'validate-client-ops-telegram-proposed-integration',
        payload_path: payloadPath.replace(/\\/g, '/'),
        gates,
        pass_count: gates.filter((g) => g.ok).length,
        fail_count: failed.length,
        verdict: finalVerdict,
      },
      null,
      2,
    ),
  );
  if (finalVerdict === 'FAIL') process.exitCode = 2;
  else if (finalVerdict === 'BLOCKED_CHAT_TARGET') process.exitCode = 3;
}

main();
