/**
 * V9-05C — Bounded project filesystem read-only adapter.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { validateAdmissionToken } from '../src/admission-token.mjs';
import { redactWpConfigMetadata } from '../src/baseline-capture.mjs';
import { RUNTIME_REASON_CODES as RC } from '../src/runtime-reason-codes.mjs';

export const ADAPTER_PHASE = 'V9-05C';
const MAX_FILES = 200;

function denyDirectAccess() {
  const err = new Error('RT_DIRECT_ADAPTER_DENIED');
  err.code = RC.RT_DIRECT_ADAPTER_DENIED;
  throw err;
}

function assertToken(token, request) {
  const validation = validateAdmissionToken(token, request);
  if (!validation.valid) {
    const err = new Error(validation.reason_codes.join(','));
    err.code = validation.reason_codes[0];
    throw err;
  }
}

function boundedFileInventory(dirPath, maxFiles = MAX_FILES) {
  const files = [];
  function walk(dir, depth = 0) {
    if (depth > 8 || files.length >= maxFiles) return;
    let entries;
    try {
      entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch {
      return;
    }
    for (const entry of entries) {
      if (files.length >= maxFiles) return;
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        walk(full, depth + 1);
      } else {
        let stat;
        try {
          stat = fs.lstatSync(full);
        } catch {
          continue;
        }
        files.push({
          relative_path: full,
          size: stat.size,
          mtime: stat.mtime.toISOString(),
        });
      }
    }
  }
  walk(dirPath);
  return files;
}

function hashFile(filePath) {
  try {
    const content = fs.readFileSync(filePath);
    return crypto.createHash('sha256').update(content).digest('hex');
  } catch {
    return null;
  }
}

export function inspectProjectThemeInventory(siteRoot, token, request) {
  if (!token) denyDirectAccess();
  assertToken(token, request);
  const themeDir = path.join(siteRoot, 'wp-content', 'themes', 'shpigovsky');
  const files = boundedFileInventory(themeDir);
  return {
    operation_id: 'wp.inspect.theme',
    report_type: 'project_theme_inventory',
    status: 'SUCCEEDED',
    theme_slug: 'shpigovsky',
    file_count: files.length,
    files: files.map((f) => ({
      path: path.relative(siteRoot, f.relative_path).replace(/\\/g, '/'),
      size: f.size,
      mtime: f.mtime,
    })),
    read_only: true,
    phase: ADAPTER_PHASE,
  };
}

export function inspectProjectPluginInventory(siteRoot, token, request) {
  if (!token) denyDirectAccess();
  assertToken(token, request);
  const pluginDir = path.join(siteRoot, 'wp-content', 'plugins', 'shpigovsky-core');
  const files = boundedFileInventory(pluginDir);
  return {
    operation_id: 'wp.inspect.functionality_plugin',
    report_type: 'project_plugin_inventory',
    status: 'SUCCEEDED',
    plugin_slug: 'shpigovsky-core',
    file_count: files.length,
    files: files.map((f) => ({
      path: path.relative(siteRoot, f.relative_path).replace(/\\/g, '/'),
      size: f.size,
      mtime: f.mtime,
    })),
    read_only: true,
    phase: ADAPTER_PHASE,
  };
}

export function inspectAcfJsonState(siteRoot, token, request) {
  if (!token) denyDirectAccess();
  assertToken(token, request);
  const acfDir = path.join(siteRoot, 'wp-content', 'plugins', 'shpigovsky-core', 'acf-json');
  let entries = [];
  let exists = false;
  try {
    exists = fs.lstatSync(acfDir).isDirectory();
    if (exists) {
      entries = fs.readdirSync(acfDir).filter((f) => f.endsWith('.json'));
    }
  } catch {
    exists = false;
  }
  return {
    operation_id: 'wp.inspect.content_model',
    report_type: 'acf_json_state',
    status: 'SUCCEEDED',
    acf_json_directory: path.relative(siteRoot, acfDir).replace(/\\/g, '/'),
    directory_exists: exists,
    json_file_count: entries.length,
    json_files: entries.sort(),
    read_only: true,
    phase: ADAPTER_PHASE,
  };
}

export function inspectMuPluginAndMetadata(siteRoot, token, request) {
  if (!token) denyDirectAccess();
  assertToken(token, request);
  const muPath = path.join(siteRoot, 'wp-content', 'mu-plugins', 'mars-local-runtime.php');
  const wpConfig = redactWpConfigMetadata(siteRoot);
  let mu = { exists: false, sha256: null, size: null };
  try {
    const stat = fs.lstatSync(muPath);
    if (stat.isFile()) {
      mu = {
        exists: true,
        sha256: hashFile(muPath),
        size: stat.size,
        mtime: stat.mtime.toISOString(),
      };
    }
  } catch {
    mu.exists = false;
  }

  const versionPath = path.join(siteRoot, 'wp-includes', 'version.php');
  let wpVersion = null;
  try {
    const content = fs.readFileSync(versionPath, 'utf8');
    const match = content.match(/\$wp_version\s*=\s*['"]([^'"]+)['"]/);
    if (match) wpVersion = match[1];
  } catch {
    wpVersion = null;
  }

  return {
    operation_id: 'wp.inspect.runtime',
    report_type: 'mu_plugin_and_metadata',
    status: 'SUCCEEDED',
    mu_plugin: mu,
    wp_version: wpVersion,
    wp_config_safe_fields: wpConfig.safe_fields,
    read_only: true,
    phase: ADAPTER_PHASE,
  };
}

const ADAPTER_MAP = Object.freeze({
  inspectProjectThemeInventory,
  inspectProjectPluginInventory,
  inspectAcfJsonState,
  inspectMuPluginAndMetadata,
});

export function executeProjectFilesystemAdapter(adapterModule, siteRoot, token, request) {
  const fn = ADAPTER_MAP[adapterModule];
  if (!fn) {
    const err = new Error(RC.RT_BINDING_NOT_FOUND);
    err.code = RC.RT_BINDING_NOT_FOUND;
    throw err;
  }
  return fn(siteRoot, token, request);
}

export default {
  inspectProjectThemeInventory,
  inspectProjectPluginInventory,
  inspectAcfJsonState,
  inspectMuPluginAndMetadata,
  executeProjectFilesystemAdapter,
};
