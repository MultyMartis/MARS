/**
 * Phase 1B-D6A — compose offline delivery-ledger workflow delta.
 * Pure composition; no live network on import.
 *
 * Applies onto the post-D1 17-node Client Ops workflow representation.
 * Does NOT mutate production; returns a put payload for future controlled apply.
 */

import { randomUUID } from 'node:crypto';
import { prepareWorkflowPutPayload } from './client-ops-n8n-workflow-update-client.mjs';
import {
  ALLOWED_WORKFLOW_ID,
  ALLOWED_WORKFLOW_NAME,
  AUTH_CRED_ID,
  TELEGRAM_NODE_NAME,
  TG_CRED_ID,
} from './client-ops-dedupe-compose.mjs';
import { DELIVERY_STATE } from './client-ops-delivery-ledger.mjs';

export const D6A_EXPECTED_NODES_PRE = 17;
export const D6A_TABLE_ID = 'H6VYhwz7RXZCBMmu';

export const DELIVERY_LEDGER_NODE_NAMES = [
  'Classify Telegram Delivery Outcome',
  'IF Delivery Finalize',
  'Delivery Ledger Finalize Update',
];

function buildIfNode(name, leftExpr, position, id) {
  return {
    parameters: {
      conditions: {
        options: {
          caseSensitive: true,
          leftValue: '',
          typeValidation: 'strict',
          version: 3,
        },
        conditions: [
          {
            id: randomUUID(),
            leftValue: leftExpr,
            rightValue: 'true',
            operator: {
              type: 'string',
              operation: 'equals',
              name: 'filter.operator.equals',
            },
          },
        ],
        combinator: 'and',
      },
      options: {},
    },
    id: id || randomUUID(),
    name,
    type: 'n8n-nodes-base.if',
    typeVersion: 2.3,
    position,
  };
}

function buildDataTableIdRef(tableId) {
  return {
    __rl: true,
    mode: 'id',
    value: tableId,
  };
}

function deliveryUpdateColumnSchema() {
  // Only delivery_state is written; schema lists match columns for filter UX.
  return [
    {
      id: 'event_id',
      displayName: 'event_id',
      required: false,
      defaultMatch: true,
      display: true,
      type: 'string',
      canBeUsedToMatch: true,
    },
    {
      id: 'delivery_state',
      displayName: 'delivery_state',
      required: false,
      defaultMatch: false,
      display: true,
      type: 'string',
      canBeUsedToMatch: true,
    },
  ];
}

function classifyTelegramCode() {
  return `// Classify Telegram Delivery Outcome — Phase 1B-D6A
// Authoritative SUCCESS requires sanitized numeric message_id and no error signal.
// Ambiguous outcomes leave delivery_state=PENDING (no finalize).
const item = $input.first();
const j = item.json || {};
const ctx = $('Prepare Dedupe Context').item.json || {};

const nodeError = Boolean(item.error) || Boolean(j.error) || j.ok === false;
const nested = (j.result && typeof j.result === 'object') ? j.result : j;
const messageIdRaw = nested.message_id != null ? nested.message_id : j.message_id;
const messageId = messageIdRaw != null ? String(messageIdRaw) : '';

let outcome = 'AMBIGUOUS';
let target = null;
let should_finalize = false;
let sanitized_error_class = null;

if (nodeError) {
  outcome = 'DEFINITE_FAILURE';
  target = 'FAILED';
  should_finalize = true;
  sanitized_error_class = 'TELEGRAM_NODE_ERROR';
} else if (messageId && /^\\d+$/.test(messageId)) {
  outcome = 'SUCCESS';
  target = 'SENT';
  should_finalize = true;
} else {
  outcome = 'AMBIGUOUS';
  target = null;
  should_finalize = false;
}

return [{
  json: {
    event_id: String(ctx.event_id || ''),
    intake_state: String(ctx.intake_state || 'FIRST_SEEN'),
    event_status: String(ctx.event_status || ''),
    telegram_outcome: outcome,
    target_delivery_state: target,
    should_finalize,
    telegram_message_id: messageId && /^\\d+$/.test(messageId) ? messageId : null,
    sanitized_error_class,
    expected_current_delivery_state: 'PENDING',
    delivery_finished_at: new Date().toISOString(),
  }
}];`;
}

/**
 * Compose D6A delivery ledger nodes onto a live/post-D1 workflow object.
 * @param {Record<string, unknown>} live
 * @param {string} tableId
 */
