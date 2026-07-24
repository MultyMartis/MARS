/**
 * Client Ops Data Table API client — allowlisted to one dedicated dedupe table name.
 * Used by Phase 1B-D1 durable dedupe sandbox runner only.
 */

import {
  loadCredentials,
  normalizeBaseUrl,
} from '../../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';

export const ALLOWED_TABLE_NAME = 'MARS Client Ops Dedupe — bzpm.ru';

/**
 * @param {string} [envPath]
 */
export function loadDataTableCredentials(envPath) {
  return loadCredentials(envPath);
}

/**
 * @param {string} method
 * @param {string} path
 * @param {unknown} [body]
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function n8nDataTableRequest(method, path, body, creds) {
  const upper = String(method).toUpperCase();
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  const allowedPrefixes = [
    '/api/v1/data-tables',
  ];
  if (!allowedPrefixes.some((p) => normalizedPath === p || normalizedPath.startsWith(`${p}/`))) {
    throw new Error(`Data Table client rejects path ${normalizedPath}`);
  }
  if (!['GET', 'POST', 'PATCH', 'DELETE'].includes(upper)) {
    throw new Error(`Data Table client rejects method ${upper}`);
  }

  const url = `${normalizeBaseUrl(creds.apiUrl)}${normalizedPath}`;
  /** @type {RequestInit} */
  const init = {
    method: upper,
    headers: {
      Accept: 'application/json',
      'X-N8N-API-KEY': creds.apiKey,
    },
  };
  if (body !== undefined) {
    init.headers = {
      ...init.headers,
      'Content-Type': 'application/json',
    };
    init.body = JSON.stringify(body);
  }

  let response;
  try {
    response = await fetch(url, init);
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    throw new Error(`Network failure calling n8n Data Table API (${normalizedPath}): ${message}`);
  }

  const text = await response.text();
  let data = null;
  if (text) {
    try {
      data = JSON.parse(text);
    } catch {
      if (response.status !== 204) {
        throw new Error(
          `Invalid JSON from n8n Data Table API (${response.status} ${normalizedPath}).`,
        );
      }
    }
  }

  if (!response.ok) {
    const detail =
      data && typeof data === 'object' && 'message' in data
        ? String(/** @type {{ message?: unknown }} */ (data).message)
        : text.slice(0, 200);
    throw new Error(
      `n8n Data Table API error ${response.status} ${normalizedPath}: ${detail}`,
    );
  }

  return { status: response.status, data };
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function listDataTables(creds) {
  const { data } = await n8nDataTableRequest('GET', '/api/v1/data-tables', undefined, creds);
  const rows = data?.data || data || [];
  return Array.isArray(rows) ? rows : [];
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} name
 */
export async function countTablesByExactName(creds, name = ALLOWED_TABLE_NAME) {
  const tables = await listDataTables(creds);
  return tables.filter((t) => t.name === name).length;
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {{ name: string, columns: Array<{ name: string, type: string }> }} payload
 */
export async function createAllowlistedDataTable(creds, payload) {
  if (payload.name !== ALLOWED_TABLE_NAME) {
    throw new Error(`Refusing to create non-allowlisted table name: ${payload.name}`);
  }
  return n8nDataTableRequest('POST', '/api/v1/data-tables', payload, creds);
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} tableId
 */
export async function getDataTable(creds, tableId) {
  return n8nDataTableRequest(
    'GET',
    `/api/v1/data-tables/${encodeURIComponent(tableId)}`,
    undefined,
    creds,
  );
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} tableId
 * @param {Record<string, unknown>} [query]
 */
export async function getDataTableRows(creds, tableId, query = {}) {
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
  const path = `/api/v1/data-tables/${encodeURIComponent(tableId)}/rows${qs ? `?${qs}` : ''}`;
  return n8nDataTableRequest('GET', path, undefined, creds);
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} tableId
 * @param {Record<string, unknown>} body
 */
export async function insertDataTableRows(creds, tableId, body) {
  return n8nDataTableRequest(
    'POST',
    `/api/v1/data-tables/${encodeURIComponent(tableId)}/rows`,
    body,
    creds,
  );
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} tableId
 * @param {Record<string, unknown>} body
 */
export async function upsertDataTableRow(creds, tableId, body) {
  return n8nDataTableRequest(
    'POST',
    `/api/v1/data-tables/${encodeURIComponent(tableId)}/rows/upsert`,
    body,
    creds,
  );
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} tableId
 * @param {Record<string, unknown>} body
 */
export async function updateDataTableRows(creds, tableId, body) {
  return n8nDataTableRequest(
    'PATCH',
    `/api/v1/data-tables/${encodeURIComponent(tableId)}/rows/update`,
    body,
    creds,
  );
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} tableId
 * @param {Record<string, unknown>} body
 */
export async function deleteDataTableRows(creds, tableId, body) {
  return n8nDataTableRequest(
    'DELETE',
    `/api/v1/data-tables/${encodeURIComponent(tableId)}/rows/delete`,
    body,
    creds,
  );
}

/**
 * Delete only the allowlisted D1 table by ID after verifying name.
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} tableId
 */
export async function deleteAllowlistedDataTable(creds, tableId) {
  const { data } = await getDataTable(creds, tableId);
  if (!data || data.name !== ALLOWED_TABLE_NAME) {
    throw new Error('Refusing to delete table: name mismatch or missing');
  }
  return n8nDataTableRequest(
    'DELETE',
    `/api/v1/data-tables/${encodeURIComponent(tableId)}`,
    undefined,
    creds,
  );
}

export const D1_TABLE_COLUMNS = [
  { name: 'event_id', type: 'string' },
  { name: 'event_fingerprint', type: 'string' },
  { name: 'site_id', type: 'string' },
  { name: 'schema_name', type: 'string' },
  { name: 'schema_version', type: 'string' },
  { name: 'event_type', type: 'string' },
  { name: 'event_status', type: 'string' },
  { name: 'intake_state', type: 'string' },
  { name: 'delivery_state', type: 'string' },
  { name: 'first_seen_at', type: 'string' },
  { name: 'last_seen_at', type: 'string' },
  { name: 'duplicate_count', type: 'number' },
  { name: 'conflict_count', type: 'number' },
  { name: 'redaction_version', type: 'string' },
  { name: 'sandbox_marker', type: 'string' },
];
