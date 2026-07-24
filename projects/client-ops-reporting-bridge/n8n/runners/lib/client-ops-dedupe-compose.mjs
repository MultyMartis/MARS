/**
 * Phase 1B-D1 — compose durable dedupe workflow PUT payload (inactive).
 * Pure composition helpers; no live network on import.
 */

import { randomUUID } from 'node:crypto';
import { prepareWorkflowPutPayload } from './client-ops-n8n-workflow-update-client.mjs';
import { ALLOWED_TABLE_NAME } from './client-ops-n8n-datatable-client.mjs';

export const ALLOWED_WORKFLOW_ID = 'tkM4H0G0gM3q9Foi';
export const ALLOWED_WORKFLOW_NAME = 'MARS Client Ops Bridge — bzpm.ru';
export const EXPECTED_NODES_PRE = 10;
export const EXPECTED_VERSION_PRE = 'fc6c6801-0c0e-48b6-bdcc-4d8b4ae6c658';
export const EXPECTED_EXEC_PRE = 26;
export const EXPECTED_MAX_EXEC_ID_PRE = 3410;
export const TG_CRED_ID = '2bIC5376l7ElXb4B';
export const TG_CRED_NAME = 'MARS Client Ops Telegram — bzpm.ru';
export const AUTH_CRED_ID = 'WKHmPaw6QBp7WnzP';
export const AUTH_CRED_NAME = 'MARS Client Ops Webhook Auth — bzpm.ru';
export const TELEGRAM_NODE_NAME = 'Telegram Notify Accepted';
export const SANDBOX_MARKER = 'mars-client-ops-dedupe-sandbox-d1';
export const REDACTION_VERSION = 'd1-v1';

export const BASE_NODE_NAMES = [
  'Webhook Intake',
  'Capture Request Metadata',
  'Process Client Ops Gates',
  'IF Accepted Branch',
  'Prepare Accepted Response',
  'Prepare Rejected Response',
  'Respond Accepted',
  'Respond Rejected',
  'Sanitized Internal Evidence',
  'Telegram Notify Accepted',
];

export const DEDUPE_NODE_NAMES = [
  'Prepare Dedupe Context',
  'Dedupe Lookup',
  'Dedupe Classify',
  'IF Dedupe First Seen',
  'Dedupe Claim Insert',
  'Prepare Non-First-Seen Response',
  'Respond Non-First-Seen',
];

/**
 * Canonical fingerprint document (no secrets, no raw payload dump).
 * @param {Record<string, unknown>} body
 */
export function buildFingerprintDocument(body) {
  const site = /** @type {Record<string, unknown>} */ (body.site || {});
  const run = /** @type {Record<string, unknown>} */ (body.run || {});
  const metrics = /** @type {Record<string, unknown>} */ (body.metrics || {});
  const action = /** @type {Record<string, unknown>} */ (body.action || {});
  return {
    schema_name: body.schema_name,
    schema_version: body.schema_version,
    event_type: body.event_type,
    site_id: site.site_id,
    domain: site.domain,
    normalized_status: run.normalized_status,
    summary_code: run.summary_code,
    source_status: run.source_status,
    action_code: action.code,
    action_required: action.required,
    metrics: {
      baseline_count: metrics.baseline_count,
      current_count: metrics.current_count,
      added_urls: metrics.added_urls,
      removed_urls: metrics.removed_urls,
      onboarding_needed_count: metrics.onboarding_needed_count,
    },
  };
}

/**
 * @param {unknown} value
 */
function canonicalize(value) {
  if (value === null || typeof value !== 'object') return value;
  if (Array.isArray(value)) return value.map(canonicalize);
  const out = {};
  for (const key of Object.keys(value).sort()) {
    out[key] = canonicalize(/** @type {Record<string, unknown>} */ (value)[key]);
  }
  return out;
}

/**
 * @param {Record<string, unknown>} body
 * @returns {string} deterministic canonical fingerprint (no Node crypto; n8n Code disallows require('crypto'))
 */
export function computeEventFingerprint(body) {
  const doc = canonicalize(buildFingerprintDocument(body));
  return JSON.stringify(doc);
}

