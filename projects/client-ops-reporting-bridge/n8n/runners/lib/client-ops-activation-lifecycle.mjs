/**
 * Phase 1B-D6C — Controlled Activation Lifecycle (offline orchestrator).
 *
 * HYBRID C1→C3 bounded contract. Explicit charter required.
 * No unattended mode. No production apply in this module alone.
 *
 * Preserves Workstream A ledger semantics and Workstream B eligibility values.
 * Does NOT implement Workstream E (retries) or D (unattended).
 */

import { ALLOWED_WORKFLOW_ID } from './client-ops-n8n-activation-client.mjs';
import {
  acquireLifecycleLock,
  releaseLifecycleLock,
  classifyLifecycleLock,
  readLifecycleLock,
} from './client-ops-lifecycle-lock.mjs';
import { MAX_RETRIES as LEDGER_MAX_RETRIES, MAX_SAFE_CONCURRENCY as LEDGER_MAX_CONCURRENCY } from './client-ops-delivery-ledger.mjs';

/** Canonical allowlisted workflow — activation is workflow-bound. */
export const D6C_ALLOWED_WORKFLOW_ID = ALLOWED_WORKFLOW_ID;
export const D6C_EXPECTED_VERSION_ID = 'dc8746bf-df9c-425d-9b3f-4ace452ac5ef';

export const LIFECYCLE_STATES = Object.freeze({
  CONTAINED: 'CONTAINED',
  PREFLIGHT_PASSED: 'PREFLIGHT_PASSED',
  ACTIVATING: 'ACTIVATING',
  ACTIVE_NOT_READY: 'ACTIVE_NOT_READY',
  ACTIVE_READY: 'ACTIVE_READY',
  REQUEST_WINDOW_OPEN: 'REQUEST_WINDOW_OPEN',
  REQUEST_WINDOW_CLOSED: 'REQUEST_WINDOW_CLOSED',
  DEACTIVATING: 'DEACTIVATING',
  RECONTAINED: 'RECONTAINED',
  RECONTAINED_WITH_ANOMALY: 'RECONTAINED_WITH_ANOMALY',
  CONTAINMENT_FAILED: 'CONTAINMENT_FAILED',
  FAILED_CLOSED: 'FAILED_CLOSED',
});

export const DELIVERY_ELIGIBILITY = Object.freeze({
  FRESH_AND_ELIGIBLE: 'FRESH_AND_ELIGIBLE',
  STALE_REVIEW_REQUIRED: 'STALE_REVIEW_REQUIRED',
  NOT_SAFE_TO_SEND: 'NOT_SAFE_TO_SEND',
});

/** Workstream B threshold — operator age > 93600 (93600 still fresh). */
export const STALE_AFTER_SECONDS = 93600;

export const D6C_DEFAULTS = Object.freeze({
  max_requests: 1,
  max_retries: 0,
  max_concurrency: 1,
  max_activation_changes: 2,
  window_seconds: 120,
  required_initial_workflow_active: false,
  emergency_containment_attempts: 1,
  normal_deactivation_attempts: 1,
});

export const D6C_ACTIVATION_CONFIRM =
  'ACTIVATE CLIENT OPS D6C BOUNDED LIFECYCLE BZPM';
export const D6C_DEACTIVATION_CONFIRM =
  'DEACTIVATE CLIENT OPS D6C BOUNDED LIFECYCLE BZPM';
export const D6C_EMERGENCY_DEACTIVATION_CONFIRM =
  'EMERGENCY DEACTIVATE CLIENT OPS D6C BOUNDED LIFECYCLE BZPM';

/** Preserve ledger constants (Workstream E not started). */
export const MAX_RETRIES = 0;
export const MAX_SAFE_CONCURRENCY = 1;

if (LEDGER_MAX_RETRIES !== 0 || LEDGER_MAX_CONCURRENCY !== 1) {
  throw new Error('D6C requires Workstream A ledger max_retries=0 concurrency=1');
}

/**
 * Workstream B freshness operator (must stay identical).
 * @param {number|null|undefined} ageSeconds
 * @param {number} [threshold]
 */
export function isStaleAge(ageSeconds, threshold = STALE_AFTER_SECONDS) {
  if (ageSeconds == null) return false;
  return Number(ageSeconds) > Number(threshold);
}

/**
 * @param {{
 *   source_status?: string,
 *   normalized_status?: string,
 *   age_seconds?: number|null,
 *   security_rejected?: boolean,
 * }} source
 */
export function evaluateDeliveryEligibility(source) {
  const status = String(source.normalized_status || source.source_status || '');
  const age = source.age_seconds;
  const stale = isStaleAge(age);

  if (status === 'BLOCKED' || source.security_rejected) {
    return {
      delivery_eligibility: DELIVERY_ELIGIBILITY.NOT_SAFE_TO_SEND,
      stale,
      freshness_reason: stale ? 'SOURCE_AUTHORITY_NOT_SAFE_AND_STALE' : 'SOURCE_AUTHORITY_NOT_SAFE',
    };
  }
  if (age == null) {
    return {
      delivery_eligibility: DELIVERY_ELIGIBILITY.NOT_SAFE_TO_SEND,
      stale: false,
      freshness_reason: 'AGE_UNKNOWN',
    };
  }
  if (stale) {
    return {
      delivery_eligibility: DELIVERY_ELIGIBILITY.STALE_REVIEW_REQUIRED,
      stale: true,
      freshness_reason: 'SOURCE_REPORT_TOO_OLD',
    };
  }
  return {
    delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
    stale: false,
    freshness_reason: 'WITHIN_FRESHNESS_THRESHOLD',
  };
}

