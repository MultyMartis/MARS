/**
 * Phase 1B-D6D — offline unattended integration harness (D1–D60 + DS1–DS10).
 * No network. No production mutation. Deterministic clock.
 */
import { mkdtempSync, rmSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import {
  runUnattendedProducer,
  buildBaseLifecycleCharter,
  EXIT_CODES,
  KILL_SWITCH_MODES,
} from '../runners/lib/client-ops-d6d-unattended-producer.mjs';
import {
  D6D_PRODUCER_IDENTITY,
  D6D_SITE_ID,
  HISTORICAL_PENDING_EVENT_ID,
  EXPECTED_VERSION_ID,
  REQUIRED_ABC_E_ANCESTORS,
  STALE_AFTER_SECONDS,
  COMPLETION_MARKER_FILENAME as MARKER_CONST,
} from '../runners/lib/client-ops-d6d-constants.mjs';
import {
  createMemoryFs,
  COMPLETION_MARKER_FILENAME,
  validateCompletedRun,
} from '../runners/lib/client-ops-d6d-artifact.mjs';
import { emptyCursor, CURSOR_STATES, sanitizeCursor } from '../runners/lib/client-ops-d6d-cursor.mjs';
import { evaluateRuntimeContract } from '../runners/lib/client-ops-d6d-runtime-gates.mjs';
import { buildProducerReceipt, assertSanitized } from '../runners/lib/client-ops-d6d-receipt.mjs';
import { acquireProducerLock } from '../runners/lib/client-ops-d6d-producer-lock.mjs';
import {
  createOfflineLifecycleTransport,
  createDeterministicClock,
} from '../runners/lib/client-ops-lifecycle-offline-transport.mjs';
import { ALLOWED_WORKFLOW_ID } from '../runners/lib/client-ops-n8n-activation-client.mjs';

const NOW = 1_700_000_000_000;
const ROOT = 'X:\\fake\\d6d\\runs';

function assert(cond, msg) {
  if (!cond) throw new Error(msg);
}

function ks(mode, extra = {}) {
  return {
    site_id: D6D_SITE_ID,
    producer_identity: D6D_PRODUCER_IDENTITY,
    mode,
    operator_reason: extra.reason || `mode=${mode}`,
    ...extra,
  };
}

function seedRun(fs, root, runId, opts = {}) {
  const dir = `${root}\\${runId}`;
  fs.mkdir(root);
  fs.mkdir(dir);
  const classification = opts.classification || 'NO_ACTION_REQUIRED';
  const observed_at =
    opts.observed_at || new Date(NOW - (opts.ageSeconds ?? 1000) * 1000).toISOString();
  const runSummary = {
    run_id: opts.omit_run_id ? undefined : runId,
    classification,
    finished_at: opts.omit_observed ? undefined : observed_at,
    captured_at: opts.omit_observed ? undefined : observed_at,
    exit_code: opts.exit_code ?? 0,
    baseline_url_count: opts.baseline ?? 100,
    current_url_count: opts.current ?? 100,
    added_count: opts.added ?? 0,
    removed_count: opts.removed ?? 0,
    onboarding_needs_count: opts.onboarding ?? 0,
  };
  if (opts.schema_version) runSummary.schema_version = opts.schema_version;
  if (opts.omit_run_id) delete runSummary.run_id;
  if (opts.omit_observed) {
    delete runSummary.finished_at;
    delete runSummary.captured_at;
  }
  const monitor = {
    classification,
    captured_at: opts.omit_observed ? undefined : observed_at,
    onboarding_needs_count: opts.onboarding ?? 0,
    added_count: opts.added ?? 0,
    removed_count: opts.removed ?? 0,
  };
  if (opts.omit_observed) delete monitor.captured_at;
  const changed = {
    baseline_url_count: opts.baseline ?? 100,
    current_url_count: opts.current ?? 100,
    added_count: opts.added ?? 0,
    removed_count: opts.removed ?? 0,
    onboarding_needs_count: opts.onboarding ?? 0,
  };
  if (opts.invalid_json) {
    fs.writeFile(`${dir}\\run-summary.json`, '{not-json');
  } else {
    fs.writeFile(`${dir}\\run-summary.json`, JSON.stringify(runSummary));
  }
  fs.writeFile(`${dir}\\monitor-classification.json`, JSON.stringify(monitor));
  fs.writeFile(`${dir}\\changed-summary.json`, JSON.stringify(changed));
  if (opts.withMarker !== false) {
    fs.writeFile(`${dir}\\${COMPLETION_MARKER_FILENAME}`, 'complete\n');
  }
  return { dir, observed_at, runId };
}

function baseInput(overrides = {}) {
  const clock = createDeterministicClock(NOW);
  const fs = createMemoryFs();
  fs.mkdir(ROOT);
  return {
    clock,
    fs,
    artifact_root: ROOT,
    allowlist_roots: [ROOT],
    kill_switch: ks(KILL_SWITCH_MODES.DRY_RUN),
    cursor: emptyCursor(),
    max_candidates_per_run: 1,
    max_safe_concurrency: 1,
    require_completion_marker: true,
    ...overrides,
    clock: overrides.clock || clock,
    fs: overrides.fs || fs,
  };
}

async function runCase(id, fn) {
  try {
    await fn();
    return { id, ok: true };
  } catch (err) {
    return { id, ok: false, error: err instanceof Error ? err.message : String(err) };
  }
}

function expectExit(result, code, extraMsg = '') {
  assert(
    result.exit_code === code,
    `${extraMsg} expected exit ${code} (${Object.entries(EXIT_CODES).find(([, v]) => v === code)?.[0]}) got ${result.exit_code} (${result.exit_class}) reasons=${JSON.stringify(result.reason_codes)}`,
  );
}

function enabledKit(opts = {}) {
  const lockDir = mkdtempSync(join(tmpdir(), 'd6d-life-'));
  const producerLock = join(lockDir, 'producer.lock');
  const lifeLock = join(lockDir, 'lifecycle.lock');
  const ledger = { ...(opts.ledger || {}) };
  const transport = createOfflineLifecycleTransport({
    id: ALLOWED_WORKFLOW_ID,
    versionId: EXPECTED_VERSION_ID,
    active: opts.active ?? false,
    nodes: 20,
    running: 0,
    executions: 34,
    seenEvents: opts.seenEvents,
  });
  if (opts.postResult) transport.setBehavior({ postResult: opts.postResult });
  if (opts.activateResult) transport.setBehavior({ activateResult: opts.activateResult });
  if (opts.deactivateResult) transport.setBehavior({ deactivateResult: opts.deactivateResult });
  if (opts.emergencyDeactivateResult) {
    transport.setBehavior({ emergencyDeactivateResult: opts.emergencyDeactivateResult });
  }
  if (opts.readinessOverride) transport.setBehavior({ readinessOverride: opts.readinessOverride });
  return {
    lockDir,
    producer_lock_path: producerLock,
    lifecycle_lock: {
      lockPath: lifeLock,
      ownerToken: `d6d-${Date.now()}`,
      processAlive: () => false,
      allowExplicitStaleRecovery: true,
    },
    transport,
    ledger,
    getLedgerRow: async (id) => ledger[id] || null,
    setLedgerRow: (id, row) => {
      ledger[id] = { ...(ledger[id] || {}), ...row };
    },
    bootstrap_boundary: opts.bootstrap_boundary || '2026-01-01T00:00:00Z',
    lifecycle_charter: buildBaseLifecycleCharter(opts.charter || {}),
    cleanup: () => {
      try {
        rmSync(lockDir, { recursive: true, force: true });
      } catch {
        /* ignore */
      }
    },
  };
}

const results = [];

// ---------------------------------------------------------------------------
// D1–D60
// ---------------------------------------------------------------------------

results.push(
  await runCase('D1', async () => {
    const r = await runUnattendedProducer(baseInput());
    expectExit(r, EXIT_CODES.SUCCESS_NO_CANDIDATE);
    assert(r.counters.webhook_calls === 0, 'no webhook');
  }),
);

results.push(
  await runCase('D2', async () => {
    const input = baseInput();
    input.fs.writeFile(`${ROOT}\\artifact.json.tmp`, '{}');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.SUCCESS_NO_CANDIDATE);
  }),
);

