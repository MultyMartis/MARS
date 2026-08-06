/**
 * Phase 1B-D6C2 — Controlled Activation Lifecycle Production Apply
 * and Synthetic Dry-Window Verification.
 *
 * Default: gate-only (no activation).
 *
 * Live dry lifecycle:
 *   --execute-dry-window
 *   --confirm-activate="ACTIVATE CLIENT OPS D6C BOUNDED LIFECYCLE BZPM"
 *   --confirm-deactivate="DEACTIVATE CLIENT OPS D6C BOUNDED LIFECYCLE BZPM"
 *
 * Zero webhook requests. Zero Telegram. Zero Data Table mutations.
 * No live action on module import.
 */

import { createHash, randomBytes } from 'node:crypto';
import {
  createReadStream,
  existsSync,
  mkdirSync,
  statSync,
  writeFileSync,
} from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { pipeline } from 'node:stream/promises';
import {
  getWorkflow,
  loadCredentials,
  normalizeBaseUrl,
} from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';
import {
  getDataTable,
  getDataTableRows,
  loadDataTableCredentials,
} from './lib/client-ops-n8n-datatable-client.mjs';
import {
  ALLOWED_WORKFLOW_ID,
  D6C_ACTIVATION_CONFIRM_PHRASE,
  D6C_DEACTIVATION_CONFIRM_PHRASE,
  D6C_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE,
} from './lib/client-ops-n8n-activation-client.mjs';
import {
  runBoundedActivationLifecycle,
  assertZeroRequestInvariant,
  assertWebhookRequestProhibitedByCharter,
  isDryLifecycleCharter,
  D6C_ALLOWED_WORKFLOW_ID,
  D6C_EXPECTED_VERSION_ID,
  MAX_RETRIES,
  MAX_SAFE_CONCURRENCY,
} from './lib/client-ops-activation-lifecycle.mjs';
import { readLifecycleLock } from './lib/client-ops-lifecycle-lock.mjs';
import { createProductionLifecycleTransport } from './lib/client-ops-lifecycle-production-transport.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const PROJECT = resolve(REPO_ROOT, 'projects/client-ops-reporting-bridge');
const EVIDENCE = resolve(
  PROJECT,
  'evidence/phase-1b-d6c2-controlled-activation-lifecycle-production-dry-window',
);
const LOCK_DIR = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/locks',
);
const LOCK_PATH = resolve(LOCK_DIR, 'd6c2-lifecycle.lock.json');

const TABLE_ID = 'H6VYhwz7RXZCBMmu';
const HIST_EVENT = 'c84e29bf-79b1-5aea-98c4-9dc8d651fc96';
const D6A2_EVENT = 'd6a2a001-27d6-4a2e-bd6a-000000000001';
const EXPECTED_NODES = 20;
const EXPECTED_EXEC = 34;
const EXPECTED_ROWS = 4;
const WINDOW_SECONDS = 30;

const CONTROL_TOOL_FILES = [
  'n8n/runners/lib/client-ops-activation-lifecycle.mjs',
  'n8n/runners/lib/client-ops-lifecycle-lock.mjs',
  'n8n/runners/lib/client-ops-lifecycle-offline-transport.mjs',
  'n8n/runners/lib/client-ops-lifecycle-production-transport.mjs',
  'n8n/runners/lib/client-ops-n8n-activation-client.mjs',
  'n8n/harness/d6c-activation-lifecycle-harness.mjs',
  'n8n/runners/run-client-ops-d6c2-activation-lifecycle-production-dry-window.mjs',
];

function parseArgs(argv) {
  const out = {
    executeDryWindow: false,
    confirmActivate: null,
    confirmDeactivate: null,
    confirmEmergency: null,
  };
  for (const a of argv) {
    if (a === '--execute-dry-window') out.executeDryWindow = true;
    else if (a.startsWith('--confirm-activate='))
      out.confirmActivate = a.slice('--confirm-activate='.length);
    else if (a.startsWith('--confirm-deactivate='))
      out.confirmDeactivate = a.slice('--confirm-deactivate='.length);
    else if (a.startsWith('--confirm-emergency='))
      out.confirmEmergency = a.slice('--confirm-emergency='.length);
  }
  return out;
}

function ensureDir(p) {
  mkdirSync(p, { recursive: true });
}

