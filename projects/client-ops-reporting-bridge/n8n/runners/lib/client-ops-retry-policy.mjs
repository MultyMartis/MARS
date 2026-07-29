/**
 * Phase 1B-D6E — Retry and Concurrency Policy Binding (offline evaluator).
 *
 * Canonical principle:
 *   NO PROOF OF NON-DELIVERY != SAFE TO RETRY
 * Ambiguity defaults to RECONCILE_BEFORE_RETRY.
 *
 * Does NOT execute retries, webhooks, activation, Telegram, or Data Table mutations.
 * Preserves Workstream A/B/C semantics. Does NOT implement Workstream D.
 */

import { DELIVERY_STATE, MAX_RETRIES, MAX_SAFE_CONCURRENCY } from './client-ops-delivery-ledger.mjs';
import { DELIVERY_ELIGIBILITY, STALE_AFTER_SECONDS } from './client-ops-activation-lifecycle.mjs';
import { REASON_CODES } from './client-ops-retry-reason-codes.mjs';
import { planReconciliation } from './client-ops-reconciliation-planner.mjs';
import { validateRetryCharter, D6E_RETRY_DEFAULTS } from './client-ops-retry-charter.mjs';
import { evaluateConcurrencyPolicy, D6E_MAX_SAFE_CONCURRENCY } from './client-ops-concurrency-policy.mjs';

export const RETRY_DECISIONS = Object.freeze({
  SAFE_TO_RETRY: 'SAFE_TO_RETRY',
  UNSAFE_TO_RETRY: 'UNSAFE_TO_RETRY',
  RECONCILE_BEFORE_RETRY: 'RECONCILE_BEFORE_RETRY',
  FINAL_FAILURE: 'FINAL_FAILURE',
});

/** Failure certainty boundaries B0–B7. */
export const FAILURE_BOUNDARIES = Object.freeze({
  B0_BEFORE_REQUEST_CONSTRUCTION: 'B0',
  B1_CONSTRUCTED_NOT_TRANSMITTED: 'B1',
  B2_TRANSMISSION_ATTEMPTED_ACCEPTANCE_UNKNOWN: 'B2',
  B3_SERVER_INTAKE_RESPONSE_KNOWN: 'B3',
  B4_DURABLE_CLAIM_ROW_KNOWN: 'B4',
  B5_TELEGRAM_OUTCOME_KNOWN_OR_UNKNOWN: 'B5',
  B6_FINAL_LEDGER_STATE_KNOWN_OR_UNKNOWN: 'B6',
  B7_LIFECYCLE_CONTAINMENT_KNOWN_OR_UNKNOWN: 'B7',
});

export const REQUEST_STAGES = Object.freeze({
  BEFORE_CONSTRUCTION: 'BEFORE_CONSTRUCTION',
  CONSTRUCTED_NOT_TRANSMITTED: 'CONSTRUCTED_NOT_TRANSMITTED',
  TRANSMISSION_AMBIGUOUS: 'TRANSMISSION_AMBIGUOUS',
  RESPONSE_KNOWN: 'RESPONSE_KNOWN',
  RESPONSE_LOST: 'RESPONSE_LOST',
});

export const TRANSPORT_OUTCOMES = Object.freeze({
  NOT_ATTEMPTED: 'NOT_ATTEMPTED',
  PRE_TRANSMISSION_FAILURE: 'PRE_TRANSMISSION_FAILURE',
  AMBIGUOUS_TRANSPORT: 'AMBIGUOUS_TRANSPORT',
  RESPONSE_KNOWN: 'RESPONSE_KNOWN',
  RESPONSE_LOST: 'RESPONSE_LOST',
});

export const TELEGRAM_OUTCOMES = Object.freeze({
  NONE: 'NONE',
  SUCCESS: 'SUCCESS',
  DEFINITE_FAILURE: 'DEFINITE_FAILURE',
  UNKNOWN: 'UNKNOWN',
});

