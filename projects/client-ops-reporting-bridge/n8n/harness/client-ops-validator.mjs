/**
 * MARS Client Ops Bridge — offline / Code@2-compatible validation library.
 *
 * Pure JavaScript. No network. No secret values emitted in responses.
 * Suitable for Node harness and for embedding into n8n Code@2 nodes.
 *
 * AUTH: MVP compares request header token to an injected expectedSecret
 * string. Live credential/env binding remains HITL_REQUIRED — do not invent
 * n8n env access syntax here.
 */

export const WORKFLOW_NAME = 'MARS Client Ops Bridge — bzpm.ru';
export const SCHEMA_NAME = 'mars.client_ops.report';
export const SCHEMA_MAJOR = 1;
export const EVENT_TYPE = 'site.post_1c_monitor';
export const SITE_ID = 'SITE-002';
export const SITE_DOMAIN = 'bzpm.ru';
export const MAX_PAYLOAD_BYTES = 256 * 1024;
export const AUTH_HEADER = 'x-mars-client-ops-token';
export const AUTH_PLACEHOLDER = '<<<HITL_REQUIRED:CLIENT_OPS_WEBHOOK_AUTH_SECRET>>>';
/** Clearly synthetic harness-only secret — never a production credential. */
export const SYNTHETIC_HARNESS_SECRET =
  'SYNTHETIC_CLIENT_OPS_HARNESS_SECRET_v1_NOT_A_REAL_CREDENTIAL';

export const ALLOWED_STATUSES = new Set(['OK', 'ATTENTION', 'FAILED', 'BLOCKED']);

export const REQUIRED_TOP_LEVEL = [
  'schema_name',
  'schema_version',
  'event_id',
  'event_type',
  'generated_at',
  'observed_at',
  'environment',
  'site',
  'producer',
  'run',
  'action',
  'metrics',
  'freshness',
  'security',
];

export const METRIC_KEYS = [
  'baseline_count',
  'current_count',
  'added_urls',
  'removed_urls',
  'onboarding_needed_count',
];

export const FORBIDDEN_TOP_LEVEL_KEYS = new Set([
  'delivery',
  'ai',
  'routing',
  'telegram',
  'chat_id',
  'bot_token',
  'webhook',
  'credentials',
  'secret',
  'secrets',
  'password',
  'token',
  'api_key',
  'openrouter',
  'atlas',
  'source_path',
  'absolute_path',
  'storage_path',
]);

const RE_WINDOWS_ABS = /[A-Za-z]:\\/;
const RE_UNC = /\\\\[^\s\\/]+\\/;
const RE_URI_CREDS = /[a-zA-Z][a-zA-Z0-9+.-]*:\/\/[^/\s]*:[^/\s]*@/;
const RE_TOKENISH =
  /(\b(api[_-]?key|bot[_-]?token|access[_-]?token|secret[_-]?key|bearer\s+[A-Za-z0-9\-._~+/]+=*)\b|\b\d{8,10}:[A-Za-z0-9_-]{30,}\b)/i;
const RE_STACK = /^(Traceback \(most recent call last\):|\s+File ".+", line \d+)/m;
const RE_PRIVATE_KEY = /-----BEGIN (RSA |OPENSSH )?PRIVATE KEY-----/i;
const RE_UUID =
  /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;

/**
 * @param {unknown} headers
 * @returns {Record<string, string>}
 */
export function normalizeHeaders(headers) {
  const out = {};
  if (!headers || typeof headers !== 'object') return out;
  for (const [key, value] of Object.entries(headers)) {
    if (value === undefined || value === null) continue;
    out[String(key).toLowerCase()] = Array.isArray(value)
      ? String(value[0] ?? '')
      : String(value);
  }
  return out;
}

/**
 * @param {Record<string, string>} headers
 * @returns {{ ok: boolean, code?: string }}
 */
