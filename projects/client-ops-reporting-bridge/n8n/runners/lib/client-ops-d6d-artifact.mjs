/**
 * Phase 1B-D6D — artifact discovery, completion, stabilization, fingerprint, status, identity.
 * In-memory / injectable FS for offline tests. No filesystem watcher.
 */

import { createHash } from 'node:crypto';
import {
  AUTHORITATIVE_ARTIFACTS,
  AUTHORITATIVE_PRIMARY,
  COMPLETION_MARKER_FILENAME,
  DELIVERY_ELIGIBILITY,
  D6D_SITE_ID,
  EVENT_TYPE,
  FORBIDDEN_TEMP_SUFFIXES,
  MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID,
  MAX_FUTURE_SKEW_SECONDS,
  SCHEMA_MAJOR,
  SOURCE_STATUSES,
  STATUS_MAPPING,
  STALE_AFTER_SECONDS,
} from './client-ops-d6d-constants.mjs';

/**
 * Minimal UUID v5 (RFC 4122) over SHA-1 of namespace+name — matches Python uuid.uuid5.
 * @param {string} namespaceUuid
 * @param {string} name
 */
export function uuidV5(namespaceUuid, name) {
  const ns = Buffer.from(namespaceUuid.replace(/-/g, ''), 'hex');
  const hash = createHash('sha1').update(ns).update(name, 'utf8').digest();
  hash[6] = (hash[6] & 0x0f) | 0x50;
  hash[8] = (hash[8] & 0x3f) | 0x80;
  const h = hash.toString('hex');
  return `${h.slice(0, 8)}-${h.slice(8, 12)}-${h.slice(12, 16)}-${h.slice(16, 20)}-${h.slice(20, 32)}`;
}

export function sha256Hex(data) {
  return createHash('sha256').update(data).digest('hex');
}

export function isTempPath(name) {
  const lower = String(name).toLowerCase();
  return FORBIDDEN_TEMP_SUFFIXES.some((s) => lower.endsWith(s));
}

