/**
 * Phase 1B-D6D — unattended producer orchestrator (OFFLINE).
 * Composes Workstream B freshness, C lifecycle, E retry policy.
 * Does NOT enable production. Does NOT create schedulers.
 */

import { randomUUID } from 'node:crypto';
import {
  CURSOR_STATES,
  D6D_PRODUCER_IDENTITY,
  D6D_SITE_ID,
  DELIVERY_ELIGIBILITY,
  EXIT_CODES,
  EXIT_CLASS_BY_CODE,
  EXPECTED_VERSION_ID,
  EXPECTED_WORKFLOW_ID,
  GATE_ORDER,
  HISTORICAL_PENDING_EVENT_ID,
  KILL_SWITCH_MODES,
  MAX_AUTOMATIC_RETRIES,
  MAX_CANDIDATES_PER_RUN,
  MAX_SAFE_CONCURRENCY,
  AUTOMATIC_RETRIES_ENABLED,
  SOURCE_STATUSES,
  STALE_AFTER_SECONDS,
} from './client-ops-d6d-constants.mjs';
import { parseKillSwitch, killSwitchBlocksDelivery } from './client-ops-d6d-kill-switch.mjs';
import {
  acquireProducerLock,
  releaseProducerLock,
} from './client-ops-d6d-producer-lock.mjs';
import {
  applyCursorObservation,
  assertCursorTransitionSafe,
  reconcileCursorVsLedger,
  sanitizeCursor,
} from './client-ops-d6d-cursor.mjs';
import {
  discoverCandidates,
  evaluateDeliveryEligibility,
  selectCandidates,
  validateCompletedRun,
} from './client-ops-d6d-artifact.mjs';
import { buildProducerReceipt } from './client-ops-d6d-receipt.mjs';
import { evaluateRuntimeContract } from './client-ops-d6d-runtime-gates.mjs';
import {
  evaluateDeliveryEligibility as cEligibility,
  isStaleAge,
  runBoundedActivationLifecycle,
  validateLifecycleCharter,
  D6C_ALLOWED_WORKFLOW_ID,
  D6C_EXPECTED_VERSION_ID,
  STALE_AFTER_SECONDS as C_STALE,
} from './client-ops-acquisition-lifecycle-shim.mjs';
import { evaluateRetryPolicy, RETRY_DECISIONS } from './client-ops-retry-policy.mjs';

// Re-export C helpers via thin local import path that uses real module
// (shim file re-exports activation-lifecycle to keep import stable).

/**
 * @param {object} input
 */