export function validateContentType(headers) {
  const raw = headers['content-type'] || '';
  const base = raw.split(';')[0].trim().toLowerCase();
  if (base !== 'application/json') {
    return { ok: false, code: 'UNSUPPORTED_MEDIA_TYPE' };
  }
  return { ok: true };
}

/**
 * Auth interface only. Does not leak secrets.
 * @param {Record<string, string>} headers
 * @param {string} expectedSecret
 * @returns {{ ok: boolean, code?: string }}
 */
export function validateAuthInterface(headers, expectedSecret) {
  if (
    !expectedSecret ||
    expectedSecret === AUTH_PLACEHOLDER ||
    expectedSecret.includes('HITL_REQUIRED')
  ) {
    return { ok: false, code: 'AUTH_BINDING_UNRESOLVED' };
  }
  const headerToken = (headers[AUTH_HEADER] || '').trim();
  const auth = (headers.authorization || '').trim();
  let presented = headerToken;
  if (!presented && /^Bearer\s+/i.test(auth)) {
    presented = auth.replace(/^Bearer\s+/i, '').trim();
  }
  if (!presented) {
    return { ok: false, code: 'UNAUTHORIZED' };
  }
  if (presented !== expectedSecret) {
    return { ok: false, code: 'UNAUTHORIZED' };
  }
  return { ok: true };
}

/**
 * @param {unknown} envelope
 * @returns {{ ok: boolean, code?: string, field?: string }}
 */
export function validateEnvelopeShape(envelope) {
  if (!envelope || typeof envelope !== 'object' || Array.isArray(envelope)) {
    return { ok: false, code: 'INVALID_SCHEMA', field: '(root)' };
  }
  for (const key of REQUIRED_TOP_LEVEL) {
    if (!(key in envelope)) {
      return { ok: false, code: 'INVALID_SCHEMA', field: key };
    }
  }
  for (const key of Object.keys(envelope)) {
    if (FORBIDDEN_TOP_LEVEL_KEYS.has(String(key).toLowerCase())) {
      return { ok: false, code: 'SECURITY_REJECTED', field: key };
    }
  }
  return { ok: true };
}

/**
 * @param {unknown} version
 * @returns {{ ok: boolean, code?: string }}
 */
export function validateSchemaVersion(version) {
  if (typeof version !== 'string' || !/^\d+\.\d+$/.test(version)) {
    return { ok: false, code: 'INVALID_SCHEMA' };
  }
  const major = Number(version.split('.')[0]);
  if (major !== SCHEMA_MAJOR) {
    return { ok: false, code: 'INVALID_SCHEMA' };
  }
  return { ok: true };
}

/**
 * @param {unknown} status
 * @returns {{ ok: boolean, code?: string }}
 */
export function validateAllowedStatus(status) {
  if (typeof status !== 'string' || !ALLOWED_STATUSES.has(status)) {
    return { ok: false, code: 'INVALID_SCHEMA' };
  }
  return { ok: true };
}

/**
 * @param {unknown} security
 * @returns {{ ok: boolean, code?: string, field?: string }}
 */
export function validateSecurityFlags(security) {
  if (!security || typeof security !== 'object') {
    return { ok: false, code: 'SECURITY_REJECTED', field: 'security' };
  }
  if (security.contains_secrets !== false) {
    return {
      ok: false,
      code: 'SECURITY_REJECTED',
      field: 'security.contains_secrets',
    };
  }
  if (security.redacted !== true) {
    return {
      ok: false,
      code: 'SECURITY_REJECTED',
      field: 'security.redacted',
    };
  }
  return { ok: true };
}

/**
 * @param {unknown} eventId
 * @returns {{ ok: boolean, code?: string }}
 */
export function validateEventId(eventId) {
  if (typeof eventId !== 'string' || !RE_UUID.test(eventId)) {
    return { ok: false, code: 'INVALID_SCHEMA' };
  }
  return { ok: true };
}

/**
 * @param {string} text
 * @param {number} [maxLen]
 */