results.push(
  await runCase('D3', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', { invalid_json: true });
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.FAILED_LOCAL_STATE);
    assert(r.counters.webhook_calls === 0, 'no activation path');
  }),
);

results.push(
  await runCase('D4', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', { withMarker: false });
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.SUCCESS_NO_CANDIDATE);
    assert(r.not_eligible || r.reason_codes?.includes('MISSING_COMPLETION_MARKER'), 'marker');
  }),
);

results.push(
  await runCase('D5', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    let flipped = false;
    input.beforeSecondRead = () => {
      if (!flipped) {
        flipped = true;
        input.fs.writeFile(
          `${ROOT}\\2026-07-01_01-00-00\\run-summary.json`,
          JSON.stringify({
            run_id: '2026-07-01_01-00-00',
            classification: 'NO_ACTION_REQUIRED',
            finished_at: new Date(NOW - 1000 * 1000).toISOString(),
            captured_at: new Date(NOW - 1000 * 1000).toISOString(),
            exit_code: 0,
            baseline_url_count: 999,
            current_url_count: 999,
            added_count: 1,
            removed_count: 0,
            onboarding_needs_count: 0,
          }),
        );
      }
    };
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.SUCCESS_NO_CANDIDATE);
    assert(r.deferred, 'deferred unstable');
  }),
);

