/**
 * Client Ops write-capable n8n client — CREATE ONLY.
 *
 * Separate from GET-only n8n-readonly-exporter client.
 * Allows POST /api/v1/workflows for inactive greenfield create.
 * Rejects update/delete/activate paths.
 */

import { loadCredentials, normalizeBaseUrl } from '../../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';

const CREATE_PATH = '/api/v1/workflows';
const FORBIDDEN_PATH_FRAGMENTS = [
  '/activate',
  '/deactivate',
  '/execute',
  '/run',
];

/**
 * @param {string} [envPath]
 */
export function loadWriteCredentials(envPath) {
  return loadCredentials(envPath);
}

/**
 * @param {string} method
 * @param {string} path
 * @param {unknown} [body]
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function n8nWriteRequest(method, path, body, creds) {
  const upper = String(method).toUpperCase();
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;

  if (upper !== 'POST') {
    throw new Error(
      `Client Ops write client rejects method ${upper}. Only POST create is allowed.`,
    );
  }
  if (normalizedPath !== CREATE_PATH) {
    throw new Error(
      `Client Ops write client rejects path ${normalizedPath}. Only ${CREATE_PATH} create is allowed.`,
    );
  }
  for (const frag of FORBIDDEN_PATH_FRAGMENTS) {
    if (normalizedPath.includes(frag)) {
      throw new Error(`Forbidden write path fragment: ${frag}`);
    }
  }

  const url = `${normalizeBaseUrl(creds.apiUrl)}${normalizedPath}`;
  let response;
  try {
    response = await fetch(url, {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'X-N8N-API-KEY': creds.apiKey,
      },
      body: body === undefined ? undefined : JSON.stringify(body),
    });
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    throw new Error(`Network failure calling n8n write API (${normalizedPath}): ${message}`);
  }

  const text = await response.text();
  let data = null;
  if (text) {
    try {
      data = JSON.parse(text);
    } catch {
      throw new Error(
        `Invalid JSON from n8n write API (${response.status} ${normalizedPath}).`,
      );
    }
  }

  if (!response.ok) {
    const detail =
      data && typeof data === 'object' && 'message' in data
        ? String(/** @type {{ message?: unknown }} */ (data).message)
        : text.slice(0, 200);
    throw new Error(`n8n write API error ${response.status} ${normalizedPath}: ${detail}`);
  }

  return data;
}

/**
 * @param {Record<string, unknown>} createPayload
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function createWorkflow(createPayload, creds) {
  return n8nWriteRequest('POST', CREATE_PATH, createPayload, creds);
}
