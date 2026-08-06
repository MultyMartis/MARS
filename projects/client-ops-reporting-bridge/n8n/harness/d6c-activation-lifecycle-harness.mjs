/**
 * Phase 1B-D6C — offline activation lifecycle harness (C1–C30).
 * No network. No production activation. Deterministic clock (no sleep).
 */

import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  runBoundedActivationLifecycle,
  createRequestBudgetGuard,
  evaluateDeliveryEligibility,
  isStaleAge,
  validateLifecycleCharter,
  describeActivationStateMachine,
  D6C_ALLOWED_WORKFLOW_ID,
  D6C_EXPECTED_VERSION_ID,
  D6C_DEFAULTS,
  LIFECYCLE_STATES,
  DELIVERY_ELIGIBILITY,
  STALE_AFTER_SECONDS,
  MAX_RETRIES,
  MAX_SAFE_CONCURRENCY,
  sanitizeLifecycleEvidence,
} from '../runners/lib/client-ops-activation-lifecycle.mjs';
import {
  createOfflineLifecycleTransport,
  createDeterministicClock,
} from '../runners/lib/client-ops-lifecycle-offline-transport.mjs';
import {
  acquireLifecycleLock,
  classifyLifecycleLock,
  readLifecycleLock,
} from '../runners/lib/client-ops-lifecycle-lock.mjs';
import {
  ALLOWED_WORKFLOW_ID,
  D6C_ACTIVATION_CONFIRM_PHRASE,
  D6C_DEACTIVATION_CONFIRM_PHRASE,
  D6C_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE,
  D6A2_ACTIVATION_CONFIRM_PHRASE,
} from '../runners/lib/client-ops-n8n-activation-client.mjs';
import {
  MAX_RETRIES as LEDGER_MAX_RETRIES,
  MAX_SAFE_CONCURRENCY as LEDGER_MAX_CONCURRENCY,
  DELIVERY_STATE,
} from '../runners/lib/client-ops-delivery-ledger.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));

function assert(cond, label) {
  if (!cond) throw new Error(label);
}

function baseCharter(overrides = {}) {
  return {
    charter_id: 'd6c-test-charter',
    workflow_id: D6C_ALLOWED_WORKFLOW_ID,
    expected_version_id: D6C_EXPECTED_VERSION_ID,
    required_initial_workflow_active: false,
    max_requests: 1,
    max_retries: 0,
    max_concurrency: 1,
    max_activation_changes: 2,
    window_seconds: 120,
    operation_type: 'NEW_DELIVERY_FIRST_SEEN',
    event_id: 'd6c-event-unseen-001',
    source: {
      source_status: 'ATTENTION',
      normalized_status: 'ATTENTION',
      age_seconds: 1000,
    },
    unattended: false,
    consumed: false,
    ...overrides,
  };
}

function freshLockDir() {
  return mkdtempSync(join(tmpdir(), 'd6c-lock-'));
}

async function runCase(id, fn) {
  const dir = freshLockDir();
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

// C1 normal lifecycle
results.push(
  await runCase('C1', async (dir) => {
    const clock = createDeterministicClock();
    const transport = createOfflineLifecycleTransport({
      versionId: D6C_EXPECTED_VERSION_ID,
      active: false,
    });
    const charter = baseCharter({ charter_id: 'c1' });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock,
      charter,
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c1-owner' },
    });
    assert(out.evidence.activation_attempts === 1, 'c1_activate');
    assert(out.evidence.requests_attempted === 1, 'c1_request');
    assert(out.evidence.request_result_class === 'HTTP_202_INTAKE_ACCEPTED', 'c1_202');
    assert(out.evidence.deactivation_attempts >= 1, 'c1_deact');
    assert(out.evidence.final_active === false, 'c1_inactive');
    assert(out.containment_verified === true, 'c1_contain');
    assert(out.state === LIFECYCLE_STATES.RECONTAINED, 'c1_state');
    assert(out.evidence.activation_changes === 2, 'c1_changes_2');
  }),
);