/** Compact pure helper embedded into n8n Code (no require). */
function prepareDedupeContextCode() {
  return `// Prepare Dedupe Context — Phase 1B-D1
// Deterministic fingerprint via canonical JSON (Node crypto require is disallowed on this n8n host).
// No network; no secrets; no filesystem.
const gates = $input.first().json || {};
const capture = $('Capture Request Metadata').item.json || {};
const body = capture.body || {};
const site = body.site || {};
const run = body.run || {};
const metrics = body.metrics || {};
const action = body.action || {};

function canonicalize(value) {
  if (value === null || typeof value !== 'object') return value;
  if (Array.isArray(value)) return value.map(canonicalize);
  const out = {};
  for (const key of Object.keys(value).sort()) out[key] = canonicalize(value[key]);
  return out;
}

const fingerprintDoc = canonicalize({
  schema_name: body.schema_name,
  schema_version: body.schema_version,
  event_type: body.event_type,
  site_id: site.site_id,
  domain: site.domain,
  normalized_status: run.normalized_status,
  summary_code: run.summary_code,
  source_status: run.source_status,
  action_code: action.code,
  action_required: action.required,
  metrics: {
    baseline_count: metrics.baseline_count,
    current_count: metrics.current_count,
    added_urls: metrics.added_urls,
    removed_urls: metrics.removed_urls,
    onboarding_needed_count: metrics.onboarding_needed_count,
  },
});

const event_fingerprint = JSON.stringify(fingerprintDoc);
const now = new Date().toISOString();

return [{
  json: {
    http_status: gates.http_status,
    response: gates.response,
    evidence: gates.evidence || {},
    received_at: gates.received_at || capture.received_at || null,
    event_id: String(body.event_id || ''),
    event_fingerprint,
    site_id: String(site.site_id || ''),
    schema_name: String(body.schema_name || ''),
    schema_version: String(body.schema_version || ''),
    event_type: String(body.event_type || ''),
    event_status: String(run.normalized_status || ''),
    first_seen_at: now,
    last_seen_at: now,
    intake_state: 'FIRST_SEEN',
    delivery_state: 'PENDING',
    duplicate_count: 0,
    conflict_count: 0,
    redaction_version: '${REDACTION_VERSION}',
    sandbox_marker: '${SANDBOX_MARKER}',
  }
}];`;
}

function dedupeClassifyCode() {
  return `// Dedupe Classify — Phase 1B-D1
// Reads durable lookup row (if any) vs prepared fingerprint context.
const ctx = $('Prepare Dedupe Context').item.json || {};
const row = $input.first().json || {};
const hasRow = Boolean(row && row.event_id);
const eventId = String(ctx.event_id || '');
const fp = String(ctx.event_fingerprint || '');

let classification = 'FIRST_SEEN';
if (hasRow) {
  const storedFp = String(row.event_fingerprint || '');
  if (storedFp && storedFp === fp) classification = 'DUPLICATE';
  else classification = 'EVENT_ID_CONFLICT';
}

let http_status = 202;
let response;
let evidence;

if (classification === 'FIRST_SEEN') {
  http_status = 202;
  response = {
    ok: true,
    result: 'ACCEPTED',
    event_id: eventId,
    dedupe: 'FIRST_SEEN',
  };
  evidence = {
    gate: 'dedupe',
    code: 'FIRST_SEEN',
    event_id: eventId,
  };
} else if (classification === 'DUPLICATE') {
  http_status = 200;
  response = {
    ok: true,
    result: 'DUPLICATE_SUPPRESSED',
    event_id: eventId,
    dedupe: 'DUPLICATE',
  };
  evidence = {
    gate: 'dedupe',
    code: 'DUPLICATE',
    event_id: eventId,
  };
} else {
  http_status = 409;
  response = {
    ok: false,
    result: 'EVENT_ID_CONFLICT',
    code: 'EVENT_ID_CONFLICT',
    event_id: eventId,
  };
  evidence = {
    gate: 'dedupe',
    code: 'EVENT_ID_CONFLICT',
    event_id: eventId,
  };
}

return [{
  json: {
    ...ctx,
    lookup_has_row: hasRow,
    stored_fingerprint: hasRow ? String(row.event_fingerprint || '') : null,
    stored_intake_state: hasRow ? String(row.intake_state || '') : null,
    stored_delivery_state: hasRow ? String(row.delivery_state || '') : null,
    stored_duplicate_count: hasRow ? Number(row.duplicate_count || 0) : 0,
    stored_conflict_count: hasRow ? Number(row.conflict_count || 0) : 0,
    dedupe_classification: classification,
    branch_first_seen: classification === 'FIRST_SEEN',
    branch_conflict: classification === 'EVENT_ID_CONFLICT',
    http_status,
    response,
    evidence,
  }
}];`;
}

