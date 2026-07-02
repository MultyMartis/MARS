/**
 * V9-05C — Project admission validator (binding-registry as operation source of truth).
 */
import { validatePath } from '../../enforcement/src/path-validator.mjs';
import { evaluateEnvironmentPolicy } from '../../enforcement/src/scope-policy.mjs';
import { evaluateKillSwitch } from '../../enforcement/src/kill-switch.mjs';
import { REASON_CODES as RC } from '../../enforcement/src/reason-codes.mjs';
import { lookupBinding } from './runtime-binding-registry.mjs';

export const PROJECT_ADMISSION_PHASE = 'V9-05C';

const VALID_REPARSE_STATUS = new Set(['VERIFIED', 'NOT_REQUIRED']);
const VALID_RUNTIME_BINDING = new Set(['PROVEN']);

export function validateProjectAdmission(request) {
  const reason_codes = [];
  const phase = PROJECT_ADMISSION_PHASE;

  if (!request?.site_id) {
    reason_codes.push(RC.FW_SITE_ID_MISSING);
  }

  if (!request?.operation_id) {
    reason_codes.push(RC.FW_OPERATION_UNKNOWN);
  }

  const bindingLookup = lookupBinding(request?.operation_id, request?.site_id);
  if (!bindingLookup.found || !bindingLookup.allowed) {
    reason_codes.push(RC.FW_OPERATION_UNKNOWN);
  }

  const risk_class = bindingLookup.binding?.risk_class ?? 'R0';

  const killEval = evaluateKillSwitch(request?.kill_switch_state ?? 'SITE_ENABLED_READ_ONLY', risk_class);
  if (!killEval.allowed) {
    reason_codes.push(...killEval.reason_codes);
  }

  if (request?.environment) {
    const envEval = evaluateEnvironmentPolicy(request.environment, risk_class, 'FW-07C-0');
    if (!envEval.allowed) {
      reason_codes.push(...envEval.reason_codes);
    }
  }

  const pathResult = validatePath({
    raw_path: request?.raw_path,
    allowed_root: request?.allowed_root,
    operation_id: request?.operation_id,
    site_id: request?.site_id,
    environment: request?.environment,
    disallow_root_mutation: false,
  });

  if (!pathResult.allowed) {
    reason_codes.push(...pathResult.reason_codes);
  }

  const bindingStatus = request?.runtime_binding_status ?? 'UNBOUND';
  if (!VALID_RUNTIME_BINDING.has(bindingStatus)) {
    reason_codes.push(RC.FW_RUNTIME_BINDING_MISSING);
  }

  const reparseStatus = request?.reparse_status ?? 'UNKNOWN';
  if (!VALID_REPARSE_STATUS.has(reparseStatus)) {
    reason_codes.push(RC.FW_REPARSE_STATUS_REQUIRED);
  }

  const uniqueReasons = [...new Set(reason_codes)];
  return {
    admitted: uniqueReasons.length === 0,
    decision: uniqueReasons.length === 0 ? 'ADMIT' : 'DENY',
    reason_codes: uniqueReasons,
    operation_id: request?.operation_id ?? '',
    risk_class,
    phase,
    path_validation: pathResult,
  };
}

export default validateProjectAdmission;