export function redactForDiagnostics(text, maxLen = 80) {
  let cleaned = String(text);
  cleaned = cleaned.replace(RE_WINDOWS_ABS, '<REDACTED_PATH>');
  cleaned = cleaned.replace(RE_UNC, '<REDACTED_UNC>');
  cleaned = cleaned.replace(RE_URI_CREDS, '<REDACTED_URI>');
  cleaned = cleaned.replace(RE_TOKENISH, '<REDACTED_TOKEN>');
  if (cleaned.length > maxLen) return `${cleaned.slice(0, maxLen - 3)}...`;
  return cleaned;
}

/**
 * @param {unknown} value
 * @param {string} [prefix]
 * @returns {Iterable<[string, string]>}
 */
function* iterStrings(value, prefix = '') {
  if (typeof value === 'string') {
    yield [prefix, value];
  } else if (value && typeof value === 'object' && !Array.isArray(value)) {
    for (const [key, child] of Object.entries(value)) {
      const path = prefix ? `${prefix}.${key}` : String(key);
      yield* iterStrings(child, path);
    }
  } else if (Array.isArray(value)) {
    for (let i = 0; i < value.length; i += 1) {
      yield* iterStrings(value[i], `${prefix}[${i}]`);
    }
  }
}

/**
 * @param {unknown} envelope
 * @returns {{ ok: boolean, code?: string, field?: string, diagnostic?: string }}
 */
export function scanUnsafeStrings(envelope) {
  for (const [path, text] of iterStrings(envelope)) {
    if (RE_WINDOWS_ABS.test(text) || RE_UNC.test(text)) {
      return {
        ok: false,
        code: 'SECURITY_REJECTED',
        field: path,
        diagnostic: 'path_pattern',
      };
    }
    if (RE_URI_CREDS.test(text)) {
      return {
        ok: false,
        code: 'SECURITY_REJECTED',
        field: path,
        diagnostic: 'uri_credentials',
      };
    }
    if (RE_TOKENISH.test(text)) {
      return {
        ok: false,
        code: 'SECURITY_REJECTED',
        field: path,
        diagnostic: 'token_like',
      };
    }
    if (RE_STACK.test(text) || RE_PRIVATE_KEY.test(text)) {
      return {
        ok: false,
        code: 'SECURITY_REJECTED',
        field: path,
        diagnostic: 'raw_secret_or_stack',
      };
    }
  }
  return { ok: true };
}

/**
 * @param {string} [eventId]
 * @param {'NEW'|'DEFERRED_SANDBOX'|'DUPLICATE'} [dedupe]
 */
export function buildAcceptedResponse(eventId, dedupe = 'DEFERRED_SANDBOX') {
  return {
    ok: true,
    result: 'ACCEPTED',
    event_id: eventId || null,
    workflow: WORKFLOW_NAME,
    dedupe,
  };
}

/**
 * @param {string} code
 * @param {string} [eventId]
 */
export function buildRejectedResponse(code, eventId) {
  const body = {
    ok: false,
    result: code === 'INTERNAL_ERROR' ? 'ERROR' : 'REJECTED',
    code,
  };
  if (eventId) body.event_id = eventId;
  return body;
}

/**
 * @param {string} eventId
 */
export function buildDuplicateResponse(eventId) {
  return {
    ok: true,
    result: 'DUPLICATE',
    event_id: eventId,
  };
}

function isNonNegInt(value) {
  return typeof value === 'number' && Number.isInteger(value) && value >= 0;
}

function parseableTimestamp(value) {
  if (typeof value !== 'string' || !value.trim()) return false;
  const t = Date.parse(value);
  return Number.isFinite(t);
}

/**
 * Full envelope business validation (already-normalized envelope only).
 * @param {unknown} envelope
 * @returns {{ ok: boolean, code?: string, field?: string, diagnostic?: string }}
 */