// C2 stale preflight
results.push(
  await runCase('C2', async (dir) => {
    const clock = createDeterministicClock();
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock,
      charter: baseCharter({
        charter_id: 'c2',
        source: { source_status: 'ATTENTION', normalized_status: 'ATTENTION', age_seconds: 93601 },
      }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c2' },
    });
    assert(out.evidence.activation_attempts === 0, 'c2_no_act');
    assert(out.evidence.requests_attempted === 0, 'c2_no_post');
    assert(out.state === LIFECYCLE_STATES.FAILED_CLOSED, 'c2_fail');
  }),
);

// C3 true BLOCKED
results.push(
  await runCase('C3', async (dir) => {
    const clock = createDeterministicClock();
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock,
      charter: baseCharter({
        charter_id: 'c3',
        source: { source_status: 'BLOCKED', normalized_status: 'BLOCKED', age_seconds: 10 },
      }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c3' },
    });
    assert(out.evidence.activation_attempts === 0, 'c3_no_act');
    assert(out.state === LIFECYCLE_STATES.FAILED_CLOSED, 'c3_fail');
  }),
);

// C4 already seen
results.push(
  await runCase('C4', async (dir) => {
    const clock = createDeterministicClock();
    const transport = createOfflineLifecycleTransport({
      versionId: D6C_EXPECTED_VERSION_ID,
      seenEvents: { 'd6c-event-unseen-001': { intake_state: 'FIRST_SEEN' } },
    });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock,
      charter: baseCharter({ charter_id: 'c4' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c4' },
    });
    assert(out.evidence.activation_attempts === 0, 'c4_no_act');
    assert(out.evidence.requests_attempted === 0, 'c4_no_post');
  }),
);

// C5 activation API failure
results.push(
  await runCase('C5', async (dir) => {
    const clock = createDeterministicClock();
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({ activateResult: 'api_failure' });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock,
      charter: baseCharter({ charter_id: 'c5' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c5' },
    });
    assert(out.evidence.activation_attempts === 1, 'c5_attempt');
    assert(out.evidence.requests_attempted === 0, 'c5_no_post');
    assert(out.evidence.final_active === false, 'c5_inactive');
  }),
);

// C6 activate success but GET inactive
results.push(
  await runCase('C6', async (dir) => {
    const clock = createDeterministicClock();
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({ activateResult: 'success_but_inactive' });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock,
      charter: baseCharter({ charter_id: 'c6' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c6' },
    });
    assert(out.evidence.requests_attempted === 0, 'c6_no_post');
    assert(out.evidence.readiness_result?.ok === false, 'c6_not_ready');
  }),
);

// C7 version mismatch after activate
results.push(
  await runCase('C7', async (dir) => {
    const clock = createDeterministicClock();
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({ versionDriftAfterActivate: 'drifted-version' });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock,
      charter: baseCharter({ charter_id: 'c7' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c7' },
    });
    assert(out.evidence.requests_attempted === 0, 'c7_no_post');
    assert(out.evidence.deactivation_attempts >= 1, 'c7_deact');
    assert(out.containment_verified === true, 'c7_contain');
  }),
);

// C8 fresh→stale before request
results.push(
  await runCase('C8', async (dir) => {
    const clock = createDeterministicClock(1_700_000_000_000);
    const observed = new Date(clock.nowMs() - 93500 * 1000).toISOString();
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    // Advance clock during lifecycle: wrap advance into post-activate by injecting after readiness
    // Use short window and advance clock before revalidation by overriding clock.nowMs after open
    let advanced = false;
    const clock2 = {
      nowMs() {
        return advanced ? clock.nowMs() + 200 * 1000 : clock.nowMs();
      },
      advance(ms) {
        return clock.advance(ms);
      },
    };
    // Force stale by advancing before POST via mutating source age path:
    // observed_at fixed; after activate we flip advanced so age > 93600
    const charter = baseCharter({
      charter_id: 'c8',
      source: {
        source_status: 'ATTENTION',
        normalized_status: 'ATTENTION',
        observed_at: observed,
      },
    });
    // Monkey-patch: after readiness, set advanced by wrapping transport.activate
    const origActivate = transport.activate.bind(transport);
    transport.activate = async (t) => {
      const r = await origActivate(t);
      advanced = true;
      return r;
    };
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: clock2,
      charter,
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c8' },
    });
    assert(out.evidence.activation_attempts === 1, 'c8_activated');
    assert(out.evidence.requests_attempted === 0, 'c8_no_post');
    assert(out.evidence.deactivation_attempts >= 1, 'c8_deact');
    assert(
      out.evidence.anomalies.some((a) => a.includes('PRE_REQUEST_FRESHNESS') || a.includes('CLOSE_REASON')),
      'c8_freshness',
    );
  }),
);

