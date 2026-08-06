/**
 * Phase 1B-D6D — producer singleton lock (distinct from Workstream C lifecycle lock).
 * Prevents overlapping scheduled producer instances. MAX_SAFE_CONCURRENCY=1.
 */

import { existsSync, mkdirSync, readFileSync, renameSync, unlinkSync, writeFileSync } from 'node:fs';
import { dirname } from 'node:path';
import { D6D_PRODUCER_SCHEMA_VERSION } from './client-ops-d6d-constants.mjs';

export const PRODUCER_LOCK_SCHEMA_VERSION = 1;

/**
 * @typedef {object} ProducerLockRecord
 * @property {number} schema_version
 * @property {string} site_id
 * @property {string} producer_identity
 * @property {number} pid
 * @property {string} process_identity
 * @property {string} session_id
 * @property {number} created_at_ms
 * @property {number} lease_expires_at_ms
 * @property {string} runtime_checkout_identity
 * @property {string} owner_token
 */

/**
 * @param {string} lockPath
 * @returns {ProducerLockRecord|null}
 */
export function readProducerLock(lockPath) {
  if (!existsSync(lockPath)) return null;
  try {
    const raw = JSON.parse(readFileSync(lockPath, 'utf8'));
    if (!raw || typeof raw !== 'object') return null;
    return /** @type {ProducerLockRecord} */ (raw);
  } catch {
    return null;
  }
}

/**
 * @param {ProducerLockRecord} lock
 * @param {{ nowMs: number, processAlive?: (pid:number)=>boolean }} ctx
 */
export function classifyProducerLock(lock, ctx) {
  const processAlive =
    typeof ctx.processAlive === 'function' ? ctx.processAlive(lock.pid) : null;
  const leaseExpired = ctx.nowMs > Number(lock.lease_expires_at_ms);

  if (processAlive === true && !leaseExpired) {
    return {
      class: 'VALID_ACTIVE_LOCK',
      action: 'FAIL_CLOSED',
      process_alive: processAlive,
      lease_expired: leaseExpired,
    };
  }
  if (processAlive === false || leaseExpired) {
    return {
      class: 'STALE_LOCK',
      action: 'EXPLICIT_STALE_RECOVERY_ALLOWED',
      process_alive: processAlive,
      lease_expired: leaseExpired,
    };
  }
  // Unknown liveness — do not silently delete
  return {
    class: 'UNKNOWN_LOCK',
    action: 'FAIL_CLOSED',
    process_alive: processAlive,
    lease_expired: leaseExpired,
  };
}

/**
 * @param {object} opts
 * @param {string} opts.lockPath
 * @param {string} opts.siteId
 * @param {string} opts.producerIdentity
 * @param {string} opts.ownerToken
 * @param {string} opts.sessionId
 * @param {string} opts.runtimeCheckoutIdentity
 * @param {number} opts.nowMs
 * @param {number} [opts.leaseMs]
 * @param {number} [opts.pid]
 * @param {string} [opts.processIdentity]
 * @param {(pid:number)=>boolean} [opts.processAlive]
 * @param {boolean} [opts.allowExplicitStaleRecovery]
 */
export function acquireProducerLock(opts) {
  const {
    lockPath,
    siteId,
    producerIdentity,
    ownerToken,
    sessionId,
    runtimeCheckoutIdentity,
    nowMs,
    leaseMs = 300_000,
    pid = process.pid,
    processIdentity = `pid:${process.pid}`,
    processAlive,
    allowExplicitStaleRecovery = false,
  } = opts;

  const existing = readProducerLock(lockPath);
  if (existing) {
    const cls = classifyProducerLock(existing, { nowMs, processAlive });
    if (cls.action === 'FAIL_CLOSED') {
      return {
        ok: false,
        reason: 'PRODUCER_LOCK_HELD',
        classification: cls,
        lock: existing,
      };
    }
    if (cls.class === 'STALE_LOCK' && !allowExplicitStaleRecovery) {
      return {
        ok: false,
        reason: 'PRODUCER_LOCK_STALE_REQUIRES_EXPLICIT_RECOVERY',
        classification: cls,
        lock: existing,
      };
    }
    if (cls.class === 'STALE_LOCK' && allowExplicitStaleRecovery) {
      try {
        unlinkSync(lockPath);
      } catch {
        return {
          ok: false,
          reason: 'PRODUCER_LOCK_STALE_CLEAR_FAILED',
          classification: cls,
          lock: existing,
        };
      }
    } else if (cls.action !== 'EXPLICIT_STALE_RECOVERY_ALLOWED') {
      return {
        ok: false,
        reason: 'PRODUCER_LOCK_UNKNOWN',
        classification: cls,
        lock: existing,
      };
    }
  }

  /** @type {ProducerLockRecord} */
  const record = {
    schema_version: PRODUCER_LOCK_SCHEMA_VERSION,
    site_id: siteId,
    producer_identity: producerIdentity,
    pid,
    process_identity: processIdentity,
    session_id: sessionId,
    created_at_ms: nowMs,
    lease_expires_at_ms: nowMs + leaseMs,
    runtime_checkout_identity: runtimeCheckoutIdentity,
    owner_token: ownerToken,
  };

  // Reject secret-bearing keys (not benign fields like owner_token)
  const forbiddenKey = Object.keys(record).find((k) =>
    /^(api_key|token|secret|password|webhook_url|authorization)$/i.test(k),
  );
  if (forbiddenKey) {
    return { ok: false, reason: 'PRODUCER_LOCK_SECRET_REJECTED' };
  }
  const serialized = JSON.stringify(record);
  if (/"(api_key|password|webhook_url|authorization)"\s*:\s*"[^"]+"/i.test(serialized)) {
    return { ok: false, reason: 'PRODUCER_LOCK_SECRET_REJECTED' };
  }

  mkdirSync(dirname(lockPath), { recursive: true });
  const tmp = `${lockPath}.tmp.${nowMs}`;
  writeFileSync(tmp, `${JSON.stringify(record, null, 2)}\n`, 'utf8');
  try {
    renameSync(tmp, lockPath);
  } catch (err) {
    try {
      unlinkSync(tmp);
    } catch {
      /* ignore */
    }
    return {
      ok: false,
      reason: 'PRODUCER_LOCK_WRITE_FAILED',
      error: err instanceof Error ? err.message : String(err),
    };
  }

  return { ok: true, lock: record, schema_version: D6D_PRODUCER_SCHEMA_VERSION };
}

/**
 * @param {string} lockPath
 * @param {string} ownerToken
 */
export function releaseProducerLock(lockPath, ownerToken) {
  const existing = readProducerLock(lockPath);
  if (!existing) return { ok: true, released: false };
  if (existing.owner_token !== ownerToken) {
    return { ok: false, reason: 'PRODUCER_LOCK_OWNER_MISMATCH', released: false };
  }
  unlinkSync(lockPath);
  return { ok: true, released: true };
}
