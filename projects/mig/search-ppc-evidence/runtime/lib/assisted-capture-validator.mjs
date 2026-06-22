import fs from 'node:fs';
import path from 'node:path';
import { validateBusinessHoursWindow } from './business-hours.mjs';
import { loadJson, sha256File, sha256Text } from './utils.mjs';

export const ASSISTED_BLOCKER = 'BLOCKED — ASSISTED LIVE CAPTURE BUNDLE INVALID';

export function hashAssistedManifestBody(bundle) {
  const copy = JSON.parse(JSON.stringify(bundle));
  delete copy.checksums;
  return sha256Text(JSON.stringify(copy));
}

const REQUIRED_MANIFEST_FIELDS = [
  'project_id',
  'session_id',
  'query_id',
  'query',
  'captured_at',
  'timezone',
  'region',
  'device_browser',
  'page_url',
  'operator_attestation',
];

export function validateAssistedCaptureBundle({
  bundleDir,
  manifest,
  querySet,
  sessionConfig,
  projectManifest,
}) {
  const blockers = [];

  if (!bundleDir || !fs.existsSync(bundleDir)) {
    return { valid: false, blockers: [`${ASSISTED_BLOCKER}: bundle directory missing`] };
  }

  const manifestPath = path.join(bundleDir, 'capture-manifest.json');
  if (!fs.existsSync(manifestPath)) {
    blockers.push('capture-manifest.json missing');
  }

  let bundle;
  try {
    bundle = loadJson(manifestPath);
  } catch (e) {
    blockers.push(`capture-manifest.json invalid: ${e.message}`);
    return { valid: false, blockers: blockers.map((b) => `${ASSISTED_BLOCKER}: ${b}`) };
  }

  for (const field of REQUIRED_MANIFEST_FIELDS) {
    if (bundle[field] == null || bundle[field] === '') blockers.push(`missing field: ${field}`);
  }

  if (projectManifest && bundle.project_id !== projectManifest.project_id) {
    blockers.push(`project_id mismatch: ${bundle.project_id}`);
  }

  if (projectManifest?.project_mode && projectManifest.project_mode !== 'TECHNICAL TEST') {
    blockers.push('assisted capture only permitted for TECHNICAL TEST projects');
  }

  if (bundle.production_authority === true) {
    blockers.push('production_authority must be false for assisted technical capture');
  }

  if (querySet?.queries) {
    const approved = querySet.queries.find((q) => q.query_id === bundle.query_id);
    if (!approved) blockers.push(`query_id ${bundle.query_id} not in approved query set`);
    else if (approved.text !== bundle.query) blockers.push('query text does not match approved query set');
  }

  if (!bundle.captured_at) blockers.push('timestamp missing');
  if (!bundle.timezone) blockers.push('timezone missing');
  if (!bundle.region) blockers.push('region missing');

  if (sessionConfig) {
    const windowCheck = validateBusinessHoursWindow({
      projectTimezone: bundle.timezone || sessionConfig.timezone,
      currentTimestamp: bundle.captured_at,
      observationWindows: sessionConfig.allowed_local_collection_windows,
      weekdayPolicy: sessionConfig.weekday_policy,
      approvedExceptions: sessionConfig.approved_exceptions || [],
    });
    if (!windowCheck.allowed) blockers.push(`outside approved window: ${windowCheck.status}`);
  }

  const screenshotPath = resolveBundleFile(bundleDir, bundle, 'screenshot');
  const htmlPath = resolveBundleFile(bundleDir, bundle, 'html');

  if (!screenshotPath || !fs.existsSync(screenshotPath)) {
    blockers.push('screenshot missing');
  }

  if (!htmlPath && !bundle.html_limitation) {
    blockers.push('HTML/DOM missing with no html_limitation record');
  }

  if (bundle.checksums) {
    if (screenshotPath && bundle.checksums.screenshot_sha256) {
      const actual = sha256File(screenshotPath);
      if (actual !== bundle.checksums.screenshot_sha256) blockers.push('screenshot checksum mismatch');
    }
    if (htmlPath && bundle.checksums.html_sha256) {
      const actual = sha256File(htmlPath);
      if (actual !== bundle.checksums.html_sha256) blockers.push('html checksum mismatch');
    }
    if (bundle.checksums.manifest_sha256) {
      const actual = hashAssistedManifestBody(bundle);
      if (actual !== bundle.checksums.manifest_sha256) blockers.push('manifest checksum mismatch');
    }
  }

  if (!bundle.operator_attestation?.attested) {
    blockers.push('operator attestation missing or not attested');
  }

  if (bundle.manual_advertiser_rows?.length) {
    blockers.push('manual advertiser rows submitted without raw evidence');
  }

  if (bundle.registered_as_production_authority === true) {
    blockers.push('technical evidence cannot be registered as production authority');
  }

  const valid = blockers.length === 0;
  return {
    valid,
    bundle,
    bundleDir,
    manifestPath,
    screenshotPath,
    htmlPath,
    blockers: blockers.map((b) => `${ASSISTED_BLOCKER}: ${b}`),
  };
}

function resolveBundleFile(bundleDir, bundle, kind) {
  const ref = bundle.files?.[kind] || (kind === 'screenshot' ? 'screenshot.png' : 'page.html');
  if (!ref) return null;
  const p = path.join(bundleDir, ref);
  return fs.existsSync(p) ? p : null;
}
