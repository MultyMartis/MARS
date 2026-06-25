import fs from 'node:fs';
import path from 'node:path';
import { loadJson, writeJson } from './utils.mjs';

export const RAW_FIREFOX_MANIFEST = 'capture-manifest by-firefox.json';
export const NORMALIZED_MANIFEST = 'capture-manifest.normalized.json';
export const CANONICAL_MANIFEST = 'capture-manifest.json';

const LEGACY_ID_MAP = {
  project_id: 'MIG-W2-3-TECH-PAID-SERP',
  session_id: 'w2-3-assisted-session-001',
  query_id: 'w2-3-q02',
};

export function listBundleManifestCandidates(bundleDir) {
  const candidates = [
    path.join(bundleDir, NORMALIZED_MANIFEST),
    path.join(bundleDir, RAW_FIREFOX_MANIFEST),
    path.join(bundleDir, CANONICAL_MANIFEST),
  ];
  return candidates.filter((p) => fs.existsSync(p));
}

export function isEmptyTemplateManifest(manifest) {
  return (
    !manifest?.captured_at ||
    !manifest?.device_browser ||
    !manifest?.page_url ||
    manifest?.operator_attestation?.attested !== true
  );
}

export function isAttestedCaptureManifest(manifest) {
  return Boolean(manifest?.captured_at && manifest?.operator_attestation?.attested === true);
}

export function resolveBundleHtmlRef(bundleDir, manifest) {
  const declared = manifest?.files?.html;
  const candidates = [declared, 'page.html', 'page.htm'].filter(Boolean);
  for (const name of candidates) {
    const p = path.join(bundleDir, name);
    if (fs.existsSync(p)) return name;
  }
  return declared || 'page.html';
}

export function normalizeLegacyIds(manifest, expected = LEGACY_ID_MAP) {
  const out = { ...manifest };
  if (manifest.query !== 'ремонт квартир под ключ') {
    return { ...out, normalization_blocked: 'QUERY_MISMATCH' };
  }
  if (manifest.region_lr !== 213 && manifest.region_lr != null) {
    return { ...out, normalization_blocked: 'REGION_LR_MISMATCH' };
  }
  out.project_id = expected.project_id;
  out.session_id = expected.session_id;
  out.query_id = expected.query_id;
  return out;
}

export function buildNormalizedManifest({ firefoxManifest, bundleDir, expectedIds = LEGACY_ID_MAP }) {
  const htmlRef = resolveBundleHtmlRef(bundleDir, firefoxManifest);
  const base = normalizeLegacyIds(firefoxManifest, expectedIds);
  if (base.normalization_blocked) {
    throw new Error(`LEGACY ID NORMALIZATION BLOCKED: ${base.normalization_blocked}`);
  }

  return {
    schema_version: firefoxManifest.schema_version || '1.0.0',
    acquisition_mode: firefoxManifest.acquisition_mode || 'OPERATOR-ASSISTED LIVE SERP CAPTURE',
    project_id: base.project_id,
    session_id: base.session_id,
    query_id: base.query_id,
    query: firefoxManifest.query,
    captured_at: firefoxManifest.captured_at,
    timezone: firefoxManifest.timezone || 'Europe/Moscow',
    region: firefoxManifest.region,
    region_lr: firefoxManifest.region_lr,
    device_browser: firefoxManifest.device_browser,
    page_url: firefoxManifest.page_url,
    page_title: firefoxManifest.page_title,
    files: {
      screenshot: firefoxManifest.files?.screenshot || 'screenshot.png',
      html: htmlRef,
    },
    operator_attestation: { ...firefoxManifest.operator_attestation },
    production_authority: false,
    technical_test_only: true,
    provenance: {
      raw_manifest: RAW_FIREFOX_MANIFEST,
      normalization_reason: 'LEGACY CAPTURE SNIPPET IDS NORMALIZED TO ACTIVE WAVE 2.3 TECHNICAL PROJECT',
      legacy_project_id: firefoxManifest.project_id,
      legacy_session_id: firefoxManifest.session_id,
      legacy_query_id: firefoxManifest.query_id,
    },
  };
}

export function selectCanonicalManifest(bundleDir) {
  const normalizedPath = path.join(bundleDir, NORMALIZED_MANIFEST);
  if (fs.existsSync(normalizedPath)) {
    return { path: normalizedPath, manifest: loadJson(normalizedPath), source: NORMALIZED_MANIFEST };
  }

  const firefoxPath = path.join(bundleDir, RAW_FIREFOX_MANIFEST);
  if (fs.existsSync(firefoxPath)) {
    const firefox = loadJson(firefoxPath);
    if (isAttestedCaptureManifest(firefox)) {
      const built = buildNormalizedManifest({ firefoxManifest: firefox, bundleDir });
      return { path: normalizedPath, manifest: built, source: RAW_FIREFOX_MANIFEST, built_on_read: true };
    }
  }

  const templatePath = path.join(bundleDir, CANONICAL_MANIFEST);
  if (fs.existsSync(templatePath)) {
    const template = loadJson(templatePath);
    if (!isEmptyTemplateManifest(template)) {
      return { path: templatePath, manifest: template, source: CANONICAL_MANIFEST };
    }
  }

  return { path: templatePath, manifest: templatePath && fs.existsSync(templatePath) ? loadJson(templatePath) : null, source: 'none' };
}

export function writeNormalizedBundleManifests(bundleDir, { syncCanonical = true } = {}) {
  const firefoxPath = path.join(bundleDir, RAW_FIREFOX_MANIFEST);
  if (!fs.existsSync(firefoxPath)) {
    throw new Error(`RAW FIREFOX MANIFEST MISSING: ${RAW_FIREFOX_MANIFEST}`);
  }
  const firefox = loadJson(firefoxPath);
  const normalized = buildNormalizedManifest({ firefoxManifest: firefox, bundleDir });
  const normalizedPath = path.join(bundleDir, NORMALIZED_MANIFEST);
  writeJson(normalizedPath, normalized);
  if (syncCanonical) {
    writeJson(path.join(bundleDir, CANONICAL_MANIFEST), normalized);
  }
  return { normalizedPath, manifest: normalized };
}
