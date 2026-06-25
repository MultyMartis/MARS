/**
 * FW-07C-0 — Forge audit event builder (no runtime write).
 */
const SECRET_FIELD_PATTERN = /password|token|secret|credential|private_key|api_key|auth_header/i;
const ENV_VAR_PATTERN = /^env_|^process\.env/i;

const FORBIDDEN_FIELDS = new Set([
  'password',
  'token',
  'secret',
  'credential',
  'private_key',
  'api_key',
  'access_token',
  'refresh_token',
  'raw_env',
  'environment_variables',
]);

/**
 * Mask or drop secret-like fields from input.
 */
export function sanitizeAuditInput(input) {
  if (!input || typeof input !== 'object') return {};
  const out = {};
  for (const [key, value] of Object.entries(input)) {
    const lowerKey = key.toLowerCase();
    if (FORBIDDEN_FIELDS.has(lowerKey) || SECRET_FIELD_PATTERN.test(key) || ENV_VAR_PATTERN.test(key)) {
      out[key] = '[REDACTED]';
      continue;
    }
    if (value && typeof value === 'object' && !Array.isArray(value)) {
      out[key] = sanitizeAuditInput(value);
    } else {
      out[key] = value;
    }
  }
  return out;
}

/**
 * Build a safe audit event object without writing to disk.
 */
export function buildAuditEvent(input) {
  const sanitized = sanitizeAuditInput(input);
  const now = new Date().toISOString();

  return {
    timestamp: sanitized.timestamp ?? now,
    agent_id: sanitized.agent_id ?? 'AG-WP-001',
    operation_id: sanitized.operation_id ?? '',
    site_id: sanitized.site_id ?? '',
    environment: sanitized.environment ?? '',
    raw_path: sanitized.raw_path ?? '',
    normalized_path: sanitized.normalized_path ?? '',
    risk_class: sanitized.risk_class ?? '',
    validator_decision: sanitized.validator_decision ?? 'DENY',
    reason_codes: Array.isArray(sanitized.reason_codes) ? [...sanitized.reason_codes] : [],
    dry_run_status: sanitized.dry_run_status ?? 'UNKNOWN',
    snapshot_id: sanitized.snapshot_id ?? null,
    approval_id: sanitized.approval_id ?? null,
    execution_status: sanitized.execution_status ?? 'NOT_EXECUTED',
    rollback_status: sanitized.rollback_status ?? 'NOT_APPLICABLE',
  };
}

export function containsRedactedFields(event) {
  return JSON.stringify(event).includes('[REDACTED]');
}

export default { buildAuditEvent, sanitizeAuditInput };
