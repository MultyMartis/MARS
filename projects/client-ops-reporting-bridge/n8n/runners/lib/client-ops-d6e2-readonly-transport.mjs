/**
 * Phase 1B-D6E2 — allowlisted GET-only production evidence transport.
 *
 * Mechanically rejects webhook POST, activation/deactivation, Data Table
 * mutation, Telegram, and retry execution. Credentials never written to evidence.
 */

import {
  loadCredentials,
  normalizeBaseUrl,
} from '../../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';

export const D6E2_ALLOWED_WORKFLOW_ID = 'tkM4H0G0gM3q9Foi';
export const D6E2_ALLOWED_DATA_TABLE_ID = 'H6VYhwz7RXZCBMmu';
export const D6E2_ALLOWED_EVENT_IDS = Object.freeze([
  'c84e29bf-79b1-5aea-98c4-9dc8d651fc96',
  'd6a2a001-27d6-4a2e-bd6a-000000000001',
]);
export const D6E2_HISTORICAL_EXECUTION_ID = '3416';

const FORBIDDEN_METHODS = new Set([
  'POST',
  'PUT',
  'PATCH',
  'DELETE',
  'OPTIONS',
  'HEAD',
]);

/**
 * Local reject of non-GET / mutation surfaces before any network call.
 * @param {string} method
 * @param {string} action
 */
export function assertGetOnlyAction(method, action = 'generic') {
  const upper = String(method || '').toUpperCase();
  if (upper !== 'GET') {
    throw new Error(
      `D6E2_READ_ONLY_INVARIANT: rejected method=${upper} action=${action}`,
    );
  }
  const forbiddenActions = new Set([
    'webhook_post',
    'activate',
    'deactivate',
    'data_table_insert',
    'data_table_update',
    'data_table_delete',
    'data_table_upsert',
    'telegram',
    'retry_execution',
    'reconcile_mutate',
    'put_workflow',
    'patch_workflow',
  ]);
  if (forbiddenActions.has(String(action))) {
    throw new Error(
      `D6E2_READ_ONLY_INVARIANT: rejected forbidden action=${action}`,
    );
  }
}

/**
 * Prove mutation surfaces cannot be issued through this wrapper.
 */
export function proveReadOnlyInvariant() {
  const probes = [
    ['POST', 'webhook_post'],
    ['POST', 'activate'],
    ['POST', 'deactivate'],
    ['POST', 'data_table_insert'],
    ['PATCH', 'data_table_update'],
    ['DELETE', 'data_table_delete'],
    ['POST', 'telegram'],
    ['POST', 'retry_execution'],
    ['PUT', 'put_workflow'],
  ];
  const rejected = [];
  for (const [method, action] of probes) {
    try {
      assertGetOnlyAction(method, action);
      rejected.push({ method, action, rejected: false });
    } catch {
      rejected.push({ method, action, rejected: true });
    }
  }
  const allRejected = rejected.every((r) => r.rejected === true);
  // GET must still be allowed
  assertGetOnlyAction('GET', 'workflow_get');
  return {
    token: allRejected
      ? 'D6E2_READ_ONLY_INVARIANT_ARMED'
      : 'D6E2_READ_ONLY_INVARIANT_FAILED',
    all_mutation_probes_rejected: allRejected,
    probes: rejected,
    allow_reads: true,
    allow_webhook: false,
    allow_activation: false,
    allow_deactivation: false,
    allow_data_table_mutation: false,
    allow_telegram: false,
    allow_retry_execution: false,
    allow_reconciliation_mutation: false,
  };
}

/**
 * @param {string} workflowId
 * @param {string} tableId
 * @param {string[]} eventIds
 */
export function securityPrecheck(workflowId, tableId, eventIds) {
  const issues = [];
  if (workflowId !== D6E2_ALLOWED_WORKFLOW_ID) {
    issues.push('workflow_id_not_allowlisted');
  }
  if (tableId !== D6E2_ALLOWED_DATA_TABLE_ID) {
    issues.push('data_table_id_not_allowlisted');
  }
  for (const id of eventIds || []) {
    if (!D6E2_ALLOWED_EVENT_IDS.includes(id)) {
      issues.push(`event_id_not_allowlisted:${id}`);
    }
  }
  return {
    token: issues.length === 0 ? 'D6E2_SECURITY_GATE_PASS' : 'D6E2_SECURITY_GATE_FAIL',
    issues,
    workflow_id_allowlisted: workflowId === D6E2_ALLOWED_WORKFLOW_ID,
    data_table_id_allowlisted: tableId === D6E2_ALLOWED_DATA_TABLE_ID,
    event_ids_allowlisted: (eventIds || []).every((id) =>
      D6E2_ALLOWED_EVENT_IDS.includes(id),
    ),
    no_arbitrary_url: true,
    no_raw_api_key_in_evidence: true,
    no_authorization_header_persisted: true,
    no_telegram_token: true,
    no_webhook_auth_secret: true,
  };
}

/**
 * @param {string} method
 * @param {string} path
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} action
 */
