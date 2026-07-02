/**
 * V9-05C — Project runtime inspection chain (FP-0002 read-only admission).
 */
import { validateProjectAdmission } from './project-admission-validator.mjs';
import { resolveSiteAuthority } from './runtime-authority.mjs';
import { validateReparseBoundary } from './reparse-boundary-validator.mjs';
import { lookupBinding } from './runtime-binding-registry.mjs';
import { createAdmissionToken, validateAdmissionToken } from './admission-token.mjs';
import { captureBaseline } from './baseline-capture.mjs';
import { detectMutation } from './mutation-detector.mjs';
import { executeWpilotAdapter } from '../adapters/wpilot-readonly-adapter.mjs';
import { executeProjectFilesystemAdapter } from '../adapters/project-filesystem-readonly-adapter.mjs';
import { loadProjectAdmission } from './project-admission-registry.mjs';
import { RUNTIME_REASON_CODES as RC } from './runtime-reason-codes.mjs';

export const CHAIN_PHASE = 'V9-05C';
export const PROJECT_SITE_ID = 'fp-0002-shpigovsky';
export const PROJECT_ENVIRONMENT = 'LOCAL_PROJECT';

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
  if (request.site_id !== PROJECT_SITE_ID) {
    reason_codes.push(RC.RT_AUTHORITY_SITE_UNKNOWN);
  }
  if (request.environment !== PROJECT_ENVIRONMENT) {
    reason_codes.push(RC.RT_REQUEST_SCHEMA_INVALID);
  }
  return reason_codes;
}

async function executeAdapter(binding, allowed_root, token, request) {
  if (binding.adapter_type === 'wpilot') {
    return executeWpilotAdapter(binding.adapter_module, allowed_root, token, request, binding);
  }
  return executeProjectFilesystemAdapter(binding.adapter_module, allowed_root, token, request);
}

/**
 * Execute FP-0002 project read-only inspection chain.
 */
export async function executeProjectRuntimeInspection(request, options = {}) {
  const reason_codes = [];
  reason_codes.push(...validateRequestSchema(request));
  if (reason_codes.length) return deny(reason_codes);

  const admissionProfile = loadProjectAdmission(PROJECT_SITE_ID);
  if (!admissionProfile || admissionProfile.admission_mode !== 'READ_ONLY' || admissionProfile.write_authorized) {
    return deny([RC.RT_BINDING_REJECTED], { step: 'project_admission_profile' });
  }

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

  const kill_switch_state = request.kill_switch_state ?? 'SITE_ENABLED_READ_ONLY';

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

  const admission = validateProjectAdmission(admissionRequest);
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
    inspectionResult = await executeAdapter(bindingLookup.binding, allowed_root, token, {
      operation_id: request.operation_id,
      site_id: request.site_id,
      logical_target,
    });
  } catch (err) {
    return deny([err.code || RC.RT_BINDING_REJECTED], {
      step: 'adapter_execution',
      error: err.message,
      wpilot_code: err.wpilot_code,
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

  return {
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
}

export function isForbiddenWriteEndpoint(endpoint) {
  const forbidden = [
    'replace-text/dry-run',
    '/backups',
    'scoped-replace',
    '/rollback',
  ];
  return forbidden.some((f) => endpoint.includes(f));
}

export default executeProjectRuntimeInspection;