export const EXECUTION_OUTCOMES = Object.freeze({
  UNKNOWN: 'UNKNOWN',
  NOT_FOUND: 'NOT_FOUND',
  EXISTS: 'EXISTS',
  AUTHORITATIVE_NO_INTAKE: 'AUTHORITATIVE_NO_INTAKE',
});

export const PRE_TX_CLASSES = Object.freeze({
  SEMANTIC: 'SEMANTIC',
  TRANSIENT: 'TRANSIENT',
  CHARTER_OR_READINESS: 'CHARTER_OR_READINESS',
  FRESHNESS: 'FRESHNESS',
});

export {
  REASON_CODES,
  DELIVERY_STATE,
  DELIVERY_ELIGIBILITY,
  STALE_AFTER_SECONDS,
  MAX_RETRIES,
  MAX_SAFE_CONCURRENCY,
  D6E_MAX_SAFE_CONCURRENCY,
  D6E_RETRY_DEFAULTS,
};

const SECRET_KEY_RE =
  /(api[_-]?key|authorization|token|secret|password|webhook_url|telegram|chat_id|n8n[_-]?key|raw_payload|customer_payload)/i;

/**
 * @typedef {object} RetryObservation
 * @property {string} [event_id]
 * @property {string} [source_status]
 * @property {string} [delivery_eligibility]
 * @property {string} [request_stage]
 * @property {string} [transport_outcome]
 * @property {number|null} [http_status]
 * @property {string|null} [intake_state]
 * @property {string|null} [delivery_state]
 * @property {string} [telegram_outcome]
 * @property {string} [execution_outcome]
 * @property {string} [containment_state]
 * @property {boolean|null} [row_found]
 * @property {string} [evidence_quality]
 * @property {string} [pre_transmission_class]
 * @property {boolean} [same_event_parallel]
 * @property {boolean} [different_event_parallel]
 * @property {boolean} [lifecycle_lock_held_by_other]
 * @property {boolean} [unresolved_active_session]
 * @property {boolean} [request_budget_exhausted]
 * @property {boolean} [retry_charter_present]
 * @property {object|null} [retry_charter]
 * @property {string|null} [source_identity_fingerprint]
 * @property {number|null} [retry_budget_remaining]
 * @property {boolean} [is_new_source_run]
 * @property {boolean} [historical_telegram_success_evidence]
 * @property {boolean} [security_scan_requested]
 * @property {Record<string, unknown>} [evidence]
 * @property {number} [now_ms]
 */

/**
 * Evaluate retry / reconciliation policy for a sanitized observation.
 * Always returns retry_authorized=false unless SAFE_TO_RETRY AND explicit charter
 * validation passes — and even then D6E keeps automatic execution disabled.
 *
 * @param {RetryObservation} obs
 */
