/**
 * Phase 1B-D6E — offline retry/concurrency policy harness (E1–E40 + EC1–EC10).
 * No network. No production mutation. Deterministic clock (no sleep).
 */

import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  evaluateRetryPolicy,
  RETRY_DECISIONS,
  TRANSPORT_OUTCOMES,
  TELEGRAM_OUTCOMES,
  EXECUTION_OUTCOMES,
  PRE_TX_CLASSES,
  REQUEST_STAGES,
  DELIVERY_STATE,
  DELIVERY_ELIGIBILITY,
  MAX_RETRIES,
  MAX_SAFE_CONCURRENCY,
  sanitizeEvidence,
  describeReconciliationAuthority,
  describeFailureBoundaries,
  describeRetryDecisionModel,
} from '../runners/lib/client-ops-retry-policy.mjs';
import { buildRetryCharterTemplate, validateRetryCharter } from '../runners/lib/client-ops-retry-charter.mjs';
import {
  evaluateConcurrencyPolicy,
  tryAcquireExclusiveLifecycleOwnership,
  describeConcurrencyModel,
  D6E_MAX_SAFE_CONCURRENCY,
} from '../runners/lib/client-ops-concurrency-policy.mjs';
import { createDeterministicClock } from '../runners/lib/client-ops-lifecycle-offline-transport.mjs';
import { REASON_CODES } from '../runners/lib/client-ops-retry-reason-codes.mjs';
import { planReconciliation } from '../runners/lib/client-ops-reconciliation-planner.mjs';
import { ALLOWED_WORKFLOW_ID } from '../runners/lib/client-ops-n8n-activation-client.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));

function assert(cond, label) {
  if (!cond) throw new Error(label);
}

function runCase(id, fn) {
  try {
    fn();
    return { id, ok: true };
  } catch (err) {
    return { id, ok: false, error: err instanceof Error ? err.message : String(err) };
  }
}

async function runAsyncCase(id, fn) {
  const dir = mkdtempSync(join(tmpdir(), 'd6e-lock-'));
  try {
    await fn(dir);
    return { id, ok: true };
  } catch (err) {
    return { id, ok: false, error: err instanceof Error ? err.message : String(err) };
  } finally {
    try {
      rmSync(dir, { recursive: true, force: true });
    } catch {
      /* ignore */
    }
  }
}

const results = [];
const clock = createDeterministicClock(1_700_000_000_000);

function expectDecision(obs, decision, reasonIncludes = null) {
  const r = evaluateRetryPolicy(obs);
  assert(r.decision === decision, `expected ${decision} got ${r.decision} (${r.reason_code})`);
  assert(r.automatic_retry === false, 'automatic_retry must be false');
  assert(r.retry_authorized === false || decision === RETRY_DECISIONS.SAFE_TO_RETRY, 'retry_authorized default');
  // Even SAFE_TO_RETRY stays unauthorized without full charter path that still keeps auto=false
  assert(r.retry_authorized === false, 'D6E never sets retry_authorized true for execution');
  assert(r.max_automatic_retries === 0, 'max_automatic_retries');
  assert(r.max_safe_concurrency === 1, 'max_safe_concurrency');
  if (reasonIncludes) {
    assert(
      String(r.reason_code).includes(reasonIncludes) || r.reason_code === reasonIncludes,
      `reason ${r.reason_code} vs ${reasonIncludes}`,
    );
  }
  return r;
}

// ---------------------------------------------------------------------------
// E1–E40
// ---------------------------------------------------------------------------

