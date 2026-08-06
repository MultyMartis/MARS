/**
 * Phase 1B-D6C2 — production control-plane transport for bounded activation lifecycle.
 *
 * Activate/deactivate + GET only. Never POSTs webhooks. Never mutates Data Table rows.
 * No secrets persisted in returned state.
 */

import {
  getWorkflow,
  loadCredentials,
  normalizeBaseUrl,
} from '../../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';
import {
  activateAllowlistedWorkflow,
  deactivateAllowlistedWorkflow,
  ALLOWED_WORKFLOW_ID,
  D6C_ACTIVATION_CONFIRM_PHRASE,
  D6C_DEACTIVATION_CONFIRM_PHRASE,
  D6C_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE,
} from './client-ops-n8n-activation-client.mjs';
import {
  getDataTableRows,
  loadDataTableCredentials,
} from './client-ops-n8n-datatable-client.mjs';
import { AUTH_CRED_ID } from './client-ops-dedupe-compose.mjs';

export const D6C2_TABLE_ID = 'H6VYhwz7RXZCBMmu';

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} workflowId
 */
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

/**
 * Structural webhook/auth presence only — never returns path or secret values.
 * @param {Array<Record<string, unknown>>} nodes
 */
export function inspectWebhookAuthStructural(nodes) {
  const webhook = (nodes || []).find((n) => n.name === 'Webhook Intake');
  const pathPresent =
    typeof webhook?.parameters?.path === 'string' &&
    String(webhook.parameters.path).length > 0;
  const authMode = webhook?.parameters?.authentication === 'headerAuth';
  const authCredId = webhook?.credentials?.httpHeaderAuth?.id;
  const authPresent = authMode && authCredId === AUTH_CRED_ID;
  return {
    webhook_path_present: Boolean(pathPresent),
    auth_config_structurally_present: Boolean(authPresent),
    webhook_node_present: Boolean(webhook),
  };
}

/**
 * @param {{
 *   creds?: { apiUrl: string, apiKey: string },
 *   dtCreds?: { apiUrl: string, apiKey: string },
 *   activateConfirm?: string,
 *   deactivateConfirm?: string,
 *   emergencyDeactivateConfirm?: string,
 *   allowWebhookPost?: boolean,
 * }} [opts]
 */
