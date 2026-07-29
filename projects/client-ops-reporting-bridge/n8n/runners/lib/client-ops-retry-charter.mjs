/**
 * Phase 1B-D6E — explicit retry charter validator (offline).
 * No automatic retry. No network.
 */

import { MAX_RETRIES, MAX_SAFE_CONCURRENCY } from './client-ops-delivery-ledger.mjs';
import { REASON_CODES } from './client-ops-retry-reason-codes.mjs';

export const RETRY_CHARTER_SCHEMA_VERSION = 1;

export const D6E_RETRY_DEFAULTS = Object.freeze({
  automatic_retry_budget: 0,
  manual_bounded_retry_budget: 1,
  max_safe_concurrency: MAX_SAFE_CONCURRENCY,
  max_automatic_retries: MAX_RETRIES,
  automatic_retries_enabled: false,
});

/**
 * Validate an explicit retry charter. Never authorizes automatic dispatch.
 *
 * @param {Record<string, unknown>|null|undefined} charter
 * @param {{
 *   event_id: string,
 *   source_identity_fingerprint?: string|null,
 *   policy_decision?: string,
 *   now_ms?: number,
 * }} ctx
 */
export function validateRetryCharter(charter, ctx) {
  const errors = [];
  if (!charter || typeof charter !== 'object') {
    return reject(REASON_CODES.RETRY_CHARTER_REQUIRED, errors.concat(['missing_charter']));
  }

  if (charter.schema_version !== RETRY_CHARTER_SCHEMA_VERSION) {
    errors.push('schema_version_invalid');
  }
  if (!charter.charter_id || typeof charter.charter_id !== 'string') {
    errors.push('charter_id_required');
  }
  if (charter.retry_decision !== 'SAFE_TO_RETRY') {
    errors.push('retry_decision_must_be_SAFE_TO_RETRY');
  }
  if (charter.automatic_retry === true) {
    errors.push('automatic_retry_forbidden');
  }
  if (Number(charter.max_retry_attempts ?? -1) !== 1) {
    errors.push('manual_budget_must_be_1');
  }
  if (Number(charter.max_concurrency ?? -1) !== 1) {
    errors.push('max_concurrency_must_be_1');
  }
  if (charter.controlled_lifecycle_required !== true) {
    errors.push('controlled_lifecycle_required');
  }
  if (charter.freshness_recheck_required !== true) {
    errors.push('freshness_recheck_required');
  }
  if (charter.unattended === true) {
    errors.push('unattended_forbidden');
  }
  if (charter.consumed === true) {
    errors.push('charter_already_consumed');
  }

  const charterEvent = String(charter.event_id || '');
  if (!charterEvent || charterEvent !== String(ctx.event_id || '')) {
    return reject(REASON_CODES.RETRY_CHARTER_EVENT_MISMATCH, errors.concat(['event_id_mismatch']));
  }

  const expectedFp = ctx.source_identity_fingerprint;
  if (expectedFp != null) {
    const got = charter.source_identity_fingerprint;
    if (got == null || String(got) !== String(expectedFp)) {
      return reject(REASON_CODES.RETRY_CHARTER_SOURCE_MISMATCH, errors.concat(['source_identity_mismatch']));
    }
  }

  if (ctx.policy_decision && ctx.policy_decision !== 'SAFE_TO_RETRY') {
    errors.push('policy_decision_not_safe');
  }

  const expires = Number(charter.expires_at_ms ?? 0);
  const now = Number(ctx.now_ms ?? 0);
  if (expires > 0 && now > expires) {
    errors.push('charter_expired');
  }

  const budgetRemaining = Number(charter.retry_budget_remaining ?? 0);
  if (budgetRemaining < 1) {
    return reject(REASON_CODES.RETRY_BUDGET_EXHAUSTED, errors.concat(['budget_exhausted']));
  }

  if (errors.length) {
    return reject(REASON_CODES.RETRY_CHARTER_REQUIRED, errors);
  }

  return {
    ok: true,
    reason_code: null,
    errors: [],
    retry_authorized: false, // D6E never auto-authorizes execution
    requires_controlled_lifecycle: true,
    charter_id: charter.charter_id,
    event_id: charterEvent,
    max_retry_attempts: 1,
    automatic_retry: false,
  };
}

function reject(reason_code, errors) {
  return {
    ok: false,
    reason_code,
    errors,
    retry_authorized: false,
    requires_controlled_lifecycle: true,
    charter_id: null,
    event_id: null,
    max_retry_attempts: 0,
    automatic_retry: false,
  };
}

/**
 * Build a sanitized charter template for SAFE_TO_RETRY future manual use.
 */
export function buildRetryCharterTemplate({
  charter_id,
  event_id,
  original_charter_id,
  reconciliation_decision,
  source_identity_fingerprint,
  expires_at_ms,
}) {
  return {
    schema_version: RETRY_CHARTER_SCHEMA_VERSION,
    charter_id,
    event_id,
    original_charter_id: original_charter_id || null,
    reconciliation_decision: reconciliation_decision || null,
    retry_decision: 'SAFE_TO_RETRY',
    source_identity_fingerprint: source_identity_fingerprint || null,
    freshness_recheck_required: true,
    controlled_lifecycle_required: true,
    max_retry_attempts: 1,
    retry_budget_remaining: 1,
    max_concurrency: 1,
    automatic_retry: false,
    unattended: false,
    consumed: false,
    expires_at_ms: expires_at_ms || null,
  };
}