function prepareAcceptedCode() {
  return `// Prepare Accepted Response — post-dedupe FIRST_SEEN path
const classified = $('Dedupe Classify').item.json || {};
return [{
  json: {
    http_status: classified.http_status,
    response: classified.response,
    evidence: classified.evidence || {},
    received_at: classified.received_at || null,
    dedupe_classification: classified.dedupe_classification || 'FIRST_SEEN',
  }
}];`;
}

function prepareNonFirstSeenCode() {
  return `// Prepare Non-First-Seen Response — DUPLICATE or EVENT_ID_CONFLICT
const j = $input.first().json || {};
return [{
  json: {
    http_status: j.http_status,
    response: j.response,
    evidence: j.evidence || {},
    received_at: j.received_at || null,
    dedupe_classification: j.dedupe_classification || null,
  }
}];`;
}

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

function columnSchema() {
  return [
    'event_id',
    'event_fingerprint',
    'site_id',
    'schema_name',
    'schema_version',
    'event_type',
    'event_status',
    'intake_state',
    'delivery_state',
    'first_seen_at',
    'last_seen_at',
    'duplicate_count',
    'conflict_count',
    'redaction_version',
    'sandbox_marker',
  ].map((name) => ({
    id: name,
    displayName: name,
    required: false,
    defaultMatch: name === 'event_id',
    display: true,
    type: name.includes('count') ? 'number' : 'string',
    canBeUsedToMatch: name === 'event_id',
  }));
}

/**
 * @param {Record<string, unknown>} live
 * @param {string} tableId
 */
