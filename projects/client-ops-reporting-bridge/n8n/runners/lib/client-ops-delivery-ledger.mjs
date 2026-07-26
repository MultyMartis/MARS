/**
 * Phase 1B-D6A — durable post-Telegram delivery ledger (offline pure logic).
 * No network. No secrets. No production mutation.
 *
 * Separates delivery_state from intake_state / event_status.
 */

export const DELIVERY_STATES = Object.freeze(['PENDING', 'SENT', 'FAILED']);

export const DELIVERY_STATE = Object.freeze({
  PENDING: 'PENDING',
  SENT: 'SENT',
  FAILED: 'FAILED',
});

/** Fields the finalizer must never mutate. */
export const FINALIZER_IMMUTABLE_FIELDS = Object.freeze([
  'event_id',
  'event_fingerprint',
  'site_id',
  'schema_name',
  'schema_version',
  'event_type',
  'event_status',
  'intake_state',
  'first_seen_at',
  'duplicate_count',
  'conflict_count',
  'redaction_version',
  'sandbox_marker',
]);

export const SCHEMA_DECISION = 'D6A_EXISTING_SCHEMA_SUFFICIENT';

export const FINALIZER_UPDATE_MODEL = 'LOOKUP_VALIDATE_UPDATE_SEQUENTIAL_ONLY';

export const MAX_SAFE_CONCURRENCY = 1;

export const MAX_RETRIES = 0;

/**
 * Telegram success authority from node output (sanitized).
 * Success requires positive message_id and no error signal.
 * message_id is optional audit metadata for SENT; state machine requires success proof only.
 *
 * @param {Record<string, unknown>|null|undefined} telegramNodeOutput
 * @param {{ nodeError?: boolean, ambiguous?: boolean }} [flags]
 */
export function classifyTelegramOutcome(telegramNodeOutput, flags = {}) {
  if (flags.ambiguous) {
    return {
      outcome: 'AMBIGUOUS',
      target_delivery_state: null,
      should_finalize: false,
      telegram_message_id: null,
      sanitized_error_class: null,
      reason: 'telegram_outcome_ambiguous',
    };
  }
  if (flags.nodeError) {
    return {
      outcome: 'DEFINITE_FAILURE',
      target_delivery_state: DELIVERY_STATE.FAILED,
      should_finalize: true,
      telegram_message_id: null,
      sanitized_error_class: 'TELEGRAM_NODE_ERROR',
      reason: 'telegram_node_definite_failure',
    };
  }

  const raw = telegramNodeOutput && typeof telegramNodeOutput === 'object' ? telegramNodeOutput : {};
  const nested = raw.result && typeof raw.result === 'object' ? raw.result : raw;
  const messageId =
    nested.message_id != null
      ? String(nested.message_id)
      : raw.message_id != null
        ? String(raw.message_id)
        : null;

  const hasErrorFlag =
    raw.ok === false ||
    nested.ok === false ||
    Boolean(raw.error) ||
    Boolean(nested.error) ||
    Boolean(raw.errno) ||
    Boolean(raw.name === 'NodeOperationError');

  if (hasErrorFlag) {
    return {
      outcome: 'DEFINITE_FAILURE',
      target_delivery_state: DELIVERY_STATE.FAILED,
      should_finalize: true,
      telegram_message_id: null,
      sanitized_error_class: 'TELEGRAM_API_ERROR',
      reason: 'telegram_api_error_flag',
    };
  }

  if (messageId && /^\d+$/.test(messageId)) {
    return {
      outcome: 'SUCCESS',
      target_delivery_state: DELIVERY_STATE.SENT,
      should_finalize: true,
      telegram_message_id: messageId,
      sanitized_error_class: null,
      reason: 'telegram_message_id_present',
    };
  }

  // Node ran without error flag but no message_id — treat as ambiguous (do not FAILED).
  return {
    outcome: 'AMBIGUOUS',
    target_delivery_state: null,
    should_finalize: false,
    telegram_message_id: null,
    sanitized_error_class: null,
    reason: 'telegram_success_unproven',
  };
}

/**
 * Transition table for delivery_state.
 * @param {string} current
 * @param {string} target
 */