/**
 * Recompute age from observed_at + clock when age_seconds not fixed.
 * @param {{ age_seconds?: number|null, observed_at?: string|null }} source
 * @param {{ nowMs: () => number }} clock
 */
export function resolveSourceAgeSeconds(source, clock) {
  if (source.age_seconds != null) return Number(source.age_seconds);
  if (!source.observed_at) return null;
  const observed = Date.parse(source.observed_at);
  if (Number.isNaN(observed)) return null;
  return Math.floor((clock.nowMs() - observed) / 1000);
}

/**
 * Dry lifecycle = open bounded request window but deliberately send zero webhooks.
 * Distinguishes DRY LIFECYCLE PREFLIGHT from SOURCE DELIVERY PREFLIGHT.
 * @param {Record<string, unknown>} charter
 */
export function isDryLifecycleCharter(charter) {
  if (!charter || typeof charter !== 'object') return false;
  return (
    Number(charter.planned_requests ?? -1) === 0 &&
    charter.allow_webhook_requests === false
  );
}

/**
 * Mechanical zero-request invariant for D6C2 dry window.
 * @param {Record<string, unknown>} charter
 * @param {{ sendRequest?: boolean }} [options]
 */
export function assertZeroRequestInvariant(charter, options = {}) {
  const errors = [];
  if (Number(charter?.planned_requests ?? -1) !== 0) {
    errors.push('PLANNED_REQUESTS_MUST_BE_ZERO');
  }
  if (charter?.allow_webhook_requests !== false) {
    errors.push('ALLOW_WEBHOOK_REQUESTS_MUST_BE_FALSE');
  }
  if (options.sendRequest === true) {
    errors.push('SEND_REQUEST_OPTION_FORBIDDEN');
  }
  if (charter?.allow_telegram === true) {
    errors.push('ALLOW_TELEGRAM_FORBIDDEN');
  }
  if (charter?.allow_data_table_mutation === true) {
    errors.push('ALLOW_DATA_TABLE_MUTATION_FORBIDDEN');
  }
  return {
    ok: errors.length === 0,
    errors,
    webhook_transport_invocation_budget: 0,
    planned_requests: Number(charter?.planned_requests ?? -1),
    allow_webhook_requests: charter?.allow_webhook_requests === false ? false : charter?.allow_webhook_requests,
  };
}

/**
 * Local orchestrator reject when charter forbids webhook.
 * @param {Record<string, unknown>} charter
 */
export function assertWebhookRequestProhibitedByCharter(charter) {
  if (isDryLifecycleCharter(charter) || charter?.allow_webhook_requests === false) {
    return {
      ok: false,
      reason: 'WEBHOOK_REQUEST_PROHIBITED_BY_CHARTER',
      planned_requests: Number(charter?.planned_requests ?? 0),
      allow_webhook_requests: false,
    };
  }
  return { ok: true };
}

/**
 * @param {Record<string, unknown>} charter
 */
export function validateLifecycleCharter(charter) {
  const errors = [];
  if (!charter || typeof charter !== 'object') {
    return { ok: false, errors: ['CHARTER_MISSING'] };
  }
  if (!charter.charter_id || typeof charter.charter_id !== 'string') {
    errors.push('CHARTER_ID_REQUIRED');
  }
  if (charter.workflow_id !== D6C_ALLOWED_WORKFLOW_ID) {
    errors.push('WORKFLOW_ID_NOT_ALLOWLISTED');
  }
  if (!charter.expected_version_id || typeof charter.expected_version_id !== 'string') {
    errors.push('EXPECTED_VERSION_ID_REQUIRED');
  }
  if (charter.required_initial_workflow_active !== false) {
    errors.push('REQUIRED_INITIAL_ACTIVE_MUST_BE_FALSE');
  }
  if (Number(charter.max_retries ?? 0) !== 0) {
    errors.push('MAX_RETRIES_MUST_BE_ZERO');
  }
  if (Number(charter.max_concurrency ?? 1) !== 1) {
    errors.push('MAX_CONCURRENCY_MUST_BE_ONE');
  }
  if (Number(charter.max_requests ?? 1) < 1) {
    errors.push('MAX_REQUESTS_INVALID');
  }
  if (Number(charter.max_activation_changes ?? 2) !== 2) {
    errors.push('MAX_ACTIVATION_CHANGES_MUST_BE_TWO');
  }
  if (charter.unattended === true || charter.auto_trigger === true) {
    errors.push('UNATTENDED_MODE_FORBIDDEN');
  }
  if (charter.consumed === true) {
    errors.push('CHARTER_ALREADY_CONSUMED');
  }
  const dry = isDryLifecycleCharter(charter);
  if (dry) {
    if (Number(charter.max_requests ?? 1) !== 1) {
      errors.push('DRY_MAX_REQUESTS_MUST_BE_ONE');
    }
    if (charter.allow_telegram === true) {
      errors.push('DRY_ALLOW_TELEGRAM_FORBIDDEN');
    }
    if (charter.allow_data_table_mutation === true) {
      errors.push('DRY_ALLOW_DATA_TABLE_MUTATION_FORBIDDEN');
    }
  } else if (
    charter.planned_requests != null &&
    Number(charter.planned_requests) === 0 &&
    charter.allow_webhook_requests !== false
  ) {
    errors.push('PLANNED_ZERO_REQUIRES_ALLOW_WEBHOOK_FALSE');
  }
  // No secrets in charter
  const forbiddenKeys = [
    'api_key',
    'token',
    'secret',
    'password',
    'webhook_url',
    'authorization',
    'headers',
  ];
  for (const k of Object.keys(charter)) {
    if (forbiddenKeys.includes(k.toLowerCase())) {
      errors.push(`SECRET_KEY_FORBIDDEN:${k}`);
    }
  }
  return { ok: errors.length === 0, errors, dry_lifecycle: dry };
}

