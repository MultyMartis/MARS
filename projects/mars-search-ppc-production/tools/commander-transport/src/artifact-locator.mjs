/**
 * Current-deliverables index contract — reusable across Search PPC pilots.
 */

/**
 * @param {object} entry
 */
export function validateArtifactLocatorEntry(entry) {
  const required = [
    'artifact_id', 'project_id', 'artifact_family', 'version', 'status',
    'audience', 'physical_path', 'current', 'protected', 'safe_to_send',
    'safe_to_import', 'safe_to_publish',
  ];
  const missing = required.filter((k) => entry[k] === undefined);
  return { valid: missing.length === 0, missing };
}

/**
 * @param {object[]} index
 * @param {object} query — { current?: boolean, artifact_family?: string }
 */
export function queryArtifactIndex(index, query = {}) {
  return index.filter((e) => {
    if (query.current === true && !e.current) return false;
    if (query.artifact_family && e.artifact_family !== query.artifact_family) return false;
    return true;
  });
}

/**
 * @param {object[]} index
 */
export function findCurrentDeliverables(index) {
  return index.filter((e) => e.current === true);
}

export const ARTIFACT_FAMILIES = Object.freeze({
  SEMANTIC_AUTHORITY: 'SEMANTIC_AUTHORITY',
  DEPLOYABLE_COMMANDER_PACKAGE: 'DEPLOYABLE_COMMANDER_PACKAGE',
  CLIENT_APPROVAL_PACK: 'CLIENT_APPROVAL_PACK',
  FINAL_PAGE_COPY: 'FINAL_PAGE_COPY',
  IMPLEMENTATION_PRODUCTION_BRIEF: 'IMPLEMENTATION_PRODUCTION_BRIEF',
  INTERNAL_REPORT: 'INTERNAL_REPORT',
  BACKUP: 'BACKUP',
});
