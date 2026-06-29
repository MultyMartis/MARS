import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import Ajv from 'ajv';
import addFormats from 'ajv-formats';
import {
  ALLOWED_AUTHORITY_ROLES,
  APPROVED_OPERATOR_APPROVAL_STATES,
  FORBIDDEN_AUTHORITY_ROLES,
  FORBIDDEN_PATH_SEGMENTS,
  REPO_ROOT,
} from './constants.mjs';
import { assertReadablePath, normalizeInputPath } from './filesystem-guard.mjs';
import { computeSha256 } from './template-validator.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const manifestSchema = JSON.parse(
  fs.readFileSync(path.join(__dirname, '../schemas/authority-manifest.schema.json'), 'utf8')
);

const ajv = new Ajv({ allErrors: true, strict: false });
addFormats(ajv);
const validateManifestSchema = ajv.compile(manifestSchema);

/**
 * @typedef {object} LoadedAuthority
 * @property {object} manifest
 * @property {Record<string, object>} byRole
 * @property {Record<string, string>} hashes
 * @property {string} manifestPath
 */

/**
 * @param {string} manifestPath
 * @param {object} [options]
 * @returns {Promise<LoadedAuthority>}
 */
export async function loadAuthority(manifestPath, options = {}) {
  const resolvedManifest = options.skipPathGuard
    ? path.resolve(manifestPath)
    : assertReadablePath(manifestPath, options);

  const manifest = JSON.parse(fs.readFileSync(resolvedManifest, 'utf8'));

  if (!validateManifestSchema(manifest)) {
    const msg = ajv.errorsText(validateManifestSchema.errors);
    throw new Error(`Authority manifest schema invalid: ${msg}`);
  }

  if (!APPROVED_OPERATOR_APPROVAL_STATES.includes(manifest.operator_approval_state)) {
    throw new Error(
      `Unapproved authority state: ${manifest.operator_approval_state}`
    );
  }

  const byRole = {};
  const hashes = {};
  const errors = [];

  for (const entry of manifest.files) {
    const { role, path: filePath, sha256: expectedSha, required } = entry;

    if (FORBIDDEN_AUTHORITY_ROLES.includes(role)) {
      errors.push({ code: 'FORBIDDEN_ROLE', message: `Forbidden authority role: ${role}` });
      continue;
    }
    if (!ALLOWED_AUTHORITY_ROLES.includes(role)) {
      errors.push({ code: 'UNKNOWN_ROLE', message: `Unknown authority role: ${role}` });
      continue;
    }
    if (byRole[role]) {
      errors.push({ code: 'DUPLICATE_ROLE', message: `Duplicate authority role: ${role}` });
      continue;
    }

    let absPath;
    try {
      absPath = normalizeInputPath(filePath);
    } catch (err) {
      errors.push({ code: 'PATH_REJECTED', message: `${role}: ${err.message}` });
      continue;
    }

    if (!absPath.toLowerCase().startsWith(path.normalize(REPO_ROOT).toLowerCase())) {
      errors.push({
        code: 'PATH_OUTSIDE_REPO',
        message: `${role}: path outside ${REPO_ROOT}`,
      });
      continue;
    }

    const lower = absPath.toLowerCase();
    if (lower.endsWith('.xlsx') || lower.endsWith('.xls')) {
      errors.push({
        code: 'XLSX_AS_AUTHORITY',
        message: `${role}: generated XLSX cannot be used as authority`,
      });
      continue;
    }

    for (const seg of FORBIDDEN_PATH_SEGMENTS) {
      if (lower.includes(seg.replace(/\\/g, '/').toLowerCase())) {
        errors.push({
          code: 'FORBIDDEN_PATH_SEGMENT',
          message: `${role}: forbidden path segment "${seg}" in ${absPath}`,
        });
      }
    }

    if (!fs.existsSync(absPath)) {
      if (required) {
        errors.push({ code: 'MISSING_FILE', message: `${role}: missing required file ${absPath}` });
      }
      continue;
    }

    const actualSha = await computeSha256(absPath);
    hashes[role] = actualSha;

    if (expectedSha && actualSha !== expectedSha.toLowerCase()) {
      errors.push({
        code: 'SHA_MISMATCH',
        message: `${role}: SHA mismatch expected ${expectedSha}, got ${actualSha}`,
        role,
        expected: expectedSha,
        actual: actualSha,
      });
      continue;
    }

    let parsed;
    try {
      parsed = JSON.parse(fs.readFileSync(absPath, 'utf8'));
    } catch (err) {
      errors.push({ code: 'PARSE_ERROR', message: `${role}: ${err.message}` });
      continue;
    }

    byRole[role] = parsed;
  }

  if (errors.length > 0) {
    const err = new Error('Authority load failed');
    err.errors = errors;
    throw err;
  }

  return { manifest, byRole, hashes, manifestPath: resolvedManifest };
}

export function getRoleData(loaded, role) {
  return loaded.byRole[role] ?? null;
}