results.push(
  await runCase('D6', async () => {
    const input = baseInput({ force_unsupported_schema: true });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', { schema_version: 'unsupported' });
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_NOT_SAFE);
  }),
);

results.push(
  await runCase('D7', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', { omit_run_id: true });
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_NOT_SAFE);
  }),
);

results.push(
  await runCase('D8', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', { omit_observed: true });
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_NOT_SAFE);
  }),
);

results.push(
  await runCase('D9', async () => {
    const input = baseInput({ allowlist_roots: ['X:\\other\\allow'] });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.FAILED_PREFLIGHT);
  }),
);

results.push(
  await runCase('D10', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', {
      observed_at: new Date(NOW + 600_000).toISOString(),
    });
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_NOT_SAFE);
  }),
);

results.push(
  await runCase('D11', async () => {
    const input = baseInput({ kill_switch: ks(KILL_SWITCH_MODES.DISABLED) });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_KILL_SWITCH);
    assert(r.counters.webhook_calls === 0 && r.counters.activation_attempts === 0, 'no act');
  }),
);

results.push(
  await runCase('D12', async () => {
    const input = baseInput({ kill_switch: ks(KILL_SWITCH_MODES.DRY_RUN) });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.SUCCESS_DRY_RUN);
    assert(r.source_status === 'OK', 'OK');
    assert(r.counters.webhook_calls === 0, 'no request');
  }),
);

results.push(
  await runCase('D13', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', {
      classification: 'ONBOARDING_REQUIRED',
      onboarding: 2,
      added: 2,
    });
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.SUCCESS_DRY_RUN);
    assert(r.source_status === 'ATTENTION', 'ATTENTION');
  }),
);

results.push(
  await runCase('D14', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', {
      classification: 'FAILURE_REVIEW_REQUIRED',
      exit_code: 1,
    });
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_NOT_SAFE);
  }),
);

results.push(
  await runCase('D15', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', { classification: 'WEIRD_UNKNOWN' });
    const r = await runUnattendedProducer(input);
    assert(
      r.exit_code === EXIT_CODES.BLOCKED_NOT_SAFE || r.source_status === 'BLOCKED',
      'blocked factual',
    );
  }),
);

results.push(
  await runCase('D16', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', { ageSeconds: STALE_AFTER_SECONDS + 1 });
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_STALE);
    assert(r.source_status === 'OK', 'preserve OK');
  }),
);

results.push(
  await runCase('D17', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', {
      classification: 'HYGIENE_REVIEW_REQUIRED',
      ageSeconds: STALE_AFTER_SECONDS + 10,
    });
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_STALE);
    assert(r.source_status === 'ATTENTION', 'preserve ATTENTION');
    assert(r.delivery_eligibility === 'STALE_REVIEW_REQUIRED', 'stale elig');
  }),
);

results.push(
  await runCase('D18', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const a = await runUnattendedProducer(input);
    const b = await runUnattendedProducer({ ...input, cursor: emptyCursor() });
    assert(a.event_id && a.event_id === b.event_id, 'same event_id');
  }),
);

results.push(
  await runCase('D19', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const first = await runUnattendedProducer(input);
    const cursor = emptyCursor();
    cursor.evaluated_runs = {
      '2026-07-01_01-00-00': {
        artifact_hash: '0'.repeat(64),
        cursor_state: CURSOR_STATES.EVALUATED,
      },
    };
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', { added: 5 });
    const r = await runUnattendedProducer({ ...input, cursor });
    expectExit(r, EXIT_CODES.BLOCKED_CONFLICT);
    assert(first.event_id, 'had first id');
  }),
);

results.push(
  await runCase('D20', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const a = await runUnattendedProducer(input);
    const input2 = baseInput();
    seedRun(input2.fs, ROOT, '2026-07-02_01-00-00');
    const b = await runUnattendedProducer(input2);
    assert(a.event_id !== b.event_id, 'new run new id');
  }),
);

results.push(
  await runCase('D21', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const dry = await runUnattendedProducer(input);
    const cursor = emptyCursor();
    cursor.evaluated_runs = {
      '2026-07-01_01-00-00': {
        cursor_state: CURSOR_STATES.DELIVERY_TERMINAL,
        delivery_decision: 'DELIVERED',
        processing_terminal: true,
        artifact_hash: dry.artifact_hash,
      },
    };
    const r = await runUnattendedProducer({
      ...input,
      cursor,
      ledger: { [dry.event_id]: { delivery_state: 'SENT' } },
    });
    expectExit(r, EXIT_CODES.SUCCESS_ALREADY_HANDLED);
  }),
);

