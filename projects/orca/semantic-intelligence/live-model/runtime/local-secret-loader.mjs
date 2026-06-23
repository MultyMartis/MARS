/**
 * Safe local secret file loader for Wave 3.1 live provider completion.
 * Never logs secret values; returns status summary only.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../..');

const DEFAULT_SECRET_PATH = path.join(REPO_ROOT, '.secrets/orca-live-model.env');

const REQUIRED_KEYS = [
  'OPENROUTER_API_KEY',
  'ORCA_SEMANTIC_PROVIDER',
  'ORCA_SEMANTIC_MODEL',
  'ORCA_EVAL_LIVE',
  'ORCA_EVAL_MAX_COST',
  'ORCA_EVAL_MAX_RECORDS',
  'ORCA_EVAL_BATCH_SIZE',
  'ORCA_EVAL_CONCURRENCY',
];

const NUMERIC_KEYS = new Set([
  'ORCA_EVAL_MAX_COST',
  'ORCA_EVAL_MAX_RECORDS',
  'ORCA_EVAL_BATCH_SIZE',
  'ORCA_EVAL_CONCURRENCY',
]);

const BOOLEAN_KEYS = new Set(['ORCA_EVAL_LIVE']);

/**
 * Parse a single KEY=value line. Returns null for comments/empty lines.
 */
export function parseEnvLine(line) {
  const trimmed = line.trim();
  if (!trimmed || trimmed.startsWith('#')) return null;
  const eq = trimmed.indexOf('=');
  if (eq <= 0) return { malformed: true, line: trimmed.slice(0, 20) };
  const key = trimmed.slice(0, eq).trim();
  let value = trimmed.slice(eq + 1).trim();
  if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
    value = value.slice(1, -1);
  }
  return { key, value };
}

/**
 * Validate a required key value without exposing the value.
 */
export function validateRequiredValue(key, value) {
  if (value === undefined || value === '') return { valid: false, reason: 'EMPTY' };
  if (NUMERIC_KEYS.has(key)) {
    const n = Number(value);
    if (!Number.isFinite(n) || n <= 0) return { valid: false, reason: 'INVALID_NUMERIC' };
  }
  if (BOOLEAN_KEYS.has(key) && !['0', '1', 'true', 'false'].includes(value.toLowerCase())) {
    return { valid: false, reason: 'INVALID_BOOLEAN' };
  }
  if (key === 'ORCA_SEMANTIC_PROVIDER' && !['openrouter', 'openai'].includes(value)) {
    return { valid: false, reason: 'INVALID_PROVIDER' };
  }
  return { valid: true };
}

/**
 * Load secrets from file into process.env without overwriting existing vars.
 * @param {object} options
 * @param {string} [options.secretFile] - override path (ORCA_SECRET_FILE)
 * @param {boolean} [options.overwrite=false] - if true, file values override env
 * @returns {object} safe status summary — no secret values
 */
export function loadLocalSecrets(options = {}) {
  const secretFile = options.secretFile || process.env.ORCA_SECRET_FILE || DEFAULT_SECRET_PATH;
  const overwrite = options.overwrite === true;
  const summary = {
    secret_file: secretFile,
    file_exists: false,
    file_readable: false,
    keys_loaded: 0,
    keys_skipped_existing: 0,
    keys_malformed: 0,
    required_status: {},
    load_status: 'NOT_LOADED',
    error: null,
  };

  for (const key of REQUIRED_KEYS) {
    summary.required_status[key] = process.env[key] ? 'SET' : 'NOT SET';
  }

  if (!fs.existsSync(secretFile)) {
    summary.load_status = 'FILE_MISSING';
    return summary;
  }
  summary.file_exists = true;

  let content;
  try {
    content = fs.readFileSync(secretFile, 'utf8');
    summary.file_readable = true;
  } catch {
    summary.load_status = 'FILE_UNREADABLE';
    summary.error = 'FILE_UNREADABLE';
    return summary;
  }

  const parsed = {};
  for (const line of content.split(/\r?\n/)) {
    const row = parseEnvLine(line);
    if (!row) continue;
    if (row.malformed) {
      summary.keys_malformed++;
      continue;
    }
    parsed[row.key] = row.value;
  }

  for (const [key, value] of Object.entries(parsed)) {
    if (!overwrite && process.env[key] !== undefined) {
      summary.keys_skipped_existing++;
      summary.required_status[key] = 'SET';
      continue;
    }
    const validation = REQUIRED_KEYS.includes(key) ? validateRequiredValue(key, value) : { valid: true };
    if (!validation.valid) {
      summary.load_status = 'MALFORMED_REQUIRED';
      summary.error = `${key}:${validation.reason}`;
      return summary;
    }
    process.env[key] = value;
    summary.keys_loaded++;
    if (REQUIRED_KEYS.includes(key)) {
      summary.required_status[key] = 'SET';
    }
  }

  for (const key of REQUIRED_KEYS) {
    const validation = validateRequiredValue(key, process.env[key]);
    if (!validation.valid) {
      summary.required_status[key] = validation.reason === 'EMPTY' ? 'NOT SET' : 'INVALID';
      summary.load_status = 'INCOMPLETE';
      return summary;
    }
    summary.required_status[key] = 'SET';
  }

  summary.load_status = 'LOADED';
  return summary;
}

/**
 * Safe config summary — values as categories, never raw secrets.
 */
export function getSafeConfigSummary() {
  return {
    OPENROUTER_API_KEY: process.env.OPENROUTER_API_KEY ? 'SET' : 'NOT SET',
    ORCA_SEMANTIC_PROVIDER: process.env.ORCA_SEMANTIC_PROVIDER || 'NOT SET',
    ORCA_SEMANTIC_MODEL: process.env.ORCA_SEMANTIC_MODEL || 'NOT SET',
    ORCA_EVAL_LIVE: process.env.ORCA_EVAL_LIVE === '1' ? 'enabled' : process.env.ORCA_EVAL_LIVE || 'NOT SET',
    ORCA_EVAL_MAX_COST: process.env.ORCA_EVAL_MAX_COST || 'NOT SET',
    ORCA_EVAL_MAX_RECORDS: process.env.ORCA_EVAL_MAX_RECORDS || 'NOT SET',
    ORCA_EVAL_BATCH_SIZE: process.env.ORCA_EVAL_BATCH_SIZE || 'NOT SET',
    ORCA_EVAL_CONCURRENCY: process.env.ORCA_EVAL_CONCURRENCY || 'NOT SET',
  };
}
