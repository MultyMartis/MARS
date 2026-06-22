import fs from 'node:fs';
import path from 'node:path';
import {
  SOURCE_CLASSES,
  loadJson,
  writeJson,
  sha256File,
  nowIso,
} from './utils.mjs';

const REQUIRED_FIELDS = [
  'source_id',
  'project_id',
  'source_class',
  'source_title',
  'source_path',
  'collection_start',
  'collection_end',
  'imported_at',
  'region',
  'timezone',
  'collection_method',
  'tool_runtime_version',
  'operator_tool',
  'raw_row_count',
  'content_checksum',
  'limitations',
  'use_authority',
  'status',
  'related_lifecycle_stage',
];

export function validateSourceRecord(record) {
  const issues = [];
  for (const field of REQUIRED_FIELDS) {
    if (record[field] == null || record[field] === '') {
      issues.push(`missing: ${field}`);
    }
  }
  if (record.source_class && !SOURCE_CLASSES.includes(record.source_class)) {
    issues.push(`invalid source_class: ${record.source_class}`);
  }
  if (record.source_class === 'SYNTHETIC / TEST' && record.use_authority === 'production') {
    issues.push('SYNTHETIC / TEST cannot have production use_authority');
  }
  if (!record.collection_start && !record.imported_at) {
    issues.push('missing collection date');
  }
  return { valid: issues.length === 0, issues };
}

export function registerSource({ registryPath, record }) {
  const working = { ...record };
  if (working.source_path && !path.isAbsolute(working.source_path)) {
    // allow relative paths at call site — caller may resolve before invoke
  }
  if (working.source_path && fs.existsSync(working.source_path) && !working.content_checksum) {
    working.content_checksum = sha256File(working.source_path);
  }

  const validation = validateSourceRecord(working);
  if (!validation.valid) {
    return {
      ok: false,
      blockers: validation.issues,
      message: validation.issues.includes('missing collection date')
        ? 'BLOCKED — SOURCE MISSING COLLECTION DATE'
        : 'BLOCKED — SOURCE REGISTRATION INVALID',
    };
  }

  if (!working.imported_at) working.imported_at = nowIso();

  let registry = { schema_version: '1.0.0', sources: [] };
  if (fs.existsSync(registryPath)) {
    registry = loadJson(registryPath);
  }

  const idx = registry.sources.findIndex((s) => s.source_id === working.source_id);
  if (idx >= 0) registry.sources[idx] = working;
  else registry.sources.push(working);

  registry.updated_at = nowIso();
  writeJson(registryPath, registry);

  return { ok: true, registry_path: registryPath, source_id: working.source_id };
}