export function composeDedupePutFromLive(live, tableId) {
  if (!tableId) return { ok: false, error: 'missing_table_id' };
  if (live.name !== ALLOWED_WORKFLOW_NAME) {
    return { ok: false, error: 'workflow_name_mismatch' };
  }
  if (live.id && live.id !== ALLOWED_WORKFLOW_ID) {
    return { ok: false, error: 'workflow_id_mismatch' };
  }

  const nodes = structuredClone(live.nodes || []);
  const connections = structuredClone(live.connections || {});

  if (nodes.length !== EXPECTED_NODES_PRE) {
    return { ok: false, error: `unexpected_pre_node_count_${nodes.length}` };
  }
  for (const name of BASE_NODE_NAMES) {
    if (!nodes.some((n) => n.name === name)) {
      return { ok: false, error: `missing_base_node_${name}` };
    }
  }
  if (nodes.some((n) => String(n.type).toLowerCase().includes('datatable'))) {
    return { ok: false, error: 'dedupe_datatable_already_present' };
  }
  if (nodes.some((n) => DEDUPE_NODE_NAMES.includes(n.name))) {
    return { ok: false, error: 'dedupe_nodes_already_present' };
  }

  const webhook = nodes.find((n) => n.name === 'Webhook Intake');
  const telegram = nodes.find((n) => n.name === TELEGRAM_NODE_NAME);
  if (!webhook || webhook.parameters?.authentication !== 'headerAuth') {
    return { ok: false, error: 'header_auth_missing' };
  }
  if (webhook.credentials?.httpHeaderAuth?.id !== AUTH_CRED_ID) {
    return { ok: false, error: 'auth_credential_mismatch' };
  }
  if (!telegram || telegram.credentials?.telegramApi?.id !== TG_CRED_ID) {
    return { ok: false, error: 'telegram_credential_mismatch' };
  }
  if (String(telegram.parameters?.chatId) !== '499423375') {
    return { ok: false, error: 'telegram_chat_mismatch' };
  }

  // Rewire accepted branch through dedupe
  if (!connections['IF Accepted Branch']?.main?.[0]?.some((c) => c.node === 'Prepare Accepted Response')) {
    return { ok: false, error: 'unexpected_accepted_branch' };
  }

  const prepareAccepted = nodes.find((n) => n.name === 'Prepare Accepted Response');
  if (!prepareAccepted) return { ok: false, error: 'missing_prepare_accepted' };
  prepareAccepted.parameters = { jsCode: prepareAcceptedCode() };

  const prepareCtx = {
    parameters: { jsCode: prepareDedupeContextCode() },
    id: randomUUID(),
    name: 'Prepare Dedupe Context',
    type: 'n8n-nodes-base.code',
    typeVersion: 2,
    position: [960, 60],
  };

  const lookup = {
    parameters: {
      resource: 'row',
      operation: 'get',
      dataTableId: buildDataTableIdRef(tableId),
      matchType: 'allConditions',
      filters: {
        conditions: [
          {
            keyName: 'event_id',
            condition: 'eq',
            keyValue: "={{ $('Prepare Dedupe Context').item.json.event_id }}",
          },
        ],
      },
      returnAll: false,
      limit: 1,
      orderBy: false,
    },
    id: randomUUID(),
    name: 'Dedupe Lookup',
    type: 'n8n-nodes-base.dataTable',
    typeVersion: 1.1,
    position: [1200, 60],
    alwaysOutputData: true,
  };

  const classify = {
    parameters: { jsCode: dedupeClassifyCode() },
    id: randomUUID(),
    name: 'Dedupe Classify',
    type: 'n8n-nodes-base.code',
    typeVersion: 2,
    position: [1440, 60],
  };

  const ifFirstSeen = buildIfNode(
    'IF Dedupe First Seen',
    '={{ String($json.branch_first_seen) }}',
    [1680, 60],
  );

  const claimInsert = {
    parameters: {
      resource: 'row',
      operation: 'insert',
      dataTableId: buildDataTableIdRef(tableId),
      columns: {
        mappingMode: 'defineBelow',
        value: {
          event_id: '={{ $json.event_id }}',
          event_fingerprint: '={{ $json.event_fingerprint }}',
          site_id: '={{ $json.site_id }}',
          schema_name: '={{ $json.schema_name }}',
          schema_version: '={{ $json.schema_version }}',
          event_type: '={{ $json.event_type }}',
          event_status: '={{ $json.event_status }}',
          intake_state: 'FIRST_SEEN',
          delivery_state: 'PENDING',
          first_seen_at: '={{ $json.first_seen_at }}',
          last_seen_at: '={{ $json.last_seen_at }}',
          duplicate_count: 0,
          conflict_count: 0,
          redaction_version: '={{ $json.redaction_version }}',
          sandbox_marker: '={{ $json.sandbox_marker }}',
        },
        schema: columnSchema(),
      },
      options: {},
    },
    id: randomUUID(),
    name: 'Dedupe Claim Insert',
    type: 'n8n-nodes-base.dataTable',
    typeVersion: 1.1,
    position: [1920, -40],
  };

  const prepareNonFirst = {
    parameters: { jsCode: prepareNonFirstSeenCode() },
    id: randomUUID(),
    name: 'Prepare Non-First-Seen Response',
    type: 'n8n-nodes-base.code',
    typeVersion: 2,
    position: [1920, 160],
  };

  const respondNonFirst = {
    parameters: {
      respondWith: 'json',
      responseBody: '={{ $json.response }}',
      options: {
        responseCode: '={{ $json.http_status }}',
      },
    },
    id: randomUUID(),
    name: 'Respond Non-First-Seen',
    type: 'n8n-nodes-base.respondToWebhook',
    typeVersion: 1.1,
    position: [2160, 160],
  };

  // Shift Prepare Accepted / Respond Accepted / Telegram slightly right visually
  prepareAccepted.position = [2160, -40];
  const respondAccepted = nodes.find((n) => n.name === 'Respond Accepted');
  if (respondAccepted) respondAccepted.position = [2400, -40];
  if (telegram) telegram.position = [2640, -40];

  nodes.push(
    prepareCtx,
    lookup,
    classify,
    ifFirstSeen,
    claimInsert,
    prepareNonFirst,
    respondNonFirst,
  );

  // Connections rewrite
  connections['IF Accepted Branch'] = {
    main: [
      [{ node: 'Prepare Dedupe Context', type: 'main', index: 0 }],
      [{ node: 'Prepare Rejected Response', type: 'main', index: 0 }],
    ],
  };
  connections['Prepare Dedupe Context'] = {
    main: [[{ node: 'Dedupe Lookup', type: 'main', index: 0 }]],
  };
  connections['Dedupe Lookup'] = {
    main: [[{ node: 'Dedupe Classify', type: 'main', index: 0 }]],
  };
  connections['Dedupe Classify'] = {
    main: [[{ node: 'IF Dedupe First Seen', type: 'main', index: 0 }]],
  };
  connections['IF Dedupe First Seen'] = {
    main: [
      [{ node: 'Dedupe Claim Insert', type: 'main', index: 0 }],
      [{ node: 'Prepare Non-First-Seen Response', type: 'main', index: 0 }],
    ],
  };
  connections['Dedupe Claim Insert'] = {
    main: [[{ node: 'Prepare Accepted Response', type: 'main', index: 0 }]],
  };
  connections['Prepare Accepted Response'] = {
    main: [[{ node: 'Respond Accepted', type: 'main', index: 0 }]],
  };
  connections['Respond Accepted'] = {
    main: [[{ node: TELEGRAM_NODE_NAME, type: 'main', index: 0 }]],
  };
  connections['Prepare Non-First-Seen Response'] = {
    main: [[{ node: 'Respond Non-First-Seen', type: 'main', index: 0 }]],
  };

  const put_payload = prepareWorkflowPutPayload({
    name: live.name,
    nodes,
    connections,
    settings: live.settings,
  });

  return {
    ok: true,
    expected_nodes_post: EXPECTED_NODES_PRE + DEDUPE_NODE_NAMES.length,
    table_name: ALLOWED_TABLE_NAME,
    table_id: tableId,
    bundle: {
      phase: '1B-D1',
      applied: false,
      workflow_id: ALLOWED_WORKFLOW_ID,
      workflow_name: ALLOWED_WORKFLOW_NAME,
      active: false,
      pre_put_versionId: live.versionId,
      dedupe_nodes: DEDUPE_NODE_NAMES,
      put_payload,
    },
  };
}

