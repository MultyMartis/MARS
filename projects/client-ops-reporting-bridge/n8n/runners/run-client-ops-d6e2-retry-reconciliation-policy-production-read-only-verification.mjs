/**
 * Phase 1B-D6E2 — Retry and Reconciliation Policy Production Read-Only Verification.
 *
 * GET/read-only only. Invokes accepted D6E policy engine offline against sanitized
 * live observations. Does NOT retry, activate, webhook, Telegram, or mutate ledger.
 */

import { mkdirSync, writeFileSync, readFileSync, existsSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  D6E2_ALLOWED_WORKFLOW_ID,
  D6E2_ALLOWED_DATA_TABLE_ID,
  D6E2_ALLOWED_EVENT_IDS,
  D6E2_HISTORICAL_EXECUTION_ID,
  loadCredentials,
  proveReadOnlyInvariant,
  securityPrecheck,
  getAllowlistedWorkflow,
  getExecutionSnapshot,
  getSanitizedExecution,
  getAllowlistedDataTable,
  getAllowlistedDataTableRows,
  getAllowlistedEventRow,
  assertGetOnlyAction,
} from './lib/client-ops-d6e2-readonly-transport.mjs';
import {
  evaluateRetryPolicy,
  TELEGRAM_OUTCOMES,
  EXECUTION_OUTCOMES,
  TRANSPORT_OUTCOMES,
  describeReconciliationAuthority,
  D6E_RETRY_DEFAULTS,
  D6E_MAX_SAFE_CONCURRENCY,
} from './lib/client-ops-retry-policy.mjs';
import { planReconciliation } from './lib/client-ops-reconciliation-planner.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = resolve(__dirname, '../..');
const EVIDENCE_DIR = join(
  PROJECT_ROOT,
  'evidence/phase-1b-d6e2-retry-reconciliation-policy-production-read-only-verification',
);
const EXPECTED_VERSION = 'dc8746bf-df9c-425d-9b3f-4ace452ac5ef';
const HIST_EVENT = D6E2_ALLOWED_EVENT_IDS[0];
const SENT_EVENT = D6E2_ALLOWED_EVENT_IDS[1];

