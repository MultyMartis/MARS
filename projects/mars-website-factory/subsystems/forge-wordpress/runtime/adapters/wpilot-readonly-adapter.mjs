/**
 * V9-05C — WPilot read-only HTTP adapter (requires admission token).
 */
import fs from 'node:fs';
import path from 'node:path';
import { validateAdmissionToken } from '../src/admission-token.mjs';
import { RUNTIME_REASON_CODES as RC } from '../src/runtime-reason-codes.mjs';
import { loadProjectAdmission } from '../src/project-admission-registry.mjs';

export const ADAPTER_PHASE = 'V9-05C';
export const WPILOT_REST_BASE = '/wp-json/wpilot/v1';
export const EXPECTED_BUILD_ID = 'v0.3.0-rc5';
export const EXPECTED_PLUGIN_FILE_COUNT = 27;

const FORBIDDEN_ENDPOINTS = [
  'replace-text/dry-run',
  '/backups',
  'scoped-replace',
  '/rollback',
];

const SECRET_OUTPUT_PATTERNS = [
  /"token"\s*:\s*"[a-zA-Z0-9_]{20,}"/i,
  /wpilot_[a-zA-Z0-9]{20,}/,
  /define\s*\(\s*['"]DB_PASSWORD['"]/i,
];

function denyDirectAccess() {
  const err = new Error('RT_DIRECT_ADAPTER_DENIED');
  err.code = RC.RT_DIRECT_ADAPTER_DENIED;
  throw err;
}

function assertToken(token, request) {
  const validation = validateAdmissionToken(token, request);
  if (!validation.valid) {
    const err = new Error(validation.reason_codes.join(','));
    err.code = validation.reason_codes[0];
    err.reason_codes = validation.reason_codes;
    throw err;
  }
}

function redactOutput(obj) {
  const json = JSON.stringify(obj);
  for (const pattern of SECRET_OUTPUT_PATTERNS) {
    if (pattern.test(json)) {
      const err = new Error(RC.RT_SECRET_OUTPUT_BLOCKED);
      err.code = RC.RT_SECRET_OUTPUT_BLOCKED;
      throw err;
    }
  }
  return obj;
}

function loadTokenFromReference(tokenReference) {
  if (!tokenReference || !fs.existsSync(tokenReference)) {
    const err = new Error(RC.RT_WPILOT_TOKEN_MISSING);
    err.code = RC.RT_WPILOT_TOKEN_MISSING;
    throw err;
  }
  return fs.readFileSync(tokenReference, 'utf8').trim();
}

function mapWpilotError(body, httpStatus) {
  const code = body?.error?.code || body?.code;
  const map = {
    AUTH_MISSING: RC.RT_WPILOT_TOKEN_MISSING,
    AUTH_INVALID: RC.RT_WPILOT_TOKEN_INVALID,
    TOKEN_REVOKED: RC.RT_WPILOT_TOKEN_INVALID,
    BRIDGE_DISABLED: RC.RT_WPILOT_BRIDGE_DISABLED,
    DEV_NOT_CONFIRMED: RC.RT_WPILOT_DEV_NOT_CONFIRMED,
    EMERGENCY_DISABLED: RC.RT_WPILOT_EMERGENCY_DISABLED,
  };
  if (code && map[code]) {
    const err = new Error(map[code]);
    err.code = map[code];
    err.wpilot_code = code;
    return err;
  }
  if (httpStatus === 404) {
    const err = new Error(RC.RT_WPILOT_ENDPOINT_MISSING);
    err.code = RC.RT_WPILOT_ENDPOINT_MISSING;
    return err;
  }
  const err = new Error(RC.RT_WPILOT_HTTP_FAILURE);
  err.code = RC.RT_WPILOT_HTTP_FAILURE;
  err.http_status = httpStatus;
  return err;
}

function assertForbiddenEndpoint(endpoint) {
  for (const forbidden of FORBIDDEN_ENDPOINTS) {
    if (endpoint.includes(forbidden)) {
      const err = new Error(RC.RT_WPILOT_WRITE_ENDPOINT_DENIED);
      err.code = RC.RT_WPILOT_WRITE_ENDPOINT_DENIED;
      throw err;
    }
  }
}

function validateEnvelope(body) {
  if (!body || typeof body !== 'object') return false;
  if (body.ok === false) return false;
  return body.ok === true && Object.prototype.hasOwnProperty.call(body, 'data');
}

export function countPluginFiles(siteRoot) {
  const pluginDir = path.join(siteRoot, 'wp-content', 'plugins', 'metacode-wpilot');
  let count = 0;
  function walk(dir, depth = 0) {
    if (depth > 6) return;
    let entries;
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      return;
    }
    for (const entry of entries) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        walk(full, depth + 1);
      } else {
        count += 1;
      }
    }
  }
  walk(pluginDir);
  return count;
}