results.push(
  runCase('E1', () => {
    expectDecision(
      {
        event_id: 'e1',
        transport_outcome: TRANSPORT_OUTCOMES.PRE_TRANSMISSION_FAILURE,
        request_stage: REQUEST_STAGES.BEFORE_CONSTRUCTION,
        pre_transmission_class: PRE_TX_CLASSES.SEMANTIC,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'PRE_TRANSMISSION_SEMANTIC',
    );
  }),
);

results.push(
  runCase('E2', () => {
    const r = expectDecision(
      {
        event_id: 'e2',
        transport_outcome: TRANSPORT_OUTCOMES.PRE_TRANSMISSION_FAILURE,
        request_stage: REQUEST_STAGES.CONSTRUCTED_NOT_TRANSMITTED,
        pre_transmission_class: PRE_TX_CLASSES.TRANSIENT,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.SAFE_TO_RETRY,
      'PRE_TRANSMISSION_TRANSIENT',
    );
    assert(r.requires_new_charter === true, 'new charter required');
    assert(r.charter_rejected === true, 'no charter present');
  }),
);

results.push(
  runCase('E3', () => {
    expectDecision(
      {
        event_id: 'e3',
        transport_outcome: TRANSPORT_OUTCOMES.AMBIGUOUS_TRANSPORT,
        request_stage: REQUEST_STAGES.TRANSMISSION_AMBIGUOUS,
        http_status: null,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
      'AMBIGUOUS',
    );
  }),
);

results.push(
  runCase('E4', () => {
    expectDecision(
      {
        event_id: 'e4',
        transport_outcome: TRANSPORT_OUTCOMES.AMBIGUOUS_TRANSPORT,
        request_stage: REQUEST_STAGES.TRANSMISSION_AMBIGUOUS,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
    );
  }),
);

results.push(
  runCase('E5', () => {
    const r = expectDecision(
      {
        event_id: 'e5',
        transport_outcome: TRANSPORT_OUTCOMES.RESPONSE_KNOWN,
        http_status: 202,
        delivery_state: DELIVERY_STATE.SENT,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.UNSAFE_TO_RETRY,
      'SENT',
    );
    assert(r.terminal_success === true, 'terminal success');
  }),
);

results.push(
  runCase('E6', () => {
    expectDecision(
      {
        event_id: 'e6',
        http_status: 202,
        delivery_state: DELIVERY_STATE.PENDING,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
      '202_PENDING',
    );
  }),
);

results.push(
  runCase('E7', () => {
    expectDecision(
      {
        event_id: 'e7',
        http_status: 202,
        delivery_state: DELIVERY_STATE.FAILED,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'FAILED',
    );
  }),
);

results.push(
  runCase('E8', () => {
    expectDecision(
      {
        event_id: 'e8',
        http_status: 200,
        delivery_state: DELIVERY_STATE.SENT,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.UNSAFE_TO_RETRY,
      'SENT',
    );
  }),
);

results.push(
  runCase('E9', () => {
    expectDecision(
      {
        event_id: 'e9',
        http_status: 200,
        delivery_state: DELIVERY_STATE.PENDING,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
      'DUPLICATE_PENDING',
    );
  }),
);

results.push(
  runCase('E10', () => {
    expectDecision(
      {
        event_id: 'e10',
        http_status: 200,
        delivery_state: DELIVERY_STATE.FAILED,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
    );
  }),
);

results.push(
  runCase('E11', () => {
    expectDecision(
      {
        event_id: 'e11',
        transport_outcome: TRANSPORT_OUTCOMES.RESPONSE_KNOWN,
        http_status: 409,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'CONFLICT',
    );
  }),
);

results.push(
  runCase('E12', () => {
    expectDecision(
      {
        event_id: 'e12',
        transport_outcome: TRANSPORT_OUTCOMES.RESPONSE_KNOWN,
        http_status: 401,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'AUTH',
    );
    expectDecision(
      {
        event_id: 'e12b',
        transport_outcome: TRANSPORT_OUTCOMES.RESPONSE_KNOWN,
        http_status: 403,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'AUTH',
    );
  }),
);

results.push(
  runCase('E13', () => {
    expectDecision(
      {
        event_id: 'e13',
        transport_outcome: TRANSPORT_OUTCOMES.RESPONSE_KNOWN,
        http_status: 404,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'WORKFLOW_INACTIVE',
    );
  }),
);

results.push(
  runCase('E14', () => {
    expectDecision(
      {
        event_id: 'e14',
        transport_outcome: TRANSPORT_OUTCOMES.RESPONSE_KNOWN,
        http_status: 400,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'VALIDATION',
    );
    expectDecision(
      {
        event_id: 'e14b',
        transport_outcome: TRANSPORT_OUTCOMES.RESPONSE_KNOWN,
        http_status: 422,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'VALIDATION',
    );
  }),
);

results.push(
  runCase('E15', () => {
    expectDecision(
      {
        event_id: 'e15',
        transport_outcome: TRANSPORT_OUTCOMES.RESPONSE_KNOWN,
        http_status: 500,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
      '5XX',
    );
  }),
);

results.push(
  runCase('E16', () => {
    expectDecision(
      {
        event_id: 'e16',
        transport_outcome: TRANSPORT_OUTCOMES.AMBIGUOUS_TRANSPORT,
        row_found: false,
        execution_outcome: EXECUTION_OUTCOMES.UNKNOWN,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
      'NO_ROW_AMBIGUOUS',
    );
  }),
);

results.push(
  runCase('E17', () => {
    const r = expectDecision(
      {
        event_id: 'e17',
        transport_outcome: TRANSPORT_OUTCOMES.AMBIGUOUS_TRANSPORT,
        row_found: false,
        execution_outcome: EXECUTION_OUTCOMES.AUTHORITATIVE_NO_INTAKE,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.SAFE_TO_RETRY,
      'AUTHORITATIVE_NO_INTAKE',
    );
    assert(r.requires_new_charter === true, 'charter still required');
  }),
);

results.push(
  runCase('E18', () => {
    expectDecision(
      {
        event_id: 'e18',
        delivery_state: DELIVERY_STATE.PENDING,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
      'PENDING',
    );
  }),
);

results.push(
  runCase('E19', () => {
    expectDecision(
      {
        event_id: 'e19',
        delivery_state: DELIVERY_STATE.SENT,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.UNSAFE_TO_RETRY,
      'SENT',
    );
  }),
);

results.push(
  runCase('E20', () => {
    expectDecision(
      {
        event_id: 'e20',
        delivery_state: DELIVERY_STATE.FAILED,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'FAILED',
    );
  }),
);

results.push(
  runCase('E21', () => {
    const r = expectDecision(
      {
        event_id: 'e21',
        delivery_state: DELIVERY_STATE.PENDING,
        telegram_outcome: TELEGRAM_OUTCOMES.SUCCESS,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.UNSAFE_TO_RETRY,
      'TELEGRAM_SUCCESS',
    );
    assert(r.no_send_guard === true, 'no-send guard');
  }),
);

results.push(
  runCase('E22', () => {
    expectDecision(
      {
        event_id: 'e22',
        delivery_state: DELIVERY_STATE.PENDING,
        telegram_outcome: TELEGRAM_OUTCOMES.UNKNOWN,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
      'TELEGRAM_UNKNOWN',
    );
  }),
);

results.push(
  runCase('E23', () => {
    expectDecision(
      {
        event_id: 'e23',
        delivery_state: DELIVERY_STATE.FAILED,
        telegram_outcome: TELEGRAM_OUTCOMES.DEFINITE_FAILURE,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'TELEGRAM_FAILED',
    );
  }),
);

results.push(
  runCase('E24', () => {
    expectDecision(
      {
        event_id: 'e24',
        containment_state: 'CONTAINMENT_FAILED',
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'CONTAINMENT_FAILED',
    );
  }),
);

results.push(
  runCase('E25', () => {
    expectDecision(
      {
        event_id: 'e25',
        containment_state: 'RECONTAINED_WITH_ANOMALY',
        delivery_state: DELIVERY_STATE.SENT,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.UNSAFE_TO_RETRY,
      'ANOMALY_SENT',
    );
  }),
);

results.push(
  runCase('E26', () => {
    expectDecision(
      {
        event_id: 'e26',
        containment_state: 'RECONTAINED_WITH_ANOMALY',
        delivery_state: DELIVERY_STATE.PENDING,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
      'ANOMALY_PENDING',
    );
  }),
);

results.push(
  runCase('E27', () => {
    const r = expectDecision(
      {
        event_id: 'e27',
        transport_outcome: TRANSPORT_OUTCOMES.PRE_TRANSMISSION_FAILURE,
        pre_transmission_class: PRE_TX_CLASSES.TRANSIENT,
        delivery_eligibility: DELIVERY_ELIGIBILITY.STALE_REVIEW_REQUIRED,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'STALE',
    );
    assert(r.freshness_blocks_retry === true, 'freshness blocks');
    assert(r.retry_authorized === false, 'not authorized');
  }),
);

results.push(
  runCase('E28', () => {
    const r = expectDecision(
      {
        event_id: 'e28',
        transport_outcome: TRANSPORT_OUTCOMES.PRE_TRANSMISSION_FAILURE,
        pre_transmission_class: PRE_TX_CLASSES.TRANSIENT,
        delivery_eligibility: DELIVERY_ELIGIBILITY.NOT_SAFE_TO_SEND,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'NOT_ELIGIBLE',
    );
    assert(r.retry_authorized === false, 'not authorized');
  }),
);

results.push(
  runCase('E29', () => {
    expectDecision(
      {
        event_id: 'e29',
        same_event_parallel: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.UNSAFE_TO_RETRY,
      'SAME_EVENT',
    );
  }),
);

results.push(
  runCase('E30', () => {
    expectDecision(
      {
        event_id: 'e30',
        different_event_parallel: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.UNSAFE_TO_RETRY,
      'GLOBAL_CONCURRENCY',
    );
  }),
);

results.push(
  runCase('E31', () => {
    const r = expectDecision(
      {
        event_id: 'e31',
        transport_outcome: TRANSPORT_OUTCOMES.PRE_TRANSMISSION_FAILURE,
        pre_transmission_class: PRE_TX_CLASSES.TRANSIENT,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
        retry_charter_present: false,
      },
      RETRY_DECISIONS.SAFE_TO_RETRY,
      'PRE_TRANSMISSION_TRANSIENT',
    );
    assert(r.charter_rejected === true, 'charter rejected');
    assert(r.charter_reject_reason === REASON_CODES.RETRY_CHARTER_REQUIRED, 'charter required');
  }),
);

results.push(
  runCase('E32', () => {
    const charter = buildRetryCharterTemplate({
      charter_id: 'rc-e32',
      event_id: 'wrong-event',
      source_identity_fingerprint: 'fp1',
      expires_at_ms: clock.nowMs() + 60_000,
    });
    const r = expectDecision(
      {
        event_id: 'e32',
        transport_outcome: TRANSPORT_OUTCOMES.PRE_TRANSMISSION_FAILURE,
        pre_transmission_class: PRE_TX_CLASSES.TRANSIENT,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
        retry_charter: charter,
        source_identity_fingerprint: 'fp1',
        now_ms: clock.nowMs(),
      },
      RETRY_DECISIONS.SAFE_TO_RETRY,
      'PRE_TRANSMISSION_TRANSIENT',
    );
    assert(r.charter_rejected === true, 'mismatch rejected');
    assert(r.charter_reject_reason === REASON_CODES.RETRY_CHARTER_EVENT_MISMATCH, 'event mismatch');
  }),
);

results.push(
  runCase('E33', () => {
    const charter = buildRetryCharterTemplate({
      charter_id: 'rc-e33',
      event_id: 'e33',
      source_identity_fingerprint: 'fp-wrong',
      expires_at_ms: clock.nowMs() + 60_000,
    });
    const r = expectDecision(
      {
        event_id: 'e33',
        transport_outcome: TRANSPORT_OUTCOMES.PRE_TRANSMISSION_FAILURE,
        pre_transmission_class: PRE_TX_CLASSES.TRANSIENT,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
        retry_charter: charter,
        source_identity_fingerprint: 'fp-correct',
        now_ms: clock.nowMs(),
      },
      RETRY_DECISIONS.SAFE_TO_RETRY,
      'PRE_TRANSMISSION_TRANSIENT',
    );
    assert(r.charter_rejected === true, 'source mismatch');
    assert(r.charter_reject_reason === REASON_CODES.RETRY_CHARTER_SOURCE_MISMATCH, 'source code');
  }),
);

results.push(
  runCase('E34', () => {
    const charter = buildRetryCharterTemplate({
      charter_id: 'rc-e34',
      event_id: 'e34',
      source_identity_fingerprint: 'fp',
      expires_at_ms: clock.nowMs() + 60_000,
    });
    charter.retry_budget_remaining = 0;
    const r = expectDecision(
      {
        event_id: 'e34',
        transport_outcome: TRANSPORT_OUTCOMES.PRE_TRANSMISSION_FAILURE,
        pre_transmission_class: PRE_TX_CLASSES.TRANSIENT,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
        retry_charter: charter,
        source_identity_fingerprint: 'fp',
        retry_budget_remaining: 0,
        now_ms: clock.nowMs(),
      },
      RETRY_DECISIONS.SAFE_TO_RETRY,
      'PRE_TRANSMISSION_TRANSIENT',
    );
    assert(r.retry_authorized === false, 'budget exhausted');
    assert(
      r.charter_reject_reason === REASON_CODES.RETRY_BUDGET_EXHAUSTED ||
        r.charter_rejected === true,
      'budget reject',
    );
  }),
);

results.push(
  runCase('E35', () => {
    const r = expectDecision(
      {
        event_id: 'e35-new',
        is_new_source_run: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'NEW_SOURCE_RUN',
    );
    assert(r.note && String(r.note).includes('new event_id'), 'ordinary pipeline note');
  }),
);

results.push(
  runCase('E36', () => {
    const r = expectDecision(
      {
        event_id: 'c84e29bf-79b1-5aea-98c4-9dc8d651fc96',
        delivery_state: DELIVERY_STATE.PENDING,
        historical_telegram_success_evidence: true,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.UNSAFE_TO_RETRY,
      'HISTORICAL_PENDING',
    );
    assert(r.no_send_guard === true, 'no blind retry');
  }),
);

results.push(
  runCase('E37', () => {
    expectDecision(
      {
        event_id: 'e37',
        transport_outcome: TRANSPORT_OUTCOMES.RESPONSE_LOST,
        delivery_state: DELIVERY_STATE.SENT,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.UNSAFE_TO_RETRY,
      'SENT',
    );
  }),
);

results.push(
  runCase('E38', () => {
    expectDecision(
      {
        event_id: 'e38',
        transport_outcome: TRANSPORT_OUTCOMES.RESPONSE_LOST,
        delivery_state: DELIVERY_STATE.FAILED,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.FINAL_FAILURE,
      'FAILED',
    );
  }),
);

results.push(
  runCase('E39', () => {
    expectDecision(
      {
        event_id: 'e39',
        transport_outcome: TRANSPORT_OUTCOMES.RESPONSE_LOST,
        delivery_state: DELIVERY_STATE.PENDING,
        row_found: true,
        delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      },
      RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
      'PENDING',
    );
  }),
);

results.push(
  runCase('E40', () => {
    const r = evaluateRetryPolicy({
      event_id: 'e40',
      delivery_state: DELIVERY_STATE.SENT,
      row_found: true,
      delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      security_scan_requested: true,
      evidence: {
        decision: 'ok',
        api_key: 'should-be-stripped',
        authorization: 'Bearer secret',
        sample: 'safe',
      },
    });
    assert(r.evidence_sanitized === true || r.evidence_issues?.length > 0, 'security scan ran');
    const cleaned = sanitizeEvidence({
      sample: 'safe',
      api_key: 'x',
      token: 'y',
    });
    assert(cleaned.ok === false, 'secrets detected');
    assert(!('api_key' in cleaned.value), 'api_key stripped');
    assert(cleaned.value.sample === 'safe', 'safe field kept');
  }),
);

// ---------------------------------------------------------------------------
// EC1–EC10 concurrency
// ---------------------------------------------------------------------------

results.push(
  runCase('EC1', () => {
    const a = evaluateRetryPolicy({
      event_id: 'same',
      same_event_parallel: true,
      delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
    });
    const b = evaluateRetryPolicy({
      event_id: 'same',
      same_event_parallel: true,
      delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
    });
    assert(a.decision === RETRY_DECISIONS.UNSAFE_TO_RETRY, 'a rejected');
    assert(b.decision === RETRY_DECISIONS.UNSAFE_TO_RETRY, 'b rejected');
  }),
);

results.push(
  await runAsyncCase('EC2', async (dir) => {
    const lockPath = join(dir, 'lifecycle.lock');
    const now = clock.nowMs();
    const acq = tryAcquireExclusiveLifecycleOwnership(
      lockPath,
      {
        schema_version: 1,
        workflow_id: ALLOWED_WORKFLOW_ID,
        charter_id: 'owner-1',
        pid: 111,
        process_identity: 'owner-1',
        created_at_ms: now,
        lease_expires_at_ms: now + 60_000,
        owner_token: 'tok-1',
      },
      { nowMs: now, processAlive: () => true },
    );
    assert(acq.ok === true, 'first lock acquired');
    const second = evaluateConcurrencyPolicy({
      event_id: 'ec2',
      lifecycle_lock_path: lockPath,
      now_ms: now,
      process_alive: () => true,
      workflow_active: false,
    });
    assert(second.rejected === true, 'second rejected');
    assert(second.reason_code === REASON_CODES.LIFECYCLE_LOCK_HELD, 'lock held');
  }),
);

results.push(
  await runAsyncCase('EC3', async (dir) => {
    const lockPath = join(dir, 'lifecycle.lock');
    const now = clock.nowMs();
    tryAcquireExclusiveLifecycleOwnership(
      lockPath,
      {
        schema_version: 1,
        workflow_id: ALLOWED_WORKFLOW_ID,
        charter_id: 'owner-a',
        pid: 222,
        process_identity: 'owner-a',
        created_at_ms: now,
        lease_expires_at_ms: now + 60_000,
        owner_token: 'tok-a',
      },
      { nowMs: now, processAlive: () => true },
    );
    const r = evaluateRetryPolicy({
      event_id: 'other-event',
      lifecycle_lock_held_by_other: true,
      delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
    });
    assert(r.decision === RETRY_DECISIONS.UNSAFE_TO_RETRY, 'different event rejected');
    assert(r.reason_code === REASON_CODES.LIFECYCLE_LOCK_HELD, 'lock');
  }),
);

results.push(
  runCase('EC4', () => {
    const r = evaluateConcurrencyPolicy({
      event_id: 'ec4',
      unresolved_active_session: true,
    });
    assert(r.rejected === true, 'unresolved session');
    assert(r.max_safe_concurrency === 1, 'concurrency 1');
  }),
);

results.push(
  runCase('EC5', () => {
    const r = evaluateConcurrencyPolicy({
      event_id: 'ec5',
      request_budget_exhausted: true,
    });
    assert(r.rejected === true, 'budget');
    assert(r.reason_code === REASON_CODES.REQUEST_BUDGET_EXHAUSTED, 'code');
  }),
);

results.push(
  runCase('EC6', () => {
    const r = evaluateConcurrencyPolicy({
      event_id: 'ec6',
      delivery_state: DELIVERY_STATE.PENDING,
    });
    assert(r.rejected === true, 'pending cannot consume attempt');
  }),
);

results.push(
  runCase('EC7', () => {
    const r = evaluateConcurrencyPolicy({
      event_id: 'ec7',
      delivery_state: DELIVERY_STATE.SENT,
    });
    assert(r.rejected === true, 'sent cannot re-enqueue');
  }),
);

results.push(
  runCase('EC8', () => {
    const r = evaluateConcurrencyPolicy({
      event_id: 'ec8',
      delivery_state: DELIVERY_STATE.FAILED,
    });
    assert(r.rejected === true, 'failed cannot auto-re-enqueue');
  }),
);

results.push(
  runCase('EC9', () => {
    const r = evaluateConcurrencyPolicy({
      event_id: 'ec9',
      delivery_eligibility: DELIVERY_ELIGIBILITY.STALE_REVIEW_REQUIRED,
    });
    assert(r.rejected === true, 'stale cannot re-enqueue');
  }),
);

results.push(
  runCase('EC10', () => {
    const blocked = evaluateConcurrencyPolicy({
      event_id: 'ec10-new',
      unresolved_active_session: true,
      delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
    });
    assert(blocked.rejected === true, 'new event blocked while session active');
    const after = evaluateConcurrencyPolicy({
      event_id: 'ec10-new',
      unresolved_active_session: false,
      delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
    });
    assert(after.rejected === false, 'may proceed after containment');
    assert(after.concurrency_allowed === true, 'allowed under concurrency=1 sequentially');
  }),
);

// Invariants
results.push(
  runCase('INV-AUTO-RETRY', () => {
    assert(MAX_RETRIES === 0, 'ledger max_retries');
    assert(MAX_SAFE_CONCURRENCY === 1, 'ledger concurrency');
    assert(D6E_MAX_SAFE_CONCURRENCY === 1, 'd6e concurrency');
    const model = describeConcurrencyModel();
    assert(model.verdict === 'D6E_CONCURRENCY_REMAINS_ONE', 'verdict');
    assert(model.overturned_by_abc === false, 'd1 not overturned');
  }),
);

results.push(
  runCase('INV-AUTHORITY', () => {
    const auth = describeReconciliationAuthority();
    assert(auth.order[0] === 'deterministic_event_identity', 'identity first');
    assert(auth.order[1] === 'durable_data_table_row', 'row second');
    assert(Object.keys(describeFailureBoundaries()).length >= 8, 'B0-B7');
    assert(Object.keys(describeRetryDecisionModel()).length === 4, 'four decisions');
  }),
);

results.push(
  runCase('INV-PLANNER', () => {
    const plan = planReconciliation({
      decision: RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
      reason_code: REASON_CODES.AMBIGUOUS_TRANSPORT,
      row_found: false,
    });
    assert(plan.production_mutation_authorized === false, 'no mutation');
    assert(plan.actions.includes('READ_DATA_TABLE_EVENT'), 'read table');
  }),
);

results.push(
  runCase('INV-CLOCK', () => {
    const t1 = clock.nowMs();
    clock.advance(5000);
    const t2 = clock.nowMs();
    assert(t2 === t1 + 5000, 'deterministic clock advance');
    const charter = buildRetryCharterTemplate({
      charter_id: 'clock',
      event_id: 'c1',
      source_identity_fingerprint: 'fp',
      expires_at_ms: t1 + 1000,
    });
    const expired = validateRetryCharter(charter, {
      event_id: 'c1',
      source_identity_fingerprint: 'fp',
      policy_decision: 'SAFE_TO_RETRY',
      now_ms: t2,
    });
    assert(expired.ok === false, 'expired charter rejected');
  }),
);

const eCases = results.filter((r) => /^E\d+$/.test(r.id));
const ecCases = results.filter((r) => /^EC\d+$/.test(r.id));
const passed = results.filter((r) => r.ok).length;
const failed = results.filter((r) => !r.ok);

const out = {
  phase: '1B-D6E',
  total: results.length,
  passed,
  failed: failed.length,
  e_cases: { total: eCases.length, passed: eCases.filter((r) => r.ok).length },
  ec_cases: { total: ecCases.length, passed: ecCases.filter((r) => r.ok).length },
  max_retries: MAX_RETRIES,
  max_safe_concurrency: MAX_SAFE_CONCURRENCY,
  automatic_retries_enabled: false,
  concurrency_model: describeConcurrencyModel(),
  results,
  failed_details: failed,
  verdict:
    failed.length === 0 && eCases.length === 40 && ecCases.length === 10
      ? 'D6E_OFFLINE_POLICY_HARNESS_PASS'
      : 'D6E_OFFLINE_POLICY_HARNESS_FAIL',
  concurrency_verdict:
    ecCases.every((r) => r.ok) && ecCases.length === 10
      ? 'D6E_CONCURRENCY_HARNESS_PASS'
      : 'D6E_CONCURRENCY_HARNESS_FAIL',
};

process.stdout.write(`${JSON.stringify(out, null, 2)}\n`);
process.exitCode = failed.length === 0 ? 0 : 1;
