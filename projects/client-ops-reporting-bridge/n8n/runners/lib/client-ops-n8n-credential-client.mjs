/**
 * Client Ops credential client — CREATE + metadata GET only.
 *
 * Separate from GET-only exporter and workflow create/update clients.
 * Rejects credential update/delete and all workflow/webhook mutations.
 */

import {
  loadCredentials,
  normalizeBaseUrl,
} from '../../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';

const CREDENTIALS_PATH = '/api/v1/credentials';
const SCHEMA_PREFIX = '/api/v1/credentials/schema/';
const FORBIDDEN_PATH_FRAGMENTS = [
  '/activate',
  '/deactivate',
  '/execute',
  '/run',
  '/workflows',
  '/webhook',
];

/**
 * @param {string} [envPath]
 */
export function loadCredentialClientCredentials(envPath) {
  return loadCredentials(envPath);
}

/**
 * @param {string} method
 * @param {string} path
 * @param {unknown} [body]
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {{ allowBody?: boolean }} [opts]
 */
async function credentialRequest(method, path, body, creds, opts = {}) {
  const upper = String(method).toUpperCase();
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;

  for (const frag of FORBIDDEN_PATH_FRAGMENTS) {
    if (normalizedPath.includes(frag) && !normalizedPath.startsWith(CREDENTIALS_PATH)) {
      throw new Error(`Credential client rejects path fragment: ${frag}`);
    }
  }
  if (normalizedPath.includes('/workflows')) {
    throw new Error('Credential client rejects workflow paths.');
  }

  if (upper === 'GET') {
    if (
      !(
        normalizedPath === CREDENTIALS_PATH ||
        normalizedPath.startsWith(`${CREDENTIALS_PATH}?`) ||
        normalizedPath.startsWith(SCHEMA_PREFIX) ||
        /^\/api\/v1\/credentials\/[^/]+$/.test(normalizedPath)
      )
    ) {
      throw new Error(`Credential client rejects GET path ${normalizedPath}`);
    }
  } else if (upper === 'POST') {
    if (normalizedPath !== CREDENTIALS_PATH) {
      throw new Error(
        `Credential client rejects POST path ${normalizedPath}. Only ${CREDENTIALS_PATH} create is allowed.`,
      );
    }
  } else {
    throw new Error(
      `Credential client rejects method ${upper}. Only GET metadata and POST create are allowed.`,
    );
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
  if (upper === 'POST') {
    if (!opts.allowBody) {
      throw new Error('Credential create requires allowBody.');
    }
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
    throw new Error(`Network failure calling n8n credential API (${normalizedPath}): ${message}`);
  }

  const text = await response.text();
  let data = null;
  if (text) {
    try {
      data = JSON.parse(text);
    } catch {
      throw new Error(
        `Invalid JSON from n8n credential API (${response.status} ${normalizedPath}).`,
      );
    }
  }

  if (!response.ok) {
    const detail =
      data && typeof data === 'object' && 'message' in data
        ? String(/** @type {{ message?: unknown }} */ (data).message)
        : `HTTP_${response.status}`;
    // Never echo request body or credential data fields.
    throw new Error(`n8n credential API error ${response.status} ${normalizedPath}: ${detail}`);
  }

  return data;
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {{ limit?: number }} [opts]
 */
export async function listCredentialsMetadata(creds, opts = {}) {
  const limit = opts.limit ?? 250;
  const data = await credentialRequest(
    'GET',
    `${CREDENTIALS_PATH}?limit=${encodeURIComponent(String(limit))}`,
    undefined,
    creds,
  );
  const list = Array.isArray(data) ? data : data?.data || [];
  return list.map((c) => ({
    id: c.id,
    name: c.name,
    type: c.type,
    createdAt: c.createdAt ?? null,
    updatedAt: c.updatedAt ?? null,
  }));
}

/**
 * @param {string} credentialTypeName
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function getCredentialSchema(credentialTypeName, creds) {
  return credentialRequest(
    'GET',
    `${SCHEMA_PREFIX}${encodeURIComponent(credentialTypeName)}`,
    undefined,
    creds,
  );
}

/**
 * Create exactly one credential. Body must never be logged by callers.
 *
 * @param {{ name: string, type: string, data: Record<string, unknown> }} createPayload
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function createCredential(createPayload, creds) {
  if (!createPayload || typeof createPayload !== 'object') {
    throw new Error('Invalid credential create payload.');
  }
  if (!createPayload.name || !createPayload.type || !createPayload.data) {
    throw new Error('Credential create requires name, type, and data.');
  }
  const result = await credentialRequest(
    'POST',
    CREDENTIALS_PATH,
    createPayload,
    creds,
    { allowBody: true },
  );
  return {
    id: result?.id ?? null,
    name: result?.name ?? null,
    type: result?.type ?? null,
    createdAt: result?.createdAt ?? null,
    updatedAt: result?.updatedAt ?? null,
  };
}

/**
 * Sanitize create/list responses — strip any accidental data fields.
 * @param {unknown} value
 */
export function sanitizeCredentialResponse(value) {
  if (!value || typeof value !== 'object') return value;
  if (Array.isArray(value)) {
    return value.map((item) => sanitizeCredentialResponse(item));
  }
  const obj = /** @type {Record<string, unknown>} */ (value);
  const out = {};
  for (const [k, v] of Object.entries(obj)) {
    if (k === 'data' || k === 'password' || k === 'value' || k === 'accessToken') {
      out[k] = 'REDACTED';
      continue;
    }
    out[k] = sanitizeCredentialResponse(v);
  }
  return out;
}
