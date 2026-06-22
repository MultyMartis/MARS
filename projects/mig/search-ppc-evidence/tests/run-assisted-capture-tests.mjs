#!/usr/bin/env node
/**
 * Wave 2.2 — Assisted capture validation tests
 */
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath } from 'node:url';
import { validateAssistedCaptureBundle, ASSISTED_BLOCKER, hashAssistedManifestBody } from '../runtime/lib/assisted-capture-validator.mjs';
import { importAssistedCaptureBundle, requireDegradedRecordForFallback } from '../runtime/lib/assisted-capture-importer.mjs';
import { extractSerpItemsFromHtml } from '../runtime/lib/serp-html-extract.mjs';
import { authorizeEvidenceCommand } from '../runtime/lib/gate.mjs';
import { loadJson, writeJson, sha256File, sha256Text } from '../runtime/lib/utils.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const FIX = path.join(__dirname, '../fixtures');
const REPO = path.resolve(__dirname, '../../../..');
const MANIFEST = path.join(REPO, 'projects/mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/project-ppc-state-manifest-v1.json');
const QUERY_SET = path.join(REPO, 'projects/mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/query-set-v1.json');
const SESSION = path.join(REPO, 'projects/mig/search-ppc-evidence/live-validation/w2-1-tech-paid-serp/session-config-v1.json');

const results = [];
function record(id, name, fn) {
  try {
    const pass = fn();
    results.push({ id, name, pass: !!pass });
  } catch (e) {
    results.push({ id, name, pass: false, error: e.message });
  }
}

function buildValidBundle(tmp) {
  const dir = path.join(tmp, 'valid-bundle');
  fs.mkdirSync(dir, { recursive: true });
  const htmlSrc = path.join(FIX, 'assisted-capture/valid-page.html');
  fs.copyFileSync(htmlSrc, path.join(dir, 'page.html'));
  fs.writeFileSync(path.join(dir, 'screenshot.png'), Buffer.from('fixture-screenshot-bytes'));
  const manifest = loadJson(path.join(FIX, 'assisted-capture/valid-manifest-template.json'));
  manifest.captured_at = '2026-06-23T10:15:00.000Z';
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

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'sppc-w22-'));
const validBundle = buildValidBundle(tmp);
const querySet = loadJson(QUERY_SET);
const session = loadJson(SESSION);
const projectManifest = loadJson(MANIFEST);

record(1, 'assisted capture missing timestamp blocked', () => {
  const dir = path.join(tmp, 'no-ts');
  fs.mkdirSync(dir, { recursive: true });
  const m = { ...loadJson(path.join(validBundle, 'capture-manifest.json')), captured_at: null };
  writeJson(path.join(dir, 'capture-manifest.json'), m);
  fs.copyFileSync(path.join(validBundle, 'screenshot.png'), path.join(dir, 'screenshot.png'));
  fs.copyFileSync(path.join(validBundle, 'page.html'), path.join(dir, 'page.html'));
  const r = validateAssistedCaptureBundle({ bundleDir: dir, querySet, sessionConfig: session, projectManifest });
  return !r.valid && r.blockers.some((b) => /timestamp/i.test(b));
});

record(2, 'assisted capture outside approved window blocked', () => {
  const dir = path.join(tmp, 'outside-window');
  fs.mkdirSync(dir, { recursive: true });
  const m = { ...loadJson(path.join(validBundle, 'capture-manifest.json')), captured_at: '2026-06-22T03:00:00.000Z' };
  writeJson(path.join(dir, 'capture-manifest.json'), m);
  fs.copyFileSync(path.join(validBundle, 'screenshot.png'), path.join(dir, 'screenshot.png'));
  fs.copyFileSync(path.join(validBundle, 'page.html'), path.join(dir, 'page.html'));
  const r = validateAssistedCaptureBundle({ bundleDir: dir, querySet, sessionConfig: session, projectManifest });
  return !r.valid && r.blockers.some((b) => /outside approved window/i.test(b));
});

record(3, 'wrong project/query blocked', () => {
  const dir = path.join(tmp, 'wrong-query');
  fs.mkdirSync(dir, { recursive: true });
  const m = { ...loadJson(path.join(validBundle, 'capture-manifest.json')), query_id: 'not-in-set', query: 'fake query' };
  writeJson(path.join(dir, 'capture-manifest.json'), m);
  fs.copyFileSync(path.join(validBundle, 'screenshot.png'), path.join(dir, 'screenshot.png'));
  fs.copyFileSync(path.join(validBundle, 'page.html'), path.join(dir, 'page.html'));
  const r = validateAssistedCaptureBundle({ bundleDir: dir, querySet, sessionConfig: session, projectManifest });
  return !r.valid;
});

record(4, 'screenshot missing blocked', () => {
  const dir = path.join(tmp, 'no-screenshot');
  fs.mkdirSync(dir, { recursive: true });
  writeJson(path.join(dir, 'capture-manifest.json'), loadJson(path.join(validBundle, 'capture-manifest.json')));
  fs.copyFileSync(path.join(validBundle, 'page.html'), path.join(dir, 'page.html'));
  const r = validateAssistedCaptureBundle({ bundleDir: dir, querySet, sessionConfig: session, projectManifest });
  return !r.valid && r.blockers.some((b) => /screenshot/i.test(b));
});