// C9 unseen→seen before request
results.push(
  await runCase('C9', async (dir) => {
    const clock = createDeterministicClock();
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    const origActivate = transport.activate.bind(transport);
    transport.activate = async (t) => {
      const r = await origActivate(t);
      transport.markEventSeen('d6c-event-unseen-001');
      return r;
    };
    const out = await runBoundedActivationLifecycle({
      transport,
      clock,
      charter: baseCharter({ charter_id: 'c9' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c9' },
    });
    assert(out.evidence.requests_attempted === 0, 'c9_no_post');
    assert(out.evidence.deactivation_attempts >= 1, 'c9_deact');
  }),
);

// C10 HTTP 202 → deactivate
results.push(
  await runCase('C10', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({ postResult: { http_status: 202, class: 'HTTP_202_INTAKE_ACCEPTED' } });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c10' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c10' },
    });
    assert(out.evidence.request_result_class === 'HTTP_202_INTAKE_ACCEPTED', 'c10_class');
    assert(out.evidence.final_active === false, 'c10_inactive');
  }),
);

// C11 HTTP 200
results.push(
  await runCase('C11', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({
      postResult: { http_status: 200, class: 'HTTP_200_DUPLICATE_SUPPRESSED' },
    });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c11' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c11' },
    });
    assert(out.evidence.request_result_class === 'HTTP_200_DUPLICATE_SUPPRESSED', 'c11');
    assert(out.evidence.final_active === false, 'c11_inactive');
  }),
);

// C12 HTTP 409
results.push(
  await runCase('C12', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({
      postResult: { http_status: 409, class: 'HTTP_409_EVENT_ID_CONFLICT' },
    });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c12' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c12' },
    });
    assert(out.evidence.request_result_class === 'HTTP_409_EVENT_ID_CONFLICT', 'c12');
    assert(out.evidence.final_active === false, 'c12_inactive');
  }),
);

// C13 HTTP 500
results.push(
  await runCase('C13', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({ postResult: { http_status: 500, class: 'HTTP_5XX' } });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c13' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c13' },
    });
    assert(out.evidence.request_result_class === 'HTTP_5XX', 'c13');
    assert(out.evidence.final_active === false, 'c13_inactive');
    assert(out.evidence.requests_attempted === 1, 'c13_no_retry');
  }),
);

// C14 timeout — no retry
results.push(
  await runCase('C14', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({ postResult: { timeout: true } });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c14' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c14' },
    });
    assert(out.evidence.request_result_class === 'READ_TIMEOUT_AMBIGUOUS', 'c14');
    assert(out.evidence.requests_attempted === 1, 'c14_one');
    assert(out.evidence.final_active === false, 'c14_inactive');
  }),
);

// C15 budget exhausted — second request rejected locally
results.push(
  await runCase('C15', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c15' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c15' },
    });
    const guard = createRequestBudgetGuard({
      requests_used: out.evidence.requests_used,
      max_requests: 1,
      closed: true,
      deadline_ms: out.evidence.window_deadline_ms,
    });
    assert(guard.canRequest().ok === false, 'c15_reject');
    assert(guard.canRequest().reason === 'WINDOW_CLOSED' || guard.canRequest().reason === 'REQUEST_BUDGET_EXHAUSTED', 'c15_reason');
  }),
);

// C16 concurrent lock rejected
results.push(
  await runCase('C16', async (dir) => {
    const lockPath = join(dir, 'lock.json');
    const a = acquireLifecycleLock({
      lockPath,
      workflowId: D6C_ALLOWED_WORKFLOW_ID,
      charterId: 'c16a',
      ownerToken: 'owner-a',
      nowMs: 1000,
      processAlive: () => true,
      workflowActive: false,
    });
    assert(a.ok, 'c16_first');
    const b = acquireLifecycleLock({
      lockPath,
      workflowId: D6C_ALLOWED_WORKFLOW_ID,
      charterId: 'c16b',
      ownerToken: 'owner-b',
      nowMs: 1001,
      processAlive: () => true,
      workflowActive: false,
    });
    assert(b.ok === false, 'c16_second_fail');
  }),
);

