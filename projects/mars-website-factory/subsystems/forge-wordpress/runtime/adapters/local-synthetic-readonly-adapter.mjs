/**
 * FW-07C-1 — Local synthetic read-only adapter (INTERNAL — requires admission token).
 * Direct invocation without validated admission is DENIED.
 */
import fs from 'node:fs';
import path from 'node:path';
import { validateAdmissionToken } from '../src/admission-token.mjs';
import { redactWpConfigMetadata } from '../src/baseline-capture.mjs';
import { RUNTIME_REASON_CODES as RC } from '../src/runtime-reason-codes.mjs';

export const ADAPTER_PHASE = 'FW-07C-1';
export const MAX_THEME_SCAN = 20;
export const MAX_PLUGIN_SCAN = 50;
export const MAX_ROUTE_FILES = 100;

const SECRET_OUTPUT_PATTERNS = [
  /define\s*\(\s*['"]DB_PASSWORD['"]/i,
  /define\s*\(\s*['"]AUTH_KEY['"]/i,
  /password\s*=\s*['"][^'"]+['"]/i,
];

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
    err.reason_codes = validation.reason_codes;
    throw err;
  }
}

function scanDirectoryBounded(dirPath, maxEntries) {
  const entries = [];
  try {
    const items = fs.readdirSync(dirPath, { withFileTypes: true });
    for (const item of items.slice(0, maxEntries)) {
      const full = path.join(dirPath, item.name);
      let stat;
      try {
        stat = fs.lstatSync(full);
      } catch {
        continue;
      }
      entries.push({
        name: item.name,
        is_directory: item.isDirectory(),
        size: stat.size,
        mtime: stat.mtime.toISOString(),
      });
    }
  } catch {
    return { exists: false, entries: [] };
  }
  return { exists: true, path: dirPath, entries };
}

function readVersionPhp(siteRoot) {
  const versionPath = path.join(siteRoot, 'wp-includes', 'version.php');
  const result = { exists: false, wp_version: null };
  try {
    const stat = fs.lstatSync(versionPath);
    if (!stat.isFile()) return result;
    result.exists = true;
    const content = fs.readFileSync(versionPath, 'utf8');
    const match = content.match(/\$wp_version\s*=\s*['"]([^'"]+)['"]/);
    if (match) result.wp_version = match[1];
  } catch {
    result.exists = false;
  }
  return result;
}

function redactOutput(obj) {
  const json = JSON.stringify(obj);
  for (const pattern of SECRET_OUTPUT_PATTERNS) {
    if (pattern.test(json)) {
      const err = new Error(RC.RT_SECRET_OUTPUT_BLOCKED);
      err.code = RC.RT_SECRET_OUTPUT_BLOCKED;
      throw err;
    }
  }
  return obj;
}

/**
 * @internal — requires admission token
 */
export function inspectRuntimeStructure(siteRoot, token, request) {
  if (!token) denyDirectAccess();
  assertToken(token, request);

  const version = readVersionPhp(siteRoot);
  const wpConfig = redactWpConfigMetadata(siteRoot);
  const topLevel = scanDirectoryBounded(siteRoot, 50);

  return redactOutput({
    operation_id: 'wp.inspect.runtime',
    report_type: 'runtime_structure_inspection',
    status: 'SUCCEEDED',
    site_root: siteRoot,
    wp_version: version.wp_version,
    version_php_exists: version.exists,
    wp_config: wpConfig,
    top_level_entry_count: topLevel.entries.length,
    top_level_sample: topLevel.entries.map((e) => e.name),
    read_only: true,
    phase: ADAPTER_PHASE,
  });
}

/**
 * @internal — requires admission token
 */
export function inspectThemeMetadata(siteRoot, token, request) {
  if (!token) denyDirectAccess();
  assertToken(token, request);

  const themesDir = path.join(siteRoot, 'wp-content', 'themes');
  const themes = scanDirectoryBounded(themesDir, MAX_THEME_SCAN);
  const themeDetails = [];

  for (const entry of themes.entries) {
    if (!entry.is_directory) continue;
    const stylePath = path.join(themesDir, entry.name, 'style.css');
    let styleMeta = { theme_slug: entry.name, style_css_exists: false };
    try {
      const stat = fs.lstatSync(stylePath);
      if (stat.isFile()) {
        const head = fs.readFileSync(stylePath, 'utf8').slice(0, 2048);
        const nameMatch = head.match(/Theme Name:\s*(.+)/i);
        const versionMatch = head.match(/Version:\s*(.+)/i);
        styleMeta = {
          theme_slug: entry.name,
          style_css_exists: true,
          theme_name: nameMatch ? nameMatch[1].trim() : null,
          theme_version: versionMatch ? versionMatch[1].trim() : null,
        };
      }
    } catch {
      /* skip */
    }
    themeDetails.push(styleMeta);
  }

  return redactOutput({
    operation_id: 'wp.inspect.theme',
    report_type: 'theme_metadata_inspection',
    status: 'SUCCEEDED',
    themes_directory: themesDir,
    theme_count: themeDetails.length,
    themes: themeDetails,
    read_only: true,
    phase: ADAPTER_PHASE,
  });
}

/**
 * @internal — requires admission token
 */
export function inspectPluginDirectory(siteRoot, token, request) {
  if (!token) denyDirectAccess();
  assertToken(token, request);

  const pluginsDir = path.join(siteRoot, 'wp-content', 'plugins');
  const plugins = scanDirectoryBounded(pluginsDir, MAX_PLUGIN_SCAN);
  const pluginDetails = plugins.entries.map((e) => ({
    slug: e.name,
    is_directory: e.is_directory,
    size: e.size,
    mtime: e.mtime,
  }));

  return redactOutput({
    operation_id: 'wp.inspect.plugin_state',
    report_type: 'plugin_directory_inspection',
    status: 'SUCCEEDED',
    plugins_directory: pluginsDir,
    plugin_count: pluginDetails.length,
    plugins: pluginDetails,
    note: 'Directory metadata only — activation state requires DB (deferred)',
    read_only: true,
    phase: ADAPTER_PHASE,
  });
}

/**
 * @internal — requires admission token
 */
export function inspectRouteSourceInventory(siteRoot, token, request) {
  if (!token) denyDirectAccess();
  assertToken(token, request);

  const htaccessPath = path.join(siteRoot, '.htaccess');
  let htaccess = { exists: false, size: null, rewrite_rules_detected: false };
  try {
    const stat = fs.lstatSync(htaccessPath);
    if (stat.isFile()) {
      const content = fs.readFileSync(htaccessPath, 'utf8').slice(0, 4096);
      htaccess = {
        exists: true,
        size: stat.size,
        rewrite_rules_detected: /RewriteRule/i.test(content),
        redacted: true,
      };
    }
  } catch {
    htaccess.exists = false;
  }

  const phpInventory = [];
  const scanRoots = [
    path.join(siteRoot, 'wp-content', 'themes'),
    path.join(siteRoot, 'wp-content', 'plugins'),
  ];

  for (const root of scanRoots) {
    try {
      const items = fs.readdirSync(root, { withFileTypes: true });
      for (const item of items) {
        if (!item.isDirectory()) continue;
        const dir = path.join(root, item.name);
        try {
          const files = fs.readdirSync(dir);
          for (const f of files) {
            if (f.endsWith('.php') && phpInventory.length < MAX_ROUTE_FILES) {
              phpInventory.push(path.relative(siteRoot, path.join(dir, f)));
            }
          }
        } catch {
          /* skip */
        }
      }
    } catch {
      /* skip */
    }
  }

  return redactOutput({
    operation_id: 'wp.inspect.routes',
    report_type: 'route_source_inventory',
    status: 'SUCCEEDED',
    htaccess,
    php_source_files_sample: phpInventory.slice(0, 30),
    php_source_file_count: phpInventory.length,
    note: 'Filename inventory only — no PHP execution or DB route resolution',
    read_only: true,
    phase: ADAPTER_PHASE,
  });
}

const ADAPTER_MAP = Object.freeze({
  inspectRuntimeStructure,
  inspectThemeMetadata,
  inspectPluginDirectory,
  inspectRouteSourceInventory,
});

export function executeBoundAdapter(adapterModule, siteRoot, token, request) {
  const fn = ADAPTER_MAP[adapterModule];
  if (!fn) {
    const err = new Error(RC.RT_BINDING_NOT_FOUND);
    err.code = RC.RT_BINDING_NOT_FOUND;
    throw err;
  }
  return fn(siteRoot, token, request);
}

export default {
  inspectRuntimeStructure,
  inspectThemeMetadata,
  inspectPluginDirectory,
  inspectRouteSourceInventory,
  executeBoundAdapter,
};