export function evaluateRetryPolicy(obs = {}) {
  const eventId = obs.event_id != null ? String(obs.event_id) : null;
  const delivery = normalizeDelivery(obs.delivery_state);
  const telegram = String(obs.telegram_outcome || TELEGRAM_OUTCOMES.NONE).toUpperCase();
  const transport = String(obs.transport_outcome || TRANSPORT_OUTCOMES.NOT_ATTEMPTED).toUpperCase();
  const eligibility = String(obs.delivery_eligibility || '').toUpperCase() || null;
  const containment = String(obs.containment_state || 'UNKNOWN').toUpperCase();
  const http = obs.http_status == null ? null : Number(obs.http_status);
  const rowFound = obs.row_found;
  const exec = String(obs.execution_outcome || EXECUTION_OUTCOMES.UNKNOWN).toUpperCase();
  const preClass = String(obs.pre_transmission_class || '').toUpperCase();

  /** @type {ReturnType<typeof decision>} */
  let result;

  // --- New source run is not a retry ---
  if (obs.is_new_source_run === true) {
    result = decision(RETRY_DECISIONS.FINAL_FAILURE, REASON_CODES.NEW_SOURCE_RUN_NOT_RETRY, {
      note: 'New monitor run creates a new event_id; ordinary A/B/C pipeline applies',
      operator_action_required: false,
      requires_reconciliation: false,
    });
    return finalize(result, obs, eventId);
  }

  // --- Concurrency gates (same/different event) ---
  const conc = evaluateConcurrencyPolicy({
    event_id: eventId || '',
    same_event_parallel: obs.same_event_parallel === true,
    different_event_parallel: obs.different_event_parallel === true,
    lifecycle_lock_held_by_other: obs.lifecycle_lock_held_by_other === true,
    unresolved_active_session: obs.unresolved_active_session === true,
    request_budget_exhausted: obs.request_budget_exhausted === true,
    delivery_state: null, // delivery handled below with richer semantics
    delivery_eligibility: null,
    now_ms: obs.now_ms,
  });
  if (conc.rejected && conc.reason_code) {
    result = decision(RETRY_DECISIONS.UNSAFE_TO_RETRY, conc.reason_code, {
      operator_action_required: true,
      requires_reconciliation: false,
    });
    return finalize(result, obs, eventId);
  }

  // --- Containment failure blocks retry ---
  if (containment === 'CONTAINMENT_FAILED') {
    result = decision(RETRY_DECISIONS.FINAL_FAILURE, REASON_CODES.CONTAINMENT_FAILED, {
      operator_action_required: true,
      requires_reconciliation: true,
    });
    return finalize(result, obs, eventId);
  }

  // --- Historical D5R2A-like fixture: PENDING + Telegram success ---
  if (
    obs.historical_telegram_success_evidence === true &&
    (delivery === DELIVERY_STATE.PENDING || delivery == null)
  ) {
    result = decision(
      RETRY_DECISIONS.UNSAFE_TO_RETRY,
      REASON_CODES.HISTORICAL_PENDING_BLIND_RETRY_PROHIBITED,
      {
        operator_action_required: true,
        requires_reconciliation: true,
        no_send_guard: true,
        note: 'Blind retry prohibited; historical Telegram success evidence implies duplicate risk',
      },
    );
    return finalize(result, obs, eventId);
  }

  // --- Telegram success + PENDING fails closed (precedence over generic PENDING) ---
  if (telegram === TELEGRAM_OUTCOMES.SUCCESS && delivery === DELIVERY_STATE.PENDING) {
    result = decision(
      RETRY_DECISIONS.UNSAFE_TO_RETRY,
      REASON_CODES.TELEGRAM_SUCCESS_LEDGER_PENDING,
      {
        operator_action_required: true,
        requires_reconciliation: true,
        no_send_guard: true,
      },
    );
    return finalize(result, obs, eventId);
  }

  // --- Containment anomaly separated from delivery ---
  if (containment === 'RECONTAINED_WITH_ANOMALY') {
    if (delivery === DELIVERY_STATE.SENT) {
      result = decision(
        RETRY_DECISIONS.UNSAFE_TO_RETRY,
        REASON_CODES.CONTAINMENT_ANOMALY_SENT_TERMINAL,
        {
          operator_action_required: true,
          requires_reconciliation: false,
          anomaly_recorded: true,
        },
      );
      return finalize(result, obs, eventId);
    }
    if (delivery === DELIVERY_STATE.PENDING || delivery == null) {
      result = decision(
        RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
        REASON_CODES.CONTAINMENT_ANOMALY_PENDING_RECONCILE,
        {
          operator_action_required: true,
          requires_reconciliation: true,
          anomaly_recorded: true,
        },
      );
      return finalize(result, obs, eventId);
    }
  }

  // --- Durable ledger authority ---
  if (delivery === DELIVERY_STATE.SENT || (rowFound === true && delivery === DELIVERY_STATE.SENT)) {
    const reason =
      transport === TRANSPORT_OUTCOMES.RESPONSE_LOST
        ? REASON_CODES.RESPONSE_LOST_SENT_TERMINAL
        : http === 202
          ? REASON_CODES.HTTP_202_SENT_TERMINAL
          : http === 200
            ? REASON_CODES.HTTP_200_DUPLICATE_SENT
            : REASON_CODES.ALREADY_SENT;
    result = decision(RETRY_DECISIONS.UNSAFE_TO_RETRY, reason, {
      operator_action_required: false,
      requires_reconciliation: false,
      terminal_success: true,
    });
    return finalize(result, obs, eventId);
  }

  if (delivery === DELIVERY_STATE.FAILED) {
    const reason =
      transport === TRANSPORT_OUTCOMES.RESPONSE_LOST
        ? REASON_CODES.RESPONSE_LOST_FAILED_TERMINAL
        : telegram === TELEGRAM_OUTCOMES.DEFINITE_FAILURE
          ? REASON_CODES.TELEGRAM_FAILED_TERMINAL
          : http === 202
            ? REASON_CODES.HTTP_202_FAILED_TERMINAL
            : http === 200
              ? REASON_CODES.HTTP_200_DUPLICATE_FAILED
              : REASON_CODES.DELIVERY_FAILED_TERMINAL;
    result = decision(RETRY_DECISIONS.FINAL_FAILURE, reason, {
      operator_action_required: true,
      requires_reconciliation: false,
      recovery_charter_required: true,
    });
    return finalize(result, obs, eventId);
  }

  if (delivery === DELIVERY_STATE.PENDING) {
    if (telegram === TELEGRAM_OUTCOMES.UNKNOWN) {
      result = decision(
        RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
        REASON_CODES.TELEGRAM_UNKNOWN_PENDING,
        { operator_action_required: true, requires_reconciliation: true },
      );
      return finalize(result, obs, eventId);
    }
    if (http === 202) {
      result = decision(
        RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
        REASON_CODES.HTTP_202_PENDING_RECONCILE,
        { operator_action_required: true, requires_reconciliation: true },
      );
      return finalize(result, obs, eventId);
    }
    if (http === 200) {
      result = decision(
        RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
        REASON_CODES.HTTP_200_DUPLICATE_PENDING,
        { operator_action_required: true, requires_reconciliation: true },
      );
      return finalize(result, obs, eventId);
    }
    if (transport === TRANSPORT_OUTCOMES.RESPONSE_LOST) {
      result = decision(
        RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
        REASON_CODES.RESPONSE_LOST_PENDING_RECONCILE,
        { operator_action_required: true, requires_reconciliation: true },
      );
      return finalize(result, obs, eventId);
    }
    result = decision(
      RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
      REASON_CODES.PENDING_NEVER_AUTO_RETRY,
      { operator_action_required: true, requires_reconciliation: true },
    );
    return finalize(result, obs, eventId);
  }

  // --- Ambiguous transport (no durable terminal row) ---
  if (
    transport === TRANSPORT_OUTCOMES.AMBIGUOUS_TRANSPORT ||
    obs.request_stage === REQUEST_STAGES.TRANSMISSION_AMBIGUOUS
  ) {
    if (rowFound === false && exec === EXECUTION_OUTCOMES.AUTHORITATIVE_NO_INTAKE) {
      result = decision(
        RETRY_DECISIONS.SAFE_TO_RETRY,
        REASON_CODES.NO_ROW_AUTHORITATIVE_NO_INTAKE,
        {
          operator_action_required: true,
          requires_reconciliation: false,
          note: 'Only when authoritative control-plane evidence proves no intake',
        },
      );
      return finalize(result, obs, eventId);
    }
    if (rowFound === false) {
      result = decision(
        RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
        REASON_CODES.NO_ROW_AMBIGUOUS,
        { operator_action_required: true, requires_reconciliation: true },
      );
      return finalize(result, obs, eventId);
    }
    result = decision(
      RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
      REASON_CODES.AMBIGUOUS_TRANSPORT,
      { operator_action_required: true, requires_reconciliation: true },
    );
    return finalize(result, obs, eventId);
  }

  if (transport === TRANSPORT_OUTCOMES.RESPONSE_LOST) {
    result = decision(
      RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
      REASON_CODES.AMBIGUOUS_TRANSPORT,
      { operator_action_required: true, requires_reconciliation: true },
    );
    return finalize(result, obs, eventId);
  }

  // --- Known HTTP outcomes without durable row yet ---
  if (transport === TRANSPORT_OUTCOMES.RESPONSE_KNOWN || http != null) {
    if (http === 409) {
      result = decision(RETRY_DECISIONS.FINAL_FAILURE, REASON_CODES.EVENT_CONFLICT, {
        operator_action_required: true,
        requires_reconciliation: false,
      });
      return finalize(result, obs, eventId);
    }
    if (http === 401 || http === 403) {
      result = decision(RETRY_DECISIONS.FINAL_FAILURE, REASON_CODES.HTTP_AUTH_REJECTED, {
        operator_action_required: true,
        requires_reconciliation: false,
      });
      return finalize(result, obs, eventId);
    }
    if (http === 404) {
      result = decision(
        RETRY_DECISIONS.FINAL_FAILURE,
        REASON_CODES.WORKFLOW_INACTIVE_BEFORE_POST,
        {
          operator_action_required: true,
          requires_reconciliation: false,
          note: 'Lifecycle/preflight failure; not a delivery retry',
        },
      );
      return finalize(result, obs, eventId);
    }
    if (http === 400 || http === 422 || (http != null && http >= 400 && http < 500)) {
      result = decision(
        RETRY_DECISIONS.FINAL_FAILURE,
        REASON_CODES.HTTP_VALIDATION_REJECTED,
        { operator_action_required: true, requires_reconciliation: false },
      );
      return finalize(result, obs, eventId);
    }
    if (http != null && http >= 500 && http < 600) {
      result = decision(
        RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
        REASON_CODES.HTTP_5XX_CLAIM_UNKNOWN,
        { operator_action_required: true, requires_reconciliation: true },
      );
      return finalize(result, obs, eventId);
    }
    if (http === 202 && delivery == null && rowFound !== true) {
      result = decision(
        RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
        REASON_CODES.HTTP_202_PENDING_RECONCILE,
        { operator_action_required: true, requires_reconciliation: true },
      );
      return finalize(result, obs, eventId);
    }
    if (http === 200 && delivery == null) {
      result = decision(
        RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
        REASON_CODES.HTTP_200_DUPLICATE_PENDING,
        { operator_action_required: true, requires_reconciliation: true },
      );
      return finalize(result, obs, eventId);
    }
  }

  // --- Pre-transmission ---
  if (
    transport === TRANSPORT_OUTCOMES.PRE_TRANSMISSION_FAILURE ||
    transport === TRANSPORT_OUTCOMES.NOT_ATTEMPTED ||
    obs.request_stage === REQUEST_STAGES.BEFORE_CONSTRUCTION ||
    obs.request_stage === REQUEST_STAGES.CONSTRUCTED_NOT_TRANSMITTED
  ) {
    if (preClass === PRE_TX_CLASSES.SEMANTIC) {
      result = decision(
        RETRY_DECISIONS.FINAL_FAILURE,
        REASON_CODES.PRE_TRANSMISSION_SEMANTIC_FAILURE,
        { operator_action_required: true, requires_reconciliation: false },
      );
      return finalize(result, obs, eventId);
    }
    if (preClass === PRE_TX_CLASSES.CHARTER_OR_READINESS) {
      result = decision(
        RETRY_DECISIONS.FINAL_FAILURE,
        REASON_CODES.PRE_TRANSMISSION_CHARTER_OR_READINESS,
        { operator_action_required: true, requires_reconciliation: false },
      );
      return finalize(result, obs, eventId);
    }
    if (preClass === PRE_TX_CLASSES.FRESHNESS) {
      result = decision(RETRY_DECISIONS.FINAL_FAILURE, REASON_CODES.SOURCE_NOT_ELIGIBLE, {
        operator_action_required: true,
        requires_reconciliation: false,
      });
      return finalize(result, obs, eventId);
    }
    if (preClass === PRE_TX_CLASSES.TRANSIENT) {
      result = decision(
        RETRY_DECISIONS.SAFE_TO_RETRY,
        REASON_CODES.PRE_TRANSMISSION_TRANSIENT_NO_SIDE_EFFECT,
        {
          operator_action_required: true,
          requires_reconciliation: false,
          note: 'Requires new explicit charter; automatic retry remains false',
        },
      );
      return finalize(result, obs, eventId);
    }
  }

  // Default: ambiguity → reconcile
  result = decision(
    RETRY_DECISIONS.RECONCILE_BEFORE_RETRY,
    REASON_CODES.AMBIGUOUS_TRANSPORT,
    { operator_action_required: true, requires_reconciliation: true },
  );
  return finalize(result, obs, eventId);
}