// C17 valid existing lock fail closed
results.push(
  await runCase('C17', async (dir) => {
    const lockPath = join(dir, 'lock.json');
    acquireLifecycleLock({
      lockPath,
      workflowId: D6C_ALLOWED_WORKFLOW_ID,
      charterId: 'c17-holder',
      ownerToken: 'holder',
      nowMs: 1000,
      processAlive: () => true,
      workflowActive: false,
    });
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c17-challenger' }),
      lock: {
        lockPath,
        ownerToken: 'challenger',
        processAlive: () => true,
      },
    });
    assert(out.evidence.activation_attempts === 0, 'c17_no_act');
    assert(out.state === LIFECYCLE_STATES.FAILED_CLOSED, 'c17_fail');
  }),
);

// C18 stale lock + inactive → explicit recovery
results.push(
  await runCase('C18', async (dir) => {
    const lockPath = join(dir, 'lock.json');
    acquireLifecycleLock({
      lockPath,
      workflowId: D6C_ALLOWED_WORKFLOW_ID,
      charterId: 'old',
      ownerToken: 'old-owner',
      nowMs: 1000,
      leaseMs: 10,
      pid: 999001,
      processAlive: () => false,
      workflowActive: false,
    });
    const classified = classifyLifecycleLock(readLifecycleLock(lockPath), {
      nowMs: 999999,
      processAlive: () => false,
      workflowActive: false,
    });
    assert(classified.action === 'EXPLICIT_RECOVERY_ALLOWED', 'c18_class');
    const denied = acquireLifecycleLock({
      lockPath,
      workflowId: D6C_ALLOWED_WORKFLOW_ID,
      charterId: 'new',
      ownerToken: 'new',
      nowMs: 999999,
      processAlive: () => false,
      workflowActive: false,
      allowExplicitStaleRecovery: false,
    });
    assert(denied.ok === false, 'c18_no_silent');
    const allowed = acquireLifecycleLock({
      lockPath,
      workflowId: D6C_ALLOWED_WORKFLOW_ID,
      charterId: 'new2',
      ownerToken: 'new2',
      nowMs: 999999,
      processAlive: () => false,
      workflowActive: false,
      allowExplicitStaleRecovery: true,
    });
    assert(allowed.ok === true, 'c18_explicit');
  }),
);

// C19 stale/unknown lock + workflow active → operator review
results.push(
  await runCase('C19', async (dir) => {
    const lockPath = join(dir, 'lock.json');
    acquireLifecycleLock({
      lockPath,
      workflowId: D6C_ALLOWED_WORKFLOW_ID,
      charterId: 'ghost',
      ownerToken: 'ghost',
      nowMs: 1000,
      leaseMs: 10,
      pid: 999002,
      processAlive: () => false,
      workflowActive: false,
    });
    const classified = classifyLifecycleLock(readLifecycleLock(lockPath), {
      nowMs: 999999,
      processAlive: () => false,
      workflowActive: true,
    });
    assert(classified.action === 'OPERATOR_REVIEW_RECONTAINMENT_REQUIRED', 'c19');
    const denied = acquireLifecycleLock({
      lockPath,
      workflowId: D6C_ALLOWED_WORKFLOW_ID,
      charterId: 'takeover',
      ownerToken: 'takeover',
      nowMs: 999999,
      processAlive: () => false,
      workflowActive: true,
      allowExplicitStaleRecovery: true,
    });
    assert(denied.ok === false, 'c19_no_takeover');
    assert(denied.reason === 'STALE_LOCK_WITH_ACTIVE_WORKFLOW', 'c19_reason');
  }),
);

// C20 deactivation success + GET inactive
results.push(
  await runCase('C20', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c20' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c20' },
    });
    assert(out.containment_verified === true, 'c20');
    assert(out.evidence.final_active === false, 'c20_active');
  }),
);

