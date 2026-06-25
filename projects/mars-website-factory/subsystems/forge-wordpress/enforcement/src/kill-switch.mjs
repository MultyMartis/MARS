/**
 * FW-07C-0 — Forge kill switch state evaluator (repo-only, pure function).
 */
import { REASON_CODES as RC } from './reason-codes.mjs';

export const KILL_SWITCH_STATES = Object.freeze([
  'GLOBAL_DISABLED',
  'SITE_DISABLED',
  'SITE_ENABLED_READ_ONLY',
  'EMERGENCY_STOP',
]);

export const DEFAULT_KILL_SWITCH_STATE = 'GLOBAL_DISABLED';

/**
 * Evaluate kill switch for admission.
 * @param {string} state
 * @param {string} riskClass
 * @returns {{ allowed: boolean, reason_codes: string[], state: string }}
 */
export function evaluateKillSwitch(state = DEFAULT_KILL_SWITCH_STATE, riskClass = 'R0') {
  const reason_codes = [];
  const effectiveState = state || DEFAULT_KILL_SWITCH_STATE;

  if (!KILL_SWITCH_STATES.includes(effectiveState)) {
    reason_codes.push(RC.FW_KILL_SWITCH_DISABLED);
    return { allowed: false, reason_codes, state: effectiveState };
  }

  switch (effectiveState) {
    case 'GLOBAL_DISABLED':
      reason_codes.push(RC.FW_KILL_SWITCH_DISABLED);
      return { allowed: false, reason_codes, state: effectiveState };

    case 'SITE_DISABLED':
      reason_codes.push(RC.FW_KILL_SWITCH_DISABLED);
      return { allowed: false, reason_codes, state: effectiveState };

    case 'EMERGENCY_STOP':
      reason_codes.push(RC.FW_KILL_SWITCH_EMERGENCY);
      return { allowed: false, reason_codes, state: effectiveState };

    case 'SITE_ENABLED_READ_ONLY':
      if (riskClass !== 'R0') {
        reason_codes.push(RC.FW_RISK_CLASS_DENIED);
        return { allowed: false, reason_codes, state: effectiveState };
      }
      return { allowed: true, reason_codes, state: effectiveState };

    default:
      reason_codes.push(RC.FW_KILL_SWITCH_DISABLED);
      return { allowed: false, reason_codes, state: effectiveState };
  }
}

export function createKillSwitchState(state = DEFAULT_KILL_SWITCH_STATE, siteId = '') {
  return {
    state,
    site_id: siteId,
    phase: 'FW-07C-0',
    evaluated_at: new Date().toISOString(),
    notes: 'Repo-only evaluator; no runtime lock files',
  };
}

export default { evaluateKillSwitch, createKillSwitchState, DEFAULT_KILL_SWITCH_STATE };