export function composeDeliveryLedgerPutFromLive(live, tableId = D6A_TABLE_ID) {
  if (!tableId) return { ok: false, error: 'missing_table_id' };
  if (live.name !== ALLOWED_WORKFLOW_NAME) {
    return { ok: false, error: 'workflow_name_mismatch' };
  }
  if (live.id && live.id !== ALLOWED_WORKFLOW_ID) {
    return { ok: false, error: 'workflow_id_mismatch' };
  }

  const nodes = structuredClone(live.nodes || []);
  const connections = structuredClone(live.connections || {});

  if (nodes.length !== D6A_EXPECTED_NODES_PRE) {
    return { ok: false, error: `unexpected_pre_node_count_${nodes.length}` };
  }
  for (const name of DELIVERY_LEDGER_NODE_NAMES) {
    if (nodes.some((n) => n.name === name)) {
      return { ok: false, error: `delivery_ledger_already_present_${name}` };
    }
  }

  const telegram = nodes.find((n) => n.name === TELEGRAM_NODE_NAME);
  if (!telegram) return { ok: false, error: 'missing_telegram_node' };
  if (telegram.credentials?.telegramApi?.id !== TG_CRED_ID) {
    return { ok: false, error: 'telegram_credential_mismatch' };
  }

  const webhook = nodes.find((n) => n.name === 'Webhook Intake');
  if (!webhook || webhook.parameters?.authentication !== 'headerAuth') {
    return { ok: false, error: 'header_auth_missing' };
  }
  if (webhook.credentials?.httpHeaderAuth?.id !== AUTH_CRED_ID) {
    return { ok: false, error: 'auth_credential_mismatch' };
  }

  const claim = nodes.find((n) => n.name === 'Dedupe Claim Insert');
  if (!claim) return { ok: false, error: 'missing_claim_insert' };

  // Ensure Telegram failures still reach classifier (do not abort before finalize).
  telegram.continueOnFail = true;
  telegram.onError = 'continueRegularOutput';

  const classify = {
    parameters: { jsCode: classifyTelegramCode() },
    id: randomUUID(),
    name: 'Classify Telegram Delivery Outcome',
    type: 'n8n-nodes-base.code',
    typeVersion: 2,
    position: [2880, -40],
  };

  const ifFinalize = buildIfNode(
    'IF Delivery Finalize',
    '={{ String($json.should_finalize) }}',
    [3120, -40],
  );

  const finalizeUpdate = {
    parameters: {
      resource: 'row',
      operation: 'update',
      dataTableId: buildDataTableIdRef(tableId),
      matchType: 'allConditions',
      filters: {
        conditions: [
          {
            keyName: 'event_id',
            condition: 'eq',
            keyValue: "={{ $json.event_id }}",
          },
          {
            keyName: 'delivery_state',
            condition: 'eq',
            keyValue: DELIVERY_STATE.PENDING,
          },
        ],
      },
      columns: {
        mappingMode: 'defineBelow',
        value: {
          delivery_state: '={{ $json.target_delivery_state }}',
        },
        matchingColumns: ['event_id'],
        schema: deliveryUpdateColumnSchema(),
      },
      options: {},
    },
    id: randomUUID(),
    name: 'Delivery Ledger Finalize Update',
    type: 'n8n-nodes-base.dataTable',
    typeVersion: 1.1,
    position: [3360, -120],
  };

  nodes.push(classify, ifFinalize, finalizeUpdate);

  // Rewire: Respond Accepted → Telegram → Classify → IF → Update
  connections['Respond Accepted'] = {
    main: [[{ node: TELEGRAM_NODE_NAME, type: 'main', index: 0 }]],
  };
  connections[TELEGRAM_NODE_NAME] = {
    main: [[{ node: 'Classify Telegram Delivery Outcome', type: 'main', index: 0 }]],
  };
  connections['Classify Telegram Delivery Outcome'] = {
    main: [[{ node: 'IF Delivery Finalize', type: 'main', index: 0 }]],
  };
  connections['IF Delivery Finalize'] = {
    main: [
      [{ node: 'Delivery Ledger Finalize Update', type: 'main', index: 0 }],
      [], // false: leave PENDING (ambiguous) — no Telegram retry
    ],
  };

  const put_payload = prepareWorkflowPutPayload({
    name: live.name,
    nodes,
    connections,
    settings: live.settings,
  });

  return {
    ok: true,
    expected_nodes_post: D6A_EXPECTED_NODES_PRE + DELIVERY_LEDGER_NODE_NAMES.length,
    table_id: tableId,
    schema_decision: 'D6A_EXISTING_SCHEMA_SUFFICIENT',
    finalization_placement: 'B_TELEGRAM_BRANCH_THEN_CONDITIONAL_UPDATE',
    telegram_continue_on_fail: true,
    bundle: {
      phase: '1B-D6A',
      applied: false,
      live_apply_performed: false,
      workflow_id: ALLOWED_WORKFLOW_ID,
      workflow_name: ALLOWED_WORKFLOW_NAME,
      active: false,
      pre_put_versionId: live.versionId || null,
      delivery_ledger_nodes: DELIVERY_LEDGER_NODE_NAMES,
      put_payload,
    },
  };
}