export function verifyWpilotBuild(siteRoot) {
  const fileCount = countPluginFiles(siteRoot);
  return {
    build_id: EXPECTED_BUILD_ID,
    plugin_file_count: fileCount,
    file_count_matches: fileCount === EXPECTED_PLUGIN_FILE_COUNT,
    verified: fileCount === EXPECTED_PLUGIN_FILE_COUNT,
  };
}

export async function wpilotRequest(siteRoot, token, request, endpoint, options = {}) {
  if (!token) denyDirectAccess();
  assertToken(token, request);
  assertForbiddenEndpoint(endpoint);

  const admission = loadProjectAdmission(request.site_id);
  const domain = admission?.domain || 'http://shpigovsky.test/';
  const tokenRef = admission?.token_reference;
  const authToken = loadTokenFromReference(tokenRef);
  const timeoutMs = options.timeout_ms ?? 30000;

  const base = domain.replace(/\/$/, '');
  const url = `${base}${WPILOT_REST_BASE}/${endpoint.replace(/^\//, '')}`;

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);

  let response;
  try {
    response = await fetch(url, {
      method: options.method || 'GET',
      headers: {
        'X-WPilot-Token': authToken,
        Accept: 'application/json',
      },
      signal: controller.signal,
    });
  } catch (err) {
    if (err.name === 'AbortError') {
      const e = new Error(RC.RT_WPILOT_TIMEOUT);
      e.code = RC.RT_WPILOT_TIMEOUT;
      throw e;
    }
    const e = new Error(RC.RT_WPILOT_HTTP_FAILURE);
    e.code = RC.RT_WPILOT_HTTP_FAILURE;
    e.cause = err.message;
    throw e;
  } finally {
    clearTimeout(timer);
  }

  let body;
  try {
    body = await response.json();
  } catch {
    const e = new Error(RC.RT_RESULT_SCHEMA_INVALID);
    e.code = RC.RT_RESULT_SCHEMA_INVALID;
    throw e;
  }

  if (!response.ok || body?.ok === false) {
    throw mapWpilotError(body, response.status);
  }

  if (!validateEnvelope(body)) {
    const e = new Error(RC.RT_RESULT_SCHEMA_INVALID);
    e.code = RC.RT_RESULT_SCHEMA_INVALID;
    throw e;
  }

  const bridge = body.data?.bridge || body.data?.environment || body.meta?.bridge;
  if (bridge?.write_enabled === true) {
    const e = new Error(RC.RT_WPILOT_WRITE_GATE_ENABLED);
    e.code = RC.RT_WPILOT_WRITE_GATE_ENABLED;
    throw e;
  }

  return redactOutput({
    operation_id: request.operation_id,
    status: 'SUCCEEDED',
    endpoint,
    http_status: response.status,
    data: body.data,
    meta: body.meta,
    read_only: true,
    phase: ADAPTER_PHASE,
    wpilot_build_check: verifyWpilotBuild(siteRoot),
  });
}

function makeWpilotHandler(endpointResolver) {
  return async (siteRoot, token, request, binding) => {
    const endpoint =
      typeof endpointResolver === 'function'
        ? endpointResolver(binding, request)
        : endpointResolver;
    return wpilotRequest(siteRoot, token, request, endpoint, {
      timeout_ms: binding?.timeout_ms,
    });
  };
}

export const wpilotSiteInfo = makeWpilotHandler('site-info');
export const wpilotThemes = makeWpilotHandler('themes');
export const wpilotPlugins = makeWpilotHandler('plugins');
export const wpilotPages = makeWpilotHandler('pages');
export const wpilotIndexingState = makeWpilotHandler('indexing-state');
export const wpilotPage = makeWpilotHandler((binding) => `pages/${binding.known_safe_page_id ?? 3}`);
export const wpilotPageStructure = makeWpilotHandler(
  (binding) => `pages/${binding.known_safe_page_id ?? 3}/structure`
);

const ADAPTER_MAP = Object.freeze({
  wpilotSiteInfo,
  wpilotThemes,
  wpilotPlugins,
  wpilotPages,
  wpilotPage,
  wpilotPageStructure,
  wpilotIndexingState,
});

export function executeWpilotAdapter(adapterModule, siteRoot, token, request, binding) {
  const fn = ADAPTER_MAP[adapterModule];
  if (!fn) {
    const err = new Error(RC.RT_BINDING_NOT_FOUND);
    err.code = RC.RT_BINDING_NOT_FOUND;
    throw err;
  }
  return fn(siteRoot, token, request, binding);
}

export default {
  wpilotRequest,
  executeWpilotAdapter,
  verifyWpilotBuild,
  countPluginFiles,
};
