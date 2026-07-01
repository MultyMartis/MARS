/**
 * MANUAL_STABLE artifact protection — generators must refuse overwrite.
 */

import fs from 'node:fs';
import crypto from 'node:crypto';

export const ARTIFACT_EDIT_STATES = Object.freeze({
  GENERATED: 'GENERATED',
  MANUALLY_EDITED: 'MANUALLY_EDITED',
  MANUAL_STABLE: 'MANUAL_STABLE',
  SUPERSEDED: 'SUPERSEDED',
  ARCHIVED: 'ARCHIVED',
});

/**
 * @param {string} filePath
 */
export function sha256File(filePath) {
  const data = fs.readFileSync(filePath);
  return crypto.createHash('sha256').update(data).digest('hex');
}

/**
 * @param {object} entry — { status, path, sha256, artifact_id }
 * @param {object} [options]
 */
export function checkManualStableOverwrite(entry, options = {}) {
  const violations = [];
  if (!entry || entry.status !== ARTIFACT_EDIT_STATES.MANUAL_STABLE) {
    return { allowed: true, violations };
  }
  if (!entry.path || !fs.existsSync(entry.path)) {
    violations.push({
      code: 'MANUAL_STABLE_FILE_MISSING',
      message: `MANUAL_STABLE file not found: ${entry.path}`,
    });
    return { allowed: false, violations };
  }
  const currentHash = sha256File(entry.path);
  if (entry.sha256 && currentHash !== entry.sha256) {
    violations.push({
      code: 'MANUAL_STABLE_HASH_DRIFT',
      message: `Recorded hash ${entry.sha256} != current ${currentHash}`,
      recorded: entry.sha256,
      current: currentHash,
    });
  }
  if (options.intent === 'overwrite') {
    violations.push({
      code: 'MANUAL_STABLE_OVERWRITE_REFUSED',
      message: `Generator must not overwrite MANUAL_STABLE artifact ${entry.artifact_id ?? entry.path}`,
      required_action: 'new_explicit_version_or_operator_authorization',
    });
    return { allowed: false, violations };
  }
  return { allowed: true, violations, current_hash: currentHash };
}

/**
 * @param {object[]} registry
 * @param {string} targetPath
 */
export function findManualStableEntry(registry, targetPath) {
  const norm = targetPath.replace(/\\/g, '/').toLowerCase();
  return registry.find((e) => {
    const p = String(e.path ?? '').replace(/\\/g, '/').toLowerCase();
    return p === norm || norm.endsWith(p) || p.endsWith(norm);
  });
}