/**
 * Offline structural validation of composed D6A put payload.
 * @param {Record<string, unknown>} putPayload
 * @param {string} tableId
 */
export function validateDeliveryLedgerPutPayload(putPayload, tableId = D6A_TABLE_ID) {
  const errors = [];
  const nodes = putPayload.nodes || [];
  const connections = putPayload.connections || {};
  const names = nodes.map((n) => n.name);

  if (nodes.length !== D6A_EXPECTED_NODES_PRE + DELIVERY_LEDGER_NODE_NAMES.length) {
    errors.push(`node_count_${nodes.length}`);
  }
  for (const name of DELIVERY_LEDGER_NODE_NAMES) {
    if (!names.includes(name)) errors.push(`missing_${name}`);
  }

  const telegram = nodes.find((n) => n.name === TELEGRAM_NODE_NAME);
  if (!telegram) errors.push('missing_telegram');
  if (!telegram?.continueOnFail) errors.push('telegram_continueOnFail_required');
  if (telegram?.credentials?.telegramApi?.id !== TG_CRED_ID) errors.push('tg_cred');

  const dtNodes = nodes.filter((n) => n.type === 'n8n-nodes-base.dataTable');
  if (dtNodes.length !== 3) errors.push(`datatable_node_count_${dtNodes.length}`);

  const finalize = nodes.find((n) => n.name === 'Delivery Ledger Finalize Update');
  if (finalize?.parameters?.operation !== 'update') errors.push('finalize_not_update');
  if (finalize?.parameters?.dataTableId?.value !== tableId) errors.push('finalize_table_id');

  const filters = finalize?.parameters?.filters?.conditions || [];
  if (!filters.some((f) => f.keyName === 'event_id' && f.condition === 'eq')) {
    errors.push('finalize_missing_event_id_filter');
  }
  if (
    !filters.some(
      (f) =>
        f.keyName === 'delivery_state' &&
        f.condition === 'eq' &&
        String(f.keyValue) === DELIVERY_STATE.PENDING,
    )
  ) {
    errors.push('finalize_missing_pending_filter');
  }

  const value = finalize?.parameters?.columns?.value || {};
  const writtenKeys = Object.keys(value);
  if (!writtenKeys.includes('delivery_state')) errors.push('finalize_missing_delivery_state_write');
  for (const forbidden of [
    'intake_state',
    'event_status',
    'event_id',
    'event_fingerprint',
    'site_id',
  ]) {
    if (writtenKeys.includes(forbidden)) errors.push(`finalize_writes_${forbidden}`);
  }

  const tgTargets = connections[TELEGRAM_NODE_NAME]?.main?.[0] || [];
  if (!tgTargets.some((c) => c.node === 'Classify Telegram Delivery Outcome')) {
    errors.push('telegram_not_to_classify');
  }

  const nonFirst = connections['Respond Non-First-Seen']?.main?.[0] || [];
  if (nonFirst.some((c) => c.node === TELEGRAM_NODE_NAME)) {
    errors.push('non_first_reaches_telegram');
  }
  if (nonFirst.some((c) => DELIVERY_LEDGER_NODE_NAMES.includes(c.node))) {
    errors.push('non_first_reaches_finalizer');
  }

  const rejected = connections['Respond Rejected']?.main?.[0] || [];
  if (rejected.some((c) => c.node === TELEGRAM_NODE_NAME)) {
    errors.push('rejected_reaches_telegram');
  }

  // Pattern B preserved: Respond Accepted → Telegram
  const accepted = connections['Respond Accepted']?.main?.[0] || [];
  if (!accepted.some((c) => c.node === TELEGRAM_NODE_NAME)) {
    errors.push('pattern_b_broken');
  }

  return { ok: errors.length === 0, errors };
}