/**
 * Empty sanitized evidence skeleton.
 */
export function createLifecycleEvidence(charter) {
  return {
    phase: '1B-D6C',
    charter_id: charter?.charter_id ?? null,
    workflow_id: charter?.workflow_id ?? null,
    workflow_version: charter?.expected_version_id ?? null,
    initial_active: null,
    preflight_result: null,
    activation_attempts: 0,
    activation_changes: 0,
    readiness_result: null,
    window_opened: false,
    window_opened_at_ms: null,
    window_deadline_ms: null,
    requests_attempted: 0,
    requests_used: 0,
    requests_remaining: Number(charter?.max_requests ?? 1),
    request_result_class: null,
    deactivation_attempts: 0,
    emergency_containment_attempts: 0,
    final_active: null,
    containment_verified: false,
    final_lifecycle_state: LIFECYCLE_STATES.CONTAINED,
    anomalies: /** @type {string[]} */ ([]),
    charter_consumed: false,
    consumption: {
      activation_attempts: 0,
      activation_changes: 0,
      requests_attempted: 0,
      deactivation_attempts: 0,
      containment_verified: false,
    },
  };
}

/**
 * Sanitize evidence — strip secrets/URLs/payloads.
 * @param {Record<string, unknown>} evidence
 */
export function sanitizeLifecycleEvidence(evidence) {
  const json = JSON.stringify(evidence);
  if (
    /api[_-]?key|Bearer\s|n8n\.ai-metacode\.com\/webhook|telegram|password|secret/i.test(
      json,
    ) &&
    /"(api_key|token|password|secret|webhook_url|authorization)"\s*:/.test(json)
  ) {
    throw new Error('EVIDENCE_CONTAINS_FORBIDDEN_SECRET_FIELDS');
  }
  return { ...evidence, anomalies: [...(evidence.anomalies || [])] };
}

/**
 * @param {object} deps
 * @param {import('./client-ops-lifecycle-offline-transport.mjs').createOfflineLifecycleTransport extends Function ? any : any} deps.transport
 * @param {{ nowMs: () => number, advance?: (n:number)=>number }} deps.clock
 * @param {Record<string, unknown>} deps.charter
 * @param {{
 *   lockPath: string,
 *   ownerToken: string,
 *   processAlive?: (pid:number)=>boolean,
 *   allowExplicitStaleRecovery?: boolean,
 * }} deps.lock
 * @param {{ sendRequest?: boolean }} [deps.options]
 */