export function evaluateDeliveryTransition(current, target) {
  const from = String(current || '');
  const to = String(target || '');

  if (!DELIVERY_STATES.includes(from)) {
    return { ok: false, action: 'REJECT', code: 'UNKNOWN_CURRENT_STATE' };
  }
  if (!DELIVERY_STATES.includes(to)) {
    return { ok: false, action: 'REJECT', code: 'UNKNOWN_TARGET_STATE' };
  }

  if (from === to) {
    return { ok: true, action: 'NOOP_IDEMPOTENT', code: 'ALREADY_FINALIZED' };
  }

  if (from === DELIVERY_STATE.PENDING && to === DELIVERY_STATE.SENT) {
    return { ok: true, action: 'UPDATE', code: 'PENDING_TO_SENT' };
  }
  if (from === DELIVERY_STATE.PENDING && to === DELIVERY_STATE.FAILED) {
    return { ok: true, action: 'UPDATE', code: 'PENDING_TO_FAILED' };
  }

  if (from === DELIVERY_STATE.SENT && to === DELIVERY_STATE.FAILED) {
    return { ok: false, action: 'REJECT', code: 'SENT_TO_FAILED_PROHIBITED' };
  }
  if (from === DELIVERY_STATE.FAILED && to === DELIVERY_STATE.SENT) {
    return {
      ok: false,
      action: 'REJECT',
      code: 'FAILED_TO_SENT_REQUIRES_RECOVERY_CHARTER',
    };
  }

  return { ok: false, action: 'REJECT', code: 'INVALID_TRANSITION' };
}

/**
 * Narrow finalizer contract input validation + apply against an in-memory row.
 * Does not perform Telegram side effects.
 *
 * @param {Record<string, unknown>} row
 * @param {{
 *   event_id: string,
 *   expected_current_delivery_state?: string,
 *   target_delivery_state: string,
 *   delivery_finished_at?: string|null,
 *   telegram_message_id?: string|null,
 *   sanitized_error_class?: string|null,
 * }} request
 */
export function applyDeliveryFinalizer(row, request) {
  if (!row || typeof row !== 'object') {
    return { ok: false, code: 'ROW_MISSING', row: null, mutation: null };
  }

  const eventId = String(request.event_id || '');
  if (!eventId || String(row.event_id || '') !== eventId) {
    return { ok: false, code: 'EVENT_ID_MISMATCH', row, mutation: null };
  }

  const current = String(row.delivery_state || '');
  const expected = request.expected_current_delivery_state
    ? String(request.expected_current_delivery_state)
    : null;
  if (expected && current !== expected) {
    // Idempotent observation of already-finalized matching target
    const transitionEarly = evaluateDeliveryTransition(current, request.target_delivery_state);
    if (transitionEarly.action === 'NOOP_IDEMPOTENT') {
      return {
        ok: true,
        code: 'ALREADY_FINALIZED',
        row: { ...row },
        mutation: null,
        transition: transitionEarly,
      };
    }
    return {
      ok: false,
      code: 'EXPECTED_STATE_MISMATCH',
      row,
      mutation: null,
      current_delivery_state: current,
    };
  }

  const transition = evaluateDeliveryTransition(current, request.target_delivery_state);
  if (!transition.ok) {
    return { ok: false, code: transition.code, row, mutation: null, transition };
  }
  if (transition.action === 'NOOP_IDEMPOTENT') {
    return {
      ok: true,
      code: 'ALREADY_FINALIZED',
      row: { ...row },
      mutation: null,
      transition,
    };
  }

  const next = { ...row, delivery_state: String(request.target_delivery_state) };
  // Observability fields are NOT persisted into the 15-column schema in D6A.
  // They may be returned for harness/audit only.
  const mutation = {
    delivery_state: String(request.target_delivery_state),
  };

  return {
    ok: true,
    code: transition.code,
    row: next,
    mutation,
    transition,
    audit: {
      delivery_finished_at: request.delivery_finished_at || null,
      telegram_message_id: request.telegram_message_id || null,
      sanitized_error_class: request.sanitized_error_class || null,
    },
    invariants: {
      intake_state: row.intake_state,
      event_status: row.event_status,
      event_id: row.event_id,
    },
  };
}

/**
 * Assert immutable intake/event fields unchanged after finalization.
 * @param {Record<string, unknown>} before
 * @param {Record<string, unknown>} after
 */
export function assertIntakeAndStatusImmutable(before, after) {
  const violations = [];
  for (const field of FINALIZER_IMMUTABLE_FIELDS) {
    if (String(before[field] ?? '') !== String(after[field] ?? '')) {
      violations.push(field);
    }
  }
  return { ok: violations.length === 0, violations };
}

/**
 * Duplicate intake must never re-trigger Telegram regardless of delivery_state.
 * @param {string} intakeClassification FIRST_SEEN | DUPLICATE | EVENT_ID_CONFLICT
 * @param {string} [deliveryState]
 */
export function shouldAttemptTelegram(intakeClassification, deliveryState) {
  void deliveryState;
  return String(intakeClassification) === 'FIRST_SEEN';
}