export function validateBusinessEnvelope(envelope) {
  const shape = validateEnvelopeShape(envelope);
  if (!shape.ok) return shape;

  const env = /** @type {Record<string, any>} */ (envelope);

  if (env.schema_name !== SCHEMA_NAME) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'schema_name' };
  }

  const ver = validateSchemaVersion(env.schema_version);
  if (!ver.ok) return { ...ver, field: 'schema_version' };

  if (env.event_type !== EVENT_TYPE) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'event_type' };
  }

  const eid = validateEventId(env.event_id);
  if (!eid.ok) return { ...eid, field: 'event_id' };

  if (!parseableTimestamp(env.generated_at)) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'generated_at' };
  }
  if (!parseableTimestamp(env.observed_at)) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'observed_at' };
  }

  if (!env.site || typeof env.site !== 'object') {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'site' };
  }
  if (env.site.site_id !== SITE_ID) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'site.site_id' };
  }
  if (env.site.domain !== SITE_DOMAIN) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'site.domain' };
  }
  if (typeof env.site.site_name !== 'string' || !env.site.site_name.trim()) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'site.site_name' };
  }

  if (!env.producer || typeof env.producer !== 'object') {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'producer' };
  }
  if (typeof env.producer.name !== 'string' || !env.producer.name.trim()) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'producer.name' };
  }
  if (typeof env.producer.version !== 'string' || !env.producer.version.trim()) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'producer.version' };
  }

  if (!env.run || typeof env.run !== 'object') {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'run' };
  }
  if (typeof env.run.run_id !== 'string' || !env.run.run_id.trim()) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'run.run_id' };
  }
  const status = validateAllowedStatus(env.run.normalized_status);
  if (!status.ok) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'run.normalized_status' };
  }
  if (typeof env.run.source_status !== 'string' || !env.run.source_status.trim()) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'run.source_status' };
  }
  if (typeof env.run.summary_code !== 'string' || !env.run.summary_code.trim()) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'run.summary_code' };
  }
  if (!Array.isArray(env.run.reason_codes)) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'run.reason_codes' };
  }

  if (!env.action || typeof env.action !== 'object') {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'action' };
  }
  if (typeof env.action.required !== 'boolean') {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'action.required' };
  }
  if (typeof env.action.code !== 'string' || !env.action.code.trim()) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'action.code' };
  }
  if (typeof env.action.text !== 'string') {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'action.text' };
  }

  if (!env.metrics || typeof env.metrics !== 'object') {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'metrics' };
  }
  for (const key of METRIC_KEYS) {
    const val = env.metrics[key];
    if (typeof val === 'boolean' || !isNonNegInt(val)) {
      return { ok: false, code: 'INVALID_SCHEMA', field: `metrics.${key}` };
    }
  }

  if (!env.freshness || typeof env.freshness !== 'object') {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'freshness' };
  }
  if (!isNonNegInt(env.freshness.age_seconds)) {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'freshness.age_seconds' };
  }
  if (typeof env.freshness.stale !== 'boolean') {
    return { ok: false, code: 'INVALID_SCHEMA', field: 'freshness.stale' };
  }

  const flags = validateSecurityFlags(env.security);
  if (!flags.ok) return flags;

  const unsafe = scanUnsafeStrings(env);
  if (!unsafe.ok) return unsafe;

  return { ok: true };
}

/**
 * Dedupe sandbox decision: deferred — never claims durable uniqueness.
 * @returns {{ mode: 'DEFERRED_SANDBOX', result: 'ACCEPTED', dedupe: 'DEFERRED_SANDBOX' }}
 */
export function decideDedupeSandbox() {
  return {
    mode: 'DEFERRED_SANDBOX',
    result: 'ACCEPTED',
    dedupe: 'DEFERRED_SANDBOX',
  };
}

/**
 * HTTP status mapping for frozen response contract.
 * @param {string} result
 * @param {string} [code]
 */