export async function runBoundedActivationLifecycle(deps) {
  const { transport, clock, charter, lock } = deps;
  const options = deps.options || {};
  const dryLifecycle = isDryLifecycleCharter(charter);
  // Dry charter always forces zero webhook invocations (no fallback auto-send).
  const sendRequest = dryLifecycle ? false : options.sendRequest !== false;

  const evidence = createLifecycleEvidence(charter);
  evidence.dry_lifecycle = dryLifecycle;
  evidence.planned_requests = Number(charter.planned_requests ?? (sendRequest ? 1 : 0));
  evidence.allow_webhook_requests = dryLifecycle ? false : charter.allow_webhook_requests !== false;
  let state = LIFECYCLE_STATES.CONTAINED;
  let ownerToken = lock.ownerToken;
  let lockAcquired = false;
  let window = null;

  const failClosed = (reason, extra = {}) => {
    evidence.final_lifecycle_state = LIFECYCLE_STATES.FAILED_CLOSED;
    evidence.anomalies.push(reason);
    evidence.preflight_result = {
      ok: false,
      reason,
      ...extra,
    };
    state = LIFECYCLE_STATES.FAILED_CLOSED;
    return finalize(evidence, state, { activation_attempts: evidence.activation_attempts });
  };

  const charterCheck = validateLifecycleCharter(charter);
  if (!charterCheck.ok) {
    return failClosed('CHARTER_INVALID', { errors: charterCheck.errors });
  }
  if (dryLifecycle) {
    const zeroInv = assertZeroRequestInvariant(charter, { sendRequest: false });
    if (!zeroInv.ok) {
      return failClosed('ZERO_REQUEST_INVARIANT_FAILED', { errors: zeroInv.errors });
    }
    evidence.zero_request_invariant = zeroInv;
  }

  // --- Lock ---
  const wfBeforeLock = await transport.getWorkflowState(clock.nowMs());
  const lockResult = acquireLifecycleLock({
    lockPath: lock.lockPath,
    workflowId: String(charter.workflow_id),
    charterId: String(charter.charter_id),
    ownerToken,
    nowMs: clock.nowMs(),
    processAlive: lock.processAlive,
    workflowActive: wfBeforeLock.active,
    allowExplicitStaleRecovery: Boolean(lock.allowExplicitStaleRecovery),
  });
  if (!lockResult.ok) {
    return failClosed(lockResult.reason, { lock_classification: lockResult.classification });
  }
  lockAcquired = true;
  ownerToken = lockResult.owner_token;

  // Mark charter session started (partial consumption on any activation attempt)
  const markConsumed = () => {
    evidence.charter_consumed = true;
    charter.consumed = true;
  };

  try {
    // --- Preflight ---
    const preflight = await runPreflight({ transport, clock, charter });
    evidence.preflight_result = preflight;
    evidence.initial_active = preflight.initial_active;
    if (!preflight.ok) {
      evidence.final_lifecycle_state = LIFECYCLE_STATES.FAILED_CLOSED;
      state = LIFECYCLE_STATES.FAILED_CLOSED;
      // Release lock — never activated
      releaseLifecycleLock({
        lockPath: lock.lockPath,
        ownerToken,
        charterId: String(charter.charter_id),
        containmentVerified: true,
      });
      lockAcquired = false;
      return finalize(evidence, state);
    }
    state = LIFECYCLE_STATES.PREFLIGHT_PASSED;

    // --- Activate ---
    state = LIFECYCLE_STATES.ACTIVATING;
    evidence.activation_attempts += 1;
    markConsumed();
    const activateResult = await transport.activate(clock.nowMs());
    evidence.activation_changes = transport.getActivationChanges();
    evidence.consumption.activation_attempts = evidence.activation_attempts;
    evidence.consumption.activation_changes = evidence.activation_changes;

    if (evidence.activation_changes > Number(charter.max_activation_changes ?? 2)) {
      evidence.anomalies.push('ACTIVATION_CHANGE_BUDGET_EXCEEDED');
      const after = await transport.getWorkflowState(clock.nowMs());
      // Fail closed: attempt recontain without request
      const contain = await closeAndRecontain({
        transport,
        clock,
        charter,
        evidence,
        lock,
        ownerToken,
        reason: 'ACTIVATION_CHANGE_BUDGET_EXCEEDED',
      });
      lockAcquired = !contain.lock_released;
      if (after.active && !evidence.containment_verified) {
        evidence.final_lifecycle_state = LIFECYCLE_STATES.CONTAINMENT_FAILED;
      } else if (!evidence.final_lifecycle_state || evidence.final_lifecycle_state === LIFECYCLE_STATES.RECONTAINED) {
        evidence.final_lifecycle_state = LIFECYCLE_STATES.FAILED_CLOSED;
      }
      return finalize(evidence, evidence.final_lifecycle_state);
    }

    if (activateResult.error_class) {
      const after = await transport.getWorkflowState(clock.nowMs());
      evidence.final_active = after.active;
      evidence.containment_verified = after.active === false;
      evidence.final_lifecycle_state = after.active
        ? LIFECYCLE_STATES.CONTAINMENT_FAILED
        : LIFECYCLE_STATES.FAILED_CLOSED;
      evidence.anomalies.push('ACTIVATION_API_FAILURE');
      if (evidence.containment_verified) {
        releaseLifecycleLock({
          lockPath: lock.lockPath,
          ownerToken,
          charterId: String(charter.charter_id),
          containmentVerified: true,
        });
        lockAcquired = false;
      }
      return finalize(evidence, evidence.final_lifecycle_state);
    }

    // --- Readiness ---
    const readiness = await verifyReadiness({
      transport,
      clock,
      charter,
      activateResult,
    });
    evidence.readiness_result = readiness;

    if (!readiness.ok) {
      state = LIFECYCLE_STATES.ACTIVE_NOT_READY;
      evidence.anomalies.push(readiness.reason || 'ACTIVE_NOT_READY');
      const contain = await closeAndRecontain({
        transport,
        clock,
        charter,
        evidence,
        lock,
        ownerToken,
        reason: 'ACTIVE_NOT_READY',
      });
      lockAcquired = !contain.lock_released;
      return finalize(evidence, evidence.final_lifecycle_state);
    }

    state = LIFECYCLE_STATES.ACTIVE_READY;

    // --- Request window ---
    const maxRequests = Number(charter.max_requests ?? D6C_DEFAULTS.max_requests);
    const windowSeconds = Number(charter.window_seconds ?? D6C_DEFAULTS.window_seconds);
    window = {
      opened_at_ms: clock.nowMs(),
      deadline_ms: clock.nowMs() + windowSeconds * 1000,
      requests_used: 0,
      max_requests: maxRequests,
      closed: false,
    };
    evidence.window_opened = true;
    evidence.window_opened_at_ms = window.opened_at_ms;
    evidence.window_deadline_ms = window.deadline_ms;
    evidence.requests_remaining = maxRequests;
    state = LIFECYCLE_STATES.REQUEST_WINDOW_OPEN;

    let requestResult = null;
    let dryReject = null;
    if (sendRequest) {
      // Budget / deadline
      if (clock.nowMs() > window.deadline_ms) {
        evidence.anomalies.push('REQUEST_WINDOW_DEADLINE_EXPIRED');
        window.closed = true;
        state = LIFECYCLE_STATES.REQUEST_WINDOW_CLOSED;
      } else if (window.requests_used >= window.max_requests) {
        evidence.anomalies.push('REQUEST_BUDGET_EXHAUSTED');
        window.closed = true;
        state = LIFECYCLE_STATES.REQUEST_WINDOW_CLOSED;
      } else {
        const reval = await revalidateBeforeRequest({
          transport,
          clock,
          charter,
          evidence,
          lock,
          ownerToken,
        });
        if (!reval.ok) {
          evidence.anomalies.push(reval.reason);
          window.closed = true;
          state = LIFECYCLE_STATES.REQUEST_WINDOW_CLOSED;
        } else if (clock.nowMs() > window.deadline_ms) {
          evidence.anomalies.push('REQUEST_WINDOW_DEADLINE_EXPIRED');
          window.closed = true;
          state = LIFECYCLE_STATES.REQUEST_WINDOW_CLOSED;
        } else {
          // Activation change budget check before POST
          if (evidence.activation_changes > Number(charter.max_activation_changes ?? 2)) {
            evidence.anomalies.push('ACTIVATION_CHANGE_BUDGET_EXCEEDED');
            window.closed = true;
            state = LIFECYCLE_STATES.REQUEST_WINDOW_CLOSED;
          } else {
            evidence.requests_attempted += 1;
            window.requests_used += 1;
            evidence.requests_used = window.requests_used;
            evidence.requests_remaining = Math.max(0, maxRequests - window.requests_used);
            evidence.consumption.requests_attempted = evidence.requests_attempted;
            requestResult = await transport.postWebhook(
              { event_id: charter.event_id, payload_ref: 'REDACTED' },
              clock.nowMs(),
            );
            evidence.request_result_class = requestResult.result_class;
            // Exhausted after one (default)
            if (window.requests_used >= window.max_requests) {
              window.closed = true;
              state = LIFECYCLE_STATES.REQUEST_WINDOW_CLOSED;
            }
          }
        }
      }
    } else {
      // Dry window: budget exists but charter forbids invocation; still deactivate.
      dryReject = assertWebhookRequestProhibitedByCharter(charter);
      evidence.dry_request_reject = dryReject;
      evidence.anomalies.push('DRY_WINDOW_NO_REQUEST');
      evidence.requests_used = 0;
      evidence.requests_attempted = 0;
      window.requests_used = 0;
      window.closed = true;
      state = LIFECYCLE_STATES.REQUEST_WINDOW_CLOSED;
    }

    // Second request attempt helper path is rejected by budget enforcement in API
    evidence._window = window;

    // --- Unconditional deactivation after window ---
    const contain = await closeAndRecontain({
      transport,
      clock,
      charter,
      evidence,
      lock,
      ownerToken,
      reason: 'WINDOW_COMPLETE',
      requestResult,
    });
    lockAcquired = !contain.lock_released;
    return finalize(evidence, evidence.final_lifecycle_state, {
      request_result: requestResult,
      dry_request_reject: dryReject,
      second_request_guard: createRequestBudgetGuard(window),
    });
  } catch (err) {
    evidence.anomalies.push(`LIFECYCLE_EXCEPTION:${err instanceof Error ? err.message : 'UNKNOWN'}`);
    try {
      await closeAndRecontain({
        transport,
        clock,
        charter,
        evidence,
        lock,
        ownerToken,
        reason: 'EXCEPTION',
      });
      lockAcquired = false;
    } catch {
      evidence.final_lifecycle_state = LIFECYCLE_STATES.CONTAINMENT_FAILED;
      evidence.containment_verified = false;
    }
    return finalize(evidence, evidence.final_lifecycle_state);
  } finally {
    if (lockAcquired) {
      // Do not release if containment not verified
      const rel = releaseLifecycleLock({
        lockPath: lock.lockPath,
        ownerToken,
        charterId: String(charter.charter_id),
        containmentVerified: evidence.containment_verified === true,
      });
      if (!rel.ok && evidence.containment_verified) {
        evidence.anomalies.push(`LOCK_RELEASE_FAILED:${rel.reason}`);
      }
    }
  }
}