/**
 * @param {string} decisionValue
 * @param {string} reason_code
 * @param {Record<string, unknown>} [extra]
 */
function decision(decisionValue, reason_code, extra = {}) {
  return {
    decision: decisionValue,
    reason_code,
    retry_authorized: false,
    automatic_retry: false,
    requires_reconciliation: Boolean(extra.requires_reconciliation),
    requires_new_charter: decisionValue === RETRY_DECISIONS.SAFE_TO_RETRY,
    freshness_recheck_required: true,
    controlled_lifecycle_required: true,
    operator_action_required: Boolean(extra.operator_action_required),
    no_send_guard: Boolean(extra.no_send_guard),
    max_automatic_retries: 0,
    max_safe_concurrency: D6E_MAX_SAFE_CONCURRENCY,
    ...extra,
  };
}

/**
 * @param {ReturnType<typeof decision>} result
 * @param {RetryObservation} obs
 * @param {string|null} eventId
 */
function finalize(result, obs, eventId) {
  const eligibility = String(obs.delivery_eligibility || '').toUpperCase() || null;

  // Freshness recheck gate — never authorize retry if not eligible
  if (
    eligibility === DELIVERY_ELIGIBILITY.STALE_REVIEW_REQUIRED ||
    eligibility === DELIVERY_ELIGIBILITY.NOT_SAFE_TO_SEND
  ) {
    result = {
      ...result,
      retry_authorized: false,
      freshness_blocks_retry: true,
      freshness_recheck_required: true,
      reason_code:
        result.decision === RETRY_DECISIONS.SAFE_TO_RETRY
          ? eligibility === DELIVERY_ELIGIBILITY.STALE_REVIEW_REQUIRED
            ? REASON_CODES.SOURCE_STALE_REVIEW_REQUIRED
            : REASON_CODES.SOURCE_NOT_ELIGIBLE
          : result.reason_code,
      decision:
        result.decision === RETRY_DECISIONS.SAFE_TO_RETRY
          ? RETRY_DECISIONS.FINAL_FAILURE
          : result.decision,
      operator_action_required: true,
    };
  }

  // Explicit charter required for SAFE_TO_RETRY — still never auto-execute
  if (result.decision === RETRY_DECISIONS.SAFE_TO_RETRY) {
    if (!obs.retry_charter_present && !obs.retry_charter) {
      result = {
        ...result,
        retry_authorized: false,
        charter_rejected: true,
        charter_reject_reason: REASON_CODES.RETRY_CHARTER_REQUIRED,
        requires_new_charter: true,
        note: 'Decision class is SAFE_TO_RETRY but execution rejected without new charter',
      };
    } else {
      const charterResult = validateRetryCharter(obs.retry_charter || {}, {
        event_id: eventId || '',
        source_identity_fingerprint: obs.source_identity_fingerprint,
        policy_decision: RETRY_DECISIONS.SAFE_TO_RETRY,
        now_ms: obs.now_ms,
      });
      if (!charterResult.ok) {
        result = {
          ...result,
          retry_authorized: false,
          charter_rejected: true,
          charter_reject_reason: charterResult.reason_code || REASON_CODES.RETRY_CHARTER_REQUIRED,
          charter_errors: charterResult.errors,
        };
      } else if (
        obs.retry_budget_remaining != null &&
        Number(obs.retry_budget_remaining) < 1
      ) {
        result = {
          ...result,
          retry_authorized: false,
          charter_rejected: true,
          charter_reject_reason: REASON_CODES.RETRY_BUDGET_EXHAUSTED,
        };
      } else {
        // Policy class allows manual bounded retry design — D6E still does not execute
        result = {
          ...result,
          retry_authorized: false,
          manual_safe_retry_prerequisites_met: true,
          note: 'SAFE_TO_RETRY class with valid charter; D6E does not execute retry',
        };
      }
    }
  }

  if (obs.security_scan_requested === true) {
    const evidence = sanitizeEvidence(obs.evidence || { sample: 'ok' });
    result = {
      ...result,
      evidence_sanitized: evidence.ok,
      reason_code: evidence.ok ? REASON_CODES.EVIDENCE_SANITIZED_OK : result.reason_code,
      evidence_issues: evidence.issues,
    };
  }

  const plan = planReconciliation({
    decision: result.decision,
    reason_code: result.reason_code,
    delivery_state: obs.delivery_state,
    row_found: obs.row_found,
    telegram_outcome: obs.telegram_outcome,
    containment_state: obs.containment_state,
    delivery_eligibility: obs.delivery_eligibility,
  });

  return {
    ...result,
    event_id: eventId,
    event_identity_preserved: true,
    automatic_retries_enabled: false,
    reconciliation_plan: plan,
    workstream_a_unchanged: true,
    workstream_b_unchanged: true,
    workstream_c_unchanged: true,
    unattended_mode_enabled: false,
  };
}