export function httpStatusFor(result, code) {
  if (result === 'ACCEPTED') return 202;
  if (result === 'DUPLICATE') return 200;
  if (code === 'UNAUTHORIZED') return 401;
  if (code === 'UNSUPPORTED_MEDIA_TYPE') return 415;
  if (code === 'PAYLOAD_TOO_LARGE') return 413;
  if (code === 'SECURITY_REJECTED') return 400;
  if (code === 'INVALID_SCHEMA') return 400;
  if (code === 'INTERNAL_ERROR') return 500;
  return 400;
}

/**
 * Full request processing pipeline for harness / Code@2.
 *
 * @param {{
 *   headers?: unknown,
 *   body?: unknown,
 *   rawBodyBytes?: number,
 *   expectedSecret?: string,
 *   forceDuplicateDeferredResponse?: boolean,
 * }} input
 */
export function processClientOpsRequest(input) {
  try {
    const headers = normalizeHeaders(input.headers || {});
    const expectedSecret =
      input.expectedSecret === undefined
        ? SYNTHETIC_HARNESS_SECRET
        : input.expectedSecret;

    const ct = validateContentType(headers);
    if (!ct.ok) {
      const code = ct.code || 'UNSUPPORTED_MEDIA_TYPE';
      return {
        http_status: httpStatusFor('REJECTED', code),
        response: buildRejectedResponse(code),
        evidence: { gate: 'content_type', code },
      };
    }

    const size = Number(input.rawBodyBytes || 0);
    if (Number.isFinite(size) && size > MAX_PAYLOAD_BYTES) {
      return {
        http_status: 413,
        response: buildRejectedResponse('PAYLOAD_TOO_LARGE'),
        evidence: { gate: 'size', code: 'PAYLOAD_TOO_LARGE' },
      };
    }

    const auth = validateAuthInterface(headers, expectedSecret);
    if (!auth.ok) {
      const code = auth.code === 'AUTH_BINDING_UNRESOLVED' ? 'UNAUTHORIZED' : auth.code;
      return {
        http_status: httpStatusFor('REJECTED', code),
        response: buildRejectedResponse(code),
        evidence: {
          gate: 'auth',
          code: auth.code,
          note:
            auth.code === 'AUTH_BINDING_UNRESOLVED'
              ? 'HITL_REQUIRED_AUTH_BINDING'
              : undefined,
        },
      };
    }

    const body = input.body;
    if (!body || typeof body !== 'object' || Array.isArray(body)) {
      return {
        http_status: 400,
        response: buildRejectedResponse('INVALID_SCHEMA'),
        evidence: { gate: 'payload_shape', code: 'INVALID_SCHEMA' },
      };
    }

    const business = validateBusinessEnvelope(body);
    if (!business.ok) {
      const code = business.code || 'INVALID_SCHEMA';
      return {
        http_status: httpStatusFor('REJECTED', code),
        response: buildRejectedResponse(code),
        evidence: {
          gate: 'business',
          code,
          field: business.field || null,
          diagnostic: business.diagnostic || null,
        },
      };
    }

    const eventId = String(body.event_id);

    if (input.forceDuplicateDeferredResponse) {
      return {
        http_status: 200,
        response: {
          ok: true,
          result: 'DUPLICATE',
          event_id: eventId,
          dedupe: 'DEFERRED_SANDBOX',
          note: 'DEDUPE_NOT_ENABLED_SANDBOX',
        },
        evidence: {
          gate: 'dedupe',
          code: 'DEDUPE_NOT_ENABLED_SANDBOX',
          event_id: eventId,
        },
      };
    }

    const dedupe = decideDedupeSandbox();
    return {
      http_status: httpStatusFor('ACCEPTED'),
      response: buildAcceptedResponse(eventId, dedupe.dedupe),
      evidence: {
        gate: 'accepted',
        code: 'ACCEPTED',
        event_id: eventId,
        dedupe: dedupe.dedupe,
        note: 'DEDUPE_NOT_ENABLED_SANDBOX',
      },
    };
  } catch {
    return {
      http_status: 500,
      response: buildRejectedResponse('INTERNAL_ERROR'),
      evidence: { gate: 'internal', code: 'INTERNAL_ERROR' },
    };
  }
}
