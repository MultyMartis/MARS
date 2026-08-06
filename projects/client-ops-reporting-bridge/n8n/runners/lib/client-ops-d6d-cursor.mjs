/**
 * Phase 1B-D6D — local producer cursor (NOT delivery dedupe authority).
 * Durable ledger (Data Table) remains authoritative for SENT/PENDING/FAILED.
 */

import { existsSync, mkdirSync, readFileSync, renameSync, unlinkSync, writeFileSync } from 'node:fs';
import { dirname } from 'node:path';
import {
  CURSOR_STATES,
  D6D_PRODUCER_SCHEMA_VERSION,
  D6D_SITE_ID,
} from './client-ops-d6d-constants.mjs';

const SECRET_RE =
  /(api[_-]?key|authorization|token|secret|password|webhook_url|telegram|customer_payload)/i;

/**
 * @typedef {object} ProducerCursor
 * @property {number} schema_version
 * @property {string} site_id
 * @property {string} producer_schema_version
 * @property {string|null} last_evaluated_run_id
 * @property {string|null} last_evaluated_event_id
 * @property {string|null} last_artifact_identity
 * @property {string|null} artifact_hash
 * @property {string|null} evaluation_timestamp
 * @property {string|null} cursor_state
 * @property {string|null} result_class
 * @property {string|null} delivery_decision
 * @property {string|null} lifecycle_result
 * @property {boolean} processing_terminal
 * @property {boolean} requires_reconciliation
 * @property {string|null} bootstrap_boundary
 * @property {Record<string, unknown>} [evaluated_runs]
 */

export function emptyCursor(siteId = D6D_SITE_ID) {
  return {
    schema_version: D6D_PRODUCER_SCHEMA_VERSION,
    site_id: siteId,
    producer_schema_version: String(D6D_PRODUCER_SCHEMA_VERSION),
    last_evaluated_run_id: null,
    last_evaluated_event_id: null,
    last_artifact_identity: null,
    artifact_hash: null,
    evaluation_timestamp: null,
    cursor_state: null,
    result_class: null,
    delivery_decision: null,
    lifecycle_result: null,
    processing_terminal: false,
    requires_reconciliation: false,
    bootstrap_boundary: null,
    evaluated_runs: {},
  };
}

/**
 * @param {string} path
 * @returns {ProducerCursor}
 */
export function readCursor(path) {
  if (!existsSync(path)) return emptyCursor();
  try {
    const raw = JSON.parse(readFileSync(path, 'utf8'));
    if (!raw || typeof raw !== 'object') return emptyCursor();
    return { ...emptyCursor(), ...raw };
  } catch {
    throw new Error('CURSOR_PARSE_FAILED');
  }
}

/**
 * Sanitize cursor for persistence / evidence (no secrets).
 * @param {ProducerCursor} cursor
 */
export function sanitizeCursor(cursor) {
  const out = { ...cursor, evaluated_runs: { ...(cursor.evaluated_runs || {}) } };
  const json = JSON.stringify(out);
  if (SECRET_RE.test(json)) {
    throw new Error('CURSOR_CONTAINS_SECRETS');
  }
  return out;
}

/**
 * Crash-safety: do not mark DELIVERY_TERMINAL without durable evidence.
 * @param {string} nextState
 * @param {{ durable_delivery_state?: string|null, ambiguous?: boolean, ledger_authoritative?: boolean }} evidence
 */
export function assertCursorTransitionSafe(nextState, evidence = {}) {
  if (nextState === CURSOR_STATES.DELIVERY_TERMINAL) {
    const ds = String(evidence.durable_delivery_state || '').toUpperCase();
    if (ds !== 'SENT' && ds !== 'FAILED') {
      return {
        ok: false,
        reason: 'CURSOR_TERMINAL_REQUIRES_DURABLE_SENT_OR_FAILED',
      };
    }
    if (evidence.ambiguous) {
      return { ok: false, reason: 'CURSOR_TERMINAL_FORBIDDEN_WHEN_AMBIGUOUS' };
    }
  }
  if (
    nextState === CURSOR_STATES.ALREADY_HANDLED &&
    evidence.durable_delivery_state &&
    String(evidence.durable_delivery_state).toUpperCase() !== 'SENT' &&
    evidence.ledger_authoritative !== false
  ) {
    // Cursor may observe already-handled only when ledger says SENT (or explicit local-only dry observation)
  }
  return { ok: true };
}

