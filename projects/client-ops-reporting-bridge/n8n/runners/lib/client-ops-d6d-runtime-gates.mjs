/**
 * Phase 1B-D6D — future producer runtime / scheduler contract gates (offline).
 * Does not create or modify Task Scheduler tasks.
 */

import {
  FORBIDDEN_MAIN_ROOT,
  FUTURE_PRODUCER_RUNTIME,
  REQUIRED_ABC_E_ANCESTORS,
  EXIT_CODES,
  MAX_SAFE_CONCURRENCY,
  AUTOMATIC_RETRIES_ENABLED,
  MAX_AUTOMATIC_RETRIES,
} from './client-ops-d6d-constants.mjs';

/**
 * @param {object} runtime
 * @param {string} runtime.workingDirectory
 * @param {string} runtime.headCommit
 * @param {boolean} runtime.dirty
 * @param {string[]} [runtime.ancestorCommits]
 * @param {boolean} [runtime.secretsPresent]
 * @param {string} [runtime.killSwitchMode]
 * @param {boolean} [runtime.producerTaskRunning]
 * @param {boolean} [runtime.monitorTaskRunning]
 * @param {boolean} [runtime.artifactStable]
 */
export function evaluateRuntimeContract(runtime) {
  const reasons = [];
  const wd = String(runtime.workingDirectory || '').replace(/\//g, '\\');
  const main = FORBIDDEN_MAIN_ROOT.replace(/\//g, '\\');

  if (wd.toLowerCase() === main.toLowerCase() || wd.toLowerCase().startsWith(`${main.toLowerCase()}\\`)) {
    // Allow only if explicitly under STORAGE runtime — reject dirty MAIN as runtime root
    if (!wd.toLowerCase().includes('\\ai mars storage\\')) {
      reasons.push('DIRTY_MAIN_RUNTIME_FORBIDDEN');
    }
  }
  if (wd.toLowerCase() === 'x:\\ai mars' || wd.toLowerCase() === 'x:\\ai mars\\') {
    reasons.push('COMMAND_POINTS_AT_DIRTY_MAIN');
  }

  if (!runtime.headCommit || runtime.headCommit === 'unknown' || runtime.headCommit === 'unpinned') {
    reasons.push('RUNTIME_COMMIT_UNPINNED');
  }

  if (runtime.dirty) {
    reasons.push('RUNTIME_CHECKOUT_DIRTY');
  }

  const ancestors = runtime.ancestorCommits || [];
  for (const req of REQUIRED_ABC_E_ANCESTORS) {
    if (!ancestors.includes(req) && !ancestors.includes(req.slice(0, 7))) {
      // allow full match only
      if (!ancestors.some((a) => a === req)) {
        reasons.push(`MISSING_ANCESTOR:${req.slice(0, 8)}`);
      }
    }
  }

  if (runtime.producerTaskRunning) {
    reasons.push('PRODUCER_OVERLAP_REJECTED');
  }

  if (runtime.monitorTaskRunning && !runtime.artifactStable) {
    reasons.push('MONITOR_RUNNING_SOURCE_UNTRUSTED');
  }

  if (runtime.killSwitchMode === 'ENABLED' && runtime.secretsPresent === false) {
    reasons.push('SECRETS_MISSING_IN_ENABLED_MODE');
  }

  if (runtime.maxConcurrency != null && Number(runtime.maxConcurrency) > MAX_SAFE_CONCURRENCY) {
    reasons.push('CONCURRENCY_ABOVE_ONE');
  }

  if (runtime.automaticRetries === true || Number(runtime.maxAutomaticRetries || 0) > 0) {
    reasons.push('AUTOMATIC_RETRIES_NOT_ALLOWED');
  }

  const ok = reasons.length === 0;
  return {
    ok,
    reasons,
    dedicated_clean_runtime_required: true,
    future_runtime_path: FUTURE_PRODUCER_RUNTIME,
    automatic_retries_enabled: AUTOMATIC_RETRIES_ENABLED,
    max_automatic_retries: MAX_AUTOMATIC_RETRIES,
    max_safe_concurrency: MAX_SAFE_CONCURRENCY,
    exit_code: ok ? EXIT_CODES.SUCCESS_NO_CANDIDATE : EXIT_CODES.FAILED_RUNTIME_CONTRACT,
  };
}

export function describeFutureSchedulerContract() {
  return {
    task_name: 'MARS_SITE_002_Client_Ops_Producer',
    created: false,
    runtime_checkout: FUTURE_PRODUCER_RUNTIME,
    working_directory: FUTURE_PRODUCER_RUNTIME,
    proposed_command:
      'node n8n/runners/run-client-ops-d6d-unattended-producer.mjs --mode from-kill-switch',
    account_security_context: 'dedicated least-privilege Windows task account (credentials not invented)',
    start_condition: 'separate schedule after monitor window; MultipleInstances IgnoreNew',
    cadence: 'daily delayed after MARS_SITE_002_Post_1C_Catalog_Monitor (exact time TBD by operator charter)',
    overlap_policy: 'IgnoreNew; producer singleton lock; max concurrency 1',
    timeout_seconds: 600,
    exit_codes: 'see EXIT_CODES; nonzero is not retry-safe by default',
    logging: 'sanitized local receipt + run log under STORAGE state root',
    kill_switch: 'DISABLED|DRY_RUN|ENABLED; missing/malformed fail-closed',
    network_requirements: 'n8n control/webhook only when ENABLED + charter; DRY_RUN may GET-only if deployed',
    recovery_behavior: 'containment failure stops producer; no automatic reactivation',
    existing_monitor_scheduler_modified: false,
    relationship: 'C_SCAN_COMPLETED_ARTIFACTS_INDEPENDENTLY',
  };
}
