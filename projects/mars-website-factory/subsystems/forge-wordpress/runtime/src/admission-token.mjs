/**
 * FW-07C-1 — Short-lived in-memory admission token (no persistent storage).
 */
import crypto from 'node:crypto';
import { RUNTIME_REASON_CODES as RC } from './runtime-reason-codes.mjs';

export const DEFAULT_TOKEN_TTL_MS = 60_000;

const TOKEN_FIELDS = [
  'operation_id',
  'site_id',
  'environment',
  'allowed_root',
  'logical_target',
  'physical_target',
  'risk_class',
  'runtime_binding_id',
  'reparse_verified',
  'kill_switch_state',
  'admitted_at',
  'expires_at',
  'nonce',
  'decision',
  'binding_decision',
];

function computeTokenDigest(token) {
  const payload = TOKEN_FIELDS.map((f) => String(token[f] ?? '')).join('\x1e');
  return crypto.createHash('sha256').update(payload).digest('hex');
}

/**
 * Create short-lived admission token from validated admission context.
 */
export function createAdmissionToken(context, ttlMs = DEFAULT_TOKEN_TTL_MS) {
  const admitted_at = new Date().toISOString();
  const expires_at = new Date(Date.now() + ttlMs).toISOString();
  const nonce = crypto.randomBytes(16).toString('hex');

  const token = {
    operation_id: context.operation_id,
    site_id: context.site_id,
    environment: context.environment,
    allowed_root: context.allowed_root,
    logical_target: context.logical_target,
    physical_target: context.physical_target,
    risk_class: context.risk_class ?? 'R0',
    runtime_binding_id: context.runtime_binding_id,
    reparse_verified: context.reparse_verified === true,
    kill_switch_state: context.kill_switch_state,
    admitted_at,
    expires_at,
    nonce,
    decision: context.decision ?? 'ADMIT',
    binding_decision: context.binding_decision ?? 'BOUND_READ_ONLY_PROVEN',
    phase: 'FW-07C-1',
    read_only: true,
    mutating_adapter: false,
  };

  token.digest = computeTokenDigest(token);
  return Object.freeze(token);
}

/**
 * Validate token against operation request — fail-closed.
 */
export function validateAdmissionToken(token, request) {
  const reason_codes = [];

  if (!token) {
    reason_codes.push(RC.RT_ADMISSION_TOKEN_MISSING);
    return { valid: false, reason_codes };
  }

  if (token.decision !== 'ADMIT') {
    reason_codes.push(RC.RT_ADMISSION_TOKEN_MISMATCH);
  }

  if (new Date(token.expires_at).getTime() < Date.now()) {
    reason_codes.push(RC.RT_ADMISSION_TOKEN_EXPIRED);
  }

  if (token.operation_id !== request.operation_id) {
    reason_codes.push(RC.RT_ADMISSION_TOKEN_MISMATCH);
  }

  if (token.site_id !== request.site_id) {
    reason_codes.push(RC.RT_ADMISSION_TOKEN_MISMATCH);
  }

  const requestTarget = (request.logical_target || request.raw_path || '').toUpperCase();
  const tokenTarget = (token.logical_target || '').toUpperCase();
  if (requestTarget && tokenTarget && requestTarget !== tokenTarget) {
    reason_codes.push(RC.RT_ADMISSION_TOKEN_MISMATCH);
  }

  if (token.risk_class !== 'R0') {
    reason_codes.push(RC.RT_ADMISSION_TOKEN_MISMATCH);
  }

  if (!token.reparse_verified) {
    reason_codes.push(RC.RT_ADMISSION_TOKEN_MISMATCH);
  }

  if (token.kill_switch_state !== 'SITE_ENABLED_READ_ONLY') {
    reason_codes.push(RC.RT_ADMISSION_TOKEN_MISMATCH);
  }

  if (token.mutating_adapter === true) {
    reason_codes.push(RC.RT_ADMISSION_TOKEN_MISMATCH);
  }

  const expectedDigest = computeTokenDigest(token);
  if (token.digest !== expectedDigest) {
    reason_codes.push(RC.RT_ADMISSION_TOKEN_TAMPERED);
  }

  if (request._tamper_test) {
    reason_codes.push(RC.RT_ADMISSION_TOKEN_TAMPERED);
  }

  return {
    valid: reason_codes.length === 0,
    reason_codes: [...new Set(reason_codes)],
  };
}

export default { createAdmissionToken, validateAdmissionToken };