results.push(
  await runCase('D22', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const dry = await runUnattendedProducer(input);
    const r = await runUnattendedProducer({
      ...baseInput(),
      fs: input.fs,
      ledger: { [dry.event_id]: { delivery_state: 'SENT' } },
    });
    // re-seed same content
    seedRun(r.fs || input.fs, ROOT, '2026-07-01_01-00-00');
    const r2 = await runUnattendedProducer({
      ...baseInput(),
      fs: input.fs,
      ledger: { [dry.event_id]: { delivery_state: 'SENT' } },
    });
    expectExit(r2, EXIT_CODES.SUCCESS_ALREADY_HANDLED);
  }),
);

results.push(
  await runCase('D23', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const dry = await runUnattendedProducer(input);
    const cursor = emptyCursor();
    cursor.last_evaluated_event_id = dry.event_id;
    cursor.cursor_state = CURSOR_STATES.DELIVERY_TERMINAL;
    cursor.evaluated_runs = {
      '2026-07-01_01-00-00': {
        cursor_state: CURSOR_STATES.DELIVERY_TERMINAL,
        delivery_decision: 'DELIVERED',
        artifact_hash: dry.artifact_hash,
      },
    };
    const r = await runUnattendedProducer({ ...input, cursor, ledger: {} });
    expectExit(r, EXIT_CODES.RECONCILIATION_REQUIRED);
  }),
);

results.push(
  await runCase('D24', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const dry = await runUnattendedProducer(input);
    const r = await runUnattendedProducer({
      ...input,
      ledger: { [dry.event_id]: { delivery_state: 'PENDING' } },
    });
    expectExit(r, EXIT_CODES.RECONCILIATION_REQUIRED);
  }),
);

results.push(
  await runCase('D25', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const dry = await runUnattendedProducer(input);
    const r = await runUnattendedProducer({
      ...input,
      ledger: { [dry.event_id]: { delivery_state: 'FAILED' } },
    });
    expectExit(r, EXIT_CODES.BLOCKED_NOT_SAFE);
  }),
);

results.push(
  await runCase('D26', async () => {
    const input = baseInput({ ambiguous_no_row: true });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.RECONCILIATION_REQUIRED);
  }),
);

results.push(
  await runCase('D27', async () => {
    const lockDir = mkdtempSync(join(tmpdir(), 'd6d-plock-'));
    const lockPath = join(lockDir, 'p.lock');
    acquireProducerLock({
      lockPath,
      siteId: D6D_SITE_ID,
      producerIdentity: D6D_PRODUCER_IDENTITY,
      ownerToken: 'other',
      sessionId: 'other-session',
      runtimeCheckoutIdentity: 'x',
      nowMs: NOW,
      pid: 999001,
      processAlive: () => true,
    });
    const input = baseInput({
      producer_lock_path: lockPath,
      processAlive: () => true,
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_OVERLAP);
    rmSync(lockDir, { recursive: true, force: true });
  }),
);

results.push(
  await runCase('D28', async () => {
    const lockDir = mkdtempSync(join(tmpdir(), 'd6d-plock2-'));
    const lockPath = join(lockDir, 'p.lock');
    acquireProducerLock({
      lockPath,
      siteId: D6D_SITE_ID,
      producerIdentity: D6D_PRODUCER_IDENTITY,
      ownerToken: 'stale',
      sessionId: 'stale-session',
      runtimeCheckoutIdentity: 'x',
      nowMs: NOW - 1_000_000,
      leaseMs: 1,
      pid: 999002,
      processAlive: () => false,
    });
    const input = baseInput({
      producer_lock_path: lockPath,
      allow_stale_lock_recovery: true,
      processAlive: () => false,
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.SUCCESS_DRY_RUN);
    rmSync(lockDir, { recursive: true, force: true });
  }),
);

results.push(
  await runCase('D29', async () => {
    const kit = enabledKit();
    // pre-hold lifecycle lock with alive process
    const { acquireLifecycleLock } = await import('../runners/lib/client-ops-lifecycle-lock.mjs');
    acquireLifecycleLock({
      lockPath: kit.lifecycle_lock.lockPath,
      workflowId: ALLOWED_WORKFLOW_ID,
      charterId: 'other-charter',
      ownerToken: 'foreign',
      nowMs: NOW,
      processAlive: () => true,
      workflowActive: false,
    });
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: { ...kit.lifecycle_lock, processAlive: () => true },
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    assert(r.counters.webhook_calls === 0, 'no request');
    assert(
      r.exit_code === EXIT_CODES.FAILED_PREFLIGHT || r.exit_class === 'FAILED_PREFLIGHT',
      `lock held exit ${r.exit_class}`,
    );
    kit.cleanup();
  }),
);

results.push(
  await runCase('D30', async () => {
    const kit = enabledKit({ active: true });
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    assert(r.counters.webhook_calls === 0, 'no request');
    assert(r.exit_code !== EXIT_CODES.SUCCESS_DELIVERED, 'fail closed');
    kit.cleanup();
  }),
);

results.push(
  await runCase('D31', async () => {
    const kit = enabledKit();
    kit.transport._mutate({ versionId: 'wrong-version' });
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    assert(r.counters.webhook_calls === 0, 'no request');
    kit.cleanup();
  }),
);

results.push(
  await runCase('D32', async () => {
    const kit = enabledKit();
    kit.transport.setBehavior({
      readinessOverride: { ok: false, reason: 'READINESS_WEBHOOK_PATH_MISSING' },
    });
    // readiness is computed inside verifyReadiness — override may need webhook_path_present false
    kit.transport._mutate({ webhook_path_present: false });
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.FAILED_READINESS);
    assert(r.counters.webhook_calls === 0, 'no request');
    kit.cleanup();
  }),
);

results.push(
  await runCase('D33', async () => {
    const kit = enabledKit();
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
      beforeLifecycle: async ({ charter }) => {
        charter.source.age_seconds = STALE_AFTER_SECONDS + 5;
      },
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_STALE);
    assert(r.counters.webhook_calls === 0, 'no request');
    kit.cleanup();
  }),
);

