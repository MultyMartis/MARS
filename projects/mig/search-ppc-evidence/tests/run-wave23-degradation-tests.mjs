#!/usr/bin/env node
/**
 * Wave 2.3 — Approved business-hours degradation tests
 */
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath } from 'node:url';
import { validateAssistedCaptureBundle, hashAssistedManifestBody } from '../runtime/lib/assisted-capture-validator.mjs';
import { importAssistedCaptureBundle } from '../runtime/lib/assisted-capture-importer.mjs';
import { buildEvidenceManifest } from '../runtime/lib/evidence-manifest.mjs';
import { hashDegradationBody } from '../runtime/lib/approved-degradation-registry.mjs';
import { loadJson, writeJson, sha256File } from '../runtime/lib/utils.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(__dirname, '../../../..');
const FIX = path.join(__dirname, '../fixtures');
const W23_BASE = path.join(REPO, 'projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp');
const W23_MANIFEST = path.join(W23_BASE, 'project-ppc-state-manifest-v1.json');
const W23_QUERIES = path.join(W23_BASE, 'query-set-v1.json');
const W23_SESSION = path.join(W23_BASE, 'session-config-v1.json');
const LIVE_BUNDLE =
  'C:/AI MARS STORAGE/incoming/mig/live-validation/w2-3-tech-paid-serp/assisted-capture-pending/w2-3-q02';

function buildOutsideWindowBundle(tmp, overrides = {}) {
  const dir = path.join(tmp, `ow-${Math.random().toString(36).slice(2, 8)}`);
  fs.mkdirSync(dir, { recursive: true });
  fs.copyFileSync(path.join(FIX, 'assisted-capture/valid-page.html'), path.join(dir, 'page.html'));
  fs.writeFileSync(path.join(dir, 'screenshot.png'), Buffer.from('w23-ow-fixture'));
  const manifest = {
    ...loadJson(path.join(FIX, 'assisted-capture/valid-manifest-template.json')),
    project_id: 'MIG-W2-3-TECH-PAID-SERP',
    session_id: 'w2-3-assisted-session-001',
    query_id: 'w2-3-q02',
    query: 'ремонт квартир под ключ',
    captured_at: '2026-06-24T04:41:47.799Z',
    operator_attestation: { attested: true, attested_at: '2026-06-24T04:41:47.799Z', statement: 'fixture' },
    ...overrides,
  };
  writeJson(path.join(dir, 'capture-manifest.json'), manifest);
  const m = loadJson(path.join(dir, 'capture-manifest.json'));
  m.checksums = {
    screenshot_sha256: sha256File(path.join(dir, 'screenshot.png')),
    html_sha256: sha256File(path.join(dir, 'page.html')),
    manifest_sha256: hashAssistedManifestBody(m),
  };
  writeJson(path.join(dir, 'capture-manifest.json'), m);
  return dir;
}

function writeFixtureDegradation(dir, overrides = {}) {
  fs.mkdirSync(dir, { recursive: true });
  const body = {
    degradation_id: 'fixture-time-window-degradation-v1',
    operator_decision_id: 'W2.3-D8-FIXTURE',
    project_id: 'MIG-W2-3-TECH-PAID-SERP',
    session_id: 'w2-3-assisted-session-001',
    query_id: 'w2-3-q02',
    capture_timestamp: '2026-06-24T04:41:47.799Z',
    original_gate: 'PREFERRED_BUSINESS_HOURS_09_00_21_00',
    original_verdict: 'BLOCKED — PAID SERP BUSINESS-HOURS WINDOW NOT SATISFIED',
    approved_degraded_verdict: 'APPROVED WITH DEGRADATION — TECHNICAL CAPABILITY ONLY',
    authority_class: 'TECHNICAL_CAPABILITY_VALIDATION',
    permitted_consumer: 'MIG-W2-3-TECH-PAID-SERP',
    reason: 'fixture degradation',
    permitted_uses: ['parser validation'],
    prohibited_uses: ['client-specific Paid SERP completion'],
    production_authority: false,
    client_authority: false,
    one_time_use: true,
    status: 'approved',
    created_at: '2026-06-24T08:00:00.000Z',
    ...overrides,
  };
  body.checksum = hashDegradationBody(body);
  writeJson(path.join(dir, 'fixture-time-window-degradation-v1.json'), body);
  writeJson(path.join(dir, 'consumption-registry-v1.json'), { schema_version: '1.0.0', consumed: [] });
  return dir;
}