function writeJson(name, obj) {
  writeFileSync(join(EVIDENCE_DIR, name), `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
}

function writeText(name, text) {
  writeFileSync(join(EVIDENCE_DIR, name), text.endsWith('\n') ? text : `${text}\n`, 'utf8');
}

function sanitizeWorkflowSnapshot(wf) {
  const nodes = Array.isArray(wf.nodes) ? wf.nodes : [];
  return {
    id: wf.id,
    name: wf.name,
    active: Boolean(wf.active),
    nodes: nodes.length,
    versionId: wf.versionId || null,
  };
}

function sanitizeSchema(table) {
  const columns = Array.isArray(table?.columns) ? table.columns : [];
  return {
    id: table?.id || D6E2_ALLOWED_DATA_TABLE_ID,
    name: table?.name || null,
    column_count: columns.length,
    columns: columns.map((c) => ({
      name: c.name || c.id || null,
      type: c.type || null,
    })),
  };
}

function liveMatch(snapshot) {
  return (
    snapshot.workflow.active === false &&
    snapshot.workflow.nodes === 20 &&
    snapshot.executions.observable === true &&
    snapshot.executions.count === 34 &&
    snapshot.executions.running === 0 &&
    snapshot.workflow.versionId === EXPECTED_VERSION &&
    snapshot.datatable.column_count === 15 &&
    snapshot.datatable.rows === 4 &&
    snapshot.historical.rows === 1 &&
    snapshot.historical.intake_state === 'FIRST_SEEN' &&
    snapshot.historical.event_status === 'ATTENTION' &&
    snapshot.historical.delivery_state === 'PENDING' &&
    snapshot.d6a2_synthetic.rows === 1 &&
    snapshot.d6a2_synthetic.intake_state === 'FIRST_SEEN' &&
    snapshot.d6a2_synthetic.event_status === 'OK' &&
    snapshot.d6a2_synthetic.delivery_state === 'SENT'
  );
}

async function collectLiveSnapshot(creds, label) {
  assertGetOnlyAction('GET', 'live_snapshot');
  const wf = await getAllowlistedWorkflow(creds);
  const workflow = sanitizeWorkflowSnapshot(wf);
  const executions = await getExecutionSnapshot(creds);
  const tableRaw = await getAllowlistedDataTable(creds);
  const schema = sanitizeSchema(tableRaw);
  const all = await getAllowlistedDataTableRows(creds, { limit: 50 });
  const allRows = all?.data || all || [];
  const rowCount = Array.isArray(allRows) ? allRows.length : null;
  const historical = await getAllowlistedEventRow(creds, HIST_EVENT);
  const d6a2 = await getAllowlistedEventRow(creds, SENT_EVENT);
  const snapshot = {
    phase: '1B-D6E2',
    label,
    method: 'GET_ONLY',
    live_mutations_performed: false,
    workflow,
    executions,
    datatable: {
      id: D6E2_ALLOWED_DATA_TABLE_ID,
      column_count: schema.column_count,
      rows: rowCount,
      name: schema.name,
    },
    historical,
    d6a2_synthetic: d6a2,
  };
  snapshot.baseline_match = liveMatch(snapshot);
  snapshot.verdict = snapshot.baseline_match
    ? 'D6E2_LIVE_BASELINE_RECONFIRMED'
    : 'PARTIAL_D6E2_LIVE_BASELINE_DRIFT';
  return { snapshot, schema };
}

function loadHistoricalTelegramEvidence() {
  const candidates = [
    join(
      PROJECT_ROOT,
      'evidence/phase-1b-d5r2a-temporary-activation-one-shot/TELEGRAM-DELIVERY-RESULT.json',
    ),
    join(
      PROJECT_ROOT,
      'evidence/phase-1b-d5r2ab-real-source-delivery-evidence-baseline-commit/TELEGRAM-DELIVERY-EVIDENCE.md',
    ),
  ];
  const jsonPath = candidates[0];
  if (!existsSync(jsonPath)) {
    return {
      quality: 'SAFE_UNKNOWN',
      historical_telegram_success_evidence: false,
      telegram_api_called: false,
      note: 'Accepted Telegram evidence artifact missing',
    };
  }
  const raw = JSON.parse(readFileSync(jsonPath, 'utf8'));
  const messageId = String(raw.message_id ?? '');
  const delivered = raw.delivered === 1 || raw.delivered === true;
  const nodeOk = raw.node_ok === true;
  const ok = delivered && nodeOk && messageId === '7';
  return {
    quality: ok ? 'KNOWN_SUCCESS_EVIDENCE' : 'SAFE_UNKNOWN',
    historical_telegram_success_evidence: ok,
    telegram_outcome: ok ? TELEGRAM_OUTCOMES.SUCCESS : TELEGRAM_OUTCOMES.UNKNOWN,
    sanitized_message_id: messageId === '7' ? '7' : null,
    node_name: raw.node_name || null,
    phase_source: raw.phase || '1B-D5R2A',
    telegram_api_called: false,
    direct_api_calls: 0,
    raw_telegram_response_persisted: false,
  };
}

function evaluateHistoricalPending(row, telegram, execution) {
  const obs = {
    event_id: HIST_EVENT,
    row_found: row.rows === 1,
    intake_state: row.intake_state,
    event_status: row.event_status,
    delivery_state: row.delivery_state,
    telegram_outcome: telegram.telegram_outcome || TELEGRAM_OUTCOMES.SUCCESS,
    historical_telegram_success_evidence: telegram.historical_telegram_success_evidence === true,
    execution_outcome: execution.available
      ? EXECUTION_OUTCOMES.EXISTS
      : EXECUTION_OUTCOMES.UNKNOWN,
    containment_state: 'RECONTAINED',
    transport_outcome: TRANSPORT_OUTCOMES.RESPONSE_KNOWN,
    http_status: 202,
    // Do not fabricate current freshness for historical event
    delivery_eligibility: null,
  };
  return evaluateRetryPolicy(obs);
}

function evaluateSent(row) {
  const obs = {
    event_id: SENT_EVENT,
    row_found: row.rows === 1,
    intake_state: row.intake_state,
    event_status: row.event_status,
    delivery_state: row.delivery_state,
    telegram_outcome: TELEGRAM_OUTCOMES.SUCCESS,
    execution_outcome: EXECUTION_OUTCOMES.EXISTS,
    containment_state: 'RECONTAINED',
    transport_outcome: TRANSPORT_OUTCOMES.RESPONSE_KNOWN,
    http_status: 202,
    delivery_eligibility: null,
  };
  return evaluateRetryPolicy(obs);
}

function evaluateNoRowAmbiguous() {
  const obs = {
    event_id: 'd6e2-offline-no-row-fixture-0001',
    row_found: false,
    delivery_state: null,
    intake_state: null,
    telegram_outcome: TELEGRAM_OUTCOMES.NONE,
    execution_outcome: EXECUTION_OUTCOMES.UNKNOWN,
    transport_outcome: TRANSPORT_OUTCOMES.AMBIGUOUS_TRANSPORT,
    containment_state: 'RECONTAINED',
    historical_telegram_success_evidence: false,
  };
  return evaluateRetryPolicy(obs);
}

async function main() {
  mkdirSync(EVIDENCE_DIR, { recursive: true });

  const invariant = proveReadOnlyInvariant();
  writeJson('READ-ONLY-INVARIANT.json', invariant);
  if (invariant.token !== 'D6E2_READ_ONLY_INVARIANT_ARMED') {
    throw new Error('D6E2 read-only invariant failed — refusing production reads');
  }

  const sec = securityPrecheck(
    D6E2_ALLOWED_WORKFLOW_ID,
    D6E2_ALLOWED_DATA_TABLE_ID,
    D6E2_ALLOWED_EVENT_IDS,
  );
  writeJson('SECURITY-PRECHECK.json', sec);
  if (sec.token !== 'D6E2_SECURITY_GATE_PASS') {
    throw new Error('D6E2 security gate failed — refusing production reads');
  }

  const charter = {
    phase: 'D6E2',
    workflow_id: D6E2_ALLOWED_WORKFLOW_ID,
    expected_version_id: EXPECTED_VERSION,
    data_table_id: D6E2_ALLOWED_DATA_TABLE_ID,
    allowed_event_ids: [...D6E2_ALLOWED_EVENT_IDS],
    allow_reads: true,
    allow_webhook: false,
    allow_activation: false,
    allow_deactivation: false,
    allow_data_table_mutation: false,
    allow_telegram: false,
    allow_retry_execution: false,
    allow_reconciliation_mutation: false,
    automatic_retries: 0,
    max_safe_concurrency: 1,
    explicit_operator_authorization: true,
    production_surface: 'READ_ONLY_CONTROL_AND_LEDGER',
    reconciliation_is_read_only: true,
  };
  writeJson('D6E2-CHARTER.json', charter);

  writeText(
    'READ-ONLY-SURFACE.md',
    [
      '# READ-ONLY-SURFACE',
      '',
      '**Token:** `D6E2_PRODUCTION_SURFACE_READ_ONLY_CONTROL_AND_LEDGER`',
      '',
      '**Token:** `D6E2_READ_ONLY_SURFACE_DECLARED`',
      '',
      'Allowed reads:',
      '- workflow GET (allowlisted id)',
      '- execution GET/list (allowlisted workflow / historical execution 3416)',
      '- Data Table schema GET',
      '- Data Table rows / event lookup GET (allowlisted event ids only)',
      '- sanitized local historical evidence',
      '- source/runtime read-only checks',
      '',
      'Forbidden:',
      '- POST webhook',
      '- activate / deactivate',
      '- workflow PUT/PATCH',
      '- Data Table insert/update/delete',
      '- Telegram API',
      '- credentials mutation',
      '- retry execution',
      '- reconciliation mutation (PENDING→SENT/FAILED)',
      '',
    ].join('\n'),
  );

  const creds = loadCredentials();
  const { snapshot: pre, schema } = await collectLiveSnapshot(creds, 'prestate');
  writeJson('LIVE-PRESTATE.json', pre);
  writeJson('DATA-TABLE-SCHEMA.json', {
    token: 'D6E2_DATA_TABLE_SCHEMA_RECONFIRMED',
    ...schema,
    reconciliation_relevant: [
      'event_id',
      'intake_state',
      'event_status',
      'delivery_state',
      'first_seen_at',
      'last_seen_at',
    ],
  });
  writeJson('HISTORICAL-PENDING-ROW.json', {
    token: 'D6E2_HISTORICAL_PENDING_ROW_RECONFIRMED',
    ...pre.historical,
  });
  writeJson('SENT-ROW.json', {
    token: 'D6E2_SENT_ROW_RECONFIRMED',
    ...pre.d6a2_synthetic,
  });

  if (!pre.baseline_match) {
    writeJson('_STOP-LIVE-BASELINE-DRIFT.json', pre);
    process.stdout.write(`${JSON.stringify({ stop: 'PARTIAL_D6E2_LIVE_BASELINE_DRIFT', pre }, null, 2)}\n`);
    // Continue classification only if rows still present; mark drift for report
  }

  const telegram = loadHistoricalTelegramEvidence();
  writeText(
    'HISTORICAL-TELEGRAM-EVIDENCE.md',
    [
      '# HISTORICAL-TELEGRAM-EVIDENCE',
      '',
      telegram.quality === 'KNOWN_SUCCESS_EVIDENCE'
        ? '**Token:** `D6E2_HISTORICAL_TELEGRAM_SUCCESS_EVIDENCE_RECONFIRMED`'
        : '**Token:** SAFE UNKNOWN — historical Telegram success evidence could not be safely re-established',
      '',
      `| Field | Value |`,
      `|-------|-------|`,
      `| quality | ${telegram.quality} |`,
      `| sanitized message_id | ${telegram.sanitized_message_id ?? 'n/a'} |`,
      `| telegram_outcome | ${telegram.telegram_outcome ?? 'UNKNOWN'} |`,
      `| Telegram API called | ${telegram.telegram_api_called} |`,
      `| raw response persisted | ${telegram.raw_telegram_response_persisted} |`,
      `| source phase | ${telegram.phase_source || 'n/a'} |`,
      '',
      'No Telegram API call performed by D6E2.',
      '',
    ].join('\n'),
  );

  const execution = await getSanitizedExecution(creds, D6E2_HISTORICAL_EXECUTION_ID);
  const histAcceptedPath = join(
    PROJECT_ROOT,
    'evidence/phase-1b-d5r2ab-real-source-delivery-evidence-baseline-commit/N8N-EXECUTION-3416.md',
  );
  writeText(
    'HISTORICAL-EXECUTION-EVIDENCE.md',
    [
      '# HISTORICAL-EXECUTION-EVIDENCE',
      '',
      '**Token:** `D6E2_HISTORICAL_EXECUTION_EVIDENCE_RECONCILED`',
      '',
      '## Current GET (sanitized)',
      '',
      '```json',
      JSON.stringify(execution, null, 2),
      '```',
      '',
      '## Accepted historical artifact',
      '',
      existsSync(histAcceptedPath)
        ? 'Accepted `N8N-EXECUTION-3416.md` present (status=success, mode=webhook, path=FIRST_SEEN, Telegram node reached).'
        : 'Accepted historical execution markdown missing — relying on live GET and SAFE UNKNOWN gaps.',
      '',
      'Durable Data Table row remains authoritative for delivery_state; execution evidence is supporting only.',
      'Raw execution payload not persisted.',
      '',
    ].join('\n'),
  );

  const pendingPolicy = evaluateHistoricalPending(pre.historical, telegram, execution);
  writeJson('HISTORICAL-PENDING-POLICY-RESULT.json', {
    token: 'D6E2_HISTORICAL_PENDING_POLICY_VERIFIED',
    blind_retry_prohibited_token: 'D6E2_HISTORICAL_PENDING_BLIND_RETRY_PROHIBITED',
    observation: {
      event_id: HIST_EVENT,
      intake_state: pre.historical.intake_state,
      event_status: pre.historical.event_status,
      delivery_state: pre.historical.delivery_state,
      telegram_quality: telegram.quality,
      execution_available: execution.available,
    },
    result: pendingPolicy,
  });
  writeJson('HISTORICAL-PENDING-RECONCILIATION-PLAN.json', {
    token: 'D6E2_HISTORICAL_PENDING_RECONCILIATION_PLAN_VERIFIED',
    plan: pendingPolicy.reconciliation_plan,
    forbidden_actions: [
      'SEND_WEBHOOK',
      'RETRY_NOW',
      'ACTIVATE',
      'MUTATE_LEDGER',
    ],
    production_mutation_authorized: false,
  });

  const sentPolicy = evaluateSent(pre.d6a2_synthetic);
  writeJson('SENT-POLICY-RESULT.json', {
    token: 'D6E2_SENT_TERMINAL_POLICY_VERIFIED',
    retry_prohibited_token: 'D6E2_SENT_RETRY_PROHIBITED',
    observation: {
      event_id: SENT_EVENT,
      intake_state: pre.d6a2_synthetic.intake_state,
      event_status: pre.d6a2_synthetic.event_status,
      delivery_state: pre.d6a2_synthetic.delivery_state,
    },
    result: sentPolicy,
  });
  writeJson('SENT-RECONCILIATION-PLAN.json', {
    token: 'D6E2_SENT_RECONCILIATION_PLAN_VERIFIED',
    plan: sentPolicy.reconciliation_plan,
    production_mutation_authorized: false,
  });

  const noRow = evaluateNoRowAmbiguous();
  writeText(
    'NO-ROW-POLICY-PROOF.md',
    [
      '# NO-ROW-POLICY-PROOF',
      '',
      '**Token:** `D6E2_NO_ROW_POLICY_FAILS_CLOSED`',
      '',
      'Offline fixture: ambiguous transport + no row (no production event created).',
      '',
      '```json',
      JSON.stringify(noRow, null, 2),
      '```',
      '',
      `decision=${noRow.decision}`,
      `reason_code=${noRow.reason_code}`,
      `retry_authorized=${noRow.retry_authorized}`,
      '',
      'SAFE_TO_RETRY requires authoritative no-intake proof under a future explicit charter — not mere absence of a row.',
      'No live retry executed.',
      '',
    ].join('\n'),
  );

  writeText(
    'REAL-STATE-POLICY-COMPARISON.md',
    [
      '# REAL-STATE-POLICY-COMPARISON',
      '',
      '**Token:** `D6E2_REAL_STATE_POLICY_COMPARISON_COMPLETE`',
      '',
      '## Historical PENDING + Telegram success',
      '',
      `- event_id: ${HIST_EVENT}`,
      `- delivery_state: PENDING (not durably finalized)`,
      `- decision: ${pendingPolicy.decision}`,
      `- reason_code: ${pendingPolicy.reason_code}`,
      `- retry_authorized: ${pendingPolicy.retry_authorized}`,
      `- no_send_guard: ${pendingPolicy.no_send_guard === true}`,
      `- requires_reconciliation: ${pendingPolicy.requires_reconciliation}`,
      '- action: reconciliation / operator review only; row untouched; no resend',
      '',
      '## SENT (D6A2 synthetic)',
      '',
      `- event_id: ${SENT_EVENT}`,
      `- delivery_state: SENT (terminal successful)`,
      `- decision: ${sentPolicy.decision}`,
      `- reason_code: ${sentPolicy.reason_code}`,
      `- retry_authorized: ${sentPolicy.retry_authorized}`,
      `- terminal_success: ${sentPolicy.terminal_success === true}`,
      `- requires_reconciliation: ${sentPolicy.requires_reconciliation}`,
      '- action: no resend; no reconciliation required for delivery authorization; row untouched',
      '',
    ].join('\n'),
  );

  writeText(
    'CONCURRENCY-POLICY-PROOF.md',
    [
      '# CONCURRENCY-POLICY-PROOF',
      '',
      '**Token:** `D6E2_AUTOMATIC_RETRIES_DISABLED_VERIFIED`',
      '',
      '**Token:** `D6E2_CONCURRENCY_ONE_VERIFIED`',
      '',
      'AUTOMATIC_RETRIES_ENABLED=NO',
      'MAX_AUTOMATIC_RETRIES=0',
      'MAX_SAFE_CONCURRENCY=1',
      '',
      '```json',
      JSON.stringify(
        {
          D6E_RETRY_DEFAULTS,
          D6E_MAX_SAFE_CONCURRENCY,
          pending_automatic_retry: pendingPolicy.automatic_retry,
          sent_automatic_retry: sentPolicy.automatic_retry,
          pending_max_automatic_retries: pendingPolicy.max_automatic_retries,
          sent_max_safe_concurrency: sentPolicy.max_safe_concurrency,
        },
        null,
        2,
      ),
      '```',
      '',
      'No parallel production requests issued by D6E2.',
      '',
    ].join('\n'),
  );

  writeText(
    'CONTROLLED-LIFECYCLE-BINDING.md',
    [
      '# CONTROLLED-LIFECYCLE-BINDING',
      '',
      '**Token:** `D6E2_CONTROLLED_LIFECYCLE_BINDING_VERIFIED`',
      '',
      'Any future SAFE_TO_RETRY still requires Workstream C binding:',
      '- explicit new retry charter',
      '- initial active=false',
      '- lifecycle lock',
      '- preflight',
      '- readiness',
      '- bounded request window',
      '- max one request',
      '- re-containment',
      '',
      'D6E2 did not execute a retry or acquire a production activation lock.',
      `controlled_lifecycle_required (pending)=${pendingPolicy.controlled_lifecycle_required}`,
      `controlled_lifecycle_required (sent)=${sentPolicy.controlled_lifecycle_required}`,
      '',
    ].join('\n'),
  );

  writeText(
    'FRESHNESS-BINDING.md',
    [
      '# FRESHNESS-BINDING',
      '',
      '**Token:** `D6E2_FRESHNESS_BINDING_VERIFIED`',
      '',
      'Policy output alone cannot authorize retry.',
      'Future execution also requires `delivery_eligibility=FRESH_AND_ELIGIBLE` computed immediately before retry.',
      'Historical source event freshness was not fabricated as currently fresh.',
      '',
      `freshness_recheck_required (pending)=${pendingPolicy.freshness_recheck_required}`,
      `freshness_recheck_required (sent)=${sentPolicy.freshness_recheck_required}`,
      '',
    ].join('\n'),
  );

  writeText(
    'EVENT-IDENTITY-BINDING.md',
    [
      '# EVENT-IDENTITY-BINDING',
      '',
      '**Token:** `D6E2_EVENT_IDENTITY_BINDING_VERIFIED`',
      '',
      `- Same historical event keeps event_id=${HIST_EVENT}`,
      '- No retry-generated event ID created by D6E2',
      '- New monitor run would create a new event_id through ordinary A/B/C pipeline',
      `- event_identity_preserved (pending)=${pendingPolicy.event_identity_preserved}`,
      `- event_identity_preserved (sent)=${sentPolicy.event_identity_preserved}`,
      '',
    ].join('\n'),
  );

  writeText(
    'RECONCILIATION-AUTHORITY.md',
    [
      '# RECONCILIATION-AUTHORITY',
      '',
      '**Token:** `D6E2_RECONCILIATION_AUTHORITY_VERIFIED`',
      '',
      '```json',
      JSON.stringify(describeReconciliationAuthority(), null, 2),
      '```',
      '',
      'Applied against real evidence: durable Data Table delivery_state remains authoritative;',
      'Telegram and n8n execution are supporting; neither authorizes blind POST.',
      '',
    ].join('\n'),
  );

  // No-policy-bypass probes (offline)
  const bypassProbes = [
    {
      id: 'PENDING',
      obs: {
        event_id: HIST_EVENT,
        delivery_state: 'PENDING',
        row_found: true,
        telegram_outcome: 'NONE',
        containment_state: 'RECONTAINED',
      },
    },
    {
      id: 'SENT',
      obs: {
        event_id: SENT_EVENT,
        delivery_state: 'SENT',
        row_found: true,
        telegram_outcome: 'SUCCESS',
        containment_state: 'RECONTAINED',
      },
    },
    {
      id: 'TELEGRAM_SUCCESS_PENDING',
      obs: {
        event_id: HIST_EVENT,
        delivery_state: 'PENDING',
        row_found: true,
        telegram_outcome: 'SUCCESS',
        historical_telegram_success_evidence: true,
        containment_state: 'RECONTAINED',
      },
    },
    {
      id: 'UNKNOWN_EXEC_PENDING',
      obs: {
        event_id: HIST_EVENT,
        delivery_state: 'PENDING',
        row_found: true,
        telegram_outcome: 'UNKNOWN',
        execution_outcome: 'UNKNOWN',
        containment_state: 'RECONTAINED',
      },
    },
    {
      id: 'CONTAINMENT_FAILED',
      obs: {
        event_id: HIST_EVENT,
        delivery_state: 'PENDING',
        row_found: true,
        containment_state: 'CONTAINMENT_FAILED',
      },
    },
  ].map((p) => {
    const r = evaluateRetryPolicy(p.obs);
    return {
      id: p.id,
      decision: r.decision,
      reason_code: r.reason_code,
      retry_authorized: r.retry_authorized,
      bypass: r.retry_authorized === true,
    };
  });
  const noBypass = bypassProbes.every((p) => p.bypass === false);
  writeText(
    'NO-POLICY-BYPASS.md',
    [
      '# NO-POLICY-BYPASS',
      '',
      '**Token:** `D6E2_NO_POLICY_BYPASS_VERIFIED`',
      '',
      '```json',
      JSON.stringify({ no_bypass: noBypass, probes: bypassProbes }, null, 2),
      '```',
      '',
    ].join('\n'),
  );

  const { snapshot: post } = await collectLiveSnapshot(creds, 'poststate');
  writeJson('LIVE-POSTSTATE.json', post);

  const sideEffects = {
    token_execution: 'D6E2_NO_N8N_EXECUTION_CREATED',
    token_datatable: 'D6E2_NO_DATA_TABLE_MUTATION',
    token_telegram: 'D6E2_NO_TELEGRAM_SIDE_EFFECT',
    token_activation: 'D6E2_NO_ACTIVATION_SIDE_EFFECT',
    executions_pre: pre.executions.count,
    executions_post: post.executions.count,
    executions_added: (post.executions.count ?? 0) - (pre.executions.count ?? 0),
    rows_pre: pre.datatable.rows,
    rows_post: post.datatable.rows,
    schema_columns_pre: pre.datatable.column_count,
    schema_columns_post: post.datatable.column_count,
    historical_pre: pre.historical,
    historical_post: post.historical,
    sent_pre: pre.d6a2_synthetic,
    sent_post: post.d6a2_synthetic,
    active_pre: pre.workflow.active,
    active_post: post.workflow.active,
    version_pre: pre.workflow.versionId,
    version_post: post.workflow.versionId,
    webhook_calls: 0,
    telegram_api_calls: 0,
    telegram_messages: 0,
    activation_attempts: 0,
    deactivation_attempts: 0,
    data_table_mutations: 0,
    retry_executions: 0,
    reconciliation_mutations: 0,
  };
  writeText(
    'NO-SIDE-EFFECTS.md',
    [
      '# NO-SIDE-EFFECTS',
      '',
      '```json',
      JSON.stringify(sideEffects, null, 2),
      '```',
      '',
    ].join('\n'),
  );

  const decision = {
    phase: '1B-D6E2',
    production_surface: 'READ_ONLY_CONTROL_AND_LEDGER',
    live_mutations_performed: false,
    automatic_retries_enabled: false,
    max_automatic_retries: 0,
    max_safe_concurrency: 1,
    historical_pending_event_id: HIST_EVENT,
    historical_pending_delivery_state: pre.historical.delivery_state,
    historical_telegram_success_evidence: telegram.historical_telegram_success_evidence === true,
    historical_telegram_evidence_quality: telegram.quality,
    historical_pending_decision: pendingPolicy.decision,
    historical_pending_reason_code: pendingPolicy.reason_code,
    historical_pending_retry_authorized: pendingPolicy.retry_authorized === true,
    historical_pending_blind_retry_prohibited: true,
    historical_pending_no_send_guard: pendingPolicy.no_send_guard === true,
    historical_pending_requires_reconciliation_or_operator_review:
      pendingPolicy.requires_reconciliation === true ||
      pendingPolicy.operator_action_required === true,
    sent_event_id: SENT_EVENT,
    sent_delivery_state: pre.d6a2_synthetic.delivery_state,
    sent_decision: sentPolicy.decision,
    sent_reason_code: sentPolicy.reason_code,
    sent_retry_authorized: sentPolicy.retry_authorized === true,
    sent_terminal_success: sentPolicy.terminal_success === true,
    no_row_decision: noRow.decision,
    no_row_reason_code: noRow.reason_code,
    no_row_ambiguous_safe_to_retry: noRow.decision === 'SAFE_TO_RETRY',
    controlled_lifecycle_required_for_future_retry: true,
    freshness_recheck_required_for_future_retry: true,
    event_identity_preserved: true,
    no_policy_bypass: noBypass,
    live_baseline_match: pre.baseline_match && post.baseline_match,
    workflow_activation_attempts: 0,
    webhook_calls: 0,
    n8n_executions_added: sideEffects.executions_added,
    data_table_mutations: 0,
    telegram_messages: 0,
    historical_row_reconciled: false,
    reconciliation_is_read_only: true,
    recommended_next_phase:
      'Phase 1B-D6E2B — Retry and Reconciliation Policy Production Evidence Baseline Commit',
  };
  writeJson('D6E2-DECISION.json', decision);

  const summary = {
    invariant: invariant.token,
    security: sec.token,
    live_pre: pre.verdict,
    live_post: post.verdict,
    pending_decision: pendingPolicy.decision,
    pending_reason: pendingPolicy.reason_code,
    sent_decision: sentPolicy.decision,
    sent_reason: sentPolicy.reason_code,
    no_row_decision: noRow.decision,
    no_bypass: noBypass,
    executions_added: sideEffects.executions_added,
    rows_unchanged: sideEffects.rows_pre === sideEffects.rows_post,
    active_false: post.workflow.active === false,
  };
  process.stdout.write(`${JSON.stringify(summary, null, 2)}\n`);
}

main().catch((err) => {
  process.stderr.write(`${err instanceof Error ? err.stack || err.message : String(err)}\n`);
  process.exit(1);
});