/**
 * @param {string} path
 * @param {ProducerCursor} cursor
 */
export function writeCursor(path, cursor) {
  const sanitized = sanitizeCursor(cursor);
  mkdirSync(dirname(path), { recursive: true });
  const tmp = `${path}.tmp`;
  writeFileSync(tmp, `${JSON.stringify(sanitized, null, 2)}\n`, 'utf8');
  renameSync(tmp, path);
  return sanitized;
}

/**
 * Advance cursor for a run observation without claiming delivery unless terminal+durable.
 * @param {ProducerCursor} cursor
 * @param {object} patch
 */
export function applyCursorObservation(cursor, patch) {
  const next = { ...cursor, evaluated_runs: { ...(cursor.evaluated_runs || {}) } };
  const runId = patch.run_id || next.last_evaluated_run_id;
  if (runId) {
    next.evaluated_runs[runId] = {
      ...(next.evaluated_runs[runId] || {}),
      event_id: patch.event_id ?? null,
      artifact_hash: patch.artifact_hash ?? null,
      cursor_state: patch.cursor_state ?? null,
      result_class: patch.result_class ?? null,
      delivery_decision: patch.delivery_decision ?? null,
      processing_terminal: Boolean(patch.processing_terminal),
      requires_reconciliation: Boolean(patch.requires_reconciliation),
      evaluation_timestamp: patch.evaluation_timestamp ?? null,
      durable_delivery_state: patch.durable_delivery_state ?? null,
    };
  }
  next.last_evaluated_run_id = patch.run_id ?? next.last_evaluated_run_id;
  next.last_evaluated_event_id = patch.event_id ?? next.last_evaluated_event_id;
  next.last_artifact_identity = patch.artifact_identity ?? next.last_artifact_identity;
  next.artifact_hash = patch.artifact_hash ?? next.artifact_hash;
  next.evaluation_timestamp = patch.evaluation_timestamp ?? next.evaluation_timestamp;
  next.cursor_state = patch.cursor_state ?? next.cursor_state;
  next.result_class = patch.result_class ?? next.result_class;
  next.delivery_decision = patch.delivery_decision ?? next.delivery_decision;
  next.lifecycle_result = patch.lifecycle_result ?? next.lifecycle_result;
  next.processing_terminal = Boolean(patch.processing_terminal);
  next.requires_reconciliation = Boolean(patch.requires_reconciliation);
  if (patch.bootstrap_boundary != null) {
    next.bootstrap_boundary = patch.bootstrap_boundary;
  }
  return next;
}

/**
 * Ledger overrides cursor: if cursor says delivered but ledger disagrees → reconcile.
 * @param {{ cursor_says_delivered: boolean, durable_delivery_state: string|null|undefined }} obs
 */
export function reconcileCursorVsLedger(obs) {
  const ds = String(obs.durable_delivery_state || '').toUpperCase() || null;
  if (obs.cursor_says_delivered && ds !== 'SENT') {
    return {
      decision: 'RECONCILE',
      reason: 'CURSOR_DELIVERED_LEDGER_DISAGREES',
      allow_resend: false,
      cursor_overrides_ledger: false,
    };
  }
  if (ds === 'SENT') {
    return {
      decision: 'ALREADY_HANDLED',
      reason: 'LEDGER_SENT_SUPPRESSES_RESEND',
      allow_resend: false,
      cursor_overrides_ledger: false,
    };
  }
  if (ds === 'PENDING') {
    return {
      decision: 'RECONCILE',
      reason: 'LEDGER_PENDING',
      allow_resend: false,
      cursor_overrides_ledger: false,
    };
  }
  if (ds === 'FAILED') {
    return {
      decision: 'FINAL_FAILURE',
      reason: 'LEDGER_FAILED',
      allow_resend: false,
      cursor_overrides_ledger: false,
    };
  }
  return {
    decision: 'CONTINUE',
    reason: 'NO_LEDGER_ROW_OR_UNKNOWN',
    allow_resend: false, // still requires full gates; no blind send
    cursor_overrides_ledger: false,
  };
}

export function clearCursorFile(path) {
  if (existsSync(path)) unlinkSync(path);
}

export { CURSOR_STATES };