results.push(
  await runCase('D34', async () => {
    const kit = enabledKit();
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
      beforeLifecycle: async ({ candidate, charter }) => {
        kit.transport.markEventSeen(candidate.event_id || charter.event_id, {
          intake_state: 'FIRST_SEEN',
          delivery_state: 'SENT',
        });
      },
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    assert(r.counters.webhook_calls === 0, 'no request');
    assert(
      r.exit_code === EXIT_CODES.SUCCESS_ALREADY_HANDLED ||
        r.reason_codes?.some((x) => String(x).includes('DEDUPE')),
      `dedupe before request: ${r.exit_class}`,
    );
    kit.cleanup();
  }),
);

results.push(
  await runCase('D35', async () => {
    const kit = enabledKit();
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
      beforeLifecycle: async ({ candidate, charter }) => {
        kit.transport.markEventSeen(candidate.event_id || charter.event_id, {
          intake_state: 'FIRST_SEEN',
          delivery_state: 'PENDING',
        });
      },
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    assert(r.counters.webhook_calls === 0, 'no request');
    kit.cleanup();
  }),
);

results.push(
  await runCase('D36', async () => {
    const kit = enabledKit({ postResult: { http_status: 202, class: 'HTTP_202_INTAKE_ACCEPTED' } });
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.SUCCESS_DELIVERED);
    assert(r.counters.webhook_calls === 1, 'one request');
    kit.cleanup();
  }),
);

results.push(
  await runCase('D37', async () => {
    const kit = enabledKit({ postResult: { http_status: 200, class: 'HTTP_200_DUPLICATE' } });
    let eventId = null;
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
      afterLifecycle: async ({ candidate }) => {
        eventId = candidate.event_id;
        kit.setLedgerRow(candidate.event_id, { delivery_state: 'SENT' });
      },
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.SUCCESS_ALREADY_HANDLED);
    assert(eventId, 'event');
    kit.cleanup();
  }),
);

results.push(
  await runCase('D38', async () => {
    const kit = enabledKit({ postResult: { http_status: 200, class: 'HTTP_200_DUPLICATE' } });
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
      afterLifecycle: async ({ candidate }) => {
        kit.setLedgerRow(candidate.event_id, { delivery_state: 'PENDING' });
      },
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.RECONCILIATION_REQUIRED);
    kit.cleanup();
  }),
);

results.push(
  await runCase('D39', async () => {
    const kit = enabledKit({ postResult: { http_status: 409, class: 'HTTP_409' } });
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_NOT_SAFE);
    kit.cleanup();
  }),
);

results.push(
  await runCase('D40', async () => {
    const kit = enabledKit({ postResult: { timeout: true } });
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.FAILED_REQUEST_AMBIGUOUS);
    assert(r.counters.webhook_calls === 1, 'exactly one attempt');
    kit.cleanup();
  }),
);

results.push(
  await runCase('D41', async () => {
    const input = baseInput({ telegram_success_pending: true });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.RECONCILIATION_REQUIRED);
  }),
);

