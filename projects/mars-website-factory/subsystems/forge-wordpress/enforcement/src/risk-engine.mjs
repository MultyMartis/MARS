/**
 * FW-07C-0 — Forge risk engine.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { REASON_CODES as RC } from './reason-codes.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const RISK_POLICY_PATH = path.resolve(__dirname, '../policies/forge-risk-policy-v1.json');

let cachedPolicy = null;

export const VALID_RISK_CLASSES = Object.freeze(['R0', 'R1', 'R2', 'R3', 'R4', 'R5']);

export function loadRiskPolicy() {
  if (!cachedPolicy) {
    cachedPolicy = JSON.parse(fs.readFileSync(RISK_POLICY_PATH, 'utf8'));
  }
  return cachedPolicy;
}

export function resetRiskPolicyCache() {
  cachedPolicy = null;
}

export function isKnownRiskClass(riskClass) {
  return VALID_RISK_CLASSES.includes(riskClass);
}

export function getRiskRequirements(riskClass) {
  const policy = loadRiskPolicy();
  const entry = Object.values(policy.risk_classes).find((r) => r.risk_class === riskClass);
  return entry ?? null;
}

/**
 * Evaluate risk class admission for FW-07C-0 phase.
 */
export function evaluateRiskClass(riskClass, phase = 'FW-07C-0', context = {}) {
  const reason_codes = [];

  if (!isKnownRiskClass(riskClass)) {
    reason_codes.push(RC.FW_UNKNOWN_RISK_CLASS);
    return { allowed: false, reason_codes, requirements: null };
  }

  const requirements = getRiskRequirements(riskClass);
  const policy = loadRiskPolicy();
  const phaseDecision = policy.fw07c0_policy?.[riskClass];

  if (phase === 'FW-07C-0' && phaseDecision === 'DENY') {
    reason_codes.push(RC.FW_RISK_CLASS_DENIED);
    return { allowed: false, reason_codes, requirements };
  }

  if (requirements && !requirements.allowed_in_phase.includes(phase)) {
    reason_codes.push(RC.FW_OPERATION_PHASE_DENIED);
    return { allowed: false, reason_codes, requirements };
  }

  if (requirements?.dry_run_required && context.dry_run_status !== 'PASSED') {
    if (context.dry_run_status === 'UNKNOWN' || context.dry_run_status === 'PENDING') {
      reason_codes.push(RC.FW_DRY_RUN_REQUIRED);
    }
  }

  if (requirements?.snapshot_required && !context.snapshot_id) {
    reason_codes.push(RC.FW_SNAPSHOT_REQUIRED);
  }

  if (requirements?.operator_approval_required && !context.approval_id) {
    reason_codes.push(RC.FW_APPROVAL_REQUIRED);
  }

  return {
    allowed: reason_codes.length === 0,
    reason_codes,
    requirements,
  };
}

export default { evaluateRiskClass, getRiskRequirements, loadRiskPolicy };
