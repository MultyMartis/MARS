/**
 * Phase 1B-D6C — local lifecycle lock (no secrets).
 * Fail-closed on valid existing lock; no silent takeover of unknown active locks.
 */

import { existsSync, mkdirSync, readFileSync, renameSync, unlinkSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';

export const LOCK_SCHEMA_VERSION = 1;

/**
 * @typedef {object} LifecycleLockRecord
 * @property {number} schema_version
 * @property {string} workflow_id
 * @property {string} charter_id
 * @property {number} pid
 * @property {string} process_identity
 * @property {number} created_at_ms
 * @property {number} lease_expires_at_ms
 * @property {string} owner_token
 */

/**
 * @param {string} lockPath
 * @returns {LifecycleLockRecord|null}
 */
export function readLifecycleLock(lockPath) {
  if (!existsSync(lockPath)) return null;
  try {
    const raw = JSON.parse(readFileSync(lockPath, 'utf8'));
    if (!raw || typeof raw !== 'object') return null;
    return /** @type {LifecycleLockRecord} */ (raw);
  } catch {
    return null;
  }
}

/**
 * @param {LifecycleLockRecord} lock
 * @param {{
 *   nowMs: number,
 *   processAlive?: (pid: number) => boolean,
 *   workflowActive?: boolean|null,
 * }} ctx
 */
export function classifyLifecycleLock(lock, ctx) {
  const processAlive =
    typeof ctx.processAlive === 'function' ? ctx.processAlive(lock.pid) : null;
  const leaseExpired = ctx.nowMs > Number(lock.lease_expires_at_ms);
  const workflowActive =
    ctx.workflowActive === undefined ? null : Boolean(ctx.workflowActive);

  if (processAlive === true && !leaseExpired) {
    return {
      class: 'VALID_ACTIVE_LOCK',
      action: 'FAIL_CLOSED',
      process_alive: processAlive,
      lease_expired: leaseExpired,
      workflow_active: workflowActive,
    };
  }

  if (workflowActive === true) {
    return {
      class: 'STALE_OR_UNKNOWN_LOCK_WORKFLOW_ACTIVE',
      action: 'OPERATOR_REVIEW_RECONTAINMENT_REQUIRED',
      process_alive: processAlive,
      lease_expired: leaseExpired,
      workflow_active: workflowActive,
    };
  }

  if (processAlive === false && workflowActive === false) {
    return {
      class: 'STALE_LOCK_WORKFLOW_INACTIVE',
      action: 'EXPLICIT_RECOVERY_ALLOWED',
      process_alive: processAlive,
      lease_expired: leaseExpired,
      workflow_active: workflowActive,
    };
  }

  if (leaseExpired && workflowActive === false) {
    return {
      class: 'STALE_LOCK_WORKFLOW_INACTIVE',
      action: 'EXPLICIT_RECOVERY_ALLOWED',
      process_alive: processAlive,
      lease_expired: leaseExpired,
      workflow_active: workflowActive,
    };
  }

  return {
    class: 'AMBIGUOUS_LOCK',
    action: 'FAIL_CLOSED_OPERATOR_REVIEW',
    process_alive: processAlive,
    lease_expired: leaseExpired,
    workflow_active: workflowActive,
  };
}

/**
 * @param {{
 *   lockPath: string,
 *   workflowId: string,
 *   charterId: string,
 *   ownerToken: string,
 *   nowMs: number,
 *   leaseMs?: number,
 *   pid?: number,
 *   processIdentity?: string,
 *   processAlive?: (pid: number) => boolean,
 *   workflowActive?: boolean|null,
 *   allowExplicitStaleRecovery?: boolean,
 * }} opts
 */
export function acquireLifecycleLock(opts) {
  const lockPath = resolve(opts.lockPath);
  const existing = readLifecycleLock(lockPath);
  if (existing) {
    const classification = classifyLifecycleLock(existing, {
      nowMs: opts.nowMs,
      processAlive: opts.processAlive,
      workflowActive: opts.workflowActive,
    });
    if (classification.action === 'FAIL_CLOSED') {
      return {
        ok: false,
        reason: 'VALID_EXISTING_LIFECYCLE_LOCK',
        classification,
        lock: sanitizeLock(existing),
      };
    }
    if (classification.action === 'OPERATOR_REVIEW_RECONTAINMENT_REQUIRED') {
      return {
        ok: false,
        reason: 'STALE_LOCK_WITH_ACTIVE_WORKFLOW',
        classification,
        lock: sanitizeLock(existing),
      };
    }
    if (classification.action === 'FAIL_CLOSED_OPERATOR_REVIEW') {
      return {
        ok: false,
        reason: 'AMBIGUOUS_LIFECYCLE_LOCK',
        classification,
        lock: sanitizeLock(existing),
      };
    }
    if (
      classification.action === 'EXPLICIT_RECOVERY_ALLOWED' &&
      !opts.allowExplicitStaleRecovery
    ) {
      return {
        ok: false,
        reason: 'STALE_LOCK_REQUIRES_EXPLICIT_RECOVERY',
        classification,
        lock: sanitizeLock(existing),
      };
    }
    // Explicit recovery: remove only after classification allows and charter opts in.
    unlinkSync(lockPath);
  }

  const leaseMs = opts.leaseMs ?? 15 * 60 * 1000;
  /** @type {LifecycleLockRecord} */
  const record = {
    schema_version: LOCK_SCHEMA_VERSION,
    workflow_id: opts.workflowId,
    charter_id: opts.charterId,
    pid: opts.pid ?? process.pid,
    process_identity: opts.processIdentity ?? `pid:${opts.pid ?? process.pid}`,
    created_at_ms: opts.nowMs,
    lease_expires_at_ms: opts.nowMs + leaseMs,
    owner_token: opts.ownerToken,
  };

  mkdirSync(dirname(lockPath), { recursive: true });
  const tmp = `${lockPath}.${record.owner_token}.tmp`;
  writeFileSync(tmp, `${JSON.stringify(record, null, 2)}\n`, 'utf8');
  try {
    renameSync(tmp, lockPath);
  } catch (err) {
    try {
      unlinkSync(tmp);
    } catch {
      /* ignore */
    }
    // Race: another process created the lock.
    const raced = readLifecycleLock(lockPath);
    return {
      ok: false,
      reason: 'LOCK_ACQUIRE_RACE',
      classification: raced
        ? classifyLifecycleLock(raced, {
            nowMs: opts.nowMs,
            processAlive: opts.processAlive,
            workflowActive: opts.workflowActive,
          })
        : null,
      lock: raced ? sanitizeLock(raced) : null,
      error_class: err instanceof Error ? err.name : 'LOCK_ERROR',
    };
  }

  return { ok: true, lock: sanitizeLock(record), owner_token: record.owner_token };
}

/**
 * Release only when ownership matches AND containment verified.
 * @param {{
 *   lockPath: string,
 *   ownerToken: string,
 *   charterId: string,
 *   containmentVerified: boolean,
 * }} opts
 */
export function releaseLifecycleLock(opts) {
  if (!opts.containmentVerified) {
    return {
      ok: false,
      reason: 'CONTAINMENT_NOT_VERIFIED',
      released: false,
    };
  }
  const existing = readLifecycleLock(opts.lockPath);
  if (!existing) {
    return { ok: true, reason: 'LOCK_ALREADY_ABSENT', released: false };
  }
  if (
    existing.owner_token !== opts.ownerToken ||
    existing.charter_id !== opts.charterId
  ) {
    return {
      ok: false,
      reason: 'OWNERSHIP_MISMATCH',
      released: false,
      lock: sanitizeLock(existing),
    };
  }
  unlinkSync(opts.lockPath);
  return { ok: true, reason: 'LOCK_RELEASED', released: true };
}

/**
 * @param {LifecycleLockRecord} lock
 */
export function sanitizeLock(lock) {
  return {
    schema_version: lock.schema_version,
    workflow_id: lock.workflow_id,
    charter_id: lock.charter_id,
    pid: lock.pid,
    process_identity: lock.process_identity,
    created_at_ms: lock.created_at_ms,
    lease_expires_at_ms: lock.lease_expires_at_ms,
    owner_token_present: Boolean(lock.owner_token),
  };
}
