/**
 * FW-07C-2C — Bounded filesystem manifest with SHA-256 aggregation.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { validateReparseBoundary } from '../reparse-boundary-validator.mjs';

const SECRET_PATTERNS = [
  /password\s*[:=]/i,
  /api[_-]?key\s*[:=]/i,
  /secret\s*[:=]/i,
  /BEGIN (RSA |OPENSSH )?PRIVATE KEY/i,
  /AUTH_KEY/i,
  /DB_PASSWORD/i,
];

export function sha256Buffer(buf) {
  return crypto.createHash('sha256').update(buf).digest('hex');
}

export function sha256File(filePath) {
  const content = fs.readFileSync(filePath);
  return sha256Buffer(content);
}

export function sha256Text(text) {
  return sha256Buffer(Buffer.from(text, 'utf8'));
}

export function aggregateHash(files) {
  const sorted = [...files].sort((a, b) => a.relative_path.localeCompare(b.relative_path));
  const h = crypto.createHash('sha256');
  for (const f of sorted) {
    h.update(f.relative_path);
    h.update('\0');
    h.update(f.sha256);
    h.update('\0');
  }
  return h.digest('hex');
}

export function scanForSecrets(filePath, content) {
  const text = typeof content === 'string' ? content : content.toString('utf8');
  const hits = [];
  for (const pattern of SECRET_PATTERNS) {
    if (pattern.test(text)) {
      hits.push(pattern.source);
    }
  }
  return { file: filePath, secrets_detected: hits.length > 0, patterns: hits };
}

/**
 * Walk directory and produce manifest.
 */
export function captureDirectoryManifest(rootDir, options = {}) {
  const {
    relativeTo = rootDir,
    exclude = [],
    hashFiles = true,
    secretScan = true,
  } = options;

  const resolved = fs.realpathSync.native(rootDir);
  const reparse = validateReparseBoundary(rootDir, rootDir);
  const files = [];
  const directories = [];
  const secret_hits = [];
  let total_bytes = 0;

  function walk(dir, depth = 0) {
    if (depth > 32) return;
    let entries;
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      return;
    }

    for (const entry of entries) {
      const full = path.join(dir, entry.name);
      const rel = path.relative(relativeTo, full).replace(/\\/g, '/');

      if (exclude.some((ex) => rel === ex || rel.startsWith(ex + '/'))) continue;

      if (entry.isDirectory()) {
        directories.push(rel);
        walk(full, depth + 1);
      } else if (entry.isFile()) {
        const stat = fs.statSync(full);
        total_bytes += stat.size;
        const entry = {
          relative_path: rel,
          size: stat.size,
          sha256: null,
        };
        if (hashFiles) {
          const content = fs.readFileSync(full);
          entry.sha256 = sha256Buffer(content);
          if (secretScan) {
            const scan = scanForSecrets(rel, content);
            if (scan.secrets_detected) secret_hits.push(scan);
          }
        }
        files.push(entry);
      }
    }
  }

  walk(resolved);
  files.sort((a, b) => a.relative_path.localeCompare(b.relative_path));
  directories.sort();

  return {
    captured_at: new Date().toISOString(),
    root: rootDir,
    resolved_absolute_path: resolved,
    file_count: files.length,
    directory_count: directories.length,
    total_bytes,
    files,
    directories,
    aggregate_sha256: hashFiles ? aggregateHash(files) : null,
    reparse_points: reparse.reparse_points,
    reparse_self_check: reparse,
    secret_scan: {
      scanned: secretScan,
      hits: secret_hits,
      secrets_detected: secret_hits.length > 0,
    },
  };
}

export default {
  captureDirectoryManifest,
  sha256File,
  sha256Text,
  aggregateHash,
  scanForSecrets,
};