record(5, 'HTML missing with no limitation blocked', () => {
  const dir = path.join(tmp, 'no-html');
  fs.mkdirSync(dir, { recursive: true });
  writeJson(path.join(dir, 'capture-manifest.json'), loadJson(path.join(validBundle, 'capture-manifest.json')));
  fs.copyFileSync(path.join(validBundle, 'screenshot.png'), path.join(dir, 'screenshot.png'));
  const r = validateAssistedCaptureBundle({ bundleDir: dir, querySet, sessionConfig: session, projectManifest });
  return !r.valid && r.blockers.some((b) => /HTML/i.test(b));
});

record(6, 'altered checksum blocked', () => {
  const dir = path.join(tmp, 'bad-checksum');
  fs.mkdirSync(dir, { recursive: true });
  fs.copyFileSync(path.join(validBundle, 'screenshot.png'), path.join(dir, 'screenshot.png'));
  fs.copyFileSync(path.join(validBundle, 'page.html'), path.join(dir, 'page.html'));
  const m = loadJson(path.join(validBundle, 'capture-manifest.json'));
  m.checksums = { ...m.checksums, screenshot_sha256: '0000000000000000000000000000000000000000000000000000000000000000' };
  writeJson(path.join(dir, 'capture-manifest.json'), m);
  const r = validateAssistedCaptureBundle({ bundleDir: dir, querySet, sessionConfig: session, projectManifest });
  return !r.valid && r.blockers.some((b) => /checksum/i.test(b));
});

record(7, 'manual advertiser rows blocked', () => {
  const dir = path.join(tmp, 'manual-ads');
  fs.mkdirSync(dir, { recursive: true });
  const m = { ...loadJson(path.join(validBundle, 'capture-manifest.json')), manual_advertiser_rows: [{ domain: 'fake.ru' }] };
  writeJson(path.join(dir, 'capture-manifest.json'), m);
  fs.copyFileSync(path.join(validBundle, 'screenshot.png'), path.join(dir, 'screenshot.png'));
  fs.copyFileSync(path.join(validBundle, 'page.html'), path.join(dir, 'page.html'));
  const r = validateAssistedCaptureBundle({ bundleDir: dir, querySet, sessionConfig: session, projectManifest });
  return !r.valid && r.blockers.some((b) => /manual advertiser/i.test(b));
});

record(8, 'technical evidence as production blocked', () => {
  const dir = path.join(tmp, 'prod-auth');
  fs.mkdirSync(dir, { recursive: true });
  const m = { ...loadJson(path.join(validBundle, 'capture-manifest.json')), registered_as_production_authority: true };
  writeJson(path.join(dir, 'capture-manifest.json'), m);
  fs.copyFileSync(path.join(validBundle, 'screenshot.png'), path.join(dir, 'screenshot.png'));
  fs.copyFileSync(path.join(validBundle, 'page.html'), path.join(dir, 'page.html'));
  const r = validateAssistedCaptureBundle({ bundleDir: dir, querySet, sessionConfig: session, projectManifest });
  return !r.valid;
});

record(9, 'valid assisted capture import', () => {
  const auth = authorizeEvidenceCommand({ manifestPath: MANIFEST, cliCommand: 'paid-serp:import-assisted' });
  if (!auth.allowed) return false;
  const out = path.join(tmp, 'import-out');
  const r = importAssistedCaptureBundle({
    bundleDir: validBundle,
    querySet,
    sessionConfig: session,
    projectManifest,
    receipt: auth.evidence_record,
    outputPath: out,
  });
  return r.ok && r.observation.observation_state === 'ADS OBSERVED' && r.observation.production_authority === false;
});

record(10, 'parser extraction from assisted live HTML', () => {
  const html = fs.readFileSync(path.join(FIX, 'assisted-capture/valid-page.html'), 'utf8');
  const ex = extractSerpItemsFromHtml(html);
  const ads = ex.items.filter((i) => i.surface_type === 'ad');
  const organic = ex.items.filter((i) => i.surface_type === 'organic');
  return ads.length >= 2 && organic.length >= 1 && !ex.hasCaptcha;
});

record(11, 'operator attestation missing blocked', () => {
  const dir = path.join(tmp, 'no-attest');
  fs.mkdirSync(dir, { recursive: true });
  const m = { ...loadJson(path.join(validBundle, 'capture-manifest.json')), operator_attestation: { attested: false } };
  writeJson(path.join(dir, 'capture-manifest.json'), m);
  fs.copyFileSync(path.join(validBundle, 'screenshot.png'), path.join(dir, 'screenshot.png'));
  fs.copyFileSync(path.join(validBundle, 'page.html'), path.join(dir, 'page.html'));
  const r = validateAssistedCaptureBundle({ bundleDir: dir, querySet, sessionConfig: session, projectManifest });
  return !r.valid && r.blockers.some((b) => /attestation/i.test(b));
});

record(12, 'fallback without degraded record blocked', () => {
  const r = requireDegradedRecordForFallback({
    automatedAttempted: true,
    automatedOutcome: { completed: [], incomplete: ['q1'] },
    assistedUsed: true,
    outputPath: path.join(tmp, 'no-degraded'),
  });
  return !r.ok && r.blockers[0].includes(ASSISTED_BLOCKER);
});

const passed = results.filter((r) => r.pass).length;
writeJson(path.join(__dirname, '../reports/assisted-capture-test-results-v1.json'), {
  suite: 'assisted-capture-tests',
  passed,
  failed: results.length - passed,
  total: results.length,
  results,
});

for (const r of results) console.log(`  [${r.pass ? 'PASS' : 'FAIL'}] #${r.id} ${r.name}`);
console.log(`Assisted capture tests: ${passed}/${results.length} passed`);
process.exit(passed === results.length ? 0 : 1);
