import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
export const PRODUCTION_ROOT = path.resolve(__dirname, '..');
export const ORCA_SI_ROOT = path.resolve(PRODUCTION_ROOT, '..');
export const REPO_ROOT = path.resolve(ORCA_SI_ROOT, '../../..');
export const INTEGRATION_RUNTIME = path.join(ORCA_SI_ROOT, 'integration/runtime/src');

export const PRODUCTION_VERSION = 'orca-semantic-production-v1.0.0';
export const BLOCKERS = {
  COUNT_MISMATCH: 'BLOCKED — FULL-CORPUS SEMANTIC RUN COUNTS DO NOT RECONCILE',
  NEGATIVE_CONFLICT: 'BLOCKED — NEGATIVE INTELLIGENCE CONFLICTS WITH ACCEPTED DEMAND',
  FROZEN_PROJECT: 'BLOCKED — FROZEN PROJECT EXECUTION',
  MISSING_REGISTRY: 'BLOCKED — MISSING SERVICE REGISTRY',
  CONTRACT_CHECKSUM: 'BLOCKED — SEMANTIC CONTRACT CHECKSUM MISMATCH',
  PARTIAL_COMPLETE: 'BLOCKED — PARTIAL RUN CANNOT BE MARKED COMPLETE',
  DIAGNOSTIC_SUBSTITUTION: 'BLOCKED — DIAGNOSTIC SAMPLE SUBSTITUTED FOR FULL CORPUS',
};

export const FINAL_DECISIONS = new Set(['FINAL ACCEPT', 'FINAL REJECT', 'FINAL ABSTAIN']);
export const ADJUDICATION_ESCALATIONS = new Set(['ESCALATE POLICY CONFLICT', 'ESCALATE DOMAIN CONFLICT', 'INVALID RECORD']);

export function readJson(p) {
  return JSON.parse(fs.readFileSync(p, 'utf8'));
}

export function writeJson(p, data) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, `${JSON.stringify(data, null, 2)}\n`, 'utf8');
}

export function sha256Text(text) {
  return crypto.createHash('sha256').update(text).digest('hex').toUpperCase();
}

export function sha256Json(obj) {
  return sha256Text(JSON.stringify(obj));
}

export function stablePhraseId(normalized, sourceId = 'prod') {
  return `PHR-${crypto.createHash('sha256').update(`${sourceId}::${normalized}`).digest('hex').slice(0, 12).toUpperCase()}`;
}

export function resolveRepo(rel) {
  return path.resolve(REPO_ROOT, rel.replace(/\//g, path.sep));
}