/**
 * Attempt a second request against a closed/exhausted window (local reject).
 * @param {{ requests_used: number, max_requests: number, closed?: boolean, deadline_ms?: number }} window
 * @param {{ nowMs: () => number }} [clock]
 */
export function createRequestBudgetGuard(window, clock) {
  return {
    canRequest() {
      if (!window || window.closed) return { ok: false, reason: 'WINDOW_CLOSED' };
      if (window.requests_used >= window.max_requests) {
        return { ok: false, reason: 'REQUEST_BUDGET_EXHAUSTED' };
      }
      if (clock && window.deadline_ms != null && clock.nowMs() > window.deadline_ms) {
        return { ok: false, reason: 'REQUEST_WINDOW_DEADLINE_EXPIRED' };
      }
      return { ok: true };
    },
  };
}

async function runPreflight({ transport, clock, charter }) {
  const gates = [];
  const wf = await transport.getWorkflowState(clock.nowMs());
  const dry = isDryLifecycleCharter(charter);

  const push = (id, ok, detail = {}) => gates.push({ id, ok, ...detail });

  push('workflow_id', wf.id === charter.workflow_id && wf.id === D6C_ALLOWED_WORKFLOW_ID, {
    observed: wf.id,
  });
  push('initial_inactive', wf.active === false, { observed_active: wf.active });
  if (wf.active === true) {
    return {
      ok: false,
      reason: 'UNEXPECTED_ACTIVE_BEFORE_CHARTER',
      initial_active: true,
      gates,
      operator_action: 'FAIL_STOP_OR_EXPLICIT_RECONTAIN_THEN_RESTART',
      preflight_kind: dry ? 'DRY_LIFECYCLE' : 'SOURCE_DELIVERY',
    };
  }
  push('version_pin', wf.versionId === charter.expected_version_id, {
    observed: wf.versionId,
    expected: charter.expected_version_id,
  });
  push('running_zero', Number(wf.running) === 0, { running: wf.running });
  push('request_budget', Number(charter.max_requests) > 0);
  push('max_requests_one', Number(charter.max_requests ?? 1) === 1);
  push('max_activation_changes_two', Number(charter.max_activation_changes ?? 2) === 2);
  push('retry_budget_zero', Number(charter.max_retries ?? 0) === 0);
  push('concurrency_one', Number(charter.max_concurrency ?? 1) === 1);
  if (wf.nodes != null) {
    push('nodes_expected', Number(wf.nodes) === Number(charter.expected_nodes ?? 20), {
      observed: wf.nodes,
      expected: charter.expected_nodes ?? 20,
    });
  }

  let eligibility = null;
  let dedupe = { event_id: null, seen: false, skipped: false };

  if (dry) {
    push('planned_requests_zero', Number(charter.planned_requests) === 0);
    push('allow_webhook_false', charter.allow_webhook_requests === false);
    push('dry_control_marker', charter.dry_control === true || charter.operation_type === 'DRY_CONTROL_NO_REQUEST', {
      dry_control: charter.dry_control === true,
      operation_type: charter.operation_type || null,
    });
    // No fabricated SITE-002 event required; skip source delivery + dedupe gates.
    push('source_delivery_gates_skipped', true, { reason: 'DRY_LIFECYCLE_PREFLIGHT' });
    dedupe = { event_id: null, seen: false, skipped: true, reason: 'DRY_LIFECYCLE_NO_SOURCE_EVENT' };
  } else {
    const age = resolveSourceAgeSeconds(
      {
        age_seconds: charter.source?.age_seconds,
        observed_at: charter.source?.observed_at,
      },
      clock,
    );
    eligibility = evaluateDeliveryEligibility({
      source_status: charter.source?.source_status,
      normalized_status: charter.source?.normalized_status || charter.source?.source_status,
      age_seconds: age,
      security_rejected: charter.source?.security_rejected,
    });
    push(
      'delivery_eligibility_fresh',
      eligibility.delivery_eligibility === DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
      eligibility,
    );

    if (!charter.event_id) {
      push('event_id', false, { reason: 'EVENT_ID_REQUIRED' });
    } else {
      push('event_id', true, { event_id: charter.event_id });
    }

    dedupe = await transport.checkDedupe(String(charter.event_id || ''), clock.nowMs());
    const opType = charter.operation_type || 'NEW_DELIVERY_FIRST_SEEN';
    if (opType === 'NEW_DELIVERY_FIRST_SEEN' && dedupe.seen) {
      push('dedupe_unseen', false, { seen: true });
    } else {
      push('dedupe_unseen', true, { seen: dedupe.seen });
    }
  }

  push('webhook_path', wf.webhook_path_present === true);
  push('auth_structural', wf.auth_config_structurally_present === true);

  const failed = gates.filter((g) => !g.ok);
  return {
    ok: failed.length === 0,
    reason: failed[0]?.id || null,
    failed_gates: failed.map((g) => g.id),
    gates,
    initial_active: wf.active,
    eligibility,
    dedupe,
    preflight_kind: dry ? 'DRY_LIFECYCLE' : 'SOURCE_DELIVERY',
  };
}

