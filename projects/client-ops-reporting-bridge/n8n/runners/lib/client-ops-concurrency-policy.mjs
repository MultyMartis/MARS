/**
 * Phase 1B-D6E — concurrency policy (offline).
 * max_safe_concurrency remains 1. D1 sequential-safe concurrency unproven overturned: NO.
 */

import { MAX_SAFE_CONCURRENCY, MAX_RETRIES } from './client-ops-delivery-ledger.mjs';
import { REASON_CODES } from './client-ops-retry-reason-codes.mjs';
import {
  acquireLifecycleLock,
  classifyLifecycleLock,
  readLifecycleLock,
} from './client-ops-lifecycle-lock.mjs';

export const D6E_MAX_SAFE_CONCURRENCY = 1;
export const D6E_MAX_AUTOMATIC_RETRIES = 0;

if (MAX_SAFE_CONCURRENCY !== 1 || MAX_RETRIES !== 0) {
  throw new Error('D6E requires Workstream A max_retries=0 concurrency=1');
}

if (D6E_MAX_SAFE_CONCURRENCY !== MAX_SAFE_CONCURRENCY) {
  throw new Error('D6E concurrency baseline drift vs ledger');
}

/**
 * Evaluate whether a delivery/retry attempt may proceed under concurrency=1.
 *
 * @param {{
 *   event_id: string,
 *   other_event_id?: string|null,
 *   same_event_parallel?: boolean,
 *   different_event_parallel?: boolean,
 *   lifecycle_lock_path?: string|null,
 *   lifecycle_lock_held_by_other?: boolean,
 *   unresolved_active_session?: boolean,
 *   request_budget_exhausted?: boolean,
 *   delivery_state?: string|null,
 *   delivery_eligibility?: string|null,
 *   now_ms?: number,
 *   process_alive?: (pid: number) => boolean,
 *   workflow_active?: boolean|null,
 * }} obs
 */
export function evaluateConcurrencyPolicy(obs) {
  const base = {
    max_safe_concurrency: D6E_MAX_SAFE_CONCURRENCY,
    max_automatic_retries: D6E_MAX_AUTOMATIC_RETRIES,
    concurrency_allowed: false,
    retry_authorized: false,
    reason_code: null,
  };

  if (obs.same_event_parallel === true) {
    return {
      ...base,
      reason_code: REASON_CODES.SAME_EVENT_CONCURRENCY_FORBIDDEN,
      rejected: true,
    };
  }

  if (obs.different_event_parallel === true) {
    return {
      ...base,
      reason_code: REASON_CODES.GLOBAL_CONCURRENCY_LIMIT,
      rejected: true,
    };
  }

  if (obs.lifecycle_lock_held_by_other === true) {
    return {
      ...base,
      reason_code: REASON_CODES.LIFECYCLE_LOCK_HELD,
      rejected: true,
    };
  }

  if (obs.unresolved_active_session === true) {
    return {
      ...base,
      reason_code: REASON_CODES.GLOBAL_CONCURRENCY_LIMIT,
      rejected: true,
    };
  }

  if (obs.request_budget_exhausted === true) {
    return {
      ...base,
      reason_code: REASON_CODES.REQUEST_BUDGET_EXHAUSTED,
      rejected: true,
    };
  }

  if (obs.delivery_state === 'PENDING') {
    return {
      ...base,
      reason_code: REASON_CODES.PENDING_NEVER_AUTO_RETRY,
      rejected: true,
      note: 'PENDING must not consume a new delivery attempt',
    };
  }

  if (obs.delivery_state === 'SENT') {
    return {
      ...base,
      reason_code: REASON_CODES.ALREADY_SENT,
      rejected: true,
    };
  }

  if (obs.delivery_state === 'FAILED') {
    return {
      ...base,
      reason_code: REASON_CODES.DELIVERY_FAILED_TERMINAL,
      rejected: true,
    };
  }

  if (
    obs.delivery_eligibility === 'STALE_REVIEW_REQUIRED' ||
    obs.delivery_eligibility === 'NOT_SAFE_TO_SEND'
  ) {
    return {
      ...base,
      reason_code:
        obs.delivery_eligibility === 'STALE_REVIEW_REQUIRED'
          ? REASON_CODES.SOURCE_STALE_REVIEW_REQUIRED
          : REASON_CODES.SOURCE_NOT_ELIGIBLE,
      rejected: true,
    };
  }

  if (obs.lifecycle_lock_path) {
    const existing = readLifecycleLock(obs.lifecycle_lock_path);
    if (existing) {
      const cls = classifyLifecycleLock(existing, {
        nowMs: Number(obs.now_ms ?? Date.now()),
        processAlive: obs.process_alive,
        workflowActive: obs.workflow_active ?? false,
      });
      if (cls.action === 'FAIL_CLOSED' || cls.action === 'FAIL_CLOSED_OPERATOR_REVIEW') {
        return {
          ...base,
          reason_code: REASON_CODES.LIFECYCLE_LOCK_HELD,
          rejected: true,
          lock_class: cls.class,
        };
      }
    }
  }

  return {
    ...base,
    concurrency_allowed: true,
    rejected: false,
    reason_code: null,
    note: 'Policy permits at most one concurrent lifecycle under charter; execution still requires C lifecycle',
  };
}

/**
 * Attempt exclusive lifecycle ownership for concurrency fixtures (offline).
 * Wraps acquireLifecycleLock option object API.
 */
export function tryAcquireExclusiveLifecycleOwnership(lockPath, record, opts = {}) {
  return acquireLifecycleLock({
    lockPath,
    workflowId: record.workflow_id,
    charterId: record.charter_id,
    ownerToken: record.owner_token,
    nowMs: opts.nowMs ?? record.created_at_ms,
    leaseMs: Math.max(1, Number(record.lease_expires_at_ms) - Number(record.created_at_ms || opts.nowMs || 0)),
    pid: record.pid,
    processIdentity: record.process_identity,
    processAlive: opts.processAlive,
    workflowActive: opts.workflow_active ?? false,
    allowExplicitStaleRecovery: opts.allowExplicitStaleRecovery === true,
  });
}

export function describeConcurrencyModel() {
  return {
    max_safe_concurrency: D6E_MAX_SAFE_CONCURRENCY,
    max_automatic_retries: D6E_MAX_AUTOMATIC_RETRIES,
    same_event_concurrency: 'FORBIDDEN',
    different_event_concurrency: 'FORBIDDEN_UNTIL_ATOMICITY_PROVEN',
    d1_historical: 'DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN',
    overturned_by_abc: false,
    verdict: 'D6E_CONCURRENCY_REMAINS_ONE',
    layers: [
      'source_producer_invocation',
      'lifecycle_orchestration',
      'workflow_activation',
      'webhook_request',
      'data_table_first_seen_claim',
      'telegram_delivery',
      'delivery_finalization',
    ],
  };
}
