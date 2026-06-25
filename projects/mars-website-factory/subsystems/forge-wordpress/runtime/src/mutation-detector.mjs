/**
 * FW-07C-1 — Baseline mutation detector (compare before/after metadata).
 */
import { RUNTIME_REASON_CODES as RC } from './runtime-reason-codes.mjs';

/**
 * Compare two baselines for unexpected mutations.
 * @returns {{ unchanged: boolean, violations: string[], diff: object }}
 */
export function detectMutation(before, after) {
  const violations = [];
  const diff = {};

  const compareFields = [
    'file_count',
    'directory_count',
    'aggregate_size',
    'latest_modified_timestamp',
  ];

  for (const field of compareFields) {
    if (before[field] !== after[field]) {
      violations.push(`FIELD_CHANGED:${field}`);
      diff[field] = { before: before[field], after: after[field] };
    }
  }

  const beforeNames = [...(before.top_level_entry_names || [])].sort().join('|');
  const afterNames = [...(after.top_level_entry_names || [])].sort().join('|');
  if (beforeNames !== afterNames) {
    violations.push('TOP_LEVEL_ENTRIES_CHANGED');
    diff.top_level_entry_names = {
      before: before.top_level_entry_names,
      after: after.top_level_entry_names,
    };
  }

  const beforeHashes = (before.allowlisted_hashes || [])
    .filter((h) => h.exists && h.sha256)
    .map((h) => `${h.filename}:${h.sha256}`)
    .sort()
    .join('|');
  const afterHashes = (after.allowlisted_hashes || [])
    .filter((h) => h.exists && h.sha256)
    .map((h) => `${h.filename}:${h.sha256}`)
    .sort()
    .join('|');
  if (beforeHashes !== afterHashes) {
    violations.push('ALLOWLISTED_HASH_CHANGED');
    diff.allowlisted_hashes = { before: before.allowlisted_hashes, after: after.allowlisted_hashes };
  }

  if ((after.audit_files_created || []).length > 0) {
    violations.push('AUDIT_FILES_CREATED_IN_RUNTIME');
    diff.audit_files_created = after.audit_files_created;
  }

  const unchanged = violations.length === 0;

  return {
    unchanged,
    violations,
    diff,
    verdict: unchanged ? 'NO_MUTATION' : 'FW07C1_READ_ONLY_VIOLATION',
    reason_codes: unchanged ? [] : [RC.RT_MUTATION_DETECTED],
    emergency_stop: !unchanged,
  };
}

export default detectMutation;