async function verifyReadiness({ transport, clock, charter, activateResult }) {
  const wf = await transport.getWorkflowState(clock.nowMs());
  if (activateResult.active_after !== true && wf.active !== true) {
    return { ok: false, reason: 'ACTIVATION_GET_INACTIVE', workflow: summarizeWf(wf) };
  }
  if (wf.active !== true) {
    return { ok: false, reason: 'READINESS_ACTIVE_FALSE', workflow: summarizeWf(wf) };
  }
  if (wf.id !== charter.workflow_id) {
    return { ok: false, reason: 'READINESS_WORKFLOW_ID_MISMATCH', workflow: summarizeWf(wf) };
  }
  if (wf.versionId !== charter.expected_version_id) {
    return { ok: false, reason: 'READINESS_VERSION_MISMATCH', workflow: summarizeWf(wf) };
  }
  if (!wf.webhook_path_present) {
    return { ok: false, reason: 'READINESS_WEBHOOK_PATH_MISSING', workflow: summarizeWf(wf) };
  }
  if (!wf.auth_config_structurally_present) {
    return { ok: false, reason: 'READINESS_AUTH_STRUCTURAL_MISSING', workflow: summarizeWf(wf) };
  }
  if (Number(wf.running) !== 0 && charter.allow_running_during_ready !== true) {
    return { ok: false, reason: 'READINESS_RUNNING_UNEXPECTED', workflow: summarizeWf(wf) };
  }
  return { ok: true, reason: null, workflow: summarizeWf(wf) };
}