// C21 deact API success but GET active → CONTAINMENT_FAILED
results.push(
  await runCase('C21', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({
      deactivateResult: 'success_but_still_active',
      emergencyDeactivateResult: 'success_but_still_active',
    });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c21' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c21' },
    });
    assert(out.state === LIFECYCLE_STATES.CONTAINMENT_FAILED, 'c21_state');
    assert(out.containment_verified === false, 'c21_not');
    assert(out.evidence.anomalies.some((a) => a.includes('CONTAINMENT_FAILED')), 'c21_anom');
  }),
);

// C22 deactivation API failure → emergency path
results.push(
  await runCase('C22', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({
      deactivateResult: 'api_failure',
      emergencyDeactivateResult: 'success',
    });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c22' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c22' },
    });
    assert(out.evidence.emergency_containment_attempts === 1, 'c22_emerg');
    assert(
      out.state === LIFECYCLE_STATES.RECONTAINED_WITH_ANOMALY ||
        out.state === LIFECYCLE_STATES.RECONTAINED,
      'c22_state',
    );
  }),
);

// C23 emergency succeeds → RECONTAINED_WITH_ANOMALY
results.push(
  await runCase('C23', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({
      deactivateResult: 'api_failure',
      emergencyDeactivateResult: 'success',
    });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c23' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c23' },
    });
    assert(out.state === LIFECYCLE_STATES.RECONTAINED_WITH_ANOMALY, 'c23');
    assert(out.containment_verified === true, 'c23_ok');
  }),
);

// C24 emergency fails → CONTAINMENT_FAILED
results.push(
  await runCase('C24', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({
      deactivateResult: 'api_failure',
      emergencyDeactivateResult: 'api_failure',
    });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c24' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c24' },
    });
    assert(out.state === LIFECYCLE_STATES.CONTAINMENT_FAILED, 'c24');
  }),
);

// C25 version change during lifecycle
results.push(
  await runCase('C25', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({ versionDriftAfterActivate: 'changed-mid-lifecycle' });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c25' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c25' },
    });
    assert(out.evidence.requests_attempted === 0, 'c25_no_post');
    assert(out.containment_verified === true, 'c25_contain');
  }),
);

// C26 window deadline before POST
results.push(
  await runCase('C26', async (dir) => {
    const clock = createDeterministicClock();
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    let dedupeCalls = 0;
    const origDedupe = transport.checkDedupe.bind(transport);
    transport.checkDedupe = async (id, t) => {
      dedupeCalls += 1;
      const r = await origDedupe(id, t);
      // Second call is pre-request revalidation; expire window before POST.
      if (dedupeCalls >= 2) clock.advance(500_000);
      return r;
    };
    const out = await runBoundedActivationLifecycle({
      transport,
      clock,
      charter: baseCharter({ charter_id: 'c26', window_seconds: 60 }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c26' },
    });
    assert(out.evidence.requests_attempted === 0, 'c26_no_post');
    assert(out.evidence.anomalies.some((a) => a.includes('DEADLINE')), 'c26_deadline');
    assert(out.evidence.deactivation_attempts >= 1, 'c26_deact');
  }),
);

// C27 activation change budget exceeded
results.push(
  await runCase('C27', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    transport.setBehavior({ extraActivationChangeOnActivate: true });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c27' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c27' },
    });
    assert(out.evidence.requests_attempted === 0, 'c27_no_post');
    assert(out.evidence.anomalies.some((a) => a.includes('ACTIVATION_CHANGE_BUDGET')), 'c27');
  }),
);

// C28 running executions remain
results.push(
  await runCase('C28', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    const origDeact = transport.deactivate.bind(transport);
    transport.deactivate = async (t, opts) => {
      const r = await origDeact(t, opts);
      transport._mutate({ running: 1 });
      return r;
    };
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c28' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c28' },
    });
    assert(out.state === LIFECYCLE_STATES.CONTAINMENT_FAILED, 'c28');
  }),
);

