/**
 * GET-only n8n REST API client.
 * Allowed: GET /api/v1/workflows, GET /api/v1/workflows/{id}
 */

import { readFileSync, existsSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../../../');
const DEFAULT_ENV_PATH = resolve(REPO_ROOT, 'local/tokens/n8n-api.env');

const ALLOWED_METHODS = new Set(['GET']);

/**
 * @param {string} [envPath]
 * @returns {{ apiUrl: string, apiKey: string, envPath: string }}
 */
export function loadCredentials(envPath = DEFAULT_ENV_PATH) {
  const resolvedPath = resolve(envPath);
  if (!existsSync(resolvedPath)) {
    throw new Error(
      `Missing credential file: ${resolvedPath}\n` +
        'Create local/tokens/n8n-api.env with N8N_API_URL and N8N_API_KEY (gitignored).',
    );
  }

  const raw = readFileSync(resolvedPath, 'utf8');
  const vars = {};
  for (const line of raw.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    const eq = trimmed.indexOf('=');
    if (eq === -1) continue;
    const key = trimmed.slice(0, eq).trim();
    let value = trimmed.slice(eq + 1).trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    vars[key] = value;
  }

  const apiUrl = (vars.N8N_API_URL || '').trim();
  const apiKey = (vars.N8N_API_KEY || '').trim();

  if (!apiUrl) {
    throw new Error('N8N_API_URL is missing or empty in credential file.');
  }
  if (!apiKey) {
    throw new Error('N8N_API_KEY is missing or empty in credential file.');
  }

  return { apiUrl: normalizeBaseUrl(apiUrl), apiKey, envPath: resolvedPath };
}

/**
 * @param {string} url
 * @returns {string}
 */
export function normalizeBaseUrl(url) {
  return url.replace(/\/+$/, '');
}

/**
 * @param {string} method
 * @param {string} path
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @returns {Promise<unknown>}
 */
export async function n8nGet(path, creds) {
  return n8nRequest('GET', path, creds);
}

/**
 * @param {string} method
 * @param {string} path
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @returns {Promise<unknown>}
 */
export async function n8nRequest(method, path, creds) {
  const upperMethod = String(method).toUpperCase();
  if (!ALLOWED_METHODS.has(upperMethod)) {
    throw new Error(
      `Rejected non-GET method: ${upperMethod}. This client is read-only (GET only).`,
    );
  }

  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  const url = `${creds.apiUrl}${normalizedPath}`;

  let response;
  try {
    response = await fetch(url, {
      method: upperMethod,
      headers: {
        Accept: 'application/json',
        'X-N8N-API-KEY': creds.apiKey,
      },
    });
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    throw new Error(`Network failure calling n8n API (${normalizedPath}): ${message}`);
  }

  const bodyText = await response.text();
  let data;
  if (bodyText) {
    try {
      data = JSON.parse(bodyText);
    } catch {
      throw new Error(
        `Invalid JSON from n8n API (${response.status} ${normalizedPath}).`,
      );
    }
  } else {
    data = null;
  }

  if (response.status === 401) {
    throw new Error(
      '401 Unauthorized — check N8N_API_KEY in local/tokens/n8n-api.env. ' +
        'Ensure the key is valid and has workflow read access.',
    );
  }
  if (response.status === 403) {
    throw new Error(
      '403 Forbidden — API key may lack permission for this endpoint.',
    );
  }
  if (response.status === 404) {
    throw new Error(`404 Not Found — ${normalizedPath}`);
  }
  if (!response.ok) {
    const detail =
      data && typeof data === 'object' && 'message' in data
        ? String(data.message)
        : bodyText.slice(0, 200);
    throw new Error(
      `n8n API error ${response.status} ${normalizedPath}: ${detail}`,
    );
  }

  return data;
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @returns {Promise<Array<{ id: string, name: string, active?: boolean }>>}
 */
export async function listWorkflows(creds) {
  const result = await n8nGet('/api/v1/workflows', creds);
  if (Array.isArray(result)) {
    return result;
  }
  if (result && Array.isArray(result.data)) {
    return result.data;
  }
  throw new Error('Unexpected workflows list response shape from n8n API.');
}

/**
 * @param {string} id
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @returns {Promise<Record<string, unknown>>}
 */
export async function getWorkflow(id, creds) {
  const result = await n8nGet(`/api/v1/workflows/${encodeURIComponent(id)}`, creds);
  if (!result || typeof result !== 'object') {
    throw new Error(`Unexpected workflow detail response for id ${id}.`);
  }
  return /** @type {Record<string, unknown>} */ (result);
}
