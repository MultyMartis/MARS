/**
 * FW-07C-0 — Forge scope policy loader and environment evaluator.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { REASON_CODES as RC } from './reason-codes.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SCOPE_POLICY_PATH = path.resolve(__dirname, '../policies/forge-scope-policy-v1.json');

let cachedPolicy = null;

export function loadScopePolicy() {
  if (!cachedPolicy) {
    cachedPolicy = JSON.parse(fs.readFileSync(SCOPE_POLICY_PATH, 'utf8'));
  }
  return cachedPolicy;
}

export function resetScopePolicyCache() {
  cachedPolicy = null;
}

export const VALID_ENVIRONMENTS = Object.freeze([
  'LOCAL_SYNTHETIC',
  'LOCAL_PROJECT_RUNTIME',
  'REMOTE_DEV',
  'REMOTE_TEST',
  'REMOTE_PRODUCTION',
]);

export function isKnownEnvironment(environment) {
  return VALID_ENVIRONMENTS.includes(environment);
}

export function getRegisteredSite(siteId) {
  const policy = loadScopePolicy();
  return (policy.registered_synthetic_sites || []).find((s) => s.site_id === siteId) ?? null;
}

/**
 * Evaluate environment admission for a risk class in FW-07C-0.
 * @returns {{ allowed: boolean, reason_codes: string[] }}
 */
export function evaluateEnvironmentPolicy(environment, riskClass, phase = 'FW-07C-0') {
  const reason_codes = [];
  const policy = loadScopePolicy();

  if (!isKnownEnvironment(environment)) {
    reason_codes.push(RC.FW_ENVIRONMENT_DENIED);
    return { allowed: false, reason_codes };
  }

  const envPolicy = policy.environments[environment];
  if (!envPolicy) {
    reason_codes.push(RC.FW_ENVIRONMENT_DENIED);
    return { allowed: false, reason_codes };
  }

  if (envPolicy.admission_default === 'DENY') {
    reason_codes.push(RC.FW_ENVIRONMENT_DENIED);
    return { allowed: false, reason_codes };
  }

  const phasePolicy = policy.phase_execution_policy?.[phase];
  if (phasePolicy?.deny_risk_classes?.includes(riskClass)) {
    reason_codes.push(RC.FW_OPERATION_PHASE_DENIED);
    return { allowed: false, reason_codes };
  }

  if (!envPolicy.allowed_risk_classes.includes(riskClass)) {
    reason_codes.push(RC.FW_RISK_CLASS_DENIED);
    return { allowed: false, reason_codes };
  }

  return { allowed: true, reason_codes };
}

export default { loadScopePolicy, evaluateEnvironmentPolicy, getRegisteredSite };
