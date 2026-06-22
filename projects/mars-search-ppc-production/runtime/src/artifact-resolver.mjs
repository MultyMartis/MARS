import fs from 'node:fs';
import path from 'node:path';
import { ARTIFACT_OWNERS } from './constants.mjs';
import { getArtifact } from './manifest-normalize.mjs';
import { rejectArtifactEntry } from './output-class-registry.mjs';

export function resolveArtifactPath(manifest, artifactType, repoRoot) {
  const entry = getArtifact(manifest, artifactType);
  if (!entry) return { exists: false, path: null, entry: null, issues: ['not registered'] };

  if (entry.status === 'NOT APPLICABLE') {
    return { exists: true, path: null, entry, issues: [] };
  }

  if (!entry.path) {
    return { exists: false, path: null, entry, issues: ['path missing'] };
  }

  let abs;
  if (path.isAbsolute(entry.path)) {
    abs = entry.path;
  } else if (entry.path.startsWith('projects/')) {
    abs = path.resolve(repoRoot, entry.path);
  } else {
    abs = path.resolve(path.dirname(manifest._manifestPath || '.'), entry.path);
  }

  const issues = [];
  if (!fs.existsSync(abs)) {
    issues.push('file not found on disk');
  }

  if (entry.project_id && entry.project_id !== manifest.project_id) {
    issues.push(`artifact belongs to project ${entry.project_id}, not ${manifest.project_id}`);
  }

  if (entry.corpus_mode && entry.corpus_mode !== 'PRODUCTION FULL CORPUS') {
    issues.push(`corpus_mode is ${entry.corpus_mode}, not PRODUCTION FULL CORPUS`);
  }

  if (entry.status === 'DIAGNOSTIC ONLY' || entry.diagnostic_only === true) {
    issues.push('artifact is diagnostic-only');
  }

  const classCheck = rejectArtifactEntry(entry);
  if (classCheck.rejected) {
    issues.push(...classCheck.issues);
  }

  if (entry.superseded === true || entry.status === 'SUPERSEDED') {
    issues.push('artifact is superseded');
  }

  if (entry.approved === false) {
    issues.push('artifact lacks approval');
  }

  if (entry.requires_collection_date && !entry.collection_date) {
    issues.push('artifact lacks required collection date');
  }

  if (entry.requires_region && !entry.region && !manifest.region) {
    issues.push('artifact lacks required region metadata');
  }

  if (entry.generated_downstream_of) {
    issues.push(`artifact generated downstream of ${entry.generated_downstream_of} too early`);
  }

  return {
    exists: fs.existsSync(abs) && issues.length === 0,
    path: abs,
    entry,
    issues,
    owner: entry.owner_system || ARTIFACT_OWNERS[artifactType] || 'SAFE UNKNOWN',
  };
}

export function verifyRequiredArtifacts(manifest, contract, stageId, repoRoot) {
  const def = contract.stages.find((s) => s.stage_id === stageId);
  if (!def) return { valid: false, missing: [], invalid: [] };

  const missing = [];
  const invalid = [];

  for (const art of def.required_artifacts || []) {
    const resolved = resolveArtifactPath(manifest, art.artifact_type, repoRoot);
    if (!resolved.entry) {
      missing.push({
        type: 'artifact',
        id: art.artifact_type,
        owner: ARTIFACT_OWNERS[art.artifact_type] || 'SAFE UNKNOWN',
      });
    } else if (!resolved.exists) {
      invalid.push({
        type: 'artifact',
        id: art.artifact_type,
        owner: resolved.owner,
        issues: resolved.issues,
        path: resolved.path,
      });
    }
  }

  return { valid: missing.length === 0 && invalid.length === 0, missing, invalid };
}