// C29 charter reuse rejected
results.push(
  await runCase('C29', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    const charter = baseCharter({ charter_id: 'c29' });
    const first = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter,
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c29a' },
    });
    assert(first.evidence.charter_consumed === true, 'c29_consumed');
    const transport2 = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    const second = await runBoundedActivationLifecycle({
      transport: transport2,
      clock: createDeterministicClock(),
      charter,
      lock: { lockPath: join(dir, 'lock2.json'), ownerToken: 'c29b' },
    });
    assert(second.evidence.activation_attempts === 0, 'c29_reuse_blocked');
    assert(second.state === LIFECYCLE_STATES.FAILED_CLOSED, 'c29_fail');
  }),
);

// C30 no secrets in evidence
results.push(
  await runCase('C30', async (dir) => {
    const transport = createOfflineLifecycleTransport({ versionId: D6C_EXPECTED_VERSION_ID });
    const out = await runBoundedActivationLifecycle({
      transport,
      clock: createDeterministicClock(),
      charter: baseCharter({ charter_id: 'c30' }),
      lock: { lockPath: join(dir, 'lock.json'), ownerToken: 'c30' },
    });
    const json = JSON.stringify(out.evidence);
    assert(!/"api_key"\s*:/.test(json), 'c30_api');
    assert(!/"token"\s*:/.test(json), 'c30_token');
    assert(!/"password"\s*:/.test(json), 'c30_pw');
    assert(!/"webhook_url"\s*:/.test(json), 'c30_url');
    const sanitized = sanitizeLifecycleEvidence(out.evidence);
    assert(sanitized.charter_id === 'c30', 'c30_ok');
    // Bad charter with secret key rejected
    const bad = validateLifecycleCharter(baseCharter({ api_key: 'SECRET' }));
    assert(bad.ok === false, 'c30_charter_secret');
  }),
);

// Invariants
assert(ALLOWED_WORKFLOW_ID === D6C_ALLOWED_WORKFLOW_ID, 'allowlist');
assert(MAX_RETRIES === 0 && LEDGER_MAX_RETRIES === 0, 'retries');
assert(MAX_SAFE_CONCURRENCY === 1 && LEDGER_MAX_CONCURRENCY === 1, 'concurrency');
assert(D6C_DEFAULTS.max_activation_changes === 2, 'act_budget');
assert(isStaleAge(93600) === false, 'threshold_eq');
assert(isStaleAge(93601) === true, 'threshold_gt');
assert(
  evaluateDeliveryEligibility({
    normalized_status: 'ATTENTION',
    age_seconds: 93600,
  }).delivery_eligibility === DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
  'elig_fresh',
);
assert(DELIVERY_STATE.PENDING === 'PENDING', 'ledger_a');
assert(typeof D6C_ACTIVATION_CONFIRM_PHRASE === 'string', 'phrase_act');
assert(typeof D6C_DEACTIVATION_CONFIRM_PHRASE === 'string', 'phrase_deact');
assert(typeof D6C_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE === 'string', 'phrase_em');
assert(typeof D6A2_ACTIVATION_CONFIRM_PHRASE === 'string', 'compat_d6a2');
assert(describeActivationStateMachine().model === 'HYBRID_C1_TO_C3_BOUNDED', 'model');
assert(STALE_AFTER_SECONDS === 93600, 'stale_const');

// Clock determinism (no sleep)
const clk = createDeterministicClock(100);
assert(clk.nowMs() === 100, 'clock1');
clk.advance(50);
assert(clk.nowMs() === 150, 'clock2');

const failed = results.filter((r) => !r.ok);
const summary = {
  phase: '1B-D6C',
  harness: 'd6c-activation-lifecycle-harness',
  total: results.length,
  passed: results.filter((r) => r.ok).length,
  failed: failed.length,
  results,
  invariants: {
    max_retries: MAX_RETRIES,
    max_concurrency: MAX_SAFE_CONCURRENCY,
    stale_after: STALE_AFTER_SECONDS,
    workflow_id: D6C_ALLOWED_WORKFLOW_ID,
    model: 'HYBRID_C1_TO_C3_BOUNDED',
  },
  verdict: failed.length === 0 ? 'D6C_OFFLINE_LIFECYCLE_HARNESS_PASS' : 'D6C_OFFLINE_LIFECYCLE_HARNESS_FAIL',
};

process.stdout.write(`${JSON.stringify(summary, null, 2)}\n`);
if (failed.length) {
  process.exitCode = 1;
}