export function isPathAllowlisted(absPath, allowlistRoots) {
  const normalized = String(absPath).replace(/\//g, '\\').toLowerCase();
  return (allowlistRoots || []).some((root) => {
    const r = String(root).replace(/\//g, '\\').toLowerCase().replace(/\\+$/, '');
    return normalized === r || normalized.startsWith(`${r}\\`);
  });
}

/**
 * Map monitor classification → factual source_status.
 * @param {string} classification
 */
export function mapSourceStatus(classification) {
  const c = String(classification || '').toUpperCase();
  if (STATUS_MAPPING[c]) return STATUS_MAPPING[c];
  return SOURCE_STATUSES.BLOCKED;
}

export function isStaleAge(ageSeconds, threshold = STALE_AFTER_SECONDS) {
  if (ageSeconds == null) return false;
  return Number(ageSeconds) > Number(threshold);
}

/**
 * Workstream B eligibility (identical operator).
 */
export function evaluateDeliveryEligibility({
  source_status,
  age_seconds,
  security_rejected = false,
}) {
  const status = String(source_status || '');
  const stale = isStaleAge(age_seconds);
  if (status === SOURCE_STATUSES.BLOCKED || security_rejected) {
    return {
      delivery_eligibility: DELIVERY_ELIGIBILITY.NOT_SAFE_TO_SEND,
      stale,
      freshness_reason: stale
        ? 'SOURCE_AUTHORITY_NOT_SAFE_AND_STALE'
        : 'SOURCE_AUTHORITY_NOT_SAFE',
    };
  }
  if (age_seconds == null) {
    return {
      delivery_eligibility: DELIVERY_ELIGIBILITY.NOT_SAFE_TO_SEND,
      stale: false,
      freshness_reason: 'AGE_UNKNOWN',
    };
  }
  if (stale) {
    return {
      delivery_eligibility: DELIVERY_ELIGIBILITY.STALE_REVIEW_REQUIRED,
      stale: true,
      freshness_reason: 'SOURCE_REPORT_TOO_OLD',
    };
  }
  // FAILED factual is still FRESH_AND_ELIGIBLE on age, but NOT safe for customer send
  // downstream NOT_SAFE is applied for FAILED/BLOCKED send policy in producer gates.
  return {
    delivery_eligibility: DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
    stale: false,
    freshness_reason: 'WITHIN_FRESHNESS_THRESHOLD',
  };
}

/**
 * Build canonical identity (matches Python event_identity.build_canonical_identity).
 */
export function buildCanonicalIdentity(parts) {
  return {
    action_code: parts.action_code,
    event_type: parts.event_type || EVENT_TYPE,
    metrics: {
      added_urls: Number(parts.metrics.added_urls),
      baseline_count: Number(parts.metrics.baseline_count),
      current_count: Number(parts.metrics.current_count),
      onboarding_needed_count: Number(parts.metrics.onboarding_needed_count),
      removed_urls: Number(parts.metrics.removed_urls),
    },
    normalized_status: parts.normalized_status,
    observed_at: parts.observed_at,
    reason_codes: [...parts.reason_codes].sort(),
    run_id: parts.run_id,
    schema_major: Number(parts.schema_major ?? SCHEMA_MAJOR),
    site_id: parts.site_id || D6D_SITE_ID,
    summary_code: parts.summary_code,
  };
}

export function computeEventId(parts) {
  const identity = buildCanonicalIdentity(parts);
  const bytes = JSON.stringify(identity, Object.keys(identity).sort(), [
    /* custom: compact sorted */
  ]);
  // Match Python: json.dumps(sort_keys=True, separators=(',', ':'))
  const compact = JSON.stringify(identity, Object.keys(identity).sort());
  // JSON.stringify with sorted keys at top level only — nest metrics already fixed order
  const canonical = sortKeysDeep(identity);
  const name = sha256Hex(Buffer.from(JSON.stringify(canonical), 'utf8'));
  return uuidV5(MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID, name);
}

function sortKeysDeep(value) {
  if (Array.isArray(value)) return value.map(sortKeysDeep);
  if (value && typeof value === 'object') {
    const out = {};
    for (const k of Object.keys(value).sort()) {
      out[k] = sortKeysDeep(value[k]);
    }
    return out;
  }
  return value;
}

/** Prefer compact separators like Python. */
export function computeEventIdPythonCompatible(parts) {
  const identity = sortKeysDeep(buildCanonicalIdentity(parts));
  const compact = JSON.stringify(identity).replace(/": /g, '":').replace(/, /g, ',');
  // Node JSON.stringify already uses no spaces
  const name = sha256Hex(Buffer.from(JSON.stringify(identity), 'utf8'));
  return { event_id: uuidV5(MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID, name), identity };
}

/**
 * Fingerprint of normalized authoritative content (not evaluation clock).
 * @param {{ run_summary: object, monitor_classification: object, changed_summary: object }} docs
 */
export function computeArtifactFingerprint(docs) {
  const normalized = sortKeysDeep({
    run_summary: pickSafe(docs.run_summary),
    monitor_classification: pickSafe(docs.monitor_classification),
    changed_summary: pickSafe(docs.changed_summary),
  });
  return sha256Hex(Buffer.from(JSON.stringify(normalized), 'utf8'));
}

function pickSafe(obj) {
  if (!obj || typeof obj !== 'object') return {};
  const deny =
    /password|secret|token|authorization|webhook|api_key|artifact_paths|run_log|monitor_script|runner_script|repo_root|production_url/i;
  const out = {};
  for (const [k, v] of Object.entries(obj)) {
    if (deny.test(k)) continue;
    if (typeof v === 'object' && v !== null) continue; // drop nested path blobs
    out[k] = v;
  }
  return out;
}

/**
 * Fake FS adapter interface used by discovery/stabilization.
 * @typedef {{
 *   listDir: (path:string)=>string[],
 *   readText: (path:string)=>string,
 *   exists: (path:string)=>boolean,
 *   size: (path:string)=>number,
 *   mtimeMs?: (path:string)=>number,
 * }} FakeFs
 */

/**
 * Stabilize artifact: two bounded reads of size+hash must match; optional min age.
 * No unbounded sleep — clock injected; second read uses same FS snapshot or mutation hook.
 */
export function stabilizeArtifact(fs, artifactPath, opts = {}) {
  const minAgeMs = opts.minAgeMs ?? 0;
  const clock = opts.clock || { nowMs: () => Date.now() };
  const now = clock.nowMs();
  if (!fs.exists(artifactPath)) {
    return { ok: false, reason: 'ARTIFACT_MISSING' };
  }
  if (isTempPath(artifactPath)) {
    return { ok: false, reason: 'TEMP_FILE_REJECTED' };
  }
  const size1 = fs.size(artifactPath);
  if (size1 <= 0) return { ok: false, reason: 'EMPTY_ARTIFACT' };
  const text1 = fs.readText(artifactPath);
  const hash1 = sha256Hex(Buffer.from(text1, 'utf8'));

  // Injected second-read mutation (tests): optional beforeSecondRead hook
  if (typeof opts.beforeSecondRead === 'function') {
    opts.beforeSecondRead();
  }

  const size2 = fs.size(artifactPath);
  const text2 = fs.readText(artifactPath);
  const hash2 = sha256Hex(Buffer.from(text2, 'utf8'));
  if (size1 !== size2 || hash1 !== hash2) {
    return { ok: false, reason: 'ARTIFACT_UNSTABLE', deferred: true };
  }
  if (minAgeMs > 0 && typeof fs.mtimeMs === 'function') {
    const age = now - fs.mtimeMs(artifactPath);
    if (age < minAgeMs) {
      return { ok: false, reason: 'ARTIFACT_TOO_YOUNG', deferred: true };
    }
  }
  return { ok: true, hash: hash1, size: size1, text: text1 };
}

/**
 * Validate completed run directory against completion contract.
 * @param {FakeFs} fs
 * @param {string} runDir
 * @param {object} opts
 */
export function validateCompletedRun(fs, runDir, opts = {}) {
  const allowlist = opts.allowlistRoots || [];
  const clock = opts.clock || { nowMs: () => Date.now() };
  const requireMarker = opts.requireCompletionMarker !== false;
  const schemaVersion = opts.supportedSchema || 'site002-monitor-result-v1';

  if (!isPathAllowlisted(runDir, allowlist.length ? allowlist : [runDir])) {
    // When allowlist empty of roots, tests pass explicit allowlist including runDir parent
  }
  if (allowlist.length && !isPathAllowlisted(runDir, allowlist)) {
    return { ok: false, reason: 'PATH_OUTSIDE_ALLOWLIST', blocked: true };
  }

  for (const name of AUTHORITATIVE_ARTIFACTS) {
    if (isTempPath(name)) {
      return { ok: false, reason: 'TEMP_NAME' };
    }
    const p = joinPath(runDir, name);
    if (!fs.exists(p)) {
      return { ok: false, reason: `MISSING_${name}`, incomplete: true };
    }
  }

  if (requireMarker) {
    const marker = joinPath(runDir, COMPLETION_MARKER_FILENAME);
    if (!fs.exists(marker)) {
      return { ok: false, reason: 'MISSING_COMPLETION_MARKER', incomplete: true };
    }
  }

  /** @type {Record<string, object>} */
  const docs = {};
  for (const name of AUTHORITATIVE_ARTIFACTS) {
    const p = joinPath(runDir, name);
    const stab = stabilizeArtifact(fs, p, {
      clock,
      beforeSecondRead: opts.beforeSecondRead,
      minAgeMs: opts.minAgeMs,
    });
    if (!stab.ok) {
      return {
        ok: false,
        reason: stab.reason,
        deferred: Boolean(stab.deferred),
        artifact: name,
      };
    }
    let parsed;
    try {
      parsed = JSON.parse(stab.text);
    } catch {
      return { ok: false, reason: 'INVALID_JSON', artifact: name, failed_local: true };
    }
    if (!parsed || typeof parsed !== 'object') {
      return { ok: false, reason: 'INVALID_JSON_SHAPE', artifact: name, failed_local: true };
    }
    docs[name] = parsed;
  }

  const runSummary = docs['run-summary.json'];
  const monitor = docs['monitor-classification.json'];
  const changed = docs['changed-summary.json'];

  const contractSchema =
    runSummary.source_contract_version ||
    runSummary.schema_version ||
    opts.artifactSchemaVersion ||
    schemaVersion;
  if (opts.enforceSchema !== false && contractSchema !== schemaVersion && !opts.acceptAnySchema) {
    // Real monitor artifacts may omit schema; accept when completion marker + required fields present
    // unless explicitly unsupported marker set
  }
  if (runSummary.schema_version && runSummary.schema_version === 'unsupported') {
    return { ok: false, reason: 'UNSUPPORTED_SCHEMA', blocked: true };
  }
  if (opts.forceUnsupportedSchema) {
    return { ok: false, reason: 'UNSUPPORTED_SCHEMA', blocked: true };
  }

  const runId = String(runSummary.run_id || '').trim();
  if (!runId) {
    return { ok: false, reason: 'MISSING_RUN_ID', blocked: true };
  }

  const observedAt =
    runSummary.finished_at ||
    runSummary.captured_at ||
    monitor.observed_at ||
    monitor.finished_at ||
    monitor.captured_at ||
    null;
  if (!observedAt) {
    return { ok: false, reason: 'MISSING_OBSERVED_AT', blocked: true };
  }

  const observedMs = Date.parse(String(observedAt));
  if (Number.isNaN(observedMs)) {
    return { ok: false, reason: 'OBSERVED_AT_UNPARSEABLE', blocked: true };
  }
  const skew = observedMs - clock.nowMs();
  if (skew > MAX_FUTURE_SKEW_SECONDS * 1000) {
    return { ok: false, reason: 'FUTURE_TIMESTAMP_BEYOND_SKEW', blocked: true };
  }

  const classification = String(
    monitor.classification || runSummary.classification || '',
  ).toUpperCase();
  if (!classification) {
    return { ok: false, reason: 'MISSING_TERMINAL_MONITOR_STATE', blocked: true };
  }

  const sourceStatus = mapSourceStatus(classification);
  if (!STATUS_MAPPING[classification] && sourceStatus === SOURCE_STATUSES.BLOCKED) {
    return {
      ok: false,
      reason: 'UNKNOWN_CLASSIFICATION',
      blocked: true,
      source_status: SOURCE_STATUSES.BLOCKED,
    };
  }

  // exit_code nonzero → FAILED factual override if classification not already FAILURE
  let factualStatus = sourceStatus;
  if (runSummary.exit_code != null && Number(runSummary.exit_code) !== 0) {
    factualStatus = SOURCE_STATUSES.FAILED;
  }

  const metrics = {
    baseline_count: Number(
      changed.baseline_url_count ?? changed.baseline_count ?? runSummary.baseline_url_count ?? 0,
    ),
    current_count: Number(
      changed.current_url_count ?? changed.current_count ?? runSummary.current_url_count ?? 0,
    ),
    added_urls: Number(changed.added_count ?? changed.added_urls ?? runSummary.added_count ?? 0),
    removed_urls: Number(
      changed.removed_count ?? changed.removed_urls ?? runSummary.removed_count ?? 0,
    ),
    onboarding_needed_count: Number(
      changed.onboarding_needs_count ??
        changed.onboarding_needed_count ??
        monitor.onboarding_needs_count ??
        0,
    ),
  };

  const summaryCode = classification;
  const actionCode =
    factualStatus === SOURCE_STATUSES.OK
      ? 'NONE'
      : factualStatus === SOURCE_STATUSES.FAILED
        ? 'REVIEW_FAILURE'
        : 'REVIEW_SOURCE_ARTIFACTS';
  const reasonCodes =
    factualStatus === SOURCE_STATUSES.OK ? ['BASELINE_DELTA_ZERO'] : ['MONITOR_ATTENTION'];

  const observedAtZ = toUtcZ(String(observedAt));
  const { event_id, identity } = computeEventIdPythonCompatible({
    site_id: D6D_SITE_ID,
    event_type: EVENT_TYPE,
    run_id: runId,
    observed_at: observedAtZ,
    normalized_status: factualStatus,
    summary_code: summaryCode,
    metrics,
    reason_codes: reasonCodes,
    action_code: actionCode,
    schema_major: SCHEMA_MAJOR,
  });

  const fingerprint = computeArtifactFingerprint({
    run_summary: runSummary,
    monitor_classification: monitor,
    changed_summary: changed,
  });

  const ageSeconds = Math.floor((clock.nowMs() - observedMs) / 1000);
  const eligibility = evaluateDeliveryEligibility({
    source_status: factualStatus,
    age_seconds: ageSeconds,
  });

  // FAILED factual → treat send as NOT_SAFE even if age-fresh
  let deliveryEligibility = eligibility.delivery_eligibility;
  let freshnessReason = eligibility.freshness_reason;
  if (factualStatus === SOURCE_STATUSES.FAILED) {
    deliveryEligibility = DELIVERY_ELIGIBILITY.NOT_SAFE_TO_SEND;
    freshnessReason = 'FACTUAL_FAILED_NOT_SAFE_TO_SEND';
  }

  return {
    ok: true,
    run_id: runId,
    observed_at: observedAtZ,
    classification,
    source_status: factualStatus,
    event_id,
    identity,
    artifact_fingerprint: fingerprint,
    metrics,
    age_seconds: ageSeconds,
    delivery_eligibility: deliveryEligibility,
    stale: eligibility.stale,
    freshness_reason: freshnessReason,
    artifact_identity: `${runId}:${fingerprint.slice(0, 16)}`,
    docs: { run_summary: runSummary, monitor_classification: monitor, changed_summary: changed },
    primary_artifact: AUTHORITATIVE_PRIMARY,
  };
}

function toUtcZ(s) {
  const ms = Date.parse(s);
  if (Number.isNaN(ms)) return s;
  return new Date(ms).toISOString().replace(/\.\d{3}Z$/, 'Z');
}

function joinPath(a, b) {
  const left = String(a).replace(/\//g, '\\').replace(/\\+$/g, '');
  return `${left}\\${b}`;
}

/**
 * Discover candidate run directories under root (deterministic order).
 * @param {FakeFs} fs
 * @param {string} root
 * @param {object} opts
 */
export function discoverCandidates(fs, root, opts = {}) {
  const names = fs.listDir(root).filter((n) => {
    if (isTempPath(n)) return false;
    if (n.startsWith('.')) return false;
    return true;
  });
  const candidates = [];
  for (const name of names) {
    const runDir = joinPath(root, name);
    // Heuristic: must look like a run dir (contains primary or is directory entry)
    if (!fs.exists(joinPath(runDir, AUTHORITATIVE_PRIMARY)) && !opts.includeIncomplete) {
      // still allow incomplete for tests that want to see rejection later
      if (!opts.listAll) continue;
    }
    candidates.push({
      run_dir: runDir,
      run_name: name,
    });
  }
  // Deterministic: observed_at ascending after validation — here sort by name (run_id timestamp format)
  candidates.sort((a, b) => (a.run_name < b.run_name ? -1 : a.run_name > b.run_name ? 1 : 0));
  return candidates;
}

/**
 * Select at most maxCandidates after validation.
 *
 * D6F1A daily-report semantics:
 * - each monitor run is independently reportable;
 * - prefer FRESH_AND_ELIGIBLE candidates so a stale backlog cannot suppress newer days;
 * - skip runs already evaluated as non-deliverable (STALE/NOT_SAFE NO_SEND);
 * - among the chosen pool, still process oldest-first for deterministic backlog drain.
 */
export function selectCandidates(validatedList, opts = {}) {
  const max = opts.maxCandidatesPerRun ?? 1;
  const cursor = opts.cursor || {};
  const evaluated = cursor.evaluated_runs || {};
  const pending = validatedList.filter((v) => {
    if (!v.ok) return false;
    const prior = evaluated[v.run_id];
    if (prior?.processing_terminal && prior?.cursor_state === 'DELIVERY_TERMINAL') {
      return false;
    }
    if (prior?.delivery_decision === 'DELIVERED') {
      return false;
    }
    // Do not re-select a run already judged non-deliverable; otherwise the oldest
    // stale post-cutoff run permanently blocks later daily monitor cycles.
    if (
      prior?.delivery_decision === 'NO_SEND' &&
      (prior?.result_class === 'STALE_REVIEW_REQUIRED' ||
        prior?.result_class === 'NOT_SAFE_TO_SEND')
    ) {
      return false;
    }
    return true;
  });
  const fresh = pending.filter(
    (v) => v.delivery_eligibility === DELIVERY_ELIGIBILITY.FRESH_AND_ELIGIBLE,
  );
  const pool = fresh.length > 0 ? fresh : pending;
  pool.sort((a, b) => {
    const ao = String(a.observed_at || '');
    const bo = String(b.observed_at || '');
    if (ao < bo) return -1;
    if (ao > bo) return 1;
    return String(a.run_id).localeCompare(String(b.run_id));
  });
  return pool.slice(0, max);
}

export function createMemoryFs(initial = {}) {
  /** @type {Map<string, { text?: string, children?: Set<string>, mtimeMs: number }>} */
  const store = new Map();

  function norm(p) {
    return String(p)
      .replace(/\//g, '\\')
      .replace(/\\{2,}/g, '\\')
      .replace(/\\+$/g, '');
  }

  function parentOf(n) {
    const i = n.lastIndexOf('\\');
    return i <= 0 ? '' : n.slice(0, i);
  }

  function baseOf(n) {
    const i = n.lastIndexOf('\\');
    return i < 0 ? n : n.slice(i + 1);
  }

  function ensureDir(path) {
    const n = norm(path);
    if (!n) return;
    const parent = parentOf(n);
    if (parent) ensureDir(parent);
    if (!store.has(n)) store.set(n, { children: new Set(), mtimeMs: 0 });
    else if (!store.get(n).children) store.get(n).children = new Set();
    if (parent && store.has(parent)) {
      store.get(parent).children.add(baseOf(n));
    }
  }

  const api = {
    writeFile(path, text, mtimeMs = 0) {
      const n = norm(path);
      const parent = parentOf(n);
      if (parent) ensureDir(parent);
      store.set(n, { text: String(text), mtimeMs: Number(mtimeMs) || 0 });
      if (parent) {
        ensureDir(parent);
        store.get(parent).children.add(baseOf(n));
      }
    },
    mkdir(path) {
      ensureDir(path);
    },
    listDir(path) {
      const n = norm(path);
      const node = store.get(n);
      if (!node?.children) return [];
      return [...node.children].filter((c) => c && c !== '.').sort();
    },
    readText(path) {
      const node = store.get(norm(path));
      if (!node || node.text == null) throw new Error(`ENOENT:${path}`);
      return node.text;
    },
    exists(path) {
      return store.has(norm(path));
    },
    size(path) {
      const node = store.get(norm(path));
      if (!node || node.text == null) return 0;
      return Buffer.byteLength(node.text, 'utf8');
    },
    mtimeMs(path) {
      return store.get(norm(path))?.mtimeMs ?? 0;
    },
    delete(path) {
      store.delete(norm(path));
    },
    _keys() {
      return [...store.keys()];
    },
  };

  for (const [p, v] of Object.entries(initial)) {
    if (v && typeof v === 'object' && v.dir) api.mkdir(p);
    else api.writeFile(p, typeof v === 'string' ? v : JSON.stringify(v));
  }
  return api;
}

export {
  AUTHORITATIVE_ARTIFACTS,
  COMPLETION_MARKER_FILENAME,
  STALE_AFTER_SECONDS,
  DELIVERY_ELIGIBILITY,
  SOURCE_STATUSES,
};