export function createProductionLifecycleTransport(opts = {}) {
  const creds = opts.creds || loadCredentials();
  const dtCreds = opts.dtCreds || loadDataTableCredentials();
  const activateConfirm = opts.activateConfirm || D6C_ACTIVATION_CONFIRM_PHRASE;
  const deactivateConfirm = opts.deactivateConfirm || D6C_DEACTIVATION_CONFIRM_PHRASE;
  const emergencyConfirm =
    opts.emergencyDeactivateConfirm || D6C_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE;
  const allowWebhookPost = opts.allowWebhookPost === true;

  let activationChanges = 0;
  /** @type {Array<{ op: string, at_ms: number }>} */
  const ops = [];
  let lastActive = null;

  return {
    kind: 'PRODUCTION_D6C_TRANSPORT',
    getActivationChanges() {
      return activationChanges;
    },
    getOps() {
      return [...ops];
    },
    async getWorkflowState(nowMs) {
      ops.push({ op: 'GET_WORKFLOW', at_ms: nowMs ?? Date.now() });
      const wf = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
      const nodes = Array.isArray(wf.nodes) ? wf.nodes : [];
      const structural = inspectWebhookAuthStructural(nodes);
      const exec = await executionSnapshot(creds, ALLOWED_WORKFLOW_ID);
      lastActive = Boolean(wf.active);
      return {
        id: wf.id,
        active: Boolean(wf.active),
        versionId: wf.versionId || null,
        nodes: nodes.length,
        running: exec.running ?? 0,
        executions: exec.count,
        executions_observable: exec.observable,
        webhook_path_present: structural.webhook_path_present,
        auth_config_structurally_present: structural.auth_config_structurally_present,
        name: wf.name || null,
      };
    },
    async activate(nowMs) {
      ops.push({ op: 'ACTIVATE', at_ms: nowMs ?? Date.now() });
      const before = lastActive;
      try {
        await activateAllowlistedWorkflow(creds, activateConfirm);
        const after = await this.getWorkflowState(nowMs);
        if (before === false && after.active === true) {
          activationChanges += 1;
        } else if (before == null && after.active === true) {
          // Unknown before — count only if transition observed via second GET later budget.
          activationChanges += 1;
        }
        return {
          attempted: true,
          changed: before !== true && after.active === true,
          active_after: after.active,
          version_id: after.versionId,
          timestamp_ms: nowMs ?? Date.now(),
          error_class: null,
        };
      } catch (err) {
        const after = await this.getWorkflowState(nowMs).catch(() => ({
          active: lastActive,
          versionId: null,
        }));
        return {
          attempted: true,
          changed: false,
          active_after: Boolean(after.active),
          version_id: after.versionId ?? null,
          timestamp_ms: nowMs ?? Date.now(),
          error_class: 'ACTIVATION_API_FAILURE',
          error_name: err instanceof Error ? err.name : 'Error',
        };
      }
    },
    async deactivate(nowMs, { emergency = false } = {}) {
      ops.push({
        op: emergency ? 'EMERGENCY_DEACTIVATE' : 'DEACTIVATE',
        at_ms: nowMs ?? Date.now(),
      });
      const phrase = emergency ? emergencyConfirm : deactivateConfirm;
      const before = lastActive;
      try {
        await deactivateAllowlistedWorkflow(creds, phrase);
        const after = await this.getWorkflowState(nowMs);
        if (before === true && after.active === false) {
          activationChanges += 1;
        } else if (after.active === false && before !== false) {
          activationChanges += 1;
        }
        return {
          attempted: true,
          changed: before === true && after.active === false,
          active_after: after.active,
          version_id: after.versionId,
          timestamp_ms: nowMs ?? Date.now(),
          error_class: null,
          emergency: Boolean(emergency),
        };
      } catch (err) {
        const after = await this.getWorkflowState(nowMs).catch(() => ({
          active: lastActive,
          versionId: null,
        }));
        return {
          attempted: true,
          changed: false,
          active_after: Boolean(after.active),
          version_id: after.versionId ?? null,
          timestamp_ms: nowMs ?? Date.now(),
          error_class: emergency
            ? 'EMERGENCY_DEACTIVATION_API_FAILURE'
            : 'DEACTIVATION_API_FAILURE',
          emergency: Boolean(emergency),
          error_name: err instanceof Error ? err.name : 'Error',
        };
      }
    },
    async checkDedupe(eventId, nowMs) {
      ops.push({ op: 'DEDUPE_CHECK', at_ms: nowMs ?? Date.now() });
      if (!eventId) {
        return { event_id: '', seen: false, row: null };
      }
      const filtered = await getDataTableRows(dtCreds, D6C2_TABLE_ID, {
        limit: 5,
        filter: { filters: [{ columnName: 'event_id', condition: 'eq', value: String(eventId) }] },
      });
      const filterRows = filtered.data?.data || filtered.data || [];
      const eventRow = Array.isArray(filterRows) && filterRows[0] ? filterRows[0] : null;
      const rowData = eventRow?.data || eventRow || {};
      return {
        event_id: String(eventId),
        seen: Boolean(eventRow),
        row: eventRow
          ? {
              intake_state: rowData.intake_state ?? null,
              delivery_state: rowData.delivery_state ?? null,
              event_status: rowData.event_status ?? null,
            }
          : null,
      };
    },
    async postWebhook(_payloadRef, nowMs) {
      ops.push({ op: 'WEBHOOK_POST_BLOCKED', at_ms: nowMs ?? Date.now() });
      if (!allowWebhookPost) {
        return {
          attempted: false,
          http_status: null,
          result_class: 'WEBHOOK_POST_FORBIDDEN_BY_PRODUCTION_TRANSPORT',
          ambiguous: false,
          timestamp_ms: nowMs ?? Date.now(),
          error_class: 'WEBHOOK_POST_FORBIDDEN',
        };
      }
      throw new Error('PRODUCTION_TRANSPORT_WEBHOOK_POST_NOT_IMPLEMENTED_FOR_D6C2');
    },
  };
}
