/**
 * Phase 1B-D6C — deterministic offline control-plane transport.
 * No real network. Injectable clock. Simulates GET/activate/deactivate/dedupe/POST.
 */

import { ALLOWED_WORKFLOW_ID } from './client-ops-n8n-activation-client.mjs';

/**
 * @typedef {object} OfflineWorkflowState
 * @property {string} id
 * @property {boolean} active
 * @property {string} versionId
 * @property {number} nodes
 * @property {number} running
 * @property {number} executions
 * @property {boolean} webhook_path_present
 * @property {boolean} auth_config_structurally_present
 */

/**
 * @param {Partial<OfflineWorkflowState> & { versionId: string }} seed
 */
export function createOfflineLifecycleTransport(seed = {}) {
  /** @type {OfflineWorkflowState} */
  let workflow = {
    id: seed.id ?? ALLOWED_WORKFLOW_ID,
    active: seed.active ?? false,
    versionId: seed.versionId,
    nodes: seed.nodes ?? 20,
    running: seed.running ?? 0,
    executions: seed.executions ?? 34,
    webhook_path_present: seed.webhook_path_present ?? true,
    auth_config_structurally_present: seed.auth_config_structurally_present ?? true,
  };

  /** @type {Map<string, { intake_state?: string, delivery_state?: string }>} */
  const events = new Map();
  if (seed.seenEvents && typeof seed.seenEvents === 'object') {
    for (const [k, v] of Object.entries(seed.seenEvents)) {
      events.set(k, v);
    }
  }

  let activationChanges = 0;
  /** @type {Array<{ op: string, at_ms: number }>} */
  const ops = [];

  /** Behavior hooks for failure injection */
  const behavior = {
    activateResult: /** @type {'success'|'api_failure'|'success_but_inactive'} */ (
      'success'
    ),
    deactivateResult: /** @type {'success'|'api_failure'|'success_but_still_active'} */ (
      'success'
    ),
    emergencyDeactivateResult: /** @type {'success'|'api_failure'|'success_but_still_active'} */ (
      'success'
    ),
    readinessOverride: /** @type {null|Record<string, unknown>} */ (null),
    postResult: /** @type {null|{ http_status?: number, class?: string, timeout?: boolean }} */ (
      null
    ),
    versionDriftAfterActivate: /** @type {string|null} */ (null),
    versionDriftBeforeRequest: /** @type {string|null} */ (null),
    extraActivationChangeOnActivate: false,
  };

  return {
    kind: 'OFFLINE_D6C_TRANSPORT',
    getBehavior() {
      return behavior;
    },
    setBehavior(partial) {
      Object.assign(behavior, partial);
    },
    markEventSeen(eventId, row = { intake_state: 'FIRST_SEEN', delivery_state: 'PENDING' }) {
      events.set(String(eventId), row);
    },
    unmarkEvent(eventId) {
      events.delete(String(eventId));
    },
    getActivationChanges() {
      return activationChanges;
    },
    getOps() {
      return [...ops];
    },
    async getWorkflowState(nowMs) {
      ops.push({ op: 'GET_WORKFLOW', at_ms: nowMs ?? 0 });
      return { ...workflow };
    },
    async activate(nowMs) {
      ops.push({ op: 'ACTIVATE', at_ms: nowMs ?? 0 });
      if (behavior.activateResult === 'api_failure') {
        return {
          attempted: true,
          changed: false,
          active_after: workflow.active,
          version_id: workflow.versionId,
          timestamp_ms: nowMs ?? 0,
          error_class: 'ACTIVATION_API_FAILURE',
        };
      }
      const before = workflow.active;
      if (behavior.activateResult === 'success_but_inactive') {
        // API claims success but GET would still show inactive — simulate by not flipping.
        return {
          attempted: true,
          changed: false,
          active_after: false,
          version_id: workflow.versionId,
          timestamp_ms: nowMs ?? 0,
          error_class: null,
          api_claimed_success: true,
        };
      }
      if (!workflow.active) {
        workflow.active = true;
        activationChanges += 1;
        if (behavior.extraActivationChangeOnActivate) {
          activationChanges += 2;
        }
      }
      if (behavior.versionDriftAfterActivate) {
        workflow.versionId = behavior.versionDriftAfterActivate;
      }
      return {
        attempted: true,
        changed: before !== workflow.active,
        active_after: workflow.active,
        version_id: workflow.versionId,
        timestamp_ms: nowMs ?? 0,
        error_class: null,
      };
    },
    async deactivate(nowMs, { emergency = false } = {}) {
      ops.push({ op: emergency ? 'EMERGENCY_DEACTIVATE' : 'DEACTIVATE', at_ms: nowMs ?? 0 });
      const mode = emergency ? behavior.emergencyDeactivateResult : behavior.deactivateResult;
      if (mode === 'api_failure') {
        return {
          attempted: true,
          changed: false,
          active_after: workflow.active,
          version_id: workflow.versionId,
          timestamp_ms: nowMs ?? 0,
          error_class: emergency
            ? 'EMERGENCY_DEACTIVATION_API_FAILURE'
            : 'DEACTIVATION_API_FAILURE',
          emergency: Boolean(emergency),
        };
      }
      const before = workflow.active;
      if (mode === 'success_but_still_active') {
        return {
          attempted: true,
          changed: false,
          active_after: true,
          version_id: workflow.versionId,
          timestamp_ms: nowMs ?? 0,
          error_class: null,
          api_claimed_success: true,
          emergency: Boolean(emergency),
        };
      }
      if (workflow.active) {
        workflow.active = false;
        activationChanges += 1;
      }
      return {
        attempted: true,
        changed: before !== workflow.active,
        active_after: workflow.active,
        version_id: workflow.versionId,
        timestamp_ms: nowMs ?? 0,
        error_class: null,
        emergency: Boolean(emergency),
      };
    },
    async checkDedupe(eventId, nowMs) {
      ops.push({ op: 'DEDUPE_CHECK', at_ms: nowMs ?? 0 });
      const row = events.get(String(eventId));
      return {
        event_id: String(eventId),
        seen: Boolean(row),
        row: row
          ? {
              intake_state: row.intake_state ?? null,
              delivery_state: row.delivery_state ?? null,
            }
          : null,
      };
    },
    async postWebhook(_payloadRef, nowMs) {
      ops.push({ op: 'WEBHOOK_POST', at_ms: nowMs ?? 0 });
      if (behavior.versionDriftBeforeRequest) {
        workflow.versionId = behavior.versionDriftBeforeRequest;
      }
      const pr = behavior.postResult || { http_status: 202, class: 'HTTP_202_INTAKE_ACCEPTED' };
      if (pr.timeout) {
        return {
          attempted: true,
          http_status: null,
          result_class: 'READ_TIMEOUT_AMBIGUOUS',
          ambiguous: true,
          timestamp_ms: nowMs ?? 0,
        };
      }
      return {
        attempted: true,
        http_status: pr.http_status ?? null,
        result_class: pr.class ?? `HTTP_${pr.http_status}`,
        ambiguous: false,
        timestamp_ms: nowMs ?? 0,
      };
    },
    /** Test helper: mutate live state */
    _mutate(partial) {
      Object.assign(workflow, partial);
    },
  };
}

/**
 * Deterministic injectable clock (no sleep).
 * @param {number} [startMs]
 */
export function createDeterministicClock(startMs = 1_700_000_000_000) {
  let now = startMs;
  return {
    nowMs() {
      return now;
    },
    nowIso() {
      return new Date(now).toISOString().replace(/\.\d{3}Z$/, 'Z');
    },
    advance(ms) {
      now += Number(ms);
      return now;
    },
    set(ms) {
      now = Number(ms);
      return now;
    },
  };
}