function normalizeDelivery(value) {
  if (value == null || value === '') return null;
  const v = String(value).toUpperCase();
  if (v === 'PENDING' || v === 'SENT' || v === 'FAILED') return v;
  return null;
}

/**
 * Ensure evidence objects do not carry secrets.
 * @param {Record<string, unknown>} evidence
 */
export function sanitizeEvidence(evidence) {
  const issues = [];
  const out = {};
  for (const [k, v] of Object.entries(evidence || {})) {
    if (SECRET_KEY_RE.test(k)) {
      issues.push(`forbidden_key:${k}`);
      continue;
    }
    if (typeof v === 'string' && SECRET_KEY_RE.test(v) && v.length > 20) {
      issues.push(`forbidden_value_pattern:${k}`);
      continue;
    }
    if (v && typeof v === 'object' && !Array.isArray(v)) {
      const nested = sanitizeEvidence(/** @type {Record<string, unknown>} */ (v));
      issues.push(...nested.issues);
      out[k] = nested.value;
    } else {
      out[k] = v;
    }
  }
  return { ok: issues.length === 0, issues, value: out };
}

/**
 * Authority order for reconciliation (documentation + machine-readable).
 */
export function describeReconciliationAuthority() {
  return {
    order: [
      'deterministic_event_identity',
      'durable_data_table_row',
      'durable_delivery_state',
      'known_telegram_delivery_evidence',
      'n8n_execution_evidence',
      'observed_http_result',
      'local_client_transport_result',
    ],
    rules: [
      'Durable SENT proof is never overridden by weaker HTTP/client evidence',
      'Telegram SUCCESS with PENDING fails closed (no resend)',
      'Ambiguous transport never implies SAFE_TO_RETRY without authoritative no-intake proof',
      'Execution evidence strengthens reconciliation but cannot authorize blind POST',
    ],
  };
}

export function describeFailureBoundaries() {
  return { ...FAILURE_BOUNDARIES };
}

export function describeRetryDecisionModel() {
  return {
    SAFE_TO_RETRY:
      'Positive evidence that no server-side intake/claim/customer-delivery side effect occurred; same event_id replay may be safe only under new explicit charter',
    UNSAFE_TO_RETRY:
      'Positive evidence that replay could cause unsafe/duplicate/contradictory side effect or violates an invariant',
    RECONCILE_BEFORE_RETRY:
      'Outcome ambiguous; durable state must be queried before any replay decision',
    FINAL_FAILURE:
      'Terminal for current charter/event unless a separate recovery/reconciliation charter is created',
  };
}
