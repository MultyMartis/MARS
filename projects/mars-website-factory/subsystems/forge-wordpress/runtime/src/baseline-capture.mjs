/**
 * FW-07C-1 — Runtime metadata baseline capture (read-only, bounded).
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { validateReparseBoundary } from './reparse-boundary-validator.mjs';

export const DEFAULT_BASELINE_LIMITS = Object.freeze({
  max_files: 50000,
  max_directories: 10000,
  max_depth: 8,
  skip_dirs: new Set([
    'node_modules',
    'vendor',
    'uploads',
    'cache',
    'upgrade',
    'backup',
    'backups',
  ]),
});

export const ALLOWLISTED_HASH_FILES = Object.freeze([
  'index.php',
  'license.txt',
  'readme.html',
  '.htaccess',
]);

const SECRET_PATTERNS = [
  /DB_PASSWORD/i,
  /AUTH_KEY/i,
  /SECURE_AUTH_KEY/i,
  /LOGGED_IN_KEY/i,
  /NONCE_KEY/i,
  /AUTH_SALT/i,
  /SECURE_AUTH_SALT/i,
  /LOGGED_IN_SALT/i,
  /NONCE_SALT/i,
];

/**
 * Bounded recursive metadata walk — read-only stat only.
 */
function walkMetadata(rootDir, limits, state, depth = 0) {
  if (depth > limits.max_depth) return;
  if (state.file_count >= limits.max_files) {
    state.truncated = true;
    return;
  }

  let entries;
  try {
    entries = fs.readdirSync(rootDir, { withFileTypes: true });
  } catch {
    return;
  }

  for (const entry of entries) {
    if (state.file_count >= limits.max_files || state.directory_count >= limits.max_directories) {
      state.truncated = true;
      return;
    }

    const fullPath = path.join(rootDir, entry.name);

    let stat;
    try {
      stat = fs.lstatSync(fullPath);
    } catch {
      continue;
    }

    const mtime = stat.mtimeMs;
    if (mtime > state.latest_mtime_ms) {
      state.latest_mtime_ms = mtime;
      state.latest_mtime_path = fullPath;
    }
    state.aggregate_size += stat.size;

    if (entry.isDirectory()) {
      state.directory_count += 1;
      if (!limits.skip_dirs.has(entry.name.toLowerCase())) {
        walkMetadata(fullPath, limits, state, depth + 1);
      }
    } else {
      state.file_count += 1;
    }
  }
}

function hashAllowlistedFile(siteRoot, filename) {
  const filePath = path.join(siteRoot, filename);
  try {
    const stat = fs.lstatSync(filePath);
    if (!stat.isFile()) return { filename, exists: false, sha256: null };
    const content = fs.readFileSync(filePath);
    return {
      filename,
      exists: true,
      size: stat.size,
      mtime_ms: stat.mtimeMs,
      sha256: crypto.createHash('sha256').update(content).digest('hex'),
    };
  } catch {
    return { filename, exists: false, sha256: null };
  }
}

/**
 * Redacted wp-config structural metadata — no secret values.
 */
export function redactWpConfigMetadata(siteRoot) {
  const configPath = path.join(siteRoot, 'wp-config.php');
  const result = {
    exists: false,
    path: configPath,
    safe_fields: {},
    secret_keys_detected: [],
    redacted: true,
  };

  try {
    const stat = fs.lstatSync(configPath);
    if (!stat.isFile()) return result;
    result.exists = true;
    result.size = stat.size;
    result.mtime_ms = stat.mtimeMs;

    const content = fs.readFileSync(configPath, 'utf8');
    for (const pattern of SECRET_PATTERNS) {
      const match = content.match(new RegExp(`define\\s*\\(\\s*['"](${pattern.source.replace(/\\/g, '')})['"]`, 'i'));
      if (match) {
        result.secret_keys_detected.push(match[1]);
      }
    }

    const safePatterns = {
      DB_NAME: /define\s*\(\s*['"]DB_NAME['"]\s*,\s*['"]([^'"]+)['"]/,
      DB_HOST: /define\s*\(\s*['"]DB_HOST['"]\s*,\s*['"]([^'"]+)['"]/,
      table_prefix: /\$table_prefix\s*=\s*['"]([^'"]+)['"]/,
      WP_DEBUG: /define\s*\(\s*['"]WP_DEBUG['"]\s*,\s*(true|false)/i,
    };

    for (const [key, regex] of Object.entries(safePatterns)) {
      const m = content.match(regex);
      if (m) result.safe_fields[key] = m[1];
    }
  } catch {
    result.exists = false;
  }

  return result;
}

/**
 * Capture full metadata baseline for a site root.
 */
export function captureBaseline(siteRoot, limits = DEFAULT_BASELINE_LIMITS) {
  const resolved = fs.realpathSync.native(siteRoot);
  const reparse = validateReparseBoundary(siteRoot, siteRoot);

  let topLevel = [];
  try {
    topLevel = fs.readdirSync(resolved, { withFileTypes: true }).map((e) => ({
      name: e.name,
      is_directory: e.isDirectory(),
      is_symlink: e.isSymbolicLink(),
    }));
  } catch {
    topLevel = [];
  }

  let rootStat;
  try {
    rootStat = fs.lstatSync(resolved);
  } catch {
    rootStat = null;
  }

  const walkState = {
    file_count: 0,
    directory_count: 0,
    aggregate_size: 0,
    latest_mtime_ms: 0,
    latest_mtime_path: '',
    truncated: false,
  };

  walkMetadata(resolved, limits, walkState);

  const allowlisted_hashes = ALLOWLISTED_HASH_FILES.map((f) => hashAllowlistedFile(resolved, f));
  const wp_config_metadata = redactWpConfigMetadata(resolved);

  const volume = /^([A-Za-z]:)/.exec(resolved)?.[1]?.toUpperCase() + '\\' ?? '';

  return {
    captured_at: new Date().toISOString(),
    site_root: siteRoot,
    resolved_absolute_path: resolved,
    volume,
    directory_exists: rootStat !== null && rootStat.isDirectory(),
    directory_attributes: rootStat?.mode ?? null,
    is_reparse_point: rootStat?.isSymbolicLink?.() ?? false,
    immediate_parent: path.dirname(resolved),
    top_level_entry_names: topLevel.map((e) => e.name).sort(),
    top_level_entries: topLevel,
    file_count: walkState.file_count,
    directory_count: walkState.directory_count,
    aggregate_size: walkState.aggregate_size,
    latest_modified_timestamp: walkState.latest_mtime_ms
      ? new Date(walkState.latest_mtime_ms).toISOString()
      : null,
    latest_modified_path: walkState.latest_mtime_path,
    allowlisted_hashes,
    wp_config_metadata,
    walk_truncated: walkState.truncated,
    reparse_self_check: reparse,
    audit_files_created: [],
  };
}

export default captureBaseline;
