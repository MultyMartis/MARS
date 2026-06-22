import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
export const RUNTIME_ROOT = path.resolve(__dirname, '..');
export const INTEGRATION_ROOT = path.resolve(RUNTIME_ROOT, '..');
export const REPO_ROOT = path.resolve(INTEGRATION_ROOT, '../../../..');

export function resolveFromRepo(relPath) {
  return path.resolve(REPO_ROOT, relPath.replace(/\//g, path.sep));
}

export function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

export function writeJson(filePath, data) {
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
}

export function ensureDir(dirPath) {
  fs.mkdirSync(dirPath, { recursive: true });
}

export const RUNTIME_VERSION = 'orca-admission-integration-core-v1.0.0';

export const BLOCK_MESSAGES = {
  MISSING: 'BLOCKED — REQUIRED SEMANTIC CONTRACT NOT LOADED',
  VERSION: 'BLOCKED — SEMANTIC CONTRACT VERSION MISMATCH',
  CHECKSUM: 'BLOCKED — SEMANTIC CONTRACT CHECKSUM MISMATCH',
  INVALID_MANIFEST: 'BLOCKED — INVALID SEMANTIC CONTRACT MANIFEST',
};

export const AUTHORITATIVE_DECISIONS = new Set(['ACCEPT', 'REJECT', 'ABSTAIN']);

export const LEGACY_AUTHORITATIVE_LABELS = new Set([
  'ELIGIBLE COMMERCIAL',
  'ELIGIBLE',
  'INELIGIBLE',
  'COMMERCIAL ELIGIBLE',
  'NON-COMMERCIAL',
  'ACTIVE',
  'EXCLUDE',
]);

export const FORBIDDEN_ADMISSION_FIELDS = [
  'campaign_group',
  'export_fields',
  'cluster_id',
  'ad_group',
  'campaign_id',
  'negative_keyword',
  'ad_phrase',
];

export const NUMERIC_SENTINELS = new Set([-1, 999, -999, 0.0, 1.0]);