/**
 * In-memory sequential Data Table for offline harness.
 */
export function createOfflineLedgerStore(initialRows = []) {
  /** @type {Map<string, Record<string, unknown>>} */
  const rows = new Map();
  for (const row of initialRows) {
    rows.set(String(row.event_id), { ...row });
  }

  return {
    get(eventId) {
      const row = rows.get(String(eventId));
      return row ? { ...row } : null;
    },
    insert(row) {
      const id = String(row.event_id);
      if (rows.has(id)) {
        return { ok: false, code: 'DUPLICATE_INSERT' };
      }
      rows.set(id, { ...row });
      return { ok: true, row: { ...row } };
    },
    /**
     * Lookup→validate→update sequential model (not atomic CAS).
     * Optionally require current delivery_state match filter.
     */
    updateDeliveryState(eventId, target, { requireCurrent = DELIVERY_STATE.PENDING } = {}) {
      const current = rows.get(String(eventId));
      if (!current) return { ok: false, code: 'ROW_MISSING' };
      if (requireCurrent && String(current.delivery_state) !== requireCurrent) {
        const transition = evaluateDeliveryTransition(current.delivery_state, target);
        if (transition.action === 'NOOP_IDEMPOTENT') {
          return { ok: true, code: 'ALREADY_FINALIZED', row: { ...current }, matched: 0 };
        }
        return {
          ok: false,
          code: 'FILTER_NO_MATCH',
          row: { ...current },
          matched: 0,
        };
      }
      const applied = applyDeliveryFinalizer(current, {
        event_id: String(eventId),
        expected_current_delivery_state: requireCurrent || undefined,
        target_delivery_state: target,
      });
      if (!applied.ok) return applied;
      if (applied.mutation) {
        rows.set(String(eventId), applied.row);
      }
      return { ...applied, matched: applied.mutation ? 1 : 0 };
    },
    snapshot() {
      return [...rows.values()].map((r) => ({ ...r }));
    },
  };
}

/**
 * Simulate FIRST_SEEN claim + Telegram + finalizer (offline).
 * Separates Telegram side effect from ledger finalization.
 */
export function simulateFirstSeenDeliveryPath({
  store,
  claimRow,
  telegramOutcome,
  finalizeFails = false,
}) {
  const telegramAttempts = { count: 0 };
  const insert = store.insert({
    ...claimRow,
    intake_state: 'FIRST_SEEN',
    delivery_state: DELIVERY_STATE.PENDING,
  });
  if (!insert.ok) return { ok: false, stage: 'claim', insert };

  const http202 = {
    http_status: 202,
    response: {
      ok: true,
      result: 'ACCEPTED',
      event_id: claimRow.event_id,
      dedupe: 'FIRST_SEEN',
    },
  };

  telegramAttempts.count += 1;
  const classified = classifyTelegramOutcome(
    telegramOutcome.output,
    {
      nodeError: Boolean(telegramOutcome.nodeError),
      ambiguous: Boolean(telegramOutcome.ambiguous),
    },
  );

  let finalize = null;
  if (classified.should_finalize) {
    if (finalizeFails) {
      finalize = {
        ok: false,
        code: 'LEDGER_WRITE_FAILURE',
        row: store.get(claimRow.event_id),
        telegram_attempts: telegramAttempts.count,
      };
      return {
        ok: true,
        http: http202,
        classified,
        finalize,
        row: store.get(claimRow.event_id),
        telegram_attempts: telegramAttempts.count,
        note: 'Telegram side effect may have occurred; durable state remains PENDING; no automatic resend',
      };
    }
    finalize = store.updateDeliveryState(
      claimRow.event_id,
      classified.target_delivery_state,
      { requireCurrent: DELIVERY_STATE.PENDING },
    );
  }

  return {
    ok: true,
    http: http202,
    classified,
    finalize,
    row: store.get(claimRow.event_id),
    telegram_attempts: telegramAttempts.count,
  };
}

/**
 * Duplicate replay path — must not Telegram.
 */
export function simulateDuplicateReplay({ store, eventId, fingerprint }) {
  const row = store.get(eventId);
  if (!row) return { ok: false, code: 'ROW_MISSING' };
  const classification =
    String(row.event_fingerprint) === String(fingerprint) ? 'DUPLICATE' : 'EVENT_ID_CONFLICT';
  const attempt = shouldAttemptTelegram(classification, row.delivery_state);
  return {
    ok: true,
    classification,
    telegram_attempted: attempt,
    http_status: classification === 'DUPLICATE' ? 200 : 409,
    delivery_state: row.delivery_state,
    intake_state: row.intake_state,
    event_status: row.event_status,
    row: { ...row },
  };
}
