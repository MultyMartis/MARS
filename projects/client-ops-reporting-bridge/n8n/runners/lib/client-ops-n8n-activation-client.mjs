/**
 * Client Ops n8n activation client — activate/deactivate ONLY for allowlisted workflow.
 *
 * Rejects create/update/delete, credential ops, and webhook POST.
 */

import {
  loadCredentials,
  normalizeBaseUrl,
} from '../../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';

export const ALLOWED_WORKFLOW_ID = 'tkM4H0G0gM3q9Foi';
export const ALLOWED_WORKFLOW_NAME = 'MARS Client Ops Bridge — bzpm.ru';
export const EXPECTED_HOST = 'n8n.ai-metacode.com';

const ACTIVATE_CONFIRM = 'TEMPORARILY ACTIVATE CLIENT OPS BRIDGE FOR POST VALIDATION';
const DEACTIVATE_CONFIRM = 'DEACTIVATE CLIENT OPS BRIDGE AFTER POST VALIDATION';
const C1_ACTIVATE_CONFIRM = 'ACTIVATE CLIENT OPS TELEGRAM SANDBOX TEST BZPM';
const C1_DEACTIVATE_CONFIRM = 'DEACTIVATE CLIENT OPS TELEGRAM SANDBOX TEST BZPM';

/**
 * @param {string} [envPath]
 */
export function loadActivationCredentials(envPath) {
  return loadCredentials(envPath);
}

/**
 * @param {string} method
 * @param {string} path
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {unknown} [body]
 */
async function activationRequest(method, path, creds, body) {
  const upper = String(method).toUpperCase();
  if (upper !== 'POST') {
    throw new Error(`Activation client rejects method ${upper}`);
  }
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  const activatePath = `/api/v1/workflows/${ALLOWED_WORKFLOW_ID}/activate`;
  const deactivatePath = `/api/v1/workflows/${ALLOWED_WORKFLOW_ID}/deactivate`;
  if (normalizedPath !== activatePath && normalizedPath !== deactivatePath) {
    throw new Error(`Activation client rejects path ${normalizedPath}`);
  }
  if (
    /\/credentials|\/execute|\/run|\/webhook/i.test(normalizedPath) ||
    (upper === 'PUT' || upper === 'DELETE' || upper === 'PATCH')
  ) {
    throw new Error('Forbidden operation for activation client');
  }

  const host = new URL(creds.apiUrl).host;
  if (host !== EXPECTED_HOST) {
    throw new Error(`Unexpected API host: ${host}`);
  }

  const url = `${normalizeBaseUrl(creds.apiUrl)}${normalizedPath}`;
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      'X-N8N-API-KEY': creds.apiKey,
    },
    body: body === undefined ? undefined : JSON.stringify(body),
  });
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
    throw new Error(`Activation API error ${response.status}: ${detail}`);
  }
  return data;
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} confirm
 */
export async function activateAllowlistedWorkflow(creds, confirm) {
  if (confirm !== ACTIVATE_CONFIRM && confirm !== C1_ACTIVATE_CONFIRM) {
    throw new Error('Activation confirmation phrase mismatch');
  }
  return activationRequest(
    'POST',
    `/api/v1/workflows/${ALLOWED_WORKFLOW_ID}/activate`,
    creds,
  );
}

/**
 * @param {{ apiUrl: string, apiKey: string }} creds
 * @param {string} confirm
 */
export async function deactivateAllowlistedWorkflow(creds, confirm) {
  if (confirm !== DEACTIVATE_CONFIRM && confirm !== C1_DEACTIVATE_CONFIRM) {
    throw new Error('Deactivation confirmation phrase mismatch');
  }
  return activationRequest(
    'POST',
    `/api/v1/workflows/${ALLOWED_WORKFLOW_ID}/deactivate`,
    creds,
  );
}

export const ACTIVATION_CONFIRM_PHRASE = ACTIVATE_CONFIRM;
export const DEACTIVATION_CONFIRM_PHRASE = DEACTIVATE_CONFIRM;
export const C1_ACTIVATION_CONFIRM_PHRASE = C1_ACTIVATE_CONFIRM;
export const C1_DEACTIVATION_CONFIRM_PHRASE = C1_DEACTIVATE_CONFIRM;