async function revalidateBeforeRequest({ transport, clock, charter, evidence, lock, ownerToken }) {
  const age = resolveSourceAgeSeconds(
    {
      age_seconds:
        charter.source?.age_seconds_fixed === true
          ? charter.source.age_seconds
          : charter.source?.recompute_age === false
            ? charter.source.age_seconds
            : null,
      observed_at: charter.source?.observed_at,
    },
    clock,
  );
  // Prefer recompute from observed_at when present; else use provided age_seconds
  const ageResolved =
    charter.source?.observed_at != null
      ? resolveSourceAgeSeconds({ observed_at: charter.source.observed_at }, clock)
      : charter.source?.age_seconds != null
        ? Number(charter.source.age_seconds)
        : age;

  const eligibility = evaluateDeliveryEligibility({
    source_status: charter.source?.source_status,
    normalized_status: charter.source?.normalized_status || charter.source?.source_status,
    age_seconds: ageResolved,
    security_rejected: charter.source?.security_rejected,
  });
  if (eligibility.delivery_eligibility !== DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE) {
    return { ok: false, reason: 'PRE_REQUEST_FRESHNESS_FAILED', eligibility };
  }

  const dedupe = await transport.checkDedupe(String(charter.event_id), clock.nowMs());
  if ((charter.operation_type || 'NEW_DELIVERY_FIRST_SEEN') === 'NEW_DELIVERY_FIRST_SEEN' && dedupe.seen) {
    return { ok: false, reason: 'PRE_REQUEST_DEDUPE_SEEN', dedupe };
  }

  const wf = await transport.getWorkflowState(clock.nowMs());
  if (wf.active !== true) {
    return { ok: false, reason: 'PRE_REQUEST_NOT_ACTIVE' };
  }
  if (wf.versionId !== charter.expected_version_id) {
    return { ok: false, reason: 'PRE_REQUEST_VERSION_MISMATCH', workflow: summarizeWf(wf) };
  }

  const existing = readLifecycleLock(lock.lockPath);
  if (!existing || existing.owner_token !== ownerToken) {
    return { ok: false, reason: 'PRE_REQUEST_LOCK_OWNERSHIP_LOST' };
  }

  if (evidence.requests_used >= Number(charter.max_requests ?? 1)) {
    return { ok: false, reason: 'PRE_REQUEST_BUDGET_EXHAUSTED' };
  }

  return { ok: true, eligibility, dedupe, workflow: summarizeWf(wf) };
}

async function closeAndRecontain({
  transport,
  clock,
  charter,
  evidence,
  lock,
  ownerToken,
  reason,
}) {
  evidence.anomalies.push(`CLOSE_REASON:${reason}`);
  let deact = await transport.deactivate(clock.nowMs(), { emergency: false });
  evidence.deactivation_attempts += 1;
  evidence.activation_changes = transport.getActivationChanges();
  evidence.consumption.deactivation_attempts = evidence.deactivation_attempts;
  evidence.consumption.activation_changes = evidence.activation_changes;

  let recon = await verifyRecontainment({ transport, clock, charter, evidence });

  if (!recon.ok && evidence.deactivation_attempts <= D6C_DEFAULTS.normal_deactivation_attempts) {
    // Emergency containment — NOT a delivery retry
    evidence.emergency_containment_attempts += 1;
    evidence.anomalies.push('EMERGENCY_CONTAINMENT_ATTEMPTED');
    deact = await transport.deactivate(clock.nowMs(), { emergency: true });
    evidence.deactivation_attempts += 1;
    evidence.activation_changes = transport.getActivationChanges();
    evidence.consumption.deactivation_attempts = evidence.deactivation_attempts;
    recon = await verifyRecontainment({ transport, clock, charter, evidence });
    if (recon.ok) {
      evidence.final_lifecycle_state = LIFECYCLE_STATES.RECONTAINED_WITH_ANOMALY;
      evidence.containment_verified = true;
      evidence.final_active = false;
      evidence.consumption.containment_verified = true;
      const rel = releaseLifecycleLock({
        lockPath: lock.lockPath,
        ownerToken,
        charterId: String(charter.charter_id),
        containmentVerified: true,
      });
      return { lock_released: Boolean(rel.released || rel.ok), recon, deact };
    }
  }

  if (!recon.ok) {
    evidence.final_lifecycle_state = LIFECYCLE_STATES.CONTAINMENT_FAILED;
    evidence.containment_verified = false;
    evidence.final_active = recon.workflow?.active ?? true;
    evidence.anomalies.push('CONTAINMENT_FAILED_OVERRIDES_DELIVERY');
    evidence.operator_emergency = {
      action: 'MANUAL_DEACTIVATE_ALLOWLISTED_WORKFLOW_AND_VERIFY_GET_ACTIVE_FALSE',
      workflow_id: D6C_ALLOWED_WORKFLOW_ID,
      do_not_release_lifecycle_as_complete: true,
      do_not_send_further_requests: true,
    };
    return { lock_released: false, recon, deact };
  }

  // Check activation change budget anomaly (expected 2 for full cycle)
  if (evidence.activation_changes > Number(charter.max_activation_changes ?? 2)) {
    evidence.anomalies.push('ACTIVATION_CHANGE_BUDGET_EXCEEDED');
    evidence.final_lifecycle_state = LIFECYCLE_STATES.RECONTAINED_WITH_ANOMALY;
  } else if (reason === 'ACTIVE_NOT_READY') {
    evidence.final_lifecycle_state = LIFECYCLE_STATES.RECONTAINED_WITH_ANOMALY;
  } else if (evidence.anomalies.some((a) => a.startsWith('PRE_REQUEST_') || a === 'REQUEST_WINDOW_DEADLINE_EXPIRED')) {
    evidence.final_lifecycle_state = LIFECYCLE_STATES.RECONTAINED_WITH_ANOMALY;
  } else {
    evidence.final_lifecycle_state = LIFECYCLE_STATES.RECONTAINED;
  }

  evidence.containment_verified = true;
  evidence.final_active = false;
  evidence.consumption.containment_verified = true;
  const rel = releaseLifecycleLock({
    lockPath: lock.lockPath,
    ownerToken,
    charterId: String(charter.charter_id),
    containmentVerified: true,
  });
  return { lock_released: Boolean(rel.released || rel.ok), recon, deact };
}

