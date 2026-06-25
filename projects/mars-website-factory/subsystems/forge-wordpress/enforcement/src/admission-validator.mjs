/**
 * FW-07C-0 — Forge admission validator (fail-closed gate).
 */
import { validatePath } from './path-validator.mjs';
import { evaluateEnvironmentPolicy, isKnownEnvironment } from './scope-policy.mjs';
import { evaluateRiskClass, isKnownRiskClass } from './risk-engine.mjs';
import { validateOperationId, getOperationRegistry } from './operation-registry.mjs';
import { evaluateKillSwitch, DEFAULT_KILL_SWITCH_STATE } from './kill-switch.mjs';
import { buildAuditEvent } from './audit-event.mjs';
import { REASON_CODES as RC } from './reason-codes.mjs';

export const ADMISSION_PHASE = 'FW-07C-0';

const REQUEST_ALLOWED_FIELDS = new Set([
  'operation_id',
  'site_id',
  'environment',
  'raw_path',
  'allowed_root',
  'source_path',
  'destination_path',
  'disallow_root_mutation',
  'reparse_status',
  'runtime_binding_status',
  'dry_run_status',
  'snapshot_id',
  'approval_id',
  'kill_switch_state',
  'agent_id',
]);

const VALID_REPARSE_STATUS = new Set(['UNKNOWN', 'VERIFIED', 'NOT_REQUIRED', 'TEST_ONLY_SYNTHETIC_BINDING']);
const VALID_RUNTIME_BINDING = new Set(['UNBOUND', 'BOUND_NOT_IMPLEMENTED', 'PROVEN', 'TEST_ONLY_SYNTHETIC_BINDING']);

function collectUnknownFields(request) {
  if (!request || typeof request !== 'object') return [RC.FW_REQUEST_SCHEMA_INVALID];
  const unknown = Object.keys(request).filter((k) => !REQUEST_ALLOWED_FIELDS.has(k));
  return unknown.length ? [RC.FW_UNKNOWN_FIELD] : [];
}

/**
 * Validate admission request — fail-closed.
 * @param {object} request
 * @returns {object} admission result
 */
export function validateAdmission(request) {
  const reason_codes = [];
  const phase = ADMISSION_PHASE;

  reason_codes.push(...collectUnknownFields(request));

  if (!request?.site_id || String(request.site_id).trim() === '') {
    reason_codes.push(RC.FW_SITE_ID_MISSING);
  }

  if (!request?.operation_id) {
    reason_codes.push(RC.FW_OPERATION_UNKNOWN);
  }

  if (request?.environment && !isKnownEnvironment(request.environment)) {
    reason_codes.push(RC.FW_ENVIRONMENT_DENIED);
  }

  const killState = request?.kill_switch_state ?? DEFAULT_KILL_SWITCH_STATE;
  const opLookup = validateOperationId(request?.operation_id);
  let risk_class = opLookup.operation?.risk_class ?? '';

  if (!opLookup.known) {
    reason_codes.push(...opLookup.reason_codes);
  }

  if (risk_class && !isKnownRiskClass(risk_class)) {
    reason_codes.push(RC.FW_UNKNOWN_RISK_CLASS);
  }

  const killEval = evaluateKillSwitch(killState, risk_class || 'R0');
  if (!killEval.allowed) {
    reason_codes.push(...killEval.reason_codes);
  }

  if (request?.environment) {
    const envEval = evaluateEnvironmentPolicy(request.environment, risk_class || 'R0', phase);
    if (!envEval.allowed) {
      reason_codes.push(...envEval.reason_codes);
    }
  }

  if (risk_class) {
    const riskEval = evaluateRiskClass(risk_class, phase, {
      dry_run_status: request?.dry_run_status ?? 'UNKNOWN',
      snapshot_id: request?.snapshot_id,
      approval_id: request?.approval_id,
    });
    if (!riskEval.allowed) {
      reason_codes.push(...riskEval.reason_codes);
    }
  }

  const pathResult = validatePath({
    raw_path: request?.raw_path,
    allowed_root: request?.allowed_root,
    operation_id: request?.operation_id,
    site_id: request?.site_id,
    environment: request?.environment,
    source_path: request?.source_path,
    destination_path: request?.destination_path,
    disallow_root_mutation: request?.disallow_root_mutation ?? false,
  });

  if (!pathResult.allowed) {
    reason_codes.push(...pathResult.reason_codes);
  }

  const bindingStatus = request?.runtime_binding_status ?? 'UNBOUND';
  const op = opLookup.operation;
  const needsRuntimeBinding =
    op &&
    (op.filesystem_scope === 'RUNTIME_READ' ||
      op.filesystem_scope === 'MUTATION' ||
      op.environment_scope.some((e) => e.includes('RUNTIME')));

  if (needsRuntimeBinding) {
    if (!VALID_RUNTIME_BINDING.has(bindingStatus)) {
      reason_codes.push(RC.FW_RUNTIME_BINDING_MISSING);
    } else if (bindingStatus === 'UNBOUND' || bindingStatus === 'BOUND_NOT_IMPLEMENTED') {
      reason_codes.push(RC.FW_RUNTIME_BINDING_MISSING);
    }
  }

  const reparseStatus = request?.reparse_status ?? 'UNKNOWN';
  if (!VALID_REPARSE_STATUS.has(reparseStatus)) {
    reason_codes.push(RC.FW_REPARSE_STATUS_REQUIRED);
  } else if (pathResult.requires_reparse_check && reparseStatus === 'UNKNOWN') {
    reason_codes.push(RC.FW_REPARSE_STATUS_REQUIRED);
  }

  const uniqueReasons = [...new Set(reason_codes)];
  const admitted = uniqueReasons.length === 0;

  return {
    admitted,
    decision: admitted ? 'ADMIT' : 'DENY',
    reason_codes: uniqueReasons,
    operation_id: request?.operation_id ?? '',
    risk_class,
    phase,
    path_validation: pathResult,
  };
}

export function validateAdmissionWithAudit(request) {
  const result = validateAdmission(request);
  const audit = buildAuditEvent({
    ...request,
    normalized_path: result.path_validation?.normalized_path ?? '',
    risk_class: result.risk_class,
    validator_decision: result.decision,
    reason_codes: result.reason_codes,
    dry_run_status: request?.dry_run_status ?? 'UNKNOWN',
    execution_status: 'NOT_EXECUTED',
    rollback_status: 'NOT_APPLICABLE',
  });
  return { admission: result, audit };
}

export default validateAdmission;