results.push(
  await runCase('D42', async () => {
    const kit = enabledKit({
      postResult: { http_status: 202, class: 'HTTP_202_INTAKE_ACCEPTED' },
      deactivateResult: 'success_but_still_active',
      emergencyDeactivateResult: 'success_but_still_active',
    });
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.FAILED_CONTAINMENT);
    kit.cleanup();
  }),
);

results.push(
  await runCase('D43', async () => {
    const kit = enabledKit({ postResult: { http_status: 202, class: 'HTTP_202_INTAKE_ACCEPTED' } });
    // Force anomaly by leaving running>0 on recontain path — use allow + mutate running
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: kit.bootstrap_boundary,
      lifecycle_charter: {
        ...kit.lifecycle_charter,
        allow_running_on_recontain: true,
      },
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      getLedgerRow: kit.getLedgerRow,
      setLedgerRow: kit.setLedgerRow,
      afterLifecycle: async ({ candidate }) => {
        kit.setLedgerRow(candidate.event_id, { delivery_state: 'SENT' });
      },
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    // Inject version drift anomaly on recontain
    kit.transport.setBehavior({ versionDriftBeforeRequest: EXPECTED_VERSION_ID });
    const r = await runUnattendedProducer(input);
    assert(
      r.exit_code === EXIT_CODES.SUCCESS_DELIVERED ||
        r.delivery_state === 'SENT',
      `delivered ${r.exit_class}`,
    );
    assert(r.counters.webhook_calls <= 1, 'no retry');
    kit.cleanup();
  }),
);

results.push(
  await runCase('D44', async () => {
    const kit = enabledKit({ postResult: { http_status: 202, class: 'HTTP_202_INTAKE_ACCEPTED' } });
    const fs = createMemoryFs();
    seedRun(fs, ROOT, '2026-07-01_01-00-00');
    const ledger = {};
    const input = baseInput({
      fs,
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: 'epoch',
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      cursorWrite: 'fail_after_sent',
      getLedgerRow: async (id) => ledger[id] || null,
      setLedgerRow: (id, row) => {
        ledger[id] = { ...row };
      },
    });
    const r1 = await runUnattendedProducer(input);
    expectExit(r1, EXIT_CODES.SUCCESS_DELIVERED);
    // next scan — new transport/lock, same ledger SENT, empty cursor
    const kit2 = enabledKit();
    const r2 = await runUnattendedProducer({
      ...baseInput({ fs }),
      kill_switch: ks(KILL_SWITCH_MODES.DRY_RUN),
      ledger,
      getLedgerRow: async (id) => ledger[id] || null,
    });
    expectExit(r2, EXIT_CODES.SUCCESS_ALREADY_HANDLED);
    kit.cleanup();
    kit2.cleanup();
  }),
);

results.push(
  await runCase('D45', async () => {
    const input = baseInput({ receiptWrite: 'fail_before' });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.FAILED_LOCAL_STATE);
    assert(r.counters.activation_attempts === 0, 'no activation');
  }),
);

results.push(
  await runCase('D46', async () => {
    const kit = enabledKit({ postResult: { http_status: 202, class: 'HTTP_202_INTAKE_ACCEPTED' } });
    const ledger = {};
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: 'epoch',
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      receiptWrite: 'fail_after_terminal',
      writeReceipt: () => {},
      getLedgerRow: async (id) => ledger[id] || null,
      setLedgerRow: (id, row) => {
        ledger[id] = { ...row };
      },
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    assert(r.delivery_state === 'SENT' || r.exit_code === EXIT_CODES.SUCCESS_DELIVERED, 'ledger');
    assert(r.receipt_write_ok === false, 'receipt fail noted');
    kit.cleanup();
  }),
);

results.push(
  await runCase('D47', async () => {
    const input = baseInput();
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', { ageSeconds: 2000 });
    seedRun(input.fs, ROOT, '2026-07-02_01-00-00', { ageSeconds: 1000 });
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.SUCCESS_DRY_RUN);
    assert(r.source_run_id === '2026-07-01_01-00-00', 'oldest first');
  }),
);

results.push(
  await runCase('D48', async () => {
    const input = baseInput({ backlog_mode: true });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00', { ageSeconds: STALE_AFTER_SECONDS + 10 });
    seedRun(input.fs, ROOT, '2026-07-02_01-00-00', { ageSeconds: 1000 });
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_STALE);
    assert(r.source_run_id === '2026-07-01_01-00-00', 'stale oldest handled first');
  }),
);

results.push(
  await runCase('D49', async () => {
    const kit = enabledKit();
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      lifecycle_charter: kit.lifecycle_charter,
      transport: kit.transport,
      lifecycle_lock: kit.lifecycle_lock,
      // no bootstrap_boundary
    });
    delete input.bootstrap_boundary;
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_BOOTSTRAP);
    kit.cleanup();
  }),
);

