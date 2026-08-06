/**
 * Client Ops workflow update client — PUT only for one allowlisted workflow ID.
 *
 * Separate from GET-only exporter and create-only write client.
 * Rejects POST create, DELETE, activate/deactivate, and webhook calls.
 */

import {
  loadCredentials,
  normalizeBaseUrl,
} from '../../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';

export const ALLOWED_WORKFLOW_ID = 'tkM4H0G0gM3q9Foi';
export const ALLOWED_WORKFLOW_NAME = 'MARS Client Ops Bridge — bzpm.ru';

const FORBIDDEN_PATH_FRAGMENTS = [
  '/activate',
  '/deactivate',
  '/execute',
  '/run',
  '/credentials',
];

/**
 * @param {string} [envPath]
 */
export function loadUpdateCredentials(envPath) {
  return loadCredentials(envPath);
}

/**
 * Strip server-managed / read-only fields for PUT body.
 * @param {Record<string, unknown>} wf
 */
export function prepareWorkflowPutPayload(wf) {
  const nodes = structuredClone(wf.nodes || []);
  for (const node of nodes) {
    delete node.webhookId;
  }
  return {
    name: wf.name,
    nodes,
    connections: structuredClone(wf.connections || {}),
    settings: {
      executionOrder:
        /** @type {{ executionOrder?: string }} */ (wf.settings)?.executionOrder || 'v1',
    },
  };
}

/**
 * @param {string} method
 * @param {string} path
 * @param {unknown} [body]
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function n8nWorkflowUpdateRequest(method, path, body, creds) {
  const upper = String(method).toUpperCase();
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;

  if (upper !== 'PUT') {
    throw new Error(
      `Workflow update client rejects method ${upper}. Only PUT is allowed.`,
    );
  }

  const expected = `/api/v1/workflows/${ALLOWED_WORKFLOW_ID}`;
  if (normalizedPath !== expected) {
    throw new Error(
      `Workflow update client rejects path ${normalizedPath}. Only ${expected} is allowed.`,
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
      method: 'PUT',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'X-N8N-API-KEY': creds.apiKey,
      },
      body: JSON.stringify(body),
    });
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    throw new Error(`Network failure calling n8n update API (${normalizedPath}): ${message}`);
  }

  const text = await response.text();
  let data = null;
  if (text) {
    try {
      data = JSON.parse(text);
    } catch {
      throw new Error(
        `Invalid JSON from n8n update API (${response.status} ${normalizedPath}).`,
      );
    }
  }

  if (!response.ok) {
    const detail =
      data && typeof data === 'object' && 'message' in data
        ? String(/** @type {{ message?: unknown }} */ (data).message)
        : text.slice(0, 200);
    throw new Error(`n8n update API error ${response.status} ${normalizedPath}: ${detail}`);
  }

  return data;
}

/**
 * @param {Record<string, unknown>} putPayload
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function updateAllowlistedWorkflow(putPayload, creds) {
  if (!putPayload || putPayload.name !== ALLOWED_WORKFLOW_NAME) {
    throw new Error('PUT rejected: workflow name mismatch.');
  }
  return n8nWorkflowUpdateRequest(
    'PUT',
    `/api/v1/workflows/${ALLOWED_WORKFLOW_ID}`,
    putPayload,
    creds,
  );
}