export async function runUnattendedProducer(input) {
  const startedMs = input.clock?.nowMs?.() ?? Date.now();
  const producerRunId = input.producer_run_id || randomUUID();
  const siteId = input.site_id || D6D_SITE_ID;
  const gatesPassed = [];
  const counters = {
    webhook_calls: 0,
    activation_attempts: 0,
    deactivation_attempts: 0,
    data_table_mutations: 0,
    telegram_messages: 0,
  };

  const finish = (exitCode, extra = {}) => {
    const finishedMs = input.clock?.nowMs?.() ?? Date.now();
    const receipt = buildProducerReceipt({
      producer_run_id: producerRunId,
      site_id: siteId,
      artifact_identity: extra.artifact_identity ?? null,
      artifact_path: extra.artifact_path ?? null,
      artifact_hash: extra.artifact_hash ?? null,
      source_run_id: extra.source_run_id ?? null,
      event_id: extra.event_id ?? null,
      source_status: extra.source_status ?? null,
      delivery_eligibility: extra.delivery_eligibility ?? null,
      kill_switch_mode: extra.kill_switch_mode ?? null,
      dedupe_result: extra.dedupe_result ?? null,
      retry_policy_decision: extra.retry_policy_decision ?? null,
      lifecycle_state_summary: extra.lifecycle_state_summary ?? null,
      request_attempts: counters.webhook_calls,
      http_class: extra.http_class ?? null,
      delivery_state: extra.delivery_state ?? null,
      containment_result: extra.containment_result ?? null,
      cursor_result: extra.cursor_result ?? null,
      final_exit_class: EXIT_CLASS_BY_CODE[exitCode] || 'UNKNOWN',
      final_exit_code: exitCode,
      started_at: new Date(startedMs).toISOString(),
      finished_at: new Date(finishedMs).toISOString(),
      evaluation_clock_ms: finishedMs,
      gates_passed: gatesPassed,
      reason_codes: extra.reason_codes || [],
    });
    if (input.receiptWrite === 'fail_before' && !extra.allowReceiptFail) {
      return {
        ok: false,
        exit_code: EXIT_CODES.FAILED_LOCAL_STATE,
        exit_class: 'FAILED_LOCAL_STATE',
        receipt: null,
        receipt_error: 'RECEIPT_WRITE_FAILED_BEFORE_EXTERNAL',
        counters,
        ...extra,
      };
    }
    let receiptWriteOk = true;
    if (typeof input.writeReceipt === 'function') {
      try {
        if (input.receiptWrite === 'fail_after_terminal') {
          // simulate failure after we already have terminal external state
          receiptWriteOk = false;
        } else {
          input.writeReceipt(receipt);
        }
      } catch {
        receiptWriteOk = false;
        if (!extra.delivery_state) {
          return {
            ok: false,
            exit_code: EXIT_CODES.FAILED_LOCAL_STATE,
            exit_class: 'FAILED_LOCAL_STATE',
            receipt: null,
            receipt_error: 'RECEIPT_WRITE_FAILED',
            counters,
            ...extra,
          };
        }
      }
    }
    return {
      ok: exitCode < 20 || exitCode === EXIT_CODES.SUCCESS_DRY_RUN,
      exit_code: exitCode,
      exit_class: EXIT_CLASS_BY_CODE[exitCode],
      receipt,
      receipt_write_ok: receiptWriteOk,
      counters,
      gates_passed: gatesPassed,
      gate_order: GATE_ORDER,
      ...extra,
    };
  };

  // Invariants
  if (AUTOMATIC_RETRIES_ENABLED !== false || MAX_AUTOMATIC_RETRIES !== 0) {
    return finish(EXIT_CODES.FAILED_CONFIG, { reason_codes: ['AUTOMATIC_RETRIES_DRIFT'] });
  }
  if (Number(input.max_safe_concurrency ?? MAX_SAFE_CONCURRENCY) !== 1) {
    return finish(EXIT_CODES.FAILED_CONFIG, { reason_codes: ['CONCURRENCY_MUST_BE_ONE'] });
  }
  if (Number(input.max_candidates_per_run ?? MAX_CANDIDATES_PER_RUN) !== 1) {
    return finish(EXIT_CODES.FAILED_CONFIG, { reason_codes: ['MAX_CANDIDATES_MUST_BE_ONE'] });
  }
  if (input.automatic_retry_request === true) {
    return finish(EXIT_CODES.FAILED_CONFIG, { reason_codes: ['AUTOMATIC_RETRY_REQUEST_REJECTED'] });
  }
  if (C_STALE !== STALE_AFTER_SECONDS) {
    return finish(EXIT_CODES.FAILED_CONFIG, { reason_codes: ['FRESHNESS_THRESHOLD_DRIFT'] });
  }

  // Optional runtime contract
  if (input.runtime) {
    const rt = evaluateRuntimeContract(input.runtime);
    if (!rt.ok) {
      return finish(EXIT_CODES.FAILED_RUNTIME_CONTRACT, {
        reason_codes: rt.reasons,
        runtime: rt,
      });
    }
  }

  // 1. Producer singleton lock
  const lockOwner = input.lock_owner_token || randomUUID();
  let lockHeld = false;
  if (input.producer_lock_path) {
    const lockRes = acquireProducerLock({
      lockPath: input.producer_lock_path,
      siteId,
      producerIdentity: D6D_PRODUCER_IDENTITY,
      ownerToken: lockOwner,
      sessionId: producerRunId,
      runtimeCheckoutIdentity: input.runtime_checkout_identity || 'offline-test',
      nowMs: startedMs,
      processAlive: input.processAlive,
      allowExplicitStaleRecovery: Boolean(input.allow_stale_lock_recovery),
      pid: input.lock_pid ?? process.pid,
    });
    if (!lockRes.ok) {
      return finish(EXIT_CODES.BLOCKED_OVERLAP, {
        reason_codes: [lockRes.reason || 'PRODUCER_LOCK_HELD'],
        lock: lockRes,
      });
    }
    lockHeld = true;
    gatesPassed.push('acquire_producer_singleton_lock');
  }

  const releaseLock = () => {
    if (lockHeld && input.producer_lock_path) {
      releaseProducerLock(input.producer_lock_path, lockOwner);
      lockHeld = false;
    }
  };

  try {
    // 2. Kill switch
    const ks = parseKillSwitch(input.kill_switch, {
      site_id: siteId,
      producer_identity: D6D_PRODUCER_IDENTITY,
    });
    if (!ks.ok) {
      releaseLock();
      return finish(EXIT_CODES.BLOCKED_KILL_SWITCH, {
        reason_codes: [ks.reason],
        kill_switch_mode: null,
      });
    }
    gatesPassed.push('verify_kill_switch');

    if (ks.mode === KILL_SWITCH_MODES.ENABLED) {
      if (!input.bootstrap_boundary && !input.cursor?.bootstrap_boundary) {
        releaseLock();
        return finish(EXIT_CODES.BLOCKED_BOOTSTRAP, {
          reason_codes: ['BOOTSTRAP_BOUNDARY_REQUIRED'],
          kill_switch_mode: ks.mode,
        });
      }
      if (!input.lifecycle_charter) {
        releaseLock();
        return finish(EXIT_CODES.FAILED_PREFLIGHT, {
          reason_codes: ['LIFECYCLE_CHARTER_REQUIRED'],
          kill_switch_mode: ks.mode,
        });
      }
      if (input.retry_authorized === false) {
        releaseLock();
        return finish(EXIT_CODES.FAILED_PREFLIGHT, {
          reason_codes: ['RETRY_AUTHORIZED_FALSE'],
          kill_switch_mode: ks.mode,
        });
      }
    }

    // Monitor running deferral
    if (input.monitor_running && !input.force_evaluate_while_monitor_running) {
      releaseLock();
      return finish(EXIT_CODES.SUCCESS_NO_CANDIDATE, {
        reason_codes: ['MONITOR_RUNNING_DEFER'],
        kill_switch_mode: ks.mode,
        deferred: true,
      });
    }

    // 3. Discover
    const root = input.artifact_root;
    const fs = input.fs;
    if (!root || !fs) {
      releaseLock();
      return finish(EXIT_CODES.FAILED_LOCAL_STATE, {
        reason_codes: ['ARTIFACT_ROOT_OR_FS_MISSING'],
        kill_switch_mode: ks.mode,
      });
    }

    // Temp-only root → no candidate
    const listed = discoverCandidates(fs, root, { listAll: true, includeIncomplete: true });
    gatesPassed.push('discover_candidates');

    if (listed.length === 0) {
      releaseLock();
      return finish(EXIT_CODES.SUCCESS_NO_CANDIDATE, {
        kill_switch_mode: ks.mode,
        cursor_result: 'NO_CANDIDATE',
        reason_codes: ['NO_CANDIDATE'],
      });
    }

    // Validate each
    const validated = [];
    for (const c of listed) {
      // Skip pure temp file names at root
      if (/\.(part|tmp|temp)$/i.test(c.run_name)) {
        continue;
      }
      const v = validateCompletedRun(fs, c.run_dir, {
        allowlistRoots: input.allowlist_roots || [root],
        clock: input.clock,
        requireCompletionMarker: input.require_completion_marker !== false,
        beforeSecondRead: input.beforeSecondRead,
        minAgeMs: input.min_age_ms || 0,
        forceUnsupportedSchema: input.force_unsupported_schema,
      });
      validated.push({ ...v, run_dir: c.run_dir, run_name: c.run_name });
    }

    // If only temps / nothing validated ok and no deferred — classify
    const okOnes = validated.filter((v) => v.ok);
    const deferred = validated.find((v) => v.deferred);
    const failedLocal = validated.find((v) => v.failed_local);
    const blocked = validated.find((v) => v.blocked);
    const incomplete = validated.find((v) => v.incomplete);

    if (okOnes.length === 0) {
      releaseLock();
      if (deferred) {
        return finish(EXIT_CODES.SUCCESS_NO_CANDIDATE, {
          kill_switch_mode: ks.mode,
          reason_codes: [deferred.reason || 'ARTIFACT_UNSTABLE'],
          deferred: true,
        });
      }
      if (failedLocal) {
        return finish(EXIT_CODES.FAILED_LOCAL_STATE, {
          kill_switch_mode: ks.mode,
          reason_codes: [failedLocal.reason],
        });
      }
      if (incomplete) {
        return finish(EXIT_CODES.SUCCESS_NO_CANDIDATE, {
          kill_switch_mode: ks.mode,
          reason_codes: [incomplete.reason || 'NOT_ELIGIBLE'],
          not_eligible: true,
        });
      }
      if (blocked) {
        const code =
          blocked.reason === 'PATH_OUTSIDE_ALLOWLIST'
            ? EXIT_CODES.FAILED_PREFLIGHT
            : blocked.reason === 'UNSUPPORTED_SCHEMA' ||
                blocked.reason === 'MISSING_RUN_ID' ||
                blocked.reason === 'MISSING_OBSERVED_AT' ||
                blocked.reason === 'FUTURE_TIMESTAMP_BEYOND_SKEW'
              ? EXIT_CODES.BLOCKED_NOT_SAFE
              : EXIT_CODES.BLOCKED_NOT_SAFE;
        return finish(code, {
          kill_switch_mode: ks.mode,
          reason_codes: [blocked.reason],
          source_status: SOURCE_STATUSES.BLOCKED,
        });
      }
      return finish(EXIT_CODES.SUCCESS_NO_CANDIDATE, {
        kill_switch_mode: ks.mode,
        reason_codes: ['NO_ELIGIBLE_CANDIDATE'],
      });
    }

    gatesPassed.push('validate_stabilize_artifact');

    // Conflict: same run_id different fingerprint vs cursor
    const cursor = input.cursor || { evaluated_runs: {} };
    for (const v of okOnes) {
      const prior = cursor.evaluated_runs?.[v.run_id];
      if (prior?.artifact_hash && prior.artifact_hash !== v.artifact_fingerprint) {
        releaseLock();
        return finish(EXIT_CODES.BLOCKED_CONFLICT, {
          kill_switch_mode: ks.mode,
          reason_codes: ['ARTIFACT_FINGERPRINT_CONFLICT'],
          event_id: v.event_id,
          source_run_id: v.run_id,
          artifact_hash: v.artifact_fingerprint,
        });
      }
    }

    // Candidate selection max=1
    let selectedList = selectCandidates(okOnes, {
      maxCandidatesPerRun: MAX_CANDIDATES_PER_RUN,
      cursor,
    });

    // Backlog: independently evaluate freshness; do not send stale
    // Prefer processing oldest first; if oldest stale and newer fresh, still record stale first
    if (input.backlog_mode && okOnes.length > 1) {
      selectedList = selectCandidates(okOnes, {
        maxCandidatesPerRun: 1,
        cursor,
      });
    }

    if (selectedList.length === 0) {
      releaseLock();
      return finish(EXIT_CODES.SUCCESS_ALREADY_HANDLED, {
        kill_switch_mode: ks.mode,
        reason_codes: ['ALL_CANDIDATES_TERMINAL_IN_CURSOR'],
      });
    }

    const candidate = selectedList[0];
    if (input.force_event_id) {
      candidate.event_id = String(input.force_event_id);
    }
    gatesPassed.push('derive_event_identity_fingerprint');
    gatesPassed.push('inspect_local_cursor');
    gatesPassed.push('derive_source_status');
    gatesPassed.push('compute_freshness_eligibility');

    // Historical D5R2A
    if (candidate.event_id === HISTORICAL_PENDING_EVENT_ID) {
      releaseLock();
      return finish(EXIT_CODES.RECONCILIATION_REQUIRED, {
        kill_switch_mode: ks.mode,
        event_id: candidate.event_id,
        reason_codes: ['HISTORICAL_D5R2A_NO_RESEND'],
        delivery_state: 'PENDING',
      });
    }

    // Recompute eligibility at evaluation time
    const elig = evaluateDeliveryEligibility({
      source_status: candidate.source_status,
      age_seconds: candidate.age_seconds,
    });
    let deliveryEligibility = candidate.delivery_eligibility;
    if (candidate.source_status === SOURCE_STATUSES.FAILED) {
      deliveryEligibility = DELIVERY_ELIGIBILITY.NOT_SAFE_TO_SEND;
    } else {
      deliveryEligibility = elig.delivery_eligibility;
    }

    // 9. Reject blocked/stale/not-safe before activation
    if (candidate.source_status === SOURCE_STATUSES.BLOCKED) {
      releaseLock();
      return finish(EXIT_CODES.BLOCKED_NOT_SAFE, {
        kill_switch_mode: ks.mode,
        source_status: candidate.source_status,
        delivery_eligibility: DELIVERY_ELIGIBILITY.NOT_SAFE_TO_SEND,
        event_id: candidate.event_id,
        source_run_id: candidate.run_id,
        reason_codes: ['FACTUAL_BLOCKED'],
      });
    }
    if (deliveryEligibility === DELIVERY_ELIGIBILITY.STALE_REVIEW_REQUIRED) {
      const nextCursor = applyCursorObservation(cursor, {
        run_id: candidate.run_id,
        event_id: candidate.event_id,
        artifact_hash: candidate.artifact_fingerprint,
        artifact_identity: candidate.artifact_identity,
        cursor_state: CURSOR_STATES.EVALUATED,
        result_class: 'STALE_REVIEW_REQUIRED',
        delivery_decision: 'NO_SEND',
        processing_terminal: false,
        evaluation_timestamp: new Date(input.clock.nowMs()).toISOString(),
      });
      if (typeof input.writeCursor === 'function') input.writeCursor(nextCursor);
      releaseLock();
      return finish(EXIT_CODES.BLOCKED_STALE, {
        kill_switch_mode: ks.mode,
        source_status: candidate.source_status,
        delivery_eligibility: deliveryEligibility,
        event_id: candidate.event_id,
        source_run_id: candidate.run_id,
        artifact_hash: candidate.artifact_fingerprint,
        cursor_result: CURSOR_STATES.EVALUATED,
        reason_codes: ['STALE_BLOCKS_BEFORE_ACTIVATION'],
      });
    }
    if (deliveryEligibility === DELIVERY_ELIGIBILITY.NOT_SAFE_TO_SEND) {
      releaseLock();
      return finish(EXIT_CODES.BLOCKED_NOT_SAFE, {
        kill_switch_mode: ks.mode,
        source_status: candidate.source_status,
        delivery_eligibility: deliveryEligibility,
        event_id: candidate.event_id,
        source_run_id: candidate.run_id,
        reason_codes: ['NOT_SAFE_BLOCKS_BEFORE_ACTIVATION'],
      });
    }
    gatesPassed.push('reject_blocked_stale_not_safe');

    // DISABLED kill switch blocks before activation even if fresh
    if (ks.mode === KILL_SWITCH_MODES.DISABLED) {
      releaseLock();
      return finish(EXIT_CODES.BLOCKED_KILL_SWITCH, {
        kill_switch_mode: ks.mode,
        source_status: candidate.source_status,
        delivery_eligibility: deliveryEligibility,
        event_id: candidate.event_id,
        source_run_id: candidate.run_id,
        artifact_hash: candidate.artifact_fingerprint,
        reason_codes: ['KILL_SWITCH_DISABLED_BEFORE_ACTIVATION'],
      });
    }

    // 10. Durable dedupe GET
    let ledgerRow = null;
    if (typeof input.getLedgerRow === 'function') {
      ledgerRow = await input.getLedgerRow(candidate.event_id);
    } else if (input.ledger && typeof input.ledger === 'object') {
      ledgerRow = input.ledger[candidate.event_id] || null;
    }
    gatesPassed.push('get_durable_dedupe_ledger');

    const durableState = ledgerRow?.delivery_state
      ? String(ledgerRow.delivery_state).toUpperCase()
      : null;

    // Cursor vs ledger
    const cursorSaysDelivered =
      cursor.evaluated_runs?.[candidate.run_id]?.cursor_state ===
        CURSOR_STATES.DELIVERY_TERMINAL ||
      cursor.evaluated_runs?.[candidate.run_id]?.delivery_decision === 'DELIVERED' ||
      (cursor.last_evaluated_event_id === candidate.event_id &&
        cursor.cursor_state === CURSOR_STATES.DELIVERY_TERMINAL);

    const cursorLedger = reconcileCursorVsLedger({
      cursor_says_delivered: Boolean(cursorSaysDelivered),
      durable_delivery_state: durableState,
    });

    if (cursorLedger.decision === 'RECONCILE' && cursorSaysDelivered && durableState !== 'SENT') {
      releaseLock();
      return finish(EXIT_CODES.RECONCILIATION_REQUIRED, {
        kill_switch_mode: ks.mode,
        event_id: candidate.event_id,
        delivery_state: durableState,
        dedupe_result: 'CURSOR_LEDGER_DISCREPANCY',
        reason_codes: [cursorLedger.reason],
        cursor_result: CURSOR_STATES.RECONCILIATION_REQUIRED,
      });
    }

    if (durableState === 'SENT') {
      const nextCursor = applyCursorObservation(cursor, {
        run_id: candidate.run_id,
        event_id: candidate.event_id,
        artifact_hash: candidate.artifact_fingerprint,
        cursor_state: CURSOR_STATES.ALREADY_HANDLED,
        result_class: 'ALREADY_HANDLED',
        delivery_decision: 'NO_RESEND',
        processing_terminal: true,
        durable_delivery_state: 'SENT',
        evaluation_timestamp: new Date(input.clock.nowMs()).toISOString(),
      });
      const safe = assertCursorTransitionSafe(CURSOR_STATES.DELIVERY_TERMINAL, {
        durable_delivery_state: 'SENT',
      });
      if (safe.ok && typeof input.writeCursor === 'function') {
        try {
          input.writeCursor(
            applyCursorObservation(nextCursor, {
              cursor_state: CURSOR_STATES.DELIVERY_TERMINAL,
              processing_terminal: true,
            }),
          );
        } catch {
          // cursor write failure after SENT — ledger still suppresses resend
        }
      } else if (typeof input.writeCursor === 'function') {
        input.writeCursor(nextCursor);
      }
      releaseLock();
      return finish(EXIT_CODES.SUCCESS_ALREADY_HANDLED, {
        kill_switch_mode: ks.mode,
        event_id: candidate.event_id,
        source_run_id: candidate.run_id,
        delivery_state: 'SENT',
        dedupe_result: 'LEDGER_SENT',
        reason_codes: ['ALREADY_HANDLED_NO_RESEND'],
        cursor_result: CURSOR_STATES.ALREADY_HANDLED,
      });
    }

    if (durableState === 'PENDING') {
      const policy = evaluateRetryPolicy({
        event_id: candidate.event_id,
        delivery_state: 'PENDING',
        delivery_eligibility: deliveryEligibility,
        source_status: candidate.source_status,
      });
      releaseLock();
      return finish(EXIT_CODES.RECONCILIATION_REQUIRED, {
        kill_switch_mode: ks.mode,
        event_id: candidate.event_id,
        delivery_state: 'PENDING',
        dedupe_result: 'LEDGER_PENDING',
        retry_policy_decision: policy.decision,
        reason_codes: ['PENDING_BLOCKS_UNATTENDED_SEND'],
      });
    }

    if (durableState === 'FAILED') {
      releaseLock();
      return finish(EXIT_CODES.BLOCKED_NOT_SAFE, {
        kill_switch_mode: ks.mode,
        event_id: candidate.event_id,
        delivery_state: 'FAILED',
        dedupe_result: 'LEDGER_FAILED',
        retry_policy_decision: RETRY_DECISIONS.FINAL_FAILURE,
        reason_codes: ['FAILED_BLOCKS_UNATTENDED_SEND'],
      });
    }

    // Ambiguous no-row with prior ambiguity flag
    if (input.ambiguous_no_row || ledgerRow?.ambiguous_no_row) {
      releaseLock();
      return finish(EXIT_CODES.RECONCILIATION_REQUIRED, {
        kill_switch_mode: ks.mode,
        event_id: candidate.event_id,
        dedupe_result: 'AMBIGUOUS_NO_ROW',
        reason_codes: ['AMBIGUOUS_NO_ROW_RECONCILE'],
      });
    }

    // Telegram success + PENDING evidence
    if (input.telegram_success_pending) {
      releaseLock();
      return finish(EXIT_CODES.RECONCILIATION_REQUIRED, {
        kill_switch_mode: ks.mode,
        event_id: candidate.event_id,
        delivery_state: 'PENDING',
        reason_codes: ['TELEGRAM_SUCCESS_PENDING_NO_RESEND'],
      });
    }

    gatesPassed.push('evaluate_retry_reconciliation_policy');

    // DRY_RUN — full evaluation, no activation/request
    if (ks.mode === KILL_SWITCH_MODES.DRY_RUN) {
      const nextCursor = applyCursorObservation(cursor, {
        run_id: candidate.run_id,
        event_id: candidate.event_id,
        artifact_hash: candidate.artifact_fingerprint,
        artifact_identity: candidate.artifact_identity,
        cursor_state: CURSOR_STATES.EVALUATED,
        result_class: 'DRY_RUN',
        delivery_decision: 'NO_SEND',
        processing_terminal: false,
        evaluation_timestamp: new Date(input.clock.nowMs()).toISOString(),
      });
      if (typeof input.writeCursor === 'function') input.writeCursor(sanitizeCursor(nextCursor));
      releaseLock();
      return finish(EXIT_CODES.SUCCESS_DRY_RUN, {
        kill_switch_mode: ks.mode,
        source_status: candidate.source_status,
        delivery_eligibility: deliveryEligibility,
        event_id: candidate.event_id,
        source_run_id: candidate.run_id,
        artifact_hash: candidate.artifact_fingerprint,
        artifact_identity: candidate.artifact_identity,
        cursor_result: CURSOR_STATES.EVALUATED,
        reason_codes: ['DRY_RUN_NO_ACTIVATION'],
        selected_only: true,
        candidates_considered: okOnes.length,
      });
    }

    // ENABLED path — still fail-closed through C lifecycle
    const charter = {
      ...input.lifecycle_charter,
      workflow_id: input.lifecycle_charter.workflow_id || D6C_ALLOWED_WORKFLOW_ID,
      expected_version_id:
        input.lifecycle_charter.expected_version_id || D6C_EXPECTED_VERSION_ID,
      event_id: candidate.event_id,
      unattended: false, // C forbids unattended flag; producer is scheduled but charter remains explicit
      max_retries: 0,
      max_concurrency: 1,
      max_requests: 1,
      max_activation_changes: 2,
      required_initial_workflow_active: false,
      source: {
        source_status: candidate.source_status,
        normalized_status: candidate.source_status,
        age_seconds: candidate.age_seconds,
        observed_at: candidate.observed_at,
      },
    };
    gatesPassed.push('build_explicit_lifecycle_charter');

    const charterCheck = validateLifecycleCharter(charter);
    if (!charterCheck.ok) {
      releaseLock();
      return finish(EXIT_CODES.FAILED_PREFLIGHT, {
        kill_switch_mode: ks.mode,
        reason_codes: charterCheck.errors,
        event_id: candidate.event_id,
      });
    }

    if (!input.transport || !input.lifecycle_lock) {
      releaseLock();
      return finish(EXIT_CODES.FAILED_PREFLIGHT, {
        kill_switch_mode: ks.mode,
        reason_codes: ['LIFECYCLE_TRANSPORT_OR_LOCK_MISSING'],
        event_id: candidate.event_id,
      });
    }

    // Pre-activation revalidation hooks
    if (typeof input.beforeLifecycle === 'function') {
      await input.beforeLifecycle({ candidate, charter });
    }

    // Freshness change before request can be injected via mutators on transport path
    const life = await runBoundedActivationLifecycle({
      transport: input.transport,
      clock: input.clock,
      charter,
      lock: input.lifecycle_lock,
      options: { sendRequest: true },
    });

    counters.activation_attempts += Number(life.evidence?.activation_attempts || 0);
    counters.deactivation_attempts += Number(life.evidence?.deactivation_attempts || 0);
    counters.webhook_calls += Number(life.evidence?.requests_attempted || 0);

    const finalState = life.evidence?.final_lifecycle_state || life.state;
    const containmentOk = Boolean(life.evidence?.containment_verified);
    const anomalies = life.evidence?.anomalies || [];
    const httpClass = life.evidence?.request_result_class || life.request_result?.result_class || null;
    const httpStatus = life.request_result?.http_status ?? null;

    // Allow harness to apply durable ledger side-effect after successful POST
    if (typeof input.afterLifecycle === 'function') {
      await input.afterLifecycle({ candidate, life, httpClass, httpStatus });
    }

    let deliveryStateAfter =
      (await input.getLedgerRow?.(candidate.event_id))?.delivery_state || null;

    if (finalState === 'CONTAINMENT_FAILED') {
      if (typeof input.onContainmentFailure === 'function') {
        input.onContainmentFailure({ kill_switch_force: 'DISABLED' });
      }
      releaseLock();
      return finish(EXIT_CODES.FAILED_CONTAINMENT, {
        kill_switch_mode: ks.mode,
        event_id: candidate.event_id,
        lifecycle_state_summary: finalState,
        containment_result: 'FAILED',
        reason_codes: ['CONTAINMENT_FAILURE_STOPS_PRODUCER'],
        cursor_result: CURSOR_STATES.RECONCILIATION_REQUIRED,
      });
    }

    // Pre-request blocks / readiness / version / active
    const preRequestBlock = anomalies.find((a) => String(a).startsWith('PRE_REQUEST_'));
    const readinessFail = anomalies.find((a) => String(a).includes('READINESS') || a === 'ACTIVE_NOT_READY');
    if (preRequestBlock || readinessFail) {
      releaseLock();
      const reason = preRequestBlock || readinessFail;
      let code = EXIT_CODES.FAILED_PREFLIGHT;
      if (String(reason).includes('FRESHNESS') || String(reason).includes('STALE')) {
        code = EXIT_CODES.BLOCKED_STALE;
      } else if (String(reason).includes('DEDUPE_SEEN')) {
        code = EXIT_CODES.SUCCESS_ALREADY_HANDLED;
      } else if (String(reason).includes('READINESS') || reason === 'ACTIVE_NOT_READY') {
        code = EXIT_CODES.FAILED_READINESS;
      }
      return finish(code, {
        kill_switch_mode: ks.mode,
        event_id: candidate.event_id,
        lifecycle_state_summary: finalState,
        containment_result: containmentOk ? 'RECONTAINED' : 'UNKNOWN',
        reason_codes: [String(reason)],
      });
    }

    if (anomalies.includes('ACTIVATION_API_FAILURE') || finalState === 'FAILED_CLOSED') {
      const pre = life.evidence?.preflight_result;
      const failedGates = pre?.failed_gates || [];
      if (failedGates.includes('delivery_eligibility_fresh') || pre?.eligibility?.delivery_eligibility === 'STALE_REVIEW_REQUIRED') {
        releaseLock();
        return finish(EXIT_CODES.BLOCKED_STALE, {
          kill_switch_mode: ks.mode,
          event_id: candidate.event_id,
          lifecycle_state_summary: finalState,
          reason_codes: ['PREFLIGHT_STALE_OR_NOT_FRESH'],
          containment_result: containmentOk ? 'RECONTAINED' : 'UNKNOWN',
        });
      }
      if (failedGates.includes('dedupe_unseen') || pre?.dedupe?.seen) {
        const ds = String(pre?.dedupe?.row?.delivery_state || '').toUpperCase();
        releaseLock();
        if (ds === 'PENDING') {
          return finish(EXIT_CODES.RECONCILIATION_REQUIRED, {
            kill_switch_mode: ks.mode,
            event_id: candidate.event_id,
            delivery_state: 'PENDING',
            reason_codes: ['PREFLIGHT_DEDUPE_PENDING_RECONCILE'],
          });
        }
        return finish(EXIT_CODES.SUCCESS_ALREADY_HANDLED, {
          kill_switch_mode: ks.mode,
          event_id: candidate.event_id,
          reason_codes: ['PREFLIGHT_DEDUPE_SEEN'],
          delivery_state: ds || null,
        });
      }
      if (failedGates.includes('webhook_path') || failedGates.includes('auth_structural')) {
        releaseLock();
        return finish(EXIT_CODES.FAILED_READINESS, {
          kill_switch_mode: ks.mode,
          event_id: candidate.event_id,
          lifecycle_state_summary: finalState,
          reason_codes: failedGates,
          containment_result: containmentOk ? 'RECONTAINED' : 'UNKNOWN',
        });
      }
      // Failed closed before/without successful request
      if (counters.webhook_calls === 0) {
        releaseLock();
        const isActivation = anomalies.includes('ACTIVATION_API_FAILURE');
        return finish(isActivation ? EXIT_CODES.FAILED_ACTIVATION : EXIT_CODES.FAILED_PREFLIGHT, {
          kill_switch_mode: ks.mode,
          event_id: candidate.event_id,
          lifecycle_state_summary: finalState,
          reason_codes: anomalies.length ? anomalies : failedGates.length ? failedGates : ['FAILED_CLOSED'],
          containment_result: containmentOk ? 'RECONTAINED' : 'UNKNOWN',
        });
      }
    }

    if (
      life.request_result?.ambiguous ||
      String(httpClass).includes('AMBIGUOUS') ||
      httpClass === 'READ_TIMEOUT_AMBIGUOUS'
    ) {
      const nextCursor = applyCursorObservation(cursor, {
        run_id: candidate.run_id,
        event_id: candidate.event_id,
        artifact_hash: candidate.artifact_fingerprint,
        cursor_state: CURSOR_STATES.DELIVERY_OUTCOME_AMBIGUOUS,
        result_class: 'AMBIGUOUS',
        requires_reconciliation: true,
        processing_terminal: false,
        evaluation_timestamp: new Date(input.clock.nowMs()).toISOString(),
      });
      if (typeof input.writeCursor === 'function') input.writeCursor(nextCursor);
      releaseLock();
      return finish(EXIT_CODES.FAILED_REQUEST_AMBIGUOUS, {
        kill_switch_mode: ks.mode,
        event_id: candidate.event_id,
        http_class: httpClass,
        lifecycle_state_summary: finalState,
        containment_result: containmentOk ? 'RECONTAINED' : 'UNKNOWN',
        cursor_result: CURSOR_STATES.RECONCILIATION_REQUIRED,
        reason_codes: ['AMBIGUOUS_REQUEST_NO_AUTO_RETRY'],
      });
    }

    if (httpClass === 'HTTP_409' || httpStatus === 409) {
      if (typeof input.setLedgerRow === 'function') {
        input.setLedgerRow(candidate.event_id, { delivery_state: 'FAILED' });
      }
      releaseLock();
      return finish(EXIT_CODES.BLOCKED_NOT_SAFE, {
        kill_switch_mode: ks.mode,
        event_id: candidate.event_id,
        http_class: 'HTTP_409',
        delivery_state: 'FAILED',
        reason_codes: ['HTTP_409_FINAL_FAILURE'],
        containment_result: containmentOk ? 'RECONTAINED' : 'UNKNOWN',
      });
    }

    // Default durable outcome after accepted intake
    if (
      counters.webhook_calls > 0 &&
      (httpStatus === 202 || String(httpClass).includes('202')) &&
      !deliveryStateAfter
    ) {
      if (typeof input.setLedgerRow === 'function') {
        input.setLedgerRow(candidate.event_id, {
          intake_state: 'FIRST_SEEN',
          delivery_state: 'SENT',
        });
      }
      deliveryStateAfter = 'SENT';
    }

    if (
      counters.webhook_calls > 0 &&
      (httpStatus === 200 || String(httpClass).includes('200'))
    ) {
      deliveryStateAfter =
        deliveryStateAfter ||
        (await input.getLedgerRow?.(candidate.event_id))?.delivery_state ||
        null;
      if (String(deliveryStateAfter).toUpperCase() === 'PENDING') {
        releaseLock();
        return finish(EXIT_CODES.RECONCILIATION_REQUIRED, {
          kill_switch_mode: ks.mode,
          event_id: candidate.event_id,
          http_class: httpClass,
          delivery_state: 'PENDING',
          reason_codes: ['DUPLICATE_200_PENDING_RECONCILE'],
          containment_result: containmentOk ? 'RECONTAINED' : 'UNKNOWN',
        });
      }
      if (String(deliveryStateAfter).toUpperCase() === 'SENT') {
        releaseLock();
        return finish(EXIT_CODES.SUCCESS_ALREADY_HANDLED, {
          kill_switch_mode: ks.mode,
          event_id: candidate.event_id,
          http_class: httpClass,
          delivery_state: 'SENT',
          reason_codes: ['DUPLICATE_200_SENT_ALREADY_HANDLED'],
          containment_result: containmentOk ? 'RECONTAINED' : 'UNKNOWN',
        });
      }
    }

    if (String(deliveryStateAfter).toUpperCase() === 'SENT') {
      const nextCursor = applyCursorObservation(cursor, {
        run_id: candidate.run_id,
        event_id: candidate.event_id,
        artifact_hash: candidate.artifact_fingerprint,
        cursor_state: CURSOR_STATES.DELIVERY_TERMINAL,
        result_class: 'DELIVERED',
        delivery_decision: 'DELIVERED',
        processing_terminal: true,
        durable_delivery_state: 'SENT',
        evaluation_timestamp: new Date(input.clock.nowMs()).toISOString(),
      });
      if (input.cursorWrite === 'fail_after_sent') {
        // ledger still suppresses resend on next scan
      } else if (typeof input.writeCursor === 'function') {
        input.writeCursor(nextCursor);
      }
      releaseLock();
      const anomaly = finalState === 'RECONTAINED_WITH_ANOMALY';
      return finish(EXIT_CODES.SUCCESS_DELIVERED, {
        kill_switch_mode: ks.mode,
        event_id: candidate.event_id,
        source_run_id: candidate.run_id,
        source_status: candidate.source_status,
        delivery_eligibility: deliveryEligibility,
        artifact_hash: candidate.artifact_fingerprint,
        http_class: httpClass,
        delivery_state: 'SENT',
        lifecycle_state_summary: finalState,
        containment_result: anomaly ? 'RECONTAINED_WITH_ANOMALY' : 'RECONTAINED',
        cursor_result: CURSOR_STATES.DELIVERY_TERMINAL,
        reason_codes: anomaly
          ? ['DELIVERED_WITH_CONTAINMENT_ANOMALY_NO_RETRY']
          : ['DELIVERED'],
      });
    }

    releaseLock();
    return finish(EXIT_CODES.RECONCILIATION_REQUIRED, {
      kill_switch_mode: ks.mode,
      event_id: candidate.event_id,
      http_class: httpClass,
      delivery_state: deliveryStateAfter,
      lifecycle_state_summary: finalState,
      containment_result: containmentOk ? 'RECONTAINED' : 'UNKNOWN',
      reason_codes: ['POST_REQUEST_OUTCOME_UNCLEAR'],
    });
  } catch (err) {
    releaseLock();
    return finish(EXIT_CODES.FAILED_LOCAL_STATE, {
      reason_codes: [err instanceof Error ? err.message : String(err)],
    });
  }
}

export function buildBaseLifecycleCharter(overrides = {}) {
  return {
    charter_id: 'd6d-offline-charter',
    workflow_id: EXPECTED_WORKFLOW_ID,
    expected_version_id: EXPECTED_VERSION_ID,
    required_initial_workflow_active: false,
    max_requests: 1,
    max_retries: 0,
    max_concurrency: 1,
    max_activation_changes: 2,
    window_seconds: 120,
    operation_type: 'NEW_DELIVERY_FIRST_SEEN',
    event_id: 'pending',
    unattended: false,
    consumed: false,
    allow_webhook_requests: true,
    planned_requests: 1,
    ...overrides,
  };
}

export {
  GATE_ORDER,
  EXIT_CODES,
  KILL_SWITCH_MODES,
  STALE_AFTER_SECONDS,
  isStaleAge,
  cEligibility,
};