results.push(
  await runCase('D50', async () => {
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.DRY_RUN),
      bootstrap_boundary: 'inventory',
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    seedRun(input.fs, ROOT, '2026-07-02_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.SUCCESS_DRY_RUN);
    assert(r.counters.webhook_calls === 0, 'no send');
  }),
);

results.push(
  await runCase('D51', async () => {
    const r = await runUnattendedProducer(baseInput({ kill_switch: { mode: 'YES' } }));
    expectExit(r, EXIT_CODES.BLOCKED_KILL_SWITCH);
  }),
);

results.push(
  await runCase('D52', async () => {
    const r = await runUnattendedProducer(baseInput({ kill_switch: null }));
    expectExit(r, EXIT_CODES.BLOCKED_KILL_SWITCH);
  }),
);

results.push(
  await runCase('D53', async () => {
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: 'epoch',
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.FAILED_PREFLIGHT);
  }),
);

results.push(
  await runCase('D54', async () => {
    const kit = enabledKit();
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.ENABLED),
      bootstrap_boundary: 'epoch',
      lifecycle_charter: kit.lifecycle_charter,
      retry_authorized: false,
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.FAILED_PREFLIGHT);
    kit.cleanup();
  }),
);

results.push(
  await runCase('D55', async () => {
    const r = await runUnattendedProducer(baseInput({ automatic_retry_request: true }));
    expectExit(r, EXIT_CODES.FAILED_CONFIG);
  }),
);

results.push(
  await runCase('D56', async () => {
    const r = await runUnattendedProducer(baseInput({ max_safe_concurrency: 2 }));
    expectExit(r, EXIT_CODES.FAILED_CONFIG);
  }),
);

results.push(
  await runCase('D57', async () => {
    const a = baseInput();
    seedRun(a.fs, ROOT, '2026-07-01_01-00-00');
    const r1 = await runUnattendedProducer(a);
    const b = baseInput();
    seedRun(b.fs, ROOT, '2026-07-03_01-00-00');
    const r2 = await runUnattendedProducer(b);
    assert(r1.event_id !== r2.event_id, 'new event eligible');
    expectExit(r1, EXIT_CODES.SUCCESS_DRY_RUN);
    expectExit(r2, EXIT_CODES.SUCCESS_DRY_RUN);
  }),
);

results.push(
  await runCase('D58', async () => {
    const input = baseInput({ force_event_id: HISTORICAL_PENDING_EVENT_ID });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.RECONCILIATION_REQUIRED);
    assert(r.reason_codes.includes('HISTORICAL_D5R2A_NO_RESEND'), 'historical');
  }),
);

results.push(
  await runCase('D59', async () => {
    const receipt = buildProducerReceipt({
      producer_run_id: 'p1',
      site_id: D6D_SITE_ID,
      event_id: 'e1',
      final_exit_class: 'SUCCESS_DRY_RUN',
      final_exit_code: 10,
    });
    assertSanitized(receipt);
    let threw = false;
    try {
      assertSanitized({ api_key: 'SECRETVALUE', token: 'x' });
    } catch {
      threw = true;
    }
    assert(threw, 'secrets rejected');
  }),
);

results.push(
  await runCase('D60', async () => {
    const c = emptyCursor();
    sanitizeCursor(c);
    let threw = false;
    try {
      sanitizeCursor({ ...c, webhook_url: 'https://secret' });
    } catch {
      threw = true;
    }
    assert(threw, 'cursor secrets rejected');
  }),
);

// ---------------------------------------------------------------------------
// DS1–DS10
// ---------------------------------------------------------------------------

results.push(
  await runCase('DS1', async () => {
    const r = evaluateRuntimeContract({
      workingDirectory: 'X:\\AI MARS',
      headCommit: REQUIRED_ABC_E_ANCESTORS[3],
      dirty: false,
      ancestorCommits: [...REQUIRED_ABC_E_ANCESTORS],
    });
    assert(!r.ok && r.reasons.some((x) => x.includes('MAIN')), 'reject MAIN');
  }),
);

results.push(
  await runCase('DS2', async () => {
    const r = evaluateRuntimeContract({
      workingDirectory: 'X:\\AI MARS STORAGE\\runtime-checkouts\\client-ops-site-002-producer\\repo',
      headCommit: 'unpinned',
      dirty: false,
      ancestorCommits: [...REQUIRED_ABC_E_ANCESTORS],
    });
    assert(!r.ok && r.reasons.includes('RUNTIME_COMMIT_UNPINNED'), 'unpinned');
  }),
);

