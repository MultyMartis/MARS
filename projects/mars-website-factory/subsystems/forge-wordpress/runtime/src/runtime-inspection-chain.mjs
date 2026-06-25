/**
 * FW-07C-1 — Runtime inspection execution chain (mandatory entrypoint).
 * operation request → enforcement gates → reparse → binding → token → adapter → result
 */
import { validateAdmission } from '../../enforcement/src/admission-validator.mjs';
import { DEFAULT_KILL_SWITCH_STATE } from '../../enforcement/src/kill-switch.mjs';
import { resolveSiteAuthority } from './runtime-authority.mjs';
import { validateReparseBoundary } from './reparse-boundary-validator.mjs';
import { lookupBinding } from './runtime-binding-registry.mjs';
import { createAdmissionToken, validateAdmissionToken } from './admission-token.mjs';
import { captureBaseline } from './baseline-capture.mjs';
import { detectMutation } from './mutation-detector.mjs';
import { executeBoundAdapter } from '../adapters/local-synthetic-readonly-adapter.mjs';
import { RUNTIME_REASON_CODES as RC } from './runtime-reason-codes.mjs';

export const CHAIN_PHASE = 'FW-07C-1';

const REQUEST_REQUIRED = ['operation_id', 'site_id', 'environment'];

function deny(reason_codes, context = {}) {
  return {
    success: false,
    decision: 'DENY',
    phase: CHAIN_PHASE,
    reason_codes: [...new Set(reason_codes)],
    ...context,
  };
}

function validateRequestSchema(request) {
  const reason_codes = [];
  if (!request || typeof request !== 'object') {
    reason_codes.push(RC.RT_REQUEST_SCHEMA_INVALID);
    return reason_codes;
  }
  for (const field of REQUEST_REQUIRED) {
    if (!request[field]) reason_codes.push(RC.RT_REQUEST_SCHEMA_INVALID);
  }
  if (request.environment !== 'LOCAL_SYNTHETIC') {
    reason_codes.push(RC.RT_REQUEST_SCHEMA_INVALID);
  }
  return reason_codes;
}

/**
 * Execute full runtime inspection chain — the ONLY supported public API.
 */
export function executeRuntimeInspection(request, options = {}) {
  const reason_codes = [];
  reason_codes.push(...validateRequestSchema(request));
  if (reason_codes.length) return deny(reason_codes);

  const authority = resolveSiteAuthority(request.site_id, request.allowed_root);
  if (!authority.valid) {
    return deny(authority.reason_codes, { step: 'runtime_authority' });
  }

  const allowed_root = authority.resolved_root;
  const logical_target = request.logical_target || request.raw_path || allowed_root;

  const bindingLookup = lookupBinding(request.operation_id, request.site_id);
  if (!bindingLookup.allowed) {
    return deny(bindingLookup.reason_codes, { step: 'runtime_binding', binding: bindingLookup.binding });
  }

  const reparse = validateReparseBoundary(logical_target, allowed_root);
  if (!reparse.allowed) {
    return deny(reparse.reason_codes.length ? reparse.reason_codes : [RC.RT_REPARSE_ESCAPE_DETECTED], {
      step: 'reparse_boundary',
      reparse,
    });
  }

  const kill_switch_state = request.kill_switch_state ?? DEFAULT_KILL_SWITCH_STATE;

  const admissionRequest = {
    operation_id: request.operation_id,
    site_id: request.site_id,
    environment: request.environment,
    raw_path: logical_target,
    allowed_root,
    kill_switch_state,
    reparse_status: 'VERIFIED',
    runtime_binding_status: 'PROVEN',
    dry_run_status: 'NOT_REQUIRED',
  };

  const admission = validateAdmission(admissionRequest);
  if (!admission.admitted) {
    return deny(admission.reason_codes, { step: 'fw07c0_admission', admission });
  }

  const token = createAdmissionToken({
    operation_id: request.operation_id,
    site_id: request.site_id,
    environment: request.environment,
    allowed_root,
    logical_target,
    physical_target: reparse.physical_path,
    risk_class: bindingLookup.binding.risk_class,
    runtime_binding_id: bindingLookup.binding.runtime_binding_id,
    reparse_verified: true,
    kill_switch_state,
    decision: 'ADMIT',
    binding_decision: bindingLookup.binding.binding_decision,
  });

  const tokenCheck = validateAdmissionToken(token, {
    operation_id: request.operation_id,
    site_id: request.site_id,
    logical_target,
  });
  if (!tokenCheck.valid) {
    return deny(tokenCheck.reason_codes, { step: 'admission_token' });
  }

  let baselineBefore = null;
  let baselineAfter = null;
  let mutation = null;

  if (options.capture_baseline !== false) {
    baselineBefore = captureBaseline(allowed_root);
  }

  let inspectionResult;
  try {
    inspectionResult = executeBoundAdapter(
      bindingLookup.binding.adapter_module,
      allowed_root,
      token,
      {
        operation_id: request.operation_id,
        site_id: request.site_id,
        logical_target,
      }
    );
  } catch (err) {
    return deny([err.code || RC.RT_BINDING_REJECTED], {
      step: 'adapter_execution',
      error: err.message,
    });
  }

  if (options.capture_baseline !== false) {
    baselineAfter = captureBaseline(allowed_root);
    mutation = detectMutation(baselineBefore, baselineAfter);
    if (!mutation.unchanged) {
      return deny(mutation.reason_codes, {
        step: 'mutation_detector',
        mutation,
        inspection_result: inspectionResult,
        emergency_stop: true,
      });
    }
  }

  const result = {
    success: true,
    decision: 'ADMIT',
    phase: CHAIN_PHASE,
    operation_id: request.operation_id,
    site_id: request.site_id,
    runtime_binding_id: bindingLookup.binding.runtime_binding_id,
    admission_token: {
      operation_id: token.operation_id,
      site_id: token.site_id,
      expires_at: token.expires_at,
      nonce: token.nonce,
      decision: token.decision,
    },
    reparse,
    inspection_result: inspectionResult,
    baseline_before: baselineBefore
      ? {
          file_count: baselineBefore.file_count,
          directory_count: baselineBefore.directory_count,
          aggregate_size: baselineBefore.aggregate_size,
          latest_modified_timestamp: baselineBefore.latest_modified_timestamp,
        }
      : null,
    baseline_after: baselineAfter
      ? {
          file_count: baselineAfter.file_count,
          directory_count: baselineAfter.directory_count,
          aggregate_size: baselineAfter.aggregate_size,
          latest_modified_timestamp: baselineAfter.latest_modified_timestamp,
        }
      : null,
    mutation_verdict: mutation?.verdict ?? 'NOT_CHECKED',
    read_only: true,
    no_write_verdict: mutation?.unchanged ?? true,
  };

  return result;
}

export default executeRuntimeInspection;
