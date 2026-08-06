/**
 * Temporary semantics workflow client — Phase 1B-C0S only.
 *
 * Allows create / update / activate / deactivate / delete ONLY for the
 * exact temporary semantics workflow name, and NEVER for the real
 * Client Ops workflow ID tkM4H0G0gM3q9Foi.
 */

import {
  loadCredentials,
  normalizeBaseUrl,
} from '../../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';

export const TEMP_WORKFLOW_NAME =
  'MARS TEMP — Respond Telegram Semantics — bzpm.ru';
export const REAL_WORKFLOW_ID_DENY = 'tkM4H0G0gM3q9Foi';
export const REAL_WORKFLOW_NAME_DENY = 'MARS Client Ops Bridge — bzpm.ru';
export const EXPECTED_HOST = 'n8n.ai-metacode.com';

/**
 * @param {string} [envPath]
 */
export function loadTempSemanticsCredentials(envPath) {
  return loadCredentials(envPath);
}

/**
 * @param {string} workflowId
 */
function assertNotRealWorkflow(workflowId) {
  if (!workflowId || typeof workflowId !== 'string') {
    throw new Error('workflowId required');
  }
  if (workflowId === REAL_WORKFLOW_ID_DENY) {
    throw new Error(
      `DENIED: real Client Ops workflow ${REAL_WORKFLOW_ID_DENY} is immutable in this client`,
    );
  }
}

/**
 * @param {string} name
 */
function assertTempName(name) {
  if (name !== TEMP_WORKFLOW_NAME) {
    throw new Error(
      `DENIED: workflow name must be exactly ${TEMP_WORKFLOW_NAME}`,
    );
  }
  if (name === REAL_WORKFLOW_NAME_DENY) {
    throw new Error('DENIED: real Client Ops workflow name');
  }
}

/**
 * @param {string} method
 * @param {string} path
 * @param {unknown} [body]
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
async function request(method, path, body, creds) {
  const host = new URL(creds.apiUrl).host;
  if (host !== EXPECTED_HOST) {
    throw new Error(`Unexpected API host: ${host}`);
  }

  const upper = String(method).toUpperCase();
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;

  if (normalizedPath.includes(REAL_WORKFLOW_ID_DENY)) {
    throw new Error('DENIED: path references real Client Ops workflow ID');
  }
  if (/\/credentials|\/webhook\b/i.test(normalizedPath) && !normalizedPath.includes('/workflows')) {
    throw new Error(`DENIED path: ${normalizedPath}`);
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
    /** @type {Record<string, string>} */ (init.headers)['Content-Type'] =
      'application/json';
    init.body = JSON.stringify(body);
  }

  const response = await fetch(url, init);
  const text = await response.text();
  let data = null;
  if (text) {
    try {
      data = JSON.parse(text);
    } catch {
      data = { parse_error: true, body_len: text.length };
    }
  }
  if (!response.ok) {
    const detail =
      data && typeof data === 'object' && 'message' in data
        ? String(/** @type {{ message?: unknown }} */ (data).message)
        : `HTTP_${response.status}`;
    throw new Error(`n8n temp-semantics API ${response.status} ${normalizedPath}: ${detail}`);
  }
  return data;
}

/**
 * @param {Record<string, unknown>} createPayload
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function createTempSemanticsWorkflow(createPayload, creds) {
  assertTempName(String(createPayload.name || ''));
  if (createPayload.id) {
    throw new Error('create payload must not include id');
  }
  if (createPayload.active === true) {
    throw new Error('create payload must not request active=true');
  }
  return request('POST', '/api/v1/workflows', createPayload, creds);
}

/**
 * @param {string} workflowId
 * @param {Record<string, unknown>} putPayload
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function updateTempSemanticsWorkflow(workflowId, putPayload, creds) {
  assertNotRealWorkflow(workflowId);
  assertTempName(String(putPayload.name || ''));
  return request(
    'PUT',
    `/api/v1/workflows/${encodeURIComponent(workflowId)}`,
    putPayload,
    creds,
  );
}

/**
 * @param {string} workflowId
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function activateTempSemanticsWorkflow(workflowId, creds) {
  assertNotRealWorkflow(workflowId);
  return request(
    'POST',
    `/api/v1/workflows/${encodeURIComponent(workflowId)}/activate`,
    undefined,
    creds,
  );
}

/**
 * @param {string} workflowId
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function deactivateTempSemanticsWorkflow(workflowId, creds) {
  assertNotRealWorkflow(workflowId);
  return request(
    'POST',
    `/api/v1/workflows/${encodeURIComponent(workflowId)}/deactivate`,
    undefined,
    creds,
  );
}

/**
 * @param {string} workflowId
 * @param {{ apiUrl: string, apiKey: string }} creds
 */
export async function deleteTempSemanticsWorkflow(workflowId, creds) {
  assertNotRealWorkflow(workflowId);
  return request(
    'DELETE',
    `/api/v1/workflows/${encodeURIComponent(workflowId)}`,
    undefined,
    creds,
  );
}

/**
 * Strip server-managed fields for PUT.
 * @param {Record<string, unknown>} wf
 */
export function prepareTempPutPayload(wf) {
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
        /** @type {{ executionOrder?: string }} */ (wf.settings)?.executionOrder ||
        'v1',
    },
  };
}
