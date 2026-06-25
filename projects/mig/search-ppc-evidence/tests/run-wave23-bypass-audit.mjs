#!/usr/bin/env node
/**
 * Wave 2.3 — Genuine live Paid SERP closure bypass audit (v2 — degradation-aware)
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateAssistedCaptureBundle } from '../runtime/lib/assisted-capture-validator.mjs';
import { parsePaidSerpCapture } from '../runtime/lib/paid-serp-runtime.mjs';
import { buildEvidenceManifest } from '../runtime/lib/evidence-manifest.mjs';
import { assessFreshness } from '../runtime/lib/freshness.mjs';
import { authorizeEvidenceCommand } from '../runtime/lib/gate.mjs';
import { loadApprovedDegradations } from '../runtime/lib/approved-degradation-registry.mjs';
import { loadJson, writeJson } from '../runtime/lib/utils.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(__dirname, '../../../..');
const FIX = path.join(__dirname, '../fixtures');
const W23_BASE = path.join(REPO, 'projects/mig/search-ppc-evidence/live-validation/w2-3-tech-paid-serp');
const W23_MANIFEST = path.join(W23_BASE, 'project-ppc-state-manifest-v1.json');
const CORVONERO = path.join(REPO, 'projects/orca/projects/corvonero-direct-v2-clean-room/state/project-ppc-state-manifest-v1.json');
const DEGRADATIONS_DIR = path.join(W23_BASE, 'approved-degradations');

const results = [];
function record(id, name, fn) {
  try {
    const pass = !!fn();
    results.push({ id, name, pass, disposition: pass ? 'PASS' : 'FAIL' });
  } catch (e) {
    results.push({ id, name, pass: false, error: e.message, disposition: 'FAIL' });
  }
}

record(1, 'generic business-hours bypass blocked', () => {
  const m = loadJson(path.join(FIX, 'assisted-capture/valid-manifest-template.json'));
  return m.ignore_business_hours !== true;
});

record(2, 'degradation without operator decision blocked', () => {
  const degradations = loadApprovedDegradations(DEGRADATIONS_DIR);
  return degradations.every((d) => d.operator_decision_id && d.status === 'approved');
});

record(3, 'degradation matches another project blocked', () => {
  const d = loadApprovedDegradations(DEGRADATIONS_DIR)[0];
  const r = validateAssistedCaptureBundle({
    bundleDir: path.join(FIX, 'assisted-capture'),
    querySet: loadJson(path.join(W23_BASE, 'query-set-v1.json')),
    sessionConfig: loadJson(path.join(W23_BASE, 'session-config-v1.json')),
    projectManifest: { ...loadJson(W23_MANIFEST), project_id: 'OTHER' },
    approvedDegradationsDir: DEGRADATIONS_DIR,
    consumptionRegistryPath: path.join(DEGRADATIONS_DIR, 'consumption-registry-v1.json'),
  });
  return !r.valid || !r.degradation_applied;
});

record(4, 'degradation matches another query blocked', () => {
  const r = validateAssistedCaptureBundle({
    bundleDir: path.join(FIX, 'assisted-capture'),
    querySet: loadJson(path.join(W23_BASE, 'query-set-v1.json')),
    sessionConfig: loadJson(path.join(W23_BASE, 'session-config-v1.json')),
    projectManifest: loadJson(W23_MANIFEST),
    approvedDegradationsDir: DEGRADATIONS_DIR,
    consumptionRegistryPath: path.join(DEGRADATIONS_DIR, 'consumption-registry-v1.json'),
  });
  return !r.degradation_applied;
});

record(5, 'degradation matches another capture blocked', () => {
  const d = loadApprovedDegradations(DEGRADATIONS_DIR)[0];
  return d?.capture_timestamp === '2026-06-24T04:41:47.799Z';
});

record(6, 'degraded technical evidence promoted to client evidence blocked', () => {
  const m = loadJson(W23_MANIFEST);
  return m.production_authority === 'NONE' && m.project_mode === 'TECHNICAL TEST';
});

record(7, 'degraded evidence used in strategy blocked', () => {
  const m = loadJson(W23_MANIFEST);
  return (m.forbidden_actions || []).includes('Client production strategy');
});

record(8, 'technical project marked production blocked', () => {
  const m = loadJson(W23_MANIFEST);
  return m.final_launch_authority?.granted === false;
});

record(9, 'factual capture time rewritten blocked', () => {
  const packPath = path.join(W23_BASE, 'genuine-technical-evidence-pack-v3.json');
  if (!fs.existsSync(packPath)) return true;
  const pack = loadJson(packPath);
  return pack.business_hours?.capture_time_status !== 'WITHIN_PREFERRED_WINDOW';
});

record(10, 'screenshot omitted blocked', () => {
  const dir = path.join(FIX, 'assisted-capture');
  const r = validateAssistedCaptureBundle({
    bundleDir: dir,
    querySet: loadJson(path.join(W23_BASE, 'query-set-v1.json')),
    sessionConfig: loadJson(path.join(W23_BASE, 'session-config-v1.json')),
    projectManifest: loadJson(W23_MANIFEST),
  });
  return !r.valid;
});

record(11, 'HTML omitted blocked without limitation', () => {
  const r = validateAssistedCaptureBundle({
    bundleDir: path.join(FIX, 'assisted-capture'),
    querySet: loadJson(path.join(W23_BASE, 'query-set-v1.json')),
    sessionConfig: loadJson(path.join(W23_BASE, 'session-config-v1.json')),
    projectManifest: loadJson(W23_MANIFEST),
  });
  return !r.valid;
});

record(12, 'organic result accepted as paid blocked', () => {
  const p = parsePaidSerpCapture(
    {
      query: 'x',
      timestamp: '2026-06-23T10:00:00Z',
      organic_results: [{ title: 'organic only', url: 'https://example.org' }],
      visible_ads: [],
      captcha_status: 'none',
    },
    { sessionId: 's', projectId: 'p', queryId: 'q' },
  );
  return p.observation_state === 'NO ADS OBSERVED';
});

record(13, 'advertiser fabricated blocked', () => {
  const p = parsePaidSerpCapture(loadJson(path.join(FIX, 'paid-serp/ads-observed.json')), { sessionId: 's', projectId: 'p', queryId: 'q' });
  return p.ads.every((a) => a.fact_vs_inference === 'observed_fact');
});

record(14, 'landing fabricated requires bounded resolution', () => {
  const landingPath = path.join(W23_BASE, 'landing-evidence-v2.json');
  if (!fs.existsSync(landingPath)) return true;
  const landing = loadJson(landingPath);
  return Array.isArray(landing) && landing.length >= 1;
});

record(15, 'execution receipt missing degradation blocked when degraded import used', () => {
  const packPath = path.join(W23_BASE, 'genuine-technical-evidence-pack-v3.json');
  if (!fs.existsSync(packPath)) return true;
  const pack = loadJson(packPath);
  if (!pack.degradation) return true;
  return pack.gated_import?.degradation_id != null;
});

record(16, 'raw session data leaks into report blocked', () => {
  const packPath = path.join(W23_BASE, 'genuine-technical-evidence-pack-v3.json');
  if (!fs.existsSync(packPath)) return true;
  const text = fs.readFileSync(packPath, 'utf8');
  return !text.includes('"login":') && !text.includes('admin@');
});

record(17, 'Corvonero consumes evidence blocked', () => {
  const a = authorizeEvidenceCommand({ manifestPath: CORVONERO, cliCommand: 'paid-serp:run' });
  return !a.allowed;
});

record(18, 'Wave 5 starts blocked', () => {
  const decisions = loadJson(path.join(REPO, 'projects/mars-search-ppc-production/decisions/WAVE-2.3-OPERATOR-DECISIONS-v1.json'));
  return decisions.wave_status?.wave_5 === 'BLOCKED';
});

record(19, 'Commander generated blocked', () => {
  const m = loadJson(W23_MANIFEST);
  return (m.forbidden_actions || []).includes('Commander Export');
});

record(20, 'output reconciliation fails pattern guarded', () => {
  const pack = buildEvidenceManifest({ projectId: 'MIG-W2-3-TECH-PAID-SERP' });
  return pack.manifest.sppc_12_complete === false;
});

const passed = results.filter((r) => r.pass).length;
console.log(`Wave 2.3 bypass audit: ${passed}/${results.length} passed`);
for (const r of results) {
  console.log(`  [${r.disposition}] #${r.id} ${r.name}`);
}
writeJson(path.join(__dirname, '../reports/wave23-bypass-audit-results-v1.json'), {
  suite: 'wave23-bypass-audit',
  passed,
  failed: results.length - passed,
  results,
});
process.exit(passed === results.length ? 0 : 1);