async function verifyRecontainment({ transport, clock, charter, evidence }) {
  const wf = await transport.getWorkflowState(clock.nowMs());
  const checks = [];
  checks.push({ id: 'active_false', ok: wf.active === false });
  checks.push({
    id: 'running_zero',
    ok: Number(wf.running) === 0 || charter.allow_running_on_recontain === true,
  });
  checks.push({
    id: 'version_unchanged',
    ok: wf.versionId === charter.expected_version_id,
  });

  if (wf.active !== false) {
    return { ok: false, reason: 'STILL_ACTIVE', workflow: summarizeWf(wf), checks };
  }

  // Running executions with inactive workflow: severe unless charter allows.
  if (Number(wf.running) > 0 && charter.allow_running_on_recontain !== true) {
    evidence.anomalies.push('RECONTAIN_RUNNING_UNEXPECTED');
    return {
      ok: false,
      reason: 'RUNNING_EXECUTIONS_REMAIN',
      workflow: summarizeWf(wf),
      checks,
    };
  }

  if (wf.versionId !== charter.expected_version_id) {
    evidence.anomalies.push('VERSION_DRIFT_ON_RECONTAIN');
    // active=false is the hard containment gate; version drift is anomaly.
  }

  return {
    ok: true,
    reason: null,
    workflow: summarizeWf(wf),
    checks,
  };
}

function summarizeWf(wf) {
  return {
    id: wf.id,
    active: wf.active,
    versionId: wf.versionId,
    nodes: wf.nodes,
    running: wf.running,
    webhook_path_present: wf.webhook_path_present,
    auth_config_structurally_present: wf.auth_config_structurally_present,
  };
}

function finalize(evidence, state, extra = {}) {
  evidence.final_lifecycle_state = state;
  const sanitized = sanitizeLifecycleEvidence(evidence);
  return {
    ok:
      state === LIFECYCLE_STATES.RECONTAINED ||
      state === LIFECYCLE_STATES.RECONTAINED_WITH_ANOMALY,
    containment_verified: evidence.containment_verified === true,
    state,
    evidence: sanitized,
    ...extra,
  };
}

/**
 * State machine documentation helper (pure).
 */
export function describeActivationStateMachine() {
  return {
    model: 'HYBRID_C1_TO_C3_BOUNDED',
    required_initial_workflow_active: false,
    states: Object.values(LIFECYCLE_STATES),
    transitions: [
      'CONTAINED -> PREFLIGHT_PASSED | FAILED_CLOSED',
      'PREFLIGHT_PASSED -> ACTIVATING',
      'ACTIVATING -> ACTIVE_READY | ACTIVE_NOT_READY | FAILED_CLOSED | CONTAINMENT_FAILED',
      'ACTIVE_NOT_READY -> DEACTIVATING',
      'ACTIVE_READY -> REQUEST_WINDOW_OPEN',
      'REQUEST_WINDOW_OPEN -> REQUEST_WINDOW_CLOSED',
      'REQUEST_WINDOW_CLOSED -> DEACTIVATING',
      'DEACTIVATING -> RECONTAINED | RECONTAINED_WITH_ANOMALY | CONTAINMENT_FAILED',
    ],
    defaults: D6C_DEFAULTS,
  };
}

export {
  acquireLifecycleLock,
  releaseLifecycleLock,
  classifyLifecycleLock,
  readLifecycleLock,
};