async function main() {
  const results = [];
  async function record(id, name, fn) {
    try {
      const pass = !!(await fn());
      results.push({ id, name, pass });
    } catch (e) {
      results.push({ id, name, pass: false, error: e.message });
    }
  }

  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'sppc-w23-deg-'));
  const querySet = loadJson(W23_QUERIES);
  const session = loadJson(W23_SESSION);
  const projectManifest = loadJson(W23_MANIFEST);
  const outsideBundle = buildOutsideWindowBundle(tmp);
  const degDir = writeFixtureDegradation(path.join(tmp, 'degradations'));
  const consumptionPath = path.join(degDir, 'consumption-registry-v1.json');

  await record(1, 'outside-window bundle blocked without degradation', () => {
    const r = validateAssistedCaptureBundle({
      bundleDir: outsideBundle,
      querySet,
      sessionConfig: session,
      projectManifest,
      approvedDegradationsDir: path.join(tmp, 'empty-deg'),
    });
    return !r.valid && r.capture_time_status === 'OUTSIDE_PREFERRED_WINDOW';
  });

  await record(2, 'exact approved degradation permits technical import', () => {
    const r = validateAssistedCaptureBundle({
      bundleDir: outsideBundle,
      querySet,
      sessionConfig: session,
      projectManifest,
      approvedDegradationsDir: degDir,
      consumptionRegistryPath: consumptionPath,
    });
    return r.valid && r.degradation_applied?.degradation_id === 'fixture-time-window-degradation-v1';
  });

  await record(3, 'wrong project does not match degradation', () => {
    const dir = buildOutsideWindowBundle(tmp, { project_id: 'OTHER-PROJECT' });
    const r = validateAssistedCaptureBundle({
      bundleDir: dir,
      querySet,
      sessionConfig: session,
      projectManifest,
      approvedDegradationsDir: degDir,
      consumptionRegistryPath: consumptionPath,
    });
    return !r.valid;
  });

  await record(4, 'wrong session does not match degradation', () => {
    const dir = buildOutsideWindowBundle(tmp, { session_id: 'wrong-session' });
    const r = validateAssistedCaptureBundle({
      bundleDir: dir,
      querySet,
      sessionConfig: session,
      projectManifest,
      approvedDegradationsDir: degDir,
      consumptionRegistryPath: consumptionPath,
    });
    return !r.valid;
  });

  await record(5, 'wrong query does not match degradation', () => {
    const dir = buildOutsideWindowBundle(tmp, { query_id: 'w2-3-q01', query: 'установка кондиционера цена' });
    const r = validateAssistedCaptureBundle({
      bundleDir: dir,
      querySet,
      sessionConfig: session,
      projectManifest,
      approvedDegradationsDir: degDir,
      consumptionRegistryPath: consumptionPath,
    });
    return !r.valid;
  });

  await record(6, 'wrong timestamp does not match degradation', () => {
    const dir = buildOutsideWindowBundle(tmp, { captured_at: '2026-06-24T02:00:00.000Z' });
    const r = validateAssistedCaptureBundle({
      bundleDir: dir,
      querySet,
      sessionConfig: session,
      projectManifest,
      approvedDegradationsDir: degDir,
      consumptionRegistryPath: consumptionPath,
    });
    return !r.valid;
  });

  await record(7, 'generic bypass flag rejected', () => {
    const dir = buildOutsideWindowBundle(tmp, { ignore_business_hours: true });
    const r = validateAssistedCaptureBundle({
      bundleDir: dir,
      querySet,
      sessionConfig: session,
      projectManifest,
      approvedDegradationsDir: degDir,
      consumptionRegistryPath: consumptionPath,
    });
    return !r.valid && r.blockers.some((b) => b.includes('ignore_business_hours'));
  });

  await record(8, 'degraded evidence cannot become client authority', () => {
    const r = validateAssistedCaptureBundle({
      bundleDir: outsideBundle,
      querySet,
      sessionConfig: session,
      projectManifest,
      approvedDegradationsDir: degDir,
      consumptionRegistryPath: consumptionPath,
    });
    return r.degradation_applied?.client_authority === false && r.degradation_applied?.production_authority === false;
  });

  await record(9, 'degraded evidence cannot complete client SPPC-10', () => {
    const pack = buildEvidenceManifest({ projectId: 'MIG-W2-3-TECH-PAID-SERP' });
    return pack.manifest.sppc_10_complete !== true && pack.manifest.sppc_12_complete !== true;
  });

  await record(10, 'execution receipt includes degradation ID', async () => {
    const oneTimeDir = writeFixtureDegradation(path.join(tmp, 'one-time-deg'));
    const oneTimeConsumption = path.join(oneTimeDir, 'consumption-registry-v1.json');
    const bundle = buildOutsideWindowBundle(tmp);
    const imported = await importAssistedCaptureBundle({
      bundleDir: bundle,
      querySet,
      sessionConfig: session,
      projectManifest,
      approvedDegradationsDir: oneTimeDir,
      consumptionRegistryPath: oneTimeConsumption,
      outputPath: path.join(tmp, 'import-out'),
    });
    return imported.ok && imported.importReceipt?.degradation_id === 'fixture-time-window-degradation-v1';
  });

  await record(11, 'factual outside-window status preserved', () => {
    const r = validateAssistedCaptureBundle({
      bundleDir: outsideBundle,
      querySet,
      sessionConfig: session,
      projectManifest,
      approvedDegradationsDir: degDir,
      consumptionRegistryPath: consumptionPath,
    });
    return (
      r.capture_time_status === 'OUTSIDE_PREFERRED_WINDOW' &&
      r.degradation_status === 'OPERATOR_APPROVED' &&
      r.business_hours?.allowed === false
    );
  });

  await record(12, 'one-time degradation cannot be reused for another capture', async () => {
    const reuseDir = writeFixtureDegradation(path.join(tmp, 'reuse-deg'));
    const reuseConsumption = path.join(reuseDir, 'consumption-registry-v1.json');
    const bundle = buildOutsideWindowBundle(tmp);
    const first = await importAssistedCaptureBundle({
      bundleDir: bundle,
      querySet,
      sessionConfig: session,
      projectManifest,
      approvedDegradationsDir: reuseDir,
      consumptionRegistryPath: reuseConsumption,
      outputPath: path.join(tmp, 'import-reuse-1'),
    });
    const second = validateAssistedCaptureBundle({
      bundleDir: bundle,
      querySet,
      sessionConfig: session,
      projectManifest,
      approvedDegradationsDir: reuseDir,
      consumptionRegistryPath: reuseConsumption,
    });
    return first.ok && !second.valid;
  });

  await record(13, 'genuine counts reconcile when live bundle present', () => {
    if (!fs.existsSync(LIVE_BUNDLE)) return true;
    const packPath = path.join(W23_BASE, 'genuine-technical-evidence-pack-v3.json');
    if (!fs.existsSync(packPath)) return true;
    const pack = loadJson(packPath);
    const m = pack.minimum_closure || {};
    return (
      m.genuine_live_serp_pages === 1 &&
      m.genuine_paid_ad_observations === 10 &&
      m.validated_advertiser_entities === 10 &&
      m.bounded_landing_resolutions === 2
    );
  });

  await record(14, 'raw evidence remains outside Git', () => {
    const tracked = ['page.htm', 'page.html', 'screenshot.png'].every(
      (f) => !fs.existsSync(path.join(W23_BASE, f)),
    );
    return tracked;
  });

  const passed = results.filter((r) => r.pass).length;
  const failed = results.length - passed;
  console.log(`Wave 2.3 degradation tests: ${passed}/${results.length} passed`);
  for (const r of results) {
    console.log(`  [${r.pass ? 'PASS' : 'FAIL'}] #${r.id} ${r.name}${r.error ? ` — ${r.error}` : ''}`);
  }
  writeJson(path.join(__dirname, '../reports/wave23-degradation-test-results-v1.json'), {
    suite: 'wave23-degradation-tests',
    passed,
    failed,
    results,
  });
  process.exit(failed > 0 ? 1 : 0);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