export async function d6e2Get(path, creds, action = 'generic_get') {
  assertGetOnlyAction('GET', action);
  const upper = 'GET';
  if (FORBIDDEN_METHODS.has(upper)) {
    throw new Error(`D6E2 rejects method ${upper}`);
  }

  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  const allowed =
    normalizedPath === `/api/v1/workflows/${D6E2_ALLOWED_WORKFLOW_ID}` ||
    normalizedPath.startsWith(
      `/api/v1/workflows/${D6E2_ALLOWED_WORKFLOW_ID}?`,
    ) ||
    normalizedPath.startsWith('/api/v1/executions') ||
    normalizedPath === `/api/v1/data-tables/${D6E2_ALLOWED_DATA_TABLE_ID}` ||
    normalizedPath.startsWith(
      `/api/v1/data-tables/${D6E2_ALLOWED_DATA_TABLE_ID}/`,
    );

  if (!allowed) {
    throw new Error(`D6E2 rejects non-allowlisted path: ${normalizedPath}`);
  }

  // Extra guard: never allow row mutation path segments even if method were wrong
  if (/\/(upsert|update|delete)\b/i.test(normalizedPath)) {
    throw new Error(`D6E2 rejects mutation path segment: ${normalizedPath}`);
  }

  const url = `${normalizeBaseUrl(creds.apiUrl)}${normalizedPath}`;
  let response;
  try {
    response = await fetch(url, {
      method: 'GET',
      headers: {
        Accept: 'application/json',
        'X-N8N-API-KEY': creds.apiKey,
      },
    });
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    throw new Error(`D6E2 network failure (${normalizedPath}): ${message}`);
  }

  const text = await response.text();
  let data = null;
  if (text) {
    try {
      data = JSON.parse(text);
    } catch {
      throw new Error(`D6E2 invalid JSON (${response.status} ${normalizedPath})`);
    }
  }
  if (!response.ok) {
    const detail =
      data && typeof data === 'object' && 'message' in data
        ? String(/** @type {{ message?: unknown }} */ (data).message)
        : text.slice(0, 200);
    throw new Error(`D6E2 API error ${response.status} ${normalizedPath}: ${detail}`);
  }
  return { status: response.status, data };
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function getAllowlistedWorkflow(creds) {
  const { data } = await d6e2Get(
    `/api/v1/workflows/${D6E2_ALLOWED_WORKFLOW_ID}`,
    creds,
    'workflow_get',
  );
  return data;
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function getExecutionSnapshot(creds) {
  const path = `/api/v1/executions?workflowId=${encodeURIComponent(D6E2_ALLOWED_WORKFLOW_ID)}&limit=100`;
  const { data } = await d6e2Get(path, creds, 'executions_list');
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
 * Sanitized execution GET — no raw payload persistence by caller.
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} executionId
 */
export async function getSanitizedExecution(creds, executionId = D6E2_HISTORICAL_EXECUTION_ID) {
  const id = String(executionId);
  if (id !== D6E2_HISTORICAL_EXECUTION_ID) {
    throw new Error(`D6E2 rejects non-allowlisted execution id: ${id}`);
  }
  try {
    const { data } = await d6e2Get(
      `/api/v1/executions/${encodeURIComponent(id)}?includeData=false`,
      creds,
      'execution_get',
    );
    return {
      available: true,
      execution_id: String(data?.id ?? id),
      workflow_id: data?.workflowId != null ? String(data.workflowId) : null,
      status: data?.status != null ? String(data.status) : null,
      finished: data?.finished === true,
      mode: data?.mode != null ? String(data.mode) : null,
      startedAt: data?.startedAt != null ? String(data.startedAt) : null,
      stoppedAt: data?.stoppedAt != null ? String(data.stoppedAt) : null,
      raw_payload_persisted: false,
    };
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    return {
      available: false,
      execution_id: id,
      reason: message.includes('404') ? 'NOT_FOUND' : 'GET_FAILED',
      detail_sanitized: message.replace(/[A-Za-z0-9_\-]{20,}/g, '[redacted]').slice(0, 160),
      raw_payload_persisted: false,
    };
  }
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function getAllowlistedDataTable(creds) {
  const { data } = await d6e2Get(
    `/api/v1/data-tables/${D6E2_ALLOWED_DATA_TABLE_ID}`,
    creds,
    'data_table_get',
  );
  return data;
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {Record<string, unknown>} [query]
 */
export async function getAllowlistedDataTableRows(creds, query = {}) {
  const params = new URLSearchParams();
  if (query.limit != null) params.set('limit', String(query.limit));
  if (query.cursor) params.set('cursor', String(query.cursor));
  if (query.filter) {
    params.set(
      'filter',
      typeof query.filter === 'string' ? query.filter : JSON.stringify(query.filter),
    );
  }
  const qs = params.toString();
  const path = `/api/v1/data-tables/${D6E2_ALLOWED_DATA_TABLE_ID}/rows${qs ? `?${qs}` : ''}`;
  const { data } = await d6e2Get(path, creds, 'data_table_rows_get');
  return data;
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} eventId
 */
export async function getAllowlistedEventRow(creds, eventId) {
  if (!D6E2_ALLOWED_EVENT_IDS.includes(eventId)) {
    throw new Error(`D6E2 rejects non-allowlisted event_id: ${eventId}`);
  }
  const filtered = await getAllowlistedDataTableRows(creds, {
    limit: 20,
    filter: { filters: [{ columnName: 'event_id', condition: 'eq', value: eventId }] },
  });
  const filterRows = filtered?.data || filtered || [];
  const rows = Array.isArray(filterRows) ? filterRows : [];
  const eventRow = rows[0] || null;
  const rowData = eventRow?.data || eventRow || {};
  return {
    event_id: eventId,
    rows: rows.length,
    intake_state: rowData.intake_state ?? null,
    event_status: rowData.event_status ?? null,
    delivery_state: rowData.delivery_state ?? null,
    first_seen_at: rowData.first_seen_at ?? null,
    last_seen_at: rowData.last_seen_at ?? null,
    duplicate_count: rowData.duplicate_count ?? null,
    conflict_count: rowData.conflict_count ?? null,
    sandbox_marker: rowData.sandbox_marker ?? null,
  };
}

export { loadCredentials, normalizeBaseUrl };
