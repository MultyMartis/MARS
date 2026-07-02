/**
 * FW-07C-1 — Runtime authority resolver (read-only metadata, no mutation).
 */
import fs from 'node:fs';
import path from 'node:path';

export const RUNTIME_PARENT = 'X:\\MARS-Localhost';
export const PROTECTED_RUNTIME_PARENT = RUNTIME_PARENT;

const _registeredSites = {
  'fws-0001': Object.freeze({
    site_id: 'fws-0001',
    runtime_id: 'MLI-WP-SYN-001',
    environment: 'LOCAL_SYNTHETIC',
    allowed_root: 'X:\\MARS-Localhost\\sites\\wordpress\\synthetic\\fws-0001',
    runtime_class: 'synthetic',
    mli_manifest: 'projects/mars-localhost-infrastructure/manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md',
  }),
  'fp-0002-shpigovsky': Object.freeze({
    site_id: 'fp-0002-shpigovsky',
    project_id: 'FP-0002',
    runtime_id: 'MLI-WP-FP0002-LOCAL',
    environment: 'LOCAL_PROJECT',
    allowed_root: 'X:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky',
    domain: 'http://shpigovsky.test/',
    runtime_class: 'project',
    admission_mode: 'READ_ONLY',
    write_authorized: false,
    control_bridge: 'WPilot',
    control_bridge_build: 'v0.3.0-rc5',
    checkpoint_identity: 'foundation-002-v9-pre-implementation',
    mli_manifest: 'projects/mars-website-factory/subsystems/forge-wordpress/projects/fp-0002/README.md',
  }),
};

export const REGISTERED_SITES = _registeredSites;

/**
 * Register additional site authority for repo-local tests only.
 * Not for production runtime preflight.
 */
export function registerTestSiteAuthority(siteId, allowedRoot, overrides = {}) {
  _registeredSites[siteId] = Object.freeze({
    site_id: siteId,
    runtime_id: overrides.runtime_id ?? 'TEST-FIXTURE',
    environment: overrides.environment ?? 'LOCAL_SYNTHETIC',
    allowed_root: path.win32.normalize(allowedRoot).replace(/\//g, '\\'),
    runtime_class: overrides.runtime_class ?? 'synthetic',
    mli_manifest: overrides.mli_manifest ?? 'TEST_ONLY',
    test_fixture: true,
  });
}

/**
 * Validate site authority against MLI-aligned registry.
 * @param {string} siteId
 * @param {string} [requestedRoot]
 */
export function resolveSiteAuthority(siteId, requestedRoot = '') {
  const reason_codes = [];
  const site = _registeredSites[siteId];

  if (!site) {
    reason_codes.push('RT_AUTHORITY_SITE_UNKNOWN');
    return { valid: false, reason_codes, site: null };
  }

  const normalizedRequested = requestedRoot
    ? path.win32.normalize(requestedRoot).replace(/\//g, '\\')
    : site.allowed_root;

  const normalizedAllowed = path.win32.normalize(site.allowed_root).replace(/\//g, '\\');

  if (normalizedRequested.toUpperCase() !== normalizedAllowed.toUpperCase()) {
    reason_codes.push('RT_AUTHORITY_PATH_MISMATCH');
  }

  const parentNorm = path.win32.normalize(PROTECTED_RUNTIME_PARENT).toUpperCase();
  const rootNorm = normalizedAllowed.toUpperCase();

  if (rootNorm === parentNorm || rootNorm === parentNorm + '\\') {
    reason_codes.push('RT_AUTHORITY_PARENT_DENIED');
  }

  let exists = false;
  let isDirectory = false;
  let attributes = null;

  try {
    const stat = fs.lstatSync(normalizedAllowed);
    exists = true;
    isDirectory = stat.isDirectory();
    attributes = stat.mode;
  } catch {
    reason_codes.push('RT_AUTHORITY_PATH_MISMATCH');
  }

  if (exists && !isDirectory) {
    reason_codes.push('RT_AUTHORITY_PATH_MISMATCH');
  }

  return {
    valid: reason_codes.length === 0,
    reason_codes,
    site,
    resolved_root: normalizedAllowed,
    runtime_parent: PROTECTED_RUNTIME_PARENT,
    exists,
    is_directory: isDirectory,
    attributes,
  };
}

export function isSiteRootNotProtectedParent(siteRoot) {
  const parentNorm = path.win32.normalize(PROTECTED_RUNTIME_PARENT).toUpperCase();
  const rootNorm = path.win32.normalize(siteRoot).toUpperCase();
  return rootNorm !== parentNorm && rootNorm !== parentNorm + '\\' && rootNorm.startsWith(parentNorm + '\\');
}

export default { resolveSiteAuthority, REGISTERED_SITES, RUNTIME_PARENT };