/**
 * Validate composed put payload structurally (offline).
 * @param {Record<string, unknown>} putPayload
 * @param {string} tableId
 */
export function validateDedupePutPayload(putPayload, tableId) {
  const errors = [];
  const nodes = putPayload.nodes || [];
  const connections = putPayload.connections || {};
  const names = nodes.map((n) => n.name);

  if (nodes.length !== EXPECTED_NODES_PRE + DEDUPE_NODE_NAMES.length) {
    errors.push(`node_count_${nodes.length}`);
  }
  for (const name of [...BASE_NODE_NAMES, ...DEDUPE_NODE_NAMES]) {
    if (!names.includes(name)) errors.push(`missing_${name}`);
  }

  const webhook = nodes.find((n) => n.name === 'Webhook Intake');
  if (webhook?.parameters?.authentication !== 'headerAuth') errors.push('auth_not_header');
  if (webhook?.credentials?.httpHeaderAuth?.id !== AUTH_CRED_ID) errors.push('auth_cred');

  const telegram = nodes.find((n) => n.name === TELEGRAM_NODE_NAME);
  if (telegram?.credentials?.telegramApi?.id !== TG_CRED_ID) errors.push('tg_cred');
  if (String(telegram?.parameters?.chatId) !== '499423375') errors.push('tg_chat');

  const forbidden = nodes.filter((n) =>
    ['httpRequest', 'googleSheets', 'scheduleTrigger', 'executeWorkflow'].some((f) =>
      String(n.type).includes(f),
    ),
  );
  if (forbidden.length) errors.push('forbidden_nodes');

  const dtNodes = nodes.filter((n) => n.type === 'n8n-nodes-base.dataTable');
  if (dtNodes.length !== 2) errors.push(`datatable_node_count_${dtNodes.length}`);
  for (const n of dtNodes) {
    if (n.typeVersion !== 1.1) errors.push(`datatable_typeVersion_${n.name}`);
    if (n.parameters?.dataTableId?.value !== tableId) errors.push(`datatable_id_${n.name}`);
  }

  const acceptedTargets = connections['Respond Accepted']?.main?.[0] || [];
  if (!acceptedTargets.some((c) => c.node === TELEGRAM_NODE_NAME)) {
    errors.push('pattern_b_broken');
  }
  const nonFirstTargets = connections['Respond Non-First-Seen']?.main?.[0] || [];
  if (nonFirstTargets.some((c) => c.node === TELEGRAM_NODE_NAME)) {
    errors.push('non_first_reaches_telegram');
  }
  const rejectedTargets = connections['Respond Rejected']?.main?.[0] || [];
  if (rejectedTargets.some((c) => c.node === TELEGRAM_NODE_NAME)) {
    errors.push('rejected_reaches_telegram');
  }

  // FIRST_SEEN path must go through claim before respond/telegram
  const ifFs = connections['IF Dedupe First Seen']?.main?.[0] || [];
  if (!ifFs.some((c) => c.node === 'Dedupe Claim Insert')) {
    errors.push('first_seen_bypasses_claim');
  }
  const claim = connections['Dedupe Claim Insert']?.main?.[0] || [];
  if (!claim.some((c) => c.node === 'Prepare Accepted Response')) {
    errors.push('claim_not_to_prepare_accepted');
  }

  // Accepted branch must enter dedupe before prepare accepted
  const ifAcc = connections['IF Accepted Branch']?.main?.[0] || [];
  if (!ifAcc.some((c) => c.node === 'Prepare Dedupe Context')) {
    errors.push('accepted_bypasses_dedupe');
  }
  if (ifAcc.some((c) => c.node === 'Prepare Accepted Response')) {
    errors.push('accepted_direct_to_prepare');
  }

  return { ok: errors.length === 0, errors };
}