function writeJson(path, obj) {
  ensureDir(dirname(path));
  writeFileSync(path, `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
}

function writeText(path, text) {
  ensureDir(dirname(path));
  writeFileSync(path, text.endsWith('\n') ? text : `${text}\n`, 'utf8');
}

function wallClock() {
  return {
    nowMs() {
      return Date.now();
    },
    nowIso() {
      return new Date().toISOString().replace(/\.\d{3}Z$/, 'Z');
    },
  };
}

async function hashFile(absPath) {
  const hash = createHash('sha256');
  await pipeline(createReadStream(absPath), hash);
  return hash.digest('hex');
}

async function executionSnapshot(creds, workflowId) {
  const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions?workflowId=${encodeURIComponent(workflowId)}&limit=100`;
  const response = await fetch(url, {
    method: 'GET',
    headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
  });
  if (!response.ok) {
    return { observable: false, reason: `HTTP_${response.status}`, count: null, running: null };
  }
  const data = await response.json();
  const rows = Array.isArray(data) ? data : data?.data;
  if (!Array.isArray(rows)) {
    return { observable: false, reason: 'unexpected_shape', count: null, running: null };
  }
  return {
    observable: true,
    count: typeof data?.count === 'number' ? data.count : rows.length,
    running: rows.filter((r) => r.status === 'running').length,
  };
}

async function eventSnap(dtCreds, eventId) {
  const filtered = await getDataTableRows(dtCreds, TABLE_ID, {
    limit: 20,
    filter: { filters: [{ columnName: 'event_id', condition: 'eq', value: eventId }] },
  });
  const filterRows = filtered.data?.data || filtered.data || [];
  const eventRow = Array.isArray(filterRows) && filterRows[0] ? filterRows[0] : null;
  const rowData = eventRow?.data || eventRow || {};
  return {
    event_id: eventId,
    rows: Array.isArray(filterRows) ? filterRows.length : null,
    intake_state: rowData.intake_state ?? null,
    event_status: rowData.event_status ?? null,
    delivery_state: rowData.delivery_state ?? null,
  };
}

async function liveSnapshot() {
  const creds = loadCredentials();
  const dtCreds = loadDataTableCredentials();
  const wf = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
  const nodes = Array.isArray(wf.nodes) ? wf.nodes : [];
  const exec = await executionSnapshot(creds, ALLOWED_WORKFLOW_ID);
  const table = await getDataTable(dtCreds, TABLE_ID);
  const tableData = table.data || table;
  const columns = Array.isArray(tableData.columns) ? tableData.columns : [];
  const all = await getDataTableRows(dtCreds, TABLE_ID, { limit: 50 });
  const allRows = all.data?.data || all.data || [];
  const historical = await eventSnap(dtCreds, HIST_EVENT);
  const d6a2 = await eventSnap(dtCreds, D6A2_EVENT);
  const out = {
    phase: '1B-D6C2',
    method: 'GET_ONLY',
    captured_at: new Date().toISOString(),
    workflow: {
      id: wf.id,
      name: wf.name,
      active: Boolean(wf.active),
      nodes: nodes.length,
      versionId: wf.versionId || null,
    },
    executions: exec,
    datatable: {
      id: TABLE_ID,
      column_count: columns.length,
      rows: Array.isArray(allRows) ? allRows.length : (tableData.rowsCount ?? null),
    },
    historical,
    d6a2_synthetic: d6a2,
  };
  const match =
    out.workflow.active === false &&
    out.workflow.nodes === EXPECTED_NODES &&
    out.executions.observable &&
    out.executions.count === EXPECTED_EXEC &&
    out.executions.running === 0 &&
    out.workflow.versionId === D6C_EXPECTED_VERSION_ID &&
    out.datatable.column_count === 15 &&
    out.datatable.rows === EXPECTED_ROWS &&
    out.historical.rows === 1 &&
    out.historical.intake_state === 'FIRST_SEEN' &&
    out.historical.event_status === 'ATTENTION' &&
    out.historical.delivery_state === 'PENDING' &&
    out.d6a2_synthetic.rows === 1 &&
    out.d6a2_synthetic.intake_state === 'FIRST_SEEN' &&
    out.d6a2_synthetic.event_status === 'OK' &&
    out.d6a2_synthetic.delivery_state === 'SENT';
  out.verdict = match ? 'D6C2_LIVE_BASELINE_RECONFIRMED' : 'D6C2_LIVE_BASELINE_DRIFT';
  return out;
}

function buildCharter() {
  return {
    phase: 'D6C2',
    charter_id: `d6c2-dry-window-${new Date().toISOString().slice(0, 10)}`,
    workflow_id: D6C_ALLOWED_WORKFLOW_ID,
    expected_version_id: D6C_EXPECTED_VERSION_ID,
    expected_nodes: EXPECTED_NODES,
    required_initial_workflow_active: false,
    required_initial_active: false,
    max_requests: 1,
    planned_requests: 0,
    max_retries: 0,
    max_concurrency: 1,
    max_activation_changes: 2,
    window_seconds: WINDOW_SECONDS,
    allow_webhook_requests: false,
    allow_telegram: false,
    allow_data_table_mutation: false,
    explicit_operator_authorization: true,
    dry_control: true,
    operation_type: 'DRY_CONTROL_NO_REQUEST',
    unattended: false,
    auto_trigger: false,
    consumed: false,
  };
}

async function declareControlToolSurface() {
  const hashes = {};
  for (const rel of CONTROL_TOOL_FILES) {
    const abs = resolve(PROJECT, rel);
    if (!existsSync(abs)) {
      hashes[rel] = { present: false };
      continue;
    }
    hashes[rel] = {
      present: true,
      sha256: await hashFile(abs),
      bytes: statSync(abs).size,
    };
  }
  return {
    phase: '1B-D6C2',
    surface: 'CONTROL_TOOL_ONLY',
    declaration: 'D6C2_CONTROL_TOOL_SURFACE_DECLARED',
    note:
      'Operator-side control-plane tooling bound for production use. Not a source→runtime n8n content deployment.',
    files: hashes,
    workflow_content_mutation_required: false,
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  ensureDir(EVIDENCE);
  ensureDir(LOCK_DIR);

  const charter = buildCharter();
  writeJson(resolve(EVIDENCE, 'D6C2-CHARTER.json'), charter);

  const zeroInv = assertZeroRequestInvariant(charter, { sendRequest: false });
  writeJson(resolve(EVIDENCE, 'ZERO-REQUEST-INVARIANT.json'), {
    ...zeroInv,
    token: 'D6C2_ZERO_REQUEST_INVARIANT_ARMED',
    dry: isDryLifecycleCharter(charter),
    local_reject: assertWebhookRequestProhibitedByCharter(charter),
  });

  const controlSurface = await declareControlToolSurface();
  writeJson(resolve(EVIDENCE, 'CONTROL-TOOL-SURFACE.json'), controlSurface);

  writeJson(resolve(EVIDENCE, 'PRODUCTION-SURFACE-DECISION.json'), {
    classification: 'D6C2_PRODUCTION_SURFACE_CONTROL_TOOL_ONLY',
    workflow_content_mutations_expected: 0,
    reason:
      'Lifecycle orchestrator is operator-side/control-plane tooling; existing n8n workflow content needs no modification for dry activation lifecycle proof.',
  });

  writeText(
    resolve(EVIDENCE, 'RECONTAINMENT-PLAN.md'),
    `# D6C2 Recontainment Plan

Token: D6C2_RECONTAINMENT_PLAN_READY

- Normal deactivate authority: \`${D6C_DEACTIVATION_CONFIRM_PHRASE}\`
- GET verification after deactivate required
- Emergency containment attempts max: 1 (\`${D6C_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE}\`)
- No generic delivery retries
- No webhook during containment
- Content rollback operations expected: 0 (no content mutation)
`,
  );

  const pre = await liveSnapshot();
  writeJson(resolve(EVIDENCE, 'LIVE-PRESTATE.json'), pre);

  if (pre.verdict !== 'D6C2_LIVE_BASELINE_RECONFIRMED') {
    writeJson(resolve(EVIDENCE, 'D6C2-DECISION.json'), {
      phase: '1B-D6C2',
      readiness: 'PARTIAL_D6C2_LIVE_BASELINE_DRIFT',
      live_prestate: pre.verdict,
      execute_attempted: false,
    });
    process.stdout.write(
      `${JSON.stringify({ ok: false, stop: 'LIVE_BASELINE_DRIFT', pre }, null, 2)}\n`,
    );
    process.exitCode = 2;
    return;
  }

  if (!args.executeDryWindow) {
    process.stdout.write(
      `${JSON.stringify(
        {
          ok: true,
          mode: 'GATE_ONLY',
          message: 'Pass --execute-dry-window with confirm phrases to run production dry lifecycle',
          live_prestate: pre.verdict,
          charter_id: charter.charter_id,
          zero_request_invariant: zeroInv.ok,
        },
        null,
        2,
      )}\n`,
    );
    return;
  }

  if (args.confirmActivate !== D6C_ACTIVATION_CONFIRM_PHRASE) {
    throw new Error('Activation confirmation phrase mismatch');
  }
  if (args.confirmDeactivate !== D6C_DEACTIVATION_CONFIRM_PHRASE) {
    throw new Error('Deactivation confirmation phrase mismatch');
  }
  if (
    args.confirmEmergency &&
    args.confirmEmergency !== D6C_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE
  ) {
    throw new Error('Emergency confirmation phrase mismatch');
  }

  const existingLock = readLifecycleLock(LOCK_PATH);
  writeJson(resolve(EVIDENCE, 'LIFECYCLE-LOCK-PRESTATE.json'), {
    path_basename: 'd6c2-lifecycle.lock.json',
    existing: existingLock
      ? {
          workflow_id: existingLock.workflow_id,
          charter_id: existingLock.charter_id,
          pid: existingLock.pid,
          process_identity: existingLock.process_identity,
          created_at_ms: existingLock.created_at_ms,
          lease_expires_at_ms: existingLock.lease_expires_at_ms,
          owner_token_present: Boolean(existingLock.owner_token),
        }
      : null,
    activation_attempts_before_lock: 0,
  });

  const transport = createProductionLifecycleTransport({
    activateConfirm: args.confirmActivate,
    deactivateConfirm: args.confirmDeactivate,
    emergencyDeactivateConfirm:
      args.confirmEmergency || D6C_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE,
    allowWebhookPost: false,
  });
  const clock = wallClock();
  const ownerToken = `d6c2-${process.pid}-${randomBytes(8).toString('hex')}`;

  const result = await runBoundedActivationLifecycle({
    transport,
    clock,
    charter,
    lock: {
      lockPath: LOCK_PATH,
      ownerToken,
      processAlive: (pid) => {
        try {
          process.kill(pid, 0);
          return true;
        } catch {
          return false;
        }
      },
      allowExplicitStaleRecovery: true,
    },
    options: { sendRequest: false },
  });

  const post = await liveSnapshot();
  writeJson(resolve(EVIDENCE, 'LIVE-POSTSTATE.json'), post);

  const lockAfter = readLifecycleLock(LOCK_PATH);
  writeJson(resolve(EVIDENCE, 'LIFECYCLE-LOCK-POSTSTATE.json'), {
    lock_present: Boolean(lockAfter),
    lock: lockAfter
      ? {
          workflow_id: lockAfter.workflow_id,
          charter_id: lockAfter.charter_id,
          pid: lockAfter.pid,
          owner_token_present: Boolean(lockAfter.owner_token),
        }
      : null,
  });

  const ev = result.evidence || {};
  writeJson(resolve(EVIDENCE, 'ACTIVATION-RESULT.json'), {
    activation_attempts: ev.activation_attempts,
    activation_changes: ev.activation_changes,
    readiness: ev.readiness_result,
    anomalies: ev.anomalies,
  });
  writeJson(resolve(EVIDENCE, 'READINESS-RESULT.json'), ev.readiness_result || null);
  writeJson(resolve(EVIDENCE, 'DRY-WINDOW-RESULT.json'), {
    window_opened: ev.window_opened,
    window_opened_at_ms: ev.window_opened_at_ms,
    window_deadline_ms: ev.window_deadline_ms,
    requests_attempted: ev.requests_attempted,
    requests_used: ev.requests_used,
    planned_requests: ev.planned_requests,
    allow_webhook_requests: ev.allow_webhook_requests,
    dry_request_reject: ev.dry_request_reject || result.dry_request_reject || null,
    max_requests: 1,
  });
  writeJson(resolve(EVIDENCE, 'DEACTIVATION-RESULT.json'), {
    deactivation_attempts: ev.deactivation_attempts,
    emergency_containment_attempts: ev.emergency_containment_attempts,
    final_active: ev.final_active,
    containment_verified: ev.containment_verified,
    final_lifecycle_state: ev.final_lifecycle_state,
  });
  writeJson(resolve(EVIDENCE, 'RECONTAINMENT-RESULT.json'), {
    containment_verified: ev.containment_verified,
    final_active: ev.final_active,
    state: result.state,
    post_active: post.workflow.active,
  });

  const execPre = pre.executions.count;
  const execPost = post.executions.count;
  const rowsPre = pre.datatable.rows;
  const rowsPost = post.datatable.rows;

  const success =
    result.containment_verified === true &&
    ev.activation_attempts === 1 &&
    ev.requests_attempted === 0 &&
    ev.window_opened === true &&
    ev.readiness_result?.ok === true &&
    ev.final_active === false &&
    post.workflow.active === false &&
    !lockAfter &&
    execPre === execPost &&
    rowsPre === rowsPost &&
    Number(ev.activation_changes) === 2;

  const decision = {
    phase: '1B-D6C2',
    production_surface: 'CONTROL_TOOL_ONLY',
    workflow_content_mutated: false,
    explicit_charter: true,
    required_initial_active: false,
    initial_active_observed: pre.workflow.active,
    lifecycle_lock_acquired:
      ev.preflight_result != null ||
      ev.activation_attempts > 0 ||
      (ev.anomalies || []).some((a) => String(a).includes('LOCK')),
    preflight_passed: ev.preflight_result?.ok === true,
    activation_attempts: ev.activation_attempts,
    activation_changes: ev.activation_changes,
    readiness_verified: ev.readiness_result?.ok === true,
    request_window_opened: ev.window_opened === true,
    max_requests: 1,
    planned_requests: 0,
    requests_attempted: ev.requests_attempted,
    allow_webhook_requests: false,
    max_retries: MAX_RETRIES,
    max_concurrency: MAX_SAFE_CONCURRENCY,
    request_window_closed: true,
    deactivation_attempts: ev.deactivation_attempts,
    emergency_containment_attempts: ev.emergency_containment_attempts,
    final_active: post.workflow.active,
    containment_verified: ev.containment_verified === true && post.workflow.active === false,
    lifecycle_lock_released_after_containment: !lockAfter && ev.containment_verified === true,
    n8n_executions_added: (execPost ?? 0) - (execPre ?? 0),
    data_table_rows_added: (rowsPost ?? 0) - (rowsPre ?? 0),
    telegram_messages: 0,
    workstream_a_unchanged: true,
    workstream_b_unchanged: true,
    unattended_mode_enabled: false,
    lifecycle_state: result.state,
    success,
    recommended_next_phase:
      'Phase 1B-D6C2B — Controlled Activation Lifecycle Production Evidence Baseline Commit',
    readiness: success
      ? 'READY_FOR_D6C2_EVIDENCE_BASELINE_COMMIT'
      : ev.containment_verified
        ? 'PARTIAL_D6C2_DRY_WINDOW_VERIFICATION_FAILED'
        : 'PARTIAL_D6C2_CONTAINMENT_FAILED',
  };

  // Refine readiness classifications
  if (!ev.preflight_result?.ok && ev.activation_attempts === 0) {
    decision.readiness = 'PARTIAL_D6C2_LOCK_OR_PREFLIGHT_FAILED';
  } else if (ev.activation_attempts === 1 && ev.readiness_result && !ev.readiness_result.ok) {
    decision.readiness = 'PARTIAL_D6C2_ACTIVE_NOT_READY';
  } else if (ev.activation_attempts === 1 && !ev.readiness_result?.ok && ev.final_active !== false) {
    decision.readiness = 'PARTIAL_D6C2_ACTIVATION_FAILED';
  } else if (ev.emergency_containment_attempts > 0 && ev.containment_verified) {
    decision.readiness = 'PARTIAL_D6C2_DEACTIVATION_ANOMALY';
  } else if (!ev.containment_verified || post.workflow.active !== false) {
    decision.readiness = 'PARTIAL_D6C2_CONTAINMENT_FAILED';
  } else if (success) {
    decision.readiness = 'READY_FOR_D6C2_EVIDENCE_BASELINE_COMMIT';
  }

  writeJson(resolve(EVIDENCE, 'D6C2-DECISION.json'), decision);

  process.stdout.write(
    `${JSON.stringify(
      {
        ok: success,
        state: result.state,
        decision_readiness: decision.readiness,
        activation_attempts: ev.activation_attempts,
        activation_changes: ev.activation_changes,
        requests_attempted: ev.requests_attempted,
        final_active: post.workflow.active,
        executions_pre: execPre,
        executions_post: execPost,
        rows_pre: rowsPre,
        rows_post: rowsPost,
        lock_released: !lockAfter,
        anomalies: ev.anomalies,
      },
      null,
      2,
    )}\n`,
  );

  if (!success) process.exitCode = 3;
}

main().catch((err) => {
  process.stderr.write(
    `${JSON.stringify({ ok: false, error: err instanceof Error ? err.message : String(err) })}\n`,
  );
  process.exitCode = 1;
});
