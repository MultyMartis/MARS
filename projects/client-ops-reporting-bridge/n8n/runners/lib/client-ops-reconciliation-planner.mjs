/**
 * Phase 1B-D6E — offline reconciliation planner (GET-only next steps).
 * Does NOT execute production reconciliation.
 */

export const RECONCILE_ACTIONS = Object.freeze({
  READ_DATA_TABLE_EVENT: 'READ_DATA_TABLE_EVENT',
  READ_N8N_EXECUTIONS: 'READ_N8N_EXECUTIONS',
  VERIFY_TELEGRAM_EVIDENCE: 'VERIFY_TELEGRAM_EVIDENCE',
  VERIFY_WORKFLOW_CONTAINMENT: 'VERIFY_WORKFLOW_CONTAINMENT',
  RECOMPUTE_FRESHNESS: 'RECOMPUTE_FRESHNESS',
  VERIFY_LIFECYCLE_LOCK: 'VERIFY_LIFECYCLE_LOCK',
  NO_MORE_ACTION_REQUIRED: 'NO_MORE_ACTION_REQUIRED',
  OPERATOR_CONTAINMENT_REQUIRED: 'OPERATOR_CONTAINMENT_REQUIRED',
  OPERATOR_REVIEW_REQUIRED: 'OPERATOR_REVIEW_REQUIRED',
});

/**
 * @param {{
 *   decision: string,
 *   reason_code: string,
 *   delivery_state?: string|null,
 *   row_found?: boolean|null,
 *   telegram_outcome?: string|null,
 *   containment_state?: string|null,
 *   delivery_eligibility?: string|null,
 * }} input
 */
export function planReconciliation(input) {
  const actions = [];
  const decision = String(input.decision || '');
  const reason = String(input.reason_code || '');
  const delivery = input.delivery_state || null;
  const containment = input.containment_state || null;
  const eligibility = input.delivery_eligibility || null;

  if (containment === 'CONTAINMENT_FAILED') {
    actions.push(RECONCILE_ACTIONS.OPERATOR_CONTAINMENT_REQUIRED);
    actions.push(RECONCILE_ACTIONS.VERIFY_WORKFLOW_CONTAINMENT);
    return sanitizePlan({ decision, reason_code: reason, actions, executable: false });
  }

  if (decision === 'SAFE_TO_RETRY') {
    actions.push(RECONCILE_ACTIONS.RECOMPUTE_FRESHNESS);
    actions.push(RECONCILE_ACTIONS.READ_DATA_TABLE_EVENT);
    actions.push(RECONCILE_ACTIONS.VERIFY_WORKFLOW_CONTAINMENT);
    return sanitizePlan({ decision, reason_code: reason, actions, executable: false });
  }

  if (decision === 'FINAL_FAILURE' || decision === 'UNSAFE_TO_RETRY') {
    if (delivery === 'SENT' || delivery === 'FAILED') {
      actions.push(RECONCILE_ACTIONS.NO_MORE_ACTION_REQUIRED);
    } else if (reason.includes('TELEGRAM_SUCCESS') || reason.includes('PENDING')) {
      actions.push(RECONCILE_ACTIONS.READ_DATA_TABLE_EVENT);
      actions.push(RECONCILE_ACTIONS.VERIFY_TELEGRAM_EVIDENCE);
      actions.push(RECONCILE_ACTIONS.READ_N8N_EXECUTIONS);
      actions.push(RECONCILE_ACTIONS.OPERATOR_REVIEW_REQUIRED);
    } else if (containment === 'RECONTAINED_WITH_ANOMALY') {
      actions.push(RECONCILE_ACTIONS.VERIFY_WORKFLOW_CONTAINMENT);
      if (delivery === 'PENDING' || delivery == null) {
        actions.push(RECONCILE_ACTIONS.READ_DATA_TABLE_EVENT);
      } else {
        actions.push(RECONCILE_ACTIONS.NO_MORE_ACTION_REQUIRED);
      }
    } else {
      actions.push(RECONCILE_ACTIONS.NO_MORE_ACTION_REQUIRED);
    }
    return sanitizePlan({ decision, reason_code: reason, actions, executable: false });
  }

  // RECONCILE_BEFORE_RETRY and defaults
  if (input.row_found !== true) {
    actions.push(RECONCILE_ACTIONS.READ_DATA_TABLE_EVENT);
    actions.push(RECONCILE_ACTIONS.READ_N8N_EXECUTIONS);
  } else {
    actions.push(RECONCILE_ACTIONS.READ_DATA_TABLE_EVENT);
  }
  if (delivery === 'PENDING' || input.telegram_outcome === 'UNKNOWN' || input.telegram_outcome === 'SUCCESS') {
    actions.push(RECONCILE_ACTIONS.VERIFY_TELEGRAM_EVIDENCE);
    actions.push(RECONCILE_ACTIONS.READ_N8N_EXECUTIONS);
  }
  actions.push(RECONCILE_ACTIONS.VERIFY_WORKFLOW_CONTAINMENT);
  if (
    eligibility === 'STALE_REVIEW_REQUIRED' ||
    eligibility === 'NOT_SAFE_TO_SEND' ||
    eligibility == null
  ) {
    actions.push(RECONCILE_ACTIONS.RECOMPUTE_FRESHNESS);
  }
  actions.push(RECONCILE_ACTIONS.OPERATOR_REVIEW_REQUIRED);

  return sanitizePlan({ decision, reason_code: reason, actions, executable: false });
}

function sanitizePlan(plan) {
  return {
    ...plan,
    production_mutation_authorized: false,
    live_reconciliation_executed: false,
    actions: [...new Set(plan.actions)],
  };
}