results.push(
  await runCase('DS3', async () => {
    const r = evaluateRuntimeContract({
      workingDirectory: 'X:\\AI MARS STORAGE\\runtime-checkouts\\client-ops-site-002-producer\\repo',
      headCommit: REQUIRED_ABC_E_ANCESTORS[3],
      dirty: true,
      ancestorCommits: [...REQUIRED_ABC_E_ANCESTORS],
    });
    assert(!r.ok && r.reasons.includes('RUNTIME_CHECKOUT_DIRTY'), 'dirty');
  }),
);

results.push(
  await runCase('DS4', async () => {
    const r = evaluateRuntimeContract({
      workingDirectory: 'X:\\AI MARS STORAGE\\runtime-checkouts\\client-ops-site-002-producer\\repo',
      headCommit: 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
      dirty: false,
      ancestorCommits: [REQUIRED_ABC_E_ANCESTORS[0]],
    });
    assert(!r.ok && r.reasons.some((x) => x.startsWith('MISSING_ANCESTOR')), 'ancestors');
  }),
);

results.push(
  await runCase('DS5', async () => {
    const r = evaluateRuntimeContract({
      workingDirectory: 'X:\\AI MARS STORAGE\\runtime-checkouts\\client-ops-site-002-producer\\repo',
      headCommit: REQUIRED_ABC_E_ANCESTORS[3],
      dirty: false,
      ancestorCommits: [...REQUIRED_ABC_E_ANCESTORS],
      producerTaskRunning: true,
    });
    assert(!r.ok && r.reasons.includes('PRODUCER_OVERLAP_REJECTED'), 'overlap');
  }),
);

results.push(
  await runCase('DS6', async () => {
    const input = baseInput({ monitor_running: true });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.SUCCESS_NO_CANDIDATE);
    assert(r.deferred, 'defer monitor running');
  }),
);

results.push(
  await runCase('DS7', async () => {
    const input = baseInput({ monitor_running: false });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.SUCCESS_DRY_RUN);
  }),
);

results.push(
  await runCase('DS8', async () => {
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.DISABLED),
      runtime: {
        workingDirectory: 'X:\\AI MARS STORAGE\\runtime-checkouts\\client-ops-site-002-producer\\repo',
        headCommit: REQUIRED_ABC_E_ANCESTORS[3],
        dirty: false,
        ancestorCommits: [...REQUIRED_ABC_E_ANCESTORS],
        killSwitchMode: 'DISABLED',
      },
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.BLOCKED_KILL_SWITCH);
  }),
);

results.push(
  await runCase('DS9', async () => {
    const input = baseInput({
      kill_switch: ks(KILL_SWITCH_MODES.DRY_RUN),
      runtime: {
        workingDirectory: 'X:\\AI MARS STORAGE\\runtime-checkouts\\client-ops-site-002-producer\\repo',
        headCommit: REQUIRED_ABC_E_ANCESTORS[3],
        dirty: false,
        ancestorCommits: [...REQUIRED_ABC_E_ANCESTORS],
        killSwitchMode: 'DRY_RUN',
      },
    });
    seedRun(input.fs, ROOT, '2026-07-01_01-00-00');
    const r = await runUnattendedProducer(input);
    expectExit(r, EXIT_CODES.SUCCESS_DRY_RUN);
    assert(r.receipt, 'local receipt');
  }),
);

results.push(
  await runCase('DS10', async () => {
    const r = evaluateRuntimeContract({
      workingDirectory: 'X:\\AI MARS STORAGE\\runtime-checkouts\\client-ops-site-002-producer\\repo',
      headCommit: REQUIRED_ABC_E_ANCESTORS[3],
      dirty: false,
      ancestorCommits: [...REQUIRED_ABC_E_ANCESTORS],
      killSwitchMode: 'ENABLED',
      secretsPresent: false,
    });
    assert(!r.ok && r.reasons.includes('SECRETS_MISSING_IN_ENABLED_MODE'), 'secrets');
  }),
);

const d = results.filter((x) => x.id.startsWith('D') && !x.id.startsWith('DS'));
const ds = results.filter((x) => x.id.startsWith('DS'));
const summary = {
  phase: '1B-D6D',
  d_pass: d.filter((x) => x.ok).length,
  d_fail: d.filter((x) => !x.ok).length,
  ds_pass: ds.filter((x) => x.ok).length,
  ds_fail: ds.filter((x) => !x.ok).length,
  total_pass: results.filter((x) => x.ok).length,
  total_fail: results.filter((x) => !x.ok).length,
  stale_after_seconds: STALE_AFTER_SECONDS,
  marker: MARKER_CONST || COMPLETION_MARKER_FILENAME,
  failures: results.filter((x) => !x.ok),
};

console.log(JSON.stringify(summary, null, 2));
if (summary.total_fail > 0) process.exit(1);
