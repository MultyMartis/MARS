/**
 * Phase 1B-D6D — kill switch parser (fail-closed).
 * Local non-secret runtime config. Missing/malformed → DISABLED-equivalent block.
 */

import { KILL_SWITCH_MODES } from './client-ops-d6d-constants.mjs';

const SECRET_KEY_RE =
  /(api[_-]?key|authorization|token|secret|password|webhook|telegram|n8n[_-]?key)/i;

/**
 * @param {unknown} raw
 * @param {{ site_id: string, producer_identity: string }} expected
 */
export function parseKillSwitch(raw, expected) {
  if (raw == null) {
    return {
      ok: false,
      mode: null,
      reason: 'KILL_SWITCH_MISSING',
      permits_evaluation: false,
      permits_activation: false,
      permits_request: false,
    };
  }
  if (typeof raw !== 'object' || Array.isArray(raw)) {
    return {
      ok: false,
      mode: null,
      reason: 'KILL_SWITCH_MALFORMED',
      permits_evaluation: false,
      permits_activation: false,
      permits_request: false,
    };
  }
  const obj = /** @type {Record<string, unknown>} */ (raw);
  for (const k of Object.keys(obj)) {
    if (SECRET_KEY_RE.test(k)) {
      return {
        ok: false,
        mode: null,
        reason: `KILL_SWITCH_SECRET_KEY_FORBIDDEN:${k}`,
        permits_evaluation: false,
        permits_activation: false,
        permits_request: false,
      };
    }
  }
  if (String(obj.site_id || '') !== expected.site_id) {
    return {
      ok: false,
      mode: null,
      reason: 'KILL_SWITCH_SITE_MISMATCH',
      permits_evaluation: false,
      permits_activation: false,
      permits_request: false,
    };
  }
  if (String(obj.producer_identity || '') !== expected.producer_identity) {
    return {
      ok: false,
      mode: null,
      reason: 'KILL_SWITCH_PRODUCER_MISMATCH',
      permits_evaluation: false,
      permits_activation: false,
      permits_request: false,
    };
  }
  const mode = String(obj.mode || '').toUpperCase();
  if (!Object.values(KILL_SWITCH_MODES).includes(mode)) {
    return {
      ok: false,
      mode: null,
      reason: 'KILL_SWITCH_MODE_UNKNOWN',
      permits_evaluation: false,
      permits_activation: false,
      permits_request: false,
    };
  }
  const operatorReason =
    typeof obj.operator_reason === 'string' ? obj.operator_reason : '';
  if (mode === KILL_SWITCH_MODES.DISABLED) {
    return {
      ok: true,
      mode,
      reason: operatorReason || 'KILL_SWITCH_DISABLED',
      permits_evaluation: true,
      permits_activation: false,
      permits_request: false,
    };
  }
  if (mode === KILL_SWITCH_MODES.DRY_RUN) {
    return {
      ok: true,
      mode,
      reason: operatorReason || 'KILL_SWITCH_DRY_RUN',
      permits_evaluation: true,
      permits_activation: false,
      permits_request: false,
    };
  }
  // ENABLED — still fails closed without charter/gates downstream
  return {
    ok: true,
    mode,
    reason: operatorReason || 'KILL_SWITCH_ENABLED',
    permits_evaluation: true,
    permits_activation: true, // subject to A/B/C/E gates
    permits_request: true, // subject to A/B/C/E gates
  };
}

export function killSwitchBlocksDelivery(parsed) {
  if (!parsed?.ok) return true;
  if (parsed.mode === KILL_SWITCH_MODES.DISABLED) return true;
  if (parsed.mode === KILL_SWITCH_MODES.DRY_RUN) return true;
  return false;
}
